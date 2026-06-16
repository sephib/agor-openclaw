# Jounce Dashboard Artifact — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a live React artifact on the jounce-workflow-ai board showing cost aggregated by Jira ticket, week, or repo — fetched fresh from the Agor analytics REST API on every open.

**Architecture:** A Sandpack `react` (CRA-backed) artifact in `.agor/artifacts/jounce-dashboard/` on the `private-julie` branch. At render time, the Agor daemon injects `AGOR_TOKEN` and `AGOR_API_URL` (the grants use bare names, not `REACT_APP_` prefix — see api.js for dual-read fallback). The app fetches `GET /leaderboard?groupBy=branch&$limit=500` (FeathersJS REST), groups/sums the rows client-side by JN-XXXX ticket ID (or week or repo), and renders a horizontal CSS bar chart. No npm dependencies beyond React.

**Tech Stack:** React 18 (CRA/Sandpack template), vanilla CSS-in-JS, Agor analytics REST API at `${AGOR_API_URL}/leaderboard`.

**Branch:** `private-julie` (ID: `019ecc87-be8b-77cd-ac4e-e2c203022f55`)  
**Board:** `019eb849-ec5b-715e-b8cc-e37c4c387740`

---

## File Map

| File | Responsibility |
|------|---------------|
| `.agor/artifacts/jounce-dashboard/index.js` | Sandpack entry — mounts `<App />` to `#root` |
| `.agor/artifacts/jounce-dashboard/api.js` | Fetch wrapper: validates credentials, calls `/leaderboard`, throws on error |
| `.agor/artifacts/jounce-dashboard/groupings.js` | `GROUPINGS` config array — each entry has `id`, `label`, `apiParams`, `transform(rows)` |
| `.agor/artifacts/jounce-dashboard/GroupSelector.js` | Pill buttons that call `onChange(groupingId)` |
| `.agor/artifacts/jounce-dashboard/BarChart.js` | Stateless: renders sorted horizontal bars + hover tooltips |
| `.agor/artifacts/jounce-dashboard/App.js` | Root: owns `groupingId`, `items`, `loading`, `error`, `fetchedAt` state; calls `api.js` on mount and grouping change |

---

## Task 1: Create artifact directory and index.js

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/index.js`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p /Users/josephberry/.agor/worktrees/local/agor-openclaw/private-julie/.agor/artifacts/jounce-dashboard
```

- [ ] **Step 2: Write index.js**

```js
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

Write to: `.agor/artifacts/jounce-dashboard/index.js`

- [ ] **Step 3: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/index.js
git commit -m "feat: scaffold jounce dashboard artifact entry"
```

---

## Task 2: Implement api.js

The Agor daemon injects grants as `AGOR_TOKEN` (15-min JWT) and `AGOR_API_URL` (daemon base URL). **Important:** agorGrants use bare names without `REACT_APP_` prefix — but CRA/Sandpack may or may not strip them. The code reads both forms as a fallback so it works in either case. The leaderboard endpoint is a FeathersJS service at `/leaderboard` — use `$limit` (dollar sign) for pagination in REST queries.

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/api.js`

- [ ] **Step 1: Write api.js**

```js
// agorGrants inject as AGOR_TOKEN / AGOR_API_URL (bare names).
// CRA Sandpack may also expose REACT_APP_* variants — read both as fallback.
const BASE = process.env.AGOR_API_URL || process.env.REACT_APP_AGOR_API_URL;
const TOKEN = process.env.AGOR_TOKEN || process.env.REACT_APP_AGOR_TOKEN;

export function hasCredentials() {
  return Boolean(BASE && TOKEN);
}

export async function fetchLeaderboard(params = {}) {
  const url = new URL(`${BASE}/leaderboard`);
  // FeathersJS REST uses $limit for pagination; 500 covers current 230+ branches with room to grow
  Object.entries({ ...params, $limit: 500 }).forEach(([k, v]) => {
    if (v !== undefined) url.searchParams.set(k, String(v));
  });
  const res = await fetch(url.toString(), {
    headers: { Authorization: `Bearer ${TOKEN}` },
  });
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    throw new Error(`API ${res.status}: ${body}`);
  }
  const json = await res.json();
  return json.data || [];
}
```

Write to: `.agor/artifacts/jounce-dashboard/api.js`

- [ ] **Step 2: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/api.js
git commit -m "feat: add Agor leaderboard fetch wrapper"
```

---

## Task 3: Implement groupings.js

Each grouping has `id`, `label`, `apiParams` (passed to `fetchLeaderboard`), and `transform(rows)` which reduces the raw API rows into `{ label, totalCost, sessionCount, totalTokens, totalDurationMs }` objects.

