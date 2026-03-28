#!/bin/bash
#
# Create Trello Processing Session with Proper Permissions
#
# This script creates sessions that have access to Trello MCP tools
# by explicitly setting permissionConfig without allowedTools restriction

set -e

WORKTREE_ID="${1:-d1ed5f5a-1937-4687-bb6c-325adb69a4f9}"
AGOR_API="http://localhost:3030/api"

if [ -z "$2" ]; then
    echo "Usage: $0 <worktree_id> <prompt>"
    echo "Example: $0 659dbc25-b301-4e2c-ab26-c07cd1737fcb 'Handle Trello ticket...'"
    exit 1
fi

PROMPT="$2"
TITLE="${3:-Trello Task}"

echo "Creating session in worktree: $WORKTREE_ID"
echo "Title: $TITLE"

# Create session with explicit permission config that allows all tools
RESPONSE=$(curl -s -X POST "$AGOR_API/sessions" \
  -H "Content-Type: application/json" \
  -d "$(jq -n \
    --arg worktreeId "$WORKTREE_ID" \
    --arg agenticTool "claude-code" \
    --arg initialPrompt "$PROMPT" \
    --arg title "$TITLE" \
    '{
      worktreeId: $worktreeId,
      agenticTool: $agenticTool,
      initialPrompt: $initialPrompt,
      title: $title,
      permissionConfig: {
        mode: "acceptEdits"
      }
    }')")

if [ $? -eq 0 ]; then
    SESSION_ID=$(echo "$RESPONSE" | jq -r '.session_id // "unknown"')
    if [ "$SESSION_ID" != "unknown" ] && [ "$SESSION_ID" != "null" ]; then
        echo "✓ Session created: $SESSION_ID"
        echo "✓ View at: http://localhost:3030/s/$SESSION_ID"
        echo "$SESSION_ID"
    else
        echo "⚠ Session creation response: $RESPONSE" >&2
        exit 1
    fi
else
    echo "✗ Failed to create session (curl error)" >&2
    exit 1
fi
