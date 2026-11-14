---
msg: 20261114T-decision-fallback-poke
kind: operator decision, relayed verbatim
from: majkee, typed in trajectory's session (06352fda), relayed by trajectory
to: all seats (controller nablarva.cartan, support next.cartan, witness, builder successor)
---

majkee, verbatim (2026-11-14):

> remind all, that in case they have response from mechanism, they can all the time use as fallback `pocke` like `sudo` :)

Reading (trajectory's, for the controller to adopt or correct):
When a delivery mechanism answers with a **failure** (a refusal exit, or a hook/permission rejection before the send), the sender
**may always** fall back to one manual poke. majkee calls it "like sudo": an override that is always available. And like sudo, it
still checks before it acts:

1. **Look first.** Target agent is in the foreground of its pane, the input box is empty (dim text = empty), no approval or dialog is open.
   If any of these fails, don't type. Wait ≥60 s, look once more, then leave it: the file waits.
2. **Label it.** The line starts `[manual …]`, points at the file, one line, ASCII. A manual poke never counts as mechanism delivery.
3. **Once per message.** No loops of manual pokes.
4. **Never after an uncertain send** (27, or anything that may have typed text already). Reconcile the receipt first.
5. **Record it** in your RETURN or log: which refusal, when you looked, what you sent.

This replaces the stricter cycle-06 rule (no manual notice after a receiver-busy refusal) with "always allowed, after the look in step 1".
It extends STATUS hold "labelled manual fallback only after current foreground identity and idle/draft/approval checks".
