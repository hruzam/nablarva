---
kind: read-back and release sheet 1 — what the lead reads back to Majkee, and the release lines of the first run, one theme at a time
by: lead (flight, pen of relay-X1-probes) · 2026-11-22 · host home
for: the exec desk and Majkee
status: DRAFT 1 — read by nobody but its author. It goes to the desk only after one opposing read by the other vendor.
rule: every line here points at or sums up a file. This sheet decides nothing and releases nothing. "Lead's view" is marked as such and is only a view.
order: as numbered. S0 first. If S1 is not given, S2 to S6 are skipped.
asked: lines 2, 3, 6, 4, 5 and 7 of the handoff's release menu (§6) — one sample, two observations. Nothing else.
not_asked: lines 8–19 — the second sample, the six deferred rows, the U01 capture. A line that is not released is NOT RUN.
handoff: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/handoff.successor-stage.2026-11-22.md
help_of_the_day: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/help.codex-0.171.0.2026-11-22.txt
---

# Why now

The handoff says nothing starts before you have heard the plan back (§8). The versions today are the ones the handoff was
written on — Claude Code 2.1.330, codex-cli 0.171.0, tmux 3.7c — so its flags still hold; after a CLI update they would have to
be read again. The party's seats are bound and idle.

# S0 — The read-back

- **Rows.** You have selected none yet. This sheet asks for the first run only: one disposable Codex sample and two tries into
  it, both **Claude → Codex** — A by `codex queue`, B by a tmux paste with Enter as a separate step. The handoff calls the
  sender "the engineer"; in this bed that seat is the **lead** (this session, pane `%70`).
- **Which bed owns each U-case.** All six belong to `relay-X1-probes`. Belonging is not a release.

  | Case | State | On this sheet |
  |---|---|---|
  | X0-U01 — unknown-view fixture | the search of the trial captures ended MISSING; you chose one new real capture | not asked (needs lines 8 and 17–19) |
  | X0-U02 — the exit race | parked by you | not asked. Observation B may show whether that seam can be watched at all. |
  | X0-U03 … U06 — receiver contract | paper work (G5), not started | not asked; paper needs no release, and it is easier after A and B |

- **Stop conditions** (handoff §3, "Stops"; the last two are the lead's additions, marked):
  - An uncertain result ends that row. It is recorded UNCERTAIN — no retry, no other sender, no other carrier.
  - A dialog on the sample ends the run until your hand clears it.
  - A process nobody started ends the run and becomes an incident note.
  - A row whose precondition cannot be established is NOT RUN, not FAIL. The preconditions, looked at and recorded before each
    try: the sample's thread id read from its own footer; the agent in the foreground of its pane; the input row empty (by the
    cursor position and the styled capture, not by eye); no dialog; **the sample idle**.
  - *Lead's addition:* each try is watched for 180 seconds after the carrier call. What is not seen by then is recorded as not
    seen — UNCERTAIN, with what was seen.
  - *Lead's addition:* **if A ends UNCERTAIN, B is NOT RUN** and the row comes back to you. A queued message that may still be
    pending would land in B's measurement.
- **Where the evidence goes.** Receipts, the observer's captures and notes: a new private folder,
  `~/.local/share/nablarva/custody/x1-probes-2026-11-22/` (0700/0600, never Git). The bed gets the result rows only, in
  `packet.md`, and the line ledger gets one pointer. Nothing a person wrote on a screen goes into the repository.
- **What the stage is not** (handoff §0): no verdict on the relay architecture, no door qualified, every result "tried once".
- **Ask (one answer):** is this the plan as you hold it — yes, or what is different?

# S1 — Line 2: start `sample-codex`, and close it at the end by the same hand

- **Context.** A disposable Codex session in its own tmux window `sample-codex`, which the desk prepares, started by your hand in
  a new empty folder outside every repository: `~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/`. A trust dialog for
  the new folder, if one appears, is your hand. Closing it at the end is the same release; the lead says in its pane when the
  observer's last read is on disk.
- **One thing the handoff left open.** It starts the sample with no sandbox and no approval flag, "so the defaults apply". Today's
  help shows both are flags (`-s read-only | workspace-write | danger-full-access`, `-a on-request | never`); your Codex config
  sets neither at top level; and the help does not say what the default is for a new folder. The sample must write one receipt
  file. If its default asks before writing, that is a dialog on the sample, and the run stops until you clear it.
