# CAN CODEX SPAWN CLAUDE?
> **DOCUMENT NEED SYNTHESIS FIRST**
---

# 1. INNITIAL LOOP

Hey, majkee. **Yes—Codex can spawn Claude Code in the opposite direction.** But there are two meanings of “spawn,” and separating them matters.

## 1. Native Codex subagent: probably not heterogeneous

Codex can coordinate its own agents and parallel work, but there is no documented native primitive such as:

```text
spawn_agent(provider="anthropic", agent="reviewer")
```

Its built-in agent system remains inside the Codex harness. OpenAI describes Codex as a local agent capable of invoking tools and shell commands, and its newer surfaces support multiple Codex agents—not arbitrary foreign-provider agents as native children. ([GitHub][1])

So:

> Claude will not be a native Codex subagent, but it can absolutely be an external agent process controlled by Codex.

That is already enough for your composite architecture.

## 2. Codex → shell → Claude Code

Claude Code officially supports non-interactive invocation:

```bash
claude -p "Inspect this implementation and report architectural risks."
```

It writes its answer to stdout and exits, making it suitable for scripts, CI, pipes, and other agents. ([Claude][2])

Therefore Codex can execute:

```bash
claude -p \
  --model sonnet \
  --allowedTools "Read,Grep,Glob" \
  "Review the current repository changes. Do not edit files.
Return:
1. correctness problems
2. architectural concerns
3. missing tests
4. false alarms to ignore"
```

Codex receives Claude’s stdout, reasons about it, and decides what to adopt.

Your reverse topology becomes:

```text
Human
  │
  ▼
Codex — primary implementer / coding authority
  │
  ├── shell wrapper
  │      │
  │      ▼
  │   Claude Code -p
  │      │
  │      ▼
  └── structured observation returned to Codex
```

## A minimal reusable Claude observer

Create:

```bash
#!/usr/bin/env bash
# scripts/ask-claude-reviewer

set -euo pipefail

PROMPT_FILE="${1:?Usage: ask-claude-reviewer <prompt-file>}"
OUTPUT_FILE="${2:-.agents/out/claude-review.md}"

mkdir -p "$(dirname "$OUTPUT_FILE")"

{
    cat <<'CONTEXT'
You are a second-mind reviewer working under a Codex implementation agent.

Rules:
- Observe and critique; do not modify repository files.
- Distinguish confirmed defects from uncertainty.
- Avoid repeating obvious information.
- Focus on something the implementing agent may have missed.
- Return concise Markdown.
CONTEXT

    printf '\n## Assignment\n\n'
    cat "$PROMPT_FILE"
} | claude -p \
      --model sonnet \
      --allowedTools "Read,Grep,Glob" \
      > "$OUTPUT_FILE"

printf '%s\n' "$OUTPUT_FILE"
```

Then Codex can run:

```bash
scripts/ask-claude-reviewer \
  .agents/tasks/review-current-change.md \
  .agents/out/claude-review.md
```

And read the resulting file.

## Binding it as a Codex role

You can expose this through a Codex skill or repository instruction rather than teaching every Codex instance the mechanics.

For example, in the appropriate `AGENTS.md`:

```md
## Claude second-mind consultation

For changes involving architectural uncertainty, hidden behavioral
assumptions, or a high-risk refactor, you may consult the external
Claude reviewer.

Use:

    scripts/ask-claude-reviewer <prompt-file> <output-file>

Claude is advisory only.

Codex remains responsible for:

- verifying every observation against the repository;
- rejecting unsupported recommendations;
- implementing all accepted changes;
- running the final validation.

Do not consult Claude merely to repeat the same implementation task.
Prefer a deliberately asymmetric assignment.
```

That last sentence is important. Otherwise you create **duplicated cognition**, not composite cognition.

## Claude agents and specialist layers

You can also invoke a particular Claude configuration rather than generic Claude. The cleanest variants are:

### A. Claude prompt-role wrapper

