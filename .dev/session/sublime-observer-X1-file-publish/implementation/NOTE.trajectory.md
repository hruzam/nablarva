# NOTE — trajectory · step 1 (plugin + contract unit tests)

- seat: trajectory (participant_2), spawned in-window by the head (Oraculum · Claude)
- date/host: 2026-11-15 · home (`hruzam`)
- scope: plugin, contract tests and this note under `implementation/` only. I did not run a real editor.

## 1. Files changed (all new)

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/implementation/SublimeObserver/publisher.py`: Sublime-facing code. Toggle command, event listener, timers and `capture_view`.
- `.../implementation/SublimeObserver/contract.py`: pure Python with no `sublime` import. Covers root resolution, sealed paths, `Store` (atomic writes, retention, index and `current`, cleanup, liveness), `Debouncer` and `Writer`.
- `.../implementation/SublimeObserver/.python-version` (`3.8`), `SublimeObserver.sublime-settings`, `SublimeObserver.sublime-commands` (one entry; there is no keymap).
- `.../implementation/tests/fakes.py`: fake `sublime` and `sublime_plugin` modules, a manual clock with a timer queue, a recording `View`, a `TrapView` for unshared views, and `SyncWriter`.
- `.../implementation/tests/reader.py`: reader helper. It reads state and then the named text, retries if that text is gone, and checks the heartbeat and epoch.
- `.../implementation/tests/test_contract.py` (29), `test_publisher.py` (21), `test_static.py` (7).
- `.../implementation/evidence/unit-tests.2026-11-15.txt`, `mutation-check.sh`, `mutation-check.2026-11-15.txt`.

## 2. Commands and outcomes

- `python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/implementation/tests -v`: **57 run, 57 passed, 0 failed**, in 0.5 s on Python 3.14.7.
- `bash .../implementation/evidence/mutation-check.sh` deliberately breaks the code in 11 ways inside a fresh `/tmp` copy, which it removes afterwards. The baseline (no change) passes. 9 of the 11 make the suite fail: max delay, write order, retention, `current` with several shares, seal check, caret-only text skip, live-publisher refusal, revision guard, resurrection after unshare. The 2 that pass break layers that are duplicated elsewhere:
  - the share guard in `touched`: `_fire` drops unshared ids before any read anyway;
  - `fchmod`: `O_EXCL` with mode 0600 already gives the right mode.
- Probes, all read-only:
  - Installed Sublime: `pacman -Qs sublime` reports `sublime-text-4 4.4215-1`. `/usr/bin/subl` exists. `/opt/sublime_text/` contains only `plugin_host-3.3` and `plugin_host-3.14`, plus `libpython3.14.so.1.0`.
  - I did **not** run `subl --version`. `subl` hands off to a running instance, and I could not rule out that it focuses the editor.
  - The disposable 4215 profile `/tmp/nablarva-observer-4215/` still exists: `portable/` with `Data/`, `home/`, `launch.log`, owner hruzam, dated 7 Nov. Not run.
  - `python3 --version` reports 3.14.7. No 3.8 interpreter exists on the host.
  - `/run/user/1000/sublime-observer` is absent before and after; no test touches it. There is no SublimeObserver in `~/.config/sublime-text/Packages/`.

## 3. Evidence paths

`implementation/evidence/unit-tests.2026-11-15.txt` · `implementation/evidence/mutation-check.2026-11-15.txt`

## 4. Mismatches and deviations from the directive (§3 and the head brief)

1. **Explicit `root`:** its parent is the base and must be a 0700 directory owned by the user. The base check requires a real directory (not a symlink), owned by the user, with mode exactly 0700. A root that already exists with the wrong mode is refused, not repaired.
2. **Added fields.** The required fields are all present; these are additions:
   - state: `text_file_encoding` (`utf-8`), `selection_count`, `selections_truncated` (at most 256 selections, the X0 limit);
   - `publisher.json`: `heartbeat_interval_s` and `stale_after_s` (3 × interval);
   - `index.json`: `contract_version`, `updated_at`, and each entry's relative `state` path.
   - Timestamps are float epoch seconds.
3. **`title`** is `view.name()`, else the basename, else null.
4. **`error`** is null or `{code, message}`, with codes `loading`, `text_missing` and `capture_failed`. While a view is loading, no text is published and `text_file` is null.
5. **Liveness detail:**
   - A different pid that is alive with a fresh heartbeat means live, so the plugin refuses with one console line.
   - A dead pid, an alive pid with a stale heartbeat (pid reuse or a hung publisher), or the same pid with another epoch (a previous load in this plugin host) counts as residue and is cleaned.
   - An unparseable `publisher.json` is "foreign": the plugin refuses and does **not** clean. Needs a head decision, because the operator must delete it by hand.
6. **Pid check uses `/proc/<pid>` only.** No signal is sent, not even signal 0. Without `/proc` the pid counts as alive and the heartbeat decides.
7. **Trust boundary is tightened, not relaxed.** The seal check also runs on the resolved path, so a symlink into a vault is refused. It runs again at every capture, so a save-as or move into a vault unshares the view. Panels and widgets (`view.element()`) are refused.
8. **Unload** removes this epoch's files, then the root directory if it is empty. There is no fsync (tmpfs). Text is encoded UTF-8 with `errors='replace'`.
9. **Threading.** I chose this split because the change-count guard makes the capture safe, and a private writer thread keeps file I/O off both the main thread and Sublime's shared async thread. It also preserves write order and can be stopped on unload.
   - The capture runs on the plugin-host main thread inside `set_timeout` callbacks, as in X0. A caret- or scroll-only change skips `substr`.
   - The capture is guarded by `change_count` before and after. A torn capture is dropped and retried after the debounce.
   - All file I/O runs on one dedicated writer thread, in order. On unload, queued work is discarded and then cleanup runs under the store lock.
   - The toggle is a `WindowCommand` acting on `active_view()`, so no edit object exists.
10. **`.python-version` stays `3.8`:**
    - At build 4215 only the 3.3 and 3.14 hosts ship.
    - X0 saw a 3.8 pin run on 3.14.6 at 4215.
    - Builds before 4205 still use the 3.8 host for that pin.
    - Without the file, the plugin would fall to the legacy 3.3 host.
    - The 3.8 grammar is checked with `ast.parse(feature_version=(3, 8))`. Stdlib use was not run on 3.8.
11. **Brief pointer.** The X0 `tests/test_rpc.py` fakes a socket server, not `sublime`. I copied the fake-module pattern from X0's `tests/test_observer.py`. `capture_view` is adapted from X0's `_capture`, without the window/view lookup and the line-range read.

## 5. Recommended next task

Assay runs §2's command. After that, run a disposable-profile trial in `/tmp/nablarva-observer-4215/portable` (copy the package into `Data/Packages/SublimeObserver/`). Set an explicit `root` under a fresh private `/tmp` directory, so the trial never creates `/run/user/1000/sublime-observer` (your recovery probe treats it as an alarm). Drive synthetic views with an X0-style fixture plugin. Check:

- `plugin_python` and `sublime_build`;
- share, edit, caret, scroll, unshare, close;
- reload and the epoch change;
- `kill -9` residue cleanup on the next start;
- refusal by a second instance;
- typing latency.

## 6. Remaining uncertainty (nothing exercised in a real editor)

- **Real API behaviour:**
  - whether `size()` points equal Python `len()` for astral characters;
  - whether `view.element`, `is_valid` and `on_close` ids behave as assumed;
  - the precision of `set_timeout`;
  - how the status marker renders;
  - whether a main-thread capture of up to 200,000 characters adds typing latency.
- **Plugin host:** whether Sublime's plugin host actually loads this on 3.8 (pre-4205) and on 3.14.
- **Module reload:** Sublime also loads `contract.py` as a plugin module. That is harmless, but reloading it alone does not refresh `publisher`'s reference to it.
- **Stale marker:** a status marker may survive a plugin-host crash. Clearing it on the next load would mean listing views, so I did not.
- **Start race:** two instances starting at the same moment can race. There is no lock file.
- **Visibility:** `publisher.json` and `index.json` exist while the editor runs, even with nothing shared. Same-user processes can see that the editor is running, but not any content.

---

# Step 2 — disposable-profile trial (Sublime 4215, home, 2026-11-15)

## 1. Files changed

- `SublimeObserver/publisher.py`, **two defect fixes exposed by the trial** (details in §4):
  - `_poll_key` and `_capture_key` replace `_viewport_key`;
  - new `SublimeObserverListener.on_exit`.
- `tests/test_publisher.py`: +2 tests, `test_eventless_selection_change_is_published_by_poll` and `test_graceful_exit_cleans_like_unload`.
- New: `tests/trial_fixture/fixture.py` (test-only fixture package) and `tests/disposable_trial.py` (the harness).
- `evidence/mutation-check.sh`: +2 mutations, one per fix.

## 2. Commands and outcomes

- `python3 -I -B .../implementation/tests/disposable_trial.py`: **17/17 pass** (16 requested checks plus extra check 17).
- `X1_ONLY=exit python3 -I -B .../tests/disposable_trial.py`: graceful exit removed the root after 0.07 s, in **3 of 3** runs.
- `X1_ONLY=exit X1_AB_NO_ON_EXIT=1 ...`, the A/B run with `on_exit` disabled in the /tmp copy only: root **never** removed within 25 s, in 3 of 3 runs.
- Unit tests, same command as Step 1: **59 run, 59 passed**.
- Mutation check: baseline OK. 11 of 13 mutations fail the suite, including both new ones. The 2 survivors are the same redundant layers as in Step 1.

| # | result | observed |
|---|---|---|
| 1 | pass | `publisher.json` reports `sublime_build` 4215 and `plugin_python` 3.14.6. The plugin host exe is `.../portable/plugin_host-3.14`. So the `.python-version` 3.8 pin selects the 3.14 host on 4215. |
| 2 | pass | Every directory 0700 and every file 0600. `current` points to `views/<id>`. The reader returned the live text, equal to the disk text. |
| 3 | pass | Revisions 0→1→2. Files after the 2nd edit are `text.1` and `text.2`; `text.0` was removed. State names `text.2`, `dirty` is true, and the disk file is unchanged. |
| 4 | pass | Caret change to state: 288 ms, after the fix. Scroll to state through the poll: 485 ms. Seq went 3→4→5 and the text inode is unchanged. |
| 5 | pass | Index lists views 26 and 40 in windows 3 and 4, with buffers 55 and 88: the same file opened in two windows gave two buffers on 4215. `current` is absent. |
| 6 | pass | Marker found 0 times under the root; the unshared view has no index entry. |
| 7 | pass | After the unshare: the A directory is gone and `current` points to the remaining B. After the close: index empty, `current` absent, marker `''`. |
| 8 | pass | Zero differences in active window, active views, selections, viewports and windows, before and after publication. |
| 9 | pass | `.majkee/x.md` and `proj/.env.test` were both refused. Index and `views/` unchanged. |
| 10 | pass | Epoch changed (e7ad442a → 2d156d5e). Shares empty, `views/` empty, old directory gone, marker erased. |
| 11 | pass | Residue right after the kill: `publisher.json`, the view directory and `current`. The reader still saw "live". The orphaned plugin host stopped beating at once, lived 10.5 s more, then removed the publication. The restart came up clean under a new epoch. |
| 12 | pass | The second instance's runtime was not publishing; refusal: "another publisher (pid …) is live … does not publish". Its share attempt was refused. The first instance kept its epoch and its heartbeat continued. |
| 13 | pass | Input `A😀B𝔘C\n👩‍💻\n`: Python `len` 10, UTF-16 units 14. `size_chars` 10, `published_chars` 10, published `len` 10, identical text. A cap of 2 gives `'A😀'`; a cap of 3 gives 3. Sublime points are code points. |
| 14 | pass | Buffer of 199,900 characters. Main-thread `capture_view`: median 0.95 ms and p95 1.87 ms with text; 0.52 / 0.67 ms state-only. Edit to state replacement: median 152.5 ms, p95 153.0 ms (n = 30). Almost all of that is the 150 ms debounce by design. |
| 15 | pass | 51 edits over 2.58 s. Gaps between publications: 1000, 1032 and 553 ms (max 1032 ms). Trailing publish 150 ms after the last edit; the final revision (52) equals the last edit. |
| 16 | pass | `get_status` returns `Observer: SHARED`; unshared views return `''`. Rendering was not seen, because the display is headless. |
| 17 (extra) | pass | In this full run, the instance restarted after the crash ignored `exit` for 20 s, so it was stopped with a guarded SIGTERM. The root went when its plugin host exited (+30.7 s). The clean `on_exit` evidence is the exit diagnostic. |

Additional measurements:
- Heartbeat cadence: intervals of 5.001, 5.0 and 5.0 s, with write lag under 45 ms.
- Startup: about 6 s per instance, under the virtual compositor.

**Isolation.** Each instance ran in bwrap:
- its own network namespace (one net namespace per instance; the operator editor's is `net:[4026531833]`);
- the host filesystem read-only, with tmpfs over `/tmp`, `/run/user/1000` and `$HOME`;
- `--multiinstance`, and the binary inode matched `/tmp/nablarva-observer-4215/portable/sublime_text`;
- dbus-run-session, then `kwin_wayland --virtual` (headless), then a private `Xwayland :71`, so **no window reached the operator's desktop**.

**Signals.** I sent signals only to pids whose exe is under `/tmp/nablarva-observer-4215/` and whose environment carried this trial's root: one SIGKILL (check 11) and SIGTERMs from the stop fallback. Everything else in each chain exited by itself.

**Cleanup.**
- No disposable process is left.
- The operator's editor, pid 1590799 (with its crash_handler 1590821 and plugin_host 1590887), stayed up for the whole trial (elapsed time about 732,560 s).
- `/run/user/1000/sublime-observer` was never created.
- All trial roots under `/tmp` are removed.
- The portable `Data/Packages` is as found: `Observer`, `User`, `sublime-mcp`.

## 3. Evidence paths

`evidence/disposable-trial.2026-11-15.json` · `evidence/disposable-trial.exit-diagnostic.2026-11-15.json` · `evidence/disposable-trial.exit-diagnostic-ab-no-on-exit.2026-11-15.json` · `evidence/unit-tests.2026-11-15.txt` (59) · `evidence/mutation-check.2026-11-15.txt`

## 4. Mismatches, deviations and the code changes

1. **Defect fixed: eventless selection changes.**
   - Found: `view.sel().clear()/add()` from the API fires no `on_selection_modified` on 4215. The event count stayed at 2, and the state kept the old caret indefinitely.
   - Fix: the poll for shared views now compares the selection too (the first 256 regions plus the count), next to viewport, visible region and path.
   - Cost: one `sel()` read per shared view per 500 ms. Caret-only changes still never read the text.
2. **Defect fixed: graceful exit left residue.**
   - Found: Sublime does not call `plugin_unloaded` when the app exits, so `publisher.json` showed a fresh heartbeat for up to 15 s, and the files stayed until the next start.
   - Fix: `on_exit` runs the same cleanup. A/B: without it, the root survived (0 of 3 removed); with it, removed at 0.07 s (3 of 3).
3. **Profile not modified.** The portable `Data/Packages` still held the X0 `Observer` symlink (socket plugin, into the X0 bed) and `sublime-mcp` (upstream bridge). Running it as found would have loaded both. Instead each instance got a fresh `Data` from the trial root, bound over `portable/Data` inside the sandbox. "Installed by copy into Packages/SublimeObserver" holds inside the namespace; on disk the profile was never written.
4. **Display.** No Xvfb, Xephyr or Xvnc exists on home. I used the headless `kwin_wayland --virtual` compositor with a private Xwayland instead of visible windows.
5. **Fixture transport.** The fixture talks through files, not a socket, so the trial itself opens no socket. Its `share` operation focuses the view, then runs the palette command. Those focus changes come from the fixture, not the publisher; check 8 measures only around publication.

## 5. Recommended next task

Assay re-verifies Step 2: the unit tests and the two fixes against this note. One optional re-run of `disposable_trial.py` (about 2.5 min, self-cleaning) is enough. Then comes the install-pkgs task and the normal-profile witness.

## 6. Remaining uncertainty

- **Crash window (decision for the head or majkee).**
  - After a `kill -9`, readers see "live" until the orphaned plugin host exits, which took about 10.5 s here. The hard bound is `stale_after_s` (15 s).
  - The publisher's pid stays alive during that window, so a pid check does not help readers.
  - Lowering `heartbeat_s` (for example to 1 s, giving a 3 s bound) is a settings choice I did not make.
- **What removes the root after a crash** is likely `on_exit` firing late in the orphaned host; that is not proven.
- **Exit after a crash-restart:** the restarted editor ignored `exit` for 20 s, twice. A crash-recovery prompt is the likely cause, but it was not seen, because the display is headless.
- **Not exercised:**
  - visual marker rendering;
  - real keyboard and mouse input, which does fire `on_selection_modified` normally (only API-driven changes were shown to lack it);
  - the pre-4205 Python 3.8 host;
  - the normal profile;
  - Wayland-native or visible-display behaviour;
  - typing latency felt by a human (only capture cost and edit-to-state timing were measured).
- **Same file in two windows** gave two buffers on 4215, unlike a clone. Readers must use view and window ids, not the buffer id.

---

# Step 2b — unshared view under load, persisting crash residue, heartbeat as a parameter, ignored exit (home, 2026-11-15)

Seat: trajectory (fresh context; read Steps 1 and 2 above first). Same isolation as Step 2: bwrap, own net namespace, read-only host, tmpfs over `/tmp`, `/run/user/1000`, `$HOME`, fresh `Data` bound over the portable profile, headless `kwin_wayland --virtual` + private Xwayland. Every run was started from a `/tmp/x1-2b-run/implementation` copy; its evidence was copied back here.

## 1. Files changed

- **No change to `SublimeObserver/`** (publisher, contract, settings). No test exposed a publisher defect. The default heartbeat stays 5 s.
- `tests/disposable_trial.py` (harness only):
  - heartbeat interval and stale bound read from `SublimeObserver.sublime-settings` (× `contract.STALE_FACTOR`). Overrides go into the disposable profile's `User` settings only: `X1_HEARTBEAT_S` for the main run, and `X1_ALT_HEARTBEAT_S` (default `1`, empty disables) reruns both crash cases at that interval;
  - check 6 rewritten. New checks: `11b`, `18`, `18@hb1`, `11@hb1`, `11b@hb1`. Check 11 now goes through the same `crash_case()` as 11b and also records the reader timeline;
  - helpers: `Inotify` (ctypes, records directory events in order), `tree()`, `kill_together()`, `reader_timeline()`, `unshared_scan()`;
  - `stop()` records a fixture `inventory` before `exit`. If `exit` is ignored for 20 s, it records the inventory again plus the processes and the profile's `Local/` and `Crash Reports/` names, then falls back to the guarded SIGTERM as before;
  - `X1_ONLY=exit2b` (ignored-exit matrix), `X1_EXIT2B_WAIT_S`, `X1_RUN_LABEL`. The evidence prefix is now `disposable-trial-2b`, so the Step 2 files are never overwritten.
- `tests/trial_fixture/fixture.py`:
  - new `inventory` op: window/view **metadata only** (ids, name, path, dirty, scratch, size; never text) of the disposable editor;
  - the inbox poll now skips the harness's dot-prefixed temp names. That fixes a harness race that broke run 2 (see §2).
- New evidence: `disposable-trial-2b.2026-11-15.json` (run 3, main) · `disposable-trial-2b.run1.2026-11-15.json` · `disposable-trial-2b.run2-harness-race.2026-11-15.json` · `disposable-trial-2b.exit-diagnostic.wait3.2026-11-15.json` · `disposable-trial-2b.exit-diagnostic.wait45.2026-11-15.json` · `unit-tests-2b.2026-11-15.txt`.

## 2. Commands and outcomes

- `python3 -I -S -B -m unittest discover -s …/implementation/tests -v`: **59 run, 59 passed** (Python 3.14.7).
- `python3 -I -B /tmp/x1-2b-run/implementation/tests/disposable_trial.py`, three full runs:
  - run 1: **22/22 pass**. Its harness differed from the final one only in exit2b-only code and the fixture race fix.
  - run 2: **20/22**. Check 14 *error*: `FileNotFoundError` on the harness's `os.replace(in/.000068.json → in/000068.json)`. The fixture's poll matched the dot-prefixed temp name (it ends in `.json`) and consumed it before the rename. This race dates from Step 2 and only surfaced now. Check 6 then *failed* as a cascade: check 14's large view (id 45) was never unshared, so the index held `[45, 47]` and the "only P is shared" precondition failed. The leak scan in that run had **0 hits in 97 files**. This was not a publisher fault. Fix: the fixture skips dot-prefixed names.
  - run 3 (final harness, after the fix): **22/22 pass**. It is the main evidence file.
- `X1_ONLY=exit2b` with `X1_EXIT2B_WAIT_S=3`, then `=45`: see §4.
- No mutation-check rerun: the publisher did not change.

## 3. The new cases (run 3 measured; runs 1 and 2 agree unless noted)

**Check 6, unshared view while another publishes: pass.**
- View P (47) was shared and under a 5 s edit burst (97 edits).
- During the burst, unshared view Q (view 48, buffer 112) was opened with 300 marker lines, edited (append), given two selections and scrolled to y = 2000. The fixture saw Q fire `on_modified` ×2 and `on_selection_modified` ×2, so the publisher did receive those events and dropped them.
- 13 snapshots, 58 file reads in total: every regular file under the root (index, publisher, every state and text file) was searched for both markers (the new Q marker and Step 2's U marker). Every JSON file was also walked for any `view` or `buffer` value equal to Q's or U's ids (views 48 and 27, buffers 112 and 58). **0 hits.**
- Index: `[47]` only, one view directory. P's text is P's content only (base plus `k`s).
- P kept publishing: seq 44 → 49 across the 2.57 s Q window (3 distinct seqs sampled inside it). The final revision (98) equals the last edit.

**Check 11b, editor and plugin hosts killed together: pass** (5 s and 1 s).
- Kill: SIGSTOP the editor, then its plugin host, then SIGKILL both, each pid passing the same guard. No disposable process survived the kill.
- Residue persisted, byte-identical in the tree listing from the kill until the restart: `current@`, `index.json`, `publisher.json`, `views/<sid>/state.json`, `views/<sid>/text.1`. The residue state named the dead epoch.
- Restart on the same profile. inotify recorded, in order: event 0 `current` deleted, 1 `index.json`, 2–3 `views/<sid>/{state.json,text.1}`, 6 `views/<sid>/`, 9 `views/`, 10 `publisher.json`. The **first creation was event 11** (`views/`, then `.tmp-publisher.json-…` → `publisher.json`). So every residue path was removed before anything new was written. Same order at 1 s.
- New epoch differs (5 s: `76438b94 → 69560733`; 1 s: `c603b20b → 76c74c11`), and the new `publisher.json` pid equals the new plugin host.
- After the restart the reader got `Unavailable: current is absent`. The old capture was not presented.

**Check 11, editor only killed (orphan plugin host): pass** (5 s and 1 s). Step 2's case, kept.
- At 5 s the orphan host **removed the publication itself at 5.3 s** (runs 1–3: 5.29 / 6.05 / 5.29 s; Step 2 saw 10.5 s) and exited at 6.8 s.
- At 1 s the heartbeat went stale first (2.87 s), while the files were still on disk; the orphan cleaned them up and exited at 6.5 s.

**Check 18 and 18@hb1: pass.**
- `publisher.json` carries exactly the values the settings give: 5.0 / 15.0, and 1.0 / 3.0 with the override.
- Measured beats: 5.001, 5.001, 5.001 s and 1.0, 1.001, 1.0, 1.0 s.

**"Still looks live" window after a crash.** This is the time from the kill until `reader.publisher()` first raises `NotLive`, sampled every 50 ms.

| case | heartbeat | measured, runs 3 / 1 / 2 | heartbeat age at kill (run 3) | inferred from `heartbeat_at + stale_after_s − kill` (run 3) | why it ended |
|---|---|---|---|---|---|
| 11b together | 5 s | **14.54 / 14.51 / 14.60 s** | 0.48 s | 14.52 s | heartbeat stale; files still on disk |
| 11b together | 1 s | **2.53 / 2.61 / 2.52 s** | 0.48 s | 2.52 s | heartbeat stale; files still on disk |
| 11 orphan | 5 s | **5.29 / 5.29 / 6.05 s** | 0.67 s | 14.33 s | orphan host deleted `publisher.json` |
| 11 orphan | 1 s | **2.87 / 2.82 / 2.86 s** | 0.18 s | 2.82 s | heartbeat stale |

- Measured values match the inferred bound to within one 50 ms sample whenever staleness ends the window.
- *Inferred, not measured:* every kill fell 0.2–0.7 s after a beat (the harness kills right after a share), so these sit near the top of the range. In general the window lies in (stale − interval, stale]: **(10, 15] s at 5 s and (2, 3] s at 1 s**, unless an orphan host cleans up sooner.
- Throughout the window, `reader.read_current()` returned the dead epoch's capture, `capture presented: … revision 1`.

## 4. Ignored exit (time-boxed: 2 diagnostic runs, 9 launches each, plus the 3 full runs)

**What I saw.**
- Every restarted instance whose profile held a **dirty file-backed view** in Sublime's crash-time `Auto Save Session.sublime_session` ignored `exit` for 20 s.
- In those cases the restarted editor had reopened that view **dirty**, despite `hot_exit: disabled` and `remember_open_files: false`, and the fixture still answered 20 s after `exit` (the editor's main loop was running).

| scenario (wait before crash) | 3 s | 45 s |
|---|---|---|
| S1 fresh profile, exit | exit 0.16 s | exit 0.16 s |
| S2 dirty file view, editor-only kill, restart, exit | exit 0.16 s (nothing restored; `Local/` empty) | **ignored, SIGTERM**; restored `e2/dirty.md` dirty |
| S3 dirty file view, kill together, restart, exit | exit 0.16 s (nothing restored) | **ignored, SIGTERM**; restored `e3/dirty.md` dirty |
| S4 scratch views only, kill together, restart, exit | exit 0.16 s | exit 0.16 s (scratch view restored, not dirty) |
| S5 clean exit, restart same profile, exit | exit 0.16 s | exit 0.16 s |

- In all three full runs, `a2-restart` (profile `data_a`, where synthetic `A/same.md` was left dirty) was ignored and restored `A/same.md` dirty. `h2-restart` (scratch-only profile) exited in 0.16 s.
- The session file was written about 16 s before the kill in each 45 s case. That puts the first auto-save around 30 s after the share (inferred from mtime). No auto-save had happened at 3 s.

**What it depends on:** a crash after Sublime has auto-saved a session holding a dirty, non-scratch, file-backed buffer. It does not depend on the crash mode (editor-only or together), and the publisher plays no part.

**Inferred cause, not seen** (the display is headless): `exit` raises a "save changes?" prompt for the restored dirty buffer, and nobody can see it. On a visible display, the operator would see that ordinary Sublime prompt after a real crash. No workaround was built.

**Side observation (Sublime, not the publisher):** after a crash, Sublime restores unsaved file-backed edits from the auto-save session even with `hot_exit` disabled. Shares do not come back (`restart_clean` true every time).

## 5. Mismatches with the contract (§3)

1. **Rule 5 and the gate clause "an editor crash leaves no capture presented as current".**
   - A reader that follows rule 5 correctly is shown the dead epoch's last capture as current for up to `stale_after_s`. Measured 14.5 s at 5 s (bound 15 s) and 2.5 s at 1 s (bound 3 s).
   - After that it is never presented, even though the files persist (11b).
   - So the clause holds only *after* the stale bound. That bound is what the owed heartbeat decision buys: 5 s gives (10, 15] s, 1 s gives (2, 3] s. A later interval change is a settings edit plus `X1_HEARTBEAT_S=<n>` for the trial; the harness needs no code change.
2. **Rule 6** ("on load, remove residue of a dead epoch after confirming that pid is gone") is now shown in a real editor with persisting residue, ordered before any new write. No mismatch.

## 6. Flagged, not acted on

- **Reader-side pid check (contract decision, not made).** In the combined crash the publisher pid is dead at once, so a reader that also checked `/proc/<publisher pid>` would see "not live" almost immediately. It does not help the orphan case, where the pid is still alive. Whether Claude or Codex default sandboxes can see the host's `/proc` is unverified.
- **Process tree.** The disposable `crash_handler` double-forks and is reparented to `systemd --user` (pid 1342), outside bwrap's process tree but in its namespaces. It carried the trial env, passed the guard listing, and exited by itself in every run, so it was never signalled.

## 7. Remaining uncertainty

- **Kill phase.** Kill phase relative to the beat was not varied, so the bottom of each window range is inferred, not measured.
- **Prompt.** The save prompt was not seen; the cause is inferred.
- **Auto-save cadence.** The ~30 s first auto-save comes from two mtimes; the cadence was not measured.
- **Check 6 limits:**
  - transient `.tmp-*` files between snapshots were not read;
  - id matching covers JSON `view` and `buffer` keys only; text files are instead checked to hold only P's content.
- **Orphan cleanup timing** varies (5.3–10.5 s across Steps 2 and 2b). Which code path in the orphaned host removes the files (likely `on_exit`) is still unproven.
- **Still not exercised:** normal profile, visible display, real keyboard and mouse, Python 3.8 host.

Cleanup at the end:
- no disposable process left;
- the operator's editor, pid 1590799, still running;
- `/run/user/1000/sublime-observer` absent;
- no trial roots under `/tmp`;
- portable `Data/Packages` as found: `Observer`, `User`, `sublime-mcp`.

---

# Step 3a — source moved to its durable home, heartbeat default 1 s (home, 2026-11-15)

Decisions by majkee (RUNBOOK): the source home is `toolbox/sublime-observer/`, with the payload in `SublimeObserver/` and the tests in `tests/` beside it; the heartbeat is 1 s, so the stale bound is 3 s.

## 1. Files

- **Created.**
  - `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/SublimeObserver/`, the payload, 5 files: `.python-version`, `SublimeObserver.sublime-commands`, `SublimeObserver.sublime-settings`, `contract.py`, `publisher.py`. No tests, fakes, caches or evidence.
  - `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/`: `disposable_trial.py`, `fakes.py`, `reader.py`, `test_contract.py`, `test_publisher.py`, `test_static.py`, `trial_fixture/fixture.py`.
  - Both were copied with `command cp -a`. Before any edit, all 12 files had sha256 hashes identical to the bed copy. `toolbox/sublime-observer/README.md` belongs to another worker; I did not create or touch it.
- **Bed.**
  - `implementation/SOURCE-MOVED.md` (new).
  - Evidence: `evidence/unit-tests-3a.2026-11-15.txt` and `evidence/disposable-trial-3a.2026-11-15.json`.
  - This section.
- **Bed copy untouched.** `implementation/SublimeObserver/` and `implementation/tests/` are byte-identical to their pre-move sha256 list (all 12 files). They stay frozen at heartbeat 5 s.
- `evidence/mutation-check.sh` stays in the bed and still points at the bed paths. It was not ported to the new layout.

## 2. Differences between the bed copy and the new source (exactly the step-3 edits; 7 of 12 files)

| file | change |
|---|---|
| `SublimeObserver/SublimeObserver.sublime-settings` | `"heartbeat_s": 5` → `1`; the comment adds "(1 s: a crashed editor can look live for at most 3 s)" |
| `SublimeObserver/contract.py` | `DEFAULTS['heartbeat_s']` `5.0` → `1.0` (one line) |
| `tests/test_static.py` | expected settings `heartbeat_s` `5` → `1` |
| `tests/test_publisher.py` | `test_heartbeat_timer` asserts 1.0 / 3.0 in `publisher.json`, no beat at +0.99 s and a beat at +1.01 s (was +5.01 s); `test_settings_validation_falls_back` fallback `5.0` → `1.0` |
| `tests/test_contract.py` | the `Store` fixture uses `contract.DEFAULTS['heartbeat_s']` (was a literal 5.0); `plant()` gains `interval=5.0`; `test_heartbeat_refreshes` expects 1.0 / 3.0; **new test** `test_live_bound_follows_the_planted_interval_at_the_1s_default` (a 1 s publisher with a beat 2.5 s old stays live; 3.5 s old is taken over) |
| `tests/fakes.py` | a layout comment; `sys.dont_write_bytecode = True` |
| `tests/disposable_trial.py` | docstring (layout, evidence rule); `sys.dont_write_bytecode = True` before `import contract`; evidence goes **only** to `X1_EVIDENCE_DIR` (required; refused when inside the source tree; checked before any editor starts); the prefix comes from `X1_EVIDENCE_PREFIX` (default `disposable-trial`) and the date from the clock; the alternate interval defaults to `5` (was `1`); the report records `source_root`, `payload_files`, `installed_into_disposable_packages` and `installed_equals_payload` |

`publisher.py`, `.python-version`, the `.sublime-commands` file, `reader.py` and `fixture.py` are unchanged.

## 3. What the layout change broke, and the fix

- **Evidence path.** The trial wrote to `IMPL/evidence`. From the toolbox that would have created `toolbox/sublime-observer/evidence/`. Fixed with the required `X1_EVIDENCE_DIR`. I checked that it refuses both an empty value and the source root itself, with exit 1, no editor started and no trial root created.
- **Caches in the payload.** Tests and trial import from the payload directory, so a run without `-B` would leave `SublimeObserver/__pycache__`. With `sys.dont_write_bytecode` on the test side, a run without `-B` (in a `/tmp` copy) left `__pycache__` only in `tests/`, never in the payload. An install must still copy only the payload files.
- **Imports and the trial's install step.** Both survive unchanged. `fakes.IMPL` and the trial's `IMPL` are the parent of `tests/`, which is now `toolbox/sublime-observer/`. The trial copies `IMPL/SublimeObserver` into the disposable `Packages/SublimeObserver`. `installed_equals_payload` is true: the same 5 names.

## 4. Commands and outcomes

- `python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests -v`: **60 run, 60 passed** (59 + 1 new).
- Mutation probe (in a `/tmp` copy): with `contract.DEFAULTS` reverted to 5.0, **4 tests fail**: `test_heartbeat_refreshes`, `test_live_bound_…`, `test_settings_validation_falls_back`, `test_heartbeat_timer`. `test_static` separately pins the settings file.
- Trial, from a `/tmp/x1-3a-run/sublime-observer` copy that matched the toolbox per `diff -r`:
  `X1_EVIDENCE_DIR=/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/implementation/evidence X1_EVIDENCE_PREFIX=disposable-trial-3a python3 -I -B /tmp/x1-3a-run/sublime-observer/tests/disposable_trial.py`
  → **22/22 pass**. The main cases ran at the 1 s default (`source: package settings`); the alternate run was at 5 s.

## 5. Measured at the 1 s default (the reader samples every 50 ms)

| case | heartbeat age at kill | measured "still looks live" | inferred bound | ended by |
|---|---|---|---|---|
| 11, editor only (orphan host) | 0.70 s | **2.35 s** | 2.30 s | heartbeat stale; files still on disk; orphan host exited at 7.2 s |
| 11b, editor and plugin host together | 0.48 s | **2.57 s** | 2.52 s | heartbeat stale; residue persisted; restart deleted all of it (events 0–10) before the first creation (event 11) |
| 11@hb5 (alternate) | 1.19 s | 4.44 s | 13.81 s | orphan host deleted `publisher.json` |
| 11b@hb5 (alternate) | 0.48 s | 14.56 s | 14.52 s | heartbeat stale |

- Check 18: `publisher.json` 1.0 / 3.0; measured beats 1.001, 1.0, 1.001 s.
- Check 12, a second instance beside a live 1 s publisher: it still refuses; the first instance kept its epoch and its heartbeat.
- Check 6: 0 hits in 58 file reads; P kept publishing (seq 44 → 49).
- *Inferred:* the window at 1 s lies in (2, 3] s. Every kill came 0.5–0.7 s after a beat, so the bottom of that range was not sampled.
- The restarted `a2-restart` ignored `exit` again; the Step 2b cause applies (a dirty `A/same.md` restored from the auto-save session).

## 6. Cleanup and remaining uncertainty

- **Cleanup.**
  - No disposable process is left; the operator's editor, pid 1590799, is still running.
  - `/run/user/1000/sublime-observer` is absent, and `/tmp/x1-3a-run` and all trial roots are removed.
  - Portable `Data/Packages` is as found; no SublimeObserver in `~/.config/sublime-text/Packages`.
- **Stray process.** My stuck interactive `cp -i` from step 2b (pids 2738685 zsh and 2738692 `cp -i`) was verified by `/proc/<pid>/cmdline`: my exact command, uid 1000. It was stopped with SIGTERM.
- **Uncertain.**
  - The kill phase was not varied.
  - Whether 1 s beats cost anything measurable on a real, busy editor; the disposable trial only shows cadence.
  - `mutation-check.sh` has not been ported to the toolbox layout.
  - Install and removal still belong to the reviewed install-pkgs task.

---

# Step 4a — read-only witness recorder for the normal-profile walk (home, 2026-11-15)

The operator walks the checklist by hand in his real Sublime. Nobody queries the editor; this recorder is the only instrument. It watches the publication directory and writes a JSONL timeline for a verifier.

## 1. Files

- **New in the toolbox.**
  - `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/witness_recorder.py`: stdlib only, Python 3.8 syntax, 592 lines, sha256 `4d34b28f…be5bc3f`.
  - `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/test_witness_recorder.py`: 14 tests, sha256 `dac8d556…6fd4e55`.
- **Unchanged.** The payload (5 files), `README.md`, `reader.py` and `test_static.py`. `test_static.py` pins only the payload, not the test list.
- **New in the bed.**
  - `evidence/unit-tests-4a.2026-11-15.txt`
  - `evidence/witness-recorder-proof-4a.2026-11-15.jsonl`: 18 of the 32 lines, kept verbatim.
  - `evidence/witness-recorder-proof-4a.driver.py`: the proof driver, kept so the proof can be rerun.
  - This section.

## 2. Command

    python3 -I -B /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/witness_recorder.py --out <new file.jsonl> --forbid <string> [--forbid <string> ...] [--root <dir>] [--interval-ms 100]

- **Default root.** The literal `/run/user/<uid>/sublime-observer`, the reader rule from directive §3. If `XDG_RUNTIME_DIR` points elsewhere, the recorder warns, because the publisher prefers that variable.
- **Exit 2 (refused), nothing created.** Any of these:
  - `--out` exists, including as a dangling symlink;
  - `--out` is under the root, checked on both the literal and the resolved path, even before the root exists;
  - the directory of `--out` is missing;
  - a `--forbid` value is empty;
  - `--interval-ms` is outside 10 to 10000.
- **Stderr.** At start it prints the root, out, forbid strings and interval. Each stamp is echoed with its local time. A forbidden hit prints a `!!! FORBIDDEN STRING FOUND: <file> contains --forbid #i '<s>' !!!` line the first time that (file, string) pair appears. At the end it prints one line: `stopped by SIG…: N records, N samples, N stamps, N forbidden hit(s)`.
- **Stamps.** The operator types `7 unshared two` + Enter. Stdin is read with `select`, which also paces the samples, so stdin never blocks sampling. When stdin reaches end of file, the recorder writes a `stdin_eof` record and keeps sampling.
- **Stopping.** SIGINT, SIGTERM and SIGHUP all end the recorder cleanly: `end` record, fsync, summary.

