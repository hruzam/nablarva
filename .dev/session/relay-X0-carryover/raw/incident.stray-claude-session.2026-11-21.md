---
kind: incident note (facts, then rule)
when: 2026-11-21T21:20:39Z to 21:20:55Z (16 seconds) · host home
cycle: '07' (read-only door inventory, cartan)
reported_by: cartan, unprompted, in _bus/07.cartan.return.md field 2
checked_by: engineer · 2026-11-21T21:26Z
decision_owed: Majkee — keep or delete the transcript named below
---

# A Claude session was started by accident and read working files

**What happened.** While collecting help texts, cartan ran `claude help agents`. Claude Code has no `help` subcommand: a positional
argument is an initial prompt (CLI reference, `claude "query"` — "Start interactive session with initial prompt"). From his shell
this started a headless session in `~/unikuklatrix/nablarva` (entrypoint `sdk-cli`, permission mode `default`, Claude Code 2.1.330,
PID 3345747). He noticed, checked the exact argv, terminated the process and verified that it exited.

**What that session did** — from the tool inputs in its transcript; I read the inputs, not the outputs:

1. Read `.dev/session/pulse.md`.
2. `git status --short`, `git diff --stat`, a listing of this bed's `_bus/` and of `.dev/session/`.
3. Read this bed's `STATUS.md`.
4. `git diff`, then `cat` of `_bus/06.cartan.return.md`, then `head -40 .dev/session/vist-X0-helloWorld/majkee-personal-notes.md`.

Six model requests, four tool calls, no Write and no Edit. The shell commands only read.

**What it therefore saw:** Majkee's uncommitted goal edit in the X0 RUNBOOK (through `git diff`), my uncommitted poke-log lines,
and the first 40 lines of `majkee-personal-notes.md`. As with any session, that content was sent to the model as tool results and
is stored in the transcript.

**What is left on the host** (checked by me): no process with that PID, no `~/.claude/sessions/3345747.json`, no new presence mark.
The transcript remains: `~/.claude/projects/-home-hruzam-unikuklatrix-nablarva/53da8285-b847-479c-81ce-c76224832046.jsonl`
(54 records, about 499 KB). I did not delete or change it.

**Not established:** whether start-up hooks ran; whether anything outside the transcript was touched (I found no sign of it);
why the recorded prompt is `help` and not `help agents`.

**Whose fault.** His command, my POINT. I allowed "`--help` of the installed CLIs and their subcommands" and did not warn that
this CLI turns words into a prompt. The gate "nothing is started" was broken by accident and he reported it himself.

**Rule from now on.** Help probes use the `--help` flag on documented subcommands only. Never `<cli> help <words>` on a CLI where
a positional argument can be a prompt. For this line it is also a finding: one wrong word on a command line activates an agent
that reads the working tree in default permission mode. It goes into the door inventory as a hazard (cycle 08).
