# Board State — jounce-workflow-ai

*Last updated: 2026-06-21 11:33 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5675-historical-visibility | [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | Code | In Review | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | ✅ **ALL GREEN** | — | 🔴 Now **CONFLICTING** (was MERGEABLE at 11:02 IDT) — needs rebase before Code Review zone move |
| jn-5729-pin-uv-default-python-2 | [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | Publish | Backlog | [#1608](https://github.com/Jounce-IO/jounce/pull/1608) **MERGED** | — | — | 🎉 PR MERGED 09:37 IDT — propose archive |
| jn-5729-pin-python-313 | [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | Code | Backlog | [#1607](https://github.com/Jounce-IO/jounce/pull/1607) **CLOSED** | — | — | 🗑️ PR CLOSED 08:03 IDT (superseded by #1608) — propose archive |
| jn-5729-pin-uv-default-python | [JN-5729](https://jounce.atlassian.net/browse/JN-5729) | Ingest | Backlog | — | — | — | 🗑️ JN-5729 done via #1608 — no PR — propose archive |
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ❌ pre-commit FAIL only (tox/nox/integration/e2e all ✅) + **CONFLICTING** | REVIEW_REQUIRED | 🔴 CONFLICTING; needs rebase + pre-commit fix to un-draft; 73h+ stalled |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | — | 🔴 Pre-commit fix needed + sephib MUST FIX comments; 74h+ stalled |
| ci-statistics-notebook | [JN-5708](https://jounce.atlassian.net/browse/JN-5708) (issue link) | Code | Done | — | — | — | ⚠️ No sessions; JN-5708 Done; scope unclear |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| code-reviewes | — | Code Review | — | — | — | — | 🗑️ Should be ARCHIVED — review done Jun 15 |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |

**Archived Since Last Run:**
- jn-5673-visibility-scaffold (archived Jun 21 04:57 IDT)
- jn-5674-operational-visibility (archived Jun 21 04:57 IDT, PR #1599 MERGED Jun 18)

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | auto-apply-labels | [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | — | **MERGED 10:50 IDT** | 🎉 MERGED — off-board, no archive needed |
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | OPEN, MERGEABLE, reviewDecision="" | 🎉 **12.5h+ since green** — needs reviewer assigned |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ e2e-smoke + e2e-tests FAIL (others ✅) | OPEN, **CONFLICTING**, REVIEW_REQUIRED | 🔴 CONFLICTING + systemic e2e failures — unchanged |

---

## Key Changes Since Last Run (Jun 21 11:02 IDT)

| What observed | Status |
|---|---|
| **🔴 PR #1601 (JN-5675) now CONFLICTING** | Was MERGEABLE + ALL GREEN at 11:02 IDT. CI still ALL GREEN (latest run). Likely caused by a main branch merge that conflicted after 11:02 IDT. Needs rebase before review. |
| **↔ PR #1602** | UNCHANGED — ALL GREEN now 12.5h+, OPEN, MERGEABLE, reviewDecision="" |
| **↔ PR #1604** | UNCHANGED — DRAFT + CONFLICTING + pre-commit fail; 73h+ stalled |
| **↔ PR #1588** | UNCHANGED — pre-commit failing; 74h+ stalled |
| **↔ PR #1606** | UNCHANGED — CONFLICTING + e2e fail |
| **No new merges** | Since 11:02 IDT — board otherwise static |

---

## Attention Items

### 🔴 NEW — PR #1601 (JN-5675) Now CONFLICTING

PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) — "feat(jbenchmark): JN-5675 historical visibility functions"

**State change since last heartbeat:** Was MERGEABLE + ALL GREEN at 11:02 IDT → now **CONFLICTING**. CI is still ALL GREEN on the current branch HEAD (all checks pass). The conflict was likely triggered by a post-11:02 IDT merge to main.

**Required action:** Rebase jn-5675-historical-visibility onto main to resolve conflicts, then push. Once MERGEABLE again, move to Code Review zone.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) CI ALL GREEN — 12.5h+ since green

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion (JN-5685, JN-5679)"

**CI ALL GREEN** — confirmed 11:33 IDT. All checks passing.
- State: OPEN, MERGEABLE, reviewDecision="" (was REVIEW_REQUIRED)
- Reviews: OmerMarcovich left a COMMENT at 04:26 IDT (not an approval)
- 12.5h+ since CI went green (00:00 IDT Jun 21). No reviewer assigned.

---

### 🆕 JN-5729 COMPLETE — 3 Worktrees to Archive

PR [#1608](https://github.com/Jounce-IO/jounce/pull/1608) merged 09:37 IDT — "fix(devcontainer): pin uv default Python to 3.13 (JN-5729)". Three worktrees now need archiving:

1. `jn-5729-pin-uv-default-python-2` (Publish zone) — PR #1608 merged ✅
2. `jn-5729-pin-python-313` (Code zone) — PR #1607 closed (superseded)
3. `jn-5729-pin-uv-default-python` (Ingest zone) — no PR, JN-5729 work complete

Also: JN-5729 Jira is still Backlog (unassigned) — should be updated to Done.

---

### 🔴 jn-5676 — CONFLICTING + DRAFT (73h+ stalled)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604): DRAFT + CONFLICTING. CI otherwise clean (only pre-commit failing). Needs rebase + pre-commit fix + un-draft. 73h+ stalled.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX (74h+ stalled)

MERGEABLE + pre-commit failing + sephib MUST FIX comments. No fix activity.

---

### 🔴 OFF-BOARD — PR #1606 (JN-5725) Systemic e2e failure + CONFLICTING

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): e2e-smoke ❌, e2e-tests ❌ (systemic). Also CONFLICTING. Both issues need attention before merge.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatch — JN-5662 still "In Review"

[JN-5662](https://jounce.atlassian.net/browse/JN-5662) Jira status: **In Review** — but PR [#1591](https://github.com/Jounce-IO/jounce/pull/1591) merged **Jun 15** (6+ days ago). Should be Done.

---

### ⚠️ Jira mismatch — JN-5729 still Backlog

[JN-5729](https://jounce.atlassian.net/browse/JN-5729) Jira status: **Backlog (unassigned)** — but PR [#1608](https://github.com/Jounce-IO/jounce/pull/1608) merged Jun 21 09:37 IDT. Should be updated to Done.

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
