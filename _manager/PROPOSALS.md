# Proposals — jounce-workflow-ai

*Last updated: 2026-06-30 18:00 IDT*

---

## Proposal: Assign jn-5795 to Plan zone — NEW (16:30 IDT Jun 30)
- **Action:** Call `agor_branches_set_zone` to move `jn-5795-upgrade-to-guidellm-v070` (branchId: `019f185c-0150-7a10-a5f7-27bc71112e3f`) to the Plan zone (`zone-1781209696300`)
- **Reason:** Worktree created 11:48 IDT Jun 30 for JN-5795 "Upgrade to GuideLLM v0.7.0" (Epic). Design session complete (143 messages, idle since 12:45 IDT, design doc at `.artifacts/design/JN-5795/03-design.md`). Should move to Plan zone to reflect current phase.
- **Risk:** Low — zone assignment is visual only, does not trigger automation
- **Worktree:** jn-5795-upgrade-to-guidellm-v070 (currently NO ZONE)
- **Status:** PENDING

---

## Proposal: Update JN-5714 to Done — Jun 30 16:00 IDT
- **Action:** Update [JN-5714](https://redhat.atlassian.net/browse/JN-5714) Jira status → Done
- **Reason:** PR #1628 merged 15:39 IDT Jun 30; Jira still "Backlog"
- **Risk:** Low — correcting stale state
- **Status:** PENDING

---

## Proposal: Move jn-5794-required-checks to Code Review zone — NEW (18:00 IDT Jun 30)
- **Action:** Call `agor_branches_set_zone` to move `jn-5794-required-checks` from Ingest zone to Code Review zone
- **Reason:** PR #1643 was published at 17:29 IDT Jun 30 (OPEN/MERGEABLE/REVIEW_REQUIRED). CI partially passing, pending jobs running. Zone still shows Ingest; board should reflect PR-published state.
- **Risk:** Low — zone assignment is visual only
- **Worktree:** jn-5794-required-checks
- **Status:** PENDING

---

## Proposal: Assign Reviewer to PR #1639 — RESOLVED (merged Jun 30 10:41 IDT)
- **Action:** ~~Assign a reviewer to PR #1639 (JN-5793)~~
- **Status:** RESOLVED — PR #1639 merged 10:41 IDT Jun 30; worktree archived.

---

## Proposal: Clarify JN-5725 / PR #1606 Intent
- **Action:** Ask Joseph whether PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606) should be closed or if CI failures need fixing
- **Reason:** Jira JN-5725 now shows "Done" but PR #1606 is still open with 4 CI failures (unchanged since Jun 29). This suggests the ticket was manually closed, but the PR is orphaned.
- **Risk:** None — clarification request only
- **Worktree:** N/A (off-board PR)
- **Status:** PENDING

---

## Proposal: Update 3 Jira Tickets to Done
- **Action:** Update JN-5612, JN-5616, JN-5724 to "Done" in Jira
- **Reason:** All 3 PRs merged Jun 29; Jira still shows In Progress/In Review. Persistent mismatch since Jun 29.
- **Risk:** Low — correcting stale state
- **Worktrees:** N/A (worktrees already archived)
- **Status:** PENDING
  - [JN-5612](https://redhat.atlassian.net/browse/JN-5612) — PR #1627 merged Jun 29, still "In Progress"
  - [JN-5616](https://redhat.atlassian.net/browse/JN-5616) — PR #1623 merged Jun 29, still "In Review"
  - [JN-5724](https://redhat.atlassian.net/browse/JN-5724) — PR #1622 merged Jun 29, still "In Review"

---

## Proposal: Archive or Fix PR #1588
- **Action:** Recommend Joseph either (a) rebase + fix pre-commit on PR #1588, or (b) close if no longer needed
- **Reason:** PR has been stale for 13+ days (CONFLICTING + pre-commit FAIL since Jun 17). No activity detected.
- **Risk:** None — recommendation only
- **Worktree:** jn-5546-docs (Code Review zone)
- **Status:** PENDING

---

## Historical Proposals (RESOLVED)

- "Investigate Missing Worktrees" — RESOLVED: previous sessions (08:00 + 08:30 IDT Jun 30) erroneously reported all worktrees gone. Full board scan at 09:01 IDT confirms 8 active worktrees.
- "Recheck PR #1606 CI Status" — RESOLVED: CI unchanged (still 4 FAIL, same run 28381202187). Ticket JN-5725 now Done.
