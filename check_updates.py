#!/usr/bin/env python3
"""Check for new comments on existing Trello cards and send updates to sessions."""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent / 'utils'))

from trello_sync import load_credentials, api_request

def check_for_updates():
    """Check each UPDATE action for new comments and prepare update prompts."""

    # Load actions file
    actions_file = sorted(Path('memory').glob('trello-actions-*.json'))[-1]
    print(f"Reading actions from: {actions_file}")

    with open(actions_file) as f:
        actions_data = json.load(f)

    # Load Trello credentials
    creds = load_credentials()

    # Filter UPDATE actions
    update_actions = [a for a in actions_data['actions'] if a['action'] == 'update']

    print(f"\n{'='*70}")
    print(f"CHECKING {len(update_actions)} EXISTING SESSIONS FOR UPDATES")
    print(f"{'='*70}\n")

    updates_to_send = []
    recent_threshold = datetime.now(timezone.utc) - timedelta(hours=24)

    for action in update_actions:
        card_id = action['card_id']
        session_id = action['session_id']
        title = action['title']
        category = action['category']
        url = action['task']['url']
        description = action['task'].get('description', '')

        print(f"Checking: {title}")
        print(f"  Session: {session_id[:8]}...")
        print(f"  Card: {card_id}")

        # Fetch latest card data from Trello (comments only)
        card_url = f"/1/cards/{card_id}?fields=dateLastActivity&actions=commentCard&actions_limit=10"

        try:
            card_data = api_request(card_url, creds)

            # Check for recent comments (last 24 hours)
            recent_comments = []
            for comment in card_data.get('actions', []):
                comment_date = datetime.fromisoformat(comment['date'].replace('Z', '+00:00'))
                if comment_date > recent_threshold:
                    recent_comments.append({
                        'text': comment['data']['text'],
                        'date': comment['date'],
                        'member': comment.get('memberCreator', {}).get('fullName', 'Unknown')
                    })

            if recent_comments:
                print(f"  ✅ {len(recent_comments)} new comment(s) found")

                # Prepare update prompt
                update_prompt = f"""🔄 Ticket Update from Trello

**Card:** {title}
**Trello URL:** {url}
**Category:** {category}

**New Comments ({len(recent_comments)}):**
"""
                for i, comment in enumerate(recent_comments, 1):
                    update_prompt += f"\n{i}. **{comment['member']}** ({comment['date']}):\n{comment['text']}\n"

                update_prompt += f"""

**Your Actions:**
1. Review the new comments above
2. Take any requested actions
3. Update progress on Trello card
4. If work is complete, mark ticket as done

⚠️ URL VERIFICATION:
- If posting links, verify they work with WebFetch
- No 404 links allowed (especially AliExpress)
- Test every URL before posting

**Current Task Description (first 500 chars):**
{description[:500]}...
"""

                updates_to_send.append({
                    'session_id': session_id,
                    'title': title,
                    'prompt': update_prompt
                })
            else:
                print(f"  ℹ️  No new comments - session still active, no update needed")

        except Exception as e:
            print(f"  ❌ Error fetching card: {e}")

        print()

    print(f"{'='*70}")
    print(f"UPDATE CHECK COMPLETE")
    print(f"  Sessions checked: {len(update_actions)}")
    print(f"  Updates to send: {len(updates_to_send)}")
    print(f"{'='*70}\n")

    return updates_to_send

if __name__ == '__main__':
    updates = check_for_updates()

    # Output updates as JSON for orchestrator to process
    output_file = Path('memory') / f'updates-to-send-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'updates': updates
        }, f, indent=2)

    print(f"✅ Updates saved to: {output_file}")

    if updates:
        print("\n📤 Send these updates using Agor MCP:")
        for u in updates:
            print(f"  - Session {u['session_id'][:8]}: {u['title']}")
    else:
        print("\n✅ No updates needed - all sessions are current")
