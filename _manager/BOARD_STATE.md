# Board State — jounce-workflow-ai

*Last updated: 2026-06-22 09:34 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ⚠️ Only CodeRabbit ✅ — GH Actions CI **not triggered** ~17h after un-draft | reviewDecision="" | 🔴 **GH Actions CI not running** — manual re-trigger needed |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Progress | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ✅ **ALL GREEN** — pre-commit now PASS (was FAIL at 09:02) | REVIEW_REQUIRED | 🎉 **CI now fully green** — still draft, blocked on #1604 merging first |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ **pre-commit FAIL** (regression — main merged into branch at 09:24 IDT, triggered new CI run) | reviewDecision="" | 🔴 **REGRESSION** — was green at 09:02, main merge broke pre-commit again |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit | — | 🔴 CONFLICTING; frozen |
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
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ **ALL GREEN** | OPEN, MERGEABLE, reviewDecision="" | 🎉 **FULLY GREEN — assign reviewer NOW** (12h+ waiting) |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ e2e-smoke FAIL (54min) + e2e-tests FAIL (pre-commit ✅) | OPEN, **MERGEABLE**, REVIEW_REQUIRED | 🔴 e2e-smoke + e2e-tests FAIL — unchanged from last night |

---

## Key Changes Since Last Run (Jun 22 09:02 IDT)

| What observed | Status |
|---|---|
| **🔴 PR #1588 REGRESSION** | Was FULLY GREEN at 09:02 IDT. Main branch merged into the branch at 09:24 IDT, triggering new CI run. pre-commit now FAILING again. |
| **🎉 PR #1615 NOW ALL GREEN** | Was pre-commit FAIL at 09:02 IDT. Now ALL CI passing including pre-commit! Still a draft, blocked on #1604 merging first. |
| **↔ PR #1604 GH Actions CI still not running** | ~17h since un-draft (17:30 IDT Jun 21). Only CodeRabbit. Unchanged. |
| **↔ PR #1602 still green, no reviewer** | Fully green, now 13h+ with no reviewer. |
| **↔ PR #1606 e2e still failing** | e2e-smoke FAIL (54min) + e2e-tests FAIL — unchanged. |
| **No new merges** | Step 1 sweep: no PRs merged since Jun 21 last run. |

---

## Attention Items

### 🔴 URGENT — PR #1588 (JN-5546) — pre-commit FAIL AGAIN (regression)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

Was fully green at 09:02 IDT. Joseph (or GH auto-update) merged main into the branch at 09:24 IDT — new CI run triggered, pre-commit now FAILING. This is a regression from the "all green" state observed in the previous run.

**Required action:** Fix pre-commit failures in the branch, then assign a reviewer. Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) to "In Review" when green.

---

### 🎉 PR #1615 (JN-5677) — NOW ALL GREEN (pre-commit fixed)

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615) — "feat(jbenchmark): historical mode notebook cells (JN-5677)"

Was pre-commit FAIL at 09:02 IDT. Now ALL CI passing — pre-commit ✅, tox ✅, integration ✅, e2e-tests ✅, build ✅. Still DRAFT. Still blocked on JN-5676 (PR #1604) merging first.

**No action needed** — wait for #1604 to merge, then un-draft and request review.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) — FULLY GREEN (13h+ waiting)

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

All checks pass/skip. OPEN, MERGEABLE, no reviewer.

**Required action:** Assign a reviewer immediately.

---

### 🔴 PR #1604 (JN-5676) — GH Actions CI NOT Running (~17h after un-draft)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

Un-drafted ~17:30 IDT Jun 21. Now 09:34 IDT Jun 22 — ~17h later. GH Actions CI has **still not triggered** — only CodeRabbit. Very abnormal.

**Required action:** Manually re-trigger CI (push empty commit or use GitHub UI → Re-run workflows), then address CodeRabbit comments, confirm CI green, request reviewer.

---

### 🔴 OFF-BOARD — PR #1606 (JN-5725) — e2e Failure Persistent

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): MERGEABLE, REVIEW_REQUIRED. Pre-commit ✅. But e2e-smoke FAIL (54min timeout) + e2e-tests FAIL — unchanged.

**Required action:** Fix e2e failures.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (2 stale tickets)

| Ticket | Jira Status | PR | Merged/State | Days Stale |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 5+ days |
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, ALL GREEN | Should be "In Review" |

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
