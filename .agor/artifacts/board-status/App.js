import React, { useState, useMemo } from "react";
import { WORKTREES, MERGED, LAST_UPDATED } from "./data";
import { ZONE_MODEL_CONFIG, SCHEDULES, REVIEWERS } from "./config";
import { HEARTBEAT_RUNS } from "./heartbeat-log";
import { SPRINTS, CURRENT_SPRINT_ID } from "./sprints";

const TYPE_STYLES = {
  running: { bg: "#e8f4fd", color: "#0969da", label: "Running" },
  owner: { bg: "#fff8e1", color: "#9a6700", label: "Needs You" },
  external: { bg: "#f0e6ff", color: "#6e40c9", label: "Waiting on Reviewer" },
  blocked: { bg: "#ffeef0", color: "#cf222e", label: "Blocked" },
};

const ZONE_COLORS = {
  Ingest: "#e3f2fd", Plan: "#e8eaf6", Code: "#e0f2f1", Revise: "#fff3e0",
  Verify: "#f3e5f5", "Validate ": "#fce4ec", Validate: "#fce4ec",
  Publish: "#e8f5e9", Respond: "#fff8e1", "Code Review": "#f3e5f5",
  BLOCKED: "#ffebee", "(floating)": "#f5f5f5",
};

const COLUMNS = [
  { key: "ticket", label: "Ticket", sortValue: (w) => w.ticket || "" },
  { key: "zone", label: "Zone", sortValue: (w) => w.zone },
  { key: "pr", label: "PR", sortValue: (w) => w.pr || "" },
  { key: "status", label: "Status", sortValue: (w) => w.status },
  { key: "session", label: "Session", sortValue: (w) => w.sessionLabel || "" },
  { key: "blockedOn", label: "Blocked On", sortValue: (w) => w.blockedType + (w.blockedOn || "") },
  { key: "lastActive", label: "Last Active", sortValue: (w) => w.lastActive || "" },
  { key: "actions", label: "Actions", sortValue: () => "" },
];

function Badge({ type }) {
  const s = TYPE_STYLES[type] || TYPE_STYLES.running;
  return (
    <span style={{ display: "inline-block", padding: "2px 8px", borderRadius: 12, fontSize: 11, fontWeight: 600, background: s.bg, color: s.color }}>
      {s.label}
    </span>
  );
}

function ZonePill({ zone }) {
  return (
    <span style={{ display: "inline-block", padding: "2px 8px", borderRadius: 4, fontSize: 11, fontWeight: 500, background: ZONE_COLORS[zone] || "#f5f5f5", color: "#333" }}>
      {zone}
    </span>
  );
}

function SortHeader({ column, sortKey, sortDir, onSort }) {
  const active = sortKey === column.key;
  const arrow = active ? (sortDir === "asc" ? " ▲" : " ▼") : "";
  return (
    <th
      onClick={() => onSort(column.key)}
      style={{ padding: "8px 6px", textAlign: "left", fontSize: 11, color: active ? "#0969da" : "#666", fontWeight: 600, cursor: "pointer", userSelect: "none" }}
    >
      {column.label}{arrow}
    </th>
  );
}

