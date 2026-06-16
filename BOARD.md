# BOARD.md - Oggy's Agent Guide Board

- **Board ID:** `019ecc25-547e-725c-a50d-75b657741ff2`
- **Board Name:** Oggy's Agent Guide
- **Board URL:** http://localhost:3030/ui/b/my-agent-guide-s-board/

---

## Purpose

This is a **meta board** — not where agents run, but where we design them and track how they perform.

**Flow:** Explore needs → Define agent guidelines → Launch agents on their own boards → Track active agents → Gather insights back here

---

## Zones

### Explore

- **Zone ID:** zone-explore
- **Purpose:** Investigating needs — "I have this problem, could an agent help?"
- **Workflow State:** exploring
- **What goes here:**
  - Cards describing problems or workflows that might benefit from agents
  - Research notes on what's possible
  - Questions to investigate
- **Agent Behavior:**
  - Brainstorm and research feasibility
  - Identify tools, MCP integrations, and skills needed
  - Move to Define when the concept is clear enough to spec out

### Define

- **Zone ID:** zone-define
- **Purpose:** Designing the agent — writing guidelines, SOUL, workflow, tools it needs
- **Workflow State:** defining
- **What goes here:**
  - Agent specs (SOUL.md drafts, CLAUDE.md guidelines)
  - Tool/MCP requirements
  - Workflow diagrams
  - Board and zone designs for the agent's own board
- **Agent Behavior:**
  - Draft agent configuration files
  - Define what repos, tools, and integrations the agent needs
  - Move to Active once the agent is created and launched on its own board

### Active

- **Zone ID:** zone-active
- **Purpose:** Agents that are live on other boards — tracking their status
- **Workflow State:** active
- **What goes here:**
  - Cards referencing agents running on other boards
  - Links to their board, worktrees, sessions
  - Status updates and health checks
- **Agent Behavior:**
  - Monitor agent performance
  - Check if agents are stuck, blocked, or producing good results
  - Gather findings and move learnings to Insights

### Insights

- **Zone ID:** zone-insights
- **Purpose:** Learnings from active agents — what works, what needs adjustment
- **Workflow State:** reflecting
- **What goes here:**
  - Patterns discovered (e.g., "Trello MCP can't comment, use curl workaround")
  - Agent refinement notes
  - Workflow improvements to feed back into Define
- **Agent Behavior:**
  - Synthesize learnings
  - Update agent guidelines based on real-world experience
  - Feed improvements back to agents in Active or new specs in Define

---

## Workflow Transitions

```
Explore → Define → Active → Insights
   ↑                           |
   └───────────────────────────┘
         (refine and iterate)
```

---

## Notes

- Agents run on their OWN boards (Jounce-speckit, openclaw-agor, etc.)
- This board tracks the meta-level: what agents exist, what they do, how well they work
- Cards here reference external boards, worktrees, and sessions
- Oggy (this agent) is the advisor who helps design and evaluate agents