- **Buys:** a receiver that no party seat depends on.
- **Cost:** one start and one close by your hand; a session record of the sample stays on the host (S6).
- **Consequences of each value:**
  - *(a) as the handoff has it* — `codex -C <folder> -m gpt-6.1-terra`. The receiver is "whatever the default is"; a write
    prompt is possible, and then B's look at the input row is disturbed by a dialog.
  - *(b) explicit* — `codex -C <folder> -m gpt-6.1-terra -s workspace-write -a never`. By the help text: writing is allowed
    inside the working folder and the sample never asks. A refused write comes back to the model, and the receipt is then
    MISSING — a clean row. The receiver configuration is a named value in the packet.
  - The model name `gpt-6.1-terra` was used by the controller for its helpers; as a value of `-m` on the command line it is not
    verified. If it is refused, startup waits until you name another.
- **Lead's view:** (b).
- **Ask (one answer):** start `sample-codex` — with (a), with (b), with other values you name, or not?

# S2 — Line 3: the standing NONCE instruction, typed into `sample-codex`

- **Context.** One instruction at the start, an input of its own. Text, with the folder written out:
  `When a message carries NONCE:<value>, write the value and the UTC time into ~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/receipts/<value>.txt and do nothing else.`
  This first turn is also what gives the sample a thread id in its footer.
- **Who types it.** The handoff does not say. An agent typing into the sample would itself be a tmux push before any measurement.
- **Buys:** a receipt that does not depend on anybody's reading of the screen.
- **Cost:** one typed line.
- **Consequences:** without it there is no receipt, and A and B could show a native turn at most.
- **Lead's view:** your hand types or pastes it.
- **Ask (one answer):** the instruction goes in — by your hand, by the desk's hand, or not?

# S3 — Line 6: what the observer may read, and the private folder

- **Context.** The observer is the auditor: never sender, never receiver, only reads. Scope, as in the handoff §3 — the bottom
  rows of the sample's pane, with UTC times, before and after each step; the sample's own session record under
  `~/.codex/sessions/`, for the native turn; the receipt file; tmux metadata of the sample's pane. Nothing of any party pane.
  It writes its note before it reads the sender's account. Folder: `~/.local/share/nablarva/custody/x1-probes-2026-11-22/`.
- **Buys:** each result is seen from outside the sender.
- **Cost:** the auditor's context (82% left at 05:41 UTC).
- **Consequences:** without an observer a result is the sender's own word, and the gate asks for the observer's confirmation.
- **Ask (one answer):** this scope and this folder — yes, or what changes?

# S4 — Line 4: observation A — `codex queue`, lead → `sample-codex`, once

- **Context.** One call: `codex queue --thread <the sample's id> --message "NONCE:<fresh value>"`, without `--resume`. The nonce
  is written into a POINT before the try. Recorded: the call with UTC before and after and its exit code; whether a native turn
  was seen; the receipt with the same nonce.
- **Buys:** the first clean answer, on today's version, to whether a message from a Claude seat reaches a Codex seat by the queue.
- **Cost:** one message into a disposable session.
- **Consequences:** it qualifies nothing — the queue is a vendor door, parked by L14 D1; the result stands as "tried once".
- **Ask (one answer):** observation A — released, or not?

# S5 — Line 5: observation B — tmux paste, then Enter, an agent (the lead) sends, → `sample-codex`, once

- **Context.** Three separate steps with a look before and after each: `tmux set-buffer`, `tmux paste-buffer -p` into the
  sample's pane, then `tmux send-keys Enter`. The text is `NONCE:<another fresh value>`. Recorded per phase: text staged on the
  input row · submit seen · native turn · receipt. No party pane is a target. It runs after A, only if A did not end UNCERTAIN,
  with the sample idle again.
- **Why it needs your own words.** This is an agent operating a tmux push. L4 records send-keys injection as a death and L17
  calls tmux push a human-operated carrier. `docs/ARCHITECTURE.md`, lines 216–219: any claimed exception "returns to Majkee with
  its evidence. No future gate may presume that exception." So this is **one explicit exception to L4 for this one measurement**.
- **Buys:** an answer for the trial's own direction and method — its three Claude → Codex attempts (0 of 3 verified, on an older
  version) went through the archived adapter; this is a hand-run paste, and the adapter is not used.
- **Cost:** one exception, used once.
- **Consequences:** it reopens nothing and adopts nothing. Without it the packet has A only, which is a valid packet.
- **Ask (one answer):** observation B, as one explicit exception to L4 for this one measurement — released, or not?

# S6 — Line 7: the sample's session record afterwards

- **Context.** Codex keeps the sample's own record under `~/.codex/sessions/`. The observer's proof of a native turn points into it.
- **Buys / cost:** keeping costs a small file on the host; deleting before your GO or STOP removes what the packet points at.
- **Lead's view:** keep it until you have recorded GO or STOP on the packet, and decide its deletion on that sheet.
- **Ask (one answer):** keep until the gate, delete right after the run, or keep for good?
