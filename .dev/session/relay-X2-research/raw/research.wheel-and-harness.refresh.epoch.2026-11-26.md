# Research refresh: wheel and vendor-harness (narrow pass on the first pass's open points)

## Header

- Who: @Epoch (researcher seat), second narrow pass. Evidence only; no verdict, no recommendation.
- Date: 2026-11-26. Every "accessed" = 2026-11-26.
- Method: live WebFetch / WebSearch only; read-only; nothing posted; no sign-in. Queries carried no private names or paths. WebFetch returns a small-model summary of a page, not raw bytes; quotes below are the tool's quotations and were not re-checked against raw bytes. "Snippet" = reached only through a search-result summary.
- All points 1-6 were attempted. None skipped.
- Still NOT reached: (a) Codex changelog entries 0.149-0.167 on the OpenAI docs page (the page is truncated; I read 0.167.0 down to 0.172.0 only; 0.149.0 and 0.171/0.172 were read on the GitHub release pages instead); (b) the Codex config-reference page itself (learn.chatgpt.com URL returned 404; reached only via search snippet of developers.openai.com); (c) Claude Code changelog page itself (1.4M chars; dates taken from the GitHub release pages, which show day+month but not the year); (d) agy 1.5.0 exact date (no official source gives one); (e) tmux GitHub issues/PRs: no issue search was possible with these tools, only CHANGES (first 100k of 180k chars) and a search; (f) Herdr's `docs/agents/` page and the agent-manager text after char 100000; (g) Gemini CLI (not asked).

---

## Point 1. OSC 7501 inside tmux

Answer: In the tmux CHANGES file (newest 100k of 180k chars read) there is NO mention of "7501" or "program status". tmux has no format variable, hook or option for OSC 7501 that I could find. Two near neighbours exist: 3.7 "Handle OSC 9;4 progress bar sequence and store in format variables" (names of the variables not given in the text read), and 3.8 (CHANGES section "CHANGES FROM 3.7c TO 3.8", i.e. master, unreleased as far as I can tell) "OSC 133 escape sequences now trigger events: pane-command-started, pane-command-finished and pane-shell-prompt." The spec never mentions tmux or multiplexers. Claude Code's doc says it checks tmux instead of the terminal, but does not say how. OpenTUI (another emitter) does not wrap reports in passthrough, and gives the reason: "The outer terminal cannot tell panes apart or see the program exit, so a `working` record from a pane would never clear."

Quotes:
- CHANGES 3.8: "OSC 133 escape sequences now trigger events: pane-command-started, pane-command-finished and pane-shell-prompt."
- CHANGES 3.7: "Handle OSC 9;4 progress bar sequence and store in format variables (from Eric Dorland in issue 4954)." and "Add ability to forward progress bar to outside terminal (issue 4972 from Eric Dorland)."
- Claude terminal-config: "**tmux**: inside tmux, Claude Code checks tmux for support instead of your terminal, and `allow-passthrough` has no effect on that. Start the session outside tmux."
- Spec (revision history): "2026-10-10 | 0.4"; the page never mentions tmux, screen, multiplexers or passthrough (per fetch summary).
- OpenTUI v0.6.3 notes: "OpenTUI also does not wrap reports in tmux or GNU Screen passthrough."

Links: https://raw.githubusercontent.com/tmux/tmux/master/CHANGES (undated file; versions listed 3.8, 3.7c, 3.7b without dates) · https://code.claude.com/docs/en/terminal-config.md (undated, fetched live) · https://superlogical.com/rex/docs/build/program-status (rev 0.4, 2026-10-10) · https://newreleases.io/project/github/anomalyco/opentui/release/v0.6.3 (page shows "one month ago", no exact date).

Not found: what "asks tmux" means mechanically (the doc does not say; no tmux version, option or query named). Not found after searching: tmux CHANGES (newest 100k chars), a web search for tmux + OSC 7501 + GitHub issue (no tmux/tmux issue returned), the spec text, the Claude doc. Not searched: tmux source code, tmux issue tracker directly, the last 80k chars of CHANGES (older versions).
Mark: PARTLY (tmux-side: NOT FOUND; Claude-side wording: SETTLED as to what the doc says, NOT FOUND as to mechanism).
Accessed 2026-11-26.

