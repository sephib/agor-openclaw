# Duplicate Prevention Workflow

## System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SCHEDULED TRIGGER (Every 4 hours)             │
│                   utils/trigger-ticket-processor.sh              │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: Generate Execution Plan                                │
│  ────────────────────────────────                               │
│  Script: utils/process_trello_tickets.py                        │
│  Input:  Trello API (fetch active cards)                        │
│  Output: memory/trello-plan-YYYYMMDD-HHMMSS.json               │
│                                                                  │
│  Contains: coding_tasks[], research_tasks[], personal_tasks[]   │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: Pre-compute Actions (UPDATE vs CREATE)                 │
│  ────────────────────────────────────────────                   │
│  Script: utils/generate_actions.py                              │
│  Input:  - Plan file (from step 1)                              │
│          - State file (memory/agor-state/trello-processor.json) │
│  Logic:  For each ticket:                                       │
│            if ticket_id IN state → action="update"              │
│            else                  → action="create"              │
│  Output: memory/trello-actions-YYYYMMDD-HHMMSS.json            │
│                                                                  │
│  Contains: stats{updates, creates}, actions[{action, ...}]      │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: PRE-FLIGHT VERIFICATION ⚠️  CRITICAL!                  │
│  ────────────────────────────────────────────                   │
│  Script: utils/verify_no_duplicates.py                          │
│  Input:  - Plan file                                            │
│          - Actions file                                         │
│          - State file                                           │
│  Checks: 1. State file exists and valid ✓                       │
│          2. Plan file exists and valid ✓                        │
│          3. Actions file exists and valid ✓                     │
│          4. NO CREATE for tickets in state ✓ ← KEY CHECK!       │
│  Output: - Verification report (JSON)                           │
│          - Exit code: 0=safe, 1=duplicates, 2=issues           │
└─────────────────────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┴────────────┐
                    │                          │
              Exit Code 1                  Exit Code 0
              (Duplicates!)                (Safe)
                    │                          │
                    ▼                          ▼
        ┌────────────────────┐    ┌────────────────────────┐
        │  ⛔ ABORT          │    │  ✅ CONTINUE           │
        │  DO NOT PROCEED     │    │  Create Orchestrator   │
        │  Log error          │    │  Session               │
        │  Save report        │    └────────────────────────┘
        └────────────────────┘                 │
                                              ▼
                              ┌──────────────────────────────┐
                              │  STEP 4: Create Orchestrator │
                              │  ──────────────────────────── │
                              │  Worktree: trello-task-      │
                              │            processor         │
                              │  Prompt: Execute actions     │
                              │          from actions file   │
                              └──────────────────────────────┘
                                              │
                                              ▼
                              ┌──────────────────────────────┐
                              │  STEP 5: Execute Actions     │
                              │  ──────────────────────────── │
                              │  For each action in file:    │
                              │                              │
                              │  if action=="update":        │
                              │    → mcp_sessions_prompt()   │
                              │      (send to existing)      │
                              │                              │
                              │  if action=="create":        │
                              │    → mcp_sessions_create()   │
                              │      (in visibility-hub)     │
                              │    → track_in_state()        │
                              │                              │
                              │  Save state file             │
                              └──────────────────────────────┘
```

---

## Data Flow

```
Trello Cards
    │
    ▼
┌─────────────┐
│ Plan File   │  Contains: All top-priority tickets
│ (JSON)      │  Structure: {coding_tasks[], research_tasks[], ...}
└─────────────┘
    │
    ▼
┌─────────────┐      ┌─────────────┐
│ Actions     │ ◄──── │ State File  │  Tracks: Active sessions by ticket_id
│ Generator   │      │ (JSON)      │
└─────────────┘      └─────────────┘
    │
    ▼
┌─────────────┐
│ Actions File│  Contains: Pre-computed UPDATE/CREATE decisions
│ (JSON)      │  Structure: {stats{}, actions[{action, ticket_id, ...}]}
└─────────────┘
    │
    ▼
┌─────────────┐
│ Verifier    │  Validates: No CREATE for existing tickets
└─────────────┘
    │
    ├─── ❌ Duplicates → ABORT
    │
    └─── ✅ Safe → Continue
              │
              ▼
         ┌─────────────┐
         │ Orchestrator│  Executes: Actions from file
         │ Session     │
         └─────────────┘
              │
              ▼
         ┌─────────────┐
         │ Ticket      │  Created/Updated: In visibility-hub worktree
         │ Sessions    │
         └─────────────┘
              │
              ▼
         ┌─────────────┐
         │ State File  │  Updated: With new/updated session info
         │ (JSON)      │
         └─────────────┘
```

---

## Verification Points

```
1. State File Validation
   ├─ File exists? ✓
   ├─ Valid JSON? ✓
   └─ Has ticket_ids? ✓

2. Plan File Validation
   ├─ File exists? ✓
   ├─ Valid JSON? ✓
   └─ Has tasks? ✓

