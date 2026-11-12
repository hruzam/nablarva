# RUNBOOK: termbrana-M0-markdown-test

```yaml
goal: >-
  From a native CLI workflow, open an explicitly selected conversation exchange in a
  new Sublime window, browse retained history while the CLI continues, preserve source
  identity and message structure, and inspect approval evidence with decisions kept
  in the native CLI.
gate: >-
  Majkee records GO or STOP on an independently verified home-host transcript-view
  experiment for Codex and Claude, demonstrating zsh selection and Sublime opening,
  snapshot-bound bookmarks across rebuild, validated carry-forward on append/resume,
  automatic cache collection with explicit reading-view refresh, truthful interactive
  approval references, native-session independence, measured performance, and a
  reviewed ia-sync source-wiring and publication proposal with capability limits.
participant_1: [Cartan, {brand: Codex, model: gpt-6.1-terra, effort: high}, {host: home, role: working head and integration owner}]
participant_2: [implementer, {brand: Codex, model: gpt-5.6-terra, effort: high}, {host: home, role: bounded implementation worker when delegated}]
participant_3: [verifier, {brand: Codex, model: gpt-5.6-sol, effort: high}, {host: home, role: independent acceptance witness}]
participant_4: [houston, {brand: Codex, model: gpt-6.1-sol, effort: high}, {host: home, role: bounded architecture consult}]
participant_5: [majkee, {brand: human, model: none, effort: none}, {host: home, role: native UI witness and final gavel}]
status_owner: Cartan
authored_by: Oraculum · Codex, under Majkee's explicit Octopus assignment
observations_read: none exist
```

## Why this session exists

The operator needs reliable reading and return addresses for CLI conversations while
their native sessions continue. JSONL parsing alone does not establish conversation
fidelity; opening a known Markdown line does not establish native-visible exchange
selection. This experiment qualifies those claims separately.

Reuse this operator-assigned bed and its three raw inputs. The shorthand
`termbrana-M0` names this Markdown experiment, not the already-frozen Zellij M0.
The gate is a qualification decision, not production deployment. STOP preserves a
useful report of the failed capability; incomplete tests are not a PASS.

## Fixed direction and authority

- Said: Majkee, 2026-11-06, approves snapshot-bound bookmarks, automatic collection
  and explicit movement of the reading view, and requests updating this existing
  RUNBOOK. This is an explicit in-place amendment for this session, overriding the
  usual fixed-RUNBOOK/numbered-successor procedure for this change only. It does not
  authorize future silent gate changes. Cartan retains execution and STATUS ownership.
- The prior universal truncate/regrow detection promise is superseded by the
  continuity contract below. Preserve `evidence.stage1-continuity.md` as evidence of
  the observation limit; do not rewrite the old result into a new acceptance PASS.

- Said: Majkee, 2026-11-05, accepted the file-first proposal and requested this
  Octopus launcher. Explicit selection plus a stable full-history snapshot is the
  first useful workflow. Native-visible exchange binding and automatic paging
  remain later capabilities, independently qualified.
- Said: Majkee, 2026-11-05, authorizes the temporary runtime layout
  `~/.nablarva/<project-slug>/<session-bed-slug>/cache.<agentive-session-id>` plus
  `read.<agentive-session-id>.md` and supporting files. Reboot cleanup is later.
  This is a task-scoped temporary choice, not a rewrite of architecture section 4.8.
- The bed slug is the task name under `.dev/session/`; the agentive session is a
  distinct vendor conversation/branch. Preserve canonical project path, vendor,
  branch/conversation identity and source identity in metadata; slugs are labels.
- Said: Majkee requests a separate function set compatible with the existing
  Termbrana zsh family and ia-sync deployment standards. The planned promotion
  target is `/home/hruzam/ia-sync/zsh/termbrana/`, subject to reviewed placement
  disposition under L8/L8′/L17. The experimental implementation remains in this bed.
