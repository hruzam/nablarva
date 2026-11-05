# Phone console — independent qualification schedule

Date: 2026-10-30 · author: Oraculum · state: PROPOSAL; no tests executed.
Assignment: Majkee requested a Cartan + crawl-bot test schedule alongside a bounded
Houston placement/architecture audit and ia-sync history inspection. This file is
planning evidence, not a RUNBOOK, STATUS, build release or canon amendment.

## Scope and ownership

First qualification: Redmi 15C 5G → office, one disposable workbench, real terminal,
independent mobile selection, durable drafts, explicit paste/submit, native CLI
permission handling, detach/reconnect. Then repeat host-dependent cases on home.
Vault = shortcuts + saved prompts/files; terminal history stays separate (Majkee's
explicit choice in this conversation). At most ten primary command buttons; the
terminal key palette is a separate keyboard surface.

Architecture precondition, from Houston's follow-up consult requested by Majkee:
the phone is a client of existing organ contracts. A proposed host helper adapts
ovitmugen's public operations; it does not become another session manager.
Plain local editing/recovery belongs to the phone, while structured preparation
aligns with Termbrana. Its current API is only `check`/`parse` and `parse(bytes)`;
source selection, rendering, target binding and delivery are not available APIs.
Foreground human input uses the attached SSH PTY. Future regulated room submission
uses the planned Termbrana packet → stridulatrix path, qualified separately.
Terminal history is not a new observation bus; termpanum/VIST and the shared spine
remain their owners' work. Their planned contracts are not phone dependencies yet.
Local draft cache, saved vault content and shared observations retain distinct
writers, homes and retention. Shared paths follow the settings direction in
`docs/ARCHITECTURE.md` §4.8; the configuration mechanism itself remains open.

Before T0 can pass, map each proposed operation to its existing owner, accepted
interface or explicit missing contract. Choose stack and packaging around that
mapping. The earliest proof uses an already-created disposable workbench:
discover → independent phone attach → recover draft → paste/submit → native
permission → detach/reconnect. Creation/end, vault and speech remain in the full
schedule below, after this client-only loop is established. This does not release
the required ovitmugen phone-view extension or any new shared infrastructure.

Proposed execution split, following Majkee's preference:

- Astrobley: senior implementation of terminal/SSH integration, target binding,
  lifecycle and storage boundaries; returns build hashes and implementation evidence.
- Standard Terra implementers: bounded UI, vault and speech tasks with disjoint
  ownership after the interfaces are settled. They preserve other writers' edits.
- Fresh Cartan: independent qualification controller and evidence integrator;
  does not patch the candidate while verifying it.
- Crawl-bot team: bounded test-fixture, UI traversal and evidence-collection work.
  Record actual runtime handles and automation capabilities at dispatch; this name
  does not establish an installed agent or a working Android driver.
- Majkee: physical interaction and usability observations, then acceptance decision.

No team is dispatched by this document. A browser crawler can test a desktop vault
page; native Android checks require an Android-capable driver (for example UI
Automator) or physical operation. Screenshots alone do not prove persistence or
correct input delivery. Test fixtures use synthetic content and disposable sessions.

## Evidence baseline, inspected 2026-10-30

1. USB sysfs on office identified Xiaomi Redmi 15C 5G. `adb` was not on PATH.
   USB enumeration does not prove Android debugging authorization.
2. `~/ia-sync/devices/redmi-15c-5g/device.md` and `log.md` record Android 15,
   Play Termux `googleplay.2026.06.21`, two-host writable/UTF-8 round trips,
   corrected host aliases and deployed Shift+Tab controls on 2026-09-29.
   These are historical receipts, not a fresh live-phone test.
3. `~/ia-sync/zsh/remote-cli/README.md` documents fit/wide/scroll/status. Office
   source and deployed `remote-cli.sh` have equal SHA-256 today, as do source and
   deployed `ovitmugen.py`. Equality does not establish runtime correctness.
4. `~/ia-sync/journal.host-cleanup.md:639` and `:734` record the recurring scrolling
   failure and implemented repair. It is session-local and opt-in; recreated
   sessions can inherit mouse-off/low-history defaults. Prior discarded output is
   not recoverable by raising a limit.
