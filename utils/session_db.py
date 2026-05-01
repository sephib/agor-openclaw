#!/usr/bin/env python3
"""
Session Database - DuckDB-based state management

Schema:
  trello_list(
    list_id TEXT PRIMARY KEY,
    list_name TEXT,
    list_type TEXT,         -- 'project', 'shopping', 'task'
    worktree_id TEXT,       -- Agor worktree ID
    worktree_name TEXT,     -- slug for path construction
    ticket_count INTEGER,
    list_context_updated TIMESTAMP,
    updated_at TIMESTAMP
  )

  ticket_sessions(
    card_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL,
    category TEXT,
    title TEXT,
    list_id TEXT,           -- FK to trello_list
    created_at TIMESTAMP,
    last_updated TIMESTAMP,
    status TEXT
  )

DB file: memory/agor-state/sessions.duckdb
"""

import duckdb
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

WORKSPACE_ROOT = Path(__file__).parent.parent
DB_PATH = WORKSPACE_ROOT / "memory/agor-state/sessions.duckdb"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class SessionDB:
    """DuckDB-based session state management"""

    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.conn = duckdb.connect(str(db_path))
        self._create_tables()

    def _create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS trello_list (
                list_id              TEXT PRIMARY KEY,
                list_name            TEXT NOT NULL,
                list_type            TEXT DEFAULT 'task',
                worktree_id          TEXT,
                worktree_name        TEXT,
                ticket_count         INTEGER DEFAULT 0,
                list_context_updated TIMESTAMP,
                updated_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS ticket_sessions (
                card_id      TEXT PRIMARY KEY,
                session_id   TEXT NOT NULL,
                category     TEXT,
                title        TEXT,
                list_id      TEXT,
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status       TEXT DEFAULT 'active'
            )
        """)

        self._migrate()

        self.conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_status ON ticket_sessions(status)
        """)
        self.conn.execute("""
            CREATE SEQUENCE IF NOT EXISTS session_history_seq START 1
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS session_history (
                id         INTEGER PRIMARY KEY DEFAULT nextval('session_history_seq'),
                card_id    TEXT NOT NULL,
                session_id TEXT NOT NULL,
                action     TEXT NOT NULL,
                timestamp  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                metadata   TEXT
            )
        """)

    def _migrate(self):
        """Add columns missing from older schema versions"""
        cols = {
            row[0] for row in
            self.conn.execute(
                "SELECT column_name FROM information_schema.columns WHERE table_name = 'ticket_sessions'"
            ).fetchall()
        }
        if 'list_id' not in cols:
            self.conn.execute("ALTER TABLE ticket_sessions ADD COLUMN list_id TEXT")
        self.conn.commit()

    # ── List CRUD ──────────────────────────────────────────────────────────────

    def upsert_list(
        self,
        list_id: str,
        list_name: str,
        list_type: str = 'task',
        worktree_id: Optional[str] = None,
        worktree_name: Optional[str] = None,
        ticket_count: int = 0,
    ):
        """Insert or update a Trello list record"""
        now = datetime.now(timezone.utc)
        self.conn.execute("""
            INSERT INTO trello_list
                (list_id, list_name, list_type, worktree_id, worktree_name,
                 ticket_count, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (list_id) DO UPDATE SET
                list_name     = EXCLUDED.list_name,
                list_type     = EXCLUDED.list_type,
                worktree_id   = COALESCE(EXCLUDED.worktree_id, trello_list.worktree_id),
                worktree_name = COALESCE(EXCLUDED.worktree_name, trello_list.worktree_name),
                ticket_count  = EXCLUDED.ticket_count,
                updated_at    = EXCLUDED.updated_at
        """, [list_id, list_name, list_type, worktree_id, worktree_name, ticket_count, now])
        self.conn.commit()

    def mark_list_context_updated(self, list_id: str):
        """Record that the list context file was just synthesized"""
        self.conn.execute(
            "UPDATE trello_list SET list_context_updated = ? WHERE list_id = ?",
            [datetime.now(timezone.utc), list_id]
        )
        self.conn.commit()

    def get_list(self, list_id: str) -> Optional[Dict]:
        row = self.conn.execute("""
            SELECT list_id, list_name, list_type, worktree_id, worktree_name,
                   ticket_count, list_context_updated, updated_at
            FROM trello_list WHERE list_id = ?
        """, [list_id]).fetchone()
        if not row:
            return None
        return {
            'list_id': row[0], 'list_name': row[1], 'list_type': row[2],
            'worktree_id': row[3], 'worktree_name': row[4],
            'ticket_count': row[5], 'list_context_updated': row[6],
            'updated_at': row[7],
        }

    def get_all_lists(self) -> List[Dict]:
        rows = self.conn.execute("""
            SELECT list_id, list_name, list_type, worktree_id, worktree_name,
                   ticket_count, list_context_updated, updated_at
            FROM trello_list ORDER BY list_name
        """).fetchall()
        return [
            {
                'list_id': r[0], 'list_name': r[1], 'list_type': r[2],
                'worktree_id': r[3], 'worktree_name': r[4],
                'ticket_count': r[5], 'list_context_updated': r[6],
                'updated_at': r[7],
            }
            for r in rows
        ]

    def get_sessions_for_list(self, list_id: str) -> List[Dict]:
        """All active sessions belonging to a given list"""
        rows = self.conn.execute("""
            SELECT card_id, session_id, category, title,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE list_id = ? AND status = 'active'
            ORDER BY created_at DESC
        """, [list_id]).fetchall()
        return [
            {
                'card_id': r[0], 'session_id': r[1], 'category': r[2],
                'title': r[3], 'created_at': r[4],
                'last_updated': r[5], 'status': r[6],
            }
            for r in rows
        ]

    # ── Session CRUD ───────────────────────────────────────────────────────────

    def has_session(self, card_id: str) -> bool:
        result = self.conn.execute("""
            SELECT COUNT(*) FROM ticket_sessions
            WHERE card_id = ? AND status = 'active'
        """, [card_id]).fetchone()
        return result[0] > 0

    def get_session(self, card_id: str) -> Optional[Dict]:
        result = self.conn.execute("""
            SELECT card_id, session_id, category, title, list_id,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE card_id = ? AND status = 'active'
        """, [card_id]).fetchone()
        if not result:
            return None
        return {
            'card_id': result[0], 'session_id': result[1],
            'category': result[2], 'title': result[3], 'list_id': result[4],
            'created_at': result[5], 'last_updated': result[6], 'status': result[7],
        }

    def create_session(
        self,
        card_id: str,
        session_id: str,
        category: str,
        title: str = "",
        list_id: Optional[str] = None,
    ):
        now = datetime.now(timezone.utc)
        self.conn.execute("""
            INSERT INTO ticket_sessions
                (card_id, session_id, category, title, list_id,
                 created_at, last_updated, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'active')
            ON CONFLICT (card_id) DO UPDATE SET
                session_id   = EXCLUDED.session_id,
                category     = EXCLUDED.category,
                title        = EXCLUDED.title,
                list_id      = COALESCE(EXCLUDED.list_id, ticket_sessions.list_id),
                last_updated = EXCLUDED.last_updated
        """, [card_id, session_id, category, title, list_id, now, now])

        self.conn.execute("""
            INSERT INTO session_history (id, card_id, session_id, action)
            VALUES (nextval('session_history_seq'), ?, ?, 'create')
        """, [card_id, session_id])
        self.conn.commit()

    def update_session(
        self,
        card_id: str,
        session_id: Optional[str] = None,
        status: Optional[str] = None,
    ):
        updates = []
        params = []

        if session_id:
            updates.append("session_id = ?")
            params.append(session_id)
        if status:
            updates.append("status = ?")
            params.append(status)

        updates.append("last_updated = ?")
        params.append(datetime.now(timezone.utc))
        params.append(card_id)

        self.conn.execute(
            f"UPDATE ticket_sessions SET {', '.join(updates)} WHERE card_id = ?",
            params
        )
        self.conn.execute("""
            INSERT INTO session_history (id, card_id, session_id, action)
            VALUES (nextval('session_history_seq'), ?, ?, 'update')
        """, [card_id, session_id or ''])
        self.conn.commit()

    def archive_session(self, card_id: str):
        """Mark session archived and decrement parent list ticket_count"""
        session = self.get_session(card_id)
        self.update_session(card_id, status='archived')
        if session and session.get('list_id'):
            self.conn.execute("""
                UPDATE trello_list
                SET ticket_count = GREATEST(0, ticket_count - 1),
                    updated_at   = ?
                WHERE list_id = ?
            """, [datetime.now(timezone.utc), session['list_id']])
            self.conn.commit()

    def delete_session(self, card_id: str):
        """Hard-delete (card permanently removed from Trello)"""
        session = self.get_session(card_id)
        if session:
            self.conn.execute("""
                INSERT INTO session_history (id, card_id, session_id, action)
                VALUES (nextval('session_history_seq'), ?, ?, 'deleted')
            """, [card_id, session['session_id']])
            if session.get('list_id'):
                self.conn.execute("""
                    UPDATE trello_list
                    SET ticket_count = GREATEST(0, ticket_count - 1),
                        updated_at   = ?
                    WHERE list_id = ?
                """, [datetime.now(timezone.utc), session['list_id']])
        self.conn.execute("DELETE FROM ticket_sessions WHERE card_id = ?", [card_id])
        self.conn.commit()

    # ── Queries ────────────────────────────────────────────────────────────────

    def get_all_active_sessions(self) -> List[Dict]:
        rows = self.conn.execute("""
            SELECT card_id, session_id, category, title, list_id,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE status = 'active'
            ORDER BY created_at DESC
        """).fetchall()
        return [
            {
                'card_id': r[0], 'session_id': r[1], 'category': r[2],
                'title': r[3], 'list_id': r[4],
                'created_at': r[5], 'last_updated': r[6], 'status': r[7],
            }
            for r in rows
        ]

    def get_sessions_by_category(self, category: str) -> List[Dict]:
        rows = self.conn.execute("""
            SELECT card_id, session_id, category, title, list_id,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE status = 'active' AND category = ?
            ORDER BY created_at DESC
        """, [category]).fetchall()
        return [
            {
                'card_id': r[0], 'session_id': r[1], 'category': r[2],
                'title': r[3], 'list_id': r[4],
                'created_at': r[5], 'last_updated': r[6], 'status': r[7],
            }
            for r in rows
        ]

    def find_duplicates(self) -> List[Dict]:
        rows = self.conn.execute("""
            SELECT card_id, COUNT(*) as session_count
            FROM ticket_sessions
            WHERE status = 'active'
            GROUP BY card_id
            HAVING COUNT(*) > 1
        """).fetchall()
        return [{'card_id': r[0], 'session_count': r[1]} for r in rows]

    def get_stats(self) -> Dict:
        total = self.conn.execute(
            "SELECT COUNT(*) FROM ticket_sessions WHERE status = 'active'"
        ).fetchone()[0]
        by_category = self.conn.execute("""
            SELECT category, COUNT(*)
            FROM ticket_sessions WHERE status = 'active'
            GROUP BY category
        """).fetchall()
        list_count = self.conn.execute(
            "SELECT COUNT(*) FROM trello_list"
        ).fetchone()[0]
        return {
            'total_active': total,
            'by_category': {r[0]: r[1] for r in by_category},
            'list_count': list_count,
        }

    def export_to_json_format(self) -> Dict:
        sessions_by_cat: Dict[str, List] = {
            'active_coding_sessions': [],
            'active_research_sessions': [],
            'active_personal_sessions': [],
        }
        for s in self.get_all_active_sessions():
            key = f"active_{s['category']}_sessions"
            if key in sessions_by_cat:
                sessions_by_cat[key].append({
                    'session_id': s['session_id'],
                    'ticket_id': s['card_id'],
                    'ticket_title': s['title'],
                    'category': s['category'],
                })
        return sessions_by_cat

    def close(self):
        self.conn.close()


# ── Convenience functions ──────────────────────────────────────────────────────

def check_if_exists(card_id: str) -> bool:
    db = SessionDB()
    exists = db.has_session(card_id)
    db.close()
    return exists


def get_active_card_ids() -> List[str]:
    db = SessionDB()
    sessions = db.get_all_active_sessions()
    db.close()
    return [s['card_id'] for s in sessions]


def get_session_mapping() -> Dict[str, str]:
    db = SessionDB()
    sessions = db.get_all_active_sessions()
    db.close()
    return {s['card_id']: s['session_id'] for s in sessions}


if __name__ == "__main__":
    db = SessionDB()
    print("Database stats:")
    print(db.get_stats())
    print("\nLists:")
    for lst in db.get_all_lists():
        print(f"  [{lst['list_type']:8}] {lst['list_name']} ({lst['ticket_count']} tickets)")
    duplicates = db.find_duplicates()
    if duplicates:
        print(f"\nWARNING: {len(duplicates)} duplicate card(s) found")
    else:
        print("\nNo duplicates found")
    db.close()
