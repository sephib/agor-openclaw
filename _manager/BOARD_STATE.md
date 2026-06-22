# Board State — jounce-workflow-ai

*Last updated: 2026-06-22 17:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ✅ **MOSTLY GREEN** (run 27959917357: pre-commit ✅, integration ✅, e2e-api ✅, tox ✅, nox ✅, integration-tests ✅, pre-commit-run ✅ — e2e-smoke ⏳ PENDING) | **APPROVED** ✅ | 🎉 **APPROVED — waiting on e2e-smoke only. Can merge when smoke passes.** |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ **pre-commit FAIL** (CI run 27934981657, created 09:52 IDT Jun 22) | REVIEW_REQUIRED | 🔴 **TRIPLE: DRAFT + CONFLICTING + pre-commit FAIL** — blocked on #1604 merging first |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | 🟡 PR checks run 27933817996 shows pre-commit FAIL (stale branch CI run); MERGEABLE | reviewDecision="" | 🟡 **Needs reviewer** — MERGEABLE; Jira should be "In Review" |
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Ingest | In Progress | — | — | — | ℹ️ **NEW** — Ingest zone; JN-5724 "In Progress"; no sessions yet |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Ingest | In Progress | — | — | — | ℹ️ **NEW** — Ingest zone; JN-5616 "In Progress"; no sessions yet |
| model-packaging-cr | — | Code Review | — | — | — | — | ⚠️ 7+ days inactive (last session Jun 15), no PR — may be stale |
| internal-cr-system | — | Code | — | — | — | — | 🔴 Filesystem FAILED (git lock) — unchanged |
| dual-heartbeat-system | — | Code | — | — | — | — | ℹ️ Idle, docs done |
| standup-drafts | — | Code | — | — | — | — | ℹ️ Utility branch, no sessions |
| jn-5695-db-connect-script | [JN-5695](https://jounce.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT | ⚠️ CONFLICTING | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://jounce.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |

**Archived This Session (14:30 IDT Jun 21):**
- jn-5675-historical-visibility (archived 14:30 IDT — PR [#1601](https://github.com/Jounce-IO/jounce/pull/1601) MERGED 16:15 IDT Jun 21)

**Archived Previous (14:00 IDT Jun 21):**
- ci-statistics-notebook (archived 14:00 IDT — JN-5708 Done + 3+ days inactive + no PR)

**Archived Previous (12:00 IDT Jun 21):**
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
| [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | auto-apply-labels | [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | — | **MERGED Jun 21** | 🎉 MERGED — off-board, no archive needed |
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | **MERGED 14:34 IDT Jun 22** | 🎉 MERGED — JN-5685 Done, JN-5679 Done |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | 🟡 **run 27958974262** (atlas-validate ✅, e2e-api ✅, check-changes ✅, CodeRabbit ✅, JIRA Association ✅, pre-commit ✅, tox ✅, integration ✅, nox ✅ — e2e-smoke ⏳ PENDING) | OPEN, **MERGEABLE**, REVIEW_REQUIRED | 🟡 **Nearly all green — only e2e-smoke pending.** JN-5725 Done in Jira. |

---

## Key Changes Since Last Run (Jun 22 17:00 IDT)

| What observed | Status |
|---|---|
| **🎉 PR #1604 reviewDecision: APPROVED** | Reviewer approved! Was "" for 10+ consecutive heartbeats. New CI run 27959917357 (all pass except e2e-smoke PENDING). Once smoke passes → can merge. |
| **🟡 PR #1606 CI run 27958974262 (supersedes 27958172294)** | New run from ~17:00 IDT. Almost all green: pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, nox ✅ — e2e-smoke still ⏳ PENDING. Getting very close. |
| **ℹ️ Two new Ingest worktrees** | jn-5724-lychee-precommit-flaky and jn-5616-replace-find-project-root appeared in Ingest zone. Both Jira tickets "In Progress". |
| **↔ PR #1615 triple problem** | Unchanged — DRAFT + CONFLICTING + pre-commit FAIL. |
| **↔ PR #1588 needs reviewer** | Unchanged — MERGEABLE, no reviewer, Jira still "In Progress". |
| **↔ Jira mismatches** | Unchanged — JN-5673 "In Review" (merged Jun 17), JN-5546 "In Progress" (should be "In Review"), JN-5725 "Done" (PR still open, CI nearly done). |

---

## Attention Items

### 🎉 PR #1604 (JN-5676) — APPROVED — waiting on e2e-smoke only

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

**reviewDecision: APPROVED** (changed this run from ""). New CI run 27959917357: all checks pass except e2e-smoke still PENDING. Once e2e-smoke passes → READY TO MERGE.

**Required action:** Monitor e2e-smoke result for run 27959917357. When smoke passes → merge.

---

### 🟡 PR #1606 (JN-5725) — Nearly all green, e2e-smoke pending

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606) — "feat(vllm-analyzer): integrate log analyzer into experiment-workflow (JN-5725)"

CI run **27958974262**: pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, nox ✅ — e2e-smoke ⏳ PENDING. MERGEABLE. REVIEW_REQUIRED. JN-5725 Done in Jira.

**Required action:** Wait for e2e-smoke. If passes → assign reviewer.

---

### 🟡 PR #1588 (JN-5546) — PR MERGEABLE, assign reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

MERGEABLE (reviewDecision=""). Assign reviewer.

**Required action:** (1) Assign a reviewer. (2) Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ PR #1615 (JN-5677) — TRIPLE: DRAFT + CONFLICTING + pre-commit FAIL

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): DRAFT, pre-commit FAIL (run 27934981657, 09:52 IDT Jun 22), CONFLICTING. Blocked on JN-5676 (#1604) merging first. Fix pre-commit and resolve conflict even while still in draft.

---

### ℹ️ Two new Ingest worktrees

**jn-5724-lychee-precommit-flaky** ([JN-5724](https://jounce.atlassian.net/browse/JN-5724)) and **jn-5616-replace-find-project-root** ([JN-5616](https://jounce.atlassian.net/browse/JN-5616)) appeared in Ingest zone this run. Both Jira tickets "In Progress". No sessions yet.

---

### ⚠️ model-packaging-cr — POTENTIALLY STALE

Branch in Code Review zone for `Jounce-IO/model-packaging-pipeline`. No PR linked. Last session Jun 15 (7+ days ago). Code review findings were written but no follow-up action visible.

**Required action:** Confirm with Joseph whether this review is still needed or can be archived.

---

### 🔴 FILESYSTEM FAILED — internal-cr-system

Git lock error — unchanged since Jun 18.

---

### ⚠️ Jira mismatches (3 items)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 5+ days stale — should be Done |
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, MERGEABLE | Should be "In Review" (open PR) |
| [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | **Done** | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, CI nearly done | Ticket Done but PR still open — wait for CI result |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://jounce.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5678](https://jounce.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | Backlog | No worktree |
| [JN-5728](https://jounce.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | Backlog | No worktree |
| [JN-5539](https://jounce.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5244](https://jounce.atlassian.net/browse/JN-5244) | Add --user, --no-cache CLI flags to runner | **In Progress** | No worktree — may be older/lower priority |

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
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
