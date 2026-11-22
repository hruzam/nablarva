---
kind: handoff — source material for the RUNBOOK of the successor stage (Majkee's proposed name `relay-X1-research`)
status: DRAFT 1 by the pen holder. Not yet read by Houston (lock fit), not yet counter-read by Oraculum, not yet put to Majkee.
by: engineer (pen of relay-X0-carryover) · 2026-11-22 · host home
authority: Majkee — walkthrough T8 (placement left to the engineer; "Trajectory brings back the exact test scope before live sends begin"; handoff files against orphans) · walkthrough 2, S1 (one new real capture for U01) and S5 (placement agreed)
releases: NONE. This file proposes. Every operation that needs Majkee's release is listed in §6 on its own line. Nothing here opens a session.
base: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/   (relative paths start here)
---

# Handoff from `relay-X0-carryover` to the successor stage

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

## 2. Open work that leaves this bed

| Item | State | Goes to the successor as |
|---|---|---|
| **G8 — live door probes** (`goals/G8.door-probes-live.md`, rev 1) | not released | its first work, with the scope in §3 |
| **U01 — one new real capture** (Majkee, S1: "taking b") | chosen, not released | planned operation, §4 |
| **G6 — U02, the exit race** (`goals/G6.u02-exit-race.md`, rev 3) | parked by Majkee (T8) | parked. It needs a carrier where text and submit are two steps, and isolation. The tmux probes of §3 may show whether that seam can be observed; r06 is one unexplained event at exactly that seam. A scoped proposal comes back to Majkee before anything runs. |
| **G7 — retire the file-poke** (`goals/G7.retire-file-poke.md`, rev 3) | tracked (T8) | tracked. The file-poke stays in use under its rules. The bed that qualifies a replacement maps what it covers and returns for three separate words: coverage, adoption, retirement. |
| **G5 — receiver contract for U03–U06** (`goals/G5.receiver-policy-contract.md`, rev 2) | not started; paper only | paper work. A contract for expiry, recipient, authority and hops is easier to write once §3 has shown what a receiver can observe. **Proposal** — it moves; Majkee may keep it here instead. |
| **G10 — friendly reminder** | deferred by Majkee (T6) | not the successor's. It belongs to the session-window helper group, which gets its own lead (S5). Pointer only: `goals/G10.friendly-reminder.md`, `raw/decision.majkee.walkthrough.2026-11-21.md` T6. |
| **G0 — the umbrella sentence** | confirmed (T3) | the umbrella of the line; the successor inherits it. |

Nothing else is open. G2, G3 and G4 are done; G9 ends with this session; G1 is this party's housekeeping and the roster is the successor's starting list (`raw/roster.2026-11-21.md`, rev 5 — re-read against live tmux).

## 3. Exact test scope for the live probes (G8) — proposed

**Aim.** One controlled try per door and direction on today's versions, so that the inventory's "candidate" becomes "tried once,
with this result". It qualifies no door and adopts none.

**Receivers — two disposable samples, nothing else.** `sample-claude` and `sample-codex`, each in its own new tmux window, started
in a new empty scratch folder outside every repository, default permission mode, the cheapest model. No party pane is ever a
target. Each sample gets one standing instruction at start: *when a message carries `NONCE:<value>`, write the value and the UTC
time into `<scratch>/receipts/<value>.txt` and do nothing else.*

**Senders.** The engineer for Claude-origin tries, the controller for Codex-origin tries. **Observer** — the auditor, who is neither
sender nor receiver: timestamped bottom rows of the sample pane before and after, the sample's own session record for the native
turn, and the receipt file.

**The tries — seven at most, one each, in this order**

| # | Door (inventory code) | From → to | Why it is in |
|---|---|---|---|
| 1 | `codex queue --thread <uuid> --message` (LQ) | engineer → sample-codex | the door this line used all night; never tried with an outside observer |
| 2 | the same (LQ) | controller → sample-codex | a Codex-origin receipt is unknown |
| 3 | tmux look-first paste, then Enter (PT) | controller → sample-claude | the reply bell; r06 failed here once |
| 4 | the same (PT) | engineer → sample-claude | Claude-origin, as p02 |
| 5 | the same (PT) | controller → sample-codex | historically 0 of 3 on an old version; unknown today |
| 6 | Claude `SendMessage` | engineer → sample-claude | documented native peer messaging; one receiver-side report only |
| 7 | `mcp__codex_tui__send_message_to_thread` | controller → sample-codex | documented tool; home once answered "active writer" |

For each try: a fresh nonce written to a POINT first; one carrier call with UTC before and after and the exit code; then the
result per layer — carrier result · native turn seen · receipt with the same nonce · observer's confirmation.

**State probes ride along, read-only, no send:** during tries 1–7 the observer also records what `~/.claude/sessions/<pid>.json`
(allowlisted keys, never the socket path), `claude agents --json` and `tmux display-message` say about the sample, against what
the pane shows.

**NOT RUN in this scope, with the reason** — App Server `turn/start` / `turn/steer` (a second writer on a live thread; binding
unknown) · `codex exec resume` and `claude -p --resume` (they start their own process; same-owner behaviour unknown; the startup
hazard) · Claude Channels (needs a configured channel and eligibility) · a script post to the Claude inbox socket (no public
payload contract) · agent-view reply (needs a managed background session) · the `asyncRewake` hook (installing a hook is
implementation) · the unknown "delivery worker" of 2026-11-12 (mechanism never inspected).

**Stops.** An uncertain result ends that door: it is recorded UNCERTAIN, with no retry and no switch to another carrier. A dialog on
a sample ends the run until Majkee's hand clears it. Any process nobody started ends the run and becomes an incident note. A try
whose prerequisite is unknown is NOT RUN, not FAIL.

**Side effects.** Receipt files and the observer's captures in the scratch folder; the two samples' own session records, which stay
on the host. Nothing is installed, no setting is changed, no hook is added. The samples are closed at the end by the hand that
started them.

## 4. The new U01 capture — proposed

Majkee chose one new real capture (S1). The search showed what it must be: a **native control of Claude that carries neither
`Do you want to proceed?` nor `Esc to cancel` in its bottom six rows**. Which control that is must be found by looking on the
day, on today's CLI version; nobody should assume it from memory.

- **Where:** on `sample-claude` from §3, so nothing private is on screen.
- **Who opens the control:** Majkee's hand, or the exec desk on his word. It is operator input, not an agent actuator.
- **Registry:** frozen before the capture — the archived set `094de33`, sha256 `ae9d5266…`.
- **Capture:** the observer takes the frame and a sidecar with the twelve fields the trial used, three times — before, with the
  control open, after it is closed — plus `claude --version` at that moment and a note that no agent typed anything.
- **Label:** a seat that did not pick the control labels the frame against the frozen registry, without the selector's opinion.
- **Then, as a separate release:** one read-only classification of the captured file with the archived helper, offline, at most
  5 seconds — the matrix row asks for it. Expected result: unknown. It runs on the file, never on a live pane.

A Codex control would be a weaker fixture, because the matcher ignores Codex panes altogether.

## 5. Locks this touches — questions put to Houston before Majkee sees this

- **L14 D4** maps the relay research to `relay-00-research` (verdict gate) first. The line ledger says new experimental routing
  does not bypass that sequence "when the work falls under it". *Do one-shot probes that adopt nothing fall under it?*
- **L14 D1** makes PTY the base layer and parks vendor doors (`codex queue`, Claude channels, ACP) as weather. **L4** records
  "tmux send-keys injection" as a death. Tries 1, 2, 6 and 7 touch vendor doors; tries 3–5 touch the recorded death. *Is measuring
  what the line already uses provisionally consistent with those locks, and under which limits?*
- **L20** — everything in §3 and §4 is observation; observations authorize nothing.
- **L21** — each activation and each delivery needs its own release; §6 lists them one by one.
- **L22**, **L12** — unchanged: vaults sealed; plain pull and push on `core`.

## 6. What Majkee would have to release — one line each, none implied by another

1. Opening the successor bed: its slug (`relay-X1-research` is his proposal), its pen, its gate.
2. Starting the two samples: who launches them, in which scratch folder, with which model. Trust dialogs are his hand.
3. The tries of §3 — all seven, or the ones he names.
4. The U01 capture of §4.
5. The one offline classification of §4.
6. Closing the samples and keeping or deleting their session records.

G6 and G7 ask for nothing now.

## 7. Proposed gate for the successor (Majkee sets the real one when he opens it)

> Majkee records GO or STOP on a witnessed probe packet: for each released door one row with the carrier result, the native turn,
> the receipt with the matching nonce and the observer's confirmation, or NOT RUN with its reason; and one independently labelled
> genuine unknown-view fixture for U01 with one offline classification result. No door is adopted and no transport is implemented.

## 8. Team — proposal only

A **new** pen for the successor, started from the cold-start card and this file: this pen has been through more than one context
reset in one bed. The controller, the auditor as observer and the exec desk can carry over. If Majkee wants the same pen to
continue, the handoff still works; the cost is the context.

## 9. What stays behind

`relay-X0-carryover` closes when Majkee has recorded GO or STOP on this handoff. Its files stay where they are; the successor reads
them by path. The private custody folders stay on home; the line ledger points at them.
