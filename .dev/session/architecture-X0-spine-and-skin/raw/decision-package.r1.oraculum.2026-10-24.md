# Decision package r1 — architecture-X0-spine-and-skin

`author: oraculum(arch-X0) · 2026-10-24 · for majkee · the return the Socratic brief asked for (raw/brief.socratic.myshell.2026-10-24.md, "After Majkee finishes collection, return …") · DRAFT until majkee answers the deck · nothing here is a lock; `locked:` tags reach only to the cited lock's text · sources: raw/inventory.what-exists.explore · raw/field.body-construction.r1 · raw/consult.d1-observation-record.houston · raw/answers.majkee.feed · raw/answers.majkee.organs · docs/ARCHITECTURE.md (cite L21 over §2.5) · flag.md`

## 1. The concrete problem and the decision question

**Problem.** nabLarva has a map (docs/ARCHITECTURE.md), law (flag L1–L23) and three bricks that converged on one layering without coordination (composer = service · ovitmugen = view + gates · HELLO r1 = substrate + living tissue; said: field §3; Houston: no break). It has **no construction**: no spine running observe → record → view (inventory: observe = one experimental script, record = nothing, view = runs), no shared layer with an owner, no address registry, no config rule. The workflow majkee wants — **HELLO**: "read this file and give me the message back within the same bash you are working on", agent ↔ agent, cross-vendor (said: majkee §4, repeated §5) — cannot be built, observed or qualified on that ground. Every brick built before the shared layers exist births its own addressing and its own signal path — "two mechanisms … a signal which is unreadable or buggy … destroying the stream" (said: majkee §6).

**Decision question.** *What is the first commitment that opens the body — which spine slice, which shared layers are born with it, and who owns the observe seam — such that HELLO becomes buildable in the termpanum and stridulatrix lines without re-cutting an organ later?*

## 2. Established facts and remaining uncertainties

### Facts (each with its strength)

| id | fact | strength |
|---|---|---|
| F1 | View (ovitmugen, rb-*) and compose (termbrana composer) run; observe and record have zero code in nablarva | bytes · inventory |
| F2 | The three built/contracted parts occupy v0's layers (service · view+gate · substrate+tissue) by convergence; 9 of 19 v0 patterns survive as-is, 7 amended, 3 dead by lock | field §2–3 · Houston "no break" |
| F3 | Shared layers with ≥2 **coded** clients today: install/package (`~/ia-sync/install-pkgs`, L8′) · KEYS grammar (ARCHITECTURE §5). Boot/env: 1 coded + 1 contracted | Houston correction of field §4 |
| F4 | majkee's named shared layers: **address registry** (writer: ovitmugen on pane creation; readers: termbrana, stridulatrix) · **shared observation record** (producers: termpanum/lab, hooks, Antensor) · **config rule** (no paths in scripts; everything resolved from nabLarva settings) | said: majkee §1, §3, §4 |
| F5 | **Split adopted (working):** termbrana composes and submits — ends at a packet file in the bus; stridulatrix sends — journal (L3 S1), ordering, cursors, delivery adapters (S5), receipts, the process/API boundary external things talk to (phone engine, L14 D6; stage 2, S7); may *request* a pane, ovitmugen *performs* it (L17) | said: majkee §4 ("I'm confirming your version"; "the sender itself should be the stridulatrix") |
| F6 | Workflow (lens 1) = **HELLO**, a hand-off; it is **delivery** — gated by L14 D4 (relay-00-research) and D7 (blind triangulation), L4 (send-keys death), U-send-keys parked for majkee | said: majkee §4, §5 · locked: L4, L14 |
| F7 | Observation record ≠ room journal: **stretches**, not breaks; 5 constraints (one serialized writer per file · name the owner or admit the owner gap · timestamp merge is a view · never room truth or delivery authority · CLI-hook producers optional, own file, hook→bus parked) | Houston consult · inferred strength |
| F8 | **Package Q** (first runnable observation slice) is built in the termpanum line by its own cSharp (bed termpanum-X0-source-contract or successor); this bed designs the body it fits | said: majkee §4 |
| F9 | **instarmux = the skin** — a real UI only if zsh + tmux + the simplified way are not enough; Slint is a candidate under it; alternative: well-designed pipes IDE → nabLarva | said: majkee §2, §7 |
| F10 | Zellij observer = second-class, dormant; tmux-first; two loaders would be the cost; "if I will even need it" open | said: majkee §2 |
| F11 | Muticula = time-limited writer token + notifier; stopped mid-build; majkee's lean for the smallest push-back: git worktrees (L12 names them) | said: majkee §6 |
| F12 | Continuity (cards, reincarnation, planning across sessions) has **no organ**; cards bind to a bed's RUNBOOK partially; the rest is undecided — majkee: "I don't have any fixation" | said: majkee §1, §8 |
| F13 | Names: stridularium retired as a *cultural* name (docs edit + one flag line, no full loop); reposoma is not an organ (PROJECT-DESIGN §3.4 misplaced); Boost to be renamed; VIST = protocol only; Antensor = lab → body translator | said: majkee §5, §8, §9 |
| F14 | docs/ARCHITECTURE.md §2.5/§4.7/§9 are stale against L21 (P5-b adopted); cite L21 | Houston · dock r8 items |

