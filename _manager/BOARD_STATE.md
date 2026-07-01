# Board State — jounce-workflow-ai

*Last updated: 2026-07-01 10:30 IDT (advance heartbeat)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5546-docs-document-module-layout-convention-and-3 | Code Review | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (run 28469578445) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 REGRESSION: Was MERGEABLE at 00:00 IDT, now CONFLICTING again. Pre-commit still failing. Rebase + fix pre-commit to unblock. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | — | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| internal-cr-system | Code | — | — | — | ⚠️ No PR; filesystem had git lock error; stagnant since Jun 18 |
| jira-operations | (no zone) | — | — | — | ⚠️ No zone, no PR — needs zone assignment or archive |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5795-upgrade-to-guidellm-v070 | NO ZONE | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) "Upgrade to GuideLLM v0.7.0" — Epic, Backlog | ℹ️ Design session done (143 msgs, idle 12:45 IDT Jun 30). No zone assigned. Proposal: move to Plan zone. |

**Note:** jn-5794-required-checks was **archived at 09:21 IDT Jul 1** after PR #1643 merged at 09:16 IDT. jn-5780-add-jn-project is not in the Agor jounce repo list (active or archived). Per data.js it belongs to a different repo (jira-autofix).

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — **Done** | ❌ e2e-smoke ❌ + e2e-tests ❌ (run 28429314700, all else ✅) | 🔴 CONFLICTING | 🔴 CONFLICTING + 2 persistent e2e failures. Jira Done. Fix conflict + e2e, or close PR. |

---

## Sprint Tickets Without Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
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
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **Cannot verify** (Jira access error) | ❌ Verify in Jira → Done (NEW) |
| [JN-5714](https://redhat.atlassian.net/browse/JN-5714) | [#1628](https://github.com/Jounce-IO/jounce/pull/1628) | MERGED Jun 30 15:39 IDT | **Backlog** | ❌ Update Jira → Done |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | MERGED Jun 29 | **In Progress** | ❌ Update Jira → Done |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, CI 2 FAIL | **Done** | ⚠️ Ticket marked Done but PR open — intentional? |
| [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | MERGED Jun 30 10:41 IDT | **Cannot check** (old Jira instance error) | ⚠️ PR merged — verify Jira is Done |

---

## Key Changes Since Last Run (09:00 IDT Jul 1)

| What observed | Status |
|---|---|
| **PR #1643 MERGED** | 🎉 Merged at 09:16 IDT Jul 1 (6 minutes before previous heartbeat finished scanning). jn-5794-required-checks worktree auto-archived at 09:21 IDT. |
| **PR #1588 REGRESSION** | 🔴 Was MERGEABLE at 00:00 IDT Jul 1; now CONFLICTING again. Something merged into main between 00:00 IDT and 10:30 IDT that caused a new conflict. Pre-commit still failing (run 28469578445). |
| **PR #1606: unchanged** | 🔴 CONFLICTING + e2e-smoke ❌ + e2e-tests ❌ (run 28429314700) — unchanged. |
| **Jira mismatches: 4 unchanged + 1 new** | JN-5714/5612/5616/5724 unresolved. NEW: JN-5794 PR merged but Jira unverifiable (access error). |

---

## Attention Items

### 🎉 PR #1643 (JN-5794) — MERGED at 09:16 IDT Jul 1

PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643): `fix(ci): add all-checks aggregator gate to prevent auto-merge bypass (JN-5794)`
- **Merged:** 09:16 IDT Jul 1 2026 (APPROVED by reviewer)
- **Worktree:** jn-5794-required-checks auto-archived at 09:21 IDT Jul 1
- **Action needed:** Verify/update [JN-5794](https://redhat.atlassian.net/browse/JN-5794) in Jira → Done (Jira MCP returning access error for this ticket)

---

### 🔴 PR #1588 (JN-5546) — CONFLICTING AGAIN (Regression)

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): `docs(jbenchmark): add CONTRIBUTING.md and service READMEs`
- **REGRESSION:** Was MERGEABLE at 00:00 IDT Jul 1; now back to CONFLICTING at 10:30 IDT
- Something merged into main between 00:00 IDT and now that created a new conflict
- **CI (run 28469578445):** pre-commit ❌ + pre-commit-run ❌ still FAILING. All other checks ✅.
- **Action needed:** Rebase on main again + fix pre-commit failures

---

### 🔴 PR #1606 (JN-5725) — CONFLICTING + e2e Failures (Off-board)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- CI run 28429314700: e2e-smoke ❌ (6m15s), e2e-tests ❌ (4s) — all other checks ✅
- Jira JN-5725 shows **Done**
- **Action needed:** Rebase on main to clear conflict, then fix e2e failures. Decide: fix and merge, or close PR.

---

### ❌ Jira Mismatches (5 tickets need action)

- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR #1643 MERGED Jul 1 09:16 IDT → Jira unverifiable (access error) (**NEW**)
- [JN-5714](https://redhat.atlassian.net/browse/JN-5714): PR #1628 MERGED Jun 30 15:39 IDT → still "Backlog"
- [JN-5612](https://redhat.atlassian.net/browse/JN-5612): PR #1627 MERGED Jun 29 → still "In Progress"
- [JN-5616](https://redhat.atlassian.net/browse/JN-5616): PR #1623 MERGED Jun 29 → still "In Review"
- [JN-5724](https://redhat.atlassian.net/browse/JN-5724): PR #1622 MERGED Jun 29 → still "In Review"

---

## Recently Merged (2026-07-01)

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | 09:16 IDT Jul 1 | Archived 09:21 IDT Jul 1 |
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
