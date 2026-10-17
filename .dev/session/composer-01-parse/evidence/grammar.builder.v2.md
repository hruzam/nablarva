---
kind: grammar-proposal
version: 2
date: 2026-10-17
author: builder · native Astrobley
cycle: '07'
status: proposed; requires review and Majkee's grammar GO
scope: composer Phase 0 only; no implementation or deployment authority
---

# Composer Phase 0 — proposed counted-body contract

Every normative choice below is proposed, not gaveled. Publication passes to or
through ia-sync under flag L8′. Exact source `/home/hruzam/ia-sync/zsh/composer/`,
Python stdlib and a fresh native Codex verifier remain review proposals. This
document creates no parser, tests, exchange writer, installer, registry or command.
Proposal revision 2 is a complete review candidate; `request/0.1` below is the
proposed initial wire version, not a claim that an earlier grammar was deployed.

## 1. Sources and scope adaptations

Relative paths use the bed
`/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/`.

| source anchor | constraint or proposed adaptation |
|---|---|
| `brief.nabla.composer-build.2026-10-17.md:55,63–73` | Grammar before code; exact corpus bodies, diagnostics and non-execution; named file ownership and four questions. |
| `raw/sella-v.0.1/brief.astrobley.sella-v.0.1.md:15–45` | Explicit small header, `request/0.1`, author-declared id/from, flat consult list, opaque body. |
| `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md:12–20,22–25` | Readable exchange; declared structure only; distinct later procedure/role bindings. |
| `raw/02_PARSER_GATE.md:20–66` | Flat header and header/payload/outside zones. Its single-message `---` fence becomes explicit composer packet/header/body framing. |
| `raw/02_PARSER_GATE.md:44–52,93–105` | Bus sender derivation, generated ids, freshness, registry and gate checks are not composer parse checks. Declared composer identity grants no authority. |
| `research.nabla.composer-prior-art.2026-10-17.md:35–48,59–61` | Human owns exchange; string headers; lossless bytes; B2/B3 typography and marker cases; diagnostic aggregation needs an explicit framing-error limit. |
| `raw/journal.2026-10-16.md:39–43,75–103` | Historic relay packets and guards are corpus content, not current authorization or doing-state. |

The disagreements are material and remain proposals for review:

- Bus `02:65` calls marker-like payload opaque while `02:66,98` reserves same-nonce
  marker lines. This contract does not reserve any body line: required `body_bytes`
  defines the body extent. The parser checks an ending marker only at the counted
  position. This is an adaptation for the composer, not an amendment of the bus.
- Composer uses author-declared `id`/`from` and `format: request/0.1`, whereas the bus
  derives sender, writes ids itself and uses `bus: 1`. Neither declaration authenticates
  the author; there is no tmux, registry, freshness, delivery or gate evaluation here.
- Bus `02:99` forbids empty task payloads and transport control bytes. This inert
  parser accepts empty and control-containing valid UTF-8 bodies. It must not echo
  raw body controls to a terminal. Transport safety remains a separate future check.
- Bus `02:93` is fail-fast; research A7 wants all findings. This proposal collects
  independent header findings in safely framed input, then stops on its first
  unusable count or framing error. It does not scan an uncertain body to recover.

These adaptations expose the overlap noted by `brief:17–18`; raw sources are
preserved. No consequential choice is promoted to a lock by this document.

## 2. Document, Q3 and ownership

Propose one human-owned Markdown exchange containing several packets in document
order. Outside text may precede, separate and follow them and is preserved verbatim.
The parser reads only saved bytes; it never writes the exchange or treats an unsaved
editor buffer as input. It recognizes no packet from informal `to-...`, `from-...`,
`&&`, bare `---`, Markdown fences or journal headings.

Q3 proposal: compose in the exchange, with no second per-prompt drafts tree. Later
Phase 2 may freeze a selected packet to `prompts/<id>/<rev>.md`; this Phase 0 creates
none. Existing frozen EXCHANGE files are bodies for tests, not composer documents to
migrate. Q4 gives `&&` no action in Phase 0; Q1/Q2 render policy and Q5 rotation stay
open. No references are opened and no body/header/outside text is executed.

