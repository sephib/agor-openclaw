# Board State — jounce-workflow-ai

*Last updated: 2026-06-23 13:31 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **DRAFT** MERGEABLE | ✅ ALL PASS (run 28020178138) | REVIEW_REQUIRED | 🟢 **PR #1622 CREATED** — DRAFT, all CI passing. Needs promotion from DRAFT. |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Publish | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **DRAFT** MERGEABLE | ✅ ALL PASS (run 28020219339) | REVIEW_REQUIRED | 🟢 **PR #1623 CREATED** — DRAFT, all CI passing. Needs promotion from DRAFT. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** CONFLICTING | ❌ pre-commit FAIL (run 27934981657) | REVIEW_REQUIRED | 🔴 **UNBLOCK** — resolve conflicts, fix pre-commit, promote from DRAFT |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ **pre-commit FAIL** (run 27933817996) | reviewDecision="" | 🔴 **CI FAILING** — pre-commit FAIL; Jira should be "In Review" |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ Session idle since 09:50 IDT; status after re-dispatch unclear |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

**Archived This Session (11:30 IDT Jun 23):**
- jn-5676-notebook-scaffold (archived 11:30 IDT — PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) MERGED 10:51 IDT Jun 23) ✅

**Archived Previous (14:30 IDT Jun 21):**
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
- model-packaging-cr (removed from tracking — not on this board; confirmed absent from board scan)

**Removed from tracking (confirmed archived on board):**
- dual-heartbeat-system — confirmed archived in board scan Jun 23
- standup-drafts — confirmed archived in board scan Jun 23

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ last known: FAILURE (run 28015066339) — no new CI run detected | OPEN, **CONFLICTING** | 🔴 **CI FAILED + CONFLICTING** — e2e-smoke and e2e-tests failed. Still conflicting. JN-5725 Done. |

---

## Key Changes Since Last Run (Jun 23 13:01 IDT)

| What observed | Status |
|---|---|
| **🟢 jn-5724 → PR #1622 CREATED** | Draft PR created: MERGEABLE, all CI checks PASS. Jira already "In Review". |
| **🟢 jn-5616 → PR #1623 CREATED** | Draft PR created: MERGEABLE, all CI checks PASS. Jira already "In Review". |
| **↔ PR #1615 (JN-5677)** | DRAFT + CONFLICTING + pre-commit FAIL. No change. |
| **↔ PR #1588 (JN-5546)** | pre-commit FAIL. MERGEABLE. No change. |
| **↔ PR #1606 (JN-5725)** | OPEN, CONFLICTING. No new CI run. Last known: CI FAILED. |
| **↔ internal-cr-system** | Session idle since 09:50 IDT after re-dispatch. |

---

## Attention Items

### 🟢 PR #1622 (JN-5724) — DRAFT: promote when ready

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- DRAFT, MERGEABLE, ALL CI PASS ✅
- Jira [JN-5724](https://jounce.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** Promote from DRAFT → Ready for Review

---

### 🟢 PR #1623 (JN-5616) — DRAFT: promote when ready

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- DRAFT, MERGEABLE, ALL CI PASS ✅
- Jira [JN-5616](https://jounce.atlassian.net/browse/JN-5616): In Review ✅
- **Action needed:** Promote from DRAFT → Ready for Review

---

### 🔴 PR #1606 (JN-5725) — CI FAILED + CONFLICTING

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): CI run 28015066339 completed with FAILURE:
- e2e-smoke: FAILED
- e2e-tests: FAILED

PR also CONFLICTING. JN-5725 Jira: Done.

Required actions:
1. Fix e2e failures (check run 28015066339 logs for root cause)
2. Rebase feat/jn-5725-integrate-vllm-log-analyzer onto main
3. Push + trigger new CI run
4. Assign reviewer

---

### 🔴 PR #1615 (JN-5677) — UNBLOCK: Resolve conflicts + promote from DRAFT

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): Still DRAFT + CONFLICTING + pre-commit FAIL (since Jun 22).

Remaining work:
1. Resolve merge conflicts (rebase onto main)
2. Fix pre-commit failure (run 27934981657)
3. Promote from DRAFT → Ready for Review

Note: JN-5677 Jira is already Done.

---

### 🔴 PR #1588 (JN-5546) — pre-commit FAIL + needs reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): pre-commit CI FAILING (run 27933817996). PR is MERGEABLE (no git conflicts).

**Required action:** (1) Fix pre-commit in PR #1588. (2) Assign reviewer. (3) Update [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ internal-cr-system — session idle, status unclear

Session [019eda0a](http://127.0.0.1:3030/ui/s/019eda0ae5667f0fa8bf3d95/) — idle since 09:50 IDT after re-dispatch. Unknown whether git lock was resolved and work completed. Check session for results.

---

### ⚠️ Jira mismatches (1 item)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, pre-commit FAIL | Should be "In Review" AND needs pre-commit fix |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache CLI flags to runner | **In Progress** | No worktree — may be older/lower priority |

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
| JN-5759 | [#1619](https://github.com/Jounce-IO/jounce/pull/1619) | Jun 23 12:30 IDT ✅ (off-board, by another contributor) |
| [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) | Jun 23 10:51 IDT ✅ |
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
