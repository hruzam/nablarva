---
kind: reader's brief for RUNBOOK authoring — facts and pointers, no verdict
line: session-window
by: field (reader agent), asked by the eSharp manager
date: 2026-11-22
read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X.ledger.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/STATUS.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/goal-substrate.2026-11-13.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/claude-export.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/live-tmux-setup.2026-11-13.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/handoff.senior-advice.trajectory.2026-11-14.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/tmux-comfort.conf
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md (row session-window-X0-substrate only)
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md (T6 and T11)
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/decision.majkee.walkthrough-2.2026-11-22.md (S4 and S5)
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/goals/G10.friendly-reminder.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/answer.majkee.reminder-and-leftovers.2026-11-21.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md
  - /home/hruzam/ia-sync/zsh/session/ovitmugen.zsh (first 40 lines)
  - /home/hruzam/ia-sync/zsh/session/ovitmugen.py (first 40 lines)
  - /home/hruzam/ia-sync/zsh/session/ovitmugen.tmux.conf (first 40 lines)
  - /home/hruzam/ia-sync/zsh/session/ovitmugen.presets.json
  - /home/hruzam/ia-sync/claude/hooks/statusline.sh
  - /home/hruzam/ia-sync/.dev/session/helper-utils-00-tmux/MOVED.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md (paragraphs L4, L17, L21)
---

# Reader's brief — session-window line

## 1. What the line is for

Majkee's words, goal-substrate.2026-11-13.md:12: "A small, personal, friendly and 'idiot resistant' utility for managing tmux sessions while he learns tmux syntax." He imagines helpers in his `.majkee/` vault with `scheme-XXXX.json` files. The core complaint, goal-substrate:27-29: "An existing session helper has been useful. Its fixed pane arrangement now gets in the way: switching between CLI sessions takes roughly three shortcut steps instead of the one he has with independent terminal views." The desired shape: each CLI view has a metadata pane below it (85/15 split); two views sit side by side; navigation is a single desktop shortcut. The metadata fields ordered by him, goal-substrate:57-66: model and reasoning effort, CWD, context remaining, session name/title (live rename), session ID, transcript path.

By T11 (decision.majkee.walkthrough.2026-11-21.md:188), the emphasis shifted: "Prioritize a flexible, vendor-neutral status line that can grow to show the clock, alerts, and other operator information. Session generation from a scheme is secondary." The 2026-11-13 framing placed launch-recipe management as the primary job; T11 placed the status surface first. These are different priority orderings.

## 2. Where it stands

Gate text, STATUS.md:13-15, verbatim: "PROVISIONAL — Majkee to confirm or rewrite. Majkee records GO or STOP on a small personal session-window helper scope: what the first version does (smallest useful action set), where it lives, the per-CLI metadata display route (native status line vs. tmux metadata pane vs. second tmux status row), and independent views with usable scrollback as default behaviour."

T11 deferred the gate: "The helper's own gate stays open." (decision.majkee.walkthrough.2026-11-21.md:188). The gate has not been confirmed or rewritten.

What was actually built: nothing. STATUS.md:17 states "Substrate only. Raw inputs gathered 2026-11-13/14 on home." Cartan manually set up grouped sessions on home as a live remedy and manually sourced tmux-comfort.conf into the running server on home only. The deployed statusline.sh predates the bed and stays in ia-sync. No helper code, no scheme schema, no design lock.

## 3. Gate texts and next steps found in the files

STATUS.md `next` field: "On office: Majkee confirms/rewrites the gate; then the first probe — capture the installed Claude statusLine stdin payload and record which fields exist (effort, session_name, context_window, multiline behaviour), with CLI version."

STATUS.md `expected` field: "A confirmed gate and one version-stamped payload record, resolving the truncation-vs-docs conflict."

Ledger open items (session-window-X.ledger.md:19-26): gate unconfirmed; first statusLine payload probe open; ovitmugen seam unresolved; `.majkee/` home of helper not settled; office and monitor unprobed; friendly reminder deferred here from relay.

T11 test (decision.majkee.walkthrough.2026-11-21.md:188): "Use the existing ovitmugen split-pane setup as evidence for navigation and test whether poke and inspection tools still target the intended CLI pane in a multi-pane window before choosing the layout."

eSharp section 2, engineer's statement (eSharp.decisions.majkee.2026-11-22.md:38): "whether the helper group continues `session-window-X0-substrate` or opens a new bed." Majkee's answer to this specific question is not yet in the files.

## 4. Locks and organ boundaries

**L4** (flag.md:20): `tmux send-keys injection` is a recorded death. The helper must not inject into agent panes.

**L17** (flag.md:193-216): "Termbrana composition and ovitmugen are independently useful clients." "Discovery is not delivery authority." The session-window helper and ovitmugen are separate tmux clients; they must not merge without a separate architectural release.

**L21** (flag.md:244-256): Amends L17. "nabLarva is one body with an architecture; its bricks can share process, API, CLI and subscription layers." But "implementing, activating, delivering through or adopting a transport for any of them needs its own separate release." The sentence about ovitmugen and termbrana being independently useful stays in force.

Ledger (session-window-X.ledger.md:30): "Agent delivery stays VIST's (L21); this line meets it only at data (window labels, session IDs)."

Ovitmugen's domain (ovitmugen.py:11-25): two-server architecture, views only, never send-keys, never kill a pane whose process is not a bare shell. The ovitmugen seam (ledger:22): "which part extends ovitmugen (`~/ia-sync/zsh/session/ovitmugen.*`, bed `ovitmugen-01-basement`) and which stays a separate helper — the X0 substrate names ovitmugen's fixed panes as the 'cage' complaint." This is unresolved.

