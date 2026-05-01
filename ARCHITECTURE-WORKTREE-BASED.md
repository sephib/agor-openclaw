# Worktree-Based List Architecture

**Date:** 2026-04-14
**Version:** 4.0
**Status:** ✅ Ready for deployment

---

## Overview

**One WORKTREE per Trello list** - each list gets its own isolated worktree with a session managing all cards in that list.

### Architecture

```
Trello Board: B.Berry Projects
├─ List: Shopping
│  └─ Agor Worktree: trello-list-shopping
│     └─ Session: Manages all Shopping cards
├─ List: Development  
│  └─ Agor Worktree: trello-list-development
│     └─ Session: Manages all Development cards
├─ List: בית (Home)
│  └─ Agor Worktree: trello-list-בית
│     └─ Session: Manages all Home cards
└─ ... (one worktree per list)
```

### Current Board State

**9 Trello lists with cards:**
1. "In Progress" → `trello-list-in-progress` (10 cards)
2. "בית" → `trello-list-בית` (6 cards)
3. "שוטף" → `trello-list-שוטף` (7 cards)
4. "מסיבה 50" → `trello-list-מסיבה-50` (6 cards)
5. "בת מצווה" → `trello-list-בת-מצווה` (7 cards)
6. "japan" → `trello-list-japan` (1 card)
7. "AliExpress" → `trello-list-aliexpress` (3 cards)
8. "Tech" → `trello-list-tech` (1 card)
9. "Vacation" → `trello-list-vacation-` (1 card)

**Total:** 9 worktrees to create on first run

---

## Benefits

### 1. Visual Organization
- ✅ Each list visible as separate worktree on board
- ✅ Clear spatial organization
- ✅ Easy to see what each list is working on
- ✅ Worktree name shows which list it manages

### 2. Complete Isolation
- ✅ Each list has its own context
- ✅ No shared state between lists
- ✅ Can work on lists independently
- ✅ Failures isolated to one worktree

### 3. Lifecycle Management
- ✅ Create worktree when list created
- ✅ Delete worktree when list deleted
- ✅ Clean, simple lifecycle
- ✅ No orphaned resources

### 4. Git Integration
- ✅ Each worktree has own branch
- ✅ Can commit/PR per list if needed
- ✅ Better organization in git

---

## How It Works

### Step 1: Generate List Actions

```bash
python3 utils/generate_list_sessions.py
```

**Output:** `memory/list-sessions-{timestamp}.json`

```json
{
  "lists": [
    {
      "list_id": "5af1465b...",
      "list_name": "Shopping",
      "worktree_name": "trello-list-shopping",
      "action": "create",
      "cards": [...]
    }
  ]
}
```

### Step 2: Orchestrator Creates Worktrees

For each list with `action: "create"`:

```python
# 1. Create worktree
worktree = agor.worktrees.create(
    repo_id="88617156-51f9-44d1-8ba2-24897afc5da6",
    worktree_name="trello-list-shopping",
    board_id="1a508c77-dacb-46fe-ab24-e527fb476882",
    create_branch=True,
    notes="Trello List: Shopping (10 cards)"
)

# 2. Create session in that worktree
session = agor.sessions.create(
    worktree_id=worktree.worktree_id,
    agentic_tool="claude-code",
    initial_prompt="Manage all cards in Shopping list..."
)

# 3. Track in DuckDB
db.create_session(
    card_id=list_id,
    session_id=session.session_id,
    category='list-manager',
    title=f"List: Shopping | WT: {worktree.worktree_id[:8]}"
)
```

### Step 3: Session Manages Cards

The session in each worktree:
- Sees all cards in its list
- Prioritizes by due date, labels, activity
- Works on highest priority first
- Updates Trello cards with progress
- Verifies all URLs before posting

### Step 4: Updates (Every 4 Hours)

For existing worktrees with `action: "update"`:

