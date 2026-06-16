// agorGrants inject as AGOR_TOKEN / AGOR_API_URL (bare names).
// CRA Sandpack may also expose REACT_APP_* variants — read both as fallback.
const BASE = process.env.AGOR_API_URL || process.env.REACT_APP_AGOR_API_URL;
const TOKEN = process.env.AGOR_TOKEN || process.env.REACT_APP_AGOR_TOKEN;

export function hasCredentials() {
  return Boolean(BASE && TOKEN);
}

export async function fetchLeaderboard(params = {}) {
  const url = new URL(`${BASE}/leaderboard`);
  // FeathersJS REST uses $limit for pagination; 500 covers current 230+ branches with room to grow
  Object.entries({ ...params, $limit: 500 }).forEach(([k, v]) => {
    if (v !== undefined) url.searchParams.set(k, String(v));
  });
  const res = await fetch(url.toString(), {
    headers: { Authorization: `Bearer ${TOKEN}` },
  });
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    throw new Error(`API ${res.status}: ${body}`);
  }
  const json = await res.json();
  return json.data || [];
}
