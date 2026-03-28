#!/usr/bin/env python3
"""
Session Manager - Handle Trello ticket sessions (update existing or create new)

This module ensures that:
1. Existing sessions get updated with latest ticket info
2. New tickets get new sessions
3. No duplicate sessions are created
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Agor MCP would be used via the agent, not direct Python import
# This script is meant to be imported by the orchestrator session

STATE_FILE = Path(__file__).parent.parent / "memory/agor-state/trello-processor.json"


def load_state() -> Dict:
    """Load current state from JSON file"""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "active_coding_sessions": [],
        "active_research_sessions": [],
        "active_personal_sessions": [],
        "max_coding_worktrees": 3,
        "max_research_sessions": 2,
    }


def save_state(state: Dict) -> None:
    """Save state to JSON file"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def find_session_for_ticket(ticket_id: str, state: Dict) -> Optional[Dict]:
    """Find existing session for a given ticket ID"""
    all_sessions = (
        state.get('active_coding_sessions', []) +
        state.get('active_research_sessions', []) +
        state.get('active_personal_sessions', [])
    )

    for session in all_sessions:
        if session.get('ticket_id') == ticket_id:
            return session

    return None


def get_active_ticket_ids(state: Dict) -> set:
    """Get set of all active ticket IDs"""
    ticket_ids = set()

    for session in state.get('active_coding_sessions', []):
        ticket_ids.add(session['ticket_id'])
    for session in state.get('active_research_sessions', []):
        ticket_ids.add(session['ticket_id'])
    for session in state.get('active_personal_sessions', []):
        ticket_ids.add(session['ticket_id'])

    return ticket_ids


def generate_update_prompt(task: Dict) -> str:
    """Generate prompt for updating an existing session"""
    return f"""🔄 **Ticket Update from Trello**

Your ticket has been refreshed from Trello. Here's the current state:

**Ticket:** {task['title']}
**Card ID:** {task['card_id']}
**Trello URL:** {task['url']}

**Current Status:**
- **List:** {task['list_name']}
- **Priority:** {task['priority_score']} ({task['priority_reasoning']})
- **Labels:** {', '.join(task.get('labels', [])) or 'None'}
- **Due Date:** {task.get('due_date') or 'None'}

**Description:**
{task['description'] or 'No description'}

---

**Your Tasks:**

1. **Review Progress:** Check what you've done so far on this ticket
2. **Check for Changes:** Compare the current ticket state with what you were working on
3. **Adjust Approach:** If requirements or priorities changed, update your plan
4. **Continue Work:** Keep working on the ticket or complete remaining tasks
5. **Update Trello:** Post a status comment to the Trello card with your progress

If the ticket is complete, mark it as done in Trello and update the state file.
"""


def generate_create_prompt(task: Dict, category: str) -> str:
    """Generate prompt for creating a new session"""
    if category == 'coding':
        return f"""🆕 **New Coding Ticket from Trello**

**Ticket:** {task['title']}
**Card ID:** {task['card_id']}
**Trello URL:** {task['url']}

**Details:**
- **List:** {task['list_name']}
- **Priority:** {task['priority_score']} ({task['priority_reasoning']})
- **Labels:** {', '.join(task.get('labels', [])) or 'None'}
- **Due Date:** {task.get('due_date') or 'None'}

**Description:**
{task['description'] or 'No description'}

---

**Your Tasks:**

1. **Create Worktree:** Create isolated worktree `ticket-{task['card_id'][:8]}`
   - Use: `agor_worktrees_create`
   - Parameters: repo_id, worktree_name, board_id, create_branch=True

2. **Create Worker Session:** Create session in the new worktree
   - Use: `agor_sessions_create`
   - Pass implementation details

3. **Implement:** Complete the ticket requirements

4. **Update Trello:** Post progress updates to the card

5. **Track State:** Update `memory/agor-state/trello-processor.json`
"""

    elif category == 'research':
        return f"""🆕 **New Research Ticket from Trello**

**Ticket:** {task['title']}
**Card ID:** {task['card_id']}
**Trello URL:** {task['url']}

**Details:**
- **List:** {task['list_name']}
- **Priority:** {task['priority_score']} ({task['priority_reasoning']})

**Description:**
{task['description'] or 'No description'}

---

**Your Tasks:**

1. **Investigate:** Research the topic/question
2. **Gather Information:** Collect relevant data and findings
3. **Provide Recommendations:** Summarize findings with actionable recommendations
4. **Post to Trello:** Add your findings as a comment on the card
5. **Track State:** Update `memory/agor-state/trello-processor.json`
"""

    else:  # personal
        return f"""🆕 **New Personal Task from Trello**

**Task:** {task['title']}
**Card ID:** {task['card_id']}
**Trello URL:** {task['url']}

**Details:**
- **List:** {task['list_name']}
- **Priority:** {task['priority_score']} ({task['priority_reasoning']})

**Description:**
{task['description'] or 'No description'}

---

**Your Tasks:**

1. **Research:** Investigate and gather helpful information
2. **Provide Guidance:** Give recommendations or next steps
3. **Post to Trello:** Add findings as a comment on the card
4. **Track State:** Update `memory/agor-state/trello-processor.json`
"""


