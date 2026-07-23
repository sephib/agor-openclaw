# Board State — jounce-workflow-ai

*Last updated: 2026-07-23 10:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | ✅ ALL CI FULLY PASSING run 29729530150 (stale) | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CONFLICTING** (5+ days unchanged). ALL CI 100% PASS. **Action: Rebase aipcc-27645-server-resources on main, then request review.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (frozen) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 23+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 15+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI FULLY PASSING run 29921067106 (stale — pre-16:03 IDT CI) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | 🔴 **NOW CONFLICTING** (regression from 16:03 IDT — was UNKNOWN/ALL-CI-PASS). CI was fully green on run 29921067106 but main advanced after #1704/#1705 merges. **Action: Rebase jn-5844 on main, then open for review.** |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | 🔴 run 29920170788: pre-commit ❌, all-checks ❌; e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, JIRA Assoc ✅ | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🔴 CONFLICTING + pre-commit ❌. **Action: Fix pre-commit + rebase jn-5845-helm-cicd-agents-md.** |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910 (stale): pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — DRAFT. Unchanged. Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 15+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 28+ days. Propose archive. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🔴 CI run 29749885088 — pre-commit ❌, all-checks ❌; JIRA Assoc ✅, nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | isDraft:false. CONFLICTING + pre-commit ❌. **Action: Rebase + fix pre-commit.** |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌; nox ✅, tox ✅ (run 29741945977) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) — In Progress | DRAFT. CI failing: pre-commit ❌. No zone assigned. MERGEABLE. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700 DRAFT](https://github.com/Jounce-IO/jounce/pull/1700) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29808132144); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT split from #1698. MERGEABLE. No zone assigned. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29845259306); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT split from #1698. MERGEABLE. No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | 🟡 all-checks ✅, JIRA Assoc ❌ only (run 29741885397) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT. MERGEABLE. JIRA Assoc ❌ only. **Action: Fix JIRA Assoc, then mark ready.** |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29846894702) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | DRAFT. MERGEABLE. CI failing pre-commit + JIRA Assoc. |

---

## 🆕 New Bot-Authored PRs (Not on Board — Flagged)

| PR | Ticket | State | CI | Notes |
|----|--------|-------|----|-------|
| [#1693](https://github.com/Jounce-IO/jounce/pull/1693) | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | OPEN, APPROVED, NOT draft | 🔴 run 29920192197: **pre-commit ❌**; e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, JIRA Assoc ✅, **e2e-product ✅** | 🔴 **NOW CONFLICTING** (was UNKNOWN MERGEABLE at 16:03). Bot "jira-autofix". APPROVED. Only pre-commit blocks merge + now CONFLICTING. |
| [#1694](https://github.com/Jounce-IO/jounce/pull/1694) | [AIPCC-27681](https://redhat.atlassian.net/browse/AIPCC-27681) | OPEN, CONFLICTING, NOT draft | 🔴 run 29740715467: JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅, e2e ✅ | Bot "jira-autofix". Unchanged. Needs Joseph review. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🟡 **LATEST RUN 29986495648**: JIRA Assoc ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, pre-commit-run ✅, integration ✅, tox ✅, e2e-smoke ✅, nox ✅; **e2e-product PENDING** | **OPEN, 🟢 MERGEABLE** | 🎉 **NEARLY DONE** — new CI run triggered since overnight. All checks pass except e2e-product still PENDING. When e2e-product completes, ready to merge! |

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

*6 mismatches remain (unchanged). Jira MCP 401 — use acli for updates.*

---

## Key Changes (10:30 IDT Jul 23 vs 22:00 IDT Jul 22)

| What changed | Delta |
|---|---|
| **🟡 #1638 (off-board): NEW CI run 29986495648** | Fresh run since overnight. All checks still passing (pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, e2e-smoke ✅, nox ✅, JIRA Assoc ✅). **e2e-product still PENDING**. |
| **🔴 Morning sessions failed (05:00 IDT Jul 23)** | 5 scheduled sessions at 05:00 IDT all failed: Board Advancement, External Sync, Daily Standup, Morning Board Scan. Likely startup issue. Board state unchanged as a result. |
| **All PRs** | No merges. All still CONFLICTING/MERGEABLE same as 22:00 IDT Jul 22. #1690 now 5+ days unchanged. |

---

## Attention Items

### 🟡 #1638 (off-board JN-5725) — NEARLY DONE (e2e-product PENDING)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)"
- State: OPEN, **🟢 MERGEABLE**
- **NEW CI run 29947598648**: JIRA Assoc ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, pre-commit-run ✅, integration ✅, tox ✅, e2e-smoke ✅, nox ✅; **e2e-product PENDING**
- Jira: JN-5725 Done ✅
- **When e2e-product completes → ready to merge!**

---

### 🔴 #1670 (jn-5844) — NOW CONFLICTING (overnight regression)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md files (JN-5844)"
- State: OPEN, **🔴 CONFLICTING** (was UNKNOWN/ALL-CI-PASS at 16:03)
- CI run 29921067106 still shows ALL PASS (stale — main advanced after #1704/#1705 merges overnight)
- **Action: Rebase jn-5844 on main. CI was fully green — should clear quickly after rebase.**

---

### 🔴 #1667 (jn-5845) — CONFLICTING + pre-commit ❌ (unchanged)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **🔴 CONFLICTING**
- CI run 29920170788 COMPLETED: **pre-commit ❌**, all-checks ❌; e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, JIRA Assoc ✅
- **Action: 1) Rebase on main. 2) Fix pre-commit hook failure. Push.**

---

### 🔴 #1693 + #1694 — Bot-Authored PRs Need Review

**[#1693](https://github.com/Jounce-IO/jounce/pull/1693)**: "fix(jbenchmark): add DuplicatePlanNameError for 409 on duplicate plan name AIPCC-27655"
- State: OPEN, **🎉 APPROVED**, **🔴 CONFLICTING** (regression from 16:03)
- CI run 29920192197: **pre-commit ❌** still failing; all others ✅ including e2e-product ✅
- **Action:** Rebase + Fix pre-commit — that's all blocking merge.

**[#1694](https://github.com/Jounce-IO/jounce/pull/1694)**: "fix(jbenchmark): share MetadataResolver across gpu_count iterations (AIPCC-27681)"
- State: OPEN, CONFLICTING, NOT draft
- CI run 29740715467: JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅, e2e ✅
- **Action:** Review PR. Rebase on main. Fix JIRA Assoc + pre-commit.

---

### 🔴 #1690 (aipcc-27645) — ALL CI PASSING BUT CONFLICTING (5+ days)

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645)"
- State: OPEN, **CONFLICTING** 🔴 (5+ days unchanged)
- Run 29729530150 — ALL CHECKS PASS
- **Action:** Rebase aipcc-27645-server-resources on main, then request review.

---

### 🔴 #1669 (jn-5872) — CI FAILING + CONFLICTING (unchanged)

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, DRAFT, **CONFLICTING** 🔴
- Run 29683534910 (stale): pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌
- **Action:** 1) Rebase on main. 2) Fix pre-commit + nox + tox-run.

