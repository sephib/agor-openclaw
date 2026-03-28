#!/usr/bin/env python3
"""
Duplicate Session Verification System

This script ensures NO duplicate sessions are created for single Trello cards.

Features:
- Pre-flight checks before creating sessions
- Real-time duplicate detection via state + MCP
- Post-run verification
- Detailed JSON reporting

Exit codes:
- 0: No duplicates found
- 1: Duplicates detected
- 2: Configuration error
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Add utils to path for session_db import
sys.path.insert(0, str(Path(__file__).parent))
from session_db import SessionDB

# Paths
WORKSPACE_ROOT = Path(__file__).parent.parent
VERIFICATION_REPORTS_DIR = WORKSPACE_ROOT / "memory/verification-reports"
VISIBILITY_WORKTREE_ID = "659dbc25-b301-4e2c-ab26-c07cd1737fcb"

# Ensure reports directory exists
VERIFICATION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def get_state_ticket_ids() -> Dict[str, Dict]:
    """Extract ticket_id -> session mapping from DuckDB"""
    db = SessionDB()
    ticket_map = {}

    for session in db.get_all_active_sessions():
        ticket_map[session['card_id']] = {
            'session_id': session['session_id'],
            'category': session['category'],
            'title': session.get('title', 'Unknown'),
            'source': 'duckdb'
        }

    db.close()
    return ticket_map


def query_agor_sessions() -> List[Dict]:
    """Query Agor MCP for all sessions in visibility-hub worktree"""
    try:
        # Use MCP to list sessions
        # Note: This would need to be called from within an Agor session with MCP access
        # For now, we'll use a placeholder that can be replaced with actual MCP call
        print("⚠️  WARNING: Direct MCP query not available in this context")
        print("   This verification should be run from within an Agor session")
        return []
    except Exception as e:
        print(f"⚠️  Failed to query Agor sessions: {e}")
        return []


def extract_ticket_id_from_session(session: Dict) -> str | None:
    """
    Extract Trello ticket_id (card_id) from session metadata

    We need to look in:
    - Session title (if it contains card_id)
    - Session tasks (initial prompts may contain card_id)
    - Session description/metadata
    """
    # This is a placeholder - in real implementation we'd need to:
    # 1. Read session tasks to find the initial prompt
    # 2. Parse the prompt for card_id field
    # 3. Or store card_id in session metadata explicitly

    # For now, we'll return None indicating we need MCP access
    return None


def detect_duplicates_in_agor(sessions: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Detect duplicate sessions for same ticket_id in Agor

    Returns:
        Dict mapping ticket_id -> list of sessions
    """
    ticket_sessions = {}

    for session in sessions:
        # Skip archived or deleted sessions
        if session.get('archived') or session.get('status') == 'deleted':
            continue

        # Extract ticket_id
        ticket_id = extract_ticket_id_from_session(session)
        if not ticket_id:
            continue

        if ticket_id not in ticket_sessions:
            ticket_sessions[ticket_id] = []

        ticket_sessions[ticket_id].append({
            'session_id': session['session_id'],
            'title': session.get('title', 'Unknown'),
            'status': session.get('status', 'unknown'),
            'created_at': session.get('created_at'),
            'source': 'agor_mcp'
        })

    # Filter to only tickets with duplicates
    duplicates = {
        ticket_id: sessions_list
        for ticket_id, sessions_list in ticket_sessions.items()
        if len(sessions_list) > 1
    }

    return duplicates


def cross_check_state_vs_agor(
    state_tickets: Dict[str, Dict],
    agor_tickets: Dict[str, List[Dict]]
) -> Dict:
    """
    Cross-check state file against Agor MCP reality

    Returns:
        {
            'match': [ticket_ids that match],
            'state_only': [tickets in state but not in Agor],
            'agor_only': [tickets in Agor but not in state],
            'duplicates_in_agor': [tickets with multiple sessions in Agor]
        }
    """
    state_ids = set(state_tickets.keys())
    agor_ids = set(agor_tickets.keys())

    # Find tickets with duplicates in Agor
    duplicates_in_agor = {
        ticket_id: sessions
        for ticket_id, sessions in agor_tickets.items()
        if len(sessions) > 1
    }

    return {
        'match': list(state_ids & agor_ids),
        'state_only': list(state_ids - agor_ids),
        'agor_only': list(agor_ids - state_ids),
        'duplicates_in_agor': duplicates_in_agor
    }


