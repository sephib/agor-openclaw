# Board State — jounce-workflow-ai

*Last updated: 2026-06-30 10:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5793-jsonb-path-fix | Code | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | ✅ **ALL PASS** (run 28376204013+28376203902) | [JN-5793](https://redhat.atlassian.net/browse/JN-5793) — cannot check (old instance?) | 🟢 **APPROVED + READY TO MERGE** — All CI green + reviewer **APPROVED** as of 10:30 IDT Jun 30. MERGEABLE. Merge immediately! |
| jn-5546-docs-document-module-layout-convention-and-3 | Code Review | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (stale run 27933817996) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 CONFLICTING + pre-commit FAIL. Stale 13+ days. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | — | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| internal-cr-system | Code | — | — | — | ⚠️ No PR; filesystem had git lock error; stagnant since Jun 18 |
| jira-operations | (no zone) | — | — | — | ⚠️ No zone, no PR — needs zone assignment or archive |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5794-required-checks | Ingest | — | — | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | ℹ️ No sessions yet. Ready to ingest. |

**Note:** jn-5780-add-jn-project is not in the Agor jounce repo list (active or archived). Per data.js it belongs to a different repo (jira-autofix). Board scan shows no record of it.

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | jn-5793-jsonb-path-fix | [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | ✅ **ALL PASS** — JIRA Association ✅ (run 28376203902), all functional ✅ (run 28376204013) | ✅ MERGEABLE, **APPROVED** | 🟢 **APPROVED + READY TO MERGE** — all checks green + reviewer approved. Merge now! |
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** | ❌ 4 FAIL (e2e-smoke ❌, e2e-tests ❌, integration ❌, integration-tests ❌) run 28381202187 | ✅ MERGEABLE | 🟡 Jira shows Done but PR still open with 4 CI failures. Unchanged since Jun 29 17:30. |
| [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | ❌ pre-commit FAIL (stale run 27933817996) | 🔴 CONFLICTING | 🔴 **STALE** — unchanged since Jun 17. Needs rebase + pre-commit fix. |
| [#1596](https://github.com/Jounce-IO/jounce/pull/1596) | jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | — | 🔴 DRAFT CONFLICTING | 🔴 Frozen; solved locally |

---

## Sprint Tickets Without Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [BUG] Auto-merge bypasses integration test failures | **Backlog** | Has worktree in Ingest zone, no sessions yet |
| [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | [BUG] search_experiments() JSONB path mismatch | **Cannot check (old Jira instance?)** | Has PR #1639 (ALL PASSING — ready to merge) |
| [JN-5790](https://redhat.atlassian.net/browse/JN-5790) | [DEV] Add integration-run to GitHub required status checks | **Waiting/Blocked** | No worktree |
| [JN-5789](https://redhat.atlassian.net/browse/JN-5789) | [HOTFIX] Fix search_experiments() JSONB path mismatch | **Waiting/Blocked** | Related to JN-5793 |
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Verify Visibility Notebook in Production Environment | **Backlog** | No worktree |
| [JN-5783](https://redhat.atlassian.net/browse/JN-5783) | [RESEARCH] Define git tagging workflow | **Backlog** | No worktree |
| [JN-5728](https://redhat.atlassian.net/browse/JN-5728) | [DEV] Fix e2e CI workflow gaps | **Backlog** | No worktree |
| [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | Create db_connect script for readonly psql access | **Backlog** | Has PR #1596 (DRAFT CONFLICTING) |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | MERGED Jun 29 | **In Progress** | ❌ Update Jira → Done |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, 4 CI FAIL | **Done** | ⚠️ Ticket marked Done but PR open — intentional? |

---

## Key Changes Since Last Committed Run (18:00 IDT Jun 29)

| What observed | Status |
|---|---|
| **PR #1639 APPROVED** | 🟢 reviewDecision changed to APPROVED as of 10:30 IDT Jun 30. All CI green. MERGEABLE. **Ready to merge immediately!** |
| **Previous sessions (08:00 + 08:30 IDT) reported board empty** | ⚠️ INCORRECT — board scan shows 8 active worktrees. Prior sessions had data error (corrected 09:01 IDT). |
| **JN-5725 Jira now Done** | ⚠️ Ticket moved to Done since last run (was In Progress/In Review). But PR #1606 still open with 4 CI failures. |
| **PR #1606 CI: unchanged** | 🟡 Same 4 failures (e2e-smoke, e2e-tests, integration, integration-tests), same run 28381202187 |
| **PR #1588: unchanged** | 🔴 Still CONFLICTING, no activity |
| **Jira mismatches: 3 persist** | JN-5612/JN-5616/JN-5724 still not updated to Done |

---

## Attention Items

### 🟢 PR #1639 (JN-5793) — APPROVED + READY TO MERGE

PR [#1639](https://github.com/Jounce-IO/jounce/pull/1639): `fix(tests): JN-5793 update plan_json fixtures to match production JSONB structure`
- **CI Status:** ALL CHECKS PASSING ✅ — JIRA Association ✅ (run 28376203902), integration ✅, pre-commit ✅, e2e-smoke ✅, e2e-tests ✅, e2e-api ✅, nox ✅, tox ✅
- **State:** MERGEABLE, **APPROVED** ✅ (confirmed 10:30 IDT Jun 30)
- **Action needed:** **MERGE NOW** — approved + all CI green!

---

### 🟡 PR #1606 (JN-5725) — Needs Decision

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- 4 CI failures unchanged since Jun 29 (e2e-smoke ❌, e2e-tests ❌, integration ❌, integration-tests ❌)
- Jira JN-5725 now shows **Done** — was this intentional? Is PR being abandoned?
- **Action needed:** Clarify intent — close PR if done, or diagnose CI failures if still in progress

---

### ❌ Jira Mismatches (3 tickets need update to Done)

- [JN-5612](https://redhat.atlassian.net/browse/JN-5612): PR #1627 MERGED Jun 29 → still "In Progress"
- [JN-5616](https://redhat.atlassian.net/browse/JN-5616): PR #1623 MERGED Jun 29 → still "In Review"
- [JN-5724](https://redhat.atlassian.net/browse/JN-5724): PR #1622 MERGED Jun 29 → still "In Review"

---

### 🔴 PR #1588 (JN-5546) — Stale and Blocked

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): `docs(jbenchmark): add CONTRIBUTING.md and service READMEs`
- **STALE:** Unchanged since Jun 17 (13+ days)
- **State:** CONFLICTING + pre-commit FAIL
- **Action needed:** Rebase on main + fix pre-commit failures, or close PR

---

## Recently Merged (2026-06-29)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | 10:42 IDT Jun 29 | Archived Jun 29 |
| [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | 10:17 IDT Jun 29 | Archived Jun 29 |
| [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | 13:45 IDT Jun 29 | Archived Jun 29 |
| [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | 15:08 IDT Jun 29 | Archived Jun 29 |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
