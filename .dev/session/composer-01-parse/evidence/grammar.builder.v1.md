---
kind: grammar-proposal
version: 1
date: 2026-10-17
author: builder · native Astrobley
cycle: '05'
status: proposed; requires review and Majkee's grammar GO
scope: composer Phase 0 only; no implementation or deployment authority
---

# Composer Phase 0 — proposed readable packet contract

Every normative choice below is a proposal for this composer, not a change to the bus
handoff or a canon lock. The operator-directed publication route is ia-sync (flag L8′).
`/home/hruzam/ia-sync/zsh/composer/`, Python stdlib, and a fresh native Codex verifier
remain implementation review proposals. No source, installer, CLI command, delivery
adapter or registry is created by this document.

## 1. Source boundaries and adaptations

All paths in this document are relative to
`/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/` unless absolute.
The 19 frozen raw files passed `sha256sum -c SHA256SUMS` at startup. Source anchors:

| source | implication for this proposal |
|---|---|
| `brief.nabla.composer-build.2026-10-17.md:55` | Phase 0 proposes grammar before code; body byte identity and diagnostic negatives are the exit evidence. |
| `raw/sella-v.0.1/brief.astrobley.sella-v.0.1.md:15–45` | Small explicit header, `consult` list, exact body preservation; example uses `format: request/0.1` and author-written `id`/`from`. |
| `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md:12–20` | Whole readable exchange; declared structure, not discovery of commands in prose. |
| `raw/02_PARSER_GATE.md:20–66` | Flat header and whole-line nonce payload markers; header, payload and outside are distinct zones. |
| `raw/02_PARSER_GATE.md:93–105` | Bus fail-fast order mixes structural checks with identity, freshness, registry and gate matters. |
| `research.nabla.composer-prior-art.2026-10-17.md:35–48` | A2–A5 ask for unambiguous framing, string values and lossless round-trip; A7 asks for all check findings. |
| `research.nabla.composer-prior-art.2026-10-17.md:59–61,72–75` | B2/B3 require explicit typography/line-ending/marker behavior; Q3 needs a decision, Q4/Q5 remain open. |
| `raw/journal.2026-10-16.md:39–43,75–103` | Existing relay guards and packet words are content in this corpus, not composer authorization or live state. |

Disagreements remain visible:

- Bus `02:22,60` starts one message with bare `---`; composer needs several packets
  amid Markdown. This proposal uses nonce-bearing opening, body and ending markers,
  without a bare `---` control fence. The example's header keys remain recognizable.
- Bus `02:44–52,95–97` requires `bus`, `type`, `created`, derives sender and rejects
  author-written `id`. Composer instead declares identity as strings, as in the
  personal Astrobley proposal. It authenticates nobody and performs no bus submission.
- Bus `02:65` says marker-looking payload is plain text, while `02:66,98` reserves
  exact nonce markers. Those claims cannot cover an exact active end marker embedded
  in its own body. Sections 3–4 reserve the active marker lines and expose this limit;
  random selection alone is not collision proof.
- Bus `02:99` rejects empty task bodies and transport control bytes. This inert
  document parser accepts empty bodies and valid UTF-8 body data, including controls.
  Delivery safety checks remain a future layer; acceptance here is not paste safety.
- Bus `02:93` is fail-fast; research A7 asks for every finding. Section 7 collects
  independent header findings within safely framed input, but stops framing at its
  first structural failure. It does not claim exhaustive diagnostics on corrupt input.

The brief's instruction at `brief:17–18` to report overlapping raw disagreements is
honored by this table; none of these adaptations rewrites or supersedes raw/02.

## 2. Reading unit and Q3

Propose packets inside the single human-owned exchange, in document order. Outside
text remains ordinary Markdown, including notes, relay brackets and historic replies.
The parser reads one saved byte sequence and never edits it. A dirty editor buffer
is not part of that input; parsing proves nothing about its unsaved contents.

Q3 proposal: the exchange is the composition source; no parallel per-prompt drafts
tree. Later frozen `prompts/<id>/<rev>.md` outputs may be derived from a selected
packet under Phase 2 authorization. They are not built in Phase 0. Existing source
EXCHANGE files are corpus bodies, not already-valid composer documents to migrate.
There is no inferred packet from informal `to-...`, `from-...`, `&&`, front matter,
Markdown fences or journal headings. Q4 assigns no `&&` action in Phase 0; Q5 rotation
and Q1/Q2 rendering decisions stay outside this grammar decision.

