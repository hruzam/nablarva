# RUNBOOK: relay-X2-research

> Authored on 2026-11-26 by the closing head of `relay-X1-probes` (flight) in the planning posture, on Majkee's word
> (`raw/decision.majkee.open.2026-11-26.md`). Fixed from the moment the lead of this bed has read it. Where things stand
> is in `STATUS.md`, never here.

```yaml
goal: >
  One recorded research verdict on the relay program — a PTY impulse layer for session relay and its tracker, under
  the operator's constraints of L14 — so that the PTY research and the tracker draft open, or do not open, on dated
  evidence instead of on momentum.
gate: >
  Majkee records GO or STOP on a recorded research VERDICT for the relay program — REINVENT, ADOPT or REFUSE, ranked,
  with its recommendation on disk — resting on a dated and sourced wheel check, overengineering check and
  vendor-harness check, with the blind research brief of L14 D7 returned beside it. The verdict locks no architecture
  and releases no build.
participant_1: [lead, {brand: claude, model: fable, effort: high}, host: home, role: "head and status_owner; reads, assigns, writes the verdict, commits and pushes its own work"]
participant_2: [auditor, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, instrument: resident, role: "the other vendor's check of every document before Majkee reads it; independent reader of the Codex-side facts"]
participant_3: [controller, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, instrument: resident, role: "hands and second reader, window supervisor-relay; runs what a POINT names; no push duty"]
participant_4: [exec, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, instrument: resident, role: "Majkee's decision desk for a gavel loop, if the head needs more than one ask"]
participant_5: [majkee, {brand: human}, host: home, role: "the gate word; sends the blind brief to the other vendor line and brings its answer back, or names who does; every release"]
status_owner: lead
schema_note: "runbook/GUIDE.md and status/GUIDE.md as read on 2026-11-26; res/research.md (gaveled 2026-09-03) is this session's shape"
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/relay-X1-probes.flight.2026-11-26.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-11-26.auditor.md
```

The codex seats' models are copied from the predecessor's RUNBOOK and were not re-read; the lead reconciles the roster
against live tmux in its first step.

## Why this session exists

L14 D4 puts research before build: one session that decides whether the relay program should exist at all, before
`relay-X3-pty` and `relay-X4-tracker` may open. A seed and two blind briefs were written on 2026-09-30 and the session
was never opened. Since then two beds on this line produced evidence — a door inventory on paper and four witnessed
probe packets — and sibling beds qualified sources and gathered alternatives. The scope is big (session relay, a
mechanical tracker, a phone lens), so the golden rule is a gate of its own here. A NO costs this one session; a missed
NO costs a program.

## Fixed facts

- **The operator's constraints are inputs, not subjects.** L14 D1 (PTY is the base layer; vendor doors are weather,
  parked), D2 (the file plane is the spine; no transport is truth), D5 and D6 (the phone is a thin, app-scoped lens)
  precede the research. D3 (discrete states, never comprehension) is pending under docket 8. The verdict may say that
  a constraint costs something; it does not reopen one.
- **A seed and the blind research brief exist** — `seed.relay-research.2026-09-30.md` and
  `brief.blind.relay-research.2026-09-30.md` (References). The brief is addressed from Majkee to the other vendor
  line and names its own deliverable: a source table, per-vendor detectable states, gaps, a verdict and one
  falsifier. Whether it was ever sent or answered is recorded as unknown (`DESIGN.md`, line 31).
- **The second blind brief, on architecture, is not this session's.** It belongs to the architecture lock.
- **Evidence this line already holds** is cited, never re-run: the predecessor beds' packets and handoffs, and the
  helper inventory. `relay-X1-probes` is closed; its rows stand as tried once and qualify no door.
- **Other beds hold part of the wheel check** — by their gates: `terminal-workspace-X0-approaches` (dated native and
  reuse alternatives), `termpanum-X1-source-qualification` and `termpanum-X0-source-contract` (a tmux output source),
  `nablarva-02-pipe-qualification` (a native assignment path). They are read by path; their pens are their heads'.
- **Dates rule.** Vendor behaviour changes release to release. A statement about a vendor without a source and a date
  is not evidence; training memory is not a source.
