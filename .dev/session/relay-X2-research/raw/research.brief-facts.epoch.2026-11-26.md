# Brief fact check — @Epoch
Who: @Epoch (researcher). Date/access date: 2026-11-26. Method: live web fetch and search only, primary sources first (vendor docs, GitHub release pages, vendor blog); no repository files read; no private data in queries. Page-reported dates without a year are flagged.

## 1. Current official names
- Claude Code: still the name. code.claude.com/docs/en/changelog titled "Claude Code changelog" (accessed 2026-11-26). H.
- Codex CLI: still the name. learn.chatgpt.com/docs/codex/cli (redirected from developers.openai.com/codex/cli; page heading "Codex CLI", banner "OpenAI Codex"; accessed 2026-11-26). H. Note: docs host moved.
- Antigravity CLI: shipped under that name since 2026-05-19 (Google Developers Blog, same date). Command `agy`: not named on the blog page, but the Gemini CLI GitHub README (accessed 2026-11-26) refers to "Antigravity CLI (`agy`)"; search results agree. H for the name, M-H for `agy`.

## 2. Gemini CLI status
Claim correct. Google blog (2026-05-19, developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/): on 2026-06-18 Gemini CLI stops serving AI Pro/Ultra and free Code Assist for individuals; GitHub app: no new installs, existing stops in following weeks. Gemini CLI README (accessed 2026-11-26): still alive, but enterprise-oriented (Code Assist Standard/Enterprise, Code Assist for GitHub, legacy paid API/Vertex keys), "not optimized for Gemini 4+", recommends `agy`. Not retired, not enterprise-only strictly (paid API keys too). "Google's successor to Gemini CLI" is still accurate: blog calls it the successor; README still points to it. Confidence H.

## 3. Current stable versions
- Claude Code 2.1.332 — 2026-11-25 (code.claude.com changelog; GitHub releases agrees: "25 Nov"). H.
- Codex CLI 0.172.0 — 2026-11-24 (github.com/openai/codex/releases, "Latest"). H.
- Antigravity CLI v1.5.16 — 2026-11-24 (antigravity.google/docs/changelog; v1.5.15 on 11-23). H. Not labelled "Latest" on the page; newest listed. (Antigravity App is a separate product, v2.35.2.)
- For completeness: Gemini CLI v0.71.1 — "24 Nov" (GitHub releases, year not shown; preview v0.72.0 exists). M.

## 4. Other stale facts in the sentence
- "Interactive CLI coding agents from three vendors" remains true, but Gemini-side vendor facts: Antigravity CLI is available to everyone only since 2026-05-19, so the brief's "three vendors" holds.
- Minor: Codex docs now live at learn.chatgpt.com (old developers.openai.com path 308-redirects) — update any cited URL.
- Antigravity CLI's single-clause "successor to Gemini CLI" omits that Gemini CLI persists for enterprise. Optional refinement.
- Tmux, workstation and Tailscale parts are operator facts, not checkable from public sources: not settled / out of scope.
