# Proposals — jounce-workflow-ai Board

*Last updated: 2026-07-20 15:30 IDT*

---

## ACTIVE PROPOSALS

### Proposal: Fix Pre-commit CI on PR #1695 (aipcc-23925-argo-public-url)

- **Action:** Investigate and fix pre-commit failures on PR #1695 in worktree `aipcc-23925-argo-public-url`. Check run 29741877329 pre-commit-run logs. Trigger a new session in the worktree.
- **Reason:** New DRAFT PR #1695 (feat: rewrite Argo URLs to public host, AIPCC-23925) has pre-commit ❌ + JIRA Assoc ❌ + all-checks ❌. Must fix before marking ready for review.
- **Risk:** Low — code fix in existing worktree
- **Worktree:** aipcc-23925-argo-public-url
- **Status:** PENDING — NEW as of 15:30 IDT Jul 20

---

### Proposal: Fix JIRA Association on PR #1696 (aipcc-23895-docs-ibm)

- **Action:** Add JIRA ticket reference (AIPCC-23895) to PR #1696 description/title to fix JIRA Association check.
- **Reason:** PR #1696 (docs: IBM cluster benchmarking workflow) has JIRA Assoc ❌ — likely branch name isn't auto-linked or PR description missing. all-checks ✅ so just the association needs fixing.
- **Risk:** Very low — title/description update only
- **Worktree:** aipcc-23895-docs-ibm
- **Status:** PENDING — NEW as of 15:30 IDT Jul 20

---

### Proposal: Assign Zones to New Worktrees (aipcc-23845, aipcc-23890, aipcc-23895, aipcc-23925)