## 3. Frame and exact byte ownership

Markers have exactly these ASCII spellings at column 1, with the shown single spaces:

```text
<!-- composer:packet N -->
<!-- composer:body N -->
<!-- composer:end N -->
```

`N` is a placeholder for exactly 16 lowercase hexadecimal characters, `[0-9a-f]{16}`.
Each top-level packet uses one N for its three frame markers and a nonce unused by
other top-level packets in that document. Nonce length adapts bus `02:66` (4–8
characters); it provides readable frame correlation, not collision-based body safety.
Body text may repeat N and any of these exact markers arbitrarily.

State sequence is outside → header(N) → counted body(N,L) → exact trailer → outside.
Outside recognizes a packet opening marker. A body/end marker outside is an orphan;
any exact marker with a previously closed top-level nonce is nonce_reused. Within
the header, lines are header fields until its matching body marker; other exact
markers are marker_order. No packet may open inside another header.

Let E be the opening marker's EOL, either LF (`0a`) or CRLF (`0d0a`). Opening,
header and body-marker syntax lines must have E; the final end marker may end at
EOF without an EOL, otherwise its EOL must be E. Different packets may use different
E. A physical line ends at LF, with immediately preceding CR counted as CRLF; bare
CR is not a line separator and is invalid on syntax lines. Body/outside line endings
are unchanged, including mixed LF/CRLF or bare CR data inside a body.

At a syntactically complete body marker, let s be the offset just after its EOL.
Decode the required `body_bytes` string into a bounded count L under section 5.
Set t = s + L. B is exactly the half-open byte slice [s,t). Do not inspect B for
markers, front matter, signs, headers, Markdown fences, commands or nested packets.
The only interpretation of B is its required UTF-8 validity and its byte extent.

At t require exactly E, which is a framing separator outside B. At t+len(E) require
exactly `<!-- composer:end N -->`, with the same N. Then require EOF or E. There is
no search for a closer, no attempt with another nonce/count, and no resynchronization
after any count, separator or end-marker error. Bytes that happen to form a marker
before or after the expected position cannot repair the frame.

The opening/body-marker EOLs, the extra separator at t, all marker bytes and the
ending marker's EOL are framing bytes. None belongs to B. The separator is exactly
len(E) bytes at the known t; never remove an additional newline or a final body CR.
For an empty B, the body-marker EOL and separator are separate: one blank physical
line is required before the end marker. Body and header spans retain all raw bytes.

| E | B in byte notation | L | bytes after body-marker EOL, before ending marker |
|---|---|---|---|
| LF | empty | 0 | `\n` |
| LF | `x` | 1 | `x\n` |
| LF | `x\n` | 2 | `x\n\n` |
| LF | `x\n\n` | 3 | `x\n\n\n` |
| LF | `x\r\n` | 3 | `x\r\n\n` |
| LF | `x\r` | 2 | `x\r\n` |
| CRLF | empty | 0 | `\r\n` |
| CRLF | `x` | 1 | `x\r\n` |
| CRLF | `x\n` | 2 | `x\n\r\n` |
| CRLF | `x\r\n` | 3 | `x\r\n\r\n` |

Explicitly empty bodies are valid syntax. Operation-specific requirements for task
content remain outside this parser. Missing body marker, omitted separator or wrong
ending marker is invalid framing. Whole-document validity requires at least one
complete packet; a valid prefix cannot authorize extraction when a later packet fails.

Outside/header lines beginning with `<!-- composer:` after removing leading ASCII
spaces/tabs, but failing the marker grammar, are marker_syntax. Never accept that
indentation, trailing spaces, capitalized verbs, malformed nonce or truncated `-->`
as a delimiter. Uppercase `COMPOSER` and inline markers are ordinary outside prose.
Markdown fences provide no shielding in outside/header states. All such spellings,
including malformed and same-nonce markers, are ordinary data inside [s,t).

## 4. Encoding and lossless representation

The complete input must be valid UTF-8; reject invalid byte sequences without
replacement decoding before interpreting structure. Preserve optional initial UTF-8
BOM bytes at absolute document offset zero as outside bytes, ignoring them only for
first-line recognition. U+FEFF elsewhere is body/outside data and counts three bytes
when in B; it is invalid in a header. Never remove a BOM from inside a body.

