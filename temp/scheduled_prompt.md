# Trello Ticket Processor - Scheduled Prompt

You are the orchestrator - manage existing sessions AND create new ones based on DuckDB state.

## 🔒 CRITICAL: Duplicate Prevention with DuckDB

This workflow uses DuckDB to track existing sessions and prevent duplicates.
- Existing tickets → UPDATE session (check for new comments)
- New tickets → CREATE session
- DO NOT create duplicate sessions

---

## Step 1: Run Scheduled Entry Point (DuckDB Check)

```bash
cd /Users/josephberry/.agor/worktrees/local/agor-openclaw/trello-task-processor
uv run python utils/scheduled_run.py
```

This script:
1. Fetches Trello tickets
2. Generates execution plan
3. **Checks DuckDB for existing sessions**
4. **Filters to ONLY new tickets**
5. Outputs: `memory/filtered-new-sessions-{timestamp}.json`

Also generates: `memory/trello-actions-{timestamp}.json` (full action list with updates)

---

## Step 2: Read Both Files

```bash
# Filtered new sessions (CREATE actions)
FILTERED_FILE=$(ls -t memory/filtered-new-sessions-*.json | head -1)

# Full actions (includes UPDATE actions)
ACTIONS_FILE=$(ls -t memory/trello-actions-*.json | head -1)

cat $FILTERED_FILE  # New sessions to create
cat $ACTIONS_FILE   # All actions (updates + creates)
```

---

## Step 3: Process UPDATE Actions (Existing Sessions)

**IMPORTANT:** For tickets that already have sessions, check if there are new comments or updates.

```python
import json
from pathlib import Path
import sys
sys.path.insert(0, 'utils')
from trello_sync import load_credentials, api_request

# Load actions file
actions_file = sorted(Path('memory').glob('trello-actions-*.json'))[-1]
actions_data = json.load(open(actions_file))

# Load Trello credentials
creds = load_credentials()

update_actions = [a for a in actions_data['actions'] if a['action'] == 'update']

print(f"\n{'='*70}")
print(f"PROCESSING {len(update_actions)} EXISTING SESSIONS")
print(f"{'='*70}\n")

for action in update_actions:
    card_id = action['card_id']
    session_id = action['session_id']
    title = action['title']

    print(f"Checking: {title}")
    print(f"  Session: {session_id[:8]}")
    print(f"  Card: {card_id}")

    # Fetch latest card data from Trello
    card_url = f"/1/cards/{card_id}?fields=desc,dateLastActivity&actions=commentCard&actions_limit=10"
    try:
        card_data = api_request(card_url, creds)

        # Check for recent comments (last 24 hours)
        from datetime import datetime, timedelta, timezone
        recent_threshold = datetime.now(timezone.utc) - timedelta(hours=24)

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
            print(f"  ✅ {len(recent_comments)} new comment(s) - sending update to session")

            # Send update prompt to existing session
            update_prompt = f"""
🔄 Ticket Update from Trello

**Card:** {title}
**Trello URL:** {action['task']['url']}

**New Comments ({len(recent_comments)}):**
"""
            for i, comment in enumerate(recent_comments, 1):
                update_prompt += f"\n{i}. **{comment['member']}** ({comment['date']}):\n{comment['text']}\n"

            update_prompt += f"""

**Your Actions:**
1. Review the new comments above
2. Take any requested actions
3. Update progress on Trello card
4. If work is complete, mark as done

⚠️ URL VERIFICATION:
- If posting links, verify they work with WebFetch
- No 404 links allowed (especially AliExpress)
- Test every URL before posting

**Current Task Description:**
{action['task'].get('description', 'No description')[:500]}
"""

            # Use agor.sessions.prompt to send update
            try:
                agor.sessions.prompt(
                    session_id=session_id,
                    prompt=update_prompt
                )
                print(f"  📤 Update sent to session {session_id[:8]}")
            except Exception as e:
                print(f"  ⚠️  Failed to send update: {e}")
        else:
            print(f"  ℹ️  No new comments - session still active, no update needed")

    except Exception as e:
        print(f"  ❌ Error fetching card: {e}")

    print()

print(f"{'='*70}")
print(f"UPDATE PROCESSING COMPLETE")
print(f"{'='*70}\n")
```

---

## Step 4: Process CREATE Actions (New Sessions)

