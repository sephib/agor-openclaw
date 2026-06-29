# Board State — jounce-workflow-ai

*Last updated: 2026-06-29 17:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) OPEN CONFLICTING (mergeable=UNKNOWN) | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996, stale) | reviewDecision="" | 🔴 **STALE** — unchanged since Jun 17. Pre-commit FAIL, CONFLICTING. Jira should be "In Review". |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT OPEN CONFLICTING | — | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jira-operations | — | (no zone) | — | — | — | — | ⚠️ session timed_out 07:38 IDT Jun 25. No PR, no Jira, no zone. Needs decision. |
| jn-5244-cli-flags | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | **Ingest** | In Progress | — | — | — | ℹ️ Created 14:49 IDT Jun 28. No sessions yet. JN-5244: Add --user, --no-cache, --skip-estimator CLI flags. Ready to ingest. |
| jn-5780-add-jn-project | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | **Plan** | Unknown | — (GitLab "create MR" link, no actual PR) | — | — | ℹ️ Different repo: redhat/jira-autofix. Not found in jounce Plan zone scan. Needs Joseph review. |
| jn-5793-jsonb-path-fix | [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | **Code** | Backlog | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) OPEN MERGEABLE | ⚠️ **1 FAIL** (JIRA Association only, run 28376204013) — all others ✅ (integration ✅, pre-commit ✅, e2e-smoke ✅ 11m34s, e2e-tests ✅, nox ✅, tox ✅, e2e-api ✅) | REVIEW_REQUIRED | 🟡 **CI IMPROVED** — was 5 failures (run 28375434698), now 1 (JIRA Association only, run 28376204013). Likely instance migration issue (jounce.atlassian.net → redhat.atlassian.net). Nearly ready — needs: (1) fix JIRA Association check, (2) assign reviewer. |
| jn-5794-required-checks | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | **Ingest** | Backlog | — | — | — | ℹ️ **NEW** — detected 16:30 IDT Jun 29. No sessions yet. JN-5794: [BUG] Auto-merge bypasses integration test failures. |

**Untracked worktrees on board:**
- `model-packaging-cr` (Code Review zone, model-packaging-pipeline repo, no PR, no sessions, last used Jun 15) — still on board. No PR to check; needs manual decision.

**Archived This Session (15:33 IDT Jun 29):**
- jn-5677-dev-historical-mode-notebook-cells (archived — PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615) MERGED 15:08 IDT Jun 29) ✅

**Archived Previous (14:00 IDT Jun 29):**
- jn-5616-replace-find-project-root (archived — PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623) MERGED 13:45 IDT Jun 29) ✅

