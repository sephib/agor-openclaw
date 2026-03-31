# Skills

Skills are reusable patterns and workflows for the agent to execute.

---

## What Are Skills?

Skills are **documented procedures** for common tasks. Think of them as SOPs (Standard Operating Procedures) that the agent can reference and follow.

**Examples:**
- Creating worktrees with consistent naming
- Spawning subsessions for research
- Running code review workflows
- Setting up CI/CD for a repo

---

## Two Types of Skills

### 1. Documented Workflows (This Directory)

Simple markdown files describing step-by-step procedures:

```
skills/
├── README.md (this file)
├── worktree-ops.md
├── session-spawn.md
└── code-review.md
```

**When to use:** Simple, human-readable procedures that don't need code execution.

### 2. Executable Tools (`.claude/` Directory)

For skills that need actual code execution, use Claude Code's `.claude/` directory:

```
.claude/
├── mcp-servers/          # Custom MCP servers
├── tools/                # Custom tool implementations
└── config.json           # Claude Code configuration
```

**When to use:** Skills that need:
- API integrations
- Complex logic
- System commands
- State management

---

## Skill Template

Create skills as markdown files with this structure:

```markdown
# Skill: [Name]

**When to use:** [Description of when this skill applies]

**Prerequisites:**
- [ ] Requirement 1
- [ ] Requirement 2

**Steps:**

1. **Step 1:** Description
   ```typescript
   // Code example if needed
   const result = await agor.worktrees.create({...});
   ```

2. **Step 2:** Description
   - Sub-step A
   - Sub-step B

3. **Step 3:** Description

**Outputs:**
- Expected result 1
- Expected result 2

**Error Handling:**
- Common error X → Solution
- Common error Y → Solution

**Related Skills:**
- [Link to related skill]
```

---

## Example: Worktree Creation Skill

See how BOOTSTRAP.md creates worktrees with the POC test. That's a skill in action:

1. Check if repo exists
2. Create worktree with Agor MCP
3. Record in memory/agor-state/worktrees.json
4. Place on main board
5. Log to daily memory

This pattern can be extracted into `skills/worktree-ops.md` for reuse.

---

## Skills vs. `.claude/` Tools

**Skills (markdown):**
- ✅ Simple to create and maintain
- ✅ Human-readable
- ✅ Easy to version control
- ✅ Agent reads and follows
- ❌ No code execution
- ❌ Manual steps

**`.claude/` Tools:**
- ✅ Executable code
- ✅ Complex logic
- ✅ API integrations
- ✅ Automatic execution
- ❌ Requires TypeScript/Node.js
- ❌ More setup overhead

**Best practice:** Start with documented skills (markdown), graduate to `.claude/` tools when automation is needed.

---

## Agor-Specific Skills

Skills in this workspace should leverage Agor MCP heavily:

### Core Skill Categories

**Worktree Operations:**
- Create feature branches
- Clean up completed work
- Sync with main branch
- Archive old worktrees

**Session Management:**
- Spawn research subsessions
- Coordinate multi-agent work
- Track genealogy
- Handle callbacks

**Code Quality:**
- Run automated reviews
- Check test coverage
- Lint and format
- Generate documentation

**Memory Management:**
- Update MEMORY.md from daily logs
- Sync agor-state/ with Agor
- Archive old logs
- Extract learnings

---

## Creating Your First Skill

1. **Identify a pattern** you repeat often
2. **Document the steps** in a new markdown file
3. **Test it** by following the steps manually
4. **Refine** based on what works
5. **Reference in AGENTS.md** so agent knows it exists

---

## The SKILL.md Standard

The [SKILL.md format](https://agentskills.io) is an open standard (originated by Anthropic) for defining agent capabilities. It's supported by 30+ platforms including Claude Code, OpenAI Codex, Cursor, GitHub Copilot, VS Code, Gemini CLI, Kiro, JetBrains, and Roo Code.

A SKILL.md file is just markdown describing:
- **When to use** the skill (trigger conditions)
- **Prerequisites** (tools, permissions, context needed)
- **Steps** to execute
- **Error handling** and edge cases

This is exactly the format used in this `skills/` directory. Skills you write here are compatible with the broader ecosystem.

---

## The Agent Skills Ecosystem

A large ecosystem of community-built skills exists across several discovery platforms:

### Discovery Platforms

| Platform | Catalog Size | Strengths | Install Method |
|----------|-------------|-----------|----------------|
| [skills.sh](https://skills.sh) | 83K+ skills | Curated, best UX, real install counts, CLI-first | `npx skills add <owner/repo>` |
| [SkillsMP](https://skillsmp.com) | 351K+ skills | Largest catalog, auto-crawls GitHub | Browse + manual install |
| [agentskills.io](https://agentskills.io) | Reference library | Official Anthropic spec site, trusted starting points | Manual |

### Installing Community Skills

```bash
# Install a skill from skills.sh
npx skills add <owner/repo>

# Skills are added to your .claude/ directory and immediately available
```

### Anthropic's Official Skills

The [anthropics/skills](https://github.com/anthropics/skills) repository contains high-quality, trusted skills maintained by Anthropic. These are good starting points and reliable references for writing your own.

### Evaluating Skill Quality and Security

**Before installing any community skill:**

1. **Read the SKILL.md source** — it's just markdown, easy to audit
2. **Check install counts** on skills.sh (higher = more vetted by community)
3. **Prefer known publishers** — official org repos, well-known maintainers
4. **Review what it executes** — skills can run shell commands; understand what they do
5. **Be cautious with low-install-count skills** from unknown authors

**Security context:** Community hubs have had malicious skill submissions (341 flagged by Feb 2026). The SKILL.md format itself is safe (it's markdown), but skills that invoke shell commands or install dependencies need scrutiny. This is standard supply-chain hygiene — same as evaluating any open-source dependency.

### When to Use Community Skills vs. Custom

**Use community skills when:**
- The task is a common pattern (linting, testing, deployment, code review)
- A well-adopted skill exists (high install count, known publisher)
- You want battle-tested workflows

**Build custom skills when:**
- The workflow is domain-specific to your repos or org
- You need tight integration with Agor MCP operations
- No community skill fits or existing ones need heavy modification
- Security requirements demand full control

**Principle:** Prefer community skills for common patterns, build custom for domain-specific needs.

---

## Skill Discovery as an Ongoing Practice

As you work with your human, watch for repeating patterns:
- Tasks that follow the same steps each time
- Workflows the human describes verbally that could be codified
- Pain points that a community skill might already solve

When you spot a pattern, check the ecosystem first. If a good skill exists, suggest it. If not, create one in `skills/` and consider contributing it back.

---

## Related Documentation

- **AGENTS.md** - References skills in the "Skills" section
- **TOOLS.md** - Environment-specific shortcuts
- **memory/learnings/** - Where you discover new patterns to turn into skills

---

_Skills are the building blocks of agent expertise. Start small, iterate, automate._