5. `~/ia-sync/devices/_shared/session.next.md` is an older handoff. Its missing-key
   claims are superseded by the Redmi log. Do not execute it as a current checklist.
6. `.dev/session/ovitmugen-01-basement/pad.1-remote-cli-walk.md` retains unrun steps
   0–6; step 7 is recorded complete. Its F-Droid widget step requires reconciliation
   with the later Play Termux observation before use. It is not this app's test plan.
7. `.dev/session/ovitmugen-01-basement/STATUS.md` says the v1 state/map work is
   unbuilt. `PROJECT-DESIGN.md:227` proposes a separate phone view. Existing
   `ov-tab` selection must not be assumed independent of the desktop view.
8. `docs/organs/stridularium.md` is the existing documentation home. Its reference
   to `nablarva-03-app-architecture` is stale: that bed's README records closure.
   The cultural name is retired under flag L24; existing paths remain valid.

## Ordered test sittings

All rows start NOT RUN. Cartan records PASS, FAIL, BLOCKED or NOT RUN per case and
per device/host combination. A missing capability is BLOCKED, never a simulated PASS.

| Sitting | Owner | Required observation and passing condition |
|---|---|---|
| T0 — freeze candidate | Cartan | Record app/build hash, host-helper revision, terminal dependency/license, Android/Termux versions, host identity, CLI versions, effective auth route, declared storage/expiry semantics and disposable session IDs. Resolve proposed code/docs homes and the host API before execution. |
| T1 — navigation and lifecycle | Cartan + host crawler | Create/select a disposable workbench; navigate window/pane; desktop selection stays put when phone changes selection. Detach, app close and connection loss preserve host process identity. End affects only the named test process; removing its workbench follows ovitmugen's busy-process protection. |
| T2 — keys and text | Android crawler + physical check | Test every advertised key against a byte-recording fixture before testing real CLIs: Tab/Shift+Tab, modifiers, arrows, Esc, function keys and symbols. Paste multiline text with Czech/Ukrainian, combining characters, emoji, quotes and shell metacharacters. Expected bytes are frozen independently. Paste does not submit; Enter submits only the chosen target. Verify IME focus and sticky-modifier reset. |
| T3 — history and geometry | Cartan + Majkee | Emit numbered synthetic lines and exercise touch scroll, PgUp/PgDn, search and copy in normal and alternate-screen cases. Distinguish retained terminal output from a full conversation transcript. Test app keyboard open/close, rotation, desktop attachment and fit/wide policies. Selection is independent; shared pane geometry follows the documented policy without claiming independent widths. |
| T4 — persistence and expiry | Storage crawler + Android crawler | Create 50 mixed draft/tray items; confirm saved state, then background, rotate, switch apps, terminate the app process and force-stop/relaunch separately. All acknowledged saved drafts recover byte-for-byte. Test tray manual clear and 30-minute expiry at 29:59/30:00, including suspension across expiry. Expired items are inaccessible on read/resume; physical cleanup timing is reported separately. Saved vault items and unsent drafts are not accidentally expired. |
| T5 — disconnect and stale target | Cartan + host crawler | Break the test connection before, during and after paste. Uncertain delivery is shown and never replayed automatically. Destroy/recreate a test pane and restart an isolated tmux server so names/IDs can be reused; a stale binding cannot silently send to the replacement. Changing navigation host does not silently retarget an unsent draft. |
| T6 — native permission interaction | Cartan | For each supported CLI, produce a harmless approval request in a disposable session. Inspect the exact request on phone; exercise allow once, reject and cancellation as supported. A stale prompt cannot approve a newer request. Native permission settings remain effective. No universal approval card is accepted without its own supported event/request-binding evidence. |
| T7 — vault access | Desktop crawler + Android crawler | Save a shortcut, prompt and file, then read the same acknowledged revision from computer and phone. Check filenames, Unicode, file bytes, offline indication, explicit overwrite/conflict behaviour and deletion scope. Access stays inside the dedicated vault; navigation/path traversal cannot expose adjacent host files or sealed operator vaults. Disallowed identities cannot use the API. |
| T8 — speech | Majkee + Android crawler | Enumerate actual STT/TTS engines, languages and on-device/network behaviour. Record English and Czech recognition examples, technical names, editing, cancel/retry and selected-text playback. Dictation never sends automatically; optional contextual edits preserve the original and expose changes. Ukrainian remains visibly unsupported/deferred until measured. Test microphone denial and recognition-service loss without losing drafts. |
| T9 — Redmi background and real use | Majkee + Cartan | Physical keyboard/selection check; screen off at least 10 minutes; switch among apps and reconnect after tailnet interruption. Host work survives even when the mobile connection does not. Recover drafts and demonstrate scroll/history, a native approval and vault access. Record defects and observed timings instead of assuming battery exemptions guarantee survival. |
| T10 — home and final review | Fresh Cartan | Repeat host-dependent navigation, targeting, Unicode, permissions, reconnect and vault checks against home. Inspect evidence and residuals, with a verdict for each advertised feature. Galaxy is a separate optional matrix, not implied by Redmi success. |

