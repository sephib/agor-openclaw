# Proposals — jounce-workflow-ai

*Last updated: 2026-06-30 09:01 IDT*

---

## Proposal: Assign Reviewer to PR #1639 — URGENT
- **Action:** Assign a reviewer to PR [#1639](https://github.com/Jounce-IO/jounce/pull/1639) (JN-5793)
- **Reason:** ALL CI checks now passing as of 09:01 IDT Jun 30 — including JIRA Association (was the last blocker). PR is MERGEABLE, REVIEW_REQUIRED. Ready to merge.
- **Risk:** None — PR is ready
- **Worktree:** jn-5793-jsonb-path-fix (Code zone)
- **Status:** PENDING

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
