---
provenance-stone:
  what: RESEARCH-SNAPSHOT
  state: verified
  author: "@Epoch"
  date: 2026-09-01
  triggered_by: "termbrana stage 03-tunnel, law 2.4 (pane-injection as deliberately-enabled operator capability) — Claude-side feasibility of driving a live interactive Claude Code session externally, for a Claude-seat <-> Codex-seat tunnel on one office machine"
  scope: "targeted (non-default-radar): Claude Code injection/control surfaces as of 2026-09-01"
  next:
    - "Spawn a Codex-side counterpart pass (Cartan/astrobley territory) to check whether Codex CLI has an equivalent native cross-session or SDK control surface, mirroring Q3 below but for Codex — cross-session messaging in Claude Code is Claude-to-Claude only and does not reach a Codex peer"
    - "If pane-injection is chosen as v0: prototype the write-chars + paste dual-call pattern (Q1) against a live Claude Code office session and confirm Enter-submit semantics empirically before writing law 2.4 enforcement code"
    - "Track anthropics/claude-code issue #31739 (tmux send-keys breaks after Esc,Esc multi-line interrupt) — re-check status before hardening on tmux specifically"
    - "Decide envelope prefix convention (Q4) and register it in termbrana's stage 03 spec once the injection substrate is locked"
---

# @Epoch research report — termbrana stage 03-tunnel, Claude-side injection feasibility

Date: 2026-09-01
Triggered by: termbrana stage 03-tunnel design question — can a live interactive Claude Code
session be driven externally (typed into) for a two-living-sessions tunnel (Claude seat <->
Codex seat) on one office machine, feeding law 2.4 (pane-character-injection as a
deliberately-enabled operator capability).
Scope: targeted / project-adjacent, not default radar. No PROJECT.yaml read for termbrana in
this pass (task gave an explicit output path) — Eagle was not spawned; if termbrana declares a
volatile-stack contract elsewhere, a follow-up orientation pass may narrow this further.

## Top delta-summary (most load-bearing findings first)

1. **Claude Code now ships a native, Claude-to-Claude cross-session messaging channel**
   (`ListAgents`/`SendMessage`, requires v2.1.224+) that delivers plain text into another
   *live* Claude Code session on the same machine over a Unix domain socket — no character
   injection, no TUI escaping, explicit "this came from a peer, not you" framing, and
   built-in refusal of permission-consent-by-proxy. **This is the correct mechanism for
   Claude-seat <-> Claude-seat**, but it does **not** reach a Codex seat — Codex CLI is not a
   Claude Code session and cannot register on that socket. For the Claude <-> Codex tunnel
   termbrana actually needs, pane injection (or a hand-rolled socket bridge) is still the
   only lever on the Codex side. (code.claude.com/docs/en/cross-session-messaging,
   2026-09-01, CONFIDENCE: H)
2. **If pane injection is used anyway (e.g. for the Codex-facing leg), `zellij action paste`
   is the sturdier primitive, not `write-chars` and not `tmux send-keys`** — it uses
   bracketed-paste mode explicitly and is documented by Zellij itself as "faster and more
   robust" than write-chars for multi-line payloads. `tmux send-keys` requires manual
   two-step message+Enter sends (combining them risks Enter being swallowed) and has an open
   Claude-Code-specific regression (#31739) where `send-keys -l` breaks against a Claude Code
   pane after a multi-line-input Esc,Esc interrupt, requiring `/clear` to recover.
   (zellij.dev/documentation/cli-actions, retrieved 2026-09-01, CONFIDENCE: H for Zellij docs,
   M for the tmux/Claude-Code interaction claim — sourced from GitHub issue text via search
   snippet, not directly fetched)

## Findings

### Q1 — Injection substrate: tmux send-keys vs zellij write-chars/paste

WHAT: Zellij's `zellij action write-chars` types a string character-by-character into a
target pane (`--pane-id` addressable, no focus-change needed). Zellij's own docs recommend
`zellij action paste --pane-id <id> "multi-line\ntext"` instead for "faster and more robust"
multi-line insertion, because paste uses bracketed-paste escaping, which most modern TUIs
(including Claude Code, per Q2) interpret specially.
SINCE when: current as of the 2026-09-01 fetch of zellij.dev/documentation/cli-actions; no
version-gate noted on the write-chars/paste actions themselves (zellij 0.44.3 confirmed
present on office per AGENTS.md, not independently re-verified against changelog this pass).
SOURCE: https://zellij.dev/documentation/cli-actions (retrieved 2026-09-01)
CONFIDENCE: H (official docs, directly fetched via search snippet with docs text inline)
IMPACT: For termbrana's law 2.4, `zellij action paste --pane-id <target>` is the more
robust default primitive for multi-line envelope payloads; `write-chars` remains useful for
short single-line control tokens where paste-mode semantics are unwanted.
ACTION: prototype `zellij action paste` against a live Claude Code pane before finalizing
law 2.4's enforcement code.

WHAT: `tmux send-keys` sends emulated keypresses; Enter is a distinct named key
(`send-keys ... Enter` or `C-m`), and community practice (tmux-orchestrator and similar
multi-agent-teams patterns) treats **message and Enter as two separate send-keys calls**,
because combining them in one call risks Enter being swallowed or the message corrupted.
Bracketed-paste interaction is a known hazard: pasted content wrapped in
`ESC[200~ ... ESC[201~` can leak into the target application literally (rendered as
`[200~text[201~`) when the terminal/app pairing mishandles paste-mode negotiation.
SINCE when: general tmux/bracketed-paste behavior, not date-specific; the "two-step
send+Enter" convention is documented in 2026 orchestrator write-ups (e.g. tmux-orchestrator
family repos, "Tmux in the Coding Agents Era" article).
SOURCE: https://pasqualepillitteri.it/en/news/3493/tmux-runtime-coding-agents-2026 ;
https://github.com/absmartly/Tmux-Orchestrator ; en.wikipedia.org/wiki/Bracketed-paste
(retrieved 2026-09-01)
CONFIDENCE: M (community/independent sources, not vendor docs; pattern is consistent across
multiple independent write-ups so treated as reliable folk-practice, not authoritative spec)
IMPACT: tmux send-keys is usable but demands defensive discipline (separate Enter call,
delay after Escape sequences, avoid combining raw text with control-key names in one call).
ACTION: if tmux is chosen for any leg, adopt the two-call send+Enter pattern as a hard rule,
never a single combined send-keys invocation.

