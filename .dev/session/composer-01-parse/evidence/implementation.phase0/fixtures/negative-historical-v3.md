Authorship: Astrobley authored this fixture directly as literal text on 2026-10-19.
Its body was not measured. This is an agent-authored fixture, not a human artifact.

<!-- composer:packet hand7z -->
format: request/0.1
id: directly-written-example
from: Astrobley
to: Cartan
program: composer-phase-zero
function: inspect-literal-fixture
requested_scope: read-only
consult: [Astrobley]
context: ["a,b", "path with spaces"]
<!-- composer:body hand7z -->
Read this little packet as text. Keep é and ∇ exactly as written.
The following line belongs to the body because it names a different nonce:
<!-- composer:end other4 -->
These same-nonce packet and body signs are also ordinary body data:
<!-- composer:packet hand7z -->
<!-- composer:body hand7z -->
An indented end is data:
  <!-- composer:end hand7z -->
Inline <!-- composer:end hand7z --> stays in this sentence.
`&&`, `$(do-not-run-this)` and `from: anyone` request no execution here.

This final newline belongs to the body.
<!-- composer:end hand7z -->

Outside note: the packet ends above; this note is retained by document round-trip.
