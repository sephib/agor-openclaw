#!/usr/bin/env python3
"""
Detect Duplicate Sessions via Agor MCP

This script MUST be run from within an Agor session that has MCP access.
It queries the Agor MCP server to find all sessions in the visibility-hub
worktree and detects duplicates based on Trello ticket IDs.

Usage:
    This script is meant to be imported and called by an Agor agent, NOT run standalone.
    The Agor agent should use mcp__agor__agor_sessions_list to query sessions.
"""

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Paths
WORKSPACE_ROOT = Path(__file__).parent.parent
STATE_FILE = WORKSPACE_ROOT / "memory/agor-state/trello-processor.json"
VISIBILITY_WORKTREE_ID = "659dbc25-b301-4e2c-ab26-c07cd1737fcb"


def extract_ticket_id_from_title(title: str) -> str | None:
    """
    Try to extract Trello ticket ID from session title

    Trello card IDs are typically 24-character hex strings.
    """
    # Look for 24-char hex pattern
    match = re.search(r'\b[0-9a-f]{24}\b', title.lower())
    if match:
        return match.group(0)
    return None


def extract_ticket_id_from_session_data(session: Dict) -> str | None:
    """
    Extract Trello ticket ID from session metadata

    Strategy:
    1. Check title for card ID pattern
    2. Check description for card ID
    3. Parse tasks/prompts for card_id field
    """
    # Try title first
    ticket_id = extract_ticket_id_from_title(session.get('title', ''))
    if ticket_id:
        return ticket_id

    # Try description
    description = session.get('description', '')
    if description:
        ticket_id = extract_ticket_id_from_title(description)
        if ticket_id:
            return ticket_id

    # TODO: Would need to fetch tasks and parse prompts for card_id
    # This requires additional MCP calls

    return None


def analyze_sessions(sessions: List[Dict]) -> Dict:
    """
    Analyze sessions to detect duplicates

    Returns:
        {
            'total_sessions': int,
            'sessions_by_ticket': {ticket_id: [session_list]},
            'duplicates': {ticket_id: [session_list]},
            'orphaned_sessions': [sessions without ticket_id],
            'by_status': {status: count}
        }
    """
    sessions_by_ticket = defaultdict(list)
    orphaned = []
    status_counts = defaultdict(int)

    for session in sessions:
        # Skip archived sessions
        if session.get('archived'):
            continue

        # Count by status
        status = session.get('status', 'unknown')
        status_counts[status] += 1

        # Extract ticket ID
        ticket_id = extract_ticket_id_from_session_data(session)

        if ticket_id:
            sessions_by_ticket[ticket_id].append({
                'session_id': session['session_id'],
                'title': session.get('title', 'Unknown'),
                'status': status,
                'created_at': session.get('created_at'),
                'last_updated': session.get('last_updated'),
                'url': session.get('url'),
                'description': session.get('description', '')
            })
        else:
            orphaned.append({
                'session_id': session['session_id'],
                'title': session.get('title', 'Unknown'),
                'status': status,
                'created_at': session.get('created_at')
            })

    # Find duplicates (tickets with multiple sessions)
    duplicates = {
        ticket_id: sessions_list
        for ticket_id, sessions_list in sessions_by_ticket.items()
        if len(sessions_list) > 1
    }

    return {
        'total_sessions': len(sessions),
        'sessions_by_ticket': dict(sessions_by_ticket),
        'duplicates': duplicates,
        'orphaned_sessions': orphaned,
        'by_status': dict(status_counts),
        'stats': {
            'unique_tickets': len(sessions_by_ticket),
            'duplicate_tickets': len(duplicates),
            'orphaned_count': len(orphaned)
        }
    }


