# Jounce Dashboard Artifact — Design Spec

**Date:** 2026-06-16  
**Branch:** private-julie (agor-openclaw)  
**Board:** jounce-workflow-ai (`019eb849-ec5b-715e-b8cc-e37c4c387740`)

---

## Goal

A live React artifact on the jounce-workflow-ai board that shows cost and progress across Jira tickets and sessions. Built in panels — one panel now, more added over time.

---

## Stage 1 Scope (this spec)

**Panel 1: Cost by Group**

A horizontal bar chart showing total cost aggregated by a user-selected grouping. Data is fetched live at view time via the Agor analytics API. No Jira credentials required.

**Stage 2 (out of scope here):** Add Jira ticket status, sprint grouping, epic grouping.

---

## Data Source

`GET /api/analytics/leaderboard` via Agor daemon, authenticated with a 15-minute JWT injected as `REACT_APP_AGOR_TOKEN`. API URL injected as `REACT_APP_AGOR_API_URL`.

Available groupings from Agor analytics API:

| Grouping | API params | Note |
|----------|------------|------|
| By Ticket | `groupBy=branch` | Extract `JN-XXXX` from branch name; sum branches sharing the same ticket ID |
| By Week | `groupBy=branch&bucket=week` | Time-series cost by calendar week |
| By Repo | `groupBy=repo` | Cost across jounce vs model-packaging-pipeline |

Future groupings (stage 2, need Jira):
- By Sprint: map ticket → sprint via Jira REST API
- By Epic: map ticket → epic via Jira REST API

---

## UI Design

### Group-by selector
Pill/tab control at the top. Options: **By Ticket** (default) | **By Week** | **By Repo**. Stage-2 options (By Sprint, By Epic) will be added as pills later — no placeholder UI now.

### Bar chart
- Horizontal bars, one per group item
- Sorted by total cost descending
- Label: ticket ID / ISO week / repo name
- Bar fill with cost in USD
- Tooltip on hover: sessions, tokens (input + output), duration
- "Last fetched" timestamp bottom-right; click to re-fetch

### Error / loading states
- Loading spinner while fetching
- "Configure AGOR_TOKEN in Agor Settings" message if token is missing
- Fetch error shown inline with a retry button

---

## Architecture

### File location

```
private-julie branch
└── .agor/
    └── artifacts/
        └── jounce-dashboard/
            ├── index.js          — Sandpack entry, mounts <App />
            ├── App.js            — root: owns fetch state + grouping state
            ├── api.js            — fetch wrapper using REACT_APP_AGOR_TOKEN
            ├── groupings.js      — grouping config + data transform logic
            ├── BarChart.js       — pure display component
            └── GroupSelector.js  — pill control
```

### Agor artifact config
- **Template:** `react` (CRA-backed, Sandpack v2)
- **agorGrants:** `agor_token: true`, `agor_api_url: true`, `agor_board_id: true`
- **requiredEnvVars:** none (grants cover everything)
- **public:** true

### Data flow

```
App mounts
  → api.js fetches /api/analytics/leaderboard with selected groupBy params
  → groupings.js transforms raw rows (extracts JN-XXXX, sums dupes, etc.)
  → BarChart renders sorted bars
  → GroupSelector change → new fetch
```

### Extending for new groupings
Add one entry to the `GROUPINGS` array in `groupings.js`:
- `id`, `label`, `apiParams`, `transformFn`

The rest of the app picks it up automatically.

---

## Publish / update workflow

Julie publishes via:
```
agor_artifacts_publish(
  branchId: "019ecc87-be8b-77cd-ac4e-e2c203022f55",
  subpath: ".agor/artifacts/jounce-dashboard",
  boardId: "019eb849-ec5b-715e-b8cc-e37c4c387740",
  name: "Jounce Dashboard",
  agorGrants: { agor_token: true, agor_api_url: true, agor_board_id: true }
)
```

Re-publish (same command with `artifactId`) to push code changes.

---

## Out of scope

- Jira status column (stage 2)
- Sprint / Epic grouping (stage 2, requires Jira credentials)
- Kanban pipeline view (stage 2)
- Drill-down to individual branches within a ticket (stage 2)
- Authentication beyond Agor TOFU consent
