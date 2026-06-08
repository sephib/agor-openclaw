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
from datetime import datetime
import sys
sys.path.insert(0, 'utils')
from session_db import SessionDB
from list_context import get_context_for_prompt, generate_aliexpress_search_url
from trello_sync import add_label_to_card, load_credentials, LABEL_IDS

# Load Trello credentials (used to apply skip label at orchestrator level)
creds = load_credentials()

# Load user preferences (injected into every new session)
user_prefs_path = Path('memory/user-preferences.md')
user_prefs = user_prefs_path.read_text() if user_prefs_path.exists() else ""

# Load actions file
actions_file = sorted(Path('memory').glob('ticket-sessions-*.json'))[-1]
data = json.load(open(actions_file))

print(f"Processing {actions_file.name}: {len(data['lists'])} lists, {data['stats']['total_cards']} cards")

# Connect to DuckDB
db = SessionDB()

# --- CLEANUP: orphaned sessions for cards no longer active in Trello ---
# archived_cards: card was archived/done in Trello → archive Agor session (DuckDB already marked archived)
# deleted_cards:  card is gone from Trello entirely → archive Agor session (DuckDB row already hard-deleted)
sessions_archived_agor = []
sessions_deleted_agor = []

for entry in data.get('archived_cards', []):
    try:
        agor.sessions.archive(session_id=entry['session_id'])
        sessions_archived_agor.append(entry)
        print(f"  ARCHIVED session {entry['session_id'][:8]} ({entry['title']})")
    except Exception as e:
        print(f"  ERROR archiving session {entry['session_id'][:8]} ({entry['title']}): {e}")

for entry in data.get('deleted_cards', []):
    try:
        agor.sessions.archive(session_id=entry['session_id'])
        sessions_deleted_agor.append(entry)
        print(f"  DELETED→archived session {entry['session_id'][:8]} ({entry['title']})")
    except Exception as e:
        print(f"  ERROR archiving deleted-card session {entry['session_id'][:8]} ({entry['title']}): {e}")

if sessions_archived_agor or sessions_deleted_agor:
    print(f"Cleanup: {len(sessions_archived_agor)} archived, {len(sessions_deleted_agor)} deleted")
# --- END CLEANUP ---

# Track created worktrees and sessions
worktrees_created = {}  # list_id → worktree_id
sessions_created = []
sessions_updated = []