## 3. Delimiters, states and collision policy

Use these exact ASCII whole-line forms, at column 1, with one ASCII space at each
shown gap. `N` is exactly 16 lowercase hexadecimal characters `[0-9a-f]{16}`:

```text
<!-- composer:packet N -->
format: request/0.1
id: review-17
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
consult: [Astrobley]
<!-- composer:body N -->
Review the named sources.

<!-- composer:end N -->
```

`N` above is a placeholder, not a valid literal nonce. The blank physical line before
the end marker in this example means the body ends with one LF under LF framing.
Nonce length is a composer proposal rather than the bus's 4–8 character rule (`02:66`).
It reduces accidental matches; uniqueness and a preflight scan do the actual work.

There are three states: outside, header(N), body(N). In outside, an exact packet
marker opens a header. An exact body/end marker there is an orphan error. In header(N),
only header lines and the exact body(N) marker are permitted; any other marker is an
ordering error. In body(N), only exact markers carrying N are active: end(N) closes;
packet(N) or body(N) is a collision/order error. Every marker with a different nonce
is literal body data, even a complete example packet. Do not recurse into bodies.

After closing N, any subsequent exact marker carrying N in outside is an error;
nonces cannot be reused by top-level packets anywhere in the document. Outside notes
may precede, separate and follow packets. A document with no top-level packets is an
error. Every packet must finish before another top-level packet begins. A closing
marker may be the final unterminated physical line at EOF; open/body/header lines
must have their required framing EOLs. No partial packet is successful at EOF.

Exact recognition does not consult Markdown: a whole active marker line in a fence
or ordinary body prose has its structural meaning. Inline markers, indented markers,
markers in block quotes, capitals or markers with trailing spaces are literal body
data. Outside/header lines beginning with the exact ASCII prefix `<!-- composer:`
but failing a marker form are BOUNDARY_INVALID (including indent/trailing-space,
capitalized verb, invalid nonce and truncated closing `-->`). Leading ASCII spaces
or tabs are ignored only to detect this malformed-marker error there, never to accept
a delimiter. Elsewhere ordinary outside prose is retained without parsing. Within a
body, malformed marker-like lines are data; only the exact active forms are reserved.

Collision policy for composing a body B: choose a nonce, scan B by physical lines for
all three exact active forms with that nonce, and choose another nonce if any occurs.
Include B's final unterminated line: adding the framing separator will terminate it.
Also ensure no reuse among top-level packets. Never escape, trim, substitute or
rewrite B to make it fit. This is a proposed preparation/check rule, not permission
for the parser to edit the human's exchange.

The parser detects packet/body(N) inside B and duplicate closing markers after a
premature end(N), including those in fences. It cannot infer intent when a body has
one end(N) that the author intended as prose and no later real end(N): that byte
sequence is indistinguishable from a valid packet followed by outside notes. Thus
structural validity cannot prove intended body extent. Exact-body guarantees require
the specified collision-free framing of a known B. Unconditional arbitrary-body
support without preflight is rejected; changing to byte lengths or escaping would
need a revised proposal and review. Different-nonce examples do not need escaping.

## 4. Bytes, line endings and empty bodies

Input is valid UTF-8 bytes. Do not open with newline conversion, Unicode normalization,
replacement decoding or a YAML loader. An optional UTF-8 BOM at absolute document
offset zero is retained as outside bytes and ignored only for first-line recognition.
U+FEFF elsewhere is ordinary body/outside content and is invalid in header syntax;
it is never silently removed. Invalid UTF-8 anywhere yields ENCODING_INVALID before
structure is interpreted. No body text, control byte or quoted instruction executes.

A physical line ends at LF; if immediately preceded by CR, its EOL is CRLF, otherwise
LF. Bare CR is data, not a line separator. Syntax lines cannot contain bare CR.
Let E be the packet opening marker's LF or CRLF EOL. All header lines, the body-marker
line and the separator immediately before the end marker must use E. Different
packets may use different E. The ending marker's optional EOL must also be E; it
belongs to the packet frame. Body-internal LF, CRLF and bare CR remain untouched.
Other outside line endings remain untouched.

