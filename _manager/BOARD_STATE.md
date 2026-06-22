# Board State — jounce-workflow-ai

*Last updated: 2026-06-22 15:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ✅ **ALL GREEN** (run 27947074357: pre-commit ✅, integration ✅, e2e-api ✅, tox ✅, nox ✅, **e2e-smoke ✅ PASSED**) | reviewDecision="" | 🎉 **ALL GREEN — ASSIGN REVIEWER NOW** |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ **pre-commit FAIL** (CI run 27934981657, created 09:52 IDT Jun 22) | REVIEW_REQUIRED | 🔴 **TRIPLE: DRAFT + CONFLICTING + pre-commit FAIL** — blocked on #1604 merging first |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | 🟡 PR checks run 27933817996 shows pre-commit FAIL (stale branch CI run); MERGEABLE | reviewDecision="" | 🟡 **Needs reviewer** — MERGEABLE; Jira should be "In Review" |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ℹ️ Idle, docs done |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit — CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

**Archived This Session (14:30 IDT Jun 21):**
- jn-5675-historical-visibility (archived 14:30 IDT — PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) MERGED 16:15 IDT Jun 21)

**Archived Previous (14:00 IDT Jun 21):**
- ci-statistics-notebook (archived 14:00 IDT — JN-5708 Done + 3+ days inactive + no PR)

**Archived Previous (12:00 IDT Jun 21):**
- jn-5729-pin-uv-default-python-2 (archived 12:00 IDT — PR #1608 MERGED)
- jn-5729-pin-python-313 (archived 12:00 IDT — PR #1607 CLOSED)
- jn-5729-pin-uv-default-python (archived 12:00 IDT — JN-5729 done, no PR)
- code-reviewes (archived 12:00 IDT — review done Jun 15, 6+ days inactive)

**Previously Archived:**
- jn-5673-visibility-scaffold (archived Jun 21 04:57 IDT)
- jn-5674-operational-visibility (archived Jun 21 04:57 IDT, PR #1599 MERGED Jun 18)

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | auto-apply-labels | [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | — | **MERGED Jun 21** | 🎉 MERGED — off-board, no archive needed |
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | **MERGED 14:34 IDT Jun 22** | 🎉 MERGED — JN-5685 Done, JN-5679 Done |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | 🔴 **Run 27950494952** (created 14:50 IDT, triggered by #1602 merge): e2e-api ❌ FAIL, e2e-tests ❌ FAIL; pre-commit ✅, integration ✅, tox ✅, nox ✅; e2e-smoke SKIPPED | OPEN, **MERGEABLE**, REVIEW_REQUIRED | 🔴 **NEW e2e-api FAIL** — regression triggered by #1602 merge; JN-5725 shows Done in Jira but PR still OPEN |

---

## Key Changes Since Last Run (Jun 22 14:30 IDT)

| What observed | Status |
|---|---|
| **🎉 PR #1602 MERGED** | Merged 14:34 IDT Jun 22 (11:34Z) by approval — REVIEW_REQUIRED → APPROVED → MERGED. JN-5685 Done ✅, JN-5679 Done ✅. Off-board PR, no worktree to archive. |
| **🔴 PR #1606 e2e-api FAIL** | New CI run 27950494952 created 14:50 IDT Jun 22 (triggered by #1602 merge into main). e2e-api ❌ FAIL, e2e-tests ❌ FAIL. Was "e2e-smoke PENDING" in prior run 27948135971. Regression introduced by #1602. |
| **⚠️ JN-5725 Done in Jira but PR #1606 open** | Jira ticket marked Done, but PR #1606 is still open with CI failures. New mismatch. |
| **↔ PR #1604 all green** | Unchanged — still ALL GREEN (run 27947074357). MERGEABLE. No reviewer assigned yet. |
| **↔ PR #1615 triple problem** | Unchanged — DRAFT + CONFLICTING + pre-commit FAIL. |
| **↔ PR #1588 branch CI pre-commit** | Unchanged — stale run 27933817996 FAIL; PR MERGEABLE (UNKNOWN in API, but MERGEABLE confirmed at 14:30 scan). |

---

## Attention Items

### 🎉 PR #1604 (JN-5676) — ALL GREEN — ASSIGN REVIEWER NOW

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

**ALL CI CHECKS NOW PASS.** e2e-smoke PASSED (run 27947074357, 10m42s). MERGEABLE. reviewDecision="" — no reviewer yet.

This was CONFLICTING + no CI for 21.5h, then conflict resolved at ~14:03 IDT, and e2e-smoke just completed and passed. 

**Required action:** Assign reviewer immediately.

---

### 🎉 PR #1602 (JN-5685/JN-5679) — MERGED 14:34 IDT Jun 22

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — MERGED. JN-5685 Done ✅, JN-5679 Done ✅. Off-board PR, no worktree to archive.

---

### 🔴 PR #1606 (JN-5725) — NEW e2e-api FAIL (regression from #1602 merge)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606) — "feat(vllm-analyzer): integrate log analyzer into experiment-workflow (JN-5725)"

New CI run 27950494952 (created 14:50 IDT Jun 22): **e2e-api ❌ FAIL, e2e-tests ❌ FAIL**. Triggered by merge of main after #1602 landed. Previous run 27948135971 had e2e-api PASS.

JN-5725 is "Done" in Jira, but PR is still OPEN with CI failures. Investigate whether:
1. PR needs to be updated to fix e2e-api regression, OR
2. Jira was prematurely closed

**Required action:** Joseph to investigate e2e-api failure and decide whether to fix or close/revert PR #1606.

---

### 🟡 PR #1588 (JN-5546) — PR MERGEABLE, assign reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

Stale branch CI run 27933817996 shows pre-commit FAIL, but PR is MERGEABLE (reviewDecision=""). Pattern from previous runs: branch CI run doesn't update PR merge gate status. Assign reviewer.

**Required action:** (1) Assign a reviewer. (2) Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ PR #1615 (JN-5677) — TRIPLE: DRAFT + CONFLICTING + pre-commit FAIL

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): DRAFT, pre-commit FAIL (run 27934981657, 09:52 IDT Jun 22), CONFLICTING. Blocked on JN-5676 (#1604) merging first. Fix pre-commit and resolve conflict even while still in draft.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (3 items)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 5+ days stale — should be Done |
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, MERGEABLE | Should be "In Review" (open PR) |
| [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | **Done** | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, e2e-api FAIL | Ticket Done but PR still open with CI failures — investigate |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Reduce Lychee precommit flaky results | Backlog | No worktree |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache CLI flags to runner | **In Progress** | No worktree — may be older/lower priority |

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
| [JN-5685](https://jounce.atlassian.net/browse/JN-5685)/[JN-5679](https://jounce.atlassian.net/browse/JN-5679) | [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | Jun 22 14:34 IDT ✅ |
| [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | Jun 21 16:15 IDT ✅ |
| [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | Jun 21 10:50 IDT ✅ |
| [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | [#1608](https://github.com/Jounce-IO/jounce/pull/1608) | Jun 21 09:37 IDT ✅ |
| [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) | Jun 18 23:55 IDT ✅ |
| JN-5619 | [#1598](https://github.com/Jounce-IO/jounce/pull/1598) | Jun 18 13:33 UTC ✅ |
| [JN-5708](https://jounce.atlassian.net/browse/JN-5708) | [#1603](https://github.com/Jounce-IO/jounce/pull/1603) | Jun 18 12:42 UTC ✅ |
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Jun 17 ✅ |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