- Model tuples above declare recommended carriage, not observed runtime facts.
  Use native role contracts; report unavailable carriage rather than silently
  substituting. Cartan in Medusa posture is the next seat because this work spans
  adapters, projection, shell integration and an operator UI sitting. No cSharp arc
  or autonomous full-session fan-out is created.

## Design and source wiring

The conventional patterns are a materialized view, a source bookmark/map and a
complete-record log reader. Keep the pipeline small:

```text
explicit vendor/source + explicit conversation/exchange choice
    -> vendor-specific history reconstruction
    -> source bookmark + deterministic Markdown + render/source map
    -> zsh prints absolute path and optionally opens Sublime at its current line
```

### Experimental and publication homes

- Implementation owner writes only
  `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/`
  and synthetic fixtures/tests below that directory. Start directories only on use.
- Shape the candidate as `transcript.zsh` plus adjacent Python stdlib helper(s),
  with a standalone Python entry and an inert experimental `base.zsh` /
  `keyboard.zsh`. Source files resolve helpers beside themselves, not from a
  hard-coded home path. The core must work without an interactive shell.
- Promotion proposal: add the separate transcript engine/helper(s) to
  `/home/hruzam/ia-sync/zsh/termbrana/`; add only transcript aliases to its existing
  `keyboard.zsh` and one inert engine source in its existing `base.zsh`.
  Preserve composer functions, grammar and acceptance. Do not create a second
  keyboard inside the family. Candidate prefix `tbv-` is provisional until the
  executor repeats the duplicate/interference sweep and records the choice.
- Existing law: aliases/comments only in `keyboard.zsh`; function bodies in the
  scope engine; source is quiet, repeatable and performs no scans, cache writes,
  Python startup or editor/session activation. Python work occurs on invocation.
- The observed publisher is `/home/hruzam/ia-sync/deploy.sh`, whose zsh rsync leg
  copies to `~/.config/zsh/`. Neither that script nor the searched shell sources
  expose literal `DEPLOY_*` controls. Do not invent flags or revive retired
  Nablarva devenv deploy scripts. The existing Termbrana README declares source-only
  use; host config wiring is a distinct activation change, not implied by copying.
- Prepare a reviewed publication proposal specifying changed source files, merge
  checks, relevant dry-run output, host-owned startup wiring, rollback and fresh-shell
  verification. This session does not execute publication. A full ia-sync deploy
  affects other families; never treat it as a transcript-only installer.
- Home and office own their respective config/zshrc files. Plan parity explicitly;
  home evidence does not qualify office. Editor package changes, if later needed,
  use the existing install-pkgs route and preserve local keymaps. No new plugin or
  package dependency is required for this first experiment.

### Transcript and interaction contract

1. Require explicit source/vendor for the first fixture. Offer a numbered exchange
   selector with role, time and snippet for recognition, backed by exact source
   identity. Duplicate text must remain distinct. Report this as transcript selection,
   never automatic selection of the exchange currently visible in the native TUI.
2. Define canonical presentation records per vendor/version, including branch and
   compaction semantics; successful JSON decoding is insufficient. Disclose omitted,
   unknown and unsupported content. Preserve text, multiline/code boundaries and
   provenance without rendering duplicate representations as duplicate exchanges.
3. Bind each bookmark to an immutable cached snapshot, vendor, specific
   conversation/branch and source record (or validated offset inside that snapshot).
   A Markdown line is derived for that snapshot/rendering. Retain the complete source
   prefix needed to reproduce it, its content digest, provenance and renderer version;
   native record IDs need vendor qualification. Snapshot identity identifies captured
   content, not an otherwise unobserved native file generation.
   Carry a bookmark forward only after checking the source identity/branch and exact
   previously captured complete prefix against the new capture. Never match by similar
   text. Observable replacement, shortening, prefix mutation, identity mismatch or
   missing source blocks automatic carry-forward, but does not invalidate a retained,
   intact historical snapshot. Report the condition and require explicit new selection.
   An unobserved same-inode truncate/regrow restoring identical bytes is indistinguishable
   from append under this contract. Disclose that limit; do not require or claim detection.
   A local UUID, timestamps or watcher events alone do not establish native generation.
