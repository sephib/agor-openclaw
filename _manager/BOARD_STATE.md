# Board State — jounce-workflow-ai

*Last updated: 2026-06-20 20:00 IDT (30-min advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5675-historical-visibility | [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | Code | In Progress | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | ❌❌ **CATASTROPHIC** — pre-commit + tox + integration + e2e-api + nox + integration-tests + e2e-tests ALL FAILING | — | 🚨 MERGEABLE (conflicts resolved by session 019ede80) but CI catastrophic — broken `__init__.py` fix needed |
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ❌ pre-commit FAIL only + **CONFLICTING** (tox/nox/integration/e2e all ✅) | — | 🔴 CONFLICTING; CI improved — only pre-commit blocking once conflict resolved |
| jn-5546-docs-module-layout | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | sephib COMMENTED (MUST FIX items) | 🔴 Pre-commit fix + sephib MUST FIX items |
| ci-statistics-notebook | [JN-5708](https://jounce.atlassian.net/browse/JN-5708) (issue link) | Code | Done | — | — | — | ⚠️ No sessions; JN-5708 Done; scope unclear |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jn-5674-operational-visibility | [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | Respond | Done | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) MERGED | — | — | 🗑️ Should be ARCHIVED — PR merged Jun 18 |
| code-reviewes | — | Code Review | — | — | — | — | 🗑️ Should be ARCHIVED — review done Jun 15 (see PROPOSALS.md) |

---

## Key Changes Since Last Run (Jun 20 19:30 IDT)

| What observed | Status |
|---|---|
| **PR #1601 (jn-5675)** | ↔ UNCHANGED — MERGEABLE (no conflicts), CI catastrophic (8 checks failing). 48h+ no new commits since rebase at 09:19 IDT Jun 19. |
| **PR #1604 (jn-5676)** | ↔ UNCHANGED — CONFLICTING + DRAFT. pre-commit failing only. Last updated Jun 18 19:14 IDT (49h+). |
| **PR #1588 (jn-5546)** | ↔ UNCHANGED — BEHIND. pre-commit failing (2 checks). Last updated Jun 18 18:12 IDT (50h+). |
| **No new merges to main** | ℹ️ Last merge: PR #1599 (jn-5674) Jun 18 23:55 IDT — board fully static 48h+. |
| **PR #1606 (JN-5725, off-board)** | ↔ UNCHANGED — 5th CI run remains most recent (completed 18:52 IDT). No new runs since 18:52 IDT (~1h+). e2e-smoke/e2e ❌, e2e-tests ❌. All other 12 checks PASSING. |

---

## Attention Items

### 🚨 HIGHEST PRIORITY — jn-5675 `__init__.py` still broken

PR #1601 is **MERGEABLE** (conflicts resolved by session 019ede80 at ~09:14 IDT). But ALL CI checks continue to fail — now 48h+ without any fix:
- `pre-commit-run / pre-commit` FAILURE
- `tox-run / tox` FAILURE
- `integration-run / integration` FAILURE
- `e2e-api / e2e` FAILURE
- `pre-commit` FAILURE
- `nox` FAILURE
- `integration-tests` FAILURE
- `e2e-tests` FAILURE

Root cause: broken `__init__.py` conflict resolution from session 019ede80 ("merged both sides"). Fix session needed.

---

### 🔴 OFF-BOARD — PR #1606 (JN-5725) 5th CI Run COMPLETED: 5TH FAILURE

PR #1606 status as of 19:00 IDT Jun 20:
- **5th CI run COMPLETED: FAILURE** — completed 18:52 IDT (run ID: 27872550696)
- ✅ PASSING: check-changes, JIRA Association, pre-commit-run/pre-commit, tox-run/tox, integration-run/integration, e2e-api/e2e, pre-commit, nox, integration-tests, atlas-validate
- ❌ FAILING: **e2e-smoke/e2e** ❌, **e2e-tests** ❌
- Skipped: bake, atlas-validate-run, e2e-product
- MERGEABLE + REVIEW_REQUIRED (0 reviews)

**Pattern: 5 consecutive failures, same 2 tests failing, all else PASSING.** This is definitively a systemic e2e issue, not random flake. The e2e-smoke/e2e and e2e-tests are the only consistent failures across all 5 runs. Investigation of the e2e failure logs is now warranted before any further re-runs.

---

### 🔴 jn-5676 — CONFLICTING but CI Almost Clean

**Good news:** CI for PR #1604 significantly improved. tox / integration / nox / integration-tests / e2e-tests are all PASSING. Only pre-commit is failing (2 checks). Once rebased and pre-commit fixed, this PR would be ready to un-draft and review.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX

Unchanged. MERGEABLE + pre-commit failing + sephib MUST FIX items outstanding.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged.

---

### ⚠️ ci-statistics-notebook — scope unclear

No sessions. JN-5708 is Done. Unchanged.

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | [DEV] Historical mode notebook cells | **In Progress** | No worktree — likely covered by JN-5676 stub |
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Reduce Lychee precommit flaky results | Backlog | No worktree |
| [JN-5662](https://jounce.atlassian.net/browse/JN-5662) | Decouple libs/sql from services/validator | In Review | No worktree on this board |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache CLI flags to runner | **In Progress** | No worktree — may be older/lower priority |

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
| [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) | Jun 18 23:55 IDT ✅ |
| JN-5619 | [#1598](https://github.com/Jounce-IO/jounce/pull/1598) | Jun 18 13:33 UTC ✅ |
| [JN-5708](https://jounce.atlassian.net/browse/JN-5708) | [#1603](https://github.com/Jounce-IO/jounce/pull/1603) | Jun 18 12:42 UTC ✅ |
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Jun 17 ✅ |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