```python
# Send update prompt to existing session
agor.sessions.prompt(
    session_id=session_id,
    prompt=f"""
    🔄 List Update: Shopping
    
    Cards changed since last run:
    - New card: "Buy USB-C cable"
    - Comment on: "Buy o-ring"
    
    Review changes and continue work...
    """
)
```

---

## Worktree Naming

**Format:** `trello-list-{sanitized-name}`

**Sanitization rules:**
- Remove special characters
- Replace spaces with hyphens
- Lowercase
- Max 30 characters

**Examples:**
```
"Shopping"        → trello-list-shopping
"In Progress"     → trello-list-in-progress
"בית"             → trello-list-בית
"מסיבה 50"        → trello-list-מסיבה-50
"Development!"    → trello-list-development
"Very Long List Name Here" → trello-list-very-long-list-name-h
```

---

## DuckDB Tracking

**What's tracked:**

```python
{
    'card_id': '5af1465b...',  # Actually list_id
    'session_id': 'abc123...',
    'category': 'list-manager',
    'title': 'List: Shopping | WT: xyz789ab'
}
```

**Lookup:**
```python
db = SessionDB()

# Check if list has worktree
if db.has_session(list_id):
    session = db.get_session(list_id)
    session_id = session['session_id']
    # Extract worktree_id from title if needed
```

---

## Lifecycle Handling

### New List Created

**User action:** Creates new Trello list "Projects"

**What happens:**
1. Next scheduled run (every 4 hours)
2. Script detects new list
3. **Action: CREATE**
4. Orchestrator creates:
   - Worktree: `trello-list-projects`
   - Session in that worktree
5. Tracked in DuckDB

**Result:** ✅ New worktree visible on board

### List Deleted

**User action:** Deletes Trello list "Old Stuff"

**What happens:**
1. Next scheduled run
2. Script detects missing list
3. **Action: ARCHIVE**
4. Orchestrator:
   - Marks session as completed
   - Removes from DuckDB
   - (Worktree cleanup may need manual step)

**Result:** ✅ Orphaned worktree archived

### List Becomes Empty

**User action:** Moves all cards out of "Temporary"

**What happens:**
- Same as deleted list
- Empty lists don't need active worktrees

**Result:** ✅ Worktree archived

### List Renamed

**User action:** Renames "Shopping" to "Buy Stuff"

**What happens:**
- List ID stays same (only name changed)
- Worktree name unchanged (created from original name)
- Session receives update with new list name
- No worktree recreation needed

**Result:** ✅ Works normally

---

## First Deployment

### Expected Actions

When deployed for the first time:

```
Lists detected: 9
Actions:
  Creates: 9 worktrees
  Updates: 0
  Archives: 0

Worktrees to create:
1. trello-list-in-progress (10 cards)
2. trello-list-בית (6 cards)
3. trello-list-שוטף (7 cards)
4. trello-list-מסיבה-50 (6 cards)
5. trello-list-בת-מצווה (7 cards)
6. trello-list-japan (1 card)
7. trello-list-aliexpress (3 cards)
8. trello-list-tech (1 card)
9. trello-list-vacation- (1 card)

Total: 42 cards across 9 worktrees
```

### Board After First Run

```
Board: openclaw-agor
├─ trello-task-processor (orchestrator)
├─ trello-list-in-progress
├─ trello-list-בית
├─ trello-list-שוטף
├─ trello-list-מסיבה-50
├─ trello-list-בת-מצווה
├─ trello-list-japan
├─ trello-list-aliexpress
├─ trello-list-tech
└─ trello-list-vacation-
```

---

## URL Verification

**CRITICAL:** Every session MUST verify URLs before posting.

### Why This Matters

**Problem:** AliExpress (and other) product links expire frequently
**Impact:** User clicks link from Trello comment → 404 error → frustration
**Solution:** Test every link with WebFetch before posting

### Verification Process

```python
# In each list session
from tools import WebFetch

# Before posting any product link
url = "https://aliexpress.com/item/..."
result = WebFetch(url)

if result.status_code == 200:
    # Link works!
    post_to_trello(f"✅ [Product](url) - Verified {date}")
else:
    # Link broken - find alternative
    search_results = WebSearch(f"{product_name} buy")
    new_url = find_working_link(search_results)
    verify_and_post(new_url)
```