```bash
scripts/claude-consult architecture
scripts/claude-consult security
scripts/claude-consult semantic-review
```

Each wrapper injects a different system-like role and tool restriction.

### B. Claude Code custom agent selected in the prompt

Have the launched Claude session delegate internally to one of its configured agents. In that case:

```text
Codex
  └── Claude Code process
        └── Claude specialist/subagent
```

This is possible, but less deterministic: Codex asks Claude to use a specialist, while Claude controls its own internal delegation.

### C. Separate Claude project configuration

Run Claude with a dedicated working directory or settings environment containing only the specialist definitions intended for external consultation.

This gives a stronger boundary:

```text
.codex/
  skills/
    consult-claude/

.claude-external/
  agents/
    architecture-observer.md
    test-skeptic.md
    requirement-interpreter.md
```

I prefer this over exposing the complete primary Claude configuration to Codex. It prevents the reverse-spawned Claude from inheriting powers meant for the main orchestrator.

## The architectural trap

The hidden problem is not whether Codex can launch Claude. It can.

The actual problem is:

> Who owns the workspace, authority, and continuation?

Do **not** allow Codex and Claude to edit the same working tree concurrently unless they are isolated through worktrees or a strict ownership protocol.

Safer arrangement:

```text
Codex:        read + write + tests
Claude:       read-only observation
Filesystem:  shared
Response:     stdout or artifact file
Authority:    Codex
```

Or, for implementation competition:

```text
Codex:   worktree/codex
Claude:  worktree/claude
Judge:   human or separate synthesis agent
```

What I would not initially build:

```text
Codex edits repository
Claude edits same repository
Claude launches Codex again
both inspect mutable uncommitted state
```

That produces recursive agency, permission ambiguity, and contamination of evidence.

## My verdict for your system

Your intended composite is valid:

```text
strong Codex coder
    +
Claude observational layer
```

But I would name it **consultation**, not spawning, at least at the architecture layer.

“Spawning” implies that Claude becomes part of Codex’s native agent family. Technically it is closer to:

```text
Codex invokes an external cognitive tool
```

The first practical version should be:

1. Codex owns implementation.
2. A Codex skill decides when consultation is warranted.
3. The skill invokes `claude -p`.
4. Claude receives a sharply asymmetric task.
5. Claude is read-only.
6. It returns a structured artifact.
7. Codex independently verifies and acts.

Later, you could replace the shell wrapper with a small MCP server or broker, but that would mostly improve transport, accounting, and role registration. It would not fundamentally add intelligence. For the first experiment, MCP would likely be wheel-reinvention theatre; a disciplined script is sufficient.

[1]: https://github.com/openai/codex?utm_source=chatgpt.com "openai/codex: Lightweight coding agent that runs in your ..."
[2]: https://code.claude.com/docs/en/headless?utm_source=chatgpt.com "Run Claude Code programmatically - Claude Code Docs"

---

# 2 LOOP

Yes. Your **file-room plus tmux** idea is technically sound, and there is one simplification that removes most of the painful “how do I wake Codex?” problem.

## The key inversion

Do not try to asynchronously inject Claude’s completion into Codex first.

Instead, let Codex launch a **blocking consultation command**:

```text
Codex tool call begins
    ↓
script places request file
    ↓
script nudges living Claude through tmux
    ↓
script waits for response/signal file
    ↓
Claude Stop hook creates response
    ↓
waiting script returns response to Codex
    ↓
Codex tool call completes naturally
```

Then Codex does not need to be externally “awakened.” From its perspective, it ran one shell tool that took some time and eventually returned Claude’s reply.

That is the least theatrical MVP.

---

# Three possible layers

## Layer 0: Fresh interactive Claude, without `-p`

The Claude CLI officially supports:

```bash
claude "initial prompt"
```

