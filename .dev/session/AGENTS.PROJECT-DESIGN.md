---
name: nablarva-project-design
what-is-it: Living design wrapper for nabLarva and its organs
status: working-draft
created: 2026-09-24
source: /home/hruzam/ia-sync/.dev/session/runbook-upgrade-02-app/raw/draft.majkee.app-scheme.2026-09-23.md
maintainer:
  role: convergence
  seat: Cartan
  assigned-by: majkee
  assigned: 2026-09-24
  attachment:
    runtime: codex
    session-id: "01a0d3ef-c76a-7042-af3f-3b5fb383edd6"
    host: hruzam-120922
---

## Document role

This is the maintained project-design draft for all runtimes. The `source` above is
the earlier draft from which this wrapper was brought into nablarva. Settled locks
belong to [flag.md](flag.md), the standing machine contract to
[PROJECT.yaml](../../PROJECT.yaml), and live work to the session `STATUS.md` files
linked by [pulse.md](pulse.md). Design statements here remain proposals unless
supported by a cited decision.

The shared maintainer role is [convergence](../../.germline/agents/convergence.md).
The frontmatter records its current assignment and runtime-specific session
reference; the role file holds the maintenance instructions.

# 1. what is it

> decission where we go now and next,
> this should be architectural session also claude (oraculum | trajectory) + codex (now cartan).

## 1.1. nablarva *(itself)*

- display form **nab∫ar∇a** (∫ U+222B, ∇ U+2207); paths, commands and slugs stay ASCII `nablarva` ([L13](flag.md))
- agentive framework, multisession drive, decentralized rag connector
- multisession driwing -mesage buss and control mechanism over vendors and sessions


---

# 2.process

1. read all first -> reconsiliation
2. `~/ia-sync/zsh/session/`-> look please on all runbook-tool sessions . `-00` is finished, `coordination` should be also. but need check if anything is not flying.

## 2.1. planning phase

