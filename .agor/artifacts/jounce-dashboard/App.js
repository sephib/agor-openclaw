import React, { useState, useEffect, useCallback } from 'react';
import { GROUPINGS, SORT_OPTIONS } from './groupings';
import { fetchLeaderboard, SNAPSHOT_DATE } from './api';
import GroupSelector from './GroupSelector';
import BarChart from './BarChart';

export default function App() {
  const [groupingId, setGroupingId] = useState('ticket');
  const [sortBy, setSortBy] = useState('cost');
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const grouping = GROUPINGS.find((g) => g.id === groupingId);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const rows = await fetchLeaderboard(grouping.apiParams);
      setItems(grouping.transform(rows, sortBy));
    } catch (e) {
      setError(e.message);
      setItems([]);
    } finally {
      setLoading(false);
    }
  }, [grouping, sortBy]);

  useEffect(() => {
    load();
  }, [load]);

  return (
    <div style={{ padding: 20, maxWidth: 700, fontFamily: 'sans-serif' }}>
      <h2 style={{ margin: '0 0 4px', fontSize: 16, fontWeight: 600, color: '#222' }}>
        Jounce Cost Dashboard
      </h2>
      <div style={{ fontSize: 11, color: '#aaa', marginBottom: 16 }}>
        Snapshot from {SNAPSHOT_DATE}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 12 }}>
        <GroupSelector groupings={GROUPINGS} selected={groupingId} onChange={setGroupingId} />
        {grouping.hasSortOptions && (
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 12, color: '#555' }}>
            <span>Sort:</span>
            {SORT_OPTIONS.map((opt) => (
              <button
                key={opt.id}
                onClick={() => setSortBy(opt.id)}
                style={{
                  padding: '2px 8px',
                  fontSize: 11,
                  border: '1px solid #ccc',
                  borderRadius: 3,
                  background: sortBy === opt.id ? '#1a73e8' : '#fff',
                  color: sortBy === opt.id ? '#fff' : '#333',
                  cursor: 'pointer',
                }}
              >
                {opt.label}
              </button>
            ))}
          </div>
        )}
      </div>
      {loading && <p style={{ color: '#888', fontSize: 13 }}>Loading…</p>}
      {error && (
        <div style={{ color: '#c00', fontSize: 13, marginBottom: 12 }}>
          {error}
        </div>
      )}
      {!loading && !error && <BarChart items={items} />}
    </div>
  );
}
