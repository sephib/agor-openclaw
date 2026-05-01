# Trello Ticket Processor - Hybrid Architecture

**One worktree per list** + **One session per ticket**

## 🎯 Architecture

```
Worktree: trello-list-shopping
├─ Session: Buy o-ring (ticket 1)
├─ Session: USB-C cable (ticket 2)
└─ Session: Product X (ticket 3)

Worktree: trello-list-development
├─ Session: Implement feature Y
└─ Session: Fix bug Z
```

**Benefits:**
- Visual organization by list (worktrees on board)
- Full context per ticket (dedicated sessions)
- Complete isolation between tickets
- Easy to see progress by category

---

## Step 1: Generate Actions

```bash
uv run python utils/generate_ticket_sessions_by_list.py
```

Outputs: `memory/ticket-sessions-{timestamp}.json`

---

## Step 2: Process Actions

```python
import json
from pathlib import Path
import sys
sys.path.insert(0, 'utils')
from session_db import SessionDB

# Load actions file
actions_file = sorted(Path('memory').glob('ticket-sessions-*.json'))[-1]
data = json.load(open(actions_file))

print(f"Processing {actions_file.name}: {len(data['lists'])} lists, {data['stats']['total_cards']} cards")

# Connect to DuckDB
db = SessionDB()

# Archive Agor sessions for deleted Trello cards
for deleted in data.get('deleted_cards', []):
    try:
        agor.sessions.archive(session_id=deleted['session_id'])
    except Exception as e:
        print(f"ERROR archiving session {deleted['session_id'][:8]} ({deleted['title']}): {e}")

# Track created worktrees and sessions
worktrees_created = {}  # list_id → worktree_id
sessions_created = []
sessions_updated = []

for list_info in data['lists']:
    list_id = list_info['list_id']
    list_name = list_info['list_name']
    worktree_name = list_info['worktree_name']
    worktree_action = list_info['worktree_action']
    cards = list_info['cards']

    # STEP 1: Ensure worktree exists
    worktree_id = None

    if worktree_action == 'create':
        try:
            worktree = agor.worktrees.create(
                repo_id="88617156-51f9-44d1-8ba2-24897afc5da6",
                worktree_name=worktree_name,
                board_id="1a508c77-dacb-46fe-ab24-e527fb476882",
                create_branch=True,
                notes=f"Trello List: {list_name} ({len(cards)} cards)"
            )
            worktree_id = worktree.worktree_id
            worktrees_created[list_id] = worktree_id
        except Exception as e:
            print(f"ERROR creating worktree {worktree_name}: {e}")
            continue

    else:
        # Worktree exists - we need to find it
        try:
            # Get worktrees from board
            worktrees = agor.worktrees.list(repo_id="88617156-51f9-44d1-8ba2-24897afc5da6")
            matching = [w for w in worktrees if w.name == worktree_name]

            if matching:
                worktree_id = matching[0].worktree_id
            else:
                # Create if it doesn't exist
                worktree = agor.worktrees.create(
                    repo_id="88617156-51f9-44d1-8ba2-24897afc5da6",
                    worktree_name=worktree_name,
                    board_id="1a508c77-dacb-46fe-ab24-e527fb476882",
                    create_branch=True,
                    notes=f"Trello List: {list_name}"
                )
                worktree_id = worktree.worktree_id

        except Exception as e:
            print(f"ERROR finding/creating worktree {worktree_name}: {e}")
            continue

    # STEP 2: Process each card (create or update session)
    for card_info in cards:
        card_id = card_info['card_id']
        title = card_info['title']
        action = card_info['action']
        category = card_info['category']
        priority = card_info['priority']
        description = card_info.get('description', '')
        url = card_info['url']

        if action == 'update':
            # UPDATE existing session
            session_id = card_info['session_id']

            update_prompt = f"""
🔄 Ticket Update from Trello

**Card:** {title}
**List:** {list_name}
**Priority:** {priority}
**Trello:** {url}

**Description:**
{description[:500] if description else 'No description'}

**Your Actions:**
1. Review any changes to the ticket
2. Continue work on this task
3. Post progress updates to Trello card AS COMMENTS
4. When complete, post completion comment

🚨 CRITICAL RULES:
- NEVER modify the card description
- ONLY post comments (not edit description)
- The description is user-maintained - hands off!
- All your updates go in COMMENTS only

⚠️ URL VERIFICATION CRITICAL:
- Test EVERY link with WebFetch before posting
- AliExpress links expire - verify before posting
- If 404, search for alternative with WebSearch
- Format: ✅ [Product](url) - Verified {datetime.now().strftime('%Y-%m-%d')}

**How to update Trello:**
```python
# CORRECT: Post comment
trello.add_comment(card_id, "Your update here...")