Define s as the first byte after body-marker EOL and c as the first byte of the
closing marker. Exactly one E immediately before c is a framing separator, not body
data. Require c >= s + len(E) and exact E there. The body is the half-open raw byte
slice [s, c - len(E)). No stripping occurs. Any preceding LF/CRLF inside that slice
belongs to B, even when identical to E. The body-marker EOL cannot double as the
separator: adjacent body/end lines without a blank line are malformed, not empty.
Match this separator as a suffix of exactly len(E) bytes. With LF framing, a bare
CR at the end of B remains body data even though CR plus the separator LF looks
like a physical CRLF; do not remove both bytes in that case.

This construction is explicit even for a body with no final newline:

| E | B in byte notation | bytes after body-marker EOL, before end-marker `<' |
|---|---|---|
| LF | empty | `\n` |
| LF | `x` | `x\n` |
| LF | `x\n` | `x\n\n` |
| LF | `x\n\n` | `x\n\n\n` |
| LF | `x\r\n` | `x\r\n\n` |
| CRLF | empty | `\r\n` |
| CRLF | `x` | `x\r\n` |
| CRLF | `x\n` | `x\n\r\n` |
| CRLF | `x\r\n` | `x\r\n\r\n` |

An explicitly empty B is valid. Missing body marker, missing separator, or missing
end marker is BOUNDARY_INVALID. Required task semantics and whether a later operation
permits an empty task are outside this parser.

Keep raw document bytes, packet/frame/header/body spans and ordered decoded fields.
Lossless re-emission means emitting original bytes/spans, not reconstructing from
decoded fields. Both the complete document and each packet must round-trip exactly,
including header spaces/quotes/order, all marker EOLs, BOM and outside notes. This
does not promise that editing a decoded field and serializing it preserves the old
packet. No mutation or canonicalizing serializer is required in Phase 0.

## 5. Flat header and string values

Every header line is `key: value` with a column-1 lowercase ASCII key matching
`[a-z][a-z0-9_]*`, immediately followed by colon and exactly one required ASCII space.
Additional ASCII spaces belong to the value's outer whitespace and are trimmed for
decoding only. No blank lines, comments, indentation, tabs, multiline values or
continuations. Header field order is free; raw order remains preserved. Unknown
keys and repeated keys are errors, including equal repeats. Capitals are not fixed.
For diagnostic tokenization only, recognize uppercase ASCII letters in a key too;
such a token is an unknown_key, not a repaired lowercase key.

| key | requirement | value shape |
|---|---|---|
| `format` | required | scalar, exactly `request/0.1` |
| `id` | required | nonempty scalar; exact decoded value unique across this document |
| `from`, `to` | required | nonempty scalar identity declarations |
| `program`, `function` | required | nonempty scalar binding names; resolution deferred |
| `requested_scope` | required | nonempty scalar; not an enforcement claim |
| `consult` | optional | flat list of string identities; absent means empty list |
| `in_reply_to` | optional | nonempty scalar reference; resolution deferred |
| `context` | optional | flat list of string references; absent means empty list |
| `expected_return`, `stop` | optional | nonempty scalar; no semantic evaluation |

No implicit fields and no hidden defaults beyond the two absent lists. `id` and
`in_reply_to` are opaque, case-sensitive strings, not paths to resolve or commands.
References may point outside this document; Phase 0 does not reject unresolved names,
missing files, cycles or future replies. Duplicate decoded ids are structural errors.
No `bus`, `type`, `hold`, `created`, `thread`, `rev` or extension keys are accepted
in version request/0.1. A future header extension requires its own reviewed version.

Scalars use either bare text or a JSON double-quoted string. Trim outer ASCII spaces
before deciding the form. Bare text is nonempty, contains no ASCII controls, `"`,
single quote, square/curly brackets, or U+FEFF, and does not start/end with a Unicode
curly quote U+2018/U+2019/U+201C/U+201D. Those curly characters inside bare text are
ordinary content. Colons, `#`, backticks, `&&`, backslashes, dates and numerals are
literal text; there are no YAML comments, booleans, dates, tags, aliases or escapes.
For example `no`, `2026-10-17` and `01234567` stay those exact strings. A scalar `#x`
is text. Bracket-led or single-quoted forms are not silently unwrapped.

