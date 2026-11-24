---
kind: backlog handoff — a design proposal for whoever opens termpanum work next. Uncanonical; nothing here is adopted,
  released or scheduled. flag.md and the termpanum beds win on conflict.
by: myShell (claude a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66, home) · 2026-11-23
authority: Majkee 2026-11-23, typed in the myShell session — asked how "such tracking script" should be designed, "if should
  controll whole tmux session or rather each record by one session", and allowed a handoff in the backlog under a termpanum slug.
read first: PROJECT-DESIGN.md §3.6 · .dev/research/termpanum-events/events-map.v0.2026-10-02.md ·
  .dev/session/toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md (axioms ax1–ax6)
basis: the provisional tracker of relay-X1-probes, read by myShell from its source on 2026-11-23. myShell did not run it,
  did not read its JSONL output, and read the termpanum docs above only in part (headings and the sections named).
---

# Session tracker for termpanum — proposal

## 1. Where it comes from

During the approval probes of `relay-X1-probes` (2026-11-23) the auditor's seat wrote two scripts to watch one Codex sample pane:

- private, host-local, outside Git: `~/.local/share/nablarva/custody/x1-probes-2026-11-22/tracker-manual.u7ady8az/` on home
  (`tracker.py` 135 lines, `chain.py` 140 lines, Python stdlib; an earlier run in `tracker.2EvwcVSe/`); a copy is on office
- its own description: `c11.tracker-report.md` in the same custody folder

It taps five sources and writes one JSON line per event, with no message, log or terminal content:

| Tap | events-map `source` | What it records |
|---|---|---|
| tmux pane bottom rows, cursor | `mux` | hash of the rows, cursor, "working" and dialog flags |
| Codex rollout file of the thread | `record` | entry type, subtype, role, source time |
| Codex runtime log database | `record` | row id, time, level, target, module |
| `/proc` of shell, CLI and descendants | `proc` | state, threads, I/O deltas, spawn and exit |
| pane output stream | `pty` | bytes, escape count, newlines per chunk |

It already behaves like termpanum's ear: read-only, paths and counts instead of content (ax5), stops itself when the pane,
process or thread identity changes. It is not a tool yet: pane id, pids, thread id, tty and a tmux file descriptor are
constants in the source; the record readers are Codex-only; the dialog flag matches two fixed phrases and missed the
"Reviewing approval request" indicator, which only a separate screen watch caught.

## 2. The question: whole tmux session, or one record per session?

**Recommendation: one record per observed agent session, one tap process per pane, and a thin registry above them.
Not one process and one file for the whole tmux session.**

- **Tap (per pane).** One process, one append-only file, one writer — the events map already says "one writer per session
  file". The join key is the agent's own session id (Claude session id, Codex thread id); pane, pid and tty are the anchor.
  The file name carries the session id, not the pane: a seat that is cleared and restarted keeps its pane and gets a new file.
- **Registry (per tmux server).** Watches only which panes exist and what is bound to them: pane ↔ shell pid ↔ tty ↔ CLI ↔
  session id. It starts a tap for a released pane, records `session_started` / `session_ended`, and holds no observations
  itself. This is the only part that looks at the whole tmux session.
- **Join (at read time).** Relay questions are pair questions: a line sent from one seat, a turn that starts in another.
  That is answered by merging the per-session files on time and nonce when someone reads, never by a shared writer.
  All taps on one host use one clock; cross-host joins state their clock error.

Why not one tracker for everything:

1. **Failure stays local.** An identity change in one pane must stop that tap only. In one process it stops, or poisons, all.
2. **Release is per session (L21) and observation authorizes nothing (L20).** A sample the lab started itself is covered
   by ax1. A living working seat is a different decision each time; a per-pane tap can be released, refused or stopped alone.
3. **Vendors differ in the high taps, not the low ones.** `mux`, `pty` and `proc` are the same for every CLI; `record` and
   `hook` are one small adapter per vendor. A tap composes shared low taps with one adapter; a whole-session tracker would
   need every adapter loaded and every format tracked at once.
4. **Privacy and custody.** One file per session can be kept, copied or deleted alone.

## 3. Shape proposed

- Arguments, not constants: `--pane`, optional `--session-id`; the tap resolves pid, tty and record path itself and refuses
  when they disagree.
- Output in the events-map envelope (`ts · session_id · event · source · certainty · anchor · payload`), using its twenty
  words where they fit and `unknown_activity` where they do not. The probe's finding fits rows 11 and 12 directly:
  `approval_requested` from the rollout (`confirmed`) and `approval_resolved` — with the resolver marked unknown, since
  no human chooser and no reviewer identity was visible.
- Same stop rules as today: `STOP` file, identity change, record shrinking.
- Scripts and plain files under the proposed `toolbox/termpanum/`; no daemon, no service, until repeated use asks for it.

## 4. Things to settle before anyone builds

- **Qualification order.** `termpanum-X1-source-qualification` (office, blocked since 2026-10-30) is still qualifying one
  synthetic tmux output source. The provisional tracker ran outside that; its captures are unqualified evidence.
  Whether a tracker may be built before X1 closes is Majkee's call.
- **The name is taken once already.** L14 reserves `relay-02-tracker`. myShell did not check whether that "tracker" means
  this tool. If it does, this handoff belongs to that session's intake instead.
- **The tmux pipe slot.** As far as myShell knows, tmux gives each pane a single `pipe-pane`; a tap that uses it shuts out
  every other tool on that pane. Verify on the installed tmux, and decide who owns the slot (not checked here).
- **Claude adapter.** Nothing was written for Claude panes. The events map lists `~/.claude/sessions/<pid>.json` and hooks
  as sources; both are untested here.
- **Envelope convergence** with `jev.event/v1` is still open in the events map (§3 there). A tracker should not freeze a
  third shape.
- **Polling against events.** The taps poll at 0.25–0.5 s. Anything shorter than a poll is invisible to `mux` and `proc`;
  only the `pty` and `record` taps see it. State that limit in every report.

## 5. Not in this handoff

No code, no session, no release. The provisional scripts stay where they are, in private custody; moving a cleaned copy
into the repository is a decision for the pen of `relay-X1-probes` and Majkee.

---

> Note by myShell, 2026-11-23, after Majkee read the above: the relay line may take this design for itself; termpanum groups
> can be pointed to it later. Neither termpanum nor the tracker has its own ledger. A relay chapter for it would be named in
> the line's own form — his example: `relay-X2-tracker` — not `relay-02-tracker`. The question in §4 "The name is taken once
> already" is therefore his to close against L14; nothing is opened by this note.

> Correction by myShell, 2026-11-23, on Majkee's word: the note above read his example wrongly. L14's reserved names are amended
> in `flag.md` to `relay-X2-pty` and `relay-X3-tracker` (or the next free X number at opening). The tracker's relay chapter is
> the second of the two, not `relay-X2-tracker`.
