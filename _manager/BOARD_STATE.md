# Board State — jounce-workflow-ai

*Last updated: 2026-07-19 18:32 IDT (advance heartbeat — weekday daytime)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690 DRAFT](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 NEW CI run 29690015249 FAILING: JIRA Association ❌, pre-commit ❌, all-checks ❌. PASS: check-changes ✅, atlas-validate ✅, build_envoy ✅, nox ✅ | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) | 🔴 Conflict resolved (was CONFLICTING at 17:02 IDT). CI now running but FAILING — JIRA Association ❌ (new failure: AIPCC format?) + pre-commit ❌. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — New | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. No change. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — New | Design session done Jun 30. Ready for Plan phase. Stale 19+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. Stale 11+ days. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI PASS (run 29403233416 — stale) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — New | DRAFT PR #1670. CI all pass (stale). Needs: mark ready for review. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | UNKNOWN (was CONFLICTING — status clearing?) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — New | 🟡 CONFLICTING status now UNKNOWN (possibly resolving). Still needs rebase on main. |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 run 29683534910: pre-commit ❌, nox ❌, tox-run ❌, all-checks ❌ | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — In Progress | 🔴 **CI ❌ + UNKNOWN mergeable** — pre-commit + nox + tox-run all failing. Mergeable UNKNOWN (was CONFLICTING). |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — New | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 11+** (still Ingest, should be Code). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 24+ days. Propose archive. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** ✅ | 🔴 **run 29689910782 CANCELLED** — FAIL: e2e-smoke ❌ (3rd consecutive), e2e-tests ❌, all-checks ❌. PASS: tox-run ✅, pre-commit-run ✅, e2e-api ✅, integration-run ✅, nox ✅, bake ✅. | OPEN, **CONFLICTING** 🔴 (conflict re-introduced; was MERGEABLE at 17:02 IDT) | 🔴 **PERSISTENT e2e-smoke FAILURE** — 3rd consecutive CI run with e2e-smoke ❌. Run was cancelled (pushed during run). PR now CONFLICTING again. Needs: resolve conflict + fix e2e-smoke. |

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

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED 13:29 IDT Jul 14** | **New** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **New** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **New** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **New** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |

*JN-5891: Done ✅. JN-5870: Done ✅. JN-5880: Done ✅. JN-5879: Done ✅. JN-5841: Done ✅. JN-5867: Done ✅. JN-5717: Done ✅. JN-5868: Done ✅. JN-5725: Done ✅. Jira MCP 401 — use acli for updates.*

---

## Key Changes (18:32 IDT Jul 19 vs 18:02 IDT Jul 19)

| What changed | Delta |
|---|---|
| **Board static — no changes** | All PR states unchanged. #1638 still OPEN/CONFLICTING (no new CI). #1690 still run 29690015249 FAILING (JIRA Association ❌ + pre-commit ❌). #1669 still run 29683534910 FAILING (pre-commit ❌, nox ❌, tox-run ❌). #1667/#1670 CI stale, mergeable UNKNOWN. 6 Jira mismatches unchanged. 0 merges. |

---

## Attention Items

### 🔴 #1638 (off-board JN-5725) — CONFLICTING + PERSISTENT e2e-smoke FAILURE (3rd run)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements (JN-5725)"
- State: OPEN, **CONFLICTING** 🔴 (conflict re-introduced; was MERGEABLE at 17:02 IDT)
- **Run 29689910782** (COMPLETE — conclusion: cancelled):
  - FAIL: e2e-smoke ❌ (**3rd consecutive run**), e2e-tests ❌, all-checks ❌
  - PASS: tox-run ✅, pre-commit-run ✅, e2e-api ✅, integration-run ✅, bake ✅, nox ✅, pre-commit ✅
  - SKIP: atlas-validate-run
- **Pattern:** e2e-smoke has failed in run 29688060716 AND run 29689910782 — persistent, not flaky.
- **Action:** 1) Resolve conflict on feat/vllm-analyzer-prerequisites. 2) Investigate e2e-smoke failure root cause (test is consistently failing across multiple pushes).

---

### 🔴 #1669 (jn-5872) — CI FAILING

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks (JN-5872)"
- State: OPEN, **UNKNOWN** mergeable (was CONFLICTING — possibly resolving)
- **Run 29683534910** (complete — regression):
  - FAIL: all-checks ❌, pre-commit ❌, nox ❌ (regression), pre-commit-run ❌, tox-run ❌ (regression)
  - PASS: JIRA ✅, atlas-validate ✅, check-changes ✅, e2e-api ✅, e2e-smoke ✅, integration-run ✅, integration-tests ✅, e2e-tests ✅
- **Action:** Fix pre-commit + nox + tox-run failures. Check if conflict resolved.

---

### 🟡 #1667 (jn-5845) — Needs rebase (UNKNOWN mergeable)

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **UNKNOWN** mergeable (was CONFLICTING — possibly resolving)
- CI run 29402877354 is stale (all-pass, but pre-conflict).
- **Action:** Rebase jn-5845-helm-cicd-agents-md on main to resolve conflict, then CI will re-run.

---

### 🟡 #1670 (jn-5844) — DRAFT (needs mark ready)

PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670): "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md files (JN-5844)"
- State: OPEN, isDraft:true, UNKNOWN mergeable
- CI run 29403233416 all-pass (stale).
- **Action:** Mark PR ready for review (remove draft status). Awaiting Joseph to approve readiness.

---

### 🔴 #1690 DRAFT (aipcc-27645-server-resources) — CI FAILING: JIRA Association ❌ + pre-commit ❌

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances (AIPCC-27645)"
- State: OPEN, isDraft:true, **UNKNOWN** mergeable (conflict resolved since 17:02 IDT)
- **New CI run 29690015249** (complete):
  - FAIL: JIRA Association ❌ (**new — AIPCC-27645 format not recognized?**), pre-commit ❌, pre-commit-run ❌, all-checks ❌
  - PASS: check-changes ✅, atlas-validate ✅, build_envoy/build-image ✅, generate_tag ✅, nox ✅, e2e-tests ✅, integration-tests ✅
  - SKIP: integration-run, e2e-api, e2e-smoke, e2e-product, e2e-priority, bake, atlas-validate-run
- **JIRA Association ❌:** Ticket is AIPCC-27645. Check may be looking for JN- prefix. The Jira migration to AIPCC happened Jul 2026 — JIRA Association check may not support new project key yet.
- **Action:** Fix JIRA Association failure (check if ticket format needs updating in commit/PR body). Fix pre-commit failures. Then CI should pass.

---

### 🟡 Jira Mismatches (6 active)

Remaining 6: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.
Use `acli jira workitem transition` to update. Jira MCP 401. acli working.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 11+)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### ✅ jn-5871 — ARCHIVED in Agor Jul 15 by Joseph

- Was previously noted as "NOT in Agor" — **CORRECTED**: jn-5871 WAS registered in Agor (Code zone, uid=283) and was archived by Joseph on Jul 15 09:57 UTC.
- No PR was created. JN-5871 still **New** in Jira — may need investigation if work should continue.

---

### 🔄 jn-5824 — Waiting for direction (stale 11+ days)

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### ⚠️ Overnight/Morning Session Failures (Jul 17–19)

Multiple consecutive session failures since Jul 17 (overnight + weekend schedules).
Daytime sessions running correctly. 51h board state gap caused by this pattern.

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
