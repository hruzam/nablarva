---
brief: termpanum — observation lab for living CLI sessions
date: 2026-10-01
version: 0.1 (substrate · drafted by symmetry from the relay-design thread 2026-09-30/10-01)
authors: symmetry (claude.ai) · operator @majkee
status: SUBSTRATE for RUNBOOK · name GAVELED (flag.md L13) · everything else PROPOSED until the brief gavels
regime: vendor-invariant local toolbox · read-only by construction
sovereignty: HIGH — scripts + plain files; MCP optional and thin; no vendor primitive in the format
etymology: terminal + tympanum (the insect ear). stridularium calls you; termpanum hears the sessions.
home: toolbox/termpanum/ · sessions .dev/session/toolbox-termpanum-* (termbrana's pattern, L12)
---

# termpanum

Not a relay, and not a reader of meaning. A read-only ear on living CLI sessions (Claude Code,
Codex, agy): it records what they do as normalized events with a source and a certainty, and
gives nablarva's relay only discrete states. It runs with nablarva absent and meets it at a file
boundary (termbrana's M4 rule).

## AXIOMS  (#grep · falsifiable · strike before reading further)
- #ax1-ear-not-hand — termpanum never writes into a living session: no keystrokes (L4), no
    context injection. The onion study's context bus (ch. 6) moves to stridulatrix. Sensing never
    shares a ladder with acting (ommatermia #ax2). Experiments run only in fixture sessions the lab
    starts itself, sandboxed (doc 04 §4.14).
- #ax2-tap-high-tap-low — hooks and on-disk session records for meaning; PTY, process tree and
    kernel for liveness (study rule 1 · doc 04 §4.2). Falsified if, for a CLI with hooks, the PTY
    tap yields a state the hooks miss.
- #ax3-discrete-states — toward the relay the lab says idle · working · waiting · exited, never
    what the screen means (study §2.4, regex over paint). A cheap model may later learn fold rules,
    as a classifier only. Falsified if a needed state can't be told without comprehension; then a
    hook is missing, not a parser.
- #ax4-one-format — doc 04 §4.13 vocabulary + certainty (confirmed · observed · correlated ·
    inferred · unknown) + termbrana's provenance grade (raw_pty · rendered_ansi · rendered_text ·
    derived). Shared with ommatermia and termbrana; no fourth shape. Falsified if a field one of
    the three needs breaks another.
- #ax5-paths-not-content — every command returns a path, never content; the reader opens the
    file. Tokens stay cheap and the files stay the truth.
- #ax6-numbers-decide — a rule leaves the lab only through doc 04 §4.12 promotion: fixture, signal
    definition, version scope, known failure, fallback, regression test, redaction review.

## INVARIANT  (#invariant)
    EXPECT → TRIGGER → OBSERVE → COMPARE
- Ommatermia's loop, narrowed to observation. Name a standard event (turn start, turn end,
    approval prompt, spawn, compaction, crash), trigger it, record what each tap saw, compare.
- The trigger comes from a fixture session or from the operator, never from the lab into a
    living session.
- `--expect` is required. Without it an observation is a log line, not an experiment.
- Output: the study's observability matrix (§0.2) filled from measurement, per CLI and version,
    in the shape of doc 04's capability handshake (§4.15).

## TAPS — the FROM pipe  (#taps)
| layer | tap | source · certainty | gives |
|---|---|---|---|
| L5 agent CLI | hooks (Claude, Codex) · on-disk session records | hook · confirmed | what happened |
| L3/L2 multiplexer, PTY | tmux `pipe-pane` (raw_pty) · `-CC` · lifecycle hooks; the adapter's raw log once adapters exist (raw_pty, L3) | pty · observed | that the screen changed; stalls |
| L1 process + fds | descendant walk + fd snapshot on a tick | proc · observed | who runs, what is open |
| L0 kernel | pidfd / wait status | kernel · observed | alive, dead, exit code |

- Agents live in tmux, so the build plan's Zellij pieces get tmux equivalents: `pipe-pane` or
    `-CC` for the view lens, a layout script for `rack.kdl`, the `pane_pid`/`pane_tty` join for
    `$ZELLIJ_PANE_ID` (study §2.6).
- Zellij `subscribe` stays valid where Zellij hosts (termbrana, L11): rendered_text only.

## OUTPUTS — the TO pipe  (#outputs)
- events — append-only NDJSON, one writer (termpanum). The truth (study rule 3; S1's shape).
- snapshots — state is only ever a snapshot; history = the snapshot appended as an event (rule 2).
- slices — small files an AI reads (< 4 KB; study ch. 7, build plan 1.5).
- live feed — each reader keeps its own cursor and asks what's new since it (S2's shape). A
    session processing data live reads the same way.