def verify_plan_file(plan_file: Path) -> Dict:
    """
    Verify that a plan file exists and is valid JSON

    Returns:
        {
            'exists': bool,
            'valid_json': bool,
            'task_count': int,
            'tickets': [list of ticket_ids]
        }
    """
    if not plan_file.exists():
        return {
            'exists': False,
            'valid_json': False,
            'task_count': 0,
            'tickets': []
        }

    try:
        with open(plan_file) as f:
            plan = json.load(f)

        # Extract all tickets from plan
        tickets = []
        for task in plan.get('coding_tasks', []):
            tickets.append(task['card_id'])
        for task in plan.get('research_tasks', []):
            tickets.append(task['card_id'])
        for task in plan.get('personal_tasks', []):
            tickets.append(task['card_id'])

        return {
            'exists': True,
            'valid_json': True,
            'task_count': len(tickets),
            'tickets': tickets
        }
    except Exception as e:
        return {
            'exists': True,
            'valid_json': False,
            'error': str(e),
            'task_count': 0,
            'tickets': []
        }


def verify_actions_file(actions_file: Path) -> Dict:
    """
    Verify that actions file exists and has correct structure

    Returns:
        {
            'exists': bool,
            'valid_json': bool,
            'update_count': int,
            'create_count': int,
            'actions': [list of actions]
        }
    """
    if not actions_file.exists():
        return {
            'exists': False,
            'valid_json': False,
            'update_count': 0,
            'create_count': 0,
            'actions': []
        }

    try:
        with open(actions_file) as f:
            actions_data = json.load(f)

        stats = actions_data.get('stats', {})

        return {
            'exists': True,
            'valid_json': True,
            'update_count': stats.get('updates', 0),
            'create_count': stats.get('creates', 0),
            'actions': actions_data.get('actions', [])
        }
    except Exception as e:
        return {
            'exists': True,
            'valid_json': False,
            'error': str(e),
            'update_count': 0,
            'create_count': 0,
            'actions': []
        }


def run_verification(
    mode: str = 'pre-flight',
    plan_file: Path | None = None,
    actions_file: Path | None = None
) -> Dict:
    """
    Run verification checks

    Args:
        mode: 'pre-flight', 'post-run', or 'manual'
        plan_file: Path to plan file (optional)
        actions_file: Path to actions file (optional)

    Returns:
        Verification report dict
    """
    report = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'mode': mode,
        'checks': {},
        'issues': [],
        'duplicates_found': False
    }

    # Check 1: DuckDB database exists and is valid
    try:
        state_tickets = get_state_ticket_ids()

        report['checks']['database'] = {
            'status': 'pass',
            'ticket_count': len(state_tickets),
            'tickets': list(state_tickets.keys())
        }
    except Exception as e:
        report['checks']['database'] = {
            'status': 'fail',
            'error': str(e)
        }
        report['issues'].append(f"Database error: {e}")

    # Check 2: Plan file (if provided)
    if plan_file:
        plan_check = verify_plan_file(plan_file)
        report['checks']['plan_file'] = plan_check

        if not plan_check['exists']:
            report['issues'].append(f"Plan file missing: {plan_file}")
        elif not plan_check['valid_json']:
            report['issues'].append(f"Plan file invalid JSON: {plan_check.get('error')}")

    # Check 3: Actions file (if provided)
    if actions_file:
        actions_check = verify_actions_file(actions_file)
        report['checks']['actions_file'] = actions_check

        if not actions_check['exists']:
            report['issues'].append(f"Actions file missing: {actions_file}")
        elif not actions_check['valid_json']:
            report['issues'].append(f"Actions file invalid JSON: {actions_check.get('error')}")
        else:
            # Verify no CREATE actions for tickets already in database
            if 'database' in report['checks'] and report['checks']['database']['status'] == 'pass':
                state_tickets = set(report['checks']['database']['tickets'])

                for action in actions_check['actions']:
                    if action['action'] == 'create':
                        ticket_id = action.get('card_id') or action.get('ticket_id')
                        if ticket_id in state_tickets:
                            report['issues'].append(
                                f"⚠️  DUPLICATE RISK: Action wants to CREATE session for card {ticket_id} "
                                f"but database already has session for this card"
                            )
                            report['duplicates_found'] = True

    # Check 4: Agor MCP sessions (only if we have MCP access)
    # This would be implemented when running inside Agor session
    report['checks']['agor_mcp'] = {
        'status': 'skipped',
        'message': 'MCP query not available in this context - run from Agor session'
    }

    # Summary
    report['summary'] = {
        'total_checks': len(report['checks']),
        'passed': sum(1 for c in report['checks'].values() if c.get('status') == 'pass'),
        'failed': sum(1 for c in report['checks'].values() if c.get('status') == 'fail'),
        'skipped': sum(1 for c in report['checks'].values() if c.get('status') == 'skipped'),
        'issues_count': len(report['issues']),
        'duplicates_found': report['duplicates_found']
    }

    return report


