# Board State — jounce-workflow-ai

*Last updated: 2026-06-29 12:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | CI | Review | Flags |
|--------|------|------|-------------|-----|-----|--------|-------|
| jn-5616-replace-find-project-root | [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | Respond | In Review | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) **OPEN** ✅ **MERGEABLE** | 🟢 **CI ALMOST GREEN** (run 28359653930 — all PASS including e2e-api ✅; only e2e-smoke ⏳ pending) | "" (no decision — assign reviewer) | 🎉 **e2e-api PASSES!** Only e2e-smoke remaining. Assign reviewer now! |
| jn-5677-dev-historical-mode-notebook-cells | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | **Respond** | Done | [#1615](https://github.com/Jounce-IO/jounce/pull/1615) **OPEN** CONFLICTING | ⚠️ **CI CHECKS GONE** — only CodeRabbit showing (no run data since Jun 25 13:05 IDT) | "" (no decision) | 🟡 **CI BLANK** — only CodeRabbit in rollup. Still CONFLICTING. |
| jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | Code Review | In Progress | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) OPEN CONFLICTING (mergeable=UNKNOWN) | ❌ **2 FAIL** (pre-commit + pre-commit-run, run 27933817996, stale) | reviewDecision="" | 🔴 **STALE** — unchanged since Jun 17. Pre-commit FAIL, CONFLICTING. Jira should be "In Review". |
| internal-cr-system | — | Code | — | — | — | — | ⚠️ No PR. No Jira. Stagnant since Jun 18. filesystem_status: failed (git lock) |
| jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | BLOCKED | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) DRAFT OPEN CONFLICTING | — | — | 🔴 CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | BLOCKED | Backlog | — | — | — | ℹ️ On hold |
| jira-operations | — | (no zone) | — | — | — | — | ⚠️ session timed_out 07:38 IDT Jun 25. No PR, no Jira, no zone. Needs decision. |
| jn-5244-cli-flags | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | **Ingest** | In Progress | — | — | — | ℹ️ Created 14:49 IDT Jun 28. No sessions yet. JN-5244: Add --user, --no-cache, --skip-estimator CLI flags. Ready to ingest. |
| jn-5780-add-jn-project | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | **Plan** | Unknown | — (GitLab "create MR" link, no actual PR) | — | — | ℹ️ Created 08:32 IDT Jun 28, different repo: redhat/jira-autofix. Not visible in jounce board scan (different repo). Needs Joseph review. |

**Untracked worktrees on board:**
- `model-packaging-cr` (Code Review zone, model-packaging-pipeline repo, no PR, no sessions, last used Jun 15) — still on board. No PR to check; needs manual decision.

**Archived This Session (11:00 IDT Jun 29):**
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
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | run 28353163424 **COMPLETE**: atlas-validate ✅, check-changes ✅, e2e-api ✅, integration ✅, integration-tests ✅, nox ✅, pre-commit ✅, pre-commit-run ✅, tox-run ✅ — **e2e-gpu-live ❌ FAIL (30m5s)** — **e2e-smoke ⏳ still PENDING** | OPEN, CONFLICTING | 🟠 e2e-gpu-live FAIL (persistent). e2e-smoke still pending — unknown if it will pass. Still CONFLICTING. Needs rebase + e2e-gpu-live investigation. |

---

## Key Changes Since Last Run (12:30 IDT Jun 29)

| What observed | Status |
|---|---|
| **Board fully static** | No new merges, no CI state changes since 12:00 IDT. |
| **PR #1623 e2e-smoke still pending** | CI run 28359653930 unchanged — all PASS except e2e-smoke ⏳ (same as 12:00 IDT). |
| **PR #1606 e2e-api + e2e-gpu-live still pending** | CI run 28361650415 unchanged — all other checks PASS; e2e-api ⏳ e2e-gpu-live ⏳ still pending. |
| **#1615, #1588 unchanged** | #1615 still CONFLICTING, CI blank. #1588 still CONFLICTING, pre-commit FAIL. |
| **Jira mismatches persist** | JN-5612 still "In Progress" (should be Done); JN-5724 still "In Review" (should be Done). |

---

## Attention Items

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

### 🟠 PR #1606 (JN-5725, off-board) — latest CI run in progress, MERGEABLE

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- OPEN, **MERGEABLE** ✅
- Latest CI run 28361650415 **IN PROGRESS**: atlas-validate ✅, check-changes ✅, integration ✅, integration-tests ✅, nox ✅, pre-commit ✅, pre-commit-run ✅, tox-run ✅ — e2e-api ⏳ PENDING, e2e-gpu-live ⏳ PENDING
- Previous pattern: e2e-gpu-live ❌ FAIL (persistent across multiple runs) — watch this
- Jira [JN-5725](https://redhat.atlassian.net/browse/JN-5725): Done (Unassigned)
- **Action needed:** Wait for e2e-api + e2e-gpu-live results on run 28361650415.

---

### ℹ️ jn-5780-add-jn-project (Plan zone) — needs clarification

Appeared in board scan (Plan zone). Created 08:32 IDT Jun 28. Different repo: redhat/jira-autofix.
- JN-5780: On redhat.atlassian.net
- PR URL: GitLab "create new MR" placeholder — no actual PR exists
- No sessions started
- **Action needed:** Joseph to clarify — is this intentional? Should it be tracked/moved/archived?

---

### 🟡 PR #1615 (JN-5677) — CI BLANK + CONFLICTING

PR [#1615](https://github.com/Jounce-IO/jounce/pull/1615): `feat(jbenchmark): historical mode notebook cells (JN-5677)`
- OPEN, CONFLICTING
- ⚠️ **CI checks missing from rollup** — only CodeRabbit showing (SUCCESS, Jun 25 13:05 IDT).
- Jira [JN-5677](https://redhat.atlassian.net/browse/JN-5677): Done ✅
- **Action needed:** (1) Fix merge conflict with main. (2) Re-run CI.

---

### 🎉 PR #1623 (JN-5616) — CI almost fully green — ASSIGN REVIEWER

PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623): `refactor(jbenchmark): replace find_project_root() in tests with conftest fixtures (JN-5616)`
- OPEN, **MERGEABLE** ✅
- CI run 28359653930 **ALMOST GREEN**: JIRA Association ✅, atlas-validate ✅, check-changes ✅, integration ✅, pre-commit ✅, pre-commit-run ✅, integration-tests ✅, nox ✅, tox-run ✅, **e2e-api ✅ PASS** (3m21s) — only e2e-smoke ⏳ PENDING
- reviewDecision: "" (no decision — assign reviewer)
- Jira [JN-5616](https://redhat.atlassian.net/browse/JN-5616): In Review ✅
- **Action needed:** Assign reviewer! e2e-smoke still pending but all other checks green including e2e-api.

---

### 🔴 PR #1588 (JN-5546) — CI FAIL + CONFLICTING (stale)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): 2 pre-commit checks FAILING (run 27933817996). PR is CONFLICTING. Stale since Jun 17.

**Required action:** (1) Fix pre-commit failures. (2) Resolve merge conflict. (3) Assign reviewer. (4) Update [JN-5546](https://redhat.atlassian.net/browse/JN-5546) from "In Progress" → "In Review".

---

### ⚠️ Jira mismatches (2 items)

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

---

## Recently Merged

| Ticket | PR | Merged |
|--------|----|--------|
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