Senior-advice rule 3 (handoff.senior-advice.trajectory.2026-11-14.md:33): "no second pane with live output in an agent window. [...] A status pane next to an agent makes the agent look busy forever." It proposes a second tmux status row instead: `tmux set -t <s> status 2; tmux set -t <s> 'status-format[1]' '…'`. This directly answers the metadata-pane vs status-line question but introduces a third option not present in the original gate.

eSharp engineer's proposal (eSharp.decisions.majkee.2026-11-22.md:29): "A separate tmux server for the helper-window group." Majkee agreed the helper group should have a separate lead (S5); he did not explicitly name the server.

## 5. What already exists and could be reused

`/home/hruzam/ia-sync/claude/hooks/statusline.sh` — deployed Claude statusLine hook; reads JSON on stdin; outputs model, effort, CWD, context%, session name, session ID, transcript path. Live in ia-sync; changes go through deploy.sh.

`/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/claude-export.md` — Trajectory's probe of `~/.claude/sessions/<pid>.json` schema plus a bash sketch `claude-pane.sh` (sidecar polling session files). The sketch was not run or tested in a pane (claude-export.md:4).

`/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/tmux-comfort.conf` — workspace-scoped comfort profile: mouse, history 50000, shifted page keys. Home-local only; not in deploy.

`/home/hruzam/ia-sync/zsh/session/ovitmugen.py` + `ovitmugen.zsh` + `ovitmugen.tmux.conf` + `ovitmugen.presets.json` — deployed tmux manager, two-server layout C. `ov-selftest` green at baseline.

`/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/live-tmux-setup.2026-11-13.md` — grouped-session recipe from the 2026-11-13 live remedy. Home-local evidence; not portable source.

Archived (not deployed): `~/ia-sync/.dev/records/vist/2026-11-14/vistMini-01-tests/scripts/vist-heartbeat.py` — bounded-wake guard with expiry and max-wakes. Relevant to G10 if that moves here.

## 6. Links to other lines

**G10 / friendly reminder:** G10.friendly-reminder.md:3 states "state: superseded-by — deferred by Majkee (T6); belongs to the session-window helper line." G10 specifies a chess clock the operator can inspect, extend, pause and reset, using the helper window as its surface (T6 summary, decision.majkee.walkthrough.2026-11-21.md:118-120). G10 stage 1 is a ~60-line script with two open questions: code home and output channel (G10.friendly-reminder.md:57-58). Stage 2 is delivery (L21) and needs its own release.

**tmux monitor-silence:** a one-window trial was decided in S4 (decision.majkee.walkthrough-2.2026-11-22.md:57). The command is documented in answer.majkee.reminder-and-leftovers.2026-11-21.md:56-72. Majkee sets it; no seat sets it.

**VIST / L21:** this line supplies labels and session IDs to VIST; it does not implement delivery.

**terminal-workspace:** sibling line, same tmux ground and principles. Ledger (session-window-X.ledger.md:29): "do not merge beds or gates without majkee."

**eSharp:** one group takes the helper-window line, one takes shared-terminal. Helper group runs first; shared-terminal starts after the first group closes a cycle (eSharp.decisions.majkee.2026-11-22.md:33-34). T11: "The shared-terminal organ is a possible future carrier for structured status events."

## 7. Read-first list for a head

1. `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X.ledger.md` — current open/solved state; most recent line of truth.
2. `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md` — the eSharp structure; most recent Majkee input; confirms separate lead and separate server.
3. `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/STATUS.md` — the PROVISIONAL gate and what was gathered.
4. `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md` — T6 and T11 only; Majkee's deferred decisions on the reminder and the helper.
5. `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/goals/G10.friendly-reminder.md` — friendly reminder spec deferred to this line.
6. `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/goal-substrate.2026-11-13.md` — most detailed description of wanted metadata fields and session manager shape; Cartan's suggestions (not yet design locks).
7. `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/handoff.senior-advice.trajectory.2026-11-14.md` — practical tmux rules; directly addresses pane-vs-status-row and agent-label questions.
8. `/home/hruzam/ia-sync/claude/hooks/statusline.sh` — deployed statusline hook; baseline for the first probe.

Stale: `tmux-comfort.conf` and `live-tmux-setup.2026-11-13.md` are home-local snapshots, not portable source. The `claude-pane.sh` sketch in claude-export.md is untested; treat as a lead, not a spec.

## 8. Open questions only Majkee can answer

1. Gate: confirm or rewrite the X0 gate? T11 deferred the gate without replacing it. The gate still lists four open choices; T11 reordered priorities but left the gate open (decision.majkee.walkthrough.2026-11-21.md:188).
2. Helper home: exact path under `.majkee/` for the helper and its `scheme-*.json` files (ledger:23).
3. First-version scope: which management actions are in beyond independent views and usable scrollback (goal-substrate:177-180 marks those as first-version requirements, but the minimum management action set is not settled)?
4. Metadata display route: native second tmux status row (senior-advice rule 3) vs. dedicated sidecar pane — this choice has layout and tool-targeting consequences not yet decided by Majkee.
5. Whether the helper group continues `session-window-X0-substrate` or opens a new bed (eSharp.decisions.majkee.2026-11-22.md:38; Majkee's answer to this question is not in the files).
6. Separate tmux server name for the helper-window group.
7. G10 output channel: beyond printed line and file note, does Majkee want a desktop notification (G10.friendly-reminder.md:58)?
8. G10 code home: bed-local or session-window line in ia-sync (G10.friendly-reminder.md:57)?
