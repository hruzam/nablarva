# field.body-construction.r1 — nabLarva: v0 construction model, survival and spine
`synthesized: field(@Field), 2026-10-24 · arch-X0 session · read-only`
`provenance key: said: v0 = Nabla-Tmux-Architecture-Draft-v0.md · said: <file> = exact path cited · locked: L<n> = flag.md · inferred: field = this document's reading`

Parts 01–04 of the X2 raw handoff were searched; no files matching `0[1-4]_*.md` exist under
`.dev/session/nablarva-X2-builder-narative/raw/`. Only `05_WAY_OF_THINKING.md` is present.

---

## 1. v0's construction model in its own terms

### Layer table (said: v0 §Layers · §Glossary · §Code layout)

| layer | what lives there | what it owns/writes | how it loads | talks to neighbours |
|---|---|---|---|---|
| **1 Boot** | `boot/env.zsh`, `shell/init.zsh`, `shell/aliases.zsh` | constants, PATH extension; writes nothing | sourced at every interactive shell start; and by every gate | exports env vars; puts `bin/` on PATH |
| **2 Living tissue** | `hooks/` — tmux `set-hook`, CLI hooks (Stop, SessionStart, …), watcher | appends to `events/*.jsonl`; writes `status.md` | always-on, outside the shell; started by tmux server config or systemd user unit | reads substrate; writes events sideways; optionally rings doorbell |
| **3 Gates** | `bin/nabla`, `bin/nabla-pane`, `bin/nabla-relay`, etc. | nothing — pure dispatch | executable; called by alias, key, popup or hook; `zsh -f` skips .zshrc | sources boot env; dispatches to bricks; calls services |
| **4 Bricks** | `pipes/<pipe>/<verb>` autoload functions | one side effect each; sets tmux user option `@nabla_role` (pane-lifetime) | `autoload -Uz` — name registered by gate; file read on first call | reads/writes substrate; emits events; never calls another brick |
| **5 Services** | `services/*.py` | none (pure compute) | called by gates as subprocess; args/stdin in, JSON stdout | returns JSON to gate; never touches tmux |
| **6 Substrate** | `~/.config/nabla/config.zsh` (config) · `~/.local/state/nabla/{bus,events,sessions,status.md,bricks/}` (state) · `$XDG_RUNTIME_DIR/nabla/` (runtime) | written by bricks and living tissue; config by operator only | files — outlive every process; three lifetimes: config / state / runtime | the only sideways channel between all layers |

### SVG diagrams — assertions beyond the prose

**layers.svg** ("Only boot loads with the shell; the rest waits to be called") — living tissue is a separate right-side column, independent of the main call chain, always-on. A dashed arrow runs from substrate back into gates ("read"), showing gates may read substrate for context — implied in prose but not stated. Solid = control, dashed = information.

**tree-and-mycelium.svg** ("Commands flow down the tree; facts spread through the substrate") — marks the brick-to-brick prohibition with a visible red X between pane-spawn and relay-doorbell. The dashed substrate-read arrow returns only to nabla-relay, not to all gates — suggesting relay is the primary substrate reader. The substrate bar is blue-highlighted as common ground, matching boot's blue in layers.svg.

**what-loads-when.svg** ("A new shell reads three small files; a call reads only its own path") — the "Ready" state is blue-highlighted: zero gates, bricks or services have been read. The gate label "sources env.zsh, marks brick names" makes explicit what loading a gate does. Only the called brick is read; its siblings stay on disk. The cost of adding one hundred bricks to shell startup = zero.

**events.svg** ("Every source writes the same record; readers can change later") — the broker box is explicitly dashed (future), making its planned absence architectural. "Bus and popups" is named as a fourth source tier alongside tmux hooks, CLI hooks and runbook runner — the bus message is itself an event. Both watcher (solid) and broker (dashed) feed the same Reactions box, so sources never need to know their reader.

**messages.svg** ("Every message is a file; tmux only rings the doorbell") — agent output and human-composed prompts take the same bus path. The classifier sits between the bus and the receivers, not between the senders — automation starts at routing, not authorship. "rules, model optional" is a visual label on the classifier: predictable without the model, optional with it.

