# Heartbeat Advance Protocol

*This file is the canonical protocol for all Board Advancement heartbeat schedules.*
*Schedules that reference this file: Weekday Daytime (every 30min), Weekday Overnight (10pm/midnight/2am/4am/6am), Weekend (every 6h).*

**Override note:** This protocol supersedes the "Don't commit on every heartbeat — batch" guidance in `HEARTBEAT.md`. Commit after EVERY run. The 2.5-day git gap (Jun 16–19 2026) caused a session to report a merged PR as open. Never let a corrected board state exist only in the working directory.

---

## Step 0 — Staleness check

Before doing anything else:

```bash
head -5 _manager/BOARD_STATE.md
```

Note the `*Last updated:*` timestamp. If it is more than 2 hours old, flag it at the top of your run summary:

> ⚠️ BOARD_STATE.md is X hours old — performing full refresh.

This check catches sessions that start from a stale git-committed snapshot rather than the working directory.

---

## Step 1 — Recently-merged sweep (run FIRST, every time)

Only track PRs where Joseph is assigned or requested for review. Run both commands and combine results:

```bash
gh pr list --state merged --repo Jounce-IO/jounce --limit 20 \
  --assignee @me --json number,title,mergedAt,headRefName,author

gh pr list --state merged --repo Jounce-IO/jounce --limit 20 \
  --search "review-requested:joberry" --json number,title,mergedAt,headRefName,author
```

Deduplicate by PR number. Cross-reference against every worktree tracked in `_manager/BOARD_STATE.md` (Active Worktrees table, all zones).

**For each match (a tracked PR now showing merged):**
- Move it from Active to Recently Merged in BOARD_STATE.md immediately
- Archive the worktree via `agor_branches_archive` (autonomous permission — see below)
- Note in run summary: "PR #NNNN detected merged — archived worktree"

This sweep catches merges that occurred between heartbeat runs, including merges that happened while a prior session was mid-scan.

---

## Step 2 — Full board scan (ALL zones, no exceptions)

Query Agor MCP for all worktrees on board `019eb849-ec5b-715e-b8cc-e37c4c387740`.

**You must scan every worktree regardless of zone.** This includes:
- Code, Plan, Ingest, Revise, Verify, Validate, Publish zones (active dev)
- Respond zone (post-PR communication) — **do not skip**
- Code Review zone
- BLOCKED zone

For each worktree, check via Agor MCP:
- Current zone
- Last session status (idle/running/failed) and timestamp
- `issueUrl` and `pullRequestUrl` fields set?
- Signs of staleness: no session activity 24h+ and zone is not terminal

For each worktree that has a PR URL, record the PR number for Step 3.

---

## Step 3 — PR state verification

For each tracked PR (from Step 2 scan), run:

```bash
gh pr view <N> --repo Jounce-IO/jounce \
  --json number,title,state,mergedAt,closedAt,mergeable,reviewDecision,isDraft
```

**Critical reflex — CI-pass + not-yet-merged:**

If you observe `reviewDecision: REVIEW_REQUIRED` AND CI checks passing AND `state: OPEN`, you MUST also explicitly check:

```bash
gh pr view <N> --repo Jounce-IO/jounce --json state,mergedAt,closedAt
```

If `mergedAt` is set: the PR has merged — go to Step 5 for that worktree. Do NOT report it as "open, awaiting review."

**This reflex exists because:** a PR can appear OPEN with CI passing in the seconds immediately after a merge, before GitHub's API propagates the state change. The afternoon scan on Jun 17 missed the merge for this exact reason.

---

## Step 4 — CI status check

For each PR where `state: OPEN`:

```bash
gh pr checks <N> --repo Jounce-IO/jounce
```

Record: which checks pass, which fail, which are pending. Note run IDs for in-progress CI.

