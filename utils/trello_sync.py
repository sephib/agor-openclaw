#!/usr/bin/env python3
"""
Trello Personal Task Sync - Label-Based Bidirectional Sync

Syncs personal tasks from B.Berry Projects Trello board to Agor zones using LABELS:
- Cards stay in their original lists (בית, שוטף, מסיבה 50, etc.)
- Backlog: Cards with "backlog" label (top 10 most recent)
- Active: Cards with "active" label (from any list)
- Done: Cards with "done" label → archive in Trello
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
import urllib.request
import urllib.parse
import urllib.error
import ssl
from time import sleep

# Create SSL context that works on macOS
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Paths
WORKSPACE_ROOT = Path(__file__).parent.parent
CONFIG_FILE = WORKSPACE_ROOT / "memory/agor-state/personal-tasks.json"
CREDENTIALS_FILE = Path.home() / ".config/mcp-trello.env"
DAILY_LOG_DIR = WORKSPACE_ROOT / "memory"

# Label IDs (created in Trello)
LABEL_IDS = {
    "backlog": "69b12e49c497c49bc237af68",
    "active": "69b12e4a3cbdfe167a6b9def",
    "done": "69b12e4ac2818bc88abd2b4d"
}


def load_credentials() -> Dict[str, str]:
    """Load Trello API credentials from env file"""
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(f"Credentials not found: {CREDENTIALS_FILE}")

    creds = {}
    with open(CREDENTIALS_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if "=" in line:
                    key, value = line.split("=", 1)
                    creds[key] = value.strip('"')

    if "TRELLO_API_KEY" not in creds or "TRELLO_TOKEN" not in creds:
        raise ValueError("Missing TRELLO_API_KEY or TRELLO_TOKEN in credentials file")

    return creds


def load_config() -> Dict:
    """Load sync configuration from personal-tasks.json"""
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")

    with open(CONFIG_FILE) as f:
        return json.load(f)


def save_config(config: Dict) -> None:
    """Save updated configuration to personal-tasks.json"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def api_request(url: str, creds: Dict, method: str = "GET", data: Optional[Dict] = None) -> Dict:
    """Make authenticated Trello API request with retry logic"""
    full_url = f"https://api.trello.com{url}"
    separator = "&" if "?" in url else "?"
    full_url += f"{separator}key={creds['TRELLO_API_KEY']}&token={creds['TRELLO_TOKEN']}"

    for attempt in range(3):
        try:
            if method == "GET":
                with urllib.request.urlopen(full_url, timeout=30, context=ssl_context) as response:
                    return json.loads(response.read().decode())
            elif method in ["PUT", "POST", "DELETE"]:
                if data:
                    encoded_data = urllib.parse.urlencode(data).encode()
                else:
                    encoded_data = None
                req = urllib.request.Request(full_url, data=encoded_data, method=method)
                with urllib.request.urlopen(req, timeout=30, context=ssl_context) as response:
                    result = response.read().decode()
                    return json.loads(result) if result else {}
            else:
                raise ValueError(f"Unsupported method: {method}")

        except urllib.error.HTTPError as e:
            if e.code == 429:  # Rate limit
                wait_time = 2 ** attempt
                print(f"Rate limited, waiting {wait_time}s...")
                sleep(wait_time)
                continue
            raise
        except Exception as e:
            if attempt < 2:
                print(f"Request failed (attempt {attempt + 1}/3): {e}")
                sleep(1)
                continue
            raise

    raise Exception("API request failed after 3 attempts")


def fetch_all_cards(creds: Dict, board_id: str) -> List[Dict]:
    """Fetch ALL cards from the board (across all lists)"""
    url = f"/1/boards/{board_id}/cards?fields=id,name,desc,url,dateLastActivity,labels,due,idList&members=false&attachments=false"
    return api_request(url, creds)


def get_list_name(creds: Dict, config: Dict, list_id: str) -> str:
    """Get list name from config or fetch from API"""
    # Check config first
    for lst in config['sync_config']['trello_lists'].get('all_lists', []):
        if lst['id'] == list_id:
            return lst['name']

    # Fallback to API
    try:
        url = f"/1/lists/{list_id}?fields=name"
        result = api_request(url, creds)
        return result.get('name', 'Unknown')
    except:
        return 'Unknown'


