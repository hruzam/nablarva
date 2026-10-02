# `jev` — identification + event catalogue row
Date: 2026-10-02 · Author: @Epoch · Triggered by: events-map v0.2 "candidate `jev` (everything unknown)"
Caveat: WebFetch returns small-model summaries (S), not verbatim pages. Conf H = vendor/primary read this run; M = third-party/summary; L = inferred. Repo stats (stars) volatile, omitted.

## 0 · Headline

**`jev` is not a terminal coding agent. It is a MODEL: TypeSafe AI's "Jev", a "System One" decision model (typed yes/no · choice · score in, calibrated probabilities out; never writes text, never calls tools, no loop).** The "different case" is therefore categorical: there is no agent session to observe. What exists in the wild is (i) the model's API/SDKs, (ii) a CLI binary literally named `jev` (jev-cli), (iii) many third-party harnesses/hooks/zsh plugins built around it. majkee's phrasing ("accessible via zsh; building UI + harness and testing where the role fits best") fits this: the model is a role-player (gate / router / filter / ranker) inside someone's harness, reached from the shell. Whether majkee means the jev-cli binary, a zsh plugin, or his own harness cannot be determined from sources — ASK.

## 1 · Candidate table (all things named jev, 2026-10-02)

| Candidate | What | Author | Licence | Install | Versions / dates | TUI / headless | Terminal coding agent? | Source | Conf |
|---|---|---|---|---|---|---|---|---|---|
| **Jev (model)** | System One decision model; cloud-only, proprietary weights; `POST https://api.typesafe.ai/v1/systemone`; $0.042/M input tokens, output free; 70–500 ms claimed | TypeSafe AI (SF; CEO Diogo Almeida per press digest) | model proprietary; SDKs MIT (`@typesafe-ai/sdk` JS, `typesafe-sdk` Py) | API key via console.typesafe.ai; Vercel AI SDK/Gateway | First public model. Announced **2026-09-15** (flaviocopes.com, search digest) vs **2026-09-28** (typesafe.ai blog fetch summary) — **sources conflict**; blog says early access/waitlist, no version number ("only 'Jev'") | n/a (API) | **No** — "not a chatbot… not a coding model" | https://typesafe.ai/blog/introducing-system-one-models-and-jev · https://flaviocopes.com/jev/ · https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making | M-H (S) |
| **`jev` CLI (jev-cli)** — the binary literally called `jev` | one-shot CLI: `jev noul|choice|score`, `jev batch run`, `jev mcp serve`, `jev validate` (offline) | shaharia-lab (third party, not TypeSafe) | Apache-2.0 OR MIT | install.sh (Linux/macOS/Win), Homebrew, `cargo install` | v0.1.0-rc.1 2026-09-19 · v0.1.0 & v0.1.1 2026-09-20 · **v0.2.0 2026-09-25 (latest)**; background auto-update with opt-out | headless only; no TUI | **No** — classifier, exit codes | https://github.com/shaharia-lab/jev-cli · .../releases | M (S) |
| jev-shell-history | zsh widget: ranks last 100 history entries with Jev, grey ghost-text, → / ^E accepts; widget `jev-accept-suggestion`; zsh 5.9+, Node 22+ | mrnugget (+ fork guuzaa) | not read | git clone + source | not read | zsh ZLE, no agent | No — this is the literal "accessible via zsh" thing | https://github.com/mrnugget/jev-shell-history | M (search digest) |
| **jevdev** | coding-agent harness around Jev: typed content-addressed state chunks in redb, Jev decides context/cache/routing/tools/permissions per turn; ratatui TUI + `jevdev run --yes` headless; Cedar policy `.jevdev/exec.cedar`; drives claude-opus-5 / sonnet-5 / haiku-4-5 via Anthropic | ibrahimcesar | Apache-2.0 | `cargo install jevdev` | 5 commits, **no release tags**, "Early" | TUI + headless | **Yes (closest to "terminal coding agent")** — but alpha | https://github.com/ibrahimcesar/jevdev | M (S) |
| jev-router-harness | Ink/React TUI on Vercel Eve; Jev routes tasks to free/budget/premium models (model names listed are old: Gemini 2.5 Flash, Claude 3.5 Sonnet…); state `.jev/memory.json` | mjmiller41 | MIT | pnpm install/build | undated | TUI + `pnpm start "prompt"` / `--dry-run` | Yes (hobby) | https://github.com/mjmiller41/jev-router-harness | M (S) |
| Astro-Han/jev-harness | minimal Python agent; Jev filters tool results before main model (DeepSeek-Flash); JSONL logs `--log run-on.jsonl`, `.jev-store/<call_id>.txt` | Astro-Han | Apache-2.0 | `uv run jev_agent.py` | "closed prototype" as of 2026-09-22 | headless only | Yes (research prototype, dead) | https://github.com/Astro-Han/jev-harness | M (S) |
| jev-guard | security hook layer ("auto mode for every agent"): scores every tool call allow/ask/deny with Jev | leepokai | MIT | plugin per agent; Node ≥20.3 | 26 commits | hook, not agent | No | https://github.com/leepokai/jev-guard | M (S) |
| jev-gateway (vinilana / DevOtts) | npm wrapper; `jev-codex`, `jev-claude`, `jev-opencode` run stock agents with Jev tool-call reasoning | vinilana · DevOtts | not read | npm | not read | wrapper | No | https://github.com/vinilana/jev-gateway | L-M |
| codex-jev | "research fork of OpenAI Codex" by CompleteTech LLC AI Research; README appears to be stock Codex README + AGENTS.md; Jev integration mechanics NOT visible | CompleteTech-LLC-AI-Research | Apache-2.0 | stock Codex channels | none visible | Codex TUI + app-server | Yes but = Codex fork | https://github.com/CompleteTech-LLC-AI-Research/codex-jev | L (S) |
| pi-jev / local-jev skill / gist (pedramamini) | agent skills/extensions calling Jev from Claude Code, Codex, OpenCode, pi | various | — | — | — | — | No | https://pi.dev/packages/pi-jev · https://gist.github.com/pedramamini/014676fa8684d91bf7000f4623701ada | L |

