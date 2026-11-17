# sublime-observer

- name: sublime-observer (Sublime Text package `SublimeObserver`)
- status: SKELETON, 2026-11-15. Built and verified in a disposable Sublime profile only. Not qualified on any host. Session gate open.
- line: `sublime-observer`, generation X, unattached. Living in `toolbox/` does not make this an organ or a toolbox.
- source: this folder is the only source. `SublimeObserver/` is the payload; `tests/` never ships.
- session: `.dev/session/sublime-observer-X1-file-publish/` (RUNBOOK and STATUS there; commit pins are added at closure)
- trust note: everything the package publishes is readable by every process of the same user.

## What it does

The operator shares a Sublime view with one command. While the view is shared, the editor keeps
a file copy of its text and state current. Agents read those files with ordinary file tools.

## What it never does

- It never publishes a view the operator has not shared, and it keeps no list of other views.
- It never notifies, wakes or rings an agent. It is observation only.
- It has no control function. Opening files or moving the caret is not a capability of this package.
- It opens no socket and ships no client.

## Sharing

- Command palette: "Sublime Observer: Share This View (toggle)". No key binding.
- A shared view shows a status-bar marker.
- Each share gets a new id. Shares do not survive a plugin reload or an editor restart.
- The toggle refuses paths inside `.majkee/` or `.hlm/` and files named `.env*`.

## Where the files are

`/run/user/<uid>/sublime-observer/` (directory mode 0700, files 0600). The path has one home:
the package settings file, `SublimeObserver/SublimeObserver.sublime-settings`. Readers use the
absolute path; `XDG_RUNTIME_DIR` is not set in every agent shell.

## File contract v1

TODO at closure: the contract moves into this folder (here, or `CONTRACT.md` if it outgrows one
page). Until then it is the session directive, section 3.

Reading order: `publisher.json` (is the publisher live?), then `views/<share_id>/state.json`,
then exactly the text file that state names. `current` exists only when exactly one view is shared.

## Limits a reader must know

- Liveness is a heartbeat, 1 s. A publisher whose heartbeat is older than 3 s is not live, and
  its files are history, not the current view.
- After a hard editor crash the last capture can still read as current for up to 3 s.
- If the editor crashes and is not restarted, the files stay. Only the stale heartbeat marks them dead.
- Text is capped at 200,000 characters per view; `truncated` says when the cap was hit.
- Sharing is not per-agent isolation (see the trust note).

## Tests

Standard library only:

    python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests -v

The real-editor trial (`tests/disposable_trial.py`) runs an isolated, disposable Sublime. It never
touches the normal profile.

Python host: `SublimeObserver/.python-version` holds `3.8`; on Sublime 4215 this selects the
3.14 plugin host. Execution on a real 3.8 host is not verified.

## Install and removal

TODO at the install phase: pointer to the reviewed task under `~/ia-sync/install-pkgs/`. Install
is a copy of `SublimeObserver/` into Sublime's `Packages/`, by that task only, on host home only.

## Not verified yet

The normal Sublime profile, real keyboard and mouse input, the status marker on screen, a read
from a sandboxed Claude Code session, hosts other than home.
