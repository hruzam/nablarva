---
what: directive for the X1 head — Sublime view publisher (file shape)
by: Oraculum · Claude · direct main, operator majkee (session oraculum.sublime-vist, cwd ~/ia-sync, host home)
date: 2026-11-15
state: PROPOSAL — authoring material. Not a release, not a RUNBOOK, clears no gate, locks no canon.
line: sublime-observer · ledger ../../sublime-observer-X.ledger.md
predecessor: ../../termbrana-sublime-observer/ (X0 prototype; Cartan's bed and STATUS — do not edit)
companion: oraculum.handoff.2026-11-15.md (Oraculum · Codex — sandbox probes and reader needs)
---
# Directive — publish operator-shared Sublime views as files

Tags: **[obs]** observed by the named seat · **[said]** majkee in this session · **[prop]** my proposal.
Lock numbers (L…) were read from nablarva files by Houston (consult, 2026-11-15), not by me.

## 1. Governing insight

The observer is an editor pin held open. The operator's act of sharing a view is the
authorization; the editor then keeps a file copy of that view current; agents read files.
No socket, no client, no inventory — the privacy gap and the sandbox problem disappear with them.

## 2. Settled by majkee [said]

- File publication only. Socket, CLI client and MCP are dropped. Lite XL rejected; Sublime stays.
- Sharing in X1 is a toggle command in Sublime only. Path-prefix sharing is parked.
- Publish directory: fixed default under the user runtime directory, held in the plugin's settings.
- Plugin source is authored in nablarva. No zsh surface in X1.
- The prototype's socket CLI is retired (touches Cartan's X0 STATUS and the shared guide — at closure).
- Line name `sublime-observer`, generation X, ledger per line. It attaches to an organ later.
- Reuse the X0 capture function and tests; rebuild transport and scope.

## 3. Proposed file contract v1 [prop]

Readers get an absolute path. `XDG_RUNTIME_DIR` is unset in Codex's tool shell [obs: Oraculum·Codex],
so the guide states `/run/user/<uid>/sublime-observer/` literally.

```
<root>/                      dir 0700, files 0600
  publisher.json             contract_version, epoch, pid, sublime_build, plugin_python,
                             started_at, heartbeat_at
  index.json                 epoch, shared: [{share_id, path, title, window, view, buffer}]
  current -> views/<id>      exists ONLY when exactly one view is shared
  views/<share_id>/
    state.json               small; rewritten on every publish
    text.<revision>          immutable once written; current and previous kept
```

`state.json` carries: contract_version, epoch, seq, share_id, window, view, buffer, path, title,
dirty, loading, revision, captured_at, encoding, size_chars, text_file, published_chars, cap,
truncated, selections (a, b, empty, start/end row-col), visible_region, viewport_position,
viewport_extent, coordinate_units, and an explicit error/unsupported field.

Rules:

1. **Consistency.** State names the immutable text file it belongs to. A reader reads `state.json`,
   then exactly that `text.<revision>`; if it is gone, re-read state (bounded retries). No hashing.
   This answers the weakest point Codex named (text and state are not one atomic capture).
   Scrolling or caret moves rewrite state only; text is written when the revision changes.
2. **Atomic writes.** Temp file in the same directory, then rename.
3. **Bounded delay.** Trailing debounce plus a maximum delay, so continuous typing cannot starve
   publication. Starting values to measure, not law: 150 ms debounce, 1 s maximum.
4. **Triggers.** Text change, selection change, load completion, share/unshare, close. Sublime has
   no scroll event [obs: Epoch], so viewport is polled for shared views only.
5. **Liveness.** `epoch` is new on every plugin load. `heartbeat_at` is refreshed on a timer.
   A reader treats an old heartbeat as "publisher not live": the retained snapshot is history,
   never "current". Sequence numbers are never compared across epochs.
6. **Cleanup.** Unshare or close removes the view directory and its index entry. On load, the
   plugin removes residue of a dead epoch after confirming that pid is gone.
7. **One publisher per runtime directory.** A second instance that finds a live publisher does not
   publish and says so in the console.
8. **`current` never guesses.** Absent when zero or several views are shared.
9. **Cap.** 200,000 characters per text file, `truncated` explicit. Readers cannot recover omitted text.
10. **Visible grant.** A shared view shows a status-bar marker; the share is a new `share_id` each time.

## 4. Constraints (Houston consult: stretches, no break)

