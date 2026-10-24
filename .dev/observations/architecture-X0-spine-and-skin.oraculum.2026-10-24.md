origin: session-process record of `.dev/session/architecture-X0-spine-and-skin` (CS-card colleague briefing → decision package → /runbook authoring of X1 + X5) · written by the head oraculum(arch-X0) · Claude (Fable) at closure, 2026-10-24 14:20 CEST, on majkee's "You have my blessing for process" · promoted before prune per runbook GUIDE §On gate closure · preservation commit: the closure commit that carries this file (sha recorded in the commit message, not here)
status: append-only, never pruned · claims: said: (path) / inferred: oraculum

# architecture-X0-spine-and-skin — what the session taught about running sessions

`what ran: one Claude head on office, 2026-10-24 ~05:30–14:20 CEST, one compaction mid-arc; spawned: Explore (inventory), Delta (zip extraction; later YAML parse), Field (v0 corpus), Houston child card: consult ×1 · product: decision package r1+r2, substrate, two authored beds (architecture-X1-bookkeeping, nablarva-X5-spine-slice), three pulse rows · gate met 13:10 CEST`

## 1. Carriage that worked

- **Deck, one block per turn, answer landed verbatim before the next block.** Seven blocks X0-1…X0-7 from 11:08 to 11:35 CEST (incl. landing + STATUS rewrite each), all answered `a`, zero re-litigation. The method from the X4 handoff §6 held a second time. inferred: oraculum — the cost per block was one `date` + one `printf >>` + one whole-STATUS rewrite; the STATUS rewrite is the expensive part (see §3).
- **Organ walk before the deck.** Naming each organ and stating its purpose, letting majkee confirm/extend/narrow (his M7 request), produced the material the deck then only had to rank. Three structural moves came out of the walk, not the deck: the termbrana/stridulatrix split, the address registry, the config rule. inferred: oraculum — the walk is the synthesis phase; the deck is the smoothing. Do not skip the walk to get to the deck.
- **Houston consult as correction, not as blessing.** The consult returned `stretches` and two corrections of my own claims (the observation-record separation was a reading, not a lock; boot/env had one coded client, not two). Both landed as corrections in the package. said: raw/consult.d1-observation-record.houston.2026-10-24.md.
- **Field on a corpus the head had not read.** The v0 zip was consumed by Field (171-line return) rather than by the head; the head compared Field's survival table against the inventory and the law. Cheap and sufficient; one counting error caught by Houston.
- **Majkee's late inputs placed first.** The X-generation naming rule arrived inside the X0-7 answer; the `/runbook` hint arrived mid-turn while the substrate was being written. Both were landed verbatim with an `inferred:` reading before any file was renamed or authored. Nothing had to be undone.
- **Substrate → RUNBOOK in one step after the hint.** The substrate (written first as a handoff for "someone else's RUNBOOK") turned out to be 80 % of the RUNBOOK; `/runbook` then only needed the fixed-form fields, prompts and the res/ chapter. inferred: oraculum — write the substrate as if it were the RUNBOOK; the step from one to the other is the fill-in, not a rewrite.
- **Parse-check by a Delta.** The carrier Bash has no interpreter; a read-only Delta ran PyYAML `safe_load` on five blocks and reported PASS verbatim. Ten seconds, 16k tokens. Worth doing every time `/runbook` authors.

## 2. Faults, mine

- **Spec too narrow for the extractor.** My Delta allow-list for the zip excluded `.svg`; Delta STOPped correctly; resumed via SendMessage allowing .svg as text data. Fault: I wrote the allow-list from the filename I expected, not from `unzip -l`. Rule: list the archive before writing the allow-list.
- **A compound command blocked by the whitelist does not run at all.** One majkee answer (M6) had to be re-landed because the `printf` was chained with a blocked `$(…)`. Rule: `date` in one call, `printf >>` in the next, nothing else in the printf call.
- **Wrong continuity guess.** I proposed reposoma as the continuity organ; majkee: reposoma is an older RAG project. Continuity stays unowned (U-continuity). Fault: I filled a gap with a name instead of leaving it `unknown:`. The same class as X3's "citation wider than its text" — a label put where no fact was.
- **Re-litigating a parked item.** I qualified the send-keys death ("tmux|PTY should be the base consumer…") in a lens reading; majkee: park it 'unanswered', don't re-litigate. Rule (also handoff §3 rule 10): deaths are not reopened by qualification; park and name the owner.
- **Compaction mid-arc.** Context ran out after X0-1; the summary carried the state. The first post-compaction turn had to present X0-2 from the package text — the summary had noted it as "presented" when it had not been. Caught because the summary writer flagged the uncertainty explicitly. Rule: a STATUS `in_flight:` that says "presented" must be written after the chat turn that presents, not in the same turn (Agol U8, clock-and-order, applies to STATUS verbs too).

## 3. Costs worth naming

- **Whole-STATUS rewrite per deck block.** Seven rewrites of a ~70-line STATUS in 30 minutes. Correct under the replacement law, but ~1.5k tokens each for a one-field change (`in_flight`). inferred: oraculum — an `Edit`-class tool on STATUS is cheaper and equally lawful (the law is about the snapshot semantics, not about the write primitive); the carrier whitelist currently forces Write.
- **Two names for the bookkeeping bed.** I proposed `nablarva-X5-bookkeeping` / `nablarva-X6-spine-slice`; majkee chose `architecture-X1-bookkeeping` + X5 for the spine. inferred: oraculum — the slug line follows the *briefing line* that produced the work (architecture-X0 → X1), not the organ it edits; cross-organ construction takes the `nablarva-X` line. Carry this as the naming reading until a lock says otherwise.
- **`.dev/observations/README.md` is dirty with another head's lines.** I did not add this file's index line to README to avoid a shared-staging problem (handoff §3 rule 8). The index entry is owed by whoever commits README next.

## 4. Open after this session (named, not dropped)

U-send-keys (majkee, on X5 evidence) · U-steward (interim = cartan-x5) · U-continuity · U-vendor-spawn · docket 8 · Field Q5 (Cartan's bed) · muticula-01-qualify pulse row (majkee, at X5 closure) · the component's disk name (X5 P1, majkee GO) · the J1b wrapper sitting · N6/N8 (dock) · this file's README index line.

## 5. Pointers

- Bed (prunable after the closure commit): `.dev/session/architecture-X0-spine-and-skin/` — raw/answers.majkee.{feed,organs,deck} (his words), decision-package r1/r2, runbook-substrate, field r1, inventory, Houston consult.
- Products that survive: `.dev/session/architecture-X1-bookkeeping/{RUNBOOK,STATUS}.md` · `.dev/session/nablarva-X5-spine-slice/{RUNBOOK,STATUS}.md` + `res/sequence-and-u-rows.md` · `.dev/session/pulse.md` rows.
- Method inherited and re-proven: `.dev/session/nablarva-X4-vist/raw/handoff.csharp-method.oraculum.2026-10-24.md` §6 (costed deck), §7 (Houston by phase).
