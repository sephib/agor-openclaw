# Board State — jounce-workflow-ai

*Last updated: 2026-07-14 18:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT + UNKNOWN; frozen since Jun 14 |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jn-5844-service-lib-sql-agents-md | **Code** | — | — | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) | ✅ Code done (SHA 86fb06b1). Internal CR done 10:46 IDT. **Still no PR** — needs PR creation. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | **⏳ CI run 29343394531 — ALL PENDING** | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | **🟢 UNDRAFTED** since last run. PR now open (REVIEW_REQUIRED). New CI run in progress. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — Backlog | Plan done ~23:06 IDT Jul 8. **Zone mismatch persists** (still Ingest, Day 14+). Propose: move to Code + trigger /implement:code. |
| jn-5871 | **Code** | — | — | [JN-5871](https://redhat.atlassian.net/browse/JN-5871) | Code done ~00:58 IDT Jul 9. SHA fc6e5f77 CLEAN. **Zone mismatch persists** (still Code, should be Verify, Day 14+). |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: generate 24 configs, rebase main, create PR. |
| jn-5867 | **Publish** | [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | **🔴 pre-commit ❌ FAIL** — run 29329734574 | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) — Backlog | **🔴 DOUBLE-BLOCKED**: pre-commit ❌ FAIL + **CONFLICTING**. No new CI runs. Sibling "Plan GCP dev cluster" session IDLE. Last code: SHA 94055cfe (10:41 IDT). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 19+ days with no session or PR. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ UNKNOWN | 🔴 UNKNOWN | 🔴 CONFLICTING 11+ days. Needs rebase + fix e2e or close PR. |
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **⏳ run 29343027544 IN PROGRESS** — pre-commit ✅ bake ✅ integration ✅ tox ✅ nox ✅ atlas ✅ — e2e-api ⏳ pre-commit(2) ⏳ | **OPEN, MERGEABLE** | New CI run in progress. Prior run had e2e-smoke ❌ — watching for result. |

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
| [JN-5826](https://redhat.atlassian.net/browse/JN-5826) | Backlog | [DEV] Execute and monitor benchmark runs on IBM cluster |
| [JN-5825](https://redhat.atlassian.net/browse/JN-5825) | Backlog | [DOCS] Update apps/jbenchmark/README.md for IBM cluster |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5870](https://redhat.atlassian.net/browse/JN-5870)** | **[#1656](https://github.com/Jounce-IO/jounce/pull/1656)** | **MERGED 17:53 IDT Jul 14** | **UNKNOWN (Jira MCP 401)** | ❌ Update Jira → Done |
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED 13:29 IDT Jul 14** | **UNKNOWN (Jira MCP 401)** | ❌ Update Jira → Done |
| **[JN-5880](https://redhat.atlassian.net/browse/JN-5880)** | **[#1666](https://github.com/Jounce-IO/jounce/pull/1666)** | **MERGED 12:20 IDT Jul 14** | **UNKNOWN (Jira MCP 401)** | ❌ Update Jira → Done |
| **[JN-5879](https://redhat.atlassian.net/browse/JN-5879)** | **[#1665](https://github.com/Jounce-IO/jounce/pull/1665)** | **MERGED 10:48 IDT Jul 14** | **UNKNOWN (Jira MCP 401)** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **In Review** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **Backlog** | ❌ Update Jira → Done |
| [JN-5717](https://redhat.atlassian.net/browse/JN-5717) | [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | MERGED Jul 6 | **Backlog** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED 14:27 IDT Jul 12 | **Backlog** | ❌ Update Jira → Done |

*10 mismatches (+1 new: JN-5870). Jira MCP 401 — use acli to update.*

---

## Key Changes Since Last Run (18:00 IDT Jul 14 — delta from 17:30 IDT Jul 14)

| What observed | Status |
|---|---|
| **🎉 #1656 (jn-5870): MERGED at 17:53 IDT** | PR "feat(jbenchmark): add cluster selection CLI and config loading (JN-5870)" MERGED. Was showing pre-commit REGRESSION at 17:30 IDT — apparently the pre-commit fix was pushed and all CI passed. Moved to Recently Merged. JN-5870 Jira → needs Done. |
| **🟢 #1667 (jn-5845): UNDRAFTED — new CI run** | PR is no longer DRAFT (reviewDecision: REVIEW_REQUIRED). New CI run 29343394531 IN PROGRESS (all pending). Was DRAFT at 17:30 IDT. |
| **⏳ #1638 (off-board): New CI run 29343027544** | pre-commit ✅ bake ✅ integration ✅ tox ✅ nox ✅ atlas-validate ✅ — e2e-api ⏳ still running. Watching for result. |
| **🔴 #1655 (jn-5867): still DOUBLE-BLOCKED (unchanged)** | pre-commit ❌ FAIL + CONFLICTING. No new CI runs or pushes. |

---

## Attention Items

### 🎉 #1656 (jn-5870) — MERGED at 17:53 IDT — ⚠️ JN-5870 Jira needs Done

PR [#1656](https://github.com/Jounce-IO/jounce/pull/1656): "feat(jbenchmark): add cluster selection CLI and config loading (JN-5870)"
- MERGED at 17:53 IDT Jul 14 🎉
- jn-5870 worktree is not an Agor-registered branch — no agor_branches_archive possible (tracked manually only)
- **Action:** Update JN-5870 Jira ticket to Done via acli.

---

### 🟢 #1667 (jn-5845) — UNDRAFTED, CI Running

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- **NO LONGER DRAFT** (reviewDecision: REVIEW_REQUIRED, isDraft: false) — undrafted since 17:30 IDT
- New CI run 29343394531 IN PROGRESS (pre-commit, tox, integration, e2e-api all PENDING)
- **Action:** Wait for CI result.

---

### 🔴 #1655 (jn-5867) — DOUBLE-BLOCKED (pre-commit ❌ FAIL + CONFLICTING)

PR [#1655](https://github.com/Jounce-IO/jounce/pull/1655): "feat(jbenchmark): add Platform enum and remove gcloud from cluster prerequisites"
- pre-commit ❌ FAIL (run 29329734574). All functional tests ✅.
- **CONFLICTING** — needs rebase on main.
- Sibling session "Plan GCP dev cluster + --dev flag for JN-5867" now IDLE.
- **Action:** Rebase on main (fix conflicts), then fix pre-commit, push again.

---

### ⏳ #1638 (off-board JN-5725) — New CI run in progress

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites"
- New CI run 29343027544 in progress. pre-commit ✅ bake ✅ integration ✅ tox ✅ nox ✅ — e2e-api ⏳ PENDING.
- Prior run had e2e-smoke ❌ FAIL — watching for current result.
- State: OPEN, MERGEABLE.

---

### ⚠️ jn-5844 — Still No PR

**jn-5844-service-lib-sql-agents-md** ([JN-5844](https://redhat.atlassian.net/browse/JN-5844)):
- Code done (SHA 86fb06b1). Internal CR done 10:46 IDT. Still in Code zone, no PR.
- **Action:** Create PR creation session.

---

### 🔴 Jira Mismatches (10 active — +1 new JN-5870)

See table above. Jira MCP 401 — use `acli` to update.

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

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Action:** Fork a new session to generate 24 configs, rebase on main, create PR.

---

### ⚠️ Overnight Session Failures (4 consecutive — no new failures since 09:00 IDT)

Sessions at 19:00 IDT Jul 13, 21:00 IDT Jul 13, 03:00 IDT Jul 14, and 06:00 IDT Jul 14 all failed.
- Daytime sessions 09:00–18:00 IDT Jul 14 all successful.
- **Action:** Investigate why overnight sessions are failing. Flag for human review.

---

### ⚠️ jira-operations — Stale (NO ZONE)

- uid=249, last_used Jun 25 2026 (19+ days stale)
- NO ZONE, no sessions, no PR
- Propose archive if no longer needed.

---

## Archived This Run (18:00 IDT Jul 14)

**jn-5870** — PR [#1656](https://github.com/Jounce-IO/jounce/pull/1656) MERGED at 17:53 IDT Jul 14. ⚠️ Note: jn-5870 is NOT an Agor-registered branch — cannot archive via MCP. Removed from active tracking. Worktree remains on disk.

Previously archived this session:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jn-5869** | [#1657](https://github.com/Jounce-IO/jounce/pull/1657) | PR CLOSED 12:03 IDT Jul 14 | **12:08 IDT Jul 14** (pre-run) |
| **jn-5842-jbenchmark-agents-md** | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | PR MERGED 13:29 IDT Jul 14 | 13:30 IDT Jul 14 |
| **jn-5880-validate-tag-glob-fix** | [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | PR MERGED 12:20 IDT Jul 14 | 12:30 IDT Jul 14 |
| **jn-5868** | [#1659](https://github.com/Jounce-IO/jounce/pull/1659) | PR CLOSED 12:26 IDT Jul 14 | 12:30 IDT Jul 14 |
| jn-5879-justfile-skip-helm | [#1665](https://github.com/Jounce-IO/jounce/pull/1665) | PR MERGED 10:48 IDT Jul 14 | 11:30 IDT Jul 14 |
| jn-5877-api-server-replicas | [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | PR MERGED 15:16 IDT Jul 13 | 15:30 IDT Jul 13 |
| jn-5874-values-prd-image-tags | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | PR MERGED 12:10 IDT Jul 13 | 12:32 IDT Jul 13 |
| jn-5401-runner-subcommands | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | PR MERGED 17:12 IDT Jul 12 | ~17:12 IDT Jul 12 |
| jn-5841-agents-md-root | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | PR MERGED 14:45 IDT Jul 12 | 16:00 IDT Jul 12 |
| jn-5827-git-tagging-workflow | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | PR MERGED 14:27 IDT Jul 12 | 14:30 IDT Jul 12 |

---

## Recently Merged (2026-07-14 / 2026-07-13 / 2026-07-12 / 2026-07-08 / 2026-07-07)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | **17:53 IDT Jul 14** 🎉 | jn-5870 — not Agor-registered (no archive action). **JN-5870 Jira → needs Done!** |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) | **13:29 IDT Jul 14** 🎉 | jn-5842-jbenchmark-agents-md — **ARCHIVED 13:30 IDT Jul 14** ✅. **JN-5842 Jira → needs Done!** |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | **12:20 IDT Jul 14** 🎉 | jn-5880-validate-tag-glob-fix — **ARCHIVED 12:30 IDT Jul 14** ✅. **JN-5880 Jira → needs Done!** |
| [#1665](https://github.com/Jounce-IO/jounce/pull/1665) | [JN-5879](https://redhat.atlassian.net/browse/JN-5879) | **10:48 IDT Jul 14** 🎉 | jn-5879-justfile-skip-helm — **ARCHIVED 11:30 IDT Jul 14** ✅. **JN-5879 Jira → needs Done!** |
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
