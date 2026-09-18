---
kind: head note — fold of the frozen relay-seam v2 brief into this bed's scope (second fold; the first is fold.relay-seam-round2.2026-09-13.md and stands)
author: oraculum (cSharp)
date: 2026-09-13
source: /home/hruzam/unikuklatrix/nablarva/meshup/a-symmetry-lightest/brief.relay-seam.v2.2026-09-13.md
authority: none — v2 is the seam thread's frozen build brief; for nablarva it is substrate. Nablarva law (flag L3/L4/L6/L9′/L12, bus GUIDE) wins on collision; the build bed (nablarva-03) cites v2 as founding substrate beside design.r1
---

# Relay seam v2 — deltas for nablarva-02, two collisions named first

## Collision 1 — first slice actuator (same as round 2, now frozen on their side)

v2 §Vertical slice: `activate(claude-code, ptr)` by **doorbell** (PTY/tmux) into a Claude session,
observed by Stop hook. Nablarva-02: native `codex queue` into a **Codex** session, observed by
app-server status / notify. Flag L4 forbids the doorbell without a gavel; v2's own activation
plane lists "native door" as legitimate. Resolution unchanged: nablarva orders actuators by law
— native first (this bed) → if native fails, STOP → a *separate* L4 gavel for a path-only
doorbell, with v2 axiom 1 as its spec. The Claude-side native door (cross-session messaging,
Stop hook) is sibling C. Neither changes bed 02.

## Collision 2 — `_bus/` vocabulary

v2 §Three planes: `_bus/X*.{request,response,receipt}.md` — three kinds. Nablarva bus law:
`point · return · verdict`, **no fourth kind**, numbered by the status owner. Mapping, so the
words never fork on disk:

| v2 | nablarva | note |
|---|---|---|
| `request` | `NN.<seat>.point.md` | exchange id = cycle number + `return_to:` |
| `response` | `NN.<seat>.return.md` | the RETURN at exactly `return_to:` |
| `receipt` | the RETURN's existence at `return_to:` (seam level) · the VERDICT's `return:` field (acceptance level) | **no `receipt` file** |
| "exchange complete" (axiom 5) | **RETURN present** | not "accepted"; acceptance = VERDICT, STATUS advance = owner — r1 keeps these distinct |

## What v2 sharpens beyond the round-2 fold (adopt)

- **Three planes** as vocabulary: ACTIVATION (doorbell/native door) · OBSERVATION (notify, hook,
  process, transcript metadata) · AUTHORITATIVE (bus files). Only plane 3 decides progress.
  Identical to r1's evidence/record split and asymmetry's two planes; now with a name.
- **Axiom 6 #notify-is-not-completion**, grounded: *Codex 0.153.x emits `agent-turn-complete`
  for hidden internal turns.* Consequence for Cartan's preflight §1.7: a notify event wakes the
  `test -f return_to` check and never closes anything; correlate by `thread_id` from the notify
  payload; verify the hidden-internal-turn behavior on installed 0.154.0. If RETURN 01 does not
  cover it, cycle 02 asks for it; POINT 01 is not edited again.
- **Axiom 8 #transcript-is-sensor** — binding `session_id` comes from the native id (notify /
  hook / `$CODEX_THREAD_ID`), never from a rollout filename; `evidence_locator` is metadata only.
  Compaction rewrites, branching multiplies files, UUIDs duplicate. r1 already separates
  session id from incarnation; this fixes *where the id comes from*.
- **Axiom 7 #nudge-is-conditional** — v2 permits an automated conditional nudge (correlated id
  ∈ active exchange ∧ no file ∧ no further turn within window). Bed 02 keeps nudges
  **human-fired and counted**; the conditional automation is an unattended grant per endpoint on
  evidence — v2's own brake says the same. No collision; a later layer.
- **Nudge window** — v2 leaves it empirical. Bed 02's positive case can measure *turn end →
  RETURN present* latency on the disposable target; record it in the PAD report fence as a
  timing observation, not a policy. Feeds the window later.
- **Rejected list** — "MCP/queue as protocol boundary": nablarva agrees. Bed 02 qualifies
  `codex queue` as an **actuator** (activation plane); the protocol boundary is the file plane.
  Say so in the VERDICT so a GO is never read as "queue is the protocol".

## Answers carried back to the seam thread (via majkee, if wanted)

- Reincarnation transition: host-local binding `generation++` + retyped STATUS hold; never a
  `_bus/` kind or label. (Unchanged from the round-2 fold.)
- Nudge window: measured in bed 02's positive case; value reported in the qualification VERDICT.
- The practical project's first slice differs from v2's by law, not by taste: native door first,
  doorbell only by gavel. Both slices share every other line of the constitution.

## Parked

Slice cast (roles by runbook — nablarva casts per bed); Ommatermia two-planes canon candidate;
unattended channels; composition. Higher mathematics stays parked.
