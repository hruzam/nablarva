---
binding: houston
vendor: claude
runtime: Claude Code (agent file, YAML frontmatter + markdown body)
scope: mechanics only — how the identity is loaded, selected, permitted and proven on this runtime; grants no authority the identity or the addendum does not already name
authority: identity (`germline/agents/houston/identity.md`) + addendum (`project/nablarva.md`) → this file; locked L16.14 (capabilities read · grep · glob · write · spawn, bounded by card)
state: CANDIDATE — review stage; placement pending the B4 test (below); no fresh-session proof yet
home: this path is the WORKBENCH (read by nobody at runtime). Canonical home of the binding source = `/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/binding.claude.md` — `locked-by-gavel: majkee 2026-10-07` ("binding homes = `<project>/.germline/agents/houston/binding.<vendor>.md`"; proposal atlas, co-signed cartan(.germline), journal 2026-10-07 §1.1.2). The source home is assigned; activation and promotion keep their own gates (the file does not exist at that path until majkee promotes).
placement: DECIDED by observation 2026-10-07 (B4, majkee): `claude --agent houston` in the project root loaded the project-scoped probe body over the global `houston` → render destination = `<project>/.claude/agents/houston.md`; the global file is a project-less fallback, out of this assignment.
revision: unresolved — uncommitted at authoring
authored: 2026-10-06 · atlas-ui(harness) · assignment _bus/15 + amendment _bus/16
---
# houston · Claude binding

## Frontmatter the render carries (the only vendor facts)

```yaml
name: houston
description: >
  Grounding architect — one identity, three cards (consult · audit · sitting). Invoke `consult`
  from a session head or majkee when a move hits a trigger class, crosses an organ boundary,
  touches a lock or shows drift, or when closure needs an architecture check; returns
  fits · stretches · breaks · unclear with ≤5 constraints. `audit` (majkee, ad hoc) walks the
  whole animal and returns mech · judge · cross findings plus a wrapper-mechanics diff majkee
  commits. `sitting` (majkee, rare) is an ordinary session for a move that reshapes the animal.
  Never owns lifecycle, STATUS, the gavel, build or functional verification. Project method
  comes from the project's addendum; this render is bound to nablarva.
model: opus
effort: high
tools:
  - Read
  - Grep
  - Glob
  - Write
  - Agent
color: orange
```

- **`model` / `effort`** are weather, set here and only here (model floor in one place). The
  identity carries none.
- **`tools`** = exactly L16.14's capability set mapped to Claude Code: read·grep·glob → `Read`,
  `Grep`, `Glob`; write → `Write` (no `Edit`: the audit pen is a *new* diff file, never an
  in-place edit of a project surface; consult writes nothing); spawn → `Agent`. **No `Bash`**
  (the identity runs no shell). **No `WebFetch`/`WebSearch`** (research is a sitting input,
  supplied by the researcher seat).
- **Dropped from the pre-forge card, deliberately:** `permissionMode: bypassPermissions` ·
  the `Stop` → `~/.claude/houston.log` hook · the `PreToolUse` Bash guard (there is no Bash) ·
  `initialPrompt` reading `session/plan/session.plan.md` (dead path; plan.md abolished) ·
  `maxTurns: 50` (a bounded invocation ends when its finding is returned) · the `/goal` ·
  `houston.goal` · CapCom autonomy loop (L16.8: no autonomous loops). None of these is a
  vendor *necessity*; all were a Claude-only shape and are retired, not migrated.

## Card selection

The invoker names the card on the **first line** of the spawn prompt or the POINT:

```text
card: consult | audit | sitting
```

Absent → `consult`. The render's body states this rule; the identity's card contracts then
apply unchanged. A prompt that asks for work outside the named card's pen is answered with the
card's finding and the line `out of card: <what was asked> → <which card / which seat owns it>`.

## Entry declaration (germline invariance — one identity, two bindings; majkee journal 2026-10-07 §1.1.1)

| | **child binding** (returns bounded work) | **main-session binding** (leads a bounded invocation) |
|---|---|---|
| **cards** | consult · audit-as-probe | audit (full) · sitting |
| **entry** | `Agent` tool from a head's or majkee's session; agent resolved from `<project>/.claude/agents/houston.md` (project wins over the global twin — observed 2026-10-07, B4) | `claude --agent houston`, started in the project root (interactive; `-p` never) |
| **permissions** | the render's `tools:` (Read Grep Glob Write Agent) minus spawn (a subagent cannot spawn — observed); writes bounded per card | the render's `tools:` in full; writes bounded per card |
| **delegation authority** | none — a child does not delegate; a card needing spawn declares itself unqualified | bounded readers/verifier only; never Houston → Houston, never the creator |
| **return destination** | the spawner's context (the head writes constraints into RUNBOOK/STATUS; majkee receives probe findings) | the assigned file in the invoking bed (`raw/houston-audit.<date>[.<cycle>].{md,diff}`) or the sitting's own bed |

