#!/bin/bash
#
# Trigger Trello Ticket Processor
#
# This script can be run:
# 1. Manually: ./trigger-ticket-processor.sh
# 2. Via cron: Add to crontab for scheduled runs
# 3. Via GitHub Actions: Called from workflow
#

set -e

# Configuration
WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON_SCRIPT="$WORKSPACE_ROOT/utils/process_trello_tickets.py"
LOG_DIR="$WORKSPACE_ROOT/memory/logs"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/trello-processor-$TIMESTAMP.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Main execution
main() {
    log "=== Trello Ticket Processor Triggered ==="
    log "Workspace: $WORKSPACE_ROOT"
    log "Log file: $LOG_FILE"

    # Check if Python script exists
    if [ ! -f "$PYTHON_SCRIPT" ]; then
        log "ERROR: Python script not found: $PYTHON_SCRIPT"
        exit 1
    fi

    # Run Python processor to generate plan
    log "Running ticket processor..."
    if python3 "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1; then
        log "✓ Ticket processing plan generated"
    else
        log "✗ Ticket processor failed (see log above)"
        exit 1
    fi

    # Find the most recent plan file
    LATEST_PLAN=$(ls -t "$WORKSPACE_ROOT/memory/trello-plan-"*.json 2>/dev/null | head -1)

    if [ -z "$LATEST_PLAN" ]; then
        log "WARNING: No plan file found, skipping Agor session creation"
        exit 0
    fi

    log "Latest plan: $LATEST_PLAN"

    # Read plan to determine if there's work to do
    CODING_COUNT=$(jq '.coding_tasks | length' "$LATEST_PLAN")
    RESEARCH_COUNT=$(jq '.research_tasks | length' "$LATEST_PLAN")
    TOTAL_WORK=$((CODING_COUNT + RESEARCH_COUNT))

    log "Work to process: $CODING_COUNT coding tasks, $RESEARCH_COUNT research tasks"

    if [ "$TOTAL_WORK" -eq 0 ]; then
        log "No tasks to process, skipping session creation"
        exit 0
    fi

    # Create Agor session - CONFIGURED
    WORKTREE_ID="d1ed5f5a-1937-4687-bb6c-325adb69a4f9"
    AGOR_API="http://localhost:3030/api"

    log "Creating Agor session in worktree $WORKTREE_ID..."

    # Build prompt with plan details
    PROMPT="Process Trello tickets (scheduled run $TIMESTAMP):

Read and execute the plan from: $LATEST_PLAN

Found:
- $CODING_COUNT coding tasks to process
- $RESEARCH_COUNT research tasks to process

For each coding task:
1. Create isolated worktree: ticket-{card-id}
2. Create new session with task details
3. Update Trello card with worktree link and progress

For each research task:
1. Spawn subsession for investigation
2. Update Trello card with findings

Respect concurrency limits:
- Max 3 coding worktrees
- Max 2 research sessions

After completion:
- Log summary to memory/$(date +%Y-%m-%d).md
- Update memory/agor-state/trello-processor.json with active workers
"

    # Create Agor session - AUTO-EXECUTION ENABLED
    log "Calling Agor API to create session..."
    RESPONSE=$(curl -s -X POST "$AGOR_API/sessions" \
      -H "Content-Type: application/json" \
      -d "{
        \"worktreeId\": \"$WORKTREE_ID\",
        \"agenticTool\": \"claude-code\",
        \"initialPrompt\": $(echo "$PROMPT" | jq -Rs .)
      }")

    if [ $? -eq 0 ]; then
        SESSION_ID=$(echo "$RESPONSE" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
        if [ "$SESSION_ID" != "unknown" ] && [ "$SESSION_ID" != "null" ]; then
            log "✓ Session created: $SESSION_ID"
            log "✓ View at: http://localhost:3030/s/$SESSION_ID"
        else
            log "⚠ Session creation response: $RESPONSE"
        fi
    else
        log "✗ Failed to create session (curl error)"
    fi

    log ""
    log "=== Trigger Complete ==="
    log "Plan generated: $(basename "$LATEST_PLAN")"
    log "Tasks found: $TOTAL_WORK ($CODING_COUNT coding, $RESEARCH_COUNT research)"
    log "Auto-execution: ENABLED"

    # Run cleanup (retention policy)
    log ""
    log "Running retention cleanup..."
    if [ -f "$WORKSPACE_ROOT/utils/cleanup_trello_processor.sh" ]; then
        "$WORKSPACE_ROOT/utils/cleanup_trello_processor.sh" >> "$LOG_FILE" 2>&1
    else
        log "⚠ Cleanup script not found, skipping"
    fi
}

main "$@"
