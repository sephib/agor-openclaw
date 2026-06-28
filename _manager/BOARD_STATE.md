# Board State — jounce-workflow-ai

*Last updated: 2026-06-28 20:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5724-lychee-precommit-flaky | [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | Publish | In Review | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (run 28164293495, unchanged since Jun 25 13:32 IDT) | REVIEW_REQUIRED | 🟡 **CONFLICTING — needs rebase.** CI still ALL PASS. |
| jn-5616-replace-find-project-root | [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | Validate | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **OPEN** ⚠️ CONFLICTING | ✅ **ALL PASS** (run 28153233486, unchanged since Jun 25 13:32 IDT) | REVIEW_REQUIRED | 🟡 **CONFLICTING — needs rebase.** CI still ALL PASS. |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | **Revise** | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** CONFLICTING | ⚠️ **CI CHECKS GONE** — only CodeRabbit showing (no run data since Jun 25 13:05 IDT) | ="" (no decision) | 🟡 **CI BLANK** — prior integration failures no longer in rollup. Still CONFLICTING. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) OPEN CONFLICTING | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996, stale) | reviewDecision="" | 🔴 **STALE** — unchanged since Jun 17. Pre-commit FAIL, CONFLICTING. Jira should be "In Review". |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT OPEN CONFLICTING | — | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jira-operations | — | (no zone) | — | — | — | — | ⚠️ session timed_out 07:38 IDT Jun 25. No PR, no Jira, no zone. Needs decision. |
| jn-5612-fix-github-sha | [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | **Publish** | In Progress ⚠️ | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) **OPEN** MERGEABLE | ✅ **ALL PASS** (run 28318509109, e2e-api ✅ 4m37s, e2e-smoke ✅ 11m9s) | REVIEW_REQUIRED | 🟢 **CI ALL PASS** — MERGEABLE, all checks complete. Jira still "In Progress" — should be "In Review". **Assign reviewer now.** |
| jn-5244-cli-flags | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | **Ingest** | In Progress | — | — | — | ℹ️ Created 14:49 IDT Jun 28. No sessions yet. JN-5244: Add --user, --no-cache, --skip-estimator CLI flags. Ready to ingest. |
| jn-5780-add-jn-project | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | **Plan** | Unknown | — (GitLab "create MR" link, no actual PR) | — | — | ℹ️ Created 08:32 IDT Jun 28, different repo: redhat/jira-autofix. JN-5780 on redhat.atlassian.net. No sessions, no actual PR. Needs Joseph review — may be agentic CI autofix worktree. |

**Untracked worktrees on board:**
- `fix-dashboard-syntax-error` (Plan zone, filesystem_status: failed, last used Jun 17) — still visible. No PR. Stale.
- `model-packaging-cr` (Code Review zone, last used Jun 15) — inactive since Jun 15. No PR. Different repo (model-packaging-pipeline).

**Archived This Session:**
- none

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

**Still on board (not archived):**
- `model-packaging-cr` (Code Review zone, model-packaging-pipeline repo, no PR, no sessions, last used Jun 15) — board scan Jun 28 16:30 IDT confirms still active. Previous tracking note "removed from tracking / confirmed absent" was incorrect. No PR to check; needs manual decision.

**Removed from tracking (confirmed archived on board):**
- dual-heartbeat-system — confirmed archived in board scan Jun 23
- standup-drafts — confirmed archived in board scan Jun 23
- fix-dashboard-syntax-error — no longer visible in any zone scan (was Plan zone); presumed archived

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | 🔴 **NEW run 28329867635** (20:30 IDT — another push since 20:00 IDT): **e2e-smoke ❌ FAIL** (12m15s). **e2e-tests ⏳ PENDING**. **e2e-gpu-live ⏳ PENDING** (run 28329867561). All other checks PASS. Third+ consecutive e2e-smoke failure — still not resolved. | OPEN, MERGEABLE | 🔴 **e2e-smoke FAILING persistently** — 3+ consecutive runs. e2e-tests/e2e-gpu-live pending. Diagnose e2e-smoke root cause in run 28329867635. |

