---
brief: relay-seam v2
date: 2026-09-13
status: FROZEN for vertical slice · conceptual loop closed · parked → practical project
authors: symmetry (claude.ai) · asymmetry (chatgpt) · gate: @majkee
lineage: brief 09-11 → asymmetry reply → countersign → addendum → consult r2 → asymmetry r2
supersedes: all of the above for build purposes; they remain as decisions record
sovereignty: HIGH — bus + protocol sovereign; adapters disposable; vendor mechanisms peripheral
placed_here_by: oraculum (cSharp nablarva-02), verbatim from majkee's drop 2026-09-13 — append-only pen; substrate for the practical project, not nablarva law; nablarva-side fold at .dev/session/nablarva-02-pipe-qualification/raw/fold.relay-seam-v2.2026-09-13.md
---

# Relay seam — v2

## What it is
A vendor-light continuity layer between disposable heterogeneous CLI sessions. Not orchestration. Not a cockpit. It removes @majkee from copy-paste relay and returns him to the gate.

## Constitution
    FILES       = truth
    MISSION     = invariant purpose  (relay carries the pointer only)
    EXCHANGE    = correlation
    PTY/TMUX    = lowest-common actuator (doorbell)
    ADAPTER     = disposable vendor knowledge
    ATTENTION   = uncertainty escalation
    NATIVE CLI  = escape hatch
    HUMAN       = gate/observer, never routine wire
    USAGE PATH  = interactive stays interactive (no silent API drift)

## Three planes  #three-planes
    ACTIVATION    tmux / PTY / native door        → endpoint      (doorbell)
    OBSERVATION   notify / hook / process / transcript metadata → relay  (evidence)
    AUTHORITATIVE _bus/X*.{request,response,receipt}.md          (truth)
Only the third decides semantic progress. Never promote plane 1 or 2 to plane 3.

## Axioms (strike cheaply)
1. #pointer-not-payload — activation is one line: *read `_bus/X42.request.md` and act.* Content never rides transport.
2. #endpoint-not-leader — seam knows `endpoint · channel · exchange · artifact · activation · attention · state`. Lead/architect are runbook roles above the seam.
3. #adapter-surface — `activate / observe / signal`. Nothing else. `observe` is an interface; sensors implement parts of it (native notify preferred, process/tmux state, expected-artifact state, transcript metadata as fallback). No sensor equals `observe`.
4. #no-record-no-delivery — seam invariant. Endpoint discipline (*produce the artifact*) is enforced by endpoint instructions, not by the seam.
5. #completion-is-protocol — exchange completes when the expected bus file exists. Not when a terminal goes quiet. Not when notify fires.
6. #notify-is-not-completion — vendor turn-end events wake the check; they never close the exchange. (Grounded: Codex 0.153.x emits agent-turn-complete for hidden internal turns.)
7. #nudge-is-conditional — notify + absent file → record observation. Nudge only when: correlated thread/session id ∈ active exchange ∧ no file ∧ no further turn within window. Every nudge is counted; nudge rate per endpoint = prompt-malformation map.
8. #transcript-is-sensor — Codex `~/.codex/sessions` / Claude Code projects JSONL: fallback evidence only. Pin on path, mtime, rollover. Never on record types or content. Never an identity authority — compaction rewrites, branching multiplies files, UUIDs duplicate. Prefer native thread/session id from notify/hook.
9. #no-transcript-injection — rejected as a channel. Revisionist door on resume, dead door live. Brief-injection via bus file is the sovereign path.
10. #mission-pointer-only — `exchange.mission:` is a reference. Reminding endpoints of purpose is another project (coherence homeostat), not this seam.
11. #native-reachable — the living session stays enterable with all vendor affordances. Relay is a view + doorbell, never a replacement terminal.
12. #usage-path — interactive subscriber sessions stay interactive; adapters must not route work into API paths silently.

## Slice cast (first instance)
- endpoint `codex` — role: lead (session, order, tests, final audit); observe via `notify` (agent-turn-complete) with thread_id correlation
- endpoint `claude-code` — role: architect (replies when a testable part is done); observe via Stop hook
- `@majkee` — gate/observer

## Vertical slice (build exactly this)
    mission M
      → _bus/X42.request.md          (authoritative)
      → activate(claude-code, ptr)   (doorbell)
      → claude-code works, emits _bus/X42.response.md
      → observe fires (hook)         → check file → complete
      → absent → observation → conditional nudge → ATTENTION → [enter native]
Required: one exchange id · one request file · one activation · one response/receipt · one attention path · one enter-native action.
Then repeat one previously painful multi-session probe. **Metric: did @majkee stop being middleware.**

## Brakes
- Count relays and nudges before/while building. Rate is the signal.
- No cockpit, scheduler, UI parser, pane scraper, new `_bus/` file kind.
- No `--resume` dependency in the seam.
- Reincarnation detector: not in the slice. Needs its own test (duplicate UUIDs, branching) before trust.
- Unattended channels: granted per channel on evidence, never default.
- Earn every layer: slice → second channel → concurrency → native adapters → composition.

## Kill test (asymmetry §11, verbatim intent)
Stop if reliable unattended crossings require continuously parsing/emulating vendor UI semantics (UI parsers, command ontology, version-specific state machines). Then: native orchestration per vendor + manual cross-vendor gates.

## Rejected (rationale in lineage files)
one-vendor teaming as whole system · full PTY orchestration as architecture · MCP/queue as protocol boundary · "say nothing to UI" rule · transcript injection · composer-reminds-purpose · nudge-on-every-absent-file · human as relay

## Open (carried, not blocking the slice)
- `_bus/` placement of reincarnation state transition (STATUS field vs label).
- Nudge window value — set empirically from the first probes.
- Two-planes contract sighted twice (here + Ommatermia) → canon candidate, separate thread.
