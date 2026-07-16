# Board State — jounce-workflow-ai

*Last updated: 2026-07-16 13:15 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | UNKNOWN (stale) | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) — Waiting/Blocked | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. No change. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | Design session done Jun 30. Ready for Plan phase. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) — In Progress | Last session Jul 8 IDLE. SHA 16ec44ea (2 commits). Needs: configs, rebase, PR. |
| jn-5844-service-lib-sql-agents-md | **Publish** | [#1670 DRAFT](https://github.com/Jounce-IO/jounce/pull/1670) | ✅ ALL CI PASS (run 29403233416) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) — Backlog | DRAFT PR #1670. CI all pass. Needs: mark ready for review. |
| jn-5845-helm-cicd-agents-md | **Publish** | [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | ✅ ALL CI PASS (run 29402877354 complete) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) — Backlog | ✅ ALL CI PASS. OPEN + MERGEABLE + reviewDecision:"". markVaykhansky COMMENTED only (no APPROVE). Awaiting formal reviewer APPROVE. |
| jn-5872 | **Code** | [#1669](https://github.com/Jounce-IO/jounce/pull/1669) | ❌ CI COMPLETE — ALL-CHECKS FAIL (pre-commit FAIL, run 29411650412) | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) — Backlog | 🔴 pre-commit FAIL. Other checks pass. OPEN + MERGEABLE. **Action: fix pre-commit failure.** No new push since last run. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) — Backlog | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 8+** (still Ingest, should be Code). |
| jn-5871 | **Code** (git-only) | — | — | [JN-5871](https://redhat.atlassian.net/browse/JN-5871) — Backlog | Code done ~00:58 IDT Jul 9. SHA fc6e5f77. ⚠️ NOT in Agor board — git branch only. No PR created. |
| **jn-5891-max-seconds-1200** | **Code** (Agor) | [#1673](https://github.com/Jounce-IO/jounce/pull/1673) | ⏳ CI run 29488750857 IN PROGRESS: pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅, **e2e-smoke PENDING** | [JN-5891](https://redhat.atlassian.net/browse/JN-5891) — Backlog | 🟡 PR #1673 **APPROVED by ushaket** (09:28 IDT Jul 16). New CI run 29488750857: pre-commit ✅ (was ❌). e2e-smoke pending. If e2e-smoke passes → READY TO MERGE. Zone correction: Agor says Code (not Publish). |
| jira-operations | NO ZONE | — | — | — | ⚠️ uid=249, last updated Jun 25. Stale 20+ days. Propose archive. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1638](https://github.com/Jounce-IO/jounce/pull/1638) | feat/vllm-analyzer-prerequisites | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | ⏳ New CI run 29488442571 IN PROGRESS: pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅, bake ✅, **e2e-smoke PENDING** | OPEN, MERGEABLE | 🟡 New CI run 29488442571. Most checks passing. e2e-smoke pending. Pattern: persistent e2e flakiness between runs. |

---

## Sprint Tickets Without Worktrees

Active sprint tickets assigned to Joseph with no board worktree:

| Ticket | Status | Summary |
|--------|--------|---------|
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Waiting/Blocked | Verify Visibility Notebook in Production Environment |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Waiting/Blocked | Refactor run_jbenchmark script to support redesign flow |
| [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | Backlog | Add subcommands to runner — PR #1654 MERGED Jul 12, Jira stale! |
| [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | In Progress | Add CLI flags (jn-5244-cli-flags archived in Agor) |
| [JN-4393](https://redhat.atlassian.net/browse/JN-4393) | In Progress | Upgrade AGENTS.md Standard |
| [JN-5851](https://redhat.atlassian.net/browse/JN-5851) | Backlog | Implement v0.7.0 Container Image & Argo Integration |
| [JN-5852](https://redhat.atlassian.net/browse/JN-5852) | Backlog | Implement v0.7.0 Report Ingestion |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| **[JN-5842](https://redhat.atlassian.net/browse/JN-5842)** | **[#1658](https://github.com/Jounce-IO/jounce/pull/1658)** | **MERGED 13:29 IDT Jul 14** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5877](https://redhat.atlassian.net/browse/JN-5877)** | **[#1663](https://github.com/Jounce-IO/jounce/pull/1663)** | **MERGED 15:16 IDT Jul 13** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5874](https://redhat.atlassian.net/browse/JN-5874)** | **[#1662](https://github.com/Jounce-IO/jounce/pull/1662)** | **MERGED 12:10 IDT Jul 13** | **Backlog** | ❌ Update Jira → Done |
| **[JN-5401](https://redhat.atlassian.net/browse/JN-5401)** | **[#1654](https://github.com/Jounce-IO/jounce/pull/1654)** | **MERGED 17:12 IDT Jul 12** | **Backlog** | ❌ Update Jira → Done |
| [JN-5827](https://redhat.atlassian.net/browse/JN-5827) | [#1648](https://github.com/Jounce-IO/jounce/pull/1648) | MERGED Jul 12 | **Backlog** | ❌ Update Jira → Done |
| [JN-5546](https://redhat.atlassian.net/browse/JN-5546) | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | MERGED Jul 7 | **In Progress** | ❌ Update Jira → Done |

*JN-5870: Done ✅. JN-5880: Done ✅. JN-5879: Done ✅. JN-5841: Done ✅. JN-5867: Done ✅. JN-5717: Done ✅. JN-5868: Done ✅. Jira MCP 401 — use acli for updates.*

---

## Key Changes (13:15 IDT Jul 16 advance heartbeat vs 12:45 IDT Jul 16)

| What changed | Delta |
|---|---|
| **No new merges** | PR sweep: no new merges detected. |
| **🔑 #1673 APPROVED by ushaket** | reviewDecision flipped to APPROVED (09:28 IDT Jul 16). ushaket = MEMBER. |
| **#1673 new CI run 29488750857** | pre-commit now ✅ PASS (was ❌ FAIL in run 29486961479). e2e-smoke PENDING. If e2e-smoke passes → READY TO MERGE. |
| **jn-5891 zone correction** | BOARD_STATE.md had "Publish" — Agor MCP confirms zone_label="Code". Corrected. |
| **#1638 new CI run 29488442571** | Most checks passing. e2e-smoke pending. Rotating e2e pattern continues. |
| **#1667 — no APPROVE** | reviewDecision still "". markVaykhansky COMMENTED only. No human APPROVE yet. |

---

## Attention Items

### 🔑 #1673 (jn-5891) — APPROVED, CI nearly clear (e2e-smoke pending)

PR [#1673](https://github.com/Jounce-IO/jounce/pull/1673): "fix(jbenchmark): set GuideLLM max_seconds default to 1200 (JN-5891)"
- State: OPEN, **MERGEABLE** ✅, **reviewDecision: APPROVED** (ushaket, 09:28 IDT)
- **CI run 29488750857** (IN PROGRESS): pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅, **e2e-smoke PENDING**
- Previous run 29486961479: pre-commit ❌ (now fixed), e2e-api ❌ (now passing)
- **Action:** Monitor e2e-smoke completion. If passes → PR is ready to merge (APPROVED + CI green).

---

### 🔴 #1669 (jn-5872) — CI FAIL: pre-commit failure

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect with namespace/service checks"
- State: OPEN, **MERGEABLE** ✅, reviewDecision: ""
- **CI run 29411650412 COMPLETE: ALL-CHECKS = FAIL**
- pre-commit FAIL, pre-commit-run/pre-commit FAIL
- Other checks: e2e-smoke ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅
- **Action:** Fix pre-commit failure. Push fix → CI will re-run.
- No new push since last run.

---

### ✅ #1667 (jn-5845) — ALL CI PASS, Awaiting Reviewer APPROVE

PR [#1667](https://github.com/Jounce-IO/jounce/pull/1667): "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files (JN-5845)"
- State: OPEN, **MERGEABLE** ✅, reviewDecision: "" (no formal APPROVE)
- markVaykhansky COMMENTED only — not approved.
- **CI run 29402877354 COMPLETE ✅**: all mandatory checks pass.
- **Action:** Await formal APPROVE from markVaykhansky (or other required reviewer).

---

### 🔴 #1638 (off-board JN-5725) — CI run in progress (e2e-smoke pending)

PR [#1638](https://github.com/Jounce-IO/jounce/pull/1638): "chore(infra): vLLM analyzer prerequisites - workflow improvements"
- **CI run 29488442571** (IN PROGRESS): pre-commit ✅, e2e-api ✅, integration ✅, tox ✅, nox ✅, bake ✅. **e2e-smoke PENDING**.
- Pattern: persistent rotating e2e flakiness across runs.
- State: OPEN, MERGEABLE.
- **Action:** Monitor e2e-smoke result. If fails again → investigate root cause.

---

### 🟡 jn-5844 — DRAFT PR #1670 (needs mark ready)

**jn-5844-service-lib-sql-agents-md** ([JN-5844](https://redhat.atlassian.net/browse/JN-5844)):
- DRAFT PR [#1670](https://github.com/Jounce-IO/jounce/pull/1670) exists. isDraft:true. CI all pass (run 29403233416). In Publish zone (Agor).
- **Action:** Mark PR ready for review (remove draft status). Awaiting Joseph to approve readiness.

---

### 🟡 Jira Mismatches (6 active)

Remaining 6: JN-5842, JN-5877, JN-5874, JN-5401, JN-5827, JN-5546.
Use `acli jira workitem transition` to update. Jira MCP 401. acli working.

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 8+)

- Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### ⚠️ jn-5871 — NOT in Agor (git-only, no PR, Day 8+)

- Code done ~00:58 IDT Jul 9. SHA fc6e5f77.
- NOT registered as an Agor worktree. Git-only branch.
- No PR created. **Flag for Joseph:** What should happen with jn-5871?

---

### 🔄 jn-5824 — Waiting for direction

- Last session Jul 8 IDLE. SHA 16ec44ea (2 commits).
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### ⚠️ Overnight/Morning Session Failures

Multiple consecutive session failures (01:00 IDT Jul 16 was latest FAILED).
Daytime sessions running correctly. Overnight schedule consistently failing.

---

## Archived This Session

None — 0 auto-archives (no new merges).

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
| [#1655](https://github.com/Jounce-IO/jounce/pull/1655) | [JN-5867](https://redhat.atlassian.net/browse/JN-5867) | **18:49 IDT Jul 14** 🎉 | jn-5867 (git-only, not Agor). JN-5867 Done ✅ |
| [#1656](https://github.com/Jounce-IO/jounce/pull/1656) | [JN-5870](https://redhat.atlassian.net/browse/JN-5870) | 17:53 IDT Jul 14 🎉 | ARCHIVED 19:30 Jul 14. JN-5870 Done ✅ |
| [#1658](https://github.com/Jounce-IO/jounce/pull/1658) | [JN-5842](https://redhat.atlassian.net/browse/JN-5842) | 13:29 IDT Jul 14 🎉 | ARCHIVED 13:30 Jul 14 |
| [#1666](https://github.com/Jounce-IO/jounce/pull/1666) | [JN-5880](https://redhat.atlassian.net/browse/JN-5880) | 12:20 IDT Jul 14 🎉 | ARCHIVED 12:30 Jul 14. JN-5880 Done ✅ |
| [#1665](https://github.com/Jounce-IO/jounce/pull/1665) | [JN-5879](https://redhat.atlassian.net/browse/JN-5879) | 10:48 IDT Jul 14 🎉 | ARCHIVED 11:30 Jul 14. JN-5879 Done ✅ |
| [#1663](https://github.com/Jounce-IO/jounce/pull/1663) | [JN-5877](https://redhat.atlassian.net/browse/JN-5877) | 15:16 IDT Jul 13 🎉 | ARCHIVED 15:30 Jul 13 |
| [#1662](https://github.com/Jounce-IO/jounce/pull/1662) | [JN-5874](https://redhat.atlassian.net/browse/JN-5874) | 12:10 IDT Jul 13 🎉 | ARCHIVED 12:32 Jul 13 |
| [#1654](https://github.com/Jounce-IO/jounce/pull/1654) | [JN-5401](https://redhat.atlassian.net/browse/JN-5401) | 17:12 IDT Jul 12 🎉 | ARCHIVED. JN-5401 Backlog → needs Done! |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
