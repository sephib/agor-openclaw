#!/usr/bin/env python3
"""
Generate List Sessions - One Session Per Trello List

Architecture:
- One session per Trello list (not per card)
- Each session manages ALL cards in its list
- DuckDB tracks list_id → session_id

This script:
1. Fetches all lists from Trello board
2. Fetches all active cards grouped by list
3. Checks DuckDB for existing list sessions
4. Generates actions: CREATE (new lists) or UPDATE (existing lists)
5. Outputs: memory/list-sessions-{timestamp}.json
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from trello_sync import load_credentials, api_request, has_label, WORKSPACE_ROOT
from session_db import SessionDB

# Configuration
BOARD_ID = "5af14633e01cb0c5e1df9df6"  # B.Berry Projects


def fetch_lists(creds: Dict) -> List[Dict]:
    """Fetch all lists from board"""
    url = f"/1/boards/{BOARD_ID}/lists?fields=id,name,pos,closed"
    lists = api_request(url, creds)

    # Filter out closed/archived lists
    active_lists = [l for l in lists if not l.get('closed', False)]

    # Sort by position
    active_lists.sort(key=lambda x: x.get('pos', 0))

    return active_lists


def fetch_cards_by_list(creds: Dict) -> Dict[str, List[Dict]]:
    """
    Fetch all active cards grouped by list

    Returns:
        Dict[list_id, List[card_dict]]
    """
    url = f"/1/boards/{BOARD_ID}/cards?fields=id,name,desc,url,dateLastActivity,labels,due,idList&members=false&attachments=false"
    all_cards = api_request(url, creds)

    # Filter out archived and done cards
    active_cards = [
        card for card in all_cards
        if not card.get('closed', False)
        and not has_label(card, 'done')
    ]

    # Group by list
    cards_by_list = {}
    for card in active_cards:
        list_id = card.get('idList')
        if list_id:
            if list_id not in cards_by_list:
                cards_by_list[list_id] = []
            cards_by_list[list_id].append(card)

    return cards_by_list


def calculate_priority(card: Dict) -> int:
    """Calculate priority score for a card (same logic as process_trello_tickets.py)"""
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


def check_list_changes(list_id: str, current_cards: List[Dict], creds: Dict) -> bool:
    """
    Check if list has changes since last check

    For now, simple heuristic: check if any card has recent activity
    Returns True if changes detected
    """
    recent_threshold = datetime.now(timezone.utc) - timedelta(hours=4)  # Since last run

    for card in current_cards:
        try:
            last_activity = datetime.fromisoformat(card.get('dateLastActivity', '').replace('Z', '+00:00'))
            if last_activity > recent_threshold:
                return True  # Recent activity detected
        except:
            pass

    # Also check for new comments (fetch from API)
    # This is optional - could make API call per card to check comments
    # For now, rely on dateLastActivity

    return False


def sanitize_worktree_name(list_name: str) -> str:
    """Convert list name to valid worktree name"""
    import re
    # Remove special characters, replace spaces with hyphens
    clean = re.sub(r'[^\w\s-]', '', list_name)
    clean = re.sub(r'[-\s]+', '-', clean)
    return f"trello-list-{clean.lower()[:30]}"


def generate_list_sessions(creds: Dict) -> Dict:
    """
    Generate list worktree and session actions

    Returns:
        Dict with list worktree/session data and actions
    """
    lists = fetch_lists(creds)
    cards_by_list = fetch_cards_by_list(creds)

    # Connect to DuckDB
    db = SessionDB()

    # Get all existing list sessions from DuckDB
    existing_sessions = db.get_all_active_sessions()
    existing_list_ids = {s['card_id'] for s in existing_sessions if s.get('category') == 'list-manager'}

    # Track which list_ids are still active
    active_list_ids = {l['id'] for l in lists if l['id'] in cards_by_list and cards_by_list[l['id']]}

    # Find orphaned sessions (lists that were deleted or became empty)
    orphaned_list_ids = existing_list_ids - active_list_ids

    # Generate actions for each list
    list_actions = []
    archive_actions = []

    # Handle orphaned sessions first
    if orphaned_list_ids:
        for list_id in orphaned_list_ids:
            session = db.get_session(list_id)
            if session:
                archive_actions.append({
                    'list_id': list_id,
                    'list_name': session['title'].replace('List: ', ''),
                    'action': 'archive',
                    'session_id': session['session_id'],
                    'reason': 'List deleted or empty'
                })

    for list_info in lists:
        list_id = list_info['id']
        list_name = list_info['name']

        # Get cards in this list
        cards = cards_by_list.get(list_id, [])
        if not cards:
            continue

        # Check if list already has a session (use list_id as card_id)
        if db.has_session(list_id):
            # UPDATE existing session
            session = db.get_session(list_id)
            session_id = session['session_id']

            # Check if list has changes
            has_changes = check_list_changes(list_id, cards, creds)

            # Prepare card data
            card_data = []
            for card in cards:
                priority = calculate_priority(card)
                card_data.append({
                    'card_id': card['id'],
                    'title': card['name'],
                    'description': card.get('desc', ''),
                    'url': card['url'],
                    'priority': priority,
                    'priority_reasoning': 'calculated based on due date, labels, activity',
                    'labels': [l.get('name', '') for l in card.get('labels', [])],
                    'due_date': card.get('due'),
                    'last_activity': card.get('dateLastActivity')
                })

            # Sort by priority
            card_data.sort(key=lambda x: x['priority'], reverse=True)

            # Get worktree_id from session metadata if available
            worktree_id = None
            try:
                # Session metadata might contain worktree_id
                # For now, we'll need to query it from Agor MCP
                # This will be populated by orchestrator
                pass
            except:
                pass

            # For UPDATE: check which cards need session updates vs creates
            # This will be determined by DuckDB card_id lookup
            list_actions.append({
                'list_id': list_id,
                'list_name': list_name,
                'worktree_name': sanitize_worktree_name(list_name),
                'action': 'update',  # Worktree exists
                'worktree_id': worktree_id,  # Will be determined by orchestrator
                'cards': card_data,
                'has_changes': has_changes
            })

        else:
            # CREATE new session
            # Prepare card data
            card_data = []
            for card in cards:
                priority = calculate_priority(card)
                card_data.append({
                    'card_id': card['id'],
                    'title': card['name'],
                    'description': card.get('desc', ''),
                    'url': card['url'],
                    'priority': priority,
                    'priority_reasoning': 'calculated based on due date, labels, activity',
                    'labels': [l.get('name', '') for l in card.get('labels', [])],
                    'due_date': card.get('due'),
                    'last_activity': card.get('dateLastActivity'),
                    'category': 'general'  # Could categorize based on labels
                })

            # Sort by priority
            card_data.sort(key=lambda x: x['priority'], reverse=True)

            list_actions.append({
                'list_id': list_id,
                'list_name': list_name,
                'worktree_name': sanitize_worktree_name(list_name),
                'action': 'create',
                'cards': card_data
            })

    db.close()

    # Build output
    output = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'board_id': BOARD_ID,
        'lists': list_actions,
        'archives': archive_actions,
        'stats': {
            'total_lists': len(lists),
            'lists_with_cards': len(cards_by_list),
            'lists_to_process': len(list_actions),
            'updates': len([a for a in list_actions if a['action'] == 'update']),
            'creates': len([a for a in list_actions if a['action'] == 'create']),
            'archives': len(archive_actions),
            'orphaned_sessions': len(orphaned_list_ids)
        }
    }

    return output


def main():
    """Main execution"""
    try:
        creds = load_credentials()
        list_sessions = generate_list_sessions(creds)

        # Save to file
        output_file = WORKSPACE_ROOT / "memory" / f"list-sessions-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(list_sessions, f, indent=2)

        s = list_sessions['stats']
        print(f"Generated {output_file.name}: {s['lists_to_process']} lists, {s['creates']} creates, {s['updates']} updates, {s['archives']} archives")
        return 0

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
