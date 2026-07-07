# Board State — jounce-workflow-ai

*Last updated: 2026-07-07 09:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5546-docs-document-module-layout-convention-and-3 | **Respond** | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | **🔴 pre-commit ❌** (run 28822455546 — 20:52 IDT Jul 6) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 MERGEABLE but pre-commit still failing. Latest run 28822455546: Build ✅, Integration ✅, e2e ✅, tox ✅, nox ✅, **pre-commit ❌** (4m28s job 85477327366). Unchanged since 00:00 IDT run. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, stagnant 21+ days. Needs investigation or archive. |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5841-agents-md-root | Ingest | — | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | Ingest session (019f3236) idle/completed. No PR yet. Ready for Plan phase. |
| jn-5795-upgrade-to-guidellm-v070 | NO ZONE | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | ℹ️ Design session done (idle Jun 30 12:45 IDT). No zone assigned. Proposal: move to Plan zone. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 12+ days with no session or PR. |
| ~~jn-5780-add-jn-project~~ | ~~Plan~~ | ~~GitLab MR#887~~ | — | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) — Done | ✅ ARCHIVED 13:34 IDT Jul 6 — JN-5780 Done + inactive 8+ days (autonomous) |
| fix-dashboard-syntax-error | Plan | — | — | — | 🔴 ZOMBIE: agor-openclaw repo, not found in Agor scan. Created Jun 17, 19+ days stale. PROPOSAL: archive. |
| sprint-planning-jul | Plan | — | — | — | ℹ️ Updated 06:50 IDT Jul 2. No sessions, no PR, no Jira. Sprint planning for July? |
| jn-5827-git-tagging-workflow | Ingest | — | — | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) — Backlog | ℹ️ Created 09:06 IDT Jul 6. Session 019f36af idle 09:11 IDT, 59 msgs — plan written. Still in Ingest zone. Consider moving to Plan zone. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ e2e-smoke ❌ + e2e-tests ❌ + all-checks ❌ (run 28527509341) | 🔴 CONFLICTING | 🔴 CONFLICTING (since 10:00 IDT Jul 2). e2e failures persist. Jira Done. Needs rebase + fix e2e or close PR. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | feat/migrate-dev-to-openshift-gcp | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) (likely) | 🔴 e2e-api ❌ + e2e-tests ❌ + all-checks ❌ (run 28801725588) | MERGEABLE | 🆕 DETECTED: Not on board. CI: e2e-api FAILURE, e2e-tests FAILURE. Pre-commit ✅ all others ✅. Updated 15:08 IDT Jul 6. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | 🔴 e2e-smoke ❌ + e2e-tests ❌ + all-checks ❌ (run 28808026450) | MERGEABLE | 🆕 DETECTED: Not on board. CI: e2e-smoke FAILURE, e2e-tests FAILURE. Pre-commit ✅ all others ✅. Updated 16:47 IDT Jul 6. |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | jn-5719-release-diff | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | ✅ all-checks ✅ (run 28775331183) | MERGEABLE | 🟢 CLEAN! All CI passing. Updated 07:41 IDT Jul 6. Ready to merge. |

---

## Sprint Tickets Without Worktrees

(Awaiting acli jira workitem search — tool syntax verification in progress)

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED 09:19 IDT Jul 6 | **Backlog** | ❌ Update Jira → Done |
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, CONFLICTING, e2e ❌ | **Done** | ⚠️ Ticket marked Done but PR open + conflicting |

---

## Key Changes Since Last Run (09:30 IDT Jul 7)

| What observed | Status |
|---|---|
| **Board static since 09:00 IDT Jul 7** | No PR merges, no zone moves, no new CI runs. Fully static (30-min delta). |
| **#1588 pre-commit ❌ persists** | CI run 28822455546 still failing (job 85477327366, 4m28s). Unchanged since 20:52 IDT Jul 6 (~13h). Needs fix before merge. |
| **PR #1606: unchanged** | Still CONFLICTING + e2e ❌ (run 28527509341). No new CI since Jul 2 (5+ days stale). |
| **PR #1596: unchanged** | DRAFT CONFLICTING. No activity. |
| **Off-board PRs unchanged** | #1632 (✅ CLEAN, REVIEW_REQUIRED), #1638 (e2e ❌ run 28808026450), #1647 (e2e-api ❌+REVIEW_REQUIRED run 28801725588). |
| **Jira mismatches: unchanged** | JN-5717 still Backlog (PR #1631 merged Jul 6); JN-5794 still In Review (PR #1643 merged Jul 1). Jira MCP 401 — unverifiable via MCP. |

---

## Attention Items

### 🔴 PR #1588 (JN-5546) — pre-commit ❌ persists

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): `docs(jbenchmark): add CONTRIBUTING.md and service READMEs`
- **Status:** **MERGEABLE** ✅ (rebased overnight Jul 6→7 — was CONFLICTING)
- **Zone:** **Respond**
- **CI run 28822455546** (triggered 20:52 IDT Jul 6):
  - Build: ✅ all 7 service images passing
  - Integration: ✅ (3m9s)
  - e2e-tests: ✅ (3s)
  - tox: ✅ (3m31s)
  - nox: ✅ (4s)
  - deploy: ✅
  - **pre-commit: ❌ FAILING** (4m28s, job 85477327366)
  - **all-checks: ❌** (blocked by pre-commit)
  - e2e-smoke / e2e-api / e2e-product: skipping (requires merge)
