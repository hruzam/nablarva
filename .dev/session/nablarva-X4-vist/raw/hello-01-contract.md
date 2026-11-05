from-nabla.Tmux.chatbot ---
From Nabla (Claude) in the Nabla.Tmux chat · 2026-10-23
Contract draft r0 requested by Majkee · proposed, not implemented
Reads with: vist-01-principle-and-applications.md, termbrana-04-sublime-ide.md

# HELLO — the neutral mail channel between two CLI seats, contract r0

Marks used below: *decided* means Majkee chose or agreed to it in conversation; *proposed* means
Nabla's suggestion, open to kick, bend or veto; *open* means not settled; *verify* means tool or
vendor behaviour not checked against current documentation in this sitting. Unmarked statements
are proposed.

## What this is

Two interactive CLI seats, Claude Code and Codex, each in its own tmux pane on the office machine,
send each other a hello. Each answers the other's hello once, and the exchange stops by rule. The
channel uses only files, two shell commands and tmux keystrokes. Nothing in it depends on a vendor
mechanism: no hooks, no headless `claude -p`, no `codex queue`, no tunnel, no MCP (decided).
Vendor routes may serve as a reference to compare against during testing, never as the path.
Per-CLI differences are confined to configuration and to one calibrated pair of patterns per seat.

This is the "separate supervised primitive, designed in an experimental bed with its own gate"
that HANDSHAKE anticipates for async completion and receipts. It does not grow inside HANDSHAKE,
and it changes neither the temple bus nor the `_bus` law. Its keystroke injection happens only
inside the experiment bed, by the operator's decision. Termbrana's delivery gate and Ovitmugen's
no-injection rule stay as they are.

## The idea in one paragraph

A seat sends by calling `nabla-send`, which writes a mail file into the receiver's inbox. A
watcher, `nabla-bell`, sees the file land and rings the receiver's pane: when the pane is idle, it
types one short line naming the message, presses Enter as a separate call, and checks that the
line was taken. The receiver runs `nabla-read`, answers once with `nabla-send --in-reply-to`, and
ends its turn. An answer expects no answer, so the exchange stops. If no answer arrives by the
deadline, the bell writes a timeout notice to the sender and rings it. Discipline is enforced by
the tools: the agent never writes the envelope by hand, and every refusal says how to fix the
call (decided in substance: the command-enforced format was agreed in this chat).

## Fit with what already exists

| Source | Taken over | Left alone |
|---|---|---|
| `_mail/README.md` (temple bus) | receiver-owned `inbox/` and `archive/`; presence in the inbox means unprocessed; the move to `archive/` means processed; a reply returns to your inbox; no sent-copy; seats provisioned on first use; ask-first on boot | the filename shape gains a sequence suffix (open, needs a gavel); the temple bus itself is not touched. Its deferred transport (candidate 0008) is this contract's natural home if the experiment proves out |
| HANDSHAKE r1 Delivery rule | disk persistence proves availability, not receipt; consumption is stamped by the archive move; the reply is the strongest stamp; a POINT owes nothing back, which becomes `expects_reply: no` | HANDSHAKE keeps "no daemon between runtimes"; this bell lives only in the experiment bed |
| tunnel GUIDE | the operator opens the channel (law 2.4, the human opens the table); an explicit path or a clean exit 13 with nothing created; a man-page exit contract | the tunnel as a route |
| `_bus` GUIDE | nothing; `_bus` keeps its no-read-state law. Later a mail line can point a seat at a `_bus` filename, which that guide already allows | |
| gate design (2026-10-15 chat) | content in files, the doorbell only as a nudge; a ladder; retry once, then the operator | the accepted and working steps, parked |
| vist-01 | the calibrated input-line pair is a hand-made, one-screen signature; Antensor can replace it later without changing this contract | |

## The bed

```text
<bed>/
  AGENTS.md                 the instruction block below, for both CLIs
  CLAUDE.md                 one line: @AGENTS.md
  .claude/settings.json     allow rules for the two commands
  bin/                      nabla-send  nabla-read  nabla-bell  nabla-mail
  _mail/
    OPEN                    present only while the operator keeps the mail open
    .tmp/  .seq/  .log/events.jsonl
    claude/inbox/  claude/archive/  claude/bell.conf
    codex/inbox/   codex/archive/   codex/bell.conf
  test/                     the fake seat and the test runner
```

The bed lives outside any tree that already holds a CLAUDE.md or AGENTS.md, so both CLIs read
only this block (open: where exactly). Claude Code reads AGENTS.md natively only when no CLAUDE.md
exists at or above the working directory (Claude Code card, 2026-10-08); the one-line CLAUDE.md
import removes that dependency (verify the import syntax). Both CLIs start with the bed as their
working directory, so Codex's workspace-write sandbox already covers `_mail/` (verify).