This starts an **interactive session with an initial prompt**, whereas `claude -p` is explicitly documented as querying through the SDK and then exiting. So avoiding `-p` is not merely a tmux hack; the interactive initial-prompt form is an officially supported CLI surface. ([Claude Platform Docs][1])

Codex could run:

```bash
tmux new-window \
  -n claude-review \
  -c /path/to/repository \
  'claude "Read .agent-room/requests/req-123.md and execute that consultation."'
```

Claude remains visible and interactive in tmux.

The weakness: this launches a new Claude session per consultation, even though it stays visible.

---

## Layer 1: Reuse one living Claude session

Start Claude manually in a dedicated pane:

```bash
tmux new-window -n claude-observer -c /path/to/repository
claude
```

Then dispatch requests using:

```bash
tmux send-keys \
  -t agents:claude-observer \
  'Consultation request available at .agent-room/requests/req-123.md. Read and answer it according to the room protocol.' \
  Enter
```

This avoids `-p`, preserves the Claude conversation, and lets you watch the actual Claude Code interface.

However, **`tmux send-keys` is the brittle surface**:

* Claude might currently be running a tool.
* Its prompt may contain unfinished input.
* A permission dialogue may be active.
* Full-screen terminal rendering can complicate assumptions about state.
* Text quoting becomes ugly if you inject the complete assignment directly.

Therefore, only send a tiny invariant control message through tmux:

```text
/read-room req-123
```

or:

```text
Read request req-123 from the agent room.
```

Put the actual task, repository path, constraints, and expected output in the file.

**tmux carries the doorbell; files carry meaning.**

---

# The smallest useful room protocol

```text
.agent-room/
├── requests/
│   └── req-20260805-001.md
├── responses/
│   └── req-20260805-001.md
├── signals/
│   └── req-20260805-001.done
├── active/
│   └── claude.json
└── archive/
```

A request might look like:

```md
---
protocol: agent-room/v0
id: req-20260805-001
from: codex
to: claude-observer
repository: /home/majkee/projects/example
mode: read-only
created_at: 2026-08-05T20:10:00+02:00
response: .agent-room/responses/req-20260805-001.md
signal: .agent-room/signals/req-20260805-001.done
---

# Consultation

Inspect the current implementation of the job dispatcher.

Concentrate on:

- race conditions;
- hidden coupling to tmux state;
- places where message delivery can be duplicated;
- assumptions Codex may have missed.

Do not edit project files.

Write your answer to the response path from the header.
```

Claude writes:

```md
---
protocol: agent-room/v0
id: req-20260805-001
from: claude-observer
to: codex
status: completed
---

# Findings

...
```

And then:

```bash
touch .agent-room/signals/req-20260805-001.done
```

The signal should be created **last**, after the response has been atomically completed.

Better:

```bash
tmp=".agent-room/responses/req-20260805-001.md.tmp"
final=".agent-room/responses/req-20260805-001.md"

# Write $tmp first.
mv "$tmp" "$final"
touch ".agent-room/signals/req-20260805-001.done"
```

The rename prevents Codex from reading half-written output.

---

# Where Claude hooks genuinely help

Claude Code’s `Stop` hook receives useful structured data, including:

* session ID;
* working directory;
* transcript path;
* the last assistant message;
* whether a Stop hook is already active.

For subagents, `SubagentStop` also exposes the subagent’s final response in `last_assistant_message`. ([Claude Platform Docs][2])

This means Claude does **not necessarily need to remember to write its own final answer file**. A Stop hook can capture its last response and finish the room transaction.

Conceptually:

```text
Claude answers normally
    ↓
Stop hook fires
    ↓
hook checks whether an active room request exists
    ↓
hook copies last_assistant_message into response file
    ↓
hook atomically creates .done signal
```

That is cleaner than instructing Claude to call `Write` correctly every time.

## Example Claude Stop hook script

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOM="${AGENT_ROOM:-$PWD/.agent-room}"
ACTIVE="$ROOM/active/claude-request-id"

