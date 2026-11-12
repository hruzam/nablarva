VERDICT: PASS
TASK: Recheck corrected zero-valued lineage handling, prior Codex-native findings, legacy synthetic compatibility, and immutable snapshot behavior using synthetic inputs only.

RAN: Full candidate suite (50 tests); focused independent lineage/compaction/rollback/history-mode matrix; native opt-in, cold rebuild, immutable old-bundle, and missing-`input_format` compatibility probes; `zsh -n`; `git diff --check`; shared composer suite (27 tests).

EVIDENCE: All documented lineage variants—including zero-valued `forked_from_ordinal_exclusive` and `subagent_history_start_ordinal`—now disclose incomplete history and prohibit carry-forward. `attached_thread:false` correctly remains non-lineage. Rollback and both compaction forms block carry-forward; unknown history modes fail closed. Native format remains opt-in. Legacy layout metadata missing `input_format` remains compatible. Cold rebuild is byte-identical and later partial publication leaves the old bundle immutable. Hashes: `codex_native.py` `d05f7eb6e8d996884d5f9c23f30cc3011eaa79422711b1fd8d73c436b51dd754`; `transcript.py` `a11b189f2c59af61a8927c044927fc22b00d7887b3710989028b99cad829df06`; `collector.py` `0beda74ca3bb2dd3ecfa61b8cd681c9dda068c65032f720a01b84696e66765bd`; integration tests `4721f093c66be90137e05ee7b85f4bb44c8bac78c901184f3bf294c497919c97`.

FAILURES: none

REPRODUCE: `python3 -I -S -B -m unittest discover -s .dev/session/termbrana-M0-markdown-test/implementation/termbrana/tests -v`; `zsh -n .dev/session/termbrana-M0-markdown-test/implementation/termbrana/{base,keyboard,transcript}.zsh`; `git diff --check -- .dev/session/termbrana-M0-markdown-test/implementation/termbrana`; `PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s /home/hruzam/ia-sync/zsh/termbrana/tests -v`.

RESIDUAL RISK: Native Codex fidelity, private/real histories, runtime-home behavior, and GUI/host interaction remain unverified by scope.