3. Actions File Validation
   ├─ File exists? ✓
   ├─ Valid JSON? ✓
   ├─ Has actions? ✓
   └─ Stats match? ✓

4. Duplicate Detection (CRITICAL)
   ├─ For each CREATE action:
   │  └─ Is ticket_id in state?
   │     ├─ YES → ⛔ DUPLICATE RISK
   │     └─ NO  → ✅ Safe to create
   └─ Exit accordingly

5. MCP Cross-Check (Manual)
   ├─ Query sessions in visibility-hub
   ├─ Group by ticket_id
   ├─ Find duplicates (count > 1)
   └─ Compare with state file
```

---

## File Locations

```
trello-task-processor/
│
├── utils/
│   ├── process_trello_tickets.py     [Step 1: Generate plan]
│   ├── generate_actions.py           [Step 2: Pre-compute actions]
│   ├── verify_no_duplicates.py       [Step 3: Verification]
│   ├── detect_duplicates_mcp.py      [MCP duplicate detector]
│   ├── test_duplicate_prevention.py  [Test suite]
│   ├── session_manager.py            [Helper functions]
│   └── trigger-ticket-processor.sh   [Main trigger script]
│
├── memory/
│   ├── agor-state/
│   │   └── trello-processor.json     [State file - active sessions]
│   │
│   ├── verification-reports/
│   │   └── verification-*.json       [Verification results]
│   │
│   ├── trello-plan-*.json            [Execution plans]
│   └── trello-actions-*.json         [Pre-computed actions]
│
└── docs/
    ├── DUPLICATE-PREVENTION-SYSTEM.md    [Complete docs]
    ├── VERIFY-BEFORE-NEXT-RUN.md         [Quick checklist]
    ├── SOLUTION-SUMMARY.md               [Overview]
    └── WORKFLOW-DIAGRAM.md               [This file]
```

---

## Decision Tree

```
                    New ticket in plan?
                           │
            ┌──────────────┴──────────────┐
            │                             │
           YES                           NO
            │                             │
            ▼                             ▼
    Ticket in state file?         Already being processed
            │                     → Skip or log
    ┌───────┴───────┐
    │               │
   YES             NO
    │               │
    ▼               ▼
 UPDATE         CREATE
existing        new
session       session
    │               │
    │               ▼
    │         Check: Would create duplicate?
    │               │
    │       ┌───────┴────────┐
    │       │                │
    │      YES              NO
    │       │                │
    │       ▼                │
    │   ⛔ ABORT             │
    │   (verification)       │
    │                        │
    └────────┬───────────────┘
             │
             ▼
     ✅ Execute action
```

---

## Monitoring Dashboard (Conceptual)

```
╔═══════════════════════════════════════════════════════════════╗
║            TRELLO TICKET PROCESSOR - STATUS                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Last Run: 2026-03-19 20:00 UTC                              ║
║  Next Run: 2026-03-20 00:00 UTC (in 3h 45m)                  ║
║  Status:   ✅ Healthy                                         ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  ACTIVE SESSIONS                                              ║
║  ────────────────                                             ║
║  Coding:    1                                                 ║
║  Research:  0                                                 ║
║  Personal:  5                                                 ║
║  Total:     6                                                 ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  LAST RUN STATISTICS                                          ║
║  ───────────────────                                          ║
║  Tickets in plan:     3                                       ║
║  Updates sent:        3                                       ║
║  New sessions:        0  ✅ (was 22 before fix)               ║
║  Duplicates detected: 0  ✅                                    ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  VERIFICATION STATUS                                          ║
║  ──────────────────                                           ║
║  Pre-flight:  ✅ PASS (0 issues)                              ║
║  Test suite:  ✅ PASS (4/4 tests)                             ║
║  MCP scan:    ✅ 0 duplicates                                 ║
║  State sync:  ✅ Matches MCP                                  ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  ALERTS                                                       ║
║  ──────                                                       ║
║  None                                                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Quick Command Reference

```bash
# Test the system
python3 utils/test_duplicate_prevention.py

# Manual verification
python3 utils/verify_no_duplicates.py \
    --mode manual \
    --plan-file memory/trello-plan-latest.json \
    --actions-file memory/trello-actions-latest.json

# Detect duplicates (run from Agor session)
python3 << 'EOF'
import sys
sys.path.insert(0, 'utils')
from detect_duplicates_mcp import generate_duplicate_report, print_duplicate_report

sessions = mcp__agor__agor_sessions_list(
    worktreeId='659dbc25-b301-4e2c-ab26-c07cd1737fcb',
    limit=500
)
report = generate_duplicate_report(sessions['data'])
print_duplicate_report(report)
EOF

# Check state file
jq '.active_personal_sessions | length' memory/agor-state/trello-processor.json

# View latest action stats
jq '.stats' $(ls -t memory/trello-actions-*.json | head -1)
```

---

**Visual Guide Created:** 2026-03-19
**Workflow Version:** 2.0 (with verification)
**Status:** ✅ Production Ready
