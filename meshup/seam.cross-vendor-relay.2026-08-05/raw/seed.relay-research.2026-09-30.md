---
seed: relay — big-scope research gate
date: 2026-09-30
home: nablarva · session root `relay-00-research/`
name: unassigned — `relay` is a working slug, yours to rename
canon: runbook/res/research.md (gaveled 2026-09-03) · runbook/GUIDE.md §golden rule · relay-seam v2 kill test (Asymmetry §11)
lineage: brief.relay-seam.v2.2026-09-13.md
status: SEED · session not opened · blind triangulation pending (2 briefs)
sovereignty: HIGH — truth on the file plane; every transport replaceable
---

# relay — research seed

## Axioms (strike by number)

1. `nablarva` is the lab that hosts big-scope research (res/research.md), not this animal's name. The animal is unnamed.
2. Scope is BIG — a standalone system: session relay + mechanical tracker + phone lens. The research gate runs before any RUNBOOK.
3. Your three parts map onto canon, not onto three new siblings: the prior-art sweep is check 1 (wheel); the formal PTY research and the tracker draft open only after the verdict, as `relay-01-pty` and `relay-02-tracker`.
4. Endpoints: claude, codex, agy. agy is Google's side since Gemini CLI stopped serving personal tiers on 2026-06-18. agy was rejected earlier as redundant with KUKLA's orchestration; here it returns as an endpoint only. Strike if you meant claude + codex.
5. The PTY is the base layer (your call): every CLI runs in a terminal, and the terminal doesn't move with vendor features. Vendor doors stay parked until the vendors' bigger shifts.
6. The PTY carries the impulse; the file carries the content. The bus file is the completion; the PTY only says something happened. Fourth sighting of the two-planes contract (after Ommatermia, relay-seam v2, Asymmetry).
7. Every prompt, hand-written included, is structured: addressed blocks (e.g. one for Cartan) in markdown or a programmatic enclosure the parser can find. Prompt forging is Ptyra's territory — the rule lands there, not as a second authority here.
8. `send` is always bound to bash or a hook. Hooks are native to Codex and Claude; a checker confirms the hook fired.
9. The parser answers discrete states — idle · working · waiting-for-input · exited — never what the screen means. A cheap model (Haiku-class) may later learn fold rules, as a classifier only. Crossing into comprehension trips the kill test.
10. Heads already fan out spawns on tight windows. How a vendor slices a spawn's context is the template for what a PTY window must show.
11. First build is a window-to-window notifier (yours); cross-session buffer first was my counter — OPEN. The full-transcription organ comes later, only if the channel proves open and the parser has stable mount points. Files stay the safe layer.
12. Part 3 (tracker builder draft) is written in a separate track by another Symmetry incarnation — or already exists from an earlier one. Strike the wrong half.

## The gate (canon, verbatim)

gate: a recorded VERDICT — worth reinventing, or not — with its recommendation on disk.

## The three checks, mapped

1. **Wheel check** ← your prior-art sweep. Who already tracks or drives CLI sessions through the terminal — published, not kept as private know-how. Dated sources, an @Epoch-class pass, not cutoff memory.
2. **Overengineering check** — does the tracker need to exist, or does a smaller composition of existing parts serve (tmux, hooks, on-disk session records, `_bus/`)?
3. **Vendor-harness check** — will the CLIs ship this natively? Name the native change that retires the build.

Closure (canon): REINVENT · ADOPT (what, plus the delta) · REFUSE. A conditional recommendation names its condition testably.

## After the verdict — open only on REINVENT or ADOPT-with-delta

| session | gate | kind |
|---|---|---|
| `relay-01-pty` | we know which session states the PTY layer yields vendor-neutrally across claude, codex and agy — and which only through per-vendor screen parsing (kill-test territory) | knowledge |
| `relay-02-tracker` | a builder-informative draft of the mechanical tracker exists, execution-ready | brief, not build |

