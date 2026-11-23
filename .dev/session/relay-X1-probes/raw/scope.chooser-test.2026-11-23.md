---
kind: scope of one further test in relay-X1-probes — a message that arrives by the carrier and meets an approval chooser a human must answer
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 1 — written from the auditor's facts (_bus/17.auditor.return.md, _bus/17.lead.verdict.md). Not challenged yet, not released. Nothing in it may be done before Majkee's release.
asked_for: Majkee, gate 3, H2 = A (raw/decision.majkee.gate-3.2026-11-23.md)
---

# The question

- **D1.** A message delivered by `codex queue` asks the receiver for a step that needs leave outside its working
  folder, and the receiver is set so that **a human reviews**. Does a chooser appear and stand? What do the record and
  the pane show while it stands? What does the human's one answer do to the turn?
- **D2 — its own row, released or not on its own.** A second `codex queue` message arrives **while the chooser of D1
  stands**. Does the carrier accept it? Does a turn start, wait, or is it lost? What becomes of it after the chooser is
  answered?

Each tried once. No verdict on the relay architecture, no door qualified, no exception to the death of send-keys
injection, nothing adopted.

# What is known before the test

- In C1 and C2 no human was asked because the reviewer was the program: `approvals_reviewer = "auto_review"` in the
  base configuration.
- The combination that should ask a human — `workspace-write`, `on-request`, reviewer `user` — was **never observed**.
  "No chooser appears" is therefore a possible result.
- What a queued message does while a chooser stands is not knowable without a try.

# The sample

- Fresh and disposable, in its own folder: `~/.cache/nablarva/relay-x1-samples/2026-11-23/sample-codex`, tmux window
  `sample-codex`, opened by Majkee's hand with
  `codex --sandbox workspace-write --ask-for-approval on-request -c 'approvals_reviewer="user"'`.
- The same standing instruction as in the first sample (a message that begins `NONCE:` gets a receipt file), typed by
  him.
- **Why isolated and not one of his working sessions:** the chooser depends on three settings, not on the folder; his
  working seats differ among themselves in exactly these settings (the auditor's own never asks). An isolated sample
  with the three values set by flag reproduces the one condition that matters and puts no working session at risk.

# Who does what

- **Majkee:** opens the sample, types the instruction, sits at it. When a chooser appears he leaves it untouched until
  the observer's second marker has been answered by the lead's send (D2) or, without D2, for 30 seconds; then he chooses
  **approve once** — never "always". He types nothing else into the sample.
- **Auditor — observer:** pre-check from the sample's record that the three effective values are as set — if the
  reviewer is not `user`, it says so and nothing is sent. One-second watch of record and pane as before; it is not told
  the nonces. It writes marker 1 (sample idle, watch running) and, for D2, marker 2 when a request for leave has stood
  unanswered for five seconds.
- **Lead — sender:** D1 by one armed shell command on marker 1, as in C1 and C2: the same message with a fresh nonce,
  the folder outside being a new one, `~/.cache/nablarva/relay-x1-samples/2026-11-23/approval-probe`. D2 by a second
  armed command on marker 2: a message with its own nonce that asks for the receipt only.
- No agent pastes or sends keys into any session. The only hand at the chooser is his.

# Stops

- The pre-check fails → nothing is sent.
- No request for leave within 60 seconds after D1's turn starts, or a request that is answered without a chooser →
  row "no chooser"; D2 is not sent.
- Any call whose outcome is unclear → UNCERTAIN, and nothing further. No retry, no second sample.
- He is called away while the chooser stands → he denies it; the row says so.

# What it will not show

A rate. A busy receiver other than one held at a chooser. What "deny" does (one answer per try, and this one is
"approve once"). What the granular default asks a human for. Anything about his working sessions.

# What the result is

A third packet with rows D1 and, if released, D2 — carrier result, native turn, receipt with the matching nonce, the
observer's confirmation, and what the chooser showed and for how long — for his GO or STOP.

# Choices the lead made in this draft — open to the challenger

1. Isolated sample with the three settings by flag, not a standard working session.
2. His one answer is "approve once", not "deny".
3. D2 is in, as its own row and its own release.
4. The chooser is held for 30 seconds, or until D2 is sent.
