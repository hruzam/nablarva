---
kind: grammar-proposal
version: 3
date: 2026-10-19
author: builder · new native Astrobley
cycle: '12'
status: complete review candidate; Majkee's GO on this written v3 remains pending
direction: Majkee's carried 2026-10-19 delimiter revision
scope: composer Phase 0 only; no implementation or deployment authority
---

# Composer Phase 0 — proposed delimiter-body contract

The delimiter direction was selected by Majkee in the carried 2026-10-19 decision;
the actual written v3 still requires native changed-section review and explicit GO.
This is a complete candidate, not an addendum to v2. `request/0.1` is the proposed
initial wire version; no prior deployed grammar is implied. Publication passes to
or through ia-sync under flag L8′. Exact source `/home/hruzam/ia-sync/zsh/composer/`,
Python stdlib and a fresh native Codex verifier remain proposals, subject to Majkee's
separate decisions. This document creates no parser, tests, helper or installed CLI.

## 1. Sources and scope adaptations

Relative source paths use the bed
`/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/`.

| source anchor | constraint or adaptation |
|---|---|
| `evidence/challenge.janus.2026-10-19.md`, verbatim carried decision | Controlling revision: first exact same-nonce end line, 4–8 lowercase alphanumeric nonce, body-final EOL retained, empty body allowed; unrepresentable nonempty body without final LF accepted. Written v3 still needs GO. |
| `brief.nabla.composer-build.2026-10-17.md` §3–4 | Grammar before code; four unchanged corpus bodies, diagnostics, non-execution, scoped pen and four questions. |
| `raw/sella-v.0.1/brief.astrobley.sella-v.0.1.md` §One readable source | Small string header, `request/0.1`, declared id/from, flat consult list and uninterpreted task text. |
| `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md:12–25` | Readable exchange; declared structure only; separate later procedure/role bindings. |
| `raw/02_PARSER_GATE.md` §Message file, §Zones | Flat header and distinct header/body/outside zones; nonce `[a-z0-9]{4,8}`. Composer adds explicit packet/header/body markers for a multi-packet exchange. |
| `raw/02_PARSER_GATE.md:44–52,93–105` | Bus sender derivation, generated ids, freshness, registry and gates remain outside composer Phase 0. Future delivery derives sender and compares it with declared from. |
| `research.nabla.composer-prior-art.2026-10-17.md` A1–A5, A7, B2–B3, Q3 | Human owns exchange, string values, preserved bytes, typography/marker cases; aggregation stops when structure becomes uncertain. |
| `raw/journal.2026-10-16.md:39–407` | Historic operational-bed packets are corpus data, not current authority or doing-state. |

The source adaptations remain explicit:

- `02` §Zones makes payload text data except its active nonce boundary. V3 reserves
  the first exact active end line, including inside Markdown fences. Same-nonce
  packet/body lines and different-nonce end lines within B are data. There is no
  claim that a later edit cannot introduce a closer.
- Composer declares `id`/`from` and `format: request/0.1`; the bus derives sender,
  generates ids and uses `bus: 1`. Phase 0 authenticates none of these strings.
  VIST supplies occupant evidence, not identity; neither VIST nor this future
  delivery note authorizes identity, relay or delivery implementation here.
- Bus payload emptiness/control restrictions serve transport. This inert parser
  accepts empty and control-containing valid UTF-8 bodies, with no raw body control
  bytes in terminal diagnostics. A future transport needs its own safety checks.
- Bus fail-fast and research A7 differ: collect independently knowable header
  findings, continue through sound delimiter frames, stop at first structural
  failure. Never recover by searching past a recognized but invalid closer.

Raw sources and v2 remain unchanged historical artifacts. No choice in this
candidate locks canon, grants a write path or closes the Phase 0 gate.

## 2. Document, Q3 and ownership

Propose one human-owned Markdown exchange containing several packets in source
order. Outside text may precede, separate and follow packets and is preserved.
Read only saved bytes; never write the exchange or claim an unsaved editor buffer
was parsed. Informal `to-...`, `from-...`, `&&`, `---`, fences and headings open
no packets and confer no authority.