Counts measure bytes of the saved UTF-8 encoding, not characters, display columns,
graphemes or a normalized string. CRLF contributes two bytes, LF one, BOM three.
For example `é∇\n` is six UTF-8 bytes (`c3 a9 e2 88 87 0a`) and three Unicode scalar
values. Do not use text-mode newline conversion or Unicode normalization. A decoded
count landing inside a multibyte sequence is ENCODING_INVALID/body_utf8_boundary,
even if the whole document has valid UTF-8. The body slice itself must decode cleanly.

Retain the original document bytes, ordered packet/header/frame/body spans and the
decoded header fields. All header values remain strings or flat lists of strings;
the numeric L is a separate framing result derived only from body_bytes. Lossless
re-emission copies original spans; it does not serialize decoded fields anew. Both
each packet and the full document must round-trip byte-identically, including raw
quotes, spaces, ordering, initial BOM, outside notes and every framing EOL. Editing
the decoded values and generating new bytes is not part of this Phase 0 contract.

## 5. Flat header, required count and strings

Header lines are column-1 `key: value`, with key `[a-z][a-z0-9_]*`, colon and one
required ASCII space. Additional ASCII spaces around a value are trimmed for decoding
only, retained in raw bytes. No tabs, blank lines, comments, indentation, continuations,
nesting or multiline values. Field order is free. All unknown keys and repeated keys
are errors, including equal repeats. For diagnostics only, tokenization can recognize
uppercase ASCII key letters too; an uppercase key is unknown_key, never corrected.

| key | required | decoded value |
|---|---|---|
| `format` | yes | scalar exactly `request/0.1` |
| `id` | yes | nonempty scalar, unique by exact decoded value in the document |
| `from`, `to` | yes | nonempty scalar declarations, no authentication |
| `program`, `function` | yes | nonempty scalar binding names; resolution deferred |
| `requested_scope` | yes | nonempty scalar; no enforcement claim |
| `body_bytes` | yes | scalar with canonical decimal syntax below |
| `consult` | no | flat string list; absent means empty list |
| `in_reply_to` | no | nonempty scalar; resolution deferred |
| `context` | no | flat string list; absent means empty list |
| `expected_return`, `stop` | no | nonempty scalar; not semantically evaluated |

For absent-required-field order, expand combined rows left to right: format, id,
from, to, program, function, requested_scope, body_bytes. No other implicit defaults.
No bus/type/hold/created/thread/rev or extension keys. Names and references are opaque
case-sensitive strings: do not open paths, query a registry, resolve reply lineage,
reject missing files or evaluate permissions. Only decoded id uniqueness is structural.

Scalar source is bare text or one complete JSON double-quoted string. Bare values
are nonempty and exclude ASCII controls (C0 and DEL), ASCII double/single quotes,
square/curly brackets and U+FEFF. U+2018/U+2019/U+201C/U+201D are prohibited only as
the first/last bare-value character, avoiding accidental smart quote delimiters;
inside a bare value they are ordinary data. Colons, hashes, backticks, `&&`, dates,
digits and backslashes are literal; there are no YAML comments, aliases or coercions.
Thus `no`, `2026-10-17` and `01234567` stay those strings in ordinary scalar fields.

JSON-string form uses standard JSON escapes and no trailing nonspace source text.
Reject empty decoded strings, C0/DEL, unpaired surrogate escapes and U+FEFF. Quoted
strings may contain apostrophes, brackets, commas and smart quotes; escaped newline
or tab is invalid after decoding. Tabs in header source are always invalid, even
inside a string. Trailing ASCII spaces are accepted and preserved in the raw header.

For body_bytes specifically, first decode the scalar by those same rules. Its
decoded string must match exactly `0|[1-9][0-9]*`. `0`, `12`, `"12"` and
`"\u0031\u0032"` are valid count spellings with string values `0` or `12`. Reject
`00`, `012`, signs, decimals, exponent notation, Unicode digits, separators, interior
spaces and quoted surrounding spaces. Never treat this as general numeric coercion.
Empty scalar uses FIELD_MISSING/empty_value; a nonempty scalar failing decimal syntax
uses FIELD_INVALID/count_syntax. Scalar/list shape or string syntax errors retain
their ordinary diagnostics. Count zero is valid and means an empty B.