## 3. Record format (one JSON object per line, flushed per line, file 0600)

- **Every record** carries `kind`, `n` (record index), `wall` (`time.time()`), `mono` (`time.monotonic()`) and `iso` (local time, ms).
- `start`: `root`, `out`, `forbid` (the list; a hit refers to its index), `interval_ms`, `pid`, `python`, `recorder_version`.
- `sample`: `changed`, `sample_n` (samples taken so far), `sample_ms`, and `snapshot`.
  - **When written.** A sample record is written when the snapshot differs from the last written one; `snapshot.volatile` is excluded from that comparison. Otherwise one is written at least every 1 s (`changed: false`).
  - **Heartbeat beats count as changes.** Each beat changes `publisher.fields.heartbeat_at`, so a live publisher yields about one `changed: true` record per second.
  - **Snapshot keys:**
    - `root`: `exists`, `type`, `mode`, `owned_by_me`. When `exists` is false, nothing else is present.
    - `entries`: every name under the root, relative, with `type` (`dir`, `file`, `symlink` or `other`) and `mode`. Files add `size`; symlinks add `target`. Symlinks are never followed.
    - `publisher`: `present`; `fields` (`contract_version`, `epoch`, `pid`, `started_at`, `heartbeat_at`, `heartbeat_interval_s`, `stale_after_s`, `sublime_build`, `plugin_python`); `other_keys`; and `reader`, which is `live`, `not live: <reason>` or `reader error: …` from `reader.publisher`.
    - `index`: `present`, `epoch`, and `shared`, a list of `{share_id, path, title, window, view, buffer, state}`.
    - `current`: `present`, `type`, `target`, `resolves_inside_root`.
    - `read_current`: what `reader.read_current` returns. Either `{ok: true, share_id, epoch, seq, revision, text_file, published_chars, text_chars, text_sha256_utf8, chars_equal_published}` or `{ok: false, reason: "<Exception>: <message>"}`. When `current` resolves outside the root, the reader is not called, and the reason says `not followed`.
    - `views.dirs.<share_id>.state`: `share_id`, `epoch`, `seq`, `revision`, `dirty`, `loading`, `path`, `title`, `size_chars`, `published_chars`, `truncated`, `text_file`, `text_file_encoding`, `selections`, `visible_region`, `viewport_position`, `error_code`.
    - `views.dirs.<share_id>.text`: `exists`, `bytes`, `chars`, `sha256` (of the bytes on disk) and `chars_equal_published`.
    - `forbidden_hits`: `[{file, forbid: [indices]}]`.
    - `errors`: `[{path, op, error}]`. Each error is `vanished`, `bad json: …`, `refused: …` or `<Type>: …`. None of them is fatal.
    - `volatile`: `heartbeat_age_s`.
