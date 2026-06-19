export const ZONE_MODEL_CONFIG = [
  { zone: "Ingest", model: "Opus", rationale: "Deep understanding to parse tickets and set context" },
  { zone: "Plan", model: "Opus", rationale: "Architecture and planning require strongest reasoning" },
  { zone: "Code", model: "Sonnet", rationale: "Execution-focused; fast and cost-effective for coding" },
  { zone: "Revise", model: "Opus", rationale: "Addressing review feedback requires judgment" },
  { zone: "Verify", model: "Sonnet", rationale: "Running checks and validations" },
  { zone: "Validate", model: "Sonnet", rationale: "Full validation passes" },
  { zone: "Publish", model: "Sonnet", rationale: "PR creation is mechanical" },
  { zone: "Respond", model: "Opus", rationale: "Communication/Slack needs nuance and judgment" },
  { zone: "Code Review", model: "Opus", rationale: "Review requires deep reasoning for subtle issues" },
  { zone: "BLOCKED", model: "Sonnet", rationale: "Triage and status checks" },
];

export const SCHEDULES = [
  {
    name: "Board Advancement",
    cadence: "Every 30 min",
    model: "Sonnet",
    status: "Active",
    description: "Scan worktrees, auto-advance when conditions met",
  },
  {
    name: "External Sync (Jira/PRs)",
    cadence: "Daily 8am IDT",
    model: "Sonnet",
    status: "Active",
    description: "Jira sprint scan, PR comments, merged PR detection",
  },
];

export const REVIEWERS = [
  {
    id: "arch",
    name: "Architecture Review",
    skill: "/senior-review:code-review",
    model: "Sonnet",
    enabled: true,
    focus: "Coupling, patterns, failure flows, scoring",
  },
  {
    id: "diff",
    name: "Diff Quality Review",
    skill: "/review-pr-diff",
    model: "Sonnet",
    enabled: true,
    focus: "Changes, readability, Pythonic quality",
  },
  {
    id: "impl",
    name: "Implementation Review",
    skill: "/implement:code",
    model: "Sonnet",
    enabled: true,
    focus: "Implementation correctness, acceptance criteria coverage, code completeness",
  },
  {
    id: "domain",
    name: "Domain Review",
    skill: "custom (TBD)",
    model: "Sonnet",
    enabled: false,
    focus: "Marimo rules, DAL patterns, test effectiveness",
  },
];