- **Action needed:** Fix pre-commit failure → full CI will pass → ready to merge

---

### 🔴 PR #1606 (JN-5725) — CONFLICTING (Off-board)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- **State:** CONFLICTING as of 10:00 IDT Jul 2
- **CI (run 28527509341):** all-checks ❌, e2e-smoke ❌ (6m17s), e2e-tests ❌ (4s) — all other checks ✅
- **Jira:** JN-5725 shows Done
- **Action needed:** Rebase on main + fix e2e failures, or close PR.

---

### 🆕 PR #1647 (JN-5445?) — e2e ❌, Not on Board

PR [#1647](https://github.com/Jounce-IO/jounce/pull/1647): `test: testing-dev-before-migration JN-5445`
- **State:** MERGEABLE
- **CI run 28801725588** (Jul 6 15:08 IDT): e2e-api ❌ (FAILURE 1m6s), e2e-tests ❌ (FAILURE 5s), all-checks ❌. Pre-commit ✅, integration ✅, tox ✅, nox ✅.
- **No worktree on board** — off-board PR.
- **Action:** Monitor or propose worktree creation if Joseph wants tracking.

---

### 🆕 PR #1638 (JN-5725?) — e2e ❌, Not on Board

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): `chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)`
- **State:** MERGEABLE
- **CI run 28808026450** (Jul 6 16:47 IDT): e2e-smoke ❌ (FAILURE 24m45s), e2e-tests ❌ (FAILURE 4s), all-checks ❌. Pre-commit ✅, integration ✅, tox ✅, nox ✅.
- **No worktree on board** — off-board PR.
- **Action:** Monitor or propose worktree creation if Joseph wants tracking.

---

### 🟢 PR #1632 (JN-5719) — CLEAN, Ready to Merge

PR [#1632](https://github.com/Jounce-IO/jounce/pull/1632): `feat(jbenchmark): release diff layer (JN-5719)`
- **State:** MERGEABLE
- **CI run 28775331183** (Jul 6 07:32 IDT): **all-checks ✅** — all CI passing (pre-commit ✅, integration ✅, tox ✅, nox ✅, e2e-smoke ✅, e2e-tests ✅, all-checks ✅)
- **No worktree on board** — off-board PR.
- **Action:** READY TO MERGE. Propose merge or propose adding to board for tracking.

---

### ❌ Jira Mismatches (2 active)

- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED 09:19 IDT Jul 6 → Jira still "Backlog"
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 → Jira still "In Review"

---

### 🔴 fix-dashboard-syntax-error — ZOMBIE WORKTREE in Plan Zone

- **Status:** Not found in current Agor scan (agor-openclaw repo — may be unregistered)
- **Created:** Jun 17 2026 (19+ days stale)
- **No PR, no Jira ticket**
- **Action needed:** Archive this worktree

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (12+ days stale)
- NO ZONE, no sessions, no PR
- Still present but stale. If no longer needed, propose archive.

---

## Archived This Run

| Worktree | Reason | Archived At |
|---------|--------|------------|
| None | — | — |

(jn-5780-add-jn-project archived 13:34 IDT Jul 6 in prior run)

---

## Recently Merged (2026-07-06 / 2026-07-01 / 2026-06-29)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | 09:19 IDT Jul 6 | Off-board PR — no worktree |
| [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | 09:16 IDT Jul 1 | Archived 09:21 IDT Jul 1 |
| [#1628](https://github.com/Jounce-IO/jounce/pull/1628) | [JN-5714](https://redhat.atlassian.net/browse/JN-5714) | 15:39 IDT Jun 30 | Archived Jun 30 16:00 IDT |
| [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | 10:41 IDT Jun 30 | Archived Jun 30 11:00 IDT |
| [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | 10:42 IDT Jun 29 | Archived Jun 29 |
| [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | 10:17 IDT Jun 29 | Archived Jun 29 |
| [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | 13:45 IDT Jun 29 | Archived Jun 29 |
| [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | 15:08 IDT Jun 29 | Archived Jun 29 |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