- `stamp`: `stamp` holds the typed line.
- `stdin_eof`: no fields.
- `end`: `reason` (the signal name), `samples`, `records` (including this one), `stamps`, and `forbidden_hits` as `[{file, forbid}]`, every distinct pair ever seen.

## 4. Read-only and containment guarantees (how)

- **Reads.** Every file the recorder opens goes through `read_bytes`:
  - the resolved path must be inside the resolved root;
  - the file is opened with `O_NOFOLLOW | O_NONBLOCK`, so a FIFO cannot block it;
  - after opening, `fstat` must show a regular file.
- **The contract reader.** `tests/reader.py` is loaded as a private module instance whose `open` is that guarded read, so even the reader cannot be led outside the root. A `text_file` of `../x` or an absolute path is refused. `reader.py` itself is unchanged.
- **Text.** It is never stored. The recorder keeps only character counts and sha256.
- **Writes.** It writes nothing but `--out`, created with `O_EXCL | O_NOFOLLOW`, mode 0600.
- **Isolation.** No socket, no subprocess, no signal sent, no `/proc` read.
- **Forbidden scan.** Each string is searched in three byte forms: raw UTF-8, JSON-escaped with `ensure_ascii=False`, and JSON-escaped as ASCII. A title such as `a"b` is therefore found in `index.json`.