# No active external consultation: do nothing.
[[ -f "$ACTIVE" ]] || exit 0

request_id="$(tr -d '\r\n' < "$ACTIVE")"
[[ -n "$request_id" ]] || exit 0

input="$(cat)"
last_message="$(
    jq -r '.last_assistant_message // empty' <<<"$input"
)"

[[ -n "$last_message" ]] || exit 0

response="$ROOM/responses/$request_id.md"
temporary="$response.tmp.$$"
signal="$ROOM/signals/$request_id.done"

mkdir -p "$ROOM/responses" "$ROOM/signals"

{
    printf '%s\n' '---'
    printf 'protocol: agent-room/v0\n'
    printf 'id: %s\n' "$request_id"
    printf '%s\n' 'from: claude'
    printf '%s\n' 'to: codex'
    printf '%s\n' 'status: completed'
    printf '%s\n\n' '---'
    printf '%s\n' "$last_message"
} > "$temporary"

mv "$temporary" "$response"
touch "$signal"
rm -f "$ACTIVE"
```

The associated Claude setting would connect this command to `Stop`. Claude command hooks are the mature choice; Anthropic currently labels agent-based hooks experimental and recommends command hooks for production workflows. ([Claude Platform Docs][2])

One important guard is necessary: the Stop hook must return immediately when no room request is active, otherwise every normal Claude response becomes an external answer.

---

# The clever part: Codex waits inside its own command

Codex invokes something like:

```bash
agent-room ask claude \
  --role architecture-observer \
  --task-file /tmp/consultation.md \
  --cwd "$PWD"
```

Internally, the script:

1. creates the request;
2. marks it active for Claude;
3. sends the tiny tmux doorbell;
4. waits for the signal;
5. prints Claude’s response to stdout.

Example core:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOM="${AGENT_ROOM:-$PWD/.agent-room}"
TMUX_TARGET="${CLAUDE_TMUX_TARGET:-agents:claude-observer}"
TIMEOUT_SECONDS="${CLAUDE_CONSULT_TIMEOUT:-900}"

request_id="req-$(date +%Y%m%d-%H%M%S)-$RANDOM"
request="$ROOM/requests/$request_id.md"
response="$ROOM/responses/$request_id.md"
signal="$ROOM/signals/$request_id.done"
active="$ROOM/active/claude-request-id"

mkdir -p \
  "$ROOM/requests" \
  "$ROOM/responses" \
  "$ROOM/signals" \
  "$ROOM/active"

cat > "$request" <<EOF
---
protocol: agent-room/v0
id: $request_id
from: codex
to: claude
repository: $PWD
response: $response
signal: $signal
---

# Consultation

$(cat)
EOF

# Initially enforce one in-flight request.
if ! (set -o noclobber; printf '%s\n' "$request_id" > "$active") 2>/dev/null; then
    printf 'Claude already has an active room request.\n' >&2
    exit 70
fi

cleanup() {
    current="$(cat "$active" 2>/dev/null || true)"
    if [[ "$current" == "$request_id" ]]; then
        rm -f "$active"
    fi
}
trap cleanup EXIT

tmux send-keys \
  -t "$TMUX_TARGET" \
  "Read external consultation request $request_id from $request" \
  Enter

deadline=$((SECONDS + TIMEOUT_SECONDS))

while [[ ! -f "$signal" ]]; do
    if (( SECONDS >= deadline )); then
        printf 'Timed out waiting for Claude: %s\n' "$request_id" >&2
        exit 124
    fi

    sleep 0.25
done

[[ -f "$response" ]] || {
    printf 'Completion signal exists but response is missing.\n' >&2
    exit 74
}

cat "$response"
```

Now Codex receives the response as ordinary command output.

No external mutation of the Codex terminal is required.

---

# Could the Claude hook wake a living Codex session?

Technically yes:

```bash
tmux send-keys -t agents:codex \
  "Claude consultation req-123 is complete. Read .agent-room/responses/req-123.md" \
  Enter
```