function Row({ w }) {
  const [copied, setCopied] = useState(false);

  const copyPath = () => {
    navigator.clipboard.writeText(w.worktreePath).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <tr style={{ borderBottom: "1px solid #eee" }}>
      <td style={{ padding: "8px 6px", fontSize: 13 }}>
        {w.ticketUrl ? (
          <a href={w.ticketUrl} target="_blank" rel="noopener noreferrer" style={{ color: "#0969da", textDecoration: "none", fontWeight: 600 }}>{w.ticket}</a>
        ) : (
          <span style={{ fontWeight: 600, color: "#333" }}>{w.branch || "—"}</span>
        )}
        <div style={{ fontSize: 11, color: "#666", marginTop: 2 }}>{w.title}</div>
      </td>
      <td style={{ padding: "8px 6px" }}><ZonePill zone={w.zone} /></td>
      <td style={{ padding: "8px 6px", fontSize: 12 }}>
        {w.pr ? (
          <a href={w.prUrl} target="_blank" rel="noopener noreferrer" style={{ color: "#0969da", textDecoration: "none" }}>{w.pr}</a>
        ) : (
          <span style={{ color: "#aaa" }}>—</span>
        )}
      </td>
      <td style={{ padding: "8px 6px", fontSize: 12, color: "#444" }}>{w.status}</td>
      <td style={{ padding: "8px 6px" }}>
        {w.sessionUrl ? (
          <a href={w.sessionUrl} target="_blank" rel="noopener noreferrer" style={{ display: "inline-block", padding: "2px 8px", borderRadius: 4, fontSize: 11, fontWeight: 500, background: "#f0f0f0", color: "#0969da", textDecoration: "none" }}>
            {w.sessionLabel || "session"}
          </a>
        ) : (
          <span style={{ color: "#ccc", fontSize: 11 }}>—</span>
        )}
      </td>
      <td style={{ padding: "8px 6px" }}>
        <Badge type={w.blockedType} />
        {w.blockedOn && <div style={{ fontSize: 11, color: "#666", marginTop: 2 }}>{w.blockedOn}</div>}
      </td>
      <td style={{ padding: "8px 6px", fontSize: 11, color: "#888" }}>
        {w.lastActive || "—"}
      </td>
      <td style={{ padding: "8px 6px" }}>
        {w.worktreePath && (
          <button
            onClick={copyPath}
            style={{ display: "inline-block", padding: "2px 8px", borderRadius: 4, fontSize: 11, fontWeight: 500, background: copied ? "#16a34a" : "#007acc", color: "#fff", border: "none", cursor: "pointer" }}
            title={w.worktreePath}
          >
            {copied ? "✓ Copied" : "Copy Path"}
          </button>
        )}
      </td>
    </tr>
  );
}

