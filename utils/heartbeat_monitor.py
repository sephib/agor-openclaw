#!/usr/bin/env python3
"""
Heartbeat Monitoring System for Nesher

Proactively monitors worktrees, sessions, and Trello tickets.
Detects stale work, missing PRs, and issues requiring attention.
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add workspace root to path
WORKSPACE_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

# Configuration
MAIN_BOARD_ID = "1a508c77-dacb-46fe-ab24-e527fb476882"
TRELLO_ACTIVE_TASKS_WORKTREE_ID = "326229ab-4f76-445a-a5f6-ef4cc3d61d9a"
STATE_DIR = WORKSPACE_ROOT / "memory" / "agor-state"
CONFIG_FILE = WORKSPACE_ROOT / "config" / "heartbeat.json"


def load_config() -> Dict:
    """Load heartbeat configuration"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)

    # Default config
    return {
        "monitoring": {
            "frequency_hours": 2,
            "stale_thresholds": {
                "medium": 7,
                "high": 14,
                "critical": 21
            }
        },
        "pr_automation": {
            "auto_create_enabled": False,
            "auto_merge_enabled": False,
            "auto_review_enabled": False
        },
        "escalation": {
            "daily_log_enabled": True,
            "slack_enabled": False
        }
    }


def fetch_all_worktrees() -> List[Dict]:
    """
    Fetch all worktrees from Agor board via MCP

    In practice, this would use:
    agor.worktrees.list(board_id=MAIN_BOARD_ID)

    For now, returns placeholder structure.
    """
    # This is a placeholder - real implementation needs MCP access
    # When run in Agor session, use:
    # return agor.worktrees.list(board_id=MAIN_BOARD_ID)

    return []


def fetch_sessions(worktree_id: Optional[str] = None) -> List[Dict]:
    """
    Fetch sessions from Agor

    In practice, this would use:
    agor.sessions.list(worktree_id=worktree_id) if worktree_id
    else agor.sessions.list(board_id=MAIN_BOARD_ID)
    """
    # Placeholder - needs MCP access
    return []


def calculate_age_days(updated_at: str) -> int:
    """Calculate days since last update"""
    try:
        updated = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        return (now - updated).days
    except:
        return 0


def sync_state_files(worktrees: List[Dict], sessions: List[Dict]) -> None:
    """Update memory/agor-state/*.json with current reality"""

    STATE_DIR.mkdir(parents=True, exist_ok=True)

    # Update worktrees.json
    state_worktrees = {
        'managed_worktrees': [
            {
                'worktree_id': wt['worktree_id'],
                'name': wt['name'],
                'zone_label': wt.get('zone_label', 'Unknown'),
                'zone_id': wt.get('zone_id'),
                'status': infer_status(wt),
                'age_days': calculate_age_days(wt.get('updated_at', '')),
                'last_checked': datetime.now(timezone.utc).isoformat(),
                'pull_request_url': wt.get('pull_request_url'),
                'issue_url': wt.get('issue_url'),
                'notes': wt.get('notes', '')[:200]  # Truncate for summary
            }
            for wt in worktrees
            if wt['name'] not in ['trello-task-processor', 'trello-active-tasks']
        ],
        'last_synced': datetime.now(timezone.utc).isoformat()
    }

    with open(STATE_DIR / 'worktrees.json', 'w') as f:
        json.dump(state_worktrees, f, indent=2)

    # Update sessions.json (for active ticket sessions)
    ticket_sessions = [
        s for s in sessions
        if s.get('worktree_id') == TRELLO_ACTIVE_TASKS_WORKTREE_ID
    ]

    state_sessions = {
        'active_ticket_sessions': [
            {
                'session_id': s['session_id'],
                'status': s.get('status', 'unknown'),
                'created_at': s.get('created_at'),
                'updated_at': s.get('updated_at')
            }
            for s in ticket_sessions
        ],
        'last_synced': datetime.now(timezone.utc).isoformat()
    }

    with open(STATE_DIR / 'sessions.json', 'w') as f:
        json.dump(state_sessions, f, indent=2)


def infer_status(worktree: Dict) -> str:
    """Infer worktree status from metadata"""
    zone = worktree.get('zone_label', '')

    if 'Done' in zone:
        return 'completed'
    elif 'In Progress' in zone:
        return 'active'
    elif 'Open a PR' in zone:
        return 'ready_for_pr'
    elif 'review' in zone.lower():
        return 'in_review'
    elif 'Design' in zone:
        return 'planning'
    else:
        return 'unknown'


def check_in_progress(worktree: Dict, issues: Dict, config: Dict) -> None:
    """Check worktrees in 'In Progress' zone for staleness"""
    age_days = calculate_age_days(worktree.get('updated_at', ''))
    thresholds = config['monitoring']['stale_thresholds']

    if age_days >= thresholds['critical']:
        severity = 'critical'
    elif age_days >= thresholds['high']:
        severity = 'high'
    elif age_days >= thresholds['medium']:
        severity = 'medium'
    else:
        return  # Not stale yet

    issues['stale_work'].append({
        'worktree_id': worktree['worktree_id'],
        'name': worktree['name'],
        'age_days': age_days,
        'severity': severity,
        'zone': worktree.get('zone_label'),
        'action': 'escalate_to_human'
    })


