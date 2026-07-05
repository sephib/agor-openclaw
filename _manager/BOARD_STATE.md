# Board State — jounce-workflow-ai

*Last updated: 2026-07-05 20:00 IDT (advance heartbeat — weekday daytime)*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5546-docs-document-module-layout-convention-and-3 | Code Review | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (run 28469578445) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 CONFLICTING + pre-commit ❌ — UNCHANGED since Jul 1 10:30. Needs rebase + pre-commit fix. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, stagnant 20+ days. Needs investigation or archive. |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5841-agents-md-root | Ingest | — | — | [JN-5841](https://redhat.atlassian.net/browse/JN-5841) | 🆕 NEW as of 19:07 IDT Jul 5. Ingest session (019f3236) idle/completed. No PR yet. |
| jn-5795-upgrade-to-guidellm-v070 | NO ZONE | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | ℹ️ Design session done (idle Jun 30 12:45 IDT). No zone assigned. Proposal: move to Plan zone. |
| jira-operations | NO ZONE | — | — | — | ⚠️ CORRECTION: still exists in Agor (uid=249, last updated Jun 25). Was incorrectly reported as deleted/missing in 15:30 IDT run. Stale 10+ days with no session or PR. |
| jn-5780-add-jn-project | Plan | GitLab [MR#887](https://gitlab.com/redhat/rhel-ai/agentic-ci/autofix/-/merge_requests/887) | — | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | ℹ️ jira-autofix repo. Session done Jun 28 09:20 IDT. MR pushed to GitLab. Needs title fix (JN-5780: prefix). |
| fix-dashboard-syntax-error | Plan | — | — | — | 🔴 ZOMBIE: agor-openclaw repo, filesystem_status=FAILED. Created Jun 17, error: "fatal: invalid reference: origin/private-julie". 18+ days stale. No Jira, no PR. PROPOSAL: archive. |
| sprint-planning-jul | Plan | — | — | — | ℹ️ Updated 06:50 IDT Jul 2. No sessions, no PR, no Jira. Sprint planning for July? Needs context. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ e2e-smoke ❌ + e2e-tests ❌ + all-checks ❌ (run 28527509341) | 🔴 CONFLICTING | 🔴 CONFLICTING (since 10:00 IDT Jul 2). e2e failures persist. Jira Done. Needs rebase + fix e2e or close PR. |
| [#1631](https://github.com/Jounce-IO/jounce/pull/1631) | jn-5717-export-hash-rehash | [JN-5717](https://redhat.atlassian.net/browse/JN-5717) — Backlog (Uri Shaket) | ✅ all CI ✅ (run 28744609795) | 🟢 MERGEABLE | All checks pass. Awaiting merge. |

---

## Sprint Tickets Without Worktrees

| Ticket | Summary | Jira Status | Notes |
|--------|---------|-------------|-------|
| [JN-5790](https://redhat.atlassian.net/browse/JN-5790) | [DEV] Add integration-run to GitHub required status checks | **Waiting/Blocked** | No worktree |
| [JN-5789](https://redhat.atlassian.net/browse/JN-5789) | [HOTFIX] Fix search_experiments() JSONB path mismatch | **Waiting/Blocked** | Related to JN-5793 (merged via #1639) |
| [JN-5788](https://redhat.atlassian.net/browse/JN-5788) | Verify Visibility Notebook in Production Environment | **Backlog** | No worktree |
| [JN-5783](https://redhat.atlassian.net/browse/JN-5783) | [RESEARCH] Define git tagging workflow | **Backlog** | No worktree |
| [JN-5728](https://redhat.atlassian.net/browse/JN-5728) | [DEV] Fix e2e CI workflow gaps | **Backlog** | No worktree |
| [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | Create db_connect script for readonly psql access | **Backlog** | Has PR #1596 (DRAFT CONFLICTING) |
| [JN-5670](https://redhat.atlassian.net/browse/JN-5670) | Benchmark Visibility Dashboard | **In Progress** | No worktree — confirmed 11:30 IDT Jul 2 |
| [JN-5539](https://redhat.atlassian.net/browse/JN-5539) | Dependency & Build Standardization | **In Progress** | No worktree — confirmed 11:30 IDT Jul 2 |
| [JN-5678](https://redhat.atlassian.net/browse/JN-5678) | [DOCS] Dashboard README and setup instructions | **Backlog** | No worktree — found 15:00 IDT Jul 2 |
| [JN-5132](https://redhat.atlassian.net/browse/JN-5132) | Refactor run_jbenchmark script to support redesign flow | **Waiting/Blocked** | No worktree — found 15:00 IDT Jul 2 |
| [JN-5462](https://redhat.atlassian.net/browse/JN-5462) | Implement agentic Jira→PR workflow - Forge | **Backlog** | No worktree — found 15:00 IDT Jul 2 |
| [JN-5461](https://redhat.atlassian.net/browse/JN-5461) | Implement agentic Jira→PR workflow - AIPCC autofix | **Backlog** | No worktree — found 15:00 IDT Jul 2 |

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **Cannot verify** (Jira MCP access error) | ❌ Verify in Jira → Done |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | MERGED Jun 29 | **In Progress** | ❌ Update Jira → Done |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, CONFLICTING, e2e ❌ | **Done** | ⚠️ Ticket marked Done but PR open + conflicting |
| [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | MERGED Jun 30 10:41 IDT | **Cannot check** (old Jira instance error) | ⚠️ PR merged — verify Jira is Done |

---

## Key Changes Since Last Run (15:30 IDT Jul 5)

| What observed | Status |
|---|---|
| **CORRECTION: jira-operations** | ⚠️ Still IN AGOR (uid=249, NO ZONE, last updated Jun 25). Previous run incorrectly reported it as "deleted/missing". It's stale but present. |
| **jn-5841-agents-md-root CONFIRMED** | 🆕 In Ingest zone since 19:07 IDT Jul 5 (already noted in 15:00 IDT run). Ingest session 019f3236 idle/completed. No PR yet. |
| **PR #1631: unchanged** | OPEN, MERGEABLE, all CI ✅ (run 28744609795). Still awaiting merge. |
| **PR #1606: unchanged** | 🔴 Still CONFLICTING + e2e ❌ (run 28527509341). No new CI. |
| **PR #1588: unchanged** | 🔴 Still CONFLICTING + pre-commit ❌ (run 28469578445). No new CI since Jun 30. |
| **Jira mismatches: unchanged** | JN-5612 still "In Progress", JN-5616 still "In Review", JN-5724 still "In Review" (all PRs merged Jun 29). |
| **No new merges** | No new merges since #1643 on Jul 1. |
| **Board worktree count** | 11 active worktrees (10 in zones + jira-operations NO ZONE + jn-5795 NO ZONE = 11 total) |

---

## Attention Items

### 🔴 PR #1588 (JN-5546) — CONFLICTING + pre-commit FAIL

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): `docs(jbenchmark): add CONTRIBUTING.md and service READMEs`
- **CI (run 28469578445):** pre-commit ❌ + pre-commit-run ❌ FAILING. All other checks ✅.
- **Action needed:** Rebase on main + fix pre-commit failures

---

### 🔴 PR #1606 (JN-5725) — CONFLICTING (Off-board)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- **State:** CONFLICTING as of 10:00 IDT Jul 2
- **CI (run 28527509341):** all-checks ❌, e2e-smoke ❌ (6m17s), e2e-tests ❌ (4s) — all other checks ✅
- **Jira:** JN-5725 shows Done
- **Action needed:** Rebase on main + fix e2e failures, or close PR.

---

### 🟢 PR #1631 (JN-5717) — CLEAN, awaiting merge (Off-board)

PR [#1631](https://github.com/Jounce-IO/jounce/pull/1631): `feat(jbenchmark): canonical export hash for release diff (JN-5717)`
- **State:** OPEN, MERGEABLE — all CI ✅ (run 28744609795: all-checks ✅, e2e-smoke ✅, e2e-api ✅, e2e-tests ✅, pre-commit ✅, integration ✅)
- **Action:** Ready to merge once review is complete.

---

### 🔴 fix-dashboard-syntax-error — ZOMBIE WORKTREE in Plan Zone

- **Filesystem status:** FAILED — `fatal: invalid reference: origin/private-julie`
- **Created:** Jun 17 2026 (18+ days stale)
- **No PR, no Jira ticket**
- **Action needed:** Archive this worktree

---

### ⚠️ jira-operations — CORRECTION: still in Agor (NO ZONE)

- uid=249, last_used Jun 25 2026 (10+ days stale)
- NO ZONE, no sessions, no PR
- Previous 15:30 IDT run reported it as "missing/deleted" — this was incorrect
- Still present but stale. If no longer needed, propose archive.

---

### 🆕 jn-5841-agents-md-root — NEW WORKTREE (Ingest zone)

- Created 19:07 IDT Jul 5 by ingest session (019f3236, title: "Implement ingest — JN-5841 AGENTS.md + model-packaging-pipeline")
- Jira: [JN-5841](https://redhat.atlassian.net/browse/JN-5841) — issue_url set
- Session idle/completed. No PR yet. Ready for Plan phase.

---

### ❌ Jira Mismatches (3 confirmed + 2 unverifiable)

- [JN-5612](https://redhat.atlassian.net/browse/JN-5612): PR [#1627](https://github.com/Jounce-IO/jounce/pull/1627) MERGED Jun 29 → still "In Progress"
- [JN-5616](https://redhat.atlassian.net/browse/JN-5616): PR [#1623](https://github.com/Jounce-IO/jounce/pull/1623) MERGED Jun 29 → still "In Review"
- [JN-5724](https://redhat.atlassian.net/browse/JN-5724): PR [#1622](https://github.com/Jounce-IO/jounce/pull/1622) MERGED Jun 29 → still "In Review"
- [JN-5794](https://redhat.atlassian.net/browse/JN-5794): PR [#1643](https://github.com/Jounce-IO/jounce/pull/1643) MERGED Jul 1 09:16 IDT → Jira unverifiable (access error)
- [JN-5793](https://redhat.atlassian.net/browse/JN-5793): PR [#1639](https://github.com/Jounce-IO/jounce/pull/1639) MERGED Jun 30 → unverifiable (old Jira instance error)

---

## Recently Merged (2026-07-01 / 2026-06-29)

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