- **Action:** Assign appropriate board zones to the 4 new worktrees created 15:14 IDT Jul 20:
  - aipcc-23845-cluster-connection (no PR yet) → Ingest or Code depending on state
  - aipcc-23890-qe-cluster-tests (no PR yet) → Ingest or Code depending on state
  - aipcc-23895-docs-ibm (PR #1696 DRAFT) → Publish zone after JIRA fix
  - aipcc-23925-argo-public-url (PR #1695 DRAFT, CI ❌) → Code zone until CI fixed
- **Reason:** All 4 worktrees have no zone (not visible on board). Need to be placed in pipeline zones to track progress.
- **Risk:** Low — zone moves are reversible
- **Status:** PENDING — awaiting Joseph confirmation of current state of each worktree

---

### Proposal: Move jn-5865-ibm-cluster-connect to Code Zone

- **Action:** Move worktree `jn-5865-ibm-cluster-connect` from Ingest zone to Code zone via `agor_branches_set_zone`, then trigger `/implement:code` session
- **Reason:** Plan session completed ~23:06 IDT Jul 8 (17+ days ago). Worktree is still in Ingest zone but should be in Code phase. **This is the longest-standing zone mismatch on the board.**
- **Risk:** Low — zone move is reversible
- **Worktree:** `jn-5865-ibm-cluster-connect`
- **Zone Target:** Code (zone-1781429763919)
- **Status:** PENDING (Day 17+ mismatch)

---

### Proposal: Investigate jn-5871 Git-Only Branch

- **Action:** Determine if jn-5871 (Code done ~00:58 IDT Jul 9, SHA fc6e5f77) should be:
  1. Registered as an Agor worktree on this board
  2. Have a PR created
  3. Be archived (work abandoned)
- **Reason:** Work appears complete (code session done Jul 9) but NOT registered in Agor as a worktree. Only exists as git branch. Ticket [JN-5871](https://redhat.atlassian.net/browse/JN-5871).
- **Risk:** None if just investigating
- **Worktree:** N/A (git-only, not in Agor)
- **Status:** PENDING (needs Joseph decision)

---

### Proposal: Archive jira-operations Stale Worktree

- **Action:** Archive worktree `jira-operations` (uid=249, NO ZONE) via `agor_branches_archive`
- **Reason:** Last updated Jun 25 2026 (21+ days stale). No sessions, no PR, no Jira. Appears to be inactive.
- **Risk:** Low if no longer needed. Archiving is reversible via `agor_branches_unarchive`.
- **Worktree:** jira-operations
- **Status:** PENDING (check with Joseph if this is still needed)

---

### Proposal: Update 6 Jira Tickets to Done

- **Action:** Transition the following Jira tickets from current status to "Done":
  - [JN-5842](https://redhat.atlassian.net/browse/JN-5842) — PR #1658 MERGED Jul 14
  - [JN-5877](https://redhat.atlassian.net/browse/JN-5877) — PR #1663 MERGED Jul 13
  - [JN-5874](https://redhat.atlassian.net/browse/JN-5874) — PR #1662 MERGED Jul 13
  - [JN-5401](https://redhat.atlassian.net/browse/JN-5401) — PR #1654 MERGED Jul 12
  - [JN-5827](https://redhat.atlassian.net/browse/JN-5827) — PR #1648 MERGED Jul 12
  - [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — PR #1588 MERGED Jul 7
- **Reason:** All PRs merged days/weeks ago but Jira tickets not updated to Done. Jira MCP 401 prevents automated updates.
- **Risk:** None — standard Jira cleanup
- **Status:** BLOCKED (Jira MCP 401; acli not working; requires manual Jira UI updates)

---

## OBSERVATIONS (No Action Required)

### Observation: #1669 Pre-commit Failure (jn-5872)

- **What:** PR #1669 has pre-commit check failing. All other checks pass (e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅). OPEN + MERGEABLE.
- **Action:** None — this is Joseph's work to fix.
- **Worktree:** jn-5872
- **Zone:** Code
- **Status:** OBSERVING

---

### Observation: #1667 Awaiting Reviewer APPROVE (jn-5845)

- **What:** PR #1667 has ALL CI PASS ✅. OPEN + MERGEABLE. reviewDecision: "" (needs formal APPROVE from markVaykhansky or other reviewer).
- **Action:** None — awaiting human reviewer.
- **Worktree:** jn-5845-helm-cicd-agents-md
- **Zone:** Publish
- **Status:** OBSERVING

---

### Observation: #1670 DRAFT Awaiting Ready Status (jn-5844)

- **What:** PR #1670 DRAFT with CI all pass. MERGEABLE. Needs: mark ready for review (remove draft status).
- **Action:** None — awaiting Joseph to approve readiness.
- **Worktree:** jn-5844-service-lib-sql-agents-md
- **Zone:** Publish
- **Status:** OBSERVING

---

### Observation: #1638 CI ALL PASS — Ready to Merge (off-board)

- **What:** Off-board PR #1638 (feat/vllm-analyzer-prerequisites) — run 29654523528 ALL-CHECKS ✅ PASS. All checks pass: pre-commit ✅, nox ✅, tox ✅, integration ✅, e2e-api ✅, e2e-smoke ✅, e2e-product ✅, bake ✅. OPEN + MERGEABLE. JN-5725 Done ✅.
- **Action:** 🟢 **Ready to merge when Joseph approves**. No blocking issues.
- **Status:** OBSERVING — awaiting Joseph merge decision

---

### Observation: jn-5824 Idle Since Jul 8

- **What:** jn-5824-benchmark-run-configs has been idle since Jul 8. Last session IDLE. SHA 16ec44ea (2 commits). No PR created.
- **Action:** None — awaiting Joseph direction on next steps (generate configs, rebase, create PR).
- **Worktree:** jn-5824-benchmark-run-configs
- **Zone:** Code
- **Status:** OBSERVING

---

## RESOLVED PROPOSALS (from prior runs)

### RESOLVED: Move jn-5845 to Code Review Zone (Jul 14 20:00)

- **Status:** SUPERSEDED — jn-5845 advanced past Code Review to Publish zone. PR #1667 now awaiting reviewer APPROVE.

---

### RESOLVED: Update JN-5717 Jira to Done

- **Status:** RESOLVED — JN-5717 confirmed Done via acli Jul 15 15:00 IDT.

---

### RESOLVED: Update JN-5794 Jira to Done

- **Status:** UNVERIFIED — Jira MCP 401; last known status "In Review" (Jul 8). Needs manual verification.

---

### RESOLVED: Add #1632 (JN-5719) to Board

- **Status:** NOT PURSUED — off-board PR, not added to board. PR clean but not tracked.

---

### RESOLVED: Monitor #1647 and #1638

- **Status:** OBSERVING — #1638 tracked in Off-Board PRs section. #1647 no longer mentioned in recent scans.

---

### RESOLVED: Archive fix-dashboard-syntax-error Zombie Worktree

- **Status:** NOT PURSUED — worktree not found in recent scans (may have been manually deleted).

---

### RESOLVED: Move jn-5795 to Plan Zone

- **Status:** NOT PURSUED — jn-5795 currently in Ingest zone (Jul 16). Design session done Jun 30, ready for Plan phase but no action taken.

---

### RESOLVED: Move jn-5827 to Plan Zone

- **Status:** SUPERSEDED — jn-5827 progressed to Publish zone, PR #1648 MERGED Jul 12. Worktree archived.

---

*All proposals require explicit approval before execution. Julie operates in SUPERVISED mode.*
