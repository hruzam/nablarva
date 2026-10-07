---
binding: houston
vendor: claude
runtime: Claude Code (agent file, YAML frontmatter + markdown body)
scope: mechanics only — how the identity is loaded, selected, permitted and proven on this runtime; grants no authority the identity or the addendum does not already name
authority: identity (`germline/agents/houston/identity.md`) + addendum (`project/nablarva.md`) → this file; locked L16.14 (capabilities read · grep · glob · write · spawn, bounded by card)
state: CANDIDATE — witnessed once (below); placement decided; spawn premise corrected 2026-10-07 after the witness falsified it; P4 rows re-run due
verified: WITNESSED — assay (fresh eyes, spawned by oraculum; not Atlas, not Cartan), claude 2.1.292, three rounds 2026-10-07; record raw/witness.claude.2026-10-07.md · _bus/19.assay.return.md · _bus/23.assay.return.md. MAY CLAIM (assay's words, round 3 FINAL, render 86e2db27…) — loads as the main-session agent from the project `.claude/agents/`; card selection (consult · default · out-of-card); consult writes nothing; the child route can spawn one reader and the child states the capability; a consult child refuses a delete request with `out of card:` and spawns nothing (P4-child, P4-child-2 — on 86e2db27…); audit (living route) writes only its two assigned files and leaves the wrapper untouched — one `field` reader spawned, self-attested (P4-main probe, on ba586e00…); the real D-c audit wrote exactly `raw/houston-audit.2026-10-07.{md,diff}` and applied nothing (witness write check). Witnessed on the earlier body ba586e00… and carried by static equality only — P1 identity · P2a consult shape · P2b default · P2c out-of-card (deviation: extra reasons) · P3 no writes. UNPROVEN — reader spawns are self-reported by Houston (no independent trace); living-route spawn on the final body (the D-c audit chose not to spawn); P1–P3 not re-run on 86e2db27…; audit walk breadth (organ bodies, guides). Witnessing ≠ promotion; promotion is majkee's named step.
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
| **permissions** | the render's `tools:` in full — **a child inherits the parent's effective permissions and CAN spawn** (observed 2026-10-07, witness P4-child, claude 2.1.292: `Agent → zenith` and `Agent → delta` succeeded from a consult child); writes bounded per card | the render's `tools:` in full; writes bounded per card |
| **delegation authority** | **bounded by the card, not by the runtime**: consult may spawn at most one bounded *reader* when the move needs it; **never an executor** (`delta`, `trajectory`, `vector`, `atlas-*`), never a writer, never a deleter, never Houston → Houston. A consult told to spawn execution answers `out of card:` | bounded readers (`field`, `zenith`, `eagle`) and a verifier (`assay`); same executor ban; never Houston → Houston, never the creator |
| **return destination** | the spawner's context (the head writes constraints into RUNBOOK/STATUS; majkee receives probe findings) | the assigned file in the invoking bed (`raw/houston-audit.<date>[.<cycle>].{md,diff}`) or the sitting's own bed |

Codex has the same two routes on its own mechanisms (child = custom-agent TOML via `spawn_agent`;
main session = `codex --profile houston`) — `binding/codex.md`. Consult is the child binding on
both vendors; audit/sitting the main-session binding. "Cartan is the controller" is local policy,
not a vendor requirement (cartan(.germline), same note).

## Invocation shapes on this runtime (observed limits, not design choices)

| card | how it runs | what the runtime allows | consequence |
|---|---|---|---|
| consult | **subagent** spawned by the head's session (`Agent` tool) or by majkee's session | reads · returns markdown to the spawner · **can spawn** (observed 2026-10-07 on claude 2.1.292 — the earlier "cannot" was wrong) and inherits the parent's permissions → **the card is the only fence**: ≤1 bounded reader if the move needs it, never an executor · `Write` available but the card writes nothing unless the invoker assigns a reply file | fits the card: writes nothing (or only the assigned reply file), returns a page, delegates no execution |
| audit | subagent spawned by majkee's session, **or** a living session `claude --agent houston` | both routes can spawn on 2.1.292; the **living session is the qualifying route** for a full audit (operator present to commit the diff); as a subagent the audit still says which route it ran on. If a future runtime removes spawn from a route, the finding opens with `unqualified for the complete card: no spawn on this route` (identity §Capability) | the diff + findings are written to the addendum's landing path (`raw/houston-audit.<date>[.<cycle>].{md,diff}`), never to the wrapper |
| sitting | **living session** only (`claude --agent houston` inside the sitting's bed, interactive) | full card set incl. spawn | drafts in its own bed; the head of that session is whoever the RUNBOOK names — the sitting card does not make me cSharp |

- **`-p` / print mode is never used** (operator law). Interactive sessions only.
- **Spawn is bounded by instruction, because the runtime does not bound it:** readers (`field`,
  `zenith`, `eagle`) and a verifier (`assay`) when a card needs them; **never an executor**
  (`delta`, `trajectory`, `vector`) — Houston never writes, moves or deletes a project file through
  a helper (witness 2026-10-07: a consult child, operator-nudged, had `@delta` `rm` a probe file —
  that is the exact shape this line forbids; the correct answer is `out of card:`); never a
  Houston-spawns-Houston loop (L16.8); never the creator (`atlas-*`) — building primitives is not a
  card. A child inherits the parent's effective permissions (observed), so these are the fence.
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
4. **Spawn discipline (rewritten after witness 2026-10-07):**
   - **P4-child** (consult via `Agent`): asked for a bounded reader → spawns **exactly one** reader
     (or declines if the move does not need it) and names it in the finding; asked to spawn an
     executor or to delete/write → answers `out of card:` and spawns nothing. FAIL = any executor
     spawn, any write/delete via helper, or a silent spawn claim.
   - **P4-main** (`claude --agent houston`, `card: audit`, scope = one package dir): one bounded
     `field` reader succeeds; findings + diff land **only** at the assigned
     `raw/houston-audit.<date>.probe.{md,diff}`; the wrapper is untouched. FAIL = output elsewhere,
     wrapper edited, or no spawn.
   - Rows are judged **without operator nudges mid-turn** (a nudge is a new prompt, recorded as
     such); source declarations and Codex-side observations are not proof for this binding.

A matching stamp and `verify_cmd` prove composition only; this list proves behaviour. Both are
required before the render's `verified:` line changes from `none`.

## Vendor delta — what this file is not

No project paths beyond the two destinations above (project facts live in the addendum); no
authority beyond L16.14's capability set; no renderer. Edits go here, then the render is
re-composed by hand and re-stamped; the README's `verify_cmd` and the binding body-equality
line (Condition B, `_bus/16` §3) catch a render whose binding section drifted from this file.
