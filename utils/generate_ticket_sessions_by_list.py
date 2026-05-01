#!/usr/bin/env python3
"""
Generate Ticket Sessions Grouped By List

Architecture:
- One WORKTREE per Trello list
- One SESSION per ticket/card (within the list's worktree)

This script:
1. Fetches all lists and cards from Trello
2. Groups cards by list
3. For each list:
   - Determines if worktree exists
   - For each card: determines if session exists
4. Outputs actions for orchestrator
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List
import re

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from trello_sync import load_credentials, api_request, has_label, WORKSPACE_ROOT
from session_db import SessionDB

# Configuration
BOARD_ID = "5af14633e01cb0c5e1df9df6"  # B.Berry Projects


def sanitize_worktree_name(list_name: str) -> str:
    """Convert list name to valid worktree name (ASCII only)"""
    # Keep only ASCII letters, numbers, spaces, and hyphens
    clean = re.sub(r'[^a-zA-Z0-9\s-]', '', list_name)
    # Replace spaces with hyphens
    clean = re.sub(r'[-\s]+', '-', clean)
    # Remove leading/trailing hyphens
    clean = clean.strip('-')
    # If empty after sanitization, use a hash of original name
    if not clean:
        import hashlib
        clean = hashlib.md5(list_name.encode()).hexdigest()[:8]
    return f"trello-list-{clean.lower()[:30]}"


def fetch_lists(creds: Dict) -> List[Dict]:
    """Fetch all lists from board"""
    url = f"/1/boards/{BOARD_ID}/lists?fields=id,name,pos,closed"
    lists = api_request(url, creds)
    active_lists = [l for l in lists if not l.get('closed', False)]
    active_lists.sort(key=lambda x: x.get('pos', 0))
    return active_lists


def fetch_cards_by_list(creds: Dict) -> Dict[str, List[Dict]]:
    """Fetch all active cards grouped by list"""
    url = f"/1/boards/{BOARD_ID}/cards?fields=id,name,desc,url,dateLastActivity,labels,due,idList&members=false&attachments=false"
    all_cards = api_request(url, creds)

    active_cards = [
        card for card in all_cards
        if not card.get('closed', False)
        and not has_label(card, 'done')
        and not has_label(card, 'skip')
    ]

    cards_by_list = {}
    for card in active_cards:
        list_id = card.get('idList')
        if list_id:
            if list_id not in cards_by_list:
                cards_by_list[list_id] = []
            cards_by_list[list_id].append(card)

    return cards_by_list


def calculate_priority(card: Dict) -> int:
    """Calculate priority score for a card"""
    score = 0

    # Due date urgency
    if card.get('due'):
        try:
            due_date = datetime.fromisoformat(card['due'].replace('Z', '+00:00'))
            now = datetime.now(timezone.utc)
            days_until_due = (due_date - now).days

            if days_until_due < 0:
                score += 100  # Overdue
            elif days_until_due <= 1:
                score += 50
            elif days_until_due <= 7:
                score += 20
            elif days_until_due <= 30:
                score += 10
        except:
            pass

    # Label-based priority
    labels = [label.get('name', '').lower() for label in card.get('labels', [])]
    if 'urgent' in labels or 'high' in labels:
        score += 30
    if 'active' in labels:
        score += 15

    # Recent activity
    try:
        last_activity = datetime.fromisoformat(card.get('dateLastActivity', '').replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        days_since_activity = (now - last_activity).days

        if days_since_activity <= 1:
            score += 15  # Active today
        elif days_since_activity <= 7:
            score += 5  # Active this week
    except:
        pass

    return score


def categorize_card(card: Dict) -> str:
    """Categorize card into: coding, research, personal"""
    title = card.get('name', '').lower()
    description = card.get('desc', '').lower()
    labels = [label.get('name', '').lower() for label in card.get('labels', [])]

    # Check labels first
    if 'code' in labels or 'coding' in labels or 'bug' in labels:
        return 'coding'
    if 'research' in labels or 'investigation' in labels:
        return 'research'

    # Check title/description for coding keywords
    coding_keywords = ['implement', 'fix', 'refactor', 'bug', 'feature', 'code', 'build', 'deploy']
    if any(kw in title or kw in description for kw in coding_keywords):
        return 'coding'

    # Check for research keywords
    research_keywords = ['investigate', 'explore', 'analyze', 'research', 'study']
    if any(kw in title or kw in description for kw in research_keywords):
        return 'research'

    return 'personal'


def generate_actions(creds: Dict) -> Dict:
    """Generate actions for worktrees and sessions"""
    lists = fetch_lists(creds)
    cards_by_list = fetch_cards_by_list(creds)

    # Connect to DuckDB
    db = SessionDB()

    # Get all existing card sessions
    existing_sessions = db.get_all_active_sessions()
    existing_card_ids = {s['card_id']: s for s in existing_sessions if s.get('category') != 'list-worktree'}

    # Detect deleted cards: in DB but no longer on board
    all_current_card_ids = {card['id'] for cards in cards_by_list.values() for card in cards}
    deleted_card_ids = set(existing_card_ids.keys()) - all_current_card_ids
    deleted_cards = []
    for card_id in deleted_card_ids:
        session = existing_card_ids[card_id]
        db.archive_session(card_id)
        deleted_cards.append({'card_id': card_id, 'session_id': session['session_id'], 'title': session.get('title', '')})

    # Generate actions
    list_actions = []
    stats = {
        'worktrees_to_create': 0,
        'worktrees_existing': 0,
        'sessions_to_create': 0,
        'sessions_to_update': 0,
        'total_cards': 0,
        'sessions_archived': len(deleted_cards)
    }

    for list_info in lists:
        list_id = list_info['id']
        list_name = list_info['name']
        worktree_name = sanitize_worktree_name(list_name)

        # Get cards in this list
        cards = cards_by_list.get(list_id, [])
        if not cards:
            continue

        # Check if any card in this list has a session (implies worktree exists)
        has_worktree = any(card['id'] in existing_card_ids for card in cards)
        worktree_action = 'exists' if has_worktree else 'create'

        if worktree_action == 'create':
            stats['worktrees_to_create'] += 1
        else:
            stats['worktrees_existing'] += 1

        # Process each card
        card_actions = []
        for card in cards:
            card_id = card['id']
            card_title = card['name']
            priority = calculate_priority(card)
            category = categorize_card(card)

            # Check if card has existing session
            if card_id in existing_card_ids:
                # UPDATE existing session
                existing = existing_card_ids[card_id]
                card_actions.append({
                    'card_id': card_id,
                    'title': card_title,
                    'action': 'update',
                    'session_id': existing['session_id'],
                    'priority': priority,
                    'category': category,
                    'description': card.get('desc', ''),
                    'url': card['url'],
                    'labels': [l.get('name', '') for l in card.get('labels', [])],
                    'due_date': card.get('due')
                })
                stats['sessions_to_update'] += 1
            else:
                # CREATE new session
                card_actions.append({
                    'card_id': card_id,
                    'title': card_title,
                    'action': 'create',
                    'priority': priority,
                    'category': category,
                    'description': card.get('desc', ''),
                    'url': card['url'],
                    'labels': [l.get('name', '') for l in card.get('labels', [])],
                    'due_date': card.get('due')
                })
                stats['sessions_to_create'] += 1

        stats['total_cards'] += len(cards)

        # Sort cards by priority
        card_actions.sort(key=lambda x: x['priority'], reverse=True)

        list_actions.append({
            'list_id': list_id,
            'list_name': list_name,
            'worktree_name': worktree_name,
            'worktree_action': worktree_action,
            'cards': card_actions
        })

    db.close()

    # Build output
    output = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'board_id': BOARD_ID,
        'lists': list_actions,
        'deleted_cards': deleted_cards,
        'stats': stats
    }

    return output


def main():
    """Main execution"""
    try:
        creds = load_credentials()
        actions = generate_actions(creds)

        # Save to file
        output_file = WORKSPACE_ROOT / "memory" / f"ticket-sessions-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(actions, f, indent=2)

        s = actions['stats']
        archived = f", {s['sessions_archived']} archived" if s['sessions_archived'] else ""
        print(f"Generated {output_file.name}: {s['total_cards']} cards, {s['sessions_to_create']} creates, {s['sessions_to_update']} updates, {s['worktrees_to_create']} new worktrees{archived}")
        return 0

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
