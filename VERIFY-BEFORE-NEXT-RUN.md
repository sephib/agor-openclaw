# ✅ Verification Checklist - Before Next Scheduled Run

**Purpose:** Ensure the duplicate prevention system is working before the next 4-hour run.

**Estimated Time:** 10 minutes

---

## Quick Verification Steps

### 1. Test the System (5 minutes)

```bash
# Run the test suite
cd /Users/josephberry/.agor/worktrees/local/agor-openclaw/trello-task-processor
python3 utils/test_duplicate_prevention.py
```

**Expected output:**
```
🧪 DUPLICATE PREVENTION TEST SUITE
✅ PASS: All tickets have sessions → creates 0
✅ PASS: All tickets are new → creates all
✅ PASS: Mixed scenario → creates only new ones
✅ PASS: Duplicate detection in verification
📊 TEST RESULTS: 4 passed, 0 failed
```

**If tests fail:** Check the error messages and fix before proceeding.

---

### 2. Verify Trigger Script (2 minutes)

```bash
# Check that pre-flight verification is integrated
grep -A 5 "PRE-FLIGHT VERIFICATION" utils/trigger-ticket-processor.sh
```

**Expected output:** Should show verification logic:
```bash
# PRE-FLIGHT VERIFICATION: Check for potential duplicates
log "Running pre-flight verification..."
if python3 "$WORKSPACE_ROOT/utils/verify_no_duplicates.py" ...
```

**If missing:** The trigger script wasn't updated. Review DUPLICATE-PREVENTION-SYSTEM.md.

---

### 3. Check Current State (2 minutes)

```bash
# View current active sessions
jq '{
  coding: (.active_coding_sessions | length),
  research: (.active_research_sessions | length),
  personal: (.active_personal_sessions | length),
  total: ((.active_coding_sessions + .active_research_sessions + .active_personal_sessions) | length)
}' memory/agor-state/trello-processor.json
```

**Expected output:**
```json
{
  "coding": 1,
  "research": 0,
  "personal": 5,
  "total": 6
}
```

Note the total count. Compare this with Agor MCP in next step.

---

### 4. Detect Existing Duplicates via MCP (3 minutes)

**IMPORTANT:** This must be run from an Agor session (not standalone).

**Option A: Create temporary Agor session**

```bash
# Open Agor UI
open http://localhost:3030/w/d1ed5f5a-1937-4687-bb6c-325adb69a4f9

# Create new session in this worktree
# Paste this code into the session:
```

```python
import sys
from pathlib import Path
sys.path.insert(0, 'utils')
from detect_duplicates_mcp import generate_duplicate_report, print_duplicate_report

# Query all sessions in visibility-hub
sessions_result = mcp__agor__agor_sessions_list(
    worktreeId='659dbc25-b301-4e2c-ab26-c07cd1737fcb',
    limit=500
)

# Generate duplicate report
report = generate_duplicate_report(
    sessions=sessions_result['data'],
    output_file=Path('memory/verification-reports/pre-run-duplicate-scan.json')
)

# Print report
print_duplicate_report(report)

# Summary
if report['analysis']['stats']['duplicate_tickets'] > 0:
    print(f"⛔ {report['analysis']['stats']['duplicate_tickets']} DUPLICATE TICKETS FOUND")
    print("   Review report and clean up before next run")
else:
    print("✅ NO DUPLICATES - System is healthy")
```

**Expected output:**
```
📊 STATISTICS:
   Total sessions: 30-50
   Unique tickets: 6
   Duplicate tickets: 0 ✅

✅ NO DUPLICATE SESSIONS FOUND

🔄 STATE FILE COMPARISON:
   Tickets in state: 6
   Tickets in MCP: 6
   In both: 6
   State only: 0
   MCP only: 0

✅ NO ISSUES FOUND
```

**If duplicates found:** Clean them up before next run (see DUPLICATE-PREVENTION-SYSTEM.md Recovery section).

---

### 5. Dry-Run Test (Optional - 5 minutes)

**Test the full flow without creating sessions:**

```bash
# Manually trigger to see what would happen
./utils/trigger-ticket-processor.sh
```

**Watch for:**
```
Running pre-flight verification...
✓ Pre-flight verification passed
Work to process: X updates, Y creates
```

**If verification fails:**
```
⛔ DUPLICATE RISK DETECTED - ABORTING
Check verification report in memory/verification-reports/
```

This means the system is working correctly (preventing duplicates).

---

### 6. Verify Scheduling Configuration (2 minutes)

**Check that the schedule is using the correct trigger script:**

```bash
# If using Agor native scheduling (from worktree notes)
cat <<EOF
Expected schedule config:
- Schedule Enabled: TRUE
- Schedule Cron: 0 */4 * * * (every 4 hours)
- Runs trigger script: utils/trigger-ticket-processor.sh
EOF

# If using system cron
crontab -l | grep trello || echo "Not using system cron"
```

**Verify:** The schedule points to `utils/trigger-ticket-processor.sh` (not a copy or old version).

---

## Summary Checklist

Before next run, verify:

- [ ] ✅ Test suite passes (4/4 tests)
- [ ] ✅ Trigger script has verification integrated
- [ ] ✅ State file shows reasonable ticket count (6-10 typical)
- [ ] ✅ MCP duplicate scan shows 0 duplicates
- [ ] ✅ State vs MCP comparison shows 0 mismatches
- [ ] ✅ Schedule configuration points to correct trigger script
- [ ] ✅ Dry-run test succeeds (or shows verification working)

**If ALL checked:** ✅ **System is ready. Next run should create 0 duplicates.**

**If ANY failed:** ⛔ **Fix issues before next scheduled run.**

---

## What to Watch After Next Run

**Immediately after next scheduled run (within 5 minutes):**

1. Check if new action file was created:
   ```bash
   ls -lt memory/trello-actions-*.json | head -1
   ```

2. Check verification report:
   ```bash
   ls -lt memory/verification-reports/ | head -1
   cat memory/verification-reports/verification-pre-flight-*.json
   ```

3. Check stats in action file:
   ```bash
   LATEST=$(ls -t memory/trello-actions-*.json | head -1)
   jq '.stats' "$LATEST"
   ```

4. Run MCP duplicate scan again:
   ```python
   # (Same as step 4 above)
   # Compare before vs after - duplicate count should NOT increase
   ```

**Success indicators:**
- ✅ Actions file created
- ✅ Verification report shows 0 issues
- ✅ Creates count is reasonable (0-3, not 22)
- ✅ MCP duplicate scan shows same or fewer duplicates

**Failure indicators:**
- ❌ No actions file created → trigger script not running
- ❌ Verification report has issues → pre-flight caught problems
- ❌ Creates count too high → generate_actions logic broken
- ❌ MCP shows NEW duplicates → system bypassed somehow

---

## Emergency Stop

**If you see duplicates being created:**

```bash
# 1. Stop the schedule immediately
# (How depends on scheduling system - Agor UI or crontab -e)

# 2. Run MCP duplicate detector to assess damage

# 3. Check logs in memory/logs/trello-processor-*.log

# 4. Review last actions file to see what was attempted

# 5. Fix root cause before re-enabling schedule
```

---

**Last Updated:** 2026-03-19
**Next Review:** After next scheduled run (check within 5 minutes of 00:00, 04:00, 08:00, 12:00, 16:00, or 20:00 UTC)
