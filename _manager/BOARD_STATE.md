# Board State — jounce-workflow-ai

*Last updated: 2026-06-23 04:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5676-notebook-scaffold | [JN-5676](https://jounce.atlassian.net/browse/JN-5676) | Publish | In Review | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) **OPEN** | ✅ **ALL GREEN** (run 27959917357: ALL checks pass) | **APPROVED** ✅ | 🎉🎉 **READY TO MERGE — ALL CI GREEN + APPROVED. 17th flag. Merge now!** |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://jounce.atlassian.net/browse/JN-5677) | Revise | In Review | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **DRAFT** OPEN | ❌ **CONFLICTING** | REVIEW_REQUIRED | 🔴 **DRAFT + CONFLICTING** — blocked on #1604 merging first |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ **pre-commit FAIL** (run 27933817996) | reviewDecision="" | 🔴 **CI FAILING** — pre-commit FAIL; Jira should be "In Review" |
| jn-5724-lychee-precommit-flaky | [JN-5724](https://jounce.atlassian.net/browse/JN-5724) | Ingest | In Progress | — | — | — | 🔴 **filesystem FAILED** (git lock — same error as internal-cr-system) |
| jn-5616-replace-find-project-root | [JN-5616](https://jounce.atlassian.net/browse/JN-5616) | Ingest | In Progress | — | — | — | ℹ️ Ingest zone; ready; no sessions yet |
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
- model-packaging-cr (removed from tracking — not on this board; confirmed absent from board scan)

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | auto-apply-labels | [JN-5730](https://jounce.atlassian.net/browse/JN-5730) | — | **MERGED Jun 21** | 🎉 MERGED — off-board, no archive needed |
| [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | persist-monotonicity-test | JN-5685/JN-5679 | ✅ ALL GREEN | **MERGED 14:34 IDT Jun 22** | 🎉 MERGED — JN-5685 Done, JN-5679 Done |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://jounce.atlassian.net/browse/JN-5725) | 🔴 **CI RUN 27980646274 — e2e-smoke FAILED** (52m58s) + **e2e-tests FAILED** (all other checks ✅: e2e-api ✅ integration ✅ tox ✅ pre-commit ✅ nox ✅ atlas-validate ✅) | OPEN, **MERGEABLE**, REVIEW_REQUIRED | 🔴 **e2e-smoke FAILED + e2e-tests FAILED** — unchanged since 02:00 IDT. Needs e2e investigation. Jira Done. |

---

## Key Changes Since Last Run (Jun 23 02:00 IDT)

| What observed | Status |
|---|---|
| **↔ PR #1604 still OPEN (17th flag)** | ALL CI GREEN + APPROVED + MERGEABLE — still not merged. |
| **↔ PR #1606 — e2e-smoke FAILED + e2e-tests FAILED** | Unchanged since 02:00 IDT. Run 27980646274 still the latest. No new commits or CI runs overnight. |
| **↔ PR #1588 pre-commit FAIL** | Still failing (run 27933817996). Unchanged. |
| **↔ PR #1615 DRAFT + CONFLICTING** | Blocked on #1604. Unchanged. |
| **↔ jn-5724 + internal-cr-system** | Git lock errors — unchanged. |
| **↔ Jira stale** | JN-5673 still In Review (PR #1595 merged Jun 17, 7+ days stale). |

---

## Attention Items

### 🎉🎉 PR #1604 (JN-5676) — ALL GREEN — READY TO MERGE NOW (17th flag)

PR [#1604](https://github.com/Jounce-IO/jounce/pull/1604) — "feat(jbenchmark): notebook scaffold + operational mode (JN-5676)"

**ALL CI CHECKS PASSED** (run 27959917357): pre-commit ✅, integration ✅, e2e-api ✅, tox ✅, nox ✅, integration-tests ✅, e2e-smoke ✅, e2e-tests ✅, atlas-validate ✅. APPROVED. MERGEABLE.

**Required action: MERGE THIS PR.** Everything is green. No blockers. This is the 17th consecutive flag.

---

### 🔴 PR #1606 (JN-5725) — e2e-smoke FAILED + e2e-tests FAILED

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606) — "feat(vllm-analyzer): integrate log analyzer into experiment-workflow (JN-5725)"

**CI RUN 27980646274** — e2e-smoke **FAILED** (52m58s) + e2e-tests **FAILED**. All other checks pass: e2e-api ✅, integration ✅, tox ✅, pre-commit ✅, nox ✅, integration-tests ✅, atlas-validate ✅. MERGEABLE, REVIEW_REQUIRED. Jira is Done.

No new commits overnight. Failure is unchanged from 02:00 IDT.

**Action: Investigate e2e-smoke failure.** Fix the e2e test or infrastructure issue, then push fix to trigger new CI run. Once CI passes → needs reviewer.

---

### 🔴 jn-5724-lychee-precommit-flaky — filesystem FAILED (git lock)

Branch `jn-5724-lychee-precommit-flaky` shows `filesystem_status: failed` with git lock error. Same error as `internal-cr-system`.

**Required action:** Fix the git lock issue — `rm /Users/josephberry/.agor/worktrees/Jounce-IO/jounce/.git/config.lock` or equivalent.

---

### ⚠️ PR #1615 (JN-5677) — DRAFT + CONFLICTING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): DRAFT, CONFLICTING. Blocked on JN-5676 (#1604) merging first. Resolve conflict after #1604 merges.

---

### 🔴 PR #1588 (JN-5546) — pre-commit FAIL + needs reviewer

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) — "docs(jbenchmark): add CONTRIBUTING.md and service READMEs (JN-5546)"

MERGEABLE (no conflicts, reviewDecision="") but **pre-commit CI FAILING** (run 27933817996).

**Required action:** (1) Fix pre-commit failure in PR #1588. (2) Assign a reviewer. (3) Update Jira [JN-5546](https://jounce.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### 🔴 FILESYSTEM FAILED — internal-cr-system + jn-5724-lychee-precommit-flaky

Two worktrees have git lock errors. The underlying `.git/config.lock` file likely persists in the worktree shared git dir.

---

### ⚠️ Jira mismatches (2 items)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5673](https://jounce.atlassian.net/browse/JN-5673) | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Merged Jun 17 | 7+ days stale — should be Done |
| [JN-5546](https://jounce.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, pre-commit FAIL | Should be "In Review" AND needs pre-commit fix |

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