1. **Observation only, organ-local** (L20, L21, ARCHITECTURE §4.1). The directory is not the shared
   observation record and not a VIST envelope. Publishing never notifies, wakes or rings an agent.
   `subl file:line` is an actuator and is not a capability of this tool.
2. **Trust boundary** (L22 vault seals). Published files are readable by every same-user process;
   sharing is not per-agent isolation. The RUNBOOK must carry this before any build.
3. **Delivery** (SYNC_DISCIPLINE, L6, L8′). An `install-pkgs/<slug>.md` task in ia-sync, by copy into
   its own `Packages/<Name>/`, never a symlink into a bed, automation `manual` until qualified,
   hosts explicit. Do not use `editor-pin-sublime.md` as the header template (old form).
4. **No zsh surface in X1.** The path has one home: plugin settings, cited by README and guide.
5. **Naming sweep, routing only.** Sweep run 2026-11-15 [obs: me]: `sublime-observer` appears only in
   the X0 bed and `reposoma/raw.guides/sublime-observer/GUIDE.md`. The word "observer" also names
   Termbrana's Zellij observer — package and runtime directory names still need majkee's word.

## 5. Evidence carried in

- Codex 0.169.0, `workspace-write`: unix-socket `connect` under `/run/user/1000` is denied; listing
  and reading files there works; a 200,000-character file reads whole [obs: Oraculum·Codex].
- Claude Code: its sandbox can block unix sockets when the seccomp filter is present [Epoch, docs].
  A Claude read of a published file under the sandbox is NOT yet witnessed.
- Sublime stable is 4215; the plugin host moved from Python 3.8 to 3.14 in build 4205 [Epoch].
  The X0 plugin pins 3.8 and ran on 3.14.6 in the disposable 4215 profile. The live build on home
  and the host the pin selects there are unverified.
- X0 capture core: explicit ids, revision guard, selections, viewport; 13 unit and 16 real-editor
  checks in a disposable profile only [obs: X0 evidence files]. These do not qualify X1.

## 6. Proposed gate [prop]

> Majkee records GO or STOP on an independently verified home-host publisher: for operator-toggled
> synthetic views in the normal Sublime profile, a fresh Claude Code session and a fresh Codex
> session each read a consistent text-and-state capture by absolute path under their default
> sandboxes; unshared views publish nothing; unshare, close, restart and an editor crash leave no
> capture presented as current; focus, selection and scroll are unchanged by publishing; install
> and removal follow a reviewed `install-pkgs` task; the trust boundary and remaining limits are stated.

Checks the gate needs: unit tests for the contract (consistency, cap, cleanup, `current`), a
disposable-profile trial reusing the X0 harness, then the normal-profile witness with synthetic
views only, typing-latency measurement, and the two fresh-session reads.

## 7. Seats [prop]

- **Head:** a Claude head (Flight), because the Claude side is the less-proven one and the head
  must run probes. Oraculum authors the RUNBOOK and returns to counsel; it does not implement,
  review code or verify its own design.
- **Implement:** Trajectory. **Verify:** Assay, without the implementer's context.
- **Cross-runtime witness:** a fresh Codex session (HANDSHAKE: verified from the other runtime).
- **Closure:** Houston consult on the documentation diff; majkee gavels.

## 8. At closure, not before

Organ README · "planned producer" on the observe row of ARCHITECTURE §4 (owner stays unknown) ·
repointed shared guide · conditional pointer in `ia-sync/codex/AGENTS.md` (Cartan's surface) ·
one-line pointer to the line in the main nablarva documentation.
Do not write: a flag line, observe-seam ownership, VIST producer or shared-layer status, "Sublime is
the editor", or "installed".

## 9. Parked

Path-prefix sharing with a deny list · Claude and Codex native editor protocols (`/ide`; Codex's
names VS Code and Cursor) · a VIST-shaped record · a read helper for agents (earn it first).

## 10. Owed to majkee

1. X1 head, and the two grants: lift of the X0 "no live profile" hold for this bed, and the L21 release.
2. Package directory and runtime directory names.
3. Should the toggle refuse sealed paths (`.majkee/`, `.hlm/`, `.env*`) even on the operator's own act?
4. Plugin source directory inside nablarva (L18 leaves the parent open).
5. Flag line at closure, or none.

## Limits of this document

I ran no tests and no probes: this seat's Bash hook allows bookkeeping only. I read the X0 handoff,
README, STATUS, baseline evidence and both source files, the runbook guide, nablarva AGENTS.md and
pulse.md. Epoch, Trajectory, Houston and Oraculum·Codex findings are relayed, each from its own report.