Bearing on the first pass: row 25 says the spec "says nothing about tmux/multiplexers": confirmed. Gap 1 in section 5 ("no tmux documentation mentioning OSC 7501"): still stands after this wider search.

---

## Point 2. Codex CLI, official sources

### 2a. `codex queue` first shipped
Answer: 0.149.0, GitHub release page shows "20 Aug" (year not shown on the page; 21:04 published). Consistent with the first pass's 2026-08-20 (row 11) but now from OpenAI's own release page. Semantics from the release notes: "Added `codex queue` for sending messages to existing local or remote sessions." Related bug-fix line: "Queued messages now wake idle sessions reliably, resolve duplicate session names more usefully," and PRs "Dispatch queued messages written by other processes" (#39034), "Prefer the most recent session when queueing by name" (#39385), "Preserve queued TUI input semantics" (#39604). The release page does NOT say whether it targets interactive TUI sessions specifically ("existing local or remote sessions"), and says nothing about delivery acknowledgement.
Link: https://github.com/openai/codex/releases/tag/rust-v0.149.0 · source date 20 Aug (2026 by sequence) · accessed 2026-11-26.
Mark: SETTLED for version/date; PARTLY for semantics (TUI targeting and ack: NOT FOUND in release notes; the `codex queue --help` or a docs page for the command was not located).

### 2b. 0.171.0 and 0.172.0 agent messages
Answer: Both are wording-limited; neither release line names "separate top-level sessions". 0.171.0 (20 Nov): "Acknowledge agent messages and clarify how to wake idle recipients" (#61894). The same release lists subagent items (subagent transcripts, "opt-in item-boundary interrupts for subagents", subagents in the TUI sidebar) but the word "mailbox" does not appear in 0.171. 0.172.0 (24 Nov): "Route injected plaintext agent mail through the native mailbox" (#62292); neighbours: "Interrupting a parent turn preserves queued replies from child agents for the next turn." (#62348), "Keep authorization evidence local to agent forks" (#62314). The surrounding lines speak of "parent turn", "child agents", "agent forks", i.e. a session tree. The notes do not say whether it also reaches a separate top-level session. 0.168.0 (13 Nov, docs changelog): "Route message-board notifications through agent mailboxes." (#59139).
Links: https://github.com/openai/codex/releases/tag/rust-v0.171.0 (20 Nov) · .../rust-v0.172.0 (24 Nov) · https://learn.chatgpt.com/docs/changelog (0.172.0 = 2026-11-24 per the page) · accessed 2026-11-26.
Mark: PARTLY (scope inferred from neighbouring lines about parent/child; PR bodies not read).

Bearing: confirms first-pass row 22 and section 4 line "scope appears to be subagents within a session tree" as consistent but still unproven.

### 2c. Codex official emission of OSC / title / notification
Answer: Official config documentation (reached via search snippet of developers.openai.com/codex/config-reference; the learn.chatgpt.com mirror URL returned 404): `tui.notification_method` values listed as auto, osc9, bel (default auto); `tui.terminal_title`: "Ordered list of terminal window/tab title item identifiers. Defaults to ["spinner", "project"]; null disables title updates." Release 0.168.0 (2026-11-13, docs changelog): "Set `tui.notification_method = "osc777"` for terminal notifications." (the reference page appears to predate osc777). OSC 7501: official repo PRs exist: #52725 "Report terminal program status with OSC 7501" (merged per snippet; emits `app=codex`, idle/working/blocked whenever stdout is a terminal); #54114 (done/error and blocking kinds permission/question/auth, merged per snippet); #57612 (disables OSC 7501 and OSC 21337 on VTE < 0.54). Issue #58136, opened 2026-10-29: request for an opt-out config ("Please add a config option to turn off terminal status reporting (OSC 7501 / OSC 21337)"), so at that date no documented switch. Issue #60296: "Resume paused goal?" prompt reports state=idle while waiting for an answer (closed not planned, per snippet). Third-party: Prowl PR #922 trusts Codex 0.163.0 native OSC 7501; Quay PR #786 notes 0.154.0 does not emit.
Links: https://github.com/openai/codex/pull/52725 · .../pull/54114 · .../pull/57612 · .../issues/58136 · .../issues/60296 · https://developers.openai.com/codex/config-reference (snippet only) · accessed 2026-11-26. PR merge dates not captured. The first emitting release number is not confirmed from an official release page (third-party points to 0.163, first-pass row 23).
Mark: PARTLY (existence in the official repo: SETTLED from PR titles via snippet; config keys for OSC 7501: NOT FOUND; version: NOT FOUND officially).

Contradiction/upgrade of first pass row 23 (L, "secondhand only"): the claim that Codex emits OSC 7501 is now backed by openai/codex PR titles (snippets), not only blogs. The "tui.notifications ... agent-turn-complete, approval-requested" part of row 23 was not re-verified; the doc snippet instead names `notify` (fires only on agent-turn-complete) and `tui.notification_method`.

### 2d. Hooks stable vs experimental; `notify`
Answer: Official hooks page: "Hooks are enabled by default." "Use `hooks` as the feature key." "`codex_hooks` still works as a deprecated alias." The page does NOT say "experimental" or "stable" (per fetch summary). Fourteen events listed: SessionStart, SessionEnd, PreToolUse, PermissionRequest, PostToolUse, PreModelRequest, PostModelRequest, PreCompact, PostCompact, UserPromptSubmit, SubagentStart, SubagentStop, Stop, Interrupt. `notify`: the config-reference/advanced-config snippets describe it as a command receiving a JSON payload, firing only on agent-turn-complete (`notify = ["python3", "/path/to/notify.py"]`); so it still exists as of the snippet; I did not open the page itself.
Links: https://learn.chatgpt.com/docs/hooks (undated, live) · https://developers.openai.com/codex/config-advanced (snippet) · accessed 2026-11-26.
Mark: SETTLED for hooks (no "experimental" label on the official page; the first pass's "conflict" with the README stands, but the official page is silent rather than saying stable); PARTLY for `notify` (snippet only).

---

## Point 3. Claude Code, official sources

### 3a. Status line JSON: any state field?
Answer: NO session-state field (busy/idle/waiting). The documented table lists: model.*, cwd, workspace.*, cost.*, context_window.*, exceeds_200k_tokens, fast_mode, effort.level, thinking.enabled, rate_limits.*, prompt_cache, session_id, session_name, prompt_id, transcript_path, version, output_style.name, vim.mode, agent.name, pr.*, worktree.*. Nearest: `prompt_id` ("UUID identifying the user prompt currently being processed ... Absent until the first user input"). Trigger events listed: new assistant message, `/compact` finishes, permission mode changes, vim toggles, refreshInterval timer, etc. Quote: "It temporarily hides during certain UI interactions, including the help menu and permission prompts."
Link: https://code.claude.com/docs/en/statusline.md (undated, live) · accessed 2026-11-26.
Mark: SETTLED (full table read, lines 182-226 of the fetched copy).
Fills the first pass's header gap ("Claude statusline JSON field list ... NOT verified").

### 3b. `claude agents --json`
Answer: The doc describes it as covering every live session, not only background ones, and the field table includes `kind` = `interactive` or `background`. Agent view carries a research-preview label. The doc also says interactive sessions in other terminals do not appear in the agent-view UI until backgrounded. Both statements are on the same page and are in tension; not tested.
Quotes: "`claude agents --json` prints active sessions as a JSON array and exits: every live session, plus background sessions that are still working or blocked even when their process has exited. Add `--all` to also include completed background sessions, and `--cwd <path>` to limit the list to sessions started under that directory." · "`cwd`, `kind`, `startedAt` | Always | The working directory, `interactive` or `background`, and the start time in Unix milliseconds" · "Agent view is in research preview. The interface and keyboard shortcuts may change as the feature evolves." · "Interactive sessions you have open in other terminals don't appear until you [background them](#from-inside-a-session)."
Link: https://code.claude.com/docs/en/agent-view.md (undated, live; first 100k of 146k chars read) · accessed 2026-11-26.
Mark: SETTLED for wording; whether `--json` actually lists a plain interactive session: NOT tested.
CONTRADICTS first pass: rows 14 and section 4 ("covers backgrounded sessions", "interactive sessions invisible until backgrounded") are only half right. The `--json` sentence says "every live session" and the schema has `kind: interactive`; the "don't appear until backgrounded" sentence is about the list view. Keep both; the first pass noted the ambiguity in row 14 but section 3a/4 stated invisibility flatly. The research-preview label is confirmed.

### 3c. Non-Claude sender into the inbox socket
Answer: The doc names the use case and gives only the auth line, not a message wire format, CLI subcommand or SDK call. Section opens: "Read this section when a session you expect isn't in the agent list, when you want a script or hook to post into a session, or when a sandboxed command can't reach the socket." Text: "A script posting to its own session's socket can send `{"type":"auth","token":"<token>"}` as the first line of its connection ... macOS and Linux, including WSL 2: the line is optional. ... Claude Code closes a connection that hasn't sent a complete line within 30 seconds." Socket path: `CLAUDE_CODE_MESSAGING_SOCKET`, `/tmp/cc-socks-<uid>`, `/status` "Peer address" row prefixed `uds:`; socket restricted to your OS user. Messages on the socket go "through the same inbound controls as any other peer message"; a script that is the session's own child is delivered by default when no `crossSessionInbound` applies; a non-child sender is not covered by that exception ("treats the message like any other that asserts no permission class, so a session that bypasses permission prompts holds it for your approval"). The doc describes "own session's socket" posting; posting to ANOTHER session's socket by a foreign (non-Claude) process is not described. Message body format after the auth line: NOT documented. The "Related" list names Channels for "push external events".
Link: https://code.claude.com/docs/en/cross-session-messaging.md (undated, live; read in full) · accessed 2026-11-26.
Mark: PARTLY (the "script or hook" sentence is quoted above; wire format NOT FOUND in the doc; searched: this page only, plus first-pass reading of the Crosley write-up).

### 3d. Release dates (GitHub release pages; day+month shown, year not shown on the page)
- v2.1.224: "07 Aug 04:00". Line: "Added cross-session `SendMessage`: Claude Code sessions can now message each other, on any of your machines, with `ListAgents` to discover them (macOS and Linux)".
- v2.1.236: "19 Aug 20:02". Line: "Added `notify_when_idle` to cross-session `SendMessage`: ask another Claude Code session on this machine to send one notice when it next goes idle — opt-in, one-shot, no polling (macOS and Linux)".
- v2.1.295: "08 Oct, 19:48". Line: "Added Program Status Protocol (OSC 7501) support: terminals that implement it can show whether Claude Code is working, waiting on you, or done".
Links: https://github.com/anthropics/claude-code/releases/tag/v2.1.224 · .../v2.1.236 · .../v2.1.295 · accessed 2026-11-26. The year (2026) is inferred from sequence (the doc says v2.1.224 shipped in the week Aug 3-7, 2026 per first pass); the changelog page itself was not read.
Mark: SETTLED (day/month from the release pages); year inferred.
Bearing on first pass: row 17/13 previously carried only "week of Aug 3-7" and no date for 2.1.295; the dates now fill these. Note: the release page says Aug 7 for 2.1.224 whereas the first pass says week Aug 3-7: consistent.

---

## Point 4. agy (Antigravity CLI)

### 4a. Hooks event list
Answer: Official hooks page "Supported events" table (six events): `SessionStart` ("Fires once when a new conversation session starts, before the first model invocation."), `PreToolUse` ("Fires before a tool is executed."), `PostToolUse` ("Fires after a tool completes."), `PreInvocation` ("Fires before the model is called."), `PostInvocation` ("Fires immediately after each model invocation completes."), `Stop` ("Fires when execution terminates."). Config: workspace `.agents/hooks.json`; global `~/.gemini/config/hooks.json`; "The file `~/.gemini/antigravity-cli/settings.json` is not loaded for hooks." No compaction, permission-request or session-end event. Changelog: 1.4.11 "hooks can now inject an `errorMessage` whose `userMessage` is shown to you"; 1.5.5 "`PreToolUse`, `PostToolUse`, `Stop`, and startup `SessionStart` hooks are now converted" (conversion context not read).
Link: https://antigravity.google/docs/hooks.md (no date or version on the page) · accessed 2026-11-26.
Mark: SETTLED.

### 4b. Inject into a running interactive agy / poll state from outside
Answer: Injection: NOT FOUND. Headless doc: "`--continue` and `--conversation` ... Each of these starts a new process." and "Use `--input-format stream-json` to maintain a single, continuous conversation process." (only within a process the caller starts). It "doesn't mention a daemon, socket, or remote control." ACP `session/load`: changelog 1.5.15 "replying to `session/load` before finishing history replay"; "attaching to a running session" was cited by the first pass; attach semantics for an interactive TUI not documented in what I read. Polling: YES a state source exists inside the TUI process, via the status-line script: the official status-line page documents JSON on stdin including `agent_state` ("Current state: `idle`, `working`, `tool_use`, `reviewing`, `authenticating`, `initializing`, or `error`."), `tool_confirmation_pending` ("True when a tool confirmation dialog is showing (omitted otherwise)."), `pending_input_count` ("Number of queued user messages (omitted when 0)."), `task_count`, `subagents`, `conversation_id`, `transcript_path`. The script runs inside the agy process; it is not an external query surface, but a script could write these fields to a file.
Links: https://antigravity.google/docs/cli/headless.md (undated) · https://www.antigravity.google/docs/cli/statusline (undated) · https://raw.githubusercontent.com/google-antigravity/antigravity-cli/main/CHANGELOG.md (no dates in the file; first 100k of 273k chars) · accessed 2026-11-26.
Mark: injection NOT FOUND (searched headless doc, changelog first 100k chars); state field SETTLED (from the official status-line page).
CHANGES first pass: section 3c row "idle ... state field for an interactive session: not found" and "status line script receiving agent-state JSON (search snippet, not verified)": now verified on the official page, including a distinct "waiting for confirmation" boolean.

### 4c. agy 1.5.0 release date
Answer: No official source gives it. The GitHub release tag page `/releases/tag/v1.5.0` returned 404; the repo CHANGELOG.md carries no dates. A third-party mirror (havoptic.com, snippet only) leaves the date blank but says 1.5.0 came 4 days after 1.4.12 (30 Oct 2026), i.e. about 3 Nov 2026 (inference), and lists 1.5.1 as 5 Nov 2026. The first pass's inference that 1.5.0 was at or before 2026-11-04 (issue #31 closed) is consistent.
Links: https://havoptic.com/r/antigravity-cli-1.5.0 (snippet) · https://www.havoptic.com/releases/antigravity-cli/2026/11 (snippet) · accessed 2026-11-26.
Mark: NOT FOUND (official); about 2026-11-03 inferred from a third party, low confidence. Searched: GitHub release tag page (404), CHANGELOG.md first 100k chars, one web search.

1.5.0 content from the changelog (paraphrased by the fetch tool): adds `acp` command ("runs the CLI as an editor-facing agent server, with image and file context, mid-turn steering, session modes, and sign-in from the terminal"), `--remote-agent`, local `/projects`.

---

## Point 5. tmux semantics (tmux(1), man7.org copy; undated, "current" man page)

| Item | Quoted sentence | Mark |
|---|---|---|
| `send-keys -l` | "The flag disables key name lookup and processes the keys as literal UTF-8 characters." | SETTLED |
| `send-keys -H` | "The flag expects each key to be a hexadecimal number for an ASCII character." | SETTLED |
| `paste-buffer -p` | "If -p is specified, paste bracket control codes are inserted around the buffer" ... "if the application has requested bracketed paste mode." | SETTLED (the tail of the sentence is from the fetch summary's continuation; the sentence is cut at that point) |
| `wait-for` | "When used without options, prevents the client from exiting until woken using wait-for -S with the same channel." | SETTLED |
| `remain-on-exit` | "A pane with this flag set is not destroyed when the program running in it exits. If set to **failed**, then only when the program exit status is not zero. If set to **key**, the pane stays open and closes when a key is pressed." | SETTLED |
| `pane_dead` / `pane_dead_status` | "1 if pane is dead" / "Exit status of process in dead pane" | SETTLED |
| hook `pane-died` | "Run when the program running in a pane exits, but remain-on-exit is on so the pane has not closed." | SETTLED |
| hook `pane-exited` | "Run when the program running in a pane exits." | SETTLED |
| `monitor-silence` | "Monitor for silence (no activity) in the window within interval seconds. Windows that have been silent for the interval are highlighted in the status line. An interval of zero disables the monitoring." | SETTLED |
| `monitor-activity` | "Monitor for activity in the window. Windows with activity are highlighted in the status line." | SETTLED |
| `allow-passthrough` | "Allow programs in the pane to bypass tmux using a terminal escape sequence." ... "If set to on, passthrough sequences will be allowed only if the pane is visible. If set to all, they will be allowed even if the pane is invisible." | SETTLED |

Link: https://man7.org/linux/man-pages/man1/tmux.1.html (read at offsets 0-200000 of 278260 chars) · accessed 2026-11-26. Man page version not stated in what was read; whether it equals 3.7c is NOT verified.
Fills gap 8 of the first pass (and row 50's "partly read").

---

## Point 6. Mechanism of large tools; existence and push dates

- Herdr (https://github.com/ogulcancelik/herdr README; docs at herdr.dev, undated, live). README does not state the mechanism. Docs concepts page: "Herdr detects agents from foreground processes, screen manifests, and optional integrations." Integrations page: some integrations "also report the agent's state" (Pi, OMP, Kimi Code CLI, OpenCode, Kilo Code CLI, MastraCode) and "The others leave state to screen detection."; for Claude Code: "state comes from Herdr's screen manifest detection."; Devin: "Devin state still comes from Herdr's screen manifest and OSC detection." The integrations page never mentions "OSC 7501" by name; it mentions "OSC detection" once. Hook reports go through "the local socket API". State meanings: working / blocked / idle-done / unknown ("Herdr cannot confidently classify the state"). Mark: SETTLED for mechanism (screen manifest primary; hooks/plugins for some agents; OSC for Devin only per text read). Last push: README shows no date; not obtained. Accessed 2026-11-26.
  CONTRADICTS first pass row 39 "mechanism not stated" and row 26's listing of Herdr as an OSC 7501 consumer: the docs read say Claude Code state is screen-manifest-based; "OSC detection" is named only under Devin; OSC 7501 by name not found on the integrations or concepts pages. `docs/agents/` not read.
- agent-manager (https://github.com/wainmann/agent-manager; docs/usage.md and docs/configuration.md, undated, live). Configuration doc: "every CLI's commands and status rules are built into the binary". Working detection: "The poll that finds its output stores `working`, and the next poll stores the status the turn ended on." Turns between polls inferred from "the newest prompt or reply on screen changing while the session rests at `finished` or `idle`." Screen matching confirmed (pane text read; "the input, approval, and activity markers"), disk state for some CLIs ("Gemini CLI, Muse, Grok and Antigravity are read from state each keeps for the agent's process"; Cursor `meta.json`; Kiro `--list-sessions -f json`), hooks only report conversation identity. Delivery rule: "The gate is the recipient tool's own rules, because text typed onto a dialog picks an option." and delivery waits until the target is not mid-turn. OSC 7501: not mentioned. Mark: SETTLED (hybrid: screen rules by default, disk state for some CLIs; no OSC 7501 on the pages read). usage.md read to 100k of 121k chars. Accessed 2026-11-26.
  Resolves first-pass row 34 ("README does not say hooks vs screen", conf L).
- tmuxcc: exists. https://github.com/nyanko3141592/tmuxcc, pushed_at 2026-01-19, 69 stars, not archived (GitHub API; accessed 2026-11-26). Fork seungjuchoi/tmuxcc (snippet; push date not fetched). Search snippet: finds agents "by process name, window title, and command line", sends keystrokes to approve or reject. Mark: SETTLED for existence/date; detection from snippet only.
- kiosk-core: exists as the core crate of https://github.com/thomasschafer/kiosk, pushed_at 2026-11-16, 4 stars, not archived (API). Search-snippet summary says agent status "comes mainly from OSC 7501 reports"; I could NOT confirm this on the README, which says "Kiosk started as a tmux session manager, which is no longer maintained" and does not discuss status detection. Mark: PARTLY. CONTRADICTS first pass row 30 ("pane-content detection", from a docs.rs snippet): the newer repo snippet points to OSC 7501 instead; neither opened at source; keep both.
- tmux-overmind: the name resolves to https://github.com/joshmedeski/tmux-overmind, "tmux plugin to interact with DarthSim's overmind" (a Procfile process manager), not an agent tool (search snippet). Different candidate: https://github.com/vanja-jansky-productive/overmind "Fleet (claude code + tmux sessions) management over multiple workstations", pushed_at 2026-11-23, 0 stars, not archived (API). Which one the first pass meant (row text says "daemon scraping each second", repo path 404) is NOT established. Mark: PARTLY (candidates found; the "scrapes each second" claim not re-verified).

---

## First-pass rows this pass changes

- Row 11 (codex queue): date now from OpenAI's own release page (rust-v0.149.0, "20 Aug"); semantics lines quoted; TUI targeting and ack still not stated officially.
- Row 14 and section 4 Claude agent-view line: `claude agents --json` is documented as "every live session" with `kind: interactive|background`; the "don't appear until backgrounded" sentence belongs to the UI list. First pass's "covers backgrounded sessions / invisible" is overstated (contradiction, both kept). Research-preview wording confirmed.
- Row 13/section 4: dates now: v2.1.224 = 07 Aug; v2.1.236 = 19 Aug (day/month, year inferred).
- Row 17: v2.1.295 = 08 Oct (day/month). tmux behaviour: no tmux-side documentation found; mechanism of "asks tmux" still not documented.
- Row 20/section 4 Codex hooks: official page says "enabled by default", silent on experimental vs stable (so the "conflict" is README-vs-silence); 14 events; Interrupt, PreModelRequest, PostModelRequest present.
- Row 22: 0.171.0 / 0.172.0 lines confirmed on release pages; neighbouring lines concern parent/child agents; no line mentions separate top-level sessions.
- Row 23: Codex OSC 7501 now backed by openai/codex PR titles (#52725, #54114, #57612) and issue #58136 (no opt-out as of 2026-10-29); osc777 notification method added in 0.168.0 (2026-11-13); `tui.terminal_title` default ["spinner","project"].
- Row 24 and section 3c: agy status-line JSON verified on official page: `agent_state` (idle/working/tool_use/reviewing/authenticating/initializing/error), `tool_confirmation_pending`, `pending_input_count`; hooks event list is six events (no compaction/permission/exit event); 1.5.0 date still unofficial (about 3 Nov by third-party inference).
- Row 25: spec silence on tmux confirmed. Gap 1 unchanged (tmux side: nothing found; tmux CHANGES has OSC 9;4 in 3.7 and OSC 133 hooks in 3.8 but no 7501).
- Row 30 (kiosk-core): one snippet says OSC 7501, the other (docs.rs) said pane content; unresolved.
- Row 34 (agent-manager): mechanism now stated in docs: screen rules compiled in the binary plus disk state for some CLIs; no OSC 7501.
- Row 39 (Herdr): mechanism now stated in docs: foreground process + screen manifests + optional integrations; Claude Code via screen manifest; OSC 7501 not named on pages read.
- Row 29 (tmuxcc): repo exists (nyanko3141592/tmuxcc, pushed 2026-01-19, 69 stars).
- Row 50 / Gap 8: tmux manual quotes for send-keys -l/-H, paste-buffer -p, wait-for, remain-on-exit, pane_dead, pane-died, pane-exited, monitor-silence, monitor-activity, allow-passthrough now in point 5.
- Header gap "statusline JSON field list not verified": closed (no state field).

sections to refresh: [Codex `codex queue` docs page and `--help` (TUI targeting, ack); Codex config-reference page itself (osc7501 key, notify); first Codex release that emits OSC 7501; PR bodies for #61894 / #62292 (scope of agent mail); agy 1.5.0 official date; kiosk README/source on OSC 7501; Herdr docs/agents page and last-push date; tmux-overmind identity; tmux CHANGES last 80k chars and tmux issue tracker; whether tmux 3.7c man page equals the man7 copy; Claude `agents --json` behaviour for a plain interactive session (untested)]