### Uncertainties (each with who resolves it and when)

| id | uncertainty | resolves | when |
|---|---|---|---|
| U-a | **Owner and home of the observe seam** — the shared observation record and the address registry (Houston constraint 2) | majkee — deck X0-3 | now |
| U-b | **Substrate home** (field D3): `<project>/.nablarva/` + `~/.nablarva/` defaults, config-resolved (majkee's lean §1) vs XDG vs bed-local | majkee — deck X0-4 | now, or deferred bed-local |
| U-c | **Doorbell mechanism** — is a contentless nudge over the PTY "injection" in L4's sense (U-send-keys) | majkee, on evidence from a running slice | after the slice |
| U-d | **Envelope** (docket 8; four candidates, ARCHITECTURE §4.5) | bounded comparison first (Agol working default) | termpanum line |
| U-e | **Observation fidelity** — pane output (`pipe-pane`) vs PTY master; stillness vs readiness (lens 5) | Package Q, termpanum line | that bed |
| U-f | **Vendor spawn/message internals** (Claude Code · Codex · Gemini CLI) — U-vendor-spawn | bounded @Epoch pass | only when a stridulatrix design needs it |
| U-g | **Continuity / journaling** — rotation of long canon files; planning continuity across sessions | majkee; no fixation yet | parked; one requirement carried: records segment-able, head/index readable in ≤80 lines |
| U-h | **Config layer** home and owner (the rule is set; the mechanism is not) | the first bed that needs it | spine bed |
| U-i | Field Q5: does termpanum's documentary D package need an architecture GO | Cartan's bed, via majkee | not this bed |

## 3. Alternatives for the first commitment, their costs, and the recommendation

| option | what it is | buys | costs | can be lost |
|---|---|---|---|---|
| **A · Spine slice first** | one read-only vertical: a producer writes the shared observation record (per-writer files) → ovitmugen (or a tiny reader) shows one derived state per seat; born WITH it: the address registry and the config rule; Package Q in the termpanum line is the observe stage | the two shared layers majkee named, proven by a client each; HELLO becomes observable before it is attempted; no lock touched (Houston: stretches, with constraints); the skin gets requirements for free (lens 9 collected while watching) | HELLO itself waits one bed; two beds coordinate (this line + termpanum); the record layout is decided before the envelope (docket 8) — reversible because per-writer files are envelope-agnostic | if the slice overbuilds (dashboard, envelope, router) it becomes the third mechanism; mitigated by acceptance evidence that is deliberately small |
| **B · HELLO first, human-carried** | termbrana submits a packet; majkee pastes it into the target pane; reply by hand; observe later | the wanted workflow in days; nothing gated (human is the carrier, L17) | unobservable: cannot tell stillness from readiness (lens 5), cannot tune; addressing is born ad hoc (no registry) — exactly the duplication §6 names; the delivery seam grows a habit before its research verdict (L14 D4) | the possibility of a clean regulated path later without re-cutting termbrana |
| **C · Skin first** (instarmux sitting) | Houston sitting on UI vs terminal; Slint vs zsh | a framework decision | no requirements exist yet (lens 9 unanswered); majkee: skin only if the simplified way is not enough — not yet shown; the sitting would decide in a vacuum | time; a framework chosen against imagined needs |
| **D · Substrate only** | registry + config rule + record layout as contracts and thin reference files; no slice | cheapest; pure design | nothing demonstrates it; design-in-vacuum risk; L21 (2): implementing a shared layer needs its own release anyway, so a contract without a client is paper | majkee's patience; the convergence evidence that only clients provide |

**Recommendation: A.** One line: *build the smallest vertical that forces the two shared layers to exist and be read by a second client, keep every write out of every session, and let HELLO be the next bed, not this one.*

Why not B, in one sentence: B gets the demo and loses the stream — the exact failure majkee described in §6.

Lens 2 test ("spine before skin"): holds. The deciding uncertainty is observation fidelity + ownership (U-a, U-e), not interaction; the skin has a running baseline (ovitmugen, rb-*) and no requirements yet; C is premature by majkee's own condition (F9).

Lens 11 (falsifiers): if the registry cannot be written by ovitmugen without a hardcoded path → the config rule is harder than assumed, stop and design config first. If no producer can write per-writer files without a serializer → Houston constraint 1 bites, narrow to one producer. If the derived state in the view needs tmux polling rather than the record → the record is not yet useful, stop. Expected results are frozen by the RUNBOOK before any producer runs (assay reads the yardstick, never the transcript).

## 4. Scope and acceptance evidence for ONE planning RUNBOOK

**Bed (proposed name, majkee picks):** `nablarva-X5-spine-slice` — or continue the X-line numbering majkee prefers (N6 lean: continuous shape by line). Head: a cSharp (fresh head). This bed (arch-X0) hands it the RUNBOOK substrate; it does not run it.

**Gate (one line):** majkee records GO or STOP on a witnessed read-only spine slice: one producer writes the shared observation record in per-writer files at a config-resolved home, the address registry holds one seat-addressed entry per pane written by ovitmugen on `ov-up` and surviving `ov-down`/`ov-up`, a second client reads both to show one derived state per seat, and an independent witness confirms that no byte was written into any session.

**In scope**
1. Address registry — contract + first writer (ovitmugen on pane creation) + first reader (a `nablarva-*` status reader or termbrana's target pick, whichever is cheaper); seat-addressed (durable identity), not PID/pane; config-resolved path.
2. Config rule — the mechanism that resolves the registry and record homes (settings file; no path in any script); home per X0-4.
3. Shared observation record — layout only: per-writer append-only files, one serialized writer each (Houston c1), segment-able with a head/index readable in ≤80 lines (U-g requirement); envelope-agnostic lines; **not** docket 8.
4. One producer — the cheapest honest one: a tmux `set-hook` writing to its own per-pane file, OR Package Q's collector if the termpanum line lands first (coordination row in STATUS).
5. One view — ovitmugen's sessions column or a tiny reader shows one derived state (e.g. active / idle by last-event age) from the record, not from tmux polling.
6. Lens-9 harvest — a one-page skin requirements note written from what the operator needed to see while using the slice; input to the instarmux sitting brief, no framework choice.
7. Houston `card: consult` at closure (touches L17/L21 by implementing a shared layer; L21 (2): its own release = this bed's GO).

**Out of scope (deliberately left open)**
delivery of any kind (HELLO, doorbell, stridulatrix) · envelope choice (docket 8) · router (`nablarva <tool>`) · dashboard · Zellij loader · muticula · skin framework · phone organ · continuity mechanism.

**Acceptance evidence (frozen before build; assay verifies)**
- E1 `grep` over the slice's scripts finds no literal registry/record path; the resolved path comes from the settings file (command + output).
- E2 `ov-up <slug>` → registry gains N seat entries; `ov-down` + `ov-up` → same seat ids, new pane ids (diff of two registry snapshots).
- E3 record directory: one file per writer; a mechanical check shows no two writers share a file (writer id in filename and in every line).
- E4 reader output shows a state per seat derived from the record; killing the producer changes the state without touching tmux state.
- E5 witness: tmux `pipe-pane`/hook audit shows zero `send-keys`/`paste-buffer`/`load-buffer` into any session pane for the slice's lifetime (L4, L17).
- E6 head/index of the record readable with `head -80`.
- E7 Houston closure consult: fits or stretches with constraints carried to flag/dock; no breaks.

**What this bed (arch-X0) hands over**: this package · the organ-walk record · field r1 · Houston consult · inventory · a RUNBOOK substrate section mirroring §4 · the costed-deck method (handoff §6) · the Houston-by-phase table (handoff §7).

## 5. Ranked next beds (the CS-card gate asked for this)

1. **spine slice** (above) — now.
2. **termpanum line: Package Q** — already theirs; coordinate the producer (in-scope item 4).
3. **bookkeeping batch** — docs/ARCHITECTURE.md r8 (dock items C1/M3/M4/C4 + §7 organ table: reposoma out, stridularium cultural retirement + flag line, Antensor as translator, instarmux as skin, split F5 as `said: majkee`) + PROJECT-DESIGN §3.4/§3.8 + termbrana README vs L21 (C2) — one small docs bed, or folded into the spine bed's closure (deck X0-5).
4. **instarmux sitting brief** — after the lens-9 harvest exists (deck X0-6).
5. **stridulatrix-00** — HELLO design on the registry + record; opens relay-00-research for real; U-send-keys decided on slice evidence; U-vendor-spawn Epoch pass as input.
6. **muticula** — stays asleep until registry + notifier exist; worktrees interim (deck X0-7).

## 6. The deck — one block at a time (answers land verbatim in raw/answers.majkee.deck.2026-10-24.md)

```
GAVEL X0-1 · Is the first commitment the read-only spine slice (A), with HELLO as the next bed?
  options:      a) A — spine slice first   b) B — HELLO first, human-carried   c) D — substrate contracts only   d) C — skin sitting first
  context:      §3 above. HELLO is your named workflow; it is delivery and research-gated. The slice makes it observable and births the two shared layers you named. B is faster to a demo and births ad-hoc addressing.
  buys/cost/lost: §3 table.
  consequence:  a) one planning RUNBOOK (§4) goes to a fresh cSharp; termpanum line coordinates Package Q.  b) termbrana-02 opens; registry deferred.  c) a contracts bed; no client.  d) Houston sitting without requirements.
  lean:         oraculum → a
  source:       this file §3; raw/answers.majkee.organs §4–§6
  answer:       ___
```
```
GAVEL X0-2 · The termbrana / stridulatrix split — record as working split in ARCHITECTURE r8 as `said: majkee`?
  options:      a) yes, as the table in chat (compose/submit | send/journal/deliver/API; boundary = packet in bus; stridulatrix requests panes, ovitmugen performs)   b) yes with a changed cell (name it)   c) not yet
  context:      You confirmed it twice (§4, §5). Recording it moves it from chat to the architecture doc; it is not a flag lock.
  lean:         oraculum → a
  source:       raw/answers.majkee.organs §4
  answer:       ___
```
```
GAVEL X0-3 · Who owns the observe seam's shared parts — the address registry and the shared observation record?
  options:      a) a new shared-substrate component (own thin folder per L18, disk name TBD, owner = the spine bed's head until a steward is named)   b) registry → ovitmugen (writer owns), record → termpanum (lab owns)   c) both → stridulatrix (the body's server), built later
  context:      Houston constraint 2: name the owner or admit the gap. a) keeps them independent of any organ's liveness (single-tool rule). b) is cheapest now but ties two shared layers to two organs' lifecycles. c) delays both behind a zero-code organ.
  buys/cost/lost: a) clean sharing / one more folder / nothing structural. b) no new folder / coupling / the registry dies with ovitmugen's scope. c) one server owns truth / waits on relay research / the slice cannot start.
  lean:         oraculum → a
  source:       raw/consult.d1-observation-record.houston (c2); raw/answers.majkee.organs §3, §4
  answer:       ___
```
```
GAVEL X0-4 · Substrate home for registry, record and settings?
  options:      a) `<project>/.nablarva/` for project-scoped state + `~/.nablarva/` for machine defaults, both resolved via the config rule   b) XDG (`~/.config/nablarva`, `~/.local/state/nablarva`)   c) defer — bed-local `<bed>/.nablarva/` for the slice only
  context:      Your §1 lean is a). HELLO r1 modelled a) concretely (field "also noticed"). v0 proposed b). c) costs nothing now and moves the choice to the slice's closure.
  lean:         oraculum → a (c acceptable if you want to see the slice first)
  source:       raw/answers.majkee.organs §1 (common things); field §6 D3
  answer:       ___
```
```
GAVEL X0-5 · Bookkeeping batch (ARCHITECTURE r8 + organ table + stridularium cultural retirement + PROJECT-DESIGN §3.4/§3.8 + termbrana README C2) — where?
  options:      a) one small docs bed now, before the spine bed opens   b) folded into the spine bed's closure promotion   c) Houston audit card, you invoke
  context:      All items are known (dock 2026-10-24 + this walk). a) gives the spine bed a clean doc to cite. b) saves a bed; the doc stays stale for weeks. c) Houston names edits; a shell seat makes the diff.
  lean:         oraculum → a (small; Delta-driven; one evening)
  source:       dock.md 2026-10-24; raw/answers.majkee.organs §5, §8; Houston consult "ARCHITECTURE is behind the flag"
  answer:       ___
```
```
GAVEL X0-6 · Skin (instarmux): sitting now, or requirements first?
  options:      a) lens-9 requirements note harvested during the spine slice; instarmux sitting brief after   b) Houston sitting now on UI vs terminal (Slint vs zsh)
  context:      Your condition: a real UI only if zsh + tmux + the simplified way are not enough — not yet shown. The slice is the first thing you will watch; what you need to see is the requirement.
  lean:         oraculum → a
  source:       raw/answers.majkee.organs §2, §7
  answer:       ___
```
```
GAVEL X0-7 · Muticula: sleep until registry + notifier exist; git worktrees interim?
  options:      a) yes   b) resume muticula-01 as is   c) retire muticula; worktrees permanent
  context:      Your lean (§6) was worktrees as the smallest push-back. A writer token needs a seat identity (registry) and a notify path (stridulatrix's one write path); built earlier it is a third mechanism.
  lean:         oraculum → a
  source:       raw/answers.majkee.organs §6; flag L12 (worktrees)
  answer:       ___
```

## 7. Not decided by this package (named, not dropped)
U-send-keys (yours, on slice evidence) · docket 8 · U-vendor-spawn · U-continuity · stridularium's new name and Boost's new name (one-cell edits later) · the phone organ (backlog) · Zellij loader · Field Q5.
