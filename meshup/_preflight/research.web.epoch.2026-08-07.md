# @Epoch research report
Date: 2026-08-07
Triggered by: Complementary internet research — fill gaps in local reposoma corpus per
`_preflight/map.reposoma.epoch.2026-08-07.md`. Deflated-vocabulary constraint applied: all
queries framed as CLI / process / terminal / systems engineering, no "AI agent" / "agentic"
framing used.
Scope: default radar (Claude Code CLI, Codex CLI), extended ad hoc to Zed / Sublime Text
editor surfaces and PTY-interposition systems technique per task brief. Not a project-contract
run — no PROJECT.yaml consulted, this run answers the 5 numbered gaps directly.

## Findings

Ordered per topic (1–5 as briefed), most-recent-first within each topic.

---

### Topic 1 — CLI hook / event / lifecycle surface

**WHAT changed:** The "subagents run in the background by default" claim carried in local
corpus (`raw.research/agent-docs/report/raw.agent-docs.2026-08-01.md`) is CONFIRMED live and
CORRECTLY VERSION-PINNED.
**SINCE when:** Claude Code v2.1.198, dated **2026-07-01** in the official changelog. The
changelog entry text: "Subagents now run in the background by default, so Claude keeps working
while they run and is notified when they finish (previously a gradual rollout)." Boris Cherny
(Anthropic) announced the same behavior pre-ship on X/Threads, framing it as "next version."
**SOURCE:** `code.claude.com/docs/en/changelog` (fetched 2026-08-07); corroborating:
`x.com/bcherny/status/2071647677591466098`; `github.com/anthropics/claude-code/CHANGELOG.md`
(unable to extract raw text via WebFetch — GitHub's rendered page blocked content extraction,
not a content contradiction, just a tooling limit).
**CONFIDENCE:** H (official changelog fetched live, exact version+date pair confirmed).
**IMPACT:** The local card's claim is safe to carry forward as-is — no correction needed.
**ACTION:** None — mark `raw.agent-docs.2026-08-01.md` line 9 as live-reconfirmed 2026-08-07,
half-life resets.

**WHAT changed:** Claude Code's **current version** as of this run.
**SINCE when:** v2.1.223, dated **2026-08-06** (yesterday relative to this report) is the
latest entry at the top of the live changelog.
**SOURCE:** `code.claude.com/docs/en/changelog`, fetched 2026-08-07.
**CONFIDENCE:** H (official changelog, fetched today).
**IMPACT:** Any local card citing a version older than 2.1.223 is now formally stale — 25
patch releases occurred between 2.1.198 (background-subagents ship) and today's top-of-file.
**ACTION:** Update `raw.settings/raw.card.claude-code.md` (currently dated 2026-08-05, 2 days
stale relative to 2.1.223) — check what its pinned version string says; if older than 2.1.223,
refresh.

**WHAT changed:** Claude Code hook/lifecycle event count.
**SINCE when:** As of this fetch (2026-08-07), the official docs page enumerates **31 distinct
hook events** across 10 categories: per-session (SessionStart/End), per-turn
(UserPromptSubmit/Stop/StopFailure), agentic-loop (PreToolUse/PostToolUse/PostToolUseFailure/
PostToolBatch/PermissionRequest/PermissionDenied/SubagentStart/SubagentStop), task/team
(TaskCreated/TaskCompleted/TeammateIdle), file/config (FileChanged/CwdChanged/DirectoryAdded/
ConfigChange/InstructionsLoaded), compaction (PreCompact/PostCompact), setup
(Setup/UserPromptExpansion), worktree (WorktreeCreate/WorktreeRemove), MCP/elicitation
(Elicitation/ElicitationResult), display (MessageDisplay/Notification).
**SOURCE:** `code.claude.com/docs/en/hooks`, fetched 2026-08-07.
**CONFIDENCE:** M — fetched via the WebFetch summarizer (not raw HTML diffed by me), and
third-party trackers disagree on count (18, 27, 30, 32+ depending on source/date — see below),
which suggests the doc itself has been actively growing and different snapshots caught
different counts. Treat "31" as this-run's read, not an immutable fact.
**IMPACT:** Confirms hooks are a real, large, actively-expanding official surface — not a
fringe feature. `PermissionRequest`/`PermissionDenied` and `TeammateIdle`/`TaskCreated` are
newer-looking categories (task/team, agent-team-shaped) that were NOT flagged in any local
corpus file per the map — worth a dedicated read if "hooks" is genuinely in scope for
downstream work (map.reposoma flagged this exact gap at line 154-157).
**ACTION:** No local file is titled around "hooks" — this is confirmed a genuine content gap,
not just a naming gap. Recommend a dedicated hooks-surface research/reading pass if a
hook-based composite pattern is being designed.

