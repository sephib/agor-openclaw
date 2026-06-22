# Board State — jounce-workflow-ai

*Last updated: 2026-06-22 11:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ⚠️ Only CodeRabbit ✅ — GH Actions CI **not triggered** ~20h after un-draft | reviewDecision="" | 🔴 **GH Actions CI not running** — manual re-trigger needed |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ **pre-commit FAIL** (CI run 27934981657, created 09:52 IDT Jun 22) | REVIEW_REQUIRED | ⚠️ **CORRECTION**: was incorrectly reported ALL GREEN — pre-commit still FAIL |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ **pre-commit FAIL** (CI run 27933817996 — main merged into branch at 09:24 IDT Jun 22) | reviewDecision="" | 🔴 **pre-commit FAIL** (regression from main merge — 4th heartbeat) |
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
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ **ALL GREEN** (run 27937907242) | OPEN, MERGEABLE, reviewDecision="" | 🎉 **FULLY GREEN — assign reviewer NOW** (~20h waiting) |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ⏳ e2e-smoke PENDING (new run), e2e-api ✅ PASS, pre-commit ✅ | OPEN, **MERGEABLE**, REVIEW_REQUIRED | ⚠️ e2e-smoke still running — possible improvement from FAIL |

---

## Key Changes Since Last Run (Jun 22 11:03 IDT)

| What observed | Status |
|---|---|
| **⚠️ PR #1615 CORRECTION — still pre-commit FAIL** | Previous 3 heartbeats (09:02, 09:34, 11:03 IDT) incorrectly reported "ALL GREEN". The cited run 27937907242 belongs to PR #1602, not #1615. PR #1615's actual latest run is 27934981657 (created 09:52 IDT Jun 22) — pre-commit FAIL. Regression has been ongoing since at least Jun 21 evening. |
| **⚠️ PR #1606 e2e-smoke now PENDING** | Was FAIL (54min+). New CI run underway — e2e-api now PASS. May be progressing toward green. |
| **↔ PR #1604 GH Actions CI still not running** | ~20h since un-draft (17:30 IDT Jun 21). Only CodeRabbit. Critical, unchanged. |
| **↔ PR #1588 pre-commit still FAILING** | 4th consecutive heartbeat with this regression from Jun 22 09:24 IDT main merge. Unchanged. |
| **↔ PR #1602 still green, no reviewer** | Fully green, now ~20h with no reviewer. Unchanged. |
| **No new merges** | Step 1 sweep confirmed: no PRs merged since Jun 21. |

---

## Attention Items

### ⚠️ CORRECTION — PR #1615 (JN-5677) — still pre-commit FAILING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615) was incorrectly reported as "ALL GREEN" by the 09:02, 09:34, and 11:03 IDT heartbeats. Those sessions cited CI run 27937907242, which belongs to PR #1602, not #1615.

PR #1615's actual latest CI run is 27934981657 (created 09:52 IDT Jun 22) — **pre-commit FAIL**. The regression is ongoing.

**Current state:** DRAFT, pre-commit FAIL, blocked on JN-5676 (#1604) merging. Fix needed even before un-drafting.

---

### 🔴 PR #1604 (JN-5676) — GH Actions CI NOT Running (~20h after un-draft)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

Un-drafted ~17:30 IDT Jun 21. Now 11:30 IDT Jun 22 — ~20h later. GH Actions CI has **still not triggered** — only CodeRabbit. Very abnormal.

**Required action:** Manually re-trigger CI (push empty commit or use GitHub UI → Re-run workflows), then address CodeRabbit comments, confirm CI green, request reviewer.

---

### 🔴 URGENT — PR #1588 (JN-5546) — pre-commit FAIL (4th heartbeat)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

Was FULLY GREEN at 09:02 IDT. Main merged into branch at 09:24 IDT Jun 22 — pre-commit now FAILING. Fourth consecutive heartbeat with this state. Jira status still "In Progress" but should be "In Review".

**Required action:** Fix pre-commit failures in the branch, then assign a reviewer. Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) to "In Review" when green.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) — FULLY GREEN (~20h waiting)

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

All checks pass/skip (run 27937907242). OPEN, MERGEABLE, no reviewer. Now ~20h waiting.

**Required action:** Assign a reviewer immediately.

---

### ⚠️ MONITORING — PR #1606 (JN-5725) — e2e-smoke now PENDING

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): MERGEABLE, REVIEW_REQUIRED. Pre-commit ✅. e2e-api now ✅ PASS (was FAIL). e2e-smoke **PENDING** (new run in progress). Possible improvement.

**Status:** Monitor — if e2e-smoke passes this will be fully green.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (3 items)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 5+ days stale — should be Done |
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, pre-commit FAIL | Should be "In Review" (open PR) |
| [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | DRAFT, pre-commit FAIL | Jira slightly ahead — PR still draft + failing |

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
