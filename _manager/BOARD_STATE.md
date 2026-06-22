# Board State — jounce-workflow-ai

*Last updated: 2026-06-22 13:32 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ⚠️ Only CodeRabbit ✅ — GH Actions CI **still never triggered** ~21h+ after un-draft | reviewDecision="" | 🔴 **CONFLICTING + CI not running** — double problem unchanged |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ **pre-commit FAIL** (CI run 27934981657, created 09:52 IDT Jun 22) | REVIEW_REQUIRED | 🔴 **TRIPLE: DRAFT + CONFLICTING + pre-commit FAIL** — blocked on #1604 merging first |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | 🟡 **PR checks ALL GREEN** (run 27937907242) — note: branch CI run 27933817996 (09:24 IDT) failed pre-commit but did NOT update PR status checks | reviewDecision="" | 🟡 **Needs reviewer** — PR checks green; underlying branch run may still have pre-commit issue |
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
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ⏳ NEW run 27945336025 (main merged by Uri Shaket ~10:54 IDT): pre-commit ✅, integration ✅, e2e-api ✅, tox ✅; **e2e-smoke PENDING** | OPEN, MERGEABLE, reviewDecision="" | 🟡 **Almost green — e2e-smoke pending** (~26.5h no reviewer) |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ⏳ Same run 27945336025: pre-commit ✅, integration ✅, e2e-api ✅; **e2e-smoke PENDING** | OPEN, MERGEABLE, REVIEW_REQUIRED | 🟡 **e2e-smoke pending** (same CI run as #1602 — shared jobs) |

---

## Key Changes Since Last Run (Jun 22 13:02 IDT)

| What observed | Status |
|---|---|
| **🟡 PR #1588 — PR checks now GREEN** | `gh pr checks` shows run 27937907242 ALL PASSING (pre-commit ✅). Branch run 27933817996 (failure) did NOT update PR status checks — PR appears ready for reviewer. Jira JN-5546 still "In Progress" → should be "In Review". |
| **🟡 PR #1602 — new CI run, e2e-smoke pending** | Main merged into branch by Uri Shaket ~10:54 IDT → new run 27945336025. Pre-commit ✅, integration ✅, e2e-api ✅, tox ✅; e2e-smoke PENDING. ~26.5h no reviewer. |
| **↔ PR #1604 CONFLICTING + no CI** | Unchanged — still CONFLICTING, GH Actions CI still never triggered (~21h). |
| **↔ PR #1615 triple problem** | Unchanged — DRAFT + CONFLICTING + pre-commit FAIL. |
| **↔ PR #1606 e2e-smoke pending** | Same CI run as #1602 (run 27945336025 — shared job IDs); e2e-smoke still PENDING. |
| **No new merges** | Step 1 sweep confirmed: no PRs merged since Jun 21. |

---

## Attention Items

### 🔴 CRITICAL — PR #1604 (JN-5676) — CONFLICTING + CI never triggered (~21.5h)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

CONFLICTING (merge conflict) AND GH Actions CI has never triggered (~21.5h since un-draft ~17:30-18:00 IDT Jun 21). Unchanged from last run.

**Required action:** (1) Resolve merge conflict (rebase onto main), (2) After push, confirm CI triggers, (3) Address CodeRabbit comments, (4) Request reviewer when green.

---

### 🟡 PR #1602 (JN-5685/JN-5679) — e2e-smoke pending, ~26.5h no reviewer

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

New CI run 27945336025 (main merged by Uri Shaket ~10:54 IDT): pre-commit ✅, integration ✅, e2e-api ✅, tox ✅; e2e-smoke PENDING. OPEN, MERGEABLE, reviewDecision="". ~26.5h no reviewer.

**Required action:** Assign a reviewer. E2e-smoke is pending (not failing) — PR is effectively ready.

---

### 🟡 PR #1606 (JN-5725) — e2e-smoke pending, REVIEW_REQUIRED

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606) — "feat(vllm-analyzer): integrate log analyzer into experiment-workflow (JN-5725)"

Same CI run 27945336025 as #1602 (shared job IDs). Pre-commit ✅, integration ✅, e2e-api ✅; e2e-smoke PENDING. REVIEW_REQUIRED.

**Monitor:** Wait for e2e-smoke; ready for review once it clears.

---

### 🟡 PR #1588 (JN-5546) — PR checks GREEN, assign reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

`gh pr checks` shows ALL GREEN (run 27937907242 — pre-commit ✅, integration ✅, tox ✅, atlas-validate ✅). Status: OPEN, MERGEABLE, reviewDecision="". Note: branch has a known CI run (27933817996, Jun 22 09:24 IDT) that failed pre-commit, but this run did NOT update PR status checks — likely from a merge-commit CI trigger that uses a different reporting path. From GitHub's merge gate perspective, the PR is green.

**Required action:** (1) Assign a reviewer NOW. (2) Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

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
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, pre-commit FAIL | Should be "In Review" (open PR) |
| [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | DRAFT, pre-commit FAIL + CONFLICTING | Jira slightly ahead — PR still draft + failing |

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
