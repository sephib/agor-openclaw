# Board State — jounce-workflow-ai

*Last updated: 2026-06-21 14:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Progress | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) DRAFT | ✅ **ALL GREEN** | REVIEW_REQUIRED | 🟡 Still DRAFT. Ready to un-draft + request review. 80h+ stalled. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | — | 🔴 Pre-commit fix needed + sephib MUST FIX comments; 77h+ stalled |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |

**Archived This Run (14:30 IDT):**
- jn-5675-historical-visibility (archived 14:30 IDT — PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) MERGED 16:15 IDT Jun 21)

**Archived Previous Run (14:00 IDT):**
- ci-statistics-notebook (archived 14:00 IDT — JN-5708 Done + 3+ days inactive + no PR)

**Archived Previous Run (12:00 IDT):**
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
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | OPEN, MERGEABLE UNKNOWN, reviewDecision="" | 🎉 **20h+ since green** — needs reviewer assigned |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ⏳ CI PENDING (new run in progress) | OPEN, **CONFLICTING**, REVIEW_REQUIRED | 🟡 CONFLICTING still; CI re-running (prev e2e-smoke/tests were failing) |

---

## Key Changes Since Last Run (Jun 21 14:00 IDT)

| What observed | Status |
|---|---|
| **🎉 PR #1601 MERGED** | Merged at 16:15 IDT — jn-5675-historical-visibility **archived** (autonomous). |
| **✅ JN-5675 already Done** | Jira ticket was already updated to Done — no mismatch. |
| **↔ PR #1604** | UNCHANGED — DRAFT, ALL CI GREEN, MERGEABLE, 80h+ stalled. |
| **↔ PR #1602** | UNCHANGED — ALL GREEN 20h+, OPEN, no reviewer yet. |
| **↔ PR #1588** | UNCHANGED — pre-commit failing; 77h+ stalled. |
| **🟡 PR #1606 CI** | New CI run PENDING (previously e2e-smoke/tests failing). Still CONFLICTING. |
| **↔ Jira mismatches** | JN-5662 (6+ days stale), JN-5673 (4+ days stale), JN-5674 (3+ days stale) — all still "In Review" despite PRs merged. |

---

## Attention Items

### 🟡 PR #1604 (JN-5676) ALL CI GREEN — Still DRAFT (80h+ stalled)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

**Required action:** Un-draft the PR and request a review. All blockers resolved. 80h+ stalled.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) CI ALL GREEN — 20h+

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

**CI ALL GREEN** — 20h+ since green. OPEN, no reviewer assigned.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX (77h+ stalled)

MERGEABLE + pre-commit failing + sephib MUST FIX comments. No fix activity.

---

### 🟡 OFF-BOARD — PR #1606 (JN-5725) CI Re-running + CONFLICTING

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): CI re-running (new run PENDING). Still CONFLICTING. Both need resolution before merge.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (3 stale tickets)

| Ticket | Jira Status | PR | Merged/State | Days Stale |
|--------|-------------|-----|--------|-----------|
| [JN-5662](https://jounce.atlassian.net/browse/JN-5662) | In Review | [#1591](https://github.com/Jounce-IO/jounce/pull/1591) | Merged Jun 15 | 6+ days |
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 4+ days |
| [JN-5674](https://jounce.atlassian.net/browse/JN-5674) | In Review | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) | Merged Jun 18 | 3+ days |

JN-5662/5673/5674 should all be Done.

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
