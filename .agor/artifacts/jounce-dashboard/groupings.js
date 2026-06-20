import { TICKET_LAST_ACTIVE } from './data';

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

export const SORT_OPTIONS = [
  { id: 'cost', label: 'Cost' },
  { id: 'date', label: 'Last Active' },
];

function sortTickets(items, sortBy) {
  if (sortBy === 'date') {
    return items.sort((a, b) => {
      const da = TICKET_LAST_ACTIVE[a.label] || '0000-00-00';
      const db = TICKET_LAST_ACTIVE[b.label] || '0000-00-00';
      return db.localeCompare(da);
    });
  }
  return items.sort((a, b) => b.totalCost - a.totalCost);
}

export const GROUPINGS = [
  {
    id: 'ticket',
    label: 'By Ticket',
    apiParams: { groupBy: 'branch' },
    hasSortOptions: true,
    transform: (rows, sortBy) => {
      const items = groupByKey(rows, (r) => extractTicket(r.branchName));
      items.forEach((item) => {
        item.lastActive = TICKET_LAST_ACTIVE[item.label] || null;
      });
      return sortTickets(items, sortBy);
    },
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
