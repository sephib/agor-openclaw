# Board State — jounce-workflow-ai

*Last updated: 2026-06-21 12:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5675-historical-visibility | [JN-5675](https://jounce.atlassian.net/browse/JN-5675) | Code | In Review | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | ✅ **ALL GREEN** | — | 🔴 **CONFLICTING** (since ~11:10 IDT) — needs rebase before Code Review zone move |
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ✅ **ALL GREEN** (was pre-commit FAIL + CONFLICTING!) | REVIEW_REQUIRED | 🟡 **IMPROVED**: conflict resolved + CI all green. Still DRAFT. Ready to un-draft + request review. 75h+ stalled. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | — | 🔴 Pre-commit fix needed + sephib MUST FIX comments; 75h+ stalled |
| ci-statistics-notebook | [JN-5708](https://jounce.atlassian.net/browse/JN-5708) (issue link) | Code | Done | — | — | — | ⚠️ No sessions; JN-5708 Done; scope unclear |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |

**Archived This Run (12:00 IDT):**
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
| [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | auto-apply-labels | [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | — | **MERGED 10:50 IDT** | 🎉 MERGED — off-board, no archive needed |
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | OPEN, MERGEABLE, reviewDecision="" | 🎉 **13h+ since green** — needs reviewer assigned |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ e2e-smoke + e2e-tests FAIL (others ✅) | OPEN, **CONFLICTING**, REVIEW_REQUIRED | 🔴 CONFLICTING + systemic e2e failures — unchanged |

---

## Key Changes Since Last Run (Jun 21 11:33 IDT)

| What observed | Status |
|---|---|
| **🎉 PR #1604 (JN-5676) NOW ALL CI GREEN + MERGEABLE** | Was CONFLICTING + pre-commit FAIL at 11:33 IDT. Now: MERGEABLE, pre-commit ✅, tox ✅, nox ✅, integration ✅, e2e-tests ✅. Still DRAFT + REVIEW_REQUIRED. Ready to un-draft. |
| **✅ JN-5729 Jira now Done** | Was flagged as stale Backlog; resolved between runs (PR #1608 merged 09:37 IDT) |
| **🗑️ 4 worktrees archived (autonomous)** | jn-5729-pin-uv-default-python-2 (PR #1608 MERGED), jn-5729-pin-python-313 (PR #1607 CLOSED), jn-5729-pin-uv-default-python (JN-5729 done), code-reviewes (6+ days inactive) |
| **↔ PR #1601** | UNCHANGED — still CONFLICTING, CI ALL GREEN |
| **↔ PR #1602** | UNCHANGED — ALL GREEN now 13h+, OPEN, MERGEABLE, reviewDecision="" |
| **↔ PR #1588** | UNCHANGED — pre-commit failing; 75h+ stalled |
| **↔ PR #1606** | UNCHANGED — CONFLICTING + e2e fail |

---

## Attention Items

### 🟡 IMPROVED — PR #1604 (JN-5676) NOW ALL CI GREEN + MERGEABLE

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

**State change since last heartbeat:** Was CONFLICTING + pre-commit FAIL → now **MERGEABLE + ALL CI GREEN** (pre-commit ✅, tox ✅, nox ✅, integration ✅, e2e-tests ✅). Still DRAFT + REVIEW_REQUIRED.

**Required action:** Un-draft the PR and request a review. The blockers (conflict + pre-commit) are resolved. 75h+ stalled — this is actionable now.

---

### 🔴 ONGOING — PR #1601 (JN-5675) CONFLICTING

PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) — "feat(jbenchmark): JN-5675 historical visibility functions"

**State:** OPEN, CONFLICTING, CI ALL GREEN. Conflict caused by post-11:02 IDT merge to main. Needs rebase.

**Required action:** Rebase jn-5675-historical-visibility onto main, push. Once MERGEABLE, move to Code Review zone.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) CI ALL GREEN — 13h+

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

**CI ALL GREEN** — 13h+ since green. OPEN, MERGEABLE, reviewDecision="". No reviewer assigned.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX (75h+ stalled)

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