Q3 proposal remains composition in that exchange, without a second per-prompt drafts
tree. Later Phase 2 may freeze selected packets to `prompts/<id>/<rev>.md`; Phase 0
creates none. Frozen EXCHANGE files are unchanged test bodies, not files to migrate.
Q4 gives `&&` no Phase 0 action; Q1/Q2 render policy and Q5 rotation remain open.
Do not open references, resolve bindings or execute header, body or outside text.

Agent-made marker drafts and a future stdout-only skeleton brick are permitted
forms of preparation, never exchange-writing authority. This grammar-only body
implements neither a skeleton nor a writer. STATUS remains the head's sole position.

## 3. Frame and exact byte ownership

Markers have exactly these ASCII spellings at column 1, with the shown spaces:

```text
<!-- composer:packet N -->
<!-- composer:body N -->
<!-- composer:end N -->
```

N is 4–8 characters matching `[a-z0-9]{4,8}`. It correlates syntax, not identity or
content integrity. Each structural packet opening uses a nonce not previously used
by another structural packet in that whole document. Once opened, that nonce stays
used through EOF; do not reset it between packets, notes or Markdown sections.
Marker-looking data inside B does not register a structural nonce.

State sequence is outside → header(N) → body(N) → outside. Outside accepts packet
openings. An exact body/end marker outside is orphaned (`marker_order`), except
that any exact marker there with an already used nonce fails `nonce_reused` first.
In header(N), only the exact body marker with N advances state; other exact markers
are `marker_order`. No nested packet opens in a header.

Physical lines end at LF. Immediately preceding CR makes that EOL CRLF; bare CR
is not a line separator. Let E be the opening marker's LF or CRLF. Opening, header
and body-marker syntax lines must end with E. A recognized end line may terminate
at EOF without EOL; otherwise its EOL must equal E. Packets may choose different E.
Outside/body EOL bytes remain unchanged, including mixed LF/CRLF and bare CR data.

After the body-marker EOL, let s be the next byte offset. Inspect successive
physical lines solely to recognize the first column-1 line whose entire content
is exactly `<!-- composer:end N -->`. Here content excludes its LF or CRLF EOL;
an EOF-terminated line has no EOL to exclude. Let t be that line's start. B is
exactly [s,t). The recognized line ends B before its own EOL is validated. If that
EOL is the wrong kind for E, fail `frame_eol` there and stop; never choose a later
correctly terminated end line instead. At EOF, an exact complete end line is valid.

All other lines in body(N) are data: same-nonce packet/body markers, different-nonce
end markers, indented/inline/quoted ends, trailing spaces, bad nonce spellings,
partial end tokens, headers, commands and Markdown fences. Do not apply the
outside/header marker-syntax check inside B. In particular, a malformed end-like
line is not a structural closer or an immediate error; it remains B. If no exact
closer ever follows, fail `missing_end` at EOF. A token followed by bare CR at EOF
is not an exact line (the CR is content); it also remains data. These rules separate
recognition from EOL validation without guessing intended delimiters.

The opening/body-marker EOLs and all marker bytes are framing. The end marker's
own EOL, when present, is framing. B includes every byte before the end line,
including its own final LF or CRLF. There is no extra separator and no newline
stripping. Empty B means the end marker starts immediately after the body-marker
EOL. Nonempty B necessarily ends in LF; a nonempty intended body without final LF
cannot be represented. Do not add a newline and claim byte identity. A body ending
in bare CR alone is likewise unrepresentable; a bare CR elsewhere stays data.

