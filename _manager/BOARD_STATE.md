# Board State — jounce-workflow-ai

*Last updated: 2026-06-24 16:30 IDT (advance heartbeat)*

> ⚠️ BOARD_STATE.md was ~25 hours old at start of this run (last updated Jun 23 15:30 IDT). Sessions at 08:00 + 08:30 IDT Jun 24 failed; 11:30 + 12:30 IDT sessions idle with no recorded output. Full refresh performed.

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **DRAFT** UNKNOWN (prev MERGEABLE) | ✅ ALL PASS (run 28020178138) | REVIEW_REQUIRED | 🟢 **PR #1622** — DRAFT, all CI passing. Needs promotion from DRAFT. |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Validate | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **DRAFT** MERGEABLE | ✅ ALL PASS (run 28020219339) | REVIEW_REQUIRED | 🟢 **PR #1623** — DRAFT, all CI passing. Needs promotion from DRAFT. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Code | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** CONFLICTING | ⚠️ Only CodeRabbit (CONFLICTING blocks CI) | REVIEW_REQUIRED | 🔴 **UNBLOCK** — resolve conflicts, fix pre-commit, promote from DRAFT. Jira Done. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGEABLE | ❌ **pre-commit FAIL** (run 27933817996) | reviewDecision="" | 🔴 **CI FAILING** — pre-commit FAIL; Jira should be "In Review" |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ filesystem_status: failed (git lock error). No PR. Stagnant. |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

**Also on board (non-jounce / utility):**
- `fix-dashboard-syntax-error` — Plan zone — Julie-internal branch, filesystem failed (origin/private-julie error), no PR. Present since Jun 17. Non-blocking.
- `model-packaging-cr` — Code Review zone — model-packaging-pipeline repo, no PR, no issue. Old/inactive.

**Archived This Session:**
- none

**Archived Previous (11:30 IDT Jun 23):**
- jn-5676-notebook-scaffold (archived — PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) MERGED 10:51 IDT Jun 23) ✅

**Archived Previous (14:30 IDT Jun 21):**
- jn-5675-historical-visibility (archived — PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) MERGED 16:15 IDT Jun 21)

**Archived Previous (14:00 IDT Jun 21):**
- ci-statistics-notebook (archived — JN-5708 Done + 3+ days inactive + no PR)

**Archived Previous (12:00 IDT Jun 21):**
- jn-5729-pin-uv-default-python-2 (archived — PR #1608 MERGED)
- jn-5729-pin-python-313 (archived — PR #1607 CLOSED)
- jn-5729-pin-uv-default-python (archived — JN-5729 done, no PR)
- code-reviewes (archived — review done Jun 15, 6+ days inactive)

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
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | 🟡 NEW CI RUN IN PROGRESS (run 28102143811) — integration+pre-commit+tox+e2e-api PENDING; atlas-validate ✅ check-changes ✅ JIRA Association ✅ CodeRabbit ✅ | OPEN, MERGEABLE (**was CONFLICTING**) | 🟡 **CI RUNNING** — someone rebased since last check. Previously CONFLICTING+CI FAILED. JN-5725 Done. Monitor outcome. |

---

## Key Changes Since Last Run (Jun 23 15:30 IDT)

| What observed | Status |
|---|---|
| **🟡 PR #1606 REBASED** | Was CONFLICTING+CI FAILED (run 28015066339). Now MERGEABLE + new CI run 28102143811 IN PROGRESS. Someone pushed a rebase. Major positive change. |
| **↔ PR #1622 (JN-5724)** | DRAFT, CI ALL PASS (run 28020178138). mergeable UNKNOWN (GitHub cache — was MERGEABLE). No functional change. |
| **↔ PR #1623 (JN-5616)** | DRAFT, CI ALL PASS (run 28020219339). MERGEABLE. No functional change. |
| **↔ PR #1615 (JN-5677)** | DRAFT + CONFLICTING. Only CodeRabbit shows (conflicts block CI). No change. |
| **↔ PR #1588 (JN-5546)** | MERGEABLE, pre-commit FAIL (run 27933817996). No new CI run. |
| **↔ internal-cr-system** | filesystem_status: failed (git lock). No change. |
| **⚠️ 25h+ gap** | Sessions 08:00+08:30 IDT Jun 24 failed; 11:30+12:30 IDT idle with no output recorded. |

---

## Attention Items

### 🟡 PR #1606 (JN-5725) — NEW CI RUN IN PROGRESS

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow (JN-5725)`
- Was CONFLICTING + CI FAILED (run 28015066339, e2e-smoke + e2e-tests). Now **MERGEABLE** + fresh CI run 28102143811 running.
- JIRA [JN-5725](https://jounce.atlassian.net/browse/JN-5725): Done
- **Watch:** If CI passes, PR is ready for reviewer assignment.

---

### 🟢 PR #1622 (JN-5724) — DRAFT: promote when ready

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- DRAFT, mergeable UNKNOWN (GitHub cache; was MERGEABLE), ALL CI PASS ✅ (run 28020178138)
- Jira [JN-5724](https://jounce.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** Promote from DRAFT → Ready for Review

---

### 🟢 PR #1623 (JN-5616) — DRAFT: promote when ready

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- DRAFT, MERGEABLE, ALL CI PASS ✅ (run 28020219339)
- Jira [JN-5616](https://jounce.atlassian.net/browse/JN-5616): In Review ✅
- Agor zone: Validate
- **Action needed:** Promote from DRAFT → Ready for Review

---

### 🔴 PR #1615 (JN-5677) — UNBLOCK: Resolve conflicts + promote from DRAFT

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): Still DRAFT + CONFLICTING (CI blocked — only CodeRabbit shows).
Agor zone: Code. Jira JN-5677: Done.

Remaining work:
1. Resolve merge conflicts (rebase onto main)
2. Fix pre-commit failure
3. Promote from DRAFT → Ready for Review

---

### 🔴 PR #1588 (JN-5546) — pre-commit FAIL + needs reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): pre-commit CI FAILING (run 27933817996). PR is MERGEABLE (no git conflicts). Not a DRAFT.

**Required action:** (1) Fix pre-commit in PR #1588. (2) Assign reviewer. (3) Update [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ internal-cr-system — filesystem failed, stagnant

Branch `internal-cr-system` in Code zone — filesystem_status: `failed` (git lock error: `.git/config` file exists). No PR. Stagnant since Jun 18.

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
| [JN-5612](https://jounce.atlassian.net/browse/JN-5612) | Fix github.GITHUB_SHA → github.sha in all workflow run-name fields | Backlog | No worktree |

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