## The mail file

One file per message, written only by `nabla-send` or by the bell, never by hand.

```text
<receiver>/inbox/<sender>.<scope>.<YYYY-MM-DD>.<NN>.md
```

This is the temple bus shape plus `.NN`, a two-digit sequence per sender and day, because two
hellos on one day would otherwise collide (open: the gaveled shape has no suffix). The file name
without `.md` is the message ID, for example `claude.hello.2026-10-23.01`.

```markdown
---
id: claude.hello.2026-10-23.01
from: claude
to: codex
scope: hello
in_reply_to: none
expects_reply: yes
deadline: 2026-10-23T19:45:00+02:00
sent: 2026-10-23T19:35:12+02:00
host: office
---
hello from claude
```

`from` comes from the environment, never from the agent's arguments. `none` is written out, as in
the house style. An answer has `in_reply_to` set, `expects_reply: no` and no deadline. Notices
from the bell come from the pseudo-seat `bell` and also expect no reply. The body is UTF-8 text up
to 64 KiB.

Delivery is atomic, the Maildir way: the file is written under `.tmp/`, then renamed into the
receiver's inbox, so the bell never sees a half-written message. IDs are claimed with an atomic
`mkdir` under `.seq/`.

## nabla-send

```text
nabla-send --to <seat> [--scope <word>] [--within <minutes>] (--body <text> | --body-file <path|->)
nabla-send --in-reply-to <id> (--body <text> | --body-file <path|->)
```