---

## Key Changes Since Last Run (20:00 IDT Jun 28)

| What observed | Status |
|---|---|
| **🔴 PR #1606 NEW run 28329867635 — e2e-smoke FAIL AGAIN** | Another push since 20:00 IDT. Run 28329867635 supersedes 28328248783. e2e-smoke ❌ FAIL (12m15s, same duration). e2e-tests ⏳ PENDING (was ❌ FAIL in prior run). e2e-gpu-live ⏳ PENDING (run 28329867561). Third+ consecutive e2e-smoke failure. Root cause still unresolved. |
| **🟢 PR #1627 CI ALL PASS — JN-5612 (unchanged)** | Still ALL PASS (run 28318509109). OPEN, MERGEABLE, REVIEW_REQUIRED. Assign reviewer. |
| **JN-5612 Jira mismatch (persists)** | Jira still "In Progress" — update → "In Review". |
| **#1622 unchanged** | Still CONFLICTING, CI ALL PASS (run 28164293495). Needs rebase. |
| **#1623 unchanged** | Still CONFLICTING, CI ALL PASS (run 28153233486). Needs rebase. |
| **#1615 unchanged** | CI still blank — only CodeRabbit in rollup. Still CONFLICTING. |
| **#1588 unchanged** | Still 2 FAIL pre-commit (run 27933817996). Stale. |
| **No new merges** | Step 1 sweep confirmed no new merges since Jun 28 20:00 IDT. |

---

## Attention Items

### 🟢 PR #1627 (JN-5612, Publish) — CI ALL PASS, assign reviewer

