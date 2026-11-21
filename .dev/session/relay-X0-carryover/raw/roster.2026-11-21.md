---
kind: party roster (data for pokes; observed, not assumed)
bed: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover
observed_by: engineer · 2026-11-21T19:00Z · host home (hruzam) · read-only tmux queries + bottom rows of each pane + ~/.claude/sessions/*.json
tmux: base session `helloWorld`, grouped views `helloWorld-37 … -40` (one client each, none read-only). tmux 3.7c.
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
  door_in: tmux pane %58 — one labelled line, look first. Typed text queues if I am mid-turn.
  writes: STATUS.md, goals/, raw/ (own files), _bus/NN.engineer.*.md, pulse row, git commits; push rarely
  bell: none owed to me. I check RETURN paths myself with a finite file check.

- seat: cartan              # co-thinker (role below)
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318
  thread_name: "controller(codex)|houston|oraculum|astrobley"
  window: controller
  pane: "%59"
  cwd: ~/unikuklatrix/nablarva
  door_in: codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<one line>"   # no --resume; queued is not read
  door_fallback: one labelled `[manual …]` line into %59 after a definite clean failure, look first
  writes: only the RETURN path a POINT names
  note: NOT the X0 pen. The X0 controller is thread 01a1d582… on office.

- seat: oraculum            # Codex-side feedback / audit
  vendor: codex
  model: GPT-6.2-Astra xhigh, profile oraculum
  thread: 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1
  thread_name: "oraculum(codex)-audit"
  window: oraculum
  pane: "%60"
  cwd: ~/unikuklatrix/nablarva
  door_in: through cartan (Codex-side iteration, Majkee D3.1), or codex queue with the thread id above when I assign directly
  writes: nothing unless a POINT names a path

- seat: myshell             # Majkee's desk; continuity over the project task is partly her job (Majkee D3)
  vendor: claude
  model: Fable 5.2 medium
  session: a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66
  session_name: majkee-04
  window: myShell
  pane: "%61"
  cwd: ~/reposoma/.majkee   # operator vault, sealed (L22). I talk to the seat; I never read the vault.
  door_in: tmux pane %61 — one labelled line, look first (bottom rows only)
  writes: her own files; in this bed only a RETURN path a POINT names

- seat: majkee
  vendor: human
  role: intent, acceptance, every release (L21), trust and permission dialogs
```

# Roles I set (Majkee D3.1: "as main engineer you can define his role")

**cartan — co-thinker.** Three duties, nothing else unless a POINT says so:
1. **Challenge before a lock:** find the weakest point of my plan or document and say it plainly.
2. **Non-author check at acceptance edges:** claims against the files, CONFIRMED / REFUTED / MISSING.
3. **Codex-side hands** when a goal needs the Codex runtime (for example a Codex door in G3), by explicit POINT.

He holds no pen here: no STATUS, no goal files, no git. He proposes goal changes in his RETURN. He may consult `oraculum` on the
Codex side for one bounded question per cycle and publishes that answer verbatim, marked as oraculum's, inside his RETURN.
Model: Sol stays. The role is judgment, not relay; Terra is not needed.

**oraculum — feedback.** Consulted by brief. No cycle pointers, no pen.

**myshell — continuity.** Told where this bed is. May be asked to hold or check continuity notes. No pen here.

# Not in this party (do not address from old records)

- X0 controller `nablarva.cartan`, Codex thread `01a1d582…` — on office since 2026-11-19.
- X0 witness, Claude `c266d10a…` — on office.
- Old operator desk, Claude `06352fda…` — not running (its pane `%49` shows a shell).