4. Defer an incomplete final record and diagnose malformed complete records. One JSONL
   line need not equal one visible message; the adapter determines presentation units.
   Capture a bounded complete prefix; validate consistency before publishing and retry
   or report uncertainty on concurrent changes. Store captured source, Markdown and
   map as one immutable snapshot bundle, with one serialized publisher. Publish only
   complete bundles through an atomic manifest/pointer switch; readers resolve one
   bundle identity and never combine files from different generations. Compare
   incremental results with full rebuilds of the same captured bytes. An interrupted
   publisher must leave the previous committed snapshot usable.
5. After explicit invocation for an explicit source, collect new complete records
   automatically into new cache snapshots. Use a bounded foreground watch command with
   a documented polling interval as the minimal dependency-free implementation; file
   notifications are optional hints, never continuity evidence. Shell sourcing starts
   nothing. No login service, persistent daemon, native-session attachment or discovery.
   Expose latest-snapshot versus selected-snapshot state through the CLI, including
   "new messages available" when the adapter establishes that fact; otherwise say
   "new records available". No editor plugin/status-bar integration is required.
   Keep the selected reading file and open snapshot unchanged while collection runs.
   Explicit refresh selects a complete newer snapshot and re-resolves the bookmark,
   or reports why carry-forward is unavailable. Do not silently relocate the reader.
   Keep the former snapshot available while retained; automatic paging and viewport
   restoration remain later work. Stopping the collector must not stop the native CLI.
   Measure idle polling and growing-history cost before adding optimization machinery.
6. An approval block shows the observed request, timestamp, source reference and
   correlated resolution when known; otherwise outcome unknown. Missing evidence is
   not a negative decision. Historical text never claims current answerability.
7. Minimum interaction: a generated approval reference opens its exact retained
   source location in the immutable snapshot using the existing editor file-address
   mechanism. Label the cached source and original provenance distinctly. An original
   live-source link may be offered only after revalidation; do not silently redirect
   a stale reference into a changed original. Use a synthetic or
   sanitized source in the UI witness. Witness this feature in Sublime; a formatted
   path alone is not an interaction PASS. Navigation to an already-running native
   session is a separate optional capability, requiring checked target identity and
   an existing view-only action. If unavailable, show that honestly; do not invent a
   working button, approve/deny control, shell link, transport or app-server resume.
8. Keep generated text separate from operator notes. Bookmarks may reference notes,
   but this session builds no note service. A snapshot retains the captured source
   needed for its own rebuild; original-source loss must be visible and blocks refresh,
   while cached historical reading remains available. Deleting a retained snapshot can
   remove the last copy behind its bookmarks: do not call that lossless disposal.
   No reboot cleanup, automatic eviction or deletion of native history belongs to this gate.

### Existing Sublime pin seam

Read Cartan's installation handoff and inspect the cited source before building a
replacement. The source offers `editor_pin_open_target` and editor-location pins;
it does not establish durable transcript identity. Its `find_git_root()` walks the
reading file's ancestors: the chosen `~/.nablarva/` output can therefore lack a
project-root field. Explicit transcript metadata must carry that identity; never
claim cache-path root discovery identifies the original project or conversation.

The handoff records installed-byte matches and stale installer bookkeeping. Those
are attributed observations to recheck as needed, not a repair assignment. The older
plugin README uses `~/.pins` while the inspected core uses `~/.wires/pins.jsonl`.
Resolve source/live facts, do not normalize their histories. Do not claim/consume,
clear or rewrite the production pin queue, invoke its tmux-send path, install a
plugin or alter keymaps. Source inspection and the existing open-target action suffice.

### Planned development tool: Sublime-to-CLI observation connector