for list_info in data['lists']:
    list_id = list_info['list_id']
    list_name = list_info['list_name']
    list_type = list_info.get('list_type', 'task')
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
                notes=f"Trello List: {list_name} ({list_type}, {len(cards)} cards)"
            )
            worktree_id = worktree.worktree_id
            worktrees_created[list_id] = worktree_id
        except Exception as e:
            print(f"ERROR creating worktree {worktree_name}: {e}")
            continue

    else:
        # Worktree exists - we need to find it
        try:
            worktrees = agor.worktrees.list(repo_id="88617156-51f9-44d1-8ba2-24897afc5da6")
            matching = [w for w in worktrees if w.name == worktree_name]

            if matching:
                worktree_id = matching[0].worktree_id
            else:
                worktree = agor.worktrees.create(
                    repo_id="88617156-51f9-44d1-8ba2-24897afc5da6",
                    worktree_name=worktree_name,
                    board_id="1a508c77-dacb-46fe-ab24-e527fb476882",
                    create_branch=True,
                    notes=f"Trello List: {list_name} ({list_type})"
                )
                worktree_id = worktree.worktree_id

        except Exception as e:
            print(f"ERROR finding/creating worktree {worktree_name}: {e}")
            continue

    # Persist list → worktree mapping
    db.upsert_list(
        list_id=list_id,
        list_name=list_name,
        list_type=list_type,
        worktree_id=worktree_id,
        worktree_name=worktree_name,
        ticket_count=len(cards),
    )

    # Build shared list context block for prompt injection
    list_context_block = get_context_for_prompt(
        worktree_name=worktree_name,
        list_name=list_name,
        list_type=list_type,
    )

    # STEP 2: Process each card (create or update session)
    for card_info in cards:
        card_id = card_info['card_id']
        title = card_info['title']
        action = card_info['action']
        category = card_info['category']
        priority = card_info['priority']
        description = card_info.get('description', '')
        url = card_info['url']
        is_aliexpress = 'aliexpress' in list_name.lower()
        aliexpress_search_url = generate_aliexpress_search_url(title) if is_aliexpress else None

        if action == 'update':
            # UPDATE existing session
            session_id = card_info['session_id']

            aliexpress_block = f"""
**AliExpress Search (stable link — never expires):**
  {aliexpress_search_url}

🔗 LINK STRATEGY FOR ALIEXPRESS:
- The search URL above is your PRIMARY link — always include it in your Trello comment
- It is query-based and will never 404
- You MAY also include 1-2 specific product links as secondary recommendations
- For product links: use clean URLs (aliexpress.com/item/ID.html — strip tracking params)
- Format: 🔍 Search: [search terms]({aliexpress_search_url})
  Optional top picks: ✅ [Product - Price](clean-url) - Verified {datetime.now().strftime('%Y-%m-%d')}
""" if aliexpress_search_url else f"""
⚠️ URL VERIFICATION:
- Test links with WebFetch before posting
- If 404, search for alternative with WebSearch
- Format: ✅ [Product](url) - Verified {datetime.now().strftime('%Y-%m-%d')}
"""

            update_prompt = f"""
🔄 Ticket Update from Trello

**Card:** {title}
**List:** {list_name} ({list_type})
**Priority:** {priority}
**Trello:** {url}

**Description:**
{description[:500] if description else 'No description'}
{list_context_block}
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
{aliexpress_block}
**How to update Trello:**
```python
# CORRECT: Post comment
trello.add_comment(card_id, "Your update here...")

# WRONG: Don't do this
trello.update_description(card_id, ...)  # ❌ NEVER!
```

**When your work is complete, add the 'skip' label** so this card won't be re-processed next run:
```python
import sys
sys.path.insert(0, 'utils')
from trello_sync import add_label_to_card, load_credentials, LABEL_IDS
creds = load_credentials()
add_label_to_card(creds, card_id="{card_id}", label_id=LABEL_IDS['skip'])
```
The user can remove the 'skip' label anytime to re-engage you on this card.
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
                # Apply skip label at orchestrator level — don't rely on worker to do it
                try:
                    add_label_to_card(creds, card_id, LABEL_IDS['skip'])
                    print(f"  SKIP label applied: {title}")
                except Exception as label_err:
                    print(f"  WARNING: skip label failed for {title}: {label_err}")
            except Exception as e:
                print(f"ERROR updating session {session_id[:8]} ({title}): {e}")

        elif action == 'create':
            # CREATE new session in this worktree

            write_back_section = f"""
## List Discovery Write-Back

If you learn something relevant to ALL tickets in this list (a decision, constraint,
booking confirmation, budget update), append a line to:
  memory/list-context/{worktree_name}.md

Format: `- [{datetime.now().strftime('%Y-%m-%d')}] {title}: <your discovery>`

Other sessions and future runs will see this.
""" if list_type != 'task' else ""

            initial_prompt = f"""
Handle ticket: **{title}**

**Details:**
- Card ID: {card_id}
- List: {list_name} ({list_type})
- Category: {category}
- Priority: {priority}
- Trello: {url}

**Description:**
{description if description else 'No description provided'}
{list_context_block}
## User Preferences

{user_prefs if user_prefs else 'No preferences configured yet. See memory/user-preferences.md'}

---

**Your Job:**
1. Understand the task from description
2. Execute the work needed
3. Post progress updates to Trello AS COMMENTS
4. When complete, post summary comment and add the 'skip' label
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

**When your work is complete, add the 'skip' label** so this card won't be re-processed next run:
```python
import sys
sys.path.insert(0, 'utils')
from trello_sync import add_label_to_card, load_credentials, LABEL_IDS
creds = load_credentials()
add_label_to_card(creds, card_id="{card_id}", label_id=LABEL_IDS['skip'])
```
The user can remove the 'skip' label anytime to re-engage you on this card.

