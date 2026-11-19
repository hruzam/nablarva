<!-- Controller metadata: /root/terminal_approaches_research, follow-up correction; body verbatim. Read with original consolidated report. -->

Correction to consolidated handoff:

**SOURCE:** Claude Agent View’s [“Run a shell command”](https://code.claude.com/docs/en/agent-view#run-a-shell-command) documents `claude --bg --exec <command>` as starting a background **PTY-backed shell job** that replaces Claude for that session—no model is invoked—and says to attach to its row to see output. Thus it is a native persistent task-shell candidate with a documented attach path, not merely conversation-only attachment.

Still **UNKNOWN:** whether an agent can access/control that same job independently; permission/sandbox behavior; full-screen/alternate-screen fidelity; stdin/EOF/Ctrl-C, resize, concurrent writers, reconnect, and restart semantics. It needs qualification.

Local corrections:

- Termbrana’s Zellij observer is observation-only; Termbrana as a whole also includes the separate L17 composition family.
- L14 D2 locks the file plane as spine. PTY-as-impulse is plan, not lock.
