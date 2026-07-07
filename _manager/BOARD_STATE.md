# Board State — jounce-workflow-ai

*Last updated: 2026-07-07 13:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, stagnant 22+ days. Needs investigation or archive. |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5841-agents-md-root | Ingest | — | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | Plan revision session (019f3ba0) — idle, `ready_for_prompt: true`, last updated 12:58 IDT Jul 7. Awaiting next action. |
| jn-5795-upgrade-to-guidellm-v070 | **Ingest** | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 12+ days with no session or PR. |
| fix-dashboard-syntax-error | Plan | — | — | — | 🔴 ZOMBIE: agor-openclaw repo, filesystem_status=failed ("fatal: invalid reference: origin/private-julie"). Created Jun 17, 20+ days stale. PROPOSAL: archive. |
| jn-5827-git-tagging-workflow | **Code** | — | — | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) — Backlog | Code session `019f3b88` — **status changed**: was `ready_for_prompt: true` at 12:30 IDT, now `ready_for_prompt: false`, last updated 12:41 IDT Jul 7. Git state DIRTY. May have received a prompt from Joseph. No PR yet. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ e2e-smoke ❌ + e2e-tests ❌ + all-checks ❌ (run 28527509341) | 🔴 CONFLICTING | 🔴 CONFLICTING (since 10:00 IDT Jul 2, 5+ days). e2e failures persist. Jira Done. Needs rebase + fix e2e or close PR. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | feat/migrate-dev-to-openshift-gcp | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) (likely) | 🔴 e2e-api ❌ + e2e-tests ❌ (run 28857608952) | MERGEABLE | 🟡 New CI run 28857608952: e2e-api ❌, e2e-tests ❌, pre-commit pending. Integration ✅, tox ✅, nox ✅. Same e2e pattern. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | ⏳ **NEW RUN 28856989908 — e2e-smoke PENDING** | MERGEABLE | 🟡 **MAJOR IMPROVEMENT**: New run 28856989908. All critical checks PASS (e2e-api ✅, integration ✅, pre-commit ✅, tox ✅, nox ✅, bake ✅, atlas-validate ✅). **Only e2e-smoke still PENDING** (was ❌ in prev run). If e2e-smoke passes → all-checks green → merge candidate! |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | jn-5719-release-diff | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | ✅ all-checks ✅ (run 28775331183) | MERGEABLE | 🟢 CLEAN! All CI passing. REVIEW_REQUIRED. Unchanged. Ready to merge. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5790](https://redhat.atlassian.net/browse/JN-5790) | Waiting/Blocked | Add integration-run to GitHub required status checks |
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5678](https://redhat.atlassian.net/browse/JN-5678) | Backlog | Dashboard README and setup instructions |
| [JN-5462](https://redhat.atlassian.net/browse/JN-5462) | Backlog | Agentic Jira → PR workflow — Forge |

(JN-5670 "Benchmark Visibility Dashboard" is the parent epic; JN-5539 "Dependency & Build Standardization" is also a parent. JN-5672 has a worktree in BLOCKED. JN-5695 has a worktree in BLOCKED.)

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED 09:19 IDT Jul 6 | **Backlog** (confirmed via acli prior run; MCP 401 this run) | ❌ Update Jira → Done |
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **In Review** (confirmed via acli prior run; MCP 401 this run) | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED 08:10 IDT Jul 7 | **In Progress** (confirmed via acli prior run; MCP 401 this run) | ❌ Update Jira → Done |

---

## Key Changes Since Last Run (12:30 IDT Jul 7)

| What observed | Status |
|---|---|
| **🟡 PR #1638: NEW CI run — near green!** | Run 28856989908 running. ALL critical checks PASS. **e2e-smoke PENDING** (was ❌). If it passes → all-checks green → merge candidate! |
| **🟡 PR #1647: new CI run 28857608952** | e2e-api ❌, e2e-tests ❌, pre-commit pending. Same e2e pattern. Integration/tox/nox ✅. |
| **🔔 jn-5827: ready_for_prompt changed** | Was `true` at 12:30 IDT; now `false` (last updated 12:41 IDT). May have received prompt from Joseph between heartbeats. |
| **jn-5841: still ready_for_prompt: true** | Idle since 08:39 IDT (still waiting). Last updated 12:58 IDT. |
| **Jira mismatches: MCP 401 again** | Cannot re-verify; 3 mismatches assumed unchanged. |
| **PR #1606: unchanged** | Still CONFLICTING + e2e ❌ (run 28527509341). 5+ days stale. |
| **PR #1632: unchanged** | All CI ✅, REVIEW_REQUIRED. Ready to merge. |

---

## Attention Items

### 🟡 PR #1638 — e2e-smoke PENDING (Near Green!)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): `chore(infra): vLLM analyzer prerequisites - workflow improvements`
- **CI run 28856989908** in progress.
- **PASSING:** e2e-api ✅, integration ✅, pre-commit ✅, tox ✅, nox ✅, bake ✅, atlas-validate ✅, integration-tests ✅, JIRA Association ✅, CodeRabbit ✅
- **PENDING:** e2e-smoke ⏳ (was ❌ in run 28854238947)
- If e2e-smoke passes: PR will be merge-ready!
- **Action:** Watch e2e-smoke result in next heartbeat. If green, propose merge.

---

### 🔔 jn-5827 — Session Status Changed

Worktree `jn-5827-git-tagging-workflow` in **Code zone**. Code session `019f3b88`:
- **Status changed:** `ready_for_prompt` went from `true` (12:30 IDT) to `false` (12:41 IDT)
- This may mean Joseph sent a prompt and the session processed it
- **Git state:** still DIRTY (uncommitted changes on `jn-5827-git-tagging-workflow`)
- **No PR yet.** Implementation in progress.
- **Action:** Monitor — watch for PR creation or new ready_for_prompt state.

---

### 🆕 jn-5841 (JN-5841) — Plan Revision Awaiting Action

Worktree `jn-5841-agents-md-root` in **Ingest zone**:
- **Session 019f3ba0:** "Revise JN-5841 plan — PR #1588 merged, deduplicate content"
- **Status:** Idle, `ready_for_prompt: true`, last updated 12:58 IDT Jul 7
- **Git state:** CLEAN
- **Action:** Plan revision session ready. Review or trigger next session.

---

### 🆕 jn-5795 — Ready for Plan Phase

Worktree `jn-5795-upgrade-to-guidellm-v070` in **Ingest zone**:
- Design session done Jun 30 (143 msgs)
- Ready for `/implement:plan` trigger
- **Action:** Trigger plan session when Joseph is ready.

---

### 🟢 PR #1632 (JN-5719) — CLEAN, Ready to Merge

PR [#1632](https://github.com/Jounce-IO/jounce/pull/1632): `feat(jbenchmark): release diff layer (JN-5719)`
- **State:** MERGEABLE, REVIEW_REQUIRED
- **CI run 28775331183:** all-checks ✅ — all CI passing
- **Action:** READY TO MERGE. Propose merge.

---

### 🔴 PR #1606 (JN-5725) — CONFLICTING (Off-board)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- **State:** CONFLICTING as of 10:00 IDT Jul 2 (5+ days)
- **CI (run 28527509341):** all-checks ❌, e2e-smoke ❌, e2e-tests ❌
- **Jira:** JN-5725 shows Done
- **Action needed:** Rebase on main + fix e2e failures, or close PR.

---

### ❌ Jira Mismatches (3 active — MCP 401, unverifiable this run)

- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED 09:19 IDT Jul 6 → Jira **"Backlog"** (should be Done)
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 → Jira **"In Review"** (should be Done)
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED 08:10 IDT Jul 7 → Jira **"In Progress"** (should be Done)

---

### 🔴 fix-dashboard-syntax-error — ZOMBIE WORKTREE in Plan Zone

- **Status:** filesystem_status=failed ("fatal: invalid reference: origin/private-julie")
- **Created:** Jun 17 2026 (20+ days stale)
- **No PR, no Jira ticket**
- **Action needed:** Archive this worktree (proposal pending)

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (12+ days stale)
- NO ZONE, no sessions, no PR
- Still present but stale. If no longer needed, propose archive.

---

## Archived This Run

| Worktree | Reason | Archived At |
|---------|--------|------------|
| None | No new merges or closures detected | — |

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
