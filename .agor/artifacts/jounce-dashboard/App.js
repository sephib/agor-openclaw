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
