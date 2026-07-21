# Board State — jounce-workflow-ai

*Last updated: 2026-07-21 10:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | ✅ **ALL CI FULLY PASSING** run 29729530150 — nox ✅, e2e-api ✅, e2e-smoke ✅, e2e-product ✅, integration-run ✅, integration-tests ✅, tox-run ✅, atlas-validate ✅, check-changes ✅, JIRA Assoc ✅, CodeRabbit ✅, pre-commit ✅, pre-commit-run ✅, e2e-tests ✅, all-checks ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CONFLICTING** (unchanged overnight). **ALL CI 100% PASS** (run 29729530150 unchanged). **Action: Rebase on main, then request review.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. No change. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 21+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 13+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI PASS (run 29403233416 — stale) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | DRAFT PR #1670. CI all pass (stale). Needs: mark ready for review. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | ✅ all-pass stale run 29402877354 | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🔴 **CONFLICTING** (unchanged overnight). CI stale (run 29402877354). **Action: Rebase jn-5845-helm-cicd-agents-md on main.** |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29741877329: pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (nox/tox now skipping — DRAFT) | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — DRAFT. Newer CI run vs prior (nox/tox now skip for draft). |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 13+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 26+ days. Propose archive. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🔴 CI run 29749885088 — **pre-commit ❌**, pre-commit-run ❌, all-checks ❌; JIRA Assoc ✅, nox ✅, tox-run ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | **isDraft:false** (ready for review!). pre-commit still ❌. MERGEABLE. **Action: Fix pre-commit.** |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌; nox ✅, tox ✅ | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) — In Progress | PR #1697 DRAFT. CI failing: pre-commit ❌. No zone assigned. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700 DRAFT](https://github.com/Jounce-IO/jounce/pull/1700) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29808132144); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | 🆕 **NEW** (created ~09:48 IDT Jul 21). DRAFT "fix(jbenchmark): script runner and cluster config (AIPCC-23845)". Split from #1698. No zone assigned. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29808455073); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | 🆕 **NEW** (created ~09:54 IDT Jul 21). DRAFT "fix(jbenchmark): config-generator hotfix (1 of 2, split from #1698)". No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29741945977) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT PR #1696 — **NOW MERGEABLE** (was CONFLICTING). pre-commit ❌ still blocks mark-ready. |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | 🟡 all-checks ✅, JIRA Assoc ❌ only (run 29741885397) — **CI IMPROVED** | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | DRAFT PR #1695 — pre-commit-run ✅, all-checks ✅. Only JIRA Assoc ❌ now. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🔴 CI **NEW run 29806749410** — **e2e-api ❌**, e2e-tests ❌, all-checks ❌; pre-commit ✅, nox ✅, tox ✅, integration ✅; e2e-smoke/product/priority: skipping | **OPEN, ✅ MERGEABLE** | 🔴 **MERGEABLE** but **e2e-api ❌ still failing** in new run 29806749410. JN-5725 Done ✅. **Action: e2e-api root cause investigation needed.** |

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

## Key Changes (10:00 IDT Jul 21 vs 08:30 IDT Jul 21)

| What changed | Delta |
|---|---|
| **2 NEW worktrees discovered** | `aipcc-23845-script-runner` (PR [#1700](https://github.com/Jounce-IO/jounce/pull/1700)) and `aipcc-23845-generator-hotfix` (PR [#1701](https://github.com/Jounce-IO/jounce/pull/1701)) — both split from #1698 (AIPCC-23845), both DRAFT, both pre-commit ❌. Created ~09:48–09:54 IDT Jul 21. |
| **0 merges, 0 archives** | No new merges or archives since 08:30 IDT. |
| **All existing PRs** | Unchanged: #1690 (CONFLICTING, all-CI ✅), #1698 (ready, pre-commit ❌), #1696 (MERGEABLE, pre-commit ❌), #1695 (JIRA ❌ only), #1697 (DRAFT, pre-commit ❌), #1667 (CONFLICTING, CI stale ✅), #1670 (DRAFT/MERGEABLE, CI stale ✅), #1669 (CONFLICTING, CI ❌), #1638 (e2e-api ❌). |

---

## Attention Items

### 🔴 #1690 (aipcc-27645) — ALL CI PASSING BUT CONFLICTING

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645)"
- State: OPEN, **CONFLICTING** 🔴 (unchanged overnight)
- **Run 29729530150** — **ALL CHECKS PASS (100%)**
- **Action:** Rebase aipcc-27645-server-resources on main, then request review.

---

### 🔴 #1638 (off-board JN-5725) — MERGEABLE but CI STILL FAILING

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)"
- State: OPEN, **✅ MERGEABLE**
- **CI run 29749975829** (unchanged, same run as Jul 20):
  - ❌ FAIL: **e2e-api ❌**, e2e-tests ❌, all-checks ❌ (e2e-smoke now shows "skipping" — downstream of e2e-api failure)
  - ✅ PASS: JIRA Assoc, atlas-validate, check-changes, integration-run, nox, pre-commit, pre-commit-run, tox-run
