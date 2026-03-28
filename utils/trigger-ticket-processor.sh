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

    # CRITICAL: Generate actions BEFORE creating orchestrator
    # This Python script reads state and decides what to do
    log "Generating action list (checking for duplicates)..."
    ACTIONS_FILE=$(python3 "$WORKSPACE_ROOT/utils/generate_actions.py" "$LATEST_PLAN" 2>&1 | grep "Actions saved to:" | awk '{print $NF}')

    if [ -z "$ACTIONS_FILE" ] || [ ! -f "$ACTIONS_FILE" ]; then
        log "ERROR: Failed to generate actions file"
        exit 1
    fi

    log "Actions file: $ACTIONS_FILE"

    # PRE-FLIGHT VERIFICATION: Check for potential duplicates
    log "Running pre-flight verification..."
    if python3 "$WORKSPACE_ROOT/utils/verify_no_duplicates.py" \
        --mode pre-flight \
        --plan-file "$LATEST_PLAN" \
        --actions-file "$ACTIONS_FILE" \
        --quiet; then
        log "✓ Pre-flight verification passed"
    else
        VERIFY_EXIT=$?
        if [ $VERIFY_EXIT -eq 1 ]; then
            log "⛔ DUPLICATE RISK DETECTED - ABORTING"
            log "Check verification report in memory/verification-reports/"
            exit 1
        elif [ $VERIFY_EXIT -eq 2 ]; then
            log "⚠ Configuration issues detected but continuing"
        fi
    fi

    # Read action stats
    UPDATE_COUNT=$(jq '.stats.updates' "$ACTIONS_FILE")
    CREATE_COUNT=$(jq '.stats.creates' "$ACTIONS_FILE")
    TOTAL_WORK=$((UPDATE_COUNT + CREATE_COUNT))

    log "Work to process: $UPDATE_COUNT updates, $CREATE_COUNT creates"

    if [ "$TOTAL_WORK" -eq 0 ]; then
        log "No tasks to process (all tickets already have active sessions)"
        exit 0
    fi

    # Create Agor session - CONFIGURED
    WORKTREE_ID="d1ed5f5a-1937-4687-bb6c-325adb69a4f9"
    AGOR_API="http://localhost:3030/api"

    log "Creating Agor session in worktree $WORKTREE_ID..."

    # Build prompt - SIMPLE executor, no decisions
    PROMPT="🤖 Trello Ticket Processor - Execute Pre-Computed Actions

**Your job:** Execute the action list. NO thinking, NO decisions, just DO.

## Read the Action List

\`\`\`bash
cat $ACTIONS_FILE
\`\`\`

This JSON has been pre-computed by generate_actions.py which already:
- ✅ Read the state file
- ✅ Checked for existing sessions
- ✅ Decided UPDATE vs CREATE for each ticket

## Execute Each Action (Loop Through actions Array)

\`\`\`python
import json
import sys
sys.path.insert(0, 'utils')
from session_manager import generate_update_prompt, generate_create_prompt, load_state, save_state

# Load actions
actions_data = json.load(open('$ACTIONS_FILE'))
state = load_state()

stats = {'updated': 0, 'created': 0}

# Execute each action
for action in actions_data['actions']:
    if action['action'] == 'update':
        # UPDATE existing session
        prompt = generate_update_prompt(action['task'])
        result = agor_sessions_prompt(
            session_id=action['session_id'],
            mode='continue',
            prompt=prompt
        )
        print(f\"✅ UPDATED {action['session_id'][:8]} - {action['title']}\")
        stats['updated'] += 1

    elif action['action'] == 'create':
        # CREATE new session
        prompt = generate_create_prompt(action['task'], action['category'])
        result = agor_sessions_create(
            worktree_id='659dbc25-b301-4e2c-ab26-c07cd1737fcb',
            agentic_tool='claude-code',
            title=action['title'],
            initial_prompt=prompt
        )
        print(f\"✅ CREATED {result.session_id[:8]} - {action['title']}\")

        # Track in state
        from session_manager import track_session_creation
        track_session_creation(result.session_id, action['task'], action['category'], state)
        stats['created'] += 1

# Save state
from datetime import datetime, timezone
state['last_run'] = datetime.now(timezone.utc).isoformat()
state['stats'] = stats
save_state(state)

print(f\"\n✅ Complete: Updated {stats['updated']}, Created {stats['created']}\")
\`\`\`

## That's It!

Just execute the actions. The Python script already did all the thinking.

Expected: $UPDATE_COUNT updates, $CREATE_COUNT creates
"

    # Create Agor session - AUTO-EXECUTION ENABLED
    # NOTE: Explicitly set permissionConfig to allow MCP tools (Trello access)
    log "Calling Agor API to create session..."
    RESPONSE=$(curl -s -X POST "$AGOR_API/sessions" \
      -H "Content-Type: application/json" \
      -d "$(jq -n \
        --arg worktreeId "$WORKTREE_ID" \
        --arg agenticTool "claude-code" \
        --arg initialPrompt "$PROMPT" \
        '{
          worktreeId: $worktreeId,
          agenticTool: $agenticTool,
          initialPrompt: $initialPrompt,
          permissionConfig: {
            mode: "acceptEdits"
          }
        }')")

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
