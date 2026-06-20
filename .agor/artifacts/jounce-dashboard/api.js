import { BRANCH_ROWS, WEEK_ROWS, REPO_ROWS, SNAPSHOT_DATE, TICKET_DETAILS } from './data';

export { SNAPSHOT_DATE, TICKET_DETAILS };

export function hasCredentials() {
  return true;
}

export async function fetchLeaderboard(params = {}) {
  if (params.groupBy === 'repo') return REPO_ROWS;
  if (params.bucket === 'week') return WEEK_ROWS;
  return BRANCH_ROWS;
}