| frame E | intended B in byte notation | bytes after body-marker EOL before end line | result |
|---|---|---|---|
| LF | empty | empty | valid empty B |
| LF | `x\n` | `x\n` | valid; final LF belongs to B |
| LF | `x\n\n` | `x\n\n` | valid; both final LFs belong to B |
| LF | `x\r\n` | `x\r\n` | valid; body CRLF is unchanged |
| LF | `x\r` or `x` | no representation | accepted limitation |
| CRLF | empty | empty | valid empty B |
| CRLF | `x\n` | `x\n` | valid; body need not use frame E |
| CRLF | `x\r\n` | `x\r\n` | valid; no extra CRLF |
| CRLF | `x\n\r\n` | `x\n\r\n` | valid; mixed body EOLs retained |
| either | `x\ry\n` | `x\ry\n` | valid; internal bare CR retained |

Whole-document validity requires at least one complete packet. Any later error
invalidates the entire document: no valid-prefix extraction or downstream packet
result. After a sound closer, resume outside at the following physical line.

Outside/header lines beginning `<!-- composer:` after removing leading ASCII
spaces/tabs, but failing the marker grammar, are `marker_syntax`. Indentation,
trailing spaces, capitalized verbs, invalid nonces or truncated tokens never form
delimiters. Uppercase `COMPOSER` and inline markers are ordinary outside prose.
Markdown fences shield nothing in outside/header states. An exact marker with an
LF/CRLF EOL is recognized before checking whether that EOL matches E.

## 4. Encoding and lossless representation

Validate the complete input as UTF-8 before structure; reject invalid sequences
without replacement decoding. Preserve an optional initial UTF-8 BOM at absolute
offset zero as outside bytes, ignoring it only for first-line recognition. U+FEFF
elsewhere is body/outside data; it is invalid in a header. An initial body BOM
is never stripped and does not exempt that line from exact column-1 matching.

No text-mode newline conversion, Unicode normalization or decode/re-encode round
trip may change source bytes. Delimiters lie on physical-line boundaries; B's
endpoints therefore cannot split a valid UTF-8 character. `é∇\n` is preserved as
its UTF-8 bytes, regardless of display width or character count.

Retain original document bytes, ordered packet/header/frame/body spans and decoded
header fields. All header values remain strings or flat string lists. Lossless
re-emission copies original spans rather than serializing decoded fields anew.
Packets and whole documents must round-trip byte-identically, including raw quotes,
spacing, field order, BOM, outside notes and framing EOLs. Editing decoded values
and generating new documents is outside this Phase 0 contract.

No fixed body-size cap is selected in this candidate. If wanted, one fixed limit
and its diagnostic must be separately decided; never add a size header. No helper
or limit implementation follows. Memory/I/O exhaustion is operational failure,
never an empty valid document or a successful shortened body.

## 5. Flat header and string scalars

Header lines are column-1 `key: value`, key `[a-z][a-z0-9_]*`, colon and one required
ASCII space. Additional ASCII spaces around a value are trimmed only for decoding
and retained in raw bytes. No tabs, blank lines, comments, indentation, continuations,
nesting or multiline values. Order is free. Unknown keys and repeated known keys
are errors even if repeated values agree. Diagnostic tokenization also recognizes
uppercase ASCII key letters; uppercase keys are `unknown_key`, never corrected.

| key | required | decoded value |
|---|---|---|
| `format` | yes | scalar exactly `request/0.1` |
| `id` | yes | nonempty scalar, unique by exact decoded value across document |
| `from`, `to` | yes | nonempty scalar declarations; no authentication |
| `program`, `function` | yes | nonempty scalar names; resolution deferred |
| `requested_scope` | yes | nonempty scalar; no enforcement claim |
| `consult` | no | flat string list; absent means empty list |
| `in_reply_to` | no | nonempty scalar; resolution deferred |
| `context` | no | flat string list; absent means empty list |
| `expected_return`, `stop` | no | nonempty scalar; no semantic evaluation |

Absent-required-field order expands combined rows left to right: format, id, from,
to, program, function, requested_scope. No other implicit defaults. No body-size,
bus/type/hold/created/thread/rev or extension keys. A legacy body_bytes line is an
unknown key; it never changes B. Names/references are opaque case-sensitive strings:
no path opening, registry query, reply-lineage resolution or permission evaluation.
Only decoded id uniqueness is structural.

