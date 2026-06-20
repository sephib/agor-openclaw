# Heartbeat Sync Protocol — External Sync (Jira & PRs)

*This file is the protocol for the "External Sync — Jira & PRs" schedule (daily 8am).*

This sync runs once daily at 8am to reconcile external system state (Jira + GitHub) against BOARD_STATE.md. It is separate from the advance heartbeat (which runs every 30min) and focuses on cross-system consistency rather than CI monitoring.

---

## Step 1 — Read current board state

```
Read _manager/BOARD_STATE.md
```

Note the last-updated timestamp. If older than 30 minutes, the advance heartbeat may not have run — proceed anyway but flag this.

---

## Step 2 — Jira sprint snapshot

Pull current sprint tickets assigned to Joseph Berry:

Via Jira MCP: search for tickets in the active sprint assigned to Joseph Berry.

For each ticket, record:
- Ticket key, summary, status
- Is there a matching worktree in BOARD_STATE.md?
- Does the Jira status match the board zone? (e.g., Jira "In Review" should match board "Code Review")

Flag mismatches:
- Jira Done + board still active → stale, propose archival
- Jira In Progress + no worktree → missing worktree, flag for Joseph
- Jira In Review + PR not open → inconsistency

---

## Step 3 — PR state sweep

For each PR tracked in BOARD_STATE.md (active AND recently merged):

```bash
gh pr list --state all --repo Jounce-IO/jounce --limit 30 \
  --json number,state,mergedAt,closedAt,title,headRefName
```

Cross-check against BOARD_STATE.md. Flag:
- PR closed/merged but still in Active Worktrees table
- PR state changed since last advance heartbeat

---

## Step 4 — Update BOARD_STATE.md if needed

If Step 2 or 3 found discrepancies, update BOARD_STATE.md and note them in the Key Changes section.

---

## Step 5 — Write sync summary to RUN_LOG.md

```
## HH:MM IDT — Daily External Sync
- Jira tickets checked: N
- Mismatches found: ...
- PR state discrepancies: ...
- Updates made to BOARD_STATE.md: yes/no
```

---

## Step 6 — Commit and push

```bash
git add _manager/ && git commit -m "chore: HH:MM IDT daily sync — <summary>" && git push origin private-julie
```

*Created: 2026-06-20*