---

## 2. Pattern survival against the locks

| # | pattern (said: v0) | verdict | governing lock / collision | amendment cost |
|---|---|---|---|---|
| P1 | Single whole-animal router `nabla <pipe> <verb>` → `bin/nabla-<pipe>` | **survives amended** | X5 · L17 (indep. clients) · L21 (tool runs alone) | Router must be optional, not a required entry point; each tool must work without it |
| P2 | Command gate: executable in `bin/`, `zsh -f`, checks input, dispatches | **survives as-is** | — pure implementation pattern | None |
| P3 | Lazy autoload bricks (`autoload -Uz`, fpath, read on first call) | **survives as-is** | — consistent with L17, L21 tool-alone rule | None |
| P4 | Edges are executables (shebang, no extension, `zsh -f`) | **survives as-is** | — | None |
| P5 | Living tissue hooks write to event log (tmux `set-hook`, CLI hooks → `events/*.jsonl`) | **survives amended** | X9 · L14 D1 (vendor doors parked) | Hooks may write events; direct hook → bus write is parked; qualified path required for bus |
| P6 | Event log: one JSONL, same format, many appenders | **survives amended** | X4 · L3 S1 (one-writer journal) · docket 8 (four candidate envelopes) | Multi-appender needs ruling against one-writer rule; envelope waits on docket 8 or scoped exception |
| P7 | Substrate file layout: config / state / runtime separation | **survives amended** | X11 · L3 S8 (neutral ground) · O3 · docket 5 · lean `~/.nablarva` or `<project>/.nablarva` | Path must change to lean; three-lifetime concept survives |
| P8 | Bus: one file per message, maildir atomic rename | **survives as-is** | — consistent with L14 D2 (file plane is the spine) | None |
| P9 | Doorbell: short nudge names the file to read | **survives amended** | X1 · L4 (send-keys = recorded death) · L3 S5 | Concept survives; `tmux send-keys -l` mechanism is dead; alternative mechanism open — any claimed exception returns to Majkee |
| P10 | Classifier: rules-first routing of bus messages | **dead as standalone brick** | X10 · L3 S4 (structural regulation) · L20 (VIST controller separate) | Could live inside VIST controller authority; no standalone classifier |
| P11 | Pane spawn brick (`pane-spawn`) | **survives as-is** | — creating a pane does not close one | None |
| P12 | Pane close brick (`pane-close`) | **survives amended** | X8 · L17 (ovitmugen protected lifetime) | Must check ovitmugen authority; who may close is open (said: ARCHITECTURE §4.4) |
| P13 | Runbook step runner (ordered steps, stop on failure) | **survives amended** | X12–X13 · ARCHITECTURE §5 reading aid (name clash with session RUNBOOK document) | Rename required; step-runner concept is fine |
| P14 | Single-writer `status.md`; view-only display in control pane | **survives as-is** | consistent with L3 S1 (one writer per file) · L14 D5 (viewer never owns lifetime) | None |
| P15 | Services: Python, pure compute, args in / JSON out, never touch tmux | **survives as-is** | consistent with L17 (Python conditional on measured responsiveness) | None |
| P16 | Tree (control down) + mycelium (information sideways through substrate) | **survives as-is** | consistent with ARCHITECTURE §2 dependency direction · L14 D2 | None |
| P17 | Compiled broker (Go/Rust) as long-running event router | **dead / gated** | X2 · L4 (C++/Go = recorded death) · docket 2 (language) · docket 4 (lifecycle) | Broker concept (ordering, retries) survives; language gated on docket 2; lifecycle on docket 4 |
| P18 | `nabla` command, `NABLA_*` env vars, `~/nabla` home | **dead** | X6 · L13 (commands stay ASCII `nablarva`) · said: ARCHITECTURE §9 X6 | Use `nablarva` on every machine surface |

---

## 3. The three existing parts, as built

