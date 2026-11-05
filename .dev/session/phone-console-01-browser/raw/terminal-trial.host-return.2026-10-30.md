# Host and owned terminal implementation return

position: Build a fixture-only component around pinned ttyd; exact authentication,
origin, target generation and view identity precede input. Keep live ovitmugen
extensions with their owner. Do not promise delivery acknowledgement or replay.

changed: apps/session-console/host/{server,security,sessions,terminal_proxy}.py,
web/terminal.js, tests/test_host.py. Added explicit-origin auth, guarded disposable
fixture lifecycle, per-view external ttyd with private service credentials and
server-side AuthToken injection, active-target validation, no navigation prefix or
status chooser on generated views, and guarded history controls. Terminal uses its
owned xterm instance, font12, corrected touch/wheel glue, explicit key actions,
safe attachment cancellation and no auto reconnect/replay. Pending output drains
before resetting for a different target. No UI/storage/manifest files changed.

verification: In apps/session-console:

```sh
.venv/bin/python -m unittest discover -s tests -p test_host.py -v
node --check web/terminal.js
.venv/bin/python -m compileall -q host/server.py host/security.py host/sessions.py host/terminal_proxy.py tests/test_host.py
```

10 host tests PASS using new pc-test-* sockets, disposable bash/sleep processes,
loopback aiohttp servers and actual external ttyd. Covered HTTP+WS credentials,
missing/null/foreign/wrong-scheme Origin, CSRF action header, dimensions/frame
validation, protected/busy/stale close, private attachment binding, exact Czech
bytes with separate Enter, detach preserving the underlying shell generation,
diverged active view refusing input, and history leave never typing q into a shell.
Syntax/compilation PASS. Initial sandbox denied tmux/socket access; escalated tests
ran successfully. The first real run found missing trailing ':' in tmux session
display targets; fixed and covered by the passing real tests. aiohttp emits a
nonfatal recommendation to use AppKey instead of string application-state keys.

Source hashes at this receipt:

```text
5974c05f7e70f811c65a438442b473e2116fc2f04aea19f1829f13f957313447 host/server.py
47ec97891673a41bb1b79e78648c53e7f96d8ce044d9af36e394166bbc4ea3c3 host/security.py
84f31b78327317f7586eb40a1a4761b28759fedd2c5fe292370acb7aab8be38a host/sessions.py
6aaefe9a0e48b265b13702ed7038eda0a79911b0fd9aa2e1570aeeed57c028b2 host/terminal_proxy.py
f54067657cfa3bbb3510105c1dcb2728c35230027998412000fd3d2964607d79 web/terminal.js
d5c57ea3ceb75bee1182447c8ee0d419122cf1e40e906e87755bb61b573f17b6 tests/test_host.py
```

curvature: Exact tmux session context requires a trailing colon. Grouped views
share window dimensions/pane selection; fixture windows must remain single-pane.
Generated view prefixes/status are disabled to prevent native tmux navigation from
silently invalidating the label. Intentional shell tmux commands remain possible;
divergence closes input/output/watchdog paths. Multiline paste is refused until the
actual target is explicitly qualified and bracketed-paste mode is active; this
candidate advertises no qualified multiline targets. Agent start/end and live
sessions remain unavailable. Unicode11 addon is in the proposal but not installed
by the parent's current manifest; current terminal uses xterm's default Unicode data.

untouched: ia-sync, live/default tmux, parent trial gateway, device/USB, STATUS,
contracts/manifests, UI and vault worker files. Parent owns runtime restarts/builds.

remaining_gate: Fresh independent full-candidate verification, browser/physical
requalification, required long-duration tests and Houston consultation. Live-owner
review remains a separate gate; passing fixture tests does not activate live mode.
