---
{
  "schema": "nablarva-qualification-fixture/v1",
  "bed": "/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification",
  "from": "oraculum",
  "to": "probe_codex",
  "scope": "Read only this fixture and its one synthetic input; compute SHA-256 of the input bytes; create exactly one correlated test RETURN at return_to; no other task effects.",
  "done_when": "The exact new RETURN contains the fixture SHA-256, challenge, observed native conversation id, input SHA-256, commands and outcomes, and exact destination; any mismatch or existing destination is refused without overwrite.",
  "workspace": "/tmp/nablarva-b-entry-20260913-01",
  "thread_id": "{{THREAD_ID}}",
  "host": "hruzam-120922",
  "incarnation": "{{INCARNATION}}",
  "generation": "{{GENERATION}}",
  "point_path": "/tmp/nablarva-b-entry-20260913-01/qualification.point.md",
  "input_path": "/tmp/nablarva-b-entry-20260913-01/qualification.input.txt",
  "return_to": "/tmp/nablarva-b-entry-20260913-01/qualification.return.md",
  "input_sha256": "{{INPUT_SHA256}}",
  "challenge": "{{CHALLENGE}}"
}
---

# Disposable qualification fixture — DRAFT, do not execute

This is a test fixture, not Nablarva BUS cycle traffic, not POINT 02, and not permission to
act as Cartan. It is deliberately unmaterialized and unplaced. Follow the placement and
arming boundary in the adjacent README. A path pointing to this draft is not activation.

When an explicitly authorized later sitting supplies the materialized fixture at `point_path`:

1. Resolve the native conversation identifier from your own runtime's non-secret identity
   surface; compare it with `thread_id`. Your test label is `probe_codex`, not a BUS seat.
   Check the exact workspace, host, paths and approved target context. Unknown or mismatch:
   report refusal in the native UI, write nothing, and wait for the operator. Do not infer
   identity from a filename, title or supplied challenge. Do not invent an incarnation proof.
2. Refuse if any placeholder remains, the input or fixture path differs, or `return_to` already
   exists, including a symlink/dangling symlink. Never overwrite, remove or redirect an existing
   file. An absent file does not authorize retry of an earlier attempt.
3. Read the exact fixture and `input_path` only. Compute SHA-256 of their actual bytes with
   ordinary local tools; report the exact commands and outcomes. Compare the input digest
   with `input_sha256`. Report the fresh challenge exactly. Do not modify either input.
4. Create the single test RETURN at `return_to`, with these facts: materialized fixture path
   and SHA-256; challenge; observed native conversation ID; input path and SHA-256; performed
   commands/results; exact destination; mismatches/uncertainty (`none` only when true).
   Do not claim your own result accepted. If the result cannot be produced under inherited
   permissions, report the obstacle without changing permissions or the usage path.
5. Finish in the native UI. No further task, retry, nudge, helper, background process, network
   access, transcript read/edit, repository write, configuration change or cross-session send.

Only the receiver may write the test RETURN. Cartan and Oraculum may independently inspect
it under the later sitting's authority; they must not author a substitute response. Oraculum
alone audits and advances the real session state. A file present at turn end is availability,
not acceptance or automatic completion of the real BUS cycle.
