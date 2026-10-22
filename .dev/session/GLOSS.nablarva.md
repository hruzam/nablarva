# GLOSS.nablarva — majkee's learning file across all nablarva-* sessions

`what: explanatory notes beside the nablarva sessions — the "what are we doing and why" for the`
`human sitting them. UNCANONICAL (like dock.md): never cite as truth; commands live in PADs only,`
`verdicts live in _bus/ VERDICTs and evidence only.`
`scope: all nablarva-<NN>-<phase> sessions (the animal itself; termbrana has its own GLOSS).`
`written by: the driver of each sitting, before the step is run. Opened 2026-09-12 (Oraculum,`
`cSharp of nablarva-01-design).`
`guide: ~/reposoma/raw.guides/gloss/GUIDE.md (GAVELED 2026-09-02)`

## The big picture (read once)

What hurts today: you run several independent AI sessions — a Claude Code window, a Codex
window — and when one needs to hand work to another, *you* are the wire: read, copy, switch
window, paste, explain, wait, notice the answer came back. The only measurement so far is the
runbook-upgrade arc: 86–88 of your messages into one head session over a week. Nobody has yet
counted how many of those were pure carrying — that count is one of the things this arc produces.

What the seam project (the "a-symmetry" briefs) decided, in plain words:

- **Files are the truth.** Whatever two sessions exchange lands as a file (POINT, RETURN,
  VERDICT). If every tool dies, you can still read the files and finish the exchange by hand.
- **You attach to an endpoint, not a leader.** An endpoint is a living session on this machine.
  "Leader" is a role a RUNBOOK hands out; the wire never knows about roles.
- **Vendor UIs are weather.** We build nothing that must understand a Claude or Codex screen.
  The native terminal stays reachable; the tool is a view plus a doorbell, never a replacement
  terminal.
- **You move from wire to gate.** You still decide, approve, redirect. You stop carrying.
- **Interactive stays interactive.** Nothing may quietly route your subscriber session onto
  API billing.

What the first brick is — decided in `nablarva-01-design` (GO, 2026-09-12): a binding record
("seat *cartan* = that Codex window"), a preview that carries pointers not content, correlation
by the BUS POINT's own `return_to:`, and a graduated path: A = attach + preview + copy in the
browser; B = one native operator-triggered assignment into a living Codex session; C = the same
for the Claude head. You chose to qualify **B first** — because B answers the two questions A
never touches: is native delivery safe (L4 untouched), and does it stay on your subscription.

Why so much ceremony for a small tool — the **L4 death**. On 2026-07-31 the triad recorded that
typing text into a session's terminal (tmux `send-keys`) is unsafe as a *message* channel: you
cannot know what the session was doing when the keys arrived. That death still binds. Bed 02
does not touch it: it uses only what Codex ships natively (`codex queue`), and if that fails the
answer is STOP, not a workaround.

Who does what: Cartan (Codex, "Astra") does the engineering. Oraculum (Claude, "Fable") audits,
keeps STATUS, and drives your sittings. You carry paths, open the throwaway session, approve
each activation, sit the steps, and gavel.

Where a build would live: this brick extends a tool that already lives on the **surgical table**
`~/ia-sync` (`zsh/session/`), so its source goes there and `deploy.sh` spreads it. That is the
tool's own rule, not a rule for every future nablarva organ — flag L6 lets experimental organs be
built here and promoted by reviewed merge. Bed 02 builds nothing deployable at all.

## nablarva-01-design · no PAD (design gate — CLOSED, GO)

What you were asked to do, and why each was a human step:

- **Carry a path.** Only the path — the file is the message. What we saw: Cartan found the
  POINT by opening the bed on its own clock, and both sessions could read each other's on-disk
  transcript when you said "new lines" — a zero-build way to carry less, but you were still the
  doorbell.
- **Say "confirm" once** on the adopted RUNBOOK — so the launcher you read is the launcher
  Cartan reads.
- **Read the VERDICT, not the RETURN.** GO was recorded against a numbered design file
  (`raw/design.r1.md`, hash `b43d10…`) — "the version you approved" is a file, not a memory.

Still owed here, two words from you: `count = <n>` (your actions for that first carry) and
`commit ok` (lets the bed be saved in git before it is pruned — files first, then deletion).

## nablarva-02-pipe-qualification · pad.1-b-entry (not yet written — steps below are the plan)

**What this bed asks, in one sentence:** can Codex's own `codex queue` put an assignment into
a *throwaway* Codex window you opened, and can that window answer with the right file — without
anyone typing into its terminal, without touching its permissions, and without leaving your
subscription. If yes, that is the pipe. If no, we stop and think, we do not improvise.

**Why throwaway sessions:** a wrong send into your working Cartan would be the exact misfire the
whole project exists to prevent. Everything here happens against a session you open for the
purpose and can close without loss.

**Step by step — what happens, what it costs you, my lean:**

1. **P0 — Cartan reads, nothing runs.** You carry one path (or say "new lines"). Cartan writes
   two files: what the installed Codex actually offers (route to a living session, identity vs
   running instance, state flags, permissions, how to *see* subscriber usage), and an executable
   plan with your hands-on steps marked `[HANDS]`. Impact on you: one carry. Lean: none needed.
2. **P1 — I audit.** Rerun kraken, dated-docs kraken, Janus. Then I turn the audited plan into a
   PAD (one step at a time, copy-paste, expected output, branch per outcome) and write the notes
   here before each step. Impact: none until I ask you to arm.
3. **P2 — you arm (gavel).** Open one named Codex session in a scratch folder the plan names
   (e.g. `/tmp/nablarva-b-entry/`), default permissions, nothing special. Tell me its name. Then
   say "activate" for that exact target — one approval per sitting; a new target is a new
   approval. Impact: two actions. Lean: do it; it is the only way to learn anything real.
4. **P3 — the sitting.** STEP 0 proves the target is alive, idle, and not one of the working
   sessions. Then one positive case (assignment in, RETURN file out at the exact path), then
   the negative cases: wrong/stale target · replaced instance · duplicate send · interruption
   mid-flight · busy/awaiting-approval (rule: no submission). Each step ends with you pasting
   the output into the PAD. Impact: ~8–12 steps, each small. Lean: sit them in order; if any
   step shows an override, a screen-parser dependence, or a usage-path surprise, we stop there.
5. **P3-opt — the characterization test (gavel).** Queue a message *while* the target is
   mid-turn to see what Codex does: deliver at the next turn boundary (the good outcome),
   inject, or refuse. It is observation only and needs your explicit yes. Impact: one extra
   step. Lean: **yes** — it is the single fact that decides whether readiness can be native;
   but it never becomes a delivery path in this bed.
6. **P4 — VERDICT, then your GO/STOP (gavel).** GO = the mechanism is qualified; the next bed
   can build the binding record + preview around it. STOP = native delivery is not trustworthy
   today; the fallback is what we already do (files + your carry), and any L4 exception would be
   a separate, explicit gavel — never a fallback inside this bed. Lean: none until evidence.

**Words new in this bed:**

| word | means | how you recognise it |
|---|---|---|
| **disposable target** | the throwaway Codex session opened for the sitting | named in STATUS `target:`; never `…c57d8` |
| **arm** | you name the target and approve activation for one sitting | STATUS gains a `target:` hold |
| **queue** | Codex's own "put a message in an existing session's inbox" | `codex queue --thread … --message …` |
| **activeFlags** | the daemon's word for "busy / waiting for approval" | read via app-server, never from the screen |
| **characterization** | an observation-only test of what queue does mid-turn | labeled, needs your yes |
| **[HANDS]** | a plan step only you can perform | copy-pasteable line + expected output |

## Words we use

