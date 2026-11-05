# Native focused challenge — cycle 06

Captured verbatim by Cartan from native challenger `/root/grammar_challenge`, fresh
context, configured gpt-5.6-sol/xhigh, 2026-10-17. The role wrote no files.
This is a read-only design finding, not a functional verification or gavel.

<!-- BEGIN VERBATIM REPLY -->
POSITION: REVISE
PRIMARY RISK: Collision preflight cannot guarantee intended body extent in the human-edited exchange: one same-nonce `end(N)` line introduced after preflight silently becomes the terminator, and the grammar explicitly accepts that truncated frame as valid. This defeats the Phase 0 body-identity gate despite acknowledging the ambiguity (`evidence/grammar.builder.v1.md:123-137,344-366`; `brief.nabla.composer-build.2026-10-17.md:55`; `research.nabla.composer-prior-art.2026-10-17.md:37-44,61`).
ALTERNATIVE: Add a required decimal `body_bytes` header field and consume exactly that many bytes after the body-marker EOL before requiring the separator and matching end marker; marker lines within that counted span remain body data, while stale counts fail closed.
WATCH: A negative that inserts one same-nonce end marker into a previously valid body without updating `body_bytes` must fail instead of returning a shorter valid packet.
<!-- END VERBATIM REPLY -->
