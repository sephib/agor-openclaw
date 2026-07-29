# Board State — jounce-workflow-ai

*Last updated: 2026-07-29 08:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 pre-commit ❌, e2e-product ❌, JIRA Assoc ❌; e2e-api ✅, tox ✅, integration ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CHANGES_REQUESTED by MenD32**. CI run completed with failures (pre-commit, e2e-product, JIRA Assoc). **Action: Address reviewer feedback + fix CI.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 29+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. Needs: configs, rebase, PR. Stale 21+ days. |
| ~~jn-5844-service-lib-sql-agents-md~~ | ~~Publish~~ | [#1670 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1670) | — | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) / AIPCC-26990 | ✅ **PR #1670 MERGED 16:03 IDT Jul 28**. Worktree ARCHIVED autonomously 18:04 IDT Jul 28. Jira → Done needed. |
| ~~jn-5845-helm-cicd-agents-md~~ | ~~Publish~~ | [#1667 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1667) | — | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | ✅ **PR #1667 MERGED 14:12 IDT Jul 28**. Worktree ARCHIVED autonomously. Jira → Done needed. |
| jn-5872 | **Code** | [#1669 DRAFT](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 JIRA Assoc ❌; resolve-conflicts ✅ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌** — DRAFT. Needs rebase + CI fix. Unchanged overnight. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 21+** (still Ingest, should be Code). |
| ~~aipcc-27994-faulty-column~~ | ~~Code Review~~ | [#1713 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1713) | — | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) | ✅ **PR #1713 MERGED 12:54 IDT Jul 27**. No Agor branch record — already cleaned. |
| ~~aipcc-27996-faulty-export-cache~~ | ~~Verify~~ | [#1723 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1723) | — | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) | ✅ **PR #1723 MERGED 11:31 IDT Jul 28**. No Agor worktree to archive. Jira → Done needed. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🟡 JIRA Assoc ❌ only (run 30195280911) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | OPEN, MERGEABLE, not draft, reviewDecision: "". JIRA Assoc ❌ only. Unchanged. |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | REVIEW_REQUIRED (draft) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) | DRAFT. No zone assigned. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700](https://github.com/Jounce-IO/jounce/pull/1700) | CodeRabbit ✅ only | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | NOT DRAFT. MERGEABLE. No zone. No full CI runs triggered yet. |
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
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | AIPCC-28249 | 🔴 e2e-product ❌; JIRA Assoc ✅, pre-commit ✅, tox ✅, integration ✅, e2e-api ✅, e2e-smoke ✅ | **OPEN, MERGEABLE** | 🔴 e2e-product ❌ is the sole remaining CI blocker. reviewDecision: "". |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | — | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | — | **MERGED 12:44 IDT Jul 26** 🎉 | Off-board. Merged. |
| [#1716](https://github.com/Jounce-IO/jounce/pull/1716) | — | [AIPCC-28110](https://redhat.atlassian.net/browse/AIPCC-28110) | — | OPEN, NOT draft, REVIEW_REQUIRED | Off-board. Monitoring only. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [AIPCC-28413](https://redhat.atlassian.net/browse/AIPCC-28413) | New | [DEV] Write api_server request/response schema conventions in AGENTS.md |
| [AIPCC-28289](https://redhat.atlassian.net/browse/AIPCC-28289) | New | Write UI requirements document based on spike findings |
| [AIPCC-23298](https://redhat.atlassian.net/browse/AIPCC-23298) | New | Implement v0.7.0 Container Image & Argo Integration |
| [AIPCC-23308](https://redhat.atlassian.net/browse/AIPCC-23308) | New | Implement v0.7.0 Report Ingestion |
| [AIPCC-23215](https://redhat.atlassian.net/browse/AIPCC-23215) | New | [DEV] Execute and monitor benchmark runs on IBM cluster |
| [AIPCC-23253](https://redhat.atlassian.net/browse/AIPCC-23253) | New | [DOCS] Update apps/jbenchmark/README.md for IBM cluster |
| [AIPCC-23157](https://redhat.atlassian.net/browse/AIPCC-23157) | New | [DOCS] Dashboard README and setup instructions |
| [AIPCC-23788](https://redhat.atlassian.net/browse/AIPCC-23788) | New | Add subcommands to jbenchmark runner for stage-level modular execution |
| [AIPCC-23882](https://redhat.atlassian.net/browse/AIPCC-23882) | New | [DEV] Integrate IBM cluster support into runner main |
| [AIPCC-23647](https://redhat.atlassian.net/browse/AIPCC-23647) | In Progress | Dependency & Build Standardization |
| [AIPCC-23857](https://redhat.atlassian.net/browse/AIPCC-23857) | In Progress | Refactor run_jbenchmark script to support redesign flow |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5844](https://redhat.atlassian.net/browse/JN-5844)** | [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | **MERGED 16:03 IDT Jul 28** | In Progress | ❌ Update Jira → Done |
| **[AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996)** | [#1723](https://github.com/Jounce-IO/jounce/pull/1723) | **MERGED 11:31 IDT Jul 28** | **New** | ❌ Update Jira → Done |
| **[AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994)** | [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | **MERGED 12:54 IDT Jul 27** | **New** | ❌ Update Jira → Done |
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** / AIPCC-26976 | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED Jul 14** | **New** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED Jul 12** | **New** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **New** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |
| **[JN-5845](https://redhat.atlassian.net/browse/JN-5845)** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | **MERGED 14:12 IDT Jul 28** | **Review** | ❌ Update Jira → Done |

*10 mismatches total (unchanged). Use `acli jira workitem transition` to update.*

---

## Key Changes (08:30 IDT Jul 29 vs 18:00 IDT Jul 28)

| What changed | Delta |
|---|---|
| **Board static overnight** | No new merges. All PRs in same state. |
| **🔴 #1690 CI run completed** | pre-commit ❌, e2e-product ❌, JIRA Assoc ❌ (was "new run PENDING"). CHANGES_REQUESTED persists. |
| **🔴 #1638 CI run completed** | e2e-product ❌ sole blocker; all other checks pass (JIRA Assoc now ✅). |
| **🟡 BOARD_STATE.md was 14h old** | Full refresh performed. |

---

## Attention Items

### 🔴 #1690 (AIPCC-27645) — CHANGES_REQUESTED + CI failing

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances"
- **State: OPEN, MERGEABLE, NOT DRAFT, CHANGES_REQUESTED by MenD32**
- CI run completed: pre-commit ❌, e2e-product ❌, JIRA Assoc ❌
- **Action: Address MenD32 review feedback + fix pre-commit.**

---

### 🎉 PR #1670 (JN-5844) — MERGED — Worktree ARCHIVED

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670) — "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md"
- **MERGED 16:03 IDT Jul 28**. APPROVED.
- Worktree `jn-5844-service-lib-sql-agents-md` **ARCHIVED autonomously** at 18:04 IDT Jul 28.
- **Action: Update Jira JN-5844 → Done.**

---

### 🎉 PR #1723 (AIPCC-27996) — MERGED

PR [#1723](https://github.com/Jounce-IO/jounce/pull/1723) — "feat(jbenchmark): exclude faulty experiments from export and cache lookups"
- **MERGED 11:31 IDT Jul 28**. APPROVED.
- No Agor worktree to archive.
- **Action: Update Jira AIPCC-27996 → Done.**

---

### 🎉 PR #1667 (JN-5845) — MERGED — Worktree ARCHIVED

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667) — "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files"
- **MERGED 14:12 IDT Jul 28**. APPROVED.
- Worktree ARCHIVED autonomously (previous run).
- **Action: Update Jira JN-5845 → Done.**

---

### 🔴 #1694 (AIPCC-27681) — BOT PR needs review

PR [#1694](https://github.com/Jounce-IO/jounce/pull/1694) — "fix(jbenchmark): share MetadataResolver across gpu_count iterations"
- OPEN, MERGEABLE, NOT DRAFT, REVIEW_REQUIRED. Bot PR (jira-autofix).
- **Action: Joseph review.**

---

### 🔴 #1638 (off-board AIPCC-28249) — e2e-product ❌ sole blocker

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638)
- State: OPEN, MERGEABLE, reviewDecision: "".
- CI: e2e-product ❌; all others pass (JIRA Assoc ✅ now).
- **Action: Investigate e2e-product failure.**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 21+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Stale (21+ days, no PR)

Last session Jul 8 IDLE.
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### 🟡 Jira Mismatches (10 active)

10 mismatches: JN-5844 (→Done), AIPCC-27996 (→Done), AIPCC-27994 (→Done), JN-5845 (→Done), JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.

---

## Archived This Session

No archives this run.

Previously archived:
| Branch | PR | Reason | Time |
|--------|-----|--------|------|
| **jn-5844-service-lib-sql-agents-md** | [#1670 MERGED](https://github.com/Jounce-IO/jounce/pull/1670) | PR MERGED 16:03 IDT Jul 28 | 18:04 IDT Jul 28 |
| **jn-5845-helm-cicd-agents-md** | [#1667 MERGED](https://github.com/Jounce-IO/jounce/pull/1667) | PR MERGED 14:12 IDT Jul 28 | 17:33 IDT Jul 28 |
| **jira-operations** | — | Stale 31+ days, no PR, no zone | 21:02 IDT Jul 26 |
| **35 Danger Delete Zone** | various MERGED/CLOSED | Mass cleanup | 10:33 IDT Jul 22 |
| **jn-5132-refactor-run-jbenchmark-script-to-support** | [#1457 CLOSED](https://github.com/Jounce-IO/jounce/pull/1457) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **jn-5246-exp-plan-modelcar** | [#1466 CLOSED](https://github.com/Jounce-IO/jounce/pull/1466) | PR CLOSED May 31 | 12:30 IDT Jul 21 |
| **aipcc-27657-guidellm-output-dir** | [#1691 MERGED](https://github.com/Jounce-IO/jounce/pull/1691) | PR #1691 MERGED Jul 20 | 10:10 IDT Jul 20 |

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) | **16:03 IDT Jul 28** 🎉 | "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md". Worktree ARCHIVED. |
| [#1723](https://github.com/Jounce-IO/jounce/pull/1723) | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) | **11:31 IDT Jul 28** 🎉 | "feat(jbenchmark): exclude faulty experiments from export and cache lookups". No Agor worktree. |
| [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | **14:12 IDT Jul 28** 🎉 | "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files". Worktree ARCHIVED. |
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
