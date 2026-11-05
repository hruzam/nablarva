# RUNBOOK: phone-console-01-browser

```yaml
goal: >-
  Deliver a small vendor-neutral browser console for Majkee's existing workstation
  sessions, with a usable Redmi terminal, durable composer and shared prompts/files
  vault, using replaceable components that can later extend Nablarva.
gate: >-
  Majkee records GO or STOP on the independently verified Redmi/office browser-console
  pilot after session navigation and guarded lifecycle, scrolling and keys, durable
  drafts/tray, explicit paste/submit, native permission interaction, shared vault
  access and detach/reconnect are demonstrated, installation/recovery evidence is
  recorded, and Houston's post-build project-documentation findings are dispositioned.
participant_1: [cartan, {brand: codex, model: terra, effort: high}, {host: office, role: execution head and integration owner}]
participant_2: [astrobley, {brand: codex, model: gpt-6.1-sol, effort: high}, {host: office, role: senior terminal and host integration}]
participant_3: [terra-ui, {brand: codex, model: terra, effort: high}, {host: office, role: bounded browser UI implementation}]
participant_4: [terra-vault, {brand: codex, model: terra, effort: high}, {host: office, role: bounded draft and vault implementation}]
participant_5: [cartan-test, {brand: codex, model: terra, effort: high}, {host: office, role: fresh independent qualification controller}]
participant_6: [crawl-web, {brand: codex, model: terra, effort: medium}, {host: office, role: bounded automated browser and fixture checks}]
participant_7: [houston, {brand: codex, model: gpt-6.1-sol, effort: high}, {host: office, role: bounded architecture and documentation consultation}]
participant_8: [majkee, {brand: human, model: none, effort: none}, {host: office-and-redmi, role: physical usability witness and acceptance}]
status_owner: cartan
observations_read: none exist
```

Oraculum authored this planning handoff at Majkee's request on 2026-10-30.
The `phone-console*` predecessor observation search was empty. Model grades above
are routing recommendations; the head records actual native roles, model handles
and availability at dispatch. No executor is started by authoring this RUNBOOK.

## Why this session exists

Majkee wants a fast usable bridge, with good interfaces for later reuse. The native
Android design is retained as a future option. Start with an existing browser
terminal such as ttyd and build the small missing mobile surface around it. Code
belongs in Nablarva as an independently buildable component; ia-sync owns reviewed
deployment and machine/device wiring. This is a bounded pilot, with one acceptance
decision, rather than a restart of the closed whole-app architecture session 03.

## Fixed scope and build order

1. **Establish the existing-session loop first.** Qualify an upstream terminal
   gateway on a disposable office workbench and the actual Redmi: terminal input,
   scrollback, IME/Unicode, special keys, independent phone selection, explicit
   paste/Enter, a harmless native permission prompt and detach/reconnect. Confirm
   ttyd's selected version, licensing, frontend extension boundary and reconnect
   semantics; do not assume iframe access or an internal JavaScript object is a
   supported API. If the terminal fails the physical usability trial, return the
   evidence before investing in the surrounding UI or changing the gate.
2. **Add the usable shell.** Host/session/window/pane picker; plain multiline
   editor; at most ten primary command buttons plus an expandable key palette;
   named create/end operations with protected host lifetime. Workbench creation,
   agent start, detach, agent end and vault-entry creation are distinct effects.
3. **Persist drafts and a small vault.** Unsent drafts survive ordinary app/browser
   switching and restart. Temporary tray supports manual clear or 30-minute expiry;
   saved vault items persist until deliberate deletion. Vault means shortcuts,
   prompts and files, with history separate. Use explicit save/load and visible
   revision conflicts for the first version rather than a general sync engine.
4. **Qualify, install narrowly, document.** Freeze the candidate for independent
   checks, prepare/review the scoped ia-sync install and rollback, demonstrate the
   real phone loop, then call Houston again for project-documentation integration.
   Majkee records the gate verdict on the evidence and actual advertised scope.