## 5. Commands and outcomes

- **Unit tests.** `python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests -v`: **74 run, 74 passed** (the existing 60 plus 14 new), no warnings. Log: `evidence/unit-tests-4a.2026-11-15.txt`.
- **What the 14 new tests show.**
  - A subprocess timeline records the root absent, then share, edit, unshare and root removal.
  - Stamps are in order, and EOF on stdin does not stop the recorder.
  - The `end` record follows SIGTERM, and the 0600 mode holds.
  - The text never appears in the output.
  - Keepalive: one record per second while unchanged, with many more samples than records.
  - A planted forbidden string is reported with its file name and the loud stderr line; the JSON-escaped form is found too.
  - Refusals: an existing `--out`, a dangling-symlink `--out`, a `--out` under the root (before and after the root exists), and an empty `--forbid`.
  - A `current` pointing outside is not followed; a `text_file` that escapes is refused by the guarded reader.
  - A symlinked view directory and a FIFO are not entered.
  - Bad JSON and a vanished text file are recorded, not fatal; a stale heartbeat reads as `not live`.
- **Mutation check** (in a `/tmp` copy, since removed). With the two containment guards disabled (the `current`-outside skip and `inside()` in `read_bytes`), 2 tests fail: `test_current_pointing_outside_is_not_followed` and `test_reader_is_guarded_against_a_text_file_that_escapes`.
- **End-to-end proof, no editor.**
  - Command: `python3 -I -B <scratch>/proof_4a.py`, kept as `evidence/witness-recorder-proof-4a.driver.py`.
  - The fake root was `/tmp/x1-4a-proof-204jtkv_/run/sublime-observer`, driven by the real `contract.Store` with a 1 s heartbeat thread. Stamps were piped in at each step.
  - The run ended with SIGINT and exit 0. The recorder was alive after stdin EOF.
  - Totals: 32 records, 119 samples, 10 stamps, 0 forbidden hits. No published text is in the JSONL.

  | t (s) | stamp | first sample after it |
  |---|---|---|
  | 0.00 | (start) | root absent |
  | 1.13 | 1 enable | epoch-A live, index `[]`, `current` absent |
  | 1.73 | 2 share one | index `[one]`, `current` → `views/one`, read_current ok rev 1 `text.1` |
  | 2.33 | 3 edit one | rev 2 `text.2`; `text.1` kept as the previous file (8 entries) |
  | 2.94 | 3b caret moves | seq 2 → 3, same revision and text file |
  | 3.54 | 4 share two | index `[one, two]`, `current` absent, `Unavailable` |
  | 4.14 | 5 unshare two | index `[one]`, `current` → `views/one` again |
  | 4.74 | 6 crash (beats stop, residue stays) | at 7.20: `not live: heartbeat is stale`; residue still on disk, `read_current` NotLive (about 3.07 s after the last beat; the bound is 3 s) |
  | 8.74 | 7 restart | epoch-B live, residue gone, index `[]` |
  | 9.34 | 8 share one again | `one-b` rev 3 ok |
  | 9.94 | 9 quit | root absent |
  | 10.54 / 11.90 | stdin_eof / end SIGINT | |

