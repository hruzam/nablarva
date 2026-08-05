# Test Spec — Seam Probe: reading a live TUI across Tailscale
## Cloth to cloth — Nabla → Atlas. Peer register, not a command sheet.

_Authored 2026-08-01 by Nabla for @majkee to hand to Atlas (the bash-capable build)._
_Phase C. Read-only first. Write-back is gated (Stage 6) and opt-in._

---

## 0. What we're actually testing (clear — shared, not a secret)

Not "can you reach the box." That's plumbing. The real question:

> **Can you read a live CLI/TUI you did not author, on a remote machine, over Tailscale — and
> correctly separate what you SAW from what you INFERRED about its state?**

The gap between seen and inferred *is* the result. A run where you report only what was literally on
the screen, and mark every state-read as inference, is a success even if some inferences are wrong.
A run that blends them — that reports "gemini is waiting for input" as if it were seen when the
screen didn't say so — is the failure mode, regardless of whether the guess happened to be right.

Honesty beats coverage. If you can't do a stage, say so plainly and move on. A false "PASS" poisons
the whole report.

---

## 1. Fill these in first (parameters)

```
REMOTE_HOST=          # Tailscale MagicDNS name or 100.x.y.z of the target machine
SSH_USER=             # user on the remote box
TARGET=               # tmux target where the other agent runs: session:window.pane  (e.g. gem:0.0)
BRAID_LOG=            # OPTIONAL: path to the pipe-pane tee log on remote, if one exists (else leave empty)
```

Assumption to confirm or correct in your report: the remote agent (gemini-spawn) runs **inside a
tmux session**. If it does not, capture-pane won't see it — report that as a blocking finding and
stop; we redesign around a pipe-pane tee instead.

---

## 2. Observation discipline (the whole point — use these tags in the report)

- `[SEEN]` — literal bytes off the screen. Quote or paste them. No paraphrase.
- `[INFERRED]` — your read of what the state *means* (idle / generating / waiting-for-input /
  errored / finished). Always a separate line from the `[SEEN]` it rests on.
- `[BLIND]` — something you needed but could not observe. Name it; don't fill the hole with a guess.

If an inference has no `[SEEN]` under it, it is a hidden assertion — delete it or demote it to
`[BLIND]`.

---

## 3. Stage 1 — Reachability (plumbing; fast)

```bash
tailscale status | grep -i "$REMOTE_HOST"
tailscale ping --c 3 "$REMOTE_HOST"
ssh "$SSH_USER@$REMOTE_HOST" 'echo reachable; uname -n'
```
Report: reachable or not. If not, stop — everything downstream is void.

## 4. Stage 2 — Can you see the session at all

```bash
ssh "$SSH_USER@$REMOTE_HOST" 'tmux list-sessions; tmux list-panes -a -F "#{session_name}:#{window_index}.#{pane_index} #{pane_current_command}"'
```
Report `[SEEN]` the pane list. `[INFERRED]` which pane is the agent. If `$TARGET` isn't in the list,
correct it here before continuing.

## 5. Stage 3 — Capture the live screen (the core read)

Visible screen, then with scrollback:
```bash
ssh "$SSH_USER@$REMOTE_HOST" "tmux capture-pane -p -t $TARGET"
ssh "$SSH_USER@$REMOTE_HOST" "tmux capture-pane -p -S -200 -t $TARGET"   # last 200 lines of history
```
Report: `[SEEN]` paste the visible frame (truncate the scrollback to the last ~40 lines if long).
Then, and only then: `[INFERRED]` what is this agent doing? Cite which lines drove the inference.

## 6. Stage 4 — Motion (a single frame can't tell generating from waiting)

A static screen is ambiguous: waiting-for-input and finished look identical in one snapshot. Two
snapshots over time disambiguate. Pure bash, no helper needed:

```bash
for i in 1 2 3; do
  ssh "$SSH_USER@$REMOTE_HOST" "tmux capture-pane -p -t $TARGET" | md5sum
  sleep 2
done
```
Report: `[SEEN]` did the hash change across the three samples? `[INFERRED]` moving hash → actively
generating; stable hash → idle/waiting/finished (still ambiguous between those three — say so, don't
overclaim). This is the stage most likely to expose a seen/inferred blur; be strict here.

## 7. Stage 5 — Braid vs river (OPTIONAL; only if `BRAID_LOG` is set)

If a pipe-pane tee log exists, compare the live capture (river) against the persisted log (braid):
```bash
ssh "$SSH_USER@$REMOTE_HOST" "tail -n 40 '$BRAID_LOG'"
```
Report: does the tail of the braid match the tail of the live capture? A mismatch is not
necessarily a bug — the river moves faster than any single read — but a *large* divergence means the
tee isn't capturing what's on screen, which is a finding we need. `[INFERRED]` your read of whether
truth-on-disk tracks resonance-on-screen.

## 8. Stage 6 — Write-back (GATED — do NOT run unless @majkee says go in this session)

Read-only proves observation. Only after a clean read do we test whether you can *act* on the remote
surface. When cleared:
```bash
ssh "$SSH_USER@$REMOTE_HOST" "tmux send-keys -t $TARGET 'echo nabla-probe-$(date +%s)' Enter"
```
Then re-capture (Stage 3) and confirm your marker appears. Report `[SEEN]` the marker on screen —
that's the closed loop: you wrote, the remote surface changed, you observed your own effect. That is
the seam closing.

---

## 9. Report format (what you hand back)

Write to `report.seam-probe.2026-08-01.md`, append-only, this shape:

```
# Seam Probe — report
## env
- host / reachable: ...
- target pane / confirmed: ...
- braid log present: yes|no

## per stage
### Stage N — <name> — PASS | PARTIAL | FAIL | SKIPPED
[SEEN]     <literal>
[INFERRED] <your read, citing the seen lines>
[BLIND]    <what you needed and couldn't get>

## headline answer
"What is the remote agent doing right now?"
[SEEN]     ...
[INFERRED] ...

## honest failures
- <anything you faked-nothing, couldn't do, or are unsure of>

## verdict
- Can you read a live remote TUI over Tailscale and keep seen/inferred separate? yes | partial | no
- one line: what surprised you.
```

---

## 10. Self-audit before you call it done

1. Every `[INFERRED]` has a `[SEEN]` beneath it, or it's demoted to `[BLIND]`. No orphan inferences.
2. Nothing you guessed is written as if you saw it. Re-read once adversarially, hunting for that blur.
3. Stage 6 stays untouched unless explicitly cleared this session.

---
_The test isn't whether you're right about the remote state. It's whether you can tell me what you
saw without smuggling in what you assumed. Report the seam; don't paper over it._