```python
from utils.session_db import SessionDB

# Load filtered file (new sessions only)
filtered_file = sorted(Path('memory').glob('filtered-new-sessions-*.json'))[-1]
data = json.load(open(filtered_file))
new_sessions = data.get('new_sessions', [])

if not new_sessions:
    print("✅ No new sessions needed - all tickets already have active sessions")
else:
    print(f"\n{'='*70}")
    print(f"CREATING {len(new_sessions)} NEW SESSIONS")
    print(f"{'='*70}\n")

    # Connect to DuckDB
    db = SessionDB()

    created_sessions = []

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

        # Create session based on category
        if category == 'coding':
            session = agor.sessions.create(
                worktree_id="659dbc25-b301-4e2c-ab26-c07cd1737fcb",
                agentic_tool="claude-code",
                initial_prompt=f"""
Handle coding ticket: {title}

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
- Mark verified links: ✅ [Link](url) - Verified {date}

See skills/trello-ticket-processor.md for details.
                """
            )

        elif category == 'research':
            session = agor.sessions.create(
                worktree_id="659dbc25-b301-4e2c-ab26-c07cd1737fcb",
                agentic_tool="claude-code",
                initial_prompt=f"""
Handle research ticket: {title}

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
- Format verified links: ✅ [Product Name](url) - Verified {date}
- For broken links: ❌ Link broken - searched for alternative: [New Link](url)

Quality check before posting to Trello:
□ All links tested with WebFetch
□ All links return HTTP 200
□ No 404 errors
□ Verification date included

No worktree needed - research in this session.
                """
            )

        elif category == 'personal':
            session = agor.sessions.create(
                worktree_id="659dbc25-b301-4e2c-ab26-c07cd1737fcb",
                agentic_tool="claude-code",
                initial_prompt=f"""
Handle personal task: {title}

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
- Format: ✅ [Product - Price](verified-url) - Checked {date}
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
            )

        # CRITICAL: Track in DuckDB immediately
        db.create_session(
            card_id=card_id,
            session_id=session.session_id,
            category=category,
            title=title
        )

        created_sessions.append({
            'session_id': session.session_id,
            'ticket_title': title,
            'ticket_id': card_id,
            'category': category
        })

        print(f"✅ Created + tracked: {title} → {session.session_id[:8]}")

    db.close()

    print(f"\n✅ Created {len(created_sessions)} sessions")
    print(f"✅ All tracked in DuckDB - no duplicates will be created next run")
```

---

## Step 5: Log Summary

```python
from datetime import datetime

# Count updates and creates
actions_data = json.load(open(actions_file))
update_count = len([a for a in actions_data['actions'] if a['action'] == 'update'])
create_count = len([a for a in actions_data['actions'] if a['action'] == 'create'])

log_entry = f"""
### Trello Ticket Processing - {datetime.now().strftime('%H:%M')} (Scheduled)

**Actions file:** {actions_file.name}
**Filtered file:** {filtered_file.name}

**Summary:**
- Updates sent: {update_count} (existing sessions checked for new comments)
- New sessions created: {create_count}
- Total actions: {update_count + create_count}

**Sessions Created:**
"""

if created_sessions:
    for s in created_sessions:
        log_entry += f"- {s['category'].title()}: \"{s['ticket_title']}\" → [session {s['session_id'][:8]}](http://localhost:3030/b/openclaw-agor/{s['session_id'][:8]})\n"
else:
    log_entry += "- None (all tickets already have active sessions)\n"

log_entry += f"""
**View active tickets:** http://localhost:3030/w/659dbc25-b301-4e2c-ab26-c07cd1737fcb

**DuckDB Status:**
- Total sessions tracked: {len(db.get_all_active_sessions()) if 'db' in locals() else 'N/A'}
- All sessions persistent in: memory/agor-state/sessions.duckdb
- Next run will check for updates + create new sessions ✅

**Configuration:**
- Visibility Worktree ID: 659dbc25-b301-4e2c-ab26-c07cd1737fcb
- Repo ID: 88617156-51f9-44d1-8ba2-24897afc5da6
- Board ID: 1a508c77-dacb-46fe-ab24-e527fb476882
- Trello Board: 5af14633e01cb0c5e1df9df6
- Max coding sessions: 10 concurrent
- Max research sessions: 10 concurrent
- Max tickets per run: 10

**URL Verification:**
- All worker sessions verify links before posting
- No 404 links allowed (especially AliExpress)
- WebFetch used to test all URLs
"""

# Append to daily log
log_file = Path('memory') / f"{datetime.now().strftime('%Y-%m-%d')}.md"
with open(log_file, 'a') as f:
    f.write("\n---\n\n" + log_entry)

print(f"\n✅ Logged to {log_file}")
```

