# Agent Onboarding Checklist

Master checklist for creating and setting up each agent. Complete the plumbing first, then onboard the agent's personality and workflow.

---

## External Service Integration Rules

When agents need to interact with external services, prefer CLIs over MCP when MCP is unreliable:

| Service | Primary | Fallback | Notes |
|---------|---------|----------|-------|
| **GitHub** | `gh` CLI | GitHub MCP | `gh` is more reliable and feature-complete |
| **GitLab** | `glab` CLI | — | Use `glab` for all GitLab interactions |
| **Jira** | Jira MCP (`4c674f09`) | `acli` CLI | If Jira MCP has issues, fall back to `acli` |
| **Trello** | Trello MCP (`197c2d91`) | `curl` with creds from `~/.config/mcp-trello.env` | MCP has no comment tool + get_card timeouts |
| **Agor** | Agor MCP | — | Always use MCP |

All agents should include these fallback instructions in their `.claude/CLAUDE.md`.

---

## Julie 👩‍⚖️ — jounce-workflow-ai Board Manager

**Board:** jounce-workflow-ai (`019eb849-ec5b-715e-b8cc-e37c4c387740`)
**Repo:** local/agor-openclaw

- [x] Create assistant via Agor UI
- [x] Assign assistant to target board
- [x] Create `.claude/CLAUDE.md` with agent instructions
- [x] Create `_manager/SOUL.md` with identity
- [x] Create `_manager/BOARD_STATE.md` (state tracking)
- [x] Create `_manager/PROPOSALS.md` (human-in-the-loop actions)
- [x] Create `_manager/RUN_LOG.md` (append-only run history)
- [x] Set up schedule (`019ecc9f-906d-7344-b355-056d288080e2` — daily 8am IST, Sun-Thu)
- [x] Configure MCP servers (Agor + Jira)
- [x] Create tracking card on Oggy's board (Active zone)
- [ ] Verify first scheduled run completes successfully
- [ ] Review first PROPOSALS.md output
- [ ] Decide which proposals to approve as autonomous patterns

---

## 📋 Trello Daily Tasks Agent

**Target board:** openclaw-agor (`1a508c77-dacb-46fe-ab24-e527fb476882`)
**Repo:** local/agor-openclaw
**MCP servers needed:** Agor + Trello
**Replaces/consolidates:** trello-task-processor (d1ed5f5a), trello-visibility-hub, 12 disabled triage schedules

### Plumbing
- [ ] Create assistant via Agor UI (name TBD, emoji TBD)
- [ ] Assign assistant to openclaw-agor board
- [ ] Create `.claude/CLAUDE.md` with agent instructions
- [ ] Create `_manager/SOUL.md` with identity
- [ ] Create `_manager/BOARD_STATE.md`
- [ ] Create `_manager/PROPOSALS.md`
- [ ] Create `_manager/RUN_LOG.md`
- [ ] Set up schedule (daily morning, Israel time)
- [ ] Configure MCP servers (Agor + Trello `197c2d91-c0be-43cf-ba3d-431ccc8da5c9`)
- [ ] Create tracking card on Oggy's board (move from Explore → Active)
- [ ] Disable old trello-task-processor schedule (`d1ed5f5a`)
- [ ] Decide: archive old trello-list-* worktrees or keep for reference?

### Onboarding (design conversation needed)
- [ ] Define task categories (research / purchase / human-only / coding)
- [ ] Define blocked-task policy (max retries, backoff, escalation)
- [ ] Define Trello MCP workarounds (curl comments, timeout handling)
- [ ] Define daily briefing format
- [ ] Define relationship with existing trello-visibility-hub

---

## 💰 Finance Management Agent

**Target board:** openclaw-agor (`1a508c77-dacb-46fe-ab24-e527fb476882`)
**Repo:** local/agor-openclaw
**MCP servers needed:** Agor + Trello (finance tasks tracked there)
**Replaces/consolidates:** financial-advisor (6062d390), recurring-reminders-quarterly (9affda3b), reminders-monthly (2d8fe4e6)

### Plumbing
- [ ] Create assistant via Agor UI (name TBD, emoji TBD)
- [ ] Assign assistant to openclaw-agor board
- [ ] Create `.claude/CLAUDE.md` with agent instructions
- [ ] Create `_manager/SOUL.md` with identity
- [ ] Create `_manager/BOARD_STATE.md`
- [ ] Create `_manager/PROPOSALS.md`
- [ ] Create `_manager/RUN_LOG.md`
- [ ] Create `_manager/DEADLINES.md` (recurring deadline tracker)
- [ ] Set up schedule(s):
  - [ ] Daily morning scan (workdays)
  - [ ] Monthly reminder (1st of month — migrate from reminders-monthly)
  - [ ] Quarterly reminder (migrate from recurring-reminders-quarterly)
