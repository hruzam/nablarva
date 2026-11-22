---
kind: decision walkthrough sheet 2 — what to put to Majkee, one theme at a time
by: engineer (pen of relay-X0-carryover) · 2026-11-22 · host home
for: the exec desk (cycle 14) and Majkee
rule: every line here is a pointer or a summary of a file in this bed. Where it matters, open the file named under "Files". This sheet decides nothing and releases nothing. "Engineer's view" is marked as such and is only a view.
order: as numbered. S1 first, because S2 and S3 lean on it. S2 is the only theme where waiting can lose something.
not_a_theme: pushes — settled by Majkee on 2026-11-22 (raw/decision.majkee.push.2026-11-22.md).
base: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/   (all relative paths below start here)
---

# Decisions owed by Majkee — five themes, one question each

## S1 — U01 has its result: MISSING. What follows?
- **Context:** the read-only search you released is finished. In the 61 screens captured by the two trial runs of 2026-11-13 there
  is no genuine unknown native view. The only native controls in them are Claude's help panel and Claude's approval prompt, and the
  signature set in force since the second run names both. Cartan gave a verdict for each of twelve groups of frames; the auditor
  then labelled, without seeing Cartan's files, the 46 frames that carry no signature text, and agrees on all 46. So the trial
  never met an unknown screen, and "unknown stays unknown" is still untested.
- **Three ways on:**
  - **(a) Leave it.** U01 stays an open, untested case and is carried to the next stage in the handoff file.
    *Buys:* nothing new is started. *Cost:* none. *Consequence:* a build could be chosen without the observer ever having been
    shown a screen it does not know.
  - **(b) One new real capture.** On a disposable sample session, bring up one native control the signature set does not name,
    capture it with its sidecar, the CLI version and a record that nothing was typed, and have it labelled independently.
    *Buys:* a genuine fixture; U01 becomes testable. *Cost:* it starts a session and takes a capture — an activation under L21, so
    it needs your release, and trust dialogs are your hand. *Consequence:* it fits beside the live door probes in the successor
    stage, where disposable sessions are set up anyway. The search narrowed what such a control must be: any Claude screen with
    the footer `Esc to cancel` already counts as a registered "dialog", so the fixture must be a control without that footer, or a
    Codex control — the matcher looks at Claude panes only.
  - **(c) Simulated shapes — your idea from T5.** Helpers build synthetic unknown screens.
    *Buys:* cheap, no session, quick; it can exercise a classifier. *Cost:* the X0 matrix calls a synthetic view invalid for
    qualifying U01, so it would be a separate test with its own label. *Consequence:* useful as a build-time test later; it does
    not answer U01.
- **Engineer's view:** (b), inside the successor stage together with the door probes — not in this bed and not tonight. (c) only
  later, as a test of a classifier once one is being built.
- **Ask (one answer):** (a), (b), (c), a combination, or not yet?
- **Files:** `goals/G4.u01-unknown-view-fixture.md` (rev 4, the result) · `raw/u01.fixture-selection.2026-11-22.md` ·
  `_bus/13.engineer.verdict.md`

## S2 — The rest of the captures in /tmp
- **Context:** private custody holds the eight pinned C04 inputs you were asked about in T2. The two folders hold 171 files,
  264 KB together. The other 163 exist only in memory-backed `/tmp` — among them the 61 screens U01 just judged, their sidecars,
  the two driver scripts and the receipts. The host has been up since 2026-09-29.
- **Buys:** *copy all* — the U01 result can be checked again later; the r1 help frames, which are the evidence of the known C10
  failure and the nearest miss, are kept; a later classifier test has real frames. *Let go* — nothing more to keep safe.
- **Cost:** copy — private screen captures go into the same private place as the eight (host-local, 0700/0600, never Git). The
  custody tool copies only the eight pinned files, so the whole folders need a plain copy with a hash manifest; a few minutes for
  the controller.
- **Consequences:** let go — after the next reboot nobody can re-check U01's labels or look at the C10 frames again. The written
  result stays.
- **Engineer's view:** copy. It is 264 KB and it is the evidence under a result that is one hour old.
- **Ask (one answer, then one more only if the first is "copy"):** copy all of both folders, or let them go? If copy — may the
  controller do it on the engineer's assignment?
- **Files:** `goals/G9.custody-and-handoff.md` (rev 4, the limit is named there) · `scripts/c04-custody.py`

## S3 — The gate of this bed
- **Context:** after you accepted the planning baseline, the engineer drafted the next gate, marked provisional: *"Majkee records
  GO or STOP on what follows U01: an independently labelled result for X0-U01 (one genuine unknown native view selected from the
  released capture folders, or MISSING with what was searched), together with the engineer's placement of the live door probes
  and their exact test scope. No live send, new capture, door adoption or successor bed is implied until he answers."*
  It has two halves. The U01 result is here now (S1). The test scope for the live probes is not written yet; the engineer owes it
  together with a handoff file.
- **Buys:** a confirmed gate fixes this bed's next stop in your words.
- **Cost:** none.
- **Consequences:** if S1 is answered tonight, the first half is used up and the gate waits only for the test scope. Rewriting
  replaces the engineer's words with yours.
- **Ask (one answer):** confirm the wording, rewrite it, or leave it provisional until the test scope arrives?
- **Files:** `STATUS.md` (`gate:`, `gate_progress:`) · `../pulse.md` (row `relay-X0-carryover`)

## S4 — The tmux `monitor-silence` one-liner (left open in T6)
- **Context:** tmux can flag a window that has printed nothing for a chosen number of seconds — a mark in the status bar, no
  script. It is off on home. In T6 this part got no clear answer. It only says "this window was quiet"; it cannot tell an idle
  agent from one that waits for you. Your T6 direction — a chess clock in the helper window — stands either way.
- **Buys:** a cheap hint for the time before a clock exists.
- **Cost:** none. One line you set yourself. It will also flag windows that are quiet for good reason.
- **Ask (one answer):** do you want it — yes (the engineer writes the exact line into the answer file for you to set), or no?
- **Files:** `raw/answer.majkee.reminder-and-leftovers.2026-11-21.md` · `goals/G10.friendly-reminder.md`

## S5 — Two calls the engineer made where you left them to her (for your information; change them if you disagree)
- **Context:** in T8 you left the placement of the live door probes to the engineer, and in T9 and T11 you asked whether she can
  coordinate a second working group.
  1. **Live probes.** They leave this bed and go to a successor research stage — your proposed name `relay-X1-research` — with
     the exit-race case (G6) parked beside them. Reasons: they are the first work that activates and delivers, so they should
     stand under their own gate; what is left in this bed is paper and read-only; and this pen has been through more than one
     context reset. Only you open a session, so nothing is opened. The engineer first owes a handoff file, the exact test scope
     and a Houston consult on how the probes sit with lock L14.
  2. **Second working group.** She should not head the session-window helper group beside relay — one pen cannot keep two lines'
     state honestly. That group needs its own head; she can hand over what this bed learned about panes and pokes.
- **Buys:** you know both calls and can turn either around before work builds on it.
- **Cost:** none.
- **Ask (one answer for each):** call 1 — agree, or change? Call 2 — agree, or change?
- **Files:** `STATUS.md` (`decided_by_engineer:`)
