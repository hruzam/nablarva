from-nabla.Tmux.chatbot ---
From Nabla (Claude) in the Nabla.Tmux chat · 2026-10-18
Personal design brief requested by Majkee · proposed, not implemented
Reads with: termbrana-04-sublime-ide.md and the Sella-v.0.1 collection

# VIST — vendor-invariant session telemetry: principle and possible applications

Marks used below: *decided* means Majkee chose it in conversation; *proposed* means Nabla's
suggestion, open to kick, bend or veto; *open* means not settled; *verify* means tool or vendor
behaviour not checked against current documentation in this sitting.

## The recommendation

Build Antensor as a read-only sensor. It watches what vendor CLIs show in tmux and turns that
into small, neutral, versioned observations: the VIST events. It cannot act. A separate
controller decides, and a separate, separately authorized actuator rings the doorbell. Every
observation is evidence with a confidence, never proof of identity, acceptance or completion.
Vendor knowledge lives in data, the signature registries, which a canary re-qualifies on each
CLI release. The names and the passive approach are decided; the rest of this brief is proposed
unless marked.

## Names

| Name | Kind | Meaning |
|---|---|---|
| VIST | protocol, factory-standard name | Vendor-Invariant Session Telemetry: neutral observations of agent sessions, recovered from outside without the agent's cooperation. |
| Antensor | device, working name | Nablarva's implementation of VIST. Antenna: it senses without touching. Tensor: one object, described from different coordinate frames. |

The tensor reading is a design rule. Claude Code, Codex and any later CLI are different
coordinate frames, with different screens, spinners and dialogs. The agent's state underneath
(busy, idle, waiting for approval) is the invariant object, and Antensor recovers it from
whichever frame it is in. So the invariant state set stays small: a state that only one vendor
has is carried as a vendor attribute on a neutral state, never added as a new invariant.

## The principle: MCP turned inside out

MCP gives the agent tools on the agent's terms. The model decides to call outward through a
formal protocol, and the vendor has to support it. VIST observes the agent on the operator's
terms. Nothing is asked of the agent, and it does not know it is watched.

| | MCP | VIST |
|---|---|---|
| Direction | agent calls outward | observer looks inward |
| Initiative | the model chooses each call | continuous, observer-driven |
| Cooperation | vendor support plus the model's choice | none |
| Context cost | tool schemas in every turn | zero |
| Contract | a formal specification | the screen, which vendors change freely |
| A stalled agent | invisible; silence looks like nothing | visible |
| Why it acts | known, if the agent says so | unknown |

The standard names for what Antensor is: black-box observation, a sidecar, and an
anti-corruption layer in the domain-driven-design sense, a translator that keeps each vendor's
shape out of the rest of the system. The two directions complement each other. A thin
cooperative channel (a small MCP tool, or a status file the agent writes) could carry what only
the agent knows, such as "blocked, need credentials", while VIST remains the record of what
visibly happened (open).

## Where VIST sits: sensor, controller, actuator

```text
   vendor CLIs in tmux panes                 Termbrana, RUNBOOK, STATUS
              |                                          |
              v                                          v
       +------------+  observations  +------------+  intents  +------------+
       |  Antensor  | -------------> | controller | --------> |  actuator  |
       |  (sensor)  |    (vist.*)    | (decides)  |           | (doorbell) |
       +------------+                +------------+           +------------+
              ^                             ^                       |
              |          receipts           |        receipts       |
              +-----------------------------+-----------------------+
                                                                    |
                                                                    v
                                                        short nudge into a pane
```

Each component emits one kind of message: Antensor emits observations, the controller intents,
the actuator receipts. Receipts go to both the controller and Antensor. VIST names only
observations; intents and receipts get their own namespaces.

The reasons are old scars. An actor's own actions show up in what it observes: the classic Tcl
expect bug is sending `echo done`, waiting for `done`, and matching the echoed command instead
of its output. Chat bots answering their own messages and two vacation auto-replies mailing each
other forever are the same bug. A pure sensor can also be replayed against recordings with no
side effects, which is what makes the canary possible. And one writer gives one place for rate
limits, a pause switch, dry-run and the audit log.

| Rule | Mechanism | Prior art |
|---|---|---|
| Antensor never writes | no input into panes, no writes into vendor logs | |
| One pane writer | the actuator; Ovitmugen stays a view manager under its no-injection rule | |
| Self-caused changes are tagged | each action carries an ID and its receipt names the exact doorbell string, so Antensor recognises the echo | RFC 3834 `Auto-Submitted` |
| The controller is level-triggered | it compares the plan with what is observed now: duplicate events change nothing, a missed one is caught on the next pass | Kubernetes reconcilers |
| Damping | a state must hold for a quiet period before anything acts | debounce |
| Runaway stop | too many actions on one pane in a short window pause that pane and alert Majkee | circuit breaker |
| Staged trust | the actuator first only logs, then asks approval for each action, then acts alone | shadow mode |

