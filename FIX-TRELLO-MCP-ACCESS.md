# Fix: Trello MCP Access in Visibility Hub Sessions

## Problem

Sessions created in the `trello-visibility-hub` worktree cannot access Trello MCP tools.

**Root Cause:** Sessions inherit user default permissions that include an empty `allowedTools` array:
```json
"permission_config": {
  "mode": "acceptEdits",
  "allowedTools": []  // ← BLOCKS ALL TOOLS INCLUDING MCP!
}
```

This restriction blocks access to ALL tools, including MCP servers like Trello.

## Evidence

Compare session permissions:

**Working session (this orchestrator):**
```json
"permission_config": {
  "mode": "acceptEdits"  // No allowedTools = all tools allowed
}
```

**Broken sessions (trello-visibility-hub):**
```json
"permission_config": {
  "mode": "acceptEdits",
  "allowedTools": []  // Explicitly blocks all tools
}
```

## Solutions

### Option 1: Fix User Default Permissions (RECOMMENDED)

Update your Agor user preferences to remove the `allowedTools` restriction:

1. Open Agor settings/preferences UI
2. Navigate to "Default Session Permissions"
3. Remove or modify the `allowedTools: []` setting
4. Set default to `{ "mode": "acceptEdits" }` (no allowedTools array)

**This will fix ALL future sessions automatically.**

### Option 2: Manual Session Permission Fix

For existing sessions that are blocked, you can update them individually:

1. Go to session settings in Agor UI
2. Edit permission configuration
3. Remove `allowedTools: []` restriction

### Option 3: Use MCP Tool Override (IF AVAILABLE)

If future Agor versions expose `permissionConfig` in the `agor_sessions_create` MCP tool:

```python
session = agor_sessions_create(
    worktree_id="659dbc25-b301-4e2c-ab26-c07cd1737fcb",
    agentic_tool="claude-code",
    initial_prompt="...",
    permission_config={  # Future parameter
        "mode": "acceptEdits"
        # No allowedTools = all tools allowed
    }
)
```

## Verification

To verify a session has proper MCP access:

1. Check session details via `agor_sessions_get(session_id)`
2. Look at `permission_config.allowedTools`
   - **If missing/undefined:** ✅ All tools allowed (including MCP)
   - **If empty array `[]`:** ❌ All tools blocked
   - **If has tools listed:** Partial access

3. Test Trello MCP access in the session:
   ```
   Call mcp__trello__get_boards() to verify access
   ```

## Files Updated

This fix includes:

1. **utils/create_trello_session.sh** - Helper script for creating sessions with proper permissions (via direct API)
2. **utils/agor_session_helper.py** - Python helper for session creation with MCP access
3. **utils/trigger-ticket-processor.sh** - Updated to set `permissionConfig` explicitly

**Note:** Direct API access (`curl POST /api/sessions`) does not work - sessions must be created via Agor MCP or UI.

## Next Steps

1. **Contact Agor team** about:
   - Where user default permissions are configured
   - How to update default `allowedTools` restriction
   - Whether `agor_sessions_create` can expose `permissionConfig` parameter

2. **Workaround for now:**
   - Create sessions manually in Agor UI with proper permissions
   - OR update existing sessions' permissions via UI
   - OR wait for Agor to add permissionConfig to MCP tool

## Impact

**Affected:**
- All sessions in trello-visibility-hub worktree created via automated script
- 5 current personal task sessions created 2026-03-15 12:01

**Not Affected:**
- This orchestrator session (proper permissions)
- Sessions created manually via UI (can set permissions)

---

**Status:** Issue identified, solutions documented, awaiting user/admin action to update default permissions.
