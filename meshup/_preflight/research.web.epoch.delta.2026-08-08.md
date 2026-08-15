# @Epoch research report — bounded verification pass (delta)
Date: 2026-08-08
Triggered by: Bounded verification pass against prior baseline
`_preflight/research.web.epoch.2026-08-07.md` — three specific surfaces named in the brief:
Claude Code background-session subcommands, Stop/SubagentStop hook payload fields, Codex CLI
hooks status/config. Rule in force: anything not confirmable against a live source this run is
explicitly flagged "CONVERT TO OPEN QUESTION" rather than asserted.
Scope: default radar, narrow/bounded — 3 named surfaces only, not a full radar sweep.

## Findings

### Surface 1 — Claude Code background-session subcommands

**VERDICT: CONFIRMED**

**WHAT changed:** All five named subcommands exist and are documented on the official CLI
reference page, plus additional related commands not named in the brief (`claude rm`,
`claude daemon status`, `claude daemon stop`).

**Exact current syntax (as fetched):**
- `claude agents` — list background sessions; flags: `--cwd <path>`, `--json`, `--all`,
  `--permission-mode`, `--model`, `--effort`, `--agent`, `--settings`, `--add-dir`,
  `--plugin-dir`, `--mcp-config`. Example: `claude agents --json` (prints active sessions as a
  JSON array for scripting; `--all` includes completed sessions).
- `claude attach <id>` — attach a background session to the terminal. Example:
  `claude attach 7c5dcf5d`.
- `claude logs <id>` — tail/view a background session's recent output. Example:
  `claude logs 7c5dcf5d`.
- `claude respawn <id>` — respawn (keeps the conversation), with `--all` flag. Example:
  `claude respawn 7c5dcf5d`.
- `claude stop <id>` — stop a background session; alias `claude kill`. Example:
  `claude stop 7c5dcf5d`.
- Related, not named in the brief but present on the same page: `claude rm <id>` (remove a
  session record), `claude daemon status` (supervisor state/version/worker count),
  `claude daemon stop --any [--keep-workers]`.
- A session is started as background via `--bg`/`--background` on any invocation, e.g.
  `claude --bg "investigate the flaky test"`.

**SOURCE:** `code.claude.com/docs/en/cli-reference`, fetched live 2026-08-08 (WebFetch,
official docs domain).
**CONFIDENCE:** H — official docs page, fetched directly this run (not a search-snippet
summary), full exact-syntax table extracted including flag lists and worked examples.
**IMPACT:** All five commands named in the brief are real and current; no correction needed to
the baseline pass's PTY/background-session framing.
**ACTION:** None. This surface is safe to cite as-is with today's date (2026-08-08) attached.

---

### Surface 2 — Claude Code `Stop` / `SubagentStop` hook payload fields

**VERDICT: CONFIRMED**

**WHAT changed:** Both `session_id` and `cwd` and `transcript_path` and `last_assistant_message`
are documented Stop-hook input fields, and `SubagentStop` is confirmed to carry
`last_assistant_message` as well (the subagent's final response) — exactly as the brief asked.

**Exact fields documented for `Stop` (and identically for `SubagentStop`):**
`session_id`, `prompt_id`, `transcript_path`, `cwd`, `permission_mode`, `effort`,
`hook_event_name`, `agent_id` (present when running with `--agent` or inside a subagent),
`agent_type` (same condition), `last_assistant_message`, `stop_hook_active`.

Documented behavior notes captured verbatim from the fetch:
- "For `Stop` and `SubagentStop`, when you resume with `--continue` or `--resume`, Claude Code
  replays the saved text rather than re-running the hook for past turns."
- "For subagents, `Stop` hooks are automatically converted to `SubagentStop` since that is the
  event that fires when a subagent completes."

**SOURCE:** `code.claude.com/docs/en/hooks`, fetched live 2026-08-08 (WebFetch, official docs
domain).
**CONFIDENCE:** H for the field-list existence and names (fetched directly from the official
hooks reference page this run). **M** on completeness — the fetch tool itself noted: "the page
content provided does not include explicit example JSON payloads for Stop or SubagentStop
events," meaning the field list was reconstructed from prose/section references rather than
a literal example-JSON block being quoted verbatim. Treat the field *names* as H-confidence,
but flag that no raw example-JSON snippet was captured this run to cross-check field ordering
or confirm no fields were missed.
**IMPACT:** Baseline's implicit assumption (fields exist, SubagentStop carries subagent's final
response) is CONFIRMED, not just plausible.
**ACTION:** If a downstream design needs to parse the literal JSON shape byte-for-byte (e.g. to
write a strict schema), do one more direct fetch specifically hunting the example-payload code
block on the same page (WebFetch summarization likely dropped the raw JSON fence) — not a full
re-verification, just an extraction-completeness follow-up.

