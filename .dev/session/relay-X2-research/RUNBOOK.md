# RUNBOOK: relay-X2-research

> Authored on 2026-11-26 by the closing head of `relay-X1-probes` (flight) in the planning posture, on Majkee's word
> (`raw/decision.majkee.open.2026-11-26.md`); checked once by the auditor before any lead read it. Fixed from the moment
> the lead of this bed has read it. Where things stand is in `STATUS.md`, never here.

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
participant_2: [auditor, {brand: codex, model: GPT-6.2-Astra, effort: high}, host: home, instrument: resident, role: "the other vendor's check of every document before Majkee reads it, the outgoing brief included"]
participant_3: [controller, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, instrument: resident, role: "hands and second reader, window supervisor-relay; runs what a POINT names; no push duty"]
participant_4: [exec, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, instrument: resident, role: "Majkee's decision desk for a gavel loop, if the head needs more than one ask"]
participant_5: [majkee, {brand: human}, host: home, role: "the gate word; sender of the blind brief, or names its courier; gates the comparison of the two answers; every release"]
status_owner: lead
schema_note: "runbook/GUIDE.md and status/GUIDE.md as read on 2026-11-26; res/research.md (gaveled 2026-09-03) is this session's shape"
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/relay-X1-probes.flight.2026-11-26.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-11-26.auditor.md
```

The codex seats' models are as their panes' footers showed them to the auditor on 2026-11-26. The lead reconciles the
roster against live tmux in its first step.

## Why this session exists

L14 D4 puts research before build: one session that decides whether the relay program should exist at all, before
`relay-X3-pty` and `relay-X4-tracker` may open. The seed of 2026-09-30 says in its own status line that the session
was not opened. Since then two beds on this line produced evidence — a door inventory on paper and four witnessed
probe packets. The scope is big (session relay, a mechanical tracker, a phone lens), so the golden rule is a gate of
its own here. A NO costs this one session; a missed NO costs a program.

## Fixed facts

- **The operator's constraints are inputs, not subjects.** L14 D1 (PTY is the base layer; vendor doors are weather,
  parked), D2 (the file plane is the spine; no transport is truth), D5 and D6 (the phone is a thin, app-scoped lens)
  precede the research. D3 (discrete states, never comprehension) is pending under docket 8. "PTY as impulse layer"
  is a proposed boundary, not a lock. The verdict may say what a constraint costs; it does not reopen one.
- **A seed and the blind research brief exist** (References). The brief is addressed from Majkee to the other vendor
  line — Asymmetry (ChatGPT) — and names its deliverable: a source table, per-vendor detectable states, gaps, a
  verdict and one falsifier. Whether it was ever sent or answered is recorded as unknown (`DESIGN.md`, line 31).
- **D7 asks for two blind briefs before the architecture is locked.** Only the research brief is this session's.
- **Evidence this line already holds** is cited, never re-run: the predecessor beds' door inventory, packets and
  handoffs, and the helper inventory. `relay-X1-probes` is closed; its rows stand as tried once and qualify no door.
- **Sibling beds are sources to inspect, not results to cite.** `terminal-workspace-X0-approaches`,
  `termpanum-X0-source-contract`, `termpanum-X1-source-qualification` and `nablarva-02-pipe-qualification` touch the
  wheel check. Their present state is in their own STATUS files; any result taken from them carries its date and its
  state there. Their pens are their heads'.
- **Dates rule.** A statement about a vendor without a source and a date is not evidence; training memory is not a
  source.
- **Several sessions commit in this checkout.** Each commits path-scoped and pushes its own work; a plain push carries
  every local commit on `core`.

## prompt-0 — lead

```text
You are the lead and status_owner of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ on host home.
Every path below is under /home/hruzam/unikuklatrix/nablarva/ unless it starts with /.
Read in order: AGENTS.md, .dev/session/flag.md (L4, L12, L14, L20, L21, L22), .dev/session/pulse.md, PROJECT.yaml,
.dev/session/relay-X2-research/RUNBOOK.md and STATUS.md, then the two files under observations_read.
Your POINTs go to .dev/session/relay-X2-research/_bus/NN.lead.point.md, RETURNs come back as
_bus/NN.<seat>.return.md, your dispositions are _bus/NN.lead.verdict.md. Majkee's words are recorded verbatim in
.dev/session/relay-X2-research/raw/decision.majkee.<topic>.<date>.md and nowhere else.

