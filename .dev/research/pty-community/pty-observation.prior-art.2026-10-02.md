# PTY-layer observation of CLI agent sessions — community prior art
Date: 2026-10-02 · Author: @Epoch · Triggered by: nablarva events map v0.1 (rows 9/10/17/18/20, `stall`, PTY-only fallback column)
Scope: what the PTY/terminal/mux layer can and cannot say about an agent CLI, as practised by third parties. Hooks are out of scope (see vendor-events.catalogue.2026-10-02.md).
Legend: **Doc** = documented by the vendor/project. **Obs** = observed/reported by third parties. Conf H/M/L. (S) = WebFetch summary, not verbatim. "TL" = training-knowledge, long-stable, NOT re-fetched this run (the man7 tmux page fetch came back truncated).

## 1. Primitives (what the layer offers)

### 1.1 tmux

| Primitive | What it gives | Doc status | Version/date | Conf | Source |
|---|---|---|---|---|---|
| `pipe-pane [-I][-O]` | tee of pane output bytes to a command; raw PTY bytes incl. escapes; `-I` feeds stdin into the pane | Doc (TL) | decades-old | H (TL) | https://man7.org/linux/man-pages/man1/tmux.1.html (not re-read) |
| `capture-pane -p -e -J -S -E` | rendered screen/scrollback snapshot (plain, with SGR attrs via `-e`, wrapped lines joined via `-J`) | Doc — flags verified this run | — | H | man7 tmux(1) (S) |
| Control mode `-C`/`-CC` | text protocol: `%begin/%end/%error` (time, cmd number, flags), async `%output`, `%extended-output` (with timing), `%window-add/close`, `%sessions-changed`, `%pause/%continue` (flow control `pause-after`), format **subscriptions** (`refresh-client -B`) | Doc | designed for iTerm2 (George Nachman) | H | https://github.com/tmux/tmux/wiki/Control-Mode (S) |
| `wait-for` (channels, `-L/-S/-U`) | named-channel rendezvous between shell commands | Doc (TL) | old | H (TL) | man7 tmux(1) |
| `wait-for -E`, `set-hook -E`, `set-hook -B/-T` (monitor hooks: format re-evaluated every second, fire hook on change; `-T` only when true) | event-driven hooks inside tmux | **new in 3.8 CHANGES** | master CHANGES "3.7→3.8" read 2026-10-02; **3.8 release status unverified** (releases page showed 3.7c stable + 3.8-rc3; dates in the fetched summary were inconsistent, so not quoted) | M | https://raw.githubusercontent.com/tmux/tmux/master/CHANGES (S) · https://github.com/tmux/tmux/releases (S) |
| **OSC 133 events**: `pane-command-started`, `pane-command-finished`, `pane-shell-prompt` (+ new OSC-133-aware commands select-output/copy-output/pipe-output in PR #5574) | hooks driven by shell prompt marks | new (3.8 line) | same CHANGES; PR https://github.com/tmux/tmux/pull/5574 (digest) | M | |
| new hooks: pane activity, pane mode/prompt changes, client create/destroy, resize/move, window events | broader hook set | new (3.8 line) | CHANGES (S) | M | |
| `monitor-activity` / `monitor-silence N` / `monitor-bell`; `alert-*` hooks | tmux-native "output seen / N seconds quiet / BEL" flags per window | Doc | old | H | https://tmuxai.dev/tmux-alerts-monitoring/ (digest; man page TL) |
| `pane-died` / `pane-exited` hooks, `remain-on-exit`, `#{pane_dead}`, `#{pane_dead_status}`, `#{pane_pid}`, `#{pane_tty}`, `#{pane_current_command}` | process-exit and join keys | Doc (TL) | old | H (TL) | man7 (remain-on-exit mention verified (S)) |
| Passthrough: `allow-passthrough` + DCS wrapping for sequences tmux doesn't forward | forward OSC to outer terminal | Doc; fragile | — | M | tmux issue #5237 (below) |

OSC 133 and tmux: issue #3064 (opened 2022-02-10) is **closed** (S); tmux historically did **not** forward OSC 133 to the outer terminal; open request #5237 asks for default forwarding. https://github.com/tmux/tmux/issues/3064 · https://github.com/tmux/tmux/issues/5237 · WezTerm prompt-nav inside tmux broken: https://github.com/wezterm/wezterm/issues/7168 (M).

### 1.2 Zellij, kitty, WezTerm, others

| Tool | Primitive | Detail | Version/date | Conf | Source |
|---|---|---|---|---|---|
| Zellij | `zellij subscribe --pane-id <id>…` | streams **rendered** viewport (optionally scrollback, `--ansi`) to stdout; `--format json` ⇒ NDJSON events **`pane_update`** (viewport/scrollback) and **`pane_closed`**; full viewport delivered at subscribe, then only changes; works on background/remote sessions (`--session`) | **0.44.0, 2026-03-23** | H | https://zellij.dev/documentation/zellij-subscribe.html (S) · https://zellij.dev/news/remote-sessions-windows-cli/ (digest) |
| kitty | remote control `kitten @ get-text --extent screen|all|selection [--ansi] [--add-cursor] [--add-wrap-markers]`, `kitten @ send-text`, `ls` | rendered text, needs `allow_remote_control` | stable | H | https://sw.kovidgoyal.net/kitty/remote-control/ · manpage kitten-@-get-text (digest) |
| WezTerm | `wezterm cli get-text [--escapes] [--start-line/--end-line]`, `list`, `send-text`; mux server | rendered text; default = screen without scrollback | stable | H-M | https://wezterm.org/cli/cli/get-text.html (digest) |
| Ghostty | macOS **AppleScript** scripting of windows/tabs/splits/terminals incl. send text | **preview**, API change expected in 1.4; also `notify-on-command-finish` via OSC 133 | 1.3.0, 2026-03-09 | M | https://ghostty.org/docs/install/release-notes/1-3-0 (S) |
| iTerm2 | tmux `-CC` integration; OSC 1337 / OSC 9 notifications; shell integration | TL (not re-fetched) | old | M (TL) | — |
| asciinema | recorder: PTY master tee → asciicast; **3.0 (Sept 2025) = Rust rewrite, asciicast v3 (event time deltas), live streaming** | recording, not live semantics | 2025-09 | H | https://blog.asciinema.org/post/three-point-o/ · https://docs.asciinema.org/manual/asciicast/v3/ |
| vhs (charmbracelet) | `.tape` script → virtual terminal → GIF/video; **drives** a terminal, not observation of a foreign one | demo-as-code | active 2026 | M | https://github.com/charmbracelet/vhs |
| ttyd | shares a PTY over WebSocket/xterm.js (browser) | transport, not semantics | 1.7.7 pkg built 2026-04-03 (Arch) | M | https://archlinux.org/packages/extra/x86_64/ttyd/ |
| `script(1)` (util-linux), `expect`, `pexpect` | PTY master/slave allocation, transcript capture, pattern-wait on the byte stream | TL (stable since 1990s, not re-fetched) | — | H (TL) | — |

### 1.3 Marks that the *emitter* puts into the stream (in-band semantics)

| Mark | Who emits | What it tells the observer | Notes | Conf | Source |
|---|---|---|---|---|---|
| OSC 133 (FinalTerm semantic prompt: A prompt start / B input start / C output start / D;exit-code) | the **shell** (via precmd/preexec, PS0/PS1, fish events) | command boundaries + exit code for **shell** commands | An agent TUI running *inside* the shell does not (as far as read) emit it; during the agent's run the shell sits at "C" (command running). **Whether Claude/Codex/Gemini emit OSC 133 themselves: not verified.** Adopted by VS Code, kitty, WezTerm, iTerm2, Ghostty ≥1.3 (much more complete), tmux 3.8 events | M | https://vtdn.dev/docs/osc/osc133/ · https://wezterm.org/shell-integration.html · Ghostty notes above |
| BEL / OSC 9 / OSC 777 / OSC 99 desktop notifications | **the agent itself** | "needs you": CC on permission prompt, idle prompt, auth, elicitation (`preferredNotifChannel`: auto/iterm2=OSC9/ghostty=OSC777/terminal_bell; `terminalSequence` hook output); Codex `[tui] notifications=["agent-turn-complete","approval-requested"]`, `notification_method=auto|osc9|bel` | **The only vendor-native waiting/idle signal that lives *in the PTY stream***; OSC 9/777 are swallowed by tmux unless passthrough; BEL works with `monitor-bell`. Codex per config-advanced doc; CC per third-party guides | M | https://developers.openai.com/codex/config-advanced · https://github.com/Anmol-Srv/ghostty-claude-notifications · https://github.com/anthropics/claude-code/issues/19979 · https://blog.jamespan.tech/posts/terminal-notifications-claude-code-remote-tmux-en |
| OSC 0/2 window title | agent/shell | agentenmux reads pane title as a status channel (needs the OSC to reach tmux) | M | agenmux README (S) |

## 2. Projects that infer idle / working / waiting from screen or PTY

"Maintenance signal" is only what the fetched pages showed (stars/commits); no last-commit dates were read — treat as weak. All rows fetched 2026-10-02.

| Project | Layer it reads | How state is decided | Agents covered | Maint. signal | Conf | Link |
|---|---|---|---|---|---|---|
| **agenmux** (yaakov300/tmux-agents-mon; fork of snirt/agenmux) | tmux screen + title + process tree | "scraping-only": walks pane process tree to identify agent; bottom **20 lines** + pane title matched by grep patterns; 4 states blocked ⣿red / working spinner / done / idle; per-agent pattern files in `~/.config/agenmux/agents/` | Claude, Codex, OpenCode, Pi | 263 commits, 0 stars (S) | M | https://github.com/yaakov300/tmux-agents-mon |
| **ccmanager** (kbwo) | PTY output parsing, "state detection strategy per CLI" | Idle / Busy / Waiting; separate *status-change hooks* are automation, not detection | Claude, Gemini, Codex, Cursor Agent, Copilot CLI, Cline, OpenCode, Kimi, MiniMax | 1.3k stars, 770 commits, MIT (S) | M | https://github.com/kbwo/ccmanager |
| **agent-deck** (asheshgoplani) | hybrid | (1) hooks for Claude/Pi, (2) **terminal-output pattern matching** for Gemini/Codex/MiniMax, (3) tmux activity timestamps as last resort | many | n/a (S) | M | https://github.com/asheshgoplani/agent-deck |
| **herdr** (as reported in rrnewton/agent-utils #179) | screen rules | rule `live_prompt_box (priority 950)` matching `❯` marks Claude **idle even mid-turn** because CC keeps the prompt box visible while working; only the footer "esc to interrupt" differs. Fix proposals: `claude agents --json`, footer visibility | Claude | issue only | M | https://github.com/rrnewton/agent-utils/issues/179 |
| **keepmind9/clibot** | tmux capture-pane stability + transcript | polling mode = capture when output "becomes stable", then reads transcript.jsonl; hook mode for Claude/Gemini/OpenCode | Claude, Gemini, OpenCode | predecessor, pkg.go.dev (M) | M | https://pkg.go.dev/github.com/keepmind9/clibot/internal/cli |
| **rorhcdream/tmux-agent-status** | **files, not screen** | Claude: `~/.claude/sessions/<pid>.json` `status` (busy/idle/waiting/shell; schema "observed v2.1.178"); Codex: rollout JSONL via `lsof` (`task_started`→working, `task_complete`→done, `turn_aborted`→cleared); ambiguous with shared Codex app-servers | Claude, Codex | 15 commits (S) | M | https://github.com/rorhcdream/tmux-agent-status |
| nipunravisara/tmux-agent-status · jward7/tmux-agent-signal · stefanahman/claude-status · FlavianMF/tmux-claude-monitor · partner0/tmux-agent-status | **hooks** → tmux user options keyed by `$TMUX_PANE` | deterministic, "independent of model output"; no screen | Claude (+Codex/OpenCode) | search digest only | M | https://github.com/nipunravisara/tmux-agent-status · https://github.com/jward7/tmux-agent-signal |
| c9watch (minchenlee) PR #132 | `claude agents --json` + liveness | drops dead PIDs before status inference | Claude | PR digest | M | https://github.com/minchenlee/c9watch/pull/132 |
| Vaduz/next-watch #15 | `sessions/<pid>.json` | a live Claude process with no pid file is **invisible** (child sessions, transcript saving off) | Claude | issue digest | M | https://github.com/Vaduz/next-watch/issues/15 |
| shindgew/agy-acp · marceldarvas/cc-multi-cli-plugin · aelaguiz/codex_monitor_skill | files/DB; PTY diagnostic only | from predecessor note 2026-10-01 | agy, Codex | not re-fetched | M | see predecessor |
| wrock/wezterm-agent-cards, cmux (manaflow-ai), claude-squad, kherep#66, claude-peers-mcp, codex-wake | not read this run | — | — | — | — | search digest only |

Pattern in the field (M, from the above): **hooks first, files second, screen last** — every tool that supports hooks prefers them; screen scraping survives for agents lacking hooks (agent-deck: Gemini/Codex/MiniMax) and as a sanity layer.

## 3. Reported failure modes (observed by third parties; no vendor fix promised)

| Failure mode | Report | Date | Effect on observation | Conf | Link |
|---|---|---|---|---|---|
| **No alternate screen**: CC repaints with cursor-up + erase-line in the main buffer; spinner/status lines leak into scrollback as stacked duplicates | CC #69577, #79229 (open-ish; state not read) | 2026 | `capture-pane` history and scrollback diffs are polluted; "viewport stable" is hard to define | M | https://github.com/anthropics/claude-code/issues/69577 · /issues/79229 |
| Fullscreen TUI mode captures all mouse events | CC #72681 | 2026 | implies a fullscreen/alt-screen-like mode exists (M-L) → observer must handle both screen regimes | L | https://github.com/anthropics/claude-code/issues/72681 |
| **Spinner / transient redraw noise** ⇒ state flicker | agenmux README limitation "transient screen redraws can cause state flickering" | 2026 | pattern classifiers need debounce | M | https://github.com/yaakov300/tmux-agents-mon |
| **Idle false-positive: prompt box visible while working** | herdr in agent-utils #179 | 2026 | "❯ visible ⇒ idle" is wrong for CC; only footer text separates them | M | https://github.com/rrnewton/agent-utils/issues/179 |
| **Bracketed paste + Enter race**: `send-keys -l` then `send-keys C-m` → Enter swallowed while the TUI is still ingesting paste; message sits unsent while sender reports success | Agents-Core #70, niles #135, marvel PR #357, gascity PR #5708, nils-cli #2009 | 2026 | **input-side** observation failure (delivery not confirmed). Fix pattern: `load-buffer` (unique name) → `paste-buffer -p -d` → Enter in one invocation; or 0.3–0.4 s delay + rescue second CR | M | https://github.com/ArcavenAE/marvel/pull/357 · https://github.com/gastownhall/gascity/pull/5708 · https://github.com/Rhovian/niles/issues/135 |
| Large pastes dropped over ssh+tmux (>9994 bytes) | cmux #10943 | 2026 | input loss on remote hops | M | https://github.com/manaflow-ai/cmux/issues/10943 |
| Bracketed paste breaks login code entry (iTerm2 default) | CC #47670 | 2026 | agent TUIs mishandle mode 2004 in some screens | M | https://github.com/anthropics/claude-code/issues/47670 |
| TUI freezes on dictation-app paste; SIGWINCH doesn't redraw | CC #24891 | 2026 | a "stall" can be a **hung TUI**, indistinguishable from waiting | M | https://github.com/anthropics/claude-code/issues/24891 |
| **Resize**: no redraw after resize (KVM switch) until input | CC #43273 | 2026 | resize events can leave the screen stale; observer sees "no change" | M | https://github.com/anthropics/claude-code/issues/43273 |
| **A byte stream is not a session**: replaying scrollback into a new emulator needs width/height, modes (alt-screen, mouse), cursor/wrap state; same bytes render differently at 40 vs 18 cols | Xtend Journal (Aouizerat) | 2026-08-21 | pipe-pane bytes alone can't rebuild the screen; need a live terminal-state model | M | https://getxtend.com/blog/terminal-state-you-cant-replay.html |
| **OSC passthrough**: tmux does not forward OSC 133 (and OSC 9/777 without `allow-passthrough`+DCS wrapping); outer-terminal shell integration silently dies inside tmux | tmux #5237, WezTerm #7168 | 2022→2026 | in-band marks can be lost between agent and observer | M | links in §1.1 |
| Scrollback is bounded / history-limit; `capture-pane -S -` cost grows | TL | — | long sessions truncate; use records for history | M (TL) | — |
| Pane titles need OSC to reach tmux; restored sidebar panes become idle shells after tmux server restart | agenmux README | 2026 | tool-specific | M | agenmux link |

## 4. Stable (TIMELESS POSIX) vs weather

| Class | Item | Why | Conf |
|---|---|---|---|
| **TIMELESS** | Process liveness: child exit via `SIGCHLD`/`wait4`/`waitid`, `pidfd_open` readable, `/proc/<pid>/stat` state, `/proc/<pid>/fdinfo` pos | kernel ABI, decades | H (TL) |
| TIMELESS | PTY master/slave semantics, `termios` (ISIG: `0x03`→SIGINT), `SIGWINCH`/`TIOCSWINSZ`, EOF/HUP on master close | POSIX | H (TL) |
| TIMELESS | "Is *any* byte moving?" — `pipe-pane` byte count / `monitor-activity` / `monitor-silence` / fdinfo pos advancing; BEL (0x07) | content-agnostic, no screen parsing | H (TL) |
| TIMELESS | tmux `pipe-pane`, `capture-pane`, `wait-for`, `pane-died`, `pane_pid`/`pane_tty`; `script`, `expect/pexpect`; xterm bracketed-paste mode 2004 | old, documented | H (TL; not re-fetched) |
| TIMELESS-ish | tmux control mode (`-C/-CC`) | designed 2010s for iTerm2, stable protocol, documented | H |
| Weather | Any agent-TUI string/glyph pattern ("esc to interrupt", `❯`, spinner glyphs, footer text) | changes with vendor release; CC alone shipped 2.1.281→2.1.287 in 9 days | H (inference from changelog cadence) |
| Weather | Rendered-screen taps (capture-pane/`zellij subscribe`/kitty get-text) as *meaning* source | no-alt-screen repaint, spinner noise, resize staleness | M |
| Weather | `zellij subscribe` (0.44.0, 2026-03-23), tmux 3.8 hook/event system + OSC 133 events (3.8 unreleased/rc seen), Ghostty AppleScript (preview), asciicast v3 | <12 months old, APIs may move | M-H |
| Weather | OSC 9/777/99 notification channels (terminal-dependent, tmux passthrough) | per-terminal support matrix | M |
| Weather | CC `sessions/<pid>.json` schema; Codex rollout names; Gemini chat JSONL layout; agy transcript layout | undocumented/internal | M |
| Weather | ACP (JSON-RPC over stdio) | young; Gemini has it, agy requested, status per vendor | M |

## 5. Things nobody has solved (as of 2026-10-02; absence of evidence in sources read, not proof)

1. **Distinguishing "waiting for approval" from "tool running slowly" or "TUI hung" with no hook, no file, no screen parsing.** Every PTY-only tool uses vendor-specific text patterns; none offers a vendor-neutral signal (agy has no hook for it — vendor catalogue).
2. **A vendor-neutral, version-stable "agent is idle" mark in-band.** OSC 133 marks shells, not agents; no evidence read that any agent CLI emits it. Agents emit OSC 9/777/BEL notifications instead — vendor-specific, terminal-dependent, lost in tmux without passthrough.
3. **Confirmed delivery of input** (did the prompt actually submit?): bracketed-paste/Enter races are patched ad hoc per project; no acknowledgement channel exists below hooks.
4. **Reconstructing screen state from `pipe-pane` bytes** without a full terminal-state model (size, modes, wrap flags); everyone either snapshots (`capture-pane`) or uses a mux that holds the model (tmux/zellij/kitty/wezterm).
5. **PID ↔ session identity across `/clear`, resume, fork, shared app-servers**: CC `sessions/<pid>.json` doesn't update on `/clear` (#36213, closed not planned); Codex has no per-pid file and shared app-servers blank the join (tmux-agent-status).
6. **Stable cross-version semantics of on-disk records** (CC: "internal… changes between versions"; Codex: "not a stable interface"; Gemini/agy: undocumented).
7. **Observing agents across an SSH hop** with fidelity: input drop >9994 bytes (cmux #10943), `zellij subscribe` works on remote sessions but only if the agent runs under zellij; no evidence of an agent-aware remote tap.
8. **Alt-screen vs main-screen regime detection** for agents that switch modes (CC main-buffer repaint vs "fullscreen" mode): no project read documents handling both.
9. **Quantified false-positive/negative rates** of any screen classifier: none of the projects read publish them (agenmux/ccmanager/agent-deck report none).

## 6. Confidence and gaps
- Live-fetched this run (S): zellij subscribe doc, tmux Control Mode wiki, tmux CHANGES (master), tmux issue #3064, Ghostty 1.3.0 notes, Xtend article, agenmux/ccmanager/agent-deck/tmux-agent-status READMEs, herdr issue #179.
- Search-digest only (not opened): kitty/wezterm get-text pages, asciinema 3.0 post, vhs, ttyd, bracketed-paste issue set, OSC 133 reference sites, Claude/Codex notification guides.
- Training knowledge (TL): `pipe-pane`/`wait-for`/`script`/`expect`/`pexpect`/POSIX items — stable for decades but not re-verified this run (man7 fetch truncated).
- tmux 3.8: release status unverified.

Sections to refresh: [tmux 3.8 release + OSC 133 hook names; zellij subscribe changes after 0.44; agy/Codex/Gemini OSC 133 emission; per-project last-commit dates; CC #69577/#79229 status; Ghostty 1.4 scripting API]
