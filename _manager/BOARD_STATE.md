# Board State — jounce-workflow-ai

*Last updated: 2026-07-20 14:33 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | ✅ **ALL CI FULLY PASSING** run 29729530150 — nox ✅, e2e-api ✅, e2e-smoke ✅, e2e-product ✅, integration-run ✅, integration-tests ✅, tox-run ✅, atlas-validate ✅, check-changes ✅, JIRA Assoc ✅, CodeRabbit ✅, pre-commit ✅, pre-commit-run ✅, e2e-tests ✅, all-checks ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🟢 **READY FOR REVIEW** — MERGEABLE, reviewDecision:"" (reset after rebase). **ALL CI 100% PASS** including e2e-product ✅ (was pending last run). **Action: Request review now.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. No change. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 20+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 12+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI PASS (run 29403233416 — stale) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | DRAFT PR #1670. CI all pass (stale). Needs: mark ready for review. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | UNKNOWN (CONFLICTING) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🟡 **CONFLICTING** — needs rebase on main. |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910 (stale): pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — unchanged. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 12+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 25+ days. Propose archive. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🟡 **RUN 29734729818** — e2e-api ✅ **NOW PASSING**, nox ✅, tox-run ✅, integration ✅, pre-commit ✅; **e2e-smoke ⏳ PENDING**; all-checks not yet shown | **OPEN, MERGEABLE** 🟡 | 🟡 **e2e-api NOW PASSING** (was ❌ at 13:03 IDT). New CI run 29734729818 — most checks ✅, e2e-smoke ⏳ PENDING. If e2e-smoke passes → all-checks ✅ → **READY FOR REVIEW**. JN-5725 Done ✅. |

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
| **[AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657)** | **[#1691](https://github.com/Jounce-IO/jounce/pull/1691) + [#1692](https://github.com/Jounce-IO/jounce/pull/1692)** | **BOTH MERGED** (10:20 + 09:36 IDT Jul 20) | **In Progress** | ❌ Update Jira → Done |
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** / AIPCC-26976 | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED 13:29 IDT Jul 14** | **New** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **New** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **New** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |

*JN-5891: Done ✅. JN-5870: Done ✅. JN-5880: Done ✅. JN-5879: Done ✅. JN-5841: Done ✅. JN-5867: Done ✅. JN-5717: Done ✅. JN-5868: Done ✅. JN-5725: Done ✅. Jira MCP 401 — use acli for updates.*

---

## Daily Jira Sprint Snapshot (12:03 IDT Jul 20)

Active sprint tickets assigned to Joseph (non-Done/Closed, via acli):

| Ticket | Status | Summary |
|--------|--------|---------|
| [AIPCC-27018](https://redhat.atlassian.net/browse/AIPCC-27018) | New | [CI] Add CI drift detection for AGENTS.md staleness |
| [AIPCC-27012](https://redhat.atlassian.net/browse/AIPCC-27012) | New | [QE] Cross-tool validation of hierarchical AGENTS.md |
| [AIPCC-27007](https://redhat.atlassian.net/browse/AIPCC-27007) | New | [DEV] Refine existing tests/e2e/AGENTS.md |
| [AIPCC-27002](https://redhat.atlassian.net/browse/AIPCC-27002) | New | [DEV] Write peripheral app AGENTS.md files |
| [AIPCC-26996](https://redhat.atlassian.net/browse/AIPCC-26996) | New | [DEV] Write Helm and CI/CD AGENTS.md files (= jn-5845 PR #1667) |
| [AIPCC-26990](https://redhat.atlassian.net/browse/AIPCC-26990) | New | [DEV] Write service/lib/sql domain AGENTS.md files (= jn-5844 PR #1670) |
| [AIPCC-26983](https://redhat.atlassian.net/browse/AIPCC-26983) | New | [CI] Remove ties infrastructure + Cursor AGENTS.md auto-generation |
| [AIPCC-26976](https://redhat.atlassian.net/browse/AIPCC-26976) | New | [DEV] Write apps/jbenchmark/AGENTS.md (= JN-5842 PR #1658 MERGED — Jira mismatch!) |
| [AIPCC-26144](https://redhat.atlassian.net/browse/AIPCC-26144) | In Progress | Add --user, --no-cache, --skip-estimator CLI flags (= JN-5244 subtask) |
| [AIPCC-25962](https://redhat.atlassian.net/browse/AIPCC-25962) | In Progress | [DOCS] Document module layout convention and Dockerfile template |
| [AIPCC-24211](https://redhat.atlassian.net/browse/AIPCC-24211) | In Progress | Upgrade AGENTS.md Standard for Jounce Repository (= JN-4393) |
| [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) | In Progress | [QE] E2E validation of IBM cluster connection workflows |
| [AIPCC-23857](https://redhat.atlassian.net/browse/AIPCC-23857) | In Progress | Refactor run_jbenchmark script (= JN-5132) |
| [AIPCC-23788](https://redhat.atlassian.net/browse/AIPCC-23788) | New | Add subcommands to jbenchmark (= JN-5401 — MERGED, Jira stale!) |
| [AIPCC-23249](https://redhat.atlassian.net/browse/AIPCC-23249) | In Progress | Prepare benchmark run configs for IBM H100/A100-80/H200 (= jn-5824 worktree) |
| [AIPCC-23308](https://redhat.atlassian.net/browse/AIPCC-23308) | New | Implement v0.7.0 Report Ingestion |
| [AIPCC-23298](https://redhat.atlassian.net/browse/AIPCC-23298) | New | Implement v0.7.0 Container Image & Argo Integration |

---

## Key Changes (14:33 IDT Jul 20 vs 14:03 IDT Jul 20)

| What changed | Delta |
|---|---|
| **Board static** | All PRs unchanged: #1690 ALL CI PASS (run 29729530150) still awaiting review; #1638 e2e-smoke ❌ FAIL confirmed (run 29734729818 final); #1669 CONFLICTING + CI ❌; #1667 CONFLICTING; #1670 DRAFT. |
| **Jira mismatches: 7** | No change. |
| **0 merges, 0 archives** | No new merges or archives this run. |

---

## Attention Items

### 🟢 #1690 (aipcc-27645) — ALL CI 100% PASSING — READY FOR REVIEW

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645) JN-5872"
- State: OPEN, **MERGEABLE** ✅, reviewDecision: "" (reset after rebase push)
- **Run 29729530150** — **ALL CHECKS PASS (100%)**:
  - ✅ PASS: e2e-smoke, pre-commit-run, nox, e2e-api, **e2e-product** ✅ (now complete!), integration-run, integration-tests, tox-run, atlas-validate, check-changes, JIRA Assoc, CodeRabbit, pre-commit, e2e-tests, all-checks
- **Action:** Request review now.

---

### 🔴 #1638 (off-board JN-5725) — e2e-smoke FAILED ❌

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)"
- State: OPEN, **MERGEABLE** 🟡
- **CI run 29734729818** (final results):
  - ✅ PASS: e2e-api ✅, nox, tox-run, integration-run, integration-tests, pre-commit-run, pre-commit, atlas-validate, check-changes, JIRA Assoc, CodeRabbit
  - ❌ FAIL: **e2e-smoke ❌** (was ⏳ PENDING at 13:33 IDT — now resolved as FAIL), all-checks ❌, e2e-tests ❌
  - ⏸ SKIP: atlas-validate-run, bake, e2e-product, e2e-priority
- Jira: JN-5725 is Done ✅
- **Action:** 🔴 Joseph needs to investigate e2e-smoke failure. Check run 29734729818 e2e-smoke logs.

---

### 🔴 #1669 (jn-5872) — CI FAILING + CONFLICTING (unchanged)

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, **CONFLICTING** 🔴
- **Run 29683534910** (stale): FAIL: all-checks ❌, pre-commit ❌, nox ❌, pre-commit-run ❌, tox-run ❌
- **Action:** 1) Rebase on main. 2) Fix pre-commit + nox + tox-run failures.

---

### 🟡 #1667 (jn-5845) — Needs rebase (CONFLICTING)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **CONFLICTING**
- **Action:** Rebase jn-5845-helm-cicd-agents-md on main.

---

### 🟡 #1670 (jn-5844) — DRAFT (needs mark ready)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md files (JN-5844)"
- State: OPEN, isDraft:true, MERGEABLE
- CI run 29403233416 all-pass (stale).
- **Action:** Mark PR ready for review (remove draft status).

---

### 🟡 Jira Mismatches (7 active)

AIPCC-27657 (#1691+#1692 both merged, Jira still In Progress).
Remaining 6: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.
Use `acli jira workitem transition` to update. Jira MCP 401. acli working.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 12+)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Waiting for direction (stale 12+ days)

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### ⚠️ Overnight/Morning Session Failures (Jul 17–19)

Multiple consecutive session failures since Jul 17 (overnight + weekend schedules).
Daytime sessions running correctly.

---

## Archived This Session

No archives this run.

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **aipcc-27657-guidellm-output-dir** | [#1691 MERGED](https://github.com/Jounce-IO/jounce/pull/1691) | PR #1691 MERGED 10:20 IDT Jul 20; autonomous archive | 10:10 IDT Jul 20 |
| **model-packaging-cr** | [#161 CLOSED](https://github.com/Jounce-IO/model-packaging-pipeline/pull/161) | PR #161 CLOSED Jun 16; stale 34 days | 12:30 IDT Jul 19 |
| **jn-5871** | — | ARCHIVED by Joseph (no PR, Code done) | 09:57 UTC Jul 15 |
| **jn-5891-max-seconds-1200** | [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | MERGED 14:14 IDT Jul 16 | 14:45 IDT Jul 16 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **10:20 IDT Jul 20** 🎉 | ARCHIVED 10:10 IDT Jul 20. AIPCC-27657 needs Done in Jira. |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **09:36 IDT Jul 20** 🎉 | Off-board companion PR (no Agor worktree). |
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
