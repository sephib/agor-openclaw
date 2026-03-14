#!/usr/bin/env python3
"""
Trello Ticket Processor - Automated Ticket Processing

Fetches Trello tickets, categorizes them, and provides execution plan
for Agor agent to delegate work to appropriate workers.
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

# Reuse trello_sync's API functions
sys.path.insert(0, str(Path(__file__).parent))
from trello_sync import (
    load_credentials,
    api_request,
    has_label,
    get_label_id_from_card,
    WORKSPACE_ROOT
)

# Configuration
BOARD_ID = "5af14633e01cb0c5e1df9df6"  # B.Berry Projects
MAX_CODING_WORKTREES = 3
MAX_RESEARCH_SESSIONS = 2
MAX_TICKETS_PER_RUN = 5

# Categorization keywords
CODING_KEYWORDS = [
    "implement", "fix", "refactor", "bug", "feature", "develop",
    "code", "build", "deploy", "api", "database", "test"
]

RESEARCH_KEYWORDS = [
    "investigate", "explore", "analyze", "research", "evaluate",
    "compare", "study", "review", "assess", "document"
]

WAITING_KEYWORDS = [
    "waiting for", "blocked by", "pending", "on hold"
]


def fetch_active_cards(creds: Dict) -> List[Dict]:
    """Fetch all active (non-archived, non-done) cards from board"""
    url = f"/1/boards/{BOARD_ID}/cards?fields=id,name,desc,url,dateLastActivity,labels,due,idList&members=false&attachments=false"
    all_cards = api_request(url, creds)

    # Filter out archived and done cards
    active_cards = [
        card for card in all_cards
        if not card.get('closed', False)
        and not has_label(card, 'done')
    ]

    return active_cards


def categorize_card(card: Dict) -> str:
    """
    Categorize card into: coding, research, personal, waiting

    Returns:
        str: Category name
    """
    title = card.get('name', '').lower()
    description = card.get('desc', '').lower()
    labels = [label.get('name', '').lower() for label in card.get('labels', [])]

    # Check labels first (most explicit)
    if 'code' in labels or 'coding' in labels or 'bug' in labels:
        return 'coding'

    if 'research' in labels or 'investigation' in labels:
        return 'research'

    if 'blocked' in labels or 'waiting' in labels:
        return 'waiting'

    # Check content for keywords
    text = f"{title} {description}"

    # Waiting/blocked takes precedence
    if any(keyword in text for keyword in WAITING_KEYWORDS):
        return 'waiting'

    # Coding detection
    if any(keyword in text for keyword in CODING_KEYWORDS):
        return 'coding'

    # Research detection
    if any(keyword in text for keyword in RESEARCH_KEYWORDS):
        return 'research'

    # Question marks suggest research
    if '?' in title:
        return 'research'

    # Default to personal
    return 'personal'


def calculate_priority_score(card: Dict) -> Tuple[int, str]:
    """
    Calculate priority score for a card.

    Higher score = higher priority

    Returns:
        Tuple[int, str]: (score, reasoning)
    """
    score = 0
    reasons = []

    # Label-based scoring
    if has_label(card, 'urgent'):
        score += 100
        reasons.append("urgent label")

    if has_label(card, 'active'):
        score += 50
        reasons.append("already active")

    # Due date scoring
    due = card.get('due')
    if due:
        due_date = datetime.fromisoformat(due.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        hours_until_due = (due_date - now).total_seconds() / 3600

        if hours_until_due < 0:
            score += 200  # Overdue!
            reasons.append("OVERDUE")
        elif hours_until_due < 24:
            score += 80
            reasons.append("due within 24h")
        elif hours_until_due < 48:
            score += 40
            reasons.append("due within 48h")
        elif hours_until_due < 168:  # 1 week
            score += 20
            reasons.append("due this week")

    # Recent activity (engagement signal)
    last_activity = card.get('dateLastActivity')
    if last_activity:
        activity_date = datetime.fromisoformat(last_activity.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        hours_since_activity = (now - activity_date).total_seconds() / 3600

        if hours_since_activity < 24:
            score += 15
            reasons.append("active today")
        elif hours_since_activity < 168:  # 1 week
            score += 5
            reasons.append("active this week")

    # Backlog label (lower priority)
    if has_label(card, 'backlog'):
        score -= 10
        reasons.append("in backlog")

    reasoning = ", ".join(reasons) if reasons else "default priority"
    return score, reasoning


def prioritize_cards(cards: List[Dict]) -> List[Tuple[Dict, int, str]]:
    """
    Prioritize cards by scoring.

    Returns:
        List of (card, score, reasoning) tuples, sorted by score descending
    """
    scored_cards = []
    for card in cards:
        score, reasoning = calculate_priority_score(card)
        scored_cards.append((card, score, reasoning))

    # Sort by score descending
    scored_cards.sort(key=lambda x: x[1], reverse=True)

    return scored_cards


def get_list_name(creds: Dict, list_id: str) -> str:
    """Get list name from Trello API"""
    try:
        url = f"/1/lists/{list_id}?fields=name"
        result = api_request(url, creds)
        return result.get('name', 'Unknown')
    except:
        return 'Unknown'


def generate_execution_plan(cards: List[Dict], creds: Dict) -> Dict:
    """
    Generate execution plan for top priority cards.

    Returns:
        Dict with categorized tasks and execution instructions
    """
    # Prioritize all cards
    prioritized = prioritize_cards(cards)

    # Take top N
    top_cards = prioritized[:MAX_TICKETS_PER_RUN]

    # Categorize top cards
    plan = {
        'coding_tasks': [],
        'research_tasks': [],
        'personal_tasks': [],
        'waiting_tasks': [],
        'stats': {
            'total_active_cards': len(cards),
            'processed': 0,
            'skipped': 0
        }
    }

    for card, score, reasoning in top_cards:
        category = categorize_card(card)
        list_name = get_list_name(creds, card['idList'])

        task_info = {
            'card_id': card['id'],
            'title': card['name'],
            'description': card.get('desc', ''),
            'url': card['url'],
            'list_name': list_name,
            'labels': [label.get('name', '') for label in card.get('labels', [])],
            'due_date': card.get('due'),
            'priority_score': score,
            'priority_reasoning': reasoning,
            'category': category
        }

        if category == 'coding':
            if len(plan['coding_tasks']) < MAX_CODING_WORKTREES:
                plan['coding_tasks'].append(task_info)
                plan['stats']['processed'] += 1
            else:
                plan['stats']['skipped'] += 1

        elif category == 'research':
            if len(plan['research_tasks']) < MAX_RESEARCH_SESSIONS:
                plan['research_tasks'].append(task_info)
                plan['stats']['processed'] += 1
            else:
                plan['stats']['skipped'] += 1

        elif category == 'personal':
            plan['personal_tasks'].append(task_info)
            plan['stats']['processed'] += 1

        elif category == 'waiting':
            plan['waiting_tasks'].append(task_info)
            # Don't count as processed (skipped)

    return plan


def format_plan_for_agent(plan: Dict) -> str:
    """Format execution plan as markdown for agent consumption"""

    output = "# Trello Ticket Processing Plan\n\n"
    output += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    output += "## Summary\n\n"
    output += f"- **Total active cards:** {plan['stats']['total_active_cards']}\n"
    output += f"- **To process:** {plan['stats']['processed']}\n"
    output += f"- **Skipped:** {plan['stats']['skipped']}\n\n"

    # Coding tasks
    if plan['coding_tasks']:
        output += f"## Coding Tasks ({len(plan['coding_tasks'])})\n\n"
        output += "**Action:** Create isolated worktree + session for each\n\n"

        for i, task in enumerate(plan['coding_tasks'], 1):
            output += f"### {i}. {task['title']}\n\n"
            output += f"- **Priority:** {task['priority_score']} ({task['priority_reasoning']})\n"
            output += f"- **List:** {task['list_name']}\n"
            output += f"- **Labels:** {', '.join(task['labels']) if task['labels'] else 'None'}\n"
            output += f"- **Due:** {task['due_date'] if task['due_date'] else 'None'}\n"
            output += f"- **URL:** {task['url']}\n\n"

            if task['description']:
                output += f"**Description:**\n{task['description'][:200]}{'...' if len(task['description']) > 200 else ''}\n\n"

            output += f"**Execution:**\n"
            output += f"```bash\n"
            output += f"# 1. Create worktree\n"
            output += f"worktree_name='ticket-{task['card_id'][:8]}'\n"
            output += f"agor worktrees create --name $worktree_name --board-id <MAIN_BOARD_ID>\n\n"
            output += f"# 2. Create session\n"
            output += f"agor sessions create --worktree-id <worktree_id> \\\n"
            output += f"  --prompt 'Implement: {task['title']}'\n\n"
            output += f"# 3. Update Trello\n"
            output += f"# Add comment with worktree link\n"
            output += f"```\n\n"

    # Research tasks
    if plan['research_tasks']:
        output += f"## Research Tasks ({len(plan['research_tasks'])})\n\n"
        output += "**Action:** Spawn subsession for investigation\n\n"

        for i, task in enumerate(plan['research_tasks'], 1):
            output += f"### {i}. {task['title']}\n\n"
            output += f"- **Priority:** {task['priority_score']} ({task['priority_reasoning']})\n"
            output += f"- **List:** {task['list_name']}\n"
            output += f"- **URL:** {task['url']}\n\n"

            output += f"**Execution:**\n"
            output += f"```bash\n"
            output += f"# Spawn research subsession\n"
            output += f"agor sessions spawn --prompt 'Research: {task['title']}'\n"
            output += f"```\n\n"

    # Personal tasks
    if plan['personal_tasks']:
        output += f"## Personal Tasks ({len(plan['personal_tasks'])})\n\n"
        output += "**Action:** Update local tracking only (no automation)\n\n"

        for i, task in enumerate(plan['personal_tasks'], 1):
            output += f"{i}. **{task['title']}** ({task['list_name']})\n"

        output += "\n"

    # Waiting tasks
    if plan['waiting_tasks']:
        output += f"## Waiting/Blocked Tasks ({len(plan['waiting_tasks'])})\n\n"
        output += "**Action:** Skip automated processing\n\n"

        for i, task in enumerate(plan['waiting_tasks'], 1):
            output += f"{i}. **{task['title']}** - {task['priority_reasoning']}\n"

        output += "\n"

    return output


def main():
    """Main execution"""
    print("=== Trello Ticket Processor ===\n")

    try:
        # Load credentials
        print("Loading Trello credentials...")
        creds = load_credentials()

        # Fetch active cards
        print(f"Fetching active cards from board {BOARD_ID}...")
        cards = fetch_active_cards(creds)
        print(f"✓ Found {len(cards)} active cards\n")

        # Generate execution plan
        print("Generating execution plan...")
        plan = generate_execution_plan(cards, creds)

        # Output plan
        plan_text = format_plan_for_agent(plan)
        print(plan_text)

        # Save to file
        output_file = WORKSPACE_ROOT / "memory" / f"trello-plan-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        with open(output_file, 'w') as f:
            f.write(plan_text)

        print(f"\n✓ Plan saved to: {output_file}")

        # Also output JSON for programmatic consumption
        json_file = output_file.with_suffix('.json')
        with open(json_file, 'w') as f:
            json.dump(plan, f, indent=2)

        print(f"✓ JSON plan saved to: {json_file}")

        return 0

    except Exception as e:
        print(f"\n✗ Processing failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
