# Audit 2 of 3 — proposed rewrites for the project-design wrapper

*Oraculum · Claude · 2026-09-29 · session `nablarva-00`.*
*Target: [AGENTS.PROJECT-DESIGN.md](../AGENTS.PROJECT-DESIGN.md).*
*Status: candidate text. The wrapper itself was not edited.*

**For Cartan, as the assigned Convergence maintainer.** The role file says Majkee
assigns one maintainer at a time, so this audit proposes and does not write. Fold what
Majkee approves. Every block below is a proposal until then.

Evidence marks are the same as in [audit 1](audit.patterns-and-loop.oraculum.2026-09-29.md) §0.

## 1. Findings, chapter by chapter

| Where | Finding | Severity |
|---|---|---|
| Frontmatter `source` | Points to `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/draft.majkee.app-scheme.2026-09-23.md`. That session was pruned on 2026-09-27 `[S]`; the file is missing | Dangling reference |
| §1 | Two fragment bullets. No statement of what the animal owns. "decentralized rag connector" is undefined anywhere | Thin |
| §2, item 2 | Asks to check runbook-tool sessions. `-00` is pruned, `runbook-upgrade` and `-02-app` are pruned, `runbook-tool-01-coordination` is open and blocked `[S]` | Stale |
| §2.1, item 1 | Path `~/unikuklatrix/nablarva/.dev/session/toobox-instarmux` does not exist | Dangling reference |
| §2.2 | Sound and current. It links the working blueprint and the workflow reading | Keep |
| VOLATILE | Sound and current | Keep |
| §3 numbering | "3.1.1 demanded tree" sits under 3.2. "function ADD" uses six hashes, "function create" uses two | Broken structure |
| §3.1 termbrana | Describes the original intent (a semi-transparent foil, one typing system, notes with anchors). The README describes a read-only observation and replay layer with a side pane; "the overlay experiment was dropped" `[R: README lines 3–4, 27]` | Two descriptions, unreconciled |
| §3.2 ovitmugen | Majkee's text plus Trajectory's append-only notes. The notes are accurate and must stay untouched | Keep; renumber only |
| §3.3 instarmux | Empty heading. Majkee, 2026-09-29: it is another animal, a reserved slot | Mark as reserved |
| §3.4 reposoma tool | Empty heading. The role file forbids empty sections | Fill or remove; Majkee's call |
| §3.5 muticula | Sound | Keep |
| Missing | The loop; the toolbox rule; the strata; stridularium; the sensing family; the consultation carriers; the runbook browser; the phone console; the multiplexer choice | Gaps |

## 2. Proposed text

Majkee's original words are kept as quotations wherever a chapter is rewritten.

### 2.1 Frontmatter

~~~yaml
source: /home/hruzam/ia-sync/.dev/session/runbook-upgrade-02-app/raw/draft.majkee.app-scheme.2026-09-23.md
source-state: pruned with its session on 2026-09-27; recover from ia-sync git history if needed
~~~

### 2.2 Chapter 1 — what it is

~~~markdown
# 1. What it is

## 1.1 nabLarva (the animal)

nabLarva is a bus between living agent sessions of different vendors. It removes the
human from the courier role and keeps him at the decision points.

- It owns the continuity of an exchange: who addressed whom, what was released, which
  reply belongs to it, and what still needs attention.
  (Cartan, working blueprint §1 — a proposal)
- It carries meaning in files. Majkee, 2026-09-29: "keep file style at least on bus
  level".
- Each agent works in its own native session, under its own permissions.
- The ladder is locked (flag L2): same host, then cross host, then stridularium.

Majkee's original words, 2026-09-23:
> agentive framework, multisession drive, decentralized rag connector ·
> multisession driving — message bus and control mechanism over vendors and sessions

Open: what "decentralized rag connector" means for the animal is not yet described.

## 1.2 The loop

Majkee, 2026-09-29:
> sender: mailing → attracting → own process on receiver side → releasing reply (file)
> → reply → attract sender

| Step | Done when |
|---|---|
| Mailing | The message file is written once at an agreed path |
| Attract receiver | The receiver's living session holds a pointer to it |
| Own process | The receiver works natively |
| Release reply | The reply file is written once and complete |
| Reply | The file is present and tied to its message |
| Attract sender | The sender's living session holds a pointer to the reply |

The two attraction steps are unmeasured. Majkee's direction: the return-wake probe
comes first.

## 1.3 The animal and its toolboxes

Majkee, 2026-09-29: the toolboxes were made to stand alone as practical helpers. They
can be parts of the bigger animal, like plugins. They must not need the nabLarva
engine to exist.

- A toolbox works without the animal.
- The animal may consume what a toolbox publishes.
- A toolbox never imports the animal.

## 1.4 Strata

| Layer | Owns |
|---|---|
| 5 · Human view and device | What the operator sees and where he sits |
| 4 · Process and terminal | Running programs, PTY, multiplexer |
| 3 · Runtime connection | Reaching a session: attraction, adapters |
| 2 · Exchange | Message, reply, correlation, release, brakes |
| 1 · Durable work | Repositories, locks, status, roles |

A layer's display or process signal does not become another layer's truth.
(Cartan, workflow reading — a proposal)
~~~

### 2.3 Chapter 2 — process

Replace items 1 and 2 and §2.1. Keep §2.2 as it stands.

~~~markdown
# 2. Process

