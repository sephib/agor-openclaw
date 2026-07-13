# Board State — jounce-workflow-ai

*Last updated: 2026-07-13 13:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jn-5842-jbenchmark-agents-md | **NO ZONE** | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | **✅ ALL PASSING** (run 29238532071) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) — Backlog | **🔴 CHANGES_REQUESTED** from markVaykhansky. CI FULLY GREEN: pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, e2e-smoke ✅, all-checks ✅. MERGEABLE. Must address review comments. |
| jn-5868 | **Publish** | [#1659](https://github.com/Jounce-IO/jounce/pull/1659) | **🟡 NEW run 29241018713 PENDING** | [JN-5868](https://redhat.atlassian.net/browse/JN-5868) — Backlog | OPEN, MERGEABLE. NEW CI run 29241018713 PENDING (new push likely). e2e-api ✅, integration ✅ early. pre-commit/tox/e2e-smoke still running. Depends on jn-5867 merging first. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — Backlog | Plan done ~23:06 IDT Jul 8. **Zone mismatch persists** (still Ingest, Day 12). Propose: move to Code + trigger /implement:code. |
| jn-5871 | **Code** | — | — | [JN-5871](https://redhat.atlassian.net/browse/JN-5871) | Code done ~00:58 IDT Jul 9. SHA fc6e5f77 CLEAN. **Zone mismatch persists** (still Code, should be Verify, Day 12). |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | "continuew" session IDLE ready_for_prompt:FALSE. SHA 16ec44ea (2 commits). Needs: generate 24 configs, rebase main, create PR. Fork a new session to continue. |
| jn-5870 | **Publish** | [#1656 DRAFT](https://github.com/Jounce-IO/jounce/pull/1656) | **🔴 pre-commit ❌** (UNCHANGED) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | **NOW CONFLICTING** (was MERGEABLE). DRAFT + pre-commit ❌. Double regression. |
| jn-5867 | **Publish** | [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | **🔴 pre-commit ❌ + e2e-api ❌** (run 29238852823 — NEW) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) — Backlog | **REGRESSION**: NEW CI run 29238852823 COMPLETE — pre-commit ❌ STILL + **e2e-api NOW FAILING** (was ✅). tox/integration ✅. REVIEW_REQUIRED. Cascade blocker — getting worse. |
| jn-5869 | **Publish** | [#1657](https://github.com/Jounce-IO/jounce/pull/1657) | **🔴 pre-commit ❌** (run 29238446686 — NEW) | [JN-5869](https://redhat.atlassian.net/browse/JN-5869) | NEW CI run 29238446686 COMPLETE — pre-commit ❌ STILL. e2e-api ✅, e2e-smoke ✅. UNKNOWN mergeable (was CONFLICTING). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 18+ days with no session or PR. |
| ~~jn-5874-values-prd-image-tags~~ | **ARCHIVED** | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) MERGED **12:10 IDT Jul 13** | ALL PASS ✅ | [JN-5874](https://redhat.atlassian.net/browse/JN-5874) — **Backlog** ⚠️ | **🎉 PR #1662 MERGED** — Worktree **ARCHIVED 12:32 IDT Jul 13**. JN-5874 Jira still Backlog → **needs Done!** |
| ~~jn-5401-runner-subcommands~~ | **ARCHIVED** | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) MERGED **17:12 IDT Jul 12** | ALL PASS ✅ | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) — **Backlog** ⚠️ | PR MERGED. ARCHIVED. JN-5401 Jira still Backlog → **needs Done!** |
| ~~jn-5841-agents-md-root~~ | **ARCHIVED** | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) MERGED 14:45 IDT Jul 12 | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) — **Done ✅** | PR MERGED. ARCHIVED 16:00 IDT Jul 12. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ CONFLICTING | 🔴 CONFLICTING | 🔴 CONFLICTING 10+ days. Needs rebase + fix e2e or close PR. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | 🔴 **run 29234035509** — e2e-product ❌ + e2e-tests ❌. pre-commit ✅. bake ✅. | OPEN | e2e-product ❌ + e2e-tests ❌ STILL FAILING (unchanged). MERGEABLE but blocked on e2e. |

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
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **Backlog** | ❌ Update Jira → Done |
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED 14:27 IDT Jul 12 | **Backlog** | ❌ Update Jira → Done |
| ~~[JN-5445](https://redhat.atlassian.net/browse/JN-5445)~~ | ~~[#1647](https://github.com/Jounce-IO/jounce/pull/1647)~~ | MERGED Jul 8 | **Done ✅** | ✅ RESOLVED |

*5 mismatches (unchanged from 12:32 IDT run). Jira MCP 401 — use acli.*

---

## Key Changes Since Last Run (13:00 IDT Jul 13 — delta from 12:32 IDT Jul 13)

| What observed | Status |
|---|---|
| **🟢 #1658 CI FULLY GREEN** | Run 29238532071 COMPLETE — ALL PASS: pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, e2e-smoke ✅, all-checks ✅. e2e-smoke was PENDING last run — now confirmed ✅. Ready for review response. |
| **🟡 #1659 NEW CI run 29241018713 PENDING** | New CI run (larger run number — likely new push). e2e-api ✅, integration ✅ early. pre-commit/tox/e2e-smoke still running. |
| **🟡 #1638 IMPROVED** | NEW CI run 29239468257 — pre-commit ✅, tox ✅, e2e-api ✅, e2e-smoke ✅, bake ✅. e2e-product PENDING (was ❌). Significant improvement. |
| **#1655 UNCHANGED** | Run 29238852823: pre-commit ❌, e2e-api ❌. Still cascade blocker. |
| **#1656 UNCHANGED** | CONFLICTING + DRAFT + pre-commit ❌. No new push. |
| **#1657 UNCHANGED** | MERGEABLE, pre-commit ❌ (run 29238446686). |

---

## Attention Items

### 🎉 #1662 (jn-5874) — MERGED ✅ — ARCHIVED

PR [#1662](https://github.com/Jounce-IO/jounce/pull/1662): "fix(helm): add missing image.tag entries to values-prd.yaml (JN-5874)"
- **MERGED 12:10 IDT Jul 13** — all CI passed.
- Worktree **ARCHIVED 12:32 IDT Jul 13** ✅ (autonomous archive — PR MERGED).
- **Action:** Update JN-5874 Jira → Done.

---

### 🔴 #1655 (jn-5867) — CI REGRESSION: e2e-api NOW FAILING

PR [#1655](https://github.com/Jounce-IO/jounce/pull/1655): "feat(jbenchmark): add Platform enum and refactor ClusterConfig for IBM support"
- **NEW CI run 29238852823 COMPLETE**: pre-commit ❌ STILL + **e2e-api ❌** (was ✅ in previous run). tox ✅, integration ✅.
- This is a regression — the previous run showed tox/integration/e2e-api ✅. New push broke e2e-api.
- REVIEW_REQUIRED + MERGEABLE.
- **Action:** Fix pre-commit AND investigate e2e-api regression. This is the cascade blocker for jn-5868/jn-5869/jn-5870.

---

### 🟢 #1658 (jn-5842) — CI FULLY GREEN (run 29238532071)

PR [#1658](https://github.com/Jounce-IO/jounce/pull/1658): "docs(jbenchmark): add app-level AGENTS.md"
- **CI FULLY GREEN** (run 29238532071): pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, **e2e-smoke ✅**, all-checks ✅.
- **Still CHANGES_REQUESTED** from markVaykhansky — review comments need addressing.
- MERGEABLE.
- **Action:** Address markVaykhansky review comments → push → re-request review.

---

### 🔴 #1656 (jn-5870) — NOW CONFLICTING (new regression)

PR [#1656](https://github.com/Jounce-IO/jounce/pull/1656): "feat(jbenchmark): add cluster selection CLI"
- **NOW CONFLICTING** (was MERGEABLE at 12:02 IDT). DRAFT + pre-commit ❌.
- **Action:** Rebase on main + fix pre-commit + undraft.

---

### 🔴 #1657 (jn-5869) — pre-commit ❌ STILL (new CI run)

PR [#1657](https://github.com/Jounce-IO/jounce/pull/1657): "feat(jbenchmark): add IBM cluster connection support (JN-5869)"
- NEW CI run 29238446686 COMPLETE — pre-commit ❌ STILL. e2e-api ✅, e2e-smoke ✅.
- UNKNOWN mergeable (was CONFLICTING — may have been rebased).
- **Action:** Fix pre-commit.

---

### 🔴 Jira Mismatches (5 active — JN-5874 newly added)

**Merged PRs not reflected in Jira (5):**
- [JN-5874](https://redhat.atlassian.net/browse/JN-5874): PR [#1662](https://github.com/Jounce-IO/jounce/pull/1662) MERGED 12:10 IDT Jul 13 → Jira **"Backlog"** (NEW)
- [JN-5401](https://redhat.atlassian.net/browse/JN-5401): PR [#1654](https://github.com/Jounce-IO/jounce/pull/1654) MERGED 17:12 IDT Jul 12 → Jira **"Backlog"**
- [JN-5717](https://redhat.atlassian.net/browse/JN-5717): PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631) MERGED → Jira **"Backlog"**
- [JN-5546](https://redhat.atlassian.net/browse/JN-5546): PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588) MERGED → Jira **"In Progress"**
- [JN-5827](https://redhat.atlassian.net/browse/JN-5827): PR [#1648](https://github.com/Jounce-IO/jounce/pull/1648) MERGED 14:27 IDT Jul 12 → Jira **"Backlog"**

---

### 🟡 jn-5868 — #1659 NEW CI run PENDING (29241018713)

PR [#1659](https://github.com/Jounce-IO/jounce/pull/1659):
- NEW CI run 29241018713 PENDING (new push likely). e2e-api ✅, integration ✅ early. pre-commit/tox/e2e-smoke still running.
- MERGEABLE. Depends on jn-5867 (#1655) merging first.
- **Action:** Await CI results; fix pre-commit if it fails again (after jn-5867 merges).

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 12)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Action:** Move to Code zone + trigger /implement:code.

---

### ✅ jn-5871 — Code Done, Wrong Zone (Day 12)

- 4 commits ahead. SHA fc6e5f77 CLEAN.
- **Action:** Move to Verify zone + trigger /implement:validate.

---

### 🔄 jn-5824-benchmark-run-configs — Waiting for direction

- "continuew" session IDLE **ready_for_prompt:FALSE**.
- **Action:** Fork a new session to generate 24 configs, rebase on main, create PR.

---

### 🟡 #1638 (off-board) — IMPROVED (NEW run 29239468257, e2e-product PENDING)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites"
- NEW CI run 29239468257: pre-commit ✅, tox ✅, e2e-api ✅, e2e-smoke ✅, bake ✅. **e2e-product PENDING** (was ❌ in prior runs).
- MERGEABLE. Await e2e-product result.

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (18+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run (12:32 IDT Jul 13)

| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| jn-5874-values-prd-image-tags | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | PR MERGED 12:10 IDT Jul 13 | 12:32 IDT Jul 13 |
| jn-5401-runner-subcommands | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | PR MERGED 17:12 IDT Jul 12 — archived prior session | ~17:12 IDT Jul 12 |
| jn-5841-agents-md-root | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | PR MERGED 14:45 IDT Jul 12 | 16:00 IDT Jul 12 |
| jn-5827-git-tagging-workflow | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | PR MERGED 14:27 IDT Jul 12 | 14:30 IDT Jul 12 |

---

## Recently Merged (2026-07-13 / 2026-07-12 / 2026-07-08 / 2026-07-07 / 2026-07-06)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
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
