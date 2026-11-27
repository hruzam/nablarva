---
kind: GOAL plan — one fixed proposal for Majkee's countersignature. Not a progress list: once signed it does not change; progress lives in each bed's STATUS.
by: lead (flight · claude 689d87d0) · 2026-11-27 · home
status: FOR SIGNATURE — written 2026-11-27 04:25 UTC. The auditor's check of the first draft (REVISE, _bus/01.auditor.return.md) and the fresh reader's walk (raw/walk.fresh-reader.md) are taken in. The auditor has not read this version.
rests_on: raw/check.beds.md · raw/check.relay-tests.md · raw/check.observation-consumer.md · raw/check.hcom.md — each one reader's work from files in this checkout; nothing was looked at on the office host and no test was run
his_words: raw/decision.majkee.release-and-go.2026-11-27.md · ../relay-X2-research/raw/decision.majkee.original-intent.2026-11-27.md · ../relay-X2-research/raw/decision.majkee.gate.2026-11-27.md
---

# GOAL

Work passes between Claude Code and Codex sessions through files and a short pointer — that runs and stays. Beside
it we build, as ordinary code with test loops: **(1)** relay tests, **(2)** a first thing that shows what each
session is doing, **(3)** a short review of the outside tool hcom. And **(4)** no bed stays open without someone
working on it or a named word it waits for.

A "bed" is a session folder under `.dev/session/` with one closing condition (its gate). "The router" is
`.dev/session/pulse.md`, the list of open beds. The team chose the order, the homes and the file layout; your keys
at the end are only the things that change a scope or release something.

# Three rules for every item — your remarks of 2026-11-27

- **A second development gets its own worktree.** A worktree is a second checkout of the same repository on its own
  branch. They live side by side in `/home/hruzam/unikuklatrix/nablarva.wt/<name>/`. A branch returns to `core` by a
  plain merge, never a rebase — the repository's branch rule (lock L12) already says so.
- **Tests in a session.** Code and its tests live in the worktree, in one folder of `toolbox/`. The bed on `core`
  holds only the launcher, the status and one table with a row per live run. Raw run output is private, outside Git.
- **Two speeds of test.** Offline tests (parsers, guards, pass/fail logic on stored samples) run on every save and
  cost nothing — the automatic loop. Live tests start real CLI sessions in the sandbox, cost tokens, and run on demand.

# The checklist, in order

## 0 · Clear the router first — words only, no work

Eight of thirteen open beds have had no commit for three weeks or more. That dates commits; it does not prove a bed
is abandoned. What each bed's own STATUS says:

| Bed | Recorded state | Proposed, and what stays recorded |
|---|---|---|
| `architecture-X1-bookkeeping` | its gate is complete (commit cb08d6f); only your closing word is missing | **close** its router row; its evidence stays, nothing is pruned. This frees the spine slice (item 4) |
| `composer-01-parse` | first phase passed; parked by you on 2026-10-22 | **close as parked**; what its resumption waits for (the reviewed outcome of its third chapter, then your word) stays in its STATUS |
| `muticula-01-qualify` | a test plan written, no run; one question to a Codex seat open since 2026-10-02 | **stop**; nothing in this plan depends on it |
| `ovitmugen-01-basement` | written, nothing built | **stop** — but one piece of it is needed: the list of seat addresses that the spine slice's gate requires. That piece moves into item 4 by name |
| `nablarva-02-pipe-qualification` | three cycles closed, nine offline tests pass; its first live sitting never began; it waits since September for one approval line from you | **stop, with its live proof recorded as outstanding.** Its gate asks more than item 1 does (a native acknowledgement, a refusal while the recipient is busy or at an approval, a correlated answer). Item 1 reuses its offline fixtures by reference, with their origin kept |

Stay open, each waiting for one word from you: `documentation-X1-organ-discovery` (GO or STOP on a finished packet)
· `sublime-observer-X1-file-publish` (install version 1.1, walk its smoke list) · `termbrana-M0-markdown-test` (close
the test views, send one follow-up) · `session-window-X1-surface` (item 2) · `phone-console-01-browser` — **kept
paused**: your recorded direction is to resume that same bed, and three of its checks are still open.
Left alone, each with its own head on the office host: `termpanum-X1-source-qualification` (its head first finds out
whether an interrupted recovery command already ran, then cleans up only what is still owed — not from the stale
STATUS) · `terminal-workspace-X0-approaches` (a handoff to office was prepared; the office side was not observed).