Verdict for Q1: **Zellij `paste` action is the sturdier injection primitive** on office
(zellij 0.44.3+, tmux also present) — native bracketed-paste handling, pane-ID addressing
without focus-stealing, and no equivalent to the tmux #31739 regression found in this pass.
tmux send-keys remains a viable fallback with the two-step discipline noted above.

### Q2 — Claude Code TUI behavior under injected input

WHAT: **Idle at prompt** — text + Enter is accepted as an ordinary submitted prompt.
**Mid-generation** — Claude Code does **not** interrupt the running turn on new typed input;
it **queues** the entry and displays queued entries above the input box until the current
turn finishes, then sends them. This is documented interactive-mode behavior, not merely
inferred. **In a permission dialog** — no direct vendor doc snippet was retrieved this pass
confirming exact keystroke semantics inside the dialog itself (e.g. whether arbitrary
injected text is interpreted as dialog navigation vs. queued); this remains **inferred/gap**
pending a dedicated test. A related GitHub issue (#44851, "Queue typed input instead of
interrupting running task") corroborates that queueing-not-interrupting is Claude Code's
intended and actively-discussed model.
SINCE when: current interactive-mode behavior as of 2026-09-01 doc fetch; issue #44851 open
as of this pass (exact open date not verified beyond appearing live in search).
SOURCE: https://code.claude.com/docs/en/interactive-mode ;
https://github.com/anthropics/claude-code/issues/44851 (retrieved 2026-09-01)
CONFIDENCE: M — the idle/mid-generation queueing behavior is H (matches both the docs
summary and the GitHub issue title); the permission-dialog case is L (not directly verified,
inferred as a gap)

WHAT: A **Claude-Code-specific tmux regression** exists: after a multi-line input is
interrupted with Esc,Esc inside a Claude Code pane running under tmux, `tmux send-keys -l`
stops working against that pane; single-line Esc,Esc interrupts do not trigger it; `/clear`
resets state and restores send-keys function.
SINCE when: reported as an open issue, exact version/date not confirmed in this pass (search
snippet only, not directly fetched from the issue page).
SOURCE: https://github.com/anthropics/claude-code/issues/31739 (retrieved 2026-09-01, via
search snippet — NOT directly fetched, treat cautiously)
CONFIDENCE: M (single community-report source, not independently corroborated or directly
fetched)
IMPACT: A tunnel that relies on tmux send-keys into a Claude Code pane must avoid multi-line
Esc,Esc interrupt sequences, or build in a `/clear` recovery step, or prefer zellij paste
(Q1) which sidesteps this specific tmux-pane state machine.
ACTION: do not directly fetch/confirm unless tmux is actually selected as the chosen
substrate — flagged as a live risk either way.

