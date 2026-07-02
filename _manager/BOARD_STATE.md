# Board State — jounce-workflow-ai

*Last updated: 2026-07-02 09:00 IDT (advance heartbeat)*

---

⚠️ BOARD_STATE.md was ~12.5 hours old — full refresh performed. Overnight heartbeat gap (no commits between 20:30 IDT Jul 1 and 09:00 IDT Jul 2).

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| jn-5546-docs-document-module-layout-convention-and-3 | Code Review | [#1588](https://github.com/Jounce-IO/jounce/pull/1588) | ❌ pre-commit FAIL (run 28469578445) | [JN-5546](https://redhat.atlassian.net/browse/JN-5546) — In Progress | 🔴 CONFLICTING + pre-commit ❌ — UNCHANGED since Jul 1 10:30. Needs rebase + pre-commit fix. |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | — | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT CONFLICTING; frozen |
| jn-5672-dal-ext-dashboard | BLOCKED | — | — | [JN-5672](https://redhat.atlassian.net/browse/JN-5672) | On hold — after notebooks complete |
| model-packaging-cr | Code Review | — | — | — | ⚠️ model-packaging-pipeline repo. Created Jun 15. No PR URL set, stagnant 17+ days. Needs investigation or archive. |
| jira-operations | (no zone) | — | — | — | ⚠️ No zone, no PR — needs zone assignment or archive |
| jn-5244-cli-flags | Ingest | — | — | [JN-5244](https://redhat.atlassian.net/browse/JN-5244) | ℹ️ No sessions yet. Ready to ingest. |
| jn-5795-upgrade-to-guidellm-v070 | NO ZONE | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) — Backlog | ℹ️ Design session done (idle Jun 30 12:45 IDT). No zone assigned. Proposal: move to Plan zone. |
| jn-5780-add-jn-project | Plan | GitLab [MR#887](https://gitlab.com/redhat/rhel-ai/agentic-ci/autofix/-/merge_requests/887) | — | [JN-5780](https://redhat.atlassian.net/browse/JN-5780) | ℹ️ jira-autofix repo. Session done Jun 28 09:20 IDT. MR pushed to GitLab. Needs title fix (JN-5780: prefix). |
| fix-dashboard-syntax-error | Plan | — | — | — | 🔴 ZOMBIE: agor-openclaw repo, filesystem_status=FAILED. Created Jun 17, error: "fatal: invalid reference: origin/private-julie". 15+ days stale. No Jira, no PR. PROPOSAL: archive. |

---

## Off-Board PRs (monitored)

| PR | Branch | Jira | CI | State | Flags |
|----|--------|------|----|-------|-------|
| [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | feat/jn-5725-integrate-vllm-log-analyzer | [JN-5725](https://redhat.atlassian.net/browse/JN-5725) — Done | ❌ e2e-smoke ❌ + e2e-tests ❌ (run 28527509341, all else ✅) | ✅ MERGEABLE | 🟡 e2e failures persist. Jira Done. Fix e2e or close PR. |

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

---

## Jira Mismatches

| Ticket | PR | PR Status | Jira Status | Action |
|--------|-----|-----------|-------------|--------|
| [JN-5794](https://redhat.atlassian.net/browse/JN-5794) | [#1643](https://github.com/Jounce-IO/jounce/pull/1643) | MERGED Jul 1 09:16 IDT | **Cannot verify** (Jira access error) | ❌ Verify in Jira → Done |
| [JN-5612](https://redhat.atlassian.net/browse/JN-5612) | [#1627](https://github.com/Jounce-IO/jounce/pull/1627) | MERGED Jun 29 | **In Progress** | ❌ Update Jira → Done |
| [JN-5616](https://redhat.atlassian.net/browse/JN-5616) | [#1623](https://github.com/Jounce-IO/jounce/pull/1623) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5724](https://redhat.atlassian.net/browse/JN-5724) | [#1622](https://github.com/Jounce-IO/jounce/pull/1622) | MERGED Jun 29 | **In Review** | ❌ Update Jira → Done |
| [JN-5725](https://redhat.atlassian.net/browse/JN-5725) | [#1606](https://github.com/Jounce-IO/jounce/pull/1606) | OPEN, e2e 2 FAIL | **Done** | ⚠️ Ticket marked Done but PR open — intentional? |
| [JN-5793](https://redhat.atlassian.net/browse/JN-5793) | [#1639](https://github.com/Jounce-IO/jounce/pull/1639) | MERGED Jun 30 10:41 IDT | **Cannot check** (old Jira instance error) | ⚠️ PR merged — verify Jira is Done |

---

## Key Changes Since Last Run (20:30 IDT Jul 1)

| What observed | Status |
|---|---|
| **Overnight gap** | No heartbeat commits Jul 1 20:30 → Jul 2 09:00 (12.5h gap). Full refresh performed. |
| **PR #1588: unchanged** | 🔴 CONFLICTING + pre-commit ❌ (run 28469578445). No new CI. |
| **PR #1606: unchanged** | 🟡 MERGEABLE + e2e-smoke ❌ + e2e-tests ❌ (run 28527509341). No new CI. |
| **fix-dashboard-syntax-error: NEW FINDING** | 🔴 Found in Plan zone — agor-openclaw repo, filesystem FAILED since Jun 17. 15+ day zombie. Proposal: archive. |
| **jn-5780: confirmed in Plan** | ℹ️ Confirmed Plan zone, GitLab MR#887 exists (Jun 28). Session idle. |
| **Jira mismatches: unchanged** | JN-5612 In Progress, JN-5616 In Review, JN-5724 In Review (all PRs merged Jun 29). JN-5794 + JN-5793 unverifiable. |

---

## Attention Items

### 🔴 fix-dashboard-syntax-error — ZOMBIE WORKTREE in Plan Zone

- **Branch:** agor-openclaw repo (not jounce)
- **Created:** Jun 17 2026
- **Filesystem status:** FAILED — `fatal: invalid reference: origin/private-julie`
- **Zone:** Plan (incorrectly placed)
- **No PR, no Jira ticket**
- **Action needed:** Archive this worktree — it's a 15-day-old failed creation artifact

---

### 🔴 PR #1588 (JN-5546) — CONFLICTING + pre-commit FAIL

PR [#1588](https://github.com/Jounce-IO/jounce/pull/1588): `docs(jbenchmark): add CONTRIBUTING.md and service READMEs`
- **Regression:** Was MERGEABLE at 00:00 IDT Jul 1; back to CONFLICTING at 10:30 IDT Jul 1
- **CI (run 28469578445):** pre-commit ❌ + pre-commit-run ❌ FAILING. All other checks ✅.
- **Action needed:** Rebase on main + fix pre-commit failures

---

### 🟡 PR #1606 (JN-5725) — e2e Still Failing (Off-board)

PR [#1606](https://github.com/Jounce-IO/jounce/pull/1606): `feat(vllm-analyzer): integrate log analyzer into experiment-workflow`
- **State:** MERGEABLE (conflict cleared Jun 17:30 IDT Jul 1)
- **CI (run 28527509341):** e2e-smoke ❌ (6m17s), e2e-tests ❌ (4s) — all other checks ✅
- **Jira:** JN-5725 shows Done
- **Action needed:** Fix e2e failures or close PR.

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