- **Proof shortcut.** For the restart, the driver sets `b._alive = lambda pid: False`, because the "crashed" epoch's pid is the driver's own live pid. A real restart has a different pid, so this shortcut does not apply there.
- **Payload.** `SublimeObserver/` still holds exactly the 5 files. There is no `__pycache__` anywhere under `toolbox/sublime-observer/`.

## 6. Deviations from the brief

- **State fields added.** `share_id`, `text_file_encoding` and `error_code` were added to the listed state fields. Only the error code is kept, never the message, because a `capture_failed` message is `str(exc)` and could carry a fragment of the buffer.
- **Signals.** SIGHUP is handled like SIGTERM, so closing the terminal still writes the `end` record.
- **Extra records.** `start`, `stdin_eof` and `end`, plus the `kind`, `n` and `iso` fields on every record.
- **Extra refusals.** An empty `--forbid`, an interval outside the range, a missing directory for `--out`, and a dangling-symlink `--out`.
- **Two hashes.** The per-view `sha256` is taken over the bytes on disk. The `read_current` hash is over the reader's decoded text, re-encoded as UTF-8. The two are equal for valid UTF-8.

## 7. What the recorder cannot see (verifier must know)

- **The editor.** It sees nothing in it: not unshared views, focus, selection, scroll or typing latency. It sees only what is published. "Publishing changed nothing in the editor" needs the operator's eyes.
- **Short-lived states.** It polls every 100 ms. A state or temp file that lives shorter than one interval can be missed, both in `entries` and in the forbidden scan. The trial's inotify stream is not part of it.
- **Snapshot consistency.** A sample is not atomic across files; it can straddle a publish. A transient `vanished` for a swept `text.N`, or a mixed seq, followed by a consistent sample, is normal.
- **Liveness.** It reads `/proc` for nothing, so the liveness verdict is the reader's heartbeat rule only. A dead editor looks live for up to `stale_after_s` (3 s). Correlate the publisher pid with the stamps by hand.
- **Clock.** Heartbeat age uses the wall clock; a clock jump distorts it. Use `mono` to order and space events.
- **Forbidden strings.** Only the three byte forms are found: not case variants, other encodings, or a string split by an escape the recorder does not produce.
- **Recorder killed.** A SIGKILL or power loss leaves no `end` record, so a missing `end` means the recorder was killed.
- **Output size.** It grows about 4 KB per record, roughly one record per second with a live publisher (about 15 MB per hour).
- **Output content.** The output contains shared paths, titles and coordinates. It is 0600 but is not checked for location beyond "not under the root".

## 8. Remaining uncertainty

- **Not yet run beside a real Sublime.** The normal profile is the operator's step, and the disposable trial was not rerun with the recorder beside it. It is untested whether 100 ms polling plus a full read of every file costs anything noticeable while the real editor publishes. The proof sample cost was 0.02 to about 3 ms.
- **Default root.** On home, `XDG_RUNTIME_DIR=/run/user/1000`, which matches the default; a different value only triggers a warning.

Cleanup: the proof's work directory under `/tmp` and the mutation copy are removed. No recorder or driver process is left. `/run/user/1000/sublime-observer` was absent before and after every run.

# Step 5 — fix round on the Codex audit (_bus/07), per the head's verdict (_bus/08) (home, 2026-11-16)

Source: `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/` only. The bed copy stays frozen. Task file: `/home/hruzam/ia-sync/install-pkgs/sublime-observer.md`.

## 1. What changed, per finding

- **1 — ownership by kernel lock (done).** `contract.py`:
  - New `acquire_lock(root, uid)`. It opens `<root>/publisher.lock` with `O_RDWR|O_CREAT|O_NOFOLLOW|O_CLOEXEC`, mode 0600, and requires a regular file owned by uid. It takes `flock(LOCK_EX|LOCK_NB)`; when another holder has the lock it returns None.
  - `Store.start` now goes: mkdir root → take the lock → read `publisher.json` → clean residue → write. Residue cleanup happens only while the lock is held.
  - The publisher holds the fd for its whole life; `Store.shutdown` releases it.
  - Removed: `pid_alive`, `assess_existing`, the `alive=` parameter, and every pid or heartbeat-age takeover path.
  - A load beside a previous load in the same plugin host that never unloaded is now refused. flock is per open file description, so the old fd still holds the lock. The trial's plugin reload (check 10) still passes, because Sublime unloads the old module before it loads the new one.
