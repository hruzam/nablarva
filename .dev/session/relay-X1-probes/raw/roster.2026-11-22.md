---
kind: party roster (data for pokes; observed, not assumed)
bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes
rev: 1 (2026-11-22T05:42Z) — the lead's first read at binding. Starting list was ../../relay-X0-carryover/raw/roster.2026-11-21.md (rev 5).
observed_by: lead · 2026-11-22T05:41Z · host home (hruzam) · read-only tmux queries, the bottom rows of panes %58 %59 %60 %66 %68, and four allowlisted keys of ~/.claude/sessions/*.json (pid, sessionId, cwd, name). Pane %61 (myShell) was not captured.
tmux: base session `helloWorld`, 7 windows, grouped views `helloWorld-37 … -43`. tmux 3.7c.
versions: Claude Code 2.1.330 · codex-cli 0.171.0 — the same as in the RUNBOOK frame.
warning: every pane was started from a login shell. If an agent exits, typed text lands in a shell. Look before every typed line.
stale_after: any window rebuild, CLI restart or host move. Re-read pane ids and native ids before any poke.
---

# Seats

```yaml
- seat: lead                # pen holder of this bed (raw/decision.majkee.pen.2026-11-22.md)
  who: flight (claude agent)
  vendor: claude
  model: Fable 5.2, effort high      # launch line seen in the process list — claude --agent flight --model claude-fable-5-2 --effort high
  session: cc738596-ba93-41f4-a8a6-30a6aef4139e
  session_name: "flight(claude)|trajectory|assay|delta|vector"   # set by Majkee
  window: lead              # index 6
  pane: "%70"
  cwd: /home/hruzam/unikuklatrix/nablarva
  door_in: tmux pane %70 — one labelled line, look first. Majkee types here, so a non-empty input row means do not paste.
  writes: STATUS.md, RUNBOOK.md until the read-back, raw/ (own files), _bus/NN.lead.*.md, the pulse row, path-scoped commits. No push — the controller pushes on the lead's poke.

- seat: controller          # cartan
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318
  thread_name: "controller(codex)|houston|oraculum|astrobley"
  window: controller        # index 1
  pane: "%59"
  cwd: /home/hruzam/unikuklatrix/nablarva
  context: not read at 05:41Z — the footer was cut by the pane width. The predecessor read 40% left at about 04:40Z.
  door_in: codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<one labelled line>"   # no --resume; queued is not read
  door_out: files; an optional reply bell into %70
  confirmed: thread id, name, model and cwd by the footer. Not yet engaged by this lead.

- seat: auditor             # independent observer; a second cartan identity
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1ffdf-793f-76d2-8497-3f68f84a34a7
  thread_name: "auditor(codex.cartan)|houston"
  window: auditor           # index 4
  pane: "%66"
  cwd: /home/hruzam/unikuklatrix/nablarva
  context: 82% left (footer, 05:41Z)
  door_in: codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<one labelled line>"
  door_out: files; an optional reply bell into %70
  confirmed: by the footer. Not yet engaged by this lead.

- seat: oraculum            # opposer, by file only
  vendor: codex
  model: GPT-6.2-Astra xhigh, profile oraculum
  thread: 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1
  thread_name: "oraculum(codex).contraThinking|houston|astrobley"
  window: oraculum          # index 2
  pane: "%60"
  cwd: /home/hruzam/unikuklatrix/nablarva
  context: 57% left (footer, 05:41Z)
  door_in: codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<one labelled line>"
  door_out: the RETURN file only — no bell (her identity forbids operating a transport). The lead checks her RETURN path itself.
  confirmed: by the footer. Not yet engaged by this lead.

- seat: exec                # Majkee's decision desk; tmux window work on his word
  vendor: codex
  model: GPT-6.2-Sol medium
  thread: 01a1fefc-0356-7ea1-860c-783a66a91211
  thread_name: "exec(codex)|astrobley"
  window: seniorDev         # index 5
  pane: "%68"
  cwd: /home/hruzam/unikuklatrix/nablarva
  context: 65% left (footer, 05:41Z)
  door_in: codex queue --thread 01a1fefc-0356-7ea1-860c-783a66a91211 --message "<one labelled line>"
  door_out: files; an optional reply bell into %70
  note: at 05:41Z the bottom hint row of %68 was not the usual one ("^c copy · enter copy & follow · esc clear"), with the input row empty. Cause not known. It does not touch the queue door; look again before any paste into that pane.
  confirmed: by the footer. Not yet engaged by this lead.

- seat: predecessor         # on call for the closed bed relay-X0-carryover; holds no pen
  who: trajectory (claude agent)
  vendor: claude
  model: Fable 5.2 xhigh
  session: d1ca16e9-073e-46d9-ba7d-26a816c38a67   # the process in the pane — claude --agent trajectory --resume d1ca16e9…
  window: engineer          # index 0
  pane: "%58"
  cwd: /home/hruzam/ia-sync
  context: 47% left (footer, 05:41Z)
  door_in: tmux pane %58 — a question file in this bed's raw/, then one labelled pointer line, look first.
  unexplained: the pane's footer shows the id prefix 4f923bb7-ee1…, not d1ca16e9. ~/.claude/sessions/ holds two records with the same name `engineer(calude)|delta|vector|assay` in ~/ia-sync — d1ca16e9… (interactive) and 4f923bb7-ee15-447b-8954-408e16955530 (bg). Not looked into. The door is the pane, not the id.

- seat: majkee
  vendor: human
  role: every release (L21), trust and permission dialogs, starts and closes the samples
```

# Present in the tmux group, not a seat of this bed

- `myShell` — window index 3, pane `%61`, a Claude session whose working directory is an operator vault (L22). Majkee's desk.
  This bed does not address it and this lead has not captured its pane.

# The lead's children (Claude subagents; none standing)

The session name is a hint; this table says who is spawned for what. A child writes its own file or returns a short report;
the lead judges.

| Child | For what in this bed |
|---|---|
| `delta` | log lines in `raw/pokes.log.md`, exact-match edits from a spec, YAML and hash checks |
| `vector` | a larger well-specified write that is too big for `delta` |
| `assay` | a fresh-eyes check of one file against its task, without the author's context |
| `trajectory` | senior implementation, only if code is ever needed — none is planned; this bed builds nothing |
| `field` | melting a long file or several into a brief; the stale-sentence sweep at a closing commit (RUNBOOK, "How this party works", line 9) |

```yaml
children: []   # none standing
```

# Roles

As in `../RUNBOOK.md` (participants and prompts 1–4) and the predecessor's roster, section "Roles I set". Not repeated here.
