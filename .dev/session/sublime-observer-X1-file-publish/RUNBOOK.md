# RUNBOOK: sublime-observer-X1-file-publish

```yaml
goal: >
  CLI agents of either vendor read the live state of Sublime views the operator has
  explicitly shared, as plain files, with no socket, client or inventory.
gate: >
  Majkee records GO or STOP on an independently verified home-host publisher. For
  operator-toggled synthetic views in the normal Sublime profile, a fresh Claude Code
  session and a fresh Codex session each read a consistent text-and-state capture by
  absolute path under their default sandboxes; unshared views publish nothing; unshare,
  close, restart and an editor crash leave no capture presented as current; focus,
  selection and scroll are unchanged by publishing; install and removal follow a reviewed
  install-pkgs task; the trust boundary and remaining limits are stated.
participant_1: [oraculum, {brand: claude, model: fable-5.2, effort: high}, host: home, role: head and status_owner]
participant_2: [trajectory, {brand: claude, model: agent definition, effort: agent definition}, host: home, role: implementer spawned in-window by the head]
participant_3: [assay, {brand: claude, model: agent definition, effort: agent definition}, host: home, role: in-window verifier without implementer context]
participant_4: [codex-auditor, {brand: codex, model: operator choice, effort: operator choice}, host: home, role: cross-runtime auditor and fresh-session reader, instrument: mail]
participant_5: [majkee, {brand: human, model: none, effort: none}, host: home, role: toggles sharing in live Sublime, carries mail to Codex, gavels]
status_owner: oraculum
schema_note: runbook GUIDE as read 2026-11-15 (file dated 2026-11-05) · status GUIDE verified 2026-09-05
observations_read: none exist
amended: >-
  2026-11-15 by the head, on majkee's word the same day and Houston's second consult
  (raw/houston.consult-source-home.2026-11-15.md): source home and heartbeat added to Fixed
  facts; prompt-1 build scope moved; one-source constraint added; "organ README" corrected to
  "component README". Goal, gate and participants are unchanged.
```

## Why this session exists

The X0 prototype (socket plus CLI) proved the capture core but cannot be reached from a
sandboxed Codex session, lists every open view, and has no durable home. X1 rebuilds
transport and scope as operator-shared file publication and qualifies it on the real host
for both vendors. It crosses a trust boundary and touches the operator's live editor, so it
earns a gate.

## Fixed facts

- Decisions by majkee, 2026-11-15: file publication only; toggle-only sharing; publish
  directory fixed under the user runtime directory and held in plugin settings; plugin source
  authored in nablarva; no zsh surface; X0 socket CLI to be retired; Sublime stays (Lite XL rejected).
- Grants by majkee, 2026-11-15, for this bed only: the X0 hold "no live Sublime plugin changes"
  is lifted for the X1 publisher; the separate release that flag L21 requires for implementing
  a transport is given for this organ-local file publication. Neither grant makes it a shared layer.
- Names: Sublime package `SublimeObserver`; runtime directory `/run/user/<uid>/sublime-observer/`.
- said: majkee, 2026-11-15 — the source home of this one body is
  `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/`: `README.md`, the payload in
  `SublimeObserver/` (exactly what install copies), tests in `tests/`. This settles the parent
  folder for this body only (flag L18 leaves it open). The line stays unattached; being in
  `toolbox/` makes it neither an organ nor a toolbox.
- said: majkee, 2026-11-15 — heartbeat interval 1 s, so a reader's stale bound is 3 s.
- Design and file contract: `raw/oraculum-claude.directive.2026-11-15.md` §3. It is a proposal;
  the head may refine it, and every refinement lands in the component README at closure.
- Reader needs and Codex sandbox probes: `raw/oraculum.handoff.2026-11-15.md`.
- Head choice: Oraculum stays as head because it holds the design and three consult returns;
  it implements nothing and closes no gate of its own. Recorded reason: majkee's assignment.

## prompt-0 — oraculum (head)

```text
You are the head and sole STATUS writer of
/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/ .
Read RUNBOOK.md once, then STATUS.md, then raw/oraculum-claude.directive.2026-11-15.md and
raw/oraculum.handoff.2026-11-15.md. Advance the gate one verified step at a time:
contract tests and plugin in the bed's implementation/ → disposable-profile trial →
source home and install-pkgs task → normal-profile witness with majkee's hands →
cross-runtime audit → closure diff. Spawn trajectory to build and assay to verify; never
write code, never verify your own design, never mark the gate. Rewrite STATUS before any
externally visible action and after every verified step. A probe your Bash hook refuses is
delegated, not skipped. Return to majkee for every decision listed under holds.
```

## prompt-1 — trajectory (implementer, spawned by the head)