| word | means | how you recognise it |
|---|---|---|
| **seat** | a role in the RUNBOOK (`oraculum`, `cartan`, `majkee`) | a `participant_N:` line; two windows can fill one seat — that is the trap |
| **endpoint** | one living session on this machine that a seat is bound to | a real window / pane / thread you could type into right now |
| **binding** | seat → endpoint, chosen by you, host-local, never committed | a small state file beside the bed (like `tunnel.state.json`) |
| **incarnation** | the running instance behind a session id — a resumed conversation can change it | same id, new process → rebind |
| **bed** | one session folder under `.dev/session/` | `RUNBOOK.md` + `STATUS.md` inside |
| **exchange** | one POINT → RETURN → VERDICT cycle | `_bus/NN.*` — the number is the exchange ID |
| **receipt** | the RETURN sitting at exactly the path the POINT named | `return_to:` in the POINT |
| **activation / doorbell** | telling an endpoint "a path is waiting" — not the message itself | today your paste; in bed 02, `codex queue` |
| **attention** | the tool giving up and calling you (no receipt, busy pane, unknown state) | never repaired silently |
| **surgical table** | `~/ia-sync` — where a tool's source lives before `deploy.sh` spreads it | this brick's home; not automatically every organ's |
| **L4** | the flag line recording the send-keys-as-message death | `.dev/session/flag.md` |
| **the browser** | `rb-open` — read + land + drain, by law never a delivery tool | `~/ia-sync/zsh/session/runbook.py` |

## nablarva-02-pipe-qualification · pad.1-baseline-carry (written before you sit it)

**What this sitting proves.** One number: how many deliberate actions *you* spend carrying one
POINT to Cartan today, by hand. Every later claim that the pipe "saves" anything is measured
against this. It was missed once; this time the count is a step with a fence, not a wish.

**Why it is a human step.** Nobody else can see your actions. Cartan sees only when a POINT
arrives and when its RETURN leaves; I see only files. The gap between those — locate, copy,
switch, paste, explain — is exactly the cost the seam exists to remove, and only you are there.

**Why a listener, and why it must be dumb.** You are on the phone; typing while carrying would
itself be a cost. A voice agent that only writes `id time device` lines is a stenographer, not a
judge. If it summarizes or "helps", the reading is contaminated. The rules in the PAD make it dumb
on purpose.

**Rehearsal vs real.** A rehearsal is allowed once, to check that the listener produces clean
lines — it never becomes a reading. Describing how the carry *would* go is not a measurement;
only the real carry counts. Phone vs PC is not a choice to make: it is a *field* you voice
(`phone` / `pc`) because switching windows costs differently on each — both are real conditions.

**What happens if Cartan pulls first.** It may open the bed on its own clock before you paste
anything, as it did in cycle 01. That is not a failed measurement — say "pull" and report the
three numbers in STEP 3. A near-zero carry is the most interesting result this sitting can give.

**Words new here.** `stenographer` — the listener's only role; `flush` — the word that makes
it print the log; `pull` — the receiver read the POINT before you delivered it.

## nablarva-02-pipe-qualification · pad.2-sitting-1 (written before you sit it)

**What this sitting proves.** Not delivery — only that a throwaway Codex window can be given its
*own* front door (a private socket), that we can look through that door and see exactly that one
window's state, and that opening the door disturbed nothing else. If all three hold, the next
sitting may try to put one message through the door. If any fails, we stop and think.

**Why a private server.** Your working sessions are attached to nothing; there is no shared
"daemon" to find. So the disposable target gets its own server, and the socket path *is* the
address — you choose it when you open the window. It cannot reach your working sessions because
they never connect to it. What it still shares with them is your Codex home (login, thread
database). That is why the sitting brackets the launch: before and after, I record the
control folder's listing and the login file's modification time — never its contents. If either
changes, the sitting stops, because "private" would have been a story, not a fact.

**Why each step is yours.** Opening a server and a window are launches — the law says the
human opens the table. `/status` is native and only you see it. The two gavels
(`open_approval`, `armed_approval: inspect`) are separate on purpose: opening a window is not
permission to read it, reading is not permission to send. You will say each in one line; I
transcribe it verbatim into STATUS; nothing is armed by a template.

**What "good" looks like at STEP 7.** The reader prints `STOP_IDENTITY_UNKNOWN`. That is the
*good* result: it read the window's state (idle, one thread, right workspace) and honestly
says it cannot prove which running instance that is. `BLOCKED` or "route unknown" means the
door did not work. Nothing here counts as native qualification — every line stays
`UNVERIFIED-native` until a real send is observed under its own approval.

**Words new here.** `bracket` — the same metadata check before and after a launch; `interlock` —
a public token I compute from the socket path and the UUID so the reader cannot connect by
accident; it is not a password and not permission; `STOP_IDENTITY_UNKNOWN` — read succeeded,
instance unproved (good); `open_approval` / `armed_approval` — your two one-line gavels.


## nablarva-X3-architecture-sitting · gavels.X4.2026-10-17.md

`what: background for the human gavel sitting. UNCANONICAL explanation, never decision evidence.`
`written by: myShell / Cartan, 2026-10-21, before G1 is answered; informed by a bounded`
`GPT-5.6-Terra source-reading consultation, with the central claims checked against the sources.`
`scope: G1 only for now; later units receive their context before their own answers.`

The physical folder is X3; the deck retains its historical X4 filename. Read the
[gavel deck](nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md) for questions and
answers, and the [sitting RUNBOOK](nablarva-X3-architecture-sitting/RUNBOOK.md) for ownership
and the route to approval. This section explains them; it does not replace either.

### STEP 1 — G1: what must be decided before we can draw the architecture?

**The practical question.** May Houston draft a useful architecture map while some product
choices remain open, or must you settle the language and the first release's size first?
That is why a small timing sentence has become a human decision.

**Where this came from.** July's design comparison brought together your file-room idea,
Oraculum's process-room idea, and a blind Codex proposal. It converged on substantial
architecture: one append-only journal owns room truth; participants receive their own
cursor-based projections; routing enforces boundaries; adapters own agent PTYs; tmux is
only an optional host/view; monitoring uses plain files. Cross-host operation was framed
around one central broker. These principles were subsequently locked as L3, with rejected
approaches recorded under L4. They are design commitments, not proof that all of this is
already implemented. See the [original comparison](../../raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md)
and [current locks](flag.md).

