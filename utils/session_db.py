#!/usr/bin/env python3
"""
Session Database - DuckDB-based state management

Simpler, faster, safer than JSON file approach.

IMPORTANT: This is a FILE-BASED database (NOT in-memory).
  - Database file: memory/agor-state/sessions.duckdb
  - Sessions PERSIST across runs (not ephemeral)
  - Survives process restarts, reboots, etc.
  - Perfect for scheduled runs every 4 hours

Schema:
  ticket_sessions(
    card_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL,
    category TEXT,
    created_at TIMESTAMP,
    last_updated TIMESTAMP,
    status TEXT
  )

Benefits:
- Fast lookups (indexed by card_id)
- Persistent storage (file-based, not in-memory)
- ACID transactions (no race conditions, no corruption)
- SQL queries (easy duplicate detection)
- Audit trail (session_history table tracks all changes)
- Type safety (schema enforced)
"""

import duckdb
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

# Database path
WORKSPACE_ROOT = Path(__file__).parent.parent
DB_PATH = WORKSPACE_ROOT / "memory/agor-state/sessions.duckdb"

# Ensure directory exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class SessionDB:
    """DuckDB-based session state management"""

    def __init__(self, db_path: Path = DB_PATH):
        """Initialize database connection"""
        self.db_path = db_path
        self.conn = duckdb.connect(str(db_path))
        self._create_tables()

    def _create_tables(self):
        """Create tables if they don't exist"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS ticket_sessions (
                card_id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                category TEXT,
                title TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        """)

        # Create index for fast lookups
        self.conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_status
            ON ticket_sessions(status)
        """)

        # Audit trail table (optional but useful)
        # Note: DuckDB auto-generates INTEGER PRIMARY KEY values
        self.conn.execute("""
            CREATE SEQUENCE IF NOT EXISTS session_history_seq START 1
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS session_history (
                id INTEGER PRIMARY KEY DEFAULT nextval('session_history_seq'),
                card_id TEXT NOT NULL,
                session_id TEXT NOT NULL,
                action TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                metadata TEXT
            )
        """)

    def has_session(self, card_id: str) -> bool:
        """
        Check if card already has an active session

        Returns:
            True if session exists, False otherwise
        """
        result = self.conn.execute("""
            SELECT COUNT(*)
            FROM ticket_sessions
            WHERE card_id = ? AND status = 'active'
        """, [card_id]).fetchone()

        return result[0] > 0

    def get_session(self, card_id: str) -> Optional[Dict]:
        """
        Get session info for a card

        Returns:
            Dict with session info or None if not found
        """
        result = self.conn.execute("""
            SELECT card_id, session_id, category, title,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE card_id = ? AND status = 'active'
        """, [card_id]).fetchone()

        if not result:
            return None

        return {
            'card_id': result[0],
            'session_id': result[1],
            'category': result[2],
            'title': result[3],
            'created_at': result[4],
            'last_updated': result[5],
            'status': result[6]
        }

    def create_session(
        self,
        card_id: str,
        session_id: str,
        category: str,
        title: str = ""
    ):
        """
        Record a new session for a card

        Args:
            card_id: Trello card ID
            session_id: Agor session ID
            category: 'coding', 'research', or 'personal'
            title: Card title
        """
        now = datetime.now(timezone.utc)

        # Insert or replace (upsert)
        self.conn.execute("""
            INSERT INTO ticket_sessions
                (card_id, session_id, category, title, created_at, last_updated, status)
            VALUES (?, ?, ?, ?, ?, ?, 'active')
            ON CONFLICT (card_id)
            DO UPDATE SET
                session_id = EXCLUDED.session_id,
                category = EXCLUDED.category,
                title = EXCLUDED.title,
                last_updated = EXCLUDED.last_updated
        """, [card_id, session_id, category, title, now, now])

        # Record in history
        self.conn.execute("""
            INSERT INTO session_history (id, card_id, session_id, action)
            VALUES (nextval('session_history_seq'), ?, ?, 'create')
        """, [card_id, session_id])

        self.conn.commit()

    def update_session(
        self,
        card_id: str,
        session_id: Optional[str] = None,
        status: Optional[str] = None
    ):
        """
        Update session info

        Args:
            card_id: Trello card ID
            session_id: New session ID (if changed)
            status: New status ('active', 'completed', 'archived')
        """
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

        self.conn.execute(f"""
            UPDATE ticket_sessions
            SET {', '.join(updates)}
            WHERE card_id = ?
        """, params)

        # Record in history
        self.conn.execute("""
            INSERT INTO session_history (id, card_id, session_id, action)
            VALUES (nextval('session_history_seq'), ?, ?, 'update')
        """, [card_id, session_id or ''])

        self.conn.commit()

    def archive_session(self, card_id: str):
        """Mark session as archived"""
        self.update_session(card_id, status='archived')

    def get_all_active_sessions(self) -> List[Dict]:
        """
        Get all active sessions

        Returns:
            List of session dicts
        """
        results = self.conn.execute("""
            SELECT card_id, session_id, category, title,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE status = 'active'
            ORDER BY created_at DESC
        """).fetchall()

        return [
            {
                'card_id': row[0],
                'session_id': row[1],
                'category': row[2],
                'title': row[3],
                'created_at': row[4],
                'last_updated': row[5],
                'status': row[6]
            }
            for row in results
        ]

    def get_sessions_by_category(self, category: str) -> List[Dict]:
        """Get active sessions for a specific category"""
        results = self.conn.execute("""
            SELECT card_id, session_id, category, title,
                   created_at, last_updated, status
            FROM ticket_sessions
            WHERE status = 'active' AND category = ?
            ORDER BY created_at DESC
        """, [category]).fetchall()

        return [
            {
                'card_id': row[0],
                'session_id': row[1],
                'category': row[2],
                'title': row[3],
                'created_at': row[4],
                'last_updated': row[5],
                'status': row[6]
            }
            for row in results
        ]

    def find_duplicates(self) -> List[Dict]:
        """
        Find cards with multiple active sessions

        Returns:
            List of duplicates with card_id and session count
        """
        # Note: This is a safety check - schema prevents duplicates via PRIMARY KEY
        # But useful for auditing if sessions exist outside DB
        results = self.conn.execute("""
            SELECT card_id, COUNT(*) as session_count
            FROM ticket_sessions
            WHERE status = 'active'
            GROUP BY card_id
            HAVING COUNT(*) > 1
        """).fetchall()

        return [
            {'card_id': row[0], 'session_count': row[1]}
            for row in results
        ]

    def get_stats(self) -> Dict:
        """Get database statistics"""
        total = self.conn.execute(
            "SELECT COUNT(*) FROM ticket_sessions WHERE status = 'active'"
        ).fetchone()[0]

        by_category = self.conn.execute("""
            SELECT category, COUNT(*)
            FROM ticket_sessions
            WHERE status = 'active'
            GROUP BY category
        """).fetchall()

        return {
            'total_active': total,
            'by_category': {row[0]: row[1] for row in by_category}
        }

    def export_to_json_format(self) -> Dict:
        """
        Export to old JSON format for compatibility

        Returns:
            Dict in old format with active_*_sessions arrays
        """
        sessions_by_cat = {
            'active_coding_sessions': [],
            'active_research_sessions': [],
            'active_personal_sessions': []
        }

        all_sessions = self.get_all_active_sessions()

        for session in all_sessions:
            cat_key = f"active_{session['category']}_sessions"
            if cat_key in sessions_by_cat:
                sessions_by_cat[cat_key].append({
                    'session_id': session['session_id'],
                    'ticket_id': session['card_id'],
                    'ticket_title': session['title'],
                    'category': session['category']
                })

        return sessions_by_cat

    def close(self):
        """Close database connection"""
        self.conn.close()


# Convenience functions for quick access

def check_if_exists(card_id: str) -> bool:
    """Quick check if card has session"""
    db = SessionDB()
    exists = db.has_session(card_id)
    db.close()
    return exists


def get_active_card_ids() -> List[str]:
    """Get list of all active card IDs"""
    db = SessionDB()
    sessions = db.get_all_active_sessions()
    db.close()
    return [s['card_id'] for s in sessions]


def get_session_mapping() -> Dict[str, str]:
    """Get card_id -> session_id mapping"""
    db = SessionDB()
    sessions = db.get_all_active_sessions()
    db.close()
    return {s['card_id']: s['session_id'] for s in sessions}


# Example usage
if __name__ == "__main__":
    db = SessionDB()

    # Example: Check if card exists before creating session
    card_id = "672215e999cf9c79e0bb303a"

    if db.has_session(card_id):
        session = db.get_session(card_id)
        print(f"Session already exists: {session['session_id']}")
        print("Action: UPDATE (send prompt to existing session)")
    else:
        print("No session found")
        print("Action: CREATE (make new session)")

    # Stats
    print("\nDatabase stats:")
    print(db.get_stats())

    # Check for duplicates
    duplicates = db.find_duplicates()
    if duplicates:
        print(f"\n⚠️  Found {len(duplicates)} duplicates!")
    else:
        print("\n✅ No duplicates found")

    db.close()