def add_label_to_card(creds: Dict, card_id: str, label_id: str) -> None:
    """Add a label to a card"""
    url = f"/1/cards/{card_id}/idLabels"
    api_request(url, creds, method="POST", data={"value": label_id})


def remove_label_from_card(creds: Dict, card_id: str, label_id: str) -> None:
    """Remove a label from a card"""
    url = f"/1/cards/{card_id}/idLabels/{label_id}"
    api_request(url, creds, method="DELETE")


def archive_card(creds: Dict, card_id: str) -> Dict:
    """Archive a Trello card"""
    url = f"/1/cards/{card_id}"
    return api_request(url, creds, method="PUT", data={"closed": "true"})


def has_label(card: Dict, label_name: str) -> bool:
    """Check if card has a specific label"""
    return any(label.get('name') == label_name for label in card.get('labels', []))


def get_label_id_from_card(card: Dict, label_name: str) -> Optional[str]:
    """Get label ID from card by name"""
    for label in card.get('labels', []):
        if label.get('name') == label_name:
            return label.get('id')
    return None


def sync_trello_to_agor(creds: Dict, config: Dict) -> tuple:
    """Sync Trello state (label-based) to local Agor state"""
    sync_config = config['sync_config']
    board_id = sync_config['trello_board_id']

    # Fetch ALL cards from board
    print("Fetching all cards from Trello board...")
    all_cards = fetch_all_cards(creds, board_id)

    # Filter by labels
    backlog_cards = [c for c in all_cards if has_label(c, 'backlog') and not has_label(c, 'active') and not has_label(c, 'done')]
    active_cards = [c for c in all_cards if has_label(c, 'active')]

    # Sort backlog by activity, take top 10
    backlog_cards.sort(key=lambda c: c.get('dateLastActivity', ''), reverse=True)
    backlog_cards = backlog_cards[:10]

    # Build new task list
    new_tasks = []

    # Add active tasks
    for card in active_cards:
        list_name = get_list_name(creds, config, card['idList'])
        task = {
            "task_id": card['id'],
            "trello_card_id": card['id'],
            "trello_list_id": card['idList'],
            "trello_list_name": list_name,
            "title": card['name'],
            "description": card.get('desc', ''),
            "status": "active",
            "zone_id": sync_config['agor_zones']['active'],
            "created_at": card.get('dateLastActivity'),
            "updated_at": card.get('dateLastActivity'),
            "completed_at": None,
            "trello_url": card['url'],
            "labels": [label['name'] for label in card.get('labels', [])],
            "due_date": card.get('due'),
            "last_synced": datetime.now(timezone.utc).isoformat()
        }
        new_tasks.append(task)

    # Add backlog tasks
    for card in backlog_cards:
        list_name = get_list_name(creds, config, card['idList'])
        task = {
            "task_id": card['id'],
            "trello_card_id": card['id'],
            "trello_list_id": card['idList'],
            "trello_list_name": list_name,
            "title": card['name'],
            "description": card.get('desc', ''),
            "status": "backlog",
            "zone_id": sync_config['agor_zones']['backlog'],
            "created_at": card.get('dateLastActivity'),
            "updated_at": card.get('dateLastActivity'),
            "completed_at": None,
            "trello_url": card['url'],
            "labels": [label['name'] for label in card.get('labels', [])],
            "due_date": card.get('due'),
            "last_synced": datetime.now(timezone.utc).isoformat()
        }
        new_tasks.append(task)

    stats = {
        "active_count": len(active_cards),
        "backlog_count": len(backlog_cards),
        "total_synced": len(new_tasks)
    }

    return new_tasks, stats


