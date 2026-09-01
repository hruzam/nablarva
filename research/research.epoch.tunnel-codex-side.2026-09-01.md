---
stone: provenance
type: research-report
agent: "@Epoch"
date: 2026-09-01
triggered_by: "termbrana stage 03-tunnel — Codex-side receive/send mechanism for a two-living-sessions Claude<->Codex tunnel on one machine"
scope: "generic Codex CLI landscape (not project-contract-narrowed; no PROJECT.yaml consulted for termbrana in this run)"
codex_version_verified_current: "0.152.0 (Sept 1 2026, per GitHub Releases)"
confidence_legend: "H = official changelog/docs/repo source · M = reliable commentator/aggregator · L = inferred/indirect"
---

# @Epoch research report
Date: 2026-09-01
Triggered by: termbrana stage 03-tunnel — can a live interactive Codex CLI session (0.150+, ChatGPT-account auth) be driven externally for a two-living-sessions Claude<->Codex tunnel on one machine?
Scope: default radar (Codex CLI substrate). Not project-contract-extended — I did not read termbrana's PROJECT.yaml this run; if termbrana pins a specific Codex version/config, re-run with `eagle` first to confirm it matches 0.152.0.

## TOP-LINE DELTA (read this first)

**The official Codex-side answer as of 2026-09-01 is: no live two-way co-presence with a Codex TUI exists or is planned-and-shipped. The vendor's own cross-runtime bridge (`openai/codex-plugin-cc`, the official Codex plugin for Claude Code) is explicitly headless, request/response, sequential — not two simultaneously-live sessions.** An RFC for TUI co-presence (multi-subscriber live thread fanout) was filed, prototyped, and closed without shipping. `codex mcp-server` was deprecated Aug 24 2026 in favor of `app-server`, which is real, documented, and JSON-RPC-based — but its "live" attach story is resume-a-stored-thread-and-continue, not observe/steer-a-running-TUI-turn concurrently. For termbrana's stage 03, this pushes the v0 mechanism toward **app-server headless invocation** (spawn/resume a Codex thread as a controlled subprocess, no TUI in the loop) rather than PTY injection into a live interactive Codex TUI, and rather than assuming a shipped co-presence primitive.

## Findings (most recent first)

---
WHAT: Official Codex↔Claude Code bridge exists and is headless-delegation-only, not live pairing.
SINCE: repo `openai/codex-plugin-cc`, referenced in Aug 24 2026 mcp-server deprecation notes as "the" recommended path from Claude Code to Codex; README undated in fetched content but active as of query date 2026-09-01.
SOURCE: https://github.com/openai/codex-plugin-cc/blob/main/README.md ; cross-ref https://developers.openai.com/codex/changelog/
CONFIDENCE: H (primary repo README, official OpenAI channel)
IMPACT: This is the closest thing to a "sanctioned" Claude↔Codex tunnel precedent, and it rules out expecting a shipped two-live-sessions primitive. Model: Claude Code issues `/codex:review`, `/codex:rescue`, etc. → spawns Codex work via local app-server → runs to completion or backgrounds → `/codex:status` / `/codex:result` poll/retrieve. `/codex:transfer` hands a Claude Code conversation into a *new persistent Codex thread* the user can then open interactively — sequential handoff, not simultaneous bidirectional live communication.
ACTION: termbrana stage 03 should not scope for "both sides live and interactively steering each other in real time" as a supported vendor pattern. Scope for delegate-and-poll (app-server driven) as the reliable v0, with an optional PTY-injection escape hatch for cases needing an actual visible interactive Codex TUI pane.

---
WHAT: RFC for external "peer-client co-presence with a live TUI thread" was filed, had a working proof-of-concept, and closed without becoming a shipped capability.
SINCE: opened 2026-05-07; closed (date of close not captured in fetch, but no merge indicated).
SOURCE: https://github.com/openai/codex/issues/21551
CONFIDENCE: H (primary GitHub issue, direct maintainer/author commentary quoted: "an additional observer did not reliably receive a normal TUI-originated turn stream")
IMPACT: Confirms directly: as of today, attaching a second client to an *already-running* interactive Codex TUI session to read its live event stream and steer turns is NOT reliable / NOT a supported capability, even though a patch branch exists. The RFC explicitly scoped this local-only (not exposing app-server WebSocket to the network) — so even the aspirational design was single-machine, matching termbrana's use case, but it isn't shipped.
ACTION: Do not build stage 03 assuming co-presence lands soon. Treat it as an unfinished experimental path; if wanted later, track issue #21551 for reopening/merge.

