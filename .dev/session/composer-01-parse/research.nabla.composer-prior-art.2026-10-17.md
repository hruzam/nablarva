---
kind: research
stamp: 8968de9b
date: 2026-10-17
author: nabla — Claude chat
method: raw/05_WAY_OF_THINKING.md, four questions per component
scope: the prompt composer (sella-v.0.1 workbench), Phases 0–4
sources: standing knowledge, named so it can be searched; not re-fetched today except where marked observed
---

# Composer — prior-art pass

SCOPE: the prompt composer, Phases 0–4.
CONTEXT: a hand-edited Markdown exchange read by deterministic code and by models; nothing may
reach a shell, and nothing writes a bed automatically.

Most of what prior art teaches is already in `raw/`; the table says where, so nothing is
re-derived. The "prior art adds" column is the only new material. The "ours" column is where
invention is allowed.

| # | Component | Conventional names (search these) | Already in raw/ | Prior art adds | Ours |
|---|---|---|---|---|---|
| C1 | Exchange document | mbox vs Maildir; event log with rebuilt projection (event sourcing) | `brief.oraculum`:12–15, :66; `note.myshell` §Own JSONL history (one event writer, index rebuilt from history) | mbox's scars: delimiter lines inside bodies (RFC 4155), and writers corrupting each other under locks that are only advisory. Maildir (Bernstein) dropped locking by giving each message its own file. → A1, A2 | a human-edited single file that models read |
| C2 | Packet header | front matter; strict YAML subset (StrictYAML); lossless round-trip | `brief.astrobley` §One readable source; `02` §Message file (flat, dependency-free) | Typed YAML loaders change values. Observed 2026-10-17, PyYAML `safe_load`: `no` → False, `2026-10-17` → a date, `01234567` → 342391 (octal). About 1 in 43 random 8-hex stamps is all digits. → A3, A5 | — |
| C3 | Signs | in-band vs out-of-band signaling; line-anchored commands (SMTP dot-stuffing, RFC 5321 §4.5.2); MIME boundary (RFC 2046 §5.1.1) | `02` §Zones (nonce markers are the only reserved strings), §Control verbs instead of magic words; `brief.oraculum`:17–20 | A sign means something only where control is read. Anywhere else the same text is content, so bodies never need escaping. → A4 | what `&&` triggers (Q4) |
| C4 | Procedure binding | dispatch table; lockfile pinning (Go `go.sum`, npm `integrity`); fail closed | `CONTEXT` §2.A (table binds name, path, expected stamp; mismatch stops); `brief.astrobley` §One generated representation | Lockfiles' usual scar: the source changes and nobody updates the pin. A read-only `check` can compare table stamps with function-file stamps. → A7 | — |
| C5 | Role binding, adapter outcomes | capability negotiation (LSP `initialize`); feature detection over brand sniffing; advisory vs mandatory controls | `brief.astrobley` §Policy and asymmetric adapters; `brief.oraculum`:32–42; `sella README` §What is neutral | A declared limit stays advisory until a test shows the effective control (precedent: the inert `sandbox_mode = "read-only"` key, witnessed 2026-10-17). → A8 | qualification by measured model behavior |
| C6 | Render, check | plan/apply (Terraform saved plan); generated-file marker (Go: `Code generated … DO NOT EDIT.`); linters report every finding | `note.myshell` §Own JSONL history (`prompts/<id>/<rev>.md` frozen); `CONTEXT` §9 | The previewed bytes are the carried bytes, never a re-render. A first-line marker keeps hand edits to a render from being lost silently. → A6, A7 | one outcome report per route |
| C7 | Evidence, receipts | end-to-end argument (Saltzer, Reed, Clark 1984); DSN/MDN (RFC 3464, RFC 8098); read-back with fixed phraseology; challenge–response | `sella README`:127–128 (neither stamps nor digests prove reading); `note.myshell` §Pending needs a reason; `journal.2026-10-16` §1.4 | Only the endpoint can confirm, and a receipt the recipient could produce without opening the file is no receipt: if the prompt carries the stamp, echoing it back proves nothing. → A9, Q1 | recipients that confabulate plausible receipts: cooperative but fallible |
| C8 | Fold preparation | maker–checker (four-eyes); patch workflow; optimistic concurrency (If-Match, RFC 9110 §13.1.1) | `sella README` §Folding automation; `brief.astrobley` §Partial reports and journal folding | A candidate prepared against one version of its target must say which. The owner's check becomes a comparison, not a reread. → A10 | owner by controller function; own-chapter scope |
| C9 | Handoff card | shift handoff with receiver read-back (I-PASS; Starmer et al., NEJM 2014); runbook | CS cards; `CONTEXT` §9 (next actions stay in STATUS, not in cards) | The receiver's first act is a read-back of what it loaded and of the next action as STATUS states it. | a receiver with no memory that may confabulate continuity |

