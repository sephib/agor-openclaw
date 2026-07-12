# Board State — jounce-workflow-ai

*Last updated: 2026-07-12 19:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jn-5842-jbenchmark-agents-md | **NO ZONE** | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | **CONFLICTING** (new conflict — #1654 merged into main) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) — Backlog | **🔴 CHANGES_REQUESTED** from markVaykhansky. **NEW: now CONFLICTING** (was MERGEABLE — #1654 merge updated main). Must fix conflict + address review. |
| jn-5868 | **Publish** | [#1659 DRAFT](https://github.com/Jounce-IO/jounce/pull/1659) | CONFLICTING | [JN-5868](https://redhat.atlassian.net/browse/JN-5868) — Backlog | PR #1659 DRAFT CONFLICTING — needs rebase on main (or jn-5867). |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — Backlog | Plan done ~23:06 IDT Jul 8. **Zone mismatch persists** (still Ingest, Day 6). Propose: move to Code + trigger /implement:code. |
| jn-5871 | **Code** | — | — | [JN-5871](https://redhat.atlassian.net/browse/JN-5871) | Code done ~00:58 IDT Jul 9. SHA fc6e5f77 CLEAN. **Zone mismatch persists** (still Code, should be Verify, Day 6). |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | "continuew" session IDLE ready_for_prompt:FALSE. SHA 16ec44ea (2 commits). Needs: generate 24 configs, rebase main, create PR. Fork a new session to continue. |
| jn-5870 | **Publish** | [#1656 DRAFT](https://github.com/Jounce-IO/jounce/pull/1656) | CONFLICTING | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | PR #1656 DRAFT CONFLICTING. 5 commits ahead. Needs rebase + undraft. |
| jn-5867 | **Publish** | [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | **🟡 run 29198902176: pre-commit ❌ only** (e2e-api ✅ NOW PASS, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, e2e-tests PENDING) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) — Backlog | **🆕 CI IMPROVED** — e2e-api now ✅ PASS (was ❌). Only **pre-commit ❌** remains as blocker. e2e-tests aggregator still PENDING. |
| jn-5869 | **Publish** | [#1657 DRAFT](https://github.com/Jounce-IO/jounce/pull/1657) | **✅ MERGEABLE** (was CONFLICTING) | [JN-5869](https://redhat.atlassian.net/browse/JN-5869) | **🆕 PR #1657 now MERGEABLE** — conflict resolved. Still DRAFT. Needs undraft. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 17+ days with no session or PR. |
| ~~jn-5401-runner-subcommands~~ | **ARCHIVED** | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) MERGED **17:12 IDT Jul 12** | ALL PASS ✅ | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) — **Backlog** ⚠️ | **🎉 PR #1654 MERGED 17:12 IDT** — CI all pass (run 29195415951). Worktree already archived. JN-5401 Jira still Backlog → **needs Done!** |
| ~~jn-5841-agents-md-root~~ | **ARCHIVED** | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) MERGED 14:45 IDT | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) — **Done ✅** | PR MERGED. **JN-5841 now Done in Jira** (confirmed 16:30 IDT). ARCHIVED 16:00 IDT Jul 12. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ CONFLICTING | 🔴 CONFLICTING | 🔴 CONFLICTING 10+ days. Needs rebase + fix e2e or close PR. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) (likely) | 🔴 **run 29193793106 — e2e-product ❌** (pre-commit ✅ FIXED from regression, e2e-api ✅, e2e-smoke ✅) | OPEN | **pre-commit REGRESSION FIXED** — pre-commit now ✅. New blocker: **e2e-product ❌**. MERGEABLE. Needs e2e-product fix. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Waiting/Blocked | Refactor run_jbenchmark script to support redesign flow |
| [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | Backlog | DAL extensions for dashboard queries (worktree in BLOCKED zone) |
| [JN-5462](https://redhat.atlassian.net/browse/JN-5462) | Backlog | Agentic Jira → PR workflow — Forge |
| [JN-5843](https://redhat.atlassian.net/browse/JN-5843) | Backlog | [CI] Remove ties infrastructure entirely + Cursor AGENTS.md auto-generation |
| [JN-5852](https://redhat.atlassian.net/browse/JN-5852) | Backlog | Implement v0.7.0 Report Ingestion |
| [JN-5851](https://redhat.atlassian.net/browse/JN-5851) | Backlog | Implement v0.7.0 Container Image & Argo Integration — **NEW** |
| [JN-5849](https://redhat.atlassian.net/browse/JN-5849) | Backlog | [CI] Add CI drift detection for AGENTS.md staleness — **NEW** |
| [JN-5848](https://redhat.atlassian.net/browse/JN-5848) | Backlog | [QE] Cross-tool validation of hierarchical AGENTS.md — **NEW** |
| [JN-5847](https://redhat.atlassian.net/browse/JN-5847) | Backlog | [DEV] Refine existing tests/e2e/AGENTS.md — **NEW** |
| [JN-5846](https://redhat.atlassian.net/browse/JN-5846) | Backlog | [DEV] Write peripheral app AGENTS.md files — **NEW** |
| [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | Backlog | [DEV] Write Helm and CI/CD AGENTS.md files — **NEW** |
| [JN-5844](https://redhat.atlassian.net/browse/JN-5844) | Backlog | [DEV] Write service/lib/sql domain AGENTS.md files — **NEW** |
| [JN-5826](https://redhat.atlassian.net/browse/JN-5826) | Backlog | [DEV] Execute and monitor benchmark runs on IBM cluster — **NEW** |
| [JN-5825](https://redhat.atlassian.net/browse/JN-5825) | Backlog | [DOCS] Update apps/jbenchmark/README.md for IBM cluster — **NEW** |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| ~~[JN-5841](https://redhat.atlassian.net/browse/JN-5841)~~ | ~~[#1649](https://github.com/Jounce-IO/jounce/pull/1649)~~ | ~~MERGED~~ | **Done ✅** | ✅ RESOLVED — Jira updated to Done (confirmed 16:30 IDT Jul 12) |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **Backlog** | ❌ Update Jira → Done 🆕 |
| [JN-5445](https://redhat.atlassian.net/browse/JN-5445) | [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | MERGED 15:03 IDT Jul 8 | **In Progress** | ❌ Update Jira → Done |
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED 14:27 IDT Jul 12 | **Backlog** | ❌ Update Jira → Done |
| [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | OPEN — MERGEABLE (rebased) | **Backlog** | ⚠️ Should be → In Review |

*6 mismatches — JN-5401 upgraded from "should be In Review" → "should be Done" (PR merged!). Jira MCP 401 — using acli.*

---

## Key Changes Since Last Run (19:00 IDT Jul 12 — delta from 18:30 IDT Jul 12)

| What observed | Status |
|---|---|
| **🆕 PR #1655 CI IMPROVED** — e2e-api now ✅ | Run 29198902176: pre-commit ❌ only. e2e-api ✅ (was ❌), e2e-smoke ✅, integration ✅, tox ✅, nox ✅. Only pre-commit blocks now. |
| **🔴 PR #1638 CI WORSENED** — e2e-smoke ❌ FAIL | Run 29196923676 completed: e2e-smoke ❌ FAIL (was PENDING last run). All other checks pass. |
| **PR #1657 mergeable: UNKNOWN** | Was MERGEABLE at 18:30 IDT — GitHub API may be slow. Still DRAFT, no CI triggered yet. |
| **PR #1659 mergeable: UNKNOWN** | Was CONFLICTING — may be resolving. Still DRAFT. |
| **No new merges** | Nothing since #1654 at 17:12 IDT. |
| **jn-5865, jn-5871 zone mismatches PERSIST** | Day 4+ still wrong zone. |

---

## Attention Items

### 🔴 JN-5401 → Done in Jira (PR #1654 MERGED!)

PR [#1654](https://github.com/Jounce-IO/jounce/pull/1654): "feat(jbenchmark): add subcommands to runner" — **MERGED 17:12 IDT Jul 12**
- CI ALL PASS (run 29195415951). Worktree jn-5401-runner-subcommands archived.
- **JN-5401 Jira still "Backlog" → needs Done!**
- **Action:** Update JN-5401 Jira → Done.

---

### 🟡 #1655 (jn-5867) — pre-commit ❌ only (e2e-api now ✅)

PR [#1655](https://github.com/Jounce-IO/jounce/pull/1655): "feat(jbenchmark): Platform enum + ClusterConfig refactor"
- **CI improved** (run 29198902176): **e2e-api ✅ PASS** (was ❌ last run). Only pre-commit ❌ remains.
- e2e-smoke ✅, integration ✅, tox ✅, nox ✅, atlas-validate ✅. e2e-tests aggregator PENDING.
- **Action:** Diagnose and fix pre-commit failure. One failing check away from merge-ready.

---

### 🔴 jn-5842 — PR #1658 CHANGES_REQUESTED + now CONFLICTING

PR [#1658](https://github.com/Jounce-IO/jounce/pull/1658): "docs(jbenchmark): add app-level AGENTS.md with benchmark platform context"
- **CHANGES_REQUESTED** from markVaykhansky (15:41 IDT Jul 12) — unchanged.
- **NEW: now CONFLICTING** — #1654 merge updated main, introduced conflict.
- **Action:** Fix conflict first, then address markVaykhansky's review comments, re-request review.

---

### 🔴 #1638 (off-board) — e2e-smoke ❌ FAIL

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites"
- **Run 29196923676 COMPLETED**: e2e-smoke ❌ FAIL (was PENDING — now complete and failed). all-checks ❌.
- Other checks: pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, bake ✅, nox ✅. MERGEABLE.
- **Action:** Diagnose e2e-smoke failure. This was the last pending check — now a new blocker.

---

### 🆕 jn-5869 — PR #1657 now MERGEABLE

PR [#1657](https://github.com/Jounce-IO/jounce/pull/1657): "feat(jbenchmark): add IBM cluster connection support"
- **Now MERGEABLE** (was CONFLICTING — conflict resolved!). Still DRAFT.
- **Action:** Undraft PR #1657. Address any remaining dirty worktree issues.

---

### 🔴 jn-5870 — PR #1656 DRAFT CONFLICTING

PR [#1656](https://github.com/Jounce-IO/jounce/pull/1656): "feat(jbenchmark): add cluster selection CLI and config loading"
- DRAFT, CONFLICTING. 5 commits ahead.
- **Action:** Rebase on main, undraft PR.

---

### 🆕 jn-5868 — PR #1659 DRAFT CONFLICTING — needs rebase

PR [#1659](https://github.com/Jounce-IO/jounce/pull/1659): "feat(jbenchmark): add ClusterRegistry loader and clusters.json"
- DRAFT, CONFLICTING. Needs rebase on jn-5867 (Platform enum dependency).
- **Action:** Rebase on jn-5867 or main once jn-5867 merges.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done)

Worktree `jn-5865-ibm-cluster-connect` (Ingest zone):
- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- 4+ days in wrong zone.
- **Action:** Move to Code zone + trigger /implement:code.

---

### ✅ jn-5871 — Code Done, Wrong Zone

Worktree `jn-5871` (Code zone, code done):
- 4 commits ahead. SHA fc6e5f77 CLEAN.
- **Action:** Move to Verify zone + trigger /implement:validate.

---

### 🔄 jn-5824-benchmark-run-configs — Waiting for direction

Worktree `jn-5824-benchmark-run-configs` (Code zone):
- "continuew" session IDLE **ready_for_prompt:FALSE**.
- **Action:** Fork a new session to generate 24 configs, rebase on main, create PR.

---

### ❌ Jira Mismatches (6 active — same count, JN-5401 upgraded from "In Review" to "Done")

**Merged PRs not reflected in Jira (5):**
- [JN-5401](https://redhat.atlassian.net/browse/JN-5401): PR [#1654](https://github.com/Jounce-IO/jounce/pull/1654) MERGED 17:12 IDT Jul 12 → Jira **"Backlog"** (should be Done) 🆕
- [JN-5445](https://redhat.atlassian.net/browse/JN-5445): PR [#1647](https://github.com/Jounce-IO/jounce/pull/1647) MERGED → Jira **"In Progress"** (should be Done)
- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED → Jira **"Backlog"** (should be Done)
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED → Jira **"In Progress"** (should be Done)
- [JN-5827](https://redhat.atlassian.net/browse/JN-5827): PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648) MERGED 14:27 IDT Jul 12 → Jira **"Backlog"** (should be Done)

**Active PRs not reflected in Jira (1):**
- [JN-5867](https://redhat.atlassian.net/browse/JN-5867): PR [#1655](https://github.com/Jounce-IO/jounce/pull/1655) OPEN → Jira **"Backlog"** (should be In Review)

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (17+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run

| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| jn-5401-runner-subcommands | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | PR MERGED 17:12 IDT Jul 12 — worktree already archived (prior session) | ~17:12 IDT Jul 12 |
| jn-5841-agents-md-root | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | PR MERGED 14:45 IDT Jul 12 — branch found in Agor (NO ZONE, branchId 019f3308) | 16:00 IDT Jul 12 |
| jn-5827-git-tagging-workflow | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | PR MERGED 14:27 IDT Jul 12 | 14:30 IDT Jul 12 |

(Previous: jn-5780-add-jn-project archived 13:34 IDT Jul 6; fix-dashboard gone between 21:30–22:00 IDT Jul 7)

---

## Recently Merged (2026-07-12 / 2026-07-08 / 2026-07-07 / 2026-07-06)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | **17:12 IDT Jul 12** 🎉 | jn-5401-runner-subcommands — ARCHIVED. **JN-5401 Jira still "Backlog" → needs Done!** |
| [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | **14:45 IDT Jul 12** | jn-5841-agents-md-root — **ARCHIVED 16:00 IDT Jul 12** ✅ |
| [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | **14:27 IDT Jul 12** | jn-5827-git-tagging-workflow — **ARCHIVED 14:30 IDT** |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | **17:10 IDT Jul 8** | Off-board PR — no worktree. JN-5719 Jira "Backlog" → needs Done. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) | 15:03 IDT Jul 8 | Off-board PR — no worktree. JN-5445 Jira "In Progress" → needs Done. |
| [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | 08:10 IDT Jul 7 | jn-5546-...-3 (already deleted from Agor) |
| [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | 09:19 IDT Jul 6 | Off-board PR — no worktree |
| [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | 09:16 IDT Jul 1 | Archived 09:21 IDT Jul 1 |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
