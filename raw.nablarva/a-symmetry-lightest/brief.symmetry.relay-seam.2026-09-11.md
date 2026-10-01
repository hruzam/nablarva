---
brief: relay-seam (cross-vendor middleware between CLI team leaders)
date: 2026-09-11
thread: agentive collaboration → parked for practical project
author: symmetry (claude.ai) · countersign pending: asymmetry (chatgpt) · gate: @majkee
regime: brief — NOT implementation; ground later
status: SEED · re-measure of a build started ~2026-07/08 · do NOT build before axioms are struck
sovereignty: HIGH — seam + protocol sovereign-authored; adapters disposable by design
---

# Brief — the relay seam

## Why re-measured now
@majkee started a tmux/PTY-layer mechanism for exchanging prompts between Claude Code and Codex sessions (~1.5 months ago). Question: did vendor or community shipping since then make it redundant? Answer: **partly — as transport, yes; as discipline, no.**

## What moved (search-derived 2026-09-11 — verify against vendor docs before build)
- **Claude Code: agent teams.** Vendor-native orchestration of multiple Claude Code sessions as teammates, driven over tmux or iTerm2 (`it2`). Claude-only. Docs: code.claude.com/docs/en/agent-teams
- **Codex: `codex queue`** (v0.149.0, 2026-08-20). CLI primitive delivering a message into a live Codex session — replaces the undocumented app-server `turn/steer` WebSocket workaround. Codex-only.
- **Codex as MCP server** (`codex mcp-server`). Second door in; new session per call, no streaming to caller.
- Community layer (primeline claude-tmux-orchestration, craftzdog tmux-claude-session-manager, CodeAgentSwarm, etc.): all single-vendor or GUI-shaped. None enforce a file-plane discipline.
- **Nobody ships the neutral seam between runtimes.** Not commercially interesting to a vendor; structurally necessary to a sovereign operator.

## Axioms (strike cheaply)  #grep
1. #transport-vs-discipline — vendors now ship *transport* (get a prompt into a session). Neither ships *discipline* (truth-lives-in-files emitted as a condition of the exchange). The build is the discipline, not the transport.
2. #seam-not-engine — do NOT build a general orchestration engine. Build the peer-level bus between **team leaders** (one Claude Code lead, one Codex lead). Each lead spawns its own sub-agents inside its vendor's native mechanism; the seam never reaches inside a half.
3. #adapter-rots-by-design — one thin adapter per vendor (delivery + read-back only). Adapters are expected to rot on vendor shifts and be rewritten in ~40 lines. Feature parity is never chased.
4. #file-plane-is-the-body — every exchange across the seam is materialised as a git-tracked markdown record before/at delivery. If the adapter dies, the record survives and the exchange is replayable by hand.
5. #floor-is-send-keys — raw tmux `send-keys` remains the fallback transport for any vendor that still has a terminal. It is the floor, not the design.
6. #tail-risk-accepted — if a vendor abandons the terminal entirely, its adapter dies, not the system. No crystal-ball engineering; design so the dying part is cheap.
7. #human-is-gate-not-wire — purpose of the build is to remove @majkee from copy-paste relay and return him to the gate (confirm / strike / reject). Relay automation must NOT automate the gate.
8. #sovereignty-gradient-applies — seam protocol and emitted records: sovereign-authored. Adapters: generated-but-committed. Vendor state: never ported.
9. #one-shot-first — first deliverable is a one-shot probe: lead A emits a file, adapter delivers to lead B, B's reply lands as a file. No held-on-line rounds before that beats once. (Costa protocol precedent.)
10. #count-before-build — count current manual relays per session (how many, how long, where they fail) before writing the adapter. Rate = signal for whether the seam earns its maintenance.

## Shape (sketch only)
```
[Claude Code lead] ←adapter-cc→  _bus/  ←adapter-cx→ [Codex lead]
        │  (agent teams,             │                   │ (native spawn,
        │   own sub-agents)     git-tracked md            │  own sub-agents)
        └─────────── @majkee reads _bus/, gates ──────────┘
```
- `_bus/` = existing file plane (BUS/STATUS/POINT/VERDICT vocabulary reused; no new file kinds).
- Adapter interface (both sides): `deliver(file) → session`, `collect(session) → file`. Nothing else.
- Candidate transports today: cc = agent-teams tmux path or send-keys; cx = `codex queue` or `codex mcp-server`; both fall back to send-keys.

## Brakes
- Do NOT build a scheduler, a pane manager, or a UI.
- Do NOT reach inside a vendor half (no sub-agent orchestration from the seam).
- Do NOT add a file kind; extend `_bus/` vocabulary only via metadata labels.
- Do NOT start before axiom-strike + countersign from Asymmetry + relay count (axiom 10).

## Rejected options (rationale logged)
- **Adopt one vendor's teaming as the whole system** — rejected: covers half the army; locks the seam to a vendor.
- **Full PTY/tmux orchestration layer (original intent)** — rejected as *plumbing*; retained only as floor (#5).
- **MCP-only bridge (Codex as MCP server called from Claude, or vice versa)** — parked, not rejected: one-directional, new session per call, no streaming; may serve as one adapter implementation, not as the seam.
- **Human continues as relay** — rejected on cost: slows work, spends judgment on keystrokes, scales badly with task difficulty.

## Open items
- Whether file emission is enforced *at the seam* (adapter refuses to deliver without a record) or *inside each half* (lead's own instructions). Symmetry leans seam.
- Read-back: how each adapter detects "lead finished a turn" without polling pane text (bell? file touch? vendor hook?).
- Whether `turn:` metadata label (already accepted) is sufficient to thread a relay exchange, or whether a `relay:` label is needed.
- Vendor drift monitoring: what minimal signal tells @majkee an adapter has rotted (health probe on session start?).
- Epistemic fork (parked, not for this brief): what the human role is once relay is automated. Working answer: gate.

## Countersign request → asymmetry
See `consult.relay-seam.asymmetry.2026-09-11.md`. Not a blind loop — peer consult. Disagree freely.
