"""
Batch prompt sessions via MCP HTTP API.
Reads the latest ticket-sessions JSON and sends prompts to all sessions,
skipping blocked cards.
"""
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# MCP endpoint config
MCP_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzMDhiZmFjMS00YTQ4LTRjMjYtYTQ0OS03Yjg0MjdlMjZmMGYiLCJ1aWQiOiI0ZmJiYzE4ZS05ODU4LTRiNzYtODFiYy1iN2U5MzFkYTc4MDUiLCJhdWQiOiJhZ29yOm1jcDppbnRlcm5hbCJ9.tq-j3lHLwaD0Pf2cFrYtV4Bd_M97mnirrRQ5TC1Jei8"
MCP_URL = f"http://localhost:3030/mcp?sessionToken={MCP_TOKEN}"

# Blocked card IDs (do not prompt these sessions)
BLOCKED_CARD_IDS = {
    "678007d9",  # Quizlet subscription
    "696c7f3b",  # 18/19 september (Bat Mitzvah date)
    "696519c0",  # Red Hat life insurance
    "696a08da",  # Sigi bike plate
    "69d8b4a5",  # Elections Committee
    "69b5a4cd",  # Guest list (רשימת מוזמנים)
}


def call_mcp(tool_name: str, arguments: dict) -> dict:
    """Call a tool via MCP HTTP API."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
    }
    payload_json = json.dumps(payload)

    result = subprocess.run(
        [
            "curl", "-s", "-X", "POST", MCP_URL,
            "-H", "Content-Type: application/json",
            "-H", "Accept: application/json, text/event-stream",
            "--data-binary", payload_json,
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )

    # Parse SSE response
    output = result.stdout
    for line in output.split("\n"):
        if line.startswith("data:"):
            try:
                data = json.loads(line[5:].strip())
                if "result" in data:
                    content = data["result"].get("content", [])
                    if content and content[0].get("type") == "text":
                        return json.loads(content[0]["text"])
                elif "error" in data:
                    return {"error": data["error"]}
            except json.JSONDecodeError:
                pass

    return {"error": f"Failed to parse response: {output[:200]}"}


def build_update_prompt(card, list_name: str) -> str:
    card_id = card["card_id"]
    title = card["title"]
    priority = card["priority"]
    url = card["url"]
    description = card.get("description", "") or ""
    today = datetime.now().strftime("%Y-%m-%d")

    return (
        f"Ticket update check-in: {title}\n\n"
        f"Card ID: {card_id}\n"
        f"List: {list_name}\n"
        f"Priority: {priority}\n"
        f"Trello: {url}\n\n"
        f"Description:\n{description[:400]}\n\n"
        f"Your Actions:\n"
        f"1. Review the current state of this ticket\n"
        f"2. Continue any in-progress work\n"
        f"3. Post progress update to Trello AS A COMMENT (not description edit)\n"
        f"4. When complete, post completion comment\n\n"
        f"CRITICAL RULES:\n"
        f"- NEVER modify the card description\n"
        f"- ONLY post comments using curl:\n"
        f"  source ~/.config/mcp-trello.env\n"
        f"  curl -s -X POST 'https://api.trello.com/1/cards/{card_id}/actions/comments' "
        f"--data-urlencode 'text=YOUR_COMMENT' "
        f"-d \"key=$TRELLO_API_KEY&token=$TRELLO_API_TOKEN\"\n\n"
        f"URL VERIFICATION (for AliExpress/shopping cards):\n"
        f"- Test EVERY link with WebFetch before posting\n"
        f"- Format: Verified {today}\n\n"
        f"Post max ONE comment per day - skip if already commented today.\n"
        f"Trello Card: {url}"
    )


def build_create_prompt(card, list_name: str, worktree_name: str) -> str:
    card_id = card["card_id"]
    title = card["title"]
    category = card["category"]
    priority = card["priority"]
    url = card["url"]
    description = card.get("description", "") or ""
    today = datetime.now().strftime("%Y-%m-%d")

    return (
        f"Handle ticket: {title}\n\n"
        f"Card ID: {card_id}\n"
        f"List: {list_name}\n"
        f"Category: {category}\n"
        f"Priority: {priority}\n"
        f"Trello: {url}\n\n"
        f"Description:\n{description[:600]}\n\n"
        f"Your Job:\n"
        f"1. Understand the task from description\n"
        f"2. Execute the work needed\n"
        f"3. Post findings/progress to Trello AS COMMENTS\n"
        f"4. When complete, post summary comment\n\n"
        f"For Research/Shopping Tasks:\n"
        f"- Research the topic thoroughly\n"
        f"- Gather information and links\n"
        f"- Post findings to Trello as comment\n\n"
        f"CRITICAL RULES:\n"
        f"- NEVER modify the card description\n"
        f"- ONLY post comments using curl:\n"
        f"  source ~/.config/mcp-trello.env\n"
        f"  curl -s -X POST 'https://api.trello.com/1/cards/{card_id}/actions/comments' "
        f"--data-urlencode 'text=YOUR_COMMENT' "
        f"-d \"key=$TRELLO_API_KEY&token=$TRELLO_API_TOKEN\"\n\n"
        f"URL VERIFICATION CRITICAL:\n"
        f"- Test EVERY link with WebFetch before posting\n"
        f"- If 404, search for alternative with WebSearch\n"
        f"- Format: Verified {today}\n\n"
        f"Trello Card: {url}\n\n"
        f"Start working on this task!"
    )


def main():
    # Load latest actions file
    actions_files = sorted(Path("memory").glob("ticket-sessions-*.json"))
    if not actions_files:
        print("No actions file found!")
        sys.exit(1)

    actions_file = actions_files[-1]
    data = json.load(open(actions_file))
    print(f"Processing {actions_file.name}: {data['stats']['total_cards']} cards")
    print(f"Blocked cards: {len(BLOCKED_CARD_IDS)}")
    print()

    sessions_prompted = []
    sessions_skipped = []
    sessions_failed = []

    for list_info in data["lists"]:
        list_name = list_info["list_name"]
        worktree_name = list_info["worktree_name"]

        for card in list_info["cards"]:
            card_id_short = card["card_id"][:8]
            title = card["title"]
            action = card["action"]

            # Check if blocked
            if card_id_short in BLOCKED_CARD_IDS:
                sessions_skipped.append({"title": title, "reason": "blocked per memory"})
                print(f"  SKIP [{card_id_short}] {title[:40]} (blocked)")
                continue

            if action == "update":
                session_id = card.get("session_id", "")
                if not session_id or len(session_id) < 8:
                    sessions_failed.append({"title": title, "reason": "invalid session ID"})
                    print(f"  FAIL [{card_id_short}] {title[:40]} (bad session ID: {session_id})")
                    continue

                prompt = build_update_prompt(card, list_name)
                print(f"  UPDATE [{card_id_short}] {title[:45]}...", end=" ", flush=True)

                result = call_mcp("agor_sessions_prompt", {
                    "sessionId": session_id,
                    "prompt": prompt,
                    "mode": "continue",
                })

                if "error" in result or result.get("success") is False:
                    err = result.get("error", result.get("message", str(result)))
                    sessions_failed.append({"title": title, "reason": str(err)[:80]})
                    print(f"FAIL: {str(err)[:60]}")
                else:
                    sessions_prompted.append({"title": title, "list": list_name, "session_id": session_id})
                    print(f"OK [{result.get('taskId', 'N/A')[:8]}]")

            elif action == "create":
                # Already created by orchestrator, just send prompt
                # Look up session_id in DuckDB
                try:
                    import duckdb
                    conn = duckdb.connect("memory/agor-state/sessions.duckdb")
                    rows = conn.execute(
                        "SELECT session_id FROM ticket_sessions WHERE card_id = ?",
                        [card["card_id"]]
                    ).fetchall()
                    conn.close()

                    if rows:
                        session_id = rows[0][0]
                        prompt = build_create_prompt(card, list_name, worktree_name)
                        print(f"  PROMPT [{card_id_short}] {title[:45]}...", end=" ", flush=True)

                        result = call_mcp("agor_sessions_prompt", {
                            "sessionId": session_id,
                            "prompt": prompt,
                            "mode": "continue",
                        })

                        if "error" in result:
                            sessions_failed.append({"title": title, "reason": str(result["error"])[:80]})
                            print(f"FAIL: {str(result['error'])[:60]}")
                        else:
                            sessions_prompted.append({"title": title, "list": list_name, "session_id": session_id})
                            print(f"OK")
                    else:
                        print(f"  SKIP [{card_id_short}] {title[:40]} (no session in DB)")
                        sessions_skipped.append({"title": title, "reason": "no session in DB"})
                except Exception as e:
                    print(f"  FAIL [{card_id_short}] {title[:40]} (DB error: {e})")
                    sessions_failed.append({"title": title, "reason": f"DB error: {e}"})

    print()
    print(f"Summary: {len(sessions_prompted)} prompted, {len(sessions_skipped)} skipped, {len(sessions_failed)} failed")

    if sessions_failed:
        print("\nFailed:")
        for s in sessions_failed:
            print(f"  - {s['title'][:50]}: {s['reason']}")

    return sessions_prompted, sessions_skipped, sessions_failed


if __name__ == "__main__":
    main()
