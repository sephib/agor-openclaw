# Board State — jounce-workflow-ai

*Last updated: 2026-07-22 12:03 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | ✅ **ALL CI FULLY PASSING** run 29729530150 (unchanged) | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CONFLICTING** (unchanged, now 3+ days). **ALL CI 100% PASS**. **Action: Rebase aipcc-27645-server-resources on main, then request review.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (frozen) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |

| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 22+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 14+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ **all-checks ✅, JIRA Assoc ✅, bake ✅** (run 29899957009 confirmed) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | DRAFT PR #1670. New CI run confirmed all-checks ✅. **Needs: mark ready for review.** |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | 🔴 run 29896027349: pre-commit ❌, all-checks ❌; JIRA Assoc ✅, nox ✅, tox ✅, e2e ✅ | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🟡 MERGEABLE ✅. **Only blocker: pre-commit ❌. Action: Fix pre-commit on jn-5845-helm-cicd-agents-md.** |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910 (stale): pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — DRAFT. Unchanged. Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 14+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 27+ days. Propose archive. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🔴 CI run 29749885088 — **pre-commit ❌**, pre-commit-run ❌, all-checks ❌; JIRA Assoc ✅, nox ✅, tox-run ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | **isDraft:false** (ready for review). CONFLICTING. pre-commit ❌. **Action: Rebase + fix pre-commit.** |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌; nox ✅, tox ✅ (run 29741945977) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) — In Progress | PR #1697 DRAFT. CI failing: pre-commit ❌. MERGEABLE. No zone assigned. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700 DRAFT](https://github.com/Jounce-IO/jounce/pull/1700) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29808132144); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT "fix(jbenchmark): script runner and cluster config". Split from #1698. No zone assigned. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29845259306); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT "fix(jbenchmark): config-generator hotfix (1 of 2, split from #1698)". No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | 🟡 all-checks ✅, JIRA Assoc ❌ only (run 29741885397) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT PR #1696 — MERGEABLE. CI: all-checks ✅, JIRA Assoc ❌ only. **Action: Fix JIRA Assoc, then mark ready.** |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29846894702) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | 🟡 **MERGEABLE** ✅. DRAFT. CI: pre-commit ❌, JIRA Assoc ❌. Needs: pre-commit fix + JIRA Assoc fix, then mark ready. |

---

## 🆕 New Bot-Authored PRs (Not on Board — Flagged)