Evidence of completion: every row of the router names a bed someone works on, or the word it waits for.

## 1 · Relay tests — a new bed, proposed name `relay-X5-tests`

The relay line's numbers 3 and 4 are reserved for two chapters that stay unopened (`relay-X3-pty`,
`relay-X4-tracker`), so the next free one is 5. Proposed gate: *Majkee records GO or STOP on a witnessed packet of
sandbox tests T0 to T2 — each fact reported as pass, fail or unknown — with the offline loop running; the tests
describe, they qualify no carrier.*

- **Owner:** a fresh head in the window `spare-claude` (your roster allows it). Implementer: trajectory (Claude,
  senior developer). Check: the existing auditor (Codex). Git: the controller.
- **Worktree and files:** branch `relay-tests` in `nablarva.wt/relay-tests/`; it changes only `toolbox/relaytest/`.
  Plain Python with no packages, as the repository's other helpers — a test helper's language is the team's choice
  and does not decide the product's language.
- **The sandbox:** a tmux server created for the run, on a socket inside the run folder, with an empty
  configuration. Each CLI runs inside bubblewrap (a Linux tool that gives a process its own view of the disk) with a
  blank home, so it cannot see the living seats' `~/.codex` or `~/.claude`. One wrapper is the only way the code
  calls tmux, and it refuses any other socket. Teardown kills only the server that run created — never the default
  server, never the shared test server of `session-window-X1-surface`.
- **T0, sandbox proof — first, and a gate for the rest.** A plain shell in the sandbox shows the real home is
  invisible; then everything is gone. No tokens, no credentials. **Until T0 passes, no credentials go in and no
  other test runs.**
- **T1, wake and read.** A throwaway Codex gets a pointer through `codex queue`. Three facts, each from its own
  source: *accepted* — the carrier's answer; *arrived* — the pointer as an input in that session's own record;
  *read* — a tool call on the file, and a secret word that exists only in the file coming back.
- **T2, a decision is outstanding.** A throwaway Codex is brought to its approval menu. Three observations are
  recorded separately, and may disagree: its record holds a request with no result · a status code in the raw
  terminal stream (predicted for this host, never measured) · the menu on the screen. A second pointer is sent;
  the sandbox is killed with the menu unanswered.
- **Reading results.** *Fail:* the sandbox leaked, a wrong secret word, a menu answered by anything. *Unknown:* a
  delivery or state not seen by the deadline — kept in the table, never repeated blindly. Each independent trial
  gets a fresh recipient, and the row says how its previous turn ended. Every run is a planned sample: it never
  enters the count of your own interventions.
- **Then, in this order:** the same under Codex's automatic reviewer · what a routine exchange costs in tokens ·
  a Claude recipient · the one question kept for `relay-X3-pty` — the last two need key K3.
- **Depends on:** key K1; then T0; then key K2. **First safe action after K1:** create the worktree, write T0.
  **Evidence of completion:** the run table with T0 to T2, and the offline loop running on save.

## 2 · A first consumer — through `session-window-X1-surface`, in two steps

That bed is live on this host and compares three ways of showing session status. Its own STATUS says "No helper is
built yet", and its gate is a comparison with a recommendation — not a build. So:

- **Step 1 (its own next action, no key):** you read that bed's sheet; its head (`lead.seswin`, Claude) finishes
  the comparison. Output: which fields can be shown today, which cannot, by which route.