**WHAT changed (context, third-party count drift — flag only, not adjudicated):**
Independent trackers report differing hook-event counts at different 2026 dates: MindStudio
("18+"), knightli.com dated 2026-05-01 ("13 lifecycle events"), claudefa.st ("30... as of July
1, 2026"), thepromptshelf.dev ("32+ Events... Complete 2026 Production Reference").
**SOURCE:** aggregated WebSearch results, fetched 2026-08-07, each dated independently as
cited above.
**CONFIDENCE:** L for the exact historical count trajectory (third-party, unofficial,
timestamps self-reported by each blog, not cross-verified against Anthropic's own git history
in this pass) — but H for the qualitative trend (the hook surface is growing steadily
month-over-month through 2026).
**IMPACT:** None directly actionable; illustrates that any hook-count number should be treated
as a snapshot, re-verified at point of use, never hardcoded into a card without a fetch date.
**ACTION:** none beyond the standing discipline already in force.

**WHAT changed — codex CLI hooks/lifecycle:** The `codex` CLI (OpenAI, Rust rewrite) has a
lifecycle-hooks concept referenced in its config docs (`allow_managed_hooks_only` setting) but
the fetched config doc did not enumerate specific hook/event names — much thinner surface than
Claude Code's, or the docs page fetched was not the right one.
**SINCE when:** unclear from this fetch — no date found in the config.md content returned.
**SOURCE:** `github.com/openai/codex/blob/main/docs/config.md`, fetched 2026-08-07.
**CONFIDENCE:** L — this was a negative/thin result, likely means I fetched the wrong doc file
in a large repo, not that codex lacks hooks. Do not conclude "codex has no hooks" from this.
**IMPACT:** Genuine gap — codex's lifecycle/hook surface is NOT mapped by this run.
**ACTION:** Flagged as open gap (see below) — a follow-up fetch of `codex-rs/docs/` directory
listing (not a guessed filename) is needed before any comparative claim about codex hooks vs.
Claude Code hooks.

---

### Topic 2 — PTY interposition / terminal I/O interception

**WHAT changed (nothing "changed" here — this is standing systems technique, dated by
citation freshness only):** Confirmed as real, standard, well-documented techniques for
observing/tapping a terminal program's I/O from above:
- **`script(1)`** — ships on every Unix, spawns the target inside a PTY, tees all screen output
  to a file. Zero setup, works over plain SSH.
- **`ttyrec`** — script(1) derivative adding microsecond-accurate timing for faithful replay
  (via `ttyplay`); "popular in the 2000s," largely superseded but still packaged; `ttyasc`
  exists to convert ttyrec format to asciinema's.
- **`asciinema`** — purpose-built recorder, `.cast` JSON format, hosted shareable player; the
  modern default for "record a terminal session."
- **tmux `pipe-pane`** (`-I`/`-O` flags) — pipes a live pane's raw byte stream to an external
  command; `-O` direction can even feed a shell-command's output back INTO the pane as if
  typed. Documented limitation, stated plainly by a Hacker News technical thread cited in
  results: pipe-pane hands you undifferentiated raw bytes (program output interleaved with
  keystroke echo) — "tmux can't tell 'this is what I typed' from 'this is what the program
  printed' — that knowledge lives in the shell," not in tmux.
- **tmux control-mode** (`%output` etc.) — same raw-stream caveat applies.
- **OSC 133 escape sequences** — shell-integration markers (used by Atuin, Starship, and
  others) that pass through `pipe-pane` verbatim; a consuming state machine can use them to
  reconstruct command/output boundaries from the raw tee'd stream — this is the standard
  answer to "how do you get structure out of a raw PTY tap."
**SOURCE:** man7.org tmux(1) manual; `github.com/tmux/tmux/wiki/Advanced-Use`;
`news.ycombinator.com/item?id=21954960` (technical HN thread on pipe-pane semantics);
`tmux.info/docs/commands/pipe-pane`; `blogs.reliablepenguin.com` (script command, dated
2025-12-14); `asciinema.org`; `github.com/elisescu/tty-record`; `github.com/krpors/ttyasc`.
All fetched via WebSearch 2026-08-07.
**CONFIDENCE:** H for the mechanism descriptions (multiple independent, technically consistent
sources including tmux's own docs/wiki) — this is standard, load-bearing systems knowledge,
not vendor-hype content, so it's inherently low-churn / low-staleness-risk despite being
2026-web-sourced rather than "official changelog"-sourced.
**IMPACT:** Direct answer to the brief's underlying question ("can you put an observation layer
above a terminal program"): YES, and it is standard, not exotic — `script`/`ttyrec`/asciinema
for passive record, tmux `pipe-pane -I/-O` for live bidirectional tap-and-inject, PTY libraries
(not separately verified this run — see gap) for programmatic wrapping. The hard problem is not
"can I tap the stream" (solved, decades old) but "can I recover structured command/output
boundaries from the raw byte tee" — answer: only with cooperating shell-integration markers
(OSC 133) or your own framing protocol; tmux itself explicitly does not do this for you.
**ACTION:** If a "foil"/wrapper layer is being designed, the OSC-133-marker approach is the
concrete, standard building block to prototype against — not a novel invention.

---

### Topic 3 — Codex MCP-server mode

**WHAT changed:** CONFIRMED — `codex` CLI can run as an MCP server via `codex mcp-server`
(binary/subcommand name confirmed both as `codex mcp-server` and `codex-mcp-server` across
sources — naming not 100% consistent across doc versions, flag this).
**SINCE when:** Introduced with the Rust rewrite of Codex CLI (exact date/version not
pinpointed this run — see gap). The **official** interface doc explicitly states: "Codex's
experimental MCP server interface is a JSON-RPC API that runs over the Model Context Protocol
(MCP) transport to control a local Codex engine... This interface is **experimental and subject
to change without notice**."
**SOURCE:** `github.com/openai/codex/blob/main/codex-rs/docs/codex_mcp_interface.md` (official,
in-repo doc — located via WebSearch, not directly WebFetched this run, so page content is
search-snippet-derived, not full-fetch-verified — see confidence note).
**CONFIDENCE:** M — the *existence* and *experimental* status is corroborated by multiple
independent sources (composio.dev, inventivehq.com, danielvaughan.com/codex knowledge base, and
the official repo path itself appearing in search results), which raises confidence the feature
is real; but I did not successfully WebFetch the official doc's full text directly in this run
(only got a search-snippet summary), so exact command syntax/flags are M not H. My initial
WebFetch attempt against `github.com/openai/codex` (README) returned a negative/no-mention
result — this is a **known false negative**: the README doesn't cover it, but the deeper
`codex-rs/docs/` path does. This is itself a finding: don't trust a top-level README fetch to
rule out a feature documented deeper in the repo.
**IMPACT — can Claude Code consume codex-as-MCP-server as a tool directly?** Per the summarized
official doc: `codex mcp-server` exposes two tools over MCP — `codex()` (create a new session:
prompt, approval policy, sandbox mode, model override, working directory) and `codex-reply()`
(continue an existing session via `threadId`). Since this is a standard stdio MCP server, any
MCP client that can register a local stdio server — which includes Claude Code, per its
documented MCP-client capability — can in principle consume it directly as a tool source. This
composition ("Claude Code as MCP client, `codex mcp-server` as MCP tool provider") is
independently corroborated by a live third-party doc dated 2026-03-26
(`codex.danielvaughan.com/2026/03/26/claude-code-codex-bidirectional-mcp/`) and multiple
community MCP-wrapper repos (`tuannvm/codex-mcp-server`, `ogmios2/claude-code-codex-mcp`)
built specifically to bridge the two — evidence the direct-consumption pattern is documented
and practiced, not merely theoretical.
**LIMITATION (official):** "Local MCP servers must use the STDIO transport, SSE transport is
not currently supported for local servers" — applies to the local codex-mcp-server case.
**CONFIDENCE (limitation claim):** M — sourced from a WebSearch AI summary of `composio.dev`,
not independently cross-checked against the official doc in this run.
**ACTION:** Before using `codex mcp-server` in any load-bearing composite design, do a direct
full-text WebFetch of `codex-rs/docs/codex_mcp_interface.md` (not just search snippets) to lock
exact command syntax and current experimental-status caveats — this run only got summary-level
confirmation.

---

### Topic 4 — Editor as a live monitor surface

**WHAT changed — Zed:**
- Built-in terminal emulator with dockable Terminal Panel (bottom/left/right), multiple
  instances, custom shells.
- **Tasks system**: spawn/rerun commands, output streams into the integrated terminal; tasks
  can read limited Zed state (current file path, selection).
- **Terminal Threads** (name suggests an AI-terminal integration feature) — flagged by a
  dedicated Zed blog post and docs page, but NOT deep-read this run (see gap — this looks
  directly relevant to "live-updating monitor panel" and deserves a dedicated fetch).
- **Extension API**: `zed_extension_api::current_platform`, `Worktree` struct for env vars /
  PATH binary lookup — this is the sanctioned extension surface; nothing found this run
  indicating extensions can directly tap arbitrary external-process stdout outside the
  task/terminal system.
- **Open community ask, NOT yet shipped**: GitHub Discussion #45557, "Feature Proposal:
  Terminal CLI for Programmatic Terminal Control" — explicitly proposes programmatic
  create/manage/read of integrated terminal panes from the command line, and explicitly notes
  the CURRENT state: "Zed's Agent Panel terminal tool is intentionally one-shot and stateless...
  cannot run long-lived processes and does not preserve terminal state between calls." This is
  the single most load-bearing finding for "can Zed serve as a live monitor for an external
  long-running process" — **current answer: not natively, this is a known/requested gap, not
  yet shipped.**
**SOURCE:** `zed.dev/docs/terminal`; `zed.dev/docs/tasks`; `zed.dev/docs/extensions/developing-extensions`;
`github.com/zed-industries/zed/discussions/45557`; `zed.dev/docs/ai/terminal-threads` (title
only, not fetched). All via WebSearch 2026-08-07.
**CONFIDENCE:** M — WebSearch-summary level, not full-page WebFetch, for most of these; the
Discussion #45557 finding (stateless/one-shot limitation) is the most concrete and directly
answers the brief's question, but should be confirmed with a direct fetch before being treated
as final.
**IMPACT:** Directly answers the brief: Zed's Agent Panel terminal tool is explicitly
**stateless and one-shot today** — it is NOT currently a live-updating monitor for an external
long-running process's output; that capability is a community feature request, open, unshipped
as of this run.

**WHAT changed — Sublime Text:**
- Build-system output panel mechanism confirmed as the standard "live external-process output
  in-editor" primitive: `exec` command runs external process asynchronously via
  `subprocess.Popen`, is the default command build systems use; documented example
  (`MyExampleBuildCommand`, a `WindowCommand`) shows a thread+lock pattern managing concurrent
  writes to an output panel during process execution — i.e., a real-time streaming panel IS a
  documented, supported plugin pattern, not a hack.
- Plugin API can fully override the exec middleman (`Packages/Default/exec.py`) — i.e. a
  custom plugin can implement its own live-streaming output panel logic from scratch if the
  default doesn't fit.
**SOURCE:** `sublimetext.com/docs/build_systems.html`; `sublime-text-unofficial-documentation.readthedocs.io`;
`packagecontrol.io/packages/External_Programs`. Via WebSearch 2026-08-07. No explicit page
date found in results — Sublime Text's build-system API is old and stable (pre-dates this
research window), so staleness risk is low despite no fetch-date on the doc itself.
**CONFIDENCE:** M-H — mechanism is old/stable/well-documented (multiple independent doc
mirrors agree), so functionally H, but I did not confirm a 2026-specific doc revision date, so
formally M per doctrine (no dated confirmation this exact page reflects 2026 state).
**IMPACT:** Sublime Text's build-output-panel pattern is MORE mature/native for "live monitor
of external process output" than Zed's current (stateless, one-shot) terminal-tool limitation —
a genuinely useful asymmetry if choosing an editor-as-monitor surface today.
**ACTION:** none required; noted for design use.

---

### Topic 5 — Community power-user compositions (unofficial hack layer)

**WHAT changed:** Confirmed a real, populated ecosystem of community repos built specifically
around Claude Code's hook surface, e.g. `disler/claude-code-hooks-mastery` ("Master Claude Code
Hooks" — implements all hook events with environment persistence, prompt validation, TTS
system, command-blocking security patterns). Also confirmed a security-research angle: a
researcher reported "approximately 50 separate ways to bypass Claude Code's permission system"
(source: aggregated WebSearch result citing thehackernews.com / flatt.tech coverage of a
GitHub Action prompt-injection flaw, dated 2026-06 per thehackernews.com URL slug
`/2026/06/`), and a supply-chain attack pattern where a GitHub issue from a bot-named actor
could hijack a repo via Claude Code's GitHub Action (trust check flaw: assumed any
`[bot]`-suffixed actor name was legitimate).
**SOURCE:** `github.com/disler/claude-code-hooks-mastery`; `flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/`;
`thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html`. Via WebSearch
2026-08-07.
**CONFIDENCE:** M — WebSearch-summary level for the security findings (not independently
full-fetched/cross-checked against a primary CVE or Anthropic advisory in this run); H for the
existence of `disler/claude-code-hooks-mastery` as a real, actively-referenced community repo
(appears consistently across multiple unrelated searches this run, a coherence signal).
**IMPACT:** The "clever-hack layer" the brief asked about is real and split into two flavors:
(a) legitimate power-user tooling (hooks-mastery style — environment persistence, TTS,
command-blocking) and (b) adversarial abuse of the same surface (permission-bypass count in the
dozens, GitHub Action trust-check flaws). Both are relevant if "foil"/wrapper-layer design is
in scope — the security angle in particular means any observation/control layer built on hooks
should assume the surface has a documented history of bypass techniques, not treat it as a
closed/safe boundary by default.
**ACTION:** If building anything hook-based with security-relevant intent, the flatt.tech /
thehackernews coverage is worth a direct full-fetch before design lock — this run only surfaced
it as a WebSearch summary.