Said: Majkee, 2026-11-06, supplied
`/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/termbrana-sublime-cli-implementer.md`
and requested adding this tool to the development portfolio. Adopt its observation
use case as a planned tool: run an experiment, inspect the actual Sublime result,
compare with expectations, fix through the existing development tools, then rerun.
The supplied brief is a proposed implementation contract with attributed upstream
research; it is not evidence that an executable or plugin is installed or qualified.
`termbrana-editor` remains a provisional command name pending the naming sweep.

Keep this connector separate from the transcript renderer. Its prospective interface
inventories windows/views and reads live buffer text, selections and view state by
explicit instance/window/view identity. In particular, disk reads cannot establish
unsaved buffer content. Read operations must preserve focus, selection and scroll.
Do not read unrelated open buffers merely because inventory exposes them; use explicit
synthetic test targets and retain only scoped, sanitized evidence.

Use the raw brief as the bounded connector-build input. Its first qualification is
one deliberately wrong-target or stale-buffer experiment, followed by a correction
and a new run proving the intended view and content. Require run correlation, explicit
handles, readiness deadlines, revision/truncation metadata, duplicate-window tests,
restart invalidation and measured latency. Inspect an existing bridge before choosing
reuse versus a small purpose-built reader; the brief's upstream claims require local
revision and capability checks. A read-only CLI wrapper does not constrain mutation
or execution endpoints exposed separately by its backend.

For this transcript experiment, a qualified connector can supply evidence of actual
buffer text, target view, caret/selection and viewport state, including refresh staying
put until requested. It cannot by itself qualify visual rendering, native transcript
fidelity, native-session independence or live approval answerability. Keep operator
or screenshot evidence where the claim requires it; never forward historical approvals.

Connector implementation/installation is a separately bounded work item using the
supplied brief, with its own file ownership, disposable-profile trial, reversible
installation/removal plan and host qualification. Adding it to this portfolio does
not release live-plugin edits under the current transcript gate. Do not introduce it
as a new prerequisite for Cartan's in-flight verification or abandon the existing PAD.
If a qualified installation becomes available, Cartan may record its exact revision,
configuration and scoped observations as supplemental evidence before relying on it.

## Reconcile the earlier candidate and execution environment

On resume, inventory the candidate and any task-attributable effects outside the
experimental tree before changing them. Reuse valid fixtures, adapter work and tests;
retire only obsolete assumptions, code paths and expectations from the old contract.
Preserve raw inputs, the capability comparison and the original continuity finding.
The five reported synthetic passes are historical evidence, not qualification of this
amendment or native fidelity. Add the same-prefix regrow case as a documented detection
limit, and test observable discontinuities separately. Serialized publication remains
required implementation work, not an architectural blocker by itself.

Majkee's rewind instruction permits reverting unnecessary effects of this experiment
if Cartan made them outside the sandbox. Establish exact paths and before/after evidence
first; restore only attributable obsolete changes without disturbing newer or unrelated
work. Do not use broad reset/clean, delete caches or histories indiscriminately, or
reverse the pre-existing Sublime installation. If attribution is uncertain, report
that specific path and continue unaffected work. Respect effective filesystem permissions;
this instruction does not grant deployment or new host configuration changes.

Use disposable output overrides for parser, snapshot, collector and shell qualification.
Sandbox limits do not block those independent tasks. Actual ~/.nablarva layout, Sublime
interaction and native-session independence require separate real host witnesses; prepare
exact PAD steps for Majkee when access or GUI control is unavailable. Never replace a
missing host witness with a sandbox PASS or widen permissions implicitly.

## prompt-0 — Cartan, working head

