# chapter-ladder — frontmatter, and the ladder hiding inside it

> Raw form. A working chapter, not a spec. Captures a live discussion between
> @majkee and Medusa (applications-in-common session, 2026-08-08). Conclusion at
> the end is mine — everything before it is the shape of the argument as it moved.

---

## Where it started

Question on the table: markdown, but with **JSON frontmatter** — can we encode
that? Yes, trivially. Two conventions in the wild:

- **Bare JSON object** (Hugo-style): file opens with `{ … }`, that brace-balanced
  block is the frontmatter, the rest is body.
- **Fenced with a language hint** (gray-matter): `---json` … `---`.

The real question was never "can we" — it was "whose parser reads it." A YAML
reader will *often* swallow flat JSON (JSON is a YAML subset), but it breaks the
moment you lean on the bare-`{}` form or JSON-specific quoting. So: encodable,
yes; free swap, no.

## The family, walked one by one

**YAML** — the ecosystem default. Wins on nested data if you have a schema check.
Loses on hand-editing: silent type coercion (the Norway problem, `no`→false,
tabs vs spaces). It fails *quietly*, which is the worst way to fail.

**JSON (+ relatives JSON5 / JSONC / HJSON)** — explicit delimiters, unambiguous
structure. Great when machine-generated end to end. Bad for human hands: no
comments, trailing-comma traps. The relatives patch the human wound without
leaving the family.

**TOML** — the middle path. No whitespace footguns (explicit by construction, so
it fails *loud*), native RFC-3339 datetimes as a real type, `#` comments, no
mandatory key quoting. Loses hard on deep nesting — nested tables get ugly past
two levels. For a flat, hand-edited, **dated** surface it's the strongest of the
three.

**JS / MDX export** — the odd one out: not data, *code*. `export const meta = {…}`,
values can be computed (`new Date()`), doc can *be* a component. Powerful in a JS
pipeline. But reading it means **executing** it — an eval surface — and it binds
you to a runtime. It's the literal inversion of "the card governs belief, not
execution." Ruled out on doctrine, not taste.

**HTML / PHP / XML (markup family)** — the cycle is the tell. Pure HTML has no
loop because it's a *document tree for presentation*, not a data model; to get a
cycle you wrap it in a template engine (PHP `foreach`, Blade), which is code
around markup — back to the JS problem. XML is the honest member (a real data
tree) but verbose. Encodable, not a data format. Earns its place only when the
artifact *is* a rendered document.

