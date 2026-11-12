# Independent review · synthetic Claude and performance

**Claude verdict: PASS.** The reviewer ran 58 tests and an independent in-memory
and CLI probe. A complete invalid UTF-8 record gives a redacted, line-specific
`SourceError` with no private marker or byte representation in the output. The
same invalid bytes in an unterminated tail remain deferred, preserving prior
exchanges. This establishes synthetic byte-boundary behavior, not Claude native
schema or fidelity.

**Performance verdict: PASS.** The reviewer ran the finalized 59-test suite,
the synthetic end-to-end benchmark, independent duplicate-ID edge probes and
raw-input hash checks. The conversation-only seen-ID set preserves ordering,
unsupported-record behavior and the exact later-duplicate error. A 2,000 to
20,000 record parser probe scaled 10× in input size in 11.28× time. The three
original raw inputs still matched their recorded SHA-256 values. Performance
numbers remain synthetic and wall-clock dependent; no native history was
inspected or benchmarked.

Reproduce from `/home/hruzam/unikuklatrix/nablarva` with:

```sh
python3 -I -S -B -m unittest discover -s .dev/session/termbrana-M0-markdown-test/implementation/termbrana/tests -v
python3 -I -S -B .dev/session/termbrana-M0-markdown-test/benchmark.sandbox.py
```