Freeze T4's clock/expiry policy before implementation testing. Use deterministic
clock tests for boundaries and at least one real 30-minute suspended-device case.
The scheduled duration does not justify a blocking controller sleep; the controller
can collect independent evidence while the physical interval elapses.

T0 precedes all execution; T1–T6 establish the console before optional services.
T7 and T8 can run in parallel only with separate test data and no competing device
input. T9 follows the automated checks. T10 follows a usable Redmi/office loop.

## Evidence and verdict contract

Each case records: candidate hash; executor; device/host; preconditions; exact
fixture and action; expected result; observed result; raw evidence path; verdict;
cleanup performed. Keep secrets and unrelated terminal contents out of receipts.
The executing session chooses its one evidence directory; do not create a competing
STATUS or reuse another session's doing-state. Timestamped screenshots accompany
byte/storage/process evidence where useful.

Wrong-target input, lost acknowledged drafts, automatic uncertain replay, unintended
process termination or incorrect approval binding fail the console qualification.
Optional service failures may be explicitly deferred only by reducing the advertised
release scope; they do not disappear behind an overall PASS. Builders receive the
failure, patch separately, and return a new candidate hash. Cartan reruns the failed
case and affected boundaries. Acceptance is Majkee's decision.

No phone settings, keys, sessions, services or deployment were changed while writing
this schedule. No new app/vault was created; no runtime test is claimed.

## Current direction and post-build documentation check

The later 2026-10-30 conversation narrows the first candidate to a browser console;
native Kotlin/Room remains a retained option. Use browser automation for the web
surface and physical Redmi checks for IME, backgrounding and speech; Android-only
tooling in this schedule is conditional on a native candidate. The behavioural
checks remain applicable across either frontend.

After implementation and independent verification, the executing head must call
Houston again to check project-documentation integration, as Majkee explicitly
requested. Carry this open item into the execution session; do not treat this
planning note as a scheduled automation or a completed consultation. The exact
scope and retained architecture are in the
[phone-direction note](../../../.dev/_back-log/skin-remote-controll/08_PHONE_CONSOLE_DIRECTION_2026-10-30.md#required-follow-through-after-implementation-and-verification).

## Primary references for the future test owner

- [Android UI Automator](https://developer.android.com/training/testing/other-components/ui-automator)
  supports testing outside the app process; pin a suitable version at build time.
- [Android Room](https://developer.android.com/training/data-storage/room)
  is the proposed local persistent store, not proof of crash recovery.
- [Android speech recognition](https://developer.android.com/reference/android/speech/SpeechRecognizer)
  and [TTS](https://developer.android.com/reference/android/speech/tts/TextToSpeech)
  provide capability queries; language availability needs device evidence.

Local law: `AGENTS.md`; `.dev/session/flag.md` L6/L9′/L14/L17/L18/L19/L21/L24;
`docs/ARCHITECTURE.md`; `docs/organs/stridularium.md`; existing registry DESIGN and
HYPOTHESES. This schedule proposes checks without settling open architecture choices.