### Quality Checklist

Before posting to Trello:
- □ Link tested with WebFetch
- □ Returns HTTP 200
- □ Product page loads
- □ Product available (not sold out)
- □ Price confirmed
- □ Verification date included
- □ Link not region-locked

---

## Configuration

**Trello:**
- Board ID: `5af14633e01cb0c5e1df9df6`
- Board Name: B.Berry Projects

**Agor:**
- Repo ID: `88617156-51f9-44d1-8ba2-24897afc5da6`
- Repo: agor-openclaw (local)
- Board ID: `1a508c77-dacb-46fe-ab24-e527fb476882`
- Board Name: openclaw-agor

**Scheduling:**
- Cron: `0 */4 * * *` (every 4 hours)
- Entry: `uv run python utils/generate_list_sessions.py`
- Agent: `claude-code`
- Prompt: `temp/scheduled_prompt.md`

---

## Files

### Core Scripts

**`utils/generate_list_sessions.py`** ✅
- Generates list actions with worktree names
- Detects orphaned worktrees
- Outputs JSON with CREATE/UPDATE/ARCHIVE actions

**`temp/scheduled_prompt.md`** ✅
- Orchestrator instructions
- Creates worktree + session for each list
- Handles updates and archives
- URL verification requirements

**`utils/session_db.py`** (unchanged)
- DuckDB wrapper
- Tracks list_id → session_id
- Uses list_id as key (not card_id)

### Documentation

**`ARCHITECTURE-WORKTREE-BASED.md`** - This file
**`temp/LIST-LIFECYCLE-HANDLING.md`** - Lifecycle management
**`temp/DEPLOYMENT-CHECKLIST.md`** - Deployment guide (needs update)

---

## Comparison: Sessions vs Worktrees

### Old (Session-Based)

```
trello-visibility-hub worktree:
├─ Session: Shopping list
├─ Session: Development list
├─ Session: Home list
└─ ... (all in one worktree)
```

**Pros:**
- All in one place
- Simpler initial setup

**Cons:**
- Hard to see on board
- Shared context
- No isolation

### New (Worktree-Based) ✅

```
Board:
├─ trello-list-shopping worktree
│  └─ Session
├─ trello-list-development worktree
│  └─ Session
├─ trello-list-בית worktree
│  └─ Session
└─ ...
```

**Pros:**
- ✅ Visual organization on board
- ✅ Complete isolation
- ✅ Clear ownership
- ✅ Easy cleanup

**Cons:**
- More worktrees to manage
- Slightly more complex setup

**Decision:** Worktree-based is better for multi-list management

---

## Next Steps

### 1. Deploy ✅ Ready

Update Agor scheduler:
- Entry: `uv run python utils/generate_list_sessions.py`
- Prompt: Copy from `temp/scheduled_prompt.md`

### 2. First Run

Will create 9 worktrees:
- One per active Trello list
- Each with session managing its cards

### 3. Monitor

Check:
- ✅ 9 worktrees created
- ✅ Each has session
- ✅ Sessions working on cards
- ✅ URL verification happening
- ✅ DuckDB tracking working

### 4. Second Run (4 Hours Later)

Should:
- Send updates to existing sessions
- Create worktrees for any new lists
- Archive any deleted lists
- No duplicates

---

## Success Criteria

All ready for deployment:

- ✅ Script generates worktree names
- ✅ Handles CREATE/UPDATE/ARCHIVE
- ✅ DuckDB tracking ready
- ✅ Orchestrator prompt updated
- ✅ URL verification included
- ✅ Lifecycle handling complete
- ✅ Documentation complete

**Status:** 🟢 **READY TO DEPLOY**

---

**Created:** 2026-04-14
**Architecture:** One worktree per Trello list
**First run:** Will create 9 worktrees for 42 cards
**Next:** Update scheduler configuration and deploy
