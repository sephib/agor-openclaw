#!/usr/bin/env python3
"""
Escalation and Alert System

Determines severity of issues and escalates to appropriate channels.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(__file__).parent.parent

ESCALATION_LEVELS = {
    'critical': {
        'threshold': 21,
        'actions': ['daily_log', 'slack'],
        'emoji': '🚨',
        'description': 'Immediate attention required'
    },
    'high': {
        'threshold': 14,
        'actions': ['daily_log'],
        'emoji': '⚠️',
        'description': 'High priority issue'
    },
    'medium': {
        'threshold': 7,
        'actions': ['daily_log'],
        'emoji': 'ℹ️',
        'description': 'Medium priority issue'
    },
    'low': {
        'threshold': 0,
        'actions': ['weekly_summary'],
        'emoji': '📝',
        'description': 'Low priority issue'
    }
}


def evaluate_escalations(issues: Dict, config: Dict) -> List[Dict]:
    """Determine what needs human attention"""

    escalations = []

    # Stale work escalation
    for stale in issues.get('stale_work', []):
        age = stale['age_days']
        severity = stale['severity']

        level_info = ESCALATION_LEVELS.get(severity, ESCALATION_LEVELS['medium'])

        message = f"{level_info['emoji']} Worktree '{stale['name']}' idle for {age} days"
        if severity == 'critical':
            message = f"CRITICAL: {message}"

        escalations.append({
            'level': severity,
            'message': message,
            'worktree_id': stale['worktree_id'],
            'type': 'stale_work',
            'actions_suggested': suggest_actions({'type': 'stale_work', 'age': age}),
            'emoji': level_info['emoji']
        })

    # Missing PRs
    for missing_pr in issues.get('missing_prs', []):
        age = missing_pr.get('age_days', 0)

        if age > 7:
            level = 'high'
            message = f"⚠️  Worktree '{missing_pr['name']}' in 'Open a PR' zone for {age} days without PR"
        else:
            level = 'medium'
            message = f"ℹ️  Worktree '{missing_pr['name']}' ready for PR (no PR created yet)"

        escalations.append({
            'level': level,
            'message': message,
            'worktree_id': missing_pr['worktree_id'],
            'type': 'missing_pr',
            'actions_suggested': ['Create PR via subsession', 'Review commits', 'Check if work is complete'],
            'emoji': '📝'
        })

    # Cleanup candidates
    for cleanup in issues.get('cleanup_candidates', []):
        escalations.append({
            'level': 'low',
            'message': f"📝 Worktree '{cleanup['name']}' in Done zone for {cleanup['age_days']} days (cleanup candidate)",
            'worktree_id': cleanup['worktree_id'],
            'type': 'cleanup_candidate',
            'actions_suggested': ['Verify PR is merged', 'Delete worktree', 'Archive from board'],
            'emoji': '🗑️'
        })

    return escalations


def suggest_actions(issue: Dict) -> List[str]:
    """Suggest remediation actions based on issue type"""

    if issue['type'] == 'stale_work':
        age = issue.get('age', 0)
        if age > 14:
            return [
                'Review recent commits',
                'Check if work is blocked',
                'Consider closing if no longer needed',
                'Spawn subsession to continue work',
                'Move to Done if actually complete'
            ]
        else:
            return [
                'Review what was last done',
                'Identify next steps',
                'Check for blockers'
            ]

    elif issue['type'] == 'missing_pr':
        return [
            'Create PR via subsession',
            'Review commits: git log main..branch',
            'Check if implementation is complete',
            'Verify tests pass'
        ]

    elif issue['type'] == 'ci_failure':
        return [
            'Review CI logs',
            'Run tests locally',
            'Fix failing tests',
            'Update dependencies if needed'
        ]

    else:
        return ['Review and assess']


def escalate_to_daily_log(escalations: List[Dict]) -> None:
    """Write escalations to today's memory log"""

    if not escalations:
        return

    today = datetime.now().strftime('%Y-%m-%d')
    log_file = WORKSPACE_ROOT / 'memory' / f'{today}.md'

    # Group by level
    by_level = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }

    for esc in escalations:
        level = esc.get('level', 'medium')
        by_level[level].append(esc)

    # Build content
    timestamp = datetime.now().strftime('%H:%M')
    content = f"\n### Heartbeat Escalations - {timestamp}\n\n"

    if by_level['critical']:
        content += "#### 🚨 CRITICAL\n\n"
        for esc in by_level['critical']:
            content += f"- {esc['message']}\n"
            if esc.get('actions_suggested'):
                content += f"  **Actions:** {', '.join(esc['actions_suggested'])}\n"
        content += "\n"

    if by_level['high']:
        content += "#### ⚠️  HIGH PRIORITY\n\n"
        for esc in by_level['high']:
            content += f"- {esc['message']}\n"
            if esc.get('actions_suggested'):
                content += f"  **Suggested:** {', '.join(esc['actions_suggested'][:3])}\n"
        content += "\n"

    if by_level['medium']:
        content += "#### ℹ️  MEDIUM PRIORITY\n\n"
        for esc in by_level['medium']:
            content += f"- {esc['message']}\n"
        content += "\n"

    if by_level['low']:
        content += "#### 📝 LOW PRIORITY\n\n"
        for esc in by_level['low']:
            content += f"- {esc['message']}\n"
        content += "\n"

    # Append to daily log
    with open(log_file, 'a') as f:
        f.write(content)

    print(f"✓ Escalations logged to {log_file}")


def escalate_to_slack(escalations: List[Dict], webhook_url: str) -> None:
    """Send critical escalations to Slack (if configured)"""

    critical = [e for e in escalations if e['level'] == 'critical']

    if not critical:
        return

    # Would implement Slack webhook here
    print(f"ℹ️  Would send {len(critical)} critical alerts to Slack")


if __name__ == "__main__":
    # Test with sample data
    sample_issues = {
        'stale_work': [
            {
                'worktree_id': 'test-123',
                'name': 'feature-oauth',
                'age_days': 15,
                'severity': 'high'
            }
        ],
        'missing_prs': [
            {
                'worktree_id': 'test-456',
                'name': 'fix-login-bug',
                'age_days': 3
            }
        ]
    }

    config = {
        'escalation': {
            'daily_log_enabled': True,
            'slack_enabled': False
        }
    }

    escalations = evaluate_escalations(sample_issues, config)
    print(f"Generated {len(escalations)} escalations")

    for esc in escalations:
        print(f"  {esc['level']}: {esc['message']}")
