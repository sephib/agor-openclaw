# Board State — jounce-workflow-ai

*Last updated: 2026-07-14 10:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT + UNKNOWN; frozen since Jun 14 |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jn-5842-jbenchmark-agents-md | **NO ZONE** | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | **✅ ALL CI GREEN** (run 29312738364 COMPLETE — e2e-smoke ✅ PASSED) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) — Backlog | **✅ ALL CI GREEN. MERGEABLE.** e2e-smoke completed PASS this run. reviewDecision cleared. |
| jn-5868 | **Publish** | [#1659](https://github.com/Jounce-IO/jounce/pull/1659) | **🔴 pre-commit ❌ FAIL** (run 29313293534 — tox modified files) | [JN-5868](https://redhat.atlassian.net/browse/JN-5868) — Backlog | **🔴 REGRESSION — new CI run 29313293534: pre-commit ❌, all-checks ❌ FAIL.** Was ALL CI GREEN (run 29254605349). Tox hook modified files. Needs new push. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — Backlog | Plan done ~23:06 IDT Jul 8. **Zone mismatch persists** (still Ingest, Day 14). Propose: move to Code + trigger /implement:code. |
| jn-5871 | **Code** | — | — | [JN-5871](https://redhat.atlassian.net/browse/JN-5871) | Code done ~00:58 IDT Jul 9. SHA fc6e5f77 CLEAN. **Zone mismatch persists** (still Code, should be Verify, Day 14). |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | "continuew" session IDLE ready_for_prompt:FALSE. SHA 16ec44ea (2 commits). Needs: generate 24 configs, rebase main, create PR. |
| jn-5870 | **Publish** | [#1656 DRAFT](https://github.com/Jounce-IO/jounce/pull/1656) | **🔴 DRAFT CONFLICTING** | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | **DRAFT + CONFLICTING** (unchanged). Rebase on main + fix pre-commit + undraft. |
| jn-5867 | **Publish** | [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | **⚠️ OLD CI GREEN** (run 29252812787) — but now **CONFLICTING** | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) — Backlog | **🔴 NOW CONFLICTING** — was MERGEABLE+GREEN at last successful run (18:00 IDT Jul 13). Something merged into main overnight. Needs rebase + new CI run. Cascade chain head **BLOCKED**. |
| jn-5869 | **Publish** | [#1657](https://github.com/Jounce-IO/jounce/pull/1657) | **✅ ALL PASSING** (run 29313871650 — NEW; was 29255496217) | [JN-5869](https://redhat.atlassian.net/browse/JN-5869) | **✅ ALL CI GREEN. MERGEABLE.** New CI run confirms green. After #1655 merges. |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 19+ days with no session or PR. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ UNKNOWN | 🔴 UNKNOWN | 🔴 CONFLICTING 11+ days. Needs rebase + fix e2e or close PR. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **⏳ NEW RUN PENDING** (run 29314599070: e2e-api ⏳, integration ⏳, pre-commit ⏳, tox ⏳) | **OPEN, MERGEABLE** | **NEW CI RUN 29314599070 STARTED** — atlas-validate ✅, bake ✅. e2e-api/integration/pre-commit/tox PENDING. Previous run 29312605152 was e2e-api ❌. |

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
| [JN-5851](https://redhat.atlassian.net/browse/JN-5851) | Backlog | Implement v0.7.0 Container Image & Argo Integration |
| [JN-5849](https://redhat.atlassian.net/browse/JN-5849) | Backlog | [CI] Add CI drift detection for AGENTS.md staleness |
| [JN-5848](https://redhat.atlassian.net/browse/JN-5848) | Backlog | [QE] Cross-tool validation of hierarchical AGENTS.md |
| [JN-5847](https://redhat.atlassian.net/browse/JN-5847) | Backlog | [DEV] Refine existing tests/e2e/AGENTS.md |
| [JN-5846](https://redhat.atlassian.net/browse/JN-5846) | Backlog | [DEV] Write peripheral app AGENTS.md files |
| [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | Backlog | [DEV] Write Helm and CI/CD AGENTS.md files |
| [JN-5844](https://redhat.atlassian.net/browse/JN-5844) | Backlog | [DEV] Write service/lib/sql domain AGENTS.md files |
| [JN-5826](https://redhat.atlassian.net/browse/JN-5826) | Backlog | [DEV] Execute and monitor benchmark runs on IBM cluster |
| [JN-5825](https://redhat.atlassian.net/browse/JN-5825) | Backlog | [DOCS] Update apps/jbenchmark/README.md for IBM cluster |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **In Review** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **Backlog** | ❌ Update Jira → Done |
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED 14:27 IDT Jul 12 | **Backlog** | ❌ Update Jira → Done |

*6 mismatches (unchanged). Jira MCP 401 — use acli.*

---

## Key Changes Since Last Run (10:30 IDT Jul 14 — delta from 10:00 IDT Jul 14)

| What observed | Status |
|---|---|
| **#1655 (jn-5867) STILL CONFLICTING** | No change. Old CI run 29252812787 still green but PR is CONFLICTING. Needs rebase. **Cascade chain head BLOCKED.** |
| **#1657 (jn-5869) — NEW CI RUN GREEN** | New CI run 29313871650: ALL GREEN. Supersedes run 29255496217. MERGEABLE. Awaits #1655. |
| **🔴 #1659 (jn-5868) — REGRESSION** | **New CI run 29313293534: pre-commit ❌ FAIL (tox modified files), all-checks ❌.** Was ALL CI GREEN (run 29254605349). Needs new push after fixing tox-modified file. |
| **✅ #1658 (jn-5842) — NOW ALL CI GREEN** | Run 29312738364 COMPLETE: e2e-smoke ✅ PASSED. All checks pass. **FULLY MERGEABLE.** Was e2e-smoke ⏳ PENDING. |
| **#1638 (off-board) — NEW CI RUN PENDING** | New run 29314599070 started (e2e-api ⏳, integration ⏳, pre-commit ⏳, tox ⏳). atlas-validate ✅, bake ✅. Previous run 29312605152 was e2e-api ❌. |
| **No new merges** | Board composition unchanged. |

---

## Attention Items

### 🔴 #1655 (jn-5867) — NOW CONFLICTING — CASCADE BLOCKER REINSTATED

PR [#1655](https://github.com/Jounce-IO/jounce/pull/1655): "feat(jbenchmark): add Platform enum and refactor ClusterConfig for IBM support"
- **NOW CONFLICTING** — was MERGEABLE+ALL GREEN as of 18:00 IDT Jul 13. Something landed in main overnight.
- Old CI (run 29252812787) still shows green, but won't re-run until rebased.
- **Cascade impact:** #1657 and #1659 cannot merge until #1655 is rebased and merges.
- **Action:** **REBASE on main + re-trigger CI. Priority #1.**

---

### ✅ #1657 (jn-5869) — ALL GREEN (new run confirms), Awaiting #1655 Rebase

PR [#1657](https://github.com/Jounce-IO/jounce/pull/1657): "feat(jbenchmark): add IBM cluster connection support"
- **NEW CI RUN 29313871650 (10:30 IDT Jul 14):** all-checks ✅, e2e-api ✅, e2e-smoke ✅, integration ✅, nox ✅, tox ✅, pre-commit ✅ — **ALL PASS**
- Supersedes run 29255496217 (same result — green). MERGEABLE.
- **Action:** Merge after #1655 rebase + merge.

---

### 🔴 #1659 (jn-5868) — REGRESSION: pre-commit ❌ FAIL

PR [#1659](https://github.com/Jounce-IO/jounce/pull/1659): "feat(jbenchmark): add ClusterRegistry loader and clusters.json"
- **NEW CI RUN 29313293534 (10:30 IDT Jul 14) — FAILING:**
  - pre-commit ❌ FAIL, all-checks ❌ FAIL
  - Failure: tox hook ran and **modified files** — `"tox (tests)......Failed — files were modified by this hook"`
  - All other checks pass: e2e-api ✅, e2e-smoke ✅, integration ✅, nox ✅, tox ✅
- Was ALL CI GREEN (run 29254605349) — this is a regression likely caused by a rebase or merge push
- **Action:** Diagnose which files tox modified. Push a fix (accept generated file changes) to re-trigger CI.

---

### 🟡 #1638 (off-board) — NEW CI RUN PENDING

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites"
- **NEW CI RUN 29314599070 started** (10:30 IDT Jul 14) — currently PENDING:
  - atlas-validate ✅, bake ✅
  - e2e-api ⏳, integration ⏳, pre-commit ⏳, tox ⏳ — all pending
- Previous run 29312605152 failed e2e-api ❌. New run may fix it if someone pushed a patch.
- **Action:** Wait for run 29314599070 to complete. Check result next heartbeat.

---

### ✅ #1658 (jn-5842) — ALL CI GREEN, FULLY MERGEABLE

PR [#1658](https://github.com/Jounce-IO/jounce/pull/1658): "docs(jbenchmark): add app-level AGENTS.md"
- **ALL CI GREEN** — run 29312738364 COMPLETE (10:30 IDT Jul 14):
  - all-checks ✅, e2e-smoke ✅, e2e-api ✅, integration ✅, nox ✅, tox ✅, pre-commit ✅
- reviewDecision: empty (cleared — was CHANGES_REQUESTED from markVaykhansky)
- **MERGEABLE**
- **Action:** Can merge now — no blockers. (This is an AGENTS.md docs PR — no ordering constraint with cascade chain.)

---

### 🔴 #1656 (jn-5870) — DRAFT + CONFLICTING (unchanged)

PR [#1656](https://github.com/Jounce-IO/jounce/pull/1656): "feat(jbenchmark): add cluster selection CLI"
- **DRAFT + CONFLICTING** (unchanged)
- **Action:** Rebase on main + fix pre-commit + undraft.

---

### 🔴 Jira Mismatches (6 active — unchanged)

**Merged PRs not reflected in Jira (6):**
- [JN-5877](https://redhat.atlassian.net/browse/JN-5877): PR [#1663](https://github.com/Jounce-IO/jounce/pull/1663) MERGED → Jira **"In Review"**
- [JN-5874](https://redhat.atlassian.net/browse/JN-5874): PR [#1662](https://github.com/Jounce-IO/jounce/pull/1662) MERGED → Jira **"Backlog"**
- [JN-5401](https://redhat.atlassian.net/browse/JN-5401): PR [#1654](https://github.com/Jounce-IO/jounce/pull/1654) MERGED → Jira **"Backlog"**
- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED → Jira **"Backlog"**
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED → Jira **"In Progress"**
- [JN-5827](https://redhat.atlassian.net/browse/JN-5827): PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648) MERGED → Jira **"Backlog"**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 14)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Action:** Move to Code zone + trigger /implement:code.

---

### ✅ jn-5871 — Code Done, Wrong Zone (Day 14)

- 4 commits ahead. SHA fc6e5f77 CLEAN.
- **Action:** Move to Verify zone + trigger /implement:validate.

---

### 🔄 jn-5824-benchmark-run-configs — Waiting for direction

- "continuew" session IDLE **ready_for_prompt:FALSE**.
- **Action:** Fork a new session to generate 24 configs, rebase on main, create PR.

---

### ⚠️ Overnight Session Failures (4 consecutive confirmed — no new failures since 09:00 IDT)

Sessions at 19:00 IDT Jul 13, 21:00 IDT Jul 13, 03:00 IDT Jul 14, and 06:00 IDT Jul 14 all failed.
- 4th failure: session 019f5e92 (Weekday Overnight — 2026-07-14T03:00:00.000Z = 06:00 IDT Jul 14) — confirmed failed.
- Daytime sessions 09:00, 09:30, 10:00, 10:30 IDT Jul 14 all successful.
- **Action:** Investigate why overnight sessions are failing. Flag for human review.

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (19+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run

None.

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| jn-5877-api-server-replicas | [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | PR MERGED 15:16 IDT Jul 13 | **15:30 IDT Jul 13** |
| jn-5874-values-prd-image-tags | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | PR MERGED 12:10 IDT Jul 13 | 12:32 IDT Jul 13 |
| jn-5401-runner-subcommands | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | PR MERGED 17:12 IDT Jul 12 | ~17:12 IDT Jul 12 |
| jn-5841-agents-md-root | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | PR MERGED 14:45 IDT Jul 12 | 16:00 IDT Jul 12 |
| jn-5827-git-tagging-workflow | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | PR MERGED 14:27 IDT Jul 12 | 14:30 IDT Jul 12 |

---

## Recently Merged (2026-07-13 / 2026-07-12 / 2026-07-08 / 2026-07-07 / 2026-07-06)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | [JN-5877](https://redhat.atlassian.net/browse/JN-5877) | **15:16 IDT Jul 13** 🎉 | jn-5877-api-server-replicas — **ARCHIVED 15:30 IDT Jul 13** ✅. **JN-5877 Jira → needs Done!** |
| [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | [JN-5874](https://redhat.atlassian.net/browse/JN-5874) | **12:10 IDT Jul 13** 🎉 | jn-5874-values-prd-image-tags — **ARCHIVED 12:32 IDT Jul 13** ✅. **JN-5874 Jira still "Backlog" → needs Done!** |
| [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | **17:12 IDT Jul 12** 🎉 | jn-5401-runner-subcommands — ARCHIVED. **JN-5401 Jira still "Backlog" → needs Done!** |
| [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | **14:45 IDT Jul 12** | jn-5841-agents-md-root — **ARCHIVED 16:00 IDT Jul 12** ✅ |
| [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | **14:27 IDT Jul 12** | jn-5827-git-tagging-workflow — **ARCHIVED 14:30 IDT** |
| [#1632](https://github.com/Jounce-IO/jounce/pull/1632) | [JN-5719](https://redhat.atlassian.net/browse/JN-5719) | **17:10 IDT Jul 8** | Off-board PR — no worktree. |
| [#1647](https://github.com/Jounce-IO/jounce/pull/1647) | [JN-5445](https://redhat.atlassian.net/browse/JN-5445) | 15:03 IDT Jul 8 | Off-board PR — no worktree. JN-5445 Jira **Done ✅**. |
| [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | 08:10 IDT Jul 7 | jn-5546-...-3 (already deleted from Agor) |
| [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | 09:19 IDT Jul 6 | Off-board PR — no worktree |
| [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | 09:16 IDT Jul 1 | Archived 09:21 IDT Jul 1 |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