## What VIST can and cannot establish

The gate design's state ladder (2026-10-15 chat) and the pending views in
note.myshell.history-and-attachments.sella-v.0.1.md both need evidence for each step. VIST
supplies some of it.

| Step | VIST evidence | Not established by VIST |
|---|---|---|
| living | occupant signature (process plus screen) and `idle` | that the occupant is the intended collaborator |
| doorbell | the actuator's receipt plus the self-caused screen change | that the nudge was read |
| accepted | `busy` soon after the receipt, weak | the accepted scope, which needs the recipient's explicit acceptance |
| working | `busy`, `needs_approval`, `needs_input` | progress or quality |
| done | `idle` after `busy`, agreeing with a vendor turn-end hook | task completion, which needs the correlated return |

This answers part of Astrobley's challenge, that a live pane is not proof of recipient identity
or readiness, with evidence rather than proof: before a doorbell the controller can require the
expected occupant in `idle`, and hold delivery on a mismatch.

## Antensor: sources and pipeline

Three passive sources feed one neutral stream.

| Source | Gives | Limits |
|---|---|---|
| tmux: `capture-pane -p -e` snapshots, pane metadata such as `pane_current_command` and `pane_pid`, later a control-mode client | UI state (idle, busy, dialogs, errors) and occupant evidence | the screen contract changes with every vendor UI |
| vendor transcript files: Claude Code and Codex keep JSONL logs | structured turns and tool calls | vendor format; tail read-only and link rather than copy (verify paths and schema) |
| vendor hooks: Claude Code `Stop`, `Notification`, `SessionStart`, `SessionEnd`; Codex `notify` | lifecycle edges | vendor-specific; calibration first (verify names) |

Majkee's own zsh bricks are not a VIST problem. They can report exact events straight to the
bus, so there is nothing to guess; passive observation is for programs he does not control.

The pipeline is capture, snapshot, match, fuse, emit. tmux already emulates the terminal, so
`capture-pane` returns the rendered screen and Antensor needs no emulator of its own; pyte
matters only for replaying raw bytes outside tmux. Start by polling the watched panes at a
modest rate, and add a control-mode client with `%output` notifications only when polling cost
shows. Attach that client with `-f read-only,ignore-size` so it can neither type nor resize
windows (verify that read-only also blocks commands in control mode on the installed tmux).

Signatures anchor on stable UI elements such as fixed labels, positions and colours, never on
prose the agent writes, and every match needs a quiet period and a timeout. A screen that
matches nothing is `unknown`, never a guess. Occupant evidence combines the pane's process with
the screen signature (verify the process names each CLI shows). Fusion lowers confidence when
sources disagree and logs the disagreement for tuning. A pane is identified by host, tmux
socket, server incarnation (server PID plus start time) and pane ID, so a reused ID after a
server restart cannot silently reconnect.

The optional local LLM (Gemma 4 E2B) belongs on the sensor side. It labels observations, for
example CLI-to-CLI versus CLI-to-human, and never acts; with a timeout and a deterministic
fallback, its absence makes labels coarser and breaks nothing. Its optional status is decided;
the placement is proposed.

## Event model v0

A minimal envelope, one JSON object per line. Field names are proposals, and the existing bus
format wins wherever they overlap.

```json
{"kind":"observation","type":"vist.agent.idle","v":0,
 "id":"obs-20261018-140322-7f3a","ts":"2026-10-18T14:03:22.418+02:00",
 "pane":{"host":"office","socket":"default","server":"4182@2026-10-18T08:00","pane":"%7"},
 "occupant":{"vendor":"claude-code","signature":"claude-code@r14"},
 "confidence":0.92,
 "evidence":{"snapshot":"sha256:9c1e2b...","sources":["screen","hook:Stop"]},
 "caused_by":null,"seq":1187}
```

| Type | Meaning |
|---|---|
| `vist.session.appeared`, `vist.session.vanished` | a known CLI occupant is detected in, or gone from, a pane |
| `vist.agent.busy` | working: a spinner or progress is visible |
| `vist.agent.idle` | the input prompt is ready and the quiet period has passed |
| `vist.agent.needs_approval` | an approval dialog is visible |
| `vist.agent.needs_input` | the agent waits for human text |
| `vist.agent.error` | a visible error state |
| `vist.agent.unknown` | the screen matches no signature |

The two session types hold the place for the lifecycle group, which is still to be mapped
(open). `seq` rises monotonically per pane so a consumer can detect gaps. `caused_by` names the
receipt when Antensor attributes a change to the animal's own doorbell.

