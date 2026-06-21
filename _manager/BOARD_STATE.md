# Board State — jounce-workflow-ai

*Last updated: 2026-06-21 20:32 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** (un-drafted ~17:30 IDT) | ⚠️ Only CodeRabbit ✅ — GH Actions CI **not triggered** 2.5h+ after un-draft | reviewDecision="" (CodeRabbit cleared) | 🔴 **GH Actions CI not running** — manual re-trigger needed before requesting human review |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Progress | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ pre-commit FAIL; tox/nox/integration/e2e-tests/atlas ✅ | REVIEW_REQUIRED | 🆕 **NEW** — first tracked run; draft PR with pre-commit failures (expected for WIP) |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (tox/integration/nox all ✅) — MERGEABLE | — | 🔴 Pre-commit fix needed + sephib MUST FIX comments; 87h+ stalled |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ✅ Idle, docs done |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ Only CodeRabbit | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

**Archived This Session (14:30 IDT):**
- jn-5675-historical-visibility (archived 14:30 IDT — PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) MERGED 16:15 IDT Jun 21)

**Archived Previous (14:00 IDT):**
- ci-statistics-notebook (archived 14:00 IDT — JN-5708 Done + 3+ days inactive + no PR)

**Archived Previous (12:00 IDT):**
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
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ⏳ ALL GREEN except e2e-smoke PENDING (new run triggered) | OPEN, MERGEABLE, reviewDecision="" | 🎉 **28h+ since green** — e2e-smoke re-running; needs reviewer assigned |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | ❌ **pre-commit FAIL** (changed from e2e FAIL); e2e checks now SKIPPING | OPEN, **MERGEABLE**, REVIEW_REQUIRED | 🟡 **Failure mode shifted**: was e2e-smoke+tests FAIL, now pre-commit FAIL — needs pre-commit fix |

---

## Key Changes Since Last Run (Jun 21 20:00 IDT)

| What observed | Status |
|---|---|
| **🆕 jn-5677 worktree detected** | Branch `jn-5677-dev-historical-mode-notebook-cells` in Revise zone with draft PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615). Was previously "Sprint Tickets Without Board Worktrees." Pre-commit failing (expected WIP). Jira JN-5677 In Progress ✅. |
| **🔴 PR #1604 GH Actions CI still not triggered** | 2.5h+ since un-draft — still only CodeRabbit visible. reviewDecision changed "" (CodeRabbit cleared). Manual CI re-trigger needed. |
| **⏳ PR #1602 e2e-smoke now PENDING** | New CI run was triggered (was "ALL GREEN 27h+"). All other checks green. e2e-smoke pending — positive development. |
| **↔ PR #1606 failure mode shifted** | Was "e2e-smoke + e2e-tests FAIL." Now pre-commit FAIL + e2e checks SKIPPING (likely gated behind pre-commit). New CI run. |
| **↔ PR #1588** | UNCHANGED — pre-commit failing; 87h+ stalled. |
| **↔ PR #1596** | UNCHANGED — CONFLICTING, DRAFT, frozen. |
| **↔ JN-5673** | UNCHANGED — still "In Review" (PR #1595 merged Jun 17, 4+ days stale). |

---

## Attention Items

### 🔴 PR #1604 (JN-5676) — GH Actions CI NOT Running (2.5h+ after un-draft)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

Un-drafted ~17:30 IDT. As of 20:32 IDT, GH Actions CI has **not triggered** — only CodeRabbit visible in `gh pr checks`. reviewDecision="" (CodeRabbit review cleared, 2 actionable comments remain open).

**Required action:** Manually re-trigger CI (push an empty commit or use GitHub UI), then address CodeRabbit actionable comments, confirm CI green, request a human reviewer.

---

### 🆕 PR #1615 (JN-5677) — New Draft PR, Pre-commit Failing (WIP)

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615) — "feat(jbenchmark): historical mode notebook cells (JN-5677)"

DRAFT, MERGEABLE. Pre-commit FAIL — expected for WIP. tox/nox/integration/e2e-tests/atlas all green. Depends on JN-5676 (PR #1604) merging first.

**No action needed** — WIP, draft, pre-commit failure is expected.

---

### 🎉 ACTION NEEDED — PR #1602 (JN-5685/JN-5679) — 28h+ Green, e2e-smoke Re-running

PR [#1602](https://github.com/Jounce-IO/jounce/pull/1602) — "feat(jbenchmark): add monotonicity verdict persistence tables and ingestion"

e2e-smoke now PENDING (new run). All other checks pass. OPEN, no reviewer assigned.

**Required action:** Wait for e2e-smoke to complete. If green → assign reviewer immediately.

---

### 🟡 OFF-BOARD — PR #1606 (JN-5725) — Failure Mode Shifted to Pre-commit

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): MERGEABLE. Previous failure was e2e-smoke. New CI run shows pre-commit FAIL with e2e checks SKIPPING. Pre-commit is gating everything.

**Required action:** Fix pre-commit failures, then re-run to see if e2e-smoke still fails.

---

### 🔴 PR #1588 (JN-5546) — pre-commit + sephib MUST FIX (87h+ stalled)

MERGEABLE + pre-commit failing + sephib MUST FIX comments. No fix activity.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (1 stale ticket — unchanged)

| Ticket | Jira Status | PR | Merged/State | Days Stale |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 4+ days |

JN-5674 ✅ Done (resolved prior run). JN-5673 should be Done.

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Reduce Lychee precommit flaky results | Backlog | No worktree |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache CLI flags to runner | **In Progress** | No worktree — may be older/lower priority |

*Note: JN-5677 now has worktree `jn-5677-dev-historical-mode-notebook-cells` — removed from this table.*

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