## (a) Requirements to adopt

- **A1** The exchange has one writer: the human. No tool writes it in Phases 0–4. Machine output
  goes to the composer's own files.
- **A2** Packets in one exchange need delimiters that cannot occur by accident. A bare `---`
  already means three things here: front-matter fence, Markdown rule, and relay bracket
  (`brief.oraculum`:1 opens one, :88 closes it). Prefer the bus's nonce-marker form (`02` §Zones).
- **A3** Header values are strings. Parse the flat subset by hand, with no YAML library; compare
  stamps and ids as strings. Lists, such as `consult: [Astrobley]` in `brief.astrobley`, need a
  flat rule of their own, proposed in the Phase 0 grammar return.
- **A4** A sign counts only inside a declared header. The same text elsewhere is content.
- **A5** Round-trip: parsing and re-emitting a packet reproduces its bytes exactly, on the whole corpus.
- **A6** A render is frozen bytes with id, rev and digest. Its first line marks it generated and
  names its source packet. What is carried is exactly those bytes.
- **A7** `check` reports every finding in one pass, stale table stamps included, and exits with
  the catalogue codes of `01_SYNC_METHOD` (65 for data errors).
- **A8** `native` requires a dated witness of the effective control. Documentation alone gives `unqualified`.
- **A9** Proposed, pending Q1: the prompt carries path and packet id, not the stamp. The composer
  checks the stamp itself at render; the recipient's return quotes the stamp it found. That
  proves retrieval, not understanding.
- **A10** A fold candidate records the target's stamp at preparation. The owner applies only if it
  still matches; otherwise the candidate is prepared again.
- **A11** `raw/` is for reading while building. At runtime the composer reads owner files at their homes.

## (b) Risks to test

- **B1** A dirty Sublime buffer saved over an external write (lost update). Test before any writer unparks.
- **B2** Dictated or hand-typed headers: smart quotes, capitals, CRLF, BOM, tabs, trailing spaces.
- **B3** Bodies containing lines that look like signs, markers, headers or relay brackets.
- **B4** Receipt confabulation: can a recipient return a correct-looking receipt without opening the file?
- **B5** Preview fatigue: is the render still read at the tenth prompt? Record it in Phase 3.
- **B6** A stale candidate: the target changes between preparation and application.

## (c) Questions only Majkee can answer

- **Q1** Stamp in the prompt (the recipient can check the version before acting) or withheld (the
  return proves retrieval)? Nabla: withhold.
- **Q2** "Point, never restate": enforced in render, so the composer never inlines a pointed file,
  while the human stays free in Sublime? Nabla: yes; flagging restated text in `check` stays parked.
- **Q3** Compose where: packets inside the exchange (D4), or per-prompt `drafts/` as in
  `note.myshell`? Nabla: inside the exchange; render freezes a packet to `prompts/<id>/<rev>.md`.
- **Q4** What does `&&` trigger?
- **Q5** When does the small exchange stop being small: rotate by date, or by closed packets?

Sella's own open choices stay where they are: `sella README` §Open choices for Majkee and Nabla.