- **Lock-unlink pitfall (chosen: unlink, then verify).** At shutdown the holder unlinks the lock file *while still holding it*, then rmdirs the root, then closes the fd. After any flock succeeds, `acquire_lock` compares `fstat(fd)` with `lstat(path)` (st_dev, st_ino). On a mismatch or ENOENT it closes the fd and retries, up to 3 times. If the root vanished, `Store.start` re-creates it and retries.
  - Why unlink rather than leave the file: leaving it would keep the root from ever being removed. The task's Removal check (`No such file or directory`) and trial check 17 depend on the root disappearing on a clean exit.
  - Never unlink at shutdown unless `_holds_path` is true.
- **Unreadable publisher.json: kept.** The lock removes its original reason: no lock-respecting publisher can be live while we hold the lock. It still guards against an unknown writer or a damaged root, and it costs nothing. The lock is released when start refuses for this reason. Test `test_unreadable_publisher_is_refused_not_cleaned`.
- **2 — no cross-share mixing (done, both sides).**
  - New `contract.text_name(share_id, revision)` returns `text.<share_id>.<revision>`, and `Store.publish` uses it. State already carried `share_id`.
  - `tests/reader.py`: new `resolve_current` (one readlink; the target must be `views/<name>`). `read_capture` reads state, then text from that one directory, then state again, and requires epoch, share_id and seq to be equal (otherwise it retries). With `share_id`, the state must name the pinned share.
  - The recorder's private reader is the same `reader.py` loaded with the guarded `open`, so it follows automatically. Its picked state fields gain `text_encoding_replaced`.
- **3 — revocation (done).**
  - `Store.revoke(share_id)` is the one main-thread entry: a set add under its own small lock, no I/O. `publish()` returns at once for a revoked share.
  - `_Runtime.unshare` (used by toggle, close, invalid view and sealed path) calls it synchronously before it queues `remove_share`. `remove_share` revokes too.
  - When removal fails, `Store._stop_publishing` sets `live=False`, so no further write of any kind and no heartbeat. As a best effort it also removes `current` and `publisher.json`, so readers see `NotLive` at once; if those removals fail too, readers see it after the stale bound. It then raises `contract.Stopped`.
  - `_Runtime._write_error` prints one line (`stopped publishing: …; readers see "not live"; reload the package or restart Sublime`), erases the markers on the main thread, and stops the heartbeat timer re-arming. Toggle then answers "not publishing".
  - `shutdown` after a stop still holds the lock and retries the cleanup.
  - The sealed-path check is synchronous. New `_Runtime.path_allowed(view_id, force)` re-runs the rule whenever the file name differs from the last checked one; it is called from `touched()`, i.e. every event and the poll, since the poll key holds the path. `on_post_save` → `saved()` forces a re-resolve, which catches a symlink retargeted into a vault without a name change. A sealed result unshares immediately, with no debounce.
- **4 — install update writes fresh inodes (done).** `command cp --remove-destination --` in the update loop. No ancestry checks; the task text now states that symlinked ancestors are unchecked.
- **5 — documentation only (head).** No code change.
- **6 — unresolvable path refused (done).** `sealed_reason`: any `OSError`, `ValueError` or `TypeError` from normpath or realpath returns `path cannot be resolved (<Type>)`. Before this, `'/tmp/a\0b'` raised a ValueError that was swallowed, and the path was allowed.
- **7 — `current` before the index (done).** New `Store._update_listing(between)`. It removes a `current` that must change before the index is replaced, and sets `current` only after the index and the directory removal (`between`). Second share added: `current` off, then index. Removal: `current` off (if it pointed at the removed share), index, directory, then `current` to the remaining single share.
- **8 — encoding flag (done).** `publish` tries strict UTF-8 first; on `UnicodeEncodeError` it writes with `'replace'` and sets `text_encoding_replaced: true` in state. The flag follows the text file on caret-only updates. `published_chars` still counts input characters (each replacement is one `?`).
- **9 — task wording (done).** An interrupted run can leave staging; ownership is by the five names only; ancestors are unchecked; the runtime `rm -r` is the operator's judgment. `version: 1.1`.
  - One extra line, flagged: `publisher.lock` added to the "Expect a directory with …" listing in Verify by eye, because the old listing would surprise.
  - Every `>from majkee`, `>to oraculum`, `> to oraculum` and `>check` note and its block is byte-identical (checked by diff: no removed line belongs to a note).
- **10, 11 — documentation only (head).** No code change.
- **README.md: unchanged.** Nothing in it became false. Its reading-order line is now incomplete, not wrong; the contract section is the head's.

## 2. Tests

