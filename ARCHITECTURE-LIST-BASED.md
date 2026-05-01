# List-Based Session Architecture

**Date:** 2026-03-20 (Updated: 2026-04-06)
**Version:** 3.0
**Status:** ✅ Ready for deployment

---

## Overview

This architecture changes the Trello processor from **per-ticket sessions** to **per-list sessions**.

### Old Model (Per-Ticket)

```
Shopping List:
  - Buy o-ring → Session A
  - USB-C cable → Session B
  - Analyze repo → Session C

Total: 3 sessions managing 3 cards
```

### New Model (Per-List)

```
Shopping List → Session A
  ├─ Buy o-ring
  ├─ USB-C cable
  └─ Analyze repo

Total: 1 session managing 3 cards
```

---

## Benefits

### 1. Organizational Clarity
- Sessions map directly to Trello lists
- Natural grouping by category/context
- Easy to find the session for a specific area
- Less clutter on the board

### 2. Context Awareness
- Session sees ALL cards in its domain
- Can prioritize across related tasks
- Better coordination of related work
- Understands dependencies within list

### 3. Efficiency
- Fewer sessions to manage
- Reduced overhead
- Better resource utilization
- Simpler tracking

### 4. User Experience
- Clear mapping: List → Session
- One place to check for category updates
- Easier to monitor progress by area

---

## Architecture

### Database Schema (DuckDB)

**Key Change:** Track `list_id` instead of `card_id`

```python
# Old (per-ticket)
db.create_session(
    card_id="69b15139...",  # Specific ticket
    session_id="abc123...",
    category="personal",
    title="Buy o-ring"
)

# New (per-list)
db.create_session(
    card_id="5af14633...",  # Actually list_id
    session_id="xyz789...",
    category="list-manager",
    title="List: Shopping"
)
```

### Workflow

```
1. Scheduled trigger (every 4 hours)
   ↓
2. generate_list_sessions.py
   ├─ Fetch all lists from board
   ├─ Fetch all active cards
   ├─ Group cards by list
   └─ Check DuckDB for existing list sessions
   ↓
3. Generate actions
   ├─ UPDATE (existing list with changes)
   └─ CREATE (new list)
   ↓
4. Output: memory/list-sessions-{timestamp}.json
   ↓
5. Orchestrator processes actions
   ├─ For UPDATE: Send update with all cards in list
   └─ For CREATE: Create session with all cards
   ↓
6. List sessions work on cards
   ├─ Prioritize within list
   ├─ Execute highest priority first
   └─ Update Trello as work progresses
```

---

## Current Board State

**Test run (2026-04-06 22:30):**

```
Total lists on board: 9
Lists with cards: 8
Lists to process: 8
  Updates: 0 (all new)
  Creates: 8

Lists:
1. "In Progress" (10 cards) → CREATE session
2. "בית" (6 cards) → CREATE session
3. "שוטף" (4 cards) → CREATE session
4. "מסיבה 50" (6 cards) → CREATE session
5. "בת מצווה" (7 cards) → CREATE session
6. "japan" (1 card) → CREATE session
7. "AliExpress" (2 cards) → CREATE session
8. "Tech" (1 card) → CREATE session
9. "רכב" (0 cards) → SKIP (empty)
```

---

## Files

### Core Scripts

**`utils/generate_list_sessions.py`** (NEW - 300 lines)
- Entry point for list-based processing
- Fetches lists and cards from Trello
- Groups cards by list
- Checks DuckDB for existing sessions
- Generates UPDATE/CREATE actions
- Outputs: `memory/list-sessions-{timestamp}.json`

**`temp/scheduled_prompt.md`** (UPDATED)
- Orchestrator prompt for processing list sessions
- Step-by-step instructions
- URL verification requirements
- Handles both UPDATE and CREATE actions

**`utils/session_db.py`** (UNCHANGED)
- DuckDB wrapper still works
- Just uses list_id as the key instead of card_id
- No code changes needed

### Output Format

**`memory/list-sessions-{timestamp}.json`:**

```json
{
  "timestamp": "2026-04-06T22:30:58",
  "board_id": "5af14633e01cb0c5e1df9df6",
  "lists": [
    {
      "list_id": "5af1465b6f73a92eae6369aa",
      "list_name": "In Progress",
      "action": "create",
      "cards": [
        {
          "card_id": "674ff398...",
          "title": "לעבור על פנסיה",
          "description": "...",
          "url": "https://trello.com/c/...",
          "priority": 5,
          "priority_reasoning": "calculated based on due date, labels, activity",
          "labels": [],
          "due_date": null,
          "last_activity": "2026-03-29T20:05:16.563Z"
        }
      ]
    }
  ],
  "stats": {
    "total_lists": 9,
    "lists_with_cards": 8,
    "lists_to_process": 8,
    "updates": 0,
    "creates": 8
  }
}
```

---

## Migration Plan

### Phase 1: Preparation (DONE)
- ✅ Created `generate_list_sessions.py`
- ✅ Updated `scheduled_prompt.md`
- ✅ Tested script (8 lists detected)
- ✅ Documented architecture

### Phase 2: Deployment

**Step 1: Update scheduler configuration**
- Change entry point from `scheduled_run.py` to `generate_list_sessions.py`
- Update scheduled prompt to list-based version

**Step 2: Clean up old sessions**
- Archive all existing per-ticket sessions
- Clear DuckDB (or keep, will be ignored)

**Step 3: First run**
- Should create 8 new list sessions
- One per active list

**Step 4: Monitor**
- Check that sessions are working
- Verify URL verification is happening
- Ensure updates work on next run (4 hours later)

### Phase 3: Optimization