---

### 🔴 #1698 (aipcc-23845) — DOUBLE-BLOCKED: CONFLICTING + pre-commit ❌

PR [#1698](https://github.com/Jounce-IO/jounce/pull/1698): isDraft:false (ready for review). CONFLICTING. pre-commit ❌ (run 29749885088).
- **Action:** 1) Rebase on main. 2) Fix pre-commit.

---

### 🔴 #1700 + #1701 (aipcc-23845 splits) — pre-commit ❌, NO ZONE

PR [#1700](https://github.com/Jounce-IO/jounce/pull/1700): DRAFT. MERGEABLE. pre-commit ❌, JIRA Assoc ❌, all-checks ❌.
PR [#1701](https://github.com/Jounce-IO/jounce/pull/1701): DRAFT. MERGEABLE. pre-commit ❌, JIRA Assoc ❌, all-checks ❌.
- **Action:** Fix pre-commit on both. Assign to appropriate zone.

---

### 🟡 #1696 (aipcc-23895) — JIRA Assoc only

PR [#1696](https://github.com/Jounce-IO/jounce/pull/1696): DRAFT, MERGEABLE. CI run 29741885397: all-checks ✅, JIRA Assoc ❌ only.
- **Action:** Fix JIRA Association, then mark ready for review.

---

### 🟡 #1695 (aipcc-23925) — MERGEABLE + CI failing

PR [#1695](https://github.com/Jounce-IO/jounce/pull/1695): DRAFT. MERGEABLE. CI run 29846894702: pre-commit ❌, JIRA Assoc ❌, all-checks ❌.
- **Action:** Fix pre-commit AND JIRA Association, then mark ready.

---

### 🟡 Jira Mismatches (6 active — unchanged)

6 mismatches: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546. Use `acli jira workitem transition` to update.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 15+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Waiting for direction (stale 14+ days)

Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

---

## Archived This Session

None — no MERGED/CLOSED PRs found overnight.

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **35 Danger Delete Zone** | various MERGED/CLOSED | Mass cleanup | 10:33 IDT Jul 22 |
| **jn-5132-refactor-run-jbenchmark-script-to-support** | [#1457 CLOSED](https://github.com/Jounce-IO/jounce/pull/1457) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **jn-5246-exp-plan-modelcar** | [#1466 CLOSED](https://github.com/Jounce-IO/jounce/pull/1466) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **aipcc-27657-guidellm-output-dir** | [#1691 MERGED](https://github.com/Jounce-IO/jounce/pull/1691) | PR #1691 MERGED Jul 20 | 10:10 IDT Jul 20 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1704](https://github.com/Jounce-IO/jounce/pull/1704) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **14:14 IDT Jul 22** 🎉 | Off-board. JN-5725 Done ✅. |
| [#1705](https://github.com/Jounce-IO/jounce/pull/1705) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **11:20 IDT Jul 22** 🎉 | Off-board. JN-5725 Done ✅. |
| [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **10:20 IDT Jul 20** 🎉 | ARCHIVED 10:10 IDT Jul 20. |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **09:36 IDT Jul 20** 🎉 | Off-board companion PR. |
| [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) | **14:14 IDT Jul 16** 🎉 | ARCHIVED 14:45 Jul 16. JN-5891 Done ✅. |
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | JN-5867 Done ✅ |
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | 17:53 IDT Jul 14 🎉 | ARCHIVED 19:30 Jul 14. JN-5870 Done ✅ |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) | 13:29 IDT Jul 14 🎉 | ARCHIVED 13:30 Jul 14 |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | 12:20 IDT Jul 14 🎉 | ARCHIVED 12:30 Jul 14. JN-5880 Done ✅ |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
