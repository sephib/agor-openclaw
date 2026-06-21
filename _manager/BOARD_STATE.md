# Board State — jounce-workflow-ai

*Last updated: 2026-06-21 04:00 IDT (overnight advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5675-historical-visibility | [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | Code | In Progress | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | ❌❌ **CATASTROPHIC** — pre-commit + tox + integration + e2e-api + nox + integration-tests + e2e-tests ALL FAILING | — | 🚨 MERGEABLE but CI broken — `__init__.py` fix needed. 52h+ no new commits |
| jn-5729-pin-python-313 | [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | Code | Backlog (unassigned) | [#1607](https://github.com/Jounce-IO/jounce/pull/1607) | ⚠️ **SUSPICIOUS** — Only CodeRabbit after 5h. Full CI not triggered. | REVIEW_REQUIRED | 🔴 CI non-trigger — 5h+ since PR created 23:15 IDT Jun 20 |
| ci-statistics-notebook | [JN-5708](https://jounce.atlassian.net/browse/JN-5708) (issue link) | Code | Done | — | — | — | ⚠️ No sessions; JN-5708 Done; scope unclear |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ❌ pre-commit FAIL only (tox/nox/integration/e2e all ✅) + **CONFLICTING** | REVIEW_REQUIRED | 🔴 CONFLICTING; needs rebase + pre-commit fix to un-draft |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | — | 🔴 Pre-commit fix needed + sephib MUST FIX comments outstanding |
| code-reviewes | — | Code Review | — | — | — | — | 🗑️ Should be ARCHIVED — review done Jun 15 |
| jn-5674-operational-visibility | [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | Respond | Done | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) MERGED | — | — | 🗑️ Should be ARCHIVED — PR merged Jun 18 (3 days ago) |
| jn-5729-pin-uv-default-python | [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | Ingest | Backlog (unassigned) | — | — | — | ⚠️ Likely superseded by jn-5729-pin-python-313 |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit (CI likely not triggered for db script only) | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | OPEN, MERGEABLE, REVIEW_REQUIRED | 🎉 **4h+ since green** — needs reviewer assigned |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ e2e-smoke + e2e-tests FAIL (others ✅) | OPEN, MERGEABLE, REVIEW_REQUIRED | 🔴 5th consecutive e2e failure — systemic pattern |

---

## Key Changes Since Last Run (Jun 21 02:01 IDT)

| What observed | Status |
|---|---|
| **↔ Board STATIC** — 0 merges, 0 zone changes, 0 new PRs since 02:01 IDT | All 12 worktrees in same zones as before. |
| **🎉 PR #1602 (JN-5685/JN-5679) — CI ALL GREEN, 4h+ waiting** | Still OPEN, MERGEABLE, REVIEW_REQUIRED — no reviewer in ~4h since green. |
| **⚠️ PR #1607 (jn-5729-pin-python-313) — CI still not triggered** | Now 5h since creation at 23:15 IDT Jun 20. Still only CodeRabbit. |
| **🔴 PR #1601 (jn-5675)** | ↔ UNCHANGED — CI catastrophic (8 checks). Now 52h+ without fix. |
| **🔴 PR #1604 (jn-5676)** | ↔ UNCHANGED — CONFLICTING + DRAFT. pre-commit only failing. |
| **🔴 PR #1588 (jn-5546)** | ↔ UNCHANGED — pre-commit failing. MERGEABLE. |
| **🔴 PR #1606 (JN-5725, off-board)** | ↔ UNCHANGED — e2e-smoke/e2e-tests ❌. 5th run remains most recent. |

---

## Attention Items

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) CI ALL GREEN — 4h+ since green

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion (JN-5685, JN-5679)"

**CI ALL GREEN — all checks passing (confirmed 04:00 IDT):**
- ✅ pre-commit-run/pre-commit, tox-run/tox, integration-run/integration
- ✅ e2e-tests, nox, integration-tests
- ✅ atlas-validate-run/atlas-validate, atlas-validate, check-changes, JIRA Association
- State: OPEN, MERGEABLE, REVIEW_REQUIRED (0 reviews), not draft

**This PR is ready for review.** Has been CI-green since ~00:00 IDT Jun 21 (4h+ as of this run). Needs a reviewer assigned.

---

### ⚠️ FLAG — PR #1607 (jn-5729) CI not triggered after 5h

PR [#1607](https://github.com/Jounce-IO/jounce/pull/1607) — "fix(devcontainer): JN-5729 pin Python to 3.13, prevent 3.14 installation"

Created 23:15 IDT Jun 20. As of 04:00 IDT Jun 21 (5h later), `gh pr checks 1607` returns only CodeRabbit. This is unusual — full CI suite has still not been triggered.

**Possible causes:** devcontainer-only change skips all CI workflows; CI triggered but errored. **Action needed:** Joseph to check why CI didn't run on this PR — may need manual re-trigger.

---

### 🚨 HIGHEST PRIORITY — jn-5675 `__init__.py` CI catastrophic (52h+ stalled)

PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) still failing all CI checks. MERGEABLE but broken:
- `pre-commit-run / pre-commit` ❌, `tox-run / tox` ❌, `integration-run / integration` ❌
- `e2e-api / e2e` ❌, `pre-commit` ❌, `nox` ❌, `integration-tests` ❌, `e2e-tests` ❌

Root cause: broken `__init__.py` conflict resolution. 52h+ without a fix. Session needed.

---

### 🔴 OFF-BOARD — PR #1606 (JN-5725) Systemic e2e failure (5th run, unchanged)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): e2e-smoke/e2e ❌, e2e-tests ❌, all others ✅. 5th consecutive failure. Pattern confirmed: systemic e2e infra issue.

---

### 🔴 jn-5676 — CONFLICTING + DRAFT (66h+ stalled)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604): DRAFT + CONFLICTING. CI otherwise clean (only pre-commit failing). Needs rebase + pre-commit fix + un-draft.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX (67h+ stalled)

MERGEABLE + pre-commit failing + sephib MUST FIX comments. No fix activity.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatch — JN-5662 still "In Review"

[JN-5662](https://jounce.atlassian.net/browse/JN-5662) Jira status: **In Review** — but PR [#1591](https://github.com/Jounce-IO/jounce/pull/1591) merged **Jun 15** (6+ days ago). Should be Done.

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | [DEV] Historical mode notebook cells | **In Progress** | No worktree — likely covered by JN-5676 stub |
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Reduce Lychee precommit flaky results | Backlog | No worktree |
| [JN-5662](https://jounce.atlassian.net/browse/JN-5662) | Decouple libs/sql from services/validator | In Review ⚠️ | PR #1591 merged Jun 15 — should be Done |
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
