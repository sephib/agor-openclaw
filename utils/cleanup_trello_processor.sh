#!/bin/bash
# Automated Cleanup for Trello Ticket Processor
# Manages retention of logs, plans, and state data

set -e

# Configuration
WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_RETENTION_DAYS=30
PLAN_RETENTION_DAYS=14
ARCHIVED_TASK_RETENTION_DAYS=30

# Ensure we're in the right directory
cd "$WORKSPACE_ROOT"

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Main cleanup function
main() {
    log "=== Trello Processor Cleanup ==="
    log "Workspace: $WORKSPACE_ROOT"
    log ""

    # 1. Clean old logs (>30 days)
    log "1. Cleaning logs older than $LOG_RETENTION_DAYS days..."
    if [ -d "memory/logs" ]; then
        DELETED_LOGS=$(find memory/logs -name "trello-processor-*.log" -mtime +$LOG_RETENTION_DAYS -print | wc -l | tr -d ' ')
        if [ "$DELETED_LOGS" -gt 0 ]; then
            find memory/logs -name "trello-processor-*.log" -mtime +$LOG_RETENTION_DAYS -delete
            log "   ✓ Deleted $DELETED_LOGS old log files"
        else
            log "   ✓ No old logs to delete"
        fi
    else
        log "   ⚠ Logs directory not found"
    fi

    # 2. Clean old execution plans (>14 days)
    log "2. Cleaning execution plans older than $PLAN_RETENTION_DAYS days..."
    DELETED_PLANS_JSON=$(find memory -name "trello-plan-*.json" -mtime +$PLAN_RETENTION_DAYS -print | wc -l | tr -d ' ')
    DELETED_PLANS_MD=$(find memory -name "trello-plan-*.md" -mtime +$PLAN_RETENTION_DAYS -print | wc -l | tr -d ' ')
    TOTAL_PLANS=$((DELETED_PLANS_JSON + DELETED_PLANS_MD))

    if [ "$TOTAL_PLANS" -gt 0 ]; then
        find memory -name "trello-plan-*.json" -mtime +$PLAN_RETENTION_DAYS -delete
        find memory -name "trello-plan-*.md" -mtime +$PLAN_RETENTION_DAYS -delete
        log "   ✓ Deleted $TOTAL_PLANS old plan files ($DELETED_PLANS_JSON JSON, $DELETED_PLANS_MD Markdown)"
    else
        log "   ✓ No old plans to delete"
    fi

    # 3. Report disk usage
    log "3. Disk usage report:"
    if [ -d "memory/logs" ]; then
        LOGS_SIZE=$(du -sh memory/logs 2>/dev/null | cut -f1)
        log "   - Logs directory: $LOGS_SIZE"
    fi
    PLANS_SIZE=$(du -sh memory/trello-plan-* 2>/dev/null | awk '{sum+=$1} END {print sum}' || echo "0")
    log "   - Active plans: $(find memory -name "trello-plan-*" | wc -l | tr -d ' ') files"

    if [ -f "memory/agor-state/trello-processor.json" ]; then
        STATE_SIZE=$(du -sh memory/agor-state/trello-processor.json 2>/dev/null | cut -f1)
        log "   - State file: $STATE_SIZE"
    fi

    # 4. Report active workers
    log "4. Active workers status:"
    if [ -f "memory/agor-state/trello-processor.json" ]; then
        if command -v jq >/dev/null 2>&1; then
            ACTIVE_CODING=$(jq '.active_workers.coding_worktrees | length' memory/agor-state/trello-processor.json 2>/dev/null || echo "0")
            ACTIVE_RESEARCH=$(jq '.active_workers.research_sessions | length' memory/agor-state/trello-processor.json 2>/dev/null || echo "0")
            log "   - Active coding worktrees: $ACTIVE_CODING"
            log "   - Active research sessions: $ACTIVE_RESEARCH"
        else
            log "   ⚠ jq not installed, skipping JSON parsing"
        fi
    fi

    # 5. Report stale worktrees (requires manual review)
    log "5. Stale worktrees check:"
    log "   ⚠ Manual review required"
    log "   Run: agor worktrees list | jq '.[] | select(.zone_label == \"Done\")'"
    log "   Then delete worktrees that have been done for >7 days"

    log ""
    log "=== Cleanup Complete ==="
    log "Next cleanup: $(date -v +7d '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date -d '+7 days' '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo 'in 7 days')"
}

# Run cleanup
main "$@"
