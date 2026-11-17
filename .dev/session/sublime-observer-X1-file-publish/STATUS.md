# STATUS: sublime-observer-X1-file-publish

```yaml
updated: 2026-11-16 (step 5b verified; Cartan confirmation and smoke pending; clock not read)
writer: oraculum · claude
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · 9b3f206 · dirty:
  .dev/session/vist-X0-helloWorld/raw/decision.majkee.witness.2026-11-14.md (not ours),
  .dev/session/pulse.md (router row for this bed),
  untracked .dev/session/sublime-observer-X.ledger.md,
  .dev/session/sublime-observer-X1-file-publish/ and toolbox/sublime-observer/.
  /home/hruzam/ia-sync · main · 6bccbca · ours: install-pkgs/README.md (modified, one entry),
  install-pkgs/sublime-observer.md (untracked; version 1.1, sha256 b1967243…48d2; also
  carries majkee's pasted witness notes, to be moved out at closure); not ours and dirty
  before us: claude/agents/trajectory.md, claude/settings.json,
  .dev/session/helper-utils-00-tmux/, claude/hooks/statusline.sh.
gate: >
  Majkee records GO or STOP on an independently verified home-host publisher. For
  operator-toggled synthetic views in the normal Sublime profile, a fresh Claude Code
  session and a fresh Codex session each read a consistent text-and-state capture by
  absolute path under their default sandboxes; unshared views publish nothing; unshare,
  close, restart and an editor crash leave no capture presented as current; focus,
  selection and scroll are unchanged by publishing; install and removal follow a reviewed
  install-pkgs task; the trust boundary and remaining limits are stated.
checkpoint: >-
  Steps 1 to 4a verified by assay; real-editor witness and repeat verified PASS WITH GAPS on
  version 1.0. Audit chain — Codex audit (_bus/07) → VERDICT (08) → step 5 → assay PASS WITH
  GAPS → Codex re-audit (10) → VERDICT (14) → step 5b → assay PASS WITH GAPS, no blocker or
  major (implementation/assay.verdict-step5b.2026-11-16.md): 105 unit tests; with a real
  writer thread no revoked capture passed the live check at or after revoke + stale bound in
  400 rounds; no stuck-pending path found; lock exclusivity and pairing unchanged; disposable
  trial judged confined and re-run by assay, 22 of 22. Current code: contract.py sha256
  fc8d951b…9eef, publisher.py f519aec5…f8b2; task file version 1.1. Nothing is installed on
  home; the smoke has not started. Ready for majkee: _bus/15.oraculum.point.md (narrow
  confirmation by Cartan, return 16) and witness/SMOKE.md with _bus/11 (fresh-read task,
  returns 12 and 13). The head advised 15 first, smoke after a clean 16.
in_flight: none
recovery_probe: |
  ls -la /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/
  ls -la /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/witness/
  ls -la /home/hruzam/.config/sublime-text/Packages/
  # _bus/16.codex.return.md present: read it; disposition goes into _bus/17. Open findings
  # → trajectory, assay; the smoke waits (or is repeated if already walked).
  # witness/recording-3.jsonl present and majkee said "smoke done": spawn assay on it, on
  # SMOKE.md (his notes) and on _bus/12 and 13; also compare the installed five files with
  # the source hashes above. Recordings are large: never Read them whole.
holds:
  - Only majkee runs the install steps, run.sh update, mark or unmark for this task, and only he acts in the live editor and runs the recorder against the real publication directory.
  - Witness with synthetic files under /tmp/sublime-observer-witness/ only (the smoke uses a fake sealed folder .hlm there; not a vault); keep that folder until the gate.
  - Never signal, list or launch against the operator's editor (no pgrep or ps for it by agents).
  - Do not edit the X0 bed termbrana-sublime-observer, its STATUS, or the termbrana-M0 session.
  - No git stage, commit or push by an agent seat. In ia-sync only the two install-pkgs files are ours; no deploy.
  - One source — toolbox/sublime-observer/. The bed copy is frozen evidence. Any further code change before the gate changes the hashes and voids a smoke already walked; minor test gaps are therefore left for after the gate.
  - This seat stays the single STATUS writer.
  - Automation stays manual until majkee's GO on the gate, then auto with a version bump.
  - The task file carries majkee's pasted outputs between its sections; they stay until closure, when they move to the bed.
  - Reader contract in force — root holds publisher.lock (readers ignore), publisher.json, index.json, `current` (symlink, only with exactly one share), views/<share_id>/state.json and text.<share_id>.<revision>. Read — publisher.json (heartbeat younger than stale_after_s; note epoch); resolve `current` once; state.json (epoch and share_id match); the named text file in the same directory (missing → state again); state again (epoch, share_id, seq unchanged → good). Valid only at the checked instant; no freshness promise at return. Times are Unix seconds. _bus/01 is superseded by _bus/11.
  - Gate sentence, as verified by assay — "After unshare or close has registered in the editor, or after a crash, no capture passes the live check later than the stale bound (3 s by default); removal normally completes far sooner but that is not guaranteed." It does not cover — the time before the editor dispatches the operator's action; a sealed path found late (a changed name waits for an event or the 500 ms poll; a symlink retargeted under an unchanged name while idle is never detected); a reader that checked liveness earlier or skips the rule; a wall clock stepped back; a restart or unload where the process dies while a heartbeat is blocked behind a slow publish (minor, inferred); a second writer after the root was replaced behind the holder.
  - Side effect of 5b — while one share's removal is pending, all shares look "not live"; after a removal failure the publisher stops with a console line until reload.
  - Limits of 1.1 to state at the gate — a publisher starting during another's shutdown refuses for its whole life; a lock descriptor inherited through a bare fork blocks the next start; save-as into a sealed path not yet shown in the real editor (smoke S8).
  - Minor, open, left until after the gate — no test for two simultaneous pending revocations; contract error under extreme start contention; lock-file owner check and O_CLOEXEC without catching tests; a silently dead writer thread fails closed but logs nothing (inferred).
  - What the 1.0 witness still stands for — install and removal mechanics, live load and unload, plugin host 3.14.6, reads by path under the agents' modes. Publish, unshare, quit, crash and fresh reads of the new code rest on the smoke.
  - Editor-disturbance evidence — static test (a denylist); disposable trial; first recording steps 3 and 4; majkee's eyes; repeat recording (selection identical through a second-view edit). Smoke S3 adds the shared view scrolled to the middle. Not shown — focus; large-buffer latency; main-thread path work added in step 5; the cause of the visible_region halving in the repeat (asked of majkee, unanswered). Gate claim — "no publication-attributable focus, selection or scroll disturbance was observed in the specified synthetic scenarios on this host and build". Majkee has an edge-case idea of his own, not yet told.
  - Fresh reads — on 1.0 Codex ran in "Approve for me" (majkee's usual mode). SMOKE.md asks him to note the Codex mode; gate wording follows what he used.
  - Recorder defects, not reachable with the real publisher, not fixed — a non-string text_file_encoding blanks a whole sample; no size cap on scanned files; heartbeat age field absent while stale.
  - Trust boundary, to state at the gate — the toggle authorises an evolving plaintext copy readable by every process of the same user, with no recipient bound; a secret pasted later is published without a new decision; unshare cannot recall copies already read; a same-user process can interfere with the runtime directory.
  - For the ledger at close — a security sibling on this line (scope from _bus/05 section 2, audit finding 6, path identity under symlink retarget); not yet dispositioned by majkee. The parked channels item is already on the ledger.
  - Closure fixes — toolbox README (contract section as above, limits, install pointer, commit pins, trust boundary); task file cleaned of notes; ledger X1 line is stale until close.
  - Still owed to majkee, reversible — toggle refuses vault and .env paths (keep); unreadable publisher.json blocks until removed by hand (kept).
  - Not X1 work (houston) — a general toolbox-module definition, a shared installer, registry publication.
  - Unverified — Python 3.8 execution; hosts other than home; several agents reading at once.
  - Still to come — Cartan's confirmation (16) and head VERDICT (17); smoke and its assay check; closure documentation diff with a Houston consult; majkee GO or STOP; ledger update at close.
next: >-
  Majkee carries _bus/15 to Cartan · Codex and tells the head when _bus/16 exists; if clean,
  he installs 1.1, walks witness/SMOKE.md and says "smoke done".
expected: >-
  _bus/16.codex.return.md with 105 tests, the two hashes, R1 confirmed or an interleaving,
  and a closing opinion. After the smoke — witness/recording-3.jsonl with stamps S1 to S11,
  _bus/12.claude.return.md, _bus/13.codex.return.md, Packages/SublimeObserver with five files.
```
