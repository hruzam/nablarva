# check.hcom — bounded web check of aannoo/hcom
Date: 2026-11-27. Web reading only; nothing posted. All reads were through WebFetch, which returns a model summary of the page, not raw text. So every "read" below is "read through a summary" unless it says otherwise. Repo reached: github.com/aannoo/hcom (OK). Mintlify docs page: HTTP 410 Gone, not read.

## 1. Licence (confidence: high on MIT, medium on "no other terms")
- LICENSE at raw.githubusercontent.com/aannoo/hcom/main/LICENSE: "MIT License", "Copyright (c) 2025 aannoo". SPDX: MIT. Read via summary, fetched 2026-11-27.
- Additional terms: none seen (only notice-keep and warranty disclaimer). No CLA, no commons clause seen. Not found: any explicit statement that none exist.
- History: CHANGELOG 0.6.9 entry says MIT licence was added (so earlier versions may have had no licence). No later change seen in 0.7.26 to 0.7.31 entries. Full git history of LICENSE not read.
- Bundled dependencies' licences: NOT checked. It has Cargo.toml, pyproject.toml, package.json, so a licence audit of dependencies is a review task.
- What MIT allows: use as-is, copy code or tests into a private repository, modify, even redistribute. Condition: keep the copyright and permission notice in copies or substantial portions. Copying its tests is permitted on the same terms.

## 2. Vitality (confidence: medium)
- Latest release 0.7.31, 21 Oct 2026 (releases page, summary). That is about 5 weeks before today, with nothing newer seen.
- Cadence: 0.7.22 (22 Jun), 0.7.23 (6 Jul), 0.7.24 (26 Jul), 0.7.25 (9 Aug), then 0.7.26 (26 Sep), 0.7.27 (1 Oct), 0.7.28 (6 Oct), 0.7.29 (12 Oct), 0.7.30 (15 Oct), 0.7.31 (21 Oct). Slow in Aug-Sep, bursts of 5-6 days in Oct. Issues are still being filed through 24 Nov, but no release since 21 Oct.
- Maintainers/contributors: NOT found (contributors page did not load; repo page gave no count). Looks like a single-author project (copyright "aannoo") but that is inference.
- Open issues: 28; open PRs: 18 (repo page, summary).
- Recent issues worth noting (issues page, summary):
  - #198 (24 Nov) `listen` redirected to /dev/null silently consumes unread messages (data-loss class).
  - #192 (10 Nov) idle sessions write about 8 GB/day from per-second heartbeats.
  - #182 (31 Oct) reaper kills live instances when hcom runs in a separate PID namespace, e.g. a Codex sandbox on Linux.
  - #181 (28 Oct) `hcom config <relay key> --info` prints the relay pre-shared key in clear (security).
  - #176 (23 Oct) Claude shown as listening while the rate-limit menu is open, so messages stay unread.
  - #194 and #193 (23 Nov) breakage after Antigravity CLI 1.5.14 and OpenCode 2 updates (not Claude or Codex).
  - #155 (11 Oct) Windows Smart App Control blocks the unsigned hcom.exe.
- Release notes show repeated Codex delivery/status fixes (0.7.26 to 0.7.31): sign of active tracking of Codex changes, and of fragility.