def sync_agor_to_trello(creds: Dict, old_tasks: List[Dict], new_tasks: List[Dict], config: Dict) -> tuple:
    """Detect local changes and sync labels back to Trello"""
    sync_config = config['sync_config']

    changes = {
        "moved_to_active": 0,
        "moved_to_backlog": 0,
        "archived": 0,
        "errors": []
    }

    # Create lookup maps
    old_tasks_map = {t['task_id']: t for t in old_tasks}
    new_tasks_map = {t['task_id']: t for t in new_tasks}

    # Check for status changes
    for task_id, old_task in old_tasks_map.items():
        if task_id not in new_tasks_map:
            # Task was deleted/archived in Trello
            continue

        new_task = new_tasks_map[task_id]
        old_status = old_task.get('status')
        new_status = new_task.get('status')

        # Skip if no status change
        if old_status == new_status:
            continue

        # Handle status transitions (old = local change, new = Trello current state)
        try:
            if old_status == "active" and new_status == "backlog":
                # Local change: user wants to activate this card
                # Action: Add "active" label, remove "backlog" label
                print(f"Activating '{new_task['title']}'...")
                add_label_to_card(creds, task_id, LABEL_IDS['active'])
                remove_label_from_card(creds, task_id, LABEL_IDS['backlog'])
                # Update new_task to reflect change
                new_task['status'] = 'active'
                new_task['zone_id'] = sync_config['agor_zones']['active']
                if 'backlog' in new_task['labels']:
                    new_task['labels'].remove('backlog')
                if 'active' not in new_task['labels']:
                    new_task['labels'].append('active')
                changes["moved_to_active"] += 1

            elif old_status == "backlog" and new_status == "active":
                # Trello change: card was activated in Trello
                # Already reflected in new_task, no action needed
                pass

            elif old_status == "done":
                # Local change: user marked as done
                # Action: Add "done" label, then archive
                print(f"Marking done and archiving '{new_task['title']}'...")
                add_label_to_card(creds, task_id, LABEL_IDS['done'])
                sleep(0.5)  # Brief pause before archiving
                archive_card(creds, task_id)
                changes["archived"] += 1
                # Remove from new_tasks
                new_tasks = [t for t in new_tasks if t['task_id'] != task_id]

        except Exception as e:
            error_msg = f"Failed to sync '{new_task['title']}': {e}"
            print(f"ERROR: {error_msg}")
            changes["errors"].append(error_msg)

    return new_tasks, changes


def log_sync_summary(stats: Dict, changes: Dict) -> None:
    """Log sync summary to daily memory"""
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = DAILY_LOG_DIR / f"{today}.md"

    timestamp = datetime.now().strftime("%H:%M")
    summary = f"""
### Personal Task Sync - {timestamp} (Label-Based)

**Trello → Agor:**
- Active tasks: {stats['active_count']} cards with "active" label
- Backlog: {stats['backlog_count']}/10 cards with "backlog" label
- Total synced: {stats['total_synced']} tasks
- Note: Cards stay in original lists (בית, שוטף, etc.)

**Agor → Trello:**
- Moved to active: {changes['moved_to_active']} (added "active" label)
- Archived: {changes['archived']} (added "done" label + archived)
- Errors: {len(changes['errors'])}

"""

    if changes['errors']:
        summary += "**Errors:**\n"
        for error in changes['errors']:
            summary += f"- {error}\n"
        summary += "\n"

    # Append to daily log
    with open(log_file, 'a') as f:
        f.write(summary)

    print(f"\nSync summary logged to {log_file}")


def main():
    """Main sync execution"""
    print("=== Trello Personal Task Sync (Label-Based) ===\n")

    try:
        # Load credentials and config
        print("Loading credentials and configuration...")
        creds = load_credentials()
        config = load_config()
        old_tasks = config.get('tasks', [])

        # Sync Trello → Agor
        new_tasks, stats = sync_trello_to_agor(creds, config)
        print(f"\n✓ Fetched {stats['total_synced']} tasks from Trello (label-based)")
        print(f"  - Active: {stats['active_count']} (cards with 'active' label)")
        print(f"  - Backlog: {stats['backlog_count']}/10 (cards with 'backlog' label)")

        # Sync Agor → Trello (detect and push label changes)
        print("\nChecking for local changes to sync back...")
        new_tasks, changes = sync_agor_to_trello(creds, old_tasks, new_tasks, config)

        total_changes = changes['moved_to_active'] + changes['archived']
        if total_changes > 0:
            print(f"\n✓ Synced {total_changes} changes to Trello (labels)")
        else:
            print("\n✓ No local changes to sync")

        # Update config
        config['tasks'] = new_tasks
        config['last_synced'] = datetime.now(timezone.utc).isoformat()
        save_config(config)
        print(f"\n✓ Updated {CONFIG_FILE}")

        # Log summary
        log_sync_summary(stats, changes)

        print("\n=== Sync Complete ===")
        return 0

    except Exception as e:
        print(f"\n✗ Sync failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