That comparison also kept decisions for you. In particular, Python versus C++ balances
delivery speed against your learning appetite; an agent cannot settle that personal trade-off
by declaring one technically preferable. The proposed first release is one machine, one
room, one human, two agents and one consultation. Confirming that cut determines what the
first release must actually deliver. Those remain docket items 2 and 6 in the
[pending-gavel list](flag.md#pending-gavel-majkee--the-docket-triadcomparison2026-07-31md).

The [architecture stub](../../docs/ARCHITECTURE.md) therefore points to the July comparison
as its proto-architecture and says the first real document comes after language and V1 cut
are settled. The later October L16.9 assigns a durable home for architecture across all
components: that same document. L16.10 asks for one home per fact and visible unknowns.
The [Houston project map](../../.germline/agents/houston/nablarva.md#1-the-map--roles-in-the-identity--real-homes-here-locked-l169)
explains the intended content: layers, dependency direction, shared grammars and ownership
between components, while local detail stays with each component.

**Why this is still a real question.** Naming the document's home does not explicitly repeal
its earlier timing condition. The [October 9 preparation](nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md)
preserved exactly this question for a ruling. L16.9 being newer is part of Oraculum's printed
reasoning for option b; recency alone is not evidence that you already approved b.

**What a draft could usefully explain now.** As an interpretation of the existing locks,
it could show how the room journal, routing, adapters, observation and human interface fit
together; where truth lives; which component owns which boundary; and where decisions
still constrain that picture. It can distinguish current components from planned ones.
This assembles the project's existing commitments into a readable map.

For example, the locked principle that tmux is not the regulated room protocol can be
explained without choosing the broker's implementation language. A map can also describe
the phone as a thin lens onto workstation sessions under L14 without promising that the
phone belongs in the first release. Those are different kinds of statement.

By contrast, declaring that the broker is a Python system service, that its journal has a
final NDJSON format, or that cross-host use ships in V1 would take positions on unresolved
language, lifecycle, storage or release-scope decisions. The draft must expose those
dependencies rather than hide decisions in apparently descriptive prose. The exact list
of dependent statements is itself work for the draft, not something G1 has already proved.

There is a current example of this distinction: L17 approves Python stdlib for the
Termbrana composition family and Rust/WASM for its observer. It does not settle the whole
broker's language. The [project contract](../../PROJECT.yaml) still explicitly leaves that
language TBD. A component's approved implementation cannot silently close docket 2.

**What each answer changes.** The authoritative wording and Oraculum's lean are in
[G1 of the deck](nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md#step-1--g1--precondition-may-the-first-doc-be-drafted-before-the-docket-closes).

| Answer | What becomes possible or must wait | What you are committing to | What remains open |
|---|---|---|---|
| a | Drafting waits; the sitting parks until docket 2 and 6 are settled. | Keep the earlier timing prerequisite. | Both product decisions, the architecture document, and X1 check 4. |
| b | Drafting may proceed with every dependent part marked `unknown: docket #N`. | Explicitly relax the timing prerequisite while preserving the unresolved choices. | Language, V1 cut, other docket items and approval of the actual architecture. |
| c | The sitting first takes your language and V1-cut decisions, then drafts on that firmer basis. | Broaden the sitting into a venue for those substantive product decisions. | Their actual values until you state them, unrelated docket items, and approval of the draft. |

Option a avoids drafting ahead of those choices, at the cost of waiting. Option b permits
a partial map, with the obligation to make its gaps and assumptions visible. Option c asks
you to spend attention on product choices now, before seeing that map. These are the
trade-offs already exposed by the deck, not new ranked recommendations. Its printed lean
is Oraculum's b.

**Change / lock / close / drain.** A G1 answer can settle the timing rule for this work.
Under b, the old stub sentence becomes history when promotion happens; it is not silently
rewritten by answering this question. Under c, language and cut need their own explicit
content from you: the letter c alone does not select a language or specify a release.

This removes one uncertainty about how to proceed. It does not clear the whole pending
docket or release work in unrelated beds. L16.12 keeps the distinction between a proposed
architecture and your GO creating a lock.

The [sitting sequence](nablarva-X3-architecture-sitting/RUNBOOK.md#sequence-under-the-gate-in-order)
still requires the remaining gavel answers, Houston's alternatives and your pick, drafts,
review, a mechanical witness, and your GO. Promotion is a separate row after that GO.
Promotion completes X1 check 4; the [X1 audit](nablarva-X1-architecture/RUNBOOK.md#checks-under-the-gate-in-order)
then follows as check 5. G1 therefore cannot by itself close the sitting, close X1, approve
the architecture body, authorize implementation, or authorize deployment.

**Why your answer matters.** Existing technical evidence can show the conflict and identify
possible dependencies. It cannot decide whether you prefer to clarify product choices
first or use a partial architecture map to help think about them. G1 puts that choice
back in your hands.


#### Current intent — tmux/PTY takes precedence

The [operator's G1 answer and correction](nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md#step-1--g1--precondition-may-the-first-doc-be-drafted-before-the-docket-closes)
are the authority for this sitting's intent. The X generation was introduced to cut away
stale design drift and work from the folded body of bricks. When narratives contradict,
the current tmux/PTY solution wins. Merely separating old and new accounts would miss that
instruction. The earlier July context above explains the timing conflict; it must not
become a route back through already-introduced intent or a requirement to rebuild the old
product picture.

The newly named [VIST brief](nablarva-X4-vist/raw/vist-01-principle-and-applications.md)
gives concrete architecture input for that direction. It describes a passive sensor,
Antensor, observing vendor CLI sessions in tmux; neutral VIST observations; a separate
controller making decisions; and a separate, authorized actuator handling the doorbell.
The intended benefit is to stop making Majkee watch every pane and carry every nudge by
hand. The sensor, decision and action responsibilities stay visible rather than merging
into one opaque automation.

The brief also keeps distinct evidence meanings: seeing a ready-looking prompt is an
observation, an actuator receipt describes its action, and explicit acceptance plus a
correlated return establish different parts of the exchange. That makes rendered terminal
observation useful without pretending it proves task completion or reproduces raw PTY
bytes. Optional transcript or hook evidence does not turn vendor cooperation into the
foundation of the solution.

This is a source of current intent, not a claim that Antensor is already implemented.
The brief marks names and passive direction as decided in conversation and much of the
pipeline, controller, event schema and deployment shape as proposed or needing verification.
The draft must preserve those marks. Any concrete contradiction with a standing lock
should be named and brought to the head for the required reconciliation, with Majkee's
explicit tmux/PTY precedence visible; it must not silently send the design back to the
superseded narrative. This explanation changes no flag entry or product implementation.


### STEP 2 — G2: how much space does each component need in the first map?

The [current wrapper](../../PROJECT-DESIGN.md) describes reusable bricks and a first useful
file-backed exchange between living agents. Read that alongside the
[VIST direction](nablarva-X4-vist/raw/vist-01-principle-and-applications.md) and the operator's
G1 correction above. This is the starting frame. The scope question should help make that
frame readable rather than restart the old design exercise.

The architecture document needs enough detail to explain relationships: how composition
prepares a prompt; how a living session is observed and identified; how a controller can
request a qualified action; where files and receipts preserve the exchange; and how the
operator sees work needing attention. Component-local implementations stay at their own
homes. The [documentation growth law](../architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md)
lets a component start as a line and grow when actual need earns more space.

The old deck's list needs two pieces of current context. First, L17 now explicitly places
composition within Termbrana, with its source family in ia-sync; the wrapper reflects this.
Composer is no longer simply an unlisted candidate from the October 17 snapshot. Covering
composition does not require inventing another independent product beside Termbrana.
Second, VIST/Antensor is now named current design input even though it is absent from that
snapshot. Its proposal status and open mechanics must remain visible in the map. See
[flag L17](flag.md) and the [Termbrana body](../../toolbox/termbrana/README.md).

Useful distinctions while reading the component names:

- Termbrana includes a Zellij observer and reusable composition; these have different source
  homes and evidence. The Zellij ceiling is rendered observations, not recovered raw PTY.
- Ovitmugen concerns views/layout and protection of living processes. Composition and
  Ovitmugen can be independently useful; discovery alone grants no delivery authority.
- VIST names observations; Antensor is the proposed passive sensor. Controller and actuator
  remain distinct responsibilities in its brief, not capabilities silently assigned to Ovitmugen.
- Muticula concerns coordination around shared checkout work. Termpanum is the observation
  laboratory. Stridulatrix names the broker; stridularium names the phone lens. Their names
  and source pointers do not establish that every intended feature is implemented.
- Instarmux and the wrapper's reposoma-tool entry have no substantive body in that wrapper.
  An honest empty/unknown entry does not create a build requirement.

The [registry](../../meshup/REGISTRY.md) lists design cross-sections, not a compulsory set of
products to rebuild. Sources should be used to find evidence for today's map.

The three printed choices vary the document's coverage and review burden. One line per
named component keeps the substance in the shared layer and ownership sections. Selected
sub-chapters give more room to explain specific interfaces but require guarding against
copying local detail. Restricting coverage to the printed subset makes a smaller map while
leaving omissions explicit. None of those formatting choices alone decides a new component's
permanent status, grants implementation authority or discards the current tmux/PTY direction.

G2 also asks explicitly about composer coverage. That answer needs today's L17 context;
the October 17 description of it cannot be treated as fresh evidence. The source question
is where composition appears in the map, with its existing Termbrana relationship preserved.
The deck's printed Oraculum lean remains a. The human answer belongs only in G2's report.


#### Termbrana itself — what the continuation still owes

`written by: myShell / Cartan, 2026-10-21, at Majkee's request for richer G2 context;`
`source-reading consultation: GPT-5.6-Terra; key claims checked against the cited files.`

The useful product promise is a surface where Majkee can prepare and inspect exchanges,
with or without an agent helping, alongside a way to return to meaningful terminal events.
The current route puts composition first: composer-01-parse, then the named Sublime/IDE
continuation. The older observer backlog is a separate lane; L17 does not make finishing
that lane a prerequisite for composition. This is the concrete small-brick reading of the
X-generation direction, rather than another attempt to design the whole animal before
anything becomes useful.

**What exists today.** The [Phase 0 source finding](composer-01-parse/evidence/phase0.exit.cartan.2026-10-21.md)
and [source-family README](/home/hruzam/ia-sync/zsh/termbrana/README.md) describe a narrowly
completed foundation: the parser preserves bytes, validates the approved framing and
returns safe metadata. It does not resolve referenced sources, assemble a prompt, render
an outgoing version, maintain a workspace/history, select a target or deliver anything.
Those missing functions are later layers, not failures of the parser's contract. Its
acceptance includes real office timing measurements, without qualifying other hosts or
future resolver/editor code. Source preservation/publication remains separate work.

The observer at [toolbox/termbrana](../../toolbox/termbrana/README.md) has a different
foundation: a Zellij host probe with a frozen M0 contract. The semantic core, review UI,
retained JSONL and replay are still future product work. Zellij supplies rendered pane
content, so that observer cannot promise original raw PTY bytes. The observer's own
milestones and benchmark stay with that lane.

**What the composition continuation owes the user.** The
[new Sublime brief](termbrana-X2-composer-sublime-ide/raw/termbrana-X3-sublime-ide.md)
records Sublime first and a server-side logic boundary. It distinguishes chat-decided
intent from proposed mechanisms and open choices. Read its examples with those marks;
the illustrative daemon, socket protocol and plugin code are not installed infrastructure.
The remaining product work falls into these useful pieces:

| Piece | What it would let Majkee do | Boundary still to establish |
|---|---|---|
| Source selection and preparation | Select common-program, germline, actual vendor-shape and SPECIAL material without an agent copying it by hand; readers may be phased, but these requirements remain in scope. | Read exact source contracts, preserve source/kind provenance, prepare before the opaque body, and keep selection separate from native activation. |
| Shared composition interface | Contribute text from human editing, pipes or an assistant through a reusable interface. | Define how parts are assembled, who writes which draft, and how concurrent edits are handled. An editor save is not a delivery request. |
| Sublime surface | Use syntax, completions, folds, inline checks, inspect/render panels and block controls. | Reuse the accepted parser; settle the declared block/pin layer without silently interpreting the opaque body as instructions. |
| Workspace, exact outgoing versions and history | See the prepared version, pending work, attempts and returns, and bring an old version back as a new draft. | Keep one history writer, preserve frozen renders, and distinguish editing history from delivery evidence. The proposed layout and daemon are design choices. |
| Attachments and status | Associate a block with a collaborator and see relevant observed state. | Keep revisable target bindings in workspace state rather than hardcoding pane identities into the document; VIST observations do not prove acceptance or completion. |
| Qualified output | Eventually carry a prepared exchange to the intended live CLI through the current tmux/PTY direction. | Establish checked target binding, operator authority, receipts and recovery at the carrier boundary. The parser or editor does not itself qualify delivery. |

These are pieces of the intended surface, not a claim that every piece is already released
for implementation. The brief proposes read-oriented editor conveniences first, then
inspection/preview, then linked history/status, with sending separately authorized. That
staging does not require rebuilding a large framework before the first useful convenience.

**The immediate handoff already has useful work.** The composer bed retains a
[reviewed preparation proposal](composer-01-parse/evidence/preparation.handoff.cartan.2026-10-21.md)
for caller-selected sources producing read-only, provenance-separated byte parts. It is
named composer-02-resolve in that proposal. The selected continuation destination can
carry this work forward without creating a second competing plan. However, its exact
controller-source contract still depends on Flight's checked G06 U3 result and Majkee's
format/stamp/pin-ownership disposition. The dependency is specific; it does not mean waiting
for every unrelated audit unit. Its scope, deferral and performance proposals are not a
blanket launch approval, and its G1/G2/G3 labels belong to that composer proposal, not this
architecture deck.

The named termbrana-X2-composer-sublime-ide folder presently contains only the
Sublime design brief, with no RUNBOOK or STATUS. Thus the continuation is owed a bounded
execution handoff connecting the accepted parser, surviving preparation work and the
chosen first editor slice. That is task shaping from existing intent, not a request to
repeat the product-intent discussion.

**What stays Termbrana's own responsibility.** L17 keeps composition useful independently
of Ovitmugen, a RUNBOOK bed, tmux, an editor or an interactive shell. Sublime is one client;
other editors and assistant calls can be edges. Ovitmugen retains its view/layout and
protected process-lifetime responsibilities. In the VIST brief, Antensor observes, the
controller decides and the actuator acts. A common mechanism needs a narrow demonstrated
integration edge and an owner, rather than merging these responsibilities into Termbrana.
See [L17](flag.md) and the [composition direction](../../toolbox/termbrana/README.md#composition-and-explicit-input-direction).

If the observer lane continues, it owes its own usable review/navigation product:
blocks, search, bookmarks, copy, retained history/replay, visible provenance and recovery
from pane closure. Before M2 adapter code, its M0 facts must be rechecked; its benchmark
requires faster retrieval with no worse success than native Zellij. Those obligations
are described in the [observer ledger](../../toolbox/termbrana/DECISIONS.md) and
[product definition](../../toolbox/termbrana/research/termbrana.project-definition.md).
They do not certify the composition lane or hold it hostage.

**What the whole-animal architecture owes Termbrana now.** Under G2's thin-map depth,
identify Termbrana's observer and composition family, their actual source homes and
independence, then explain only their crossings with observation, target binding, history
and delivery. Point at the living product sources for detail. That is enough to preserve
Termbrana's place while the smaller bricks advance; the architecture draft need not freeze
every editor feature or claim the product is finished.


#### Termbrana route names — operator clarification, 2026-10-21

The [G2 report](nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md)
retains Majkee's words, including the superseded folder name and the later correction.
For current navigation the route is:

1. composer-01-parse — the pilot and its retained acceptance/preparation evidence.
2. termbrana-X1-composer-sourcing — the intended next part, properly under Termbrana.
3. termbrana-X2-composer-sublime-ide — the first editor target is Sublime Text; the
   underlying composition design remains application-neutral.

Only the wrapping folders were renamed. The raw Sublime brief keeps its existing filename
and intended content; earlier mentions of composer-02-resolve in the retained preparation
proposal identify that proposal rather than a competing new session. The links in this
GLOSS now follow the renamed Sublime folder. The sourcing folder currently has an empty
raw/; the Sublime folder contains its design brief. These names establish the intended
sequence without claiming either continuation already has a RUNBOOK, STATUS or build release.


#### New architect evidence — what it answers for this gavel

`written by: myShell / Cartan, 2026-10-21; updated after reading the current architect report,`
`generation-X operator direction, checked handoff and composer STATUS.`

The [Houston report](composer-01-parse/evidence/audit.houston.termbrana-shape.2026-10-21.md)
and [current handoff](composer-01-parse/evidence/handoff.termbrana-generation-x.2026-10-21.md)
answer the important scope and evidence questions for G2. This is a bounded native
Houston audit-as-probe, not the proposed whole-animal sitting. It checks the current
implementation shape and saved evidence; it does not claim fresh functional tests,
resolve the open shared layer, or make a new product lock.

The report gives the architecture owner concrete evidence for a thin Termbrana entry:
the observer and composition family have distinct homes and acceptance boundaries;
the existing parser validates content; sourcing is planned; Ovitmugen keeps its
view/layout and protected process-lifetime responsibilities. It also supplies proposed
L17 architecture wording and a wrapper-mechanics diff. The later handoff corrects the
audit's loose phrase about composition preparing and validating: actual preparation is
future work, so those verbs must not be merged into one present-tense capability.

The [recorded operator direction](composer-01-parse/evidence/direction.majkee.termbrana-generation-x.2026-10-21.md)
also corrects an earlier framing in this explanation: common programs, germline, vendor
shapes and SPECIAL, including germline/pipes, are original first-class sourcing
requirements. Vendor readers and the wider SPECIAL surface cannot be silently treated
as optional extras after a controller/function plus whole-file example. Implementation
may be split into bounded sourcing gates, with the remaining coverage explicit.

Consequently, the reviewed two-reader RUNBOOK is useful preparation for a first
checkpoint, but its gate is superseded as a proposed complete X1 exit. Merely renaming
its destination does not make the gate complete. The continuation still needs actual
source-shape, reader, owner, selected-content/provenance, failure and acceptance coverage;
then a reconciled full gate or explicit bounded sourcing gates. This is a concrete
planning debt within the stated product direction, not another product-intent debate.

For this architecture G2, the evidence answers who Termbrana is and where its parts
belong. It supports the already-selected thin map with pointers and honest planned
capabilities. A complete resolver specification or an editor implementation is not
needed to describe those relationships. The sourcing proposal's own G1/G2/G3 labels
remain separate from this architecture deck's gavels.

The remaining caveats have specific homes and consequences:

- The source-contract owner evidence and consequential decisions remain prerequisites
  for controller-profile and stamp/pin ownership. At this reading, G06 RESULT.U3.md is
  still absent. The current handoff keeps that dependency and the relevant decisions
  for the other consumed source shapes.
- The original live-role/liveness/target-binding exit is not fulfilled by preparing
  source text. Any narrower next gate must identify that deferral and its future
  owner/gate. Shared preparation/write/target-binding ownership, home and API remain
  open; rendered observations and metadata confer no sending authority.
- The Sublime brief's existing-loader assumption is unproved. Body-block semantics,
  daemon/socket, history writer and live attachments remain design work. Phase0 keeps
  body bytes opaque. App-neutral design and Sublime as the first target remain the
  stated direction.
- Accepted source and evidence need a preservation/publication disposition and real
  commit-pinned qualification links before the retained bed can be pruned. Historical
  package29 remains immutable; a passing historical package is not current staging
  authorization.
- The architecture router's old X4 target, the observer README's obsolete next-pad
  instruction and related qualification pointers are bounded documentation debts.
  The audit proposes corrections; it has not applied them or taken another head's pen.

The [head's check receipt](composer-01-parse/evidence/head.audit-checks.termbrana.2026-10-21.json)
records the exact inspected source identities and limits. My fresh read also found all
ten composition files matching those recorded identities. This strengthens the current
shape evidence without expanding parser acceptance to sourcing, editor or carrier work.


#### Operator dispositions and brainstorm — sourcing manager, editor and history

`written by: myShell / Cartan, 2026-10-21; operator words are retained verbatim in`
`G2's report. The brainstorm is future product input, not a settled UI or storage contract.`

**Ownership and readiness.** Full X1 source coverage and the bounded execution plan belong
with the application team. Consequential hard choices return to Majkee, consulting Houston.
The source-contract wait lasts until the relevant germline realization plan and fixed
sources to load from are ready; Majkee can then inspect what can be sent. Checked G06 U3
is one named prerequisite already in the handoff, not a substitute for readiness of the
other actual consumed source shapes. This architecture sitting need not solve that work.

**Small brainstorm note — from Majkee:**

> i should have manager UI witch allows me check and load what should be sourced

Possible reading for the application team, inferred by myShell: a visible source manager
could list the available source categories, show the exact selected source and its
provenance, preview the parts to be loaded, and load the chosen parts into a draft for
inspection. Prepared text, source selection and actual native activation remain distinct.
The point is that Majkee can inspect and compose without needing an agent to perform
routine copying. The concrete controls and source adapters are still to be designed.

**What the shared-interface question refers to.** The phrase previously covered several
connections, which should be named separately rather than implying one common framework:

| connection | what crosses it | standing boundary / remaining work |
|---|---|---|
| Composition/sourcing ↔ Sublime or another editor | selections, prepared parts, checks and render previews | Keep the composition contract app neutral; the editor consumes it. Exact APIs and writer policy remain application-team work. |
| Composition ↔ Ovitmugen or another discovery client | optional session metadata and attachment candidates | Composition remains independently useful; Ovitmugen retains view/layout and protected process lifetime. Discovery is not delivery authority. |
| Exchange workspace ↔ telemetry/controller/actuator | observed state, delivery requests and action receipts | VIST proposes separate observation, decision and action responsibilities. Concrete ownership, target binding, transport and receipt contracts remain open. |

The IDE boundary and the Ovitmugen boundary may use some common mechanism if actual
consumers justify it; no decision here requires a single daemon or a shared module.

**Editor usability and the Laravel requirement.** Majkee wants the whole prompt-manager
experience in a comfortable visible UI. A design usable only through hidden/headless
commands and key bindings would not satisfy that goal. The
[current Sublime brief](termbrana-X2-composer-sublime-ide/raw/termbrana-X3-sublime-ide.md)
already proposes panels, selection lists, annotations and inline pseudo-buttons, but those
are untested design input rather than proof of comfort or API feasibility. A small real
workflow should expose Sublime's limits before escalating into a larger integration.
Sublime remains the first target because Majkee already has the Laravel support he needs
there. If the required interaction proves awkward, assess Lite XL against both the prompt
manager workflow and Laravel development needs; its suitable community support is unknown
in this sitting. No alternate editor is selected by this note.

**Operational history — future direction.** Majkee proposes JSONL for the prompt/exchange
flow, with two possible homes: a project-local .nablarva directory, analogous in placement
to .codex, or a centralized ~/.nablarva/<path-to-history>/ tree. The future UI should load
and show relationships to the participating agents' session-memory JSONL. Own exchange
records and references to vendor session history can provide that glue; the vendor formats,
correlation scheme, permissions, home and writer contract have not been qualified or chosen.
Similarity to vendor JSONL does not establish a compatible schema. This is a location and
relationship brainstorm, not an instruction to copy or rewrite vendor session databases.

**The earlier preservation caveat means something else.** It concerns preserving the
accepted implementation, test evidence and actual commit-pinned pointers before pilot-bed
pruning. Operational prompt history records future use of the product. Both are useful,
but choosing a history directory does not by itself preserve the pilot's accepted evidence.


#### Ovitmugen–Termbrana: the direction is already settled

The [Phase0 decision](composer-01-parse/evidence/decision.majkee.phase0-go.2026-10-20.md)
explicitly selects layering B, and [flag L17](flag.md) carries the durable boundary.
Majkee has brought that result into this sitting's G2 context. It is not another A/B
choice waiting for this architecture sitting.

Termbrana owns composition and stays independently useful without Ovitmugen, a session
bed or editor. Ovitmugen retains view/layout and protected process/session-lifetime
ownership. Optional use of Ovitmugen discovery data is compatible with that independence.
Delivery still requires checked target binding and explicit authority.

Thus the Ovitmugen–Termbrana caveat concerns only the actual shared mechanisms and their
exact owner, code home and API, together with carrier qualification. A common framework
or carrier has not been approved for implementation. The separate editor-facing interface
can consume composition without inheriting ownership of Ovitmugen's session lifetime.
The architecture draft should carry this settled direction once and mark only its concrete
unresolved parts open; it should not rerun the layering choice.


### STEP 3 — G3: put the shared key meanings in their durable home

`written by: myShell / Cartan, 2026-10-21, before the G3 answer.`

The branches so far are context feeding one sitting. The PAD holds the operator's exact
answers, its GAVELS sink supplies the sitting prompt, this GLOSS explains why, and each
owning STATUS retains its own doing-state. Historical names and raw briefs remain attributed
inputs. Returning to the next numbered gavel brings the extra threads back to one table;
it does not promote every brainstorm into an additional decision.

**What is being moved.** [KEYS CODE](../../PROJECT-DESIGN.md#keys-code) is the shared
meaning of keys in the organs' own terminal views. For example, Enter acts on the selected
item, q/Esc goes back by closing a view, and x x removes in two presses. Each organ owns
its code and extra bindings. This chapter fixes common meanings rather than creating a
second key registry. It also reserves the tmux prefixes and keys needed by a running agent.
G3 relocates this already-accepted material; it does not choose a new Sublime shortcut
scheme, redefine input delivery or repair existing implementation deviations.

**Why a move is proposed.** Under L16.9, shared cross-organ grammars belong in the whole-
animal architecture document, while PROJECT-DESIGN stays a thin index. The older
[Houston audit J1](nablarva-X1-architecture/raw/houston-audit.2026-10-07.md)
identified the full grammar in the wrapper as declared interim content. The
[documentation migration record](../architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md)
and [X1 check 4](nablarva-X1-architecture/RUNBOOK.md) explicitly plan this move.

There is a live consumer: the Ovitmugen basement's
[RUNBOOK](ovitmugen-01-basement/RUNBOOK.md), [STATUS](ovitmugen-01-basement/STATUS.md)
and [pulse route](pulse.md) cite PROJECT-DESIGN.md section KEYS CODE. A safe migration
therefore leaves that same heading in place with one line and a pointer to the new home.
Following the existing reference must still reach the grammar.

The acceptance record also needs to survive pruning. It currently points into the
[basement D3 source](ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md).
A checked existing commit contains that acceptance:
`nablarva@c630f0e8b1490e34458a52988342d679b24f2f5b:.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md`.
The proposed draft can cite such an immutable source while keeping the September 29
acceptance date. This is provenance preservation, not a fresh approval of the keys.

**What the timing choices mean.**

| choice | consequence for this sitting | consequence after promotion |
|---|---|---|
| a | Include the accepted grammar and pinned acceptance in the architecture draft; prepare a thinning diff retaining the old heading and pointer. | One published grammar home, with the live Ovitmugen reference still usable; J1's grammar portion can close. |
| b | Keep the grammar at its current wrapper home, have the draft point there, and leave this migration open. | Existing references keep their current target; the shared grammar's move and that part of J1 remain owed. |
| c | Plan a published copy in architecture while retaining the full wrapper copy until Ovitmugen closes. | Two active copies during the interval, contrary to L16.10's one-home-per-fact rule. The deck lists this for completeness. |

Under a, drafting and preparing the diff happen in the sitting's raw work. The currently
published wrapper remains the working home until the later GO and promotion procedure.
A temporary draft is not another published authority. Under c, the proposal deliberately
retains two published bodies after promotion; that is the meaningful difference.

The printed Oraculum lean is a: it follows X1 check 4 and protects the live reference with
the retained heading. G3's answer belongs in the PAD, and the current product files are not
moved by merely answering the question. Later review and the mechanical witness check the
diff and reference preservation under the sitting's existing sequence.


#### G3 expanded context — keyboard design stays open for Houston

Majkee's concern is larger than relocation: too many per-tool key vocabularies, a whole-
animal command/key view feeding HELP.md, generic patterns compatible with native hosts,
fast direct access, and command discovery attached to the active toolbox. He wants this
as an early open design topic in the architecture sitting. Gaming conventions and
ergonomics are explicit hypotheses to investigate, not a selected keymap.

Majkee authorized folding the larger conclusion and handoff directly into this sitting's
raw/. The completed [keyboard research brief](nablarva-X3-architecture-sitting/raw/brief.keys-command-discovery.2026-10-21.md)
contains the local source audit, primary host/accessibility/HCI sources, falsifiable
hypotheses and Oraculum's attributed critique. The two research seats used Terra/high;
Oraculum used Astra/high. No actual host collision capture or user trial was run.

The central distinction is between a catalogue of what exists and an attached palette
showing what is available here and what it will affect. Owner-derived help/discovery is
a candidate; missing action meaning or availability may need explicit owned metadata.
The interface is part of the toolbox body even if a separate pane/window presents it.
Opening that palette changes focus, so its intended toolbox target needs to remain clear.
No common framework or central dispatcher is selected by the research.

The existing G3 relocation answer is still unconfirmed. The larger design request is
captured as context; it must not be silently converted into a, b or c. Relocation of the
current accepted grammar and a future keyboard-normalization design remain distinct
choices. The head/Houston can carry the brief into the sitting as an early open topic;
this research does not change RUNBOOK, STATUS, flag or deployed bindings.


### STEP 4 — G4: a default home for enduring component documentation

`written by: myShell / Cartan, 2026-10-21, before the G4 answer.`

The architecture's thin organ list needs to point somewhere durable for each component's
contract, key files, decisions and design detail. A task bed holds work while that task is
open; its raw files are not automatically the component's lasting documentation home.
G4 asks whether to settle a default location for components that have no established home.

The [Houston addendum](../../.germline/agents/houston/nablarva.md) currently labels the
fallback rule proposed, not locked. The
[documentation record](../architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md)
proposes: retain an existing home; otherwise start at docs/organs/<organ>.md and grow to
docs/organs/<organ>/ when a larger body is needed. The project wrapper points to that home.
This follows the small-file-first growth approach rather than creating a full tree for
every named component immediately.

There is already one concrete example: [stridularium's working wrapper](../../docs/organs/stridularium.md)
was moved there under Majkee's October 10 ruling, recorded in commit 22cfa26 and referenced
by flag L14 D5. That settles its own location; it does not by itself prove the general
fallback rule has already been gaveled for all other organs. Choosing a makes that
prospective generalization explicit.

**What the rule controls.** It selects where enduring component documentation goes.
It does not place every source tree under docs/organs or declare all text in that home
accepted architecture. Stridularium's body still identifies itself as a working draft.
Existing component homes remain: Termbrana keeps toolbox/termbrana, while its composition
source/interface remains at ia-sync/zsh/termbrana under L17. A numbered Termbrana session
bed remains task work, not a replacement source or product home.

| answer | what happens now | what remains for the sitting |
|---|---|---|
| a | Majkee gives GO on the default documentation rule; the named head records it in flag. | Drafts can use established homes plus the settled fallback. Organ contents, implementation and ownership still need their actual evidence/decisions. |
| b | Houston drafts the proposed lock text in raw/lock-proposals.md; the rule stays inferred in the architecture draft. | Majkee decides the proposed lock at the later GO. |
| c | The general rule remains unlocked. | The draft lists unresolved homes as unknown except the existing Termbrana and stridularium cases. |

G4 a is a standing documentation-rule decision, not merely permission to prepare a
relocation diff. The driver records the answer; Oraculum holds the flag pen under the
deck's rule. A recorded GO and the later observation of an appended flag entry must remain
distinguishable. No directories or component documents are automatically created here.

The deck's printed Oraculum lean is a, citing the existing stridularium practice. The
question is whether to adopt that lightweight fallback generally now, propose it until
final GO, or retain unknown locations for the moment.

### STEP 4 — expanded context: component folders and future consumers

`written by: myShell / Cartan, 2026-10-21; G4 still unanswered; consultation requested by Majkee.`

Majkee's corrected publication input is the root
[Symmetry documentation record](../architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md).
Its header says final; the similar file under process/ is an earlier un-gaveled draft.
L16 cites the root record. The one-home/thin-growth discipline is settled; the general
component directory fallback remains proposed.

The larger [component documentation and Nablarva Boost brief](nablarva-X3-architecture-sitting/raw/brief.component-docs-and-nablarva-boost.2026-10-21.md)
folds two Terra readers, an independent challenger and Astra Oraculum. It distinguishes
component role, code home, documentation body, entry shape, machine metadata and consumer
interface. A choice on one need not silently settle the others.

My proposed direction is a useful entry at each existing home and consideration of
README.md in a component folder for new bodies, with chapters/res added when needed.
That folder-first convention deserves an explicit reconciliation with the current
growth law. Keeping future selective loading in mind is useful now; a metadata schema
needs a consumer with defined questions and ownership. MCP discovery additionally needs
an implemented resource interface; frontmatter alone does not supply one.

The choice can therefore be smaller than a complete documentation framework: decide the
entry/home convention while leaving taxonomy and future adapters open. Locking a schema
or public identity later would constrain consumers more deeply than choosing a readable
entry today. The brief records those consequences and an unrun reader comparison for
Houston. This explanation supplies no G4 answer or new lock.

### STEP 4 — operator acceptance and the reader-design space

`written by: myShell / Cartan, 2026-10-21, after Majkee's G4 ruling.`

Majkee has now accepted the team's result as GAVELED. His full words are in report 4;
the approved sink points there as own. The preceding unanswered/pre-answer explanations
are historical context. His acceptance does not need another confirmation here.

His follow-up question identifies a separate design need: README and optional chapters
describe where content lives, not how a helper discovers, reads and searches it. Our
particular folder convention was an adaptation for Nablarva, not a Laravel Boost reader
contract. Astrobley's consultation and the implementation research are folded into the
[floating Nablarva Boost reader concept](nablarva-X3-architecture-sitting/raw/brief.nablarva-boost-reader-concept.2026-10-21.md).

The concept keeps one owned Markdown corpus readable directly and accessible through a
possible helper. It proposes explicit navigation and bounded discover/read/search, with
MCP as a possible later interface. Which navigation surface, corpus, metadata and adapter
to implement remains open. This provides a design topic for the architecture sitting
without requiring the documentation-location ruling to settle that mechanism too.

### STEP 4 — clarification: frontmatter has a named mechanical reader

`written by: myShell / Cartan, 2026-10-21; follow-up consultation with Astrobley.`

Majkee clarified that a hardcoded sourcing engine under his keys must navigate sources
and provide pins to Termbrana or an IDE. That is a third consumer alongside the human
and file-reading agent. Frontmatter now has an explicit intended consumer; it deserves
a concrete design proposal rather than indefinite deferral until one appears.

The [reader concept](nablarva-X3-architecture-sitting/raw/brief.nablarva-boost-reader-concept.2026-10-21.md#third-consumer-deterministic-sourcing-under-operator-keys)
now includes Astrobley's candidate header, typed navigation, source adapters and an
acquisition sequence. GUIDE and controller/function sources already demonstrate entry
metadata and declared members, though their formats differ. The engine can preserve
those differences while returning selected original content and comparable receipts.

A declared controller stamp checks a binding. A derived content digest identifies the
bytes actually acquired; a commit alone cannot identify later worktree edits. The
proposal keeps these distinctions visible for both prepared grounding and fresh collection.
It also separates the common source engine from a light command client or richer IDE UI.
The G4 ruling remains recorded; the schema and implementation are still open design.

### STEP 5 — G5: where architectural decision records belong

`written by: myShell / Cartan, 2026-10-21, before the G5 answer.`

An ADR is an architectural decision record: a place for the context, choice and
consequences of a technical decision. The flag remains the authority for Majkee's locks;
an ADR can explain a technical choice and cite its authorizing lock without copying the
flag into another ledger. Termbrana already has that local DECISIONS.md pattern.

The current whole-animal decisions directory has only a README promise. That older stub
says gaveled items will land there, while the later documentation record says the ADR
series remains unbuilt until a technical decision earns it. PROJECT.yaml still points
decisions to flag. G5 asks how the architecture draft should resolve that promise.

Here, unbuilt means not starting a new ADR series; the directory and README stub already
exist. Option a retains the stub and describes the current flag-plus-component-ledger
arrangement, allowing a later justified ADR. Option b begins the series with an adoption
record for the architecture document. Option c proposes retiring the stub through the
later reviewed change, which requires Majkee's GO. The printed Oraculum lean is a under
K8/L16.7: no measured failure of the existing arrangement was cited.

This question concerns decision records, not the frontmatter/navigation contract of the
open sourcing-engine design. An ADR choice does not by itself implement that reader or
require a separate record for every keypress, source acquisition or prompt.

### STEP 5 — expanded context: who receives the reasons

`written by: myShell / Cartan, 2026-10-21, G5 context consultation; answer still pending.`

An ADR preserves why a significant choice won and what could make reconsidering it
sensible. A routine implementer needs applicable constraints and prerequisites; someone
changing that boundary needs the alternatives and assumptions too. A verifier needs
the scope and evidence obligations. Those needs follow the assignment, not a permanent
agent identity. The same seat may need different context on its next task.

The [ADR task-context briefing](nablarva-X3-architecture-sitting/raw/brief.adr-task-context.2026-10-21.md)
folds Oraculum, Astrobley and the primary-source reader/researcher. It proposes linking
each surviving decision from its owning contract/component, selecting relevant references
when preparing the task, and checking replacement/evidence links during review and closure.
This gives records a route into work instead of relying on a future agent to search all history.

The intended Termbrana source engine can acquire declared decision context with reasons
for selection and source pins. Frontmatter/descriptors can express those relationships;
they cannot prove the task's full architectural impact. Required context must remain
visible if it cannot fit the budget. MCP can expose the same acquisition; VIST supplies
separately attributed observations, not proof that a decision was understood.

Termbrana already has ADRs in its local ledger, including partial supersession. The
latest ADR is therefore not automatically the only relevant one. G5 concerns an additional
root series and the old stub's promise; retaining rationale does not depend on starting
that series. The triad also identifies the stub's broad promotion wording as something
to reconcile explicitly. This explanation and the proposed process do not select a G5 option.

### STEP 5 — survival of the preparation procedure

`written by: myShell / Cartan, 2026-10-21; answer to Majkee's placement question.`

A CONTROLLER-indexed function is a suitable candidate home for the reusable agent-facing
preparation procedure. The reader's deterministic contract/code belongs to its application
owner; ADRs and applicability facts stay in the projects that own them. Those homes
should point to one another rather than duplicate their rules and records.

At present the procedure is preserved as linked design input, not as a promoted or
installed germline function. The [brief's survival section](nablarva-X3-architecture-sitting/raw/brief.adr-task-context.2026-10-21.md#where-the-reader-procedure-survives)
makes that outstanding promotion obligation explicit. Before bed pruning, the head must
route accepted process material through the appropriate germline/source-contract gates
and preserve resolvable durable pointers. G5 remains unanswered; nothing here freezes
the future program name or global program shape.

### STEP 5 — accepted direction and when reading happens

`written by: myShell / Cartan, 2026-10-21, after Majkee's own/amended G5 answer.`

Majkee accepted the team observation and controller possibility for selected agents in
the process chain, then requested a fixed reading schedule. His complete message is
recorded verbatim in G5 report 5 and folded into the approved sitting sink. Earlier
unanswered notes are historical. Root-stub correction versus retirement was not selected.

The [reading schedule](nablarva-X3-architecture-sitting/raw/brief.adr-task-context.2026-10-21.md#subsequent-operator-disposition-and-reading-schedule)
puts planner grounding before RUNBOOK authorship, context preparation before each
assignment, and recipient reading/checking at entry. The builder reads relevant mechanism
and process architecture; the planner additionally checks wider project alignment and
gate ownership. The verifier reads the actual artifacts and acceptance independently.
Houston receives a bounded architectural question when required, without taking lifecycle.

RUNBOOK carries stable assignments and shared rules; STATUS carries current position
and holds. Unchanged pinned context can be reused during ordinary work. Resume, new scope,
changed governing material or a discovered conflict refreshes the affected selection.
The controller can prepare a package, but each receiving agent still checks its applicable
instructions and task context. The matrix is now linked design input for the sitting;
concrete reader fields and program installation remain separate qualification work.

### STEP 5 — explicit gavel on the reading schedule

`written by: myShell / Cartan; operator follow-up: "gaveled." / "continue."`

The role/timing schedule is now explicitly gaveled for the sitting. Those exact words
were appended to G5 report 5 and the handoff identifies the matrix as accepted. Its
promotion route is still work to perform; an accepted procedure is not evidence of an
installed controller or source engine.

### STEP 6 — G6: calendar freshness versus task preparation

`written by: myShell / Cartan, before the G6 answer.`

G5 settled who prepares and reads task context, with refresh when work or sources change.
G6 asks a separate question: whether the architecture document also gets an age-based
review interval and possibly a scheduled reminder.

A checked date says when the content was last checked. A half-life interval says when
age should trigger review attention; it does not revoke a decision or prove it wrong.
The existing card convention uses half_life_days as the machine-readable interval.
Applying that convention to the architecture body would be a new use, not evidence that
an architecture reminder is already wired.

Option a uses the checked stamp and revisits calendar machinery when justified. Option b
also declares the interval but wires no reminder. Option c adds the interval and a cron
nudge now as an explicit exception to L16.7. The printed Oraculum lean is a: the real
architecture body has not yet existed long enough to demonstrate drift. The process
record's proposed cadence threshold remains a proposal, not an already locked trigger.

### STEP 6 — operator answer

`written by: myShell / Cartan; operator: "a- gaveled."`

G6 a is recorded and folded into the sitting sink: the architecture draft carries the
checked stamp, without adding a half-life interval or cron reminder now. The age-based
rhythm remains a later evidence-based question. G5's accepted task-entry and affected-source
refresh procedure remains distinct from that calendar question.

### STEP 7 — G7: advice on open choices versus deciding them

`written by: myShell / Cartan, before the G7 answer.`

The sitting will encounter open choices such as broker lifetime, storage and scope.
G7 asks whether Houston can offer recommendations about them or should only map what
depends on each answer. It does not decide any of those questions itself.

Option a permits only open questions and their dependencies. Option b permits advice in
raw/lock-proposals.md, marked inferred: houston and supported by its driving constraint;
the architecture body must not present those leans as adopted choices. Docket 2, the v1
language choice, remains excluded because the live docket reserves weighing it to Majkee.
Option c also permits advice there, conflicting with that wording. The printed lean is b.

The operator still gavels; the head carries proposed locks to the docket; Houston does
not write flag. Existing answers—including G1's tmux/PTY precedence—continue to bind.
A generic old UI-versus-terminal question does not reopen that accepted direction.

### STEP 7 — operator answer with flexibility

`written by: myShell / Cartan; complete operator wording is in G7 report 7.`

Majkee gaveled b and added that the process must allow ad hoc shifts beyond a boundary,
because a perfectly normalized but overly tight cage has caused problems. The full
qualification is preserved in the report and sitting sink; the handoff explicitly
requires reading it with b. Branch: RESHAPED.

My interpretation is to use the boundary as the working default while allowing useful
out-of-frame observations and reasoned departures to be articulated. A template is not
a reason to suppress an important insight. Name the departure and its consequences;
where an actual lock or authority change is involved, Majkee still holds that decision.
This does not require a new permission round-trip for every ordinary reasoning choice.

### STEP 8 — G8: learning a sitting card from the sitting

`written by: myShell / Cartan, before the G8 answer.`

Houston's sitting card is currently a short named stub. Its own text says the full
card is written at the first real sitting. G8 asks when to capture that reusable method.
The product here would be a draft in this bed, not an edit to the installed card.

Option a drafts it from the sitting's actual work and sends it to germline-01 for
acceptance after GO. Option b keeps lessons in arc.md and leaves full authorship to
the forge later. Option c drafts it through a second explicit Houston invocation after
the review rows, allowing those findings to inform the card. The printed lean is a.
The forge still owns acceptance, and the head carries the artifact. Project-specific
exploration does not automatically become a universal card rule.

### STEP 8 — operator answer

`written by: myShell / Cartan; operator: "a gaveled"`

G8 a is recorded and folded: Houston drafts card.sitting.draft.md in this sitting's
raw/ from the work actually done; it goes to the germline-01 forge for acceptance after
GO. This authorizes the sitting's draft, not direct installation of the global card.

### STEP 9 — G9: evidence before the sitting versus audit after promotion

`written by: myShell / Cartan, before the G9 answer.`

The sitting card requires a fresh audit unless equivalent current whole-animal evidence
is cited. The October 7 audit exists and examined the earlier wrapper/keeper topology.
Its structural findings include the missing whole-animal architecture body, so it is
useful background for this sitting. Age alone does not determine whether it remains
equivalent; the intervening changes matter.

Option a reuses that evidence with a stated, re-read delta at the start of arc.md. The
deck names the Houston fold/install, wrapper/stridularium moves and L8′. Current inspection
also shows L17's composition boundary and uncommitted changes in flag, PROJECT-DESIGN
and Termbrana's README. A commit log alone omits these. The current generation-X/source
work and this deck's accepted directions must be considered in the actual delta review.
This inspection identifies changed surfaces; it is not itself a new whole-animal audit.

Option b requests a fresh Houston audit before the sitting. Option c relies only on
X1 check 5 after the architecture document, which does not supply the required earlier
evidence unless a's equivalence citation is also made. The printed lean is a, conditional
on arc.md stating the delta and Houston surfacing any material difference for Majkee.

The audit itself leaves useful/overreaching/missing classification to Majkee. A later
Oraculum prompt calls it USEFUL, but that wording alone is not a recovered operator
classification receipt. That uncertainty remains explicit rather than silently resolved.

### STEP 9 — operator answer and completed deck

`written by: myShell / Cartan; operator answer is preserved verbatim in G9 report 9.`

Majkee gaveled G9 a and requested a to-oraculum handoff prompt. All nine answers are
now present in the approved sitting sink, and the deck's verdict map is complete.
G1/G2/G4/G5/G7 retain their amended meanings; a bare sequence of letters is insufficient.

The head resumes from the actual X3 bed, reads the operator reports and linked briefs,
and carries the accepted reading/controller procedure through the appropriate promotion
path. Houston's arc begins with the explicit audit delta, including current working-tree
changes. A material difference is surfaced rather than silently declaring old evidence
equivalent. The head retains STATUS and lifecycle; Houston's next main-session sitting
still presents the arc and alternatives before drafting. No STATUS or RUNBOOK was edited
by the driver, and completing the deck does not mark the architecture gate complete.