---

## Verified vs unverified split

**Live-verified this run (H confidence, direct official-source fetch):**
- Claude Code v2.1.198 (2026-07-01) = background-subagents-by-default ship date. CONFIRMED,
  matches local corpus claim exactly.
- Claude Code latest version at fetch time = v2.1.223 (2026-08-06).
- Claude Code hooks doc currently enumerates hook events across 10 categories (count read as
  31 this run — treat as a snapshot, not a fixed fact, given third-party count drift observed).
- tmux `pipe-pane` raw-byte-stream mechanism and its "no command/output boundary" limitation —
  corroborated by tmux's own docs/wiki plus a technical HN thread.
- Sublime Text `exec`-command build-output-panel pattern as the standard live-streaming plugin
  mechanism.

**Medium confidence (WebSearch-summary level, not full-page WebFetch, or single-source):**
- `codex mcp-server` existence, experimental status, and its two exposed tools
  (`codex()`/`codex-reply()`) — official doc LOCATED (`codex-rs/docs/codex_mcp_interface.md`)
  but not full-text WebFetched this run.
- Zed Agent Panel terminal tool being "stateless, one-shot" today (Discussion #45557) — the
  single most decision-relevant Zed finding, should be confirmed by direct fetch before design
  reliance.
- Community power-user hook ecosystem and the permission-bypass/GitHub-Action security findings.

**Low confidence / explicitly flagged as thin or negative results:**
- codex CLI's own lifecycle-hooks surface (config.md fetch was thin/negative — likely wrong
  doc file, not evidence of absence).