- **Unit suite:** `python3 -I -S -B -m unittest discover -s …/tests -v`: **98 run, 98 pass**, 4.3 s. Before this step: 74. Log: `evidence/unit-tests-5.2026-11-16.txt`.
- **Removed (premise gone):** the 5 takeover tests (`test_dead_epoch_residue_is_removed`, `test_real_dead_pid_via_proc`, `test_live_publisher_is_left_alone`, `test_live_bound_follows…`, `test_alive_pid_with_stale_heartbeat_is_residue`) and `test_reload_cleans_own_previous_epoch`. `test_save_as_into_vault_unshares` became `…_at_once`.
- **Acceptance (a):**
  - `test_simultaneous_start_in_threads_one_owner`: 8 Stores, Barrier.
  - `test_simultaneous_start_in_processes_one_owner`: 4 child processes.
  - `test_resumed_old_owner_and_a_new_start_never_both_publish`: a real child, SIGSTOP, a new start refused, SIGCONT, the child publishes, then it dies without cleanup and a third start cleans its residue.
  - `test_holder_with_a_stale_heartbeat_keeps_the_root`, `test_lock_file_unlinked_by_a_finishing_holder_is_not_a_second_lock` (flock patched to run the holder's shutdown between open and lock), `test_second_store_in_the_same_process_is_refused`, `test_symlinked_lock_file_is_refused`.
- **Acceptance (b):** `CurrentSwitchTests`. Shares A and B are both at revision 1 with distinct bodies. Between the state read and the text read, B is shared and A unshared, so `current` → B.
  - The v1.0 naive reader finds no file (guard: names).
  - The step-5 reader never pairs wrongly, either with real names or with names patched back to `text.<rev>` (guard: pin plus second read).
- **Acceptance (c):**
  - `test_queued_publish_then_unshare_with_removal_failure` (plugin, `fakes.QueueWriter`): a queued capture, then unshare, then an injected removal failure. Result: the queued capture is discarded (seq unchanged), there is one console line, `NotLive` at once, `current` is absent, the heartbeat stops, and toggle refuses.
  - `test_queued_publish_then_unshare_close_or_sealed_save_writes_nothing`.
  - Contract side: `RevocationTests` (directory failure → NotLive at once; every removal failing → heartbeat frozen and NotLive after the bound; shutdown after a stop still cleans).
- **Acceptance (d):** `tests/test_install_task.py`. It extracts the Install block from the task file and runs it with `HOME` pointed at a temp directory, where `contract.py` in the destination is a hard link to an unrelated file. The unrelated file is untouched. Against the v1.0 block this test FAILED (it overwrote the unrelated file with `contract.py`); it passes now. A second test shows the first install still works. Skipped where the task file or bash is absent; `SUBLIME_OBSERVER_TASK` overrides the path.
- **Item 5 tests:** `ListingOrderTests` (2), `SmallFixTests` (unresolvable path, encoding flag), plus `test_unresolvable_path_is_refused` at the plugin level.
- **Mutation check:** `evidence/mutation-check-5.py` → `evidence/mutation-check-5.2026-11-16.txt`. 17 mutations, each in a fresh temp copy, and every one makes the suite fail; the output names the catching tests.
  - Two guard pairs are redundant by design, so each pair member is mutated separately:
    - Reader pin versus second read: either one alone prevents a wrong pairing. b2 removes both and fails `test_reader_rule_never_pairs_across_shares`; b3 removes the second read only and fails the freshness test. Removing only the pin is not caught; the second read covers it.
    - Events versus save: c4 removes the event path check and is caught by the poll test; c5 un-forces save and is caught by the symlink-retarget test.

## 3. Disposable trial

`X1_EVIDENCE_DIR=<bed>/implementation/evidence X1_EVIDENCE_PREFIX=disposable-trial-5 X1_NO_OPERATOR_PROBES=1 python3 -I -B tests/disposable_trial.py`

- **Result: 22 of 22 checks pass**, 155 s. Report `evidence/disposable-trial-5.2026-11-16.json`; console `evidence/disposable-trial-5.console.2026-11-16.txt`.
- **Check 12:** the second editor's refusal names the lock: `another publisher holds …/publisher.lock (publisher.json names pid 234193); this instance does not publish`.
- **Check 11b:** the crash residue includes `publisher.lock`. The restart reuses it (no delete event, by design) and removes every other residue path before creating anything. The reader saw `NotLive` 2.57 s after the kill.
- **Check 3:** names are `text.<share_id>.<rev>`.
- **Trial edits:** check 3 uses `contract.text_name`; crash residue accounting excludes `publisher.lock` and asserts that it is present.
- **New switch `X1_NO_OPERATOR_PROBES=1`.** It skips the two probes the brief forbade: the `/proc` metadata of the operator's editor, and the existence check of `/run/user/<uid>/sublime-observer`. Both report `skipped`. `/proc/<pid>/exe` readlinks for the signal guard remain.
- No disposable process was left; the trial root was removed. Nothing in the operator's editor or profile was started, signalled or read.

## 4. Not done, limits, things a verifier should attack

- **No real-editor demonstration of:** sealed save-as or rename, queued-capture discard, or removal failure (the fixture has no save-as op). These are unit-test evidence only.
- **Start during a holder's shutdown.** A new publisher that starts while the old one is between `remove_publication` and close gets EWOULDBLOCK and refuses for its life (fail closed, one line). There is no retry.
- **Lock inheritance.** `O_CLOEXEC` keeps the lock out of exec'd children. A `fork` without exec by another plugin in the same host would share the open file description and could keep the lock after the plugin host dies. Not tested.
- **Same-user interference.** It is still out of scope (audit 10). The lock file is advisory; a same-user process can delete it or write files.
- **Revocation timing.** Revocation is synchronous for pending and future captures. A publish already running on the writer thread completes, and the directory removal runs after it. The removal waits behind other shares' queued work, which is not cancelled.

## 5. Hashes (sha256, payload)

- `.python-version` `5b02189ab1f9bb5caa7611320f35cd6a072da88db0533f62c4b3194f8bee4b79` (unchanged)
- `SublimeObserver.sublime-commands` `63940d84652e35b78b02225c91bf8b24bc5320de7af78211534222f64e5e4857` (unchanged)
- `SublimeObserver.sublime-settings` `449ad70ba465589e677dfb5e269599c9cb0ae7c2ce493fc91b3bf8be821b1d5d` (unchanged)
- `contract.py` `aed98299c12cb69c0cb93813eb2df803ee0894c830443851dc8be60a9721dfab` (was `d5ec4fb1…6551`)
- `publisher.py` `59fd8126e54e2821ad04fbca8f764a5b4129471471b828acbcdd5e6f832cf98f` (was `2ea61ba0…9847`)
- Task file `sublime-observer.md` `b196724342d62c198a1d2849b6a8dec6072564e88257bc41727baaeb64c948d2` (version 1.1)

Tests touched: `test_contract.py`, `test_publisher.py`, `test_witness_recorder.py`, `fakes.py` (`QueueWriter`), `reader.py`, `witness_recorder.py` (docstring, one field), `disposable_trial.py`, plus new `test_install_task.py`. `test_static.py` is unchanged: `fcntl` was never on its denylist. No `__pycache__` exists, the payload holds exactly 5 files, and no stray process is left. No git action was taken, and STATUS, RUNBOOK, ledger, `_bus/` and `witness/` are untouched.

---

# Step 5b — bounded revocation and test sensitivity, per the re-audit (_bus/10) and the head's verdict (_bus/14) (home, 2026-11-16)

Source: `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/` only. Task file untouched (version 1.1, sha256 `b1967243…48d2`, unchanged). The pre-5b source was snapshotted to a scratchpad only so the mutation run could compare old tests; that snapshot is not evidence.

## 1. What changed, per item

- **R1 — bounded revocation (done).** `contract.py`, 4 small edits:
  - `Store._pending`: a set of revoked share ids whose removal has not completed. `revoke()` adds to it inside the `_revoke_lock` section it already took. So the main thread gets no new lock acquisition and no file operation.
  - `heartbeat()` reads the clock **first**, then returns without writing if `not live` or any revocation is pending. It decides at execution time against the set that `revoke()` changes synchronously.
  - `remove_share` discards the id from `_pending` only after `_update_listing` (current off, index, directory, current to the remaining share) succeeded. On failure the existing `_stop_publishing` applies and pending stays (irrelevant, `live=False`).
  - Resume: unshare submits `remove_share` in the same main-thread call as the revoke. So the only heartbeats that get skipped are those queued *before* the unshare. Heartbeats queued after it run right after the removal and write at once, with no extra interval of waiting. Nothing new was added to the main thread.
- **R2 (done).** `test_queued_publish_then_unshare_close_or_sealed_save_writes_nothing` now wraps `contract.atomic_write` while the queue drains. It asserts that no write carries `QUEUED SECRET` and no `state.json` is written. Pre-5b version under `_is_revoked → False`: OK (blind). New version: FAIL.
- **R4 (done).** `publisher.py`:
  - `path_allowed` wraps `file_name()` in a try block. An exception unshares with `unshared, path unknown (<Type>)` and returns False. Every event route (`touched`, `saved`, `publish`) goes through it.
  - `_poll`: when `_poll_key` raises, it calls `path_allowed(view_id)`, so a raising `file_name()` revokes there too. A different raising API with a working `file_name()` keeps the old behavior (skip this tick).
  - Path latency (realpath on the main thread when the spelling changes) remains a stated limit.
- **Test sensitivity (done, partly by design).**
  - `test_simultaneous_start_in_threads_one_owner` collects every thread's exception and fails on any. Legitimate outcomes under this test's contention are exactly one `(True, …)` and `(False, "… does not publish")` for the rest. No Store shuts down in this test, so the lock file is never unlinked and the root never vanishes. The "kept being replaced / kept disappearing" `ContractError`s are therefore illegitimate here; they are legitimate only under shutdown churn (assay's 9,000-start run), which this test does not exercise. It also fails if a thread never answers.
  - New `test_shutdown_never_unlinks_a_lock_file_it_does_not_hold`: A's lock file is unlinked behind it, B locks a fresh file, A shuts down, and B's inode must still be at the path. No root needed.
  - **Left untested, as ordered:** the lock-file owner check (`st_uid != uid` needs a foreign-owned file, i.e. root) and `O_CLOEXEC`.
- **Disposable trial confinement (done).** `tests/disposable_trial.py`:
  - Removed: `all_pids()` and every `/proc` listing. The operator-editor probe is removed in **all** modes (it can only work by reading processes the trial did not start); `operator_editor_before/after` now read `not probed (step 5b)`.
  - Discovery walks `/proc/<pid>/task/<tid>/children` from the trial's own pid only. Each child is pinned with `os.pidfd_open` and re-confirmed under its parent. Liveness (`gone()`) and signals (`signal.pidfd_send_signal`) go through the pidfd, so the old `/proc/<pid>` existence checks are gone.
  - `_proc_path()` refuses any pid that is neither self nor pinned. `proc()` also refuses a pinned pid whose pidfd shows it exited, before and after reading.
  - The trial sets `PR_SET_CHILD_SUBREAPER`. The editor's double-forked `crash_handler` (step 5: ppid 1342, outside the tree) and the orphaned plugin host now stay in the trial's tree. Orphans are reaped at the end.
  - An audit hook records every `/proc` path opened or listed (a listing of `/proc` itself included); the report carries `proc_access`.
  - `X1_NO_OPERATOR_PROBES=1` now only skips the `/run/user/<uid>/sublime-observer` existence check, since nothing else remains to skip.
  - The trial now needs Python ≥ 3.9 on the host for pidfd (host: 3.14.7). The payload stays 3.8.

## 2. The revocation bound that now holds (stated precisely)

Let t_r be the instant `Store.revoke()` returns on the main thread. That is synchronous inside `unshare`, which is called by toggle, close, an invalid view, a sealed path or an unknown path. Let S = `stale_after_s` (3 × `heartbeat_s`, 3 s by default).

- **Until the removal completes,** every `heartbeat_at` written after t_r is earlier than t_r. The heartbeats that run then either skip (pending) or passed the check before t_r, and those read the clock before the check. **This includes the one heartbeat write already executing at t_r:** its file may land after t_r, but its stamp precedes t_r. So a rule-following reader whose liveness check runs at wall time T ≥ t_r + S gets `NotLive`. That holds for every share, by design: fail closed.
- **After the removal completes,** the revoked share's state, text, index entry and `current` are gone (Unavailable). Heartbeats resume for the remaining shares.
- **If removal fails:** `live=False`, no further heartbeat, and the same bound holds. If the removal hangs forever, the writer is stuck, so nothing is written, and the same bound holds.
- **Where it does not hold:**
  1. Before t_r. The operator's keypress or close reaches the callback after Sublime's own dispatch latency, which is unbounded here. For sealed paths, t_r is the *detection*: a save is forced at once, a changed spelling waits for the next event or poll (nominal 500 ms, no hard bound), and a symlink retargeted under an unchanged name while idle is never detected until a save or a capture (security-sibling limit).
  2. A reader whose liveness check ran before t_r + S and which keeps reading afterwards. There is no lease, and copied bytes cannot be recalled.
  3. A reader that skips the heartbeat rule, e.g. reading `views/<id>/` directly. For it, only removal completion counts.
  4. A wall clock stepped backwards between the stamp and the reader's check.
  5. R3: a second writer after the root was replaced behind a live holder. That is outside the same-user boundary.
  - The head's gate wording ("after the event") is true only if "event" means t_r.

## 3. Tests

- **Unit suite:** **105 run, 105 pass**, 4.3 s (98 before). Log: `evidence/unit-tests-5b.2026-11-16.txt`.
- **New tests (7):**
  - plugin: `test_heartbeat_queued_before_unshare_does_not_refresh_the_revoked_capture` (the re-audit's probe: publish, drain, queue a heartbeat, unshare, advance 10 s, run only that heartbeat; the reader gets NotLive/Unavailable, never the text)
  - plugin: `test_heartbeats_resume_after_removal_and_an_unrelated_share_reads_again` (B is NotLive while A's removal waits; after the drain the heartbeat equals now, B reads through `current`, and the cadence continues)
  - plugin: `PathUnknownTests` ×2 (5 event hooks via subTest; poll)
  - contract: `test_no_heartbeat_while_a_revocation_is_pending_and_again_after_removal`
  - contract: `test_heartbeat_in_flight_at_revoke_stamps_a_time_before_it` (the revoke lands during the clock read, and right after the pending check)
  - contract: `test_shutdown_never_unlinks_a_lock_file_it_does_not_hold`
- **Changed tests (2):** the R2 test and the thread test.
- **Unchanged:** `test_static.py`, `fakes.py`, `reader.py`, `test_install_task.py` and the witness files are byte-identical to pre-5b.
- **Mutation check:** script `evidence/mutation-check-5b.py`, output `evidence/mutation-check-5b.2026-11-16.txt`.
  - 7 payload mutations (r1a–e, r4a–b) and 3 sensitivity mutations (s1 publish ignores revocation, s2 contended losers raise, s3 shutdown unlinks without `_holds_path`): all caught, and the intended catcher is present in 10 of 10.
  - s1 and s2 rerun against the pre-5b test versions: both pass, confirming the old tests were blind.
  - 3 trial mutations (t1 scan every pid, t2 `_proc_path` guard removed, t3 no subreaper): each gives NOT CONFINED from `evidence/trial-confinement-check-5b.py`. Its foreign process is a `sleep` started by the runner itself.
- **Confinement self-check (no editor):** `evidence/trial-confinement-check-5b.2026-11-16.txt` → CONFINED. Only `self` and pinned children were touched, the double-forked grandchild was kept, and the foreign pid was refused by `proc`, `_proc_path` and `gone`.

## 4. Disposable trial

`X1_EVIDENCE_DIR=<bed>/implementation/evidence X1_EVIDENCE_PREFIX=disposable-trial-5b X1_NO_OPERATOR_PROBES=1 python3 -I -B tests/disposable_trial.py`. The editor came only from `/tmp/nablarva-observer-4215`.

- **Final run: 22 of 22 pass**, 155 s. Report `evidence/disposable-trial-5b.2026-11-16.json`, console `…5b.console.2026-11-16.txt`. Trial file sha256 `ddb0a92b…5966`.
  - `proc_access.entries_not_self_and_not_started`: `[]`, with 145 pinned pids. `started_processes_still_running`: `[]`. The trial root was removed.
  - `crash_handler` ppid is inside the trial tree (step 5: 1342).
  - Check 11/11b orphan and reader windows match step 5 within 0.1 s (11: 7.28 s vs 7.19 s; 11b: reader window 2.54 s vs 2.57 s).
  - a2-restart again ignored `exit` and needed SIGTERM after 20 s. This is the known step-2b behavior, identical in the 2b, 3a and 5 runs.
- **Superseded runs (kept):**
  - `…5b.run1-check17-nameerror…`: 21/22. Check 17 hit a NameError I introduced: a `for key, gone in` loop in `main()` shadowed the new `gone()` helper. The loop variable was renamed.
  - `…5b.run2-pre-final-audit-hook…`: 22/22, before the audit hook also recorded a listing of `/proc` itself.

## 5. Flagged, not acted on

- One of my commands was denied by the permission layer before it ran. It included `pgrep -a sublime`, which would have listed the operator's editor; that was my mistake against the brief. Nothing executed, and the rerun omitted it.
- The fail-closed side effect is real: one stuck removal makes every share look not live until it completes or fails. The head accepted this.
- `_poll` with a raising non-path API still just skips the tick (the share stays shared). That is unchanged and outside R4.

## 6. Hashes (sha256, payload)

- `contract.py` `fc8d951bc31c7543259e6edde207a21322c78854789df28268dfbaa116489eef` (was `aed98299…dfab`)
- `publisher.py` `f519aec57e196cf9c20f42c0a91b77f428615c96ab7ac7ef49cf0342fd06f8b2` (was `59fd8126…f98f`)
- `.python-version`, `.sublime-commands`, `.sublime-settings`: unchanged (`5b02189a…`, `63940d84…`, `449ad70b…`).
- Both payload `.py` files parse as Python 3.8. The payload holds exactly 5 files, and no `__pycache__` exists.

No git action. STATUS, RUNBOOK, ledger, `_bus/`, `witness/`, README and the task file are untouched. No background process is left.

---

# Step 5c — removal submitted before any editor notification, per _bus/16 section 2 and the head's verdict (_bus/17) (home, 2026-11-17)

Source: `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/` only. The pre-5c source was snapshotted to a scratchpad only so the mutation run could use the pre-5c tests. That snapshot is not evidence. `contract.py` is unchanged, and no change to it was needed.

## 1. What changed

- **`SublimeObserver/publisher.py`, `_Runtime.unshare`, lines 212–226** (was 210–224). The `writer.submit(store.remove_share, …)` call now sits at line 216, inside the same `if self.store is not None:` block as `revoke()` (line 215). So it runs right after the revoke and before any editor call. `debouncer.cancel` stays at 217; it is in-memory only and not a notification. `erase_status` (218–221) was already guarded. `sublime.status_message` (222–226) is now inside `try/except Exception: pass`. No other line of the payload changed.
- **Effect:** if a notification raises, the removal is still queued, and nothing propagates into the editor. Notifications are now best effort only.

## 2. Routes that revoke (all go through `unshare`; line numbers after the change)

| Route | Call site | Notification calls after revoke |
|---|---|---|
| Toggle unshare | `toggle`, publisher.py:189 | erase_status, status_message `unshared` |
| Path unknown (raising `file_name()`) on events, save, publish | `path_allowed`, publisher.py:238 (reached from `touched` 254, `saved` 261, `publish` 283) | erase_status, status_message `unshared, path unknown (…)` |
| Path unknown at the poll | `_poll` except, publisher.py:341 → `path_allowed` 238 | same |
| Sealed path (event, forced save, publish, changed path at the poll via `touched`) | `path_allowed`, publisher.py:244 | erase_status, status_message `unshared, <reason>` |
| Close | `closed`, publisher.py:271 | erase_status only (`why == 'closed'`) |
| Invalid view at publish | `publish`, publisher.py:281 | erase_status only |
| Invalid view at the poll | `_poll`, publisher.py:336 | erase_status only |

On all seven routes, the removal is submitted at line 216, before either call. No route has a console print (`_log`) between revoke and submission.

These are not revocation routes and are unchanged:
- `_stopped` (writer `Stopped`) clears shares without revoke or removal, because the store is already `live=False`.
- `stop()` (shutdown path, not ordered).
- `toggle`'s `refused to share` message at line 201 is for a view that was never shared.

## 3. Tests (`tests/test_publisher.py`, class `RevocationTests`)

- **`test_failing_notification_on_revoke_still_queues_the_removal`** (lines 447–491).
  - Five routes as subTests: unshare, sealed save, path unknown, close, invalid at the poll. Each route gets a fresh QueueWriter runtime, so a stuck share cannot carry into the next route.
  - Each subTest shares and drains, then makes both `sublime.status_message` and the view's `erase_status` raise, and acts.
  - After the drain it asserts: the share is gone from runtime shares, `store._pending == set()`, the share directory is gone, the heartbeat stamp equals now after 1.01 s, and `reader.publisher` accepts. The last assertion is that nothing propagated.
  - The sealed route uses the synthetic `/srv/app/.env.local`, not a vault spelling.
- **`test_two_pending_revocations_hold_the_heartbeat_until_both_removals_complete`** (lines 493–521).
  - Shares A and B, drains, then unshares A by toggle and B by close. It asserts the queue is exactly `[remove_share(A), remove_share(B)]`, then advances 10 s.
  - It runs only A's removal: A's directory is gone and B's remains. A direct heartbeat leaves the stamp unchanged, and `reader.publisher` gives NotLive.
  - Then B's removal runs and a heartbeat writes now.
- **Unit suite:** `python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests -v` → **107 run, 107 pass**, 4.4 s (105 before). Log: `evidence/unit-tests-5c.2026-11-17.txt`.
- **Mutation check:** script `evidence/mutation-check-5c.py`, output `evidence/mutation-check-5c.2026-11-17.txt`. Each mutation runs on a temporary copy of the source with the full suite.
  - **baseline:** 107 OK.
  - **m1, exact pre-5c `unshare` body restored:** FAIL in 3 subTests (unshare, sealed save, path unknown). Each fails at the `_pending` assertion, which is the defect itself: the share stays pending. Close and invalid-at-poll pass under m1, as expected, because they call no unguarded notification.
  - **m2, new order but `status_message` unguarded:** FAIL in the same 3 subTests, at `assertIsNone(raised)`. The removal happens, but the exception reaches the editor.
  - **m3, `remove_share` clears all pending ids (`_pending.clear()`):** FAIL in `test_two_pending_…` (`1010.0 != 1000.0`, the heartbeat wrote between the two removals). The same mutation against the **pre-5c test suite: 105 OK, nothing caught**. This confirms assay's 5b finding.
  - An earlier run of m1, before each subTest got a fresh runtime, also failed close and invalid-at-poll, but only through a share left pending by an earlier subTest. That run was superseded; its output was overwritten and not kept.
- **Hash pins:** no test, and not the task file, pins a payload hash (grep for hex digests, `hashlib`, `digest` in `tests/*.py` except the witness recorder's own text hashing; grep in the task file). `test_install_task.py` is unchanged.

## 4. Disposable trial

`X1_EVIDENCE_DIR=<bed>/implementation/evidence X1_EVIDENCE_PREFIX=disposable-trial-5c X1_NO_OPERATOR_PROBES=1 python3 -I -B tests/disposable_trial.py`, run from the source root. The editor came only from `/tmp/nablarva-observer-4215`.

- **22 of 22 pass**, 155 s. Report: `evidence/disposable-trial-5c.2026-11-17.json`. Console: `evidence/disposable-trial-5c.console.2026-11-17.txt`.
- `installed_equals_payload: true`.
- `proc_access.entries_not_self_and_not_started: []`, with 147 pinned pids.
- `cleanup.started_processes_still_running: []`.
- `run_user_sublime_observer_exists: skipped`.
- The trial root was removed.
- The trial file is unchanged (`ddb0a92b…5966`). The trial exercises unshare and close in the real editor, but not a raising notification. The new path is unit-test evidence only.

## 5. Flagged, not acted on

- `toggle` share route, lines 204–207: the share is put into `self.shares`, then `set_status` and `status_message` run unguarded before `publish` and `_arm_poll`. If either raises, the view counts as shared but is not published until its next event. The poll may also not be armed. This fails closed, since nothing is written, but it is the same class of issue on a non-revoking route. Outside the order.
- With the real threaded Writer, the removal may now start on the writer thread while the main thread is still setting the status bar. Neither depends on the other (inferred).

## 6. Hashes (sha256, payload)

- `contract.py` `fc8d951bc31c7543259e6edde207a21322c78854789df28268dfbaa116489eef` (unchanged)
- `publisher.py` `0fb95e5c9509dd89786f41e2c4b9c133c620b04b9e0d51a1be5cac959e4d30cb` (was `f519aec5…f8b2`)
- `.python-version`, `.sublime-commands`, `.sublime-settings`: unchanged (`5b02189a…`, `63940d84…`, `449ad70b…`).
- `tests/test_publisher.py` `4b226bb445a6d96b2c131b97969333c4bda54f03d047f52bb93e0431f81cf71f`. All other test files are byte-identical to pre-5c.
- The payload holds exactly 5 files, and no `__pycache__` exists.

No git action. STATUS, RUNBOOK, ledger, `_bus/`, `witness/`, README, the install task and `contract.py` are untouched. No install, `run.sh` call or deploy. No background process is left. The operator's editor and its profile were not listed, probed or touched.
