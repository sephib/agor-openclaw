# Board State — jounce-workflow-ai

*Last updated: 2026-07-28 09:31 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 run 30278052480: pre-commit ❌, JIRA Assoc ❌, e2e-api ❌, all-checks ❌; e2e-product ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, atlas-validate ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CHANGES_REQUESTED by MenD32**. pre-commit ❌ + JIRA Assoc ❌ + e2e-api ❌. **Action: Address reviewer feedback + fix CI.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 28+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. Needs: configs, rebase, PR. Stale 20+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | 🟢 run 30278289196: ALL CHECKS ✅ (JIRA Assoc ✅, pre-commit ✅, e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, deploy ✅, all-checks ✅) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) / AIPCC-26990 — In Progress | 🟢 **CI ALL GREEN**. reviewDecision: REVIEW_REQUIRED. **Action: Request review — all blockers resolved.** |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | 🔴 run 30278034133: pre-commit ❌, JIRA Assoc ❌, nox ❌, tox ❌, all-checks ❌ | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) / AIPCC-26996 — Review | 🔴 **CI DEGRADED** — new failures: nox ❌ + tox ❌ added to pre-commit ❌ + JIRA Assoc ❌. **Action: Rebase on main + fix CI.** |
| jn-5872 | **Code** | [#1669 DRAFT](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 30278029097: JIRA Assoc ❌, pre-commit ❌, all-checks ❌; nox ✅, tox ✅ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌** — DRAFT. Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 20+** (still Ingest, should be Code). |
| ~~aipcc-27994-faulty-column~~ | ~~Code Review~~ | [#1713 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1713) | — | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) | ✅ **PR #1713 MERGED 12:54 IDT Jul 27**. No Agor branch record — already cleaned. |
| aipcc-27996-faulty-export-cache | **Verify** | — | — | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) — New | No sessions yet. No PR. Stale 5 days. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🟡 JIRA Assoc ❌ only (run 30195280911) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | OPEN, MERGEABLE, not draft, reviewDecision: "". JIRA Assoc ❌ only. |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | REVIEW_REQUIRED (draft) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) | DRAFT. No zone assigned. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700](https://github.com/Jounce-IO/jounce/pull/1700) | CodeRabbit ✅ only | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | NOT DRAFT. MERGEABLE. No zone. No CI runs triggered yet. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | REVIEW_REQUIRED (draft) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT. No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | REVIEW_REQUIRED (draft) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT. No zone. |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | REVIEW_REQUIRED (draft) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | DRAFT. No zone. |

---

## 🆕 New Bot-Authored PRs (Not on Board — Flagged)

| PR | Ticket | State | CI | Notes |
|----|--------|-------|----|-------|
| ~~[#1693](https://github.com/Jounce-IO/jounce/pull/1693)~~ | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **MERGED 15:02 IDT Jul 26** 🎉 | — | Bot PR merged. AIPCC-27655 resolved. |
| [#1694](https://github.com/Jounce-IO/jounce/pull/1694) | [AIPCC-27681](https://redhat.atlassian.net/browse/AIPCC-27681) | OPEN, MERGEABLE, NOT draft, REVIEW_REQUIRED | CodeRabbit only (bot ineligible) | Bot "jira-autofix". Needs Joseph review. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | AIPCC-28249 | 🟢 run 30296923601: **ALL CHECKS ✅** (e2e-api ✅, e2e-smoke ✅, e2e-product ✅, pre-commit ✅, JIRA Assoc ✅, integration ✅, tox ✅, nox ✅, all-checks ✅) | **OPEN, MERGEABLE** | 🟢 **CI CLEARED**. e2e-smoke was failing last run — now passing. reviewDecision: "". |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | — | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | — | **MERGED 12:44 IDT Jul 26** 🎉 | Off-board. Merged. |
| [#1716](https://github.com/Jounce-IO/jounce/pull/1716) | — | [AIPCC-28110](https://redhat.atlassian.net/browse/AIPCC-28110) | — | OPEN, NOT draft, REVIEW_REQUIRED | Off-board. Monitoring only. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Waiting/Blocked | Refactor run_jbenchmark script to support redesign flow |
| [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | New | Add subcommands to runner — PR #1654 MERGED Jul 12, Jira stale! |
| [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | In Progress | Add CLI flags |
| [JN-4393](https://redhat.atlassian.net/browse/JN-4393) | In Progress | Upgrade AGENTS.md Standard |
| [JN-5851](https://redhat.atlassian.net/browse/JN-5851) | New | Implement v0.7.0 Container Image & Argo Integration |
| [JN-5852](https://redhat.atlassian.net/browse/JN-5852) | New | Implement v0.7.0 Report Ingestion |
| AIPCC-23882 | New | [DEV] Integrate IBM cluster support into runner main |
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
| **[AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994)** | [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | **MERGED 12:54 IDT Jul 27** | **New** | ❌ Update Jira → Done |
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** / AIPCC-26976 | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED Jul 14** | **New** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED Jul 12** | **New** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **New** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| **[AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996)** | — | No PR (Verify) | **New** | ❌ Update Jira → In Progress |

*8 mismatches total (AIPCC-27994 added, count unchanged). Use `acli jira workitem transition` to update.*

---

## Key Changes (09:31 IDT Jul 28 vs 08:30 IDT Jul 27)

| What changed | Delta |
|---|---|
| **🎉 PR #1713 MERGED** | AIPCC-27994 merged 12:54 IDT Jul 27. No Agor branch to archive (was not tracked as Agor worktree). Jira mismatch added. |
| **🟢 #1638 CI CLEARED** | Was e2e-smoke ❌ — now ALL GREEN (run 30296923601). |
| **🟢 #1670 CI CLEARED** | Was JIRA Assoc ❌ — now ALL GREEN (run 30278289196, JIRA Assoc ✅). Ready for review request. |
| **🔴 #1667 CI DEGRADED** | Was pre-commit ❌ + JIRA Assoc ❌ — now also nox ❌ + tox ❌ (run 30278034133). Needs rebase. |
| **🔴 #1690 CI** | Was pre-commit ❌ + JIRA Assoc ❌ — now also e2e-api ❌ added (run 30278052480). CHANGES_REQUESTED unchanged. |
| **Multiple morning sessions failed** | Sessions at 05:00, 05:30, 06:00 IDT all failed. This 09:30 IDT session is first to succeed today. |
| **aipcc-27996 stays on board** | Restored after accidental archive. No PR, Verify zone, stale 5 days. |

---

## Attention Items

### 🎉 PR #1713 (AIPCC-27994) — MERGED

PR [#1713](https://github.com/Jounce-IO/jounce/pull/1713) — "feat(jbenchmark): add is_faulty column, PATCH endpoint, and list filtering"
- **MERGED 12:54 IDT Jul 27**. APPROVED.
- No Agor branch record existed — no archive action needed.
- **Action: Update Jira AIPCC-27994 → Done.**

---

### 🟢 #1670 (jn-5844) — CI ALL GREEN — Request Review

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670)
- State: OPEN, MERGEABLE, NOT DRAFT, reviewDecision: REVIEW_REQUIRED
- **CI run 30278289196**: ALL CHECKS ✅ — JIRA Assoc ✅, pre-commit ✅, e2e-api ✅, e2e-smoke ✅, integration ✅, tox ✅, nox ✅, deploy ✅, all-checks ✅
- **Action: Request review — PR is ready.**

---

### 🔴 #1690 (AIPCC-27645) — CHANGES_REQUESTED + CI DEGRADED

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances"
- **State: OPEN, MERGEABLE, NOT DRAFT, CHANGES_REQUESTED by MenD32**
- **CI run 30278052480**: pre-commit ❌, JIRA Assoc ❌, e2e-api ❌, all-checks ❌; e2e-smoke ✅, integration ✅, tox ✅, nox ✅
- New: e2e-api failure added since last scan.
- **Action: Address MenD32 review feedback + fix CI failures.**

---

### 🔴 #1667 (jn-5845) — CI DEGRADED (nox + tox now failing)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667)
- **CI run 30278034133**: pre-commit ❌, JIRA Assoc ❌, nox ❌, tox ❌, all-checks ❌
- **Degraded since last scan** — now 4 failing checks vs 2 before.
- **Action: Rebase on main + fix all CI failures.**

---

### 🟢 #1638 (off-board AIPCC-28249) — CI CLEARED

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638)
- Was e2e-smoke ❌ FAILED — now **ALL GREEN** (run 30296923601).
- State: OPEN, MERGEABLE, reviewDecision: "".
- **Action: Ready for review request.**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 20+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Stale (20+ days, no PR)

Last session Jul 8 IDLE.
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### 🟡 Jira Mismatches (8 active)

8 mismatches: AIPCC-27994 (→Done), JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546, AIPCC-27996 (→In Progress).

---

## Archived This Session

| Branch | Reason | Time |
|--------|--------|------|
| *(accidental archive of aipcc-27996-faulty-export-cache — immediately restored)* | Error — unarchived | 09:32 IDT Jul 28 |

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jira-operations** | — | Stale 31+ days, no PR, no zone | 21:02 IDT Jul 26 |
| **35 Danger Delete Zone** | various MERGED/CLOSED | Mass cleanup | 10:33 IDT Jul 22 |
| **jn-5132-refactor-run-jbenchmark-script-to-support** | [#1457 CLOSED](https://github.com/Jounce-IO/jounce/pull/1457) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **jn-5246-exp-plan-modelcar** | [#1466 CLOSED](https://github.com/Jounce-IO/jounce/pull/1466) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **aipcc-27657-guidellm-output-dir** | [#1691 MERGED](https://github.com/Jounce-IO/jounce/pull/1691) | PR #1691 MERGED Jul 20 | 10:10 IDT Jul 20 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) | **12:54 IDT Jul 27** 🎉 | "feat(jbenchmark): add is_faulty column, PATCH endpoint, and list filtering". No Agor branch. |
| [#1693](https://github.com/Jounce-IO/jounce/pull/1693) | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **15:02 IDT Jul 26** 🎉 | Bot PR (jira-autofix). No Agor worktree. |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | **12:44 IDT Jul 26** 🎉 | Off-board. |
| [#1704](https://github.com/Jounce-IO/jounce/pull/1704) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **14:14 IDT Jul 22** 🎉 | Off-board. |
| [#1705](https://github.com/Jounce-IO/jounce/pull/1705) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **11:20 IDT Jul 22** 🎉 | Off-board. |
| [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **10:20 IDT Jul 20** 🎉 | ARCHIVED. |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **09:36 IDT Jul 20** 🎉 | Off-board companion PR. |
| [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) | **14:14 IDT Jul 16** 🎉 | ARCHIVED. |
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | Done ✅ |
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | **17:53 IDT Jul 14** 🎉 | ARCHIVED. |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) | **13:29 IDT Jul 14** 🎉 | ARCHIVED. |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | **12:20 IDT Jul 14** 🎉 | ARCHIVED. |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