**Most plausible reading for "a terminal coding agent called jev in 2026": none exists as a first-party product.** Order of plausibility for what majkee means: (1) the `jev` binary (jev-cli) or a zsh plugin — "accessible via zsh" — used as a role inside his own UI+harness; (2) jevdev (if he is literally using a Jev-based coding harness). Do not treat any as settled. Question for majkee: which artefact do you run — `which jev`, or a repo path?

## 2 · Catalogue (a–f) — answered for the Jev family

### a. Hook / lifecycle events

| Surface | Events | Config | Doc'd? | Conf |
|---|---|---|---|---|
| Jev model / API | none — stateless request/response | — | n/a | M |
| jev-cli | none. Only process exit codes: 0 ok · 2 validation · 3 auth · 10 condition false · 11 abstain band | env `TYPESAFE_API_KEY` or 0600 credentials file | README (S) | M |
| jev-guard (a consumer, not emitter) | rides HOST agents' hooks: CC `UserPromptSubmit`+`PreToolUse`; Codex `BeforeTool` (name as reported — differs from catalogue's Codex `PreToolUse`; unverified); Copilot `PreToolUse`; Gemini `BeforeAgent`; Cursor `preToolUse`; ACP proxy `jev-guard acp -- <agent>` intercepting `terminal/create`, `fs/write_text_file` | `~/.jev-guard/config.json` | README (S) | M |
| jevdev | internal decisions per turn (context/cache/route/tool/permission); no hook API found | `.jevdev/exec.cedar`, `AGENTS.md` | README (S) | L-M |

**Net: no hook/lifecycle event vocabulary exists for "jev".** The jev-guard ACP finding is useful independently: a proxy can sit on an ACP stdio pipe and see `terminal/create` — a push/observation door for ACP agents.

### b. On-disk session record

| Artefact | Path | Format | Doc'd vs observed | Conf |
|---|---|---|---|---|
| jev-cli | none found (batch: "resumable" — state file path not read) | — | — | L |
| jevdev | `.jevdev/state.redb` (immutable chunk log, blake3-addressed); `.jevdev/progress.md` | redb binary + md | README | M |
| jev-router-harness | `.jev/memory.json` | JSON, atomic temp-rename | README | M |
| jev-harness (Astro-Han) | `.jev-store/<call_id>.txt`; `--log run-on.jsonl` | JSONL | README | M |
| jev-guard | `~/.jev-guard/sessions/`, `scan-cache.json`; README also says nothing is logged | per-session ctx files | README (contradictory wording) | L-M |

