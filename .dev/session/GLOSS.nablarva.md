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