**questions which should be answered**
1. wrapper| ui -> still terminal or some terminal wraper + process window -> real app -> than build should move seriously to `~/unikuklatrix/nablarva/.dev/session/toobox-instarmux
2. but also prepared for your advices

## 2.2. Architecture work

The first useful loop is file-backed prompts and replies between living agents,
with an inspectable inter-session roller. Majkee's priority is to remove routine
human carriage while keeping human decisions at meaningful boundaries. Peers from
different vendors may use their own specialist rosters. A small application core
with explicit adapters and thin clients is the candidate under challenge; runtime
activation remains a qualified, replaceable dependency. The study compares its ownership
boundary with an operator workbench and a process-owning room host, using the
earlier sessions and observed workflow. Existing session tools remain reusable.

[L14](flag.md) supplies the current premises: PTY is the relay's base layer, files
are the spine, and research precedes build (`relay-00-research` → `relay-01-pty` ·
`relay-02-tracker`). Termpanum is the first-build plan. Vendor doors remain weather;
the research verdict and blind triangulation must precede a relay-architecture lock.
The architecture session proposes final organ homes; lifecycle and journal-store
choices remain docket 4 and 5. Its first automated exchange depends on that research
verdict as well as the separately owned native-carrier qualification.

The [architecture session](nablarva-03-app-architecture/RUNBOOK.md) holds the
[working blueprint](nablarva-03-app-architecture/raw/architecture.working.md):
animal/toolbox boundaries, source tree, code/config/data/runtime homes, installation,
wiring, administration and the first complete exchange. These remain proposals.
Its [STATUS](nablarva-03-app-architecture/STATUS.md) owns progress; the project
[pulse](pulse.md) routes all active work. Cartan synthesizes; the attached Claude
seat, Flight, challenges the architecture independently. Flight joins
through the RUNBOOK's scoped prompt; its attachment and assignments live in STATUS.
Keep detailed research and review in that bed.

The [workflow reading and alternatives](nablarva-03-app-architecture/raw/workflow-reading.2026-09-29.md)
preserves the earlier comparison of the onion-terminal observation device. Its
optional-build framing is superseded by L14's termpanum-first plan. Observation,
message delivery and context insertion retain separate responsibilities; this
wrapper authorizes no implementation or live sampling.

Existing [Claude → Codex consultation tools](nablarva-03-app-architecture/raw/tunnel-consultation.2026-09-29.md)
offer a fresh relay for a new opinion and a stored-thread tunnel for continued
conversation. Their relationship to exchanges between living peers is in the study.

# VOLATILE

*Current delivery shape · checked 2026-09-29 · maintained by Convergence.*

Until a separate UI versus integration into a specific IDE is decided, useful
increments continue as **zsh-layer bricks**. Session-facing tools currently fit
`~/ia-sync/zsh/session/`; nabLarva may be delivered in this early phase through
`~/ia-sync/`, the **surgical table**. Each task retains its own source, promotion and
deployment authority. A future app-source/installation model is still a proposal.

The present route is authored ia-sync source → reviewed `bash ~/ia-sync/deploy.sh`
→ live `~/.config/zsh/`; host activation beyond copying uses the separate
`install-pkgs` leg where needed. Command details and constraints live in the
[delivery discipline](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md) and the
[maintainer's route](../../.germline/agents/convergence.md#interim-delivery-route).

Update this section when the route changes. For actual work and verification use
[pulse.md](pulse.md) → the owning `STATUS.md`; this wrapper carries the description
and pointers, not a second progress register or deployment authorization.

# 3. APP parts

## 3.1. termbrana

 - semitransparent foil allowing one typewriting system over all (keys, shortcuts, lighter navigation for terminal inputs -> agentive UI)
 - bridge between terminal, ai session, browser (firefox), files
 - example: have file on line nr. xxx will add `NOTE<nr>` -> open appropriate buffer collector for notes -> I can attach ai session on specific notes, same should be allowed in browser by press any key I can make note with address and anchor to specific HTML part or
 - requires `instatmux` -> dashboard part with sessions
 --> if to much - heavy on one toobox can be splitted to parts per scope of process.

---

## 3.2. ovitmugen *(tool)*
- origin `instar` - phase session (taken from biological names), `tmux`
-> tmux manager - part of runbook tool
- reconsiliate if columns are enough layout, I assume growing needs more space, untill today it was only helper
- holding session dashboard

###### function ADD
- click on some selected session vault, run tmux manager over it (user
  should fill session name, number of 'columns' - I assume windows and name for bed - postures, we can have generic fallback - default_(n), cSharp, bus,... I can add to existing scheme also new beds for another agentive sessions
## function create
no bond to specific `.dev/session/<specific-session>`

## another managing options
 like
 - kill whole tmux session, extend to another beds


### 3.1.1. demanded tree

```tree

└── global-tmux-session # majkee: assume per <slug> f.e.. maybe I am not understanding what session is here (coliding to twins?)
    │
    ├── window_1 # f.e. bed for agent who will drive task proces like cSharp (somebody in charge)
    │	 └── cSharp # pane, majkee: still not understanding why is pane something different from window
    │
    ├── window_2
	...	 └── bus # here is another agentive session with different task


