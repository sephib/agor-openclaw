#!/usr/bin/env python3
"""
Migrate JSON state to DuckDB

One-time migration from:
  memory/agor-state/trello-processor.json
To:
  memory/agor-state/sessions.duckdb

Usage:
  python3 utils/migrate_json_to_duckdb.py [--dry-run] [--backup]
"""

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from session_db import SessionDB

WORKSPACE_ROOT = Path(__file__).parent.parent
JSON_STATE_FILE = WORKSPACE_ROOT / "memory/agor-state/trello-processor.json"
DB_PATH = WORKSPACE_ROOT / "memory/agor-state/sessions.duckdb"


def load_json_state() -> Dict:
    """Load existing JSON state"""
    if not JSON_STATE_FILE.exists():
        print(f"❌ JSON state file not found: {JSON_STATE_FILE}")
        return {
            "active_coding_sessions": [],
            "active_research_sessions": [],
            "active_personal_sessions": []
        }

    with open(JSON_STATE_FILE) as f:
        return json.load(f)


def migrate_to_duckdb(state: Dict, dry_run: bool = False) -> Dict:
    """
    Migrate JSON state to DuckDB

    Args:
        state: JSON state dict
        dry_run: If True, don't actually write to database

    Returns:
        Migration report
    """
    report = {
        'total_sessions': 0,
        'migrated': 0,
        'skipped': 0,
        'errors': [],
        'sessions_by_category': {}
    }

    if not dry_run:
        db = SessionDB()

    # Process each category
    for category_key in ['active_coding_sessions', 'active_research_sessions', 'active_personal_sessions']:
        sessions = state.get(category_key, [])
        category = category_key.replace('active_', '').replace('_sessions', '')

        report['sessions_by_category'][category] = len(sessions)
        report['total_sessions'] += len(sessions)

        for session in sessions:
            try:
                card_id = session.get('ticket_id')
                session_id = session.get('session_id')
                title = session.get('ticket_title', '')

                if not card_id or not session_id:
                    report['errors'].append(f"Missing card_id or session_id in {category}: {session}")
                    report['skipped'] += 1
                    continue

                if dry_run:
                    print(f"[DRY-RUN] Would migrate: {card_id} → {session_id} ({category})")
                else:
                    # Check if already exists
                    if db.has_session(card_id):
                        existing = db.get_session(card_id)
                        print(f"⚠️  Card {card_id} already in DB (session: {existing['session_id']})")
                        print(f"   Keeping existing, skipping JSON entry")
                        report['skipped'] += 1
                    else:
                        db.create_session(
                            card_id=card_id,
                            session_id=session_id,
                            category=category,
                            title=title
                        )
                        print(f"✅ Migrated: {card_id} → {session_id} ({category})")
                        report['migrated'] += 1

            except Exception as e:
                report['errors'].append(f"Error migrating session {session}: {e}")
                report['skipped'] += 1

    if not dry_run:
        db.close()

    return report


def backup_json_state():
    """Create backup of JSON state file"""
    if not JSON_STATE_FILE.exists():
        print("⚠️  No JSON state file to backup")
        return None

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_file = JSON_STATE_FILE.parent / f"trello-processor-backup-{timestamp}.json"

    shutil.copy2(JSON_STATE_FILE, backup_file)
    print(f"✅ Backup created: {backup_file}")

    return backup_file


def verify_migration():
    """Verify migration was successful"""
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)

    # Load JSON state
    json_state = load_json_state()
    json_count = (
        len(json_state.get('active_coding_sessions', [])) +
        len(json_state.get('active_research_sessions', [])) +
        len(json_state.get('active_personal_sessions', []))
    )

    # Check DuckDB
    db = SessionDB()
    db_stats = db.get_stats()
    db_count = db_stats['total_active']

    print(f"JSON sessions: {json_count}")
    print(f"DuckDB sessions: {db_count}")

    if json_count == db_count:
        print("✅ Counts match!")
    else:
        print(f"⚠️  Mismatch: {json_count} in JSON vs {db_count} in DuckDB")

    print(f"\nBy category:")
    print(f"  Coding: {db_stats['by_category'].get('coding', 0)}")
    print(f"  Research: {db_stats['by_category'].get('research', 0)}")
    print(f"  Personal: {db_stats['by_category'].get('personal', 0)}")

    # Check for duplicates
    duplicates = db.find_duplicates()
    if duplicates:
        print(f"\n⚠️  Found {len(duplicates)} duplicates in database!")
        for dup in duplicates:
            print(f"   Card {dup['card_id']}: {dup['session_count']} sessions")
    else:
        print("\n✅ No duplicates found")

    db.close()

    return json_count == db_count


def main():
    """Main migration script"""
    import argparse

    parser = argparse.ArgumentParser(description="Migrate JSON state to DuckDB")
    parser.add_argument('--dry-run', action='store_true', help='Show what would be migrated without actually doing it')
    parser.add_argument('--backup', action='store_true', help='Create backup of JSON state before migration')
    parser.add_argument('--skip-verification', action='store_true', help='Skip verification step')

    args = parser.parse_args()

    print("="*60)
    print("JSON → DuckDB MIGRATION")
    print("="*60)
    print()

    # Check if JSON exists
    if not JSON_STATE_FILE.exists():
        print(f"⚠️  No JSON state file found at: {JSON_STATE_FILE}")
        print("   Nothing to migrate. DuckDB will start fresh.")
        sys.exit(0)

    # Backup if requested
    if args.backup and not args.dry_run:
        backup_json_state()
        print()

    # Load JSON state
    print("Loading JSON state...")
    state = load_json_state()

    total_sessions = (
        len(state.get('active_coding_sessions', [])) +
        len(state.get('active_research_sessions', [])) +
        len(state.get('active_personal_sessions', []))
    )

    print(f"Found {total_sessions} sessions in JSON")
    print()

    if args.dry_run:
        print("🔍 DRY-RUN MODE - No changes will be made")
        print()

    # Migrate
    print("Migrating to DuckDB...")
    report = migrate_to_duckdb(state, dry_run=args.dry_run)

    # Print report
    print()
    print("="*60)
    print("MIGRATION REPORT")
    print("="*60)
    print(f"Total sessions: {report['total_sessions']}")
    print(f"Migrated: {report['migrated']}")
    print(f"Skipped: {report['skipped']}")
    print(f"Errors: {len(report['errors'])}")
    print()
    print("By category:")
    for cat, count in report['sessions_by_category'].items():
        print(f"  {cat.capitalize()}: {count}")

    if report['errors']:
        print()
        print("⚠️  Errors encountered:")
        for error in report['errors']:
            print(f"   - {error}")

    # Verify
    if not args.dry_run and not args.skip_verification:
        verify_migration()

    print()
    if args.dry_run:
        print("🔍 Dry-run complete. Run without --dry-run to actually migrate.")
    elif report['migrated'] > 0:
        print("✅ Migration complete!")
        print()
        print("Next steps:")
        print("1. Verify database: python3 -c 'from utils.session_db import SessionDB; db = SessionDB(); print(db.get_stats())'")
        print("2. Update scripts to use DuckDB")
        print("3. Test with: python3 utils/generate_actions_v2.py <plan-file>")
        print("4. After confirming it works, delete JSON file")
    else:
        print("⚠️  No sessions were migrated. Check errors above.")

    sys.exit(0 if not report['errors'] else 1)


if __name__ == "__main__":
    main()