- **Several sessions commit in this checkout.** Each commits path-scoped and pushes its own work; a plain push carries
  every local commit on `core`.

## prompt-0 — lead

```text
You are the lead and status_owner of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ on host home.
Read in order: /home/hruzam/unikuklatrix/nablarva/AGENTS.md, .dev/session/flag.md (L4, L12, L14, L20, L21, L22),
.dev/session/pulse.md, this RUNBOOK, STATUS.md, then the two files under observations_read. Then:

1. Reconcile the roster against live tmux and say in STATUS what differs. Poke no seat outside participants 2 to 4.
2. Map what is already held, by path, into raw/prior-evidence.map.md: the seed, the brief, DESIGN.md and
   HYPOTHESES.md of the seam folder; the two relay beds' packets and handoffs; the helper inventory; the sibling
   beds named in Fixed facts. One line per item: what it establishes, its date, what it does not show.
3. The blind brief first, because it runs in parallel. Check the 2026-09-30 brief for stale facts (vendors, versions,
   dates). Change facts only — add no finding and no lean of this line. Bring it to Majkee in one ask: he sends it, or
   names who does. File the answer verbatim in raw/ before you read it against your own work.
4. The three checks of /home/hruzam/reposoma/raw.guides/runbook/res/research.md, each dated and sourced:
   wheel — a dated research pass by a research child (@Epoch class), in the brief's source-table shape;
   overengineering — would a smaller composition serve: the file plane, the file-poke with a finite watch, native
   status surfaces, the recurring kinds in the helper inventory;
   vendor harness — what the vendors ship or have announced, and the native change that would retire the build.
5. Write research-verdict.md in the bed: one ranked verdict — REINVENT, ADOPT or REFUSE — its recommendation, any
   condition stated testably, and one falsifier. Put the blind answer beside it and list where the two differ. Do not
   merge them: the termination is a committed answer and a falsifier, never consensus.
6. Give the verdict file to the auditor for its check before Majkee reads it; take its points; then ask him for GO or
   STOP in one ask. Record his words verbatim in raw/decision.majkee.*.md and nowhere else.

Done when: his GO or STOP on research-verdict.md is recorded. Return upward to Majkee only for the gate word, a
release, a lock, or an act that reaches outside this bed; decide everything else with the team and report it as done.
```

## prompt-1 — auditor

```text
You are the auditor of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident, host home).
You act on a POINT of the lead: a file in _bus/, announced by one poke line. You look and report; you change nothing
outside your RETURN. Your standing task: check every document that goes to Majkee against its sources before he reads
it — numbers, dates, links, and above all sentences that claim more than their source shows. Answer PASS or REVISE in
the first line of field 4. Write the RETURN to the path the POINT names and ring one reply bell into the lead's pane.
```

## prompt-2 — controller

```text
You are the controller of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident, host
home, window supervisor-relay). You act on a POINT of the lead: a file in _bus/, announced by one poke line. You run
exactly what it names — local, read-only facts of the Codex side (installed version, help surfaces, changelog as
shipped), a second reading of a source table — and write a RETURN to the path it names, with one reply bell. You
start no session, send nothing into any session, and do not push for this bed.
```

## prompt-3 — exec

```text
You are Majkee's decision desk for /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident,
host home). Only if the lead sends a sheet: present its questions one at a time, record his answers verbatim in the
file the sheet names, read the summary back. Answer from files whatever a file can answer before you ask him.
```

## Candidate rows from the closing harvest — candidates, not law

Carried from `harvest.2026-11-26.auditor.md`; the lead adopts, adapts or declines each and says so once in STATUS.

- **U20** — a receipt records carrier acceptance, end of watch and later arrival separately.
- **U21** — a comparison of trials names how the target's last turn ended and what earlier actions may affect it.
- **U22** — before any walkthrough, the desk answers what files can answer; his time goes to choices that change the work.
- **U23** — an interim claim is checked against current evidence before he hears it, or carries its observation time
  and names the pending check.

## Known constraints + destructive holds

