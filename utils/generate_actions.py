#!/usr/bin/env python3
"""
Generate Actions v2 - DuckDB Version

Much simpler than JSON version:
- Just query: SELECT card_id WHERE status='active'
- Check if card_id in results → UPDATE, else → CREATE
- Done!

Compare to v1:
- No loading entire JSON file
- No building maps
- No manual deduplication
- Instant lookups via index
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from session_db import SessionDB

WORKSPACE_ROOT = Path(__file__).parent.parent


def generate_actions(plan_file: str) -> Dict:
    """Generate action list from plan and database"""

    # Load plan
    with open(plan_file) as f:
        plan = json.load(f)

    # Connect to database
    db = SessionDB()

    # Get active card IDs (one simple query!)
    active_card_ids = set(s['card_id'] for s in db.get_all_active_sessions())

    print(f"✓ Found {len(active_card_ids)} active sessions in database")

    # Generate actions
    actions = []
    stats = {
        'updates': 0,
        'creates': 0,
        'skipped': 0
    }

    # Process all tasks from plan
    all_tasks = (
        [(t, 'coding') for t in plan.get('coding_tasks', [])] +
        [(t, 'research') for t in plan.get('research_tasks', [])] +
        [(t, 'personal') for t in plan.get('personal_tasks', [])]
    )

    for task, category in all_tasks:
        card_id = task['card_id']

        # THE CRITICAL CHECK: Is this card already in the database?
        if card_id in active_card_ids:
            # Get session info
            session = db.get_session(card_id)

            # UPDATE existing session
            actions.append({
                'action': 'update',
                'session_id': session['session_id'],
                'card_id': card_id,
                'title': task['title'],
                'category': category,
                'task': task
            })
            stats['updates'] += 1
            print(f"  → UPDATE {session['session_id'][:8]} - {task['title']}")
        else:
            # CREATE new session
            actions.append({
                'action': 'create',
                'card_id': card_id,
                'title': task['title'],
                'category': category,
                'task': task
            })
            stats['creates'] += 1
            print(f"  → CREATE new session - {task['title']}")

    db.close()

    # Build output
    output = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'plan_file': plan_file,
        'stats': stats,
        'actions': actions,
        'active_sessions_count': len(active_card_ids)
    }

    return output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_actions_v2.py <plan_file.json>")
        sys.exit(1)

    plan_file = sys.argv[1]

    print(f"Generating actions from: {plan_file}\n")

    actions = generate_actions(plan_file)

    # Save to file
    output_file = WORKSPACE_ROOT / "memory" / f"trello-actions-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(actions, f, indent=2)

    print(f"\n✓ Actions saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Updates: {actions['stats']['updates']}")
    print(f"  Creates: {actions['stats']['creates']}")
    print(f"  Total actions: {len(actions['actions'])}")

    # Also output to stdout for piping
    print("\n" + "="*60)
    print(json.dumps(actions, indent=2))