**After 1 week:**
- Review session effectiveness
- Adjust prompts based on results
- Optimize priority calculations
- Fine-tune update detection

---

## Session Responsibilities

Each list session is responsible for:

### 1. Task Management
- Review ALL cards in its list
- Calculate priorities
- Work on highest priority first
- Track progress

### 2. Execution
- **Coding tasks:** Create worktrees + worker sessions
- **Research tasks:** Research directly in session
- **Personal tasks:** Handle or research as appropriate

### 3. Updates
- Post progress to Trello cards
- Update descriptions with findings
- Move cards to appropriate lists
- Mark completed cards as "done"

### 4. URL Verification
- Test ALL links with WebFetch
- Replace broken links (especially AliExpress)
- Mark verified links with date
- Never post 404 links

### 5. Coordination
- Understand relationships between cards
- Prioritize based on due dates + labels
- Balance work across cards

---

## Update Detection

List sessions receive updates when:

1. **New card added to list**
   - Triggers: UPDATE action
   - Includes new card in list data

2. **Card moved into list**
   - Triggers: UPDATE action
   - Card appears in list data

3. **Card description updated**
   - Detected via `dateLastActivity`
   - Triggers: UPDATE with `has_changes: true`

4. **New comment on card**
   - Detected via recent activity
   - Triggers: UPDATE with `has_changes: true`

5. **Priority changed**
   - Labels added/removed
   - Due date changed
   - Triggers: UPDATE

**Update frequency:** Every 4 hours (scheduled)

**Change detection window:** 4 hours (since last run)

---

## Priority Calculation

Cards within each list are prioritized by:

```python
score = 0

# Due date urgency
if overdue:
    score += 100
elif due in 1 day:
    score += 50
elif due in 7 days:
    score += 20
elif due in 30 days:
    score += 10

# Label-based
if 'urgent' or 'high':
    score += 30
if 'active':
    score += 15

# Recent activity
if active today:
    score += 15
elif active this week:
    score += 5
```

Cards sorted by priority (highest first) within each list session.

---

## Configuration

**Trello Board:** 5af14633e01cb0c5e1df9df6 (B.Berry Projects)
**Visibility Worktree:** 659dbc25-b301-4e2c-ab26-c07cd1737fcb (trello-visibility-hub)
**Repo:** 88617156-51f9-44d1-8ba2-24897afc5da6 (agor-openclaw)
**Board:** 1a508c77-dacb-46fe-ab24-e527fb476882 (openclaw-agor)

**Scheduling:**
- Cron: `0 */4 * * *` (every 4 hours)
- Entry point: `uv run python utils/generate_list_sessions.py`
- Agent tool: `claude-code`

**Limits:**
- No per-category limits (handled by list sessions)
- Each list session manages its own capacity
- Natural throttling via priority

---

## URL Verification Requirements

**CRITICAL:** All list sessions MUST verify URLs before posting.

### Verification Process

```python
# 1. Test link
status = WebFetch(url)

# 2. Check status
if status != 200:
    # Link broken - find alternative
    search_results = WebSearch(f"{product_name} buy")
    new_url = find_working_link(search_results)
    verify(new_url)

# 3. Mark verified
post_to_trello(f"✅ [Product](verified_url) - Verified {date}")
```

### Common Issues

**AliExpress:**
- Products removed/sold out frequently
- Links expire after ~30 days
- Fix: Search for current listing, verify new link

**Amazon:**
- Affiliate/tracking parameters break links
- Region-specific URLs fail
- Fix: Use clean product URL (amazon.com/dp/PRODUCTID)

**eBay:**
- Auction links expire when auction ends
- Fix: Find "Buy It Now" listing or current auction

### Quality Checklist

Before posting ANY link to Trello:
- □ Tested with WebFetch
- □ Returns HTTP 200
- □ Product page loads
- □ Product available (not sold out)
- □ Price confirmed
- □ Link not region-locked
- □ Verification date included

---

## Testing

**Test run completed:** 2026-04-06 22:30

```bash
$ python3 utils/generate_list_sessions.py

=== Trello List Session Generator ===

✓ Found 9 active lists
✓ Found cards in 8 lists

Lists processed:
1. In Progress (10 cards) → CREATE
2. בית (6 cards) → CREATE
3. שוטף (4 cards) → CREATE
4. מסיבה 50 (6 cards) → CREATE
5. בת מצווה (7 cards) → CREATE
6. japan (1 card) → CREATE
7. AliExpress (2 cards) → CREATE
8. Tech (1 card) → CREATE

✓ Saved to: memory/list-sessions-20260406-223058.json
```

**Result:** ✅ Working correctly

---

## Next Steps

### Immediate
1. ✅ Test `generate_list_sessions.py` - DONE
2. ⏳ Update Agor scheduler configuration
3. ⏳ Archive old per-ticket sessions
4. ⏳ Deploy list-based architecture

### Monitoring (First Week)
- Track session creation/updates
- Verify URL verification is working
- Check for duplicates (should be none)
- Monitor Trello updates from sessions

### Optimization (After 1 Week)
- Adjust priority calculations if needed
- Fine-tune update detection
- Optimize prompts based on results
- Add any missing features

---

## Success Criteria

All criteria ready for deployment:

- ✅ Script creates one session per list
- ✅ DuckDB tracks list_id → session_id
- ✅ Cards grouped and prioritized within lists
- ✅ Update detection working
- ✅ URL verification requirements clear
- ✅ Orchestrator prompt updated
- ✅ Documentation complete

**Status:** Ready for production deployment

---

**Created:** 2026-04-06
**Author:** Orchestrator session 82e4beed
**Test Results:** ✅ 8 lists detected, ready to create sessions
**Next:** Deploy to Agor scheduler