PR [#1627](https://github.com/Jounce-IO/jounce/pull/1627): `fix(ci): JN-5612 replace github.GITHUB_SHA with github.sha in workflow run-names`
- OPEN, MERGEABLE (no git conflict), REVIEW_REQUIRED
- CI run 28318509109 — **ALL PASS** ✅: pre-commit ✅, integration ✅, tox ✅, nox ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅ (4m37s), e2e-smoke ✅ (11m9s)
- Jira [JN-5612](https://redhat.atlassian.net/browse/JN-5612): **In Progress** ⚠️ — should be "In Review" now PR is fully CI-green
- **Action needed:** (1) **Assign a reviewer now** — CI is fully green. (2) Update Jira JN-5612 → "In Review".

---

### 🔴 PR #1606 (JN-5725, off-board) — e2e-smoke FAIL persistent (run 28329867635)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- OPEN, MERGEABLE (no git conflict)
- **NEW run 28329867635** (20:30 IDT — another push since 20:00 IDT): e2e-smoke ❌ FAIL (12m15s). e2e-tests ⏳ PENDING. All other checks PASS.
- **e2e-gpu-live ⏳ PENDING** (run 28329867561)
- Third+ consecutive e2e-smoke failure — root cause NOT resolved despite multiple pushes.
- Jira [JN-5725](https://redhat.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Diagnose e2e-smoke root cause — persistent across 3+ runs. Check e2e-smoke logs in run 28329867635.

---

### ℹ️ jn-5780-add-jn-project (Plan zone) — new worktree, needs clarification

Appeared in board scan (Plan zone). Created 08:32 IDT Jun 28.
- Repo: redhat/jira-autofix (not jounce)
- JN-5780: On redhat.atlassian.net (different Jira instance from jounce)
- PR URL: GitLab "create new MR" placeholder — no actual PR exists
- No sessions started
- **Action needed:** Joseph to clarify — is this intentional? Should it be tracked/moved/archived?

---

### 🟡 PR #1615 (JN-5677) — CI BLANK + CONFLICTING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- OPEN, CONFLICTING
- ⚠️ **CI checks missing from rollup** — only CodeRabbit showing (SUCCESS, Jun 25 13:05 IDT). Previous integration failures (run 28167796913) no longer appear.
- Jira [JN-5677](https://redhat.atlassian.net/browse/JN-5677): Done ✅
- **Action needed:** (1) Determine if branch was force-pushed without CI trigger. (2) Fix merge conflict with main. (3) Re-run CI.

---

### 🟡 PR #1622 (JN-5724) — CI ALL PASS but CONFLICTING

PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622): `fix(lychee): remove stale exclude_path for non-existent directory (JN-5724)`
- OPEN, CONFLICTING (since Jun 25 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28164293495 — **ALL checks ✅ PASS** (e2e-smoke 10m29s)
- Jira [JN-5724](https://redhat.atlassian.net/browse/JN-5724): In Review ✅
- **Action needed:** Rebase on main. CI will re-run. Assign reviewer once green.

---

### 🟡 PR #1623 (JN-5616) — CI ALL PASS but CONFLICTING

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- OPEN, CONFLICTING (since Jun 25 15:32 IDT), REVIEW_REQUIRED
- CI: Run 28153233486 — **ALL checks ✅ PASS** (e2e-product 27m56s, e2e-smoke 10m11s)
- Jira [JN-5616](https://redhat.atlassian.net/browse/JN-5616): In Review ✅
- **Action needed:** Rebase on main. CI will re-run. Assign reviewer once green.

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + CONFLICTING (stale)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (run 27933817996). PR is CONFLICTING. Stale since Jun 17.

**Required action:** (1) Fix pre-commit failures. (2) Resolve merge conflict. (3) Assign reviewer. (4) Update [JN-5546](https://redhat.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ JN-5612 — Jira still "In Progress" despite PR #1627 CI ALL PASS

[JN-5612](https://redhat.atlassian.net/browse/JN-5612): "Fix github.GITHUB_SHA → github.sha in all workflow run-name fields" — **In Progress** (should be "In Review"). Worktree `jn-5612-fix-github-sha` in **Publish zone**. PR [#1627](https://github.com/Jounce-IO/jounce/pull/1627) is OPEN, MERGEABLE, ALL CI PASS. **Action:** Update Jira → "In Review" + assign reviewer immediately.

---

### ⚠️ jira-operations — session timed_out, no zone

Branch `jira-operations` — No PR, no Jira ticket, no zone assigned.
- Session timed_out at 07:38 IDT (Jun 25). Title: "Create Q4 Planning Epic + Stories"
- **Action needed:** Joseph to decide: archive (if one-off task) or assign zone + create tickets

---

### ⚠️ internal-cr-system — no PR, no Jira, stagnant

Branch `internal-cr-system` in Code zone — no PR, no Jira ticket. Stagnant since Jun 18. filesystem_status: failed (git lock on .git/config).

---

### ⚠️ Jira mismatches (2 items)

| Ticket | Jira Status | PR | Merged/State | Notes |
|--------|-------------|-----|--------|-----------|
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | OPEN, 2 CI FAIL + CONFLICTING | Should be "In Review" AND needs CI fix |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | In Progress | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | OPEN, MERGEABLE, ALL CI PASS | Should be "In Review" now PR is open |

---

## Sprint Tickets Without Board Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5670](https://redhat.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree |
| [JN-5539](https://redhat.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — may be cross-cutting |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Refactor run_jbenchmark script to support redesign flow | **Waiting/Blocked** | No worktree — parent of JN-5244 |
| [JN-5678](https://redhat.atlassian.net/browse/JN-5678) | Dashboard README and setup instructions | **Backlog** | No worktree |
| [JN-5728](https://redhat.atlassian.net/browse/JN-5728) | Fix e2e CI workflow gaps | **Backlog** | No worktree |

*(JN-5244 removed — worktree jn-5244-cli-flags created 14:49 IDT Jun 28)*
*(JN-5612 removed — worktree jn-5612-fix-github-sha exists on board)*

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
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
