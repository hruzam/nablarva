---
kind: planning check "relay tests" — one of the four checks of prompt-0, step 1; on paper, nothing started
by: child of the lead (trajectory, claude, Opus 5.5) · 2026-11-27 · host home · branch core at cda56e5
read: RUNBOOK; release-and-go; gate remarks; research verdict (Verdict, §3, §6, §9, §10, Erratum 1); relay-X.ledger.md "Open";
  relay-X1-probes packet.md to packet-4.md; master.symmetry §8; note.symmetry §1.1–1.3, §3; blind answer §8–9; flag.md L4, L12,
  L14, L21, docket; PROJECT.yaml; file-poke.md; toolbox/sublime-observer/tests/disposable_trial.py (header only)
ran: tmux -V (3.7c) · codex --version (0.172.0) · codex --help · codex queue --help · claude --version (2.1.332) · claude --help ·
  git worktree list (one: the main checkout) · ls · command -v (bwrap present, inotifywait absent, python3 3.14.7)
---

# 0. What I would do differently — said first

1. **Prove the sandbox before any agent runs, and prove it by construction, not by checking the living folders.** The
   living seats write to `~/.codex` and `~/.claude` all the time, so a before/after check of them can never be clean.
   The repository already has the stronger pattern: `disposable_trial.py` (sublime-observer) runs its subject under
   bwrap (bubblewrap, a Linux tool that gives a process its own view of the filesystem) with a blank `$HOME`. Do that.
2. **Two tiers, and only the cheap one loops automatically.** An offline tier (the parsers that read session records,
   the guards, the pass/fail logic, fed with synthetic records) runs on every save and costs nothing — that is the
   "automatic looping tests" Majkee knows from web work. The live tier starts real CLIs, costs tokens, and runs on
   demand under a cap (§6).
3. **The first three tests use only Codex as recipient, through `codex queue`.** It is the one carrier that needs no
   typing. Every Claude-recipient case of the running bridge is a paste plus Enter into a pane — typing (§5).
4. **Never reuse a session after a chooser or an aborted turn.** Packet 4 §5: both pointers accepted and never seen
   followed an aborted turn. A reused session would carry that history into the next test. One fresh session per test.
5. **Do not automate the answer to a chooser** (the approval menu Codex shows a human). Fact three — a real request for a
   human's decision is outstanding — can be shown by holding the chooser and then killing the sandbox, unanswered.
6. **Credentials are the likeliest blocker, not tmux.** Settle §2.3 with Majkee before code is written.

# 1. Worktree and branch

- **Path and branch** (names proposed; no collision found for `relay-tests`, `relaytest`, `nablarva.wt` in tracked files):
  `git -C /home/hruzam/unikuklatrix/nablarva worktree add -b relay-tests /home/hruzam/unikuklatrix/nablarva.wt/relay-tests core`.
  `nablarva.wt/` is a sibling folder that holds one worktree per second development — the answer to "when we can have
  second development, needs it own worktree" as a pattern, not a one-off. A worktree is a second checkout of the
  same repository on its own branch; L12 (the repository lock: one repo, branch `core`, plain pull and push, parallel
  work through `git worktree`) names it as the way.
- **What lives where — one rule.** In the worktree the branch changes **only** `toolbox/relaytest/` (code, its unit
  tests, synthetic fixtures, a README). The worktree's copy of `.dev/session/` is a stale snapshot and is never edited:
  two editable copies of a STATUS are two authorities, which L9′ (one doing-state per session) forbids. The bed —
  RUNBOOK, STATUS, decisions, `_bus/`, and a `runs.md` with one row per live run (run id, tool commit, CLI versions,
  result per fact, durations, token counts, SHA-256 of the private bundle) — lives on `core` in the main checkout.
  That answers "how we should treat tests in session worktree": code in the worktree, evidence summary in the bed,
  raw evidence private.
- **Private run artifacts** go to `/home/hruzam/.local/share/nablarva/relaytest/runs/<UTC-stamp>-<random>/`, folders 0700,
  files 0600, the pattern of the custody folders in the ledger. The runner refuses a run root inside any Git worktree
  (as `c04-custody.py` does) and deletes the copied credential file at teardown.
- **Back to core, never rebase, never force:** push the branch plainly (`git push -u origin relay-tests`); take up core
  inside the worktree with `git merge core`; return from the main checkout with `git pull` then
  `git merge --no-ff relay-tests` then `git push`. Before the merge, `git diff --name-only core...relay-tests` must list
  only `toolbox/relaytest/` — otherwise stop. Commits and pushes go through the controller on a POINT, as now.
  Afterwards `git worktree remove`; delete the branch only with `git branch -d`, never `-D`.

