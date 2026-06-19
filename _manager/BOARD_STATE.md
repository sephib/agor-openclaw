# Board State — jounce-workflow-ai

*Last updated: 2026-06-19 10:03 IDT (30-min advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5675-historical-visibility | [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | Code | In Progress | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | ❌❌ **CATASTROPHIC** — pre-commit + tox + integration + e2e-api + nox + integration-tests + e2e-tests ALL FAILING | — | 🚨 NOW **MERGEABLE** (conflicts resolved by session 019ede80) but CI catastrophic — broken `__init__.py` fix needed |
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ❌ pre-commit FAIL only + **CONFLICTING** (tox/nox/integration/e2e all ✅) | — | 🔴 CONFLICTING; CI improved — only pre-commit blocking once conflict resolved |
| jn-5546-docs-module-layout | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) | sephib COMMENTED (MUST FIX items) | 🔴 Pre-commit fix + sephib MUST FIX items |
| ci-statistics-notebook | [JN-5708](https://jounce.atlassian.net/browse/JN-5708) (issue link) | Code | Done | — | — | — | ⚠️ No sessions; JN-5708 Done; scope unclear |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jn-5674-operational-visibility | [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | Respond | Done | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) MERGED | — | — | 🗑️ Should be ARCHIVED — PR merged Jun 18 |

---

## Key Changes Since Last Run (Jun 19 09:33 IDT)

| What observed | Status |
|---|---|
| **PR #1601 (jn-5675) now MERGEABLE** | 🆕 Conflicts resolved — was CONFLICTING at 09:33 IDT. CI still catastrophic (8 checks failing). |
| **PR #1604 (jn-5676) CI improved** | 🆕 tox / integration / nox / integration-tests / e2e-tests all NOW PASSING. Only pre-commit failing + still CONFLICTING. |
| **PR #1588 (jn-5546) unchanged** | ❌ pre-commit still failing, MERGEABLE. No new CI run. |
| **No new merges to main** | ℹ️ Last merge: PR #1599 (jn-5674) Jun 18 23:55 IDT |
| **JN-5670 "Benchmark Visibility Dashboard" in Jira** | ⚠️ In Progress — no board worktree |
| **JN-5539, JN-5244 in Jira** | ℹ️ In Progress — not on this board |

---

## Attention Items

### 🚨 HIGHEST PRIORITY — jn-5675 `__init__.py` still broken

PR #1601 is now **MERGEABLE** (conflicts resolved by session 019ede80 at ~09:14 IDT). But ALL CI checks continue to fail:
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

### 🔴 jn-5676 — CONFLICTING but CI Almost Clean

**Good news:** CI for PR #1604 significantly improved. tox / integration / nox / integration-tests / e2e-tests are all PASSING. Only pre-commit is failing (2 checks). Once rebased and pre-commit fixed, this PR would be ready to un-draft and review.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX

Unchanged. MERGEABLE but pre-commit failing + sephib MUST FIX items outstanding.

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
