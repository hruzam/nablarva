# @Epoch reading-map — reposoma raw.* trees
Date: 2026-08-07
Triggered by: Preflight PARALLEL track — reposoma reading-map for thematic area (single-CLI-program / two-programs-communicating)
Method: inventory + locate + flag. NOT content synthesis. One-liners below are inferred from
path/filename/first-lines only (per subagent report), not deep-read. Treat any "what it is"
line as a LOCATE gist, not a verified summary.
Discipline note: full recursive listing performed by @zenith subagent (mtimes from filesystem,
not git). Four target files + raw.settings/README.md content-gisted (first ~15-20 lines each).
raw.guides/ and raw.research/ have NO top-level README/INDEX — confirmed absent.

---

## 1. HOW REPOSOMA IS ORGANIZED

Three raw.* trees, distinct roles, only one carries an explicit signpost:

- **raw.guides/** — how-to / operational guides, no top-level README. 9 subdirs (codex-builder-user,
  geminicli@com, intake, PAD, piql, project-base-pattern, reach, research.web) + loose root files
  (guide-publishing.md, recover-broken-loop.md, onboarding-kit.md, bootstrap-new-project.md,
  project-intake.md, audit-loop.card.draft.md). 22 files, 9 dirs. Newest activity: 2026-08-07
  (codex-builder-user/, PAD/pad-builder.md — same-day as this run).

- **raw.research/** — dated research output, topic-per-subdir pattern with `draft/` (sources.jsonl,
  README working notes) + `report/` (dated `raw.<topic>.<date>.md` deliverables) pairs. Largest tree:
  94 files, 48 dirs. Topics observed: agent-docs, ai-news, arch, capabilities-economy-hygiene.claude,
  claude-code-coldstart, cli-fork-branch, editors, fable-restrictions, harness (briefs+reports),
  laravel, nature, octopus-pilot, ollama-docs, openrouter, session-hygiene, temple-audit-2, trace-refs.
  No top-level README/INDEX — the draft/report pairing per-topic IS the implicit structure
  (draft = working/sources, report = dated finished output).

- **raw.settings/** — "reference primitives and knowledge cards." **Has an explicit signpost**:
  `raw.settings/README.md` (dated 2026-08-03), which states: this dir holds volatile RAG-refreshable
  facts about tools the temple builds with; "the recalibration researcher refreshes these; agent
  authors read them." Pattern legend from the README itself:
  - `raw.card.*.md` = RELATIVE knowledge cards, volatile facts, **decay by `half_life_days`**
    (frontmatter field — not independently verified per-card in this pass, see GAPS)
  - `raw.claude-agents.harness.*.md` = full Claude Code agents harness (dated snapshot)
  - `researcher.recalibration.standing-prompt.md` = standing prompt for the recalibration researcher (me)
  - `card.template.md` = template, copy for new cards
  - `agents-staging/` = agent drafts pre-promotion to `~/.claude/agents/`
  27 files, 3 dirs. Newest: 2026-08-05 (raw.card.claude-code.md, raw.card.codex-cli.md,
  raw.card.session-hygiene.md).

Signpost logic: raw.settings is the only tree that explains itself in-tree. raw.guides and
raw.research rely on filename/path convention only — a real gap for a first-time reader (see GAPS).

---

## 2. READING INVENTORY

### SCOPE 1 — single CLI as a program (terminal, events, hooks, life-hacks, harness lifecycle)

| Path | What it is (locate gist) | Freshness |
|---|---|---|
| `raw.research/harness/reports/2026-07-20-harness-lifecycle-skill-injection-safe-protocol.md` | Harness lifecycle / skill-injection mechanics study — mental model "Agent=program, harness=glue," framed as safe-protocol study for harness builder | 2026-07-20 — aging (18d old), recheck against current Claude Code skill-injection behavior |
| `raw.research/harness/reports/2026-08-01-remote-control-tmux-ssh-persistence.md` | Remote control / tmux / ssh persistence for CLI sessions | 2026-08-01 — current |
| `raw.research/harness/reports/2026-07-20-cloud-session-invariance.md` | Cloud session invariance (single-session lifecycle under cloud conditions) | 2026-07-20 — aging |
| `raw.research/harness/method.ring-trio.md` | Named method doc, likely harness-testing pattern (ring-trio) | 2026-07-16 — aging, unverified content |
| `raw.research/harness/research-pattern.md` / `.json` / `.jsonl` | Research-pattern schema/log for harness research | 2026-06-17 — STALE, oldest in tree |
| `raw.research/harness/source-catalog.json` / `.jsonl` | Source catalog for harness research runs | 2026-06-17 — STALE |
| `raw.research/harness/briefs/kick-brief-R1-research-center.md`, `R2-gemini.md`, `R3-chatgpt-cursor.md`, `R1-contamination-log.md` | Original kickoff briefs for a 3-way (R1/R2/R3) harness research round | 2026-06-17 — STALE, likely superseded |
| `raw.research/harness/reports/report-R1-research-center-grounded.md`, `report-R2-gemini*.md`, `report-R3-chatgpt-reality-check.md`, `RR-01-brand-competence-*.md`, `triangulation-R1-R2-R3.md` | Grounded reports + triangulation from the R1/R2/R3 round | 2026-06-17 — STALE |
| `raw.research/claude-code-coldstart/README.md` + `report/2026-07-21-claude-p-cold-start-mechanics.md` | Claude Code `-p` cold-start mechanics (single CLI program boot behavior) | 2026-07-21 — aging, worth re-verify (`-p` flag behavior version-sensitive) |
| `raw.research/agent-docs/report/raw.agent-docs.2026-08-01.md` | Fetched substrate snapshot of claude-code-docs (sub-agents doc, scope precedence table, "background by default since v2.1.198") — 8/8 sources, dated fetch | 2026-08-01 — current, BUT contains a version-pinned claim (`v2.1.198`) that must be re-verified live before quoting |
| `raw.research/agent-docs/report/2026-07-17-claude-skills-nesting-rube-goldberg.md` | Claude skills nesting behavior study | 2026-07-17 — aging |
| `raw.research/agent-docs/draft/README.md` + `sources.jsonl` | Working notes / source list for agent-docs topic | 2026-07-10 — aging |
| `raw.research/session-hygiene/report/raw.session-hygiene.2026-08-01.md` | Session hygiene findings (single-CLI lifecycle discipline) | 2026-08-01 — current |
| `raw.research/session-hygiene/draft/README.md` + `sources.jsonl` | Working draft for session-hygiene | 2026-08-01 — current |
| `raw.settings/raw.card.claude-code.md` | Knowledge card: Claude Code CLI (version/capability facts) | 2026-08-05 — current, but is exactly the kind of card that decays by half_life_days — verify field before trusting |
| `raw.settings/raw.card.codex-cli.md` | Knowledge card: Codex CLI | 2026-08-05 — current, same caveat |
| `raw.settings/raw.card.gemini-cli.md` | Knowledge card: Gemini CLI | 2026-07-03 — STALE-leaning (35d), Gemini CLI ships fast, re-verify |
| `raw.settings/raw.card.session-hygiene.md` | Knowledge card: session hygiene practices | 2026-08-05 — current |
| `raw.settings/raw.card.claude-ai.md` | Knowledge card: claude.ai (web) | 2026-07-16 — aging |
| `raw.settings/raw.card.cursor-ide.md` | Knowledge card: Cursor IDE | 2026-07-16 — aging |
| `raw.settings/raw.card.eagle.md` | Knowledge card: Eagle (project-orientation agent) | 2026-07-16 — aging |
| `raw.guides/codex-builder-user/codex-line.builder.md` | Builder-side guide for "codex-line" (Codex CLI harness pattern) | 2026-08-07 — current, written TODAY |
| `raw.guides/codex-builder-user/codex-line.user.md` | User-side guide for "codex-line" | 2026-08-07 — current, written TODAY |
| `raw.guides/PAD/pad-builder.md` | PAD builder guide (single-agent primitive?) | 2026-08-07 — current, written TODAY |
| `raw.guides/geminicli@com/subagents.md` | Gemini CLI subagents guide | 2026-06-19 — STALE, Gemini CLI subagent shape likely moved since |
| `raw.guides/guide-publishing.md` | Guide-publishing process doc | 2026-06-17 — STALE |
| `raw.guides/recover-broken-loop.md` | Life-hack: recovering a broken agent loop | 2026-06-17 — STALE (mechanics-focused, may still be valid but unverified) |
| `raw.guides/onboarding-kit.md` | Onboarding kit for new sessions/agents | 2026-07-07 — aging |
| `raw.guides/bootstrap-new-project.md` | Bootstrap-new-project guide | 2026-07-07 — aging |
| `raw.guides/project-intake.md` | Project intake process | 2026-07-15 — aging |

### SCOPE 2 — two programs communicating (composites)

| Path | What it is (locate gist) | Freshness |
|---|---|---|
| `raw.research/cli-fork-branch/cli-fork-branch.source-map.2026-08-05.md` | Source map for CLI fork/branch topic — likely session-forking across CLI instances (composite pattern) | 2026-08-05 — current |
| `raw.research/cli-fork-branch/report/raw.cli-fork-branch.2026-08-05.md` | Report deliverable for cli-fork-branch | 2026-08-05 — current |
| `raw.research/octopus-pilot/program.pulse.md` | Octopus-pilot program pulse — multi-agent/multi-program orchestration pilot | 2026-07-16 — aging |
| `raw.research/octopus-pilot/session/tasks/T1.md` | Octopus-pilot session task T1 | 2026-07-16 — aging |
| `raw.research/octo-launcher.handoff.claude.md` | Handoff doc for an "octo-launcher" — likely the multi-instance launcher for octopus-pilot | 2026-07-16 — aging |
| `raw.research/program-pulse.contract.claude.md` | Contract doc for program-pulse pattern (cross-program status protocol) | 2026-07-16 — aging |
| `raw.research/multi-agent-composition-and-swarms.seed.2026-06-16.md` | Seed doc on multi-agent composition/swarms | 2026-06-16 — STALE, oldest research file in tree |
| `raw.research/swarm-composition-source-loop.md` | Swarm composition source loop pattern | 2026-06-17 — STALE |
| `raw.research/agentic-sovereignty.source-map.2026-06-16.md` + `.report.2026-06-16.md` | Agentic sovereignty source-map + report — likely governs autonomy boundaries in composite/multi-agent setups | 2026-06-16/17 — STALE |
| `raw.research/real-reposoma-domain-seats.seed.md` | Domain-seat allocation seed (which agent owns which domain — cross-agent boundary design) | 2026-06-17 — STALE |
| `raw.settings/raw.card.gty.md` + `raw.card.gty.addendum-by-majkee-headless-regime.md` | Knowledge card "gty" + headless-regime addendum — likely a cross-program/headless orchestration pattern (name not expanded, verify) | 2026-06-19/20 — STALE |
| `raw.settings/raw.card.autonomous-orchestrator.md` | Knowledge card: autonomous orchestrator pattern (composite control) | 2026-06-20 — STALE |
| `raw.settings/agents-staging/epoch.md`, `orby.md`, `agy/orby.SKILL.md`, `agy/FORMAT-FINDINGS.md` | Agent drafts pre-promotion — epoch.md is a draft of THIS agent; orby.md + orby.SKILL.md suggest a second agent seat that composites with Epoch | 2026-06-19 — STALE, and epoch.md draft is worth diffing against my live definition |
| `raw.research/harness/reports/2026-08-01-remote-control-tmux-ssh-persistence.md` | (cross-listed) remote-control persistence is inherently two-endpoints-communicating (local driver + remote tmux/ssh target) | 2026-08-01 — current |

---

## 3. FRESHNESS FLAGS (Epoch specialty)

- **Version-pinned claim found and NOT yet live-verified**: `raw.research/agent-docs/report/raw.agent-docs.2026-08-01.md`
  line 9 states subagents run "Background by default since v2.1.198." This is a concrete Claude Code
  version string, dated fetch 2026-08-01 (6 days old, otherwise current-leaning), but per doctrine
  I do not carry a version claim forward without live re-verification in the actual research run.
- **raw.settings/raw.card.*.md decay mechanism unconfirmed**: README says cards "decay by `half_life_days`"
  (frontmatter field), but this preflight pass did NOT open each card to read its frontmatter —
  only mtimes were collected. Before trusting any card's currency, the actual `half_life_days`
  value must be read, not inferred from file mtime alone. This is a genuine gap in this pass (method:
  inventory/locate, not content-read — flagging, not fixing).
- **raw.settings/raw.card.gemini-cli.md** (2026-07-03, 35 days old) and **raw.guides/geminicli@com/subagents.md**
  (2026-06-19, 49 days old) — Gemini CLI ships fast; both are stale-leaning candidates for a live
  Epoch research pass before any Gemini CLI decision.
- **harness/ R1-R3 round** (briefs + reports + research-pattern + source-catalog, all 2026-06-17) is the
  oldest coherent cluster in raw.research (51 days old) — likely superseded by newer harness reports
  dated 2026-07-20 and 2026-08-01 in the same subdir. Reading order should prefer the newer two over
  the R1-R3 round unless doing archaeology.
- **Same-day files** (2026-08-07, i.e. today): `raw.guides/codex-builder-user/*` and
  `raw.guides/PAD/pad-builder.md` — these are the freshest artifacts in either tree and were almost
  certainly produced by/for this same preflight cycle. Worth confirming they're not still mid-draft.
- **agentic-sovereignty / multi-agent-composition-and-swarms / real-reposoma-domain-seats** cluster
  (all 2026-06-16/17) is the oldest material touching scope-2 (composites) — 51+ days old, predates
  the more recent cli-fork-branch (2026-08-05) and octopus-pilot (2026-07-16) work. If scope-2 reading
  starts here, flag that domain-seat conclusions may have been superseded by octopus-pilot / cli-fork-branch.

---

## 4. GAPS (candidates for a live research pass)

- **No top-level README/INDEX in raw.guides/ or raw.research/** — only raw.settings self-documents.
  A reader entering raw.guides or raw.research cold has to infer structure from filename convention
  alone (draft/report pairing in raw.research; loose topical subdirs in raw.guides). Not a live-research
  gap, but a structural one worth flagging to whoever owns reposoma.
- **"gty" card** (`raw.settings/raw.card.gty.md` + headless-regime addendum) — name never expanded in
  this pass; if this is load-bearing for the scope-2 (composite) reading, its meaning should be
  confirmed by reading it, not inferred.
- **codex-line (raw.guides/codex-builder-user/)** is brand-new (today) and not yet cross-referenced
  against `raw.settings/raw.card.codex-cli.md` (2026-08-05) — worth checking these two don't
  contradict each other on Codex CLI capability claims.
- **No live-verified current state for**: Gemini CLI (card 35d old), Cursor IDE (card 22d old),
  Claude Code exact current version (the `v2.1.198` claim above). These are exactly the candidates
  a live Epoch pass should target next, per my own doctrine, before any version-sensitive claim is
  used downstream.
- **Octopus-pilot / octo-launcher cluster** (2026-07-16) touches scope-2 directly (multi-instance
  launcher) but has no visible newer report — unclear if it's active or dormant. Worth a status check
  before relying on it as current composite-pattern doctrine.
- **No file in either tree explicitly titled around "hooks"** despite scope-1 asking for
  "events, hooks, life-hacks" — closest matches are the harness lifecycle/skill-injection report
  (2026-07-20) and cold-start mechanics report (2026-07-21), but neither is a dedicated hooks doc.
  This is a candidate gap for a live research pass if hooks specifically are in scope.

---

## Sections to refresh: [raw.settings/raw.card.gemini-cli.md, raw.guides/geminicli@com/subagents.md, the v2.1.198 subagents-background-default claim in raw.agent-docs.2026-08-01.md, raw.settings/raw.card.cursor-ide.md, raw.settings/raw.card.claude-code.md half_life_days field, harness/ R1-R3 round superseded-status check]
