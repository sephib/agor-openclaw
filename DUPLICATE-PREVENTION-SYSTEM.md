# Duplicate Prevention System

**Status:** ✅ Implemented
**Last Updated:** 2026-03-19
**Bug Report:** 22+ duplicates created before cleanup; 20:01 run created 3 new duplicates

---

## Problem Statement

The Trello ticket processor was creating **duplicate sessions** for the same Trello card every 4 hours. This resulted in:

- 22+ duplicate sessions created before cleanup
- **3 NEW duplicates at 20:01 run** despite initial fix attempts
- State file out of sync with Agor MCP reality
- No pre-flight verification to prevent duplicates

**Root Cause:**
1. Scheduled cron may not be using the updated trigger script
2. Orchestrator wasn't executing pre-computed actions correctly
3. No defensive checks to abort if duplicates would be created

---

## Solution Architecture

### 1. Pre-computed Action System

**File:** `utils/generate_actions.py`

**What it does:**
- Reads the state file (`memory/agor-state/trello-processor.json`)
- Reads the execution plan (`memory/trello-plan-*.json`)
- For each ticket, decides: **UPDATE** existing session OR **CREATE** new session
- Outputs decision file (`memory/trello-actions-*.json`)

**Key logic:**
```python
if ticket_id in active_sessions:
    action = "update"  # Send prompt to existing session
else:
    action = "create"  # Create new session
```

### 2. Verification System

**File:** `utils/verify_no_duplicates.py`

**Features:**
- Pre-flight checks before creating sessions
- Verifies plan file exists and is valid
- Verifies actions file exists and has correct structure
- **Detects CREATE actions for tickets already in state** (duplicate risk)
- Post-run verification
- Detailed JSON reporting

**Exit codes:**
- `0`: No duplicates found ✅
- `1`: Duplicates detected ⛔ (ABORT)
- `2`: Configuration issues ⚠️

### 3. MCP Duplicate Detector

**File:** `utils/detect_duplicates_mcp.py`

**Purpose:** Query Agor MCP to find actual duplicate sessions

**Must be run from within Agor session** (has MCP access)

**What it detects:**
- Tickets with multiple sessions in Agor
- State file vs MCP mismatches
- Orphaned sessions (no ticket ID)
- Sessions in state but not in MCP (and vice versa)

### 4. Integration with Trigger Script

**File:** `utils/trigger-ticket-processor.sh`

**Updated workflow:**

```bash
1. Run process_trello_tickets.py (generate plan)
2. Find latest plan file
3. ✅ CRITICAL: Run generate_actions.py (decides UPDATE vs CREATE)
4. ✅ NEW: Run verify_no_duplicates.py (pre-flight check)
   - If duplicates detected → ABORT ⛔
   - If configuration issues → WARN but continue ⚠️
5. Create orchestrator session (with pre-computed actions)
6. Orchestrator executes actions (UPDATE or CREATE)
```

---

## How to Use

### Before Next Scheduled Run

**1. Verify the trigger script is correct:**
```bash
cat utils/trigger-ticket-processor.sh | grep -A 10 "PRE-FLIGHT VERIFICATION"
```

Should show verification logic.

**2. Check that cron is using the right script:**
```bash
# If using cron
crontab -l | grep trello

# If using Agor scheduling
# Check worktree notes or session metadata
```

**3. Manually test the verification:**
```bash
# Find latest plan
LATEST_PLAN=$(ls -t memory/trello-plan-*.json | head -1)

# Generate actions
python3 utils/generate_actions.py "$LATEST_PLAN"

# Find latest actions file
LATEST_ACTIONS=$(ls -t memory/trello-actions-*.json | head -1)

# Run verification
python3 utils/verify_no_duplicates.py \
    --mode pre-flight \
    --plan-file "$LATEST_PLAN" \
    --actions-file "$LATEST_ACTIONS"

# Check exit code
echo "Exit code: $?"
# 0 = safe to proceed
# 1 = duplicates would be created (ABORT)
# 2 = configuration issues
```

### Manual Duplicate Detection (via Agor MCP)

