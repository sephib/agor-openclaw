#!/bin/bash
# Install Cron Job for Trello Ticket Processor

set -e

WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TRIGGER_SCRIPT="$WORKSPACE_ROOT/utils/trigger-ticket-processor.sh"
CRON_EXPRESSION="0 */4 * * *"
CRON_COMMENT="# Trello Ticket Processor - Every 4 hours"

echo "=== Trello Ticket Processor - Cron Installation ==="
echo ""
echo "This will install a cron job to run every 4 hours:"
echo "  Schedule: $CRON_EXPRESSION (00:00, 04:00, 08:00, 12:00, 16:00, 20:00)"
echo "  Script: $TRIGGER_SCRIPT"
echo ""

# Check if trigger script exists
if [ ! -f "$TRIGGER_SCRIPT" ]; then
    echo "✗ Error: Trigger script not found at $TRIGGER_SCRIPT"
    exit 1
fi

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "trello-task-processor"; then
    echo "⚠ Cron job already installed!"
    echo ""
    echo "Current entry:"
    crontab -l | grep -A 1 "Trello Ticket Processor"
    echo ""
    read -p "Do you want to reinstall? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi

    # Remove existing entry
    echo "Removing existing entry..."
    crontab -l | grep -v "trello-task-processor" | grep -v "Trello Ticket Processor" | crontab - 2>/dev/null || true
fi

# Backup existing crontab
BACKUP_FILE="$HOME/crontab-backup-$(date +%Y%m%d-%H%M%S).txt"
crontab -l > "$BACKUP_FILE" 2>/dev/null || touch "$BACKUP_FILE"
echo "✓ Backed up existing crontab to: $BACKUP_FILE"

# Add new cron entry
echo "Installing cron job..."
(crontab -l 2>/dev/null; echo ""; echo "$CRON_COMMENT"; echo "$CRON_EXPRESSION $TRIGGER_SCRIPT") | crontab -

if [ $? -eq 0 ]; then
    echo "✓ Cron job installed successfully!"
    echo ""
    echo "Verification:"
    crontab -l | tail -3
    echo ""
    echo "Schedule: Every 4 hours (00:00, 04:00, 08:00, 12:00, 16:00, 20:00)"
    echo ""
    echo "To test manually:"
    echo "  $TRIGGER_SCRIPT"
    echo ""
    echo "To view logs:"
    echo "  tail -f $WORKSPACE_ROOT/memory/logs/trello-processor-*.log"
    echo ""
    echo "To uninstall:"
    echo "  crontab -e  # Then delete the lines with 'Trello Ticket Processor'"
    echo ""
else
    echo "✗ Failed to install cron job"
    echo ""
    echo "This may require Full Disk Access on macOS:"
    echo "  System Settings → Privacy & Security → Full Disk Access"
    echo "  Add: /usr/sbin/cron or your terminal app"
    echo ""
    echo "Manual installation:"
    echo "  1. Run: crontab -e"
    echo "  2. Add this line:"
    echo "     $CRON_EXPRESSION $TRIGGER_SCRIPT"
    echo "  3. Save and exit"
    exit 1
fi
