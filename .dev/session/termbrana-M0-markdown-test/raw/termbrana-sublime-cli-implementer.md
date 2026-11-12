# Termbrana · Sublime-to-CLI connector

Implementer brief from Wave · 2026-11-06 · proposed scope

Operator clarification — provide an additional observation tool so the developing CLI agent can check outputs sent to Sublime tabs/windows by experimental scripts. The first milestone is run → inspect actual editor output → compare → fix the script → rerun.

## Outcome

Give Majkee’s developing CLI agent a small executable that inspects what experimental scripts actually produce inside Sublime. It must identify the intended window and tab, capture its live text and relevant view state, and return evidence the agent can compare with the experiment’s expected output. The agent continues developing and running scripts through its existing repository and shell tools. This connector supplies the missing observation of the resulting editor state.

Start with a local Arch Linux workstation where Sublime and the CLI run under the same user. Use Python and standard libraries where practical. Measure latency before optimizing transport. Keep installation reversible and document the exact files and links created.

## First milestone · verify experimental output in Sublime

Use an experimental script that sends generated Markdown or text to Sublime as the end-to-end scenario.

1. Capture the relevant window/tab inventory before the run. Run the script through the agent’s normal shell tool and record its command, exit status and a unique run ID.
2. Correlate the output with the intended view. Prefer a view handle returned by the script’s editor integration. Otherwise use a unique output path or test marker plus before/after inventory. Identify a reused tab as well as a newly created one. Return ambiguity when several candidates match.
3. Wait for a specific observable condition with a deadline, such as the run marker appearing in that view and a final completion marker arriving. Script exit or the return of `subl` alone does not establish that the editor has loaded the output. Report a timeout, partial output or still-loading state accurately. For existing experiments without completion signals, report only what was observed at capture time.
4. Read the actual buffer and capture window/view IDs, path/title, revision, active-view identity, selection/caret and visible region or scroll position where relevant. Verify generated content, intended tab/window, duplicate or stale output and any requested jump-to-line behavior.
5. Compare with the expected result and preserve a compact evidence record keyed by run ID. The agent fixes the experimental script using its existing tools, reruns it and checks the new editor output through this connector.

The first demonstration should let the agent discover a deliberately wrong output target or stale buffer, fix the experimental script and prove that the next run reached the correct view with the expected content.

Buffer capture supports content checks. A visible-region/viewport capture supports navigation checks. If an experiment tests rendered layout, font appearance or clipped text, add an explicit visual check through a screenshot or operator observation and report that evidence separately. A successful buffer comparison establishes only the tested text and state properties.

## Evidence already collected

Wave inspected upstream documentation and source. No running Sublime installation was available for an end-to-end test. Treat runtime compatibility and response times as unmeasured.

| Candidate | Observed behavior | Consequence |
|---|---|---|
| `dpc00/sublime-mcp` at `6fdcf8d322d25af6b690f64afd288aeeed27b7ef` | Plugin exposes plain HTTP as well as MCP. Linux defaults are HTTP 9501 and MCP 9503. Read handlers include active buffer, selections, open files and view content. | Provides an immediate baseline through curl. |
| Same revision, `_get_open_files`, `_get_file_content`, `_get_view_content`, `_get_selection` | Inspected handlers resolve through the active window. View content can use an index or partial name. | Test focus changes and duplicate names. Those routes alone do not satisfy explicit multi-window addressing. |
| Same revision, `_get_active_file` | Reads the live buffer, defaults to 20,000 characters and indicates truncation. | Check response metadata before treating output as complete. |
| `benyue1978/sublime-mcp` at `ebe64b03f6fc15b0e3bab0e90bad7a2cd80a7084` | `bridge_core.py` skips every view with a filename. | Its scratch-buffer scope omits modified named files. |
| Sublime API | Exposes windows, views, buffer text, selections and change counters. | Supports a small purpose-built reader if upstream adaptation is larger. |

Sources are linked at the end. Recheck the chosen installed revision and its local configuration before using the commands below.

## Work order