- [ ] Configure MCP servers (Agor + Trello)
- [ ] Create tracking card on Oggy's board (move from Explore → Active)
- [ ] Disable old reminders-monthly schedule
- [ ] Disable old recurring-reminders-quarterly schedule

### Onboarding (design conversation needed)
- [ ] Inventory all finance-related Trello cards
- [ ] Define deadline tracking rules (Israeli tax calendar, insurance renewals)
- [ ] Define escalation policy (how aggressively to remind)
- [ ] Define what the agent can DO vs just remind about
- [ ] Decide: separate board or share openclaw-agor?

---

## ✍️ Blog Writing Agent

**Target board:** Blogs (`220997ae-5fd7-4a48-92c4-f34bd07bca17`)
**Repo:** sephib/sephib.github.io (`b16286a4-2efd-458c-a665-05ae6f33a837`)
**MCP servers needed:** Agor + GitHub (`064aafa2-d5fd-46fa-98b6-3785fee4af5d`)
**Existing zones:** Ideas, social - short blogs, Review

### Plumbing
- [ ] Create assistant via Agor UI (name TBD, emoji TBD)
- [ ] Assign assistant to Blogs board
- [ ] Create `.claude/CLAUDE.md` with agent instructions
- [ ] Create `_manager/SOUL.md` with identity
- [ ] Create `_manager/DRAFTS_STATE.md` (track blog post pipeline)
- [ ] Create `_manager/PROPOSALS.md`
- [ ] Create `_manager/RUN_LOG.md`
- [ ] Set up schedule (weekly? on-demand? TBD)
- [ ] Configure MCP servers (Agor + GitHub)
- [ ] Create tracking card on Oggy's board (move from Explore → Active)
- [ ] Verify blog repo structure (Jekyll/Hugo/other — check sephib.github.io)

### Onboarding (design conversation needed)
- [ ] Define blog workflow (idea → outline → draft → review → publish)
- [ ] Define topics Joseph wants to write about
- [ ] Define agent role: research? writing? editing? all?
- [ ] Map existing Blogs board zones to workflow
- [ ] Define publishing process (PR to sephib.github.io? manual?)
- [ ] Define cadence (weekly scan for ideas? on-demand only?)

---

## 🏛️ Hakhel NGO Agent

**Target board:** hakhel (`c2287fc7-edd9-45e4-8a0f-497f1dcda38c`)
**Repo:** sephib/hakhel (`8fff4c8a-ee18-46d3-8a63-c796af6d5c00`)
**MCP servers needed:** Agor + (TBD — depends on NGO tooling)
**Existing zones:** ideas
**Related:** keren-adi board + repo

### Plumbing
- [ ] Create assistant via Agor UI (name TBD, emoji TBD)
- [ ] Assign assistant to hakhel board
- [ ] Create `.claude/CLAUDE.md` with agent instructions
- [ ] Create `_manager/SOUL.md` with identity
- [ ] Create `_manager/BOARD_STATE.md`
- [ ] Create `_manager/PROPOSALS.md`
- [ ] Create `_manager/RUN_LOG.md`
- [ ] Set up schedule (TBD — depends on NGO needs)
- [ ] Configure MCP servers (Agor + TBD)
- [ ] Create tracking card on Oggy's board (move from Explore → Active)
- [ ] Set up board zones (only "ideas" exists — needs workflow zones)

### Onboarding (design conversation needed)
- [ ] Understand what Hakhel does and what tasks need managing
- [ ] Define: coding work, admin work, or both?
- [ ] Identify tools/integrations the NGO uses
- [ ] Clarify relationship between Hakhel and Keren Adi
- [ ] Identify who else is involved (team? solo?)
- [ ] Define board zone structure for hakhel board
- [ ] Explore what's already in the hakhel repo

---

## Common Pattern — Agent Setup Template

Every agent follows this structure:

```
private-<agent-name>/          # Branch (created via Agor UI)
├── .claude/
│   └── CLAUDE.md              # Agent instructions (what to do each run)
└── _manager/
    ├── SOUL.md                # Who the agent is
    ├── BOARD_STATE.md         # Current board snapshot (updated each run)
    ├── PROPOSALS.md           # Actions awaiting human approval
    └── RUN_LOG.md             # Append-only run history
```

**Schedule pattern:** Daily morning scan (Israel time), with domain-specific additional schedules as needed.

**Mode:** All agents start SUPERVISED. Autonomy is earned per-action through positive feedback.

**MCP:** Agor is always included. Domain-specific MCPs added per agent.

**Tracking:** Each agent gets a card on Oggy's board, moving Explore → Define → Active → Insights.