Double-quoted form is one complete JSON string with standard JSON escapes, no
trailing nonspace data. Decode escapes; reject empty decoded strings, C0 controls,
DEL, unpaired surrogate escapes and U+FEFF in the result. A quoted string may contain
literal apostrophes, brackets, smart quotes, colons or commas. It may encode a
backslash with `\\`; `\n` is rejected because the decoded header value would contain
a control character. All successfully decoded scalar values remain strings. ASCII
tabs are forbidden anywhere in header source, even between tokens; `\t` also fails
after decoding. Trailing ASCII spaces are accepted and retained in raw bytes.

## 6. Flat lists

Only `consult` and `context` accept lists. Syntax is `[` followed by zero or more
string items separated by a comma, followed by `]`. ASCII spaces may surround items
and commas. Empty list `[]` is valid. No trailing commas, empty items, nesting, maps,
comments or multiline forms. A bare list item follows the bare scalar rule but
cannot contain a comma; quote any item needing a comma or a bracket. A quoted item
uses exactly the scalar JSON-string rule, so `context: ["a,b", "path with spaces"]`
has two string items. Quote-aware tokenization, not splitting every comma, is needed.

Retain list order and repeated elements as supplied; deduplication or collaborator
identity comparison belongs to a later binding layer. A scalar in a list field or a
list in a scalar field is FIELD_INVALID. `consult: [Astrobley]` from the original
example remains accepted. No string/list element undergoes numeric/date conversion.

## 7. Whole-document errors and deterministic diagnostics

The parsing result is either a valid document with all packets in source order or
an invalid result with diagnostics and no successful packet extraction for downstream
use. A valid prefix cannot license work when a later packet fails. Outside notes and
complete original input can still be retained for human diagnosis.

Proposed check result: success exits 0; input data errors exit 65, reusing the bus
catalogue's data-error class (`raw/01_SYNC_METHOD.md:78–91`). File-open/I/O failures
remain operational failures (propose 74), never invalid or successful empty input.
This does not settle the eventual CLI surface or transport catalogue.

Each data diagnostic contains exactly `code`, `reason`, `byte_offset`, `line`,
`byte_column`, `packet_nonce` (string or null), and `field` (header key or null).
Unknown keys populate field with their literal key; missing fields name the absent
key; other field errors name the affected key; non-field errors use null.
Offsets are zero-based absolute
byte offsets; lines/byte columns are one-based, LF increments line. BOM bytes count
toward offsets/columns. EOF points at offset len(input), including after a final LF.
No absolute path, clock, randomness, locale, object repr or raw body text enters a
data diagnostic. Fixed reason identifiers below avoid unstable prose.

| code | fixed reasons |
|---|---|
| ENCODING_INVALID | `invalid_utf8` |
| BOUNDARY_INVALID | `marker_syntax`, `marker_order`, `nonce_reused`, `missing_body`, `missing_end`, `missing_separator`, `frame_eol`, `no_packets` |
| HEADER_INVALID | `header_line`, `header_syntax`, `unsupported_format` |
| FIELD_MISSING | `required_absent`, `empty_value` |
| FIELD_INVALID | `unknown_key`, `duplicate_key`, `wrong_shape`, `invalid_string`, `invalid_list`, `duplicate_id` |

Use ENCODING_INVALID alone at the first undecodable byte if UTF-8 fails. Otherwise
walk framing in source order; collect header errors in each safely completed header
and continue through sound frames. At the first framing failure emit that structural
error and stop framing: do not seek a new packet inside a possibly truncated body.
Retain earlier independent header findings. No hypothetical errors from unframed
suffixes are reported. This conservative limit is the explicit A7 adaptation.

Within a header line: header shape first; then known/unique key; then value shape;
then scalar/list decoding. Emit the first failing class for that line. Seen-key
tracking includes recognized keys with bad values, so another occurrence is still
duplicate_key. At header closure, required_absent only for keys never seen; empty
or invalid seen values already have their own error. Missing required fields use
the table order in section 5. Format validation happens only after successful string
decoding. Duplicate ids are checked only for successfully decoded ids, on the later
packet; comparison uses exact strings, without case or Unicode normalization.
Blank, comment, indented or tab-containing header lines use header_line; other
failures of the key/colon-space line form use header_syntax. A scalar field whose
trimmed value starts `[` or `{`, or a list field not starting `[`, uses wrong_shape.
Bad scalar quoting/characters/escapes use invalid_string; bad list tokenization or
items use invalid_list. An empty scalar, bare or decoded, uses empty_value; an empty
list item uses invalid_list. A header line with the wrong or missing frame EOL is
frame_eol before any header-value finding from that line.

