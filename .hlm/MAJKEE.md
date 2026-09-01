---
doc: MAJKEE.md
kind: project-overview · pseudo-CLAUDE.md · human-only (majkee)
classification: TOP SECRET · 6378 preflight
wired_to_llm: false
growth: additive-append
reporter: "accrete"
partitions: [common-knowledge, opened, closed]
build_part: "grep -n '^## ' for the chapter spine, '^### ' for sub-blocks — this book is a pointer-index, navigate by header. New chapters append above the FOOTER; named headers are never renumbered. Full mechanism: section '## BUILD PART'; colleague tasks: section '## FOOTER → REPORTER'."
---

# MAJKEE.md — majkee's project overview (TOP SECRET · 6378 preflight)

> **`MAJKEE.md` — HUMAN-ONLY (majkee).** Pseudo-`CLAUDE.md`: orientation for *me*, not an agent instruction file.
> **NOT wired to any LLM** — do not auto-load, do not feed to a blind session. Holds KEY-side vocabulary + bonds;
> must never enter phase-3 blind scope. (The name is not `CLAUDE.md`/`AGENTS.md`, so no harness auto-loads it.)

Human map: **name · scope · the door to open.** Walk these yourself, in parallel with the agents.
Raw-side, pre-mask — vocabulary as-is. Built by @Flight, 2026-08-07.

**This is majkee's bible — ONE self-contained study-book.** Everything is inlined here: the full SOURCES
pointer-lists, DOUBLES, FORKS (both branches, UNRESOLVED), GAPS, and DECISIONS-FOR-MAJKEE from each theme
now live under their scope section. The four `task.<theme>.md` docs are source-only — you never need to open
another file to read this cover-to-cover. Some text is duplicated across sections on purpose (a pointer or a
fork that belongs in two places is written in both). Pointers only — nothing here is a summary.

_Roots — MESHUP: `/home/hruzam/unikuklatrix/nablarva/meshup/` · REPOSOMA: `/home/hruzam/reposoma/`_
_Source maps — Field: `/home/hruzam/unikuklatrix/nablarva/meshup/_preflight/map.meshup.field.2026-08-07.md` · Epoch: `/home/hruzam/unikuklatrix/nablarva/meshup/_preflight/map.reposoma.epoch.2026-08-07.md`_

---

## MAIN RULES — read first (the book's own law)

Top chapter. These govern how the book is touched — by me (majkee) and by any editing colleague/agent.

1. **Never write behind the FOOTER.** Nothing is written below `## FOOTER → REPORTER` unless majkee explicitly says so. The FOOTER is a **floating object** — it always rides last; new chapters and content append *above* it, never after it.

**Open epistemic question — under independent research:** can this book carry an **inner `CLAUDE.md` — markdown-in-markdown — as a mechanism**? i.e. an embedded, agent-consumed block nested inside this deliberately human-only file, without breaking the clean-room wall (frontmatter `wired_to_llm: false`). Independent research pass spawned this session → `_preflight/research.inner-claude-md.2026-08-06.md`.

---

## BUILD PART — this book's own mechanism

*How this document is read, partitioned, and grown. Info, not a task.*

**Grep spine.** `grep -n '^## ' MAJKEE.md` → the chapter spine; `grep -n '^### ' MAJKEE.md` → the sub-blocks inside a scope (SOURCES · DOUBLES · FORKS · GAPS · DECISIONS FOR MAJKEE). Why: the book is a pointer-index, not prose — you navigate by header, jump to the scope, then grep the sub-block.

**Growth is additive.** The file is expected to extend. New chapters append **above** `## FOOTER → REPORTER`; existing chapters are never renumbered (headers are named, not numbered, on purpose). The FOOTER always stays last.