def compare_with_state(analysis: Dict, state_file: Path = STATE_FILE) -> Dict:
    """
    Compare MCP analysis with state file

    Returns:
        {
            'state_tickets': [ticket_ids in state],
            'mcp_tickets': [ticket_ids in MCP],
            'in_both': [tickets in both],
            'state_only': [tickets in state but not MCP],
            'mcp_only': [tickets in MCP but not state],
            'mismatches': [{ticket_id, state_session, mcp_sessions}]
        }
    """
    # Load state
    if state_file.exists():
        with open(state_file) as f:
            state = json.load(f)
    else:
        state = {}

    # Extract ticket IDs from state
    state_tickets = {}
    for session in state.get('active_coding_sessions', []):
        ticket_id = session.get('ticket_id')
        if ticket_id:
            state_tickets[ticket_id] = session['session_id']

    for session in state.get('active_research_sessions', []):
        ticket_id = session.get('ticket_id')
        if ticket_id:
            state_tickets[ticket_id] = session['session_id']

    for session in state.get('active_personal_sessions', []):
        ticket_id = session.get('ticket_id')
        if ticket_id:
            state_tickets[ticket_id] = session['session_id']

    # Extract ticket IDs from MCP
    mcp_tickets = set(analysis['sessions_by_ticket'].keys())
    state_ticket_ids = set(state_tickets.keys())

    # Find mismatches
    mismatches = []
    for ticket_id in state_ticket_ids & mcp_tickets:
        state_session_id = state_tickets[ticket_id]
        mcp_sessions = analysis['sessions_by_ticket'][ticket_id]

        # Check if state session exists in MCP
        mcp_session_ids = [s['session_id'] for s in mcp_sessions]

        if state_session_id not in mcp_session_ids:
            mismatches.append({
                'ticket_id': ticket_id,
                'state_session': state_session_id,
                'mcp_sessions': mcp_session_ids,
                'issue': 'State session not found in MCP'
            })
        elif len(mcp_sessions) > 1:
            mismatches.append({
                'ticket_id': ticket_id,
                'state_session': state_session_id,
                'mcp_sessions': mcp_session_ids,
                'issue': f'Duplicate sessions in MCP ({len(mcp_sessions)} sessions)'
            })

    return {
        'state_tickets': list(state_ticket_ids),
        'mcp_tickets': list(mcp_tickets),
        'in_both': list(state_ticket_ids & mcp_tickets),
        'state_only': list(state_ticket_ids - mcp_tickets),
        'mcp_only': list(mcp_tickets - state_ticket_ids),
        'mismatches': mismatches
    }


def generate_duplicate_report(
    sessions: List[Dict],
    output_file: Path | None = None
) -> Dict:
    """
    Generate comprehensive duplicate detection report

    Args:
        sessions: List of sessions from MCP query
        output_file: Optional path to save report

    Returns:
        Complete report dict
    """
    # Analyze sessions
    analysis = analyze_sessions(sessions)

    # Compare with state
    comparison = compare_with_state(analysis)

    # Build report
    report = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'visibility_worktree_id': VISIBILITY_WORKTREE_ID,
        'analysis': analysis,
        'comparison': comparison,
        'issues': []
    }

    # Identify issues
    if analysis['stats']['duplicate_tickets'] > 0:
        report['issues'].append({
            'severity': 'critical',
            'type': 'duplicates_in_mcp',
            'count': analysis['stats']['duplicate_tickets'],
            'message': f"Found {analysis['stats']['duplicate_tickets']} tickets with multiple sessions"
        })

    if comparison['mismatches']:
        report['issues'].append({
            'severity': 'high',
            'type': 'state_mcp_mismatch',
            'count': len(comparison['mismatches']),
            'message': f"Found {len(comparison['mismatches'])} mismatches between state and MCP"
        })

    if comparison['state_only']:
        report['issues'].append({
            'severity': 'medium',
            'type': 'state_only',
            'count': len(comparison['state_only']),
            'message': f"Found {len(comparison['state_only'])} tickets in state but not in MCP"
        })

    if comparison['mcp_only']:
        report['issues'].append({
            'severity': 'medium',
            'type': 'mcp_only',
            'count': len(comparison['mcp_only']),
            'message': f"Found {len(comparison['mcp_only'])} tickets in MCP but not in state"
        })

    # Save report if requested
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

    return report