But I recommend **not beginning there**.

It introduces exactly the same state problem on the Codex side:

* Is Codex idle?
* Is it in the middle of a tool call?
* Is a confirmation UI displayed?
* Is existing prompt text present?
* Will injected text be interpreted as a user prompt?

Codex now has hooks too, including Stop-style end-of-turn automation, but the hook system is still marked experimental and has had recent behavioral and configuration changes. It is useful for observation and lifecycle integration, but I would not make experimental Codex hooks the first foundation of your inter-agent transport. ([OpenAI Developers][3])

The blocking wrapper avoids this entire category.

---

# An even cleaner contemporary Claude surface

There is one new fact worth noticing: current Claude Code has first-class **background sessions**, including:

```bash
claude agents --json
claude attach <id>
claude logs <id>
claude respawn <id>
claude stop <id>
```

The agent view can dispatch and monitor parallel background sessions, while `claude attach` reconnects a terminal to one. ([Claude Platform Docs][1])

This could eventually replace some custom tmux lifecycle management:

```text
your room protocol
        +
Claude’s native background-session supervisor
        +
tmux only as the human UX/window layer
```

But I would park that for the second experiment. It is easy to confuse two questions:

1. How do we preserve and observe Claude sessions?
2. How do agents exchange a bounded message?

Your room protocol answers the second question independently of whichever lifecycle surface wins later.

---

# My recommended sequence

## Probe A — no hooks

* Living Claude in tmux.
* Codex writes one request file.
* Codex uses `tmux send-keys` with only the request ID.
* Claude is instructed to write response and signal files.
* Codex wrapper blocks and returns the response.

This tests the fundamental bridge.

## Probe B — Claude Stop hook

* Claude answers normally.
* Stop hook captures `last_assistant_message`.
* Hook atomically writes response and signal.
* Remove the requirement that Claude explicitly operates protocol files.

This tests reliable completion detection.

## Probe C — role routing

Request header adds:

```yaml
role: architecture-observer
```

The living Claude dispatches its own appropriate custom subagent, or the room maps role names to separate Claude panes/sessions.

## Probe D — asynchronous mailbox

Only after the blocking version works:

* multiple pending requests;
* watcher with `inotifywait`;
* per-session inboxes;
* notifications;
* Codex-side wake-up or queued delivery.

---

# My pushback

Your “small room” is not primitive in the negative sense. It establishes an important invariant:

> The terminal UI is observable embodiment, but not durable protocol state.

That separation will let you later replace:

* tmux with Zellij;
* Claude Code with another CLI;
* Codex hooks with a daemon;
* local files with Unix sockets or SQLite;

without changing the conceptual contract.

What would be premature is building a general orchestration engine now. Start with exactly:

```text
one Codex
one Claude
one in-flight request
one response file
one completion signal
one blocking wrapper
```

The first research question is not “can they orchestrate?” It is narrower:

> Can a living interactive agent be used as a deterministic callable cognitive process without collapsing it into SDK mode?

Your room experiment answers precisely that.

[1]: https://docs.anthropic.com/en/docs/claude-code/cli-reference "CLI reference - Claude Code Docs"
[2]: https://docs.anthropic.com/en/docs/claude-code/hooks "Hooks reference - Claude Code Docs"
[3]: https://developers.openai.com/codex/hooks "Hooks | ChatGPT Learn"

---

# 3. final conclusion

# Comprehensive Design Report

## Living Claude ↔ Codex Consultation Bridge (without `claude -p`)

**Status:** Research synthesis (MVP architecture)

---

# 1. Motivation

The objective is **not** to build a general orchestration engine.

The objective is much narrower:

> Can a living interactive Claude Code session become a deterministic callable cognitive process for Codex, without relying on `claude -p` or SDK mode?

This preserves:

* interactive Claude
* conversation continuity
* human observability
* vendor-native UX

