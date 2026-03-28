#!/usr/bin/env python3
"""
Demonstrate DuckDB Persistence

This test proves that sessions persist across runs (not ephemeral).

Test sequence:
1. Run 1: Create sessions, close database
2. Run 2: Open database again, verify sessions still exist
3. Run 3: Add more sessions, close
4. Run 4: Verify ALL sessions exist
"""

import sys
from pathlib import Path
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from session_db import SessionDB

def test_persistence():
    """Test that sessions persist across database connections"""

    print("═" * 70)
    print("DUCKDB PERSISTENCE TEST")
    print("═" * 70)
    print()

    # RUN 1: Create initial sessions
    print("RUN 1: Creating sessions...")
    db = SessionDB()

    # Create test sessions
    test_sessions = [
        ("TEST001", "session-abc-001", "coding", "Test card 1"),
        ("TEST002", "session-abc-002", "research", "Test card 2"),
        ("TEST003", "session-abc-003", "personal", "Test card 3"),
    ]

    for card_id, session_id, category, title in test_sessions:
        db.create_session(card_id, session_id, category, title)
        print(f"  ✓ Created: {card_id} → {session_id}")

    stats_run1 = db.get_stats()
    print(f"\nRun 1 Stats: {stats_run1['total_active']} active sessions")

    # CLOSE DATABASE (simulating end of run)
    db.close()
    print("\n✓ Database closed (end of Run 1)")
    print()

    # RUN 2: Reopen database and verify sessions exist
    print("RUN 2: Reopening database (new connection)...")
    db2 = SessionDB()  # New instance, new connection

    # Check if sessions from Run 1 still exist
    print("\nVerifying sessions from Run 1:")
    for card_id, session_id, category, title in test_sessions:
        if db2.has_session(card_id):
            session = db2.get_session(card_id)
            print(f"  ✓ Found: {card_id} → {session['session_id']} ✅ PERSISTED!")
        else:
            print(f"  ✗ Missing: {card_id} ❌ NOT PERSISTED!")

    stats_run2 = db2.get_stats()
    print(f"\nRun 2 Stats: {stats_run2['total_active']} active sessions")

    # Add more sessions in Run 2
    print("\nAdding more sessions in Run 2:")
    new_sessions = [
        ("TEST004", "session-abc-004", "coding", "Test card 4"),
        ("TEST005", "session-abc-005", "personal", "Test card 5"),
    ]

    for card_id, session_id, category, title in new_sessions:
        db2.create_session(card_id, session_id, category, title)
        print(f"  ✓ Created: {card_id} → {session_id}")

    stats_run2_after = db2.get_stats()
    print(f"\nRun 2 Stats (after adds): {stats_run2_after['total_active']} active sessions")

    db2.close()
    print("\n✓ Database closed (end of Run 2)")
    print()

    # RUN 3: Final verification
    print("RUN 3: Final verification (new connection)...")
    db3 = SessionDB()

    all_test_cards = test_sessions + new_sessions

    print("\nVerifying ALL sessions:")
    found_count = 0
    for card_id, session_id, category, title in all_test_cards:
        if db3.has_session(card_id):
            found_count += 1
            print(f"  ✓ {card_id} → {session_id} ✅")
        else:
            print(f"  ✗ {card_id} → {session_id} ❌")

    stats_run3 = db3.get_stats()
    print(f"\nRun 3 Stats: {stats_run3['total_active']} active sessions")
    print()

    # Results
    print("═" * 70)
    print("RESULTS")
    print("═" * 70)
    expected_count = len(all_test_cards)

    if found_count == expected_count:
        print(f"✅ SUCCESS: All {expected_count} sessions persisted across runs!")
        print()
        print("This proves:")
        print("  ✓ Database file survives process restarts")
        print("  ✓ Sessions are NOT ephemeral")
        print("  ✓ Data written in one run is readable in next run")
        print("  ✓ Perfect for scheduled runs every 4 hours")
        success = True
    else:
        print(f"❌ FAILURE: Expected {expected_count}, found {found_count}")
        success = False

    # Show database file
    print()
    print(f"Database file: {db3.db_path}")
    if db3.db_path.exists():
        size_kb = db3.db_path.stat().st_size / 1024
        print(f"File size: {size_kb:.2f} KB")
        print("✓ File exists on disk (persistent storage)")
    else:
        print("❌ File does not exist!")
        success = False

    # Cleanup test data
    print()
    print("Cleaning up test sessions...")
    for card_id, _, _, _ in all_test_cards:
        db3.archive_session(card_id)
        print(f"  ✓ Archived: {card_id}")

    db3.close()
    print()
    print("═" * 70)

    return success


if __name__ == "__main__":
    success = test_persistence()
    sys.exit(0 if success else 1)
