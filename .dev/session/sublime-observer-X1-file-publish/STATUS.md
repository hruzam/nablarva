# STATUS: sublime-observer-X1-file-publish

```yaml
updated: 2026-11-17 (step 5c verified; code frozen for the smoke; smoke pending with majkee)
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
  version 1.0. Audit chain — Codex audit (_bus/07) → VERDICT (08) → step 5 → assay → Codex
  re-audit (10) → VERDICT (14) → step 5b → assay → Cartan's narrow confirmation (16; R1
  fixed, "sound with named conditions") → VERDICT (17) → step 5c → assay PASS WITH GAPS, no
  blocker or major (implementation/assay.verdict-step5c.2026-11-17.md): 107 unit tests;
  removal is submitted right after revoke on all seven revoking routes; notifications
  raising on six routes with the real writer thread left nothing pending; 9 of 10 mutants
  caught; disposable trial re-run by assay, 22 of 22. Code now frozen for the smoke:
  contract.py sha256 fc8d951bc31c7543259e6edde207a21322c78854789df28268dfbaa116489eef,
  publisher.py 0fb95e5c9509dd89786f41e2c4b9c133c620b04b9e0d51a1be5cac959e4d30cb,
  .sublime-settings 449ad70b…1d5d, .sublime-commands 63940d84…4857, .python-version
  5b02189a…4b79. Cartan audited publisher.py f519aec5…f8b2; the 5c change (one reordering in
  _Runtime.unshare, one try block) was verified by assay only. Task file version 1.1.
  Nothing is installed on home (checked on disk 2026-11-17); the smoke has not started.
in_flight: none
recovery_probe: |
  ls -la /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/witness/
  ls -la /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/
  ls -la /home/hruzam/.config/sublime-text/Packages/
  # witness/recording-3.jsonl present and majkee said "smoke done": spawn assay on it, on
  # SMOKE.md (his notes) and on _bus/12 and 13; also have assay compare the installed five
  # files with the frozen hashes above. Recordings are large: never Read them whole.
  # Packages/SublimeObserver present but no "smoke done": the walk is under way; wait.
holds:
  - Only majkee runs the install steps, run.sh update, mark or unmark for this task, and only he acts in the live editor and runs the recorder against the real publication directory.
  - Witness with synthetic files under /tmp/sublime-observer-witness/ only (the smoke uses a fake sealed folder .hlm there; not a vault); keep that folder until the gate.
  - Never signal, list or launch against the operator's editor (no pgrep or ps for it by agents).
  - Do not edit the X0 bed termbrana-sublime-observer, its STATUS, or the termbrana-M0 session.
  - No git stage, commit or push by an agent seat. In ia-sync only the two install-pkgs files are ours; no deploy.
  - One source — toolbox/sublime-observer/. The bed copy is frozen evidence. Any further code change before the gate changes the hashes and voids the smoke; the remaining minor gaps are left for after the gate.
  - This seat stays the single STATUS writer.
  - Automation stays manual until majkee's GO on the gate, then auto with a version bump.
  - The task file carries majkee's pasted outputs between its sections; they stay until closure, when they move to the bed.
  - Reader contract in force — root holds publisher.lock (readers ignore), publisher.json, index.json, `current` (symlink, only with exactly one share), views/<share_id>/state.json and text.<share_id>.<revision>. Read — publisher.json (heartbeat live; note epoch); resolve `current` once; state.json (epoch and share_id match); the named text file in the same directory (missing → state again); state again (epoch, share_id, seq unchanged → good). Valid only at the checked instant; no freshness promise at return. Times are Unix seconds. The reference reader calls a heartbeat stale when its age is greater than stale_after_s (equality passes); _bus/11 says "younger than", stricter and harmless; the closure README states it as the reader implements it. _bus/01 is superseded by _bus/11.
  - Gate sentence (VERDICT 17) — "After unshare or close has registered in the editor, a reader that checks liveness more than stale_after_s (3 s by default) later does not get that share — its files are removed or the heartbeat is stale. After the publisher process has ended, the same limit applies to every share. Removal normally completes far sooner, without a deadline." Conditions — the reader follows the full rule and checks liveness at that instant; the wall clock does not step back; no one replaces the runtime directory behind the publisher. Not covered — the time before the editor registers the action; a path that became sealed without an event (a changed name waits for an event or the 500 ms poll; a symlink retargeted under an unchanged name while idle is never detected); bytes already read; restart or unload initiation as such (bounded only once shutdown completes or the process ends).
  - Side effect of 5b — while one share's removal is pending, all shares look "not live"; after a removal failure the publisher stops with a console line until reload.
  - Limits of 1.1 to state at the gate — a publisher starting during another's shutdown refuses for its whole life; a lock descriptor inherited through a bare fork blocks the next start; save-as into a sealed path not yet shown in the real editor (smoke S8); main-thread path resolution has no latency bound.
  - Minor or note, open, left until after the gate — the tests cannot catch "removal submitted before revoke" (code is correct); the share route of toggle (publisher.py:204–207) has unguarded notifications, so a raising one leaves a share unpublished until its next event (fails safe); contract error under extreme start contention; lock-file owner check and O_CLOEXEC without catching tests; a silently dead writer thread fails closed but logs nothing (inferred); stop() does not silence an executing heartbeat.
  - What the 1.0 witness still stands for — install and removal mechanics, live load and unload, plugin host 3.14.6, reads by path under the agents' modes. Publish, unshare, quit, crash and fresh reads of the new code rest on the smoke.
  - Editor-disturbance evidence — static test (a denylist); disposable trial; first recording steps 3 and 4; majkee's eyes; repeat recording (selection identical through a second-view edit). Smoke S3 adds the shared view scrolled to the middle. Not shown — focus; large-buffer latency; main-thread path work added in step 5; the cause of the visible_region halving in the repeat (asked of majkee, unanswered). Gate claim — "no publication-attributable focus, selection or scroll disturbance was observed in the specified synthetic scenarios on this host and build". Majkee has an edge-case idea of his own, not yet told.
  - Fresh reads — on 1.0 Codex ran in "Approve for me" (majkee's usual mode). SMOKE.md asks him to note the Codex mode; gate wording follows what he used.
  - Recorder defects, not reachable with the real publisher, not fixed — a non-string text_file_encoding blanks a whole sample; no size cap on scanned files; heartbeat age field absent while stale.
  - Trust boundary, to state at the gate — the toggle authorises an evolving plaintext copy readable by every process of the same user, with no recipient bound; a secret pasted later is published without a new decision; unshare cannot recall copies already read; a same-user process can interfere with the runtime directory (including replacing the root behind the holder, which allows a second writer).
  - For the ledger at close — a security sibling on this line (scope from _bus/05 section 2, audit finding 6, path identity under symlink retarget); not yet dispositioned by majkee. The parked channels item is already on the ledger.
  - Closure fixes — toolbox README (contract section as above, limits, install pointer, commit pins, trust boundary); task file cleaned of notes; ledger X1 line is stale until close.
  - Still owed to majkee, reversible — toggle refuses vault and .env paths (keep); unreadable publisher.json blocks until removed by hand (kept).
  - Not X1 work (houston) — a general toolbox-module definition, a shared installer, registry publication.
  - Unverified — Python 3.8 execution; hosts other than home; several agents reading at once; a notification raising in the real editor.
  - Still to come — smoke and its assay check; closure documentation diff with a Houston consult; majkee GO or STOP; ledger update at close.
next: >-
  Majkee installs 1.1 (first-install path in install-pkgs/sublime-observer.md), walks
  witness/SMOKE.md and says "smoke done". The fresh-read prompts in SMOKE.md point at _bus/11.
expected: >-
  witness/recording-3.jsonl with stamps S1 to S11, _bus/12.claude.return.md,
  _bus/13.codex.return.md, Packages/SublimeObserver with five files whose hashes equal the
  frozen ones in the checkpoint.
```