- **Step 2 (key K5):** that line's next bed builds one short command that prints the state of named throwaway seats
  from what the installed tools already report (`claude agents --json`; tmux's own pane fields). Listing the living
  seats, or attaching a tap to one, is a separate scope and is not asked here.
- **What it cannot do yet:** tell reliably whether a Codex seat is free or waiting for an answer. Two passive tests
  could not split the two; that does not prove it impossible for every interface.
- **Owner:** that bed's head; this plan proposes and does not reach into another bed.

## 3 · hcom — a bounded review, a task inside `relay-X5-tests`

hcom is an outside tool that lets CLI sessions message each other. Found so far, all read through page summaries:
licence MIT, so code and tests may be copied if the notice is kept (dependencies not checked); tests with real
Claude and Codex binaries, one for a message that waits behind an approval and is delivered after it; no test
found that proves the recipient read the message; several of its releases contain fixes to Codex delivery or status.

- **Step 1 (no key):** read its source for the Codex path. **Step 2 (key K3):** run its approval test in the
  sandbox beside T2 — only if the sandbox is shown to contain what hcom's wrapper can see and control; otherwise stop
  at the source review. **Output:** one page, with the CLI versions each side used, and the difference kept
  visible: its test approves and delivers, T2 leaves the menu unanswered.
- Adopting it as the carrier is not asked. That is yours and reopens the research question.

## 4 · The shared record — `nablarva-X5-spine-slice`, on the office host, later

The route in one sentence: the surface comparison on home (item 2) shows which fields and unknowns matter → the
spine slice on office proves one writer and one reader of a shared, append-only record → the lab's source
qualification (`termpanum-X1`) supplies its synthetic evidence under its own release. A new dependency between
these beds needs their heads' agreement.

- **Owner:** a fresh Codex head on office (yours to wake). **First action there:** freeze its existing yardstick.
  Its gate also needs the seat-address list from the stopped `ovitmugen-01` (item 0) — built inside the slice.
- **Yours before it builds:** the closing word of item 0, its folder name, and your GO on the surface comparison.

## 5 · Continuity — three small repairs, from the fresh reader's walk

A reader who knew nothing started at `AGENTS.md` five times, once per item (`raw/walk.fresh-reader.md`). One item
was found directly, four only with a detour; ten beds turned out to wait for you. What would have saved the most:

1. **`AGENTS.md`, read order:** name the line ledgers (`.dev/session/<line>-X.ledger.md`). Today nothing at the front
   door leads to the relay line once its bed is closed.
2. **`flag.md`, under the research-before-build lock (L14, part D4):** one dated line that the gate was answered —
   REFUSE, with the paths of the verdict and the ledger.
3. **The router:** the two finished or parked rows go with key K4. Showing host, head and the awaited word per row
   would need a change to the router's own rule (lock L9′) — not asked now.

**Owner:** the lead drafts 1 and 2 as two one-line diffs; you commit or strike them. No new standing rule.

# Your keys — six. Each line can be answered alone; "all as recommended" is a valid answer

| Key | What it releases or changes | Recommended |
|---|---|---|
| **K1** | Open `relay-X5-tests` with the gate, owner and worktree of item 1 (change any of them here). Live runs: at most 20 a day until T1 has measured what a run costs, then a token budget you set. T0 to T2 may run with nobody present: yes / no | yes · yes |
| **K2** | After T0 passes: how the sandbox logs in — **the one key that needs your hands.** Separate API keys for both vendors, given to the sandbox only. Copying your login tokens is not offered: nobody knows whether a token refresh there would log out the living seats | API keys |
| **K3** | Three separate lines. (a) Test code may send scripted input into panes it created itself on the run's own server, for the named cases: yes / defer. (b) Install and run pinned hcom's approval test there: yes / defer. (c) The question kept for `relay-X3-pty` — run it here once and return the finding to the ledger while that chapter stays unopened, or leave it for that chapter: here / defer. Your release covers throwaway sessions on a separate server; it does not expressly say these three, so they are asked | (a) yes · (b) yes · (c) here |
| **K4** | The five closings and stops of item 0, with the pending work recorded as written there (strike any) | yes |
| **K5** | After the surface comparison has your GO: that line's next bed builds the one command of item 2, on throwaway seats | yes |
| **K6** | The two one-line repairs of item 5 (`AGENTS.md` read order; one dated line in `flag.md`) — drafted by the lead as diffs for you to commit | yes |

Not asked now, and yours when their time comes: the carrier toward a Codex seat · who owns the shared record · the
event vocabulary (the existing list treats working, waiting, idle and exited as exclusive; the newer research says a
question can be outstanding while work goes on) · the spine slice's folder name and its head on office · any change
to `AGENTS.md` beyond key K6 · a name other than `CACHE…` for a seat's support memory (your roster gives that to `myShell`).

This plan opens no bed, starts no session and stops nothing — your keys do. It does not design the vendor-neutral
mailbox with one adapter per vendor; that idea stays under `relay-X3-pty`, and the tests of item 1 will tell whether
and how to open it.