body_bytes must occur exactly once and have valid syntax before any body can be
consumed. Missing, malformed, duplicated or otherwise undecodable count makes its
frame unusable. Complete the already readable header's independent findings at its
body marker, then stop without scanning any prospective body or emitting a second
speculative boundary error. Do not pick the first or last of duplicate counts.

For a usable count and known s, let R = len(input) - s. Compare canonical decimal
digits against the decimal representation of R by length and lexicographic order
before integer conversion. L > R, including a million-digit valid decimal, is
BOUNDARY_INVALID/body_truncated at EOF, field body_bytes. Do not allocate L bytes,
clamp L or impose an undocumented host-dependent integer limit. Convert only after
L <= R, so L and t are bounded by the actual input's byte length. No fixed payload
cap is proposed here; memory/I/O exhaustion is operational failure, never success.
A body that fits R can still lack its required separator/trailer and then fails
those exact-position checks. Counts do not include separator or marker bytes.

## 6. Flat lists

Only consult/context use lists: `[` zero or more string items separated by commas
`]`, with ASCII spaces around tokens permitted. `[]` is valid; no empty item,
trailing comma, nesting, maps, comments, tabs or multiline forms. A bare item follows
the scalar rule but cannot include a comma. JSON-quote an item needing commas or
brackets, e.g. `context: ["a,b", "path with spaces"]`. Tokenization respects quotes
and escapes; blindly splitting commas is incorrect. Empty decoded items are invalid.
`consult: [Astrobley]` remains accepted. Retain order and repeated elements; identity
resolution/deduplication is not parsing. Scalar in a list field or list in a scalar
field is FIELD_INVALID/wrong_shape. Never convert a list item to a number/date.

## 7. Complete valid examples and maintenance tradeoff

Before a body edit (LF frame; B = `alpha\nomega\n`, 12 bytes):

```text
<!-- composer:packet 0123456789abcdef -->
format: request/0.1
id: example
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
body_bytes: 12
<!-- composer:body 0123456789abcdef -->
alpha
omega

<!-- composer:end 0123456789abcdef -->
```

After inserting a literal same-nonce end-marker line in B and refreshing the count
(B = `alpha\n<!-- composer:end 0123456789abcdef -->\nomega\n`, 51 bytes):

```text
<!-- composer:packet 0123456789abcdef -->
format: request/0.1
id: example
from: Majkee
to: myShell
program: journal-continuity
function: list-pending
requested_scope: read-only
body_bytes: 51
<!-- composer:body 0123456789abcdef -->
alpha
<!-- composer:end 0123456789abcdef -->
omega

<!-- composer:end 0123456789abcdef -->
```

These are separate documents, not two packets with duplicate id/nonce. The blank
line before each true ending marker is the extra framing separator after B's final
LF. The internal same-nonce line in the second example has no structural meaning.
With body_bytes left at 12 after that insertion, the byte at s+12 is not LF: report
separator_mismatch at s+12, never a shorter successful packet. This is a specific
negative with checked arithmetic, not a promise that every conceivable stale count
or edit can be recognized.

Human-maintenance cost is explicit: every body byte-length change requires updating
body_bytes, including line-ending conversion, a new final newline, smart quote
substitution or a multibyte character. LF→CRLF on the frame alone leaves L unchanged;
doing so inside B generally changes L. UTF-8 encoding arithmetic is less convenient
than hand-editing prose. A future read-only count/check helper could explain a
mismatch but must be separately scoped; no automatic repair, exchange writer or
preflight utility is authorized by this proposal. The parser must not recompute
and silently replace a supplied count or guess the intended ending marker.

L establishes declared extent, not authenticity, unchanged content, authorization,
intended prose or semantic correctness. Equal-byte-length edits can remain valid;
even a stale count can coincide with a valid trailer at that offset. This contract
reports the span the complete syntax declares. It does not certify the author's
unrecorded intent. Literal markers anywhere inside a correctly counted B are
unconditionally opaque; no collision scan or nonce regeneration is required for B.

