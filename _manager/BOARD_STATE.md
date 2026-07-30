# Board State — jounce-workflow-ai

*Last updated: 2026-07-31 10:15 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 pre-commit ❌, JIRA Assoc ❌, e2e-product ❌; nox ✅, e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅ (**NEW run 30548288372**) | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) — In Progress | 🔴 **CHANGES_REQUESTED by MenD32**. MERGEABLE. CI re-ran — same failures. **Action: Address reviewer feedback + fix pre-commit + investigate e2e-product.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — In Progress | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 31+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) / [AIPCC-23249](https://redhat.atlassian.net/browse/AIPCC-23249) — In Progress | Last session Jul 8 IDLE. Needs: configs, rebase, PR. Stale 23+ days. |
| ~~jn-5844-service-lib-sql-agents-md~~ | ~~Publish~~ | [#1670 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1670) | — | [AIPCC-26990](https://redhat.atlassian.net/browse/AIPCC-26990) — **Closed** ✅ | ✅ **PR #1670 MERGED 16:03 IDT Jul 28**. Worktree ARCHIVED. Jira now Closed. |
| ~~jn-5845-helm-cicd-agents-md~~ | ~~Publish~~ | [#1667 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1667) | — | [AIPCC-26996](https://redhat.atlassian.net/browse/AIPCC-26996) — **Closed** ✅ | ✅ **PR #1667 MERGED 14:12 IDT Jul 28**. Worktree ARCHIVED. Jira now Closed. |
| jn-5872 | **Code** | [#1669 DRAFT](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 CONFLICTING | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **DRAFT + CONFLICTING**. tox-run ❌, nox ❌, pre-commit ❌ (unchanged). Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 23+** (still Ingest, should be Code). |
| ~~aipcc-27994-faulty-column~~ | ~~Code Review~~ | [#1713 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1713) | — | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) — **Closed** ✅ | ✅ **PR #1713 MERGED 12:54 IDT Jul 27**. No Agor branch record — already cleaned. Jira now Closed. |
| ~~aipcc-27996-faulty-export-cache~~ | ~~Verify~~ | [#1723 **MERGED**](https://github.com/Jounce-IO/jounce/pull/1723) | — | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) — **Closed** ✅ | ✅ **PR #1723 MERGED 11:31 IDT Jul 28**. No Agor worktree. Jira now Closed. |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🟡 CONFLICTING (JIRA Assoc ❌ only; stale run from Jul 20) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) — New | OPEN, **CONFLICTING**, not draft. Needs rebase + JIRA Assoc fix. |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | REVIEW_REQUIRED (draft) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) — In Progress | DRAFT. No zone assigned. Jira = In Progress. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700](https://github.com/Jounce-IO/jounce/pull/1700) | CONFLICTING | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | NOT DRAFT. **CONFLICTING**. No zone. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | REVIEW_REQUIRED (draft) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT. No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | REVIEW_REQUIRED (draft) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT. No zone. |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | REVIEW_REQUIRED (draft) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) — New | DRAFT. No zone. Jira = New. |

---

## 🆕 New Bot-Authored PRs (Not on Board — Flagged)

| PR | Ticket | State | CI | Notes |
|----|--------|-------|----|-------|
| ~~[#1693](https://github.com/Jounce-IO/jounce/pull/1693)~~ | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **MERGED 15:02 IDT Jul 26** 🎉 | — | Bot PR merged. AIPCC-27655 resolved. |
| [#1694](https://github.com/Jounce-IO/jounce/pull/1694) | [AIPCC-27681](https://redhat.atlassian.net/browse/AIPCC-27681) | OPEN, MERGEABLE, NOT draft, REVIEW_REQUIRED | CodeRabbit only (bot ineligible) | Bot "jira-autofix". Needs Joseph review. |
| [#1729](https://github.com/Jounce-IO/jounce/pull/1729) | [AIPCC-28414](https://redhat.atlassian.net/browse/AIPCC-28414) | OPEN, NOT draft, REVIEW_REQUIRED | — | Bot autofix. test(jbenchmark): verify updated_at after PATCH experiment. Needs Joseph review. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | AIPCC-28249 | 🔴 e2e-product ❌ FAILED (**NEW run 30548081534**); all other checks ✅ | **OPEN, MERGEABLE** | 🔴 **e2e-product ❌ FAILED** — CI re-ran, still failing. e2e-product is sole blocker. |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | — | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | — | **MERGED 12:44 IDT Jul 26** 🎉 | Off-board. Merged. |
| [#1716](https://github.com/Jounce-IO/jounce/pull/1716) | autofix/aipcc-28110 | [AIPCC-28110](https://redhat.atlassian.net/browse/AIPCC-28110) | — | OPEN, NOT draft, REVIEW_REQUIRED, MERGEABLE | Off-board. Bot autofix. Monitoring only. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [AIPCC-28289](https://redhat.atlassian.net/browse/AIPCC-28289) | New | Write UI requirements document based on spike findings |
| [AIPCC-23298](https://redhat.atlassian.net/browse/AIPCC-23298) | New | Implement v0.7.0 Container Image & Argo Integration |
| [AIPCC-23308](https://redhat.atlassian.net/browse/AIPCC-23308) | New | Implement v0.7.0 Report Ingestion |
| [AIPCC-23215](https://redhat.atlassian.net/browse/AIPCC-23215) | New | [DEV] Execute and monitor benchmark runs on IBM cluster |
| [AIPCC-23253](https://redhat.atlassian.net/browse/AIPCC-23253) | New | [DOCS] Update apps/jbenchmark/README.md for IBM cluster |
| [AIPCC-23157](https://redhat.atlassian.net/browse/AIPCC-23157) | New | [DOCS] Dashboard README and setup instructions |
| [AIPCC-23882](https://redhat.atlassian.net/browse/AIPCC-23882) | New | [DEV] Integrate IBM cluster support into runner main |
| [AIPCC-23119](https://redhat.atlassian.net/browse/AIPCC-23119) | New | Upgrade to GuideLLM v0.7.2 |
| [AIPCC-23220](https://redhat.atlassian.net/browse/AIPCC-23220) | New | [DEV] Implement git tagging workflow for 3.5GA release |
| [AIPCC-23574](https://redhat.atlassian.net/browse/AIPCC-23574) | New | implement an agentic jira -> PR workflow - Forge |
| [AIPCC-23169](https://redhat.atlassian.net/browse/AIPCC-23169) | In Progress | Mode Validation 3.5GA Release |
| [AIPCC-23104](https://redhat.atlassian.net/browse/AIPCC-23104) | In Progress | Benchmark Visibility Dashboard |
| [AIPCC-25962](https://redhat.atlassian.net/browse/AIPCC-25962) | In Progress | [DOCS] Document module layout convention and Dockerfile template |
| [AIPCC-23657](https://redhat.atlassian.net/browse/AIPCC-23657) | In Progress | [DEV] Add integration-run to GitHub required status checks |

*Sprint unchanged from previous run. AIPCC-28413 dropped (removed from sprint or closed).*

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[AIPCC-26976](https://redhat.atlassian.net/browse/AIPCC-26976)** (JN-5842) | [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | **MERGED Jul 14** | **New** | ❌ Update Jira → Done |
| **[AIPCC-24425](https://redhat.atlassian.net/browse/AIPCC-24425)** (JN-5877) | [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[AIPCC-23824](https://redhat.atlassian.net/browse/AIPCC-23824)** (JN-5874) | [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | **MERGED Jul 13** | **New** | ❌ Update Jira → Done |
| **[AIPCC-23220](https://redhat.atlassian.net/browse/AIPCC-23220)** (JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | **MERGED Jul 12** | **New** | ❌ Update Jira → Done |
| **[AIPCC-25962](https://redhat.atlassian.net/browse/AIPCC-25962)** (JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | **MERGED Jul 7** | **In Progress** | ❌ Update Jira → Done |

*5 mismatches — unchanged. Jira MCP unavailable this run; use `acli jira workitem transition` to update.*

---

## Key Changes (10:15 IDT Jul 31 advance heartbeat vs 16:15 IDT Jul 30 advance heartbeat)

| What changed | Delta |
|---|---|
| **#1690 CI** | **NEW run 30548288372** (was 30438043057). Same failures: e2e-product ❌, pre-commit ❌, JIRA Assoc ❌. All passes unchanged. |
| **#1638 CI** | **NEW run 30548081534** (was 30438015210). Same failure: e2e-product ❌. All other checks ✅. |
| **Board zones** | Fully static — no zone changes. |
| **Merges** | None detected. |
| **Jira mismatches** | Unchanged at 5 (Jira MCP unavailable). |
| **Sprint tickets** | AIPCC-28413 confirmed dropped from sprint (removed since previous run). All others unchanged. |

---

## Attention Items

### 🔴 #1690 (AIPCC-27645) — CHANGES_REQUESTED + CI failing

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances"
- **State: OPEN, MERGEABLE, NOT DRAFT, CHANGES_REQUESTED by MenD32**
- CI (run 30548288372 — new): nox ✅, e2e-smoke ✅, e2e-api ✅, tox ✅; **e2e-product ❌**, pre-commit ❌, JIRA Assoc ❌
- **Action: Address MenD32 review feedback + fix pre-commit + investigate e2e-product failure.**

---

### 🔴 #1669 (JN-5872) — CI degraded + CONFLICTING

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect"
- **State: OPEN, DRAFT, CONFLICTING**
- CI: tox-run ❌, nox ❌, JIRA Assoc ❌, pre-commit ❌ — unchanged
- **Action: Rebase on main + fix CI failures.**

---

### 🔴 #1694 (AIPCC-27681) — BOT PR needs review

PR [#1694](https://github.com/Jounce-IO/jounce/pull/1694) — "fix(jbenchmark): share MetadataResolver across gpu_count iterations"
- OPEN, MERGEABLE, NOT DRAFT, REVIEW_REQUIRED. Bot PR (jira-autofix).
- **Action: Joseph review.**

---

### 🟡 #1729 (AIPCC-28414) — BOT PR needs review

PR [#1729](https://github.com/Jounce-IO/jounce/pull/1729) — "test(jbenchmark): verify updated_at after PATCH experiment"
- OPEN, NOT DRAFT, REVIEW_REQUIRED. Bot autofix PR.
- **Action: Joseph review.**

---

### 🔴 #1638 (off-board AIPCC-28249) — e2e-product ❌ FAILING

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638)
- State: OPEN, MERGEABLE, reviewDecision: "".
- CI (run 30548081534 — new): **e2e-product ❌ FAILED** — re-ran, still failing. All other checks ✅.
- **e2e-product is the sole remaining blocker. Needs investigation.**

---

### 🟡 #1698 (AIPCC-23845) — CONFLICTING

PR [#1698](https://github.com/Jounce-IO/jounce/pull/1698) — CONFLICTING (since ~00:05 IDT Jul 30).
- JIRA Assoc ❌ only CI failure (stale run from Jul 20).
- **Action: Rebase on main + fix JIRA Assoc.**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 23+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Stale (23+ days, no PR)

Last session Jul 8 IDLE.
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### 🟡 Jira Mismatches (5 remaining)

5 mismatches: AIPCC-26976 (JN-5842, →Done), AIPCC-24425 (JN-5877, →Done), AIPCC-23824 (JN-5874, →Done), AIPCC-23220 (JN-5827, →Done), AIPCC-25962 (JN-5546, →Done).
Unchanged — Jira MCP unavailable this run.

---

## Archived This Session

No archives this run (10:15 IDT Jul 31 advance heartbeat).

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
| [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | [AIPCC-26990](https://redhat.atlassian.net/browse/AIPCC-26990) (JN-5844) | **16:03 IDT Jul 28** 🎉 | "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md". Worktree ARCHIVED. Jira Closed. |
| [#1723](https://github.com/Jounce-IO/jounce/pull/1723) | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) | **11:31 IDT Jul 28** 🎉 | "feat(jbenchmark): exclude faulty experiments from export and cache lookups". No Agor worktree. Jira Closed. |
| [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | [AIPCC-26996](https://redhat.atlassian.net/browse/AIPCC-26996) (JN-5845) | **14:12 IDT Jul 28** 🎉 | "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files". Worktree ARCHIVED. Jira Closed. |
| [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) | **12:54 IDT Jul 27** 🎉 | "feat(jbenchmark): add is_faulty column, PATCH endpoint, and list filtering". No Agor branch. Jira Closed. |
| [#1693](https://github.com/Jounce-IO/jounce/pull/1693) | [AIPCC-27655](https://redhat.atlassian.net/browse/AIPCC-27655) | **15:02 IDT Jul 26** 🎉 | Bot PR (jira-autofix). No Agor worktree. |
| [#1714](https://github.com/Jounce-IO/jounce/pull/1714) | [AIPCC-28059](https://redhat.atlassian.net/browse/AIPCC-28059) / JN-5714 | **12:44 IDT Jul 26** 🎉 | Off-board. |
| [#1704](https://github.com/Jounce-IO/jounce/pull/1704) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **14:14 IDT Jul 22** 🎉 | Off-board. |
| [#1705](https://github.com/Jounce-IO/jounce/pull/1705) | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | **11:20 IDT Jul 22** 🎉 | Off-board. |
| [#1691](https://github.com/Jounce-IO/jounce/pull/1691) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **10:20 IDT Jul 20** 🎉 | ARCHIVED. |
| [#1692](https://github.com/Jounce-IO/jounce/pull/1692) | [AIPCC-27657](https://redhat.atlassian.net/browse/AIPCC-27657) | **09:36 IDT Jul 20** 🎉 | Off-board companion PR. |
| [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) | **14:14 IDT Jul 16** 🎉 | ARCHIVED. |
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | Done ✅ |
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | **17:53 IDT Jul 14** 🎉 | ARCHIVED. |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [AIPCC-26976](https://redhat.atlassian.net/browse/AIPCC-26976) (JN-5842) | **13:29 IDT Jul 14** 🎉 | ARCHIVED. |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | **12:20 IDT Jul 14** 🎉 | ARCHIVED. |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
