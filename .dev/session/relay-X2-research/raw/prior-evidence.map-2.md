---
written-by: "@Field (reader child) · 2026-11-26"
corpus-read: "10 source files: vendor-events research (3), termpanum-events (1), pty-community (1), termpanum-X0-source-contract raw (3), nablarva-X4-vist brief (1), observations (1)"
corpus-not-read: "termpanum-X0-source-contract/raw/research-disposition.md (being read by the lead — excluded by instruction); relay-X2-research own files except prior-evidence.map.md (hard rule); research.wheel-and-harness.* (hard rule); CACHE.md / CACHE.*.md (hard rule); .majkee/ and .hlm/ directories (hard rule)"
---

# Prior-evidence map 2 — relay-X2-research · 2026-11-26

---

## Group F — vendor-events research

- `/home/hruzam/unikuklatrix/nablarva/.dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md` — establishes: hook surfaces for Claude Code (32 events listed; SessionEnd later found missed by summariser), Codex CLI (12 events), and agy (5 events) exist and can supply three to four session states without PTY screen reading; PTY's legitimate role narrowed to liveness · date/state: 2026-10-01; @Epoch research report, live-fetched that run with stated caveats; VERDICT section present · does not show: agy waiting-for-approval state gap unresolved; fixture validation not performed; several items explicitly flagged for refresh including CC SessionEnd presence and Codex rollout approval persistence

  bears on the gate:
  - [wheel] §6: keepmind9/clibot uses PTY stability as a completion trigger when hooks disabled, then reads transcript.jsonl for content — hybrid approach documented (confidence M)
  - [wheel] §6: aelaguiz/codex_monitor_skill infers WORKING/WAITING/IDLE from last 50 lines / 500 KB tail of rollout JSONL — files-only approach, heuristic not documented semantics (confidence M, summary of scripts/sessions.py)
  - [wheel] §6: shindgew/agy-acp reads agy conversation SQLite DB; "PTY output is diagnostic only, never parsed" — existing tool covers agy content without PTY meaning extraction (confidence M, README)
  - [vendor] §1 Claude Code: Stop carries transcript_path, last_assistant_message; PermissionRequest covers waiting-for-approval — confidence H, official docs fetched 2026-10-01
  - [vendor] §1 Codex CLI: hooks documented stable since v0.124.0 (2026-04-23); PermissionRequest + Stop cover three of four states — confidence M-H
  - [vendor] §1 agy: 5 hook events (PreInvocation, PostInvocation, PreToolUse, PostToolUse, Stop); no approval hook found; "brief #gate premise 'agy: no known hook surface' is OUTDATED" — confidence M, third-party sources from 2026-07-16
  - [smaller] §VERDICT: "Driller's meaning-extraction is redundant for Claude and Codex. It stays a live, but NARROW, contingency for agy ONLY, and only for the one state 'waiting-for-approval'" — equivalent to do-not-build PTY meaning layer for first-class vendors
  - [smaller] §3: stall heuristic (PTY quiet + no PostToolUse after PreToolUse) proposed as narrow liveness-class fallback for agy approval gap; "acceptable under #ax3"; fixture recommended before building

