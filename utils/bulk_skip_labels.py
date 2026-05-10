#!/usr/bin/env python3
"""
Bulk Skip Labels — Add 'skip' label to all active cards on the board.

Pauses all automated scheduling. Remove 'skip' from individual cards
to re-engage the agent on that ticket.

Usage: uv run python utils/bulk_skip_labels.py
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from trello_sync import load_credentials, api_request, add_label_to_card, has_label, LABEL_IDS

BOARD_ID = "5af14633e01cb0c5e1df9df6"


def fetch_open_cards(creds):
    url = f"/1/boards/{BOARD_ID}/cards?fields=id,name,labels,closed"
    all_cards = api_request(url, creds)
    return [c for c in all_cards if not c.get('closed', False)]


def main():
    creds = load_credentials()
    cards = fetch_open_cards(creds)

    to_label = [c for c in cards if not has_label(c, 'skip')]
    already_skipped = len(cards) - len(to_label)

    print(f"{len(cards)} open cards: {already_skipped} already have 'skip', labeling {len(to_label)}...")

    success, failed = 0, 0
    for card in to_label:
        try:
            add_label_to_card(creds, card['id'], LABEL_IDS['skip'])
            print(f"  ✓ {card['name']}")
            success += 1
            time.sleep(0.1)
        except Exception as e:
            print(f"  ✗ {card['name']}: {e}")
            failed += 1

    print(f"\nDone: {success} labeled, {failed} failed, {already_skipped} already had 'skip'")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