def track_session_creation(session_id: str, task: Dict, category: str, state: Dict) -> None:
    """Track newly created session in state file"""
    session_info = {
        'session_id': session_id,
        'ticket_title': task['title'],
        'ticket_id': task['card_id'],
        'category': category,
        'url': f"http://localhost:3030/b/openclaw-agor/{session_id[:8]}",
        'trello_url': task['url'],
        'created_at': datetime.now(timezone.utc).isoformat(),
        'last_updated': datetime.now(timezone.utc).isoformat(),
        'update_count': 0,
        'status': 'active',
        'note': '✅ NEW SESSION - Created by session manager'
    }

    category_key = f'active_{category}_sessions'
    if category_key not in state:
        state[category_key] = []

    state[category_key].append(session_info)


def track_session_update(session: Dict, state: Dict) -> None:
    """Track session update in state file"""
    session['last_updated'] = datetime.now(timezone.utc).isoformat()
    session['update_count'] = session.get('update_count', 0) + 1
    session['status'] = 'active'


def get_statistics(state: Dict) -> Dict:
    """Calculate current statistics"""
    return {
        'active_coding': len(state.get('active_coding_sessions', [])),
        'active_research': len(state.get('active_research_sessions', [])),
        'active_personal': len(state.get('active_personal_sessions', [])),
        'total_active': (
            len(state.get('active_coding_sessions', [])) +
            len(state.get('active_research_sessions', [])) +
            len(state.get('active_personal_sessions', []))
        )
    }


def process_plan_instructions(plan: Dict) -> str:
    """Generate markdown instructions for processing a plan"""
    state = load_state()
    active_tickets = get_active_ticket_ids(state)

    # Categorize tasks
    new_tasks = []
    update_tasks = []

    all_tasks = (
        [(t, 'coding') for t in plan.get('coding_tasks', [])] +
        [(t, 'research') for t in plan.get('research_tasks', [])] +
        [(t, 'personal') for t in plan.get('personal_tasks', [])]
    )

    for task, category in all_tasks:
        if task['card_id'] in active_tickets:
            existing = find_session_for_ticket(task['card_id'], state)
            update_tasks.append((task, category, existing))
        else:
            new_tasks.append((task, category))

    # Generate instructions
    output = "# Trello Session Processing Instructions\n\n"
    output += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    output += "## Summary\n\n"
    output += f"- **New sessions to create:** {len(new_tasks)}\n"
    output += f"- **Existing sessions to update:** {len(update_tasks)}\n"
    output += f"- **Total tasks:** {len(all_tasks)}\n\n"

    # Update existing sessions
    if update_tasks:
        output += "## 🔄 Update Existing Sessions\n\n"
        output += "Send update prompts to these active sessions:\n\n"

        for task, category, existing in update_tasks:
            output += f"### {task['title']}\n\n"
            output += f"- **Session ID:** {existing['session_id']}\n"
            output += f"- **Category:** {category}\n"
            output += f"- **Created:** {existing['created_at']}\n"
            output += f"- **Updates:** {existing.get('update_count', 0)}\n"
            output += f"- **URL:** {existing['url']}\n\n"

            output += "**Action:**\n"
            output += "```python\n"
            output += f"# Send update to session {existing['session_id'][:8]}\n"
            output += f"agor_sessions_prompt(\n"
            output += f"    session_id='{existing['session_id']}',\n"
            output += f"    prompt=generate_update_prompt(task)\n"
            output += f")\n"
            output += "# Mark as updated in state\n"
            output += f"track_session_update(existing, state)\n"
            output += "```\n\n"

    # Create new sessions
    if new_tasks:
        output += "## 🆕 Create New Sessions\n\n"
        output += "Create sessions for these new tickets:\n\n"

        for task, category in new_tasks:
            output += f"### {task['title']}\n\n"
            output += f"- **Card ID:** {task['card_id']}\n"
            output += f"- **Category:** {category}\n"
            output += f"- **Priority:** {task['priority_score']}\n"
            output += f"- **Trello:** {task['url']}\n\n"

            output += "**Action:**\n"
            output += "```python\n"
            output += f"# Create session in trello-visibility-hub\n"
            output += f"session = agor_sessions_create(\n"
            output += f"    worktree_id='659dbc25-b301-4e2c-ab26-c07cd1737fcb',\n"
            output += f"    agentic_tool='claude-code',\n"
            output += f"    title='{task['title']}',\n"
            output += f"    initial_prompt=generate_create_prompt(task, '{category}')\n"
            output += f")\n"
            output += "# Track in state\n"
            output += f"track_session_creation(session.session_id, task, '{category}', state)\n"
            output += "```\n\n"

    # Save state
    output += "## 💾 Save State\n\n"
    output += "After all updates and creations:\n\n"
    output += "```python\n"
    output += "state['last_run'] = datetime.now(timezone.utc).isoformat()\n"
    output += "state['stats']['created'] = len(new_tasks)\n"
    output += "state['stats']['updated'] = len(update_tasks)\n"
    output += "save_state(state)\n"
    output += "```\n\n"

    return output


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 session_manager.py <plan_file.json>")
        sys.exit(1)

    plan_file = sys.argv[1]
    with open(plan_file) as f:
        plan = json.load(f)

    instructions = process_plan_instructions(plan)
    print(instructions)