def check_ready_for_pr(worktree: Dict, issues: Dict, config: Dict) -> None:
    """Check worktrees in 'Open a PR' zone for missing PRs"""

    # Missing PR
    if not worktree.get('pull_request_url'):
        issues['missing_prs'].append({
            'worktree_id': worktree['worktree_id'],
            'name': worktree['name'],
            'path': worktree.get('path'),
            'age_days': calculate_age_days(worktree.get('updated_at', '')),
            'action': 'create_pr',
            'safety': 'spawn_subsession'  # Don't create directly
        })


def check_in_review(worktree: Dict, issues: Dict, config: Dict) -> None:
    """Check worktrees in review zones"""
    pr_url = worktree.get('pull_request_url')
    if not pr_url:
        return

    # Would check PR status here via gh CLI
    # For now, just note it exists
    issues['pr_in_review'].append({
        'worktree_id': worktree['worktree_id'],
        'name': worktree['name'],
        'pr_url': pr_url,
        'action': 'monitor'
    })


def check_completed(worktree: Dict, issues: Dict, config: Dict) -> None:
    """Check worktrees in Done zone for cleanup candidates"""
    age_days = calculate_age_days(worktree.get('updated_at', ''))

    # Cleanup candidates (>30 days in Done)
    if age_days > 30:
        issues['cleanup_candidates'].append({
            'worktree_id': worktree['worktree_id'],
            'name': worktree['name'],
            'age_days': age_days,
            'action': 'mark_for_cleanup',
            'safety': 'manual_approval_required'
        })


def analyze_worktrees(worktrees: List[Dict], config: Dict) -> Dict:
    """Analyze all worktrees and identify issues"""

    issues = {
        'stale_work': [],
        'missing_prs': [],
        'pr_in_review': [],
        'pr_updates': [],
        'cleanup_candidates': []
    }

    for wt in worktrees:
        zone = wt.get('zone_label', '')

        if 'In Progress' in zone:
            check_in_progress(wt, issues, config)
        elif 'Open a PR' in zone:
            check_ready_for_pr(wt, issues, config)
        elif 'review' in zone.lower():
            check_in_review(wt, issues, config)
        elif 'Done' in zone:
            check_completed(wt, issues, config)

    return issues


def generate_action_plan(issues: Dict, config: Dict) -> Dict:
    """Generate action plan from identified issues"""

    actions = {
        'escalations': [],
        'safe_actions': [],
        'pending_approval': []
    }

    # Import escalation logic
    from escalation import evaluate_escalations

    # Evaluate what needs escalation
    actions['escalations'] = evaluate_escalations(issues, config)

    # Safe actions (monitoring only for now)
    actions['safe_actions'] = [
        {'type': 'sync_state', 'description': 'State files updated'},
        {'type': 'log_issues', 'description': f'Found {len(issues["stale_work"])} stale worktrees'}
    ]

    # Pending approval (manual actions)
    if issues['cleanup_candidates']:
        actions['pending_approval'].extend([
            {
                'type': 'cleanup_worktree',
                'worktree_id': item['worktree_id'],
                'reason': f'Worktree idle for {item["age_days"]} days'
            }
            for item in issues['cleanup_candidates']
        ])

    return actions


def execute_safe_actions(action_plan: Dict) -> None:
    """Execute safe monitoring actions (no destructive operations)"""

    for action in action_plan['safe_actions']:
        # Just log for now
        print(f"✓ {action['description']}")


def heartbeat_check() -> None:
    """Main heartbeat orchestration"""

    print("=== Heartbeat Monitor ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Load config
    config = load_config()

    # NOTE: This script is designed to be run inside an Agor session
    # where agor MCP tools are available. When run standalone, it's
    # a placeholder that shows the structure.

    print("⚠️  This script needs to run in an Agor session with MCP access")
    print("   For now, showing structure only")
    print()

    # Would fetch real data:
    # worktrees = fetch_all_worktrees()
    # sessions = fetch_sessions()

    # Placeholder
    worktrees = []
    sessions = []

    print(f"Worktrees found: {len(worktrees)}")
    print(f"Sessions found: {len(sessions)}")
    print()

    # Sync state files
    sync_state_files(worktrees, sessions)
    print("✓ State files synced")

    # Analyze worktrees
    issues = analyze_worktrees(worktrees, config)
    print(f"✓ Worktrees analyzed")
    print(f"  - Stale work: {len(issues['stale_work'])}")
    print(f"  - Missing PRs: {len(issues['missing_prs'])}")
    print(f"  - Cleanup candidates: {len(issues['cleanup_candidates'])}")
    print()

    # Generate action plan
    action_plan = generate_action_plan(issues, config)
    print(f"✓ Action plan generated")
    print(f"  - Escalations: {len(action_plan['escalations'])}")
    print(f"  - Safe actions: {len(action_plan['safe_actions'])}")
    print(f"  - Pending approval: {len(action_plan['pending_approval'])}")
    print()

    # Execute safe actions
    execute_safe_actions(action_plan)
    print()

    # Escalate issues
    if config['escalation']['daily_log_enabled']:
        from escalation import escalate_to_daily_log
        escalate_to_daily_log(action_plan['escalations'])
        print(f"✓ {len(action_plan['escalations'])} issues escalated to daily log")

    print()
    print("=== Heartbeat Complete ===")


if __name__ == "__main__":
    heartbeat_check()