---

## Important Notes

### ✅ Dual Workflow: Updates + Creates

**UPDATE existing sessions (tickets already in DuckDB):**
1. Fetch latest Trello card data
2. Check for new comments (last 24 hours)
3. If new comments → send update prompt to existing session
4. If no changes → skip (session still active, no action needed)

**CREATE new sessions (tickets NOT in DuckDB):**
1. Check DuckDB to confirm not already tracked
2. Create session in trello-visibility-hub
3. Track in DuckDB immediately
4. Log creation

### ⚠️ URL Verification (CRITICAL)

**All worker sessions MUST verify links before posting:**

```bash
# Method 1: WebFetch tool (preferred)
WebFetch(url)  # Returns status + content

# Method 2: curl
curl -I "https://aliexpress.com/item/..." | head -1
# Expected: HTTP/1.1 200 OK
```

**Quality checklist for sessions:**
- □ All product links tested with WebFetch
- □ All links return HTTP 200
- □ No 404 errors in final Trello comments
- □ Verification date included
- □ Broken links replaced with working alternatives

**Common issues:**
- **AliExpress:** Product links expire frequently (item removed/sold out)
  - Fix: Search for current product, verify new link
- **Amazon:** Affiliate/tracking parameters break links
  - Fix: Use clean product URL (amazon.com/dp/PRODUCTID)
- **eBay:** Auction links expire when auction ends
  - Fix: Find "Buy It Now" or current listing

**Fix process:**
1. Test link with WebFetch
2. If broken (404/403), use WebSearch to find current product
3. Verify new link works
4. Add note: "✅ Link verified {date}" or "⚠️ Original link expired - found current alternative"

### ✅ Duplicate Prevention

**How it works:**
- DuckDB tracks all sessions in `memory/agor-state/sessions.duckdb`
- `scheduled_run.py` filters to ONLY new tickets
- Orchestrator receives pre-filtered list (no decision-making)
- Each session tracked in DuckDB immediately after creation
- Next run checks DuckDB first → no duplicates ✅

**Safety check before creating any session:**
```python
if db.has_session(card_id):
    print(f"⚠️ SKIP - already exists in DuckDB")
    continue
```

### ✅ Configuration

- Max coding: 10 concurrent (was 3)
- Max research: 10 concurrent (was 2)
- Max tickets per run: 10 (was 5)

### ✅ Workflow Diagram

```
scheduled_run.py
    ↓
DuckDB check
    ↓
┌──────────────┬──────────────┐
│  UPDATE      │  CREATE      │
│  (existing)  │  (new)       │
├──────────────┼──────────────┤
│ Check Trello │ Create       │
│ for comments │ session      │
│ ↓            │ ↓            │
│ If new       │ Track in     │
│ → Send       │ DuckDB       │
│   update     │              │
│ If none      │              │
│ → Skip       │              │
└──────────────┴──────────────┘
    ↓
All sessions verify URLs ✅
    ↓
No duplicates ✅
```

### ⚠️ Critical Safety Checks

1. **Before creating session:**
   ```python
   if db.has_session(card_id):
       skip()  # Already tracked
   ```

2. **Before posting links:**
   ```python
   status = WebFetch(url)
   if status != 200:
       find_alternative()
   ```

3. **After creating session:**
   ```python
   db.create_session(card_id, session_id, category, title)
   # Immediately tracked - prevents duplicates
   ```

---

## See Also

- `skills/trello-ticket-processor.md` - Full workflow documentation
- `SOLUTION-FINAL.md` - Complete duplicate prevention architecture
- `utils/scheduled_run.py` - Entry point with DuckDB filtering
- `utils/session_db.py` - DuckDB wrapper for persistence
- `utils/trello_sync.py` - Trello API helpers

---

## Key Principles

1. **Orchestrator is DUMB EXECUTOR** - Receives pre-filtered input, just executes
2. **DuckDB is SOURCE OF TRUTH** - All session tracking happens here
3. **UPDATE existing sessions** - Check Trello for new comments, send updates
4. **VERIFY ALL URLS** - No 404s allowed, especially AliExpress
5. **NO decision-making** - All filtering happens in `scheduled_run.py`

---

**Version:** 2.0 (with UPDATE support + URL verification)
**Last Updated:** 2026-03-20
**Status:** Ready for production