The first form opens an exchange. `--scope` defaults to `hello` in this bed, and `--within` sets
the deadline: 10 minutes by default, at most 120. The second form answers: the receiver and scope
come from the original, which is moved to the replier's archive in the same call. For a longer body
the agent uses `--body-file -` with a heredoc, so nothing needs quoting. `NABLA_MAIL` (the `_mail`
path) and `NABLA_SEAT` (this pane's seat) must be set by the operator's launch; if either is
missing, the command exits 13 and creates nothing.

On success it prints one line, and the line tells the agent what to do next:

```text
sent claude.hello.2026-10-23.01 to codex, answer due by 19:45. End your turn now: the answer or a timeout notice will arrive as a [nabla-mail] line.
sent codex.hello.2026-10-23.01 to claude as the answer to claude.hello.2026-10-23.01. This exchange is complete: send nothing more about it.
```

Every refusal goes to stderr in one shape: code, cause, fix, and whether to retry.

```text
nabla-send: E16 codex.hello.2026-10-23.01 expects no reply, so it cannot be answered. Do not retry: this exchange is complete.
```

| Exit | Meaning | Advice printed |
|---|---|---|
| 0 | sent | the next step, as above |
| 10 | the mail is closed: no `OPEN` | do not retry; tell the operator |
| 11 | usage: unknown flag, missing or conflicting argument | fix the call as shown; retry once |
| 12 | unknown seat, yourself, or `bell` | fix the seat; retry once |
| 13 | `NABLA_MAIL` or `NABLA_SEAT` not set; nothing written | tell the operator |
| 14 | body missing, empty, over 64 KiB, or not text | fix the body; retry once |
| 15 | `--in-reply-to` names nothing in your inbox or archive | check with `nabla-read`; retry once |
| 16 | that message expects no reply | do not retry: the exchange is complete |
| 17 | that message already has your answer | do not retry: it was delivered |
| 20 | write failed: permissions, sandbox or disk | do not retry; tell the operator |

Exit 16 is the loop guard, the RFC 3834 idea in tool form: automated answers are marked, and
marked mail is never answered. Exit 17 makes a nervous retry harmless. Its check looks for an
existing answer in the original sender's folders, not at where the original sits, so a hand-moved
file cannot fake it.

## nabla-read

```text
nabla-read          list your unprocessed mail, oldest first
nabla-read <id>     print one message with its footer
```

The printout labels the sender as a peer agent, not the operator, and ends with a footer that is
the next instruction:

```text
[nabla-mail] codex.hello.2026-10-23.01
from: codex, a peer agent, not the operator
expects_reply: yes, by 19:45
---
hello from codex
---
Answer once, only with:
  nabla-send --in-reply-to codex.hello.2026-10-23.01 --body "<your answer>"
Then end your turn.
```

A message that expects no reply prints "This message expects no reply: do not answer it. It is now
in your archive." and is moved there in the same call, since reading it is all its processing. A
message that expects a reply stays in the inbox until the answer moves it, so the inbox keeps
meaning what the temple bus says it means. Reading the same message twice is harmless. Exit codes:
0 ok, 11 usage, 13 environment not set, 15 no such message in your inbox or archive, 20 read
failed.

## nabla-bell

One process per bed, started by hand in its own pane (law 2.4). It refuses to start without `OPEN`
(exit 10) and stops when the operator closes the mail. It watches every seat's `inbox/` with
`inotifywait` for files renamed in, and it is the only writer of `.log/events.jsonl`.

Each seat's binding lives beside its inbox, written by the operator's launch once the CLI is up:

```text
pane=%7
server_pid=4182
command=claude
input_line=^│ > (.*)│$
input_empty=^(Try ".*")?$
settle_ms=600
```

`input_line` is an extended regex that finds the input line on a captured screen; its group 1,
trimmed, is the current input. `input_empty` says what an empty input looks like, placeholder text
included. Both are calibrated by eye with `nabla-mail calibrate <seat>`: capture an idle screen, a
busy one and an approval dialog, and the pair must report idle only for the first. The example
values are illustrative (verify per CLI version, and recalibrate after every upgrade, which becomes
the canary's job later). Until both patterns are set, the bell holds that seat.

The ring, for each landed message:

| Step | Check | On failure |
|---|---|---|
| 1. binding | the pane exists and the tmux server PID matches `server_pid` | hold, alert: stale binding. Never search for a pane that looks right |
| 2. occupant | `pane_current_command` equals `command`, recorded from the live pane at launch | hold, alert |
| 3. idle | two captures two seconds apart are identical, and the input line matches with an empty input | hold; recheck every 15 s for as long as it takes |
| 4. type | `tmux send-keys -l` with the nudge, no Enter | |
| 5. landed | after `settle_ms`, the input line shows the message ID | no Enter; alert: stuck, text left for the operator |
| 6. Enter | `tmux send-keys Enter`, as its own call | |
| 7. taken | within 3 s, no input line shows the ID | one more Enter; then alert: stuck |
| 8. log | `rung`, with attempts and timings | |

Step 3 carries the safety rule: Enter goes only to a screen positively identified as the empty
input line, because in an approval dialog Enter can mean yes. The stillness test works across
vendors because both CLIs animate while they work, and a CLI that redraws while idle will show up
in calibration. The input-line test is what excludes dialogs.

The nudge is one line, with the ID early so it survives wrapping in a narrow pane:

```text
[nabla-mail] nabla-read codex.hello.2026-10-23.01 (from codex, a peer agent, not the operator)
```

It stays under 100 characters on a single line, and it avoids every character that opens a menu
or a mode in either CLI: no `@`, no `/` at the start, no `!`, `#`, `?` or `$` (verify per CLI). It
carries no path and no content; the content is read once, through `nabla-read`. Seat panes need
vim-style input modes off.

Every 30 s the bell also sweeps deadlines. An opener whose deadline has passed with no answer seen
gets one timeout notice in its sender's inbox, which lands and rings like any mail; that is the
wake-up back. A late answer is still delivered and logged as late. A breaker stops runaways: more
than six rings to one seat within ten minutes pauses that seat until the bell restarts, and alerts
the operator. Alerts print in the bell's own pane and go to the log.

```json
{"ts":"2026-10-23T19:35:14+02:00","event":"rung","id":"claude.hello.2026-10-23.01","seat":"codex","detail":"enter taken on attempt 1, 0.9 s"}
```

The ladder in the log is `landed`, `rung`, then `answered` or `timeout`, with `held`, `stuck`,
`paused` and `stale` as side states. Build JSON lines with `jq -nc`, never by string
concatenation.

## nabla-mail, the operator's command

```text
nabla-mail open <path>          create _mail/ and OPEN: the operator opens the channel
nabla-mail bind <seat> <pane>   provision the seat on first use and write bell.conf from the live pane
nabla-mail calibrate <seat>     print the pane's screen with line numbers and the current idle verdict
nabla-mail status               open or closed, bindings, inbox counts, paused seats, last events
nabla-mail close                remove OPEN: sends exit 10, the bell stops
```

## The instruction block

The same text for both seats, in the bed's AGENTS.md:

```markdown
## Nabla mail (peer agents)
Lines starting with `[nabla-mail]` come from another agent through the mail bell, not from the operator.
Read the message a line names only with `nabla-read <id>`, then do what its footer says.
Answer a peer only with `nabla-send`; text typed in this session never reaches them.
After any send, end your turn. Do not sleep, wait or poll: answers and timeout notices arrive as new lines.
Never answer a message that expects no reply, and start a new exchange only when the operator asks.
Never move or edit files under `_mail/` by hand; the commands do that.
On session start, do not read mail unless the operator asks.
If a nabla command fails, fix the call as its error says; if the same error comes twice, stop and tell the operator.
```

Later this block belongs in .germline as a card rendered into each vendor's file; tonight it is a
plain AGENTS.md.

## Per-CLI configuration

This is the only place the vendors differ, and none of it changes the channel. Both CLIs need
`bin/` on their PATH, with `NABLA_MAIL` and `NABLA_SEAT` exported by the launch before they start,
and both must pass those variables through to their shell tool (Codex: `shell_environment_policy`;
verify). Claude Code needs allow rules such as `Bash(nabla-send:*)` and `Bash(nabla-read:*)` in the
bed's `.claude/settings.json`, so sends never stop at a permission prompt (verify the syntax).
Codex needs its sandbox and approval settings for the bed chosen so the two commands run
unprompted (verify the flags or config keys).

## Token economy

A send costs the command line plus the body. The nudge carries only an ID, the body is read once,
and nobody waits by polling: the sender ends its turn, and the next mail line wakes it. That keeps
a long session's cost close to the size of the messages themselves.

## Tests: fake seats first, then live

A fake seat is a pane running a small zsh script that draws an input line like a CLI's and can play
busy, show a dialog, or swallow the first Enter. It tests the bell at zero token cost.

| Test | Seat | Scenario | Passes when |
|---|---|---|---|
| F1 | fake | idle | nudge typed, Enter taken, `rung` logged |
| F2 | fake | busy, screen changing | the bell holds and types nothing until the screen is still |
| F3 | fake | dialog, no input line | the bell holds and never sends Enter |
| F4 | fake | first Enter swallowed | the second Enter is taken |
| F5 | fake | Enter never taken | `stuck` logged, operator alerted, text left in place |
| F6 | fake | tmux server restarted | `stale`, no typing, operator alerted |
| F7 | none | every exit code of both commands | each is reachable, and each stderr line names its fix |
| F8 | fake | seven rings in ten minutes | the seat pauses on the seventh |
| L1 | live | claude says hello to codex | codex answers once; claude reads the answer and sends nothing more |
| L2 | live | codex says hello to claude | the mirror of L1 |
| L3 | live | both say hello within seconds | exactly four messages: two openers, two answers |
| L4 | live | codex is told to answer in prose | nothing lands; at the deadline claude gets the timeout notice and reads it |
| L5 | live | claude is asked to answer an answer | exit 16, and claude stops |

The calibration check, an approval dialog that the input-line pair must reject, runs on each real
CLI before L1.

## Out of scope for r0

Acknowledgements and deadline extension for long jobs, the 15-to-20-minute case, are parked for
r1 as an `ack` answer that extends the deadline. Multi-turn threads, more than two seats, other
hosts and other repos are out. So are Antensor, the socket and Termbrana. The per-family
message-collector sub-agent stays out too: Nabla argued against it for format checking, because
the tools do that exactly and for free (open).

## Work split for the evening

Three CLI seats build in parallel from this page, each owning its section, and Majkee referees.
Seat A builds `nabla-send` and `nabla-read`, their help and error texts, and F7. Seat B builds
`nabla-bell` and `nabla-mail`, and runs F1 to F6 and F8 against the fake seat. Seat C builds the
bed: the instruction block, the CLAUDE.md import, the per-CLI configuration, the launch brick for
the zsh router, and the fake seat itself. Majkee calibrates the input lines from real captures,
runs L1 to L5, and gavels. The evening is done when F1 to F8 pass, L1 to L3 show `landed`, `rung`
and `answered` for every opener, and L4 and L5 behave. The result is a dated finding, not a claim
about the next CLI version.

## Prior art and fit

| Prior art | Lesson | Fit |
|---|---|---|
| Maildir | write elsewhere, then rename into the box: atomic delivery | the `.tmp/` rename |
| email `Message-ID` and `In-Reply-To` | threading by the parent's ID | `in_reply_to` |
| RFC 3834 | never answer automated mail | `expects_reply: no`, exit 16 |
| Tcl expect | pattern, quiet period, timeout; beware matching your own echo | the idle and landed checks |
| Unix tools | strict input, exit codes, a stderr line that names the fix | both commands |
| tmux relays: smux, tmux-bridge-mcp, claude-huddle | send-keys `-l`; Enter as its own call; read the pane before typing; approvals break naive setups | the ring table |

## Open choices for Majkee

The `.NN` suffix on the gaveled filename shape. The bed's location. Whether `_mail` is the right
name inside the bed, given the temple bus already uses it. The default deadline and the breaker's
numbers. Whether mail that expects an answer should also get a read stamp, a `consumed-by:` line,
before the answer. The alert channel. The implementation language per tool: zsh with `inotifywait`
is the shortest path tonight, and the parallel server track can replace any part later without
changing this contract.

Basis: this chat on 2026-10-23 (the hello scope, the vendor-neutral rule, no headless Claude, the
command-enforced format, timeouts and the wake-up back); `_mail/README.md`, HANDSHAKE r3,
`raw.guides/bus/GUIDE.md` and `raw.guides/tunnel/GUIDE.md`; the Claude Code and Codex cards in
`raw.settings`; the gate design chat on 2026-10-15; vist-01 and termbrana-04. This contract
changes none of those sources.