Anchor line errors at their first byte; duplicate ids/keys at the later header-line
start; absent fields at body-marker start; missing body/end at EOF; missing separator
at end-marker start; orphan/reused/order/syntax/EOL markers at offending marker-line
start. `no_packets` uses offset zero. Final order is ascending byte_offset, then
code ASCII order, then the section-5 required-key order for equal required_absent
records; other equal records use reason ASCII order and retain source encounter
order for exact ties. Set field only after a syntactically valid header key has
been identified. Records are not deduplicated.

When one marker could have several failures, precedence is malformed syntax, reused
nonce, marker order, frame EOL, separator. A well-formed wrong-nonce marker inside a
header is marker_order; inside a body it is data. For EOF in a header report
missing_body; for EOF in a body report missing_end. These rules make every negative's
expected code, position and ordering stateable before implementation.
Nonce reuse applies in outside state; different-nonce header markers still use
marker_order. An opening/body marker without its required EOL uses frame_eol;
missing_body/missing_end apply when no such malformed syntax line precedes EOF.

## 8. Acceptance plan for a later implementation POINT

This is a specification and future evidence plan, not executed parser tests. The
implementation POINT must name the approved source home, callable parse/check and
lossless byte-output interfaces, fixture/output paths and exact runner commands.
Do not invent an installed executable now. Verification must retain command lines,
exit statuses, diagnostic bytes, fixture digests and direct byte comparisons; digest
agreement supplements, rather than replaces, comparison.

Build fixtures only in the later authorized test/output scope. Read these pinned
sources as bytes, without running their text:

| fixture body B | exact source extent |
|---|---|
| counsel exchange | `raw/EXCHANGE.md`, whole file, lines 1–159 |
| Sella exchange | `raw/sella-v.0.1/EXCHANGE.md`, whole file, lines 1–130 |
| Oraculum brief | `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md`, whole file, lines 1–88 |
| operational bed | `raw/journal.2026-10-16.md`, bytes from line 39 `## 1.4. OPERATIONAL BED` through line 407 inclusive; stop before line 408 `# 2. JEV` |

For every B choose a distinct nonce proven absent from its three exact marker forms.
Wrap it with a valid header and the mandatory extra separator. Compare extracted body
to B using `cmp -- <original-body-file> <extracted-body-file>` (exit 0); compare
losslessly re-emitted packet/document to its fixture with `cmp --` (exit 0). For the
journal slice compare against the separately byte-sliced fixture, never a copied
Markdown quotation. Record source slice offsets and SHA-256. Repeat all four bodies
with LF and CRLF frames, keeping each B unchanged (8 corpus fixtures), then combine
them into one mixed-frame document with outside notes and a starting BOM. Require
exact packet order/count, all four body comparisons, and whole-document comparison.

Additional positive checks:

- Each section-4 byte-table case, plus B ending in bare CR, leading LF/CRLF, multiple
  blank lines, tabs, smart quotes, BOM bytes, non-ASCII code points and valid UTF-8
  control bytes. Cover final closing marker with EOL and at EOF without EOL.
- Different-nonce complete packet examples inside B, active marker text inline or
  indented/quoted, marker-like text with trailing spaces, `---`, apparent headers,
  relay wrappers, `&&`, backticks and fences. Require exact byte preservation and
  exactly one outer packet, not extracted nested packets.
- Same-nonce active marker lines inside fences must follow section 3: packet/body
  yields marker_order; an extra end plus the real end yields nonce_reused at the
  later end. Record the single-end ambiguous case as a valid frame whose
  intended body cannot be inferred; demonstrate preflight refusing that chosen nonce.
- Headers with unquoted `no`, `2026-10-17`, `01234567`, all-digit ids and double-quoted
  equivalents must yield strings. Cover colon/hash/backslash data, accepted trailing
  spaces, arbitrary field order, absent/empty lists, quoted list commas, literal
  apostrophes in quoted strings and repeated list elements in their original order.

