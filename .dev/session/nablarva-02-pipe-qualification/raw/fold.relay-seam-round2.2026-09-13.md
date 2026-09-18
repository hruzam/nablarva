---
kind: head note — fold of an external consult into this bed's scope
author: oraculum (cSharp)
date: 2026-09-13
source: /home/hruzam/unikuklatrix/nablarva/meshup/a-symmetry-lightest/consult.relay-seam.round2.symmetry.2026-09-13.md (symmetry → asymmetry, relayed by majkee)
authority: none — observations for the practical project; anything that binds goes through POINT/RETURN/VERDICT or a majkee gavel
---

# Relay seam round 2 — what folds into nablarva-02, what parks, what collides

## 1. The one collision, named first

Symmetry §1: *"Codex transport: interactive CLI + tmux activation + file ack first; `codex queue`
/ MCP demoted to adapter internals."* Nablarva flag L4 records tmux send-keys injection as a
death, and this bed's RUNBOOK forbids send-keys of any kind. The two documents agree on the
contract (activation = one pointer line; content never rides transport; receipt = file) and
disagree only on the **order of actuators**. Nablarva's order is fixed by law: native first
(`codex queue`, app-server status) — that is this bed. If native fails, this gate STOPs, and
the seam's path-only doorbell becomes the candidate for a separate L4 gavel, with symmetry's
§3 "pointer, not payload" as its spec. Nothing in bed 02 changes; the STOP branch is now
pre-shaped. (The seam's "PTY = lowest-common actuator" stands as substrate, not architecture —
asymmetry §2 already said so.)

## 2. Folds into POINT 01 / the preflight (read-only, Codex side — symmetry §0)

- **Turn-complete signal.** Does installed Codex expose a turn-complete hook or `notify`
  program with a stable payload (thread id, turn id, last message)? Can it be configured
  workspace-locally for a disposable target without touching global config? If none: fallback
  is app-server `turn/completed` / `thread/read` status, then rollout mtime — in that order.
- **Rollout semantics.** Is the rollout JSONL append-only during a live run and the read path
  only on `resume`/`fork`? What happens to the file on resume (same file? rollover? new file
  with duplicated items — the false "new session" trap symmetry names for Claude)?
- **observe() = metadata only.** Existence · path · session id · mtime · rollover. Never record
  types or content. This is sharper than r1's `evidence_locator` and supersedes it in the
  build bed: transcript *pickup* (operator-signalled public-text read) stays a separate,
  labeled communication comparator; it is not `observe()`.

## 3. Folds into the qualification plan (P1–P3)

- **Consumption check = "expected RETURN exists at turn end."** Positive, checkable, cheap. On
  the disposable target: turn-complete signal (if it exists) → `test -f return_to` → present /
  absent. Absent at turn end is the ATTENTION condition, counted per endpoint.
- **Nudge stays operator-triggered in this bed.** Symmetry's "absent → nudge" is a second
  activation with the same pointer. r1's rule (no blind retry) is not violated by a nudge
  *after a completed turn with no receipt* — but automating it is unattended behavior, which
  bed 02 does not earn. Count nudges; a human fires them.
- **Reincarnation → binding `generation++`, never a BUS file.** Answer to symmetry §6: the
  transition lands in the host-local binding record (r1 already carries `generation`) and is
  retyped as a STATUS hold; `_bus/` gains no kind and no label. A stale generation invalidates
  every prepared preview and never resends.

## 4. Already decided on the practical side (for symmetry's §2 fork)

r1 §Correlation, approved GO 2026-09-12: *mission = the owning RUNBOOK path; no purpose
composer.* That is symmetry's position, taken for this build by the design gate. The
conceptual fork (lighthouse / coherence-homeostat) remains the seam thread's; nablarva does not
reopen it by analogy.

## 5. Parked (not this bed)

- Slice cast (`codex` = lead, `claude-code` = architect) — roles by runbook; nablarva already
  casts per bed; no seam primitive needed.
- Ommatermia "description-not-pixels" second sighting → canon candidate; separate thread.
- Unattended channels per endpoint after the relay count — after B and C, with policy.
- `brief.relay-seam.v2` → the a-symmetry thread's own deliverable; nablarva cites, does not author.

## 6. Vocabulary added for the GLOSS (when a sitting needs it)

`nudge` — a second activation carrying the same pointer after a completed turn produced no
receipt; counted per endpoint; human-fired in this bed.
`observe()` — metadata-only look at an endpoint's on-disk log: exists · path · id · mtime ·
rollover; never content.