**Archived Previous (11:00 IDT Jun 29):**
- jn-5612-fix-github-sha (archived — PR [#1627](https://github.com/Jounce-IO/jounce/pull/1627) MERGED 10:42 IDT Jun 29) ✅

**Archived Previous (10:30 IDT Jun 29):**
- jn-5724-lychee-precommit-flaky (archived — PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622) MERGED 10:17 IDT Jun 29) ✅

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

**Removed from tracking (confirmed archived on board):**
- dual-heartbeat-system — confirmed archived in board scan Jun 23
- standup-drafts — confirmed archived in board scan Jun 23
- fix-dashboard-syntax-error — no longer visible in any zone scan; presumed archived

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | run 28366983945 **COMPLETE**: e2e-api ✅ (4m1s), e2e-gpu-live ✅ (10m22s), integration ✅, integration-tests ✅, nox ✅, pre-commit ✅, tox ✅ — **e2e-smoke ❌ (5m28s), e2e-tests ❌ (3s) FAIL** | 🔴 **CONFLICTING** (unchanged) | 🔴 **CONFLICTING** — due to #1615 merge to main. CI still shows e2e-smoke ❌ + e2e-tests ❌ (3+ runs, run unchanged). Owner must rebase + diagnose e2e-smoke + e2e-tests root cause. |

---

## Key Changes Since Last Run (16:30 IDT Jun 29)

| What observed | Status |
|---|---|
| **PR #1639 CI IMPROVED** | New run `28376204013`: only JIRA Association ❌ — all others ✅ (down from 5 failures). Nearly mergeable. |
| **PR #1606 unchanged** | Still CONFLICTING + e2e-smoke ❌ (5m28s) + e2e-tests ❌ (3s) — same run 28366983945. |
| **PR #1588 unchanged** | Still CONFLICTING + pre-commit ❌ — same stale run 27933817996. |
| **Jira mismatches unchanged** | JN-5616 "In Review", JN-5612 "In Progress", JN-5724 "In Review" — 3 still stale. |

---

## Attention Items

### 🟡 PR #1639 (JN-5793, Code zone) — CI IMPROVED (1 failure remaining)

PR [#1639](https://github.com/Jounce-IO/jounce/pull/1639): `fix(tests): JN-5793 update plan_json fixtures to match production JSONB structure`
- Detected 16:30 IDT Jun 29. JN-5793: Backlog, assigned to Joseph Berry.
- **Previous run** (28375434698): 5 failures — JIRA Association ❌, integration ❌, integration-tests ❌, pre-commit ❌, pre-commit-run ❌
- **Current run** (28376204013): **1 failure only** — JIRA Association ❌; all others ✅ (e2e-smoke ✅ 11m34s, e2e-tests ✅, integration ✅ 3m20s, integration-tests ✅, pre-commit ✅ 4m52s, e2e-api ✅, nox ✅, tox ✅)
- JIRA Association failure likely due to instance migration (jounce.atlassian.net → redhat.atlassian.net)
- **Action needed:** (1) Fix or suppress JIRA Association check (migration-related). (2) Assign reviewer — nearly ready to merge.

---

### ℹ️ jn-5794-required-checks (Ingest) — NEW worktree

JN-5794: [BUG] Auto-merge bypasses integration test failures — integration-run not a required check. Backlog, assigned to Joseph Berry.
- No sessions, no PR yet. Ready to start.

---

### 🎉 PR #1615 (JN-5677, Respond) — MERGED at 15:08 IDT Jun 29 ✅

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)` — **MERGED**
- Final CI: e2e-smoke ✅ (11m13s), e2e-tests ✅ (3s) passed; integration ❌ + integration-tests ❌ still failing
- Merged via admin merge despite 2 CI failures
- Worktree `jn-5677-dev-historical-mode-notebook-cells` **ARCHIVED** (autonomous action, 15:33 IDT)
- Jira [JN-5677](https://redhat.atlassian.net/browse/JN-5677): **Done** ✅ — Jira correct, no action needed.

---

### 🔴 PR #1606 (JN-5725, off-board) — CONFLICTING + e2e-smoke + e2e-tests FAIL

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- 🔴 **CONFLICTING** (since #1615 merged to main)
- CI run 28366983945 **COMPLETE** (no new run): e2e-api ✅, e2e-gpu-live ✅, integration ✅, integration-tests ✅ — **e2e-smoke ❌ (5m28s), e2e-tests ❌ (3s) FAIL**
- Pattern: e2e-smoke + e2e-tests fail across 3+ CI runs
- Jira [JN-5725](https://redhat.atlassian.net/browse/JN-5725): Done (Unassigned) ✅
- **Action needed:** (1) Rebase on main (CONFLICTING). (2) Diagnose root cause of persistent e2e-smoke + e2e-tests failures.

---

### 🎉 PR #1623 (JN-5616) — MERGED at 13:45 IDT Jun 29 ✅

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)` — **MERGED**
- Worktree `jn-5616-replace-find-project-root` **ARCHIVED** (autonomous action, 14:00 IDT)
- Jira [JN-5616](https://redhat.atlassian.net/browse/JN-5616): still **"In Review"** ⚠️ — **should be "Done"**
- **Action needed:** Update Jira JN-5616 → "Done".

---

### 🎉 PR #1627 (JN-5612, Publish) — MERGED at 10:42 IDT Jun 29 ✅

PR [#1627](https://github.com/Jounce-IO/jounce/pull/1627): `fix(ci): JN-5612 replace github.GITHUB_SHA with github.sha in workflow run-names` — **MERGED**
- Worktree `jn-5612-fix-github-sha` **ARCHIVED** (autonomous action, 11:00 IDT)
- Jira [JN-5612](https://redhat.atlassian.net/browse/JN-5612): still **"In Progress"** ⚠️ — **should be "Done"**
- **Action needed:** Update Jira JN-5612 → "Done".

---

### 🎉 PR #1622 (JN-5724) — MERGED at 10:17 IDT Jun 29 ✅

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)` — **MERGED**
- Worktree `jn-5724-lychee-precommit-flaky` **ARCHIVED** (10:30 IDT autonomous)
- Jira [JN-5724](https://redhat.atlassian.net/browse/JN-5724): still **"In Review"** ⚠️ — **should be "Done"**
- **Action needed:** Update Jira JN-5724 → "Done".

---

### ℹ️ jn-5780-add-jn-project (Plan zone) — needs clarification

Appeared in board scan (Plan zone). Created 08:32 IDT Jun 28. Different repo: redhat/jira-autofix.
- JN-5780: On redhat.atlassian.net
- PR URL: GitLab "create new MR" placeholder — no actual PR exists
- No sessions started; not found in jounce Plan zone scan (different repo)
- **Action needed:** Joseph to clarify — is this intentional? Should it be tracked/moved/archived?

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + CONFLICTING (stale)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (run 27933817996). PR is CONFLICTING. Stale since Jun 17.

**Required action:** (1) Fix pre-commit failures. (2) Resolve merge conflict. (3) Assign reviewer. (4) Update [JN-5546](https://redhat.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ Jira mismatches (3 items)

- **JN-5616**: still "In Review" — PR #1623 **MERGED** Jun 29 13:45 IDT → update to **"Done"**
- **JN-5612**: still "In Progress" — PR #1627 **MERGED** Jun 29 10:42 IDT → update to **"Done"**
- **JN-5724**: still "In Review" — PR #1622 **MERGED** Jun 29 10:17 IDT → update to **"Done"**

---

### ⚠️ jira-operations — session timed_out, no zone

Branch `jira-operations` — No PR, no Jira ticket, no zone assigned.
- Session timed_out at 07:38 IDT (Jun 25). Title: "Create Q4 Planning Epic + Stories"
- **Action needed:** Joseph to decide: archive (if one-off task) or assign zone + create tickets

---

### ⚠️ internal-cr-system — no PR, no Jira, stagnant

Branch `internal-cr-system` in Code zone — no PR, no Jira ticket. Stagnant since Jun 18. filesystem_status: failed (git lock on .git/config).

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://redhat.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5539](https://redhat.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Refactor run_jbenchmark script to support redesign flow | **Waiting/Blocked** | No worktree — parent of JN-5244 |
| [JN-5678](https://redhat.atlassian.net/browse/JN-5678) | Dashboard README and setup instructions | **Backlog** | No worktree |
| [JN-5728](https://redhat.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | **Backlog** | No worktree |

*(JN-5244 removed — worktree jn-5244-cli-flags exists on board, Ingest zone)*
*(JN-5793 removed — worktree jn-5793-jsonb-path-fix exists on board, Code zone)*
*(JN-5794 removed — worktree jn-5794-required-checks exists on board, Ingest zone)*
*(JN-5677 removed — PR #1615 MERGED, worktree archived 15:33 IDT Jun 29)*
*(JN-5612 removed — PR #1627 MERGED, worktree archived 11:00 IDT Jun 29)*
*(JN-5616 removed — PR #1623 MERGED, worktree archived 14:00 IDT Jun 29)*

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
| [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | Jun 29 15:08 IDT ✅ — worktree archived (admin merge, integration ❌) |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | Jun 29 13:45 IDT ✅ — worktree archived |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | Jun 29 10:42 IDT ✅ — worktree archived |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | Jun 29 10:17 IDT ✅ — worktree archived |
| JN-5762 | [#1624](https://github.com/Jounce-IO/jounce/pull/1624) | Jun 24 14:05 IDT ✅ |
| JN-5759 | [#1619](https://github.com/Jounce-IO/jounce/pull/1619) | Jun 23 12:30 IDT ✅ (off-board, by another contributor) |
| [JN-5676](https://redhat.atlassian.net/browse/JN-5676) | [#1604](https://github.com/Jounce-IO/jounce/pull/1604) | Jun 23 10:51 IDT ✅ |
| [JN-5685](https://redhat.atlassian.net/browse/JN-5685)/[JN-5679](https://redhat.atlassian.net/browse/JN-5679) | [#1602](https://github.com/Jounce-IO/jounce/pull/1602) | Jun 22 14:34 IDT ✅ |
| [JN-5675](https://redhat.atlassian.net/browse/JN-5675) | [#1601](https://github.com/Jounce-IO/jounce/pull/1601) | Jun 21 16:15 IDT ✅ |
| [JN-5730](https://redhat.atlassian.net/browse/JN-5730) | [#1605](https://github.com/Jounce-IO/jounce/pull/1605) | Jun 21 10:50 IDT ✅ |
| [JN-5729](https://redhat.atlassian.net/browse/JN-5729) | [#1608](https://github.com/Jounce-IO/jounce/pull/1608) | Jun 21 09:37 IDT ✅ |
| [JN-5674](https://redhat.atlassian.net/browse/JN-5674) | [#1599](https://github.com/Jounce-IO/jounce/pull/1599) | Jun 18 23:55 IDT ✅ |
| JN-5619 | [#1598](https://github.com/Jounce-IO/jounce/pull/1598) | Jun 18 13:33 UTC ✅ |
| [JN-5708](https://redhat.atlassian.net/browse/JN-5708) | [#1603](https://github.com/Jounce-IO/jounce/pull/1603) | Jun 18 12:42 UTC ✅ |
| [JN-5673](https://redhat.atlassian.net/browse/JN-5673) | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Jun 17 ✅ |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