Negative checks must assert exit 65, exact code/reason/position and no usable partial
packet result, with every diagnostic byte identical on two runs:

| family | cases and expected principal result |
|---|---|
| encoding | Invalid UTF-8 at document start/header/body/outside → ENCODING_INVALID only, first bad byte. |
| marker spelling | Truncated markers, malformed nonce, indented/trailing-space outside markers, capitalized verb → BOUNDARY_INVALID/marker_syntax. Uppercase `COMPOSER` is ordinary outside text; by itself gives no_packets. |
| ordering | Orphan body/end, nested packet in header, active packet/body in body, reused top-level nonce, wrong nonce in header → BOUNDARY_INVALID/marker_order or nonce_reused. A body marker before any fields closes an empty header and produces required_absent findings; it is not itself an ordering fault. |
| truncation | EOF after opening/header → missing_body; EOF after body marker/body → missing_end; adjacent body/end with no separator → missing_separator. |
| EOL | Mixed LF/CRLF frame/header lines or incorrect closing EOL/separator → frame_eol (separator mismatch alone → missing_separator); unchanged mixed body EOLs are positive cases. |
| fields | Missing required fields/empty scalar → FIELD_MISSING; unsupported version → HEADER_INVALID/unsupported_format; uppercase/unknown keys and repeated keys → FIELD_INVALID. |
| scalar syntax | Header tabs, indented/blank/comment lines, absent colon-space → HEADER_INVALID; single quotes, curly-quote delimiters, bracket/map scalar, bad JSON escape, escaped controls/surrogates/BOM → FIELD_INVALID. |
| lists | Scalar for list, list for scalar, nested list/map, trailing comma, empty item, unclosed quote/bracket → FIELD_INVALID. |
| document | Empty/only-outside input → no_packets; duplicate decoded ids → duplicate_id at second id; valid first packet followed by corrupt second → invalid whole result. |

Freeze a diagnostic oracle from section 7 before writing implementation assertions;
where a fixture triggers several errors, assert the defined precedence and retained
independent findings, not a generic nonzero status. Exercise an unknown key plus a
missing field in each of two sound packets, then a corrupt third frame: all safely
known header findings and the first framing error must be returned in defined order.

Non-execution witness: in fixture bodies, quotes and outside notes include literal
shell substitutions, backticks, `&&`, apparent CLI invocations, and named sentinel
file write instructions. Construct fixture bytes without shell interpolation; run
only the approved parser/checker. Compare sentinel absence and before/after byte
identities of input fixtures and protected reference files; capture child-process
observations if the runner offers them. Expected: no child command or sentinel write,
inputs unchanged, no exchange/raw/STATUS mutation. A lack of a sentinel alone is not
a complete proof of no execution: independently inspect the parse/output call path
for shell/eval/exec, interpolation and implicit opening of header/body references.
The parser's permitted output is confined to later-authorized test outputs and
diagnostics, which must never echo raw control bytes from the body to a terminal.

## 9. Four questions and review decisions

Using `raw/05_WAY_OF_THINKING.md:7–21`:

1. Conventional name: a line-framed multipart document with a flat string header and
   lossless byte spans. This names the pattern; it does not claim MIME compatibility.
2. Already addressed by the supplied prior-art pass: delimiter collision, implicit
   YAML typing and round-trip loss (`research:23–25,37–44`). Borrow explicit boundaries,
   string-only decoding, collision preflight and preserved original bytes. Reject
   bare `---`, implicit YAML coercion and reconstructive reserialization.
3. Open in this case: hand-editing can introduce an active marker or unsaved state;
   byte syntax cannot know intended prose or authority. Specify visible failure and
   preflight limits. Reject nonce probability as proof and Markdown-fence heuristics.
4. Specific choices here: Q3 exchange ownership, proposed marker/header vocabulary,
   required separator ownership and the small Phase 0 validation boundary. Propose
   these for Majkee's decision; leave registries, dispatch, policy and rendering out.

Review must accept, amend or reject the concrete framing, preflight limitation,
string/list/header vocabulary, empty/control-containing body policy, Q3, and the
diagnostic aggregation boundary together. Exact source subpath, stack and verifier
still need their implementation decision. Neither this proposal nor a successful
future parse resolves a binding, grants authority, proves reading, delivers a prompt
or closes the Phase 0 gate.
