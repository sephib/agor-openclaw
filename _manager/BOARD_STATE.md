# Board State — jounce-workflow-ai

*Last updated: 2026-07-07 21:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, no sessions. Stale 22+ days. |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5841-agents-md-root | **Validate** | — | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | 🟡 Validate session [019f3d82](http://127.0.0.1:3030/ui/s/019f3d8216db751081637244/) "Validate JN-5841 — AGENTS.md + CLAUDE.md refactor" **IDLE + ready_for_prompt: TRUE** (completed ~20:03 IDT). Joseph needs to review validate output and advance. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 12+ days with no session or PR. |
| fix-dashboard-syntax-error | Plan | — | — | — | 🔴 ZOMBIE: agor-openclaw repo, filesystem_status=FAILED. 20+ days stale. PROPOSAL: archive. |
| jn-5827-git-tagging-workflow | **Publish** | [#1648 DRAFT](https://github.com/Jounce-IO/jounce/pull/1648) | 🟢 **ALL PASS** (run 28885455833) | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | 🟢 **CI ALL PASS** (run 28885455833): pre-commit ✅, tox ✅, nox ✅, all-checks ✅. e2e/bake SKIPPING (DRAFT). **Ready to remove DRAFT flag** → triggers full e2e. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ CONFLICTING | 🔴 CONFLICTING | 🔴 CONFLICTING 5+ days. Needs rebase + fix e2e or close PR. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | feat/migrate-dev-to-openshift-gcp | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) (likely) | 🔴 **pre-commit ❌ + e2e-product ❌** (run 28869593069) | MERGEABLE | 🔴 **DEGRADED**: run 28869593069 — e2e-product ❌ (32m25s, FAILED) + pre-commit ❌. Two blockers. Unchanged. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | 🔴 **tox ❌ + nox ❌** NEW run 28885456652 + e2e-smoke ⏳ | MERGEABLE | 🔴 **NEW RUN REGRESSION** (run 28885456652): tox ❌ (5m4s) + nox ❌. e2e-smoke PENDING. pre-commit ✅ / e2e-api ✅ / integration ✅ / bake ✅. Previous run 28864329208 had e2e-product ❌; now tox+nox also failing. |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | jn-5719-release-diff | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | ✅ all-checks ✅ (run 28775331183) | MERGEABLE | 🟢 CLEAN! All CI passing. REVIEW_REQUIRED. Ready to merge. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Waiting/Blocked | Refactor run_jbenchmark script to support redesign flow |
| [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | Backlog | DAL extensions for dashboard queries (worktree in BLOCKED zone) |
| [JN-5462](https://redhat.atlassian.net/browse/JN-5462) | Backlog | Agentic Jira → PR workflow — Forge |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED 09:19 IDT Jul 6 | **Backlog** (confirmed acli Jul 7 18:32 IDT) | ❌ Update Jira → Done |
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **In Review** (confirmed acli Jul 7 18:32 IDT) | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED 08:10 IDT Jul 7 | **In Progress** (confirmed acli Jul 7 18:32 IDT) | ❌ Update Jira → Done |

---

## Key Changes Since Last Run (20:30 IDT Jul 7)

| What observed | Status |
|---|---|
| **🟡 #1638 NEW CI run 28887503203 IN PROGRESS** | Someone pushed a fix commit after run 28885456652 (tox ❌ + nox ❌). New run 28887503203: tox ⏳ / e2e-api ⏳ / integration ⏳ / pre-commit ⏳ all PENDING. bake ✅ / check-changes ✅ / atlas-validate ✅. Monitoring — result pending next heartbeat. |
| **jn-5841 — Unchanged** | Validate session [019f3d82](http://127.0.0.1:3030/ui/s/019f3d8216db751081637244/) IDLE + ready_for_prompt: TRUE. Joseph still needs to review validate output. |
| **#1648 (jn-5827) — Unchanged** | DRAFT, CI ALL PASS (run 28885455833 unchanged). Remove DRAFT flag to trigger full e2e. |
| **#1647 — Unchanged** | pre-commit ❌ + e2e-product ❌ (run 28869593069). |
| **#1632 — Unchanged** | All CI ✅, REVIEW_REQUIRED. Ready to merge. |
| **Jira mismatches** | Jira MCP 401 error this run; acli has no issue-view command. Last confirmed 18:32 IDT Jul 7 — assumed unchanged (JN-5717/5794/5546 all still need Done). |
| **No merges detected** | 0 auto-archives this run. |

---

## Attention Items

### 🟢 jn-5827 — PR #1648: CI ALL PASS — Remove DRAFT Flag!

Worktree `jn-5827-git-tagging-workflow` in **Publish** zone:
- **PR [#1648 DRAFT](https://github.com/Jounce-IO/jounce/pull/1648)**: "feat(release): implement git tagging workflow for 3.5GA (JN-5827)"
- **NEW CI run 28885455833**: **ALL PASS** ✅ — pre-commit ✅, tox ✅, nox ✅, all-checks ✅, deploy ✅, JIRA Association ✅, check-changes ✅, atlas-validate ✅
- e2e-product, e2e-smoke, e2e-api, integration-run, bake, atlas-validate-run: all **SKIPPING** (DRAFT PR)
- **Action:** Remove DRAFT flag → triggers full e2e run. Request external code review.

---

### 🟡 jn-5841 — Validate Session COMPLETE, Awaiting Joseph's Review

Worktree `jn-5841-agents-md-root` in **Validate** zone:
- **Session [019f3d82](http://127.0.0.1:3030/ui/s/019f3d8216db751081637244/)** "Validate JN-5841 — AGENTS.md + CLAUDE.md refactor": **IDLE + ready_for_prompt: TRUE** (completed ~20:03 IDT)
- "continue" session [019f3d35](http://127.0.0.1:3030/ui/s/019f3d35877277f2bff66999/) IDLE, ready_for_prompt: FALSE
- **Action:** Joseph reviews validate session output. If pass → advance to Publish zone and trigger `/implement:publish`. If issues → revise.

---

### 🟡 PR #1638 — NEW CI Run 28887503203 IN PROGRESS (Fix Attempt)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): `chore(infra): vLLM analyzer prerequisites`
- **NEW CI run 28887503203** (21:00 IDT): tox ⏳ + e2e-api ⏳ + integration ⏳ + pre-commit ⏳ all PENDING.
- bake ✅, check-changes ✅, atlas-validate ✅ already passing in new run.
- Previous run 28885456652 had: tox ❌ (5m4s) + nox ❌ — someone pushed a fix commit.
- **Action:** Monitor next heartbeat for run 28887503203 results. If tox ✅ + nox ✅ → regression resolved.

---

### 🔴 PR #1647 — DEGRADED: Both Pre-commit AND e2e-product FAILING

PR [#1647](https://github.com/Jounce-IO/jounce/pull/1647): `test: testing-dev-before-migration JN-5445`
- **CI run 28869593069:** pre-commit ❌ (4m38s) + e2e-product ❌ (32m25s — FAILED) — unchanged
- e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅
- **Action:** Both pre-commit AND e2e-product need fixing. Two blockers now.

---

### 🟢 PR #1632 (JN-5719) — CLEAN, Ready to Merge

PR [#1632](https://github.com/Jounce-IO/jounce/pull/1632): `feat(jbenchmark): release diff layer`
- **State:** MERGEABLE, REVIEW_REQUIRED
- **CI:** all-checks ✅ — all CI passing (unchanged run 28775331183)
- **Action:** READY TO MERGE.

---

### ❌ Jira Mismatches (3 active — confirmed via acli 18:32 IDT Jul 7)

- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED Jul 6 → Jira **"Backlog"** (should be Done)
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 → Jira **"In Review"** (should be Done)
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED Jul 7 → Jira **"In Progress"** (should be Done)

---

### 🔴 fix-dashboard-syntax-error — ZOMBIE WORKTREE in Plan Zone

- **Status:** agor-openclaw repo, filesystem_status=FAILED, 20+ days stale
- **Created:** Jun 17 2026
- **No PR, no Jira ticket**
- **Action needed:** Archive this worktree (proposal pending)

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (12+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run

| Worktree | Reason | Archived At |
|---------|--------|------------|
| None | No merged/closed PRs detected | — |

(jn-5780-add-jn-project archived 13:34 IDT Jul 6 in prior run)

---

## Recently Merged (2026-07-07 / 2026-07-06 / 2026-07-01 / 2026-06-29)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | 08:10 IDT Jul 7 | jn-5546-...-3 (already deleted from Agor) |
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