Scalar source is bare text or one complete JSON double-quoted string. Bare values
are nonempty and exclude C0/DEL controls, ASCII double/single quotes, square/curly
brackets and U+FEFF. U+2018/U+2019/U+201C/U+201D are prohibited only as the first/last
bare-value character to catch accidental smart quote delimiters; internally they
are data. Colons, hashes, backticks, `&&`, dates, digits and backslashes are literal;
no YAML comments, aliases or coercions. `no`, `2026-10-17`, `01234567` remain strings.

JSON-string form uses standard JSON escapes with no trailing nonspace text. Reject
empty decoded strings, C0/DEL, unpaired surrogate escapes and U+FEFF. Quoted strings
may contain apostrophes, brackets, commas and smart quotes. Escaped newline/tab is
invalid after decoding. Tabs in header source are always invalid, even in a quoted
string. Trailing ASCII spaces are accepted and preserved in the raw header.

## 6. Flat lists

Only consult/context use lists: `[` zero or more string items separated by commas
`]`, with ASCII spaces around tokens. `[]` is valid. No empty items, trailing comma,
nesting, maps, comments, tabs or multiline forms. A bare item follows scalar rules
but cannot contain a comma. JSON-quote items needing commas/brackets, e.g.
`context: ["a,b", "path with spaces"]`. Respect quotes and escapes during tokenization;
do not blindly split commas. Empty decoded items are invalid. `consult: [Astrobley]`
remains accepted. Preserve order and repeated elements; resolution/deduplication is
not parsing. Scalar in list field or list in scalar field is `wrong_shape`. Do not
convert list items into dates/numbers.

## 7. Complete examples and editing limits

Valid LF document; B is `alpha\nomega\n`, with no extra separator:

```text
<!-- composer:packet a7b2 -->
format: request/0.1
id: example
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
<!-- composer:body a7b2 -->
alpha
omega
<!-- composer:end a7b2 -->
```

Valid empty body in a separate document:

```text
<!-- composer:packet empty8 -->
format: request/0.1
id: empty-example
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
<!-- composer:body empty8 -->
<!-- composer:end empty8 -->
```

Required negative insertion witness: insert one same-nonce end line into the first
example's intended body while retaining the original end. This entire document is
invalid:

```text
<!-- composer:packet a7b2 -->
format: request/0.1
id: example
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
<!-- composer:body a7b2 -->
alpha
<!-- composer:end a7b2 -->
omega
<!-- composer:end a7b2 -->
```

The first end closes B as `alpha\n`. `omega\n` is outside text. The retained true
end is then an exact outside marker with a used nonce: `BOUNDARY_INVALID/nonce_reused`
at that second end's line start, field null, nonce `a7b2`. Reject the whole document,
including that shorter packet; never scan past the first closer to repair B.

If that true end is absent, the syntax can instead be valid with a shorter B and
outside prose. Framing cannot discover the author's unrecorded intent. A random or
agent-suggested nonce is no proof against later collision, authenticity or mutation.
To include an exact end-looking line as body data, choose an active nonce different
from that line before use; no escaping or automatic nonce repair is defined. Bodies
with no final LF remain unrepresentable. Ordinary prose edits need no size metadata.

`evidence/fixtures/packet.handwritten.v3.md` is one literal, directly text-authored
packet fixture by this Astrobley, with authorship recorded in outside notes. It is
not claimed as human-authored and its body has not been measured. No fixture
generator or executable fixture code is supplied.

## 8. Deterministic diagnostics and aggregation boundary

Check success exits 0; input data errors exit 65 (`raw/01_SYNC_METHOD.md:78–91`).
Operational file/I/O/resource failure proposes exit 74 and is never success. No
installed CLI or parse/byte-output interface is chosen. Invalid input returns
diagnostics and no usable packet result, even after a sound prefix. Retaining raw
input for human diagnosis is permitted; acting on prefix packets is not.

