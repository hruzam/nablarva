---
kind: party roster (data for pokes; observed, not assumed)
bed: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover
rev: 2 (2026-11-21T21:00Z) — team widened by Majkee, see decision.majkee.team-and-doors.2026-11-21.md
observed_by: engineer · 2026-11-21T20:58Z · host home (hruzam) · read-only tmux queries + bottom rows of each pane + ~/.claude/sessions/*.json
tmux: base session `helloWorld`, grouped views `helloWorld-37 … -41`. Windows by name — engineer, controller, oraculum, myShell, auditor. tmux 3.7c.
versions: Claude Code 2.1.330 · codex-cli 0.171.0
warning: every pane root is `zsh -l` (the CLI was started from a shell). If an agent exits, typed text lands in a shell. Look before every typed line.
stale_after: any window rebuild, CLI restart or host move. Pane ids and native ids must be re-read then.
---

# Seats

```yaml
- seat: engineer            # pen holder of this bed
  who: trajectory (claude agent), subagents delta · vector · assay
  vendor: claude
  model: Fable 5.2 xhigh
  session: d1ca16e9-073e-46d9-ba7d-26a816c38a67
  window: engineer
  pane: "%58"
  cwd: ~/ia-sync            # work root for this bed is ~/unikuklatrix/nablarva (absolute paths)
  door_in: tmux pane %58 — one labelled line, look first. Typed text queues if I am mid-turn. Majkee types here too, so a non-empty input row means do not paste.
  writes: STATUS.md, goals/, raw/ (own files), _bus/NN.engineer.*.md, pulse row, git commits. I do not push; the controller does.
  bell: a reply bell is asked from every poked seat (Majkee's note). I still check RETURN paths myself with a finite file check.

- seat: cartan              # controller (role below)
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318
  thread_name: "controller(codex)|houston|oraculum|astrobley"
  window: controller
  pane: "%59"
  cwd: ~/unikuklatrix/nablarva
  permissions: Full Access — Majkee's word (decision file) and the pane line "Permission selection requested … Full Access" seen 20:58Z. His own probe is asked in cycle 03; until it returns this is unconfirmed from his side.
  door_in: codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<one line>"   # no --resume; queued is not read
  door_fallback: one labelled `[manual …]` line into %59 after a definite clean failure, look first
  door_out: files, plus the reply bell into %58 once his probe shows tmux is reachable. In cycle 01 his sandbox could not reach tmux (01.cartan.return.md field 2); that was before the permission change.
  writes: only the paths a POINT names. No STATUS, no goal files, no commits unless a POINT gives him owned paths.
  note: NOT the X0 pen. The X0 controller is thread 01a1d582… (office record).
  confirmed: thread, cwd and the earlier co-thinker role by himself (cycle 01). Pane and model are my observation only.

- seat: oraculum            # opposer and counter-signature (role below)
  vendor: codex
  model: GPT-6.2-Astra xhigh, profile oraculum
  thread: 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1
  thread_name: "oraculum(codex)-audit"
  window: oraculum
  pane: "%60"
  cwd: ~/unikuklatrix/nablarva
  door_in: codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<one line>"
  door_out: files; reply bell if her sandbox reaches tmux (unknown until cycle 04 returns)
  writes: only the RETURN path a POINT names
  seen: 20:58Z idle, "Standing by for trajectory's message".

- seat: auditor             # outside audit (role below); a second Cartan identity
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1ffdf-793f-76d2-8497-3f68f84a34a7
  thread_name: "auditor(codex.cartan)|houston"
  window: auditor
  pane: "%66"
  cwd: ~/unikuklatrix/nablarva
  door_in: codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<one line>"
  door_out: files; reply bell if its sandbox reaches tmux (unknown until cycle 05 returns)
  writes: only the RETURN path a POINT names
  seen: 20:58Z idle, waiting for trajectory's message before reading further.

- seat: myshell             # Majkee's desk; continuity over the project task is partly her job (Majkee D3)
  vendor: claude
  model: Fable 5.2 medium
  session: a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66
  session_name: majkee-04
  window: myShell
  pane: "%61"
  cwd: ~/reposoma/.majkee   # operator vault, sealed (L22). I talk to the seat; I never read the vault.
  door_in: tmux pane %61 — one labelled line, look first (bottom rows only)
  writes: her own files; in this bed only a RETURN path a POINT names. She does not commit project files (02.myshell.return.md).
  confirmed: window list matched roster rev 1 (her own `tmux list-windows`, 2026-11-21T19:03Z, cycle 02). Not re-engaged since.

- seat: majkee
  vendor: human
  role: intent, acceptance, every release (L21), trust and permission dialogs
```

# Roles I set (Majkee: "as main engineer you can define his role"; "who and what you pick … is on you")

**Team size: two at work, two on call.** Core is engineer + cartan. Oraculum and the auditor are called by POINT, not kept busy.

**cartan — controller.** Majkee's words define the job (decision file, item C). How I use it:
1. **Hands.** Runs what a POINT names with an unrestricted shell: reading, crawling, probes, inventories. G3 is his first job after binding.
2. **Push.** I commit path-scoped; on my poke he fetches, checks that `core` is only ahead, runs one plain `git push`, and reports the range. Never `pull --rebase`, never force.
3. **Non-author check** of my documents, as in cycle 01.
4. **Coding by POINT** when a goal is released. Then I check his work, or oraculum does; nobody accepts their own.
5. **Codex-side subagents** (`houston`, `oraculum`, `astrobley`) when a POINT allows it. Their words are published verbatim and attributed.

He holds no pen: no STATUS, no goal files, no release decisions. The push service is Majkee's routing, written down; it is not a
way around a permission another seat lacks (scar S7), and it is not to be stretched into "run this for me because I may not".

**oraculum — opposer and counter-signature.** A peer of my tier from the other vendor. Called before a lock, before a gate text goes
to Majkee, and before a goal that carries a release starts. Senior dev partner if a build is released. No pen.

**auditor — outside audit.** One bounded audit of this bed now (cycle 05). Afterwards a candidate for the independent observer that
G8 requires; otherwise Majkee can close the window. No pen.

**A second relay Cartan — not asked for.** One controller covers hands and push today, and an idle seat is a cost. I ask Majkee for it
when crawling and reading start to eat the controller's context.

**myshell — continuity.** Told where this bed is. May be asked to hold or check continuity notes. No pen here.

**Reply bell (Majkee's note, all seats).** After the RETURN is on disk: look at the target pane first (foreground is the agent, input
row empty, no dialog), then one labelled line `[bell rNN] return at <path>`, pasted and submitted as separate steps, once. If the
pane is not clean, nothing is typed and the RETURN says so. A bell is a hint; the file is the truth.

# Not in this party (do not address from old records)

- X0 controller `nablarva.cartan`, Codex thread `01a1d582…` — office record of 2026-11-19.
- X0 witness, Claude `c266d10a…` — office.
- Old operator desk, Claude `06352fda…` — not running (its pane `%49` shows a shell).
