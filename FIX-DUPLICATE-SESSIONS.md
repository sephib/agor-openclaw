# 🚨 FIX: Duplicate Session Creation Issue

**Status:** ❌ EPIC FAILURE - Still failing as of 2026-03-19 08:01
**Total Duplicates:** 20 sessions across 8+ runs
**Fix Required:** URGENT - Pattern continues every 4 hours

## Problem

The Trello ticket processor creates duplicate sessions every 4 hours for the same tickets.

**Evidence (Updated 2026-03-19 08:01):**
- 2026-03-16 14:01: Created session `6d1fd712` for "creat website from notebook lm.and Gemini"
- 2026-03-16 18:00: Created session `76185251` for same ticket (DUPLICATE #2)
- 2026-03-17 20:02: Created session `228288f1` for same ticket (DUPLICATE #3)
- 2026-03-18 12:02: Created session `c5cbc4b2` for same ticket (DUPLICATE #4)
- 2026-03-19 08:01: Created session `d391afc7` for "התקנת אינטרנט" (DUPLICATE #8) ← **TODAY!**
- 2026-03-19 08:01: Created session `d8680b71` for "Buy o ring" (DUPLICATE #8) ← **TODAY!**

**Root Cause:**
1. `utils/process_trello_tickets.py` generates plan without checking existing sessions ✅ (This is OK - plan includes all active tickets)
2. **ORCHESTRATOR fails to read `memory/agor-state/trello-processor.json` before creating sessions** ❌ (THIS IS THE BUG!)

The processor script is fine - it's the orchestrator that's broken!

## Solution

### CRITICAL: Orchestrator Must Read State File FIRST

**The orchestrator MUST execute these steps IN ORDER:**

```python
# STEP 1: Generate plan
uv run utils/process_trello_tickets.py
plan = read_json("memory/trello-plan-YYYYMMDD-HHMMSS.json")

# STEP 2: READ STATE FILE FIRST! (THIS IS THE FIX!)
state_file = 'memory/agor-state/trello-processor.json'
if os.path.exists(state_file):
    state = json.load(open(state_file))
else:
    state = {"active_coding_sessions": [], "active_research_sessions": [], "active_personal_sessions": []}

# STEP 3: Extract ALL active ticket IDs
active_ticket_ids = set()
for session in state.get('active_coding_sessions', []):
    active_ticket_ids.add(session['ticket_id'])
for session in state.get('active_research_sessions', []):
    active_ticket_ids.add(session['ticket_id'])
for session in state.get('active_personal_sessions', []):
    active_ticket_ids.add(session['ticket_id'])

print(f"✅ Found {len(active_ticket_ids)} tickets already active")

# STEP 4: Filter plan to exclude tickets with active sessions
coding_tasks = [t for t in plan['coding_tasks'] if t['card_id'] not in active_ticket_ids]
research_tasks = [t for t in plan['research_tasks'] if t['card_id'] not in active_ticket_ids]
personal_tasks = [t for t in plan['personal_tasks'] if t['card_id'] not in active_ticket_ids]

skipped_count = (len(plan['coding_tasks']) - len(coding_tasks) +
                 len(plan['research_tasks']) - len(research_tasks) +
                 len(plan['personal_tasks']) - len(personal_tasks))

print(f"✅ Skipped {skipped_count} tickets that already have sessions")
print(f"✅ Creating sessions for {len(coding_tasks)} coding + {len(research_tasks)} research + {len(personal_tasks)} personal tasks")

# STEP 5: NOW create sessions using filtered arrays (not original plan)
for task in coding_tasks:  # Use filtered array!
    # Create session...
    pass

for task in research_tasks:  # Use filtered array!
    # Create session...
    pass

for task in personal_tasks:  # Use filtered array!
    # Create session...
    pass
```

## Why This Keeps Failing

**Orchestrator behavior pattern:**
1. ✅ Generates plan correctly
2. ✅ Reads plan JSON
3. ❌ **NEVER reads state file**
4. ❌ Creates sessions for ALL tasks in plan (no filtering)
5. ✅ Updates state file (too late, damage done)

**The pattern has repeated 8+ times:**
- Every 4-hour run creates duplicates
- State file tracks the duplicates
- But next run ignores the state file
- Cycle repeats

## Impact Analysis

**Total Duplicates by Ticket:**
- "creat website from notebook lm.and Gemini" (69b0f3d5) - 4 duplicates
- "התקנת אינטרנט" (672215e9) - 8 duplicates (4 personal + 4 research)
- "Buy o ring for dishwasher" (69b15139) - 8 duplicates
- **Total: 20 duplicate sessions**

**Board Pollution:**
- Visibility worktree cluttered with 20 orphaned sessions
- Hard to see actual work in progress
- Confusing for human to track what's happening

**Wasted Resources:**
- AI agents running duplicate work
- Multiple sessions trying to solve same problem
- Confusion about which session is authoritative

## Testing the Fix

**Dry-run test before deploying:**

```bash
# Test state checking logic WITHOUT creating sessions
python3 << 'EOF'
import json
import os

# Read state
state_file = 'memory/agor-state/trello-processor.json'
state = json.load(open(state_file))

# Extract active IDs
active = set()
for cat in ['active_coding_sessions', 'active_research_sessions', 'active_personal_sessions']:
    for s in state.get(cat, []):
        active.add(s['ticket_id'])

print(f"Active tickets: {len(active)}")
print(f"Ticket IDs: {active}")

# Read latest plan
import glob
latest_plan = sorted(glob.glob('memory/trello-plan-*.json'))[-1]
plan = json.load(open(latest_plan))

print(f"\nPlan has:")
print(f"  Coding: {len(plan['coding_tasks'])}")
print(f"  Research: {len(plan['research_tasks'])}")
print(f"  Personal: {len(plan['personal_tasks'])}")

# Test filtering
new_coding = [t for t in plan['coding_tasks'] if t['card_id'] not in active]
new_research = [t for t in plan['research_tasks'] if t['card_id'] not in active]
new_personal = [t for t in plan['personal_tasks'] if t['card_id'] not in active]

print(f"\nAfter filtering:")
print(f"  Coding: {len(new_coding)} (skipped {len(plan['coding_tasks']) - len(new_coding)})")
print(f"  Research: {len(new_research)} (skipped {len(plan['research_tasks']) - len(new_research)})")
print(f"  Personal: {len(new_personal)} (skipped {len(plan['personal_tasks']) - len(new_personal)})")

print(f"\n✅ Would create {len(new_coding) + len(new_research) + len(new_personal)} sessions")
print(f"✅ Would skip {len(active)} duplicates")
EOF
```

**Expected output for current state:**
```
Active tickets: 3
Ticket IDs: {'69b0f3d51f042e4bd727ce07', '672215e999cf9c79e0bb303a', '69b151392ad9bcd88525c47c'}

Plan has:
  Coding: 1
  Research: 1
  Personal: 1

After filtering:
  Coding: 0 (skipped 1)
  Research: 0 (skipped 1)
  Personal: 0 (skipped 1)

✅ Would create 0 sessions
✅ Would skip 3 duplicates
```

## Verification Checklist

After implementing fix, verify:

- [ ] State file is read BEFORE creating any sessions
- [ ] Active ticket IDs are extracted from ALL categories
- [ ] Plan tasks are filtered against active ticket IDs
- [ ] Only NEW tickets (not in state) get sessions
- [ ] Log shows "Skipped X tickets (already active)"
- [ ] Next run creates 0 duplicates
- [ ] State file duplicate count stops increasing

## Monitoring After Fix

**Add to daily logs:**
```markdown
### Trello Processing - HH:MM (Scheduled)

**Duplicate Prevention:**
- Active tickets: X
- New tickets: Y
- Skipped: Z (already active)
- Sessions created: Y (only new)
- Duplicates prevented: Z

✅ No duplicates created!
```

## Files to Update

1. **Orchestrator prompt** (CRITICAL!) - Add state checking BEFORE session creation
2. `memory/agor-state/trello-processor.json` - Already tracking duplicates
3. `memory/YYYY-MM-DD.md` - Log each run's duplicate prevention stats
4. `skills/trello-ticket-processor.md` - Document the fix

---

## 🆕 UPDATE: 2026-03-19 08:01 Run (Latest Failure)

### What Happened

Created 2 MORE duplicate sessions:
- ❌ d391afc7 - "התקנת אינטרנט" (DUPLICATE #8) - Already had 7 sessions!
- ❌ d8680b71 - "Buy o ring for dishwasher" (DUPLICATE #8) - Already had 7 sessions!

### Critical Analysis

**The orchestrator has now:**
- Created duplicates 8 consecutive times
- Ignored state file 8 times
- Created 20 total duplicate sessions
- Demonstrated it NEVER learns from previous runs

**Conclusion:** The orchestrator prompt/workflow is fundamentally broken and needs complete rewrite.

### Required Changes

**Update the orchestrator session initial prompt to:**

```
You are the orchestrator - delegate each ticket to a named session in the visibility worktree.

## Step 1: Generate Execution Plan

Run the ticket processor:
uv run utils/process_trello_tickets.py

## Step 2: Read State File FIRST! (CRITICAL!)

BEFORE creating ANY sessions, check for existing work:

import json
state = json.load(open('memory/agor-state/trello-processor.json'))
active_tickets = set()
for cat in ['active_coding_sessions', 'active_research_sessions', 'active_personal_sessions']:
    for s in state.get(cat, []):
        active_tickets.add(s['ticket_id'])

## Step 3: Read Plan and Filter

plan = json.load(open('memory/trello-plan-*.json'))  # latest
coding = [t for t in plan['coding_tasks'] if t['card_id'] not in active_tickets]
research = [t for t in plan['research_tasks'] if t['card_id'] not in active_tickets]
personal = [t for t in plan['personal_tasks'] if t['card_id'] not in active_tickets]

## Step 4: Create Sessions ONLY for Filtered Tasks

(Use filtered arrays: coding, research, personal - NOT plan arrays!)
```

### Next Run: 12:00

**Expected behavior if fix is applied:**
- Plan will have 3 tasks (same tickets)
- State has 3 active tickets
- Filter will result in 0 new tasks
- **Should create:** 0 sessions
- **Will create (if still broken):** 2 duplicates (#9)

---

**Status:** ❌ CRITICAL FAILURE - 20 duplicates and counting
**Next Run:** 12:00 (in 4 hours)
**Action Required:** FIX ORCHESTRATOR PROMPT IMMEDIATELY
**Urgency:** MAXIMUM - Every run creates more duplicates