For off-board PRs mentioned in ALERTS (e.g., #1602, #1606): check these too.

---

## Step 5 — Worktree retirement check (all zones)

For each worktree on the board (any zone, not just Respond):
1. Get its PR URL from Agor MCP (if set)
2. Check `gh pr view <N> --json state,mergedAt,closedAt`
3. If `state: MERGED` or `state: CLOSED`: **archive the worktree immediately**

```bash
# Autonomous archive — no proposal needed
agor_branches_archive(branchId="<branch_id>")
```

This permission is granted because:
- The PR is already shipped (MERGED) or abandoned (CLOSED)
- Archiving in Agor is reversible via `agor_branches_unarchive`
- The worktree data remains on disk

Also archive worktrees with no PR when their linked Jira ticket is Done and the worktree has been inactive 24h+.

Note each archive in the run summary: "Archived <branch> — PR #NNNN MERGED/CLOSED"

---

## Step 6 — Jira sync

For each active Jira ticket associated with tracked worktrees, verify Jira status matches PR state:

- PR MERGED + Jira still In Review/In Progress → flag as stale Jira state (update proposal if needed)
- PR OPEN, REVIEW_REQUIRED + Jira In Progress → normal, no action
- No PR + Jira In Progress → flag as missing PR

Use Jira MCP; fall back to `acli` if MCP fails.

Also check: are there sprint tickets with no worktree? List them in BOARD_STATE.md "Sprint Tickets Without Board Worktrees" table.

---

## Step 7 — Write BOARD_STATE.md

Update `_manager/BOARD_STATE.md` with:
- Current timestamp in header: `*Last updated: HH:MM IDT (advance heartbeat)*`
- Updated Active Worktrees table
- Updated Key Changes section (delta from previous run)
- Updated Attention Items (priority-ordered)
- Updated Recently Merged table
- Any Respond-zone retirement flags

---

## Step 8 — Write RUN_LOG.md

Append a single run summary block to `_manager/RUN_LOG.md`:

```
## HH:MM IDT — [Weekday Daytime|Overnight|Weekend] Heartbeat
- PRs checked: #NNNN (state), ...
- Merges detected: none / PR #NNNN merged <date> (was active)
- CI changes: ...
- Flags: ...
- Next: ...
```

---

## Step 9 — Update dashboard artifact (data.js)

Update `.agor/artifacts/board-status/data.js` to reflect current board state:
- `LAST_UPDATED` timestamp
- `WORKTREES` array (active worktrees)
- `MERGED` array (recently merged PRs)
- `ALERTS` array (current red/yellow flags)

Append to `.agor/artifacts/board-status/heartbeat-log.js` as well.

---

## Step 10 — COMMIT AND PUSH (mandatory, every run)

```bash
git add _manager/ .agor/artifacts/
git commit -m "chore: HH:MM IDT advance heartbeat — <one-line summary>"
git push origin private-julie
```

**This step is NOT optional.** A board state that exists only in the working directory will be lost if any subsequent session starts from git HEAD. Every run must end with a commit and push, even if the summary is "board static, no changes."

If git push fails (network, auth): note the failure in the run summary but do NOT skip the git commit. A local commit is better than nothing.

---

## Quick reference — key commands

```bash
# Recently merged sweep — scoped to Joseph's PRs (Step 1 — run first)
gh pr list --state merged --repo Jounce-IO/jounce --limit 20 --assignee @me --json number,title,mergedAt,headRefName,author
gh pr list --state merged --repo Jounce-IO/jounce --limit 20 --search "review-requested:joberry" --json number,title,mergedAt,headRefName,author

# PR state (Step 3)
gh pr view <N> --repo Jounce-IO/jounce --json number,title,state,mergedAt,closedAt,mergeable,reviewDecision,isDraft

# CI status (Step 4)
gh pr checks <N> --repo Jounce-IO/jounce

# Archive worktree — autonomous when PR MERGED/CLOSED (Step 5)
# Via Agor MCP: agor_branches_archive(branchId="<branch_id>")

# Commit and push (Step 10 — every run)
git add _manager/ .agor/artifacts/ && git commit -m "chore: HH:MM IDT advance heartbeat — <summary>" && git push origin private-julie
```

---

## What this protocol fixes

| RCA Fix | Addressed by |
|---------|-------------|
| Fix 1 — Explicit protocol checklist | This file |
| Fix 2 — mergedAt check when CI passes | Step 3 critical reflex |
| Fix 3 — Commit after every run | Step 10 (mandatory) |
| Fix 4 — Recently merged sweep | Step 1 (scoped to Joseph's PRs) |
| Fix 5 — Any-zone retirement trigger | Step 5 (all zones, autonomous archive) |
| Fix 6 — BOARD_STATE.md staleness warning | Step 0 |
| Fix 7 — Autonomous archive for MERGED/CLOSED | Step 5 + CLAUDE.md permission grant |

*Created: 2026-06-20 | Reason: RCA for stale PR #1595 report (merged Jun 17, reported as open Jun 17-18 due to race condition + git commit gap)*
