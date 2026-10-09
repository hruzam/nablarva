# Witness — Houston as a Codex child (X1 check 3, child route)

`witness: assay (fresh eyes, read-only) · spawned by oraculum(cSharp) · 2026-10-09 · filed verbatim by the carrier`
`evidence: head rollout 01a11f8d-c6c9-7051-b8b5-6c38daa3267a · child rollout 01a11f95-17d1-7e63-928c-fb8273800ff0 · brief raw/probe-brief.houston-child.2026-10-09.md · artifact .codex/agents/houston.toml (developer_instructions → 9c0856f5)`

WITNESS: PASS-WITH-FINDINGS

1. ROUTE: PASS. Head line 1 = spawn_agent {"task_name":"houston_consult","agent_type":"houston","fork_turns":"all"}; child session_meta parent_thread_id=01a11f8d…, agent_role="houston", agent_path=/root/houston_consult, depth 1, cli 0.162.0.
2. RENDER LOADED: PASS. Child line 9 developer message (27996 bytes) byte-identical to the TOML developer_instructions (blob 9c0856f5); opens with the identity stamp 32fcf199…; tail present ("These document entry mechanisms, not this candidate's fresh-session behaviour.").
3. IDENTITY: no visible collision, weak positive evidence. Child also loaded the project AGENTS.md chain (line 5, user role) incl. "I am @Cartan"; Houston render sits on the developer message. Child never claimed Cartan; output followed the Houston card shape. No direct "who are you" probe was run.
4. CARD SHAPE: PASS. "card: consult / verdict: fits", evidence PROJECT.yaml:14 + flag.md:150–153 (loose; item 9 is 149–152), Unverified line, 0 constraints, full 3-part source stamp named.
5. BOUNDS: PASS, cooperative only. 2 exec calls, read only PROJECT.yaml + flag.md (whole file); no writes, no spawns. Child turn_contexts = head's exactly (workspace-write, network off, on-request, reviewer "user", model gpt-5.6-terra, effort medium) — the TOML narrows nothing; read-only rests on the card text. Runtime injected "multi_agent_mode: do not spawn sub-agents".
6. RELAY: PASS. Head line 34 relays verbatim and stops.
7. FINDING CORRECT: yes (PROJECT.yaml:14 docs.architecture → docs/ARCHITECTURE.md; flag L16 · 9 names it as the whole-animal home; file exists).

findings: Turn 2 effectively ran via the parent's followup_task (head line 105 → child turn 3, answer line 49): child kept context, named decisive evidence, quoted the tail canary verbatim. Direct /subagents input disabled by design (head line 160) — continuation goes through the parent. fork_turns="all" yet child history shows only AGENTS.md + brief + render.
unverified: encrypted spawn/follow-up payloads; Houston voice under a prompt that does not name it; any enforced (not cooperative) read-only bound.