- states → stridulatrix reads termpanum's journal from its own cursor. No pipe to name; it's a file.
- PAPERS — rare reports (#papers).

## ACCESS  (#access)
    agent ↔ (bash | MCP) ↔ termpanum CLI ↔ files
- Scripts + a key first (L3: monitor = plain files).
- MCP = an optional thin layer for seats without a shell: one read-only tool per CLI command, no
    server process holding state.
- Verbs (proposed): doc 04's lab surface renamed — `run <fixture>` · `replay <capture>` ·
    `compare <capture> <expected>` · `promote <set>` — plus three live ones: `state [<session>]` ·
    `since <cursor>` · `slice <name> <session>`. Each returns a path.
- The command family follows the claviature rule; the prefix is majkee's pick.

## STORAGE  (#storage)
Sovereignty gradient (ommatermia's shape):
    1. schema — authored, sovereign: the shared format (#ax4)
    2. events · snapshots · slices — generated. Live sessions: XDG state, not committed.
       Experiment bundles that a PAPER cites (doc 04 §4.9): committed.
    3. raw PTY bytes · full payloads — generated + gitignored
- Redact by default (doc 04 §4.14): keys, auth headers, environment secrets, tokens. Record an
    environment allowlist, never a dump. Raw PTY bytes carry whatever was typed.
- Final homes (code, config, data, runtime) belong to `nablarva-03-app-architecture`.

## PAPERS  (#papers · rare by design)
- Triggers: the version-drift alarm (doc 04 §4.15) · an event kind never seen before · a rule that
    passes the promotion test (§4.12).
- Path: `toolbox/termpanum/papers/<paper-content>.(<serial>.)<date>.md`
- Frontmatter = the abstract. Body facts cite event IDs.
- A reader seat drafts from slices; the lab never writes prose.
- Not the build plan's `docs/reports/`: those record probe results while building; PAPERS record
    what the running lab found.

## FALSIFICATION GATE  (#gate)
STOP building the PTY tap (keep L0/L1 liveness) if every state termpanum reports is already
available from hooks or on-disk session records, for Claude, Codex and agy alike. That is the
prior-art pattern (#weather); if it holds for all three, the screen tap is redundant.
Where the tap earns its keep: a CLI with no hook surface and a silent headless mode — agy today,
until its hook surface is known.

## ADOPTED — prior work, with the delta  (#adopt)
The wheel check on our own work comes out ADOPT:
- onion study (Nabla, 2026-09-17) = the formal PTY research: L0–L5 map, taps per multiplexer.
- unilarvatrix build plan (2026-09-18) = the builder draft; phases 0–2 stand.
- doc 04 lab (2026-07-31) = components, experiment bundle, promotion rule, vocabulary.
- termbrana M0 (frozen 2026-09-02) = what a Zellij plugin can capture.
Delta:
    1. name + home — `unilarvatrix`/`ulx` (standalone repo) and doc 04's `larva-lab` → termpanum
       at `toolbox/termpanum/` (L12: one repo).
    2. host — the Zellij rack → its own tmux window. Study §2.5 holds: never the window it observes.
    3. Phase 3 (context bus) leaves → stridulatrix.
    4. Phase 4's hook search for Codex and agy = the only external sweep left.
    5. Events take the shared format (#ax4), not the plan's own `{kind, src}` envelope.

## BUILD BOUNDARY  (#boundary)
BUILD NOW (once this brief gavels): build plan phases 0–2 with the delta above.
NOT HERE: context bus (→ stridulatrix) · any write into a living session · meaning read off the
screen · syscall tracing outside experiments (doc 04 §4.7) · vision · a GUI.

## HANDOFF → practical layer  (#handoff)
Owed, not resolved here:
- Codex and agy hook and on-disk session surfaces, current versions.
- The tmux pieces above, and the build plan's probe set (0.2) rerun under tmux.
- The shared format, frozen as its own small decision before a third toolbox hardens its own.
- The thin MCP layer, only when a shell-less seat needs it.

## WEATHER — prior art, 2026-09-30 (re-verify before use)  (#weather)
None of these reads session state off the screen. They use hooks or on-disk records, and tmux
only to type.
- keepmind9/clibot — tmux session per CLI; send-keys in; replies from history files or hooks.
    https://pkg.go.dev/github.com/keepmind9/clibot/internal/cli
- aelaguiz/codex_monitor_skill — Codex WORKING / WAITING / IDLE from rollout JSONL on disk.
    https://github.com/aelaguiz/codex_monitor_skill
- CochranResearchGroup/codex-wake — timed Codex wakes; context delivered by hook.
    https://github.com/CochranResearchGroup/codex-wake
- cfaysal/kherep #66 — Claude wakes an idle Codex across hosts with `codex queue`; content via a
    UserPromptSubmit hook. https://github.com/cfaysal/kherep/issues/66
- louislva/claude-peers-mcp — Claude↔Claude push through channels; broker + per-session MCP.
    https://github.com/louislva/claude-peers-mcp
- interlink-mcp — signed cross-machine agent chat over channels; hook-based wait fallback.
    https://docs.rs/crate/interlink-mcp/latest/source/docs/DELIVERY.md
- marceldarvas/cc-multi-cli-plugin — Claude Code drives Codex, Cursor, agy, OpenCode headless;
    agy read back from its on-disk transcript. https://github.com/marceldarvas/cc-multi-cli-plugin
- shindgew/agy-acp — one interactive agy PTY per session; state polled from agy's conversation db.
    https://github.com/shindgew/agy-acp
- tacogips/codex-agent — Codex session discovery, streaming, resume/fork, queue, daemon mode.
    https://github.com/tacogips/codex-agent
Vendor doors, parked (PTY is the base): Claude Code channels (research preview) · `codex queue`
(0.149.0+) · agy: no push door, no ACP yet.

## LINEAGE  (#lineage)
- 2026-07-31 doc 04 — lab designed as `larva-lab`; vocabulary; promotion rule.
- 2026-09-02 termbrana M0 frozen — Zellij plugins never see raw_pty.
- 2026-09-04 ommatermia brief — two ladders, experiment loop, sovereignty gradient (shape borrowed).
- 2026-09-17/18 onion study + unilarvatrix build plan (Nabla).
- 2026-09-30/10-01 relay-design thread (symmetry × majkee): PTY = base stone · discrete states ·
    the lab is a toolbox, not a second animal · context bus → relay · one format · scripts first,
    MCP thin · name termpanum (confirmed 10-01, L13).
- Kept separate from: stridulatrix (the relay; it writes) · ommatermia (graphical sensing; may one
    day graduate an actuator — termpanum never does).