1. Reconcile the roster against live tmux and write what differs into STATUS. Poke no seat outside participants 2 to 4.
   The three codex seats stay in their windows from relay-X1-probes and remember that bed, not this one: your first
   POINT to each names this bed, tells the seat to read its prompt in this RUNBOOK, and names your own pane for the
   reply bell (read it from tmux, do not assume the predecessor's). Ask them for facts by POINT; take no briefing.
2. Map what is already held, by path, into .dev/session/relay-X2-research/raw/prior-evidence.map.md: the seed, the
   brief, DESIGN.md and HYPOTHESES.md of the seam folder; the two relay beds' packets and handoffs; the helper
   inventory; the sibling beds of Fixed facts. One line each: what it establishes, its date and state, what it does
   not show.
3. The blind brief first, because it runs in parallel. Leave the dated original untouched. Make a send copy in
   raw/ that corrects stale facts only (vendors, versions, dates) and carries no finding and no lean of this line;
   have the auditor check it; show Majkee the corrections in one ask. He sends it, or names the courier. When the
   answer comes back it is filed verbatim in raw/ and stays unread by you and by your research child.
4. The three checks of /home/hruzam/reposoma/raw.guides/runbook/res/research.md, each dated and sourced:
   wheel — a dated research pass by a research child of yours (a subagent, @Epoch class; not a new CLI session), in
   the brief's source-table shape;
   overengineering — would a smaller composition serve: the file plane, the file-poke with a finite watch, native
   status surfaces, the recurring kinds in the helper inventory;
   vendor harness — what the vendors ship or have announced, and the native change that would retire the build.
5. Write .dev/session/relay-X2-research/research-verdict.md: one ranked verdict — REINVENT, ADOPT or REFUSE — with its
   recommendation, every condition stated testably, and one falsifier. For ADOPT, name the existing thing and the
   delta it needs. Commit it. Only after that commit read the blind answer, and list where the two differ. Do not
   merge them: the termination is a committed answer and a falsifier, never consensus. Majkee gates the comparison.
6. Give the verdict file and the list of differences to the auditor before Majkee reads them; take its points; then
   ask him for GO or STOP in one ask.

Done when: his GO or STOP on research-verdict.md is recorded. Return upward to Majkee only for the gate word, the
brief, a release, a lock, or an act that reaches outside this bed; decide everything else with the team and report it
as done.
```

## prompt-1 — auditor

```text
You are the auditor of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident, host home).
You act on a POINT of the lead: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/_bus/NN.lead.point.md,
announced by one poke line. You look and report; you change nothing outside your RETURN at
/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/_bus/NN.auditor.return.md. Your standing task: check
every document that goes to Majkee against its sources before he reads it — the outgoing brief, the verdict, the list
of differences: numbers, dates, links, and above all sentences that claim more than their source shows. PASS or
REVISE in the first line of field 4. One reply bell into the lead's pane is your allowance; you send nothing else.
```

## prompt-2 — controller

```text
You are the controller of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident, host
home, window supervisor-relay). You act on a POINT of the lead:
/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/_bus/NN.lead.point.md, announced by one poke line.
You run exactly what it names — local, read-only facts of the Codex side (installed version, help surfaces, changelog
as shipped), a second reading of a source table — and write
/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/_bus/NN.controller.return.md. One reply bell into
the lead's pane is your allowance; apart from it you start no session, send nothing into any session, and do not
push for this bed.
```

## prompt-3 — exec

```text
You are Majkee's decision desk for /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/ (codex, resident,
host home). Only if the lead sends a sheet under /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/:
present its questions one at a time, record his answers verbatim in the decision file the sheet names, read the
summary back. Answer from files whatever a file can answer before you ask him.
```

## How this party talks

The shared rule is `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md` (provisional). What this party does with it:

- **Lead → a codex seat:** the POINT file first, committed; look at the target pane; then one labelled line —
  `codex queue --thread <id> --message "[poke pNN] read <absolute path> — <a few words>"`, without `--resume`. Exit 0
  proves that the queue accepted the call, nothing more. Every poke is logged in `raw/pokes.log.md`.
- **A codex seat → lead:** the RETURN file, and one bell `[bell rNN] return at <absolute path>` into the lead's pane.
  The file is the truth; the bell is a seat's hint and never Majkee's word.
- **Wait with a finite file watch** on the RETURN path, in the background. Silence says nothing about a seat's health.
- **Fallback.** After a *definite* failure — the call exits non-zero — one labelled manual pointer, once, logged. No
  agent types into a codex pane (L4), so the manual sender is Majkee: ask him by the notifier. After an *uncertain*
  send — accepted, no RETURN within the watch — nothing is repeated and no carrier is switched until the receipt is
  reconciled from the file or the pane.

## Candidate rows from the closing harvest — candidates, not law

From `harvest.2026-11-26.auditor.md`; the lead adopts, adapts or declines each and says so once in STATUS.

- **U20** — a receipt records carrier acceptance, end of watch and later arrival separately, and keeps the original
  watch deadline when later evidence appears.
- **U21** — a pair of trials names how the target's last turn ended and which earlier actions may affect the
  comparison; independent trials use fresh samples, a trial of queued input may deliberately keep the first turn.
- **U22** — before any walkthrough the desk answers what files can answer; his time goes to choices that change the work.
- **U23** — an interim claim is checked against current evidence before he hears it, or carries its observation time
  and names the pending check.

## Known constraints + destructive holds

- **Nothing is activated and nothing is delivered** (L21): no CLI session is started and no sample; nothing goes into
  any session except coordination pokes to participants 2 to 4 and their reply bells. The windows `spare-codex` and
  `spare-claude` are free; starting anything in them needs Majkee's own word.
- **L4** — send-keys injection is a recorded death; the one exception is spent. Reply bells into the lead's pane are
  an older, separate allowance.
- **L12** — branch `core`, plain pull and push, never rebase, never force; commits path-scoped; history is not
  rewritten. Other sessions' files are never staged.
- **L14** — the verdict locks no architecture, opens neither `relay-X3-pty` nor `relay-X4-tracker`, and qualifies no
  door. **L20** — observations authorize nothing. **L22** — `.majkee/` and `.hlm/` are never read or listed, in any
  repository; git commands there are path-scoped.
- **His typed words** stand verbatim only in `raw/decision.majkee.*.md`. A bell or a note from a seat is never his word.
- **Nothing private goes into Git.** `CACHE.md` and `CACHE.*.md` in any bed are his continuity files: never opened,
  and excluded from every search. `~/.codex/rules/default.rules` and `~/.codex/config.toml` are his.
- **Not this bed's seats:** `seniorDev`, `myShell`, `eSharp`, `supervisorCli`. They are not poked.
- **Web research reads; it posts nothing** and sends no private path, name or address to any service.

## Acceptance evidence

- `research-verdict.md`, committed before the blind answer was read: the three checks with dated sources; one ranked
  verdict with its recommendation and a falsifier; for ADOPT the named thing and its delta.
- The source table and `raw/prior-evidence.map.md`.
- The brief's send copy as checked and sent, its answer verbatim, and the list of differences.
- The auditor's RETURNs on the brief and on the verdict, with the lead's VERDICTs.
- Majkee's GO or STOP in `raw/decision.majkee.*.md`. On GO the verdict file is the founding reference of whatever
  opens next under L14; a REFUSE that he accepts ends the scope here, and that is a success of the gate.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L14 with the amendment of 2026-11-23; the locks above.
- `/home/hruzam/reposoma/raw.guides/runbook/res/research.md` — the research gate: three checks, three verdicts.
- `/home/hruzam/unikuklatrix/nablarva/meshup/seam.cross-vendor-relay.2026-08-05/raw/decisions.relay.2026-09-30.md`
- `/home/hruzam/unikuklatrix/nablarva/meshup/seam.cross-vendor-relay.2026-08-05/raw/seed.relay-research.2026-09-30.md`
- `/home/hruzam/unikuklatrix/nablarva/meshup/seam.cross-vendor-relay.2026-08-05/raw/brief.blind.relay-research.2026-09-30.md`
- `/home/hruzam/unikuklatrix/nablarva/meshup/seam.cross-vendor-relay.2026-08-05/DESIGN.md` and `HYPOTHESES.md` beside it.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/handoff.successor-stage.2026-11-26.md` — what the
  predecessor established and left open; its section 3 before poking anyone.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md` — the line ledger: open work, custody pointers.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md`
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/STATUS.md`
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/STATUS.md`
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/STATUS.md`
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/STATUS.md`
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` and `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md`

## What this session deliberately does not do

- No PTY research and no tracker draft — those are `relay-X3-pty` and `relay-X4-tracker`, after the verdict.
- No architecture: no design, no second blind brief, no lock.
- No probe, no sample, no qualification of a door; the open rows of `relay-X1-probes` stay in the line ledger.
- No retirement of the file-poke; if the verdict names a replacement, mapping its coverage is a later bed's work.

## Seat to wake

A fresh lead — @Flight in project-session mode, driven by Majkee, in the window `lead`: one head coordinating a
research child and resident seats of the other vendor toward one written verdict. The reasons and the alternative are
in the cold-start card. The operator wakes the seat.

## Provisional coordination carry-forward

- Shared coordination and retirement obligation: `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md`, §Carry-forward and retirement.
- Owning development line: `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md`; the shared bridge is tracked there.
- At closure, account for the provisional dependency in the ledger and the successor's references until its recorded replacement disposition.
