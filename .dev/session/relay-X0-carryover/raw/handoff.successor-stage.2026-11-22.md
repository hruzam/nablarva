---
kind: handoff — source material for the RUNBOOK of the successor stage (Majkee's proposed name `relay-X1-research`)
status: DRAFT 2 by the pen holder — revised after Houston's consult (verdict `stretches`, five constraints, all taken; _bus/16.houston.return.md). Not yet counter-read by Oraculum, not yet put to Majkee.
by: engineer (pen of relay-X0-carryover) · 2026-11-22 · host home
authority: Majkee — walkthrough T8 (placement left to the engineer; "Trajectory brings back the exact test scope before live sends begin"; handoff files against orphans) · walkthrough 2, S1 (one new real capture for U01) and S5 (placement agreed)
releases: NONE. This file proposes. Every operation that needs Majkee's release is listed in §6 on its own line. Nothing here opens a session.
base: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/   (relative paths start here)
---

# Handoff from `relay-X0-carryover` to the successor stage

## 0. What the successor is not (first lines of its RUNBOOK — Houston, constraint 1)

- It is **not** `relay-00-research`. That name stays reserved for the L14 D4 sequence, and this stage does not stand in for it.
- It gives **no verdict on the relay architecture**. Its packet is offered to `relay-00-research` as evidence input, nothing more.
- It **qualifies no door** — neither as a relay transport nor as the replacement for the file-poke. G7's three words (coverage,
  adoption, retirement) are not in its gate.
- Each result is recorded as **"tried once"**. It is not cited to reopen L4 (tmux send-keys injection, a recorded death) or
  L14 D1 (vendor doors parked) except through the flag's own route for new evidence, under Majkee's gavel.

## 1. What this bed established (pointers, not copies)

| Fact | Where |
|---|---|
| What the home trial of 2026-11-12/13 can and cannot support, checked four times by a non-author | `raw/export.vist-x0.engineer.2026-11-21.md` (rev 4) |
| Which doors exist per direction on today's versions, on paper; no door adopted | `raw/doors.inventory.2026-11-21.md` |
| U01's search of the trial captures: **MISSING** — only Claude's help panel and approval prompt were ever captured, and the registry names both | `goals/G4.u01-unknown-view-fixture.md` (rev 4) · `_bus/11–13.engineer.verdict.md` |
| Three signature sets exist — r1 `428ef2a`, r2 `22d5008`, archived `094de33` (812 bytes, sha256 `ae9d5266…`); the last two have the same rules | `_bus/12.engineer.verdict.md` |
| The generic rule calls every Claude screen with the footer `Esc to cancel` a "dialog"; the matcher looks at Claude panes only | `goals/G4…` · `_bus/12.engineer.verdict.md` |
| Both capture folders and the U01 working files are in private custody on home, outside Git | `../relay-X.ledger.md` (two custody entries) |
| Coordination practice of one night, as observation only: 20 pokes by `codex queue` (p01, p03–p21), every call accepted and each followed by its RETURN or a pushed ref; 5 look-first pastes into Claude panes, 4 submitted, 1 staged with Enter returning 0 and no submit (r06, cause unknown) | `raw/pokes.log.md` |
| Hazards found: a word after `claude` starts an agent; a list of forbidden git verbs is read as "no git"; a POINT that asks for one word gets one word | `raw/incident.stray-claude-session.2026-11-21.md` · `exp/` |
| Majkee's decisions, verbatim | `raw/decision.majkee.*.md` (six files) |
| Lock fit of this handoff — Houston, card consult, verdict `stretches` | `_bus/16.houston.return.md` |

## 2. Open work that leaves this bed

| Item | State | Goes to the successor as |
|---|---|---|
| **G8 — live door probes** (`goals/G8.door-probes-live.md`, rev 1) | not released | its first work, with the scope in §3 |
| **U01 — one new real capture** (Majkee, S1: "taking b") | chosen, not released | planned operation, §4 |
| **G6 — U02, the exit race** (`goals/G6.u02-exit-race.md`, rev 3) | parked by Majkee (T8) | parked. It needs a carrier where text and submit are two steps, and isolation. The tmux tries of §3 may show whether that seam can be observed; r06 is one unexplained event at exactly that seam. A scoped proposal comes back to Majkee before anything runs. |
| **G7 — retire the file-poke** (`goals/G7.retire-file-poke.md`, rev 3) | tracked (T8) | tracked, outside the successor's gate (§0). The file-poke stays in use under its rules. A bed that qualifies a replacement maps what it covers and returns for three separate words: coverage, adoption, retirement. |
| **G5 — receiver contract for U03–U06** (`goals/G5.receiver-policy-contract.md`, rev 2) | not started; paper only | paper work. A contract for expiry, recipient, authority and hops is easier to write once §3 has shown what a receiver can observe. **Proposal** — it moves; Majkee may keep it here instead. |
| **G10 — friendly reminder** | deferred by Majkee (T6) | not the successor's. It belongs to the session-window helper group, which gets its own lead (S5). Pointer only: `goals/G10.friendly-reminder.md`, `raw/decision.majkee.walkthrough.2026-11-21.md` T6. |
| **G0 — the umbrella sentence** | confirmed (T3) | the umbrella of the line; the successor inherits it. |

