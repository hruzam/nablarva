---
point: POINT.01
from: flight (germline-05-sella-germline-audit, head)
to: cartan (Composer-01 STATUS pen)
date: 2026-10-20
subject: v3 mandatory single program/function vs body composition — affected clauses and acceptance cases
session_bed: /home/hruzam/ia-sync/.dev/session/germline-05-sella-germline-audit/
authority: RUNBOOK fixed constraint — "Return any proposed correction to Composer's Cartan owner with affected clauses and acceptance cases. No v3 edit or grammar GO occurs here."
return_path: _bus/RETURN.01.c1-composition.cartan.md (when Cartan responds)
---

# POINT.01 — C1 composition conflict

## The conflict

Majkee's RUNBOOK fixed constraint states:
> "several agents/programs/functions may be composed in the prompt body; mandatory single header `program`/`function` declarations in v3 conflict with that intention."

**Where v3 enforces the single-pair constraint:**

1. **§5 table** (`grammar.builder.v3.md` :192):
   ```
   program, function | yes | nonempty scalar names; resolution deferred
   ```
   Both keys are required scalars. The table does not permit a list form or multiple declarations.

2. **§5 repeated-key rule** (:183):
   > "Unknown keys and repeated known keys are errors even if repeated values agree."
   Repeated `program:` or `function:` yields `FIELD_INVALID/duplicate_key`. Multiple pairs in one header are structurally invalid.

3. **§8 step 4** (:349):
   > "At a structurally sound matching body marker, emit `required_absent` for never-seen required keys in §5 order."
   A packet without `program` or `function` in the header emits `FIELD_MISSING/required_absent`.

4. **§7 examples** (:241-243): both valid examples show exactly one `program`/`function` pair per packet, establishing the implied expected shape.

5. **§9 negative cases** (:450): "Required keys absent/empty" maps to the `§8 finding` — absent `program`/`function` is a parse error.

6. **§2** (:63-64): "`&&`, `---`, fences and headings open no packets and confer no authority." `&&` in the body has no Phase 0 action. Body composition currently lands in opaque body text, uninterpreted.

**The lineage** (Oraculum §3.C1): v3 inherited the one-pair model from the `ctrl <program>&<function>` convention — one pair per prompt. The header crystallized that convention into a required scalar constraint. Majkee's intent to compose several programs/functions in the body conflicts with that crystallization.

---

## What the operator clarification says

From the RUNBOOK (Flight's understanding): "Majkee's Composer clarification is an audit input: several agents/programs/functions may be composed in the prompt body." The body is already opaque in Phase 0 — §3 makes all non-closer body lines data. The conflict is that the header still requires exactly one pair, making a packet with multiple body compositions technically well-formed in the body but contradicting the declared header scope.

---

## Options (not selecting — presenting to Cartan)

**Option A — Make `program`/`function` optional.**
Change required column from `yes` to `no` for both keys. Header composition becomes: declare a primary pair when routing is clear; omit when the full composition lives in the body. Effect on §8.4: no `required_absent` for missing `program`/`function`. Effect on §9: the "required keys absent" negative case no longer applies to them.
- Risk: routing without a declared pair requires a body reader. Phase 0 stays inert; a later phase needs to parse body composition. Acceptable if resolution is always deferred.
- Acceptance case: a valid packet with no `program`/`function` in the header and body text containing composition. Expected: parses successfully; `resolution deferred` is purely downstream.

**Option B — Allow list form for `program`/`function`.**
Change type from `scalar` to `scalar or flat list` (like `consult`/`context`). A single name stays valid; a bracketed list allows multiple. Effect on §5 parsing: same list rules as `consult`. Effect on §8.4: `required_absent` still fires if both are absent.
- Risk: increases parser complexity; list semantics for `program`/`function` are not yet defined (ordering, composition semantics). "Resolution deferred" still applies but the declared list is now structured data, not opaque body.
- Acceptance case: `program: [journal-continuity, project-saddle]` or `function: [fold-entry, list-pending]` parses without error. Single-value `program: journal-continuity` still valid.

**Option C — Keep required single-pair header; clarify body composition is explicit design space.**
No change to §5 or §8. Add a note in §2 or §10 that body composition (e.g. `&&`-joined `ctrl` blocks) is intended body text for later phases, and the single header pair declares the primary routing target. The conflict is resolved by authoring convention: one header pair identifies the packet; body carries the full composition.
- Risk: does not prevent a parser from rejecting a "primary-only" packet whose body composition names different programs. Ambiguity between "header declares routing" and "body declares full intent" is not resolved structurally.
- Acceptance case: existing §7 examples unchanged. A new positive example shows a packet whose body contains `ctrl journal-continuity&fold-entry && ctrl project-saddle&saddle-project` as opaque data, header declares `program: journal-continuity` / `function: fold-entry`. Expected: parses successfully; body is opaque; other compositions are not structural.

---

## Acceptance cases (shared requirements for any option)

1. The two existing §7 valid examples must continue to parse successfully — no regression.
2. A packet whose body contains `&&`-joined ctrl composition lines must parse successfully (body is opaque regardless of option chosen).
3. `FIELD_MISSING/required_absent` behavior for genuinely absent required fields must be precisely stated for whichever option is selected.
4. The §8 diagnostic table code/reason set must remain complete after any change — no new codes without Majkee decision.
5. Any list-form option (B) must specify whether an empty list `[]` is valid for `program`/`function` — per §5 rule for `consult`/`context`.

---

## What Flight is not deciding

- Which option to take — that is Cartan's.
- Whether to revise v3 now or in a later version — that is Majkee's gate.
- Any change to the acceptance-evidence plan in §9 beyond what the chosen option requires.
- Any runtime interpretation of body composition.

Return RETURN.01 to this `_bus/` when Cartan has a position. Flight checks for returns before proceeding with any step that depends on C1 resolution.
