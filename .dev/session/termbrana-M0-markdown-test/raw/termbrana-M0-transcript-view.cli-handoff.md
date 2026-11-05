# Termbrana M0 · Open a CLI session transcript at a pin

**From Wave to the CLI team · 2026-11-05 · research brief for Majkee**

Start with one operator action. I am in a native CLI session. Give me a path I can open in a new Sublime Text window at the exchange I am looking for. Let me read further back while the CLI carries on. If I encounter an old approval request, show what was actually observed and when. I make any decision in the native CLI.

## What we have to work from

I reviewed the repository at `hruzam/nablarva`, branch `core`, commit `132699a4276c2f7cb94755b9c70f5f5e76cd8f2d`. Repository reading was limited to `docs/` and the matching `.dev/session/termbrana-M0*` notes. The handwritten page supplies the operator scenario. Treat the design below as a proposal.

| Source | Constraint or observation to carry forward |
|---|---|
| [Architecture §§2–4 and organ index](https://github.com/hruzam/nablarva/blob/132699a4276c2f7cb94755b9c70f5f5e76cd8f2d/docs/ARCHITECTURE.md) | Termbrana includes a Zellij observer and a separate composition family. The observer reads, records and reports with provenance. Ovitmugen owns view/layout and protected process lifetime. Stridulatrix owns the planned delivery path. Sublime is the current editor target, with editor choice open. A local transcript view grants no delivery, approval or room-journal authority. |
| [Repo unification](https://github.com/hruzam/nablarva/blob/132699a4276c2f7cb94755b9c70f5f5e76cd8f2d/docs/repo-unification.2026-09-02.md) | Standalone operation survives as a library boundary. Keep vendor record parsing at the edge. The first experiment should work with a file and an editor, even with the room offline. |
| [Majkee–Cartan M0 log, including Zeno’s investigation](https://github.com/hruzam/nablarva/blob/132699a4276c2f7cb94755b9c70f5f5e76cd8f2d/.dev/session/termbrana-M0-markdown-test/raw/majkee-cartan-log.md) | A prompt reappeared after a terminal window was killed and the session resumed. The one-hour interval was untested. The log distinguishes Codex 0.166.0 rollout history from a live app-server request. For Claude Code 2.1.286, the retained evidence left ordinary pending-permission recovery open. These are versioned findings from the log. Record versions on the test host. |
| Majkee’s sketch | Candidate home `~/.nablarva/<project>/<session-id>/`. Read session JSONL, translate to a Markdown file, send a pin from the terminal, open a new Sublime window, load older history on upward scroll. Investigate cache cleanup and approval capture. “Cleared” and the cleanup interval need experimental definitions. |

## First assignment · prove the pin with one fixture

1. Inspect the team’s current branch, session handoff and working changes. Record the commit and installed versions. Use a disposable directory and a synthetic or sanitized fixture from one identified CLI session. Pass the source file and vendor explicitly. Automatic discovery can wait.
2. Choose three identifiable exchanges. Include a multiline message and two identical-looking prompts in different turns. Render a single Markdown file in chronological order. Preserve who said what, code fences and multiline text. Keep a pointer back to each source record. Test what happens to an unknown record type and an unfinished final JSONL line. Defer the partial line until complete.
3. Print a plain absolute file path for any reader. Resolve a selected pin to a line in the current rendering, then try the following on the workstation. Capture the target exchange and whether a new window actually opened.

   ```sh
   # md_path is the absolute path produced by the render. line is a 1-based line number.
   subl -n "${md_path}:${line}"
   ```

   A line number is an editor address for this rendering. Keep the pin as session identity plus a source record identity. If the source lacks stable IDs, try a source-generation fingerprint plus byte offset. Invalidate the pin on replacement or truncation. Never resolve it to a similar-looking exchange. Sublime documents both new-window opening and file-position suffixes. [Command-line reference](https://www.sublimetext.com/docs/command_line.html)

4. Cold-open, append a complete turn, then resume the same session. Re-resolve the original pin each time and compare against a fresh full render. Run a second session under the same project and check that its content never appears in the first view. Close the editor and verify the original native session still answers. Retain only redacted examples.

**First pass criterion.** One terminal invocation opens the intended exchange, including when the same words appear twice. After append or resume there are no missing or duplicate turns. Rebuilding from the same source reproduces the view. Report unsupported cases explicitly. Stop here if session identity or source fidelity is unreliable.

## What to investigate next

| Priority | Question | Smallest discriminating experiment and evidence |
|---|---|---|
| 1 · Session lifecycle | What does “cleared” mean on this CLI? | Compare new session, resume, screen clear/redraw, and the CLI’s own conversation clear/reset, if available. For each record session ID, source generation, last complete offset, visible tail and the old pin result. Treat forks as separate sessions with a possible parent. A disappearing screen alone cannot establish a history boundary. |
| 2 · Approval capture | At which surface can we observe the request, its resolution, and whether a human can still answer it? | Run the matrix below. Compare transcript, native prompt and any already-available read-only protocol evidence. Mark fields absent on each surface. Do not install hooks or introduce another decision channel for this pass. |
| 3 · Is a cache needed? | How much does rendering the full file actually cost on Majkee’s weaker host? | Compare a full render with a recent-turn window on the same small and large fixtures. Record source bytes/turns, cold-open time, warm pin lookup and peak memory. Choose a paging threshold from those numbers. Until then a generated Markdown file may be the entire cache. |
| 4 · Scroll-back | Can more history load without moving the passage the operator is reading? | First expose an explicit “load older” action in the experiment. Pin the first visible record; prepend a page while a new turn arrives. Verify the same record stays at the same viewport position, once with wrapped lines. Then test whether wheel, keyboard and scrollbar approach to the top can trigger that same action once. Compare to opening the full file. Sublime exposes viewport coordinates; scroll-trigger behavior still needs a host probe. [View API](https://www.sublimetext.com/docs/api_reference.html) |
| 5 · Cleanup and recovery | Which bytes can be dropped while an editor or resumed session still needs them? | Trial an idle interval with a simulated clock, including 59/61 minutes if testing an hourly policy. Test an open view, two readers and a reopened cold cache. Evict only derived data when safe. Rebuild the same pin from the retained source. If the source has disappeared, show that explicitly. Measure disk savings before choosing a timer. |

**Proposed ownership.** Vendor-owned JSONL stays at its native location. The proposed project/session directory holds derived files only. Qualify the session key by vendor and use an unambiguous project key so two worktrees with the same basename can coexist. Compare an explicit project key with a checkout-derived one. Publish complete renderings atomically with one writer per view. Keep the operator’s notes separate from generated text. Keep raw transcripts and sensitive tool arguments out of repository evidence.

### Approval experiment · capture the event, then test liveness separately

Use an isolated test home, a disposable session and a harmless operation which genuinely prompts under that host’s policy. Use a fresh request per case. Capture the version, session/turn/request IDs if exposed, time, client and server process lifetimes, evidence surface, and observed outcome. Use a unique harmless marker per trial if native IDs are hidden. A matching marker alone leaves “original vs reissued” unresolved.

| Case | What would distinguish the explanations? |
|---|---|
| Prompt visible, before any answer | Is there already a durable request record? Does it identify this call, or is the screen the only witness? |
| Detach/close only the client, keep server alive, resume from another terminal | Does the same request ID reappear? Can the operator decline it in the native client and observe the matching resolution? Distinguish tmux detach from terminating the client process. |
| Press Esc; repeat separately with Ctrl+C | Record which modal had focus and whether the request was declined, the turn interrupted, or the result stayed unknown. Then check what resume displays. |
| End the disposable owning process, then resume | Verify the owning PID actually exited. Distinguish old history, a newly issued request, and a demonstrably answerable original. Never terminate a shared production daemon for a test. |
| Leave the session idle across the suggested hour | Hold process lifetime and session identity constant. Record elapsed time and whether the same request is answerable on either side. Keep the derived-file cleanup experiment separate. |

For Markdown use the weakest truthful wording, for example **“approval requested · observed at T · outcome unknown”**. Add a resolution only when its source can be correlated. A static file can always report a historical observation. A claim about *currently pending* needs a live source, an observation time and a way to expire that claim when the source disconnects. Keep the first file historical. For Claude, separate stock permission prompts from hook-deferred calls. For Codex, distinguish ordinary CLI resume from a protocol client reattaching to the same daemon.

## Return to Majkee

Return one short experiment report with the exact reproduction command, versioned evidence, a redacted input/output pair with a working pin, the lifecycle/approval matrix with unknowns intact, and the two render timings. Separate **adopt**, **reject** and **needs operator decision**. Use the results to answer three questions: Is the plain Markdown view sufficient on the weaker machine? Is there a reliable approval-capture surface for each installed CLI? Does automatic paging justify an editor integration? Keep the project storage path, cleanup cadence and permanent component owner provisional until then.

## AI HANDOFF

**Goal:** Open the right session exchange from the terminal and inspect its history in Sublime.  
**Current state:** Repository and sketch reviewed. M0 already contains approval research and a terminal-loss observation.  
**Decisions made:** Proposed a file-first experiment with stable pins and a historical approval view.  
**Files changed:** This handoff only.  
**Validation performed:** Checked the cited repository paths at the pinned revision and Sublime’s documented file/line launch and viewport APIs.  
**Open questions / risks:** Source identity across clear/fork, live approval state, cache benefit, and reading-position stability during paging.  
**Recommended next move:** Run the one-fixture pin test before building a watcher, cache service or editor plugin.  
**Agent:** Wave