- `/home/hruzam/unikuklatrix/nablarva/.dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md` — establishes: corrected vendor hook catalogues for Claude Code (33 events), Codex CLI (12 events, Interrupt added 0.150.0), Gemini CLI (11 events, enterprise/paid only since 2026-06-18), agy (5 events unchanged); reveals undocumented CC per-PID live status file; Codex App Server `waitingOnApproval` flag; Gemini CLI not usable by personal-account operators · date/state: 2026-10-02; @Epoch, extends/corrects predecessor; rows marked (S) capped at confidence M; "re-read primaries before gaveling a field name" · does not show: CC sessions/<pid>.json schema not vendor-documented (schema "observed v2.1.178 / v2.1.284"); Codex approval persistence in rollout still unverified; Codex exec official doc returned 404; fixture not run for any vendor

  bears on the gate:
  - [vendor] §1f: CC SessionEnd confirmed in 3 independent doc pages; 33 events total — confidence H, fetched 2026-10-02
  - [vendor] §2a: Codex SessionEnd flaky — "missed in 3/10 `codex exec` runs on macOS 0.158.0 (5 s shutdown budget consumed by FSEvents teardown)" issue #49003; L0 mandatory — confidence H-M
  - [vendor] §1b C7: CC `~/.claude/sessions/<pid>.json` with `status` busy/idle/waiting/shell; `sessionId` not updated on `/clear` (issue #36213, closed not planned); dir mentioned in official docs, schema undocumented — confidence M, observed v2.1.178 and v2.1.284
  - [vendor] §1d: CC `claude agents --json` (research preview) fields `state` (working/blocked/done/failed/stopped), `status` (busy/waiting/idle), `waitingFor`; v2.1.212+ recommended — confidence M-H
  - [vendor] §2c: Codex App Server `thread/status/changed` with `waitingOnApproval` flag; `item/permissions/requestApproval` — confidence H-M
  - [vendor] §2a: Codex `notify` config emits `approval-requested` as OSC 9/BEL to PTY stream; `agent-turn-complete` only via notify program — confidence M
  - [vendor] §3.0: Gemini CLI "stopped serving requests" for personal/free tiers 2026-06-18; enterprise/paid API key required; "stable v0.62.0 on 2026-09-29" — confidence H; "not runnable" for a personal-account operator
  - [smaller] §2b: tmux-agent-status (rorhcdream) reads CC sessions/<pid>.json and Codex rollout JSONL for state without hooks or screen — files-only approach, shared app-servers break the join (confidence M)

- `/home/hruzam/unikuklatrix/nablarva/.dev/research/vendor-events/jev.agent-cli.2026-10-02.md` — establishes: "jev" is TypeSafe's decision model (not a terminal coding agent); no hook/lifecycle event vocabulary exists for jev; jev-guard's ACP proxy finding shows a proxy on an ACP stdio pipe can observe `terminal/create` and `fs/write_text_file`; proposed events-map row: "jev = L0-only, category: model-role, not session" · date/state: 2026-10-02; @Epoch, triggered by events-map v0.2 "candidate jev (everything unknown)"; confidence capped M on most rows (summaries) · does not show: which jev artefact majkee uses (file states "ASK"); no first-party terminal coding agent named jev exists; jevdev is alpha (5 commits, no release tags); jev-guard's Codex "BeforeTool" naming vs catalogue's documented "PreToolUse" — unreconciled

  bears on the gate:
  - [wheel] §1a: jev-guard proxies ACP stdio pipe and intercepts `terminal/create`, `fs/write_text_file` — an existing tool shows an ACP proxy as a push/observation door for ACP agents (confidence M, README summary)
  - [wheel] §0: jevdev uses redb content-addressed state store (.jevdev/state.redb) with per-turn decisions — demonstrates local state-store pattern for session observation (confidence M, README summary)
  - [smaller] §2e: jev-cli is L0-only (child process, exit codes); "harness around it is the event emitter and should speak the vendor-neutral vocabulary natively — that is the one case where nablarva can define the source side" — no PTY required for jev-as-callee
  - [smaller] §2e: proposed events-map row: "jev = L0-only, 'category: model-role, not session'" — relay need not treat jev as a parallel session
  - [vendor] §0 candidate table: jevdev v0 ("Early"), 5 commits, no release tags — alpha; not a stable dependency candidate (2026-10-02)
  - [vendor] §1c/§1d: jev-cli v0.2.0 released 2026-09-25; `jev mcp serve` exposes tools as MCP callee; exit codes carry verdict (10 false, 11 abstain)

---

## Group G — termpanum-events

- `/home/hruzam/unikuklatrix/nablarva/.dev/research/termpanum-events/events-map.v0.2026-10-02.md` — establishes: 20-event shared vocabulary (internal version v0.3 at this filename), 4 derived states (working/waiting/idle/exited), per-vendor hook/record/PTY/L0 source assignments, vendor tiers (CC and Codex first-class; Gemini and agy second-level; jev model-role callee), envelope-convergence note with jev's `jev.event/v1` ledger format, dropped events list · date/state: 2026-10-02; "DRAFT for docket 8 — rows confirmed by majkee as reversible; v1 after first fixture run"; smoothed with majkee 2026-10-02 · does not show: v1 not reached (fixture not yet run); jev envelope convergence still open ("OPEN → majkee"); GM and AG rows in §1 mostly (S) or ? pending fixture; tmux 3.8 OSC 133 events cell not filled

  bears on the gate:
  - [wheel] §1 record-sources paragraph: rorhcdream/tmux-agent-status reads CC `sessions/<pid>.json` + Codex rollout JSONL; CC `claude agents --json` (preview) `state/status/waitingFor`; Codex App Server `waitingOnApproval` — cited record-source wheels for state without screen
  - [vendor] §1 record-sources: CC `~/.claude/sessions/<pid>.json` → `status: busy|idle|waiting|shell`; "sessionId stale after /clear, #36213" — confidence M, undocumented
  - [vendor] §1 jev paragraph: jev's own ledger `~/.jev/sessions/<id>/events.jsonl` with five kinds (request_prepared, send_attempted, reply_received, request_failed, disposition_recorded) — existing documented record format for a callee, confidence "confirmed" per single-writer lock + SHA-256 correlation
  - [smaller] §5: "the relay (stridulatrix) reads states derived from them, never the screen" — 20-event vocabulary explicitly designed to make screen reading unnecessary
  - [smaller] §2 four-states table: stall event (PTY-sourced, inferred) is the PTY-only waiting fallback; "cannot distinguish approval from slow tool" stated as a known limit
  - [vendor] §3 majkee decision (reversible, 2026-10-02): "projecting vendor-specific events into the app is chasing vendors — a race, likely unsustainable"; vendor hooks are sources, never words; vocabulary stays vendor-neutral
  - [vendor] §2 four-states table: "CC all 4 · CX working/waiting/idle, exited needs L0 · GM all 4 on paper (M, no fixture) · AG working/idle only · jev n/a (callee)" — per-vendor state coverage as of 2026-10-02
  - [wheel] §3 open item: envelope convergence with jev's `jev.event/v1` before jev's implementation starts; "jev is at Flight-review stage — the cheapest moment to align field names" — existing format candidate worth examining

---

## Group H — pty-community

- `/home/hruzam/unikuklatrix/nablarva/.dev/research/pty-community/pty-observation.prior-art.2026-10-02.md` — establishes: community prior art for PTY-layer observation of agent CLI sessions; ranked failure modes for screen-based approaches; 9 unsolved problems as of 2026-10-02; stable/TIMELESS vs weather classification of PTY primitives; "pattern in the field: hooks first, files second, screen last" (M) · date/state: 2026-10-02; @Epoch; scope is PTY/terminal/mux layer only (hooks explicitly out of scope) · does not show: quantified false-positive/negative rates for any screen classifier; last-commit dates for community projects not read; tmux 3.8 release status unverified (rc3 seen); CC issues #69577/#79229 state not read

  bears on the gate:
  - [wheel] §2: agenmux (yaakov300/tmux-agents-mon): scraping-only, 4 states, bottom 20 lines + pane title, per-agent pattern files in `~/.config/agenmux/agents/` — existing PTY-only wheel; known limit: "transient screen redraws can cause state flickering" (confidence M)
  - [wheel] §2: ccmanager (kbwo): PTY output parsing, idle/busy/waiting per CLI, 1.3k stars, MIT, covers Claude/Gemini/Codex/Cursor/Copilot/Cline/OpenCode — large existing wheel (confidence M, summary)
  - [wheel] §2: nipunravisara/tmux-agent-status and siblings: hooks → tmux user options keyed by `$TMUX_PANE`; "deterministic, independent of model output" — no screen reading, existing approach (confidence M, search digest)
  - [wheel] §2: herdr failure mode: "❯ visible ⇒ idle" is wrong for CC; only footer text "esc to interrupt" separates idle from working — documented false-positive for prompt-based classifiers (confidence M, issue #179)
  - [smaller] §1.3: BEL/OSC 9/777 is "the only vendor-native waiting/idle signal that lives in the PTY stream"; OSC 9/777 swallowed by tmux unless passthrough; BEL works with monitor-bell — a smaller in-band signal path with known tmux limitation (confidence M)
  - [smaller] §4 TIMELESS: SIGCHLD/wait4/pidfd, pipe-pane, pane-died, POSIX termios form a liveness floor that is independent of vendor API changes — classified as stable (confidence H, TL)
  - [vendor] §1.2: Zellij 0.44.0 (2026-03-23): `zellij subscribe --pane-id` → NDJSON `pane_update`/`pane_closed` events, rendered viewport on change — confidence H
  - [wheel] §3: bracketed-paste + Enter race documented in multiple community projects; fix pattern: `load-buffer` (unique name) → `paste-buffer -p -d` → Enter in one invocation, or 0.3–0.4 s delay + rescue CR — an existing documented failure mode the relay must address (confidence M)

---

## Group I — termpanum-X0-source-contract

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/source-contract.md` — establishes: documentary qualification contract for `pipe-pane -O` as a PTY output source; planned workloads with exact bounds (normal 256 KiB/30 runs, burst 4 MiB/30 runs, false-completion, sink-failure, identity-reuse, replay/rejection); ADOPT narrow lab method recommended; Q path proposed as `termpanum-X1-source-fixture/`; struck hooks-stop rule recorded as stale and inoperative · date/state: 2026-10-22; "all qualification below is planned"; SHA-256 7086e595...; accepted by Majkee 2026-10-22 as documentary input · does not show: qualification not yet run; no D4 verdict; fixture execution not authorized by this document; language/dependencies for Q not selected here; no event schema, four-state vocabulary, or shared consumer contract created

  bears on the gate:
  - [smaller] §Method choice: pipe-pane -O "reuses tmux's own pane PTY without claiming ownership or durability" — explicitly preferred over new PTY owner or Zellij adapter for the first source question
  - [smaller] §Method choice: "capture-pane-only is rejected for Q because a snapshot cannot establish original output completeness" — eliminates one candidate approach for byte-fidelity qualification
  - [smaller] §Distinct legacy constraints: struck hooks-stop rule — original Termpanum brief's "stop when hooks cover every state" rule struck on 2026-10-02; "PTY floor is now unconditional on vendor features" and "inoperative"
  - [smaller] §Distinct legacy constraints: D4 remains binding; "research gate required before Q/C build unless Majkee grants explicit named exception naming the exact Q effects"
  - [vendor] §Scope: tmux 3.7c pinned as target; "first question is version-scoped to tmux 3.7c. A Q run must record its actual binary, tag and hash again" (2026-10-22)
  - [smaller] §Corrected independent oracle: oracle author and collector author are different sequential assignments; oracle frozen before collector work — separation of concerns for qualification
  - [smaller] §Observation contract: "freshness is not inferred from output silence. A quiet source can be known alive when an independent fixture control and direct child wait status prove it" — explicit limit of pipe-pane as a liveness signal
  - [vendor] §Method choice: Zellij adapter deferred "because it changes ownership/effects before the small source question is answered" — scope boundary stated in this document

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/review.packet.r2.2026-10-22.md` — establishes: cycle-05 independent PASS for the Termpanum X0 documentary packet; confirms source-contract SHA-256 `7086e595...` and research-disposition SHA-256 `b2cad9da...`; confirms Q path `termpanum-X1-source-fixture/`, distinct writers, and separate Q helper language release as requirements · date/state: 2026-10-22; cycle-05 independent verifier; VERDICT: PASS · does not show: "PASS supplies documentary readiness only, not a D4 verdict, Q/C release, architecture choice, or runtime acceptance"; URL reachability not independently rechecked in this cycle; 590+1 corpus count not rerun

  bears on the gate:
  - [smaller] §RESIDUAL RISK: PASS is documentary only — no D4 verdict, no fixture or Q execution release, no C release, no runtime acceptance — explicit scope limit on what the acceptance supplies
  - [smaller] §EVIDENCE: Q helper language/dependencies "must be separately and explicitly released" before Q execution — a remaining prerequisite even after documentary acceptance
  - [smaller] §EVIDENCE: independent oracle must be authored and hashes frozen before collector implementation — ordering constraint preserved in this PASS

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/decision.majkee.packet-acceptance.2026-10-22.md` — establishes: Majkee accepted the independently checked documentary packet as ready input for the relay-research decision; gate MET; narrow ADOPT remains a recommendation; acceptance supplies no D4 verdict, fixture or Q execution exception, collector or C release, or runtime acceptance; relay-verdict owner not appointed · date/state: 2026-10-22 17:58 CEST; recorded by cartan-termpanum-x0; GATE MET · does not show: D4 verdict not supplied; open ownership decisions not resolved; no successor bed opened; "appoints no relay-verdict owner and resolves none of the open ownership decisions"

  Note (paraphrase, not verbatim operator words): The operator's message accepted the packet as ready input for the relay-research decision, stated the gate was met, and confirmed the narrow ADOPT remains a recommendation that does not authorize fixture or collector execution.

  bears on the gate:
  - [smaller] §Accepted subject and effect: "narrow ADOPT remains a recommendation" — the source contract's ADOPT recommendation for pipe-pane -O is explicitly not locked by this acceptance
  - [smaller] §Accepted subject and effect: acceptance is "ready input for the applicable relay-00-research decision" — framed as input to this gate, not a substitute verdict
  - [smaller] §Accepted subject and effect: acceptance "supplies no applicable D4 verdict, fixture/Q execution exception, collector/C release or runtime acceptance" — four-clause limit

---

## Group J — nablarva-X4-vist

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/brief.x4-runbook-input.cartan.2026-10-23.md` — establishes: authoring brief for X4 (PTY/tmux/Termpanum/VIST shared work vault); five disposition rows for effects/authority, identity/evidence, recovery, homes/effects, independent acceptance; U-rows (U1–U4) as authoring candidates; master-file handoff through Majkee; L4 reconciliation required before any automatic send-keys experiment · date/state: 2026-10-23; Cartan; "documentary brief, not a RUNBOOK, gate, plan amendment or execution release" · does not show: RUNBOOK not authored yet; X4 "remains raw-only until a RUNBOOK is separately authored"; no releases follow from upload; D4 route still must be identified

  bears on the gate:
  - [smaller] §Effects and authority row: "Separate observation, deadline/retry decisions and typing/Enter" — effects and authority must be kept distinct; directly applies to relay relay-send design
  - [smaller] §Effects and authority row: "Any proposed automatic send-keys experiment needs explicit L4 reconciliation by Majkee; inherited source labels are not a witnessed exception" — L4 (tmux send-keys as a recorded death) applies to any relay injection
  - [smaller] §Effects and authority row: D4 decision route must be identified; "no implication from X0/X2 GO" — gate rule carried forward to any relay build
  - [smaller] §Independent acceptance row: "a local HELLO log is not the room journal or an adopted VIST envelope" — local observation vs shared event schema is a live distinction for the relay
  - [smaller] §Concrete authoring task, final sentence: "Qualified evidence may later feed C/R/L/E/V; none is already released by this brief" — no relay transport or relay build released by this prior work

---

## Group K — observations

- `/home/hruzam/unikuklatrix/nablarva/.dev/observations/termpanum-X0-source-contract.cartan.2026-10-23.md` — establishes: promoted process observation from termpanum-X0; records session scars — search overstating literal exclusions, shortened paths, 591-vs-590 corpus count, undefined Q base; explains why the arc held (one body writer, separate reviewer, immutable generations, corrections attributed to their actual bytes); "no successor opens here"; post-termios oracle and Q helper language/dependencies remain outstanding prerequisites · date/state: source 2026-10-22, promoted 2026-10-23; Cartan; preservation commit 78ff8b22; append-only, never pruned · does not show: no prune performed; no successor opened; this file is a process keeper, not a results record

  bears on the gate:
  - [smaller] §Scars: "establish path roots and corpus membership before delivery" — process lesson applicable to relay gate's own evidence packets
  - [smaller] §Why the arc held: one body writer + separate reviewer + immutable earlier findings = attribution stays correct per correction — method applicable to relay gate's review chain
  - [smaller] §Checked rules: "narrow ADOPT is a recommendation and supplies no D4/Q/C release" — the distinction between recommendation and release is a process lesson for relay-X2-research
  - [smaller] §Checked rules: "post-termios oracle and separately released Q helper language/dependencies remain prerequisites" — these are outstanding before relay can proceed to PTY build

---

## Verdict-like statements found

Every place where one of these files itself states or recommends REINVENT / ADOPT / REFUSE or an equivalent:

1. `research.epoch.hooks-vs-pty-meaning.2026-10-01.md` §VERDICT: "Driller's meaning-extraction is redundant for Claude and Codex. It stays a live, but NARROW, contingency for agy ONLY, and only for the one state 'waiting-for-approval'." — equivalent to REFUSE PTY-meaning-extraction for first-class vendors; partial REFUSE for agy except one narrow case. Author: @Epoch. Status: research report, not gaveled.

2. `research.epoch.hooks-vs-pty-meaning.2026-10-01.md` §VERDICT: "Recommended before building anything: run termpanum's EXPECT/TRIGGER/OBSERVE on an agy fixture" — equivalent to DEFER build; fixture must precede build decision. Author: @Epoch. Status: recommendation, not gaveled.

3. `vendor-events.catalogue.2026-10-02.md` §6: no explicit ADOPT/REFUSE verdict; residual unknowns listed as "what this pass could NOT settle." Status: open fixture list.

4. `source-contract.md` §Method choice: "Recommendation: ADOPT the narrow lab method—capture, retain, replay and compare one prospective version-scoped `pipe-pane -O` source, with independent post-termios byte and rendered-screen expectations." Author: cartan-termpanum-x0. Status: recommendation; accepted as documentary input by Majkee 2026-10-22, but "narrow ADOPT remains a recommendation" per decision file — not a D4 verdict, not gaveled.

5. `source-contract.md` §Method choice: "`capture-pane`-only is rejected for Q because a snapshot cannot establish original output completeness." — equivalent to REFUSE for capture-pane-only as byte-fidelity qualification method. Author: cartan-termpanum-x0. Status: documentary recommendation, accepted as input.

6. `decision.majkee.packet-acceptance.2026-10-22.md` §Accepted subject: "The narrow ADOPT remains a recommendation. This acceptance supplies no applicable D4 verdict, fixture/Q execution exception, collector/C release or runtime acceptance." — restates recommendation status of ADOPT; confirms no relay verdict issued. Author: cartan-termpanum-x0 recording Majkee's words. Status: GATE MET; ADOPT remains recommendation.

---

## Disagreements seen

1. **Q path name discrepancy.** `source-contract.md` (accepted 2026-10-22) proposes `Q = .dev/session/termpanum-X1-source-fixture/` as the fixture bed path. The first map (`prior-evidence.map.md`) documents the actual running bed as `.dev/session/termpanum-X1-source-qualification/STATUS.md` (suffix "source-qualification" not "source-fixture"). Both are dated before 2026-11-26. Whether the bed was opened under the proposed name or a different one, or the source-contract name was revised before opening, is not resolvable from these two files.
   Paths: `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/source-contract.md` vs first map entry for `termpanum-X1-source-qualification/STATUS.md`.

2. **jev announcement date conflict.** `jev.agent-cli.2026-10-02.md` §1 candidate table: "Announced 2026-09-15 (flaviocopes.com search digest) vs 2026-09-28 (typesafe.ai blog fetch summary)." Both dates are within the same file and explicitly flagged as unresolved. Noted here because a gate that includes jev as a target vendor cannot settle on its birth date from these sources.
   Path: `/home/hruzam/unikuklatrix/nablarva/.dev/research/vendor-events/jev.agent-cli.2026-10-02.md` §1.

3. **jev-guard Codex hook name.** `jev.agent-cli.2026-10-02.md` §1a: jev-guard reports `BeforeTool` for Codex. `vendor-events.catalogue.2026-10-02.md` §2a documents Codex's 12 events where the equivalent is `PreToolUse`. Both files are from 2026-10-02; the jev.agent-cli file explicitly notes this as "unreconciled."
   Paths: `jev.agent-cli.2026-10-02.md` §1a vs `vendor-events.catalogue.2026-10-02.md` §2a.

4. **events-map file name vs internal version.** The file is on disk as `events-map.v0.2026-10-02.md` but its internal YAML header declares `version: v0.3`. The first map does not reference this file (it is new to this map). Whether the filename was frozen at v0 and later iterations applied internally without renaming, or v0.3 is the same as v0 by convention, is not stated in the file.
   Path: `/home/hruzam/unikuklatrix/nablarva/.dev/research/termpanum-events/events-map.v0.2026-10-02.md` header vs filename.

---

## Not read / not found

- `.dev/session/termpanum-X0-source-contract/raw/research-disposition.md` — excluded by instruction: "being read by the lead itself"
- Glob of `.dev/research/termpanum-events/` found one file only (`events-map.v0.2026-10-02.md`); no later version of the events map exists in that folder
- Glob of `.dev/research/pty-community/` found one file only (`pty-observation.prior-art.2026-10-02.md`); no other `.md` files in that folder
- Files referenced within these sources but outside the listed set: `.dev/session/nablarva-X2-builder-narative/raw/research.tmux-source-fidelity.2026-10-22.md`; `nablarva-X2-builder-narative/raw/termpanum.build-plan.md`; `toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md`; `meshup/lab.observability-probes.2026-08-01/DESIGN.md`; `toolbox/termbrana/DECISIONS.md` (ADR-0002); nablarva-X4-vist handoffs and catalogue files referenced in the brief — all outside the listed source set, not opened
- `nablarva-X4-vist/raw/handoff.x0-source-contract.cartan.2026-10-23.md` and sibling handoff/catalogue/consult files in that bed — referenced within `brief.x4-runbook-input.cartan.2026-10-23.md` §Read before authoring; outside the listed source set; not opened
- CACHE.md, CACHE.exec.md, CACHE.lead.md in any bed — hard rule; not opened or listed
- `.majkee/` and `.hlm/` directories — hard rule; not listed or opened

Also noticed: `pty-observation.prior-art.2026-10-02.md` §2 documents `c9watch` (minchenlee PR #132) using `claude agents --json` + liveness to drop dead PIDs before status inference — a wheel that uses the research-preview API named in vendor-events.catalogue C7, and one that is not yet in the first map's wheel inventory.
