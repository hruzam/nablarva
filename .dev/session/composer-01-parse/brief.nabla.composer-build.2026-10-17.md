---
kind: brief
stamp: e04f1a62
date: 2026-10-17
author: nabla — Claude chat, Majkee's Nabla.Tmux project
process-amendment: myShell, 2026-10-17; BUS return packaging and YAML scalar quoting only
project: nablarva
bed: ~/unikuklatrix/nablarva/.dev/session/composer-01-parse
reader: the composer builder (seat assigned by majkee)
owns: "decisions closed in the Nabla thread, and the phase frame. Live position: STATUS.md."
---

# Prompt composer — builder brief

STATUS.md says where the build is; this brief never does. Every source sits in `raw/`, pinned by
`SHA256SUMS`, so line pointers below stay exact. The prior-art pass and its ids (A, B, Q) are in
`research.nabla.composer-prior-art.2026-10-17.md`. Where a `raw/` file covers something, it wins
and the overlapping line here is the bug: report it, don't reconcile it.

## 1. What you are building

The workbench in `raw/sella-v.0.1/README.md` §The recommendation, drawn in §The animal's parts.
Three attributed views sit beside it: `brief.astrobley` (programmer), `brief.oraculum` (designer),
`brief.myshell` with `note.myshell.history-and-attachments` (the agent who will use it). The shared
question is `raw/EXCHANGE.md` §Shared question; the converged proposal is `raw/CONTEXT.md` §9.
The controller tables it resolves against are described in `raw/CONTEXT.md` §2.A. At runtime the
composer reads them at their homes, never from `raw/` (A11).

## 2. Decisions closed in the Nabla thread

None is gaveled; Majkee locks. Tags as in germline: `said` = Majkee stated it; `inferred` = Nabla
proposed it and no veto came.

| # | Decision | Rejected alternative | Tag |
|---|---|---|---|
| D1 | Build now; the sella pilot becomes the Phase 3 gate inside the schedule. | Run the pilot before building anything. | said: builders first learn the design from Nabla |
| D2 | This brief is a thin layer over `raw/`: decisions, phases, prior art. | A consolidated extract of the sella set: a second copy that drifts (day-square rule one, "point, never restate"; the Termbrana-02 failure). | said: format left to Nabla, 2026-10-17 |
| D3 | Sella's sharpenings stand as written: two bindings, four adapter outcomes, rendered ≠ carried ≠ accepted. | One merged binding table; supported/unsupported only; pins or diffs read as delivery; `LOADED` read as authority. | inferred |
| D4 | Reading unit: the whole exchange document, entered through a cold-start card that points at the one open packet and owner STATUS. | Message files as the human's reading unit (`brief.astrobley`). | inferred |
| D5 | The composer's handoff artifact is a cold-start card in the existing CS shape. | A new handoff format. | inferred: Majkee named the card the inter-session glue |
| D6 | Automation stops at fold preparation (`sella README` §Folding automation). Delivery and automatic writing stay parked, each behind its own authorization. | An automatic writer in v0. | inferred |
| D7 | Deterministic: no model in the parse or render path. An agent may later be a guest in one field. | Model-assisted rendering. | inferred |
| D8 | Terminal program first. No editor plugin; pins are plain files. The GUI (foil, belt, marker, slider) is parked as its own sub-animal. | GUI or Sublime plugin first. | inferred |
| D9 | Every composer sign starts its own line. | Inline signs with `"`-escaped `&&`. What `&&` triggers is still open (Q4). | inferred |
| D10 | Address first: vendor and project are known before any capability list is shown. | Capability lists before the address. | inferred |
| D11 | When delivery unparks, it goes through the bus gate and door; "confirm bash" only through the door, with pane capture and prompt-string match. | Direct send-keys from the composer. | inferred |
| D12 | Role binding selects among sessions registered in tmux (`04_REGISTRY`: definitions vs liveness). | A composer-side list of live agents. | inferred |

## 3. Phase frame

Dates are a frame, not deadlines. A phase opens only on the previous phase's dated finding.

| Phase | Frame | Build | Read first | Exit finding |
|---|---|---|---|---|
| 0 · readable document + parse | Oct 17–22 | Open with a grammar return for gavel: packet delimiters, header keys, list syntax, Q3. Then parse packets out of one exchange: header to data, body untouched, nothing executed. | `brief.astrobley` §One readable source · `brief.oraculum`:12–20 · `02_PARSER_GATE` §Message file, §Zones, §Parser · A2–A5, B2–B3 | Every corpus body round-trips byte-identical; every negative yields a diagnostic and none executes. Corpus: both `EXCHANGE.md` files, `brief.oraculum` and `journal.2026-10-16.md` §1.4, each used as a packet body, plus hand-made negatives. |
| 1 · resolve + load (two bindings) | Oct 23–29 | Procedure binding through the existing controller tables, read-only: stamp match or hold. Role binding through collaborator definitions and observed liveness. No new registry. | `sella README` §The animal's parts · `brief.astrobley` §One generated representation · `brief.oraculum`:22–42 · `04_REGISTRY` · `note.myshell` §Optional bed · A3, A8 | Two materially different bindings resolve; a stamp mismatch holds; an unknown binding is rejected. |
| 2 · render + check (preview only) | Oct 30–Nov 5 | Exact outgoing prompt frozen with id, rev and digest; one adapter outcome per route; every missing input reported in one pass. Nothing is sent. | `brief.astrobley` §Policy and asymmetric adapters · `note.myshell` §Pending needs a reason, §Own JSONL history · `sella README` §What is neutral · A6–A9 | The same source renders identical bytes twice; `check` lists every gap; each route shows native, manual, unsupported or unqualified. |
| 3 · experiment GATE | Nov 6–10 | No new features. Run the pilot. | `sella README` §Proposed first experiment · `brief.oraculum`:68–76 · B4, B5 | Dated finding against Oraculum's acceptance list, with recovery effort against the old journal workflow. Phase 4 opens only on Majkee's go. |
| 4 · fold preparation only | Nov 12–15 | Candidate: exact text, attribution, evidence, destination scope, target stamp, packet id, handed to the authorized function owner. No write. | `sella README` §Folding automation · `brief.astrobley` §Partial reports and journal folding · A10, B6 | The owner applied or rejected each candidate; work saved is measured (sella open choice 3). |

Beyond Phase 4, delivery and automatic writing stay parked.

## 4. Pen and method

- Write code only in the code home STATUS names. Anything else you would change, STATUS included,
  goes into your return as a prepared change for its owner.
- Never write `raw/`, journals, controller tables or the exchange. No commit, push, deploy or gavel.
- For work delegated through `_bus/`, return the six fields required by the bus guide.
  Include the five-line receipt from `raw/journal.2026-10-16.md` §1.4 (packet, evidence,
  observed, uncertain, gate) as a code block in field 2. The card's FIRST STEP remains a
  five-line conversational readiness receipt, before any work is authorized.
- When you add a component or a contract, or a failure surprises you, run the four questions in
  `raw/05_WAY_OF_THINKING.md` and record the decision with the alternative you rejected.
