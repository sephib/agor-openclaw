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