The pilot is office + Redmi. Home is a later repeat of host-dependent checks, not
an inferred PASS. Keyboard dictation may be used if the actual input method supports
it; custom STT/TTS, contextual rewriting and Ukrainian support remain later adapters.
Czech Unicode input is required in the terminal/draft test. The native Android,
Docker and Kubernetes options stay in the retained backlog, not in pilot prerequisites.

## Existing substrate and golden-rule check

Reuse ovitmugen's `ls --json` and guarded lifecycle operations. It has no released
general prompt-delivery API. Its shared `--left` selection is not an independent
phone view; coordinate a small owner-aligned extension rather than silently moving
the desktop selection. Reuse remote-cli fit/wide/scroll/status controls where suitable.
Those deployed office sources matched ia-sync on 2026-10-30; this is byte equality,
not fresh functional qualification. The later Redmi log supersedes the old missing-key
handoff; the current phone and host configuration still need rechecking.

Evaluate ttyd as an external dependency before writing a terminal transport. The
installed Codex CLI 0.166.0 exposes an experimental `remote-control` command; its
presence does not meet the vendor-neutral requirement or prove phone functionality.
Do not repeat the older claim that Codex has no remote-control surface. A maintained
vendor-neutral terminal offering the missing composer/vault controls could retire
our custom UI/adapter; recheck that bounded alternative before building the delta.

Termbrana currently offers inert check/parse, not a renderer, source picker or sender.
Plain editing belongs to the phone; future structured preparation aligns with that
family. Human input travels through the attached PTY. Future regulated room delivery
belongs to stridulatrix. Planned VIST/spine records are not usable APIs today; the
phone must not invent a competing observer, address registry or event bus.

## Ownership and delegation

The head fixes public contracts before parallel writes. Proposed component home:
`/home/hruzam/unikuklatrix/nablarva/apps/session-console/`. Perform the final naming
and dependency-collision check before creating it; no public package name is claimed.

| Seat | Initial file/responsibility boundary |
|---|---|
| cartan | This STATUS, worker briefs, integration, contract decisions inside the granted scope, build entry and evidence disposition. Own `contracts/` after senior proposal review. |
| astrobley | `host/` and the terminal-transport frontend module assigned by Cartan; propose contracts before consumers implement. Scoped ovitmugen/ia-sync changes only after overlap and publication review. |
| terra-ui | Browser navigation, composer presentation and key palette under a named `web/` subset; excludes the transport module and storage adapter. |
| terra-vault | Named storage-adapter subset of `web/`, plus vault persistence module assigned under `host/`; excluded from Astrobley's writes before dispatch. |
| cartan-test | Independent qualification and its test fixtures/evidence; no changes to application code. |
| crawl-web | Narrow browser traversals and fixture checks assigned by cartan-test/head; no fixes or real-session destructive actions. |
| houston | Bounded consult; after implementation, documentation-fit findings or explicitly assigned audit mechanics. Never STATUS or implementation acceptance. |

Do not launch both host writers with overlapping ownership. Worker briefs give exact
files and say that other writers are active and their changes must be preserved.
Use native in-window delegation; no cross-vendor transport or full-session fanout is
needed. Reuse the normal Terra implementer/worker; do not create a global crawl-bot
role. `cartan-test` must be a fresh context, distinct from the integration head.

## prompt-0 — cartan

###### prompt

```text
Use $medusa as fresh Cartan, preferably Terra/high. Work from
/home/hruzam/unikuklatrix/nablarva. Read its AGENTS.md, .dev/session/flag.md,
.dev/session/pulse.md and PROJECT.yaml, then
/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md
and its STATUS.md. You own this session's STATUS as cartan. Follow the current
next action; do not restart planning or dispatch every participant at once.
First establish the current host/worktree/device/transport baseline and assign the
bounded existing-session terminal trial to Astrobley. Use native Terra workers for
bounded UI/storage work only after interfaces and disjoint file ownership are fixed.
Keep the first build browser-based and vendor-neutral. Preserve unrelated changes.
The inherited evidence and exact acceptance schedule are referenced below; read them
as evidence, not proof of current device state. Use a fresh independent test seat.
After implementation and verification, call Houston with card: consult, or explicitly
bounded card: audit for documentation mechanics. Integrate its findings and present
the gate evidence to Majkee. No architecture/canon lock follows from your own verdict.
```

