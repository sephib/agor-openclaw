#!/usr/bin/env python3
"""
Create Sessions From Filtered List

Reads filtered output (only NEW sessions) and creates them.
Tracks each session in DuckDB to prevent future duplicates.

This script is SAFE because:
1. Input is pre-filtered (only tickets without existing sessions)
2. Each session is tracked in DuckDB immediately after creation
3. No decision-making - just loop and execute
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).parent.parent

# Add utils to path for imports
sys.path.insert(0, str(WORKSPACE_ROOT / "utils"))

from session_db import SessionDB


def main():
    """Create sessions from filtered list"""

    if len(sys.argv) < 2:
        print("Usage: python3 create_sessions_from_filtered.py <filtered_file.json>")
        print("\nThis script creates sessions for NEW tickets only.")
        print("Input must be pre-filtered by scheduled_run.py")
        return 1

    filtered_file = Path(sys.argv[1])

    if not filtered_file.exists():
        print(f"Error: File not found: {filtered_file}")
        return 1

    # Load filtered data
    with open(filtered_file) as f:
        data = json.load(f)

    new_sessions = data.get('new_sessions', [])

    if not new_sessions:
        print("No new sessions to create - input list is empty")
        return 0

    print(f"\n{'='*70}")
    print(f"CREATING {len(new_sessions)} NEW SESSIONS")
    print(f"{'='*70}\n")

    # Connect to DuckDB
    db = SessionDB()

    created_count = 0
    failed_count = 0

    for i, session_info in enumerate(new_sessions, 1):
        card_id = session_info.get('card_id')
        title = session_info.get('title')
        category = session_info.get('category')
        url = session_info.get('url')

        print(f"[{i}/{len(new_sessions)}] {title}")
        print(f"   Card ID: {card_id}")
        print(f"   Category: {category}")

        # Double-check this ticket doesn't already have a session
        if db.has_session(card_id):
            print(f"   ⚠️  SKIP: Session already exists in DuckDB!")
            failed_count += 1
            continue

        # Create session using Agor MCP
        # NOTE: This requires running within an Agor session with MCP access
        print(f"   📝 Creating session in trello-visibility-hub...")

        try:
            # Import Agor MCP tools
            # In actual execution, these would be available via the MCP
            # For now, output instructions for the orchestrator

            session_id = f"PLACEHOLDER-{card_id[:8]}"  # Will be replaced by actual session ID

            print(f"   ⚙️  Orchestrator should create session here")
            print(f"   ⚙️  Session ID will be: {session_id}")

            # Track in DuckDB
            db.create_session(
                card_id=card_id,
                session_id=session_id,
                category=category,
                title=title
            )

            print(f"   ✅ Tracked in DuckDB")
            created_count += 1

        except Exception as e:
            print(f"   ❌ Failed: {e}")
            failed_count += 1

        print()

    db.close()

    print(f"{'='*70}")
    print(f"SUMMARY:")
    print(f"  Created: {created_count}")
    print(f"  Failed: {failed_count}")
    print(f"  Total: {len(new_sessions)}")
    print(f"{'='*70}\n")

    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