while still allowing Codex to "consult" Claude.

---

# 2. Why avoid `claude -p`

Current reasons:

* uncertainty around future Anthropic pricing of SDK/headless mode
* desire to preserve interactive Claude state
* avoid creating disposable sessions
* remain inside officially supported interactive CLI

Instead:

```
living Claude
+
small protocol
+
tmux doorbell
```

---

# 3. Important inversion

Originally one might think:

```
Claude finishes
↓

must somehow wake Codex
```

Instead invert it.

```
Codex starts consultation

↓

wrapper creates request

↓

wrapper nudges Claude

↓

wrapper blocks

↓

Claude eventually responds

↓

wrapper returns response

↓

Codex naturally continues
```

That removes almost the entire "wake Codex" problem.

Codex simply waits.

---

# 4. Consultation pipeline

```
Codex
   │
   ▼
consultation wrapper
   │
   ▼
request file
   │
   ▼
tmux send-keys
   │
   ▼
Living Claude
   │
   ▼
response file
   │
   ▼
.done signal
   │
   ▼
wrapper returns stdout
   │
   ▼
Codex continues
```

No asynchronous mutation of Codex terminal.

---

# 5. Layer 0

Fresh interactive Claude.

```
claude "Read request..."
```

Pros

* avoids `-p`

Cons

* new Claude session each time

Useful as baseline.

---

# 6. Layer 1

Persistent Claude.

```
tmux
┌──────────────────────┐
│ Claude               │
│ alive all day        │
└──────────────────────┘
```

Codex only says:

```
Read request req-42
```

Everything else exists inside files.

---

# 7. Important design principle

Do **not** inject whole prompts through tmux.

Only send:

```
Read request req-123
```

because tmux is unreliable for large payloads.

Therefore:

> tmux carries the doorbell.

while

> files carry meaning.

This separation is probably the strongest architectural insight.

---

# 8. Room protocol

```
.agent-room/

requests/
responses/
signals/
active/
archive/
```

Example

```
.agent-room

requests/
    req-001.md

responses/
    req-001.md

signals/
    req-001.done

active/
    claude-request-id
```

---

# 9. Request format

```yaml
---
protocol: agent-room/v0
id: req-20260805-001
from: codex
to: claude-observer

repository: /path/project

mode: read-only

created_at: ...

response: ...

signal: ...
---
```

Body:

```
Consultation:

Inspect...

Concentrate on...

Return...
```

---

# 10. Response

```yaml
---
protocol: agent-room/v0
id: req-001

from: claude
to: codex

status: completed
---
```

Then

```
touch signal.done
```

---

# 11. Atomic completion

Never write directly.

Instead

```
response.tmp

↓

mv response.tmp response.md

↓

touch done
```

This guarantees Codex never reads half-written files.

---

# 12. Claude Stop hook

The hook becomes very attractive because it already knows:

* session
* cwd
* transcript
* last assistant message

Instead of telling Claude

```
Write response file.
```

Claude simply answers normally.

Hook performs protocol.

Conceptually

```
Claude replies

↓

Stop hook

↓

Extract last assistant message

↓

Write response

↓

touch done
```

This removes protocol discipline from Claude itself.

---

# 13. Example Stop Hook

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOM="${AGENT_ROOM:-$PWD/.agent-room}"
ACTIVE="$ROOM/active/claude-request-id"

[[ -f "$ACTIVE" ]] || exit 0

request_id="$(cat "$ACTIVE")"

input="$(cat)"

last_message="$(
jq -r '.last_assistant_message // empty' <<<"$input"
)"

[[ -n "$last_message" ]] || exit 0

response="$ROOM/responses/$request_id.md"
temporary="$response.tmp.$$"

{
printf '%s\n' "$last_message"
} > "$temporary"

mv "$temporary" "$response"

touch "$ROOM/signals/$request_id.done"