{f'''🔗 LINK STRATEGY FOR ALIEXPRESS:
- Your PRIMARY link (always include in Trello comment):
  {aliexpress_search_url}
- This search URL is query-based and will NEVER 404
- You MAY also include 1-2 specific product links as secondary picks
- For product links: use clean URLs (aliexpress.com/item/ID.html — strip tracking params)
- Format: 🔍 Search: [search terms]({aliexpress_search_url})
  Optional: ✅ [Product - Price](clean-url) - Verified {datetime.now().strftime("%Y-%m-%d")}
''' if aliexpress_search_url else f'''⚠️ URL VERIFICATION:
- Test links with WebFetch before posting to Trello
- If link 404s, search for alternative with WebSearch
- Format: ✅ [Product - Price](url) - Verified {datetime.now().strftime("%Y-%m-%d")}
'''}
**Quality Standards:**
□ Updates posted as COMMENTS only (not description edits)
{f"□ Search URL included as primary link" if aliexpress_search_url else "□ All links tested with WebFetch"}
{write_back_section}
**Trello Card:** {url}

Start working on this task!
"""

            try:
                session = agor.sessions.create(
                    worktree_id=worktree_id,
                    agentic_tool="claude-code",
                    initial_prompt=initial_prompt
                )

                # Track in DuckDB (with list_id)
                db.create_session(
                    card_id=card_id,
                    session_id=session.session_id,
                    category=category,
                    title=title,
                    list_id=list_id,
                )

                # Apply skip label at orchestrator level — don't rely on worker to do it
                try:
                    add_label_to_card(creds, card_id, LABEL_IDS['skip'])
                    print(f"  SKIP label applied: {title}")
                except Exception as label_err:
                    print(f"  WARNING: skip label failed for {title}: {label_err}")

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
- Sessions archived (card archived/done): {len(sessions_archived_agor)}
- Sessions deleted (card gone from Trello): {len(sessions_deleted_agor)}
- Total cards processed: {data['stats']['total_cards']}

**Worktrees Created:**
"""

if worktrees_created:
    for list_id, wt_id in worktrees_created.items():
        list_data = [l for l in data['lists'] if l['list_id'] == list_id][0]
        log_entry += f"- {list_data['list_name']} ({list_data.get('list_type','task')}) → `{list_data['worktree_name']}` [{wt_id[:8]}]\n"
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
- AliExpress cards use stable search URLs as primary links (never 404)
- Non-AliExpress links verified with WebFetch before posting
"""

# Append to daily log
log_file = Path('memory') / f"{datetime.now().strftime('%Y-%m-%d')}.md"
with open(log_file, 'a') as f:
    f.write("\n---\n\n" + log_entry)

print(f"Processed {data['stats']['total_cards']} cards: {len(sessions_created)} created, {len(sessions_updated)} updated, {len(worktrees_created)} new worktrees, {len(sessions_archived_agor)} archived, {len(sessions_deleted_agor)} deleted")
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

### ✅ Link Strategy
- AliExpress cards get stable search URLs as primary links (query-based, never 404)
- Product-specific links are optional secondary recommendations (clean URLs, no tracking params)
- Non-AliExpress links verified with WebFetch before posting

### ✅ DuckDB Tracking
- `trello_list`: list_id → list_type, worktree_id, ticket_count
- `ticket_sessions`: card_id → session_id, list_id
- Context files: `memory/list-context/{worktree_name}.md`

### ✅ Three-Tier Context
Every new session gets: card context + list context + user preferences

### ✅ List Types
| Pattern | Type | Shared context |
|---|---|---|
| trip/travel/vacation | `project` | Full synthesis |
| party/event/wedding | `project` | Full synthesis |
| home/house/renovation | `project` | Full synthesis |
| aliexpress/shopping/buy | `shopping` | Item summary |
| anything else | `task` | None |

---

## See Also

- `utils/generate_ticket_sessions_by_list.py` - Entry point
- `utils/session_db.py` - DuckDB wrapper (trello_list + ticket_sessions)
- `utils/list_context.py` - List context synthesis and injection
- `utils/trello_sync.py` - Trello API helpers
- `memory/user-preferences.md` - Global user preferences

---

**Version:** 6.1 (AliExpress search URLs as primary links)
**Last Updated:** 2026-06-08
**Status:** Ready for deployment