1. Read the checkout’s instructions, current handoff and git status/diff. Identify existing Termbrana or editor integration code before adding anything. Preserve active work. Record host, Sublime build, plugin Python runtime and upstream revision.
2. Obtain a baseline from the broader existing plugin in a disposable Sublime profile or agreed test setup. Confirm the actual Packages directory through Preferences → Browse Packages. The upstream repository root is the package. Its documented Linux install links the checkout into `~/.config/sublime-text/Packages/sublime-mcp`. Avoid overwriting an existing install.
3. Exercise the read routes below with test buffers. Check focus races and whether the current upstream provides explicit IDs elsewhere. Inspect a narrowly relevant API if the version has changed.
4. Select the smallest implementation that passes the acceptance table. Reuse or extend the existing bridge if its targeting can be corrected with a focused change. Otherwise build the plugin-and-CLI pair described below. Record the deciding evidence and any upstream license obligations.
5. Complete the experiment-observation loop above. Deliver the executable, plugin or focused upstream patch, installation/removal instructions, and a short validation report. Continue through implementation and local tests when the required host is available. Record GUI-dependent checks as pending when it is unavailable.

## Baseline commands

Run these after installing the existing plugin and restarting Sublime. They assume its default Linux port and unset authentication. If authentication is configured, pass its required Authorization header using the host’s established secret-handling method.

```sh
curl --fail --silent --show-error --max-time 5 \
  http://127.0.0.1:9501/health

curl --fail --silent --show-error --max-time 5 \
  http://127.0.0.1:9501/open_files

curl --fail --silent --show-error --max-time 5 \
  http://127.0.0.1:9501/active_file

curl --fail --silent --show-error --max-time 5 \
  http://127.0.0.1:9501/selection

curl --fail --silent --show-error --max-time 5 --get \
  --data-urlencode 'path=/absolute/path/to/test.md' \
  http://127.0.0.1:9501/file_content
```

The final route reads the open buffer in the active window. A successful HTTP response can still contain an application error. Inspect both. These probes establish a baseline, not completion of the multi-window contract.

The upstream plugin also supplies mutation and Python-execution operations. Its settings include `auth_token`, `disabled_tools` and `allow_lan_access`. Keep the trial local. A wrapper exposing only reads limits its own command surface; evaluate the separately exposed plugin endpoints when choosing the permanent implementation.

## Proposed CLI contract

These commands are the interface to implement. They are not existing upstream commands. Use `termbrana-editor` provisionally, adapting the name to the checkout’s established naming if necessary.

```sh
termbrana-editor windows
termbrana-editor tabs --instance INSTANCE --window 12
termbrana-editor read --instance INSTANCE --window 12 --view 37
termbrana-editor selection --instance INSTANCE --window 12 --view 37
termbrana-editor read --instance INSTANCE --window 12 --view 37 --lines 40:90
termbrana-editor state --instance INSTANCE --window 12 --view 37
```

Use JSON on stdout and diagnostics on stderr. Success exits zero. Failures return a structured error and a nonzero status. Establish a bounded timeout, initially five seconds. Report unavailable editor, invalid target, expired instance, loading buffer and oversized response explicitly.

Inventory returns all editor windows, project roots and their text views. Record non-text sheets as unsupported when present. Text responses carry instance ID, window ID, view ID, buffer ID, optional filename, title, dirty flag, loading state, change count, capture time, requested range, returned range and truncation status. The state command also reports which view is active, caret/selection regions and viewport information needed by the experiment. Ordinary reads preserve focus and scroll position. Use a fresh instance token after plugin restart/reload so an old handle cannot silently resolve to a newly created view. Cloned views may share a buffer while having different selections.

Read using the supplied IDs. A closed or mismatched target produces an error. Tab order, partial title matching and changing focus must never silently redirect an explicit request. If multiple editor instances are running, require explicit instance selection when routing is ambiguous.

Line ranges use one-based inclusive bounds. Define behavior at EOF and reject invalid ranges. Preserve Unicode and multiline text. For selections, return every region and distinguish an empty caret from selected text. Document point-offset units if exposing Sublime offsets; avoid treating them as byte offsets.

Read metadata, content and selections in one short scheduled capture. Bound the content size, and detect content changes during capture where needed. A change count describes text revisions; selection changes require their own fresh capture. For paged reads, accept an expected change count and report a revision conflict if the text changed between pages.

Implement bounded polling for readiness in the experiment harness using the same read/state contract. Keep capture useful as a standalone CLI operation. One run’s marker and target handle must never be satisfied by an older run or a similarly named tab.

## Small custom implementation if needed

Use one Sublime Python plugin and one Python CLI executable. The plugin performs the named inventory, read and state-capture operations through the editor API. The CLI requests a snapshot and prints the response.

For the first transport, evaluate `subl --background --command` invoking a registered plugin command, with a unique request/response directory per call. Construct subprocess arguments as an argument array and JSON-encode command parameters. Probe command dispatch in the installed build, including multiple windows and editor instances. Give routing an explicit failure mode if the launcher cannot select the requested instance reliably.

