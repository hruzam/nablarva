---
kind: party roster (data for pokes; observed, not assumed)
bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes
rev: 3 (2026-11-22T14:57Z) — two roles narrowed by Majkee, section "Rev 3" at the end. Rev 2 (2026-11-22T14:02Z) — roles as Majkee named them during the day, section "Rev 2" at the end; ids not re-read except where that section says. Rev 1 (2026-11-22T05:42Z) was the lead's first read at binding. Starting list was ../../relay-X0-carryover/raw/roster.2026-11-21.md (rev 5).
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
  This bed does not address it and this lead has not captured its pane. — Rev 2: superseded, see the end.

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

# Rev 2 — who is who and for what, as Majkee named it on 2026-11-22

Sources: `raw/decision.majkee.countersignature.2026-11-22.md` · `raw/decision.majkee.seats-and-notice.2026-11-22.md` ·
`raw/decision.majkee.cache-and-commits.2026-11-22.md`. Footers as he pasted them or as the lead saw them at the time given.

| Seat | Who | What for | Reached by |
|---|---|---|---|
| lead | Claude, this session, window `lead`, pane `%70` | pen; plans, assigns, checks, commits; sends the Claude-origin tries when released | — |
| exec | Codex, `exec(codex)\|astrobley`, thread `01a1fefc-0356-7ea1-860c-783a66a91211`, window `seniorDev`, pane `%68` — 62% left at 13:56Z | **the decision, gavel and check loop with Majkee** ("decision loop stays with exec"); tmux windows on his word | POINT file + `codex queue`; RETURN file and a reply bell |
| oraculum | Codex, `oraculum(codex).contraThinking\|houston\|astrobley`, thread `01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1`, window `oraculum`, pane `%60` — 39% left at 13:54Z | **the countersignature** — the qualified opposing read by a second thinking entity of a different brand; every sheet that asks him for a release, and the packet | POINT file + `codex queue`; RETURN file; she rings no bell (a limit of her own seat) |
| auditor | Codex, `auditor(codex.cartan)\|houston`, thread `01a1ffdf-793f-76d2-8497-3f68f84a34a7`, window `auditor`, pane `%66` — 82% left as he pasted it | independent observer of each try, and **the final work audit agent** — the packet against the evidence before it goes to him | POINT file + `codex queue`; RETURN file and a reply bell |
| controller | Codex, `controller(codex)\|houston\|oraculum\|astrobley`, thread `01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318`, window `controller`, pane `%59` | hands; pushes on the lead's poke; a Codex-origin try only if one is released | `codex queue`; the remote ref shows a push |
| predecessor | Claude, `engineer(calude)\|delta\|vector\|assay`, session `4f923bb7-ee15-447b-8954-408e16955530`, window `engineer`, pane `%58` — 47% left as he pasted it | on call for advice about the closed bed; holds no pen | one file + look-first paste |
| myShell | Claude, session `a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66`, window `myShell`, pane `%61`, working directory in an operator vault | Majkee's continuity desk — orphaned work across his tasks; not a seat of this bed, askable on his word; wrote `CACHE.md` for the lead | POINT file + look-first paste; RETURN file and a reply bell. Only the bottom rows of the pane are ever read, for the look. |
| majkee | human | every release; trust dialogs; starts and closes the samples | the exec desk for decisions; window `lead` for the lead's reports |

Pokes there and back are the lead's call. A reply comes by the RETURN file; the bell is beside it.

Confirmed by Majkee, typed in the lead session shortly before 14:05 UTC: "roster is correct, going to exec now". The table above is what he read.

# Rev 3 — two roles narrowed by Majkee, shortly before 14:56 UTC

Source: `raw/decision.majkee.roster-correction.2026-11-22.md`. The Rev 2 table stands except for these rows.

| Seat | What for — as corrected |
|---|---|
| oraculum | the second thinking voice of the other brand: co-thinking and triangulation **when the lead faces a strategic decision of its own** — not every loop, not every sheet. She writes no code; a child of hers (`astrobley`, about what `trajectory` is here; `luna` for a reply poke) may. |
| auditor | from the other brand, what the lead's `assay` child does — **for a bigger piece of work made final**: a pre-production check for red flags, leaks and weaknesses. In this bed: the packet. Observer of the tries only if he releases that at the desk (sheet theme S3). |
| any seat | may spawn `houston` for alignment with the project and for navigating documentation and logs; the seat decides. |