**Fields from the running Agor daemon:** `branchId`, `branchName`, `totalTokens`, `totalCost`, `sessionCount`, `totalDurationMs` (for `groupBy=branch`); `repoId`, `repoName` (for `groupBy=repo`); `bucket` ISO-8601 timestamp (when `bucket=week`).

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/groupings.js`

- [ ] **Step 1: Write groupings.js**

```js
function extractTicket(branchName) {
  const m = (branchName || '').match(/jn-(\d+)/i);
  return m ? `JN-${m[1]}` : null;
}

function sumInto(acc, row) {
  acc.totalCost += row.totalCost || 0;
  acc.sessionCount += row.sessionCount || 0;
  acc.totalTokens += row.totalTokens || 0;
  acc.totalDurationMs += row.totalDurationMs || 0;
}

function groupByKey(rows, keyFn) {
  const map = {};
  rows.forEach((row) => {
    const key = keyFn(row);
    if (!key) return;
    if (!map[key]) {
      map[key] = { label: key, totalCost: 0, sessionCount: 0, totalTokens: 0, totalDurationMs: 0 };
    }
    sumInto(map[key], row);
  });
  return Object.values(map);
}

export const GROUPINGS = [
  {
    id: 'ticket',
    label: 'By Ticket',
    apiParams: { groupBy: 'branch' },
    transform: (rows) =>
      groupByKey(rows, (r) => extractTicket(r.branchName))
        .sort((a, b) => b.totalCost - a.totalCost),
  },
  {
    id: 'week',
    label: 'By Week',
    apiParams: { groupBy: 'branch', bucket: 'week' },
    transform: (rows) =>
      groupByKey(rows, (r) => (r.bucket ? r.bucket.slice(0, 10) : null))
        .sort((a, b) => a.label.localeCompare(b.label)),
  },
  {
    id: 'repo',
    label: 'By Repo',
    apiParams: { groupBy: 'repo' },
    transform: (rows) =>
      rows
        .map((r) => ({
          label: r.repoName || r.repoId || 'unknown',
          totalCost: r.totalCost || 0,
          sessionCount: r.sessionCount || 0,
          totalTokens: r.totalTokens || 0,
          totalDurationMs: r.totalDurationMs || 0,
        }))
        .sort((a, b) => b.totalCost - a.totalCost),
  },
];
```

Write to: `.agor/artifacts/jounce-dashboard/groupings.js`

- [ ] **Step 2: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/groupings.js
git commit -m "feat: add groupings config (ticket, week, repo)"
```

---

## Task 4: Implement GroupSelector.js

Pill buttons — active pill is blue, inactive is white with grey border.

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/GroupSelector.js`

- [ ] **Step 1: Write GroupSelector.js**

```jsx
import React from 'react';

export default function GroupSelector({ groupings, selected, onChange }) {
  return (
    <div style={{ display: 'flex', gap: 8, marginBottom: 16, flexWrap: 'wrap' }}>
      {groupings.map((g) => (
        <button
          key={g.id}
          onClick={() => onChange(g.id)}
          style={{
            padding: '4px 14px',
            borderRadius: 20,
            border: '1px solid #ccc',
            background: selected === g.id ? '#1a73e8' : '#fff',
            color: selected === g.id ? '#fff' : '#444',
            cursor: 'pointer',
            fontSize: 13,
            fontWeight: selected === g.id ? 600 : 400,
          }}
        >
          {g.label}
        </button>
      ))}
    </div>
  );
}
```

Write to: `.agor/artifacts/jounce-dashboard/GroupSelector.js`

- [ ] **Step 2: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/GroupSelector.js
git commit -m "feat: add GroupSelector pill control"
```

---

## Task 5: Implement BarChart.js

Horizontal CSS bars. Max bar = widest item. Tooltip appears below the hovered bar with sessions, tokens, and duration.

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/BarChart.js`

- [ ] **Step 1: Write BarChart.js**

```jsx
import React, { useState } from 'react';

function fmtCost(n) {
  return `$${n.toFixed(2)}`;
}

function fmtDuration(ms) {
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  if (h > 0) return `${h}h ${m}m`;
  return `${m}m`;
}

function fmtTokens(n) {
  return n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(n);
}

