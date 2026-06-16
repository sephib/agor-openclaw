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
