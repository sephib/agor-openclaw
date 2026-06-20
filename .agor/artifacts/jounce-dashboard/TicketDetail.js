import React from 'react';

const STAGE_COLORS = {
  Ingest: '#9e9e9e',
  Plan: '#ff9800',
  Code: '#1a73e8',
  Revise: '#e91e63',
  Validate: '#9c27b0',
  Publish: '#4caf50',
  Respond: '#00bcd4',
  'Code Review': '#795548',
  Other: '#bdbdbd',
};

const MODEL_COLORS = {
  opus: '#1a73e8',
  sonnet: '#34a853',
  haiku: '#ff9800',
};

function fmtCost(n) {
  return `$${n.toFixed(2)}`;
}

function fmtTokens(n) {
  return n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(n);
}

function MiniBar({ items, colorMap, maxVal }) {
  if (!items || !items.length) return null;
  const max = maxVal || Math.max(...items.map((i) => i.c), 0.01);
  return (
    <div>
      {items.map((item, idx) => (
        <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 3 }}>
          <span
            style={{
              width: 70,
              fontSize: 10,
              color: '#555',
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
          <div style={{ flex: 1, background: '#f0f0f0', borderRadius: 3, height: 14, overflow: 'hidden' }}>
            <div
              style={{
                width: `${(item.c / max) * 100}%`,
                background: colorMap[item.label] || '#999',
                borderRadius: 3,
                height: '100%',
                minWidth: 3,
              }}
            />
          </div>
          <span style={{ width: 50, fontSize: 10, color: '#555', flexShrink: 0 }}>
            {fmtCost(item.c)}
          </span>
          <span style={{ width: 45, fontSize: 10, color: '#888', flexShrink: 0 }}>
            {fmtTokens(item.t)}
          </span>
        </div>
      ))}
    </div>
  );
}

function StagePill({ stage }) {
  return (
    <span
      style={{
        display: 'inline-block',
        padding: '1px 5px',
        fontSize: 9,
        borderRadius: 3,
        background: STAGE_COLORS[stage] || '#999',
        color: '#fff',
        whiteSpace: 'nowrap',
      }}
    >
      {stage}
    </span>
  );
}

function ModelPill({ model }) {
  if (!model) return null;
  return (
    <span
      style={{
        display: 'inline-block',
        padding: '1px 5px',
        fontSize: 9,
        borderRadius: 3,
        background: MODEL_COLORS[model] || '#999',
        color: '#fff',
        whiteSpace: 'nowrap',
      }}
    >
      {model}
    </span>
  );
}

export default function TicketDetail({ detail }) {
  if (!detail) return null;

  const stageItems = (detail.stages || []).map((s) => ({ label: s.z, c: s.c, t: s.t }));
  const modelItems = (detail.models || []).map((m) => ({ label: m.m, c: m.c, t: m.t }));

  return (
    <div
      style={{
        marginLeft: 88,
        marginTop: 4,
        marginBottom: 8,
        padding: '8px 12px',
        background: '#fafafa',
        border: '1px solid #e0e0e0',
        borderRadius: 6,
        fontSize: 11,
      }}
    >
      {stageItems.length > 0 && (
        <div style={{ marginBottom: 10 }}>
          <div style={{ fontSize: 11, fontWeight: 600, color: '#333', marginBottom: 4 }}>
            Stage Breakdown
          </div>
          <MiniBar items={stageItems} colorMap={STAGE_COLORS} />
        </div>
      )}

      {modelItems.length > 0 && (
        <div style={{ marginBottom: 10 }}>
          <div style={{ fontSize: 11, fontWeight: 600, color: '#333', marginBottom: 4 }}>
            Model Breakdown
          </div>
          <MiniBar items={modelItems} colorMap={MODEL_COLORS} />
        </div>
      )}

      {detail.sessions && detail.sessions.length > 0 && (
        <div>
          <div style={{ fontSize: 11, fontWeight: 600, color: '#333', marginBottom: 4 }}>
            Session Timeline
          </div>
          <div style={{ maxHeight: 180, overflowY: 'auto' }}>
            {detail.sessions.map((s, idx) => (
              <div
                key={idx}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  padding: '2px 0',
                  borderBottom: '1px solid #eee',
                }}
              >
                <span style={{ width: 62, fontSize: 10, color: '#888', flexShrink: 0 }}>
                  {s.d}
                </span>
                <StagePill stage={s.z} />
                <ModelPill model={s.m} />
                <span
                  style={{
                    flex: 1,
                    fontSize: 10,
                    color: '#444',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                  }}
                  title={s.t}
                >
                  {s.t}
                </span>
                {s.k > 0 && (
                  <span style={{ fontSize: 9, color: '#aaa', flexShrink: 0 }}>
                    {s.k} tasks
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
