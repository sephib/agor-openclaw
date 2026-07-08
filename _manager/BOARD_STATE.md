# Board State — jounce-workflow-ai

*Last updated: 2026-07-08 11:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, no sessions. Stale 23+ days. |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 13+ days with no session or PR. |
| jn-5841-agents-md-root | **Publish** | [#1649 DRAFT](https://github.com/Jounce-IO/jounce/pull/1649) | 🟢 **CI PASS** run 28924179820 | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | 🟡 **DRAFT PR created 10:04 IDT Jul 8.** CI run 28924179820: pre-commit ✅, tox ✅, nox ✅, all-checks ✅ (docs-only; e2e/deploy/api skipping). Session [019f3e01](http://127.0.0.1:3030/ui/s/019f3e01ee07703caf8b9576/) IDLE + **ready_for_prompt: TRUE**. **Action: Review PR, remove DRAFT, request reviewer.** |
| jn-5827-git-tagging-workflow | **Publish** | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | 🟢 **ALL PASS** run 28922899326 | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | 🟢 **PR #1648 OPEN — CI ALL PASS.** Run 28922899326: all required checks ✅. CodeRabbit review completed ✅. reviewDecision: "" (no required-reviewer policy). **Action: Get human LGTM to merge.** |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ CONFLICTING | 🔴 CONFLICTING | 🔴 CONFLICTING 6+ days. Needs rebase + fix e2e or close PR. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | feat/migrate-dev-to-openshift-gcp | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) (likely) | 🔴 **pre-commit ❌ + e2e-product ❌** (run 28869593069) | MERGEABLE | 🔴 **DEGRADED**: run 28869593069 — e2e-product ❌ (32m25s, FAILED) + pre-commit ❌. Unchanged. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | 🟡 **NEW run 28928793754 IN PROGRESS** (started 11:29 IDT) | MERGEABLE | 🟡 **NEW CI RUN**: run 28928793754 started 11:29 IDT — bake ✅, atlas-validate ✅, check-changes ✅; e2e-api/integration/pre-commit-run/tox PENDING. Was: run 28900734572 e2e-smoke ❌. |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | jn-5719-release-diff | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | 🟢 **run 28922685430 ALL PASS + CodeRabbit ✅** | MERGEABLE | 🟢 **READY TO MERGE.** Run 28922685430: all CI ✅ including e2e-smoke ✅, CodeRabbit ✅ complete. REVIEW_REQUIRED — needs final reviewer LGTM. |

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
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** (confirmed acli Jul 8) | ❌ Update Jira → Done |
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 | **In Review** (confirmed acli Jul 8) | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** (confirmed acli Jul 8) | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | OPEN — CI ALL PASS | **Backlog** (confirmed acli Jul 8) | ⚠️ Should be → In Review |
| [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | [#1649 DRAFT](https://github.com/Jounce-IO/jounce/pull/1649) | OPEN DRAFT | **Backlog** (confirmed acli Jul 8) | ⚠️ Should be → In Progress |

---

## Key Changes Since Last Run (11:00 IDT Jul 8)

| What observed | Status |
|---|---|
| **🟡 #1638 — NEW CI RUN 28928793754 IN PROGRESS** | New run started 11:29 IDT. bake ✅, atlas-validate ✅, check-changes ✅; e2e-api/integration/pre-commit-run/tox PENDING. Was: run 28900734572 e2e-smoke ❌. Watch for result. |
| **🟡 jn-5841 — PR #1649 DRAFT unchanged** | CI run 28924179820 ALL PASS. Still DRAFT. Session [019f3e01](http://127.0.0.1:3030/ui/s/019f3e01ee07703caf8b9576/) IDLE + ready_for_prompt: TRUE. **Action: Remove DRAFT, request reviewer.** |
| **🟢 #1648 (jn-5827) — unchanged** | CI run 28922899326 ALL PASS. CodeRabbit completed ✅. reviewDecision "". Needs human LGTM. |
| **🟢 #1632 — unchanged** | Run 28922685430 ALL PASS + CodeRabbit ✅. REVIEW_REQUIRED. Still needs final LGTM. |
| **#1647 — Unchanged** | pre-commit ❌ + e2e-product ❌ (run 28869593069). No new run. |
| **Jira mismatches — 5 active** | JN-5717 "Backlog", JN-5794 "In Review", JN-5546 "In Progress" (need Done). JN-5827 "Backlog" + JN-5841 "Backlog" (active PRs). All confirmed. |
| **No merges detected** | 0 auto-archives this run. |

---

## Attention Items

### 🟡 jn-5841 — PR #1649 CREATED (DRAFT) — Needs Review

Worktree `jn-5841-agents-md-root` in **Publish** zone:
- **PR [#1649](https://github.com/Jounce-IO/jounce/pull/1649)** "docs: add root AGENTS.md and refactor CLAUDE.md (JN-5841)" created **10:04 IDT Jul 8**
- **DRAFT** — needs to be promoted to ready for review
- **CI run 28924179820**: all-checks ✅, pre-commit ✅, tox ✅, nox ✅ (docs-only; e2e/deploy/integration/api all skipping)
- **Session [019f3e01](http://127.0.0.1:3030/ui/s/019f3e01ee07703caf8b9576/)**: IDLE, **ready_for_prompt: TRUE**
- **Action:** Review the PR content. If satisfied, remove DRAFT flag and request reviewer.

---

### 🟢 #1648 (jn-5827) — PR OPEN, CI ALL PASS — Get Human LGTM

PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648): "feat(release): implement git tagging workflow for Jounce repo (JN-5827)"
- **CI run 28922899326**: ALL required checks PASS
- **CodeRabbit**: Review completed ✅
- **reviewDecision**: "" (no required-reviewer policy currently blocking)
- **Action: Get a human reviewer to LGTM and merge.**

---

### 🟢 PR #1632 (JN-5719) — READY TO MERGE

PR [#1632](https://github.com/Jounce-IO/jounce/pull/1632): `feat(jbenchmark): release diff layer`
- **CI run 28922685430**: ALL checks ✅ including e2e-smoke ✅
- **CodeRabbit ✅** complete
- State: OPEN, MERGEABLE, REVIEW_REQUIRED
- **Action:** Get final reviewer LGTM → merge.

---

### 🟡 PR #1638 — NEW CI RUN 28928793754 IN PROGRESS (started 11:29 IDT)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): `chore(infra): vLLM analyzer prerequisites - workflow improvements`
- **Previous run 28900734572**: e2e-smoke ❌ FAILED (10m24s)
- **NEW run 28928793754**: started 11:29 IDT, IN PROGRESS — bake ✅, atlas-validate ✅, check-changes ✅; e2e-api/integration/pre-commit-run/tox PENDING
- **Action:** Wait for run 28928793754 to complete. If e2e-smoke passes, PR may be ready.

---

### 🔴 PR #1647 — DEGRADED: Both Pre-commit AND e2e-product FAILING

PR [#1647](https://github.com/Jounce-IO/jounce/pull/1647): `test: testing-dev-before-migration JN-5445`
- **CI run 28869593069:** pre-commit ❌ (4m38s) + e2e-product ❌ (32m25s — FAILED) — unchanged
- e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅
- **Action:** Both pre-commit AND e2e-product need fixing.

---

### ❌ Jira Mismatches (5 active)

**Merged PRs not reflected in Jira (3):**
- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED Jul 6 → Jira **"Backlog"** (should be Done)
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 → Jira **"In Review"** (should be Done)
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED Jul 7 → Jira **"In Progress"** (should be Done)

**Active PRs not reflected in Jira (2 — lower priority):**
- [JN-5827](https://redhat.atlassian.net/browse/JN-5827): PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648) OPEN, CI ALL PASS → Jira **"Backlog"** (should be In Review)
- [JN-5841](https://redhat.atlassian.net/browse/JN-5841): PR [#1649 DRAFT](https://github.com/Jounce-IO/jounce/pull/1649) OPEN DRAFT → Jira **"Backlog"** (should be In Progress)

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (13+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run

None.

(jn-5780-add-jn-project archived 13:34 IDT Jul 6; fix-dashboard gone between 21:30–22:00 IDT Jul 7)

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
