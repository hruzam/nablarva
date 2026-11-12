# Native capability comparison · 2026-11-05

Observed on hruzam: `codex --version` reports `codex-cli 0.166.0`; `claude --version` reports `2.1.286 (Claude Code)`; `subl` and `zsh` are installed. CLI help exposes Codex resume/fork and Claude resume/continue/fork, but this does not prove source-bookmark fidelity.

- Claude's [session documentation](https://code.claude.com/docs/en/sessions) describes `/export` as readable plain text, and warns its native JSONL format is internal and version-dependent. Export is useful for reading; stable source-record mapping, interaction during a continuing session, and installed-version behavior remain unverified.
- [Codex app-server documentation](https://learn.chatgpt.com/docs/app-server) describes read-only thread metadata and paginated turn/item reads without resume. Forked threads have distinct thread IDs and may share a root session ID. Documentation describes current protocol; installed 0.166.0 support has not been probed. No app-server client is activated in this gate.
- [Sublime's command line](https://www.sublimetext.com/docs/command_line.html) documents `-n` and file line suffixes. The inspected `editor_pin_open_target` source opens an existing address with encoded position; actual interaction remains an operator witness. It supplies editor location, not transcript identity. Its git-root detection starts from the rendered file. README names `~/.pins`, whereas current `pin_core.py` names `~/.wires/pins.jsonl`; neither store was read.

No native facility has yet been shown to meet the full gate. Retire the experimental adapter if a native facility is demonstrated to provide the same selection, source identity, continuity and interaction properties. Treat historical approval data as evidence of a request, not proof of a live pending decision.

Naming sweep: `rg -n 'tbv[-_]' /home/hruzam/ia-sync/zsh /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana -g '!*.lock'` returned exit 1 (no matches) on this host. This is a bounded source sweep, not a global namespace guarantee.