**Compiled-ecosystem formats (Rust / C++ / C#)** — the ones probed last:
Bincode/Postcard (Rust), Bond/FlatBuffers/Cap'n Proto/Protobuf (C++/C#),
MessagePack/CBOR (cross-lang). All **binary wire formats** — fast, tiny,
zero-copy, and completely unreadable at the top of a text file. Frontmatter
*requires* human-readable delimitable text, so these fail by definition:
representable only as base64 blobs, which throws away every reason frontmatter
exists. The one compiled-ecosystem member that qualifies is **RON** (Rusty Object
Notation) — text, readable — but it fails the same test JS did: it binds a
Python/shell harness to a foreign runtime.

**Programmable-but-safe config languages** — Dhall (typed, total, no arbitrary
eval), CUE (config + schema + validation), Jsonnet (templating). These matter not
as frontmatter but as **validators** over whatever format you pick.

## The turn — model-readability and the "moredimensional" effect

Second axis, sharper: what's most readable **to the model**, pure-data side, as
dimensionality rises?

- **Flat data:** JSON and TOML tie; TOML wins the human side at no cost.
- **Nested / multi-dimensional:** **JSON**, and not close — every structural
  boundary (`{ } [ ] : ,`) is a *hard token*. Depth is tracked by counting
  explicit delimiters, and that survives tokenization. YAML's depth lives in
  **whitespace**, and indentation is the least reliable thing to count — at depth
  3–4 a level can silently drop.

The finding hiding in the hunch: **there is a crossover.** YAML optimizes for
human eyes; JSON optimizes for model accuracy; the gap only opens as depth grows.
"Most readable" is not one format — it's **depth-dependent**.

Prediction (falsifiable, to be tested by needle-at-depth, fresh eyes scoring, not
self-scored): *for a value at depth N, retrieval accuracy stays high for
explicit-delimiter formats (JSON) as N grows and degrades for indentation formats
(YAML); at N≤1 they tie; crossover ~depth 3–4.*

## The real idea — metadata scripting as a process ladder → events

The move that dissolves the earlier eval problem. The proposal wasn't "put code in
frontmatter" — it was metadata that describes a **process ladder**: rungs
(states), the harness signals that fire (events), and the transitions between
them. A trusted interpreter walks it.

This is a known shape — GitHub Actions (`on:` + steps), systemd units, Ansible,
K8s manifests, XState. And the harness *already is one*, enacted by hand:
`program.pulse.md` carries the rungs (staged → issued → blocked → parked → done),
the hooks are the events (SessionStart / Stop / UserPromptSubmit / SessionEnd),
and the orchestrator is the interpreter.

The key that keeps it honest: **declarative data interpreted by a trusted runtime
is NOT executable metadata.** JS frontmatter was bad because the metadata *was* the
code (read = eval). A declared transition table stays inert **data**; the runtime
owns execution. Metadata declares *desired state and legal transitions* — belief.
The interpreter owns *what runs* — execution. Never fuse them. That is the wiring
rule restated: "the card governs belief, not execution."

The line to hold:
- Metadata **may** declare: states, events, transitions, guards-by-name. (data)
- Metadata **may not** carry: expressions, computed values, conditionals-as-code.
  (the moment it does, it's JS frontmatter with extra steps, and inertness is lost)
- The interpreter reads a **defined schema surface**, not free prose.

Format fit for the ladder: TOML arrays-of-tables express a flat list of
transitions cleanly and inertly —

```toml
[[rung]]
state = "issued"
on    = "assay.PASS"
to    = "done"

[[rung]]
state = "issued"
on    = "assay.FAIL"
to    = "staged"
```

— and *this* is where CUE/Dhall finally earn keep: as a validator over the ladder
(every state reachable, every event handled, no orphan rung). Computation at
*check* time, inertness at *read* time.

---

## Conclusion (mine)

Three things settle out of this, and they don't all point the same direction —
which is the useful part.

**1. On format, for a hand-edited dated harness: TOML wins, and it's not close.**
Loud failure over YAML's silent coercion, native datetimes for a dated surface,
comments and no quoting-ceremony. The exotic formats either lose readability
(binary) or add a runtime dependency (RON/JS) for capability the surface doesn't
need. The only caveat is inertia — TOML commits the reader to a `+++` parser — but
in `.dev/` the reader is ours to control.

**2. On model-readability, format is depth-dependent, not absolute.** This is the
genuinely new thing in the discussion. For flat data, pick for the human (TOML).
For anything deep that the *model* must read reliably, explicit delimiters (JSON)
beat indentation (YAML), because delimiters are hard tokens and indentation is
whitespace. If a surface is both hand-edited *and* deep and model-read, that's a
real tension with no free answer — and it's worth measuring rather than asserting.

**3. On the ladder: this is the actual prize, and it's safe *if* it stays
declarative.** "Metadata scripting" is not reckless the moment you refuse to let
the metadata execute. Declare states/events/transitions as inert data; let the
trusted runtime (the Python/shell harness that already exists) enact them; validate
the shape with a schema. That is not inventing a format — it is recognizing you are
building a small declarative workflow engine and borrowing the proven shape instead
of eval'ing code.

But the honest placement, and I'll hold this line: the ladder is a **strong
experiment, weak foundation — yet.** It would formalize (and thereby ossify) a
state model that is still young and moving. So it does not belong baked into the
harness. It belongs in `experiments/<slug>/` with a hypothesis and a prediction
written first, let to clash with reality on one real loop (the assay PASS/FAIL
transition is the obvious candidate), and adopted only if the declared machine
actually beats the-orchestrator-as-interpreter rather than just adding a schema to
maintain.

The one-line version: **don't put code in the metadata — put the map in the
metadata and keep the engine trusted.** Belief in the card, execution in the
runtime, and prove the ladder before it becomes doctrine.

— Medusa, 2026-08-08
