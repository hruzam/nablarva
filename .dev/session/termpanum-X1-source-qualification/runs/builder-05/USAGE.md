# Q helper — partial builder delivery

This is an experimental C++17 helper, not a qualified source or product. Build
v4 completed with empty diagnostics. Only one normal and one burst run finalized
successfully; one ONLCR capture remains unfinalized after a cleanup race. All
other mode implementations and the full-matrix entry remain unexercised.

From `/home/hruzam/unikuklatrix/nablarva`:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -Wpedantic \
  .dev/session/termpanum-X1-source-qualification/src/collect/main.cpp \
  .dev/session/termpanum-X1-source-qualification/src/collect/sink.cpp \
  .dev/session/termpanum-X1-source-qualification/src/fixture/fixture.cpp \
  .dev/session/termpanum-X1-source-qualification/src/compare/compare.cpp \
  -o <fresh-build-output>
```

Do not overwrite retained binaries. Their corresponding sources are retained in
`build/source-v2`, `build/source-v3`, and `build/source-v4`. `tq-v1` was an earlier
compile-only artifact. Build logs and compiler version are under `build/`.

The executable supports these entries; placeholders must be replaced by exact
absolute owned paths. These examples are documentation, not new runtime authority.

```text
<helper> verify <bed>
<helper> suite <bed> <run-root> pilot
<helper> suite <bed> <fresh-run-root> matrix
<helper> run <bed> <run-root> <mode>
<helper> compare <retained-run> <bed>/expected <mode>
<helper> recover <bed> <incomplete-run>
```

`suite ... matrix` declares 201 cases: 30 each normal/burst/false_completion;
10 each onlcr/screen/sink_loss/pause/disconnect/delete/duplicate/reorder/
pane_recreate/server_recreate/late_attach; one missing_capture. It has **not**
been executed. A matrix root must have no existing runtime index. Pilot mode
resumes completed cases from `results.json` and appends new bundles to the same
index, retaining older attempts. Its remaining modes have not been validated.
Use a new POINT before further builder runtime; the controller stopped this cycle.

`compare` returns 0 for a supported complete case and 2 for rejection. Sink loss
and disconnect are meant to reject with independently measured coverage/exit
evidence. Replay mutation negatives copy the retained healthy normal bundle,
replace only its captured wire with the specified frozen mutated input, and retain
the original. Missing-capture negative copies the original and removes only
`g0/capture.bin`; its extra rejection output is separate. These paths are untested.

`fixture` and `sink` are internal entries launched only by the private owned
runner. The fixture constructs its pre-termios payload from the specification,
without opening expected files. Its in-pane supervisor forks the emitter and
records independent direct wait status. The sink retains actual completed append
offsets/times. `hold` is an internal synthetic keeper for pane recreation.

Runtime subprocesses are the installed `/usr/bin/tmux` and `/bin/sh` for tmux's
output pipe command (`exec` of this helper). There are no Python Q helpers,
downloads, packages, vendor CLIs or global configuration writes. Compiler,
clang-format, SHA/JSON/file inspection were administrative build/evidence tools.
The helper includes its own SHA-256 and limited JSON reader/writer. Every tmux
call includes the exact private socket and `-f /dev/null`. Pane execution is direct,
80x24, with an environment allowlist and no login-shell startup.

The first pilot used the outer tool's default zsh login wrapper; the synthetic
pane and pipe themselves used the controlled paths above. Use `login:false` for
subsequent host tool invocations. Private PID/start identities are additionally
bound to the PID namespace. A changing per-command sandbox cannot safely recover
a host run; `recover` rejects that mismatch before mutation/signaling. Host
execution requires the concrete sandbox boundary to be resolved by the controller.

`runtime-index.json` is the recovery entrypoint. Every actual run manifest records
the exact private directory/socket before spawn; command/process identities are
persisted before control actions. The runner reserves 13 seconds for active work
and two seconds for cleanup. Watchdog/fault branches remain unexercised. The
pre-runtime HOLD is outside the source runtime; preflight attempts are separately
retained and must never be counted as qualification runs.

**Outstanding recovery:** inspect `onlcr-pre-recovery-manifest.json`, then reconcile
the actual state of host namespace `pid:[4026531836]` before any action on the
ONLCR manifest's exact identities. Its socket still existed at the final read-only
inspection. Existence does not establish a living server. The attempted host
recovery approval returned no execution/session receipt, and neither designated
stdout nor stderr file exists. Do not repeat or launch recovery blindly.