### Ovitmugen — CODE-RUNS (said: inventory §1 · said: ovitmugen.py header)

| dimension | detail |
|---|---|
| Entry | `ov-up <slug>` → alias `keyboard.zsh:36-41` → `_ov_up` in `ovitmugen.zsh` → `python3 ~/.config/zsh/session/ovitmugen.py up` |
| Process model | Two tmux servers, never mixed: `tmux -L default` (AGENTS: one window per agent tab, named `<slug>--left` and `<slug>--<win>`) · `tmux -L ovitmugen` (FRAME: one session per bed, prefix C-a, config from `ovitmugen.tmux.conf`) |
| State files | None durable. Tmux option `@nabla_role` = pane-lifetime only. Source: `~/ia-sync/zsh/session/ovitmugen.py`; deployed: `~/.config/zsh/session/ovitmugen.py`. |
| Config | `ovitmugen.presets.json` (tab presets); env `OV_AGENTS_SOCKET`, `OV_FRAME_SOCKET`, `OV_FRAME_CONF` |
| Command surface | `ov-up · ov-tab · ov-ls · ov-down · ov-console · ov-selftest` |
| v0 layer | **View** (locked: L17 "view/layout and protected process-lifetime ownership"; ARCHITECTURE §1 view plane) |
| Agrees with v0 | Two-server isolation mirrors v0 substrate/living-tissue separation. No send-keys (law L-a = L4). Viewer never owns lifetime (L-b = locked: L14 D5). `--dry-run` prints literal tmux commands. Presets.json = config-layer concept. Zero durable state files = consistent with P7 pane-lifetime-only facts in tmux options. |
| Contradicts v0 | No event log emitted. Has own `ov-*` surface, not `nablarva pane spawn` router. Frame popup (`display-popup … console`) runs Python directly — no gate. |

### Termbrana composer — CODE-RUNS (said: inventory §4 · said: ia-sync/zsh/termbrana/README.md)

| dimension | detail |
|---|---|
| Entry | `tbc-check` / `tbc-parse` (require explicit `source base.zsh`) → `_tbc_check` / `_tbc_parse` in `composer.zsh` → `python3 -I -S -B composer.py check|parse` |
| Process model | Stateless; each call is its own process; no tmux, ovitmugen, or nablarva dependency; Python stdlib only |
| State files | None. Read-only. No state, cache, output files, network calls, or child processes. |
| Config | None (`-I -S -B` explicitly ignores all Python env); only explicit input file argument |
| Command surface | `tbc-check · tbc-parse`; Python API `composer.parse(bytes)` |
| v0 layer | **Services** (pure compute, data in, JSON/JSONL out, never touches tmux — P15) |
| Agrees with v0 | Python computes, zsh acts (P15). Stateless. Fails soft — "standalone operation with nabLarva completely absent" (said: toolbox/termbrana/README.md §Product direction). Exit codes follow sysexits pattern (0/64/65/74). |
| Contradicts v0 | No `nablarva termbrana parse` router path — own `tbc-*` surface. Not an autoload brick. No gate in v0 sense. |

### HELLO contract — DOC-CONTRACT, not implemented (said: inventory §2 · said: hello-01-contract.md · said: hello-02-addendum-r1.md)