function HeartbeatTab() {
  const runs = HEARTBEAT_RUNS;
  const advanceRuns = runs.filter((r) => r.type === "advance");
  const syncRuns = runs.filter((r) => r.type === "sync");
  const totalActions = runs.reduce((sum, r) => sum + (r.actions || 0), 0);
  const totalFindings = runs.reduce((sum, r) => sum + (r.findings || 0), 0);
  const lastAdvance = advanceRuns[0];
  const lastSync = syncRuns[0];
  const errors = runs.filter((r) => r.status === "error");

  const statusDot = (s) => (
    <span style={{
      display: "inline-block", width: 8, height: 8, borderRadius: "50%",
      background: s === "ok" ? "#22c55e" : s === "error" ? "#ef4444" : "#94a3b8",
      marginRight: 6,
    }} />
  );

  return (
    <div>
      <div style={{ display: "flex", gap: 12, marginBottom: 16, flexWrap: "wrap" }}>
        <div style={{ padding: "8px 14px", borderRadius: 8, background: "#e8f4fd", minWidth: 100, textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: 700, color: "#0969da" }}>{runs.length}</div>
          <div style={{ fontSize: 11, color: "#0969da", fontWeight: 500 }}>Total Runs</div>
        </div>
        <div style={{ padding: "8px 14px", borderRadius: 8, background: "#e0f2f1", minWidth: 100, textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: 700, color: "#0d9488" }}>{advanceRuns.length}</div>
          <div style={{ fontSize: 11, color: "#0d9488", fontWeight: 500 }}>Advance</div>
        </div>
        <div style={{ padding: "8px 14px", borderRadius: 8, background: "#f0e6ff", minWidth: 100, textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: 700, color: "#6e40c9" }}>{syncRuns.length}</div>
          <div style={{ fontSize: 11, color: "#6e40c9", fontWeight: 500 }}>Sync</div>
        </div>
        <div style={{ padding: "8px 14px", borderRadius: 8, background: "#e8f5e9", minWidth: 100, textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: 700, color: "#2e7d32" }}>{totalActions}</div>
          <div style={{ fontSize: 11, color: "#2e7d32", fontWeight: 500 }}>Actions Taken</div>
        </div>
        <div style={{ padding: "8px 14px", borderRadius: 8, background: errors.length > 0 ? "#ffeef0" : "#f3f4f6", minWidth: 100, textAlign: "center" }}>
          <div style={{ fontSize: 22, fontWeight: 700, color: errors.length > 0 ? "#cf222e" : "#6b7280" }}>{errors.length}</div>
          <div style={{ fontSize: 11, color: errors.length > 0 ? "#cf222e" : "#6b7280", fontWeight: 500 }}>Errors</div>
        </div>
      </div>

      <div style={{ display: "flex", gap: 16, marginBottom: 16, fontSize: 12 }}>
        <div>
          <span style={{ color: "#666" }}>Last advance: </span>
          <span style={{ fontWeight: 500 }}>{lastAdvance ? lastAdvance.timestamp : "Never"}</span>
        </div>
        <div>
          <span style={{ color: "#666" }}>Last sync: </span>
          <span style={{ fontWeight: 500 }}>{lastSync ? lastSync.timestamp : "Never"}</span>
        </div>
      </div>

      {runs.length === 0 ? (
        <div style={{ padding: 20, textAlign: "center", color: "#999", fontSize: 13, background: "#f9fafb", borderRadius: 8 }}>
          No heartbeat runs yet. The first advance run will fire at the next :00 or :30 mark.
        </div>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)" }}>
          <thead>
            <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Status</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Type</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Time</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Actions</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Findings</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Summary</th>
              <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Session</th>
            </tr>
          </thead>
          <tbody>
            {runs.map((r, i) => (
              <tr key={i} style={{ borderBottom: "1px solid #eee" }}>
                <td style={{ padding: "6px 8px" }}>{statusDot(r.status)}</td>
                <td style={{ padding: "6px 8px" }}>
                  <span style={{
                    padding: "2px 6px", borderRadius: 4, fontSize: 10, fontWeight: 600,
                    background: r.type === "advance" ? "#e0f2f1" : "#f0e6ff",
                    color: r.type === "advance" ? "#0d9488" : "#6e40c9",
                  }}>{r.type}</span>
                </td>
                <td style={{ padding: "6px 8px", fontSize: 11, color: "#666" }}>{r.timestamp}</td>
                <td style={{ padding: "6px 8px", fontWeight: 500 }}>{r.actions || 0}</td>
                <td style={{ padding: "6px 8px", fontWeight: 500, color: r.findings > 0 ? "#9a6700" : "#666" }}>{r.findings || 0}</td>
                <td style={{ padding: "6px 8px", color: "#444" }}>{r.summary}</td>
                <td style={{ padding: "6px 8px" }}>
                  {r.sessionUrl ? (
                    <a href={r.sessionUrl} target="_blank" rel="noopener noreferrer" style={{ padding: "2px 6px", borderRadius: 4, fontSize: 10, background: "#f0f0f0", color: "#0969da", textDecoration: "none" }}>view</a>
                  ) : "—"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

function SprintsTab() {
  const sprintStats = useMemo(() => {
    return SPRINTS.map((sprint) => {
      const activeCount = WORKTREES.filter((w) => {
        if (w.pr && (w.pr.includes("MERGED") || w.pr.includes("CLOSED"))) return false;
        return w.sprint === sprint.id;
      }).length;

      const mergedCount = MERGED.filter((m) => m.sprint === sprint.id).length;

      const noSprintActive = WORKTREES.filter((w) => {
        if (w.pr && (w.pr.includes("MERGED") || w.pr.includes("CLOSED"))) return false;
        return !w.sprint;
      }).length;

      const noSprintMerged = MERGED.filter((m) => !m.sprint).length;

      return {
        ...sprint,
        activeCount,
        mergedCount,
        totalCount: activeCount + mergedCount,
        noSprintActive: sprint.id === SPRINTS[0]?.id ? noSprintActive : 0,
        noSprintMerged: sprint.id === SPRINTS[0]?.id ? noSprintMerged : 0,
      };
    });
  }, []);

  return (
    <div>
      <div style={{ marginBottom: 16 }}>
        <div style={{ fontSize: 13, color: "#666", marginBottom: 8 }}>
          Sprint overview showing active and merged tickets per sprint
        </div>
      </div>

      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)" }}>
        <thead>
          <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
            <th style={{ padding: "8px 10px", textAlign: "left", fontSize: 11, color: "#666", fontWeight: 600 }}>Sprint</th>
            <th style={{ padding: "8px 10px", textAlign: "left", fontSize: 11, color: "#666", fontWeight: 600 }}>Date Range</th>
            <th style={{ padding: "8px 10px", textAlign: "center", fontSize: 11, color: "#666", fontWeight: 600 }}>Active</th>
            <th style={{ padding: "8px 10px", textAlign: "center", fontSize: 11, color: "#666", fontWeight: 600 }}>Merged</th>
            <th style={{ padding: "8px 10px", textAlign: "center", fontSize: 11, color: "#666", fontWeight: 600 }}>Total</th>
          </tr>
        </thead>
        <tbody>
          {sprintStats.map((s) => (
            <tr key={s.id} style={{ borderBottom: "1px solid #eee", background: s.isCurrent ? "#f0f9ff" : "transparent" }}>
              <td style={{ padding: "8px 10px", fontWeight: 600, color: s.isCurrent ? "#0969da" : "#333" }}>
                {s.name} {s.isCurrent && "⭐"}
                {s.noSprintActive + s.noSprintMerged > 0 && (
                  <div style={{ fontSize: 10, color: "#666", fontWeight: 400, marginTop: 2 }}>
                    + {s.noSprintActive + s.noSprintMerged} no-sprint items
                  </div>
                )}
              </td>
              <td style={{ padding: "8px 10px", fontSize: 11, color: "#666" }}>
                {s.startDate} → {s.endDate}
              </td>
              <td style={{ padding: "8px 10px", textAlign: "center", fontWeight: 600, color: "#0969da" }}>
                {s.activeCount + s.noSprintActive}
              </td>
              <td style={{ padding: "8px 10px", textAlign: "center", fontWeight: 600, color: "#2e7d32" }}>
                {s.mergedCount + s.noSprintMerged}
              </td>
              <td style={{ padding: "8px 10px", textAlign: "center", fontWeight: 700, color: "#333" }}>
                {s.totalCount + s.noSprintActive + s.noSprintMerged}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function ConfigTab() {
  const modelBadge = (m) => (
    <span style={{
      display: "inline-block", padding: "2px 8px", borderRadius: 4, fontSize: 11, fontWeight: 600,
      background: m === "Opus" ? "#fef3c7" : "#e0f2fe",
      color: m === "Opus" ? "#92400e" : "#0369a1",
    }}>{m}</span>
  );

  return (
    <div>
      <h3 style={{ fontSize: 13, fontWeight: 600, color: "#333", marginBottom: 8 }}>Zone → Model Mapping</h3>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)", marginBottom: 20 }}>
        <thead>
          <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Zone</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Model</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Rationale</th>
          </tr>
        </thead>
        <tbody>
          {ZONE_MODEL_CONFIG.map((z) => (
            <tr key={z.zone} style={{ borderBottom: "1px solid #eee" }}>
              <td style={{ padding: "6px 8px" }}><ZonePill zone={z.zone} /></td>
              <td style={{ padding: "6px 8px" }}>{modelBadge(z.model)}</td>
              <td style={{ padding: "6px 8px", color: "#666" }}>{z.rationale}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3 style={{ fontSize: 13, fontWeight: 600, color: "#333", marginBottom: 8 }}>Scheduled Heartbeats</h3>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)", marginBottom: 20 }}>
        <thead>
          <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Schedule</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Cadence</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Model</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Status</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Description</th>
          </tr>
        </thead>
        <tbody>
          {SCHEDULES.map((s) => (
            <tr key={s.name} style={{ borderBottom: "1px solid #eee" }}>
              <td style={{ padding: "6px 8px", fontWeight: 500 }}>{s.name}</td>
              <td style={{ padding: "6px 8px" }}>{s.cadence}</td>
              <td style={{ padding: "6px 8px" }}>{modelBadge(s.model)}</td>
              <td style={{ padding: "6px 8px" }}>
                <span style={{ padding: "2px 6px", borderRadius: 4, fontSize: 10, fontWeight: 600, background: s.status === "Active" ? "#dcfce7" : "#f3f4f6", color: s.status === "Active" ? "#166534" : "#6b7280" }}>{s.status}</span>
              </td>
              <td style={{ padding: "6px 8px", color: "#666" }}>{s.description}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3 style={{ fontSize: 13, fontWeight: 600, color: "#333", marginBottom: 8 }}>Internal Code Reviewers</h3>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)" }}>
        <thead>
          <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>ID</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Name</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Skill</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Model</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Enabled</th>
            <th style={{ padding: "6px 8px", textAlign: "left", fontSize: 11, color: "#666" }}>Focus</th>
          </tr>
        </thead>
        <tbody>
          {REVIEWERS.map((r) => (
            <tr key={r.id} style={{ borderBottom: "1px solid #eee", opacity: r.enabled ? 1 : 0.5 }}>
              <td style={{ padding: "6px 8px", fontFamily: "monospace", fontSize: 11 }}>{r.id}</td>
              <td style={{ padding: "6px 8px", fontWeight: 500 }}>{r.name}</td>
              <td style={{ padding: "6px 8px", fontFamily: "monospace", fontSize: 11 }}>{r.skill}</td>
              <td style={{ padding: "6px 8px" }}>{modelBadge(r.model)}</td>
              <td style={{ padding: "6px 8px" }}>{r.enabled ? "Yes" : "No"}</td>
              <td style={{ padding: "6px 8px", color: "#666" }}>{r.focus}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function App() {
  const [activeTab, setActiveTab] = useState("status");
  const [sortKey, setSortKey] = useState("lastActive");
  const [sortDir, setSortDir] = useState("desc");
  const [sprintFilter, setSprintFilter] = useState(CURRENT_SPRINT_ID);
  const [pageLoaded] = useState(() => {
    const now = new Date();
    return now.toLocaleString("en-US", {
      year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", timeZoneName: "short"
    }).replace(/(\d+)\/(\d+)\/(\d+),/, "$3-$1-$2");
  });

  const handleSort = (key) => {
    if (sortKey === key) {
      setSortDir((d) => (d === "asc" ? "desc" : "asc"));
    } else {
      setSortKey(key);
      setSortDir("asc");
    }
  };

  const activeWorktrees = useMemo(() => {
    return WORKTREES.filter((w) => {
      // Filter out merged/closed PRs
      if (w.pr && (w.pr.includes("MERGED") || w.pr.includes("CLOSED"))) {
        return false;
      }
      // Show items with no sprint OR items matching selected sprint
      // Special case: "all" shows everything
      if (sprintFilter === "all") return true;
      return !w.sprint || w.sprint === sprintFilter;
    });
  }, [sprintFilter]);

  const sorted = useMemo(() => {
    if (!sortKey) return activeWorktrees;
    const col = COLUMNS.find((c) => c.key === sortKey);
    if (!col) return activeWorktrees;
    const items = [...activeWorktrees];
    items.sort((a, b) => {
      const va = col.sortValue(a);
      const vb = col.sortValue(b);
      const cmp = va < vb ? -1 : va > vb ? 1 : 0;
      return sortDir === "asc" ? cmp : -cmp;
    });
    return items;
  }, [sortKey, sortDir, activeWorktrees]);

  const filteredMerged = useMemo(() => {
    if (sprintFilter === "all") return MERGED;
    return MERGED.filter((m) => !m.sprint || m.sprint === sprintFilter);
  }, [sprintFilter]);

  const needsYou = activeWorktrees.filter((w) => w.blockedType === "owner");
  const running = activeWorktrees.filter((w) => w.blockedType === "running");
  const waiting = activeWorktrees.filter((w) => w.blockedType === "external");
  const blocked = activeWorktrees.filter((w) => w.blockedType === "blocked");

  return (
    <div style={{ padding: 16, fontFamily: "system-ui, sans-serif", maxWidth: 900 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <h2 style={{ margin: 0, fontSize: 15, fontWeight: 700, color: "#222" }}>
            Board Status — jounce-workflow-ai
          </h2>
          <select
            value={sprintFilter}
            onChange={(e) => setSprintFilter(e.target.value)}
            style={{
              padding: "4px 8px", fontSize: 12, fontWeight: 500, borderRadius: 6,
              border: "1px solid #d0d7de", background: "#fff", color: "#333", cursor: "pointer"
            }}
          >
            <option value="all">All Sprints</option>
            {SPRINTS.map((s) => (
              <option key={s.id} value={s.id}>
                {s.name} {s.isCurrent ? "⭐" : ""}
              </option>
            ))}
          </select>
        </div>
        <div style={{ textAlign: "right" }}>
          <div style={{ fontSize: 11, color: "#999" }}>
            Data from: {LAST_UPDATED}
          </div>
          <div style={{ fontSize: 10, color: "#bbb", marginTop: 2 }}>
            Page loaded: {pageLoaded}
          </div>
        </div>
      </div>

      <div style={{ display: "flex", gap: 4, marginBottom: 16, borderBottom: "2px solid #e0e0e0" }}>
        {[
          { id: "status", label: "Board Status" },
          { id: "sprints", label: `Sprints (${SPRINTS.length})` },
          { id: "heartbeat", label: `Heartbeat (${HEARTBEAT_RUNS.length})` },
          { id: "config", label: "Configuration" },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              padding: "8px 16px", fontSize: 12, fontWeight: 600, border: "none", borderBottom: activeTab === tab.id ? "2px solid #0969da" : "2px solid transparent",
              background: "none", color: activeTab === tab.id ? "#0969da" : "#666", cursor: "pointer", marginBottom: -2,
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {activeTab === "config" && <ConfigTab />}
      {activeTab === "heartbeat" && <HeartbeatTab />}
      {activeTab === "sprints" && <SprintsTab />}

      {activeTab === "status" && <>
      <div style={{ display: "flex", gap: 12, marginBottom: 16, flexWrap: "wrap" }}>
        {[
          { label: "Needs You", count: needsYou.length, ...TYPE_STYLES.owner },
          { label: "Running", count: running.length, ...TYPE_STYLES.running },
          { label: "Waiting on Reviewer", count: waiting.length, ...TYPE_STYLES.external },
          { label: "Blocked", count: blocked.length, ...TYPE_STYLES.blocked },
        ].map((s) => (
          <div key={s.label} style={{ padding: "8px 14px", borderRadius: 8, background: s.bg, minWidth: 100, textAlign: "center" }}>
            <div style={{ fontSize: 22, fontWeight: 700, color: s.color }}>{s.count}</div>
            <div style={{ fontSize: 11, color: s.color, fontWeight: 500 }}>{s.label}</div>
          </div>
        ))}
      </div>

      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13, background: "#fff", borderRadius: 8, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,0.08)" }}>
        <thead>
          <tr style={{ background: "#f8f9fa", borderBottom: "2px solid #e0e0e0" }}>
            {COLUMNS.map((col) => (
              <SortHeader key={col.key} column={col} sortKey={sortKey} sortDir={sortDir} onSort={handleSort} />
            ))}
          </tr>
        </thead>
        <tbody>
          {sorted.map((w, i) => (
            <Row key={w.ticket || w.branch || i} w={w} />
          ))}
        </tbody>
      </table>

      {filteredMerged.length > 0 && (
        <>
          <h3 style={{ fontSize: 13, fontWeight: 600, color: "#666", marginTop: 20, marginBottom: 8 }}>Recently Merged</h3>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
            {filteredMerged.map((m) => (
              <div key={m.ticket} style={{ padding: "6px 12px", borderRadius: 6, background: "#e8f5e9", fontSize: 12 }}>
                <a href={m.ticketUrl} target="_blank" rel="noopener noreferrer" style={{ color: "#2e7d32", textDecoration: "none", fontWeight: 600 }}>{m.ticket}</a>
                {" "}
                <a href={m.prUrl} target="_blank" rel="noopener noreferrer" style={{ color: "#2e7d32", textDecoration: "none" }}>{m.pr}</a>
                <span style={{ color: "#666", marginLeft: 6 }}>{m.mergedDate}</span>
              </div>
            ))}
          </div>
        </>
      )}
      </>}
    </div>
  );
}