Each diagnostic has exactly code, reason, byte_offset, line, byte_column,
packet_nonce (string or null), field (header key or null). Offsets are zero-based
absolute; line/byte_column one-based, with each LF starting a new line. BOM bytes
count toward offsets/columns. EOF is len(input), following final LF at next line
column 1. Never emit raw body text, time, randomness, paths or locale-dependent prose.

| code | reasons |
|---|---|
| ENCODING_INVALID | invalid_utf8 |
| BOUNDARY_INVALID | marker_syntax, marker_order, nonce_reused, missing_body, missing_end, frame_eol, no_packets |
| HEADER_INVALID | header_line, header_syntax, unsupported_format |
| FIELD_MISSING | required_absent, empty_value |
| FIELD_INVALID | unknown_key, duplicate_key, wrong_shape, invalid_string, invalid_list, duplicate_id |

This is the complete reason set. Count/byte-endpoint/separator errors are removed.
The former exact-position end_mismatch/end_truncated reasons also have no v3 role:
nonmatching/partial body lines are data, and exhaustion without a closer is
`missing_end`. A recognized closer with wrong LF/CRLF uses `frame_eol`. No size-limit
code is added without selection of a fixed limit.

Textual diagnostics are one JSON object per LF-terminated line, keys in the order
above, no spaces around separators, integer decimal offsets, literal JSON null,
no summary or interleaved output. Empty sequence emits no diagnostic bytes.

Deterministic processing and stopping rules:

1. Validate whole-input UTF-8 first. Failure yields only `invalid_utf8` at the first
   invalid-sequence start, null nonce/field; parse no structure.
2. Walk outside/header lines in source order. For marker-like lines there, precedence
   is malformed spelling, reused nonce (outside only), marker order, required EOL.
   Stop at the first such structural failure, retaining prior independent header
   findings. A wrong-nonce marker in a header is `marker_order`. Header EOF without
   its body marker yields `missing_body`; no search forward or resynchronization.
3. Header ordinary lines first require E (otherwise `frame_eol`, stop). Then check
   line shape, known/unique key, value shape, string/list decoding, supported format,
   and decoded id uniqueness. Emit only the first failure per line. A recognized key
   with invalid value still counts as seen; later occurrence is `duplicate_key`.
   Unknown-key repetitions stay `unknown_key`. A successfully decoded id registers
   for document uniqueness even if another field in its packet is invalid.
4. At a structurally sound matching body marker, emit `required_absent` for never-seen
   required keys in §5 order. Invalid/empty seen keys already have findings. Collect
   all independent header findings and continue delimiter recognition even when
   header values are invalid; these values cannot change the delimiter nonce.
5. In body(N), ignore every line except the first exact column-1 end line with N
   under §3. EOF without one yields `missing_end` at EOF, active N, null field;
   no guessed later packets/header findings. Once recognized, validate its EOL
   immediately. LF versus CRLF mismatch is `frame_eol` at the first differing EOL
   byte. EOF without any EOL is valid. Never skip a recognized wrong-EOL closer.
6. After a sound closer, resume outside, retaining all known ids/nonces. Thus the
   insertion witness's second end fails `nonce_reused`. At otherwise clean EOF with
   no opened packet, report `no_packets` at offset zero. Do not add it after a more
   specific opening/header/structural error. Any finding invalidates the document.

For outside/header syntax lines, an exact marker token at EOF is still recognized
for precedence. An opening or body marker there then lacks its required E and gives
`frame_eol` at EOF. A bare-CR suffix fails marker spelling there (`marker_syntax`);
in body it remains data as §3 specifies. For ordinary header lines, bare CR is an
invalid EOL: `frame_eol` at that CR. LF/CRLF mismatch anchors at its first differing
byte; missing required EOL anchors at EOF. These rules do not require uniform body EOL.

Blank/comment/indented/tab-containing ordinary header lines use `header_line`; other
key/colon-space violations use `header_syntax`. After a known unique key, scalar
value beginning `[`/`{`, or list value not beginning `[`, uses `wrong_shape`. Bad
scalar syntax uses `invalid_string`; bad list syntax/items uses `invalid_list`.
Empty bare/decoded scalar uses `empty_value`; empty list item uses `invalid_list`.
Unsupported decoded format uses `unsupported_format`. Duplicate id checks use exact
successfully decoded strings, without case folding/normalization.