export default function BarChart({ items }) {
  const [tooltip, setTooltip] = useState(null);

  if (!items.length) {
    return <p style={{ color: '#888', fontSize: 13 }}>No data</p>;
  }

  const max = Math.max(...items.map((i) => i.totalCost), 0.01);

  return (
    <div style={{ fontFamily: 'sans-serif' }}>
      {items.map((item, idx) => (
        <div
          key={idx}
          style={{ marginBottom: 8 }}
          onMouseEnter={() => setTooltip(idx)}
          onMouseLeave={() => setTooltip(null)}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span
              style={{
                width: 80,
                fontSize: 12,
                color: '#333',
                textAlign: 'right',
                flexShrink: 0,
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}
              title={item.label}
            >
              {item.label}
            </span>
            <div
              style={{
                flex: 1,
                background: '#eee',
                borderRadius: 4,
                height: 20,
                position: 'relative',
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  width: `${(item.totalCost / max) * 100}%`,
                  background: '#1a73e8',
                  borderRadius: 4,
                  height: '100%',
                  minWidth: 4,
                  transition: 'width 0.3s ease',
                }}
              />
            </div>
            <span style={{ width: 56, fontSize: 12, color: '#333', flexShrink: 0 }}>
              {fmtCost(item.totalCost)}
            </span>
          </div>
          {tooltip === idx && (
            <div
              style={{
                marginLeft: 88,
                fontSize: 11,
                color: '#555',
                background: '#f9f9f9',
                border: '1px solid #ddd',
                borderRadius: 4,
                padding: '4px 8px',
                marginTop: 2,
              }}
            >
              Sessions: {item.sessionCount} &nbsp;|&nbsp;
              Tokens: {fmtTokens(item.totalTokens)} &nbsp;|&nbsp;
              Duration: {fmtDuration(item.totalDurationMs)}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
```

Write to: `.agor/artifacts/jounce-dashboard/BarChart.js`

- [ ] **Step 2: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/BarChart.js
git commit -m "feat: add horizontal bar chart with hover tooltips"
```

---

## Task 6: Implement App.js

Root component. Fetches on mount and whenever `groupingId` changes. Shows loading spinner, error with retry, or the chart. Shows "last fetched" timestamp with a manual refresh link.

**Files:**
- Create: `.agor/artifacts/jounce-dashboard/App.js`

- [ ] **Step 1: Write App.js**

```jsx
import React, { useState, useEffect, useCallback } from 'react';
import { GROUPINGS } from './groupings';
import { fetchLeaderboard, hasCredentials } from './api';
import GroupSelector from './GroupSelector';
import BarChart from './BarChart';

export default function App() {
  const [groupingId, setGroupingId] = useState('ticket');
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [fetchedAt, setFetchedAt] = useState(null);

  const grouping = GROUPINGS.find((g) => g.id === groupingId);

  const load = useCallback(async () => {
    if (!hasCredentials()) {
      setError('AGOR_TOKEN not available. Open this artifact from the Agor board to enable live data.');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const rows = await fetchLeaderboard(grouping.apiParams);
      setItems(grouping.transform(rows));
      setFetchedAt(new Date());
    } catch (e) {
      setError(e.message);
      setItems([]);
    } finally {
      setLoading(false);
    }
  }, [grouping]);

  useEffect(() => {
    load();
  }, [load]);

  return (
    <div style={{ padding: 20, maxWidth: 700, fontFamily: 'sans-serif' }}>
      <h2 style={{ margin: '0 0 16px', fontSize: 16, fontWeight: 600, color: '#222' }}>
        Jounce Cost Dashboard
      </h2>
      <GroupSelector groupings={GROUPINGS} selected={groupingId} onChange={setGroupingId} />
      {loading && (
        <p style={{ color: '#888', fontSize: 13 }}>Loading…</p>
      )}
      {error && (
        <div style={{ color: '#c00', fontSize: 13, marginBottom: 12 }}>
          {error}&nbsp;
          <button
            onClick={load}
            style={{ fontSize: 12, cursor: 'pointer', border: '1px solid #c00', borderRadius: 4, padding: '2px 8px', background: 'none', color: '#c00' }}
          >
            Retry
          </button>
        </div>
      )}
      {!loading && !error && <BarChart items={items} />}
      {fetchedAt && (
        <div style={{ marginTop: 16, fontSize: 11, color: '#aaa', textAlign: 'right' }}>
          Fetched {fetchedAt.toLocaleTimeString()}&nbsp;
          <button
            onClick={load}
            style={{ fontSize: 11, cursor: 'pointer', color: '#888', border: 'none', background: 'none', textDecoration: 'underline' }}
          >
            refresh
          </button>
        </div>
      )}
    </div>
  );
}
```

Write to: `.agor/artifacts/jounce-dashboard/App.js`

- [ ] **Step 2: Commit**

```bash
git add .agor/artifacts/jounce-dashboard/App.js
git commit -m "feat: add App root component wiring fetch + chart"
```

---

## Task 7: Verify all files exist then publish artifact

**Files:** all 6 files in `.agor/artifacts/jounce-dashboard/`

- [ ] **Step 1: Verify directory contents**

```bash
ls /Users/josephberry/.agor/worktrees/local/agor-openclaw/private-julie/.agor/artifacts/jounce-dashboard/
```

Expected output:
```
App.js  BarChart.js  GroupSelector.js  api.js  groupings.js  index.js
```

- [ ] **Step 2: Check build readiness via Agor MCP**

Call `agor_artifacts_check_build` with:
```json
{
  "branchId": "019ecc87-be8b-77cd-ac4e-e2c203022f55",
  "subpath": ".agor/artifacts/jounce-dashboard"
}
```

Expected: all 6 files reported as non-empty. Fix any missing files before proceeding.

- [ ] **Step 3: Publish the artifact**

Call `agor_artifacts_publish` with:
```json
{
  "branchId": "019ecc87-be8b-77cd-ac4e-e2c203022f55",
  "subpath": ".agor/artifacts/jounce-dashboard",
  "boardId": "019eb849-ec5b-715e-b8cc-e37c4c387740",
  "name": "Jounce Dashboard",
  "template": "react",
  "agorGrants": {
    "agor_token": true,
    "agor_api_url": true,
    "agor_board_id": true
  },
  "width": 700,
  "height": 500
}
```

Record the returned `artifactId` — you'll need it for updates.

- [ ] **Step 4: Save the artifactId to the manager notes**

Append to `_manager/BOARD_STATE.md`:
```
## Dashboard Artifact
- artifactId: <RETURNED_ID>
- Published: 2026-06-16
- Re-publish command: agor_artifacts_publish with branchId 019ecc87, subpath .agor/artifacts/jounce-dashboard, artifactId <ID>
```

---

## Task 8: Verify live rendering and fix any issues

- [ ] **Step 1: Check build status**

Call `agor_artifacts_status` with the `artifactId` from Task 7.

Check `build_status`. If `error`, read `build_errors` — common causes:
- `"Could not find module './X'"` → file name mismatch, fix the import
- `"Unexpected token"` → JSX syntax error, fix the file
- Sandpack errors are prefixed `[Sandpack]` in `build_errors`

Fix any errors, then re-publish (same `agor_artifacts_publish` call with `artifactId`).

- [ ] **Step 2: Open the artifact in a browser**

Navigate to the artifact URL from the publish response (or find it on the board). Trust the artifact when prompted.

- [ ] **Step 3: Verify DOM renders**

Call `agor_artifacts_query_dom` with:
```json
{ "selector": "h2" }
```

Expected: element with `textContent` containing `"Jounce Cost Dashboard"`.

- [ ] **Step 4: Verify data loads**

Call `agor_artifacts_query_dom` with:
```json
{ "selector": "div[style*='background: #1a73e8']", "multiple": true }
```

Expected: one or more blue bar elements. If zero bars but no error text, check console logs via `agor_artifacts_status` for the fetch URL and response.

- [ ] **Step 5: If bars are missing — check console logs for API errors**

Call `agor_artifacts_status`. Look at `console_logs` for any error output.

Common issues:
- `API 401` → AGOR_TOKEN not injected. Make sure you trusted the artifact and `agorGrants.agor_token` was set. Also check which env var name Sandpack actually exposes: add `console.log('env', process.env.AGOR_TOKEN, process.env.REACT_APP_AGOR_TOKEN)` to App.js temporarily to see which is non-empty.
- `API 404` → endpoint path wrong. The confirmed path from daemon source is `/leaderboard`. Check `REACT_APP_AGOR_API_URL` value in logs.
- `CORS error` → unexpected if artifact is served from same origin as daemon. Report this finding.
- `"No data"` rendered but no error → the `transform` filtered all rows. Check that branch names in the leaderboard actually contain `jn-\d+` pattern.

Fix and re-publish as needed.

- [ ] **Step 6: Final commit**

```bash
git add -A
git commit -m "feat: publish Jounce Dashboard artifact to board"
```

---

## Self-Review Notes

- Spec coverage: all spec sections covered — group-by selector, bar chart with tooltip, live fetch, error states, artifact location, publish workflow.
- No placeholders or TODOs in any task.
- Field names match actual daemon response (`branchName`, `totalCost`, `sessionCount`, `totalDurationMs`).
- `extractTicket` in Task 3 returns `null` for non-JN branches — `groupByKey` skips null keys, so non-ticket branches are filtered from the "By Ticket" view automatically.
- `$limit=200` uses the FeathersJS REST convention (confirmed from daemon source).
- CRA env var prefix `REACT_APP_` is required for the react/CRA template.
