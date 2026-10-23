crawl: v0-zip · writer: eagle (mechanical, 2026-10-22 ~07:00 CEST) · landed verbatim by oraculum(cSharp) X3 head · for: Houston arc.r2 + assay

Source (Majkee's folder, untouched by the head):
- /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md — sha256 00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0 (head, 07:12)
- /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.zip — sha256 a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7 (head, 07:12)

Isolated extraction (session-temporary; durable cite = the zip + its sha256 above):
S = /tmp/claude-1000/-home-hruzam-unikuklatrix-nablarva/46c2dcf6-0264-4d06-8316-77fe12e0fa0f/scratchpad/apology-zip
Nothing from the archive was executed.

Below: eagle's report, verbatim.

---

STEP 1 unzip -l
```
Archive:  .../raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    23437  2026-10-17 18:14   nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
     4327  2026-10-17 18:14   nabla-tmux-architecture/diagrams/events.svg
     4186  2026-10-17 18:14   nabla-tmux-architecture/diagrams/layers.svg
     3455  2026-10-17 18:14   nabla-tmux-architecture/diagrams/messages.svg
     4689  2026-10-17 18:14   nabla-tmux-architecture/diagrams/tree-and-mycelium.svg
     3143  2026-10-17 18:14   nabla-tmux-architecture/diagrams/what-loads-when.svg
---------                     -------
    43237                     6 files
```
Path check: no absolute or `..` entries.

STEP 2 extraction
The directory S was created empty (0 existing entries). I extracted with `unzip -n`, which inflated all 6 files under S/nabla-tmux-architecture/ (the .md plus diagrams/*.svg).

STEP 3 sha256
```
00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0  S/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
936a483d95b8b2ecf4623a7b2f27af559cd4a2630318a4d3684df966a050abc6  S/nabla-tmux-architecture/diagrams/what-loads-when.svg
985cd8c9ed3dd5e279b1453dd4e79e2fc8de2401a03680412a2b0af98daf4aea  S/nabla-tmux-architecture/diagrams/tree-and-mycelium.svg
7db75b063b6c8c7a58078f6e9d4eab55e7347e324c75a25ce5814b96abb78b2b  S/nabla-tmux-architecture/diagrams/messages.svg
12211e4ce39ec1d220a4ce32561c9f95d95661b1151637d0ce365ddfaecc49d4  S/nabla-tmux-architecture/diagrams/layers.svg
1fe20f9c21c29d30e71d6f8386a50f0070402c00b57351e092a049d3993064a1  S/nabla-tmux-architecture/diagrams/events.svg
```
wc (lines, bytes):
```
  382 23437 S/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
    1  3143 S/.../diagrams/what-loads-when.svg
    1  4689 S/.../diagrams/tree-and-mycelium.svg
    1  3455 S/.../diagrams/messages.svg
    1  4186 S/.../diagrams/layers.svg
    1  4327 S/.../diagrams/events.svg
  387 43237 total
```

STEP 4 headings (.md; there are no .txt or .html files)
```
1:# Nabla.Tmux — Architecture Draft v0
5:## The idea
13:## Principles
28:## Layers
37:## If you think in Laravel
60:## Tree and mycelium
69:## What loads when
78:## Code layout and file naming
118:## Substrate
141:## Events
150:### Record format
164:### Lifecycle map, first pass
186:## Messages: relay and popups
199:## Runbooks and the control pane
207:## Which language goes where
222:## Decisions and when to revisit them
237:## Migration path
251:## Skeleton
336:## Study list
362:## Glossary
```
(Lines 258–324 that start with `#` are comments inside code blocks, not headings.)

SVG text labels

what-loads-when.svg:
```
A new shell reads three small files; a call reads only its own path
New interactive shell
A call from an alias, key, popup or hook
.zshrc
one Nabla line: source shell/init.zsh
shell/init.zsh
adds bin/ to PATH, sources boot/env.zsh
and shell/aliases.zsh
Ready
no gate, brick or service has been read
bin/nabla
router: finds bin/nabla-pane and execs it
bin/nabla-pane
gate: sources env.zsh, marks brick names
checks input and picks the verb
pipes/pane/pane-spawn
read now, on its first call; siblings stay unread
```
tree-and-mycelium.svg:
```
Commands flow down the tree; facts spread through the substrate
Solid arrows carry commands. Dashed arrows carry facts.
bin/nabla
router: maps names to gates
nabla-pane
gate of the pane pipe
nabla-relay
gate of the relay pipe
nabla-runbook
gate of the runbook pipe
pane-spawn
brick: opens a pane
relay-doorbell
brick: nudges a pane
runbook-step
brick: runs one step
Substrate (shared files)
bus/ · events/*.jsonl · sessions/ · status.md
Bricks write facts here; whoever cares reads them
tmux.pane.created
bus.doorbell.rung
runbook.step.done
read
never brick to brick
```
messages.svg:
```
Every message is a file; tmux only rings the doorbell
Agent output and your prompts take the same path through the bus.
Agent A pane
its Stop hook writes the turn’s
final text into the bus
You, in a popup
compose a prompt for an agent
and pick who receives it
Bus: one file per message
content stays in files; a pane only ever receives the doorbell
Classifier
addressed: passes through
the rest: rules, model optional
Agent B pane
doorbell: read this file
You
shown in status or a popup
writes output
writes the prompt
new message
for an agent
for you, or unsure
```
layers.svg:
```
Only boot loads with the shell; the rest waits to be called
Solid arrows carry control. Dashed arrows carry information.
1 · Boot
Loads with every interactive shell: constants, PATH, aliases
Registers names and executes nothing
2 · Living tissue
Always on, outside the shell
tmux hooks, CLI hooks, watcher
Notices and writes events only
3 · Gates
Executables in bin/, read when called
Called by an alias, key, popup or hook
Check input, resolve the target, dispatch
4 · Bricks
Autoload functions
Read on first call
One side effect each
5 · Services
Python, called by gates
Data in, JSON out
Never touch tmux
6 · Substrate
Files: bus, events, state, status
The only sideways channel
Outlives every process
you call a name
dispatch
ask, get JSON
write events
read
write state and events
```
events.svg:
```
Every source writes the same record; readers can change later
Dashed parts come later. Nothing above them has to change.
tmux hooks
pane exited or died,
bell, silence
CLI hooks
session start, end,
turn done, attention
Runbook runner
step done or failed,
run finished
Bus and popups
message written,
prompt composed
Event log: events/*.jsonl
one JSON line per event, the same fields from every source
append-only, so any view can be rebuilt by replaying it
Today: a small watcher
tail -F on the log, or inotifywait
runs the few reactions you have
Later: a broker
one Go or Rust binary on the same records
adds ordering, retries, subscriptions
Reactions
update status.md, which the control pane shows
ring the doorbell: tell a pane which file to read
```

STEP 5 cmp
Compared S/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md with /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md. Result: identical.

I wrote nothing outside S, did not touch the repo, and ran nothing from the extracted files.
