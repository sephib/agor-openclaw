# Board State — jounce-workflow-ai

*Last updated: 2026-07-26 21:00 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 run 30207422955: pre-commit ❌, JIRA Assoc ❌; e2e-product ✅, e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅, atlas-validate ✅; all-checks ❌ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CHANGES_REQUESTED by MenD32**. pre-commit ❌ + JIRA Assoc ❌ unchanged. **Action: Address reviewer feedback + fix pre-commit/JIRA Assoc.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (frozen) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 26+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 18+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | 🟡 run 30207532827: JIRA Assoc ❌ (still); e2e-api ✅, e2e-smoke ✅, pre-commit ✅, integration ✅, tox ✅, nox ✅; **all-checks ✅** | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) / AIPCC-26990 — In Progress | 🟡 JIRA Assoc ❌ still blocking. all-checks ✅. **Action: Fix JIRA Assoc, then request review.** |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | 🟡 run 30207429826: pre-commit ❌, JIRA Assoc ❌; e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅ | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) / AIPCC-26996 — Review | 🟡 **pre-commit ❌ + JIRA Assoc ❌ unchanged.** **Action: Fix pre-commit + JIRA Assoc hook failures.** |
| jn-5872 | **Code** | [#1669 DRAFT](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910 (stale): pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + CONFLICTING** — DRAFT. Unchanged. Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 18+** (still Ingest, should be Code). |
| ~~jira-operations~~ | ~~NO ZONE~~ | — | — | — | ✅ **ARCHIVED 21:02 IDT Jul 26** — stale 31+ days, no PR, no zone. |
| aipcc-27994-faulty-column | **Code Review** | [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | 🔴 run 30207527731: **e2e-api ❌ FAILED** (still), e2e-tests ❌, all-checks ❌; JIRA Assoc ✅, pre-commit ✅, atlas-validate ✅, atlas-validate-run ✅, integration ✅, tox ✅, nox ✅, deploy ✅ | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) — New | 🔴 **e2e-api FAILED** — REGRESSION persists (new run, same result). Needs investigation. |
| aipcc-27996-faulty-export-cache | **Verify** | — | — | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) — New | No sessions yet. No PR. Stale. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🔴 run 29749885088 — pre-commit ❌, all-checks ❌; JIRA Assoc ✅, nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | isDraft:false. UNKNOWN mergeable. pre-commit ❌. **Action: Fix pre-commit.** |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌; nox ✅, tox ✅ (run 29741945977) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) — In Progress | DRAFT. CI failing: pre-commit ❌. No zone assigned. UNKNOWN mergeable. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700](https://github.com/Jounce-IO/jounce/pull/1700) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29808132144); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | NOT DRAFT. UNKNOWN mergeable. No zone assigned. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29845259306); nox ✅, tox ✅ | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT. UNKNOWN mergeable. No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | 🟡 all-checks ✅, JIRA Assoc ❌ only (run 29741885397) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT. UNKNOWN mergeable. JIRA Assoc ❌ only. **Action: Fix JIRA Assoc, then mark ready.** |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | 🔴 pre-commit ❌, JIRA Assoc ❌, all-checks ❌ (run 29846894702) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | DRAFT. UNKNOWN mergeable. CI failing pre-commit + JIRA Assoc. |

---

## 🆕 New Bot-Authored PRs (Not on Board — Flagged)

| PR | Ticket | State | CI | Notes |
|----|--------|-------|----|-------|
| ~~[#1693](https://github.com/Jounce-IO/jounce/pull/1693)~~ | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **MERGED 15:02 IDT Jul 26** 🎉 | — | Bot PR merged. AIPCC-27655 resolved. |
| [#1694](https://github.com/Jounce-IO/jounce/pull/1694) | [AIPCC-27681](https://redhat.atlassian.net/browse/AIPCC-27681) | OPEN, UNKNOWN mergeable, NOT draft | 🔴 run 29740715467 (stale): JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅, e2e ✅ | Bot "jira-autofix". Unchanged. Needs Joseph review. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🟡 run 30202214886 (NEW): JIRA Assoc ✅, atlas-validate ✅, check-changes ✅; pre-commit PENDING, e2e-api PENDING, integration PENDING, tox PENDING | **OPEN, MERGEABLE** | 🟡 New CI run triggered. JIRA Assoc ✅ holding. Core checks still PENDING. JN-5725 Done ✅. |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | — | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | — | **MERGED 12:44 IDT Jul 26** 🎉 | Off-board. Merged today. "feat(jbenchmark): expose HF metadata fields in inference model API" |
| [#1716](https://github.com/Jounce-IO/jounce/pull/1716) | — | [AIPCC-28110](https://redhat.atlassian.net/browse/AIPCC-28110) | — | OPEN, NOT draft | New off-board PR (not Joseph's). Monitoring only. |

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
| AIPCC-23882 | New | [DEV] Integrate IBM cluster support into runner main (new — no worktree) |
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
| **[AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994)** | [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | OPEN (Code Review) | **New** | ❌ Update Jira → In Review |
| **[AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996)** | — | No PR (Verify) | **New** | ❌ Update Jira → In Progress |

*8 mismatches total — unchanged. Use `acli jira workitem transition` to update.*

---

## Key Changes (21:00 IDT Jul 26 advance vs 15:30 IDT Jul 26 advance)

| What changed | Delta |
|---|---|
| **#1693 MERGED** 🎉 | Bot PR (AIPCC-27655) **MERGED 15:02 IDT Jul 26** — was OPEN+APPROVED+CONFLICTING at last run. Resolved. |
| **jira-operations ARCHIVED** | Stale 31+ days, no PR, no zone — archived autonomously 21:02 IDT Jul 26. |
| **#1713 CI** | 🔴 New run 30207527731 — e2e-api ❌ STILL FAILING. No improvement since 15:30. |
| **#1670 CI** | 🟡 New run 30207532827 — JIRA Assoc ❌ still only blocker. all-checks ✅ unchanged. |
| **#1690 CI** | 🔴 New run 30207422955 — pre-commit ❌ + JIRA Assoc ❌ unchanged. |
| **#1667 CI** | 🟡 New run 30207429826 — pre-commit ❌ + JIRA Assoc ❌ unchanged. |
| **#1638 CI** | 🔴 **NEW FAILURE** — run 30207418279: **e2e-smoke ❌ FAILED** (was PENDING). e2e-tests ❌, all-checks ❌. e2e-api ✅, pre-commit ✅, JIRA Assoc ✅. |

---

## Attention Items

### 🔴 #1713 (AIPCC-27994) — e2e-api FAILED — REGRESSION PERSISTS

PR [#1713](https://github.com/Jounce-IO/jounce/pull/1713)
- State: OPEN, **🟢 MERGEABLE**, NOT DRAFT, reviewDecision: ""
- **CI run 30207527731** (new): **e2e-api ❌ FAILED**, e2e-tests ❌, all-checks ❌; JIRA Assoc ✅, pre-commit ✅, atlas-validate ✅, atlas-validate-run ✅, integration ✅, tox ✅, nox ✅, deploy ✅
- **e2e-api FAILED in both 15:30 and 21:00 runs. Action: Investigate e2e-api failure URGENTLY.**

---

### 🟡 #1670 (jn-5844) — JIRA Assoc ❌ Only Blocker

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670)
- State: OPEN, **🟢 MERGEABLE**, NOT DRAFT, reviewDecision: REVIEW_REQUIRED
- **CI run 30207532827** (new): JIRA Assoc ❌ still failing; e2e-api ✅, e2e-smoke ✅, pre-commit ✅, integration ✅, tox ✅, nox ✅; all-checks ✅
- JIRA Assoc ❌ is the single remaining blocker.
- **Action: Fix JIRA Assoc regression, then request review.**

---

### 🔴 #1690 (AIPCC-27645) — CHANGES_REQUESTED + CI FAILING

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645)"
- **State: OPEN, 🟢 MERGEABLE, NOT DRAFT, CHANGES_REQUESTED by MenD32**
- **CI run 30207422955** (new): pre-commit ❌, JIRA Assoc ❌; e2e-product ✅, e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, atlas-validate ✅
- **Action: Joseph to review MenD32 feedback + fix pre-commit + JIRA Assoc**

---

### 🟡 #1667 (jn-5845) — pre-commit ❌ + JIRA Assoc ❌

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667)
- CI run 30207429826 (new): pre-commit ❌, JIRA Assoc ❌; e2e-smoke ✅, e2e-api ✅, integration ✅
- **Action: Fix pre-commit + JIRA Assoc hook failures.**

---

### 🎉 #1693 (AIPCC-27655) — MERGED 15:02 IDT Jul 26

PR [#1693](https://github.com/Jounce-IO/jounce/pull/1693) — bot PR (jira-autofix) — **MERGED**
- Was APPROVED+CONFLICTING at last run (15:30). Merged at 15:02 IDT today.
- No Agor worktree to archive (was a bot-authored PR).

---

### 🔴 #1638 (off-board JN-5725) — e2e-smoke FAILED

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638)
- State: OPEN, MERGEABLE
- **CI run 30207418279** (new): **e2e-smoke ❌ FAILED** (was PENDING), e2e-tests ❌, all-checks ❌; e2e-api ✅, pre-commit ✅, JIRA Assoc ✅
- JN-5725 is Done ✅. **Action: Investigate e2e-smoke failure. Consider closing PR if ticket Done.**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 18+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Stale (18+ days, no PR)

Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### 🟡 Jira Mismatches (8 active — unchanged)

8 mismatches: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546, AIPCC-27994 (→In Review), AIPCC-27996 (→In Progress). Use `acli jira workitem transition` to update.

---

## Archived This Session

| Branch | Reason | Time |
|--------|--------|------|
| **jira-operations** | Stale 31+ days, no PR, no zone — autonomous archive | 21:02 IDT Jul 26 |

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
| [#1693](https://github.com/Jounce-IO/jounce/pull/1693) | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **15:02 IDT Jul 26** 🎉 | Bot PR (jira-autofix). "fix(jbenchmark): add DuplicatePlanNameError for 409". No Agor worktree. |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | **12:44 IDT Jul 26** 🎉 | Off-board. "feat(jbenchmark): expose HF metadata fields". |
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
