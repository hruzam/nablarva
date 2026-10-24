# Houston consult — the D1 move: observation record ≠ L3 room journal

`card: consult · spawned by oraculum(arch-X0) on majkee's "consult" (M6, 2026-10-24) · child route, read-only, wrote nothing, spawned nothing · landed verbatim by the head 2026-10-24 (clock-read in the same turn) · the move as briefed: separate (a) an organ-local observation record — per-source append-only files, one writer per file, readers merge, envelope not chosen — from (b) L3 S1's single-writer room journal, untouched; secondary context = the head's construction reading (layering by convergence; shared layers with ≥2 real clients; optional git-style router)`

---

Route: spawned by a parent agent → child; otherwise main session (canary: cl-e1a94c37).
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/consult.md · stamp: 5435b1c7

**About this run:** card consult, running as a child agent. Addendum found by walking up from the environment's working directory `/home/hruzam/unikuklatrix/nablarva`. I have no Bash, so I did not run `pwd -P`. I wrote nothing and spawned nothing.
**Files read:** `.dev/session/flag.md` (all of it) · `docs/ARCHITECTURE.md` §0–4, §9 · `raw/field.body-construction.r1.2026-10-24.md` §1–6 · `raw/inventory.what-exists.explore.2026-10-24.md` (summary table, plus a grep).

## Verdict: **stretches**

1. The move does not reopen L3. L3 S1 binds only "append-only single-writer journal as sole room truth" (locked: L3), and a lock reaches no further than its own text. So an observation record that never becomes room truth sits outside S1. The writer half of X4 is answered by v0's own candidate rule, "Every state file has exactly one writer" (said: ARCHITECTURE §3 row 1). No lock has to change (inferred: houston).
2. The grounding is a reading, not a lock. The plane table in §1 is labelled "`inferred: houston`, assembled from the locks cited per row" (ARCHITECTURE §1). §2.3 says "never depends on". L17 itself only says "Discovery is not delivery authority", and L20 says "Observations authorize nothing" (locked: L17, L20). So "the architecture already implies (a) ≠ (b)" holds at `inferred:` strength. Neither locks nor ARCHITECTURE §1/§2.3 state it as a locked separation.
3. Calling the record "organ-local" (said: cartan-x2 X2-2) is not yet proven. The observe seam's owner is `unknown:`. The named producers come from different organs: v0 living tissue, CLI hooks, and a termpanum collector. The record's readers are views (said: ARCHITECTURE §4 observe row; §9 cross-head X2-1). Without the constraints below, this is a cross-organ seam presented as a local record (inferred: houston).

## Constraints the move must carry

1. **One writer means one serialized writing process per file, not one kind of producer.** tmux `set-hook` runs once per event in every pane. If all those runs append to one "tmux file", the file has many appenders again. Split the files per instance or serialize the writes (inferred: houston, against said: ARCHITECTURE §9 X4 "one event record, many appenders").
2. **Name the organ that owns the record, or admit it is the §4 observe seam with its owner gap.** If the record turns into a mechanism shared across bricks, implementing it is a shared layer that needs its own release (locked: L21 (2)). The termpanum↔VIST↔stridulatrix overlaps stay unassigned (locked: L20).
3. **Merging by timestamp is a reader-side view, not truth.** It promises no total order and adopts none of the four envelopes. Docket 8 stays open (said: ARCHITECTURE §4.5), so X4's envelope half remains open and only its writer half is answered. The merge is a stage-1 rule only; it does not extend across hosts (locked: L2 framing; inferred: houston).
4. **The observation record never becomes room truth or delivery authority.** A room fact taken from it enters only through the journal's single writer (locked: L3 S1 "sole room truth"). No reader acts on it: no delivery, no pane close, no admission (locked: L17, L20; said: ARCHITECTURE §1 observation row, forbidden effects).
5. **A CLI-hook producer is a vendor feature.** It is allowed only as an optional producer writing observation to its own file, under "No vendor devices or features where avoidable" (locked: L14 D1). Hook → bus stays parked (said: ARCHITECTURE §9 X9; field P5). Building or running any producer needs a separate release (said: termpanum build plan §1 via inventory, "synthetic fixture needs a separate release").

## Secondary context
One break, a counting error: "boot/env has ≥2 real clients" counts HELLO r1. HELLO is a written contract with no code ("proposed, not implemented … no code found", said: inventory Summary). Also the two variables named don't overlap: `NABLA_BED` belongs to HELLO and `OV_*` to ovitmugen (said: field §4 row 1). Today boot/env has one coded client. Install/package and KEYS still stand (inferred: houston). The optional router reading has no break.

**ARCHITECTURE.md is behind the flag (the flag wins):** its header still says "DRAFT r7 … not promoted". §2 item 5, §4.7 and §9 still treat P5 as not yet decided and L17's narrow edge as unchanged. But L21 adopted P5-b on 2026-10-23, records promotion at f20dda5, and the Archived index lists the L17 phrases as superseded. Field D2 ("P5-a / P5-b proposals not yet gaveled") repeats the stale text. Cite L21 in place of ARCHITECTURE §2.5.

**Not verified:** I checked no source for HELLO r1 or v0 directly; the HELLO and v0 claims here come through field and inventory. I did not test whether O_APPEND writes are atomic on the target filesystem (constraint 1 assumes they may not be). The termpanum build plan is cited through the inventory only.

---

## Head's reading (inferred: oraculum, appended at landing)

- Verdict accepted. The move proceeds at `inferred:` strength with the five constraints; it is a design move inside the observation plane, not a lock change. I was stating the separation as if the architecture already locked it — Houston is right that it is a reading. Corrected.
- Counting correction accepted: shared layers with ≥2 **coded** clients today = install/package · KEYS grammar. Boot/env drops to one coded client (ovitmugen) + one contract (HELLO). My "three real" becomes "two real, one contracted".
- Constraint 1 is the sharpest: "one writer" = one serialized process per file. A tmux hook firing per pane is N appenders. The slice design must give each producer *instance* its own file or a serializer — this decides the record layout before any envelope question.
- Constraint 2 names the real hole: the observe seam has no owner. The slice cannot pretend the record is organ-local while termpanum (lab), VIST (principle) and living-tissue hooks all produce into it. Owner question → majkee, in the decision package.
- Stale ARCHITECTURE §2.5 / §4.7 / §9 vs L21: already carried in dock.md as the r8 items (C1); Field's D2 inherited the stale text. For this session: cite L21, never §2.5.
