# Sublime observation connector: trial handoff

This is a task-scoped prototype, tested in a separate portable Sublime Text 4215
profile. It is not installed in the user's Sublime profile. The plugin is a
read-only local socket server; the Python CLI reads it. It can observe actual
unsaved text, selection and viewport for an explicitly identified view. It does
not judge visual rendering or native transcript fidelity.

## Using a separately authorized installation

The reversible trial installation would be a symlink from
`~/.config/sublime-text/Packages/TermbranaObserver` to this bed's
`implementation/plugin` directory. First check that destination does not exist;
never replace an existing package. Remove only that symlink to uninstall. This
bed is temporary: keep it in place while the link is in use, and treat any
lasting installation as a separate reviewed promotion. No installation is
performed by this handoff.

With the plugin loaded, run the CLI below. `XDG_RUNTIME_DIR` must be the same
private runtime directory used by Sublime; otherwise pass `--runtime PATH`
before the subcommand. It creates private socket and descriptor files there.

```sh
OBS=/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-sublime-observer/implementation/observer.py
python3 -I -S -B "$OBS" instances
python3 -I -S -B "$OBS" windows --instance INSTANCE
python3 -I -S -B "$OBS" tabs --instance INSTANCE --window WINDOW
python3 -I -S -B "$OBS" read --instance INSTANCE --window WINDOW --view VIEW
python3 -I -S -B "$OBS" state --instance INSTANCE --window WINDOW --view VIEW
python3 -I -S -B "$OBS" selection --instance INSTANCE --window WINDOW --view VIEW
```

Pick the synthetic target by its path and explicit window/view IDs; do not read
unrelated views. Inspect `loading`, `dirty`, `revision`, `truncated`, and range
metadata. `read --lines START:END` uses inclusive one-based lines;
`--expected-revision N` rejects changed buffers. IDs belong to one plugin
instance and must be rediscovered after a restart or reload; stale descriptors
can appear with `reachable: false` and cannot be used.

For an experiment that controls its own output, issue `new-run --instance
INSTANCE --window WINDOW` and put its returned begin and end markers around
the new output. Then use `--timeout SECONDS wait --instance INSTANCE --window
WINDOW --view VIEW --run-id RUN_ID`. A successful wait consumes the run token.
The caller must independently verify the view's expected path: markers and a
window binding alone do not establish that it is the intended target. Failed
or incomplete waits must not be treated as fresh evidence.

## Evidence and limits

See [evidence.baseline.md](evidence.baseline.md) and
[the disposable trial report](evidence.disposable-4215.json) for the upstream
comparison, wrong-target/fix/rerun experiment and real-editor checks. The
latest disposable trial checked tab closing and reordering using a separate
test-only fixture; it did not use the upstream bridge. An earlier disposable
editor exit following an upstream close request remains unexplained.

In a further isolated trial, the real transcript opener opened the synthetic
snapshot in two new windows; the observer measured the two duplicate prompts
at their expected caret lines. See [the opening report](evidence.opening-4215.json).
This does not prove visual appearance. The connector does not control Sublime,
and installation and qualification in the normal profile remain separate work.

Run the isolated automated checks with:

```sh
python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-sublime-observer/implementation/tests -v
```
