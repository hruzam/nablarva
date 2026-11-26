---
kind: local read-only facts of the Claude side, as installed on home — help text and environment, nothing run beyond that
by: lead (flight · claude 689d87d0-6d49-4c5c-ae33-7fe561e92ac8) · home
looked: 2026-11-26T04:05:18Z, one shell command; and 2026-11-26 03:49 UTC for the process lines
use: the vendor-harness check. These are the program's own words and this host's state on this day — not a test of any door.
---

# What was looked at

1. `claude --version` → `2.1.332 (Claude Code)`.
2. `claude --help`, Commands section, lists among others: `agents [options]` "Manage background agents" ·
   `attach <id|name>` "Open a background session in this terminal" · `logs <id|name>` "Print a background session's
   recent terminal output" · `respawn` · `rm` · `stop|kill`.
3. `claude agents --help`, the line for `--json`: "Print active sessions (interactive and background) as a JSON array
   and exit (for scripts; works without a terminal)"; `--all`: "With --json: also include completed background
   sessions"; `--cwd <path>`: "Show only background sessions started under <path>".
4. In the shell of this session: `CLAUDE_CODE_MESSAGING_SOCKET=/run/user/1000/cc-socks/3858720.sock`, and
   `CLAUDE_CODE_MESSAGING_TOKEN` is set (value not printed, not recorded). 3858720 is the pid of this session's
   process (`claude bg-spare …`, seen at 03:49 UTC).
5. This session's own tool list carries `ListAgents` and, deferred, `SendMessage` — the vendor's tools for listing and
   messaging other sessions. Neither was called.
6. At 03:49 UTC: the process in tmux pane %70 is `claude attach b155ba44`; the session shown there runs under
   `claude bg-pty-host … --bg-spare …`, a child of the user's systemd, not of the pane's shell.
7. `tmux -V` → `tmux 3.7c`.

# What this shows, and what it does not

- **Shows:** the installed Claude Code names, in its own help, a scriptable listing of active sessions that covers
  interactive ones; a per-session messaging socket exists for this session; the sessions in this tmux window are
  already hosted by the vendor's background supervisor and merely attached in the pane.
- **Where it differs from the research child's table** (`raw/research.wheel-and-harness.epoch.2026-11-26.md`):
  row 14 reports the documentation as saying interactive sessions do not appear until backgrounded and marks the
  point ambiguous — the installed help says "interactive and background"; row 13 gives the socket directory as
  `/tmp/cc-socks-<uid>` — here it is `/run/user/1000/cc-socks/`. Both sides are kept; neither is flattened.
- **Does not show:** what `claude agents --json` actually prints for a session in a tmux pane, which states it
  reports, how fresh they are, or whether a message through the socket or `SendMessage` arrives. Nothing was listed,
  nothing was sent. Running either would be a probe; this bed runs none (RUNBOOK, "deliberately does not do").
- The help text carries no "preview" or "experimental" mark on `agents`; the research child's row 14 reads the
  documentation as "research preview". Both are recorded.