## prompt-1 — astrobley

###### prompt

```text
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md
and STATUS.md plus Cartan's exact file-scoped assignment. You are the senior executor
for the existing terminal gateway and host/session adapter. You are not alone in the
codebase: preserve other writers' work and avoid unassigned files. Qualify the narrow
Redmi/office terminal loop first; challenge a claimed API or mobile usability before
building on it. Propose the minimal contracts to Cartan; do not create another session
manager or room sender. Return changed paths, version/hash, actual tests and evidence,
limitations and one integration action. You do not own STATUS, canon or broad deployment.
```

## prompt-2 — terra-ui / terra-vault (one assignment per worker)

###### prompt

```text
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md
and your exact assignment from Cartan. Work only in its named files against the
accepted contracts. You are not alone: preserve other edits and report overlap before
writing. Implement the bounded UI OR storage slice assigned to you, with proportionate
behavioural tests. Return paths/diff summary, verification evidence and unresolved
limitations. Do not own STATUS, dispatch another team, widen transport authority,
commit, push or deploy. Missing contract decisions return to Cartan.
```

## prompt-3 — cartan-test / crawl-web

###### prompt

```text
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md,
its STATUS.md, the frozen candidate manifest, and
/home/hruzam/unikuklatrix/nablarva/meshup/stridularium.mobile-console.2026-09-29/raw/test-schedule.oraculum.2026-10-30.md.
Act as independent qualification, not the builder. cartan-test coordinates; crawl-web
performs only the assigned fixture/browser checks. Record actual automation capability;
a browser crawler cannot attest physical Android keyboard, microphone or lock-screen
behaviour. Use synthetic data and disposable workbenches. Do not fix app code or write
STATUS. Return PASS/FAIL/BLOCKED/NOT RUN per case with candidate hash and raw evidence.
Wrong target, lost acknowledged drafts, uncertain-input replay, unintended process
termination or incorrect approval binding fail qualification. Majkee witnesses usability.
```

## prompt-4 — houston, post-build documentation integration

###### prompt

```text
card: consult phone-console-01-browser post-build project-documentation integration
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md
and STATUS.md, then the supplied implementation/interface map, test and deployment
evidence. Check the actual result against current project owners and documentation
homes. Return fits/stretches/breaks and exact documentation changes, separating
implemented facts from deferred options. Preserve the native architecture table in
/home/hruzam/unikuklatrix/nablarva/.dev/_back-log/skin-remote-controll/08_PHONE_CONSOLE_DIRECTION_2026-10-30.md.
Correct stale project pointers in the proposed fold. Cartan retains integration and
STATUS. If explicitly assigned card: audit instead, restrict writes to the approved
documentation mechanics; no implementation, canon lock or self-verification.
```

## Known constraints and publication boundary

- Existing dirty Nablarva and ia-sync work belongs to other participants. Capture
  baseline and protect it; a worktree must deliberately carry these uncommitted
  planning references before being treated as a complete handoff.
- Ovitmugen-01, composer-01, X5 and termpanum have their own owners/gates. Reconcile
  overlap before any shared-source change; this session does not take their STATUS
  pens or claim their planned capabilities are built.
- Local build, disposable tests and bounded delegated implementation are the task.
  Publication follows L6 and ia-sync's reviewed path: prepare a concrete scoped
  install/rollback with evidence before applying changes to live host/device state.
  Do not turn ordinary reversible task work into repeated permission requests.
  New architectural locks, changed authentication/ACL scope or destructive live
  actions require the owning decision, not an inferred exception.
