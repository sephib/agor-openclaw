# Proposals — jounce-workflow-ai Board

*Last updated: 2026-07-14 20:00 IDT*

---

## Proposal: Move jn-5845 to Code Review Zone (NEW — 20:00 IDT Jul 14)

- **Action:** Move worktree `jn-5845-helm-cicd-agents-md` from Publish zone to Code Review zone via `agor_branches_set_zone`
- **Reason:** PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667) CI run 29356096050 is COMPLETE with ALL checks passing ✅ (pre-commit ✅ tox ✅ integration ✅ e2e-api ✅ e2e-smoke ✅ all-checks ✅). PR is OPEN, MERGEABLE, REVIEW_REQUIRED. Ready for code review.
- **Risk:** Low — zone move is reversible
- **Worktree:** `jn-5845-helm-cicd-agents-md` (branch_id: `019f5ffb-a84e-7b98-b48e-d0373337ad2f`)
- **Zone:** Code Review (zone-1781430099126)
- **Status:** PENDING

---

## Proposal: Update JN-5717 Jira to Done

- **Action:** Transition [JN-5717](https://redhat.atlassian.net/browse/JN-5717) from "Backlog" to "Done"
- **Reason:** PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) was merged on 2026-07-06 at 09:19 IDT. Ticket should reflect merged status.
- **Risk:** None — standard Jira cleanup
- **Worktree:** N/A (off-board PR)
- **Status:** PENDING

---

## Proposal: Update JN-5794 Jira to Done

- **Action:** Transition [JN-5794](https://redhat.atlassian.net/browse/JN-5794) from "In Review" to "Done"
- **Reason:** PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) was merged on 2026-07-01 at 09:16 IDT (6+ days ago). Ticket should reflect merged status.
- **Risk:** None — standard Jira cleanup
- **Worktree:** N/A (worktree already archived on Jul 1)
- **Status:** PENDING

---

## Proposal: Add #1632 (JN-5719) to Board — Clean PR Ready to Merge

- **Action:** Create worktree for PR [#1632](https://github.com/Jounce-IO/jounce/pull/1632) (jn-5719-release-diff) and place in Code Review or Publish zone
- **Reason:** This PR has **all CI passing** ✅ (run 28775331183, all-checks ✅, e2e ✅, pre-commit ✅). It's ready to merge but not tracked on the board. Ticket [JN-5719](https://redhat.atlassian.net/browse/JN-5719).
- **Risk:** Low — PR is clean. Adding to board just improves visibility.
- **Worktree:** Would create `jn-5719-release-diff` worktree
- **Status:** PENDING

---

## Proposal: Monitor #1647 and #1638 — Off-board PRs with e2e Failures

- **Action:** Add #1647 (feat/migrate-dev-to-openshift-gcp) and #1638 (feat/vllm-analyzer-prerequisites) to monitoring list or create worktrees
- **Reason:** Both PRs are MERGEABLE but have e2e test failures. #1647: e2e-api ❌ + e2e-tests ❌. #1638: e2e-smoke ❌ + e2e-tests ❌. Both updated Jul 6. Currently not on board.
- **Risk:** None if just monitoring. If creating worktrees, minimal — just adds board visibility.
- **Worktree:** Would create worktrees if approved
- **Status:** PENDING (low priority — Joseph may not want these on board)

---

## Proposal: Archive fix-dashboard-syntax-error Zombie Worktree

- **Action:** Archive worktree `fix-dashboard-syntax-error` (agor-openclaw repo)
- **Reason:** This worktree is **19+ days stale** (created Jun 17), has no PR, no Jira ticket, filesystem_status: failed, and was not found in latest Agor scan. It's a zombie.
- **Risk:** Low if Joseph no longer needs it. Could ask first.
- **Worktree:** fix-dashboard-syntax-error
- **Status:** PENDING (repeated from prior runs — needs decision)

---

## Proposal: Archive jira-operations Stale Worktree

- **Action:** Archive worktree `jira-operations` (uid=249, NO ZONE)
- **Reason:** Last updated Jun 25 2026 (12+ days stale). No sessions, no PR, no Jira. Appears to be inactive.
- **Risk:** Low if no longer needed. Could ask first.
- **Worktree:** jira-operations
- **Status:** PENDING (check with Joseph if this is still needed)

---

## Proposal: Move jn-5795-upgrade-to-guidellm-v070 to Plan Zone

- **Action:** Move worktree `jn-5795-upgrade-to-guidellm-v070` from NO ZONE to Plan zone
- **Reason:** Design session completed Jun 30 12:45 IDT (idle). Worktree has no zone assigned but appears to be in planning phase. Ticket [JN-5795](https://redhat.atlassian.net/browse/JN-5795) is in Backlog.
- **Risk:** None — just board organization
- **Worktree:** jn-5795-upgrade-to-guidellm-v070
- **Status:** PENDING (repeated from Jun 30 — still unresolved)

---

## Proposal: Move jn-5827-git-tagging-workflow to Plan Zone

- **Action:** Move worktree `jn-5827-git-tagging-workflow` from Ingest zone to Plan zone
- **Reason:** Session 019f36af completed with 59 messages (idle Jun 6 09:11 IDT) — plan written. Still in Ingest zone but ready for Plan phase.
- **Risk:** None — standard workflow progression
- **Worktree:** jn-5827-git-tagging-workflow
- **Status:** PENDING

---

## Observation: #1588 Pre-commit Failure Persists

- **What:** PR #1588 (jn-5546-docs-module-layout) has been MERGEABLE since overnight rebase (Jul 6→7), but **pre-commit check is still failing** (CI run 28822455546, job 85477327366, 4m28s). All other checks passing (build ✅, integration ✅, e2e ✅, tox ✅, nox ✅).
- **Action:** None — this is Joseph's work to fix. Just flagging for visibility.
- **Worktree:** jn-5546-docs-document-module-layout-convention-and-3
- **Zone:** Respond
- **Status:** OBSERVING (no proposal)

---

## Observation: #1606 Still CONFLICTING + e2e Failures

- **What:** Off-board PR #1606 (feat/jn-5725-integrate-vllm-log-analyzer) has been CONFLICTING since Jul 2 (5+ days). e2e-smoke ❌ + e2e-tests ❌. Jira [JN-5725](https://redhat.atlassian.net/browse/JN-5725) is marked Done but PR is still open.
- **Action:** None — awaiting Joseph's decision to rebase+fix or close.
- **Status:** OBSERVING (no proposal — flagged in multiple prior runs)

---

## Historical Proposals (RESOLVED since Jun 30)

- **JN-5714 to Done** — RESOLVED: PR #1628 merged Jun 30, Jira updated (confirmed Done Jul 6)
- **JN-5794 Code Review zone** — RESOLVED: PR #1643 merged Jul 1, worktree archived
- **JN-5612/5616/5724 to Done** — RESOLVED: All 3 confirmed Done via acli on Jul 6
- **Assign Reviewer to PR #1639** — RESOLVED: PR merged Jun 30
- **JN-5725 / PR #1606 Intent** — UNRESOLVED: Still open as Observation above

---

*All proposals require explicit approval before execution.*