**Partitions** (frontmatter `partitions:`) — the door-state of each chapter:
- **common-knowledge** — settled shared vocabulary + the skeleton (`## BONDS`, DOOR #1 consensus).
- **opened** — live, under active study (`## SCOPE 1`, `## SCOPE 2`, `## ORCHESTRATION CONCEPT`, `## METHOD / STYLE`).
- **closed** — gaveled / do-not-re-litigate (DOOR #1 · G5 toolkit-not-engine). [FOREIGN-ID]

**Maintenance model** *(planned — info, not a task now)*: this folder should get a small maintenance colleague for this book — a Claude that **only edits, never writes from scratch**; for any other purpose it spawns agents. Its MCP whitelist **folds from the recorder build**. The only second seat is technical support (**Trajectory or Flight** — no further seat needed).

**Future conception** *(info)*: this document is conceived to become, in the future, **a program itself** — not only a human-read pointer-index but an executable substrate (the book *as* program). Today it is read by hand; the growth path is toward the book running, not merely being read. Everything above (grep spine, additive chapters, partitions, the edit-only maintenance seat) is the groundwork for that turn.

**Build addendum — Sublime markdown chaptering side panel** *(info / build note)*: Sublime Text has **no native persistent outline sidebar** (unlike VS Code's Outline view). What ships natively is **Goto Symbol** (`Ctrl+R`) — an ephemeral fuzzy list of this file's `#`/`##` headings with jump-on-select; it reads the chapter spine directly but isn't a docked panel. A true docked chaptering panel is **not native but buildable** as a small Sublime plugin (Python API): collect headings via `view.find_by_selector("markup.heading")` (or the symbol index), render them into a companion view / output panel, and wire a jump command on selection — effort: small. Confidence: medium — verify exact package names before relying (e.g. MarkdownTOC writes an in-document TOC, *not* a side panel; general "Outline" packages tend to be file-browsers). Ties to G7 monitor-surface + the SCOPE-1 Sublime `exec` finding.

---

## DOOR #1 — EXISTING CONSENSUS (walk this before generating anything new)

The first big research already ran once, as a blind-triangulation. Read its **shape** before any new pass —
this is the reinvent-the-wheel guard. ("The consensus in the replay may beat any new answer.")

- **The atlas (RAG thread)** → `nabla-lab/drafts/orchestration-atlas-v2.md` — file-backed agentic RAG stack. *(v1 was committed then deleted in the same commit = your restart, on disk.)*
- **The multi-orchestration thread** → `nabla-lab/drafts/three-spines-orchestration.md` — multi-agent orchestration over a file-backed substrate.
- **The blind packet** → `nabla-lab/drafts/atlas2-research-substrate.md`
- **The gathered leg-outputs** → `nabla-lab/session/research-atlas2-stance-geometry/` — `leg-epoch`, `leg-gemini`, `leg-color`, `cross-measure` + `report.final.oraculum.2026-07-02.md`
- **Deeper root** → `reposoma/raw.research/agentic-sovereignty.report.2026-06-16.md`

### Harvest (Eagle, 2026-08-07) — the shape, already decided

> ⚠ **ATTENTION — FOREIGN CONTEXT** (grep tag: `[FOREIGN-ID]`). The identifiers in this DOOR #1 harvest —
> **G5 · G3 · F1/F2/F3 (Gate-1) · P4** — are BORROWED from the old nabla-lab 2026-07-02 ballot/report. They
> COLLIDE with this fold's OWN numbering: its own **G5** = "Brick-factory stock" (STYLE/SUPPORT gaps), its own
> **F1–F5** = the forks, its own **P1–P4** = the product ledger. **majkee repairs by hand** — grep `[FOREIGN-ID]` to jump to each.

- **Ballot** → `nabla-lab/session/gavels.2026-07-07.md` — G3 ACCEPT points to the oracle report; **G5 AGREE** is the engine call. [FOREIGN-ID]
- **Oracle report** → `nabla-lab/session/report.final.oraculum.2026-07-02.md` — Gate-1 verdicts F1/F2/F3 + the P4 "fence" (subai/reposoma RAG boundary). [FOREIGN-ID]
- **How decided results are treated** → `session/split-map.2026-07-02.md` (finding → destination card) then `shaped/` → @Janus verdict → `papers/`.

**Exportable-engine promise: YES, but as a TOOLKIT, not a shared engine.** The `spectral` anchor (split-map row A3, "Spectral engine core" — diffusion retrieval + spectral clustering) is "ONE card, two mounting faces" — but **G5 gaveled it: shared mathematical toolkit (card + fixtures + doctrine), NOT a shared engine; ownership split stands.** Report §4 fence: *"two engines, two graphs, no overlap"* — recall rented over MCP, not shared as a library. [FOREIGN-ID]

> **Already decided — do not re-litigate.** The toolkit-not-engine call is a standing gavel (G5). The exportable shape = the `spectral` toolkit card (A3), not a shared codebase. Deeper pass only if you want the actual card A3 fixtures/code, not the verdict. [FOREIGN-ID]

---

## BONDS — how the parts connect (the skeleton)

Structural links only — *X feeds / constrains / sits-on Y.* Pointers, not prose.

- **Scope-1 hooks / PTY / events** → *feed* → **Scope-2 room/broker.** A composite is two scope-1 programs wired together; you can't build the room until you can observe and drive one CLI.
- **Scope-1 output-observation** (`terminal-onion-study`, `seam-probe`) → *is the input to* → **the driller / tokenizer** (`02_DRILLER`) → *which feeds* → the room's clean-event stream.
- **Door-#1 consensus** (G5: toolkit-not-engine + ownership fence) → *constrains* → **the orchestration forks (T3/T4).** Any "shared engine" branch contradicts a standing gavel. [FOREIGN-ID]
- **The 2026-07-02 blind-handoff method** (leg-epoch / gemini / color → cross-measure → oracle report) → *is the template for* → **this program's blind research (P3).** Same shape.
- **Composites F3** (`-p` in/out) → *gated by* → an external constraint (Anthropic billing), not an internal design choice — it can flip without the architecture changing.
- **MAJKEE.md (this file, KEY-side)** ⟂ **the blind phase-3 corpus** — deliberately *not* bonded. That non-bond is the clean-room wall.

---

## YOUR-WORK — majkee's own observation tasks (stubs, not content)

Things *you* do by hand — links, not walls. Fill/expand as you go.

- **PADs to create** (ant-work observability, PAD style) → tool: `reposoma/raw.guides/PAD/pad-builder.md`; target: `04_LABORATORY_OBSERVABILITY`.
- **AUR / Linux internals to visit** — the low-level terminal/CLI parts (PTY, tty, process layers) you want to see behind the curtain.
- **Build a monitor surface** — Sublime `exec` streaming panel (confirmed viable — see SCOPE-1 WEB FINDINGS), or a small SSH / helper program.
- **Terminal-layer testing regimes** — regimes that uncover what happens in the terminal layers (tie to `interposition-study` + `terminal-onion-study`).
- **Commands / features to see inside the CLIs** — the claude / codex flags, hooks, event streams to probe.

---

## SCOPE 1 — the CLI as a program (primary)

Terminal, events, hooks, life-hacks. Directly observable.

- **Theme:** T1 — "harness as programming layer" — single CLI as a program: terminal, events, hooks, lifecycle, life-hacks.
- **Scope:** meshup T1 cluster + Epoch SCOPE-1 reposoma candidates (single CLI as a program).
- **What tyler does with it:** enters the corpus of how one CLI behaves as a programmable substrate (terminal rings, PTY wire, disk/JSONL truth, hooks/skills/bonding, live-screen read) — meshup design substrate on the left, reposoma research/settings candidates on the right.

Start-here:
- **natural-ladders** (deep source) → `meshup/natural-ladders-grounded-phase.a-sym`
- **old-but-good-onion** (terminal layers · what to measure) → `meshup/old-but-good-onion`
- **lab-observability** (ant-work testable, *no mask* — PAD style) → `meshup/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md`

  > **[verbatim excerpt — meshup/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md]**
  > ## 4.1 Meaning of "hacker" in this project
  >
  > The intended hacker stance is not intrusion or policy bypass.
  >
  > It is:
  >
  > > Treat the CLI as an unknown machine. Stimulate it with controlled inputs. Observe every boundary legitimately available on the owned system. Correlate independent signals. Infer only what the evidence supports.
  >
  > The laboratory exists to discover the machine's real behavior before production architecture hardens around terminal guesses.
  >
  > ## 4.2 Why the laboratory changes the design
  >
  > A terminal screen is the outermost and often least semantic layer.
  >
  > The system should prefer higher-quality signals when available:
  >
  > ```text
  > native lifecycle event
  >         ↓ unavailable
  > structured vendor event stream
  >         ↓ unavailable
  > local process/file/tool observation
  >         ↓ unavailable
  > PTY reconstruction
  >         ↓
  > statistical inference
  > ```
  >
  > This leads to a key architectural refinement:
  >
  > > The driller is not the universal first interpreter. It is the fallback and correlation engine after native and structured signals have been considered.
- **harness lifecycle / skill-injection** → `reposoma/raw.research/harness/reports/2026-07-20-harness-lifecycle-skill-injection-safe-protocol.md`
- CLI knowledge cards (claude-code, codex-cli) — full paths below.

### SOURCES

#### From Field's meshup map (T1 cluster)

- `/home/hruzam/unikuklatrix/nablarva/meshup/old-but-good-onion/terminal-onion-study.md` · primary substrate: the terminal ring map, PTY wire, disk truth (JSONL paths at `~/.claude/projects/`), tap drill; foundational for any hook/interposition work. · Field map

  > **[verbatim excerpt — meshup/old-but-good-onion/terminal-onion-study.md]**
  > ## 1. The onion — outer skin → core
  >
  > | # | Ring | What lives here | Kernel? |
  > |---|------|-----------------|:---:|
  > | 1 | **TUI / application** | `claude`, `gemini`, `vim`, `htop`, `lazygit` | — |
  > | 2 | **Escape-sequence protocol** | `\e[31m` red, `\e[2J` clear, `\e[?1049h` alt-screen | — |
  > | 3 | **Terminal emulator** | alacritty, kitty, foot, wezterm, st — turns escapes → pixels, holds PTY **primary** | — |
  > | 4 | **PTY pair** | the wire: `/dev/ptmx` → `/dev/pts/N` | **yes** |
  > | 5 | **Line discipline (`n_tty`)** | echo, backspace, Ctrl-C→SIGINT, canonical vs raw | **yes** |
  > | 6 | **Shell** | bash/zsh/fish — *just another tenant*; forks+execs the tool, then blocks | — |
  > | 7 | **Process + FD layer** | fork/exec, process table, `/proc/PID/fd/` | **yes** |
  > | 8 | **Core** | kernel + silicon | **yes** |
  >
  > The cardinal sin: conflating **ring 3 (emulator)** with **ring 6 (shell)**.
  > They are different programs. The shell is not special; the kernel is.
- `/home/hruzam/unikuklatrix/nablarva/meshup/old-but-good-onion/interposition-study.md` · primary T1 document: wrapping the unmodified CLI via PTY, file-backed loop, hook/MCP seam table, policy green zone (OAuth token stays inside Claude Code), resilience (spine/seam/canary), open branch (parallel-finger daemon via inotifywait). · Field map

  > **[verbatim excerpt — meshup/old-but-good-onion/interposition-study.md]**
  > ## 1. Vendor app ≠ SDK → the verb is *interpose*
  >
  > You don't **link** these tools and call their functions. They are vendor
  > **applications**, not libraries. So you **interpose** — wedge code between two
  > rings of a binary you don't own. The onion gives a seam at almost every ring.
  >
  > | Ring | Seam | Buys | Cost |
  > |---|---|---|---|
  > | **1** | **MCP server** (JSON-RPC / stdio) | hand the agent a new tool | none — a contract |
  > | **1** | **Hooks** (PreToolUse / PostToolUse / Stop) | intercept/rewrite a command pre-run | none — sanctioned |
  > | **6** | **`$PATH` shadow** wrapper | env/arg munging, logging | crude, zero-dep |
  > | **3–4** | **PTY wrap** (tmux / Zellij / `portable-pty`) | *become its terminal*: inject input, tee output, multiplex | language-agnostic, binary untouched |
  > | **7** | **`NODE_OPTIONS=--require`** | patch `https`/`fs`/`child_process` at load | brittle vs updates, ToS exposure |
  > | **7** | **network proxy** (mitmproxy + `NODE_EXTRA_CA_CERTS`) | sit on the API stream | uses app's own proxy plumbing |
  > | **7** | **`LD_PRELOAD`** | shim `connect`/`write`/`openat` at libc | max power, max fragility |
  >
  > **Principle: stay shallow.** Ring 1 survives updates because it's a contract,
  > not a hack. Drop to ring 4 only to own the stream itself; ring 7 only to bend
  > runtime behavior — and pay the fragility tax knowingly.
- `/home/hruzam/unikuklatrix/nablarva/meshup/natural-ladders-grounded-phase.a-sym/Houston.research.skill-script-bonding-layer.md` · deep T1 for Claude Code: complete bonding layer (hooks → skills → bonding mechanisms), community patterns, 7 vectors including !command as wake contract, skill-scoped hooks as regime enforcement, hook-gated regime transitions. · Field map

  > **[verbatim excerpt — meshup/natural-ladders-grounded-phase.a-sym/Houston.research.skill-script-bonding-layer.md]**
  > ### 1.3. The Bonding Mechanisms (The Middle Layer)
  >
  > Between hooks and skills, three mechanisms create the "bonded script" surface:
  >
  > #### 1.3.1. `!command` Shell Injection (Deterministic, Pre-Model)
  >
  > The `!` backtick syntax in SKILL.md body runs shell commands **before** the skill content reaches the model. The command output replaces the placeholder inline — Claude sees only the result, never the command.
  >
  > ```markdown
  > ---
  > name: pr-summary
  > description: Summarise changes in a pull request
  > context: fork
  > agent: Explore
  > allowed-tools: Bash(gh *)
  > ---
  >
  > ## Pull request context
  >
  > - PR diff: !`gh pr diff`
  > - PR comments: !`gh pr view --comments`
  > - Changed files: !`gh pr diff --name-only`
  >
  > ## Your task
  >
  > Summarise this pull request...
  > ```
  >
  > **Trust model:** Deterministic. The script runs unconditionally when the skill activates. The model has no say in whether it runs — only in what it does with the output. This is the closest thing to a "bonded script" in the traditional sense.
- `/home/hruzam/unikuklatrix/nablarva/meshup/natural-ladders-grounded-phase.a-sym/asymmetry.codex-bonding-layer.research.2026-08-05.md` · deep T1 for Codex: four-plane bonding stack, 20 mechanisms, lifecycle hooks, JSONL exec stream, app server, MCP-server mode; mirrors Houston's scope for the other platform. · Field map

  > **[verbatim excerpt — meshup/natural-ladders-grounded-phase.a-sym/asymmetry.codex-bonding-layer.research.2026-08-05.md]**
  > ## 1. Executive Finding
  >
  > Codex does not have one named "bonded script" primitive.
  >
  > Its bonding layer is distributed across four planes:
  >
  > 1. **Instruction plane** — `AGENTS.md`, memories, skills, and custom-agent instructions shape model behavior.
  > 2. **Mechanical plane** — lifecycle hooks, sandbox boundaries, approvals, and command rules intercept or constrain action.
  > 3. **Delegation plane** — custom subagents and multi-agent tools create bounded specialist threads.
  > 4. **Control plane** — `codex exec --json`, resumable sessions, the SDK, MCP-server mode, and the app server let an external program supervise Codex.
  >
  > The most Codex-native opportunity is not merely "a skill with a script." It is a **closed loop across planes**:
  >
  > > instructions choose intent → hooks and rules guard execution → JSONL/app-server events expose state → an external supervisor evaluates results → the same thread or a successor is resumed with corrective context.
  >
  > This composition is stronger than any single primitive. It also creates more failure modes: duplicated policy, event ambiguity, context drift, unsafe external wrappers, and hidden state spread across files and runtime databases.
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md` · practical T1 probe: can one agent read another's live TUI screen? Stage spec with observation discipline. · Field map _(also appears in SCOPE 2)_
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` · T1 execution result: Ink TUI not cleanly readable via `capture-pane` (renderQueue noise); reliable channel is JSONL. · Field map _(also appears in SCOPE 2)_

#### From Epoch's reposoma map (SCOPE-1 — single CLI as a program)

Epoch discipline note carried forward: one-liners are LOCATE gists inferred from path/filename/first-lines, NOT verified summaries; freshness is from filesystem mtime.

- `/home/hruzam/reposoma/raw.research/harness/reports/2026-07-20-harness-lifecycle-skill-injection-safe-protocol.md` · Harness lifecycle / skill-injection mechanics study — mental model "Agent=program, harness=glue," framed as safe-protocol study for harness builder · Epoch: 2026-07-20 aging (18d), recheck against current Claude Code skill-injection behavior
- `/home/hruzam/reposoma/raw.research/harness/reports/2026-08-01-remote-control-tmux-ssh-persistence.md` · Remote control / tmux / ssh persistence for CLI sessions · Epoch: 2026-08-01 current _(Epoch cross-lists this into SCOPE-2 too: two-endpoints-communicating)_
- `/home/hruzam/reposoma/raw.research/harness/reports/2026-07-20-cloud-session-invariance.md` · Cloud session invariance (single-session lifecycle under cloud conditions) · Epoch: 2026-07-20 aging
- `/home/hruzam/reposoma/raw.research/harness/method.ring-trio.md` · Named method doc, likely harness-testing pattern (ring-trio) · Epoch: 2026-07-16 aging, unverified content
- `/home/hruzam/reposoma/raw.research/harness/research-pattern.md` / `.json` / `.jsonl` · Research-pattern schema/log for harness research · Epoch: 2026-06-17 STALE, oldest in tree
- `/home/hruzam/reposoma/raw.research/harness/source-catalog.json` / `.jsonl` · Source catalog for harness research runs · Epoch: 2026-06-17 STALE
- `/home/hruzam/reposoma/raw.research/harness/briefs/kick-brief-R1-research-center.md`, `R2-gemini.md`, `R3-chatgpt-cursor.md`, `R1-contamination-log.md` · Original kickoff briefs for a 3-way (R1/R2/R3) harness research round · Epoch: 2026-06-17 STALE, likely superseded
- `/home/hruzam/reposoma/raw.research/harness/reports/report-R1-research-center-grounded.md`, `report-R2-gemini*.md`, `report-R3-chatgpt-reality-check.md`, `RR-01-brand-competence-*.md`, `triangulation-R1-R2-R3.md` · Grounded reports + triangulation from the R1/R2/R3 round · Epoch: 2026-06-17 STALE
- `/home/hruzam/reposoma/raw.research/claude-code-coldstart/README.md` + `/home/hruzam/reposoma/raw.research/claude-code-coldstart/report/2026-07-21-claude-p-cold-start-mechanics.md` · Claude Code `-p` cold-start mechanics (single CLI program boot behavior) · Epoch: 2026-07-21 aging, worth re-verify (`-p` flag behavior version-sensitive) _(the `-p` question itself is a live fork — see SCOPE 2 F3 + DECISIONS)_
- `/home/hruzam/reposoma/raw.research/agent-docs/report/raw.agent-docs.2026-08-01.md` · Fetched substrate snapshot of claude-code-docs (sub-agents doc, scope precedence table, "background by default since v2.1.198") — 8/8 sources, dated fetch · Epoch: 2026-08-01 current, BUT contains version-pinned claim (`v2.1.198`) that must be re-verified live before quoting
- `/home/hruzam/reposoma/raw.research/agent-docs/report/2026-07-17-claude-skills-nesting-rube-goldberg.md` · Claude skills nesting behavior study · Epoch: 2026-07-17 aging
- `/home/hruzam/reposoma/raw.research/agent-docs/draft/README.md` + `sources.jsonl` · Working notes / source list for agent-docs topic · Epoch: 2026-07-10 aging
- `/home/hruzam/reposoma/raw.research/session-hygiene/report/raw.session-hygiene.2026-08-01.md` · Session hygiene findings (single-CLI lifecycle discipline) · Epoch: 2026-08-01 current
- `/home/hruzam/reposoma/raw.research/session-hygiene/draft/README.md` + `sources.jsonl` · Working draft for session-hygiene · Epoch: 2026-08-01 current
- `/home/hruzam/reposoma/raw.settings/raw.card.claude-code.md` · Knowledge card: Claude Code CLI (version/capability facts) · Epoch: 2026-08-05 current, but decays by half_life_days — verify field before trusting
- `/home/hruzam/reposoma/raw.settings/raw.card.codex-cli.md` · Knowledge card: Codex CLI · Epoch: 2026-08-05 current, same caveat
- `/home/hruzam/reposoma/raw.settings/raw.card.gemini-cli.md` · Knowledge card: Gemini CLI · Epoch: 2026-07-03 STALE-leaning (35d), Gemini CLI ships fast, re-verify
- `/home/hruzam/reposoma/raw.settings/raw.card.session-hygiene.md` · Knowledge card: session hygiene practices · Epoch: 2026-08-05 current
- `/home/hruzam/reposoma/raw.settings/raw.card.claude-ai.md` · Knowledge card: claude.ai (web) · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.settings/raw.card.cursor-ide.md` · Knowledge card: Cursor IDE · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.settings/raw.card.eagle.md` · Knowledge card: Eagle (project-orientation agent) · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.guides/codex-builder-user/codex-line.builder.md` · Builder-side guide for "codex-line" (Codex CLI harness pattern) · Epoch: 2026-08-07 current, written TODAY
- `/home/hruzam/reposoma/raw.guides/codex-builder-user/codex-line.user.md` · User-side guide for "codex-line" · Epoch: 2026-08-07 current, written TODAY
- `/home/hruzam/reposoma/raw.guides/PAD/pad-builder.md` · PAD builder guide (single-agent primitive?) · Epoch: 2026-08-07 current, written TODAY
- `/home/hruzam/reposoma/raw.guides/geminicli@com/subagents.md` · Gemini CLI subagents guide · Epoch: 2026-06-19 STALE, Gemini CLI subagent shape likely moved since
- `/home/hruzam/reposoma/raw.guides/guide-publishing.md` · Guide-publishing process doc · Epoch: 2026-06-17 STALE
- `/home/hruzam/reposoma/raw.guides/recover-broken-loop.md` · Life-hack: recovering a broken agent loop · Epoch: 2026-06-17 STALE (mechanics-focused, may still be valid but unverified)
- `/home/hruzam/reposoma/raw.guides/onboarding-kit.md` · Onboarding kit for new sessions/agents · Epoch: 2026-07-07 aging
- `/home/hruzam/reposoma/raw.guides/bootstrap-new-project.md` · Bootstrap-new-project guide · Epoch: 2026-07-07 aging
- `/home/hruzam/reposoma/raw.guides/project-intake.md` · Project intake process · Epoch: 2026-07-15 aging

### DOUBLES

- **D4 — "Resonance lives in streams. Truth lives in files." (tagline)** touches T1. Both locations are T1 primary substrate:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/old-but-good-onion/terminal-onion-study.md` §8 final lines: `"Resonance lives in streams.   Truth lives in files."`
  - `/home/hruzam/unikuklatrix/nablarva/meshup/old-but-good-onion/interposition-study.md` §8 final lines: `"Resonance in streams.   Truth in files."`
  - Field note: slightly different wordings (interposition drops "lives" twice), same tagline closing the §8 summary block in both sibling files; trivially reworded. **Raw preserved, not merged.**

### FORKS

- **F5 — Adapter session ownership: adapter-launches vs adapter-attaches** touches T1 (harness lifecycle / session control). Marked **UNRESOLVED (tracked fork)**.
  - **Question:** Must adapters always launch their own PTY-owned CLI sessions, or can a later version attach to already-running sessions through official APIs?
  - **Branch A (adapter owns and launches):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.3 and §1.11 (Adapter-owned PTY, contestable decision); `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.2 ("Session control: Provisional / Adapter owns PTY").
  - **Branch B (adapter may attach to running sessions):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.9 "Session attachment" open question; `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/07_AI_HANDOFF.md` open questions (exact structured interfaces available).
  - Field status: A = V1 choice, provisional; B = future-path open question. Not resolved — tracked.
- **F3 — `claude -p` use vs exclude** also has a T1 face (the `-p` reposoma cold-start file above), but its home is the Codex↔Claude bridge → folded in **SCOPE 2 (F3 + DECISIONS FOR MAJKEE)**.

### GAPS

#### Field gaps touching T1
- **G7. Monitor surface compatibility (Sublime/Zed).** Multiple files note Sublime Text (C++ engine) as chosen monitor surface and flag "brick-set compatibility" as open experiment item. No experiment results or compatibility analysis in corpus.
- **G3. V1 implementation code** (shared with T2). All architecture material is conceptual/design; no implementation code for larvad, larva CLI, adapters, or room protocol. (`assymetry-preConsultation.md` has working shell for the Costa bridge specifically — see SCOPE 2.)

#### Epoch gaps touching SCOPE-1
- **No file explicitly titled around "hooks"** despite scope-1 asking for "events, hooks, life-hacks" — closest matches are the harness lifecycle/skill-injection report (2026-07-20) and cold-start mechanics report (2026-07-21); neither is a dedicated hooks doc. Candidate gap for a live research pass if hooks specifically are in scope.
- **codex-line (raw.guides/codex-builder-user/) brand-new (today), not yet cross-referenced** against `/home/hruzam/reposoma/raw.settings/raw.card.codex-cli.md` (2026-08-05) — worth checking these two don't contradict on Codex CLI capability claims.
- **raw.card.*.md decay mechanism unconfirmed** — README says cards decay by `half_life_days` (frontmatter), but this pass read mtimes only, not per-card frontmatter. Read the actual field before trusting any card's currency.
- **No top-level README/INDEX in raw.guides/ or raw.research/** (structural gap; only raw.settings self-documents). A cold reader infers structure from filename convention alone.
- **Version-pinned claim `v2.1.198`** in `raw.agent-docs.2026-08-01.md` (line 9, "Background by default since v2.1.198") NOT yet live-verified — do not carry forward without live re-verification.
- **Gemini CLI staleness:** `raw.card.gemini-cli.md` (35d) and `raw.guides/geminicli@com/subagents.md` (49d) are stale-leaning candidates for a live Epoch pass before any Gemini CLI decision.
- **harness/ R1-R3 round** (all 2026-06-17, 51d) likely superseded by newer harness reports (2026-07-20, 2026-08-01) in same subdir; prefer the newer two unless doing archaeology.

### DECISIONS FOR MAJKEE (T1)

- None originating in T1 alone. The `-p` decision (F3) surfaces here via the reposoma `2026-07-21-claude-p-cold-start-mechanics.md` and the `claude-code` card, but the human call is carried in **SCOPE 2 → DECISIONS FOR MAJKEE (F3)** — do NOT auto-decide it (Field flagged the billing reason as still-live).

#### SCOPE-1 WEB FINDINGS (Epoch web pass, 2026-08-07 — verified)

Full report: `_preflight/research.web.epoch.2026-08-07.md`. Deflated queries, documented tool-surfaces only — the boundary held (no agentive framing).

- **Subagents background-by-default** — CONFIRMED: shipped Claude Code **v2.1.198, 2026-07-01** (verified vs `code.claude.com/docs/en/changelog`). Local corpus claim was correct.
- **Claude Code current version** — **v2.1.223 (2026-08-06)**; local `raw.card.claude-code.md` (2026-08-05) is slightly stale, worth a bump.
- **Codex MCP-server mode** — real (`codex_mcp_interface.md`) but **experimental, subject to change**; exists, exact syntax not locked.
- **Monitor surface** — **Sublime** `exec` build-output panel streams output in real time (documented, supported). **Zed** terminal tool is **stateless / one-shot today** (GH #45557) — not a live monitor yet. (Zed "Terminal Threads" spotted by title only = highest-value follow-up; could flip this.)
- **Still open** — codex's *own* hooks/lifecycle surface (thin result this run), eBPF-on-tty, programmatic PTY libraries.

---

## SCOPE 2 — composites (two programs communicating)

- **Theme:** T2 — "composites" — two programs communicating: claude[codex], codex[claude].
- **Scope:** meshup T2 cluster + Epoch SCOPE-2 reposoma candidates (two programs communicating).
- **What tyler does with it:** enters the corpus on inter-program bridges — the Costa Codex↔Claude consultation bridge, the room/broker N-agent topology, cross-host read attempts, and the reposoma multi-agent/orchestration research.

Start-here:
- **asymmetry pre-consultation** (the bridge derivation) → `meshup/grounded-composites/assymetry-preConsultation.md`
- **costa seed** (the named bridge) → `meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md`
- **the room / broker** → `meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` *(+ 02_DRILLER, 03_COST siblings)*

### SOURCES

#### From Field's meshup map (T2 cluster)

- `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` · primary T2 document: the full research session deriving the consultation bridge; loop 1 (initial `-p` design), loop 2 (blocking wrapper + room protocol), loop 3 (comprehensive design report); all shell code. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` · T2 crystallization: the named bridge ("Costa"), core inversion, doorbell/meaning separation, probe sequence A–E, -p exclusion, trust tier question. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` · T2 at scale: the room with `larva-agent-claude` and `larva-agent-codex` as two adapters communicating through `larvad`; covers the broader N-agent topology. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md` · output-cleaning stage: hard prefilters, reversible tokenization, sparse vector/tensor representation, synchronization, transforms, mathematical reconstruction. (descriptor from set `00_README`) · ⚠ **audit-fix reachability pointer** — Field's clustering never assigned this file; placed here with its `01_`/`04_` siblings by reachability, NOT interpretation — verify theme against raw.
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md` · resource cost, where the real complexity lies, why the full generalized tokenizer engine is parked rather than discarded. (descriptor from set `00_README`) · ⚠ **audit-fix reachability pointer** — Field's clustering never assigned this file; placed here by reachability, NOT interpretation — verify theme against raw.
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md` · T2 attempt: Atlas tries to read a remote agent over Tailscale (cross-host composite, read-only). · Field map _(also appears in SCOPE 1)_
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` · T2 result: partial; read of chrome possible, transcript unreadable. · Field map _(also appears in SCOPE 1)_

#### From Epoch's reposoma map (SCOPE-2 — two programs communicating)

Epoch discipline note carried forward: one-liners are LOCATE gists inferred from path/filename/first-lines, NOT verified summaries; freshness is from filesystem mtime.

- `/home/hruzam/reposoma/raw.research/cli-fork-branch/cli-fork-branch.source-map.2026-08-05.md` · Source map for CLI fork/branch topic — likely session-forking across CLI instances (composite pattern) · Epoch: 2026-08-05 current
- `/home/hruzam/reposoma/raw.research/cli-fork-branch/report/raw.cli-fork-branch.2026-08-05.md` · Report deliverable for cli-fork-branch · Epoch: 2026-08-05 current
- `/home/hruzam/reposoma/raw.research/octopus-pilot/program.pulse.md` · Octopus-pilot program pulse — multi-agent/multi-program orchestration pilot · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.research/octopus-pilot/session/tasks/T1.md` · Octopus-pilot session task T1 · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.research/octo-launcher.handoff.claude.md` · Handoff doc for an "octo-launcher" — likely the multi-instance launcher for octopus-pilot · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.research/program-pulse.contract.claude.md` · Contract doc for program-pulse pattern (cross-program status protocol) · Epoch: 2026-07-16 aging
- `/home/hruzam/reposoma/raw.research/multi-agent-composition-and-swarms.seed.2026-06-16.md` · Seed doc on multi-agent composition/swarms · Epoch: 2026-06-16 STALE, oldest research file in tree
- `/home/hruzam/reposoma/raw.research/swarm-composition-source-loop.md` · Swarm composition source loop pattern · Epoch: 2026-06-17 STALE
- `/home/hruzam/reposoma/raw.research/agentic-sovereignty.source-map.2026-06-16.md` + `/home/hruzam/reposoma/raw.research/agentic-sovereignty.report.2026-06-16.md` · Agentic sovereignty source-map + report — likely governs autonomy boundaries in composite/multi-agent setups · Epoch: 2026-06-16/17 STALE
- `/home/hruzam/reposoma/raw.research/real-reposoma-domain-seats.seed.md` · Domain-seat allocation seed (which agent owns which domain — cross-agent boundary design) · Epoch: 2026-06-17 STALE
- `/home/hruzam/reposoma/raw.settings/raw.card.gty.md` + `/home/hruzam/reposoma/raw.settings/raw.card.gty.addendum-by-majkee-headless-regime.md` · Knowledge card "gty" + headless-regime addendum — likely a cross-program/headless orchestration pattern (name not expanded, verify) · Epoch: 2026-06-19/20 STALE
- `/home/hruzam/reposoma/raw.settings/raw.card.autonomous-orchestrator.md` · Knowledge card: autonomous orchestrator pattern (composite control) · Epoch: 2026-06-20 STALE
- `/home/hruzam/reposoma/raw.settings/agents-staging/epoch.md`, `orby.md`, `agy/orby.SKILL.md`, `agy/FORMAT-FINDINGS.md` · Agent drafts pre-promotion — epoch.md is a draft of THIS agent; orby.md + orby.SKILL.md suggest a second agent seat that composites with Epoch · Epoch: 2026-06-19 STALE, epoch.md draft worth diffing against live definition
- `/home/hruzam/reposoma/raw.research/harness/reports/2026-08-01-remote-control-tmux-ssh-persistence.md` · (cross-listed from SCOPE-1) remote-control persistence is inherently two-endpoints-communicating (local driver + remote tmux/ssh target) · Epoch: 2026-08-01 current

### DOUBLES

- **D1 — "tmux carries the doorbell; files carry meaning."** touches T2. Both locations are T2:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` line 369 (loop 2, Layer 1 section): `"**tmux carries the doorbell; files carry meaning.**"`
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` line 27 (§The Separation): `"**tmux carries the doorbell; files carry meaning.**"`
  - Field note: verbatim, bold in both; costa.seed explicitly cites its source as the asymmetry research. **Raw preserved, not merged.**
- **D2 — "Can a living interactive agent be used as a deterministic callable cognitive process without collapsing it into SDK mode?"** touches T2. Both locations are T2:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` line 768 (loop 2 pushback section, final line of loop 2).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` line 13 (§The Research Question).
  - Field note: verbatim block-quote in both; costa labels it "The Research Question" and attributes it to Asymmetry. **Raw preserved, not merged.**
- **D6 — The `.agent-room/` directory structure (BORDERLINE)** touches T2. Both locations are T2:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` loop 2 (lines ~374–385, room protocol): `.agent-room/` with `requests/ responses/ signals/ active/ archive/`.
  - `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` (lines 73–80): `.agent-room/` with `sessions/costa-…/consultation.md`, `archive/`, `room.sh`.
  - Field note: layouts diverge significantly (costa uses a `sessions/` subdirectory and git-tracked single file rather than separate requests/responses/signals); flagged as a near-double on the top-level `.agent-room/` name/concept only — "not a strong D candidate, leave for the caller to assess." **Raw preserved, not merged.** → carried to DECISIONS FOR MAJKEE below.

### FORKS

- **F3 — `claude -p` use vs exclude** touches T2 directly (the Codex↔Claude bridge invocation method). Marked **UNRESOLVED — human call pending (see DECISIONS)**.
  - **Question:** Should `claude -p` (non-interactive headless mode) be used as the invocation method for the Claude participant in the Codex↔Claude bridge?
  - **Branch A (use -p):** `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` loop 1 (lines 29–66, "Codex → shell → Claude Code" section; working bash script using `claude -p --model sonnet --allowedTools "Read,Grep,Glob"`). Also reposoma: `/home/hruzam/reposoma/raw.research/claude-code-coldstart/report/2026-07-21-claude-p-cold-start-mechanics.md`.
  - **Branch B (exclude -p):** `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` §"The -p Exclusion" (lines 83–91); `/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/assymetry-preConsultation.md` loop 2 (§Layer 0) and loop 3 (§"# 2 Why avoid claude -p").
  - Field status: Position B (exclude -p) is the settled direction in loop 2/3 and the costa seed; Position A appears only in loop 1 and is superseded within the same file. Candidate for "superseded, later wins" — BUT the explicit architectural reason (billing uncertainty) is load-bearing and may shift again. → DECISIONS FOR MAJKEE.

### GAPS

#### Field gaps touching T2
- **G8. Codex as MCP server for direct Claude invocation.** `assymetry-preConsultation.md` notes (post-research confirmation) that Codex's MCP-server mode "means Claude Code could call Codex as a tool directly (no room script, no files). Cleanest one-shot path." Mentioned only once as an alternative, not developed. Costa's probe E covers the reverse direction; the MCP-as-substitute-for-room path has essentially zero corpus coverage.
- **G3. V1 implementation code** (shared with T1). No implementation code for larvad, larva CLI, adapters, or room protocol; the nabLarva broker has no code. (`assymetry-preConsultation.md` has working shell for the Costa bridge specifically.)

#### Epoch gaps touching SCOPE-2
- **"gty" card** (`/home/hruzam/reposoma/raw.settings/raw.card.gty.md` + headless-regime addendum) — name never expanded in Epoch's pass; if load-bearing for composite reading, confirm meaning by reading, not inferring.
- **Octopus-pilot / octo-launcher cluster** (2026-07-16) touches scope-2 directly (multi-instance launcher) but has no visible newer report — unclear if active or dormant. Status check before relying on it as current composite-pattern doctrine.
- **agentic-sovereignty / multi-agent-composition-and-swarms / real-reposoma-domain-seats cluster** (all 2026-06-16/17, 51+d) is the oldest material touching scope-2 — predates the more recent cli-fork-branch (2026-08-05) and octopus-pilot (2026-07-16) work. If scope-2 reading starts here, flag that domain-seat conclusions may have been superseded.
- **No top-level README/INDEX in raw.research/** (structural) — draft/report pairing per-topic is the only implicit structure.

### DECISIONS FOR MAJKEE (T2)

- **F3 — `claude -p` use vs exclude.** Field flagged this as maybe "superseded, later wins" (Position B / exclude is the settled direction in loop 2/3 + costa seed) BUT with a still-live billing reason: "uncertain future Anthropic pricing of SDK/headless mode (billing shift announced then cancelled)." **Do NOT auto-decide.** The architectural reason is load-bearing and may shift again — human call. Branches and locations as under FORKS above.
- **D6 — borderline `.agent-room/` double.** Field explicitly declined to rate this a strong double: the two `.agent-room/` layouts diverge (requests/responses/signals/active/archive vs sessions/archive/room.sh). "Leave for the caller to assess." **Human call whether these are one convention with drift or two distinct designs.** Locations under DOUBLES above. Raw preserved, not merged either way.

---

## ORCHESTRATION CONCEPT — parked forks (later, under tyler)

CREATURE ⟷ primary-larva + F2 (Python/C++) + F5 (adapter ownership). All UNRESOLVED — your calls.

- **Theme:** T3/T4 — the orchestration-concept fork: living process (Y / stridulator / CREATURE) vs file-only (X / primary-larva), plus related orchestration forks.
- **Scope:** meshup T3/T4 cluster + the fork records F1, F2, F5 (all touching room/broker orchestration).
- **What tyler does with it:** enters an UNRESOLVED fork. Both branches are located and preserved. Tyler reads BOTH before any decision; the gavel is not closed in the corpus.

### SOURCES

#### T3 — CREATURE / room-is-a-process (Y position) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` · the canonical Y document: stridulator as one small static binary; PTY adoption; in-memory socket routing; structural regulation (turn quotas enforced by router, not agents); failure story (hard failure). · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "Y — room-is-a-process" · Y described for fresh reader; the bus-mediated, structure-enforced alternative. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.11 · hybrid that substantially adopts Y (broker process = larvad; adapter-owned PTY); broker vs files/FIFOs contestable decision resolved in favour of broker. · Field map

#### T4 — primary-larva / room-is-a-file (X position) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` · the X formulation (pre-triangulation); "COMPOSER = most hardcoding"; roller; "dialogue-room repo?"; no daemon posited. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "X — room-is-a-file" · X described: roller, git-diff wire, cooperative anchors, fails soft; position that died (git-as-wire reversed mid-session). · Field map

#### Fork record files (both positions present) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` · convergence record; deaths of X-specific elements; gavel item 1 (files-only spike: yes or no?). · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` · decision ledger holding both alternatives with status. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md` · transmission that resolves toward hybrid. · Field map

_(No reposoma SCOPE candidate is assigned to this fork by Epoch's map; the orchestration-fork material is meshup-side. Epoch's scope-2 multi-agent/orchestration research is folded in SCOPE 2 above.)_

### FORKS

#### F1 — CREATURE vs primary-larva — the archetype fork (per brief) · UNRESOLVED
- **Question:** Should the nabLarva room be regulated by a living process (structural enforcement) or by file conventions alone (cooperative enforcement)?
- **Branch A (CREATURE / room-is-a-process / Y):** the stridulator: one small static binary; PTY adoption; in-memory socket routing over Unix domain sockets; turn quotas and drift gates enforced by the router, not requested of agents; an agent cannot drift on traffic it never receives. Fails hard (dead router = dead room).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` (entire document, Oraculum's sealed position)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "Y — room-is-a-process"
- **Branch B (primary-larva / room-is-a-file / X):** ledger-mediated; roller as append-only markdown; regulation by cooperative convention; agents obey anchors because they're told to; git-as-wire (reversed mid-session, but position held by majkee). Fails soft (a file is always readable).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` (majkee's original position; Cluster A + B)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "X — room-is-a-file"
- **Field status (verbatim intent):** The Wave conversation (`01_ARCHITECTURE_ROOM_AND_BROKER.md`) proposes a hybrid broker (larvad) substantially closer to Y/CREATURE; the triad voted 2:1 against X. Gavel item 1 remains open: "files-only control spike — build X-pure as one-day control experiment, or accept 2:1 vote and skip." **Not resolved; gavel pending.** → DECISIONS FOR MAJKEE.

#### F2 — v1 language: Python stdlib vs C++ · UNRESOLVED
- **Question:** What implementation language for the nabLarva broker (larvad) and adapters?
- **Branch A (Python stdlib first):** delivery speed, zero deps, rapid experiment and PTY support (`asyncio`, `pty`, `subprocess`); Rust rewrite only after real reliability/performance pressure demonstrated.
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.10 (V1 recommended technology)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.6 ("Python standard library: Provisional V1")
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` deaths section ("C++/Go static binary as Y language: outvoted by Python-stdlib-first")
- **Branch B (C++):** majkee's stated learning appetite; "smallest safe solution" implies writing C++ to learn it on this project; explicitly not overridden — only majkee weighs this decision.
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §8 gavel item 2 ("Python-stdlib-first (Z's argument) vs majkee's appetite to learn C++ on this. These optimize different goods: delivery speed vs growth. Only majkee weighs.")
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` gavel item 2
- **Field status:** Technical recommendation = Python. Personal call = C++. Majkee's gavel not recorded in corpus. → DECISIONS FOR MAJKEE.

#### F5 — Adapter session ownership: adapter-launches vs adapter-attaches · UNRESOLVED (tracked)
- **Question:** Must adapters always launch their own PTY-owned CLI sessions, or can a later version attach to already-running sessions through official APIs?
- **Branch A (adapter owns and launches):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.3 and §1.11; `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.2.
- **Branch B (adapter may attach to running sessions):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.9 "Session attachment"; `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/07_AI_HANDOFF.md` open questions.
- **Field status:** A = V1 choice, provisional; B = future-path open question. Not a resolved fork — a tracked fork. _(Also cross-referenced in SCOPE 1.)_

### DOUBLES

- **D3 — Promotion criteria — 7-item list for a finding to enter production** touches this theme (staged-decision / lab-to-production, part of the room's anti-drift regulation). Two locations:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md` §4.12 (lines ~315–324): "1. repeatable fixture; 2. precise signal definition; 3. supported CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md` Message 4: "1. repeatable fixture; 2. precise observable signal; 3. explicit CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."
  - Field note: items 2 and 3 differ in one word each; items 1, 4–7 verbatim. **Raw preserved, not merged.**
- **D5 — nablarva.wave.full-report.2026-08-05.md contains verbatim doubles of all chapter content** touches this theme (the fork records 01/05/06 are chapters inside the aggregate). `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md` opens identically to `00_README.md` and reproduces chapters 01–07 verbatim. Field note: systematic (derived aggregate, not authored separately), not flagged individually. **Raw preserved, not merged.**

### GAPS

#### Field gaps touching orchestration
- **G1. Conflict resolution for shared writes (load-bearing gap).** Flagged "unresolved, load-bearing" in `seed.entity.full-idea.2026-08-02.md` (§open), raised to "LOAD-BEARING PRECONDITION" in `triangulation.entity.symmetry-x-asymmetry.2026-08-03.md` (#conflict-is-ontology: "no multi-host write topology before the conflict rule exists"), and listed as an open question in `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`. No file proposes a concrete mechanism. _(Also surfaces in METHOD/STYLE via the entity files.)_
- **G2. Math engine research.** Referred to repeatedly as "untabled, blocks final forge" (`handoff.applications-in-common.2026-07-31.FINAL.md` §11 thread 1; `triad.comparison.2026-07-31.md` "Untabled (blocks final forge)"). No file in the corpus contains this material.
- **G4. Cluster B (product/strategy) elaboration.** `seed.oraculum.2026-07-31.md` splits material into Cluster A (mechanism) and Cluster B (product/strategy); Cluster A heavily documented, Cluster B (nabLarva identity, multi-vendor onboarding, human-team hub / stridularium as product) has almost no corpus presence beyond the seed's sketch. The provisorium content referenced in the handoff is not present.
- **G6. Gavel outcomes.** 7-item gavel docket (`triad.comparison.2026-07-31.md`) and associated decisions (language, git residual seat, component naming, V1 sweet-spot, journal store, broker lifecycle) have no resolution document in the corpus. Gavel process announced as starting on "nabla-lab side" at session close; outcomes absent.
- **G3. V1 implementation code** (shared with T1/T2) — no code for larvad, larva CLI, adapters, room protocol.

### DECISIONS FOR MAJKEE (T3-T4)

- **F1 gavel item 1 — files-only control spike: yes or no?** Build X-pure as a one-day control experiment, or accept the 2:1 vote against X and skip. Gavel pending; not resolved in corpus. Branches/locations under F1 above. **BOTH branches preserved — do not collapse to the hybrid.**
- **F2 — v1 language: Python stdlib vs C++.** Technical recommendation = Python; personal call = C++ ("only majkee weighs" — delivery speed vs growth appetite). Majkee's gavel not recorded in corpus. Locations under F2 above.
- **G6 — the wider 7-item gavel docket** (`triad.comparison.2026-07-31.md`) has no resolution document; its outcomes are a standing human/gavel obligation flagged by Field as absent from the corpus.

---

## METHOD / STYLE — how blind questions are posed

The symmetry/asymmetry entity dialogue (the "pure gold" exemplars) + the §11 lens palette in the brief.

- **Theme:** STYLE (the symmetry/asymmetry entity dialogue — how blind philosophical questions are posed) + SUPPORT (sella & co; buffer / bride-and-book; misc).
- **Scope:** meshup STYLE-exemplar cluster + SUPPORT cluster. (No reposoma candidates assigned — this is meshup-side.)
- **What tyler does with it:** consults STYLE as the exemplar of the blind-triangulation question/answer form (not as content to fold into architecture), and SUPPORT as the connective / parked / index tissue around the main themes.

### SOURCES — STYLE exemplars (the entity dialogue)

All under `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/`

- `.../seed.entity.vision-not-explored.2026-08-02.md` · the question instrument itself; exemplar of how to pose position-free philosophical probes (E1–E8, S1–S8, extended palette); the [canon]/[blind] reading-key device is demonstrated in the sibling seed. · Field map
- `.../seed.entity.full-idea.2026-08-02.md` · exemplar of the seed format with `[canon]`/`[blind]` dual-reading annotation; `#brakes` section; grep-tags; fork ledger. · Field map
- `.../reply.entity.vision-not-explored.md` · Asymmetry's blind answer: exemplar of how the blind walk proceeds in practice; structurally models what an agent uncontaminated by vocabulary produces. · Field map
- `.../replies.symmetry.vision-not-explored.2026-08-03.md` · Symmetry's reference-strain answer: the "fixed point" the blind answers are measured against; different name (RIVERBED-BEING vs Inscribed Continuant vs ENTITY/ameba). · Field map
- `.../triangulation.entity.symmetry-x-asymmetry.2026-08-03.md` · collision/measurement record: exemplar of how the divergence map is read and what gets adopted. · Field map
- `.../triangulation.entity.round-two.2026-08-04.md` · round-two: exemplar of multi-round triangulation where corrections flow back and a live disagreement (#bed-vs-discipline) is deliberately preserved as an instrument. · Field map
- `.../reply.entity.full-idea.md` · Asymmetry post-revelation: exemplar of what is adopted vs what stays as pressure. · Field map
- `.../replies.symmetry.entity-full-idea.incontext.2026-08-03.md` · Symmetry in-context: exemplar of "the author's own pressure" on their own work (#bed-not-water, #router-weather, #noether-test). · Field map

### SOURCES — SUPPORT (sella & co; buffer/bride-and-book; misc)

- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md` · the buffer/bride-and-book document: Nabla's provenance substrate; the Braid/Book dual projection; `[ARCH]/[NABLA]/[MEASURED]/[INFERRED]/[OPEN]` tagging discipline. Named role in the broader system. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md` · support: test harness for the seam probe. · Field map _(primary home: SCOPE 1 / SCOPE 2)_
- `/home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` · support: probe execution results. · Field map _(primary home: SCOPE 1 / SCOPE 2)_
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/07_AI_HANDOFF.md` · support: session-closing state handoff format. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/00_README.md` · support: index/governing-principle document. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/parked.larvanizer-tensor-drill.2026-08-04.md` · support/parked: larvanizer staging concept; wake conditions. · Field map

#### Derived/composite artifacts (read-only, not original sources) — Field PART 1
- `/home/hruzam/unikuklatrix/nablarva/meshup/repomix.meshup.md` · Repomix-generated concatenation of all other source files; automated merge artifact, not an authored document; excluded from theme clustering. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md` · Aggregated version of the Wave conversation export; opens identically to `00_README.md` and concatenates the chapter files verbatim; no unique content beyond the chapter files. · Field map _(see D5)_

### DOUBLES

- **D5 — nablarva.wave.full-report.2026-08-05.md contains verbatim doubles of all chapter content** touches SUPPORT (the aggregate is a support/derived artifact and opens identically to the support index `00_README.md`).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md` vs `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/00_README.md` + chapters 01–07.
  - Field note: systematic (derived aggregate); noted as a structural property, not flagged individually. **Raw preserved, not merged.**
- _(D1, D2, D6 → SCOPE 2; D3 → ORCHESTRATION CONCEPT; D4 → SCOPE 1. None are STYLE-internal doubles.)_

### FORKS

- **F4 — #bed-vs-discipline — what IS the entity's identity?** touches STYLE (the entity dialogue). Marked **UNRESOLVED — deliberately preserved as an instrument.**
  - **Question:** Is the entity's identity the durable file plane itself (the bed), or the invariant transition discipline by which the bed continues functioning as THIS bed?
  - **Branch A (identity = the bed / "RIVERBED-BEING"):** identity is the durable, tended store — files plus conventions that keep them coherent; the body is what persists, can be injured, can be inherited. "The bed holds; the water is honest about being water."
    - `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.vision-not-explored.2026-08-03.md` (S3, HERAKLIT-1, synthesis — "RIVERBED-BEING")
    - `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.entity-full-idea.incontext.2026-08-03.md` §3
  - **Branch B (identity = the discipline / "Inscribed Continuant"):** identity = the set of invariants reproduced by the system's discipline across allowed transformations, without requiring any single component to preserve them alone. Store completely migrated → identity survives via discipline + provenance → identity was never literally the files.
    - `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/reply.entity.full-idea.md` (§"Where my blind answer adds pressure"; closing brake)
    - `/home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/triangulation.entity.round-two.2026-08-04.md` §3 (#bed-vs-discipline) and §1 (#noether-corrected)
  - **Field status (verbatim intent):** Deliberately unresolved. `triangulation.entity.round-two.2026-08-04.md` §3: "DO NOT resolve linguistically. The gap is itself an instrument — substrate migration is a Noether transformation, so the disagreement is SCOREABLE: run a migration test someday; whichever reading predicts the outcome better wins the word." Resolution mechanism = a migration test, not a majkee gavel — kept as UNRESOLVED, not sent to DECISIONS.

### GAPS

- **G1. Conflict resolution for shared writes (load-bearing gap)** surfaces in the STYLE/entity files: flagged "unresolved, load-bearing" in `seed.entity.full-idea.2026-08-02.md` (§open), raised to "LOAD-BEARING PRECONDITION" in `triangulation.entity.symmetry-x-asymmetry.2026-08-03.md` (#conflict-is-ontology). No concrete mechanism proposed. _(Primary home: ORCHESTRATION CONCEPT.)_
- **G5. Brick-factory stock.** Referred to as "untabled, relevant to adapters/monitor layer" (`handoff.applications-in-common.2026-07-31.FINAL.md` §11 thread 2). No file describes what the brick factory is or produces; one participant name (Ommatidium, "PTY tap / bridge (brick1.py lineage)") suggests existing code in the brick line, but nothing is present here. _(SUPPORT-adjacent — provenance/monitor tissue.)_

### DECISIONS FOR MAJKEE (STYLE-SUPPORT)

- None requiring a human gavel originate in STYLE-SUPPORT. **F4 (#bed-vs-discipline) is deliberately left UNRESOLVED by design** — its authors specified resolution by a future migration test, not by decision. It is recorded here as an open instrument, not a pending majkee call. (The corpus-wide human calls are carried in SCOPE 2 — F3, D6 — and ORCHESTRATION CONCEPT — F1 gavel item 1, F2, G6.)

---

## YOUR OPEN DECISIONS (consolidated — preserved forks · none block scope-1)

The human calls, gathered from all sections. Detail (branches + verbatim locations) lives under each section's FORKS / DECISIONS blocks above — repeated here as the single docket.

- **F3 (`claude -p` use vs exclude)** → SCOPE 2. Position B (exclude) is the settled direction in loop 2/3 + costa seed, BUT the billing reason is still-live ("uncertain future Anthropic pricing of SDK/headless mode — billing shift announced then cancelled"). **Do NOT auto-decide.** Also carries a T1 face (reposoma `-p` cold-start file).
- **D6 (borderline `.agent-room/` double)** → SCOPE 2. Two layouts diverge (requests/responses/signals/active/archive vs sessions/archive/room.sh). **Human call: one convention with drift, or two distinct designs.** Raw preserved either way.
- **F1 gavel item 1 (files-only control spike)** → ORCHESTRATION CONCEPT. Build X-pure as a one-day control experiment, or accept the 2:1 vote against X and skip. **BOTH branches preserved — do not collapse to the hybrid.**
- **F2 (v1 language: Python stdlib vs C++)** → ORCHESTRATION CONCEPT. Technical recommendation = Python; personal call = C++ ("only majkee weighs" — delivery speed vs growth appetite). Majkee's gavel not recorded in corpus.
- **F5 (adapter session ownership: adapter-launches vs adapter-attaches)** → SCOPE 1 + ORCHESTRATION CONCEPT. UNRESOLVED (tracked): A = V1 choice, provisional; B = future-path open question.
- **G6 (the wider 7-item gavel docket)** → ORCHESTRATION CONCEPT. `triad.comparison.2026-07-31.md` docket (language, git residual seat, component naming, V1 sweet-spot, journal store, broker lifecycle) has no resolution document — a standing human/gavel obligation.
- **F4 (#bed-vs-discipline)** → METHOD/STYLE. NOT a majkee call: deliberately left UNRESOLVED, resolution by a future migration test, not a gavel. Listed here for completeness as an open instrument.

---

## FOOTER → REPORTER

> Frontmatter item: `reporter: "<waiting on agent>"` — fill with the colleague's handle once the seat is taken.

majkee's standing tasks for the collaborating colleague (AI) who edits this book **during sessions** — edit-only, per the maintenance model in `## BUILD PART`. This is majkee's task bed for the book itself; it is orientation for *me* and my colleague, **not** agent-consumed instruction (the file is not wired to any LLM — see banner).

- **Keep the partitions honest.** When a fork resolves, move its chapter's door-state `opened` → `closed`; keep `common-knowledge` limited to settled vocabulary + the skeleton (`## BONDS`).
- **Fold, don't author.** New findings arrive from named research runs (recorder build). Fold their *pointers* in — edit-only, never invent content. Pointers only; nothing here is a summary.
- **Bump what's flagged stale.** e.g. `raw.card.claude-code.md` is behind current version (SCOPE-1 web findings) — carry the bump when the card refreshes.
- **Append, don't renumber.** New chapters go **above** this FOOTER; the FOOTER stays last (headers are named, not numbered).

_(Reporter seat empty. Add concrete per-session tasks below this line as they arise.)_
