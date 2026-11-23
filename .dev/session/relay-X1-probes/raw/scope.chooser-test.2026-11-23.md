---
kind: scope of one further test in relay-X1-probes — a message that arrives by the carrier and meets an approval chooser a human must answer
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 2 — FOR MAJKEE'S RELEASE. Written from the auditor's facts (_bus/17.*) and revised after Oraculum's challenge (REVISE — _bus/18.oraculum.return.md, _bus/18.lead.verdict.md). The revision was read by no second seat. Nothing in it may be done before his release, except the preparation named below, which starts nothing.
asked_for: Majkee, gate 3, H2 = A (raw/decision.majkee.gate-3.2026-11-23.md)
---

# The question — one row, D1, tried once

A message delivered by `codex queue` asks the receiver for a step that needs leave outside its working folder, and the
receiver is set so that **a human reviews**. Does a chooser appear on the screen? What do the record and the pane show
while it stands? What does his one answer do to the turn?

No verdict on the relay architecture, no door qualified, no exception to the death of send-keys injection, nothing
adopted.

# What is known before the test

- In C1 and C2 no human was asked because the reviewer was the program: `approvals_reviewer = "auto_review"` in his base
  configuration.
- The combination that should ask a human — sandbox `workspace-write`, approval `on-request`, reviewer `user` — was
  **never observed**. A request for leave is not yet a chooser: only the pane can show that one appeared. "No chooser"
  is a possible result.

# The sample

- Fresh, disposable, isolated: folder `~/.cache/nablarva/relay-x1-samples/2026-11-23/sample-codex`, empty but for
  `receipts/`; tmux window `sample-codex`.
- Started **by Majkee's hand** with one command:
  `tmux new-window -n sample-codex 'bash ~/.cache/nablarva/relay-x1-samples/2026-11-23/start-sample.sh'`
  The script changes into the sample's folder and starts `codex --sandbox workspace-write --ask-for-approval on-request
  -c 'approvals_reviewer="user"'` with the standing instruction as its first prompt (`instruction.txt` beside it). He
  types no instruction. If the program asks whether it trusts the folder, he says yes.
- The standing instruction allows the extra step: receipt first; one more step if the message asks for it, attempted
  once; permission asked and waited for; then stop.
- Isolated and not a working session, because the chooser depends on three settings, not on the folder, and his working
  seats differ in exactly these settings.

# Who does what, in order

1. **Prepared before he is called** (done at the time of this draft; it starts nothing): the folder, `receipts/`,
   `instruction.txt`, `start-sample.sh`.
2. **Majkee** runs the one command, sees the sample answer "instruction is in", and tells the lead the sample is up.
3. **Auditor — observer.** Pre-check from the sample's record: its working folder, the three effective values, and that
   the target folder lies outside its writable roots. If any is not as scoped, it says so and **nothing is sent**. Then
   its one-second watch of record and pane, and its marker: sample idle, watch running. It is not told the nonce.
4. **Lead — sender.** One armed shell command on the marker, as in C1 and C2: `codex queue`, without `--resume`, the
   message `NONCE:<value>` plus the request to create the folder
   `~/.cache/nablarva/relay-x1-samples/2026-11-23/approval-probe` and in it an empty file `<value>.txt`.
5. **Majkee at the sample.** When a chooser appears: count slowly to ten, then choose **deny — this once**. Nothing
   else is typed. If no chooser appears, he touches nothing; the lead tells him in its window when the try is over.
6. **Observer** closes its watch and reports. The chooser counts as witnessed when at least two consecutive captures
   show it with its choices.

No agent pastes or sends keys into any session. The only hand at the sample is his. His presence: about ten minutes.

# Stops

- The pre-check fails → nothing is sent.
- The carrier accepts but no turn starts within 30 seconds → "no turn"; nothing further.
- A turn runs but no chooser is on the screen within 60 seconds of its start — whether the request was refused by
  policy, reviewed by the program or never made → row "no chooser", with where it stopped; nothing further.
- Any call whose outcome is unclear → UNCERTAIN, and nothing further. No retry, no second sample.
- He is called away while a chooser stands → he denies it at once; the row says so.

# What it will not show

What "approve" does — the one answer of this try is "deny". What happens to a second message that arrives while a
chooser stands — taken out of this test on Oraculum's challenge; open work for the line, not released. A rate. What the
granular default asks a human for. Anything about his working sessions. A chooser shorter than two samples of a
one-second watch.

# What the result is

A third packet with row D1 — carrier result, native turn, receipt with the matching nonce, the observer's
confirmation, what the chooser showed and for how long, his answer and what the turn did with it, and that no file
exists outside — for his GO or STOP.
