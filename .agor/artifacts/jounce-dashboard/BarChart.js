import React, { useState } from 'react';
import TicketDetail from './TicketDetail';
import { TICKET_DETAILS } from './api';

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

const JIRA_PATTERN = /^JN-\d+$/;
const JIRA_BASE = 'https://jounce.atlassian.net/browse/';

export default function BarChart({ items }) {
  const [tooltip, setTooltip] = useState(null);
  const [expanded, setExpanded] = useState(null);

  if (!items.length) {
    return <p style={{ color: '#888', fontSize: 13 }}>No data</p>;
  }

  const max = Math.max(...items.map((i) => i.totalCost), 0.01);

  return (
    <div style={{ fontFamily: 'sans-serif' }}>
      {items.map((item, idx) => {
        const isTicket = JIRA_PATTERN.test(item.label);
        const detail = isTicket ? TICKET_DETAILS[item.label] : null;
        const hasDetail = !!detail;
        const isExpanded = expanded === item.label;

        return (
          <div
            key={idx}
            style={{ marginBottom: 8 }}
            onMouseEnter={() => !isExpanded && setTooltip(idx)}
            onMouseLeave={() => setTooltip(null)}
          >
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                cursor: hasDetail ? 'pointer' : 'default',
              }}
              onClick={() => {
                if (hasDetail) {
                  setExpanded(isExpanded ? null : item.label);
                  setTooltip(null);
                }
              }}
            >
              {hasDetail && (
                <span style={{ width: 12, fontSize: 10, color: '#888', flexShrink: 0 }}>
                  {isExpanded ? '▼' : '▶'}
                </span>
              )}
              {!hasDetail && <span style={{ width: 12, flexShrink: 0 }} />}
              {isTicket ? (
                <a
                  href={`${JIRA_BASE}${item.label}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={(e) => e.stopPropagation()}
                  style={{
                    width: 68,
                    fontSize: 12,
                    color: '#1a73e8',
                    textAlign: 'right',
                    flexShrink: 0,
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                    textDecoration: 'none',
                  }}
                  title={item.label}
                >
                  {item.label}
                </a>
              ) : (
                <span
                  style={{
                    width: 68,
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
              )}
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
            {tooltip === idx && !isExpanded && (
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
                {item.lastActive && <>&nbsp;|&nbsp; Last: {item.lastActive}</>}
                {hasDetail && (
                  <span style={{ color: '#1a73e8', marginLeft: 8 }}>Click to expand</span>
                )}
              </div>
            )}
            {isExpanded && <TicketDetail detail={detail} />}
          </div>
        );
      })}
    </div>
  );
}
