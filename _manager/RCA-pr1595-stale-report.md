# RCA: Stale PR #1595 Report — "Open, Awaiting Review"

*Written: 2026-06-20 | Author: Julie (board manager)*

---

## Summary

Julie reported PR [#1595](https://github.com/Jounce-IO/jounce/pull/1595) (JN-5673) as "all checks pass, mergeable, awaiting review" when the PR had actually been **merged on June 17 at 12:57 IDT** (09:57 UTC). The error traces to a 28-hour detection blind spot caused by two compounding failures: a race condition between the June 17 afternoon scan and the PR merge, and a 2.5-day gap in git commits that meant the corrected state was never durably recorded.

---

## 1. Timeline

| Time (IDT) | Event |
|------------|-------|
| **Jun 17 09:33 IDT** | Morning scan (session 019ed3f3): PR #1595 CI still pending e2e result |
| **Jun 17 ~12:57 IDT** | **PR #1595 merged** to main (09:57 UTC, by sephib/Joseph Berry) |
| **Jun 17 ~13:00 IDT** | Afternoon scan (session 019ed501): saw CI as "fully passed ✅ — all checks green including e2e"; noted Respond-zone session "waiting on Slack channel answer for PR #1595 post"; treated PR as still active |
| **Jun 16 17:43 IDT** | *Last git commit on private-julie branch before heartbeat automation* — BOARD_STATE.md committed showing PR #1595 as OPEN in Respond zone |
| **Jun 18 16:30–17:00 IDT** | Two heartbeats fire. Focus on newly-active PRs #1599/#1601/#1604 and conflict cascade. jn-5673 worktree (Respond zone) not scanned. |
| **Jun 18 17:30 IDT** | First heartbeat to detect: "PR #1595 merged Jun 17 but Jira still In Review — 24h+ stale." Updated working-directory BOARD_STATE.md but **did NOT commit to git**. |
| **Jun 19 10:03 IDT** | **First git commit after 2.5-day gap.** BOARD_STATE.md now correctly omits jn-5673 from active table. |
| **Jun 19 14:33 IDT** | First heartbeat to note "JN-5673 Jira now Done ✅" |
| **Jun 20 (all runs)** | All 30-min advance heartbeats correctly show PR #1595 in "Recently Merged" |
| **Jun 20 (reported session)** | A session reads BOARD_STATE.md with "last updated June 16" state (git-committed version); reports PR #1595 as open awaiting review |

**Gap between merge and first heartbeat detection: ~28 hours**
**Gap between last git commit and first heartbeat git commit: ~64 hours (June 16 17:43 → June 19 12:06)**

---

## 2. Root Cause

**Primary: Race condition between the June 17 afternoon scan and the PR merge.**

The afternoon scan (session 019ed501) ran at approximately 13:00 IDT — within minutes of the merge at 12:57 IDT. The session's `gh pr view 1595` call either:

- Executed before the merge and correctly returned `state: OPEN` (GitHub processes merges with seconds of latency after the button click), OR
- Returned OPEN because the merge had just completed and GitHub's PR state change hadn't propagated to the API at the instant of the call

In either case, the session observed PR #1595 as OPEN with CI fully passing and recorded this in BOARD_STATE.md. The session then flagged the jn-5673 worktree as "Respond zone, waiting on Slack channel answer" — an active state, not a terminal one.

**Secondary: Missing heartbeat coverage of Respond-zone worktrees.**

The June 18 early heartbeats (16:30, 17:00 IDT) scanned the active development pipeline but did not re-check worktrees in the Respond zone. The heartbeat scan logic implicitly assumed that Respond-zone worktrees were "handled" and didn't require PR state re-verification. There is no `heartbeat-advance.md` protocol file to enforce coverage of all zones.

**Tertiary: 2.5-day git commit gap.**

The June 17-18 sessions — including the June 18 17:30 IDT heartbeat that CORRECTLY detected the merge — **never committed their changes to git**. The private-julie branch has no commits between June 16 17:43 IDT and June 19 12:06 IDT (2.5 days). This means:

```
git-committed truth: June 16 17:43 IDT → PR #1595 = OPEN (Respond zone, In Review)
working-dir truth:   June 18 17:30 IDT → PR #1595 = MERGED (correctly detected)
```

Any session that started from the git-committed state (fresh spawn, git pull, or Agor session bootstrap that reads from the branch's HEAD) would get the June 16 stale snapshot — showing PR #1595 as open, review required.

---

## 3. Contributing Factors

| Factor | Description |
|--------|-------------|
| **`heartbeat-advance.md` does not exist** | The protocol file for what the advance heartbeat should do was never created in `_manager/`. Without a written checklist, heartbeat sessions exercised judgment about what to scan, and Respond-zone PRs fell outside the default scope. |
| **No "CI pass → verify merge" reflex** | When the afternoon scan observed "CI all green," it correctly noted this as progress but didn't trigger a follow-up: "CI passed, was this merged yet?" This verification would catch the race. |
| **No recently-merged sweep** | The heartbeat had no step like `gh pr list --state merged --limit 10 --since yesterday` to proactively catch merges between runs. |
| **No worktree retirement trigger on merge** | When a PR merges, the expectation was that a session would archive the worktree. But if that session (the Respond-zone session) never received the merge signal, the worktree stayed active indefinitely. |
| **Git backup not enforced after Jun 16** | BACKUP.md describes committing and pushing at the end of each session. The June 17-18 sessions did not follow this. The corrected state existed only in the working directory — vulnerable to being overwritten by a session that started from git HEAD. |
| **No `closedAt`/`mergedAt` field in scan queries** | The heartbeat was querying PR state fields that show "OPEN + MERGEABLE + CI results" but not explicitly checking `mergedAt`. A PR can appear MERGEABLE even seconds after merging (until the API state refreshes). |

---

## 4. What data.js / Dashboard Shows

The current `data.js` artifact (updated 2026-06-20 22:30 IDT) **correctly shows PR #1595 in the `MERGED` array** with `mergedDate: "2026-06-17"` and `note: "Jira now Done ✅"`. The dashboard artifact is not stale — it reflects the working-directory state, which was corrected by the June 18 17:30 IDT heartbeat.

The stale data exists only in the **git-committed snapshot** (June 16 17:43 IDT), which any new session bootstrapping from git HEAD would receive.

---

## 5. Proposed Fixes

### Fix 1 — Create `heartbeat-advance.md` with explicit checklist
**Priority: High**

The advance heartbeat protocol must explicitly enumerate what to check on every run, including:
- All worktrees in ALL zones (not just active-dev zones)
- Any PR tracked in BOARD_STATE.md that was "CI-passing but not merged" on the previous run → re-verify with `--json state,mergedAt,closedAt`
- A `gh pr list --state merged --limit 20 --repo Jounce-IO/jounce` sweep to catch merges missed between runs

### Fix 2 — Always check `mergedAt` when CI passes
**Priority: High**

When a heartbeat observes `reviewDecision: REVIEW_REQUIRED` + all CI checks passing, it MUST add an explicit check:
```bash
gh pr view <N> --repo Jounce-IO/jounce --json state,mergedAt,closedAt
```
Report `mergedAt` if set. If the PR merged between the last run and this one, retire the worktree immediately.

### Fix 3 — Commit after every heartbeat run (enforce BACKUP.md)
**Priority: High**

The 2.5-day git commit gap is the most dangerous contributing factor. A session's corrected state is meaningless if it exists only in the working directory. Every heartbeat session MUST end with:
```bash
git add _manager/ .agor/artifacts/ && git commit -m "chore: HH:MM IDT advance heartbeat — <summary>" && git push origin private-julie
```
The June 18 17:30 IDT heartbeat detected the merge correctly but never committed. That detection was lost to any session starting from git HEAD.

### Fix 4 — Add "recently merged" sweep to every run
**Priority: Medium**

At the start of each heartbeat:
```bash
gh pr list --state merged --repo Jounce-IO/jounce --limit 20 --json number,mergedAt,title,headRefName
```
Cross-reference against BOARD_STATE.md active worktrees. Any match → immediately retire from active table, move to Recently Merged, flag for archival proposal.

### Fix 5 — Retirement trigger on Respond-zone PRs
**Priority: Medium**

Worktrees in the Respond zone exist to communicate about a completed PR. The heartbeat should check: does the PR for a Respond-zone worktree show `state: MERGED`? If yes, add to retirement proposal queue automatically.

### Fix 6 — Date the BOARD_STATE.md timestamp prominently
**Priority: Low**

The current header format `*Last updated: 2026-06-20 22:30 IDT*` is correct. But a session reading a stale file might not notice the date. Add a staleness warning when a session detects the timestamp is >2h old at startup:

> ⚠️ BOARD_STATE.md is 3 days old — perform full refresh before reporting.

---

## 6. What Heartbeat Sessions Were Correctly Doing

To be fair: **all June 20 heartbeat sessions correctly report PR #1595 as merged.** The failure window was June 17 13:00 → June 18 17:30 (28 hours). By the time the June 19 10:03 IDT heartbeat committed to git, the board state was correct.

The "June 20 session" that reported #1595 as open most likely:
- Started from the git-committed state (June 16 HEAD) rather than the working directory
- Read the June 16 BOARD_STATE.md showing `jn-5673-visibility-module | Respond | In Review | #1595 | ⚠️ Slack posted?`
- Ran `gh pr view 1595` — but the result (OPEN vs MERGED) depends on whether this was a reconstructed scenario from the June 17 race window, because on June 20 the API correctly returns MERGED

The most parsimonious explanation: the problematic session ran on June 17 (minutes before or after the merge, in the race window), and the failure was only DISCOVERED by Joseph on June 20 when checking board status.

---

## 7. Immediate Actions

| Action | Owner | Status |
|--------|-------|--------|
| Verify PR #1595 merged (confirmed: Jun 17 12:57 IDT by sephib) | ✅ Done | |
| Verify BOARD_STATE.md now correct (confirmed: Shows #1595 in Recently Merged) | ✅ Done | |
| Verify data.js now correct (confirmed: MERGED array, Jun 17, Jira Done) | ✅ Done | |
| Create `heartbeat-advance.md` with full protocol checklist | Julie | PENDING — requires Joseph approval of scope |
| Add commit-after-every-run to heartbeat protocol | Julie | PENDING |
| Add `gh pr list --state merged` sweep step | Julie | PENDING |

---

*This RCA covers the failure class that produced the stale PR #1595 report. The same class of error could affect any PR that merges while a heartbeat session is mid-run or while no heartbeat session is covering that zone.*
