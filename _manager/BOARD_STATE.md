# Board State — jounce-workflow-ai

*Last updated: 2026-07-20 08:10 IDT (daily external sync)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | ✅ ALL CI PASS (run 29698050089) — JIRA ✅, all-checks ✅, pre-commit ✅, pre-commit-run ✅, tox-run ✅, nox ✅, e2e-smoke ✅, e2e-api ✅, e2e-tests ✅, integration-run ✅, integration-tests ✅, atlas-validate ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) | 🟢 **READY FOR REVIEW** — not DRAFT, ALL CI PASS. State: OPEN, MERGEABLE ✅. Unchanged overnight. |
| aipcc-27657-guidellm-output-dir | **Code** | [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | 🟡 **NEW RUN 29717054182** — pre-commit ✅ NOW PASSES (regression fixed!). PASS: JIRA ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, e2e-smoke ✅, integration-run ✅, integration-tests ✅, nox ✅, pre-commit ✅, pre-commit-run ✅, tox-run ✅, CodeRabbit ✅. **e2e-product ⏳ PENDING** — all-checks not yet complete. | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | 🟡 **pre-commit FIXED** — new run 29717054182. Awaiting e2e-product to complete. ⚠️ PR title contains "JN-5872" — verify title. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — New | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. No change. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 20+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 12+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI PASS (run 29403233416 — stale) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | DRAFT PR #1670. CI all pass (stale). Needs: mark ready for review. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | UNKNOWN (CONFLICTING) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🟡 **CONFLICTING** — needs rebase on main. |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910: pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ (stale — no new run) | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — unchanged from previous run. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 12+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 25+ days. Propose archive. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | ✅ **Run 29694608697** — **ALL CI FULLY PASS**: JIRA ✅, pre-commit ✅, pre-commit-run ✅, atlas-validate ✅, check-changes ✅, e2e-smoke ✅, e2e-api ✅, e2e-product ✅, integration-run ✅, integration-tests ✅, tox-run ✅, nox ✅. | OPEN, **MERGEABLE** ✅ | 🎉 **ALL CI FULLY PASS** — ready for review. Unchanged overnight. |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | aipcc-27657-test-updates | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | 🟡 Run 29717285073 — pre-commit ✅, pre-commit-run ✅, e2e-api ✅, e2e-smoke ✅, integration-run ✅, tox-run ✅, nox ✅, atlas-validate ✅. **e2e-product ⏳ PENDING**. CodeRabbit disabled (feature branch base). | OPEN, **MERGEABLE** ✅ | 🆕 **NEW** (overnight) — test fixtures for GuideLLM v0.6.1. Targets `aipcc-27657-guidellm-output-dir` (feeds into #1691). Merge this first, then #1691 into main. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Waiting/Blocked | Refactor run_jbenchmark script to support redesign flow |
| [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | New | Add subcommands to runner — PR #1654 MERGED Jul 12, Jira stale! |
| [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | In Progress | Add CLI flags (jn-5244-cli-flags archived in Agor) |
| [JN-4393](https://redhat.atlassian.net/browse/JN-4393) | In Progress | Upgrade AGENTS.md Standard |
| [JN-5851](https://redhat.atlassian.net/browse/JN-5851) | New | Implement v0.7.0 Container Image & Argo Integration |
| [JN-5852](https://redhat.atlassian.net/browse/JN-5852) | New | Implement v0.7.0 Report Ingestion |
| AIPCC-27018 | New | [CI] Add CI drift detection for AGENTS.md staleness |
| AIPCC-27012 | New | [QE] Cross-tool validation of hierarchical AGENTS.md |
| AIPCC-27007 | New | [DEV] Refine existing tests/e2e/AGENTS.md |
| AIPCC-27002 | New | [DEV] Write peripheral app AGENTS.md files |
| AIPCC-26983 | New | [CI] Remove ties infrastructure entirely |
| AIPCC-23890 | In Progress | [QE] E2E validation of IBM cluster connection workflows |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** / AIPCC-26976 | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED 13:29 IDT Jul 14** | **New** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **New** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **New** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |

*JN-5891: Done ✅. JN-5870: Done ✅. JN-5880: Done ✅. JN-5879: Done ✅. JN-5841: Done ✅. JN-5867: Done ✅. JN-5717: Done ✅. JN-5868: Done ✅. JN-5725: Done ✅. Jira MCP 401 — use acli for updates.*

---

## Daily Jira Sprint Snapshot (08:10 IDT Jul 20)

Active sprint tickets assigned to Joseph (via acli, `openSprints()`):

| Ticket | Status | Summary |
|--------|--------|---------|
| [AIPCC-23169](https://redhat.atlassian.net/browse/AIPCC-23169) | In Progress | Mode Validation 3.5GA Release |
| [AIPCC-23119](https://redhat.atlassian.net/browse/AIPCC-23119) | New | Upgrade to GuideLLM v0.7.0 |
| [AIPCC-23104](https://redhat.atlassian.net/browse/AIPCC-23104) | In Progress | Benchmark Visibility Dashboard |
| [AIPCC-27018](https://redhat.atlassian.net/browse/AIPCC-27018) | New | [CI] Add CI drift detection for AGENTS.md staleness |

All other sprint tickets returned by Jira are Closed. The 6 Jira mismatches (JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546) are old JN-prefix tickets not appearing in this sprint search — status unchanged, still need manual acli update.

---

## Key Changes (08:10 IDT Jul 20 vs 06:04 IDT Jul 20)

| What changed | Delta |
|---|---|
| **🎉 #1691 (AIPCC-27657) pre-commit FIXED** | NEW RUN 29717054182 — pre-commit ✅ NOW PASSES (was failing 2 consecutive runs). All checks pass except e2e-product ⏳ still pending. Once e2e-product passes, all-checks should complete and PR is ready for review. |
| **🆕 PR #1692 (AIPCC-27657 test fixtures)** | NEW PR overnight — test fixtures for GuideLLM v0.6.1 on `aipcc-27657-test-updates`. CI mostly passing, e2e-product pending. Feeds into #1691 branch. Must merge before #1691. |
| **Jira sprint** | 4 non-Closed tickets: AIPCC-23169 (In Progress), AIPCC-23119 (New), AIPCC-23104 (In Progress), AIPCC-27018 (New). All others Closed. 6 Jira mismatches unchanged. |
| **#1690 unchanged** | ALL CI PASS (run 29698050089). READY FOR REVIEW. No change. |
| **#1638 unchanged** | ALL CI PASS (run 29694608697). READY FOR REVIEW. No change. |
| **#1669/#1667 CONFLICTING unchanged** | No CI changes. Still failing/conflicting. |
| **0 merges** | No new merges since 06:04 IDT. |

---

## Attention Items

### 🟡 #1691 (aipcc-27657) — pre-commit FIXED, e2e-product PENDING

PR [#1691](https://github.com/Jounce-IO/jounce/pull/1691): "fix(helm): update GuideLLM flag from --output-path to --output-dir (AIPCC-27657) JN-5872"
- State: OPEN, NOT DRAFT, **MERGEABLE** ✅
- **Run 29717054182** (NEW — as of 08:04 IDT):
  - **PASS**: JIRA ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, e2e-smoke ✅, integration-run ✅, integration-tests ✅, nox ✅, **pre-commit ✅ FIXED**, pre-commit-run ✅, tox-run ✅, CodeRabbit ✅
  - **PENDING**: e2e-product ⏳ (still running)
  - all-checks: not yet complete (depends on e2e-product)
- ⚠️ **PR title includes "JN-5872"** — this may be an error (JN-5872 is a different ticket). Verify PR title.
- **Action:** Wait for e2e-product to complete. If it passes, PR is ready for review + merge. 🎉
- ⚠️ Also see companion **PR #1692** (test fixtures) which must merge into this branch first — it's also awaiting e2e-product.

---

### 🆕 #1692 (aipcc-27657-test-updates) — New companion PR

PR [#1692](https://github.com/Jounce-IO/jounce/pull/1692): "test(jbenchmark): update test fixtures for GuideLLM v0.6.1 (JN-5872) aipcc-27657"
- State: OPEN, NOT DRAFT, **MERGEABLE** ✅. Base: `aipcc-27657-guidellm-output-dir` (feeds into #1691).
- **Run 29717285073** — pre-commit ✅, pre-commit-run ✅, e2e-api ✅, e2e-smoke ✅, integration-run ✅, tox-run ✅, nox ✅. **e2e-product ⏳ PENDING**.
- CodeRabbit disabled (base is feature branch, not main).
- **Action:** Merge this into `aipcc-27657-guidellm-output-dir` first, then merge #1691 into main.

---

### 🟢 #1690 (aipcc-27645) — READY FOR REVIEW (unchanged)

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645) JN-5872"
- State: OPEN, **NOT DRAFT**, **MERGEABLE** ✅
- **Run 29698050089** (ALL PASS — unchanged from last run):
  - PASS: JIRA ✅, all-checks ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, e2e-smoke ✅, e2e-tests ✅, integration-run ✅, integration-tests ✅, nox ✅, pre-commit ✅, pre-commit-run ✅, tox-run ✅
  - CodeRabbit review: COMPLETED
- **Action:** Review + merge. 🎉

---

### 🎉 #1638 (off-board JN-5725) — ALL CI FULLY PASS! (unchanged)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)"
- State: OPEN, **MERGEABLE** ✅
- **Run 29694608697** (ALL PASS — unchanged):
  - PASS: JIRA ✅, pre-commit ✅, pre-commit-run ✅, atlas-validate ✅, check-changes ✅, e2e-smoke ✅, e2e-api ✅, **e2e-product ✅**, integration-run ✅, integration-tests ✅, tox-run ✅, nox ✅
- **Action:** PR fully ready for review — submit now.

---

### 🔴 #1669 (jn-5872) — CI FAILING + CONFLICTING (unchanged)

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, **CONFLICTING** 🔴
- **Run 29683534910** (stale — no new push):
  - FAIL: all-checks ❌, pre-commit ❌, nox ❌ (regression), pre-commit-run ❌, tox-run ❌ (regression)
  - PASS: JIRA ✅, e2e-api ✅, e2e-smoke ✅, e2e-tests ✅, integration-run ✅, integration-tests ✅
- **Action:** 1) Rebase on main to resolve conflict. 2) Fix pre-commit + nox + tox-run failures.

---

### 🟡 #1667 (jn-5845) — Needs rebase (CONFLICTING)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **CONFLICTING**
- **Action:** Rebase jn-5845-helm-cicd-agents-md on main to resolve conflict.

---

### 🟡 #1670 (jn-5844) — DRAFT (needs mark ready)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md files (JN-5844)"
- State: OPEN, isDraft:true, MERGEABLE
- CI run 29403233416 all-pass (stale).
- **Action:** Mark PR ready for review (remove draft status).

---

### 🟡 Jira Mismatches (6 active)

Remaining 6: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.
Use `acli jira workitem transition` to update. Jira MCP 401. acli working.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 12+)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### ✅ jn-5871 — ARCHIVED in Agor Jul 15 by Joseph

- Was previously noted as "NOT in Agor" — **CORRECTED**: jn-5871 WAS registered in Agor (Code zone, uid=283) and was archived by Joseph on Jul 15 09:57 UTC.
- No PR was created. JN-5871 still **New** in Jira — may need investigation if work should continue.

---

### 🔄 jn-5824 — Waiting for direction (stale 12+ days)

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### ⚠️ Overnight/Morning Session Failures (Jul 17–19)

Multiple consecutive session failures since Jul 17 (overnight + weekend schedules).
Daytime sessions running correctly. This overnight session (Jul 20 midnight) is running successfully.

---

## Archived This Session

| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **model-packaging-cr** | [#161 CLOSED](https://github.com/Jounce-IO/model-packaging-pipeline/pull/161) | PR #161 CLOSED Jun 16; stale 34 days | 12:30 IDT Jul 19 |

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jn-5871** | — | ARCHIVED by Joseph (no PR, Code done) | 09:57 UTC Jul 15 |
| **jn-5891-max-seconds-1200** | [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | MERGED 14:14 IDT Jul 16 | 14:45 IDT Jul 16 |

Previously archived (Jul 14):
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jn-5870** | [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | MERGED 17:53 IDT Jul 14 | 19:30 IDT Jul 14 |
| **jn-5869** | [#1657](https://github.com/Jounce-IO/jounce/pull/1657) | CLOSED 12:03 IDT Jul 14 | 12:08 IDT Jul 14 |
| **jn-5842-jbenchmark-agents-md** | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | MERGED 13:29 IDT Jul 14 | 13:30 IDT Jul 14 |
| **jn-5880-validate-tag-glob-fix** | [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | MERGED 12:20 IDT Jul 14 | 12:30 IDT Jul 14 |
| **jn-5868** | [#1659](https://github.com/Jounce-IO/jounce/pull/1659) | CLOSED 12:26 IDT Jul 14 | 12:30 IDT Jul 14 |
| jn-5879-justfile-skip-helm | [#1665](https://github.com/Jounce-IO/jounce/pull/1665) | MERGED 10:48 IDT Jul 14 | 11:30 IDT Jul 14 |
| jn-5877-api-server-replicas | [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | MERGED 15:16 IDT Jul 13 | 15:30 IDT Jul 13 |
| jn-5874-values-prd-image-tags | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | MERGED 12:10 IDT Jul 13 | 12:32 IDT Jul 13 |
| jn-5401-runner-subcommands | [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | MERGED 17:12 IDT Jul 12 | ~17:12 IDT Jul 12 |
| jn-5841-agents-md-root | [#1649](https://github.com/Jounce-IO/jounce/pull/1649) | MERGED 14:45 IDT Jul 12 | 16:00 IDT Jul 12 |
| jn-5827-git-tagging-workflow | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED 14:27 IDT Jul 12 | 14:30 IDT Jul 12 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) | **14:14 IDT Jul 16** 🎉 | ARCHIVED 14:45 Jul 16. JN-5891 Done ✅. |
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | jn-5867 (git-only). JN-5867 Done ✅ |
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | 17:53 IDT Jul 14 🎉 | ARCHIVED 19:30 Jul 14. JN-5870 Done ✅ |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) | 13:29 IDT Jul 14 🎉 | ARCHIVED 13:30 Jul 14 |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | 12:20 IDT Jul 14 🎉 | ARCHIVED 12:30 Jul 14. JN-5880 Done ✅ |
| [#1665](https://github.com/Jounce-IO/jounce/pull/1665) | [JN-5879](https://redhat.atlassian.net/browse/JN-5879) | 10:48 IDT Jul 14 🎉 | ARCHIVED 11:30 Jul 14. JN-5879 Done ✅ |
| [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | [JN-5877](https://redhat.atlassian.net/browse/JN-5877) | 15:16 IDT Jul 13 🎉 | ARCHIVED 15:30 Jul 13 |
| [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | [JN-5874](https://redhat.atlassian.net/browse/JN-5874) | 12:10 IDT Jul 13 🎉 | ARCHIVED 12:32 Jul 13 |
| [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | 17:12 IDT Jul 12 🎉 | ARCHIVED. JN-5401 needs Done! |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