## 3. Install and footprint (confidence: medium-low)
- Language: Rust is the core (CI runs cargo, clippy, MSRV 1.89, tests in .rs files); also Python packaging (pyproject.toml), a Node/TypeScript part (typecheck job, plugin tests). Inferred from CI and the file list.
- Install: `uv tool install hcom`; `brew install aannoo/hcom/hcom`; install script (macOS, Linux, Android); PowerShell script (Windows). 0.7.31 dropped ephemeral `uvx hcom`: hooks need a persistent `hcom` on PATH (breaking change).
- Config it writes: README does not say. Changelog says hooks "moved to each launch" for several tools (0.7.27), and `HCOM_DIR` isolates hcom state (0.7.28). User config lives at ~/.hcom/config.toml and ~/.hcom/env. Exactly which Claude/Codex settings files it edits: NOT found. This is a first thing to read in a deeper review.
- Wrapper or attach: README says hooks activate only when an agent is launched with `hcom` in front (wrapper owns the terminal, PTY). Existing sessions can be resumed or forked through hcom (`hcom r`, `hcom f`). Tools without hooks can join with `hcom start` from inside, or poll with `hcom listen`. Attaching to an already-running native session for automatic delivery: not described.
- Daemon: README does not say. There is a background-pty headless mode, a reaper process (issue #182), per-second heartbeats (#192), and an optional MQTT relay for cross-device. A persistent daemon is not confirmed either way.

## 4. Tests (confidence: medium-high on existence, low on behaviour depth)
- tests/ (repo tree, summary; list may be partial): real_tool_claude.rs, real_tool_codex.rs, real_tool_hermes.rs, send_delivery.rs, test_pty_delivery.rs, pty_backpressure.rs, test_relay_roundtrip.rs, plugin_delivery.test.ts, cli_smoke.rs, uvx_install.rs, bundled_scripts.rs, support/.
- Real binaries: yes. scripts/mock-tools.pins (raw file, summary) pins `@openai/codex@0.162.1` and `@anthropic-ai/claude-code@2.1.296`. This matches the blind review's numbers. The pins file also states Claude minimums: 2.1.198 (prompt_id, background Agent/Task) and 2.1.286 (native delivery).
- CI: .github/workflows/ci.yml (summary). Runs on every push and PR; jobs: rust-tests, msrv, windows-build, typecheck, dist-check, and real-tool-tests (Codex, Claude, relay round-trip; Ubuntu and Windows; Codex under a bubblewrap sandbox). Real tests are `#[ignore]`d and run only in that job. Actions pinned to commit SHAs. Public.
- Is CI green: NOT checked (no Actions run page read).
- tests/real_tool_codex.rs (raw file, summary), three tests:
  - `real_codex_full_lifecycle_send_fork_kill_resume_and_cleanup`: delegates to a shared runner; send likely covers idle delivery but the file does not say so.
  - `real_codex_approval_gate_blocks_pending_message_then_clears_on_approval`: message sent while an approval prompt is open stays queued (unread_count 1, status `blocked(pty:approval)`); after approval it is delivered (unread_count 0). This is the approval-prompt case, covered with a real Codex.
  - `real_codex_argument_overrides_survive_resume_resume_fork_resume`: arguments only.
- Idle delivery: exists via lifecycle test and send_delivery/test_pty_delivery (names only; contents unread).
- Read acknowledgement by the recipient: no dedicated test found. Closest is unread_count dropping to 0 on delivery, which is a store counter, not proof the model read it. real_tool_claude.rs not read.

## 5. Codex path (confidence: low-medium)
- Mechanism is not stated in README or CHANGELOG. Evidence points to terminal reading by the wrapper, not a vendor interface: status string `blocked(pty:approval)` in the test; changelog items on telling Codex placeholder text from typed input, "not ready" during startup or update screens, messages stuck behind an answered approval "while the screen kept redrawing (/voice)"; test_pty_delivery and pty_backpressure files. So: idle/approval likely inferred from the PTY screen (plus hooks for activity); text likely typed into the terminal by the wrapper. This is inference; source code not read.
- Not found: whether Codex `notify` or any app-server interface is used.
- Fragility signal: each Codex update has needed fixes (0.157 startup waits, update screen, approval status).

## 6. Comparator: Agent Deck (confidence: medium on licence, low on version)
- github.com/asheshgoplani/agent-deck (repo page, summary): MIT. "Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more." Version v1.16.40 not verified; release page not read.

## Bottom line for the decision
- Licence is permissive (MIT); reuse of code and tests in a private repository is allowed with the notice kept. Dependency licences still unchecked.
- Worth a review for its real-binary Codex tests (including approval-pending delivery) pinned to the versions the blind review named.
- Cautions: Codex handling probably relies on terminal screen reading (brittle across Codex updates); it needs its wrapper launch; open issue about silent message loss (#198); no ack test; maintainer count unknown; no release in 5 weeks.
