#!/usr/bin/env python3
"""Create new sessions for tickets not yet in DuckDB."""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent / 'utils'))

from session_db import SessionDB

def create_new_sessions():
    """Read filtered file and return session data to create."""

    # Load filtered file (new sessions only)
    filtered_file = sorted(Path('memory').glob('filtered-new-sessions-*.json'))[-1]
    print(f"Reading new sessions from: {filtered_file}")

    with open(filtered_file) as f:
        data = json.load(f)

    new_sessions = data.get('new_sessions', [])

    if not new_sessions:
        print("✅ No new sessions needed - all tickets already have active sessions")
        return []

    print(f"\n{'='*70}")
    print(f"PREPARING {len(new_sessions)} NEW SESSIONS")
    print(f"{'='*70}\n")

    # Connect to DuckDB
    db = SessionDB()

    sessions_to_create = []

    for session_info in new_sessions:
        card_id = session_info['card_id']
        title = session_info['title']
        category = session_info['category']
        url = session_info['url']
        priority = session_info['priority']
        description = session_info['description']

        # Double-check not already in DuckDB (safety check)
        if db.has_session(card_id):
            print(f"⚠️  SKIP {title} - already has session in DuckDB")
            continue

        # Prepare session prompt based on category
        if category == 'coding':
            initial_prompt = f"""Handle coding ticket: {title}

Task Details:
- Card ID: {card_id}
- Title: {title}
- Description: {description}
- Priority: {priority}
- Trello URL: {url}

Your Job:
1. Create dedicated worktree: ticket-{card_id[:8]}
   - Use: agor.worktrees.create(
       repo_id="88617156-51f9-44d1-8ba2-24897afc5da6",
       worktree_name="ticket-{card_id[:8]}",
       board_id="1a508c77-dacb-46fe-ab24-e527fb476882",
       create_branch=True
     )

2. Create worker session in that worktree
3. Implement the feature
4. Update Trello card with progress
5. When complete, post comment on Trello card: {url}

⚠️ URL VERIFICATION REQUIRED:
- Before posting ANY links (especially AliExpress), verify they work
- Use: WebFetch(url) to check HTTP status
- If 404, find working alternative with WebSearch
- Only include verified working links in your output
- Mark verified links: ✅ [Link](url) - Verified {{date}}

See skills/trello-ticket-processor.md for details.
"""

        elif category == 'research':
            initial_prompt = f"""Handle research ticket: {title}

Task Details:
- Card ID: {card_id}
- Title: {title}
- Description: {description}
- Priority: {priority}
- Trello URL: {url}

Your Job:
1. Investigate the topic/question
2. Gather relevant information
3. Provide findings and recommendations
4. Post findings to Trello card: {url}

⚠️ URL VERIFICATION CRITICAL:
- BEFORE including ANY link in your findings, VERIFY it works
- Use WebFetch to check each URL returns HTTP 200
- Common issues:
  * AliExpress links often 404 (product removed/changed)
  * Use WebSearch to find current working alternatives
  * Test EVERY link before including it
- Format verified links: ✅ [Product Name](url) - Verified {{date}}
- For broken links: ❌ Link broken - searched for alternative: [New Link](url)

Quality check before posting to Trello:
□ All links tested with WebFetch
□ All links return HTTP 200
□ No 404 errors
□ Verification date included

No worktree needed - research in this session.
"""

        elif category == 'personal':
            initial_prompt = f"""Handle personal task: {title}

Task Details:
- Card ID: {card_id}
- Title: {title}
- Description: {description}
- Priority: {priority}
- Trello URL: {url}

Your Job:
1. Research/handle the personal task
2. Provide findings or recommendations
3. Update Trello card: {url}

⚠️ URL VERIFICATION CRITICAL FOR SHOPPING/PRODUCT LINKS:
- Test EVERY product link before posting to Trello
- Method: WebFetch(url) - check for HTTP 200 and product availability
- AliExpress links expire frequently - always verify
- If link 404s:
  1. Search for same product with WebSearch
  2. Find current working link
  3. Verify new link works
  4. Include note: "Original link expired - found current link"
- Format: ✅ [Product - Price](verified-url) - Checked {{date}}
- NEVER post unverified links - causes user frustration with 404s

Quality check before posting to Trello:
□ All links tested with WebFetch
□ All links return HTTP 200
□ Product pages load correctly
□ No 404 errors
□ Prices and availability confirmed
□ Links are NOT region-locked or temporary

Common issues to avoid:
- AliExpress: Product removed/expired → Search for current alternative
- Amazon: Affiliate/tracking links broken → Use clean product URL
- eBay: Auction ended → Find "Buy It Now" or current listing
"""

        sessions_to_create.append({
            'card_id': card_id,
            'title': title,
            'category': category,
            'url': url,
            'priority': priority,
            'initial_prompt': initial_prompt
        })

        print(f"✅ Prepared: {title} ({category})")

    db.close()

    print(f"\n{'='*70}")
    print(f"READY TO CREATE {len(sessions_to_create)} SESSIONS")
    print(f"{'='*70}\n")

    return sessions_to_create

if __name__ == '__main__':
    sessions = create_new_sessions()

    # Output as JSON for orchestrator
    output_file = Path('memory') / f'sessions-to-create-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'sessions': sessions
        }, f, indent=2)

    print(f"✅ Session creation data saved to: {output_file}")

    if sessions:
        print("\n📋 Next: Create these sessions using Agor MCP and track in DuckDB")
        for s in sessions:
            print(f"  - {s['category'].title()}: {s['title']}")
    else:
        print("\n✅ No new sessions to create")