The CLI creates a private per-request directory below the user’s runtime directory, writes the request, invokes the plugin command and waits to a deadline. The plugin validates the request, captures the target and atomically publishes the complete response. Echo the request ID and verify it before returning. Handle plugin reload, timeout, late response and concurrent callers without consuming another request’s result. Treat the response directory as temporary and apply bounded cleanup after abandoned requests.

Use existing `subprocess`, JSON and filesystem primitives. Do not construct shell commands from tab names or paths. Implement the observation operations and use them to complete the experimental-script feedback loop. Add MCP exposure only if a concrete client needs it.

If subprocess/file overhead is measurable and obstructs normal use, retain the contract and evaluate a Unix-domain socket served by the plugin. Run transport I/O off the UI thread and schedule short captures. Keep large encoding and file I/O outside the editor’s critical path where feasible.

## Acceptance checks

| Scenario | Required result |
|---|---|
| Unnamed draft | Exact live text can be read by its explicit handle. |
| Named file with unsaved edits | Returned text includes the unsaved changes. Disk content is untouched. |
| Two windows, duplicate tab titles | Inventory distinguishes them; every read reaches the requested view. |
| Switch active window between list and read | Explicit target remains correct. |
| Reorder or close a target tab | Reordering preserves targeting; closing returns an error. |
| Clone a view | Shared buffer identity and per-view selections are represented correctly. |
| Multiple selections, carets, Unicode and multiline content | Content and documented coordinates are correct. |
| Plugin/editor restart | Old instance handles fail clearly. |
| Concurrent CLI requests | Request IDs and responses remain isolated. |
| Edit during a multi-page read | Expected revision detects the change. |
| Large buffer | Output is bounded and any truncation is explicit. |
| Editor absent, plugin unavailable or request timed out | CLI exits within its deadline and reports the failure. |
| Script writes to a new tab or reuses an existing tab | Capture identifies the correct destination for the current run. |
| Earlier run contains identical output | Run identity and target correlation prevent a stale success. |
| Script exits before the editor finishes loading | Deadline-based observation waits for the defined condition or reports incomplete evidence. |
| Incremental output arrives in chunks | Partial and complete states follow the experiment’s completion signal. |
| Script targets the wrong window | Verification reports the mismatch, even when the text is correct. |
| Script requests a particular line or selection | Captured caret, selection and viewport state support the relevant assertions. |
| Agent fixes and reruns the experiment | Evidence identifies both runs and shows the corrected observed result. |

Use small synthetic fixtures. Record observed failures and the correction made. Measure end-to-end warm request latency, cold behavior and response size for representative buffers on the actual host. Report median and p95 with sample count. Define a practical latency target from the operator’s workflow and the baseline measurements.

## Completion and integration

The first successful operator workflow is “run this experiment, inspect its output in Sublime, identify what failed, fix the script and verify the next run” through the connector and the CLI agent’s existing development tools. Add a short usage note to the appropriate existing agent instructions. Reading one named tab should require one call once its handle is known.

Keep live editor capture separate from the JSONL-to-Markdown transcript renderer discussed in Termbrana M0. The renderer produces readable session history. This connector makes the resulting tab, draft or selection observable to a CLI agent. A selected historical approval request remains captured text with provenance; approval handling continues through the established native CLI path.

Editor mutation commands remain a possible later extension. Complete the observation milestone first.

Return implementation paths, actual commands executed, test outcomes, measured latency, installation/removal steps and outstanding host checks. Append the checkout’s normal AI HANDOFF with goal, current state, decisions, files changed, validation, risks, next move and implementing agent.

## Sources

- [Sublime Python API](https://www.sublimetext.com/docs/api_reference.html)
- [Sublime command-line interface](https://www.sublimetext.com/docs/command_line.html)
- [Broader connector README at inspected revision](https://github.com/dpc00/sublime-mcp/blob/6fdcf8d322d25af6b690f64afd288aeeed27b7ef/README.md)
- [Broader connector handlers](https://github.com/dpc00/sublime-mcp/blob/6fdcf8d322d25af6b690f64afd288aeeed27b7ef/sublime_mcp.py)
- [Broader connector settings](https://github.com/dpc00/sublime-mcp/blob/6fdcf8d322d25af6b690f64afd288aeeed27b7ef/MCP%20Commander.sublime-settings)
- [Scratch-only connector implementation](https://github.com/benyue1978/sublime-mcp/blob/ebe64b03f6fc15b0e3bab0e90bad7a2cd80a7084/sublime_mcp_server/bridge_core.py)
