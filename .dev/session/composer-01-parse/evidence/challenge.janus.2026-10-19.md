# Cycle 11 — carried Janus / Majkee decision

Head-authored capture by Cartan on 2026-10-19. Source: Majkee's user message,
addressed `to-cartan from-janus`, carrying the grammar decision after cycle 11.
The payload below is verbatim, including its wrapper and typographic markers.
No separate ranked Janus transcript or runtime receipt was supplied; none is
reconstructed. This direct operator-carried instruction authorizes the bounded
v3 revision and native re-review. It explicitly leaves grammar GO on v3 pending.

## Verbatim carried message

````text
to-cartan from-janus ---

`
Grammar decision (majkee, 2026-10-19, after Janus review cycle 11): drop body_bytes.
▎ Body = the bytes after the body-marker EOL up to the start of the first column-1 line that is exactly <!-- composer:end N --> with the packet's nonce, as in 02 §Zones. The body's own final EOL belongs to the body; an empty body is a body marker immediately followed by the end marker; bodies without a final newline are not representable — accepted. A same-nonce end line inside the intended body closes it early and the true end marker then fails as nonce_reused; the whole document is rejected, no scanning fallback — the §9 "insertion witness" expectation changes accordingly. Nonce: 4–8 chars [a-z0-9] per 02:66.
▎ Keep the rest of v2: string-only flat header, list rule, Q3, UTF-8/BOM/CRLF rules, error model minus the count-specific reasons (count_syntax, body_truncated, body_utf8_boundary, separator_*), diagnostics without raw body text, non-execution plan.
▎ A maximum body size, if wanted, is a fixed limit set once (PAYLOAD_TOO_LARGE style), never a header field.
▎ Add at least one hand-written, un-measured packet to the fixtures.
▎ Astrobley returns v3 as a bounded POINT; the native challenger re-reads the changed sections; grammar GO is then on v3, not v2. Code home, stack and verifier remain my separate decisions.

---

- from: keep as declared string in Phase 0 (no change). Future note for the delivery/relay design: derive sender and compare to declared, as 02 §Message file already rules; VIST supplies occupant evidence, not identity.
- Agent-generated markers: allowed as drafts or via a stdout-only skeleton brick; never a writer of the exchange. No grammar change.
`

---
````