# WRONG: Don't do this
trello.update_description(card_id, ...)  # ❌ NEVER!
```
"""

            try:
                agor.sessions.prompt(
                    session_id=session_id,
                    prompt=update_prompt
                )
                sessions_updated.append({
                    'title': title,
                    'session_id': session_id,
                    'list_name': list_name
                })
            except Exception as e:
                print(f"ERROR updating session {session_id[:8]} ({title}): {e}")

        elif action == 'create':
            # CREATE new session in this worktree

            initial_prompt = f"""
Handle ticket: **{title}**

**Details:**
- Card ID: {card_id}
- List: {list_name}
- Category: {category}
- Priority: {priority}
- Trello: {url}

**Description:**
{description if description else 'No description provided'}

**Your Job:**
1. Understand the task from description
2. Execute the work needed
3. Post progress updates to Trello AS COMMENTS
4. When complete, post summary comment
5. Move card to appropriate list when done

**For Coding Tasks:**
- You're already in a worktree ({worktree_name})
- Implement changes here
- Create PR when ready
- Link PR in Trello comment

**For Research/Shopping Tasks:**
- Research the topic
- Gather information
- Post findings to Trello as comment

🚨 CRITICAL RULES FOR TRELLO UPDATES:
- NEVER modify the card description
- ONLY post comments (not edit description)
- The description is user-maintained - read-only for you!
- All your updates MUST go in COMMENTS only

**How to update Trello:**
```python
# CORRECT: Post comment with your findings
from trello_sync import add_comment
add_comment(card_id="{card_id}", text="Your update here...")

# WRONG: Don't do this
update_card_description(...)  # ❌ NEVER modify description!
```

⚠️ URL VERIFICATION CRITICAL:
- Test EVERY link with WebFetch before posting to Trello
- AliExpress/Amazon/eBay links expire - always verify
- If link 404s:
  1. Search for alternative with WebSearch
  2. Verify new link works
  3. Note: "Original link expired - found alternative"
- Format: ✅ [Product - Price](url) - Verified {datetime.now().strftime('%Y-%m-%d')}

**Quality Standards:**
□ All links tested with WebFetch
□ All links return HTTP 200 (no 404s)
□ Product availability confirmed
□ Verification date included
□ Updates posted as COMMENTS only (not description edits)

**Trello Card:** {url}

Start working on this task!
"""

            try:
                session = agor.sessions.create(
                    worktree_id=worktree_id,
                    agentic_tool="claude-code",
                    initial_prompt=initial_prompt
                )

                # Track in DuckDB
                db.create_session(
                    card_id=card_id,
                    session_id=session.session_id,
                    category=category,
                    title=title
                )

                sessions_created.append({
                    'title': title,
                    'session_id': session.session_id,
                    'list_name': list_name,
                    'worktree_name': worktree_name
                })

            except Exception as e:
                print(f"ERROR creating session for {title}: {e}")

db.close()

```

---

## Step 3: Log Summary