| dimension | detail |
|---|---|
| Entry | `nabla-send`, `nabla-read`, `nabla-bell` (proposed executables in bed's `bin/`) |
| Process model | File-based; `nabla-bell` = watcher (inotify/poll); no daemon required; keystroke injection only inside experiment bed by operator decision |
| State files (proposed) | `<bed>/.nablarva/sessions/<YYYY-MM-DD>.<NN>/events.jsonl` (one writer = bell) · inbox mail files · `archive/` (processed) · `bell.conf` |
| Config (proposed) | `<bed>/.nablarva/config.conf` · `~/.nablarva/` (machine defaults) · `NABLA_BED` env var required — explicit-only state-path gate |
| Command surface (proposed) | `nabla-send · nabla-read · nabla-bell · nabla-mail` |
| v0 layer | Substrate + Living tissue (bell = watcher; mail files = substrate; send/read = bricks/gates) |
| Agrees with v0 | File-as-content with maildir atomic rename (said: hello-01-contract.md §Bus). Doorbell concept (bell rings, names the file). Session events.jsonl = one writer (bell) — echoes P6 single-writer variant. Three-lifetime split echoes P7 substrate design. |
| Contradicts v0 | `nabla-send` not under router. Keystroke injection scoped only to experiment bed — v0's doorbell (P9) uses `send-keys -l` globally, which is dead (L4). Home is `.nablarva` not XDG. |

---

## 4. Candidate shared layers under L21

L21 rule (locked: L21): bricks may share process, API, CLI and subscription layers; a particular tool still runs without waking the whole animal; no shared layer implementation is authorized yet.

| candidate | runtime coupling required | parts needing TODAY (≥2 = real) | natural owner | home per L18 | breaks single-tool rule if wrong |
|---|---|---|---|---|---|
| **Boot / env vars** | `NABLA_BED`, `OV_AGENTS_SOCKET`, install path convention | ovitmugen + HELLO = **2 → real** | boot layer (v0 `boot/env.zsh` pattern) | new thin component folder under `~/ia-sync/zsh/` per L18 | mandatory source at shell start breaks tool isolation |
| **Install/package** | `bash ~/ia-sync/install-pkgs/run.sh update` · `deploy.sh` | ovitmugen + termbrana composer = **2 → real** | `~/ia-sync/install-pkgs/` (existing, said: L8′) | `~/ia-sync/` (locked: L8′) | atomic install-all-or-nothing breaks single-tool testing |
| **KEYS CODE grammar** | shared key meanings across TUI organs | ovitmugen console + runbook pane = **2 → real** | ARCHITECTURE §5 (accepted, said: majkee 2026-09-29) | `docs/ARCHITECTURE.md §5` (existing, locked: L16.9) | not runtime coupling; grammar only — no breakage risk |
| **Config / registry** | `.nablarva/` layering, `NABLA_BED` convention | HELLO proposes it; ovitmugen uses presets.json independently; termbrana ignores all config = **1–2 → marginal** | unknown (said: ARCHITECTURE §4.8, R9-1 N2 = direction only) | lean: `~/.nablarva/` (said: X11 lean; HELLO r1) | required global config before any tool runs breaks single-tool rule |
| **CLI router** | shared `bin/nablarva` on PATH | no part uses it today = **0 → hoped-for** | unknown | unknown | mandatory router breaks standalone operation |
| **Event subscription / log** | shared `events/*.jsonl` path, shared envelope | no shared code today = **0 → hoped-for** | unknown; docket 8 unresolved | lean `~/.nablarva/` | subscription required at startup breaks single-tool rule |
| **Python shared library** | importable common module | termbrana composer (own module); termpanum (proposed); no shared module today = **1 → hoped-for** | unknown | new component folder per L18 | import fails without nablarva present → breaks standalone |

---

## 5. Spine candidates

The minimal running observe → record → view vertical implied by v0 + existing parts:

**Conventional names (05 Q1):**
- "Append-log pipeline" (syslog/journald → logwatch; Kafka → stateless consumer)
- "Terminal session recorder with replay" (script+tlog; ttyrec+ttyrec2; asciinema+player)
- "Agent health monitor" (tail/grep on JSONL + curses projection)

### Write paths and truth location (lens 7 + lens 6)

| effect | one write path | truth lives where | type | writer | CODE today |
|---|---|---|---|---|---|
| Record agent session event | hook → `events/<date>.jsonl` (proposed) | event log file | source evidence (append-only) | living tissue (proposed) | CODE-DRAFT: `reincarnation-session.sh` only (pipe-pane → raw.log, experimental; said: inventory §3) |
| Record bus message landed | `nabla-bell` → `<bed>/.nablarva/sessions/…/events.jsonl` (proposed HELLO r1) | session events file | source evidence | bell (1 writer) | NAME-ONLY |
| Show session status | watcher → `status.md` → display (proposed) | `status.md` | projection (derived from events) | watcher (proposed) | NAME-ONLY (watcher); CODE-RUNS (ovitmugen frame shows runbook pane, not event-derived status.md) |
| Manage pane lifetime | `ov-up` / `ov-down` → tmux server | tmux server state | source evidence (ephemeral) | ovitmugen (sole writer, locked: L17) | CODE-RUNS |
| Deliver message to pane | doorbell mechanism (open; send-keys dead) | open | open | open | NAME-ONLY |
| Capture pane output bytes | `pipe-pane -O` → `runs/<run-id>/` (proposed termpanum Q) | capture file | source evidence (pane output, not PTY master) | termpanum collector (proposed) | DOC-PLAN |

**Spine inventory tag:** Observe = CODE-DRAFT (experimental only); Record = NAME-ONLY; View = CODE-RUNS (ovitmugen, views only). The vertical is not yet running: view exists and runs; observe is experimental and not the intended architecture; record is a design.

---

## 6. Unresolved disagreements and operator questions

### Disagreements (kept, not settled)

**D1.** v0's event log has many appenders (tmux hooks, CLI hooks, runbook runner, bus) — said: v0 §Events. L3 S1 says "append-only single-writer journal as sole room truth" — locked: L3. These may be different journals. If they are the same, many-appender violates the lock. If separate, which one-writer rule applies to each is not ruled. `⚡ CONFLICT: no gavel separates v0 event log from L3 room journal.`

**D2.** L21 says "tool still runs without waking the whole animal" AND "bricks can share process, API, CLI and subscription layers" — locked: L21. A shared CLI router (P1) satisfies the second clause but risks violating the first if required. How a shared router can exist and remain optional is not resolved. `⚡ CONFLICT named and left open in ARCHITECTURE §2 item 5; P5-a / P5-b proposals not yet gaveled.`

**D3.** Three incompatible substrate path proposals: v0 proposes XDG `~/.local/state/nabla/` — said: v0 §Substrate; HELLO r1 proposes `<bed>/.nablarva/sessions/` and `~/.nablarva/` — said: hello-02-addendum-r1.md; ARCHITECTURE §9 X11 lean is `~/.nablarva` or `<project>/.nablarva`. None is gaveled; all three differ. `⚡ CONFLICT.`

**D4.** Two "control pane" concepts: v0's `status.md` driven by a watcher reading the event log — said: v0 §Runbooks; ovitmugen's right pane driven by the runbook tool reading session RUNBOOK/STATUS.md — said: inventory §1, CODE-RUNS. Same visual role, different truth sources. Whether they merge or stay separate is open; no ruling.

### Operator questions (≤5, one line each)

**Q1.** Does the `nablarva <pipe> <verb>` router apply to existing organs (ovitmugen, termbrana), or only to new bricks — and if existing tools keep their own surfaces, how does a caller know which surface to use?

**Q2.** Is v0's event log (many appenders, `events/*.jsonl`) the same single-writer journal L3 S1 governs, or are they separate records with separate writer rules?

**Q3.** Which substrate home is chosen: `~/.nablarva/` (HELLO r1 lean, vendor-mirroring), XDG `~/.local/state/nabla/` (v0 original), or `<project>/.nablarva/` (HELLO r1 project scope)?

**Q4.** Can the doorbell use inotify/FIFO/named-pipe polling instead of `send-keys` — and if so, which alternative should the architecture candidate test first before the mechanism is opened for termpanum's Q package?

**Q5.** Does termpanum's documentary D package (source contract, no runtime work) require an architecture GO from this session, given that the relay-00-research gate (L14 D4) was scoped only to runtime execution?

---

Also noticed: the HELLO r1 `.nablarva/` layering table (said: hello-02-addendum-r1.md §Layering) is the only existing document that concretely models a per-session runtime state layout alongside vendor-native patterns (`~/.claude/`, `~/.codex/`). It is DOC-CONTRACT, not gaveled; but it is the strongest available template for the substrate home question.
