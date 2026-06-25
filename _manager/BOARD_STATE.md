# Board State — jounce-workflow-ai

*Last updated: 2026-06-25 16:02 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (e2e-smoke ✅ 10m29s, run 28164293495) | REVIEW_REQUIRED | 🟡 **NOW CONFLICTING** — CI still ALL PASS (run unchanged). Developed merge conflict with main since 15:32 run. Needs rebase. |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Validate | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (e2e-product ✅ 27m56s, run 28153233486) | REVIEW_REQUIRED | 🟡 **NOW CONFLICTING** — CI still ALL PASS (run unchanged). Developed merge conflict with main since 15:32 run. Needs rebase. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | **Revise** | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** CONFLICTING | ⚠️ **2 FAIL** (integration-run + integration-tests, run 28167796913) — run COMPLETE | REVIEW_REQUIRED | 🟡 **CI STABLE at 2 FAIL** — run 28167796913 now complete: e2e-api ✅ PASS (was pending), e2e-smoke ✅ PASS. Only integration-run + integration-tests still FAIL. CONFLICTING unchanged. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) UNKNOWN | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996) | reviewDecision="" | 🔴 **CI FAILING** — pre-commit fails; Jira should be "In Review" |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
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
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ⏳ **MOSTLY PASS** (run 28171648898 IN PROGRESS: most ✅, e2e-smoke ⏳) | OPEN, **MERGEABLE** (conflict resolved!) | 🟢 **CONFLICT RESOLVED + CI ADVANCING** — run 28171648898: all checks ✅ PASS (e2e-api ✅ 3m53s, integration ✅, pre-commit ✅, tox ✅), e2e-smoke ⏳ still running. Previously CONFLICTING; now MERGEABLE. |

---

## Key Changes Since Last Run (15:32 IDT Jun 25)

| What observed | Status |
|---|---|
| **#1622 NOW CONFLICTING** | CI still ALL PASS (run 28164293495 unchanged). REVIEW_REQUIRED. **New merge conflict with main since 15:32.** Needs rebase. |
| **#1623 NOW CONFLICTING** | CI still ALL PASS (run 28153233486 unchanged). REVIEW_REQUIRED. **New merge conflict with main since 15:32.** Needs rebase. |
| **#1615 — CodeRabbit pending** | No new full CI run complete. Integration failures (2 FAIL, run 28167796913) still standing. CONFLICTING unchanged. |
| **#1606 — conflict RESOLVED + MERGEABLE** | Was CONFLICTING at 15:32; now MERGEABLE. New run 28171648898: all ✅ PASS, e2e-smoke ⏳ pending. |
| **#1588 unchanged** | Still 2 FAIL pre-commit (run 27933817996). CONFLICTING. |
| **No new merges** | Step 1 sweep confirmed no new merges. |
| **Jira unchanged** | JN-5616 In Review, JN-5724 In Review, JN-5677 Done, JN-5546 In Progress (stale), JN-5612 In Progress (no worktree) |

---

## Attention Items

### 🟡 PR #1622 (JN-5724) — CI ALL PASS but NOW CONFLICTING

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- OPEN, CONFLICTING (new since 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28164293495 — **ALL checks ✅ PASS** (including e2e-smoke 10m29s) — CI still green
- Jira [JN-5724](https://jounce.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** (1) Rebase on main to resolve merge conflict. CI will re-run. (2) Assign reviewer once green again.

---

### 🟡 PR #1623 (JN-5616) — CI ALL PASS but NOW CONFLICTING

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- OPEN, CONFLICTING (new since 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28153233486 — **ALL checks ✅ PASS** (including e2e-product 27m56s, e2e-smoke 10m11s) — CI still green
- Jira [JN-5616](https://jounce.atlassian.net/browse/JN-5616): In Review ✅
- **Action needed:** (1) Rebase on main to resolve merge conflict. CI will re-run. (2) Assign reviewer once green again.

---

### 🟡 PR #1615 (JN-5677) — 2 CI FAIL + CONFLICTING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- OPEN, CONFLICTING, REVIEW_REQUIRED
- CI: Run 28167796913 now **COMPLETE**:
  - ✅ PASS: pre-commit, pre-commit-run, e2e-api (resolved from pending!), e2e-smoke, tox, nox, atlas-validate
  - ❌ FAIL: integration-run, integration-tests
- 2 FAIL remaining (integration tests)
- **CONFLICTING** — merge conflict with main still present
- Jira [JN-5677](https://jounce.atlassian.net/browse/JN-5677): Done ✅
- **Action needed:** (1) Fix integration test failures. (2) Resolve merge conflict with main.

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + needs reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (run 27933817996). PR is MERGEABLE (no git conflicts). Not a DRAFT.

**Required action:** (1) Fix pre-commit failures. (2) Assign reviewer. (3) Update [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### 🟢 PR #1606 (JN-5725, off-board) — Conflict RESOLVED + CI nearly done

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- OPEN, **MERGEABLE** (conflict resolved since 15:32 IDT)
- Run 28171648898 IN PROGRESS:
  - ✅ PASS: e2e-api (3m53s), integration-run, integration-tests, pre-commit, pre-commit-run, tox-run, atlas-validate, nox
  - ⏳ PENDING: e2e-smoke
- JIRA [JN-5725](https://jounce.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Wait for e2e-smoke to complete. If PASS, this PR becomes fully green and merge-ready.

---

### ⚠️ JN-5612 — sprint ticket without board worktree

[JN-5612](https://jounce.atlassian.net/browse/JN-5612): "Fix github.GITHUB_SHA → github.sha in all workflow run-name fields" — **In Progress**, assigned to Joseph. No worktree on board. Newly spotted in sprint this run.

---

### ⚠️ jira-operations — new worktree, session timed_out

Branch `jira-operations` — appeared in board scan Jun 25 08:00 IDT. No PR, no Jira ticket, no zone assigned.
- Session timed_out at 07:38 IDT (Jun 25). Title: "Create Q4 Planning Epic + Stories"
- No git commits (SHA unchanged from base)
- **Action needed:** Joseph to decide: archive (if one-off task) or assign zone + create tickets

---

### ⚠️ internal-cr-system — no PR, no Jira, stagnant

Branch `internal-cr-system` in Code zone — no PR, no Jira ticket. Stagnant since Jun 18. filesystem_status: failed (git lock on .git/config).

---

### ⚠️ Jira mismatches (1 item)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, 2 CI FAIL | Should be "In Review" AND needs CI fix |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5612](https://jounce.atlassian.net/browse/JN-5612) | Fix github.GITHUB_SHA → github.sha | **In Progress** | No worktree — newly spotted |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
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