- Jira: JN-5725 is Done ✅
- **Action:** e2e-api root-cause investigation needed.

---

### 🔴 #1669 (jn-5872) — CI FAILING + CONFLICTING (unchanged)

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, **CONFLICTING** 🔴
- **Run 29683534910** (stale): FAIL: all-checks ❌, pre-commit ❌, nox ❌, pre-commit-run ❌, tox-run ❌
- **Action:** 1) Rebase on main. 2) Fix pre-commit + nox + tox-run failures.

---

### 🔴 #1667 (jn-5845) — CONFLICTING (unchanged)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **🔴 CONFLICTING** (unchanged overnight)
- CI: stale run 29402877354 all-pass. No new CI triggered.
- **Action:** Rebase jn-5845-helm-cicd-agents-md on main.

---

### 🔴 #1698 (aipcc-23845) — Ready for review but pre-commit ❌

PR [#1698](https://github.com/Jounce-IO/jounce/pull/1698): isDraft:false (marked ready!). pre-commit ❌ (run 29749885088).
- **Action:** Fix pre-commit to unblock review.

---

### 🆕 #1700 (aipcc-23845-script-runner) + #1701 (aipcc-23845-generator-hotfix) — NEW, split from #1698

PR [#1700](https://github.com/Jounce-IO/jounce/pull/1700): "fix(jbenchmark): script runner and cluster config (AIPCC-23845)" — DRAFT, MERGEABLE
PR [#1701](https://github.com/Jounce-IO/jounce/pull/1701): "fix(jbenchmark): config-generator hotfix (1 of 2, split from #1698)" — DRAFT, MERGEABLE
- Created ~09:48–09:54 IDT Jul 21. Both split from #1698 (AIPCC-23845 cluster connection).
- CI: pre-commit ❌, JIRA Assoc ❌, all-checks ❌ on both. nox ✅, tox ✅.
- Both in NO ZONE — need zone assignment.
- **Action:** Fix pre-commit on both. Assign to appropriate zone (Plan or Code).

---

### 🔴 #1696 (aipcc-23895) — pre-commit ❌ still failing (NOW MERGEABLE)

PR [#1696](https://github.com/Jounce-IO/jounce/pull/1696): DRAFT. pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29741945977).
- **NEW (08:30 IDT):** Now MERGEABLE — was CONFLICTING in prior runs. Conflict resolved.
- **Action:** Fix pre-commit before marking ready.

---

### 🟡 #1695 (aipcc-23925) — CI improved (all-checks now ✅)

PR [#1695](https://github.com/Jounce-IO/jounce/pull/1695): DRAFT. all-checks ✅, pre-commit-run ✅ (run 29741885397). Only JIRA Assoc ❌.
- **Action:** Fix JIRA Association (ensure AIPCC ticket ref in PR title/description), then mark ready.

---

### 🟡 #1670 (jn-5844) — DRAFT (needs mark ready)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md files (JN-5844)"
- State: OPEN, isDraft:true, MERGEABLE, CI all pass (stale).
- **Action:** Mark PR ready for review.

---

### 🟡 Jira Mismatches (7 active — unchanged overnight)

AIPCC-27657 (#1691+#1692 both merged, Jira still In Progress).
Remaining 6: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.
Use `acli jira workitem transition` to update. Jira MCP 401. acli working.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 13+)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Waiting for direction (stale 13+ days)

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### ⚠️ Overnight Session Failures (Jul 17–20)

Multiple consecutive overnight session failures (Jul 17–20). Daytime sessions running correctly.

---

## Archived This Session

No archives this run (10:00 IDT Jul 21 — no merged/closed PRs detected).

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
