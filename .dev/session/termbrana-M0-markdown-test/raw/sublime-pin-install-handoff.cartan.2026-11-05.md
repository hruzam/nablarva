---
title: Sublime pin installation and source map
date: 2026-11-05
author: Cartan
status: observed; handoff only
session: termbrana-M0-markdown-test
scope: local home host · applications-in-common · ia-sync install-pkgs
---

# Sublime pin installation and source map

This is a reader handoff for the Sublime/editor-pin material relevant to the M0
Markdown transcript-view experiment. It records where the source, installer recipe,
machine-local state and live installation can be inspected. It does not change the
installation or claim a new product decision.

## Bottom line

The Sublime pin plugin is installed on the home host. The live plugin files and merged
keymap match the current `applications-in-common` source byte-for-byte. The runner's
bookkeeping is behind: `installed.json` records `sublime-keymap` as version `1.2`, while
the task recipe declares `1.3`. The task is manual, so `run.sh update` does not overwrite
the keymap automatically.

## Reader route

Read these in order:

1. [Plugin overview](../../../../../../www/elements-factory/applications-in-common/experiments/editor-pin-sublime/README.md) — purpose, files, commands, pin claiming and operational cautions.
2. [Canonical source keymap](../../../../../../www/elements-factory/applications-in-common/experiments/editor-pin-sublime/Default.sublime-keymap) — the bindings copied into Sublime.
3. [Pin core](../../../../../../www/elements-factory/applications-in-common/experiments/editor-pin-sublime/pin_core.py) — pin construction and JSONL serialization.
4. [Sublime install recipe](../../../../../../ia-sync/install-pkgs/editor-pin-sublime.md) — plugin deployment and `~/.wires` setup.
5. [Merged keymap task](../../../../../../ia-sync/install-pkgs/sublime-keymap.md) — current version, host scope, manual-install rationale and verification.
6. [Install runner](../../../../../../ia-sync/install-pkgs/run.sh) — how `list`, `update`, `mark` and per-machine state work.
7. [Local runner state](../../../../../../.local/state/ia-sync/installed.json) — home-host bookkeeping; machine-local and intentionally not synced.

The relative links above are convenient from this handoff; the absolute paths are:

```text
/home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/
/home/hruzam/ia-sync/install-pkgs/
/home/hruzam/.local/state/ia-sync/installed.json
```

## What the installed feature does

Sublime commands create structured pins containing editor location/context for agent
consumption. The global store is:

```text
~/.wires/pins.jsonl
```

The plugin is a zero-build Python plugin. The keymap also combines the pin bindings with
Markdown preview, navigation, build and numpad bindings. `claim-pins.sh` consumes pins
for a project scope; inspect its README before using it because claiming is destructive
to the unclaimed queue for that scope.

## Observed home-host state

Observed read-only on 2026-11-05:

| Surface | Observation |
|---|---|
| `~/.config/sublime-text/Packages/User/editor_pin.py` | Exists; SHA-256 matches source. |
| `~/.config/sublime-text/Packages/User/pin_core.py` | Exists; SHA-256 matches source. |
| `~/.config/sublime-text/Packages/User/Default (Linux).sublime-keymap` | Exists; `cmp` with source succeeds. |
| `~/.wires/pins.jsonl` | Exists; current pin data is machine-local. Contents were not copied into this handoff. |
| `~/.local/state/ia-sync/installed.json` | Records `sublime-keymap` version `1.2`, timestamp `2026-08-07T04:48:20Z`. |
| current task recipe | Declares `sublime-keymap` version `1.3`, `home office`, `manual`. |

Source/live hashes checked:

```text
editor_pin.py  5bce360a1d4cc36d9783fb92aea9bebc0ddb1a13644575dc6a915c43f9dc648c
pin_core.py    4ab00de8ac353af4942035dca4f1574372a241d052418ead259c3215d4b092d3
```

The source keymap and live keymap are byte-identical. Therefore the stale runner state
does not currently imply stale installed bytes.

## How `run.sh update` relates to this

`run.sh` identifies this host as `home`, reads task metadata, and keeps state in
`~/.local/state/ia-sync/installed.json`. For `automation: manual` tasks it runs the
check block, prints the recipe, and waits for the operator to perform/merge the change
and then run:

```bash
bash /home/hruzam/ia-sync/install-pkgs/run.sh mark sublime-keymap
```

That is why `bash /home/hruzam/ia-sync/install-pkgs/run.sh update` is not sufficient
evidence that the keymap was copied. The live-file comparison is the stronger evidence.

The older `editor-pin-sublime.md` recipe describes the plugin deployment, but its header
uses `developed-on` and `install-on` rather than the runner's current `version`, `hosts`
and `automation` fields. Consequently the current runner reports that task as not
applicable rather than as an installed task. The actual installed plugin files are still
verified against source.

## Relevant history / why the keymap changed

The source repository commit `54b51a3` (`sublime key updates`, 2026-08-07) changed the
merged keymap. The recipe records these reasons:

- Markdown preview moved to the working GitHub parser path because the local parser
  failed inside Sublime's Python environment.
- `ctrl+r` was restored to Goto Symbol, with `ctrl+shift+r` retained as an alias.
- Numpad bindings were added as protection against NumLock/Wayland behavior.
- The task remains manual because a plain keymap copy can overwrite local bindings.

## What this gives the M0 transcript-view work

The existing Sublime pin path is a usable editor-side delivery surface for a generated
Markdown transcript, but it does not by itself prove transcript identity or stable
history resolution. A future M0 probe should keep these separate:

- Sublime pin: editor location and context for the rendered file.
- Transcript identity: vendor, project, session ID and source-record identity.
- Render validity: source offset/generation and whether the generated file was replaced
  or truncated.
- Agent consumption: explicit claim/read operation, not an assumption from the editor.

The existing M0 handoff's first-fixture test should therefore use the installed keymap
only as the opening mechanism, while recording the stable source identity alongside the
Markdown line address.

## Recheck commands

These are read-only except that `run.sh list` ensures its state directory exists:

```bash
bash /home/hruzam/ia-sync/install-pkgs/run.sh list | rg -i 'sublime|host:|TASK'
cmp \
  /home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/Default.sublime-keymap \
  "$HOME/.config/sublime-text/Packages/User/Default (Linux).sublime-keymap"
sha256sum \
  /home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/editor_pin.py \
  "$HOME/.config/sublime-text/Packages/User/editor_pin.py"
ls -l "$HOME/.wires/pins.jsonl"
```

Do not run `mark` merely to make the state look current without confirming that the
operator wants the machine-local bookkeeping corrected. The current evidence says the
bytes are current and the recorded version is stale.

## Handoff

**Goal:** Give the M0 reader a route from the transcript-view experiment to the existing
Sublime pin implementation and its installation evidence.

**Observed:** Source/live plugin and keymap match; `~/.wires/pins.jsonl` exists; runner
state says keymap `1.2` while recipe says `1.3`.

**Not claimed:** No new install, repair, state update, pin consumption or transcript
qualification was performed.

**Next safe move:** Use the existing M0 one-fixture test with an absolute Markdown path,
then open the selected line through Sublime and record source/session identity separately.
