# B-entry fixtures — drafts, not active assignments

Owner: Cartan's POINT 02 engineering lane. Authority:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/02.oraculum.point.md`.
No fixture has been placed in the scratch workspace in this cycle. It stays empty, mode 700,
owned by `hruzam`. No target is opened, connected, armed or sent to.

## What this is

`qualification.point.draft.md` is a synthetic receiver test, **not** a new BUS file kind,
cycle, seat, runtime configuration or identity registry. `probe_codex` is a test-only label.
The real BUS seats remain `oraculum` and `cartan`; Cartan alone writes `02.cartan.return.md`.
Python is the disposable probe's explicitly authorized implementation language, not a gavel
on Nablarva's product-language docket.

The validator accepts a deliberately narrow **JSON-form YAML frontmatter** between `---`
fences. This lets a stdlib-only parser reject duplicate keys, unknown fields and nonfinite
numbers; it is not a general YAML parser or a changed BUS contract. Draft placeholders make
this particular file invalid for `PREPARED` until it is materialized and placed by an approved
later step. The ordinary Markdown body is part of the fixture hash.

## Fixed positive-fixture paths

| Purpose | Exact path |
|---|---|
| Workspace | `/tmp/nablarva-b-entry-20260913-01` |
| Materialized fixture | `/tmp/nablarva-b-entry-20260913-01/qualification.point.md` |
| Synthetic input | `/tmp/nablarva-b-entry-20260913-01/qualification.input.txt` |
| Receiver's only write | `/tmp/nablarva-b-entry-20260913-01/qualification.return.md` |

These future file paths do not authorize writes today. The absence check and empty directory
creation are the only scratch operations in POINT 02. Existing content or a symlink must
never be “fixed” by reuse/deletion. Other live test cases need separately approved distinct
fixtures and RETURN destinations; this version's validator supports only the fixed positive
paths, so changing that profile requires a reviewed change, not bypassing validation.

## Placement and ownership at a later arming

1. Oraculum audits the returned engineering and records its VERDICT. The missing native
   transport facts in `raw/route.r1.md` must be resolved before it releases a live read step.
   `PREPARED` and offline PASS are not arming or native qualification.
2. Oraculum's PAD distinguishes authorization to **open** the named scratch TUI from arming
   an already-open exact UUID/instance for inspection. Majkee must be able to grant the first
   before that UUID exists; no placeholder UUID may masquerade as `armed_target`.
3. Majkee opens/names/inspects the disposable session only when the head releases those
   actions. Oraculum records the exact native target and a separate approval scope, expiry
   and sitting identifier. No permission/model/provider/profile override is part of setup.
4. A later POINT explicitly authorizes Cartan, or its bounded engineering helper, to create
   the two input files at the exact paths. Cartan materializes a fresh challenge, observed
   native UUID and instance evidence, nonnegative integer generation, and SHA-256 of the
   final synthetic input bytes. The current string `{{GENERATION}}` becomes a JSON integer.
   The complete resulting fixture bytes are frozen and hashed **after** substitution.
5. The head places those hashes and the preview in the PAD. It releases exactly one send
   only after the native route, acknowledgement and admission/instance fences are proved
   and majkee separately approves that action. Only a path pointer travels through the
   approved native carrier. This probe revision has **no live send implementation**.
6. The receiver writes the test RETURN; Oraculum audits it. Tests, human actions, timing and
   any uncertainty land in the existing PAD report fences, not a second per-step ledger.

No placement, arming, config/hook install, proxy connection or native send is performed by
this README. Missing identity, unsafe defaults, failed validation or an existing RETURN
stops the step. Timeout/quietness/file absence does not clear a possibly submitted attempt.

## Validation tuple

The tuple is an explicit immutable **test preview**, not persistent binding state and not
an approval token. Exact fields; no aliases or unknown keys:

```json
{
  "schema": "nablarva-qualification-tuple/v1",
  "bed": "/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification",
  "seat": "probe_codex",
  "workspace": "/tmp/nablarva-b-entry-20260913-01",
  "thread_id": "{{THREAD_ID}}",
  "host": "hruzam-120922",
  "incarnation": "{{INCARNATION}}",
  "generation": "{{GENERATION}}",
  "fixture": "/tmp/nablarva-b-entry-20260913-01/qualification.point.md",
  "fixture_sha256": "{{FINAL_FIXTURE_SHA256}}",
  "input_path": "/tmp/nablarva-b-entry-20260913-01/qualification.input.txt",
  "input_sha256": "{{INPUT_SHA256}}",
  "return_to": "/tmp/nablarva-b-entry-20260913-01/qualification.return.md",
  "challenge": "{{CHALLENGE}}"
}
```

This example deliberately cannot pass validation. Every shared value must match the frozen
fixture, and its hash must match the actual final bytes. There is no self-hash field inside
the fixture. Neither a display name nor a copied generation/incarnation string proves a
native running instance; native qualification stays separate.

The first fixture's exact frontmatter fields are `schema`, `bed`, `from`, `to`, `scope`,
`done_when`, `workspace`, `thread_id`, `host`, `incarnation`, `generation`, `point_path`,
`input_path`, `return_to`, `input_sha256`, and `challenge`. `scope` and `done_when` must be
nonempty materialized strings. Canonical UUIDs, hashes, paths and generation types are checked
by `qualify.py`; symlink/escape/existing-destination rejection is part of the static check.
No race-free native admission claim follows from a static filesystem check.

## Offline verification and evidence limits

Runner, no bytecode files or temporary fixture directories:

```sh
python3 -B /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/test_qualify.py
```

Tests use in-memory filesystem/response/attempt doubles. Mock carrier-call counters check
local refusal, duplicate and restart handling; they are not native queue observations.
Every mock result is labeled `UNVERIFIED-native`. A guard modeled with callbacks is not
proof that the vendor offers an atomic idle/approval/incarnation guard.

The live `inspect` path remains fail-closed before connection because the permitted sources
have not established its transport contract. The reader's message/response logic can be
exercised offline, but no command in this cycle reads a live daemon or thread. See
`/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/route.r1.md`
before deriving any STEP 0c command. Default gate disposition remains STOP.