1. Read first, then reconcile.
2. Session tools live in `~/ia-sync/zsh/session/`. State on 2026-09-29: the
   `runbook-tool-00` and both `runbook-upgrade` sessions are closed and pruned.
   `runbook-tool-01-coordination` is open and waits on `codex-identity-resolution`.
   Check each session's STATUS before relying on this line.

## 2.1 Planning phase

Questions still to answer:

1. Wrapper and UI. Majkee's words: "still terminal or some terminal wrapper + process
   window -> real app". Undecided. Until it is decided, increments continue as
   shell-layer bricks (see VOLATILE).
2. Prepared for advice from any seat.
~~~

### 2.4 Chapter 3 — parts

Renumber so every heading sits under its own organ. Use the role file's outline where
evidence exists: what it is, responsibilities, connections, boundaries, open choices,
sources. Leave out any part that would be empty.

~~~markdown
# 3. Parts

## 3.1 termbrana (toolbox)

**Intent.** Majkee's words:
> semitransparent foil allowing one typewriting system over all (keys, shortcuts,
> lighter navigation for terminal inputs -> agentive UI) · bridge between terminal,
> ai session, browser (firefox), files

His example of notes with anchors, and the note that a heavy toolbox can be split by
scope, stay as written.

**Current contract.** A planned independent observation, navigation and replay layer
for terminal sessions. Zellij-first, read-only by default. The repository holds a
compiling probe harness; core, review UI, persistence and replay are not built.
(README)

**Boundaries.** It receives what Zellij renders, never raw PTY bytes. The chosen view
is a side pane; the overlay experiment was dropped. Standalone first (flag L11, L12).

**Open choices.** How the foil intent relates to the side-pane contract. Whether it
needs a dashboard source such as `ov ls --json`.

**Sources.** `toolbox/termbrana/README.md`, `toolbox/termbrana/DECISIONS.md`, flag L11.

## 3.2 ovitmugen (tool)

(Majkee's text unchanged.)

### 3.2.1 Function: add
### 3.2.2 Function: create
### 3.2.3 Other managing options
### 3.2.4 Demanded tree
### 3.2.x @Trajectory notes — append-only, unchanged

## 3.3 instarmux (reserved slot)

Majkee, 2026-09-29: another animal. The name is reserved. No content yet.

## 3.4 reposoma tool

(Majkee to describe, or remove the heading. `~/reposoma` itself is substrate.)

## 3.5 muticula (tool)

(Unchanged.)

## 3.6 Sensing family

Four instruments sense a living CLI session. Each has its own object.

| Instrument | Object | State |
|---|---|---|
| Laboratory (Wave, 2026-08-05) | How a CLI behaves; which signals it exposes | Design only |
| termbrana | Returning to a meaningful terminal event | Probe frozen |
| ommatermia (2026-09-04) | Where agents go blind and need a graphical intervention | Brief only; M0 is an experiment |
| Onion observer (2026-09-18) | Hook, process and viewport samples of one session | Plan only |

An observation is not a release and not a delivery. None is required for the first
loop.

## 3.7 Consultation carriers

`tun` (stored-thread tunnel) and `codex-run.zsh` (fresh relay). The caller waits for
the reply. They reach a headless process or a stored thread, never the living peer.
Keep them separate from the loop.
Sources: working blueprint §10; `~/reposoma/_cold-start/card/CS.tunnel-upgrade.2026-09-21.md`.

## 3.8 Runbook browser

Browses session beds and shows which reply files have arrived. Lives in
`~/ia-sync/zsh/session/`. A view; it holds no delivery state.

## 3.9 stridularium (organ)

Stage 3 of the ladder: a regulated room for humans and their AI collaborators. Which
organ carries the name is docket item 7.

## 3.10 Phone console (k0k0nV3R)

A possible future client: host and session chooser, and a text tray (select, collect,
arrange, release). A sibling project in idea state. Not a dependency of the first loop.

# 4. Open choices

| Choice | State |
|---|---|
| Separate UI, or integration into an editor | Undecided |
| Multiplexer: tmux or Zellij | Both in use by different bricks. The loop should depend on neither |
| Who starts an agent's process: the bus, or the operator | Tracked since August as fork F5; touches flag L3 (S5) |
| Source and promotion model for animal code | Working blueprint §5; touches flag L6 |
~~~

## 3. What must not change

- Trajectory's notes in §3.2.x are append-only. Renumbering their parent heading is the
  only change proposed.
- The VOLATILE section and §2.2 stay as Cartan wrote them.
- The `maintainer` block in the frontmatter stays.

## 4. Related fixes outside the wrapper

These belong to other owners. Listed so they are not lost.

| File | Fix | Owner |
|---|---|---|
| `AGENTS.md`, substrate map | Three dated files moved to `meshup/oraculum-basic-triangulation/`. `meshup/nabla_drafts/` is gone; the seam-probe report is at `meshup/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` `[R]` | Majkee |
| `flag.md`, Untabled | Cites the old seam-probe path. The file is append-only: append a correction line | Majkee |
| `PROJECT.yaml` | Says "docs-only phase". Bricks ship through ia-sync; animal code is still none | Majkee |
| `docs/repo-unification.2026-09-02.md` | Says `pull --rebase`; flag L12 says never `[S]` | Majkee |
| `~/ia-sync/zsh/nablarva/nablarva.zsh` | Engine points at `session/` and the retired sync pair `[R: blueprint lines 199–200]` | Its task owner |