# 2. The sandbox

1. **Its own tmux server on a socket inside the run root:** `tmux -S <run>/tmux.sock -f /dev/null …`. `-S` names the socket
   by path, so the guard can check it; `-f /dev/null` keeps Majkee's tmux configuration and plugins out — a session-saving
   plugin would otherwise record the throwaway sessions into his living setup.
2. **Each CLI starts inside bwrap:** a blank tmpfs over `/home/hruzam` and over `/run/user/1000`, the run root bound back in
   as the sandbox `$HOME`, binaries read-only, network kept (the CLIs need their API). Inside:
   `HOME`, `CODEX_HOME=$HOME/.codex`, `CLAUDE_CONFIG_DIR=$HOME/.claude`, `XDG_*` under `$HOME`, `TMPDIR` private,
   `TMUX` and `TMUX_PANE` unset; working folder `$HOME/work`, which is in no Git repository, so neither CLI picks up an
   `AGENTS.md` or `CLAUDE.md` from above it. `codex queue` is run **inside the same bwrap**, by the same wrapper.
3. **Credentials — open, his call.** A blank home has no login. Options: (a) API keys for both vendors, passed in the
   environment (Claude's `--bare` mode then also skips hooks, memory and CLAUDE.md, which is cheaper); (b) a copy of the
   subscription token files into the sandbox home. For (b) I could not determine whether a token refresh inside the
   sandbox rotates the shared refresh token and logs the living seats out. I would not take (b) without that known.
4. **What `codex queue` addresses** (help text): `--thread` takes a "Session UUID or exact session name"; `-p` reads
   `$CODEX_HOME/<name>.config.toml`, so `CODEX_HOME` is honoured. Use UUIDs only, read from the sandbox's own session
   record, and refuse any UUID that is not in the sandbox's `sessions/`. **Not determinable without running:** where an
   accepted message is stored; whether a running app-server daemon of the living side (default socket under
   `$HOME/.codex/app-server-control/`, note.symmetry §1.3) would be found — the blank home should hide it; whether
   Claude's live-session listing and messaging between Claude sessions reach across the sandbox through an abstract
   socket, which a filesystem sandbox does not hide (only a separate network namespace would); whether Codex's own
   workspace sandbox runs inside bwrap; which first-run dialogs (trust, onboarding) a blank home brings up.
5. **Teardown** kills only that server (`tmux -S <run>/tmux.sock kill-server`; bwrap `--die-with-parent`); asserts no socket, no process.
6. **Guard:** one wrapper is the only way the code calls tmux, and it always adds `-S <run>/tmux.sock`; it refuses a socket
   outside the run root, any socket under `/tmp/tmux-1000/` (where the default server lives), and a socket that existed
   before the run. An offline unit test reads the tool's own source and fails on any tmux call outside the wrapper and
   on `send-keys` or `paste-buffer` anywhere — the L4 line enforced as a test until Majkee signs otherwise.

# 3. Language and runner

- **Pending:** v1 language is docket item 2 (Python stdlib or C++, "only majkee weighs"); `PROJECT.yaml`: `lang: TBD`.
- **What the repository does for helpers and tests:** Python 3 standard library throughout — `relay-X0-carryover/scripts/`
  (two custody tools), `toolbox/sublime-observer/tests/` (unittest, `subprocess`, a disposable trial), the probe
  qualifiers of other beds; `toolbox/termbrana/` is Rust, forced by its plugin host (L11 says it does not pre-decide docket 2).
- **Proposal:** Python 3 stdlib, `unittest`, no packages. Runner: `python3 -m unittest discover toolbox/relaytest/tests` for
  the offline tier; `python3 toolbox/relaytest/run.py --live T0 T1 T2` for the live tier; `run.py --watch` re-runs the
  offline tier when a file changes (polls modification times — `inotifywait` is not installed). No daemon, no cron.
- **Point for his signature:** that test tooling in Python stdlib does not decide docket 2, as L11 said for Rust.

# 4. The first three tests

| | **T0 sandbox-proof** | **T1 codex-wake-and-read** | **T2 codex-chooser-outstanding** |
|---|---|---|---|
| Does | starts the server and one plain shell pane in bwrap; the pane writes its environment, `ls` of the real `~/.codex` and `~/.claude` paths, `codex --version`, `codex login status`, and `codex queue` to a random UUID into files; tears down | starts `codex` in bwrap with the smallest model, `-s workspace-write -a never`, a launch prompt (no typing): "on a pointer, read the file it names and do what it says"; waits for the first turn to end; writes `point.md` holding a nonce; sends `codex queue --thread <uuid> --message "[poke t1] read <abs>/point.md"` — the nonce is in the file only; the file asks for `receipts/<nonce>.txt` | fresh session, `-a on-request -c approvals_reviewer="user"`; pointer 1 names a file that asks for a write outside the working folder; after the chooser stands, pointer 2 (receipt only, nonce 2); holds 60 s; kills the server without answering |
| Pass reads | the files written inside: sandbox `HOME`, real paths absent, `TMUX` unset, the queue call refused; then socket gone, no process left | three facts apart: **accepted** — exit 0 and `Queued message <id>`; **arrived** — the session record (`$CODEX_HOME/sessions/…/rollout-*.jsonl`, Codex's own log of a session) holds the pointer as an input and a turn start; **read** — a tool call on `point.md` and a receipt with the file's nonce. Also the record's token counts | pointer 1 accepted, arrived, read; **outstanding** from three sources kept apart: the record holds the escalation request and no result while held; the raw terminal stream (tmux `pipe-pane`) carries an OSC 7501 "blocked" (a status code the program writes into the terminal itself); `capture-pane` shows the chooser. Pointer 2: accepted; arrived or not |
| Unknown | a step that could not run (no login, dialog at start) — reported as which step | accepted, nothing in the record by the deadline (180 s): UNKNOWN, never FAIL — the shape of E2 and E3 | any of the three sources missing or disagreeing is reported as such; pointer 2 not arriving is the expected UNKNOWN of E3 |
| Fail | anything of the real home visible, a tmux call off the run socket, a leftover process | carrier error, wrong nonce, receipt without a read of the file | sandbox breach; a chooser answered by anything |
| Time, roughly | 5–10 s | 1–2 min | 3–5 min |

The record's event names are pinned from T1's first capture, not assumed here. Every run is a planned sample: it never
enters the count of operator interventions (the verdict's falsifier) and qualifies nothing.

**Next, in order, not first:** T3 the same as T2 with `approvals_reviewer="auto_review"` (the automatic reviewer; costs
its own tokens) · T4 a routine exchange's cost, from T1's token counts over N runs · T5 a Claude recipient · T6 the
paste-burst question. T5 and T6 type into a pane (§5). The manual fallback is a human typing by definition and is not
automated; only its look-first check can be tested, offline, against captured frames.

# 5. What is not automated, and where X3 begins

- **Never:** any tmux command against the default server; any keystroke into a living pane; any write into the real
  `~/.codex` or `~/.claude`; any wording in a run report that a door is qualified or a carrier chosen — the carrier is
  Majkee's (verdict §7; D1, the base-layer lock of L14, parks `codex queue` as a vendor door).
- **Typing into a sandbox pane** — dismissing a first-run dialog, answering a chooser, the paste plus Enter toward a Claude
  recipient (T5), the paste-burst question (T6). My reading: **the release does not cover it.** It releases throwaway
  sessions; its own record says L4 (the recorded death of tmux send-keys injection) is not changed; and packet 1 treated
  a paste into a disposable receiver as "one explicit exception to L4". **Point for his signature.**
- **T6 is `relay-X3-pty`'s one small question** (ledger, Standing): which way of writing and which gap before Enter submits a
  pointer, read from the record. Running it here answers the reserved chapter's question outside the chapter. Whether it
  runs here or opens X3 is his. T5 is the running bridge's own Claude direction, not X3 — but it is typing all the same.

# 6. Cost

- T0: no tokens. T1: two turns, about four model calls; T2: about four, plus the hold. With Codex's system prompt and tool
  list at an estimated 8–15 thousand input tokens per call, mostly served from cache, one loop of T0–T2 is roughly
  60–120 thousand input tokens and under 3 thousand output — an estimate until T1 measures it.
- Keep it cheap: smallest model the account offers, pinned and recorded per run, low reasoning effort; launch prompt and
  pointer files of a few lines; no `AGENTS.md` in the working folder; T3 only on demand. Reuse code and the server
  within a run, never a session across tests (§0.4). Live runs on demand, one per call, a daily cap in the config.
- **Point for his signature:** the credential route (§2.3) and the daily cap, since both are his account and his spend.

# 7. Points for Majkee's signature

1. Credentials for the sandbox — API keys, or copied subscription tokens with the refresh question unanswered.
2. Typing into sandbox panes (dialogs, chooser answers, T5) — L4 reading; and whether T6 runs here or under `relay-X3-pty`.
3. Python stdlib for test tooling, not deciding docket 2.
4. The bed's name, and whether it takes a relay-line X number — names are his; `relay-X3-pty` and `relay-X4-tracker` stay unspent.
5. A daily cap on live runs, and whether a live run may start without a person present.
