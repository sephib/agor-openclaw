#!/usr/bin/env python3
"""
List Context - Shared context files for Trello lists.

Each Trello list can have a context file at:
  memory/list-context/{worktree_name}.md

List types determine context depth:
  project  — full card description synthesis + sibling session table
  shopping — category-level rules + item summary
  task     — no shared context (each card is independent)

Sessions read this file at startup (injected into initialPrompt by orchestrator).
Sessions append list-level discoveries back to this file.
"""

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

WORKSPACE_ROOT = Path(__file__).parent.parent
LIST_CONTEXT_DIR = WORKSPACE_ROOT / "memory" / "list-context"

# Patterns for list type classification (checked against lowercased list name)
_TYPE_PATTERNS = [
    (r'\b(trip|travel|vacation|holiday|tour|brno|prague|japan|abroad)\b', 'project'),
    (r'\b(party|event|wedding|mitzvah|celebration|fest|conference)\b', 'project'),
    (r'\b(home|house|renovation|apartment|flat|garden|kitchen)\b', 'project'),
    (r'\b(aliexpress|amazon|ebay|shopping|buy|order|purchase|store)\b', 'shopping'),
]


def classify_list_type(list_name: str) -> str:
    """Classify a Trello list as 'project', 'shopping', or 'task'"""
    lower = list_name.lower()
    for pattern, list_type in _TYPE_PATTERNS:
        if re.search(pattern, lower):
            return list_type
    return 'task'


def get_context_path(worktree_name: str) -> Path:
    return LIST_CONTEXT_DIR / f"{worktree_name}.md"


def read_list_context(worktree_name: str) -> str:
    path = get_context_path(worktree_name)
    return path.read_text() if path.exists() else ""


def synthesize_list_context(
    list_name: str,
    list_type: str,
    worktree_name: str,
    cards: List[Dict],
    sibling_sessions: Optional[List[Dict]] = None,
) -> str:
    """
    Build the shared context markdown from all cards in a list.

    cards: list of dicts with 'title', 'description'/'desc', 'url', 'card_id'
    sibling_sessions: list of dicts with 'title', 'session_id', 'card_id'
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    lines = [
        f"# List Context: {list_name}",
        f"**Type:** {list_type}  |  **Synthesized:** {now}  |  **Cards:** {len(cards)}",
        "",
    ]

    if list_type == 'project':
        lines += _project_section(cards)
    elif list_type == 'shopping':
        lines += _shopping_section(cards)

    if sibling_sessions:
        lines += _sibling_section(sibling_sessions)

    # Preserve any existing session discoveries from previous runs
    existing = read_list_context(worktree_name)
    discoveries = _extract_discoveries(existing)
    if discoveries:
        lines.append("## Session Discoveries (from previous runs)")
        lines.append("")
        lines.append(discoveries)
        lines.append("")

    lines += [
        "## Append Your Discoveries Here",
        "<!-- When you learn something relevant to ALL tasks in this list,",
        "     append a line below: - [YYYY-MM-DD] YourCardTitle: discovery -->",
        "",
    ]

    return "\n".join(lines)


def _project_section(cards: List[Dict]) -> List[str]:
    lines = ["## Project Cards", ""]
    for card in cards:
        title = card.get('title') or card.get('name', '?')
        desc = (card.get('description') or card.get('desc') or '').strip()
        url = card.get('url', '')
        lines.append(f"### {title}")
        if url:
            lines.append(f"[Trello]({url})")
        if desc:
            truncated = desc[:400] + ("..." if len(desc) > 400 else "")
            lines.append(truncated)
        else:
            lines.append("_(no description yet)_")
        lines.append("")
    return lines


def _shopping_section(cards: List[Dict]) -> List[str]:
    lines = ["## Items in This List", ""]
    for card in cards:
        title = card.get('title') or card.get('name', '?')
        desc = (card.get('description') or card.get('desc') or '').strip()
        summary = desc[:120] + ("..." if len(desc) > 120 else "") if desc else ""
        entry = f"- **{title}**"
        if summary:
            entry += f": {summary}"
        lines.append(entry)
    lines.append("")
    return lines


def _sibling_section(sibling_sessions: List[Dict]) -> List[str]:
    lines = ["## Sibling Sessions (this run)", ""]
    for s in sibling_sessions:
        title = s.get('title', s.get('card_id', '?'))
        sid = s.get('session_id', '')[:8]
        status = s.get('status', 'active')
        lines.append(f"- **{title}** — session `{sid}` ({status})")
    lines.append("")
    return lines


def _extract_discoveries(existing_content: str) -> str:
    """Pull out the discoveries section from a previously written context file"""
    marker = "## Append Your Discoveries Here"
    if marker not in existing_content:
        return ""
    # Everything between the two discovery sections
    discovery_marker = "## Session Discoveries (from previous runs)"
    if discovery_marker in existing_content:
        start = existing_content.index(discovery_marker) + len(discovery_marker)
        end = existing_content.index(marker)
        block = existing_content[start:end].strip()
        # Remove comment lines
        lines = [l for l in block.splitlines() if not l.strip().startswith("<!--")]
        return "\n".join(lines).strip()
    # Check for appended lines after the marker (from session write-backs)
    after = existing_content.split(marker, 1)[1]
    lines = [
        l for l in after.splitlines()
        if l.strip().startswith("- [") and not l.strip().startswith("<!--")
    ]
    return "\n".join(lines).strip()


def write_list_context(worktree_name: str, content: str):
    LIST_CONTEXT_DIR.mkdir(parents=True, exist_ok=True)
    get_context_path(worktree_name).write_text(content)


def get_context_for_prompt(
    worktree_name: str,
    list_name: str,
    list_type: str,
) -> str:
    """Return the block to inject into a session's initialPrompt, or '' for 'task' lists"""
    if list_type == 'task':
        return ""
    content = read_list_context(worktree_name)
    if not content:
        return ""
    return f"\n## Shared List Context: {list_name}\n\n{content}\n"