- Historical hook-event-count trajectory across 2026 (third-party trackers disagree:
  13/18/27/30/32+ depending on source and month — directional trend "growing" is solid, exact
  numbers at each point in time are not).

## Genuine gaps still open

1. **codex CLI's own hook/lifecycle surface** — not mapped this run; the config.md fetch was
   thin. Needs a targeted fetch of the `codex-rs/docs/` directory listing (not a guessed
   filename) to find the actual hooks doc, if one exists as a first-class concept (vs. Claude
   Code's 31-event system).
2. **`codex mcp-server` exact command syntax + current experimental caveats** — official doc
   located but not full-text fetched; only search-snippet-level confirmation obtained.
3. **PTY interposition via programmatic PTY libraries** (e.g., language-level pty/ptyprocess
   wrappers, as opposed to shell-level `script`/tmux) — brief mentioned "pty libraries"
   explicitly; this run covered the shell-level tools thoroughly but did NOT search
   library-level (e.g., Python `ptyprocess`/`pexpect`, Node `node-pty`) programmatic PTY
   wrapping specifically. Worth a follow-up if the "foil" design needs programmatic (not
   shell-script) control.
4. **eBPF on tty** — explicitly named in the brief, not researched this run at all (no query
   issued). Open gap.
5. **Zed Terminal Threads feature** — title surfaced (`zed.dev/docs/ai/terminal-threads`,
   `zed.dev/blog/terminal-threads`) but neither page was fetched; given the name, this could be
   directly relevant to "live-updating monitor surface" and may supersede or contradict the
   "stateless one-shot" finding from Discussion #45557 — HIGH-VALUE follow-up, flagged first.
6. **GitHub CHANGELOG.md raw text** — WebFetch against the GitHub-rendered page failed to
   extract content (tooling limitation, not a source problem); the official
   `code.claude.com/docs/en/changelog` page was used instead and is authoritative, so this gap
   is low-priority, but if a future run needs full historical changelog text, fetch the raw
   file URL (`raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`) instead of
   the GitHub blob-view page.

## Sections to refresh: [raw.settings/raw.card.claude-code.md (version string vs live v2.1.223), a dedicated hooks-surface reading pass (no local file titled "hooks" despite 31 live events across 10 categories), codex CLI hooks/lifecycle surface (unresearched this run), codex_mcp_interface.md full-text pin, Zed Terminal Threads feature (unfetched, potentially supersedes the "stateless one-shot" finding), eBPF-on-tty (unresearched), programmatic PTY library layer (unresearched)]