Method for 01 — yours, with Ommatermia's loop as precedent: drive the standard events (turn start, turn end, approval prompt, spawn, compaction, crash) with an `--expect` for each, then compare what the tracker saw. The log becomes an experiment: OBSERVE → EXPECT → INTERVENE → OBSERVE → COMPARE.

## DO NOT BUILD — until the verdict

- no parser, no notifier daemon, no phone-app code
- no per-vendor screen-state machine — the kill test names "version-specific state machines"
- no transcript injection (rejected, relay-seam v2)
- no full PTY orchestration as architecture (rejected, relay-seam v2). PTY as impulse layer is not that — keep the difference visible.

## Symmetry-side sightings, 2026-09-30 — weather; keep from blind seats until the collision

Wheel candidates:
- keepmind9/clibot — one tmux session per CLI; input by send-keys; replies pulled from history files or hooks; Gemini and ACP adapters. https://pkg.go.dev/github.com/keepmind9/clibot/internal/cli
- aelaguiz/codex_monitor_skill — Codex session state (WORKING / WAITING / IDLE) parsed from rollout JSONL on disk. https://github.com/aelaguiz/codex_monitor_skill
- CochranResearchGroup/codex-wake — timed Codex wakes, tmux-targeted or app-server-targeted; context delivered by hook. https://github.com/CochranResearchGroup/codex-wake
- cfaysal/kherep #66 — a Claude session wakes an idle Codex session across hosts with `codex queue`, pointer-only text; content arrives through a UserPromptSubmit hook. https://github.com/cfaysal/kherep/issues/66
- louislva/claude-peers-mcp — Claude↔Claude messages pushed through channels; broker plus per-session MCP server. https://github.com/louislva/claude-peers-mcp
- interlink-mcp — signed cross-machine agent chat over channels, with a hook-based wait fallback. https://docs.rs/crate/interlink-mcp/latest/source/docs/DELIVERY.md
- marceldarvas/cc-multi-cli-plugin — Claude Code drives Codex, Cursor, agy and OpenCode over headless transports; agy's answer is read back from its on-disk transcript. https://github.com/marceldarvas/cc-multi-cli-plugin
- shindgew/agy-acp — ACP adapter: one interactive agy PTY per session, state polled from agy's conversation db. https://github.com/shindgew/agy-acp
- tacogips/codex-agent — Codex session discovery, streaming, resume/fork, queue, daemon mode. https://github.com/tacogips/codex-agent

Pattern: none of these reads session state off the screen. They read on-disk session records or hooks, and use tmux only to type. Hypothesis for check 1, not a finding. If it holds, it sharpens axiom 5 toward PTY as actuator (seam v2's doorbell) and files/hooks as sensor.

Vendor-harness candidates:
- Claude Code channels — MCP servers push events into a running session; research preview, v2.1.80+, custom servers behind a development flag, claude.ai login. https://code.claude.com/docs/en/channels.md
- `codex queue` — Codex 0.149.0 (2026-08-20); delivers into an existing session via the shared app-server; observed waking an idle session on 0.153.4. https://codex.danielvaughan.com/2026/08/29/codex-cli-v0149-multi-session-agents-dashboard-codex-queue-working-directory/
- agy — no push door found; no native ACP (open request). https://github.com/google-antigravity/antigravity-cli/issues/31
- Retirement candidate: a push door or native ACP in all three CLIs retires the PTY doorbell.

## Carried from earlier this thread — unstruck

What rolls to majkee from cSharp (vocabulary-bound):
1. gavel — promote, deploy, canon change
2. gate change or sibling opening
3. STOP or BLOCKED VERDICT
4. loop budget spent (~10 cycles, "buy more loops") or fork width > 3–4
5. irreversible op outside RUNBOOK holds
6. seats still disagreeing after one pushback each
7. curvature the head can't resolve

## Open

- program name (`relay` is a placeholder)
- build order: notifier-first vs buffer-first (axiom 11)
- phone lens: own program, or inside this scope → note.phone-lens.2026-09-30.md