def print_duplicate_report(report: Dict):
    """Print human-readable duplicate report"""
    print("\n" + "=" * 80)
    print("🔍 DUPLICATE SESSION DETECTION REPORT (via Agor MCP)")
    print("=" * 80)
    print(f"Timestamp: {report['timestamp']}")
    print(f"Worktree: {report['visibility_worktree_id']}")
    print()

    # Statistics
    stats = report['analysis']['stats']
    print("📊 STATISTICS:")
    print(f"   Total sessions: {report['analysis']['total_sessions']}")
    print(f"   Unique tickets: {stats['unique_tickets']}")
    print(f"   Duplicate tickets: {stats['duplicate_tickets']} ⚠️" if stats['duplicate_tickets'] > 0 else f"   Duplicate tickets: 0 ✅")
    print(f"   Orphaned sessions: {stats['orphaned_count']}")
    print()

    # Session status breakdown
    print("📈 BY STATUS:")
    for status, count in report['analysis']['by_status'].items():
        print(f"   {status}: {count}")
    print()

    # Duplicates
    if report['analysis']['duplicates']:
        print("🚨 DUPLICATE SESSIONS FOUND:")
        for ticket_id, sessions in report['analysis']['duplicates'].items():
            print(f"\n   Ticket: {ticket_id} ({len(sessions)} sessions)")
            for i, session in enumerate(sessions, 1):
                print(f"      {i}. {session['session_id'][:8]} - {session['title']}")
                print(f"         Status: {session['status']}, Created: {session['created_at']}")
                if session.get('description'):
                    print(f"         Note: {session['description']}")
        print()
    else:
        print("✅ NO DUPLICATE SESSIONS FOUND")
        print()

    # State comparison
    comp = report['comparison']
    print("🔄 STATE FILE COMPARISON:")
    print(f"   Tickets in state: {len(comp['state_tickets'])}")
    print(f"   Tickets in MCP: {len(comp['mcp_tickets'])}")
    print(f"   In both: {len(comp['in_both'])}")
    print(f"   State only: {len(comp['state_only'])}")
    print(f"   MCP only: {len(comp['mcp_only'])}")
    print()

    if comp['mismatches']:
        print("⚠️  MISMATCHES:")
        for mismatch in comp['mismatches']:
            print(f"   Ticket: {mismatch['ticket_id']}")
            print(f"   Issue: {mismatch['issue']}")
            print(f"   State session: {mismatch['state_session']}")
            print(f"   MCP sessions: {', '.join(mismatch['mcp_sessions'])}")
            print()

    # Issues summary
    if report['issues']:
        print("🚨 ISSUES SUMMARY:")
        for issue in report['issues']:
            emoji = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '🟢'}.get(issue['severity'], '❓')
            print(f"   {emoji} [{issue['severity'].upper()}] {issue['message']}")
        print()
    else:
        print("✅ NO ISSUES FOUND")
        print()

    print("=" * 80)
    print()


# Example usage for Agor agents:
EXAMPLE_USAGE = """
# This script should be called from within an Agor session like this:

```python
import sys
sys.path.insert(0, 'utils')
from detect_duplicates_mcp import generate_duplicate_report, print_duplicate_report

# Query Agor MCP for sessions
sessions_result = mcp__agor__agor_sessions_list(
    worktreeId='659dbc25-b301-4e2c-ab26-c07cd1737fcb',
    limit=500  # Adjust as needed
)

# Generate report
report = generate_duplicate_report(
    sessions=sessions_result['data'],
    output_file=Path('memory/verification-reports/duplicate-report-latest.json')
)

# Print report
print_duplicate_report(report)

# Check for duplicates
if report['analysis']['stats']['duplicate_tickets'] > 0:
    print("⛔ DUPLICATES FOUND - DO NOT CREATE NEW SESSIONS")
else:
    print("✅ No duplicates - safe to proceed")
```
"""


if __name__ == "__main__":
    print("⚠️  This script must be run from within an Agor session with MCP access")
    print()
    print(EXAMPLE_USAGE)
