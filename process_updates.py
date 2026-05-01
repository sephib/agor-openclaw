#!/usr/bin/env python3
"""
Process UPDATE actions - check for new comments and send updates to existing sessions.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent / 'utils'))

from trello_sync import load_credentials, api_request

def check_for_updates():
    """Check each existing session for new Trello comments and send updates."""

    # Load actions file
    actions_file = sorted(Path('memory').glob('trello-actions-*.json'))[-1]
    print(f"\n{'='*70}")
    print(f"PROCESSING TRELLO UPDATES")
    print(f"{'='*70}\n")
    print(f"Actions file: {actions_file.name}\n")

    actions_data = json.load(open(actions_file))
    update_actions = [a for a in actions_data['actions'] if a['action'] == 'update']

    if not update_actions:
        print("✅ No update actions needed")
        return []

    print(f"Found {len(update_actions)} existing sessions to check\n")

    # Load Trello credentials
    creds = load_credentials()

    # Track updates to send
    updates_to_send = []
    recent_threshold = datetime.now(timezone.utc) - timedelta(hours=24)

    for i, action in enumerate(update_actions, 1):
        card_id = action['card_id']
        session_id = action['session_id']
        title = action['title']
        category = action['category']
        url = action['task']['url']
        description = action['task'].get('description', 'No description')[:500]

        print(f"{i}. Checking: {title}")
        print(f"   Session: {session_id[:8]}...")
        print(f"   Category: {category}")

        # Fetch latest card data from Trello
        card_url = f"/1/cards/{card_id}?fields=desc,dateLastActivity&actions=commentCard&actions_limit=10"

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
                print(f"   ✅ {len(recent_comments)} new comment(s) found")

                # Build update prompt
                update_prompt = f"""🔄 Ticket Update from Trello

**Card:** {title}
**Trello URL:** {url}
**Category:** {category}

**New Comments ({len(recent_comments)}):**
"""
                for j, comment in enumerate(recent_comments, 1):
                    update_prompt += f"\n{j}. **{comment['member']}** ({comment['date']}):\n{comment['text']}\n"

                update_prompt += f"""

**Your Actions:**
1. Review the new comments above
2. Take any requested actions
3. Update progress on Trello card
4. If work is complete, mark as done

⚠️ URL VERIFICATION CRITICAL:
- Before posting ANY links (especially AliExpress), verify they work
- Use WebFetch to check each URL returns HTTP 200
- If link 404s, find working alternative with WebSearch
- Format verified links: ✅ [Product Name](url) - Verified {{date}}
- NO unverified links allowed

**Current Task Description:**
{description}...
"""

                updates_to_send.append({
                    'session_id': session_id,
                    'title': title,
                    'prompt': update_prompt,
                    'comment_count': len(recent_comments)
                })

            else:
                print(f"   ℹ️  No new comments - session still active, no update needed")

        except Exception as e:
            print(f"   ❌ Error fetching card: {e}")

        print()

    return updates_to_send

if __name__ == '__main__':
    updates = check_for_updates()

    # Save updates to send
    if updates:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        output_file = Path('memory') / f'updates-to-send-{timestamp}.json'

        with open(output_file, 'w') as f:
            json.dump({
                'generated_at': datetime.now(timezone.utc).isoformat(),
                'update_count': len(updates),
                'updates': updates
            }, f, indent=2)

        print(f"\n{'='*70}")
        print(f"SUMMARY")
        print(f"{'='*70}\n")
        print(f"Updates to send: {len(updates)}")
        print(f"Saved to: {output_file.name}\n")

        print("Next steps:")
        print("1. Use Agor MCP to send prompts to each session")
        print("2. Log results to daily memory\n")
    else:
        print(f"\n{'='*70}")
        print(f"✅ NO UPDATES NEEDED")
        print(f"{'='*70}\n")
        print("All sessions are up-to-date. No new comments found.\n")