**Run this from an Agor session:**

```python
import sys
sys.path.insert(0, 'utils')
from detect_duplicates_mcp import generate_duplicate_report, print_duplicate_report

# Query sessions in visibility-hub worktree
sessions_result = mcp__agor__agor_sessions_list(
    worktreeId='659dbc25-b301-4e2c-ab26-c07cd1737fcb',
    limit=500
)

# Generate report
report = generate_duplicate_report(
    sessions=sessions_result['data'],
    output_file=Path('memory/verification-reports/duplicate-scan-latest.json')
)

# Print report
print_duplicate_report(report)

# Decision
if report['analysis']['stats']['duplicate_tickets'] > 0:
    print("⛔ DUPLICATES EXIST - Need cleanup")
else:
    print("✅ No duplicates")
```

### Run Test Suite

**Verify the fix works correctly:**

```bash
python3 utils/test_duplicate_prevention.py
```

**Expected output:**
```
✅ PASS: All tickets have sessions → creates 0
✅ PASS: All tickets are new → creates all
✅ PASS: Mixed scenario → creates only new ones
✅ PASS: Duplicate detection in verification

📊 TEST RESULTS: 4 passed, 0 failed
```

---

## Debugging Workflow

### If Duplicates Are Created Again

**1. Identify when it happened:**
```bash
ls -lt memory/trello-actions-*.json | head -5
```

**2. Check verification reports:**
```bash
ls -lt memory/verification-reports/ | head -5
cat memory/verification-reports/verification-pre-flight-*.json
```

**3. Check if actions file was created:**
```bash
# Should have matching timestamps
ls -lt memory/trello-plan-*.json | head -3
ls -lt memory/trello-actions-*.json | head -3
```

If actions file is **missing** → `generate_actions.py` wasn't called → trigger script not being used.

**4. Check what actions were generated:**
```bash
LATEST_ACTIONS=$(ls -t memory/trello-actions-*.json | head -1)
jq '.stats' "$LATEST_ACTIONS"
jq '.actions[] | select(.action == "create")' "$LATEST_ACTIONS"
```

If `creates > 0` for tickets already in state → `generate_actions.py` logic bug.

**5. Verify state file accuracy:**
```bash
jq '.active_personal_sessions | length' memory/agor-state/trello-processor.json
```

Compare against Agor MCP session count (run MCP detector).

**6. Check orchestrator session:**
Find the orchestrator session that ran:
```bash
# Look for sessions in trello-task-processor worktree
# Check initial prompt - should reference actions file
```

**7. Verify cron/schedule configuration:**
```bash
# If using cron
crontab -l

# If using Agor scheduling
# Check worktree metadata for schedule configuration
```

---

## Configuration

### Key Files

| File | Purpose | Updated By |
|------|---------|------------|
| `memory/agor-state/trello-processor.json` | Tracks active sessions | Orchestrator after CREATE/UPDATE |
| `memory/trello-plan-*.json` | Execution plan from Trello | `process_trello_tickets.py` |
| `memory/trello-actions-*.json` | Pre-computed actions | `generate_actions.py` |
| `memory/verification-reports/` | Verification results | `verify_no_duplicates.py` |

### Important IDs

- **Orchestrator Worktree:** `d1ed5f5a-1937-4687-bb6c-325adb69a4f9` (trello-task-processor)
- **Visibility Hub Worktree:** `659dbc25-b301-4e2c-ab26-c07cd1737fcb` (where ticket sessions live)
- **Board ID:** `1a508c77-dacb-46fe-ab24-e527fb476882`

### Scheduling

**Current setup:**
- Schedule: Every 4 hours (`0 */4 * * *`)
- Runs: 00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC
- Trigger: `utils/trigger-ticket-processor.sh`

**Verification points:**
1. ✅ Before creating orchestrator session (pre-flight)
2. ✅ Actions file validates against state
3. ⏳ TODO: Post-run verification (after orchestrator completes)

---

## Success Criteria

**The system is working correctly if:**

