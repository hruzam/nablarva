# Cycle 15 — native challenger on C1 grammar v4

Head-authored capture by Cartan, 2026-10-20, office. Native target:
`/root/grammar_challenge_v4`, role `challenger`, fresh context (`fork_turns: none`).
It received POINT 15 and artifact paths, with no builder working transcript or
prior review/verdict conclusions. The newly observed version of Flight's POINT
was supplied as an additional source during review. No claim of an enforced
read-only sandbox or independent functional acceptance is made.

Reviewed v4 SHA256:
`a977682c65bcd6b3c66cc67cb7c2b40a926cf4d96a7f58eb50f1a1fb0839b2ec`.

## Verbatim native reply

```text
POSITION: PROCEED
PRIMARY RISK: Implementation could treat removed `program`/`function` as optional known fields, producing `duplicate_key`, `empty_value`, `wrong_shape`, or success instead of `unknown_key`; v4 explicitly requires whitelist lookup before value and repetition handling and retains exactly five required keys (`grammar.builder.v4.md:205–228, 387–405`).
ALTERNATIVE: Implement one whitelist-first header-classification path and a table-driven conformance case covering scalar, list, empty, malformed-value, and repeated removed keys (`grammar.builder.v4.md:505–518`).
WATCH: Confirm a five-key pair-free header succeeds, a truly empty header yields exactly five `required_absent` findings, and the first exact wrong-EOL closer still stops with `frame_eol` (`grammar.builder.v4.md:400–414, 495–517, 525–527`).
```