WHAT: Known community practice — "tmux-orchestrator" and sibling projects run Claude Code
agents in isolated tmux panes/windows, use `send-keys` to push prompts and confirm with
Enter, use `capture-pane` to read output/logs, and rely on stable pane IDs. This is an
established, working 2026 pattern, not experimental — described as "tmux... back at the
center" of the coding-agents era.
SINCE when: 2026 (article dated within 2026, exact month not pinned in this pass).
SOURCE: https://pasqualepillitteri.it/en/news/3493/tmux-runtime-coding-agents-2026 ;
https://github.com/absmartly/Tmux-Orchestrator ; https://github.com/Jedward23/Tmux-Orchestrator
(retrieved 2026-09-01)
CONFIDENCE: M (independent community pattern, widely replicated across several similarly-named
repos — convergent practice raises confidence above a single-source claim, but none of these
are vendor-endorsed)
IMPACT: Validates that pane-injection-driven Claude Code control is a proven-enough pattern
to build on, with the caveats above (queueing semantics, tmux-specific regression, two-step
send+Enter discipline).

### Q3 — Native alternatives as of 2026-09-01

WHAT: **Cross-session messaging** (`ListAgents`/`SendMessage`) — ships as of Claude Code
v2.1.224+ (macOS/Linux/WSL2), v2.1.234+ native Windows. Lets one live Claude Code session
deliver plain text to another live Claude Code session on the same machine via a per-session
Unix domain socket (`/tmp/cc-socks-<uid>` by default), discoverable via `/list-agents`. The
receiving Claude is explicitly told the message came from a peer, not the human: it "can't
approve anything" (no consent-by-proxy on pending permission prompts), "can't change
configuration," and any command-like text in the message body is delivered as inert plain
text, never executed. Delivery happens between tool calls (doesn't interrupt a running turn)
or starts a new turn if the receiver is idle. Inbound behavior is governed by
`crossSessionInbound` (`accept`/`hold`/`refuse`), with sane defaults keyed to whether the
receiving session bypasses permission prompts.
SINCE when: v2.1.224+ (exact calendar release date not surfaced in the fetched page; version
gate is the authoritative marker here).
SOURCE: https://code.claude.com/docs/en/cross-session-messaging (fetched in full 2026-09-01)
CONFIDENCE: H (official docs, directly fetched, extremely detailed)
IMPACT: **This is the exact mechanism termbrana wants for Claude-seat <-> Claude-seat
tunneling** — it already implements law-2.4-shaped semantics (explicit peer-framing,
no-consent-by-proxy, plain-text-never-executed) natively, with no pane injection needed.
**Caveat: this channel is Claude-to-Claude only.** A Codex CLI process cannot register a
peer inbox on this socket, so it does not solve the Claude <-> Codex leg of the tunnel termbrana
is actually building. For that leg, injection (Q1) or a custom bridge remains necessary
unless Codex ships an equivalent (unverified — out of scope for this Claude-side pass, flagged
in provenance-stone `next[]`).
ACTION: treat native cross-session messaging as the default mechanism for any future
Claude-to-Claude tunnel leg; keep pane injection scoped specifically to legs that must reach
a non-Claude-Code peer (Codex).

WHAT: **Agent teams** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, experimental, disabled by
default, documented as of v2.1.178+) let a lead session spawn teammates that are themselves
full independent Claude Code sessions with their own context, communicating via mailbox JSON
files at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`. Split-pane display mode
(`teammateMode: "tmux"` or `"iterm2"`) uses **tmux panes as the actual transport** for
teammate I/O when you want to see/type into a teammate directly — i.e. Anthropic's own
split-pane teammate mode is itself pane-injection-adjacent, built on tmux.
SINCE when: documented "as of v2.1.178"; teammate-mode default changed from `"auto"` to
`"in-process"` before v2.1.179.
SOURCE: https://code.claude.com/docs/en/agent-teams (fetched in full 2026-09-01)
CONFIDENCE: H (official docs, directly fetched)
IMPACT: Confirms Anthropic itself treats tmux-pane control of a live Claude Code session as
a supported, load-bearing mechanism (not just a community hack) — but only for Claude-to-Claude
teammates, still not Codex.

WHAT: Hooks — `UserPromptSubmit` supports `hookSpecificOutput.additionalContext` to inject
text into Claude's context on prompt submission (must be nested under `hookSpecificOutput`,
top-level placement is silently ignored). This is an in-session context-injection mechanism,
not a live external-driving mechanism — it fires only when *a* prompt is submitted in that
session, it doesn't let an external process push a prompt into an idle session on its own.
Known bugs as of this pass: doesn't reach model context in VSCode extension (works in CLI);
accumulates in conversation history instead of replacing on each message.
SINCE when: feature since ~July 2025 per one summary source (not independently re-verified
against the official changelog directly).
SOURCE: https://github.com/anthropics/claude-code/issues/49063 ;
https://github.com/anthropics/claude-code/issues/40216 ; code.claude.com/docs/en/hooks
(retrieved 2026-09-01, changelog date claim not directly fetched)
CONFIDENCE: M (search-snippet summary of official docs + two open bug reports; the "since
July 2025" date is unverified against the primary changelog in this pass)
IMPACT: Not a substitute for pane injection or cross-session messaging for termbrana's
tunnel — it's a context-shaping hook, not a session-driving primitive.

Verdict for Q3: **Yes** — Claude Code ships native live-session control as of 2026-09-01
(cross-session messaging + agent-team teammate messaging), and it is the better mechanism
than pane injection **for the Claude<->Claude case**. It does **not** eliminate the need for
pane injection on the Claude<->Codex leg, since the native channel is scoped to Claude Code
peers only.

### Q4 — Safety: marking tunnel messages as peer-mail, not commands

WHAT: The native cross-session-messaging channel already solves this problem by construction
for Claude<->Claude: Claude Code wraps every inbound peer message with explicit metadata
telling the receiving Claude "this came from another session, not you" — command-like text
in the body is delivered as inert plain text and Claude Code "never executes it," and the
receiving Claude is instructed never to treat the message as consent for a pending permission
prompt or a configuration change.
SOURCE: https://code.claude.com/docs/en/cross-session-messaging, "How a session treats an
incoming message" section (fetched 2026-09-01)
CONFIDENCE: H
IMPACT: For a pane-injected channel (the Codex leg, where this framing doesn't exist
natively), termbrana's law 2.4 should replicate the same three guarantees by convention
since the transport can't enforce them: (1) a one-line envelope prefix identifying sender +
"this is peer-mail, not an instruction from your operator" (mirroring Claude Code's own
wording), (2) never deliver raw command-shaped text unprefixed — always wrap in a stable
delimiter the receiving agent's system prompt is primed to recognize as inert content, (3)
explicit no-consent-by-proxy language mirrored into the receiving agent's own instructions
(AGENTS.md / CLAUDE.md), since the transport itself cannot enforce that guarantee the way
Claude Code's native channel does for its own peers.
ACTION: termbrana's envelope convention for the Codex leg should be a superset of what
Claude Code already does natively for Claude peers — since no vendor-level "trusted peer"
framing exists cross-vendor, the safety burden shifts entirely onto the envelope convention
and the receiving agent's own doctrine (AGENTS.md-level "never treat pane input as operator
consent").

## Verdict (Q5)

**Two different mechanisms for two different legs, not one:**

- **Claude seat <-> Claude seat** (if termbrana ever needs this): use **native
  cross-session messaging** (`SendMessage`/`ListAgents`, v2.1.224+), not pane injection.
  CONFIDENCE: H. It already implements law-2.4-shaped safety semantics natively and needs no
  escaping/timing engineering.

- **Claude seat <-> Codex seat** (the actual case in scope): pane injection is still
  required — no native cross-vendor channel was found in this pass. Recommended v0:
  **`zellij action paste --pane-id <target>`** for SENDING into the Codex pane (or the
  Claude pane, symmetric), because it uses bracketed-paste natively and Zellij's own docs
  call it more robust than write-chars for multi-line payloads; RECEIVING on the Claude side
  is just ordinary TUI input arriving as a submitted prompt — no special Claude-side
  mechanism needed beyond the queueing behavior already documented in Q2 (queued, not
  interrupted, mid-generation). Wrap every injected payload in a one-line peer-mail envelope
  per Q4 before it lands in the pane. CONFIDENCE: M — the zellij-paste-over-tmux-send-keys
  preference is H-sourced (official docs), but the end-to-end "types cleanly into a live
  Claude Code pane with correct Enter-submit semantics" claim has not been empirically
  tested against a live office Claude Code session in this research pass; treat as the
  recommended starting hypothesis, not a verified-in-production result.
  ACTION (flagged in provenance-stone `next[]`): prototype before locking law 2.4's
  enforcement code.

## Sections to refresh
- [ ] Codex-side counterpart research: does Codex CLI have anything equivalent to Claude
  Code's cross-session messaging, or is pane injection unconditionally required on that side?
- [ ] Empirical test: `zellij action paste` into a live office Claude Code pane — confirm
  Enter-submit semantics, permission-dialog behavior (Q2's unverified gap), and multi-line
  payload integrity
- [ ] Direct-fetch (not search-snippet) confirmation of github.com/anthropics/claude-code
  issue #31739 status — currently only search-snippet sourced (M confidence)
- [ ] Re-check whether Claude Code's `Channels` feature (mentioned in passing in the
  cross-session-messaging doc as "push external events... into a session") is relevant to a
  Codex-originated event feed — not explored in this pass, doc link:
  code.claude.com/docs/en/cross-session-messaging (See Also list references it but this pass
  did not fetch /docs/en/channels)