Codex has the same two routes on its own mechanisms (child = custom-agent TOML via `spawn_agent`;
main session = `codex --profile houston`) — `binding/codex.md`. Consult is the child binding on
both vendors; audit/sitting the main-session binding. "Cartan is the controller" is local policy,
not a vendor requirement (cartan(.germline), same note).

## Invocation shapes on this runtime (observed limits, not design choices)

| card | how it runs | what the runtime allows | consequence |
|---|---|---|---|
| consult | **subagent** spawned by the head's session (`Agent` tool) or by majkee's session | reads · returns markdown to the spawner · **cannot spawn** (a subagent cannot spawn subagents — observed in this harness) · `Write` available but the card writes nothing | fits the card exactly: writes nothing, returns a page |
| audit | subagent spawned by majkee's session, **or** a living session `claude --agent houston` | as a subagent: reads + `Write`, **cannot spawn** → its finding must open with `unqualified for the complete card: no spawn on this route` (identity §Capability); as a living session it *can* spawn readers → the qualifying route for a full audit | the diff + findings are written to the addendum's landing path (`raw/houston-audit.<date>[.<cycle>].{md,diff}`), never to the wrapper |
| sitting | **living session** only (`claude --agent houston` inside the sitting's bed, interactive) | full card set incl. spawn | drafts in its own bed; the head of that session is whoever the RUNBOOK names — the sitting card does not make me cSharp |

- **`-p` / print mode is never used** (operator law). Interactive sessions only.
- **Spawn is bounded:** readers (`field`, `zenith`, `eagle`) and a verifier when a card needs
  them; never a Houston-spawns-Houston loop (L16.8), never the creator (`atlas-*`) — building
  primitives is not a card.
- **Context loading is CWD-based**, not agent-file-based (temple card `raw.card.claude-code.md`
  §Context loading): the render receives the CLAUDE.md/AGENTS.md stack of the directory the
  session started in. Invoke from the project root so the saddle is the project's.

## Placement — pending the B4 test

Two candidate destinations; which one the render needs is **decided by one observation**, not
by preference:

| destination | role | holds if… |
|---|---|---|
| `<project>/.claude/agents/houston.md` (project-scoped) | the nablarva-bound render | a project agent **wins over a same-name global twin** when invoked inside its project folder (temple card `raw.card.claude-code.md:101`, `verified: 2026-09-02`, **expired** — the B4 test re-verifies) |
| `~/ia-sync/claude/agents/houston.md` (global, deploy.sh → `~/.claude/agents/`) | project-less fallback — **out of this assignment's scope** (`_bus/15` §Outside) | always loads; becomes a thin fallback only if B4 holds, else must itself carry the nablarva render |

**B4 test (step 0 of this assignment, write scope: one untracked file):** an untracked
`nablarva/.claude/agents/houston.md` with marker `description: HOUSTON_PLACEMENT_PROBE …`;
a **fresh** interactive session started in `/home/hruzam/unikuklatrix/nablarva`; `/agents`;
observe which `houston` is listed (marker = project wins; the global description = global wins);
delete the file. Result → `_bus/15.atlas-ui.return.md` field 2, and this table collapses to one
row.

## Fresh-session proof — what "verified" requires (separate recorded check, `_bus/15` §Checks (2))

A fresh interactive session, started in the project root, with the render at its decided
destination, must show — each as a dated line with the command/observation:

1. **Invocation identity:** the `/agents` wizard is **removed** in the current Claude Code
   (observed 2026-10-07: "The /agents wizard has been removed … edit the files directly:
   .claude/agents/ (this project) · ~/.claude/agents/ (all projects)"). Proof is therefore
   behavioural: start `claude --agent houston` in the project root and ask *"do you know this
   text?"* with a sentence unique to this render — the reply must locate it in its system
   instructions (not the pre-forge body). Same probe via `Agent` for the child route.
2. **Card selection:** a spawn with `card: consult` on line 1 returns a consult-shaped finding
   (verdict · ≤5 constraints · tags); a spawn with no card line defaults to consult; a spawn
   asking for an audit under `card: consult` returns `out of card:`.
3. **Read/write scope:** consult writes no file (check the bed before/after); audit writes only
   `raw/houston-audit.<date>.{md,diff}` in the invoking bed.
4. **Spawn capability:** as a subagent, an `Agent` call is refused or absent (expected); as a
   living session, one bounded reader spawn succeeds. Source declarations and the earlier
   nested-spawn observation on the Codex side are **not** proof for this binding.

A matching stamp and `verify_cmd` prove composition only; this list proves behaviour. Both are
required before the render's `verified:` line changes from `none`.

## Vendor delta — what this file is not

No project paths beyond the two destinations above (project facts live in the addendum); no
authority beyond L16.14's capability set; no renderer. Edits go here, then the render is
re-composed by hand and re-stamped; the README's `verify_cmd` and the binding body-equality
line (Condition B, `_bus/16` §3) catch a render whose binding section drifted from this file.