## 8. Deterministic errors and aggregation boundary

Check success exits 0; any input data error exits 65 (the data-error class from
`raw/01_SYNC_METHOD.md:78–91`). File/I/O/resource failure is operational (propose 74),
never an empty valid document. No eventual CLI or installed command is settled here.
An invalid document yields diagnostics and no successful packet result for downstream
use, even if earlier packets were sound. Retaining raw bytes for human diagnosis is
permitted; acting on a valid prefix is not.

Each diagnostic has exactly code, reason, byte_offset, line, byte_column,
packet_nonce (string or null), and field (header key or null). Byte offsets are
zero-based absolute; lines/byte columns one-based, each LF increments line. BOM bytes
count toward offsets/columns. EOF is len(input); offset after a final LF is next
line column 1. Never include raw body text, clock, randomness, locale-dependent
prose or file paths. Fixed code/reason pairs:

| code | reasons |
|---|---|
| ENCODING_INVALID | invalid_utf8, body_utf8_boundary |
| BOUNDARY_INVALID | marker_syntax, marker_order, nonce_reused, missing_body, frame_eol, no_packets, body_truncated, separator_missing, separator_mismatch, end_truncated, end_mismatch |
| HEADER_INVALID | header_line, header_syntax, unsupported_format |
| FIELD_MISSING | required_absent, empty_value |
| FIELD_INVALID | unknown_key, duplicate_key, wrong_shape, invalid_string, invalid_list, duplicate_id, count_syntax |

For textual diagnostics, propose one JSON object per LF-terminated line, keys in
the order listed above, no spaces around JSON separators, integer decimal offsets,
literal JSON null and no summary or other output interleaved. Empty diagnostic
sequence emits no diagnostic bytes. This freezes the diagnostic representation
without choosing an installed CLI or the parse/byte-output invocation interface.

Deterministic processing order:

1. Validate complete-input UTF-8 first. On failure return only invalid_utf8 at the
   first invalid-sequence start, with null nonce/field; do not parse structure.
2. Walk outside/header syntax in source order. For markers, precedence is malformed
   marker spelling, reused nonce (outside only), marker order, then required EOL.
   A wrong-nonce marker in a header is marker_order. EOF without its matching body
   marker is missing_body. Never search forward past a structural error.
3. For header lines, wrong/missing frame EOL is frame_eol before value checks.
   Otherwise check line shape, known/unique key, value shape, string/list decoding,
   then format/count constraints. One first-failure diagnostic per line. Recognized
   keys with invalid values still count as seen; another occurrence is duplicate_key.
   Unknown-key repeats remain unknown_key because no supported field was recognized.
4. At matching body marker, add required_absent for never-seen required keys only,
   in section-5 order. Empty/invalid seen keys already have findings. Retain every
   independent header finding collected. If body_bytes is absent/unusable, stop
   framing here; its original header diagnostics suffice. Do not invent an inferred
   count or an extra body/trailer error. Non-count field errors alone do not prevent
   checking a safely counted span, but the whole document remains invalid.
5. With usable L, compare against R before conversion. L > R gives body_truncated
   at EOF. Otherwise inspect only B's UTF-8 validity: an endpoint in a multibyte
   sequence gives body_utf8_boundary at t, field body_bytes. Then check exact E
   at t: too few bytes gives separator_missing at EOF if the available prefix is
   correct; a mismatching byte gives separator_mismatch at the first mismatch.
6. Check the exact end-marker bytes at m=t+len(E), sequentially: first mismatch is
   end_mismatch there, including wrong nonce/spelling/indentation; a matching proper
   prefix reaching EOF is end_truncated at EOF. After the marker require EOF or E;
   bad/partial EOL gives frame_eol at its first wrong/missing byte. Stop on the first
   of these failures, with no scanning fallback. No other line can close that body.
7. After sound trailer, resume outside at the next line. Check decoded id uniqueness
   only for ids whose first occurrence had a successfully decoded value, at each
   later successfully decoded id line. No normalization/case folding. At clean EOF
   with no opened packet, no_packets at offset zero. Never add no_packets after a
   more specific failed opening/header. Retain earlier independent header findings
   when a later structural failure stops the walk.

