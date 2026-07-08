# Board State — jounce-workflow-ai

*Last updated: 2026-07-08 13:00 IDT (advance heartbeat)*

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
| jn-5841-agents-md-root | **Publish** | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | 🟢 **run 28932482752: ALL PASS** | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | 🟢 **READY FOR REVIEW.** New CI run 28932482752: pre-commit ✅, e2e-smoke ✅, tox ✅, nox ✅, all-checks ✅. Previous run 28931349732 had pre-commit ❌ — resolved. reviewDecision: REVIEW_REQUIRED. **Action: Get reviewer LGTM to merge.** |
| jn-5827-git-tagging-workflow | **Publish** | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | 🟢 **ALL PASS** run 28922899326 | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | 🟢 **PR #1648 OPEN — CI ALL PASS.** Run 28922899326: all required checks ✅. CodeRabbit review completed ✅. reviewDecision: "" (no required-reviewer policy). **Action: Get human LGTM to merge.** |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ CONFLICTING | 🔴 CONFLICTING | 🔴 CONFLICTING 6+ days. Needs rebase + fix e2e or close PR. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | feat/migrate-dev-to-openshift-gcp | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) (likely) | 🔴 **pre-commit ❌ + e2e-product ❌** (run 28869593069) | APPROVED | 🟡 **APPROVED** (since 12:00 IDT Jul 8). But all-checks still FAIL — cannot merge. Pre-commit ❌ + e2e-product ❌ still blocking. Unchanged. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | 🔴 **run 28931312110 FAILED** (e2e-smoke ❌) | MERGEABLE | 🔴 **5th+ consecutive CI failure** (e2e-smoke ❌ persistent). Run 28931312110 FAILED. Pre-commit ✅, tox ✅, nox ✅, bake ✅ — but e2e-smoke ❌ blocks all-checks. Unchanged. |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | jn-5719-release-diff | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | 🟢 **run 28922685430 ALL PASS + CodeRabbit ✅** | MERGEABLE | 🟢 **READY TO MERGE.** Run 28922685430: all CI ✅ including e2e-smoke ✅, CodeRabbit ✅ complete. REVIEW_REQUIRED — needs final reviewer LGTM. Unchanged. |

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
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** (assumed unchanged — Jira MCP 401) | ❌ Update Jira → Done |
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 | **In Review** (assumed unchanged — Jira MCP 401) | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** (assumed unchanged — Jira MCP 401) | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | OPEN — CI ALL PASS | **Backlog** (assumed unchanged — Jira MCP 401) | ⚠️ Should be → In Review |
| [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | OPEN (was DRAFT, now READY) | **Backlog** (assumed unchanged — Jira MCP 401) | ⚠️ Should be → In Review |

---

## Key Changes Since Last Run (12:30 IDT Jul 8)

| What observed | Status |
|---|---|
| **🟢 #1649 — CI NOW ALL PASS** | New run 28932482752: pre-commit ✅, e2e-smoke ✅, tox ✅, nox ✅, all-checks ✅. Previous run 28931349732 had pre-commit ❌ — RESOLVED. PR is OPEN (not draft), REVIEW_REQUIRED. Ready for reviewer LGTM. |
| **🔴 #1638 — unchanged** | Run 28931312110 still latest (FAILED, e2e-smoke ❌). No new run. |
| **🟢 #1648 (jn-5827) — unchanged** | CI run 28922899326 ALL PASS. Needs human LGTM. |
| **🟢 #1632 — unchanged** | Run 28922685430 ALL PASS + CodeRabbit ✅. Needs LGTM. |
| **🟡 #1647 — unchanged** | APPROVED (since 12:00 IDT). CI still run 28869593069 — pre-commit ❌ + e2e-product ❌. |
| **Jira MCP — 401 again** | MCP 401. 5 mismatches assumed unchanged. |
| **No merges detected** | 0 auto-archives this run. |

---

## Attention Items

### 🟢 #1649 — CI ALL PASS — Needs Reviewer LGTM

Worktree `jn-5841-agents-md-root` in **Publish** zone:
- **PR [#1649](https://github.com/Jounce-IO/jounce/pull/1649)** — OPEN (not draft), REVIEW_REQUIRED
- **CI run 28932482752**: ALL PASS — pre-commit ✅ (4m47s), e2e-smoke ✅ (11m10s), tox ✅, nox ✅, all-checks ✅
- Previous run 28931349732 had pre-commit ❌ — RESOLVED (new push or re-trigger fixed it)
- **Action:** Get reviewer LGTM to merge.

---

### 🔴 PR #1638 — 5th CONSECUTIVE CI FAILURE (e2e-smoke persistent)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): `chore(infra): vLLM analyzer prerequisites - workflow improvements`
- **Run 28930566279** (was in-progress at 12:00 IDT): completed — FAILURE
- **Run 28931312110** (newer, current): FAILED — e2e-smoke ❌ (11m4s), e2e-tests ❌, all-checks ❌
- GOOD NEWS: pre-commit ✅, tox ✅, nox ✅, bake ✅, integration ✅, e2e-api ✅ — all pass now
- e2e-smoke is the sole persistent blocker
- **Action:** Investigate e2e-smoke failure in run 28931312110 — is it a flaky test or a code issue?

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

### 🟡 PR #1647 — APPROVED but CI STILL FAILING

PR [#1647](https://github.com/Jounce-IO/jounce/pull/1647): `test: testing-dev-before-migration JN-5445`
- **reviewDecision: APPROVED** (since 12:00 IDT Jul 8)
- **CI run 28869593069:** pre-commit ❌ (4m38s) + e2e-product ❌ (32m25s) — still failing, unchanged
- all-checks ❌ — cannot merge despite approval
- **Action:** Fix pre-commit + e2e-product failures before this can merge.

---

### ❌ Jira Mismatches (5 active)

**Merged PRs not reflected in Jira (3):**
- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED Jul 6 → Jira **"Backlog"** (should be Done)
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 → Jira **"In Review"** (should be Done)
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED Jul 7 → Jira **"In Progress"** (should be Done)

**Active PRs not reflected in Jira (2 — lower priority):**
- [JN-5827](https://redhat.atlassian.net/browse/JN-5827): PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648) OPEN, CI ALL PASS → Jira **"Backlog"** (should be In Review)
- [JN-5841](https://redhat.atlassian.net/browse/JN-5841): PR [#1649](https://github.com/Jounce-IO/jounce/pull/1649) OPEN READY → Jira **"Backlog"** (should be In Review)

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
