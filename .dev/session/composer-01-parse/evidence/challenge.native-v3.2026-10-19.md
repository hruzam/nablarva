# Native v3 challenger — cycle 13

Captured verbatim by Cartan on 2026-10-19 from the final native reply of new
`/root/grammar_challenge_v3`, role `challenger` (configured gpt-5.6-sol/xhigh),
fresh initial context. The former child was absent at dispatch; this is not a
restored session. Read-only reply, head-authored capture in evidence/.
Subject: grammar v3 SHA256
578f01f9f5f01e7121cdcdee224c5259f32c345079e3a0dfe09c9344f56bf91b.

## Verbatim reply

POSITION: PROCEED
PRIMARY RISK: Text-mode line handling may erase the distinction between malformed end-like body data and the first exact closer with a wrong EOL; §§3 and 8 require that closer to fail immediately with `frame_eol`, without fallback.
ALTERNATIVE: Parse physical lines from raw UTF-8 bytes while retaining each original terminator, and freeze the §9 wrong-EOL-first-closer case before acceptance.
WATCH: Any test accepts a later valid closer after the first exact closer has the wrong EOL.