Blank/comment/indented/tab-containing header lines use header_line; other violations
of key/colon-space use header_syntax. Scalar value beginning `[`/`{`, or list value
not beginning `[`, uses wrong_shape. Bad scalar syntax uses invalid_string; bad
list syntax/items use invalid_list. Empty bare/decoded scalar uses empty_value;
empty list item invalid_list. Nonempty decoded body_bytes with invalid decimal
syntax uses count_syntax. Unsupported decoded format uses unsupported_format.

Header findings anchor at offending line start (including duplicate id/key), absent
fields at body-marker start, malformed/order/reused markers at their line start,
missing_body at EOF. All byte checks use the offsets specified above. Field names
are populated only after key tokenization; body_bytes field-validation errors,
body_truncated and body_utf8_boundary use field body_bytes. Separator/end/marker/
frame-EOL and other non-field errors use null. Nonces are null before
a valid opening is known and N thereafter; orphan end/body uses its parsed nonce.

Sort final diagnostics by ascending byte_offset, code ASCII order, reason ASCII
order, then field ASCII order with null first. Exact ties retain encounter order;
do not deduplicate. This total deterministic ordering is independent of locale.
Only independently knowable findings are aggregated: no diagnostics are claimed
for the unframed suffix after count/framing failure. This is the explicit A7 limit.

## 9. Future acceptance evidence

This is a plan, not implemented or executed parser tests. A later POINT must supply
approved code home, callable check/parse/lossless-output interfaces, output/fixture
scope and exact commands. Retain runner commands, exit outcomes, diagnostic bytes,
source offsets/hashes and direct `cmp -- <expected> <actual>` outcomes (expected 0).
Hash agreement supplements exact comparison rather than substituting for it.

Use every brief §3 body unchanged, measured from the frozen input bytes:

| B | source extent | body_bytes |
|---|---|---|
| counsel exchange | `raw/EXCHANGE.md`, whole file, lines 1–159 | 10307 |
| Sella exchange | `raw/sella-v.0.1/EXCHANGE.md`, whole file, lines 1–130 | 8459 |
| Oraculum brief | `raw/sella-v.0.1/brief.oraculum.sella-v.0.1.md`, whole file, lines 1–88 | 5499 |
| operational bed | `raw/journal.2026-10-16.md`, lines 39–407 inclusive, byte slice [2061,16595), ending before line 408 `# 2. JEV` | 14534 |

`evidence/corpus-inventory.cartan.json` supplies only these observed byte/line/hash
facts, not grammar or test conclusions. Recheck input identities and arithmetic
before using them. For each B, wrap with correct L and LF, then CRLF framing without
altering B (eight fixtures). Also combine four packets in one mixed-frame document
with outside notes and initial BOM. Require exact order/count, B byte comparisons,
packet byte comparisons and whole-document round-trip. No collision-free nonce
selection is required for B; only distinct top-level nonces.

Additional positive fixtures must cover:

- Every section-3 byte-table row, bodies with/without final newline, multiple final
  blank lines, BOMs, CRLF/LF/bare CR, Unicode, tabs and valid UTF-8 control bytes.
  Cover a final end marker both with its EOL and directly at EOF without EOL.
- Exact same-nonce packet/body/end lines together inside one counted body (121
  bytes for the three LF-terminated forms with N=0123456789abcdef); same forms in
  prose/fences, a matching-end line alone, malformed/different-nonce markers, headers,
  signs, relay brackets, `---`, backticks, `&&`, inline and indented versions. Every
  byte inside B stays data; no recursive extraction or extra-pair rejection.
- Both complete section-7 examples with L=12 and L=51; one full second example
  plus outside notes. Require the complete declared body, including its internal
  same-nonce end line, not the shorter delimiter-prefix body.
- B=`é∇\n`, L=6 (three Unicode scalars); body_bytes bare, JSON-quoted and escaped
  decimal strings; zero count; empty/absent lists; quoted list commas; raw/quoted
  `no`, dates and digit-only ids; reordered headers and trailing spaces preserved.
- Deliberate equal-byte-length body edits with unchanged count and correct trailer
  remain parse-valid. This witnesses that length is not content integrity.