---
WHAT: `codex mcp-server` is deprecated; `app-server` is the recommended programmatic surface going forward, with a runtime deprecation warning added.
SINCE: deprecation announced 2026-08-24; warning-emitting PR: https://github.com/openai/codex/pull/39657
SOURCE: https://developers.openai.com/codex/changelog/ (per WebSearch synthesis); PR #39657 title "Warn when launching the deprecated MCP server"
CONFIDENCE: H (changelog + PR title, both primary)
IMPACT: Any tunnel design that assumed `codex mcp-server` as the live-control surface is building on a surface the vendor is actively steering users away from as of 8 days before this report. app-server is the forward-compatible choice.
ACTION: If termbrana's existing research assumed MCP-server-as-control-surface, flag that card for refresh.

---
WHAT: App-server protocol confirmed: JSON-RPC 2.0 over stdio (default) / WebSocket / Unix socket; `thread/start`, `thread/resume`, `thread/fork`, `turn/start`, `turn/steer` (adds input to an in-flight turn without starting a new one), `turn/interrupt`, streaming via `turn/started`/item-deltas/`turn/completed`.
SINCE: current as of fetch 2026-09-01; codified in `codex-rs/app-server/README.md` on the `main` branch.
SOURCE: https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md (fetched via raw.githubusercontent.com mirror; official docs mirror at https://learn.chatgpt.com/docs/app-server confirms positioning but not co-presence)
CONFIDENCE: H (primary repo source for the protocol shape); M for the "positioned as primary programmatic interface" framing (paraphrased from docs prose, not a literal deprecation clause naming mcp-server)
IMPACT: `turn/steer` is the operationally interesting primitive for termbrana — it is the officially sanctioned way to inject text into an **already-running turn** without racing the paste-burst/newline hazards of PTY character injection. This is real "external control of a live Codex process," just not of a live *TUI-rendered* process — app-server-driven threads are headless by default; a TUI can *also* attach to the same thread via `thread/resume`, but concurrent dual-attach hits the RFC #21551 limitation above.
ACTION: Design stage 03 v0 around app-server `thread/start` + `turn/steer` + `turn/interrupt` against a headless Codex thread, not against a rendered Codex TUI pane.

---
WHAT: PTY/tmux character-injection hazard analogous to the heredoc column-0 fragility already known in the wrapper world: Codex TUI's paste-burst detector (3+ chars within 8ms = "paste-like") suppresses Enter-as-submit for a 120ms window; `tmux send-keys -l <text>` immediately followed by `tmux send-keys Enter` lands the Enter inside that suppression window and is swallowed as a newline instead of submitting — so naive two-command injection can never submit.
SINCE: issue активность recent (2026, exact date not isolated from search snippet); documented via GitHub issues #21699 ("Shift+Enter is not recognized inside tmux"), #2376 (earendil-works/pi, "multi-line paste submits on first newline inside tmux"), and PR #21943/#24371 (tmux csi-u / modifyOtherKeys fixes).
SOURCE: https://github.com/openai/codex/issues/21699 ; https://github.com/earendil-works/pi/issues/2376 ; https://github.com/openai/codex/pull/21943 ; https://github.com/openai/codex/pull/24371
CONFIDENCE: M (WebSearch-synthesized across multiple issues; individual issue text not independently fetched line-by-line this run — recommend a follow-up fetch of #21699 directly before committing termbrana's injection-timing constant to a spec)
IMPACT: If termbrana's v0 falls back to PTY injection at all (e.g., for a visible Codex TUI pane), the concrete mitigation is a >120ms sleep between the text `send-keys -l` and the Enter `send-keys`, mirroring the delay discipline already known for heredoc-adjacent tools. This is a genuine, named, TUI-specific hazard — not hypothetical.
ACTION: If PTY injection is used anywhere in stage 03 (even as escape hatch), hardcode a ≥150ms gap between text-send and Enter-send, and treat rapid multi-line paste as unsafe without it.

---
WHAT: A second, broader hazard class named directly by a Codex maintainer-facing issue: local terminal injection generally has "text landing in the draft without submitting," "injected text racing with a human actively typing," and "ad hoc attribution/dedupe/replay" — the maintainers' own framing for why app-server-style session semantics are preferred over PTY emulation.
SINCE: issue opened 2026-03-20, appears still open/unresolved as of this run.
SOURCE: https://github.com/openai/codex/issues/15355
CONFIDENCE: H (primary issue text, quoted directly by the fetch)
IMPACT: This is the vendor's own diagnosis that PTY/tmux injection into Codex is a known-fragile pattern, not a Claude-side or termbrana-side design flaw to work around quietly — it validates prioritizing app-server over pane injection wherever the workflow allows headless operation.
ACTION: Cite this issue in termbrana's stage 03 card as the canonical justification for choosing app-server-first design.

---
WHAT: Codex-native subagents (multi_agent / multi_agent_v2) are opt-in, unstable, and actively landmine-ridden; conflicting community reports on GA status could not be fully reconciled this run.
SINCE: multi_agent_v2 opt-in via `[features]` in `~/.codex/config.toml` or `/experimental`; one commentary source claims subagents "became generally available in March 2026, graduating from feature-flag preview to stable default" and "multi-agent v2 stabilized in v0.145.0" — but a live, still-open bug (#36294, opened 2026-07-31, Codex Desktop 26.727.40816 / bundled CLI 0.146.0-alpha.9.2) shows `spawn_agent` still validating against a stale static catalog value even when the runtime feature flag is enabled, producing a misleading "Unknown model" rejection. Other open issues (#31097 "GPT-5.5 forces MultiAgentV2 despite disable," #31814 "GPT-5.6 Sol cannot specify subagent models, forcing all subagents to [default]") corroborate ongoing instability into the same window.
SOURCE: https://github.com/openai/codex/issues/36294 ; https://github.com/openai/codex/issues/27331 ; https://github.com/openai/codex/issues/31097 ; https://github.com/openai/codex/issues/31814 ; commentary (M-tier, not independently confirmed against an official changelog this run): https://codex.danielvaughan.com/2026/05/03/codex-cli-multiagentv2-custom-roles-thread-orchestration-parallel-workflows/
CONFIDENCE: M overall (the "GA in March 2026" and "stabilized in v0.145.0" claims are third-party commentary, NOT confirmed against an official OpenAI changelog entry in this run — flagging per the task's own note that a prior delta sheet could not confirm v2 status in the current config reference). The open-bug evidence (#36294 etc.) is H — primary GitHub issues.
IMPACT: A live Codex architect seat tasking its own Codex subagents today should NOT be assumed reliable. Known landmines found this run: (a) static-catalog vs. runtime-flag mismatch causing valid children to be rejected (#36294); (b) forced model selection overriding explicit per-subagent model config (#31097, #31814) — i.e. model-override landmine confirmed; (c) fork/depth-specific issues were referenced in aggregate commentary but not independently verified against a primary source this run (L-confidence, do not cite as fact without follow-up).
ACTION: Treat Codex-native multi-agent as experimental-with-known-bugs for termbrana's purposes; do not depend on it for stage 03's Codex-side orchestration. If termbrana needs Codex-side parallelism, prefer multiple independent app-server threads driven externally over relying on Codex's own subagent spawner. Recommend a follow-up @Epoch or @field pass specifically on the official OpenAI Codex changelog (not third-party commentary) to pin the true GA/version status of multi_agent_v2 before any spec commits to it.

---
WHAT: Community cross-runtime pairing precedent landscape (Aug–Sep 2026): tmux remains the dominant substrate for running Claude Code and Codex CLI side by side, but every found project is orchestration/dispatch (one side spawns/monitors/messages the other from outside), not a peer-to-peer live-TUI-to-live-TUI tunnel.
SINCE: ongoing ecosystem as of query date 2026-09-01; no single dated release identified as authoritative for "current."
SOURCE: https://github.com/awslabs/cli-agent-orchestrator (AWS "CAO," coordinates Claude Code, Kiro, Codex in isolated tmux sessions) ; https://github.com/kingbootoshi/codex-orchestrator (Claude Code spawns/monitors/messages Codex via tmux) ; https://github.com/bradAGI/awesome-cli-coding-agents (directory) ; https://github.com/hesreallyhim/awesome-claude-code/issues/1279 (tmux-orchestrator proposal)
CONFIDENCE: M (WebSearch synthesis across multiple repos; individual repo internals not independently fetched this run)
IMPACT: No community precedent was found running two genuinely co-equal *live interactive* sessions (both TUIs concurrently steerable by a human or by each other) — every pattern found is hierarchical dispatch, matching the vendor's own official plugin shape. This corroborates the top-line delta rather than contradicting it.
ACTION: If termbrana wants a stronger precedent search (e.g. specifically "Codex TUI receiving injected turns while a human/Claude drives the pane live"), that needs a dedicated @field or @zenith grind across the awesome-lists' individual repos — out of scope for this pass's source budget.

## Answers to the five numbered questions (compressed)

1. **TUI injection hazards:** Real and named by the vendor. Paste-burst detector (3 chars/8ms triggers "paste mode," 120ms Enter-suppression window) is the direct analog to heredoc column-0 fragility — `tmux send-keys -l` + immediate `send-keys Enter` gets swallowed. Mitigation: ≥120ms (use 150ms for margin) delay between text and Enter sends. Vendor's own issue #15355 additionally names draft-without-submit, injection-racing-human-typing, and no attribution/dedupe/replay as systemic PTY-injection weaknesses — this is why they're building app-server instead. CONFIDENCE H.

2. **Official programmatic live-session surfaces:** `codex app-server` is real, documented, JSON-RPC 2.0 (stdio/WebSocket/Unix socket), with `thread/start|resume|fork`, `turn/start|steer|interrupt`. It supersedes `codex mcp-server`, deprecated 2026-08-24. It does NOT reliably support a second client co-observing/steering an *already-running TUI* thread concurrently — that capability (RFC #21551) was prototyped and closed unshipped. So: app-server makes pane injection unnecessary for headless Codex control, but does NOT yet make it unnecessary for controlling a Codex process that is simultaneously rendering its own interactive TUI. `codex exec resume --last` works for sequential (not concurrent) session continuation. CONFIDENCE H.

3. **Multi-agent status:** Cannot fully confirm GA/v2 status from an official changelog this run (flagged, matches the prior delta sheet's inconclusiveness) — third-party commentary claims GA March 2026 / stabilized v0.145.0 (M-confidence only). Live open bugs as of Jul–Aug 2026 show real landmines: static-catalog-vs-runtime-flag mismatches rejecting valid children, and forced-model-override ignoring explicit subagent model config. Do not build on Codex-native subagents as a reliable primitive today. CONFIDENCE M (bugs are H, GA claim is M/unconfirmed).

4. **Cross-runtime precedent:** All found Aug–Sep 2026 patterns (AWS CAO, codex-orchestrator, and OpenAI's own official `codex-plugin-cc`) are hierarchical/dispatch-based via tmux or app-server, none are peer live-TUI-to-live-TUI. CONFIDENCE M.

5. **Verdict — recommended v0 mechanism:**
   - **Codex-side RECEIVING:** app-server `turn/start` / `turn/steer` against a headless Codex thread (no rendered TUI). This sidesteps every PTY hazard in finding 1 and matches the vendor's own recommended pattern (finding re: mcp-server deprecation + issue #15355). CONFIDENCE H that this is the safer path; M that it fully satisfies "two LIVING sessions" framing, since a headless app-server thread is not the same experiential object as a live rendered Codex TUI — clarify with termbrana whether "living" requires a visible, human-legible Codex TUI or just a live, steerable process. If a visible TUI is required, fall back to PTY injection with the ≥150ms Enter-delay mitigation, accepting the draft-race/attribution hazards named in #15355 as open risk, not solved risk.
   - **Codex-side SENDING (Codex → Claude seat):** app-server's streaming notifications (`turn/started`, item deltas, `turn/completed`) give a clean read channel for an external process; no injection needed on this leg regardless of receiving-side choice.
   - Net: **app-server-first, PTY-injection-as-explicit-fallback-only**, do not depend on Codex-native co-presence or subagents shipping soon.

## Sections to refresh
- Official OpenAI Codex changelog pass specifically to pin multi_agent_v2 GA/version status (this run relied on M-confidence third-party commentary for that one claim; matches prior delta sheet's stated gap).
- Direct primary-source fetch of GitHub issues #21699 and earendil-works/pi #2376 (this run's paste-burst-timing hazard came from a WebSearch synthesis, not an independent per-issue fetch — worth confirming the exact 8ms/120ms constants against the issue text itself before termbrana hardcodes them).
- A dedicated precedent grind (via @field or @zenith) across the awesome-cli-coding-agents / awesome-agent-orchestrators lists' individual repos, specifically hunting for any project that achieves live TUI-to-TUI co-presence rather than dispatch — this run's search budget only reached the directory/aggregator level.
- Re-run this whole brief through `eagle` against termbrana's actual PROJECT.yaml / stage 03 spec if the project pins a Codex version other than 0.152.0, since this run used default-radar scope only.