```text
Use $medusa in /home/hruzam/unikuklatrix/nablarva.
Read /home/hruzam/unikuklatrix/nablarva/AGENTS.md and its required read order,
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md,
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/STATUS.md,
and /home/hruzam/reposoma/raw.guides/status/GUIDE.md.
You are Cartan, sole status_owner and integration owner. Resolve actual host,
worktree, permissions and overlapping work, then run the STATUS recovery probe.
Read the three original raw inputs and the planned connector section; read the
connector brief when evaluating that tool, plus only the source/canon needed.
Use the surgical-coding skill for implementation. Check native export/navigation
and installed vendor versions first; retain an existing facility if it meets the
gate. Do not re-run broad research or consume real transcript/pin stores casually.

Own this bed's STATUS, evidence, UI PAD and final REPORT; preserve existing raw files.
First reconcile the earlier candidate and effects under this RUNBOOK's reconciliation
section; record the attributable keep/adapt/revert decisions in evidence.
Stage 1: reuse the frozen synthetic fixture, qualify canonical projection, immutable
snapshot bundles and snapshot-bound bookmarks using explicit vendor/source. Freeze
amended expectations before comparing implementation results.
Stage 2: qualify both installed vendor adapters, observable discontinuities, validated
carry-forward, automatic foreground collection and explicit reading-view refresh,
plus the selector and inert zsh surface. Use sanitized fixtures; isolated native
sessions require the operator's involvement, and native histories stay host-local.
Stage 3: prepare a short operator PAD, run home-host Sublime interaction and native
session-independence checks with Majkee, and measure small/large fixture costs.
Stage 4: obtain the independent verifier return and Houston consult on the concrete
integration/publication proposal; disposition findings without locking canon.
Stage 5: write /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/REPORT.md
with reproducible commands, redacted evidence, capability matrix, timings, source
wiring proposal, remaining limits and GO/STOP recommendation; ask Majkee for the gate.

You may implement directly or delegate prompt-1 with exact file ownership; do not
write the same files concurrently. The native verifier is independent and never fixes.
Use prompt-3 Houston only as a bounded consult, not a substitute implementation head.
Use /home/hruzam/reposoma/raw.guides/PAD/GUIDE.md when authoring the human sitting.
Maintain STATUS before effects and after verified transitions. If permission blocks
the temporary runtime home, use an explicit disposable output override for fixture
work and record that the actual path witness remains unpaid; never claim parity.
Return architectural/ownership changes to Majkee and Oraculum's planning sitting.
Stop after presenting the verified report and recording the operator's gate decision.
No Git publication, live deploy, host-config edit, new transport or session injection.
```

## prompt-1 — implementer, if delegated

```text
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md
and /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/STATUS.md.
Act under your native implementer role. You are not alone in the codebase: preserve
others' edits and adapt to them. Cartan must name the bounded stage and expected
inputs before this prompt is dispatched; do not choose additional work yourself.
Own only /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/
for that stage. Implement its synthetic fixtures/tests, standalone Python stdlib
projection and source-relative zsh surface as specified in this RUNBOOK.
No STATUS/raw/canon/ia-sync/live-editor/host-config writes, no global pin queue access,
no native-session start/resume/stop, no commit/push/deploy. Run scoped meaningful
tests and return exact changed paths, commands, observed results and unsupported
cases to Cartan. Do not independently claim the overall gate.
```

## prompt-2 — verifier

```text
Independently verify the candidate under
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/.
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md
and the exact candidate/evidence revision Cartan supplies. Compare the actual diff,
fixtures, output and commands against Acceptance evidence; do not trust writer claims.
Run isolated tests with a disposable output override. Inspect operator UI receipts;
if you cannot observe a UI claim independently, distinguish operator-witnessed from
machine-verified and mark missing proof. Verify raw-input preservation and declared
scope. Do not fix anything or rewrite STATUS. Return PASS/FAIL/UNVERIFIED by criterion,
reproduction commands, missing proof, and status_rewritten: false. Cartan records your
verbatim return at /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/verdict.transcript.verifier.md.
```

## prompt-3 — Houston, card: consult

```text
Card: consult. Load your shared identity, Codex binding, Nablarva addendum and consult
card. Read /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md,
its current STATUS.md, and Cartan's concrete report/proposed publication diff in that
bed. Consult the relevant flag locks, docs/ARCHITECTURE.md and Termbrana source rules.
Check observation/view authority, historical approval wording, the existing Sublime
pin seam, temporary storage exception, separate zsh functions, L8 processor-placement
boundary and reviewed ia-sync promotion/activation. The preplanning consult returned
stretches; assess this actual result freshly. Return fits/stretches/breaks/unclear,
at most five constraints and cited evidence. No writes, implementation, STATUS
ownership or further delegation. Cartan records your return verbatim in this bed's raw/.
```

