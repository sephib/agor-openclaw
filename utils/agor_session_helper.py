#!/usr/bin/env python3
"""
Agor Session Helper - Create sessions with proper MCP tool access

This helper ensures sessions have access to MCP tools (like Trello)
by explicitly setting permissionConfig without allowedTools restriction.
"""

import json
import requests
from typing import Optional, Dict, List


AGOR_API = "http://localhost:3030/api"


def create_session(
    worktree_id: str,
    agentic_tool: str = "claude-code",
    initial_prompt: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    context_files: Optional[List[str]] = None,
    allow_all_tools: bool = True
) -> Dict:
    """
    Create an Agor session with explicit permission configuration.

    Args:
        worktree_id: Target worktree ID
        agentic_tool: Agent type (default: claude-code)
        initial_prompt: Initial prompt to execute
        title: Session title
        description: Session description
        context_files: Context file paths to load
        allow_all_tools: If True, allows all tools including MCP (default: True)

    Returns:
        Dict with session details including session_id

    Raises:
        requests.HTTPError: If API call fails
    """
    payload = {
        "worktreeId": worktree_id,
        "agenticTool": agentic_tool,
    }

    if initial_prompt:
        payload["initialPrompt"] = initial_prompt

    if title:
        payload["title"] = title

    if description:
        payload["description"] = description

    if context_files:
        payload["contextFiles"] = context_files

    # Critical: Set permissionConfig to allow MCP tools
    if allow_all_tools:
        payload["permissionConfig"] = {
            "mode": "acceptEdits"
            # No allowedTools array = all tools allowed (including MCP)
        }

    response = requests.post(
        f"{AGOR_API}/sessions",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    response.raise_for_status()
    return response.json()


def create_trello_ticket_session(
    task: Dict,
    visibility_worktree_id: str = "659dbc25-b301-4e2c-ab26-c07cd1737fcb"
) -> Dict:
    """
    Create a session for handling a Trello ticket.

    Args:
        task: Task dict from trello-plan JSON (with card_id, title, description, etc.)
        visibility_worktree_id: Trello visibility hub worktree ID

    Returns:
        Dict with session details
    """
    category = task.get('category', 'personal')

    # Build prompt based on task category
    if category == 'coding':
        prompt = f"""Handle coding ticket: {task['title']}

Task Details:
- Card ID: {task['card_id']}
- Title: {task['title']}
- Description: {task['description']}
- Priority: {task['priority_score']} ({task['priority_reasoning']})
- Labels: {', '.join(task.get('labels', []))}
- Due: {task.get('due_date', 'None')}
- Trello URL: {task['url']}
- List: {task['list_name']}

Your Job:
1. Create dedicated worktree for implementation: ticket-{task['card_id'][:8]}
2. Create worker session in that worktree
3. Implement the feature/fix
4. Update Trello card with progress
5. Track in memory/agor-state/trello-processor.json
"""
    elif category == 'research':
        prompt = f"""Handle research ticket: {task['title']}

Task Details:
- Card ID: {task['card_id']}
- Title: {task['title']}
- Description: {task['description']}
- Priority: {task['priority_score']} ({task['priority_reasoning']})
- Trello URL: {task['url']}
- List: {task['list_name']}

Your Job:
1. Investigate the topic/question
2. Gather relevant information
3. Provide findings and recommendations
4. Post findings to Trello card
5. Track in memory/agor-state/trello-processor.json
"""
    else:  # personal
        prompt = f"""Handle personal task: {task['title']}

Task Details:
- Card ID: {task['card_id']}
- Title: {task['title']}
- Description: {task['description']}
- Priority: {task['priority_score']} ({task['priority_reasoning']})
- Trello URL: {task['url']}
- List: {task['list_name']}

Your Job:
1. Research and provide helpful information
2. Post findings/recommendations to Trello card
3. Track in memory/agor-state/trello-processor.json
"""

    return create_session(
        worktree_id=visibility_worktree_id,
        agentic_tool="claude-code",
        initial_prompt=prompt,
        title=task['title'],
        allow_all_tools=True  # Critical: Enable MCP tools
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 agor_session_helper.py <plan_file.json>")
        print("Creates sessions for all tasks in the plan")
        sys.exit(1)

    plan_file = sys.argv[1]

    with open(plan_file) as f:
        plan = json.load(f)

    created = []

    # Create sessions for coding tasks
    for task in plan.get('coding_tasks', []):
        print(f"Creating coding session: {task['title']}")
        session = create_trello_ticket_session(task)
        created.append({
            'session_id': session['session_id'],
            'title': task['title'],
            'category': 'coding',
            'url': f"http://localhost:3030/s/{session['session_id']}"
        })
        print(f"  ✓ Session: {session['session_id']}")

    # Create sessions for research tasks
    for task in plan.get('research_tasks', []):
        print(f"Creating research session: {task['title']}")
        session = create_trello_ticket_session(task)
        created.append({
            'session_id': session['session_id'],
            'title': task['title'],
            'category': 'research',
            'url': f"http://localhost:3030/s/{session['session_id']}"
        })
        print(f"  ✓ Session: {session['session_id']}")

    # Create sessions for personal tasks
    for task in plan.get('personal_tasks', []):
        print(f"Creating personal session: {task['title']}")
        session = create_trello_ticket_session(task)
        created.append({
            'session_id': session['session_id'],
            'title': task['title'],
            'category': 'personal',
            'url': f"http://localhost:3030/s/{session['session_id']}"
        })
        print(f"  ✓ Session: {session['session_id']}")

    print(f"\n✓ Created {len(created)} sessions total")
    print("\nSessions:")
    for s in created:
        print(f"  - [{s['category']}] {s['title']}")
        print(f"    {s['url']}")