Nothing else is open. G2, G3 and G4 are done; G9 ends with this session; G1 is this party's housekeeping and the roster is the successor's starting list (`raw/roster.2026-11-21.md`, rev 5 — re-read against live tmux).

## 3. Exact test scope for the live probes (G8) — proposed

**Aim.** One controlled try per door and direction on today's versions, so that the inventory's "candidate" becomes "tried once,
with this result". These are activations and deliveries, each under its own release (§6). They qualify no door and adopt none.

**Receivers — two disposable samples, nothing else.** `sample-claude` and `sample-codex`, each in its own new tmux window, started
in a new empty scratch folder outside every repository, default permission mode, the cheapest model. No party pane is ever a
target. Each sample is given one standing instruction at start — an input of its own, listed in §6: *when a message carries
`NONCE:<value>`, write the value and the UTC time into `<scratch>/receipts/<value>.txt` and do nothing else.*

**Senders.** The engineer for Claude-origin tries, the controller for Codex-origin tries. In tries 3–5 an **agent** operates the
tmux push. L17 calls tmux push a human-operated carrier "until separately qualified", so each of those three release lines says
in words that an agent sends, once, under that release.

**Observer** — the auditor, who is neither sender nor receiver and only reads: timestamped bottom rows of the sample pane before
and after, the sample's own session record for the native turn, and the receipt file.

**The tries — seven at most, one each, in this order**

| # | Door (inventory code) | From → to | Why it is in | Precondition; otherwise NOT RUN |
|---|---|---|---|---|
| 1 | `codex queue --thread <uuid> --message` (LQ) | engineer → sample-codex | the door this line used all night; never tried with an outside observer | the sample's thread id is read from its own footer |
| 2 | the same (LQ) | controller → sample-codex | a Codex-origin receipt is unknown | as try 1 |
| 3 | tmux look-first paste, then Enter (PT) | controller → sample-claude | the reply bell; r06 failed here once | empty input row, no dialog, agent in the foreground |
| 4 | the same (PT) | engineer → sample-claude | Claude-origin, as p02 | as try 3 |
| 5 | the same (PT) | controller → sample-codex | historically 0 of 3 on an old version; unknown today | as try 3 |
| 6 | Claude `SendMessage` | engineer → sample-claude | documented native peer messaging; one receiver-side report only | first show, without sending, that the tool exists in the sender and that an independent tmux-hosted session can be addressed at all |
| 7 | `mcp__codex_tui__send_message_to_thread` | controller → sample-codex | documented tool; home once answered "active writer" | the tool is enabled in the sender |

For each try: a fresh nonce written to a POINT first; one carrier call with UTC before and after and the exit code; then the
result per layer — carrier result · native turn seen · receipt with the same nonce · observer's confirmation.

**State probes ride along, read-only, no send.** During the tries the observer also records what `~/.claude/sessions/<pid>.json`
(allowlisted keys, never the socket path) and `tmux display-message` say about the sample, against what the pane shows.
`claude agents --json` is included **only** if `claude --help` on the day lists `agents` as a subcommand; a word after `claude`
that is not a subcommand is a prompt and starts an agent. If it is not listed, that probe is NOT RUN.

**NOT RUN in this scope, with the reason** — App Server `turn/start` / `turn/steer` (a second writer on a live thread; binding
unknown) · `codex exec resume` and `claude -p --resume` (they start their own process; same-owner behaviour unknown; the startup
hazard) · Claude Channels (needs a configured channel and eligibility) · a script post to the Claude inbox socket (no public
payload contract) · agent-view reply (needs a managed background session) · the `asyncRewake` hook (installing a hook is
implementation) · the unknown "delivery worker" of 2026-11-12 (mechanism never inspected).

**Stops.** An uncertain result ends that door: it is recorded UNCERTAIN, with no retry and no switch to another carrier. A dialog on
a sample ends the run until Majkee's hand clears it. Any process nobody started ends the run and becomes an incident note. A try
whose precondition is unknown is NOT RUN, not FAIL.

**Side effects.** Receipt files and the observer's captures in the scratch folder; the two samples' own session records, which stay
on the host. Nothing is installed, no setting is changed, no hook is added. The samples are closed at the end by the hand that
started them.

## 4. The new U01 capture — proposed

Majkee chose one new real capture (S1). The search showed what it must be: a **native control of Claude that carries neither
`Do you want to proceed?` nor `Esc to cancel` in its bottom six rows**. Which control that is must be found by looking on the
day, on today's CLI version; nobody should assume it from memory.

- **Where:** on `sample-claude` from §3, so nothing private is on screen.
- **Who opens the control:** Majkee, by his own hand. If he would rather have the exec desk type it, that is an agent acting on a
  pane and has its own release line in §6 (Houston, constraint 4).
- **Registry:** frozen before the capture — the archived set `094de33`, sha256 `ae9d5266…`.
- **Capture:** the observer takes the frame and a sidecar with the twelve fields the trial used, three times — before, with the
  control open, after it is closed — plus `claude --version` at that moment and a note that no agent typed anything. The observer
  only reads.