## prompt-4 — Majkee, native UI witness and gavel

```text
Open /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/STATUS.md.
With Cartan, follow the prepared UI PAD in that same bed on home. Use disposable
native sessions and redacted/synthetic approval material. Witness the intended
exchange in a new Sublime window, the approval source-reference action, duplicate
prompt disambiguation, and the CLI still answering after the editor closes. While
collection runs, append new conversation content: witness availability reporting with
the open snapshot unchanged, then explicit refresh to the newer snapshot. Stop the
collector and confirm that the native session remains usable.
Make any real permission decision only in the native CLI. Record what you actually
saw; a screenshot or old prompt alone does not prove live answerability.
Review REPORT.md and the independent returns in this bed; record GO or STOP on the
single gate. A GO accepts this qualification, not automatic publication or deployment.
```

## Known constraints and holds

- Follow Nablarva flags L6, L8/L8′, L9′, L11/L12, L16–L22. No local Termbrana
  harness, no Zellij-M0 reopening, no inherited Zellij source grade/Rust mandate/M2
  benchmark for this separate transcript experiment. No sealed-vault reads.
- Prototype writes are confined to the owned experimental tree, head-owned evidence
  and explicit derived-output directories. Private native logs remain host-local;
  committed evidence contains only synthetic or explicitly sanitized material.
- The source-only build and runtime invocation do not authorize edits in ia-sync,
  installation, startup sourcing, dependency installation, cross-host transport,
  commit/push or deployment. Prepare the publication path concretely for review.
- Permanent function ownership needs disposition against L8/L8′ before promotion.
  The operator's separate-zsh-function direction is not a global canon amendment.
- No application-server resume just to read history, no input injection, signals,
  acceptance forwarding, send-keys, pin claiming or invented approval controls.
  Live approval recovery probes require separate bounded operator release; reuse
  the raw research as attributed evidence and preserve its unknowns.
- Existing files under raw/ belong to their authors. In particular preserve the
  untracked Cartan Sublime handoff. Do not absorb its installer bookkeeping repair.
- Cleanup on reboot, automatic eviction, persistent background services, automatic
  paging, note service and autonomous native-session discovery/attachment remain
  later work. Explicitly started foreground automatic collection is in this gate.

## Acceptance evidence

| Claim | Required witness |
|---|---|
| Existing facilities and boundaries | Installed versions, native export/navigation comparison, exact source inputs, existing pin-plugin inspection, naming sweep and retired-by-native condition. |
| Conversation fidelity | Per-vendor/version fixtures with frozen expected conversation, multiline/code, duplicate-looking prompts, duplicate representations, unsupported records, partial final line, malformed complete line and branch/compaction cases. |
| Snapshot bookmarks and carry-forward | Correct mapping within a retained snapshot after cold rebuild; validated carry-forward on append/resume; isolation across conversations and colliding project basenames. Observable shortening, replacement, prefix mutation, identity mismatch or source loss blocks carry-forward while retained history stays readable. Same-prefix unobserved regrow is explicitly recorded as undetectable, not claimed as caught. |
| Automatic collection and explicit refresh | Complete appended records become available within the documented polling interval plus processing time; partial tails wait; no duplicate exchanges on repeated polls. Open snapshot and selected reading file stay unchanged until explicit refresh. Test collector restart, concurrent publication, interrupted publication and unchanged-source polling; readers see only complete matching bundles. No automatic native-session or editor activation. |
| zsh entry | Direct Python and source-relative shell invocation agree; keyboard has aliases/comments only; repeated source has no I/O/process/editor effects; ordinary errors are actionable; composer regression checks remain green if shared files are proposed for promotion. |
| Temporary layout | Witness the authorized project/bed/agentive-session layout, collision checks, metadata/source-map consistency, complete publication and cache rebuild. An override-only test cannot qualify the actual temporary home. |
| Editor interaction | Operator witnesses new window and correct exchange, including already-open-file case; actual approval source-reference navigation; source-vs-editor pin distinction; native CLI continues and survives view closure. |
| Approval truth | Request/time/provenance, correlated resolution or explicit unknown; no live-pending claim from history alone; unavailable source fields and native target navigation clearly marked. |
| Performance | On home, record fixture bytes/turns and small/large cold full-render time, warm pin lookup, idle polling cost, append-to-availability latency and peak memory with exact commands. Record the operator's usable/unusable judgment; do not import composer budgets or fabricate a paging threshold. |
| Review and return | Independent verifier result, fresh Houston finding, disposition of every material finding, concrete ia-sync source/wiring/activation proposal and Majkee GO/STOP. |