- Keep a browser terminal behind authenticated private access; validate HTTP and
  WebSocket authorization/origin binding. Do not expose a shell publicly, accept
  arbitrary URL commands or silently remove existing forced-SSH restrictions. A
  new HTTPS route may require a narrowly reviewed tailnet-access change; inspect
  current policy instead of assuming it exists from SSH reachability.
- No blind send-keys wrapper, hidden replay, session-name-only stale target binding,
  guessed approval state, whole-home file exposure or broad tmux cleanup. Keep
  native CLI approvals intact. Never read sealed `.hlm/` or `.majkee/`.
- No unsolicited commit/push, global deployment, phone reset, Termux replacement,
  Kubernetes, full native Android rewrite or new project harness.
- The head returns architectural/ownership curvature to Majkee/Oraculum with
  concrete alternatives; it does not reopen the whole project to settle a local choice.

## Acceptance evidence and closure

Use the linked independent schedule as the behavioural source. T0–T7 and T9 cover
the office pilot; T8 only covers speech actually advertised by this release. T10's
home repetition is deferred unless explicitly added without changing this gate.
Freeze the candidate and record versions, actual target IDs, expected vs observed
bytes/storage/process effects and screenshots/physical observations where relevant.
Use at least one real 30-minute expiry test and one screen-off interval of at least
10 minutes; the head can work while those intervals elapse. An inaccessible external
phone or missing test driver is BLOCKED evidence, not a simulated PASS.

The vault must be reachable from both phone and computer with the same acknowledged
saved revision. Draft persistence must include browser/process restart, reconnect
and denied persistent-storage requests. Retained terminal history is not promised
as the full vendor conversation. Demonstrate new/end on disposable targets and the
effect of shared window sizing on the desktop view.

After candidate verification, request Houston's documented follow-up, reconcile the
organ body, cross-organ architecture, wrapper pointers and actual ia-sync install
facts, and retain deferred native/container ideas in the backlog. The head reports
all failures/deferred features honestly and obtains Majkee's GO or STOP. Apply the
shared runbook closure/observation-preservation law; no automatic pruning or commit.

## References

- `/home/hruzam/unikuklatrix/nablarva/AGENTS.md`
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — locks, especially L6/L12/L14/L17–L24.
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md` — current seams and owners.
- `/home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md` — existing phone body; retired name retained as path.
- `/home/hruzam/unikuklatrix/nablarva/.dev/_back-log/skin-remote-controll/08_PHONE_CONSOLE_DIRECTION_2026-10-30.md` — operator-requested direction and retained table.
- `/home/hruzam/unikuklatrix/nablarva/.dev/_back-log/skin-remote-controll/09_V0_PHONE_EXTENSION_2026-10-30.md` — candidate v0 additions.
- `/home/hruzam/unikuklatrix/nablarva/meshup/stridularium.mobile-console.2026-09-29/raw/test-schedule.oraculum.2026-10-30.md` — independent test matrix and baseline evidence.
- `/home/hruzam/ia-sync/devices/redmi-15c-5g/device.md` and `/home/hruzam/ia-sync/devices/redmi-15c-5g/log.md` — device history, not current live proof.
- `/home/hruzam/ia-sync/zsh/remote-cli/README.md` and `/home/hruzam/ia-sync/zsh/session/ovitmugen.py` — existing implementation boundaries.
- `/home/hruzam/ia-sync/AGENTS.md` and `/home/hruzam/ia-sync/SYNC_DISCIPLINE.md` — source/publication rules before ia-sync changes.
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` and `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` — session/control-surface law.
- `/home/hruzam/.agents/skills/medusa/SKILL.md` — fresh working-head protocol.
- `https://github.com/tsl0922/ttyd` — upstream candidate; recheck selected release.
- `https://developer.mozilla.org/en-US/docs/Web/API/StorageManager/persist` — persistent browser storage is a request, not a guarantee.
