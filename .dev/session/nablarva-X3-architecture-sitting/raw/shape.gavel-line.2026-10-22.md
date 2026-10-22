# Shape — the testable gavel line (for myShell's gavel loop)

`author: oraculum(cSharp) · 2026-10-22 · status: candidate convention (therapy S11 shadow gavel — majkee decides) · use: fold decisions from any source document into this shape; check every block with the tests below before majkee reads it`

Why: majkee's loop reads text, not pointers. A lean behind a path is invisible to it. Length is fine; unfindable is not.

## 1. The shape

```
GAVEL <id> · <question in one sentence>
  options:      a) …  b) …  c) …
  context:      <what this is about, in full sentences — enough to decide without opening any file>
  cost:         <per option: time · majkee's hands · risk>
  consequence:  <per option: what follows, what it closes, what it opens>
  lean:         <seat> → <option> — <one-sentence reason>
  source:       <path[:line] — for verification only, never the only carrier of meaning>
  answer:       ___
```

## 2. Tests (a block passes only if all hold)

| # | test | how to check |
|---|---|---|
| T1 | all eight fields present, in order | grep the field names per block |
| T2 | question is one sentence ending in `?` | line 1 |
| T3 | ≥2 options, each distinct | `options:` has `a)` and `b)` |
| T4 | `context:` is prose, ≥1 full sentence, and does not consist only of a path | not matching `^\s*context:\s*\S+\.(md|toml|yaml)\S*\s*$` |
| T5 | `cost:` and `consequence:` name every option | each option letter appears in both |
| T6 | `lean:` names a seat, an option letter and a reason after `—` | regex `lean:\s*\S+\s*→\s*[a-z]\)?.*—\s*\S` |
| T7 | every `source:` path exists | `test -e` per path (strip `:line`) |
| T8 | no decision is manufactured — if the source leaves it open, the block says `open:` in context and the lean may be "defer" | read against the source |
| T9 | `answer:` is empty (`___`) until majkee fills it | literal match |

## 3. Brief for the folding seat (paste as is; folder = @field or a myShell agent, checker = @assay)

```
Fold every pending decision in <SOURCE FILES> into the gavel shape in
<this file> §1. One block per decision, ids G<n> in source order. Write the
blocks to <OUTPUT FILE> (new file). Put the meaning in context/cost/
consequence/lean as text — a path goes only in source:. If a source leaves
a question open, say `open:` in context and do not invent an answer.
Return: the output path + count of blocks.
```

```
@assay: check <OUTPUT FILE> against tests T1–T9 in <this file> §2.
Read-only. Per block: PASS or the failing test ids + one-line reason.
Then T8 against <SOURCE FILES>: list any block whose options or lean
assert something the source does not say. Return the table only.
```

## 4. Notes
- The folder writes, the checker only checks — the same split as builder/witness everywhere else.
- Cheap: one folding pass + one assay pass per document set; neither needs the head's context.
- Compatible with the polyp PAD deck: a gavel block can sit inside a STEP; the PAD's report fence stays the answer sink.