Header findings anchor at line start, absent keys at body-marker start, malformed/
order/reused markers at their line start. `missing_body`/`missing_end` anchor at EOF.
Fields are populated only after key tokenization; structural/encoding errors use
null field. Marker errors in header/body use active N. Outside exact markers use
their parsed nonce; malformed outside markers use null. `no_packets` and initial
UTF-8 errors use null nonce; outside frame errors on openings use the opening N.

Sort final diagnostics by byte_offset ascending, then code ASCII, reason ASCII,
field ASCII with null first; exact ties retain encounter order, no deduplication.
Absent fields therefore encounter §5 order but final output follows this total
sort. Aggregate only independently knowable findings before the structural stop;
claim none for an unframed suffix. This is the explicit research A7 boundary.

## 9. Future acceptance evidence

This is an evidence plan, not implemented or executed parser tests. A later POINT
must supply approved code home, callable check/parse/lossless-output interfaces,
fixture/output scope and exact commands. Retain actual commands, exit outcomes,
diagnostic bytes, source identities and direct `cmp -- <expected> <actual>` results
(expected 0). Hashes supplement exact comparison. No functional pass is claimed here.

Use all four brief §3 bodies unchanged:

| B | frozen source extent |
|---|---|
| counsel exchange | `raw/EXCHANGE.md`, whole file, lines 1–159 |
| Sella exchange | `raw/sella-v.0.1/EXCHANGE.md`, whole file, lines 1–130 |
| Oraculum brief | `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md`, whole file, lines 1–88 |
| operational bed | `raw/journal.2026-10-16.md:39–407` inclusive, byte slice [2061,16595), ending before line 408 `# 2. JEV` |

The existing `evidence/corpus-inventory.cartan.json` supplies observed source/slice
identities and EOL facts only; it is not framing metadata or grammar proof. Recheck
frozen identities and extents before use, including final LF representability.
Choose distinct valid active nonces absent as exact end lines in each unchanged B;
do not edit B to avoid collision. Wrap each with LF and CRLF framing (eight cases)
without altering body EOL bytes, and combine four into a mixed-frame document with
outside notes/initial BOM. Check packet order/count, body/packet byte comparisons
and whole-document round-trip. Collision checks during future fixture preparation
do not guarantee that a later human edit remains collision-free.

Also use the directly authored, unmeasured fixture
`evidence/fixtures/packet.handwritten.v3.md` as saved. Require successful parsing,
body byte identity, full-document round-trip and preservation of its outside
authorship note. Future byte comparisons need no declared size in that fixture;
its authorship does not claim independent functional evidence.

Additional positive cases:

- Every representable §3 table row, empty body, multiple final blank lines, body
  BOM, mixed LF/CRLF, internal bare CR, Unicode, tabs and valid UTF-8 controls.
  End marker with E and directly at EOF. Distinct packets with 4- and 8-character
  nonces containing letters beyond hexadecimal and digits.
- Same-nonce packet/body lines in B, different-nonce ends, malformed/partial end
  lines followed by a valid closer, trailing-space, indented and inline ends,
  fences, quoted tags, relay brackets, `---`, backticks, `&&` and header-looking text.
  Only the active exact end line is structural even inside a fence.
- Both valid §7 examples, Unicode `é∇\n`, absent/empty lists, quoted commas/brackets,
  repeated list elements, raw/quoted `no`, dates, digit-only ids, reordered fields,
  preserved header trailing spaces and outside notes.
- Body edits of any length remain valid when they retain representability and add
  no structural collision. This shows framing is not an integrity/authorship check.

Negative cases assert exit 65, no usable prefix and repeatable exact diagnostics:

| family | cases and predicted reason |
|---|---|
| insertion witness | Literal §7 negative: first closer ends B, retained true end outside gives `nonce_reused` at its start. No fallback to true end. |
| missing closer | EOF after body marker or body data, wrong-nonce end only, partial/malformed end only, bare-CR-suffixed end at EOF: `missing_end` at EOF. Do not reinterpret apparent later packet/header data. |
| exact closer wrong EOL | LF closer in CRLF frame or CRLF closer in LF frame: `frame_eol` at its first differing EOL byte, even when a later closer has correct E. |
| unavailable final LF | Concatenate nonempty `x` with an end token without intervening LF: no exact column-1 end, hence `missing_end` at EOF. Never normalize into a valid body. |
| outside/header markers | Invalid nonce length/alphabet, indentation/trailing spaces, malformed token: `marker_syntax`; exact orphan/wrong-order marker: `marker_order`; any exact outside marker with previously used nonce: `nonce_reused` first. |
| missing body/header EOL | Header EOF: `missing_body`; opening/body token at EOF when expected in state: `frame_eol`; mismatched syntax EOL: `frame_eol`. Orphan/reused/order checks retain their stated precedence. |
| header | Required keys absent/empty, unknown/capitalized/duplicate keys, legacy body_bytes, unsupported format, indentation/tabs/comments, bad strings/escapes/lists/nesting: corresponding §8 finding. |
| encoding | Invalid UTF-8 anywhere: only `invalid_utf8`, no structural diagnostics. Header BOM/smart-quote delimiter cases fail their defined string/header rules; body BOM stays data. |
| document | Outside-only input: `no_packets`; duplicate decoded ids: `duplicate_id`; reused opening nonce: `nonce_reused`; sound prefix plus later error invalidates all packets. |

Freeze expected multi-error sequences from §8 before writing assertions. Include
two sound frames with independent header errors followed by a third body missing
its end; retain preceding findings plus `missing_end`, with no speculative suffix
header diagnostics. Include a wrong-EOL first closer followed by a good closer to
prove the first structural error stops recognition. Include an early exact closer
with no retained true end as a parse-valid limitation, not a fabricated failure.

Non-execution: put literal shell substitutions/backticks, `&&`, executable-looking
tags and sentinel write instructions in body, quoted content and outside. Construct
fixture bytes without shell interpolation. Run only the approved parser; record
sentinel absence, input/reference before/after identities and child-process evidence
where available. Independently inspect its call path for shell/eval/exec, reference
opening and dispatch; sentinel absence alone proves too little. Expected: no child
execution or exchange/raw/STATUS mutation; no command interpretation; outputs only
in the future authorized scope, diagnostics with no raw body control bytes. Boundary
recognition alone does not execute or interpret task prose.

## 10. Four questions and decisions for review

Using `raw/05_WAY_OF_THINKING.md:7–21`:

1. Conventional pattern: a delimiter-framed readable multipart document with flat
   string metadata and lossless source spans.
2. Supplied prior art already names delimiter collision, YAML coercion and lossy
   round-trips. Borrow exact nonce lines, string-only decoding and raw spans.
   The carried decision chooses delimiter scanning over counted framing; no new
   external research or platform qualification is claimed by this grammar revision.
3. Open edge: later edits can introduce an active end line. The retained-end witness
   rejects as nonce reuse, but absent structural evidence of intent cannot be detected.
   Nonempty no-final-LF bodies cannot be represented. These limits replace a manual
   byte-count burden; no repair helper, writer or authenticity promise is proposed.
4. Our choices: composer header vocabulary, exchange composition/Q3, syntax-EOL
   checks and deterministic diagnostic aggregation. Procedure registry, policy,
   rendering, delivery and project state stay in their separate owners/later phases.

Direction is selected; written-contract approval is pending. Review this complete
v3's consistent delimiter, header/list, empty/control-body, Q3 and diagnostic rules.
Any fixed cap still needs selection; exact code home, stack and verifier remain
Majkee's separate decisions. A new implementation POINT follows those gates.
Syntax validity authenticates no content, proves no reading/delivery, grants no
authority and closes no Phase 0 gate.