- **Label:** a seat that did not pick the control labels the frame against the frozen registry, without the selector's opinion.
  The labeller only reads.

**The classification the matrix row asks for is not settled, and this handoff proposes no method.** The row wants one read-only
classification, at most 5 seconds, compared with what an independent observer saw. Two ways exist, and each has a cost:
- *The archived helper in its dry mode* (`VIST_DRY=1` — resolve and observe, no send). I read its source: it classifies a **live
  pane**, not a file, and it needs the old resolver set-up. Running it is reactivating archived adapter code, which G8's bounds
  rule out for the probes; for U01 it would need its own release and its own argument.
- *The frozen patterns applied to the captured file by the documented rule* (bottom six non-blank rows, first match), as in this
  bed's cycle 12. It touches no pane and runs no archived code, but it is a literal comparison, not the classifier.

Draft 1 of this file said "with the archived helper, offline, on the file". That was wrong: the helper cannot read a file. The
successor proposes the method and Majkee releases it as its own line.

A Codex control would be a weaker fixture, because the matcher ignores Codex panes altogether.

## 5. Locks this touches — Houston's finding, card consult, 2026-11-22: `stretches`

The move holds if the constraints are honoured. All five are taken into this draft.

| Lock | Finding | Where it landed |
|---|---|---|
| **L14 D4** — research sequence, `relay-00-research` first | an X stage may carry the probes without bypassing the sequence only if it says it is not `relay-00-research`, gives no architecture verdict, offers its packet as evidence input only, and qualifies no door | §0, §7 |
| **L14 D1** (vendor doors parked) · **L4** (tmux send-keys injection, a recorded death) | a one-shot measurement fits — parked is not forbidden, and measuring a death does not revive it; results are "tried once" and reopen nothing | §0, §3 |
| **L17** — tmux push is a human-operated carrier until separately qualified | tries 3–5 are sent by agents; each release line must say so | §3, §6 |
| **L21** — each activation and delivery needs its own release | one line per try; the sample's standing instruction is an input of its own | §6 |
| **L20** — observation, decision and action are separate | the tries are deliveries, not observations; the observations they produce authorize nothing. Opening the U01 control is an action — Majkee's hand, or its own release line. Observer and labeller only read. | §3, §4, §6 |
| **L22**, **L12** | unchanged — vaults sealed; plain pull and push on `core` | — |

Houston did not check, and says so: `decisions.relay.2026-09-30`, `docs/ARCHITECTURE.md`, whether the archived classifier counts
as the adapter code G8 forbids (taken up in §4), and whether L14's "session relay" covers coordination between agent seats —
he assumes it does, because the ledger merges coordination into the relay line.

## 6. What Majkee would have to release — one line each, none implied by another

1. Opening the successor bed: its slug (`relay-X1-research` is his proposal), its pen, its gate.
2. Starting `sample-claude`: who launches it, in which scratch folder, with which model. Trust dialogs are his hand.
3. Starting `sample-codex`: the same.
4. The standing NONCE instruction typed into each sample at start — one input per sample.
5. Try 1 — `codex queue`, engineer → sample-codex.
6. Try 2 — `codex queue`, controller → sample-codex.
7. Try 3 — tmux paste then Enter, **an agent (the controller) sends**, → sample-claude.
8. Try 4 — tmux paste then Enter, **an agent (the engineer) sends**, → sample-claude.
9. Try 5 — tmux paste then Enter, **an agent (the controller) sends**, → sample-codex.
10. Try 6 — Claude `SendMessage`, engineer → sample-claude.
11. Try 7 — the Codex TUI message tool, controller → sample-codex.
12. The U01 capture of §4, with the control opened by Majkee's own hand.
13. Only if he wants it instead of 12's "own hand": the exec desk types the command that opens the control.
14. One classification for U01, by a method the successor proposes (§4).
15. Closing the samples, and keeping or deleting their session records.

G6 and G7 ask for nothing now. He may release any subset; a try that is not released is NOT RUN.

## 7. Proposed gate for the successor (Majkee sets the real one when he opens it)

> Majkee records GO or STOP on a witnessed probe packet: for each released door one row with the carrier result, the native turn,
> the receipt with the matching nonce and the observer's confirmation, or NOT RUN with its reason; and one independently labelled
> genuine unknown-view fixture for U01. Every result stands as "tried once". The packet gives no verdict on the relay
> architecture, qualifies no door as a transport or as a replacement for the file-poke, adopts nothing, and is evidence input
> for `relay-00-research` only.

## 8. Team — proposal only

A **new** pen for the successor, started from the cold-start card and this file: this pen has been through more than one context
reset in one bed. The controller, the auditor as observer and the exec desk can carry over. If Majkee wants the same pen to
continue, the handoff still works; the cost is the context.

## 9. What stays behind

`relay-X0-carryover` closes when Majkee has recorded GO or STOP on this handoff. Its files stay where they are; the successor reads
them by path. The private custody folders stay on home; the line ledger points at them.