- **Nothing is activated and nothing is delivered** (L21): no session is started, no sample, no message into any
  session except coordination pokes to participants 2 to 4. The windows `spare-codex` and `spare-claude` are free;
  starting anything in them needs Majkee's own word.
- **L4** — send-keys injection is a recorded death; the one exception is spent. Reply bells into the lead's pane are
  an older, separate allowance.
- **L12** — branch `core`, plain pull and push, never rebase, never force; commits path-scoped; history is not
  rewritten. Other sessions' files are never staged.
- **L14** — the verdict locks no architecture, opens neither `relay-X3-pty` nor `relay-X4-tracker`, and qualifies no
  door. **L20** — observations authorize nothing. **L22** — `.majkee/` and `.hlm/` are never read or listed.
- **His typed words** stand verbatim only in `raw/decision.majkee.*.md`. A bell or a note from a seat is never his word.
- **Nothing private goes into Git.** `CACHE.*.md` files in any bed are his continuity files: never opened, and
  excluded from every search. `~/.codex/rules/default.rules` and `~/.codex/config.toml` are his.
- **Not this bed's seats:** `seniorDev`, `myShell`, `eSharp`, `supervisorCli`. They are not poked.
- **Web research reads; it posts nothing** and sends no private path, name or address to any service.

## Acceptance evidence

- `research-verdict.md`: the three checks, each with dated sources; one ranked verdict with its recommendation and a
  falsifier; conditions stated testably.
- The source table and `raw/prior-evidence.map.md`.
- The blind brief as sent and its answer verbatim in `raw/`, with the list of differences beside the verdict.
- The auditor's RETURN on the verdict file, and the lead's VERDICT on that RETURN.
- Majkee's GO or STOP in `raw/decision.majkee.*.md`.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L14 with the amendment of 2026-11-23; the locks named above.
- `/home/hruzam/reposoma/raw.guides/runbook/res/research.md` — the research gate: three checks, three verdicts.
- `/home/hruzam/unikuklatrix/nablarva/meshup/seam.cross-vendor-relay.2026-08-05/raw/` — `decisions.relay.2026-09-30.md`,
  `seed.relay-research.2026-09-30.md`, `brief.blind.relay-research.2026-09-30.md`; beside it `DESIGN.md`, `HYPOTHESES.md`.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/handoff.successor-stage.2026-11-26.md` — what the
  predecessor established and left open; its section 3 before poking anyone.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md` — the line ledger: open work, custody pointers.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md` — helpers built
  ad hoc and the kinds that recur.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/STATUS.md`,
  `.../termpanum-X1-source-qualification/STATUS.md`, `.../termpanum-X0-source-contract/STATUS.md`,
  `.../nablarva-02-pipe-qualification/STATUS.md` — the sibling beds named in Fixed facts.
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` and `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md` — POINT,
  RETURN, VERDICT and the file-poke.

## What closes the gate

Majkee's recorded GO or STOP on `research-verdict.md`. On GO the verdict file becomes the founding reference of
whatever opens next under L14; on a REFUSE that he accepts, the scope ends here and that is a success of the gate.

## What this session deliberately does not do

- No PTY research and no tracker draft — those are `relay-X3-pty` and `relay-X4-tracker`, after the verdict.
- No architecture: no design, no second blind brief, no lock.
- No probe, no sample, no qualification of a door; the open rows of `relay-X1-probes` stay in the line ledger.
- No retirement of the file-poke; if the verdict names a replacement, mapping its coverage is a later bed's work.

## Seat to wake

A fresh lead: @Flight in project-session mode, driven by Majkee, on the carriage `relay-X1-probes` ran on (claude,
fable, effort high), in the window `lead`. Reason: the work is one head coordinating a research child and two
resident seats of the other vendor toward one written verdict — the shape the predecessor ran. If he wants the verdict
written by a strategist instead, the same RUNBOOK serves @Oraculum as head with no other change than participant_1.
The operator wakes the seat, with the cold-start card.

## Provisional coordination carry-forward

- Shared coordination and retirement obligation: `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md`, §Carry-forward and retirement.
- Owning development line: `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md`; the shared bridge is tracked there.
- At closure, account for the provisional dependency in the ledger and the successor's references until its recorded replacement disposition.