Negative fixtures assert exit 65, no usable partial result and exact diagnostics,
with repeated runs producing byte-identical diagnostic output:

| family | cases and expected result |
|---|---|
| missing/unusable count | Absent body_bytes → required_absent; empty → empty_value; duplicate even equal → duplicate_key; invalid string/list/decimal → its defined field error; stop at body marker without scanning B. |
| decimal syntax | `00`, `012`, `-1`, `+1`, `1.0`, `1e2`, Arabic-Indic digits, `" 12 "` → count_syntax; huge valid canonical decimal → body_truncated by bounded comparison, no huge allocation. |
| required insertion witness | Insert the section-7 same-nonce end line into B=`alpha\nomega\n` without changing L=12 → separator_mismatch at s+12; require rejection instead of a shorter valid body. |
| stale small/large counts | Set L to actual bytes minus/plus one with known ASCII boundary bytes chosen to mismatch the expected separator/end; assert the resulting exact-position error, never search forward. Include deletion and LF↔CRLF conversion inside B without refreshing L. |
| UTF-8 counts | Whole input invalid UTF-8 → invalid_utf8 only; L=1 for B starting `é` → body_utf8_boundary at s+1; L=3 (character count) for `é∇\n` → body_utf8_boundary at s+3. |
| truncated body/trailer | L greater than bytes remaining after s → body_truncated at EOF; L consumes exactly to EOF → separator_missing at EOF; missing/partial separator or end marker → defined first mismatch/EOF error. |
| boundary | Wrong separator, matching end marker only later, wrong end nonce, missing/bad end EOL, adjacent body/end without separator even with L=0 → exact-position boundary error; no fallback. |
| header | Required fields absent/empty, unknown/capitalized or duplicate keys, unsupported version, indentation/tabs/comments, bad quotes/lists/nesting/escapes → defined header errors. |
| document | Only outside text → no_packets; reused top-level nonce or orphan marker → boundary error; duplicate ids → duplicate_id; valid prefix and malformed later packet → whole document invalid. |

Freeze each multi-error expected diagnostic sequence from section 8 before writing
assertions. Include two soundly counted frames with non-count header errors followed
by an unusable-count third frame: collect all safe header findings, then stop without
reporting fabricated errors from its body or any apparent later packets.

Non-execution: include literal shell substitutions/backticks, `&&`, executable-looking
tags and sentinel write instructions inside body, quoted body content and outside.
Construct fixture bytes without shell interpolation. Run only the approved parser;
capture sentinel absence, input/reference before/after identities and child-process
evidence where available. Independently inspect its call path for shell/eval/exec,
reference opening and command dispatch: sentinel absence alone proves too little.
Expected: no child execution, no exchange/raw/STATUS mutation, no interpretation of
body markers/commands, outputs confined to the future authorized fixture/output
scope and escaped diagnostics. No raw body control bytes may reach terminal output.

## 10. Four questions and decisions for review

Using `raw/05_WAY_OF_THINKING.md:7–21`, briefly:

1. Conventional pattern: a length-prefixed UTF-8 record in a readable multipart
   document, with flat string metadata and preserved byte spans.
2. Supplied prior art already identifies delimiter collision, implicit YAML typing
   and round-trip loss (`research:23–25,37–44`). Borrow exact counts and positions,
   string-only decoding and raw spans. Reject delimiter scanning and reserialization.
3. Open edge here: the human must maintain a UTF-8 byte count while editing prose.
   Stale counts often reject but are not an integrity/authorship mechanism. Expose
   mismatch, never silently fix it. Any count helper needs a separate authority edge.
4. Our specific choices: counted composer framing/header vocabulary, Q3 exchange
   ownership and the diagnostic recovery boundary. Keep registry, policy, rendering,
   delivery and project state in their separate owners/later phases.

Review must decide the concrete counted frame, required count syntax, header/list
vocabulary, empty/control-body policy, Q3 and limited diagnostic aggregation. Exact
external home/stack/verifier and the implementation POINT remain pending. Validity
under this proposal proves only the declared byte structure; it grants no authority,
proves no reading/delivery, authenticates no content and closes no Phase 0 gate.