```

--> **reconsiliate** if columns are enough layout, I assume growing needs more space, untill
  today it was only helper

### 3.2.x. @Trajectory notes — tips, observations, upgrade ideas *(append-only, dated)*

> Full architecture: `~/unikuklatrix/nablarva/raw.nablarva/ovitmugen-00-console/draft.trajectory.ovitmugen-architecture.2026-09-23.md`
> These notes are the short, growing layer on top of it. Newest at the bottom.

**2026-09-24 · answers to the inline questions in 3.1.1**
- *"what is session here, colliding to twins?"* A session = a named group of windows. It
  remembers **one** current window, so two terminals on one session always show the same
  window (the twins). Fix: every terminal column gets its own **view** session (`<slug>--<win>`),
  sharing the same windows. Columns are then independent.
- *"why is pane different from window?"* Window = a whole screen (a tab). Pane = a piece of
  that screen when you split it. Every window has at least 1 pane; the agent runs in the pane.
  One agent per window → you can ignore panes.
- *"are columns enough layout?"* Yes, with layout C: the left pane switches between tabs, so
  it grows by adding **tabs**, not columns. Screen width stops being the limit.

**2026-09-24 · decided so far** (source: architecture doc §1, §5.7, §9)
- layout C: frame (own tmux server `ovitmugen`) + agents (normal tmux) · left = tabs, right = runbook fixed
- split 60/40, live resize `C-a <` / `C-a >` · prefix `C-a` (`C-a C-a` = shell start-of-line)
- tabs = empty shells, agents started by hand · console = one view: popup `C-a t` / runbook `T` / `ov`
- docs in nablarva · build in `~/ia-sync/zsh/session/` → `bash deploy.sh`

**2026-09-24 · tips (learned the hard way, 2026-09-23)**
- **Address by ID, not by name**, after creating anything. One session had two windows named
  `bus`, and any `:bus` target became a guess. tmux hands back IDs (`@12`, `%7`) at creation.
- **`=` on a pane target fails** (`=frame:0.1` → can't find pane). `=` is fine for session/window.
- **Name the tmux server in every call** (`-L default` / `-L ovitmugen`). runbook runs *inside*
  the frame, so a bare `tmux` from runbook would hit the frame, not the agents.
- **`window-size largest`** (`~/.tmux.conf`): a tab seen in the narrow left pane *and* on the phone
  gets sized to the phone's width, so the left pane crops. Plan: per-window `window-size latest`.
- Safe-kill rule used in the cleanup: a pane hosts an agent if its command isn't a bare shell
  **or** the shell has child processes. Never kill those.

**2026-09-24 · principles worth keeping beyond ovitmugen** (candidates, not law)
- **A viewer never owns lifetime.** Frame, termbrana foil, a future GUI: they only *show*.
  Closing a viewer must never kill an agent or the broker. Direct consequence for nablarva
  docket 4 (broker as a tmux pane): the broker gets a **tab in the agents server**, never a
  pane in the frame.
- **Dry-run = the manual recipe.** Every zsh/py brick's `--dry-run` prints the literal
  commands; that output is the HELP. Tool and docs can't drift apart.
- **ovitmugen never types into panes** (no `send-keys`, nablarva L4). It switches *views* only.
  If someone asks "can ovitmugen send the prompt to tab X?", the answer is no; that's the bus's job.

**upgrade ideas (not scheduled, pick when needed)**
- `ov ls --json` → termbrana reads it as its dashboard source (3.1 "requires … dashboard part with sessions")
- phone view `<slug>--phone`: the phone attaches to its own view and never steals the left pane's tab
- permanent console pane as a preset option (`"fixed": ["runbook","ovitmugen"]`) if the popup gets used constantly
- t41 folds into ovitmugen (`t41` = thin alias over `ov up`), one preset file for both
- cross-host frame: home shows office agents (`ssh -t office tmux -L ovitmugen attach`), nablarva Stage 2
- tab badges in the console: `●` agent running · `○` empty · later `!` = agent waiting for input (read-only signal, never input)

---

## 3.3. instarmux *(tool)*

## 3.4. reposoma *(tool, not `~/reposoma` - this is substrate)*

## 3.5. muticula *(tool)*

- origin `mutex` × Latin `cuticula` (small skin) -> protective skin around work in progress
- file-backed concurrency coordination for cooperating teams across vendors in one identified checkout
- claim, work, explicitly hand over or release; current design gates commits to the team's live, adopted paths
- claims alone do not prevent edits, identify who typed each byte, or isolate builds from neighboring changes
- source: [master brief](muticula-01-qualify/raw/muticula.master.2026-09-26.md); enforcement coverage is being qualified in the [current task](muticula-01-qualify/STATUS.md)

---

## 3.6. termpanum *(toolbox)*

- observation lab, named by [L13](flag.md): the read-only ear on living CLI sessions;
  adopts the onion study, unilarvatrix build plan and earlier lab design
- L14 D1 supplies the PTY base and first-build plan; hooks and records enrich it.
  The proposed state vocabulary remains docket 8, not a frozen protocol
- observes and records events with source and certainty; never types into sessions
  or injects context. Proposed context-bus ownership belongs to stridulatrix
- proposed home `toolbox/termpanum/`, scripts and plain files first; optional read-only
  MCP and a separate observation window remain design choices for session 03
- sources and open probes: [lab registry design](../../meshup/lab.observability-probes.2026-08-01/DESIGN.md)
  and [hypotheses](../../meshup/lab.observability-probes.2026-08-01/HYPOTHESES.md);
  [brief](toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md)

## 3.7. stridulatrix *(broker + CLI)*

- the broker and its CLI, named by [L13](flag.md) for voice-input reliability;
  L3 supplies the single-writer room journal, participant cursors and adapter-owned
  PTY delivery; L4's rejected input mechanisms remain rejected
- L14 D1/D2: PTY carries the impulse; file-backed content remains inspectable.
  Proposed boundary: owns writes into sessions, including the context bus;
  consumes termpanum observations without turning observation into acceptance
- lifecycle (docket 4), store (docket 5), command prefix and final source home remain
  open. [Session 03](nablarva-03-app-architecture/STATUS.md) owns the architecture
  proposal; relay-00-research supplies its transport/research verdict
- shape and sources: [room registry design](../../meshup/room.brokered-journal.2026-07-31/DESIGN.md);
  cross-vendor research: [seam design](../../meshup/seam.cross-vendor-relay.2026-08-05/DESIGN.md)

## 3.8. stridularium *(phone app)*

- the human's door to stage 3, named by [L13](flag.md); an organ with a proposed
  independently usable console core, not a second authority for the room
- L14 D5/D6: thin lens over host-resident sessions; attaching is advisory and
  detaching never closes a bed. A host-side engine hosts the processes; the app
  sends commands/prompts and receives output. Device reach is the app and its
  files; an operator-scoped vault is a later extension
- console versus rendered cards, voice input, per-target buffers, carousel,
  breadcrumbs and bridge choices remain design input. The two origins disagree
  about a native terminal on the phone; this fold preserves that open question.
  `stridularium/{android,host}` is a home proposal for session 03, not a created tree
- [registry design and origins](../../meshup/stridularium.mobile-console.2026-09-29/DESIGN.md)
  → [living phone wrapper](AGENTS.stridularium-design.md) →
  [open hypotheses](../../meshup/stridularium.mobile-console.2026-09-29/HYPOTHESES.md).
  Majkee drafts the app in stridularium-00-design when that gate opens

---

# KEYS CODE

*Added 2026-09-29 by Trajectory (ovitmugen-00-console) at majkee's request · **ACCEPTED by
majkee 2026-09-29** (D3 in `ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md`).*

**DRY:** the meanings live only here. An organ's help points to this chapter and lists only
its own extra keys — it never copies this table.

One shortcut style for every organ's TUI: **the same key means the same thing everywhere**,
so moving between toolboxes never means relearning. This is a grammar, not a registry:
each organ keeps its keys in its own code; this chapter only fixes their meaning.

Shell commands stay under the claviature rule (`~/ia-sync/zsh/guides/claviature.global.spec.md`,
"derive, don't register"): families only (`ov-`, `rb-` …), the `keys` panel derives the rest.

## Shared meanings (all organs)

| key | meaning |
|---|---|
| ↑↓ · j k | move |
| Enter | act / open the selected item |
| q · Esc | back (close the view, never quit something running) |
| ? | help for this view |
| / | search |
| a | add |
| x x | remove — **always two presses** (first arms, second acts, any other key disarms) |
| b | build (create what is missing) |
| o | open / attach |
| r | refresh |
| T | tabs (agent tabs of the bed) |
| 1-9 | jump to item / part N |

## Reserved (never bound by an organ)

- `C-a` — the ovitmugen frame prefix (frame keys: focus, split, popup, restart, tabs).
- `C-b` — the agents' own tmux.
- Keys a running agent needs (anything typed into an agent pane) — organs act only in
  their own views.
- `Alt-…` — open: may become prefix-less tab jumps (`Alt-1…9`); decide before any organ uses Alt.

## Conformity today (honest check, 2026-09-29)

| organ · view | follows | deviates |
|---|---|---|
| ovitmugen console | ↑↓ j k · Enter · q Esc · a · x x · b · o · r | ? and / not yet |
| runbook tree | ↑↓ · Enter · q Esc · ? · r · T · 1-5 · A A (two-press) | no j k; `h` also opens help; no / (search only inside help: Ctrl-F / F) |
| runbook buffer view (P) | q · ↑↓ | `x` removes a line with ONE press |
| ovitmugen frame (C-a …) | reserved prefix | — |

Deviations are listed, not fixed here: each fix belongs to its organ's own session.
