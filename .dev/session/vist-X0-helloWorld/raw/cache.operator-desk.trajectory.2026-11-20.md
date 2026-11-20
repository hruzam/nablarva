---
kind: dated-operator-desk-context-cache
date: '2026-11-20'
author: trajectory (Claude, operator desk, session 06352fda, host home)
source_revision: ec090ec (nablarva core)
authority: Historical context and source map only. STATUS.md remains the sole doing-state and the controller's
  pen decides whether this file is committed. No new pen, roster, gate, release or next-action authority.
inputs: transcript audit by @vector 2026-11-15 (13 orphans, 3 compaction summaries), re-checked against disk 2026-11-20
---

# Operator desk — what the next desk needs

## Position (read STATUS, do not trust this)
- Pen: nablarva.cartan since 810cf1d; moved to office 2026-11-19 by transcript, same identity
  (`raw/cache.controller-office.nablarva-cartan.2026-11-19.md`).
- Witness moved to office the same way (`raw/witness.host-move.2026-11-19.md`).
- STATUS `operator_desk` still names Trajectory 06352fda on **home**, successor unbound. If majkee now works from
  office, the desk binding is stale. Moving it is majkee's word, then the controller's STATUS edit.
- Only open VIST gate: majkee ACCEPT / REVISE / STOP on the reviewed documentary packet
  (`raw/preparation.review-input.01.2026-11-14.json`, hashes unchanged per STATUS 11-19).

## Do not resume the wrong session
- `b0080cc2-e56d-4244-86a9-b88660720e63` is an idle ia-sync spare, NOT the trajectory successor. A compaction
  summary called it the successor. The successor is a fresh Claude in nablarva per
  `~/reposoma/_cold-start/card/CS.trajectory-successor.vist.2026-11-14.md`, started only when the controller asks
  for a builder.

## Carried rules
- Fallback poke like sudo: `raw/decision.majkee.fallback-poke.2026-11-14.md`. Look first, label `[manual …]`, once,
  never after an uncertain send, record it. Whether it applies to the witness is still open (witness note).
- Never retry: t03 and `~/.local/state/vist/sent/c08r1-05-ae3ee8e7` (home host-local state).
- Doors: `codex queue --thread <uuid> --message "<one line>"` (queued ≠ read); into a Claude window only look-first
  manual paste as three separate tmux calls. Shared file-poke chapter now: `~/reposoma/raw.guides/bus/res/file-poke.md`.

## Owed decisions (majkee)
1. RUNBOOK packet: ACCEPT / REVISE / STOP (above).
2. `git push` runs without prompt for every seat in ia-sync and nablarva on all three hosts
   (`.claude/settings.local.json`, merged 2026-11-14). "Only the controller pushes" is unenforced; the desk broke it
   twice (therapy Arc 6). Keep, or restore the prompt except for the controller.
3. Witness hook extras beyond the brief (`-L <name>`, short aliases): not yet ruled on (witness note).
4. helper-utils-00-tmux: parallel with VIST or after (asked 11-14, unanswered). Its handoff lives in ia-sync, not here.

## Outside this bed (placed elsewhere)
- ia-sync hygiene (tracked `_mail/*/archive` files, settings-merge journal entry): `~/ia-sync/journal.host-cleanup.md`.
- helper-utils ids and first prompt: `~/ia-sync/.dev/session/helper-utils-00-tmux/raw/handoff.senior-advice.trajectory.2026-11-14.md`.
- Desk re-entry card: `~/reposoma/_cold-start/card/CS.trajectory-operator-desk.2026-11-20.md` (if majkee approves).

## Uncommitted by the desk
- `raw/decision.majkee.witness.2026-11-14.md` (majkee's "witness can hand the hook repair to delta" block; repair done
  in ia-sync 23f15e0). Controller excluded it as foreign; commit or drop is the controller's call.
- reposoma `raw.therapy/trajectory/therapy.md` (Arc 6) and `.majkee/journal/raw.2026-11-13.md` §1.2–1.5 (never
  committed by this seat).