```text
Source of the package and its tests: /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/
(SublimeObserver/ is the payload, tests/ beside it). Build there only. Evidence and your handoff
note go to /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/implementation/
(evidence/ and NOTE.trajectory.md); the package and tests copies left in that bed are frozen
and are not edited. Contract: raw/oraculum-claude.directive.2026-11-15.md §3 in that bed.
Never edit the X0 bed termbrana-sublime-observer. Synthetic buffers only; a disposable portable
Sublime profile only, unless the head's brief says otherwise. No install into
~/.config/sublime-text, no git stage or commit, no change in ~/ia-sync. Done when the head's
stated checks pass and you return files changed, commands and outcomes, evidence paths,
mismatches and remaining uncertainty.
```

## prompt-2 — assay (verifier, spawned by the head)

```text
Verify the stated task against the bed at
/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/ and the source at
/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/ using only the head's task text and
the implementer's handoff note. Run the declared tests. Return PASS or FAIL with evidence.
Fix nothing.
```

## prompt-3 — codex-auditor (carried by majkee, by path)

```text
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/RUNBOOK.md,
STATUS.md and the POINT file named to you under _bus/. Act as an independent auditor in a fresh
Codex session under your default sandbox: read the published files by absolute path, audit the
contract and the implementation against the POINT, and write your RETURN to the exact path the
POINT names. Change nothing else. Never read an unshared or non-synthetic view.
```

## Known constraints + destructive holds

- Trust boundary (flag L22): published files are readable by every same-user process; sharing is
  not per-agent isolation. Until majkee says otherwise, the toggle refuses paths inside operator
  vaults (`.majkee/`, `.hlm/`) and `.env*` files.
- Observation only (flag L20, L17): publishing never notifies, wakes or rings an agent; no control
  function; `subl file:line` is not a capability of this tool; no inventory of unshared views.
- Organ-local (flag L21): the directory is not the shared observation record and not a VIST envelope.
- One source: `toolbox/sublime-observer/` is the only source once its copy is verified. The
  payload folder holds nothing but what is installed; tests, reader, fakes and trial fixture
  stay outside it. The bed keeps evidence.
- Durable text cites this bed only by commit pin, never by a live path, and never says
  "installed", "organ", "Sublime is the editor", VIST producer or shared layer.
- Synthetic views only for every test and witness. Never read private transcript caches.
- Live profile: nothing is installed before an `install-pkgs` task in `~/ia-sync` is reviewed by
  majkee; install by copy of the payload into `Packages/SublimeObserver/`, never a symlink;
  `hosts: home`, `automation: manual`; no public package name claim (Package Control);
  existing packages (`SFTP`, `Terminal`, `User`, editor pin) are never modified.
- `~/ia-sync` changes follow `SYNC_DISCIPLINE.md`; `ia-sync/codex/` is Cartan's surface.
- The X0 bed, its STATUS and the termbrana-M0 session are not edited. The pin queue
  `~/.wires/pins.jsonl` is not read or consumed.
- No git stage, commit or push by any agent seat; majkee commits.
- `docs/ARCHITECTURE.md` is under edit by `architecture-X1-bookkeeping`; any change there is
  coordinated through majkee and happens at closure only.

## Acceptance evidence

- Contract unit tests and a disposable-profile trial report in the bed, verified by assay.
- A normal-profile witness on home with synthetic views: share, read, unshare, close, restart, crash.
- One read from a fresh Claude Code session and one from a fresh Codex session, sandbox defaults.
- A Codex audit RETURN and the head's VERDICT under `_bus/`.
- The reviewed `install-pkgs` task and a demonstrated removal.
- Houston consult on the closure documentation diff returning fits or stretches with no break.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X.ledger.md` — line ledger
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — locks L6, L8′, L9′, L17, L18, L20, L21, L22
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-sublime-observer/` — X0 prototype, nablarva@059b060
- `/home/hruzam/ia-sync/SYNC_DISCIPLINE.md` and `/home/hruzam/ia-sync/install-pkgs/README.md` — delivery
- `/home/hruzam/ia-sync/HANDSHAKE.md` — cross-runtime delivery rule
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` — POINT, RETURN, VERDICT files
- `/home/hruzam/reposoma/raw.guides/runbook/res/token-economy.md` — in-window delegation (DRAFT)
- `/home/hruzam/reposoma/raw.guides/sublime-observer/GUIDE.md` — shared guide, repointed at closure

## What this session deliberately does not do

- Path-prefix sharing, a read helper, native editor protocols (`/ide`), a VIST-shaped record.
- Any host other than home. Office and monitor are later siblings on this line.
- Attaching the line to an organ, a flag line, or ownership of the observe seam.
- A general toolbox-module definition, a shared installer, or registry publication.
- Editing or closing the X0 bed, or changing the termbrana-M0 session.
