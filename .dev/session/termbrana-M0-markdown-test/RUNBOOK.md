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
  source-bookmark fidelity across rebuild and append/resume, truthful interactive
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
3. Pins address vendor + specific conversation/branch + source record. A Markdown
   line is derived for one rendering. Use native identities where qualified; offset
   fallback must revalidate source continuity. Detect mutation, truncation,
   replacement and truncate/regrow; never relocate by similar text. Codex's current
   protocol can share sessionId across forked threads; verify installed semantics.
4. Defer an incomplete final record, diagnose malformed complete records, and record
   renderer version, source generation and last complete boundary. Compare incremental
   results against full rebuilds. Generated output and its map must represent the same
   generation, with one serialized publisher. No half-written reading file is exposed.
5. Default to a stable snapshot while reading. Explicit refresh re-resolves the same
   source bookmark, or reports loss; new output must not silently move the reader.
   Automatic tailing/paging and viewport restoration are later work. Full-history
   snapshot costs are measured before inventing a cache service or editor integration.
6. An approval block shows the observed request, timestamp, source reference and
   correlated resolution when known; otherwise outcome unknown. Missing evidence is
   not a negative decision. Historical text never claims current answerability.
7. Minimum interaction: a generated approval reference opens its exact local source
   location using the existing editor file-address mechanism. Use a synthetic or
   sanitized source in the UI witness. Witness this feature in Sublime; a formatted
   path alone is not an interaction PASS. Navigation to an already-running native
   session is a separate optional capability, requiring checked target identity and
   an existing view-only action. If unavailable, show that honestly; do not invent a
   working button, approve/deny control, shell link, transport or app-server resume.
8. Keep generated text separate from operator notes. Bookmarks may reference notes,
   but this session builds no note service. Derived cache is disposable only while its
   retained source supports rebuild. Missing source must be visible. No reboot cleanup,
   retention daemon or deletion of native history belongs to this gate.

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

## prompt-0 — Cartan, working head

```text
Use $medusa in /home/hruzam/unikuklatrix/nablarva.
Read /home/hruzam/unikuklatrix/nablarva/AGENTS.md and its required read order,
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md,
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/STATUS.md,
and /home/hruzam/reposoma/raw.guides/status/GUIDE.md.
You are Cartan, sole status_owner and integration owner. Resolve actual host,
worktree, permissions and overlapping work, then run the STATUS recovery probe.
Read the three raw inputs named in References and only the source/canon needed.
Use the surgical-coding skill for implementation. Check native export/navigation
and installed vendor versions first; retain an existing facility if it meets the
gate. Do not re-run broad research or consume real transcript/pin stores casually.

Own this bed's STATUS, evidence, UI PAD and final REPORT; preserve existing raw files.
Stage 1: qualify one synthetic fixture, canonical projection and stable pins, using
explicit vendor/source. Freeze expected exchanges before implementation results.
Stage 2: qualify both installed vendor adapters, adversarial identity/lifecycle
cases, the selector and inert zsh surface. Use sanitized fixtures; isolated native
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
prompt disambiguation, and the CLI still answering after the editor closes.
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
- Cleanup on reboot, background watchers, automatic paging, note service and
  autonomous native-session discovery/attachment remain later work.

## Acceptance evidence

| Claim | Required witness |
|---|---|
| Existing facilities and boundaries | Installed versions, native export/navigation comparison, exact source inputs, existing pin-plugin inspection, naming sweep and retired-by-native condition. |
| Conversation fidelity | Per-vendor/version fixtures with frozen expected conversation, multiline/code, duplicate-looking prompts, duplicate representations, unsupported records, partial final line, malformed complete line and branch/compaction cases. |
| Stable pins | Correct source-to-line mapping after cold rebuild, append and resume; isolation across two conversations and colliding project basenames; explicit failure after invalidating mutation/truncation/replacement/regrow or source loss. |
| zsh entry | Direct Python and source-relative shell invocation agree; keyboard has aliases/comments only; repeated source has no I/O/process/editor effects; ordinary errors are actionable; composer regression checks remain green if shared files are proposed for promotion. |
| Temporary layout | Witness the authorized project/bed/agentive-session layout, collision checks, metadata/source-map consistency, complete publication and cache rebuild. An override-only test cannot qualify the actual temporary home. |
| Editor interaction | Operator witnesses new window and correct exchange, including already-open-file case; actual approval source-reference navigation; source-vs-editor pin distinction; native CLI continues and survives view closure. |
| Approval truth | Request/time/provenance, correlated resolution or explicit unknown; no live-pending claim from history alone; unavailable source fields and native target navigation clearly marked. |
| Performance | On home, record fixture bytes/turns and small/large cold full-render time, warm pin lookup and peak memory with exact commands. Record the operator's usable/unusable judgment; do not import composer budgets or fabricate a paging threshold. |
| Review and return | Independent verifier result, fresh Houston finding, disposition of every material finding, concrete ia-sync source/wiring/activation proposal and Majkee GO/STOP. |

Cartan stores redacted evidence in this bed on demand and returns one REPORT with
adopt / reject / operator decision clearly separated. It includes exact commands,
input/output fixture pair, working pin, lifecycle/approval capability matrix and
timings. Unavailable runtime/GUI evidence remains UNVERIFIED and prevents a GO
claim for that capability. Follow the shared closure law; promotion, observations
and pruning are separately authorized effects, never an automatic cleanup step.

## References

- `/home/hruzam/unikuklatrix/nablarva/AGENTS.md`, `.dev/session/flag.md`, `.dev/session/pulse.md`, `PROJECT.yaml` — repository authority and router (read from this absolute repository root).
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md` — observation/view, L8 placement and section 4.8 configuration direction.
- `/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md` and `/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md` — separate observer and composition contracts.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/termbrana-M0-transcript-view.cli-handoff.md` — Wave's proposal, not a build release by itself.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/raw/majkee-cartan-log.md` — versioned approval findings and explicit gaps.
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