Cartan stores redacted evidence in this bed on demand and returns one REPORT with
adopt / reject / operator decision clearly separated. It includes exact commands,
input/output fixture pair, working pin, lifecycle/approval capability matrix and
timings. Report snapshot retention and the unobservable-rewrite limit explicitly.
Unavailable runtime/GUI evidence remains UNVERIFIED and prevents a GO
claim for that capability. Follow the shared closure law; promotion, observations
and pruning are separately authorized effects, never an automatic cleanup step.

## References

- `/home/hruzam/unikuklatrix/nablarva/AGENTS.md`, `.dev/session/flag.md`, `.dev/session/pulse.md`, `PROJECT.yaml` — repository authority and router (read from this absolute repository root).
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md` — observation/view, L8 placement and section 4.8 configuration direction.
- `/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md` and `/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md` — separate observer and composition contracts.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/termbrana-M0-transcript-view.cli-handoff.md` — Wave's proposal, not a build release by itself.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/majkee-cartan-log.md` — versioned approval findings and explicit gaps.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/termbrana-sublime-cli-implementer.md` — operator-supplied proposed editor-observation tool; separate from transcript rendering and not yet qualified.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/sublime-pin-install-handoff.cartan.2026-11-05.md` — existing source/install map; preserved operator-supplied handoff.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/05_WAY_OF_THINKING.md` — conventional pattern, solved practice, open edges and case-specific invention.
- `/home/hruzam/ia-sync/zsh/termbrana/README.md`, `/home/hruzam/ia-sync/zsh/termbrana/base.zsh`, `/home/hruzam/ia-sync/zsh/termbrana/keyboard.zsh`, `/home/hruzam/ia-sync/zsh/termbrana/composer.zsh` — existing source-only family.
- `/home/hruzam/ia-sync/AGENTS.md`, `/home/hruzam/ia-sync/zsh/AGENTS.md`, `/home/hruzam/ia-sync/SYNC_DISCIPLINE.md`, `/home/hruzam/ia-sync/zsh/guides/guide-for-builder.md`, `/home/hruzam/ia-sync/zsh/guides/keyboard.md`, `/home/hruzam/ia-sync/deploy.sh` — source, shell and publication rules; older guide references to sync.sh are superseded by SYNC_DISCIPLINE.
- `/home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/README.md`, `/home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/pin_core.py`, `/home/hruzam/www/elements-factory/applications-in-common/experiments/editor-pin-sublime/editor_pin.py` — inspect only; no queue consumption, installation or modification.
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md`, `/home/hruzam/reposoma/raw.guides/runbook/res/token-economy.md`, `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` — launcher, bounded delegation and recovery shape. Token-economy chapter is draft; Medusa permits direct scoped implementation.
- `/home/hruzam/.agents/skills/medusa/SKILL.md` — working-head entry and return boundary.
- https://www.sublimetext.com/docs/command_line.html — documented new-window and line-address launch; host behavior still needs a witness.
- https://learn.chatgpt.com/docs/app-server — current thread/branch identity; recheck against the installed version, do not activate a protocol client in this gate.
- https://code.claude.com/docs/en/sessions — current native history/export behavior; recheck installed semantics.
