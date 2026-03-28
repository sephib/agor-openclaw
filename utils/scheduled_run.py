#!/usr/bin/env python3
"""
Scheduled Run Entry Point - DuckDB Duplicate Prevention

This is the MAIN entry point for Agor's scheduled runs.
It ensures duplicate prevention by checking DuckDB BEFORE creating sessions.

Flow:
1. Generate Trello ticket plan
2. Check DuckDB for existing sessions
3. Filter out tickets that already have sessions
4. Output ONLY new tickets that need sessions
5. Orchestrator creates sessions for filtered list only

This prevents duplicates by removing decision-making from the orchestrator.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).parent.parent


def run_command(cmd: list, description: str) -> tuple:
    """Run command and return (success, stdout, stderr)"""
    print(f"\n{'='*70}")
    print(f"⚙️  {description}")
    print(f"{'='*70}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=WORKSPACE_ROOT
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode != 0:
            print(f"❌ Failed: {result.stderr}", file=sys.stderr)
            return False, result.stdout, result.stderr

        return True, result.stdout, result.stderr

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return False, "", str(e)


def main():
    """Main scheduled run flow"""
    print("\n" + "="*70)
    print("🤖 TRELLO TICKET PROCESSOR - SCHEDULED RUN")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # STEP 1: Generate plan from Trello
    success, stdout, stderr = run_command(
        ["python3", "utils/process_trello_tickets.py"],
        "STEP 1: Fetching Trello tickets and generating plan"
    )

    if not success:
        print("\n❌ FAILED: Could not generate plan")
        return 1

    # Extract plan file from output
    plan_file = None
    for line in stdout.split('\n'):
        if 'JSON plan saved to:' in line:
            plan_file = line.split('JSON plan saved to:')[1].strip()
            break

    if not plan_file or not Path(plan_file).exists():
        print("\n❌ FAILED: Could not find plan file")
        return 1

    print(f"\n✅ Plan generated: {plan_file}")

    # STEP 2: Generate actions with DuckDB duplicate check
    success, stdout, stderr = run_command(
        ["python3", "utils/generate_actions.py", plan_file],
        "STEP 2: Checking DuckDB for existing sessions"
    )

    if not success:
        print("\n❌ FAILED: Could not generate actions")
        return 1

    # Extract actions file from output
    actions_file = None
    for line in stdout.split('\n'):
        if 'Actions saved to:' in line:
            actions_file = line.split('Actions saved to:')[1].strip()
            break

    if not actions_file or not Path(actions_file).exists():
        print("\n❌ FAILED: Could not find actions file")
        return 1

    print(f"\n✅ Actions generated: {actions_file}")

    # Load actions to check what needs to be done
    with open(actions_file) as f:
        actions_data = json.load(f)

    stats = actions_data.get('stats', {})
    updates = stats.get('updates', 0)
    creates = stats.get('creates', 0)

    print(f"\n📊 ACTION SUMMARY:")
    print(f"   Updates: {updates} (existing sessions)")
    print(f"   Creates: {creates} (new sessions needed)")
    print(f"   Total: {updates + creates}")

    # STEP 3: Filter to only CREATE actions
    create_actions = [
        action for action in actions_data.get('actions', [])
        if action.get('action') == 'create'
    ]

    if creates == 0:
        print("\n✅ NO NEW SESSIONS NEEDED")
        print("   All tickets already have active sessions.")
        print("   Nothing to do - exiting.")
        return 0

    # STEP 4: Output filtered plan for orchestrator
    print(f"\n📝 CREATING {creates} NEW SESSIONS:")

    output = {
        'timestamp': datetime.now().isoformat(),
        'plan_file': plan_file,
        'actions_file': actions_file,
        'new_sessions': []
    }

    for action in create_actions:
        task = action.get('task', {})
        category = action.get('category', 'unknown')

        session_info = {
            'card_id': action.get('card_id'),
            'title': action.get('title'),
            'category': category,
            'url': task.get('url'),
            'priority': task.get('priority_score'),
            'description': task.get('description', '')[:200]  # Truncate
        }

        output['new_sessions'].append(session_info)

        print(f"   • {session_info['title']} ({category})")

    # Save filtered output
    filtered_file = WORKSPACE_ROOT / "memory" / f"filtered-new-sessions-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(filtered_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n✅ Filtered output: {filtered_file}")

    # STEP 5: Output instructions for orchestrator
    print("\n" + "="*70)
    print("📋 ORCHESTRATOR INSTRUCTIONS:")
    print("="*70)
    print(f"""
For each session in {filtered_file}:

1. Create session in trello-visibility-hub worktree
2. Use session title and description from JSON
3. Track session_id in DuckDB:

   from utils.session_db import SessionDB
   db = SessionDB()
   db.create_session(card_id, session_id, category, title)
   db.close()

4. DO NOT create sessions for tickets already in DuckDB
5. ONLY create sessions listed in filtered output above

This prevents duplicates by checking DuckDB first.
""")

    print("="*70)
    print(f"✅ SCHEDULED RUN COMPLETE - {creates} new sessions to create")
    print("="*70)

    return 0


if __name__ == "__main__":
    sys.exit(main())
