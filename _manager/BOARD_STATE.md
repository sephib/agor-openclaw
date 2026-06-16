# Board State — jounce-workflow-ai

*Last updated: 2026-06-16 (first full scan)*

---

## Active Worktrees

| Branch | Jira | Zone | Jira Status | PR | Last Session Activity | Flags |
|--------|------|------|-------------|-----|----------------------|-------|
| jn-5673-visibility-scaffold | JN-5673 | Ingest | In Review | — | Jun 12 (4d ago), 0-msg session | ⚠️ STALE ORPHAN |
| manage-agor-ingest-jira | — | (floating) | N/A | — | Jun 15 orchestration done | ℹ️ no zone |
| jn-5673-visibility-module | JN-5673 | Respond | In Review | [#1595](https://github.com/Jounce-IO/jounce/pull/1595) | Jun 15 session idle, last msg empty | ⚠️ Slack posted? |
| jn-5672-dal-ext-dashboard | JN-5672 | plan | Backlog | — | Jun 14 subtasks created (2d ago) | ⚠️ stale |
| jn-5695-db-connect-script | JN-5695 | Publish | Backlog | [#1596](https://github.com/Jounce-IO/jounce/pull/1596) | Jun 15 push confirmed | ⚠️ Jira status wrong |
| jn-5674-operational-visibility | JN-5674 | Publish | Backlog | — | Jun 15 session blocked | 🔴 BLOCKED |
| code-reviewes | — | Code Review | N/A | — | Jun 15 review saved to temp | ℹ️ cleanup? |
| jn-5676-notebook-scaffold | JN-5676 | plan | Backlog | — | Jun 15 plan written | ⚠️ ready for Code |
| model-packaging-cr | — | Code Review | N/A | — | Jun 15 created, 0 sessions | ℹ️ no sessions |
| private-julie | — | (floating) | N/A | — | Jun 16 (me) | ✓ |

## Dashboard Artifact
- artifactId: 019ed0df-754f-77c4-9c13-02063e1be52e
- Published: 2026-06-16
- URL: http://localhost:3030/ui/a/019ed0df754f77c49c130206/
- Re-publish command: agor_artifacts_publish with branchId 019ecc87-be8b-77cd-ac4e-e2c203022f55, subpath .agor/artifacts/jounce-dashboard, artifactId 019ed0df-754f-77c4-9c13-02063e1be52e
| board-manager | — | (archived) | N/A | — | Jun 15 archived | ✓ |

---

## Attention Items

### 🔴 BLOCKED — jn-5674-operational-visibility (JN-5674)

Session `019ecbe7` (Jun 15 15:31) is **waiting for human decision**:

> "There are uncommitted changes (staged) that need to be handled before pushing"
> - `benchmark_visibility/README.md` (+85 lines)
> - `benchmark_visibility/operational_notebook.py` (+183/-115 lines)
> - `lcov.info` (+106/-106 lines)

Validation passed (PASS). No PR created yet. Session is asking Joseph what to do with the staged files.

---

### ⚠️ STALE ORPHAN — jn-5673-visibility-scaffold (JN-5673)

- Created Jun 11, sitting in Ingest 4 days
- Only 1 session, 0 messages — never actually started
- **Duplicate**: JN-5673 has a real worktree (`jn-5673-visibility-module`) with PR #1595 in Respond zone
- Candidate for archival

---

### ⚠️ JIRA STATUS MISMATCH — jn-5695-db-connect-script (JN-5695)

- Agor zone: **Publish** with PR #1596
- Jira status: **Backlog** (should be In Review or similar)
- Last session pushed new commits Jun 15 14:23

---

### ⚠️ JIRA STATUS MISMATCH — jn-5674-operational-visibility (JN-5674)

- Agor zone: **Publish** (advanced stage)
- Jira status: **Backlog** (significant mismatch)

---

### ⚠️ Slack notification unclear — jn-5673-visibility-module (JN-5673)

- PR #1595 exists, session at Jun 15 07:43 had a Slack draft ready but was asking which channel
- Latest session (019ecc22, Jun 15 16:37) has 43 messages but **empty last_message**
- Unclear if Slack message was ever posted

---

### ⚠️ Plan done, no Code move — jn-5676-notebook-scaffold (JN-5676)

- Plan written Jun 15 (yesterday)
- Still in **plan** zone, no session started for Code

---

### ⚠️ Stale in plan — jn-5672-dal-ext-dashboard (JN-5672)

- Sub-tasks JN-5693 and JN-5694 created Jun 14
- No movement in 2 days

---

## Sprint Tickets Without Board Worktrees

Tickets assigned to Joseph that are "In Progress" or "In Review" — may have worktrees on other boards:

| Ticket | Summary | Jira Status |
|--------|---------|-------------|
| JN-5662 | [DEV] Decouple libs/sql from services/validator | In Review |
| JN-5546 | [DOCS] Document module layout convention | In Review |
| JN-5382 | Add --labels CLI flag to runner | In Review |
| JN-5244 | Add --user, --no-cache, --skip-estimator flags | In Progress |
| JN-5132 | Refactor run_jbenchmark script | Waiting/Blocked |

*(These are not on this board; may be on the old board. Not flagging for action without more context.)*

---

## Backlog Tickets Without Worktrees (not yet started)

| Ticket | Summary |
|--------|---------|
| JN-5675 | [DEV] Historical visibility functions |
| JN-5677 | [DEV] Historical mode notebook cells |
| JN-5678 | [DOCS] Dashboard README and setup instructions |
| JN-5461 | Agentic jira → PR workflow - AIPCC autofix |
| JN-5462 | Agentic jira → PR workflow - Forge |
