# Board State — jounce-workflow-ai

*Last updated: 2026-06-30 16:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5546-docs-document-module-layout-convention-and-3 | Code Review | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (stale run 27933817996) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 CONFLICTING + pre-commit FAIL. Stale 13+ days. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | — | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| internal-cr-system | Code | — | — | — | ⚠️ No PR; filesystem had git lock error; stagnant since Jun 18 |
| jira-operations | (no zone) | — | — | — | ⚠️ No zone, no PR — needs zone assignment or archive |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5794-required-checks | Ingest | — | — | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5795-upgrade-to-guidellm-v070 | NO ZONE | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) "Upgrade to GuideLLM v0.7.0" — Epic, Backlog | ℹ️ **NEW** — Created 11:48 IDT Jun 30. Design session done (143 msgs, idle 12:45 IDT). No zone assigned yet. Proposal: move to Plan zone. |

**Note:** jn-5780-add-jn-project is not in the Agor jounce repo list (active or archived). Per data.js it belongs to a different repo (jira-autofix). Board scan shows no record of it.

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** | ❌ e2e-smoke ❌ + e2e-tests ❌ (run 28429314700, all else ✅) | 🔴 CONFLICTING (regression: was MERGEABLE) | 🔴 Now CONFLICTING + 2 persistent e2e failures. Jira Done. Fix conflict + e2e, or close PR. |
| [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | jn-5546-docs-document-module-layout-convention-and-3 | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | ❌ pre-commit FAIL (stale run 27933817996) | 🔴 CONFLICTING | 🔴 **STALE** — unchanged since Jun 17. Needs rebase + pre-commit fix. |
| [#1596](https://github.com/Jounce-IO/jounce/pull/1596) | jn-5695-db-connect-script | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | — | 🔴 DRAFT CONFLICTING | 🔴 Frozen; solved locally |

---

## Sprint Tickets Without Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [BUG] Auto-merge bypasses integration test failures | **Backlog** | Has worktree in Ingest zone, no sessions yet |
| [JN-5790](https://redhat.atlassian.net/browse/JN-5790) | [DEV] Add integration-run to GitHub required status checks | **Waiting/Blocked** | No worktree |
| [JN-5789](https://redhat.atlassian.net/browse/JN-5789) | [HOTFIX] Fix search_experiments() JSONB path mismatch | **Waiting/Blocked** | Related to JN-5793 (now merged via #1639) |
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Verify Visibility Notebook in Production Environment | **Backlog** | No worktree |
| [JN-5783](https://redhat.atlassian.net/browse/JN-5783) | [RESEARCH] Define git tagging workflow | **Backlog** | No worktree |
| [JN-5728](https://redhat.atlassian.net/browse/JN-5728) | [DEV] Fix e2e CI workflow gaps | **Backlog** | No worktree |
| [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | Create db_connect script for readonly psql access | **Backlog** | Has PR #1596 (DRAFT CONFLICTING) |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5714](https://redhat.atlassian.net/browse/JN-5714) | [#1628](https://github.com/Jounce-IO/jounce/pull/1628) | MERGED Jun 30 15:39 IDT | **Backlog** | ❌ Update Jira → Done (NEW) |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | MERGED Jun 29 | **In Progress** | ❌ Update Jira → Done |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, CI 2 FAIL | **Done** | ⚠️ Ticket marked Done but PR open — intentional? |
| [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | MERGED Jun 30 10:41 IDT | **Cannot check** (old Jira instance error) | ⚠️ PR merged — verify Jira is Done |

---

## Key Changes Since Last Run (16:00 IDT Jun 30)

| What observed | Status |
|---|---|
| **NEW: jn-5795-upgrade-to-guidellm-v070** | ℹ️ New worktree on board, NO ZONE. JN-5795 "Upgrade to GuideLLM v0.7.0" (Epic, Backlog). Design session done (143 msgs, idle 12:45 IDT). Proposal: assign to Plan zone. |
| **PR #1606 regression** | 🔴 Now CONFLICTING (was MERGEABLE since Jun 22). CI unchanged: e2e-smoke ❌ + e2e-tests ❌ (run 28429314700). |
| **Jira mismatches: 4 unchanged** | JN-5714/5612/5616/5724 all still unresolved — no updates since last run |
| **PR #1588: unchanged** | 🔴 Still CONFLICTING + pre-commit FAIL, stale 14+ days |
| **PR #1628 / #1639** | Already captured as MERGED; no new merges this run |

---

## Attention Items

### ℹ️ NEW: jn-5795-upgrade-to-guidellm-v070 — Design Done, No Zone

- **Worktree:** `jn-5795-upgrade-to-guidellm-v070` created 11:48 IDT Jun 30
- **Ticket:** [JN-5795](https://redhat.atlassian.net/browse/JN-5795) "Upgrade to GuideLLM v0.7.0" — Epic, Backlog, assigned to Joseph
- **Status:** Design session complete (143 messages, idle since 12:45 IDT)
- **Missing:** No board zone assigned, no PR
- **Proposal:** Assign to Plan zone (design artifact ready in `.artifacts/design/JN-5795/03-design.md`)

---

### 🎉 PR #1628 (JN-5714) — MERGED at 15:39 IDT Jun 30

PR [#1628](https://github.com/Jounce-IO/jounce/pull/1628): `feat(jbenchmark): release manifest schema (JN-5714)` — **MERGED ✅**
- **Merged:** 15:39 IDT Jun 30 2026
- **cr-pr-1628 worktree:** archived automatically 16:00 IDT Jun 30
- **Action needed:** Update JN-5714 in Jira → Done (currently shows "Backlog")

---

### 🔴 PR #1606 (JN-5725) — REGRESSION: Now CONFLICTING + 2 e2e Failures

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- **NEW:** `mergeable: CONFLICTING` (was MERGEABLE since Jun 22 — something merged into main that conflicts)
- CI run 28429314700 **STALE**: e2e-smoke ❌ (6m15s), e2e-tests ❌ (4s) — all other checks ✅
- Jira JN-5725 shows **Done**
- **Action needed:** Rebase on main to clear conflict, then diagnose e2e failures. Decide: fix and merge, or close PR (Jira already Done).

---

### ❌ Jira Mismatches (4 tickets need update to Done)

- [JN-5714](https://redhat.atlassian.net/browse/JN-5714): PR #1628 MERGED Jun 30 15:39 IDT → still "Backlog" (**NEW**)
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

## Recently Merged (2026-06-29 to 2026-06-30)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1628](https://github.com/Jounce-IO/jounce/pull/1628) | [JN-5714](https://redhat.atlassian.net/browse/JN-5714) | 15:39 IDT Jun 30 | Archived Jun 30 16:00 IDT |
| [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | 10:41 IDT Jun 30 | Archived Jun 30 11:00 IDT |
| [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | 10:42 IDT Jun 29 | Archived Jun 29 |
| [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | 10:17 IDT Jun 29 | Archived Jun 29 |
| [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | 13:45 IDT Jun 29 | Archived Jun 29 |
| [#1615](https://github.com/Jounce-IO/jounce/pull/1615) | [JN-5677](https://redhat.atlassian.net/browse/JN-5677) | 15:08 IDT Jun 29 | Archived Jun 29 |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