All are project-local, harness-specific, third-party. No common schema.

### c. Headless / structured output

| Mode | Shape | Source | Conf |
|---|---|---|---|
| jev-cli | stdout tables or JSON; stderr diagnostics; exit-code-as-answer (10 false, 11 abstain); `batch run` JSON/CSV rows, `--input-format json`, `--merge` (v0.2.0) | https://github.com/shaharia-lab/jev-cli | M (S) |
| API | typed JSON: noul prob 0–1; choice (≤255 options) with confidences; score (2–10 levels) distribution | https://flaviocopes.com/jev/ | M (S) |
| jevdev | `jevdev run --yes` (output format unknown) | repo | L |

### d. Push / wake doors

| Door | Status | Conf |
|---|---|---|
| MCP | `jev mcp serve` exposes tools (per-call spend caps, deny-by-default file access) — jev as a callee only | M |
| ACP | no jev ACP agent found; jev-guard proxies ACP pairs | M |
| Queue/remote control/channels | none found | L |

Nothing can wake or notify nablarva: Jev never initiates.

### e. Mapping onto the 20-event map

| State | Derivable without screen? | Why |
|---|---|---|
| working | n/a for the model/CLI (a `jev` call is a ~0.25–1 s child process; L0 sees spawn/exit = `process_spawned`/`process_exited` #9/#10) | one-shot |
| waiting | none (jev asks no approval) — only if a harness adds one | — |
| idle | n/a | — |
| exited | yes, L0 (SIGCHLD/wait4 + exit code; jev-cli exit code 10/11 carry the verdict) | kernel |

Events with a jev source: #9, #10 (L0), #2-like only via L0. All other 18 events: `—`. If majkee's harness invokes `jev` as a subprocess, then `tool_started/ended` for that call are just child-process events. If the "jev" he tests is **jevdev**: PTY/L0 fallback only (no hooks, no JSONL record; redb is binary and single-writer-locked — do not read live). Proposed row for the map: **`jev` = L0-only, "category: model-role, not session"**; the harness around it (majkee's own) is the event emitter and should speak the vendor-neutral vocabulary natively — that is the one case where nablarva can define the source side.

### f. Runs in a PTY like the others?

| Artefact | PTY? | Alt-screen / spinner | Conf |
|---|---|---|---|
| jev-cli | no TTY need; prints and exits | none | M |
| jev-shell-history | lives inside zsh ZLE; ghost text drawn on the prompt line; no alt-screen | none | M |
| jevdev | ratatui TUI → very probably alt-screen + raw mode (ratatui default; README does not say) ; spinner unreported | unverified | L |
| jev-router-harness | Ink/React TUI (Ink: no alt-screen by default; unverified) | unreported | L |

## 3 · Not found / unverified

- Any first-party TypeSafe coding agent or TUI named `jev` — none found (searched 2026-10-02; blog says nothing on coding agents).
- Which artefact majkee means — unknowable from the web; needs his answer.
- Announcement date conflict: 2026-09-15 vs 2026-09-28; blog says early access/waitlist while jev-cli shipped 09-19 (consistent with API open earlier than blog date). Unresolved.
- Primary TypeSafe docs (console.typesafe.ai / docs site) not fetched — API shape is from a secondary blog (flaviocopes.com) + search digest.
- jev-cli state-file path for resumable batch; jevdev alt-screen use; jevdev headless output format; jevdev licence/version tags beyond README.
- codex-jev: what, if anything, differs from upstream Codex (could carry Codex hooks verbatim, then Codex catalogue §2a applies).
- jev-guard's Codex `BeforeTool` naming vs the catalogue's 12 documented Codex events — unreconciled.
- jev-shell-history / jevdev / jev-router-harness repos judged from summaries only; star counts and commit dates unchecked.

Sections to refresh: [events-map §1 header "candidate `jev`" and §4 gap "jev: everything" · vendor tiers line; vendor-events catalogue (add a jev row: model-role, L0-only) · majkee's answer on which artefact]
