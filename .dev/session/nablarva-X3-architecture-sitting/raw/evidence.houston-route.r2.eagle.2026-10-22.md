# evidence.houston-route.r2.eagle.2026-10-22 (mechanical extraction, no judgement)

## 1. Source
```zsh
print -r -- $F; wc -lc < $F; sha256sum $F
```
```text
/home/hruzam/.claude/projects/-home-hruzam-unikuklatrix-nablarva/46c2dcf6-0264-4d06-8316-77fe12e0fa0f/subagents/agent-a0618d796fbb697ce.jsonl
    337 2651682
856242efa18e32206fa2dc5f41f0d5d74d8d49275b6cf3a2745de63c1a2fdeb0  /home/hruzam/.claude/projects/-home-hruzam-unikuklatrix-nablarva/46c2dcf6-0264-4d06-8316-77fe12e0fa0f/subagents/agent-a0618d796fbb697ce.jsonl
```

## 2. Fixed prefix (H=179)
```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use" and .name=="SubagentHandback") | $l' "$F" | head -n 1
```
```text
179
```

```zsh
head -n 179 "$F" | sha256sum; head -n 179 "$F" | wc -c
```
```text
4f19e0567ba384c0e8343686a1c2da049fe62bc3d2cf763d4f298d514f3c14a6  -
1531193
```

## 3. Handbacks
```zsh
jq -c 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use" and .name=="SubagentHandback") | [$l, (.input|keys)]' "$F"
```
```text
[179,["message"]]
[242,["message"]]
[263,["message"]]
[336,["message"]]
```

```zsh
for n in $(jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use" and .name=="SubagentHandback") | $l' "$F"); do echo "--- line $n"; sed -n ${n}p "$F" | jq -r '.message.content[]|select(.type=="tool_use" and .name=="SubagentHandback")|.input.message' | head -n 6; done
```
```text
--- line 179
Route: spawned by a parent agent → child; otherwise main session (canary: cl-e1a94c37).
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/sitting.md · stamp: 630f58c3

--- line 242
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/sitting.md · stamp: 630f58c3

**Card: sitting** (continuation, same child and same pen). I spawned nothing. I edited no existing file, and arc.md is untouched. I did not write to or message X2.
--- line 263
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/sitting.md · stamp: 630f58c3

**Card: sitting.** I spawned nothing and edited no existing file; arc.md and arc.r2.md are untouched. I read the X2 disposition file read-only.
--- line 336
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/sitting.md · stamp: 630f58c3

**Card: sitting (R5).** I spawned nothing, applied nothing and edited no existing file; every write is a new file in raw/. Stopped after the four drafts.
```

## 4. Reads before H
```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use") | [$l, .name, (.input.file_path // .input.path // .input.pattern // .input.subagent_type // "")] | @tsv' "$F" | awk -F'\t' '$1<179 && $2=="Read"'
```
```text
16	Read	/home/hruzam/.germline/agents/houston/identity.md
17	Read	/home/hruzam/.germline/agents/houston/binding.claude.md
21	Read	/home/hruzam/.germline/agents/houston/cards/sitting.md
32	Read	/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md
34	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/RUNBOOK.md
36	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md
38	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/prompt.sitting.2026-10-17.md
46	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/crawl.r1-mechanical.2026-10-22.md
47	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/handoff.composer-boundaries.cartan.2026-10-22.md
48	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md
57	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/crawl.r1-mechanical.2026-10-22.md
59	Read	/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
61	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
69	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md
70	Read	/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
71	Read	/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md
72	Read	/home/hruzam/unikuklatrix/nablarva/docs/decisions/README.md
82	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.component-docs-and-nablarva-boost.2026-10-21.md
83	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.adr-task-context.2026-10-21.md
91	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.nablarva-boost-reader-concept.2026-10-21.md
92	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.keys-command-discovery.2026-10-21.md
100	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md
101	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.preflight-and-operator-asks.2026-10-22.md
110	Read	/home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-to-X3-arc.agol.2026-10-22.md
114	Read	/home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md
116	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/cleanup.termbrana.2026-10-21/architecture-owner.proposal.md
124	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md
125	Read	/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md
135	Read	/home/hruzam/unikuklatrix/nablarva/meshup/REGISTRY.md
136	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md
144	Read	/home/hruzam/unikuklatrix/nablarva/PROJECT.yaml
157	Read	/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-X1-composer-sourcing/raw/handoff.cartan.runbook-preparation.2026-10-21.md
```

## 5. Non-Read tool_use before H
```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use") | [$l, .name, (.input.file_path // .input.path // .input.pattern // .input.subagent_type // "")] | @tsv' "$F" | awk -F'\t' '$1<179 && $2!="Read"' | grep . || echo none
```
```text
20	Glob	/home/hruzam/unikuklatrix/nablarva
102	Grep	/home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-to-X3-arc.agol.2026-10-22.md
112	Grep	/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md
126	Glob	/home/hruzam/unikuklatrix/nablarva
145	Grep	/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement
146	Glob	/home/hruzam/ia-sync/zsh/session
155	Grep	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative
165	Glob	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting
172	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/arc.md
```

## 6. Spawn and Write/Edit events (whole file)
```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use") | [$l, .name, (.input.file_path // .input.path // .input.pattern // .input.subagent_type // "")] | @tsv' "$F" | awk -F'\t' '$2=="Agent"||$2=="Task"' | grep . || echo none
```
```text
none
```

```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use") | [$l, .name, (.input.file_path // .input.path // .input.pattern // .input.subagent_type // "")] | @tsv' "$F" | awk -F'\t' '$2=="Write"||$2=="Edit"||$2=="NotebookEdit"' | grep . || echo none
```
```text
172	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/arc.md
236	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/arc.r2.md
257	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/arc.pick.2026-10-22.md
304	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/ARCHITECTURE.draft.md
312	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/wrapper-thinning.diff
321	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/lock-proposals.md
329	Write	/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/card.sitting.draft.md
```

## 7. Other tool names
```zsh
jq -r 'select(.type=="assistant") | input_line_number as $l | .message.content[] | select(.type=="tool_use") | [$l, .name, (.input.file_path // .input.path // .input.pattern // .input.subagent_type // "")] | @tsv' "$F" | awk -F'\t' '$2!="Read"&&$2!="Grep"&&$2!="Glob"&&$2!="Write"&&$2!="SubagentHandback"{print $1"\t"$2}' | grep . || echo none
```
```text
none
```

