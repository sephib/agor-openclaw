# Board State — jounce-workflow-ai

*Last updated: 2026-06-27 06:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (run 28164293495, unchanged since Jun 25 13:32 IDT) | REVIEW_REQUIRED | 🟡 **CONFLICTING — weekend, no rebase done.** CI still ALL PASS. Needs rebase before merge. |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Validate | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (run 28153233486, unchanged since Jun 25 13:32 IDT) | REVIEW_REQUIRED | 🟡 **CONFLICTING — weekend, no rebase done.** CI still ALL PASS. Needs rebase before merge. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | **Revise** | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** CONFLICTING | ⚠️ **CI CHECKS GONE** — only CodeRabbit showing (no run data since Jun 25 13:05 IDT) | ="" (no decision) | 🟡 **CI BLANK** — prior integration failures (run 28167796913) no longer in rollup. Branch may have been touched but CI not triggered. Still CONFLICTING. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) OPEN CONFLICTING | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996, stale) | reviewDecision="" | 🔴 **STALE** — unchanged since Jun 17. Pre-commit FAIL, CONFLICTING. Jira should be "In Review". |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT OPEN CONFLICTING | — | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jira-operations | — | (no zone) | — | — | — | — | ⚠️ session timed_out 07:38 IDT Jun 25. No PR, no Jira, no zone. Needs decision. |

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
- fix-dashboard-syntax-error — no longer visible in any zone scan (was Plan zone); presumed archived

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ **3 FAIL** (e2e-gpu-live, e2e-smoke, e2e-tests — run 28231394764) | OPEN, MERGEABLE (no git conflict) | 🔴 **CI WORSENED** — The e2e-smoke that was pending at 16:02 IDT Jun 25 came back FAILED. Also e2e-gpu-live FAIL, e2e-tests FAIL. Other checks (e2e-api, integration, pre-commit, tox, nox, atlas-validate) still ✅ PASS. Was expected to be merge-ready — now blocked on CI. |

---

## Key Changes Since Last Run (00:00 IDT Jun 27)

| What observed | Status |
|---|---|
| **Board fully static** | No new merges, no CI changes on any tracked PR since Jun 27 00:00 IDT. |
| **#1622 unchanged** | Still CONFLICTING, CI ALL PASS (run 28164293495). Weekend — no rebase. |
| **#1623 unchanged** | Still CONFLICTING, CI ALL PASS (run 28153233486). Weekend — no rebase. |
| **#1606 unchanged** | Still 3 FAIL (e2e-gpu-live, e2e-smoke, e2e-tests, run 28231394764). Off-board, MERGEABLE. |
| **#1615 unchanged** | CI still blank — only CodeRabbit in rollup. Still CONFLICTING. |
| **#1588 unchanged** | Still 2 FAIL pre-commit (run 27933817996). Stale. |
| **No new merges** | Step 1 sweep confirmed no new merges. |

---

## Attention Items

### 🔴 PR #1606 (JN-5725, off-board) — CI WORSENED (3 FAIL)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- OPEN, MERGEABLE (no git conflict)
- Run 28231394764 — **3 FAIL**: e2e-gpu-live ❌, e2e-smoke ❌, e2e-tests ❌
- Passing: e2e-api ✅, integration ✅, pre-commit ✅, tox ✅, nox ✅, atlas-validate ✅
- Jira [JN-5725](https://jounce.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Investigate e2e-smoke failure — may be flaky or reflect a real regression in the vllm-log-analyzer integration.

---

### 🟡 PR #1615 (JN-5677) — CI BLANK + CONFLICTING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- OPEN, CONFLICTING
- ⚠️ **CI checks missing from rollup** — only CodeRabbit showing (SUCCESS, Jun 25 13:05 IDT). Previous integration failures (run 28167796913) no longer appear.
- Jira [JN-5677](https://jounce.atlassian.net/browse/JN-5677): Done ✅
- **Action needed:** (1) Determine if branch was force-pushed without CI trigger. (2) Fix merge conflict with main. (3) Re-run CI.

---

### 🟡 PR #1622 (JN-5724) — CI ALL PASS but CONFLICTING

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- OPEN, CONFLICTING (since Jun 25 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28164293495 — **ALL checks ✅ PASS** (e2e-smoke 10m29s)
- Jira [JN-5724](https://jounce.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** Rebase on main. CI will re-run. Assign reviewer once green.

---

### 🟡 PR #1623 (JN-5616) — CI ALL PASS but CONFLICTING

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- OPEN, CONFLICTING (since Jun 25 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28153233486 — **ALL checks ✅ PASS** (e2e-product 27m56s, e2e-smoke 10m11s)
- Jira [JN-5616](https://jounce.atlassian.net/browse/JN-5616): In Review ✅
- **Action needed:** Rebase on main. CI will re-run. Assign reviewer once green.

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + CONFLICTING (stale)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (run 27933817996). PR is CONFLICTING. Stale since Jun 17.

**Required action:** (1) Fix pre-commit failures. (2) Resolve merge conflict. (3) Assign reviewer. (4) Update [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ JN-5612 — sprint ticket without board worktree

[JN-5612](https://jounce.atlassian.net/browse/JN-5612): "Fix github.GITHUB_SHA → github.sha in all workflow run-name fields" — **In Progress**, assigned to Joseph. No worktree on board.

---

### ⚠️ jira-operations — session timed_out, no zone

Branch `jira-operations` — No PR, no Jira ticket, no zone assigned.
- Session timed_out at 07:38 IDT (Jun 25). Title: "Create Q4 Planning Epic + Stories"
- **Action needed:** Joseph to decide: archive (if one-off task) or assign zone + create tickets

---

### ⚠️ internal-cr-system — no PR, no Jira, stagnant

Branch `internal-cr-system` in Code zone — no PR, no Jira ticket. Stagnant since Jun 18. filesystem_status: failed (git lock on .git/config).

---

### ⚠️ Jira mismatches (1 item)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, 2 CI FAIL + CONFLICTING | Should be "In Review" AND needs CI fix |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5612](https://jounce.atlassian.net/browse/JN-5612) | Fix github.GITHUB_SHA → github.sha | **In Progress** | No worktree |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache, --skip-estimator CLI flags | **In Progress** | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps — BRANCH_NAME on dispatch + scoped secrets | **Backlog** | No worktree |

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
| JN-5762 | [#1624](https://github.com/Jounce-IO/jounce/pull/1624) | Jun 24 14:05 IDT ✅ |
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