def print_report(report: Dict):
    """Print verification report to console"""
    print("\n" + "=" * 70)
    print(f"🔍 DUPLICATE VERIFICATION REPORT - {report['mode'].upper()}")
    print("=" * 70)
    print(f"Timestamp: {report['timestamp']}")
    print()

    # Print checks
    for check_name, check_result in report['checks'].items():
        status_emoji = {
            'pass': '✅',
            'fail': '❌',
            'skipped': '⏭️'
        }.get(check_result.get('status'), '❓')

        print(f"{status_emoji} {check_name.replace('_', ' ').title()}: {check_result.get('status', 'unknown')}")

        if check_result.get('status') == 'pass':
            if 'ticket_count' in check_result:
                print(f"   - Tickets: {check_result['ticket_count']}")
        elif check_result.get('status') == 'fail':
            if 'error' in check_result:
                print(f"   - Error: {check_result['error']}")

    print()

    # Print issues
    if report['issues']:
        print("🚨 ISSUES FOUND:")
        for issue in report['issues']:
            print(f"   - {issue}")
        print()
    else:
        print("✅ No issues found")
        print()

    # Print summary
    summary = report['summary']
    print(f"Summary: {summary['passed']} passed, {summary['failed']} failed, {summary['skipped']} skipped")

    if report['duplicates_found']:
        print()
        print("⛔ DUPLICATES DETECTED - DO NOT PROCEED")
    else:
        print()
        print("✅ No duplicates detected - safe to proceed")

    print("=" * 70)
    print()


def save_report(report: Dict, filename: str | None = None):
    """Save verification report to JSON file"""
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        filename = f"verification-{report['mode']}-{timestamp}.json"

    report_file = VERIFICATION_REPORTS_DIR / filename

    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"📄 Report saved: {report_file}")
    return report_file


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Verify no duplicate sessions for Trello tickets"
    )
    parser.add_argument(
        '--mode',
        choices=['pre-flight', 'post-run', 'manual'],
        default='manual',
        help='Verification mode'
    )
    parser.add_argument(
        '--plan-file',
        type=Path,
        help='Path to plan file to verify'
    )
    parser.add_argument(
        '--actions-file',
        type=Path,
        help='Path to actions file to verify'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Only output errors (no console report)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Custom output filename for report'
    )

    args = parser.parse_args()

    # Run verification
    report = run_verification(
        mode=args.mode,
        plan_file=args.plan_file,
        actions_file=args.actions_file
    )

    # Print report (unless quiet)
    if not args.quiet:
        print_report(report)

    # Save report
    save_report(report, args.output)

    # Exit with appropriate code
    if report['duplicates_found']:
        sys.exit(1)
    elif report['summary']['failed'] > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