```python
from datetime import datetime

log_entry = f"""
### Trello Processing - {datetime.now().strftime('%H:%M')} (Scheduled)

**Architecture:** One worktree per list + One session per ticket

**Actions file:** {actions_file.name}

**Summary:**
- Worktrees created: {len(worktrees_created)}
- Sessions created: {len(sessions_created)}
- Sessions updated: {len(sessions_updated)}
- Total cards processed: {data['stats']['total_cards']}

**Worktrees Created:**
"""

if worktrees_created:
    for list_id, wt_id in worktrees_created.items():
        # Find list name
        list_data = [l for l in data['lists'] if l['list_id'] == list_id][0]
        log_entry += f"- {list_data['list_name']} → `{list_data['worktree_name']}` [{wt_id[:8]}]\n"
else:
    log_entry += "- None (all lists had worktrees)\n"

log_entry += f"""
**Sessions Created:**
"""

if sessions_created:
    for s in sessions_created[:10]:  # First 10
        log_entry += f"- **{s['title']}** in `{s['worktree_name']}` → [{s['session_id'][:8]}]\n"
    if len(sessions_created) > 10:
        log_entry += f"- ... and {len(sessions_created) - 10} more\n"
else:
    log_entry += "- None (all tickets had sessions)\n"

log_entry += f"""
**Sessions Updated:** {len(sessions_updated)}

**View board:** http://localhost:3030/b/1a508c77-dacb-46fe-ab24-e527fb476882

**Configuration:**
- Repo ID: 88617156-51f9-44d1-8ba2-24897afc5da6
- Board ID: 1a508c77-dacb-46fe-ab24-e527fb476882
- Trello Board: 5af14633e01cb0c5e1df9df6

**DuckDB:**
- Tracks card_id → session_id
- {len(sessions_created)} new entries
- {len(sessions_updated)} existing entries updated

**Quality:**
- All sessions verify URLs before posting
- No 404 links allowed (especially AliExpress)
"""

# Append to daily log
log_file = Path('memory') / f"{datetime.now().strftime('%Y-%m-%d')}.md"
with open(log_file, 'a') as f:
    f.write("\n---\n\n" + log_entry)

print(f"Processed {data['stats']['total_cards']} cards: {len(sessions_created)} created, {len(sessions_updated)} updated, {len(worktrees_created)} new worktrees")
```

---

## Architecture Summary

### Hierarchy

```
Board
└─ Worktree (per list)
   └─ Session (per ticket)
```

### Example

**Trello has 3 lists:**
1. Shopping (5 cards)
2. Development (3 cards)
3. Home (2 cards)

**Agor creates:**
```
Board: openclaw-agor
├─ trello-list-shopping (worktree)
│  ├─ Session: Buy o-ring
│  ├─ Session: USB-C cable
│  ├─ Session: Product A
│  ├─ Session: Product B
│  └─ Session: Product C
├─ trello-list-development (worktree)
│  ├─ Session: Implement feature X
│  ├─ Session: Fix bug Y
│  └─ Session: Refactor Z
└─ trello-list-home (worktree)
   ├─ Session: Task 1
   └─ Session: Task 2
```

**Total:** 3 worktrees, 10 sessions

---

## Current State (First Run)

Based on test run:

```
Worktrees to create: 1 (japan)
Worktrees existing: 8
Sessions to create: 16
Sessions to update: 26
Total cards: 42
```

**Will create:**
- 1 new worktree (japan)
- 16 new sessions in their respective worktrees
- Send updates to 26 existing sessions

---

## Key Points

### ✅ Organization
- Lists = Worktrees (spatial organization on board)
- Tickets = Sessions (full context per task)

### ✅ Isolation
- Each session has dedicated context
- Sessions in same worktree share list context
- Complete isolation between tickets

### ✅ URL Verification
- EVERY session verifies links before posting
- No 404s allowed (especially AliExpress)
- WebFetch tool required

### ✅ DuckDB Tracking
- Tracks: `card_id → session_id`
- Not list-based anymore (back to per-ticket)
- Simple duplicate prevention

---

## See Also

- `utils/generate_ticket_sessions_by_list.py` - Entry point
- `utils/session_db.py` - DuckDB wrapper
- `utils/trello_sync.py` - Trello API helpers

---

**Version:** 5.0 (hybrid: worktree per list + session per ticket)
**Last Updated:** 2026-04-14
**Status:** Ready for deployment
