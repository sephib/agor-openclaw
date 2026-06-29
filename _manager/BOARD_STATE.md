# Board State — jounce-workflow-ai

*Last updated: 2026-06-29 14:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | Respond | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** ✅ **MERGEABLE** | 🔴 **CI FAILING** (run 28366765871 — e2e-api ❌ 3m23s, e2e-tests ❌ 3s, integration ❌ 2m56s, integration-tests ❌ 2s; pre-commit ✅, tox ✅, nox ✅, check-changes ✅) | ✅ **APPROVED** | 🔴 **CI FAILING despite APPROVED+MERGEABLE** — new run triggered after rebase; 4 checks fail. Fix CI before merge! |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) OPEN CONFLICTING (mergeable=UNKNOWN) | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996, stale) | reviewDecision="" | 🔴 **STALE** — unchanged since Jun 17. Pre-commit FAIL, CONFLICTING. Jira should be "In Review". |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT OPEN CONFLICTING | — | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jira-operations | — | (no zone) | — | — | — | — | ⚠️ session timed_out 07:38 IDT Jun 25. No PR, no Jira, no zone. Needs decision. |
| jn-5244-cli-flags | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | **Ingest** | In Progress | — | — | — | ℹ️ Created 14:49 IDT Jun 28. No sessions yet. JN-5244: Add --user, --no-cache, --skip-estimator CLI flags. Ready to ingest. |
| jn-5780-add-jn-project | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | **Plan** | Unknown | — (GitLab "create MR" link, no actual PR) | — | — | ℹ️ Different repo: redhat/jira-autofix. Not found in jounce Plan zone scan. Needs Joseph review. |

**Untracked worktrees on board:**
- `model-packaging-cr` (Code Review zone, model-packaging-pipeline repo, no PR, no sessions, last used Jun 15) — still on board. No PR to check; needs manual decision.

**Archived This Session (14:00 IDT Jun 29):**
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
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | run 28366983945 **IN PROGRESS**: atlas-validate ✅, check-changes ✅, integration ✅, integration-tests ✅, nox ✅, tox-run ✅ — **e2e-api ⏳, e2e-gpu-live ⏳, pre-commit-run ⏳ PENDING** (new run after prior e2e-smoke ❌ + e2e-tests ❌ failures) | OPEN, MERGEABLE | 🟡 New CI run in progress (28366983945) — watchin e2e-api + e2e-gpu-live + pre-commit-run. Previous run had e2e-smoke + e2e-tests failing. |

---

## Key Changes Since Last Run (13:00 IDT Jun 29)

| What observed | Status |
|---|---|
| **PR #1623 (JN-5616) MERGED** ✅ | Merged at 13:45 IDT — detected via Step 3. `jn-5616-replace-find-project-root` archived (autonomous action, 14:00 IDT). |
| **PR #1615 MAJOR CHANGE** | Was: OPEN CONFLICTING, CI blank. Now: OPEN MERGEABLE APPROVED + CI FAILING (e2e-api ❌, e2e-tests ❌, integration ❌, integration-tests ❌ — run 28366765871). Rebase resolved conflict but uncovered failures. |
| **PR #1606: new CI run 28366983945** | New run after prior e2e-smoke/e2e-tests failures. Currently IN PROGRESS — e2e-api/gpu-live/pre-commit-run pending. |
| **JN-5616 Jira mismatch** | PR #1623 MERGED — Jira JN-5616 still "In Review" → needs "Done". |
| **#1588 unchanged** | Still CONFLICTING, pre-commit FAIL. |

---

## Attention Items

### 🎉 PR #1623 (JN-5616) — MERGED at 13:45 IDT Jun 29 ✅

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)` — **MERGED**
- CI run 28359653930: ALL CHECKS PASS (e2e-product ✅ 20m39s confirmed after pending)
- Worktree `jn-5616-replace-find-project-root` **ARCHIVED** (autonomous action, 14:00 IDT)
- Jira [JN-5616](https://redhat.atlassian.net/browse/JN-5616): still **"In Review"** ⚠️ — **should be "Done"**
- **Action needed:** Update Jira JN-5616 → "Done".

---

### 🔴 PR #1615 (JN-5677, Respond) — APPROVED + MERGEABLE but CI FAILING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- **MAJOR CHANGE** from prior state: was CONFLICTING + CI blank → now OPEN + **MERGEABLE** + **APPROVED** ✅
- But CI run 28366765871 **FAILING**: e2e-api ❌ (3m23s), e2e-tests ❌ (3s), integration ❌ (2m56s), integration-tests ❌ (2s). pre-commit ✅, tox ✅, nox ✅, check-changes ✅, atlas-validate ✅.
- Jira [JN-5677](https://redhat.atlassian.net/browse/JN-5677): Done ✅ (Jira OK)
- **Action needed:** Diagnose + fix e2e-api, e2e-tests, integration, integration-tests failures, then merge (already APPROVED).

---

### 🔴 PR #1606 (JN-5725, off-board) — new CI run 28366983945 in progress

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- OPEN, **MERGEABLE** ✅
- New CI run 28366983945 **IN PROGRESS**: atlas-validate ✅, check-changes ✅, integration ✅, integration-tests ✅, nox ✅, tox-run ✅ — e2e-api ⏳, e2e-gpu-live ⏳, pre-commit-run ⏳ PENDING
- Previous run 28361650415 had: e2e-gpu-live ✅ (breakthrough) + e2e-api ✅ but e2e-smoke ❌ + e2e-tests ❌
- Jira [JN-5725](https://redhat.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Watch e2e-api + e2e-gpu-live results in new run.

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

### 🟡 PR #1615 (JN-5677) — CI BLANK → CI FAILING (see top attention item)

*(See top attention item — PR status changed significantly; CI failures need diagnosis.)*

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
*(JN-5612 removed — PR #1627 MERGED, worktree archived 11:00 IDT Jun 29)*
*(JN-5616 removed — PR #1623 MERGED, worktree archived 14:00 IDT Jun 29)*

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
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