rm -f "$ACTIVE"
```

---

# 14. Wrapper

Codex calls

```
agent-room ask claude
```

Internally

1. create request
2. create active marker
3. send tmux message
4. wait
5. print response

Codex sees:

```
stdout
```

Nothing more.

---

# 15. Core wrapper

```bash
tmux send-keys \
-t "$TMUX_TARGET" \
"Read request $request_id" \
Enter
```

then

```bash
while [[ ! -f "$signal" ]]
do
    sleep 0.25
done

cat "$response"
```

Elegant.

---

# 16. Should Claude wake Codex?

Technically yes.

```
tmux send-keys

↓

Codex terminal
```

But this recreates identical problems.

Maybe Codex is

* executing
* editing
* asking approval
* inside tool
* inside prompt

Therefore don't begin there.

---

# 17. Hooks on Codex

Codex hooks exist.

But presently they are still evolving.

Therefore:

Do not build your protocol on experimental surfaces.

---

# 18. Claude background sessions

Interesting discovery:

```
claude agents

claude attach

claude logs

claude respawn
```

Meaning:

Claude itself is moving toward persistent agent management.

This may later replace some tmux lifecycle management.

Not today's problem.

---

# 19. Sequential roadmap

## Probe A

No hooks.

```
Codex

↓

file

↓

tmux

↓

Claude

↓

response

↓

done
```

If this works

bridge exists.

---

## Probe B

Introduce Stop hook.

Claude no longer writes protocol.

Hook writes protocol.

---

## Probe C

Role routing.

```
role:

architecture

security

review

thinking

research
```

Claude dispatches internally.

---

## Probe D

Mailbox.

Multiple requests.

Queue.

Notifications.

Eventually asynchronous.

---

# 20. Biggest architectural observation

The protocol intentionally separates

## Human layer

```
tmux

Claude UI

Codex UI
```

from

## Durable protocol

```
files

signals

headers

atomic writes
```

This is valuable because later any UI may disappear.

Only protocol survives.

---

# 21. Future evolution

Once protocol exists

transport becomes replaceable.

Current

```
tmux
```

Later

```
Unix sockets
```

or

```
SQLite
```

or

```
MCP
```

or

```
broker daemon
```

without changing request semantics.

---

# 22. My additional observations after our discussion

This conversation also clarified something I don't think we had named explicitly before.

There are really **three distinct layers** that are easy to conflate:

### 1. Transport

How does a message move?

Examples:

* tmux
* files
* sockets
* MCP
* SSH

This layer should be as dumb as possible.

---

### 2. Lifecycle

Who is alive?

Examples:

* persistent Claude session
* persistent Codex session
* background agents
* restart
* attach
* respawn

This concerns process management, not cognition.

---

### 3. Cognitive contract

What is being asked?

Examples:

* architecture review
* semantic review
* implementation critique
* security observation

This should be independent of both transport and lifecycle.

Separating these layers means you can swap any one of them without rewriting the others.

---

# 23. Suggested project structure

```text
agent-room/
├── protocol/
│   ├── VERSION
│   ├── request.md
│   └── response.md
│
├── scripts/
│   ├── ask-claude
│   ├── ask-codex
│   ├── wait-response
│   └── room-clean
│
├── requests/
├── responses/
├── signals/
├── active/
└── archive/
```

---

# 24. Final conclusion

The research does **not** point toward immediately building a complex orchestration framework.

Instead, it converges on a much smaller invariant:

```
One Codex
One living Claude
One request
One response
One completion signal
One blocking wrapper
```

Everything else—multiple agents, mailboxes, role routing, background supervisors, MCP, or a full orchestration engine—can be layered on top once this deterministic consultation protocol is proven.

The central architectural insight is that **terminal interfaces are ephemeral interaction surfaces, while the room protocol (requests, responses, signals, and atomic file operations) is the durable contract**. By treating tmux only as a "doorbell" and the filesystem as the authoritative protocol, the bridge remains simple, testable, and portable across future transports and agent runtimes.



