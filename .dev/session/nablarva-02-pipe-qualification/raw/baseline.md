---
kind: measurement protocol + log — the manual relay baseline
author: oraculum (cSharp); operator-reported numbers transcribed verbatim
date: 2026-09-13
authority: none — an instrument definition and its readings; no law; feeds VERDICT 02 and the qualification VERDICT
---

# Baseline — how one manual carry is counted

**Why.** r1's acceptance test and the seam's hardest brake say: no savings claim without a
hand-counted manual baseline. Two chances (bed 01 POINT 01; bed 02 POINT 02) passed unmeasured. The next real carry
— **POINT 03 of this bed** — is the remeasure, sat with `pad.1-baseline-carry.md`. Events are defined here *before* it happens so the
count is not a reconstruction.

**Unit.** One deliberate human action = 1. Repetitions count (two pastes = 2). Model/tool work is
not human labor and is not counted. Waiting is not an action; its duration is noted separately.

## Sender side — majkee (report in chat, any order, phone clock is fine)

| id | event | count when | also note |
|---|---|---|---|
| S1 | NOTICE | the moment you learn a POINT is waiting | source: oraculum chat / STATUS / Cartan said · time |
| S2 | LOCATE | each time you look for or open the exact path | — |
| S3 | COPY | each copy of the path to clipboard | — |
| S4 | SWITCH | each change of window/app/phone-screen to reach the target session | — |
| S5 | PASTE | each paste into the target | — |
| S6 | SUBMIT | each Enter/send | — |
| S7 | EXPLAIN | each extra message typed beyond the one carry line | rough word count |
| S8 | NOTICE-RETURN | the moment you learn the RETURN exists | source · time |
| S9 | RELAY-BACK | each switch + message to tell the head | — |
| W | WAIT | not counted | told→RETURN duration if you know it |
| X1–X6 | noise · [TAB] loop marker · pause · resume · stop · rewind | lifecycle marks, not actions | defined in `../res/skills/stenograph/skill.stenograph.md` (majkee's instrument; authoritative for the log format) |

Categories (r1): S1–S9 above are **routine carriage**. Anything you did to *set up* (open a
session, name it) is **setup** — none expected this carry. Any repeat because something went
wrong is **recovery** — count it under its S-id and say "recovery".

**Pull path.** If Cartan opens the bed on its own clock and reads the POINT before you paste
anything, report exactly that: `pull · S1 <time> · S8 <time> · S9 n` — a near-zero sender count
is a valid and useful reading, not a failed measurement.

## Recipient side — cartan (in the measured cycle's RETURN §3, timestamps from `date -Iseconds`)

| id | event | note |
|---|---|---|
| R1 | TOLD | how you learned of the POINT (operator paste · own bed read · other) · time |
| R2 | READ | first read of the POINT · time |
| R3 | CLARIFY | each question you had to ask a human before working · what was missing |
| R4 | WORK | start · end (model work; not human labor) |
| R5 | RETURN | written · time |
| R6 | TELL | how majkee learned the RETURN exists · time |

## Instrument checks (never readings)

### Rehearsal · 2026-09-14 · mobile · `human-relay-time-logs/rehearsal.mobile.telemetry.2026-09-14.md`

40 lines, no timestamps (the listener did not log time; majkee will say times aloud next time).
Totals by ID: S1 1 · S2 5 · S3 5 · S4 10 · S5 2 · S6 3 · S7 1 · S8 1 · S9 0 · W 1 · ? 10 · X5 1 —
all `phone`. What it checked: the log form works; `?` lines capture real recovery paths
(Tailscale drop, lost buffer, Cartan stuck on a bash confirmation) and narrated durations
("15 s per copy", "2–15 min per reply"). What it found about the instrument: **switching app
windows on the phone ends the voice regime** — live voicing during a phone carry is not
possible; the PAD now prescribes step-then-voice-with-time or PC carry with phone recorder.
Nothing here is a count of a real carry.

## Readings

### Exchange: bed 02 · cycle 03 (POINT 03 carry) — the remeasure

sender (majkee): REAL · pc · 13:57–15:08 · `human-relay-time-logs/stenograph.real.pc.2026-09-14.md` (stenograph via ChatGPT voice, ptyra; 106 lines).
Totals verbatim from the log: S1 0 · S2 8 · S3 6 · S4 14 · S5 3 · S6 18 · S7 17 · S8 10 · S9 3 · W 7 (not counted) · ? 20 · X1–X6 0 → **99 actions, all pc**. The log covers the whole living workflow of that hour (this bed's carry + a parallel reincarnation arc with a second Oraculum, Trajectory and a new Cartan), not only this exchange.
Head segmentation of the POINT 03 exchange (a proposal drawn from the log's own lines and times — not the instrument's output):
- carry leg 13:57–14:04: S4 13:57 · S2 13:59 (read Oraculum output) · S2 14:01 (scroll for the forgotten prompt) · S7 14:01 (ask Oraculum for it; recovery of the head's omission) · S6 14:03 · S8 14:03 (prompt arrives) · S3 14:03 · S4 14:03 · S5 14:03 · S6 14:04 (Cartan starts) → **10 actions, of which 4 are recovery of a forgotten prompt; the carry proper is 5** (S2·S3·S4·S5·S6).
- return leg 14:04–14:57: partial-reply relays (S8·S3·S9 at --:-- and 14:23), Cartan check-ins (S4 14:13 · S4/W 14:21 · S4+S2 14:52 · S4 14:55), bash-approval S6 (~14:22; matches Cartan's R3 sample 14:23:15), final notice S8 14:55 + S3 + S3 recovery (copy failed once) + S9 14:57 + S6 14:57 → **≈19 actions + 4 W**.
- measurement overhead attributable to the head's own instruction: S7+S6 15:03 ("relay still being recorded") → 2 actions.
told→RETURN: submit 14:04 (Cartan R1 sample 14:04:15) → Cartan seal 14:39:27 → **noticed 14:55 (16 min notice lag; no native notification inside tmux)** → relayed 14:57.
Findings the log carries beyond the count: (a) a forgotten prompt in the head's previous answer cost 4 actions and 4 minutes; (b) Codex approval prompts inside tmux are not surfaced — the operator polls by eye (S4/S2 at 14:13, 14:21, 14:52, 14:55) — this is the ATTENTION plane's missing signal, measured; (c) long head outputs cost reading time (`?` "reading" lines at 13:59, 14:07, 14:13); (d) the copy from tmux failed once (S3 recovery 14:55).
recipient (cartan), verbatim from RETURN 03 §3 (clock samples, +02:00): R1 TOLD — operator supplied the exact POINT 03 carry in the user message (paste, not pull); first sample after receipt 2026-09-14T14:04:15 · R2 READ — first read of the POINT from disk by 14:04:32 · R3 CLARIFY — 0 human questions before work (one sandbox permission prompt for the test's own fake socket, after work began; not a sender event) · R4 WORK — 14:04:32 → 14:39:27 (model/tool work incl. review and permission wait) · R5 RETURN — first file creation bracketed by two samples both 14:34:39; final seal 14:39:27 · R6 TELL — notice emitted via the session's output then the copyable @oraculum handoff; sample 14:39:27 (not an observed human read)
told→RETURN: told 14:04 → sealed 14:39:27 (≈35 min model work) → noticed 14:55 → relayed 14:57 — ≈53 min end to end, of which ≈16 min is notice lag

### Exchange: bed 02 · cycle 02 (POINT 02 carry) — not measured on the sender side

sender (majkee): `unknown` — the instrument was defined after this carry; not estimated
recipient (cartan), verbatim from RETURN 02 §3 (2026-09-14): R1 TOLD — operator-pasted carry in the current user message, receipt time unknown · R2 READ — opened the exact POINT from disk before task actions, time unknown · R3 CLARIFY — 0 questions to a human before working · R4 WORK — start unknown; end unknown · R5 RETURN — first file creation between two `date -Iseconds` readings both 2026-09-14T00:02:56+02:00 · R6 TELL — planned: final copyable absolute-path notice to majkee; time unknown
told→RETURN: unknown

### Exchange: bed 01 · cycle 01 (POINT 01) — missed

sender: `unknown` (not reported; Cartan's RETURN observed no path paste — pull path likely)
recipient: RETURN 01 §3 of bed 01 (one generic resume instruction; located POINT via bed; one
non-blocking clarification asked; timing not established)
