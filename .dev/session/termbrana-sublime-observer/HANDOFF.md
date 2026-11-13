# Sublime observer: development handoff

Majkee is continuing this connector in a separate session. Its purpose is to
let CLI agents inspect the actual contents and state of a specifically chosen
Sublime view, so routine checks do not require a person to transcribe them.
This task is separate from the Termbrana transcript renderer.

## Start here

1. Read [STATUS.md](STATUS.md), [README.md](README.md) and
   [evidence.baseline.md](evidence.baseline.md). STATUS describes the previous
   trial and its holds; reconcile them with Majkee's instructions for the new
   session before acting.
2. Read the original proposed contract at
   [termbrana-sublime-cli-implementer.md](../termbrana-M0-markdown-test/raw/termbrana-sublime-cli-implementer.md)
   and the connector section of the
   [transcript RUNBOOK](../termbrana-M0-markdown-test/RUNBOOK.md). Treat these
   as requirements and context, not as evidence of installation.
3. Inspect the existing implementation:
   [CLI](implementation/observer.py),
   [Sublime plugin](implementation/plugin/observer.py), and
   [tests](implementation/tests/). The shared cross-CLI guide is
   [sublime-observer/GUIDE.md](/home/hruzam/reposoma/raw.guides/sublime-observer/GUIDE.md).

## What Cartan needs

- Explicit instance, window and view handles, so an agent can select the right
  file even when multiple windows or tabs have the same name. Handle restart,
  closed views and stale handles honestly.
- Read the live buffer, including unsaved text, and report buffer identity,
  file path, revision, dirty/loading state, selection/caret, visible region and
  viewport. Preserve focus, selection and scroll. Bound output and report
  truncation, errors and unsupported views.
- A reliable way to correlate observations with a particular experiment run:
  unique run IDs, readiness/deadline behavior and safe concurrent calls. The
  caller must still verify the target path; a marker alone is not proof.
- Usable from different CLI agents running as the same user, with a short
  discoverable command or guide. Inventory must not turn into permission to
  read unrelated buffers. The local same-user socket is a trust boundary.
- A documented, reversible installation/removal path and host qualification
  against explicit synthetic views. Keep the live user profile and existing
  packages safe; any release or installation is governed by the new session's
  explicit scope and repository rules.

This tool supplies buffer and view-state evidence. A person or an appropriate
visual tool may still be needed to judge appearance, and it cannot by itself
prove native-session independence, complete transcript fidelity or live
approval answerability.

## What exists and what remains

The prototype is a read-only Sublime plugin plus a Python standard-library CLI.
It was tested with a separate portable Sublime 4215 profile, not installed in
the normal profile. The [disposable report](evidence.disposable-4215.json)
covers live text, unsaved buffers, duplicate windows, reorder, close, restart,
run correlation and concurrent calls. The [opening report](evidence.opening-4215.json)
covers the actual transcript opener and measured caret positions in an isolated
profile. Earlier, a disposable editor exited following a separate upstream
bridge close request; its cause remains unknown. The read-only prototype was
not shown to cause that exit.

Run the self-contained tests with:

```sh
python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-sublime-observer/implementation/tests -v
```

The real-editor test scripts are `implementation/tests/disposable_trial.py`
and `implementation/tests/opening_trial.py`; inspect their `--help` and trial
requirements before running. They use an isolated portable editor and synthetic
files. Do not copy private native transcript caches into evidence or a repo.

When ready, report the exact revision and path, installation state, supported
operations, privacy boundary, verification commands/results, and any remaining
limits to the main transcript session. Do not assume the temporary bed is a
permanent installation source or prune it while a symlink depends on it.