---

### Surface 3 — Codex CLI hooks status and config surface

**VERDICT: CONFIRMED (existence, structure, config surface) / UNCERTAIN (explicit
experimental-vs-stable labeling)**

**WHAT changed relative to baseline:** The 2026-08-07 baseline pass had this as a near-total gap
("thin/negative result... likely fetched the wrong doc file"). This run located and fetched the
correct, current official page and can now report substantive content.

**Current config surface (as fetched):**
- File locations: `~/.codex/hooks.json`, `~/.codex/config.toml` (inline `[hooks]` tables),
  `<repo>/.codex/hooks.json`, `<repo>/.codex/config.toml`.
- Structure, quoted: "Hooks are organized in three levels: A hook event such as PreToolUse,
  PostToolUse, PreCompact, SubagentStart, or Stop; A matcher group that decides when that event
  matches; One or more hook handlers that run when the matcher group matches."
- Event names documented: `SessionStart`, `SessionEnd`, `SubagentStart`, `PreToolUse`,
  `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
  `SubagentStop`, `Stop`. (Note: this is 11 named events — much thinner than Claude Code's
  31-event surface per baseline, but a real, structured, multi-event system, not the near-empty
  result baseline reported.)
- Matcher syntax, quoted: "The matcher field is a regex string that filters when hooks fire. Use
  `*`, `\"\"`, or omit matcher entirely to match every occurrence." Examples: `Bash`,
  `^apply_patch$`, `startup|resume|clear|compact`.
- Trust/safety gate: "Before a non-managed command hook can run, Codex requires you to review
  and trust the exact hook definition, and it records trust against the hook's current hash so
  new or changed hooks are marked for review and skipped until trusted" (from a companion
  `hooks/list` command doc, corroborating source).

**Status labeling — UNCERTAIN, converting to open question:** The fetched Hooks page does NOT
carry an explicit "experimental" / "beta" / "stable" banner or label in the content extracted
this run. A companion search surfaced that Codex's `dynamicTools` field (a different, unrelated
feature) is explicitly labeled experimental, which is a false-lead risk — do not conflate that
with hooks' own status. No page fetched this run contains a direct quotable sentence
classifying the *hooks framework itself* as experimental/stable.

**SOURCE:** `developers.openai.com/codex/hooks` (redirects live to
`learn.chatgpt.com/docs/hooks`, both fetched 2026-08-08); corroborating:
`developers.openai.com/codex/cli/reference`, `developers.openai.com/codex/changelog` (listed by
search, not independently fetched this run).
**CONFIDENCE:** M overall — H for structure/config-surface/event-names (directly fetched from
the current official page, not a search snippet), but the status question is genuinely
unresolved, not merely low-confidence.
**IMPACT:** Baseline's Topic-1 gap ("codex CLI's own hook/lifecycle surface — not mapped this
run") is now substantially closed for structure/config, but the experimental-vs-stable question
the brief specifically asked about is NOT closed.
**ACTION → CONVERT TO OPEN QUESTION:** "Is the Codex CLI hooks framework currently labeled
experimental, beta, or stable by OpenAI, and if so where exactly is that label stated?" Needs a
direct fetch of `developers.openai.com/codex/changelog` (to find the ship-date/status
announcement) and a full-page (non-summarized) read of the hooks page itself, since WebFetch
summarization may have dropped a status banner near the top of the page that a prose-extraction
pass would deprioritize.

---

## Verdict summary (compact)

| Surface | Verdict | Confidence | Source date |
|---|---|---|---|
| 1. Background-session subcommands (`agents`/`attach`/`logs`/`respawn`/`stop`) | CONFIRMED | H | fetched 2026-08-08, `code.claude.com/docs/en/cli-reference` |
| 2. Stop/SubagentStop payload fields (`last_assistant_message`, `session_id`, `cwd`, `transcript_path`) | CONFIRMED | H (fields) / M (raw-JSON completeness) | fetched 2026-08-08, `code.claude.com/docs/en/hooks` |
| 3a. Codex hooks existence + config surface | CONFIRMED | H | fetched 2026-08-08, `developers.openai.com/codex/hooks` |
| 3b. Codex hooks experimental-vs-stable status | UNCERTAIN | — | CONVERT TO OPEN QUESTION |

## Sections to refresh: [research.web.epoch.2026-08-07.md Topic 1's codex-hooks gap — now
partially closed (structure/config confirmed) but the experimental-status sub-question remains
open and should be re-flagged rather than assumed either way; Stop/SubagentStop hook field list
can now be cited with H confidence in downstream cards, replacing any prior "presumed" framing]