| PR | Ticket | State | CI | Notes |
|----|--------|-------|----|-------|
| [#1693](https://github.com/Jounce-IO/jounce/pull/1693) | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | OPEN, MERGEABLE, NOT draft | 🟡 run 29905405310: **e2e-api ✅, nox ✅, tox ✅, integration ✅**; pre-commit ❌, JIRA Assoc ❌; e2e-smoke PENDING | Bot "jira-autofix". **🎉 reviewDecision: APPROVED** (12:03 IDT). Only blockers: pre-commit ❌ + JIRA Assoc ❌ + e2e-smoke PENDING. |
| [#1694](https://github.com/Jounce-IO/jounce/pull/1694) | [AIPCC-27681](https://redhat.atlassian.net/browse/AIPCC-27681) | OPEN, CONFLICTING, NOT draft | 🔴 run 29740715467 (latest): JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅, e2e ✅ | Bot "jira-autofix" authored. "fix(jbenchmark): share MetadataResolver across gpu_count iterations". Unchanged. Needs Joseph review. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🟡 **NEW run 29905926340 in progress** (someone pushed fix): integration-run ✅, integration-tests ✅, atlas-validate ✅, JIRA Assoc ✅; e2e-api PENDING, tox PENDING, pre-commit PENDING | **OPEN, 🟢 MERGEABLE** | 🟡 **New CI run started** (12:03 IDT). Previous run 29900239662 had e2e-api ❌. Push detected. Waiting on e2e-api result. |
| [#1704](https://github.com/Jounce-IO/jounce/pull/1704) | — | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | NOT CHECKED | OPEN, NOT draft (by AlonKellner-RedHat) | 🆕 New off-board PR Jul 21: "chore: dependencies, test config, docs, and tooling (JN-5725)" |
| [#1705](https://github.com/Jounce-IO/jounce/pull/1705) | — | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | NOT CHECKED | OPEN, NOT draft (by AlonKellner-RedHat) | 🆕 New off-board PR Jul 21: "feat(e2e): enhanced test infrastructure -- clients, diagnostics, helpers (JN-5725)" |

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

*6 mismatches remain. AIPCC-27657: Closed ✅ (13:00 IDT Jul 21). JN-5891: Done ✅. JN-5870: Done ✅. JN-5880: Done ✅. JN-5879: Done ✅. JN-5841: Done ✅. JN-5867: Done ✅. JN-5717: Done ✅. JN-5868: Done ✅. JN-5725: Done ✅. Jira MCP 401 — use acli for updates.*

---

## Key Changes (12:03 IDT Jul 22 vs 11:33 IDT Jul 22)

| What changed | Delta |
|---|---|
| **#1638 NEW CI run 29905926340** 🟡 | Someone pushed to fix the e2e-api failure. New run in progress: integration-run ✅, atlas-validate ✅, JIRA Assoc ✅; e2e-api PENDING, tox PENDING, pre-commit PENDING. Previous run 29900239662 had e2e-api ❌. |
| **#1693 reviewDecision: APPROVED** 🎉 | Bot PR now APPROVED! New CI run 29905405310: e2e-api ✅, nox ✅, tox ✅, integration ✅. Remaining blockers: pre-commit ❌ + JIRA Assoc ❌ + e2e-smoke PENDING. e2e-product no longer failing in new run. |
| **All other active pipeline PRs** | Unchanged — #1690 CONFLICTING all-CI-pass, #1667 pre-commit ❌, #1669 CI ❌+CONFLICTING, #1670 DRAFT clean. 6 Jira mismatches unchanged. |

---

## Attention Items

### 🟡 #1638 (off-board JN-5725) — NEW CI RUN IN PROGRESS (e2e-api fix pushed)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites (JN-5725)"
- State: OPEN, **🟢 MERGEABLE**
- **NEW run 29905926340** (in progress): integration-run ✅, integration-tests ✅, atlas-validate ✅, JIRA Assoc ✅; e2e-api PENDING, tox PENDING, pre-commit PENDING
- Previous run 29900239662 had e2e-api ❌ — push detected (someone pushed a fix)
- Jira: JN-5725 Done ✅
- **Action:** Monitor e2e-api result in run 29905926340. If passes → PR is CI-clean.
- **Note:** Two related PRs #1704 + #1705 by AlonKellner-RedHat also open (JN-5725 scope).

---

### 🟡 #1693 + #1694 — Bot-Authored PRs Need Review

**[#1693](https://github.com/Jounce-IO/jounce/pull/1693)**: "fix(jbenchmark): return 409 Conflict on duplicate experiment plan name (AIPCC-27655)"
- State: OPEN, MERGEABLE, NOT draft
- **🎉 reviewDecision: APPROVED** (12:03 IDT)
- **New run 29905405310**: e2e-api ✅, nox ✅, tox ✅, integration ✅ — core CI passing; pre-commit ❌, JIRA Assoc ❌; e2e-smoke PENDING
- **Action:** Fix pre-commit + JIRA Assoc. Wait for e2e-smoke. If e2e-smoke ✅ → ready to merge.

**[#1694](https://github.com/Jounce-IO/jounce/pull/1694)**: "fix(jbenchmark): share MetadataResolver across gpu_count iterations (AIPCC-27681)"
- State: OPEN, CONFLICTING, NOT draft
- CI run 29740715467: JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅, e2e ✅
- **Action:** Review PR. Rebase on main (CONFLICTING). Fix JIRA Assoc + pre-commit.

---

### 🔴 #1690 (aipcc-27645) — ALL CI PASSING BUT CONFLICTING

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645)"
- State: OPEN, **CONFLICTING** 🔴 (3+ days unchanged)
- **Run 29729530150** — **ALL CHECKS PASS (100%)**
- **Action:** Rebase aipcc-27645-server-resources on main, then request review.

---

### 🔴 #1669 (jn-5872) — CI FAILING + CONFLICTING

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, **CONFLICTING** 🔴
- Run 29683534910 (stale): FAIL: pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌
- **Action:** 1) Rebase on main. 2) Fix pre-commit + nox + tox-run.

---

### 🟡 #1667 (jn-5845) — MERGEABLE (pre-commit ❌ only)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **MERGEABLE** ✅
- Run 29896027349: pre-commit ❌, all-checks ❌; **JIRA Assoc ✅, nox ✅, tox ✅, e2e-api ✅, e2e-smoke ✅, integration ✅**
- **Only blocker: pre-commit ❌**
- **Action:** Fix pre-commit on jn-5845-helm-cicd-agents-md.

---

### 🟡 #1670 (jn-5844) — DRAFT, ALL CI CLEAN (needs mark ready)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): isDraft:true, MERGEABLE. New CI run 29899957009: all-checks ✅, JIRA Assoc ✅, bake ✅.
- **Action:** Mark PR ready for review.

---

### 🔴 #1698 (aipcc-23845) — DOUBLE-BLOCKED: CONFLICTING + pre-commit ❌

PR [#1698](https://github.com/Jounce-IO/jounce/pull/1698): isDraft:false (marked ready!). CONFLICTING. pre-commit ❌ (run 29749885088).
- **Action:** 1) Rebase on main. 2) Fix pre-commit.

---

### 🔴 #1700 + #1701 (aipcc-23845 splits) — pre-commit ❌, NO ZONE

PR [#1700](https://github.com/Jounce-IO/jounce/pull/1700): DRAFT, MERGEABLE. pre-commit ❌, JIRA Assoc ❌, all-checks ❌.
PR [#1701](https://github.com/Jounce-IO/jounce/pull/1701): DRAFT, MERGEABLE. pre-commit ❌, JIRA Assoc ❌, all-checks ❌.
- **Action:** Fix pre-commit on both. Assign to appropriate zone.

---

### 🟡 #1696 (aipcc-23895) — JIRA Assoc only

PR [#1696](https://github.com/Jounce-IO/jounce/pull/1696): DRAFT, MERGEABLE. CI run 29741885397: **all-checks ✅, JIRA Assoc ❌ only**.
- **Action:** Fix JIRA Association, then mark ready for review.

---

### 🟡 #1695 (aipcc-23925) — MERGEABLE + CI failing

PR [#1695](https://github.com/Jounce-IO/jounce/pull/1695): DRAFT, MERGEABLE. CI run 29846894702: **pre-commit ❌, JIRA Assoc ❌, all-checks ❌**.
- **Action:** Fix pre-commit AND JIRA Association, then mark ready.

---

### 🟡 Jira Mismatches (6 active — unchanged)

6 mismatches: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546. Use `acli jira workitem transition` to update.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 14+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Waiting for direction (stale 14+ days)

Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

---

## Archived This Session

**🧹 Mass Danger Delete Zone cleanup — 35 worktrees archived (10:33 IDT Jul 22):**

All had MERGED or CLOSED PRs, or were in Done/Danger Delete Zone with no active PR:

| Branch | PR | Reason |
|--------|-----|--------|
| jn-2739-planning-service2 | [#1279 MERGED](https://github.com/Jounce-IO/jounce/pull/1279) | PR MERGED |
| jn-2741-execution-service2 | [#1196 CLOSED](https://github.com/Jounce-IO/jounce/pull/1196) | PR CLOSED |
| jn-2741-implement-execution-service-for-workflow-orchestration | [#1196 CLOSED](https://github.com/Jounce-IO/jounce/pull/1196) | PR CLOSED |
| jn-2743-update-post-processing-for-new-schema | [#1224 CLOSED](https://github.com/Jounce-IO/jounce/pull/1224) | PR CLOSED |
| jn-3676-implement-soft-delete-pattern | [#1225 CLOSED](https://github.com/Jounce-IO/jounce/pull/1225) | PR CLOSED |
| jn-3762-execute-b200-benchmarks | [#1200 CLOSED](https://github.com/Jounce-IO/jounce/pull/1200) | PR CLOSED |
| jn-3925-release-tagging-convention | [#1252 CLOSED](https://github.com/Jounce-IO/jounce/pull/1252) | PR CLOSED |
| jn-4058-implement-benchmark-runner | [#1236 MERGED](https://github.com/Jounce-IO/jounce/pull/1236) | PR MERGED |
| jn-4061-argo-artifact-spike | [#1247 CLOSED](https://github.com/Jounce-IO/jounce/pull/1247) | PR CLOSED |
| jn-4062-update-execution-flow | [#1251 MERGED](https://github.com/Jounce-IO/jounce/pull/1251) | PR MERGED |
| jn-4200-implement-combinatorial-matrix-expansion-logic | [#1280 MERGED](https://github.com/Jounce-IO/jounce/pull/1280) | PR MERGED |
| jn-4212-update-tooling-configuration | [#1281 MERGED](https://github.com/Jounce-IO/jounce/pull/1281) | PR MERGED |
| jn-4390-benchmark-app-management | [#1295 CLOSED](https://github.com/Jounce-IO/jounce/pull/1295) | PR CLOSED |
| jn-4503-poc-slack-incoming-webhook | [#1322 MERGED](https://github.com/Jounce-IO/jounce/pull/1322) | PR MERGED |
| jn-4526-integrate-run-estimator | [#1303 MERGED](https://github.com/Jounce-IO/jounce/pull/1303) | PR MERGED |
| jn-4621-estimator-new-schema | [#1425 CLOSED](https://github.com/Jounce-IO/jounce/pull/1425) | PR CLOSED |
| jn-5161-jn-4621-sub-task-1-create-schema-handler-p | [#1437 MERGED](https://github.com/Jounce-IO/jounce/pull/1437) | PR MERGED |
| jn-5162-jn-4621-sub-task-2-implement-v2schemahandl | [#1439 MERGED](https://github.com/Jounce-IO/jounce/pull/1439) | PR MERGED |
| jn-5181-populate-tensor-parallel | [#1451 MERGED](https://github.com/Jounce-IO/jounce/pull/1451) | PR MERGED |
| jn-5133-use-cases-benchmark-visibility | [#1418 MERGED](https://github.com/Jounce-IO/jounce/pull/1418) | PR MERGED |
| jn-4833-model-configs-2026-04 | [#1366 MERGED](https://github.com/Jounce-IO/jounce/pull/1366) | PR MERGED |
| jn-4910-hw-aware-runner | [#1365 CLOSED](https://github.com/Jounce-IO/jounce/pull/1365) | PR CLOSED |
| jn-4958-update-config-status-run | [#1387 CLOSED](https://github.com/Jounce-IO/jounce/pull/1387) | PR CLOSED |
| jn-5243-refactor-run-jbenchmark-runner-orchestrati-8 | [#1468 MERGED](https://github.com/Jounce-IO/jounce/pull/1468) | PR MERGED (Done zone) |
| jn-5246-enrich-experimentplan-deployment-configs-f-4 | [#1470 MERGED](https://github.com/Jounce-IO/jounce/pull/1470) | PR MERGED |
| jn-5246-enrich-experimentplan-deployment-configs-f-8 | [#1466 CLOSED](https://github.com/Jounce-IO/jounce/pull/1466) | PR CLOSED |
| jn-5243-refactor-run-jbenchmark-runner-orchestrati-9 | — | Done zone, no PR |
| jn-5244-add-user-no-cache-skip-estimator-cli-flag-2 | — | Done zone, no PR |
| jn-5244-add-user-no-cache-skip-estimator-cli-flags-8 | — | Done zone, no PR |
| jn-5250-implement-run-estimator-server-side-skip-l-6 | — | Done zone, no PR |
| jn-5326-integrate-v2-configgenerator-into-runner-3 | — | Done zone, no PR |
| jn-5326-integrate-v2-configgenerator-into-runner-o-5 | — | Done zone, no PR |
| jn-5191-db-erd-modelcar | — | Danger Delete Zone, Jira Done |
| jn-5405-ci-test-coverage | — | Danger Delete Zone, unassigned |
| root-value-analysis-prompt | — | Danger Delete Zone, Jira Done |

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jn-5132-refactor-run-jbenchmark-script-to-support** | [#1457 CLOSED](https://github.com/Jounce-IO/jounce/pull/1457) | PR CLOSED May 31; detected in board scan | 12:30 IDT Jul 21 |
| **jn-5246-exp-plan-modelcar** | [#1466 CLOSED](https://github.com/Jounce-IO/jounce/pull/1466) | PR CLOSED May 31; detected in board scan | 12:30 IDT Jul 21 |
| **aipcc-27657-guidellm-output-dir** | [#1691 MERGED](https://github.com/Jounce-IO/jounce/pull/1691) | PR #1691 MERGED Jul 20 | 10:10 IDT Jul 20 |
| **model-packaging-cr** | [#161 CLOSED](https://github.com/Jounce-IO/model-packaging-pipeline/pull/161) | PR #161 CLOSED Jun 16 | 12:30 IDT Jul 19 |
| **jn-5871** | — | ARCHIVED by Joseph | 09:57 UTC Jul 15 |
| **jn-5891-max-seconds-1200** | [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | MERGED Jul 16 | 14:45 IDT Jul 16 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **10:20 IDT Jul 20** 🎉 | ARCHIVED 10:10 IDT Jul 20. AIPCC-27657 **Closed ✅** (13:00 IDT Jul 21). |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **09:36 IDT Jul 20** 🎉 | Off-board companion PR. |
| [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) | **14:14 IDT Jul 16** 🎉 | ARCHIVED 14:45 Jul 16. JN-5891 Done ✅. |
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | git-only. JN-5867 Done ✅ |
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
