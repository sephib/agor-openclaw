# Board State — jounce-workflow-ai

*Last updated: 2026-06-25 13:32 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **DRAFT** MERGEABLE | ✅ ALL PASS/SKIP | REVIEW_REQUIRED | 🟢 **PR #1622** — DRAFT, all CI passing. Needs promotion from DRAFT. |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Validate | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **OPEN** MERGEABLE | ❌ **2 FAIL** (e2e-product/e2e FAIL 43m53s + e2e-tests FAIL 3s, run 28153233486 COMPLETE) | REVIEW_REQUIRED | 🔴 **CI FAILING** — run 28153233486 now fully complete with FAILURE. Both e2e-product AND e2e-tests FAIL. No new CI run triggered. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | **Respond** | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** MERGEABLE | ❌ **2 FAIL** (integration-run + integration-tests, run 28153631250) | reviewDecision="" | 🔴 **CI FAILING** — integration tests fail. CodeRabbit: 10 actionable comments. Jira Done but PR stuck. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGEABLE | ❌ **2 FAIL** (pre-commit + pre-commit-run/pre-commit) | reviewDecision="" | 🔴 **CI FAILING** — pre-commit fails; Jira should be "In Review" |
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
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ⏳ **e2e-smoke PENDING** (run 28163223200 IN PROGRESS since 13:17 IDT — all others ✅ PASS) | OPEN, MERGEABLE | 🟡 **NEW PUSH + NEW CI RUN** — developer pushed new commit (d9ae5eb6) at 13:17 IDT, cancelling run 28161157784. New run 28163223200 in progress: all checks PASS, e2e-smoke PENDING. Positive development. |

---

## Key Changes Since Last Run (13:32 IDT Jun 25)

| What observed | Status |
|---|---|
| **#1606 NEW PUSH** | Developer pushed new commit (SHA d9ae5eb6) at ~13:17 IDT. Previous run 28161157784 **CANCELLED** by new push. New run 28163223200 **IN PROGRESS** (started 13:17 IDT) — all checks PASS, e2e-smoke still PENDING. Positive — active fix attempt. |
| **#1623 unchanged** | Still ❌ 2 FAIL — e2e-product/e2e FAIL (43m53s) + e2e-tests FAIL (3s), run 28153233486. No new CI run. |
| **#1615 unchanged** | Still 2 FAIL (integration-run + integration-tests, run 28153631250). |
| **#1622 unchanged** | Still DRAFT, all CI PASS/SKIP. |
| **#1588 unchanged** | Still pre-commit FAIL. |
| **No new merges** | Step 1 sweep confirmed no new merges of tracked PRs. |
| **Jira unchanged** | JN-5616 In Review, JN-5724 In Review, JN-5677 Done, JN-5546 In Progress (stale) |

---

## Attention Items

### 🔴 PR #1623 (JN-5616) — CI FAILING — both e2e checks fail

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- OPEN, MERGEABLE, REVIEW_REQUIRED
- CI: ❌ **2 FAIL** — e2e-product/e2e FAIL (43m53s) + e2e-tests FAIL (3s) — run 28153233486 COMPLETE
- e2e-tests failing in 3s suggests a setup/config error, not a test content failure
- Jira [JN-5616](https://jounce.atlassian.net/browse/JN-5616): In Review
- **Action needed:** Investigate e2e-product and e2e-tests failures; fix and push to trigger new CI run.

---

### 🔴 PR #1615 (JN-5677) — Integration CI failing

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- OPEN, MERGEABLE, reviewDecision=""
- CI: ❌ 2 FAIL — `integration-run/integration` + `integration-tests` (run 28153631250)
- CodeRabbit posted **10 actionable comments** at 07:28 IDT — issues in historical.py, benchmark_visibility_notebook.py, transforms.py, operational.py
- In **Respond** zone — odd placement given CI failures (Respond is post-merge comms)
- Jira [JN-5677](https://jounce.atlassian.net/browse/JN-5677): Done ✅
- **Action needed:** Fix integration test failures; address CodeRabbit actionable items. Consider moving back to Code/Revise zone.

---

### 🟡 PR #1606 (JN-5725, off-board) — NEW PUSH + CI IN PROGRESS

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- Developer pushed new commit (SHA d9ae5eb6) at ~13:17 IDT Jun 25
- Previous run 28161157784 **CANCELLED** by new push
- New run 28163223200 **IN PROGRESS** (started 13:17 IDT): all checks ✅ PASS, e2e-smoke ⏳ PENDING
- JIRA [JN-5725](https://jounce.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Monitor result of run 28163223200 (e2e-smoke running). If passes → ready for review. If fails again → root cause investigation required.

---

### 🟢 PR #1622 (JN-5724) — DRAFT: promote when ready

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- DRAFT, MERGEABLE, REVIEW_REQUIRED, ALL CI PASS/SKIP
- Jira [JN-5724](https://jounce.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** Promote from DRAFT → Ready for Review

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + needs reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (9 ✅, 2 fail, 5 skip). PR is MERGEABLE (no git conflicts). Not a DRAFT.

**Required action:** (1) Fix pre-commit failures. (2) Assign reviewer. (3) Update [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

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
