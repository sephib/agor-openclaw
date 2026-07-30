# Board State — jounce-workflow-ai

*Last updated: 2026-07-30 08:01 IDT (advance heartbeat) — merged with 10:30 IDT manual scan*

---

## Active Worktrees

| Worktree | Zone | PR | CI | Jira | Status |
|---------|------|----|----|------|--------|
| aipcc-27645-server-resources | **Code** | [#1690](https://github.com/Jounce-IO/jounce/pull/1690) | 🔴 pre-commit ❌, JIRA Assoc ❌, e2e-product ❌; nox ✅, e2e-smoke ✅, e2e-api ✅, tox ✅ (run 30438043057) | [AIPCC-27645](https://redhat.atlassian.net/browse/AIPCC-27645) | 🔴 **CHANGES_REQUESTED by MenD32**. MERGEABLE. **Action: Address reviewer feedback + fix pre-commit + investigate e2e-product.** |
| jn-5695-db-connect-script | BLOCKED | [#1596 DRAFT](https://github.com/Jounce-IO/jounce/pull/1596) | CONFLICTING | [JN-5695](https://redhat.atlassian.net/browse/JN-5695) | 🔴 DRAFT + CONFLICTING; frozen since Jun 14. |
| jn-5795-upgrade-to-guidellm-v070 | Ingest | — | — | [JN-5795](https://redhat.atlassian.net/browse/JN-5795) | Design session done Jun 30. Ready for Plan phase. Stale 30+ days. |
| jn-5824-benchmark-run-configs | Code | — | — | [JN-5824](https://redhat.atlassian.net/browse/JN-5824) | Last session Jul 8 IDLE. Needs: configs, rebase, PR. Stale 22+ days. |
| jn-5872 | **Code** | [#1669 DRAFT](https://github.com/Jounce-IO/jounce/pull/1669) | 🔴 tox ❌, nox ❌, JIRA Assoc ❌, pre-commit ❌; CONFLICTING (run 30376499699) | [JN-5872](https://redhat.atlassian.net/browse/JN-5872) | 🔴 **CI degraded** — DRAFT, CONFLICTING. Unchanged since Jul 15. Needs rebase + CI fix. |
| jn-5865-ibm-cluster-connect | **Ingest** | — | — | [JN-5865](https://redhat.atlassian.net/browse/JN-5865) | Plan done ~23:06 IDT Jul 8. **Zone mismatch Day 22+** (still Ingest, should be Code). |
| aipcc-23845-cluster-connection | **Plan** | [#1698](https://github.com/Jounce-IO/jounce/pull/1698) | 🟡 CONFLICTING | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | OPEN, **CONFLICTING**, not draft. Needs rebase. |
| aipcc-23890-qe-cluster-tests | **NO ZONE** | [#1697 DRAFT](https://github.com/Jounce-IO/jounce/pull/1697) | REVIEW_REQUIRED (draft) | [AIPCC-23890](https://redhat.atlassian.net/browse/AIPCC-23890) | DRAFT. No zone assigned. |
| aipcc-23845-script-runner | **NO ZONE** | [#1700](https://github.com/Jounce-IO/jounce/pull/1700) | CONFLICTING, CodeRabbit only | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | NOT DRAFT. CONFLICTING. No zone. |
| aipcc-23845-generator-hotfix | **NO ZONE** | [#1701 DRAFT](https://github.com/Jounce-IO/jounce/pull/1701) | REVIEW_REQUIRED (draft) | [AIPCC-23845](https://redhat.atlassian.net/browse/AIPCC-23845) | DRAFT. No zone assigned. |
| aipcc-23895-docs-ibm | **Plan** | [#1696 DRAFT](https://github.com/Jounce-IO/jounce/pull/1696) | REVIEW_REQUIRED (draft) | [AIPCC-23895](https://redhat.atlassian.net/browse/AIPCC-23895) | DRAFT. |
| aipcc-23925-argo-public-url | **Plan** | [#1695 DRAFT](https://github.com/Jounce-IO/jounce/pull/1695) | REVIEW_REQUIRED (draft) | [AIPCC-23925](https://redhat.atlassian.net/browse/AIPCC-23925) | DRAFT. |

---

## Off-Board Worktrees (on different boards)

| Worktree | Board | Zone | Last Used | Notes |
|---------|-------|------|-----------|-------|
| create-jira-tickets | ed856893-92ff-40d0-8cba-6bdba005549b | Create Jira ticket | Jan 29 2026 | Different board, JN-5132 |
| jira-tickets-for-sephi | ed856893-92ff-40d0-8cba-6bdba005549b | Find Jira tickets | Jan 17 2026 | Different board |
| jn-4624-combine-data-from-all-regions | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Blocked | Apr 16 2026 | Different board, stale |
| jn-5120-update-marimo-experiment-dashboard-based-o | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Blocked | Apr 26 2026 | Different board |
| jn-5134-create-sql-queries-for-benchmark-visibilit | ed856893-92ff-40d0-8cba-6bdba005549b | Waiting | Apr 16 2026 | Different board |
| jn-5136-integrate-sql-queries-into-marimo-dashboar | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Blocked | Apr 26 2026 | Different board |
| jn-5246-enrich-experimentplan-deployment-configs-f-3 | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Blocked | May 12 2026 | Different board |
| jn-5527-remove-legacy-template-and-consolidate-con | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Ready | Jun 11 2026 | Different board |
| jn-5670-benchmark-visibility-dashboard | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Ready | Jun 11 2026 | Different board |
| jn-5676-dev-notebook-scaffold-operational-mode | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Ready | Jun 11 2026 | Different board |
| jn-5678-docs-dashboard-readme-and-setup-instructio | ee6dc34a-c588-4cd0-bca2-388abc670cdc | Blocked | Jun 11 2026 | Different board |
| jounce-mono-repo-analysis | ed856893-92ff-40d0-8cba-6bdba005549b | Plan | Mar 21 2026 | Different board |

---

## Attention Items

### 🔴 #1690 (AIPCC-27645) — CHANGES_REQUESTED

PR [#1690](https://github.com/Jounce-IO/jounce/pull/1690): "fix(helm): increase API server resources and probe tolerances"
- **State: OPEN, MERGEABLE, NOT DRAFT, CHANGES_REQUESTED by MenD32**
- **Action: Address MenD32 review feedback.**

---

### 🔴 #1669 (JN-5872) — CONFLICTING + DRAFT

PR [#1669](https://github.com/Jounce-IO/jounce/pull/1669): "feat(jbenchmark): improve dev-connect"
- **State: OPEN, DRAFT, CONFLICTING**
- **Action: Rebase on main + fix CI failures.**

---

### 🟡 #1698 (AIPCC-23845) — CONFLICTING

PR [#1698](https://github.com/Jounce-IO/jounce/pull/1698) — **CONFLICTING** (was MERGEABLE at last check).
- **Action: Rebase on main.**

---

### 📋 jn-5865 — Zone Mismatch (Ingest, Plan Done — Day 22+)

Plan session done ~23:06 IDT Jul 8. No code session triggered.
- **Propose:** Move to Code zone + trigger /implement:code.

---

### 🔄 jn-5824 — Stale (22+ days, no PR)

Last session Jul 8 IDLE.
- **Propose:** Fork a new session to generate configs, rebase on main, create PR.

---

### 🟡 4 Worktrees with NO ZONE

- aipcc-23890-qe-cluster-tests (#1697 DRAFT)
- aipcc-23845-script-runner (#1700 NOT DRAFT)
- aipcc-23845-generator-hotfix (#1701 DRAFT)
- All need zone assignment

---

## Recently Merged

| PR | Ticket | Merged | Worktree |
|----|--------|--------|---------|
| [#1670](https://github.com/Jounce-IO/jounce/pull/1670) | [JN-5844](https://redhat.atlassian.net/browse/JN-5844) | **16:03 IDT Jul 28** 🎉 | "docs(jbenchmark): add service, libs, and SQL domain AGENTS.md". Worktree ARCHIVED. |
| [#1723](https://github.com/Jounce-IO/jounce/pull/1723) | [AIPCC-27996](https://redhat.atlassian.net/browse/AIPCC-27996) | **11:31 IDT Jul 28** 🎉 | "feat(jbenchmark): exclude faulty experiments from export and cache lookups". No Agor worktree. |
| [#1667](https://github.com/Jounce-IO/jounce/pull/1667) | [JN-5845](https://redhat.atlassian.net/browse/JN-5845) | **14:12 IDT Jul 28** 🎉 | "docs(jbenchmark): add Helm and CI/CD domain AGENTS.md files". Worktree ARCHIVED. |
| [#1713](https://github.com/Jounce-IO/jounce/pull/1713) | [AIPCC-27994](https://redhat.atlassian.net/browse/AIPCC-27994) | **12:54 IDT Jul 27** 🎉 | "feat(jbenchmark): add is_faulty column, PATCH endpoint, and list filtering". No Agor branch. |

---

## Dashboard Artifact

- Board status dashboard artifactId: `019ed99f-bf7d-7c0b-b31d-c34d6da728ae`
- Jounce dashboard artifactId: `019ed0df-754f-77c4-9c13-02063e1be52e`
- Both on board `019eb849-ec5b-715e-b8cc-e37c4c387740`