1. ✅ `generate_actions.py` is called on every run
2. ✅ Actions file is created with correct CREATE/UPDATE decisions
3. ✅ Pre-flight verification runs and aborts if duplicates detected
4. ✅ State file stays in sync with Agor MCP reality
5. ✅ No new duplicate sessions are created (verified via MCP)
6. ✅ Test suite passes all 4 tests

**Monitor these metrics:**
- Number of CREATE actions per run (should be 0-3, not 22!)
- State file ticket count vs MCP session count (should match)
- Verification reports (should have 0 issues)

---

## Recovery Procedures

### If Duplicates Already Exist

**1. Detect duplicates via MCP:**
```python
# Run from Agor session (see "Manual Duplicate Detection" above)
```

**2. Mark duplicates for deletion:**
For each duplicate set, keep the **earliest created** session, mark others.

**3. Update state file:**
Remove duplicate entries from:
- `active_coding_sessions`
- `active_research_sessions`
- `active_personal_sessions`

**4. Archive duplicate sessions:**
```python
# Via Agor MCP (if API supports)
# Or manually via UI
```

---

## Testing Strategy

### Unit Tests

**File:** `utils/test_duplicate_prevention.py`

**Test cases:**
1. ✅ All tickets have sessions → creates 0
2. ✅ All tickets are new → creates all
3. ✅ Mixed scenario → creates only new
4. ✅ Verification detects duplicate risk

### Integration Tests

**Manual dry-run:**
1. Create mock state with 3 tickets
2. Create plan with 3 same + 2 new tickets
3. Run `generate_actions.py` → expect 3 updates, 2 creates
4. Run `verify_no_duplicates.py` → expect 0 issues
5. Verify output files are correct

### End-to-End Test

**Safe test run:**
1. Disable actual session creation (comment out in trigger script)
2. Run trigger script manually
3. Verify actions file is correct
4. Verify verification passes
5. Check logs for any errors

---

## Future Improvements

**High Priority:**
- [ ] Post-run verification (detect if duplicates were created despite checks)
- [ ] Auto-sync state file with MCP reality on every run
- [ ] Alert system if duplicates detected (Slack/email)

**Medium Priority:**
- [ ] Store ticket ID explicitly in session metadata (not just in prompt)
- [ ] MCP query optimization (batch queries, caching)
- [ ] Automated cleanup of old plan/action files

**Low Priority:**
- [ ] Dashboard showing duplicate stats over time
- [ ] Rollback mechanism if bad run detected
- [ ] Canary deployments for trigger script changes

---

## Contact & Support

**Created:** 2026-03-19
**Author:** Claude (Duplicate Prevention Task)
**Worktree:** trello-task-processor
**Session:** `c355ad94-ecfb-4915-bbce-9777be1034d2`

**For issues:**
1. Check verification reports in `memory/verification-reports/`
2. Run test suite: `python3 utils/test_duplicate_prevention.py`
3. Run MCP duplicate detector from Agor session
4. Review this documentation

---

## Appendix: File Formats

### Actions File Schema

```json
{
  "generated_at": "2026-03-19T20:00:00Z",
  "plan_file": "memory/trello-plan-20260319-200000.json",
  "stats": {
    "updates": 3,
    "creates": 0,
    "skipped": 0
  },
  "actions": [
    {
      "action": "update",
      "session_id": "abc123...",
      "ticket_id": "672215e999cf9c79e0bb303a",
      "title": "Ticket title",
      "category": "personal",
      "task": { /* full task object */ }
    }
  ],
  "active_sessions_count": 3
}
```

### Verification Report Schema

```json
{
  "timestamp": "2026-03-19T20:00:00Z",
  "mode": "pre-flight",
  "checks": {
    "state_file": {
      "status": "pass",
      "ticket_count": 7,
      "tickets": ["672215e...", ...]
    },
    "actions_file": {
      "status": "pass",
      "update_count": 3,
      "create_count": 0
    }
  },
  "issues": [],
  "duplicates_found": false,
  "summary": {
    "total_checks": 3,
    "passed": 3,
    "failed": 0,
    "duplicates_found": false
  }
}
```