## Registries: the programmatic part and the source part

The split is Majkee's (decided). Stable code sits on one side: capture, snapshot, the matcher
engine, fusion, the envelope and the router. Versioned data sits on the other: the signature map
per vendor and version range, the invariant state set, the event-to-handler map and the doorbell
vocabulary. Each data file has a schema and its own tests, recordings with their expected
observation sequences. The files live in git, reload hot, and fall back to the last good version
when validation fails. One rule keeps the split honest: a vendor update may only touch data. If
it forces a code change, the engine is missing something general, and that gets fixed once in
the engine.

Recordings capture everything that was on screen, secrets included. Redact before a recording
becomes a committed test fixture, and keep raw logs local with mode 0600.

## Canary

The idea is Majkee's (decided): a cron job that notices a new CLI release and works out what it
means for the projection. The proposed shape: watch npm or GitHub releases per CLI, pull the
changelog, and have an agent rate the impact against that vendor's signature map, as advice
only. Then install the new version in isolation, run a scripted session in a test pane, and
check that Antensor reports the expected states in order. Production stays pinned to the last
version that passed, and every stored recording is replayed for regression. A pass earns a
dated finding for that version, not a claim about the next one.

## Prior art and fit

| Prior art | Lesson | Fit |
|---|---|---|
| Tcl expect | pattern plus timeout plus quiet period; the echo gotcha | direct; the reason for echo tagging |
| mainframe screen scraping, RPA | anchor on stable labels; keep an explicit unknown | direct, for signature design |
| tmux `capture-pane` and control mode | the multiplexer already holds the rendered screen | direct; may remove the need for an own emulator |
| OSC 133 shell integration | exact prompt and command marks | only panes Majkee controls; vendor TUIs will not emit them |
| Language Server Protocol | capability handshake, versioned messages | adapters and the bus, not observation |
| RFC 3834 `Auto-Submitted` | tag automated output so responders ignore it | self-caused tagging |
| Kubernetes controllers | level-triggered, idempotent reconcile | the controller, not Antensor |
| debounce, circuit breaker | damp flicker, stop runaways | controller and actuator |
| mail delivery: retry versus dead-letter | temporary versus permanent failure | already in the gate design |
| vendor JSONL transcripts | a structured passive record | a second source, vendor-specific |

## Possible applications

| Application | What VIST supplies |
|---|---|
| doorbell readiness | the expected occupant in `idle` before a nudge; delivery held on mismatch |
| liveness | process alive plus screen change as a heartbeat that needs no cooperation, for the gate design's liveness check |
| CLI-to-CLI relay | a turn end in one pane cues a nudge for the other to read the handoff file: the relay Majkee did by eye, together with the optional LLM label |
| schedule runner | sequential blocks advance on turn end, level-triggered |
| approval routing | `needs_approval` reaches Majkee in the control panel or on the phone, queued by urgency; no auto-approve by default |
| control-panel status | live per-pane state beside STATUS, display only; STATUS still owns project position |
| stall and loop alarms | busy too long without screen change, or repeating screens |
| Termbrana pending views | evidence for the move from Awaiting receipt to Awaiting return, never acceptance |
| context pressure | where a CLI shows its context use, an early cue to ask for a cold-start handoff card before compaction (verify per CLI) |
| canary oracle | expected observation sequences as the pass condition for a new CLI version |
| any interactive TUI | installers, REPLs, database consoles, ssh sessions: the same engine with a new signature map |

## Limits and non-goals

VIST cannot know why an agent does anything, and it can be wrong when a vendor changes its
interface between canary runs. Its observations authorize nothing and form no security boundary.
It reads screens, so its cost grows with the number of watched panes and the snapshot rate;
coalesce per pane and bound the rate. It replaces neither MCP nor the recipient's explicit
acceptance and return.

## Open choices for Majkee

Whether hooks stay a permanent source or only calibrate signatures until Antensor agrees with
them reliably. Whether Antensor runs inside the socket daemon or as its own process that
publishes to it; proposed is its own process, so a matcher crash cannot take the bus down.
Whether confidence is a number or three levels. Snapshot cadence and quiet-period defaults per
vendor. Whether to add the thin cooperative channel. Where recordings live and who redacts them.
The session lifecycle group.

Basis: this chat on 2026-10-18 (names, principle, the observe/act split, the canary idea,
registries); the prompt-automatization gate chat on 2026-10-15 (doorbell and content split,
state ladder, retry and dead-letter); the Sella-v.0.1 collection (README,
note.myshell.history-and-attachments) for pending views, attachment identity and Astrobley's
challenge. This brief changes none of those sources.
