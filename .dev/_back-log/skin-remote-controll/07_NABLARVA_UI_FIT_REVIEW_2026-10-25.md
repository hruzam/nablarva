---
title: "nabLarva — repository-grounded UI and integration fit review"
date: '2026-10-25'
author: Wave
language: en
type: architecture review and handoff addendum
status: advisory; no project decision or implementation release
repository: hruzam/nablarva
branch: core
commit: fe64b099156ed96836256e82273f5f394545a4d8
commit_date_utc: '2026-10-24T00:24:41Z'
review_mode: read-only remote snapshot
runtime_validation: not performed
supersedes: application of the generic 2026-10-23 workspace recommendations where this review identifies a conflict
---

# nabLarva — UI and integration fit review

## 1. Verdict

**The earlier direction fits, but the proposed component boundaries need correction.**

A native UI is a credible presentation layer for nabLarva. It should not become a second session manager, a new relay, or a replacement for Termbrana's composition family. RustDesk is not justified as the foundation of the project by the requirements reviewed here.

My preferred decision split is:

- **Structured workbench, composition, navigation and observation:** evaluate Slint with Rust or C++ while retaining existing native terminals.
- **A desktop workbench that must contain a fully interactive terminal:** evaluate Qt + QTermWidget against that concrete requirement before choosing custom terminal integration.
- **Mobile:** retain the unresolved terminal-versus-cards choice. Slint supports Android, but toolkit support does not qualify keyboard behaviour, reconnection, lifecycle or the selected phone design.

These are engineering judgments, not approved project choices or measured performance rankings. The project-wide implementation language remains open; Rust in one frontend would not settle it.[^contract][^flag][^slint][^android][^qterm]

## 2. Scope and authority

I inspected the remote `core` snapshot pinned above, prioritizing `docs/ARCHITECTURE.md`, `docs/organs/stridularium.md`, `PROJECT-DESIGN.md`, the governing flag, the pulse router, relevant session statuses, Termbrana's README, and the opening 145 lines of its Zellij probe source. I also read the prior downloadable relay/UI/handoff briefs and checked current official Slint and Qt/QTermWidget documentation.

This is not a complete code audit. I did not inspect the live `ia-sync` source checkout, workstation configuration, uncommitted work, runtime processes or device behaviour. Recorded test results below belong to the repository's authors; I did not rerun them.

Authority matters here:

- `flag.md` governs durable decisions, including later amendments.
- `pulse.md` routes to the session `STATUS.md` that owns current work state.
- Architecture and component documents describe the system, but their proposals and historical wording must not override newer locks or status receipts.[^agents][^flag][^pulse]

**L21 is decisive.** It amends L17 to allow shared process/API/CLI/subscription layers and a coherent UI framework, while retaining independently useful clients. Phase 0 did not authorize implementation of that shared framework or a transport. It is therefore wrong both to forbid shared UI design and to treat it as already released for implementation.[^flag]

## 3. What the repository already assigns

| Responsibility | Existing owner or direction | Consequence for a new UI |
|---|---|---|
| View, layout and protected process lifetime | ovitmugen, under L17 | Use its boundaries; do not add a parallel lifecycle controller. |
| Composition | Termbrana composition family, sourced in `ia-sync/zsh/termbrana/` | Reuse the validator and its byte contract; do not replace it with GUI string processing. |
| Zellij observation | Termbrana observer at `toolbox/termbrana/` | Respect its read-only default, host boundary and separate milestones. |
| Observation principle | VIST, under L20; concrete protocol not adopted | Show provenance without inventing one global event schema. |
| Observation lab | termpanum | Its proposed observations are evidence, not authority to act. |
| Regulated room delivery | stridulatrix direction; delivery research and qualification remain gates | A frontend may eventually request an authorized action; it must not implement a hidden shortcut. |
| Mobile human interface | stridularium | Host-resident processes, app-scoped phone reach, detach without closing a bed. |

The first three are not one interchangeable “Termbrana panel.” Shared presentation is possible without moving their ownership into the UI.[^flag][^architecture][^design][^termbrana][^phone]

## 4. Recorded implementation state versus design

| Area | Evidence in the inspected snapshot | Do not assume |
|---|---|---|
| ovitmugen | `ovitmugen-01-basement/STATUS.md` records a tested baseline and says nothing of gate 01 is built. | The proposed versioned map, action journal and remembered-bed files already exist. |
| Composition | `composer-01-parse/STATUS.md` records Phase 0 PASS, preservation commits and a parked sourcing continuation. | A released loader, picker, editor integration or delivery adapter. |
| Termbrana observer | README and probe source identify an M0 truth-spike harness; core, review UI, persistence and replay remain planned. | A semantic terminal MVP ready to embed in another frontend. |
| Mobile | A working design wrapper preserves competing terminal/cards approaches. | An accepted mobile UI architecture or created app implementation. |
| Whole application | `PROJECT.yaml` still leaves the v1 language undecided. | Rust, C++, a GUI toolkit or a common runtime has been chosen for the whole system. |

The practical lesson is to consume interfaces that exist and use clearly labelled fixtures for ones still proposed. A diagram must not silently turn a planned producer into a working dependency.[^ovstatus][^composerstatus][^termbrana][^probe][^phone][^contract]

## 5. Disposition of the previous recommendations

| Earlier suggestion | Repository-grounded disposition |
|---|---|
| Keep execution on the workstation and make the client disposable | **Keep.** It matches the phone/session and protected-lifetime boundaries. |
| Preserve files and avoid a remote-desktop transport for text relay | **Keep, with precision.** The room's single-writer journal, component logs, payload files and UI caches have different roles; not every file is room truth. |
| Build a small Slint companion panel | **Keep as a candidate, change its scope.** It can present existing organ capabilities within a coherent workbench, rather than introduce another uncoordinated panel. |
| Start by discovering sessions directly through tmux | **Prefer the existing ovitmugen boundary.** Direct tmux access is an implementation detail to inspect, not the default new owner of the session map. |
| Use tmux control mode | **Potential observation/view implementation only.** It is not the room protocol, a source of agent identity, or permission to write. It is not required for a first UI evaluation. |
| Use `send-keys` as the ordinary automated delivery leg | **Reject for regulated relay.** L4 records its rejection. L17's human-operated editor/pipe/tmux direction is a distinct, unqualified seam, not a blanket exception. |
| Keep every tool in a narrowly separate UI | **Revise.** L21 permits coherent shared UI and shared mechanisms while tools remain independently usable. |
| Qt + QTermWidget for an embedded desktop terminal | **Keep as a serious alternative.** Attach a viewer to the existing session; do not make it own agent lifetime. |
| Extract RustDesk components or introduce its transport | **No demonstrated core need.** Keep desktop remote access separate unless a concrete screen-control requirement emerges. |
| Adopt tmate/WezTerm as a replacement session platform | **Not justified by this review.** Optional human tools are not reasons to migrate nabLarva's session ownership. |
| Require relay Phase B before evaluating a GUI | **Remove that dependency.** Read-only UI and inert composition evaluation can proceed independently of regulated delivery, under their own authorization. |

These dispositions qualify the generic pack rather than changing repository law. In particular, the earlier `05_IMPLEMENTATION_HANDOFF.md` must not be used as a ready-to-run nabLarva work order without this reconciliation.[^flag][^architecture][^ovdesign][^ovstatus][^termbrana]

## 6. A UI shape that fits

This is a proposed presentation structure, not a released API or implementation:

```text
Desktop workbench                  Phone client
          \                         /
           shared interaction meanings
           and explicitly owned contracts
                         |
       available CLI/file interfaces; fixtures for gaps
          /              |              |               
  view/navigation    composition    observations     delivery request
          |              |              |               |
     ovitmugen       Termbrana      graded sources   qualified owner
  protected life    validation      / projections    only when released
          |                                             |
     existing sessions                        regulated session delivery

Native terminal access remains available independently.
Closing a viewer is not a session-destruction command.
```

“Shared interaction meanings” is not a proposal for a new central authority. A common shell can provide consistent focus, navigation, source selectors and command presentation while invoking the proper owner for each effect.

Likewise, a common visual design does not require one permanently running monolith. L21 permits shared mechanisms; it does not require waking the whole animal to use one tool.[^flag]

For a first desktop view, I would use an existing-session navigator, a composition/inspection area, and an observation/result area. Native terminal access would remain an explicit action. This is a proposed layout, not a replacement for the existing ovitmugen horizontal/vertical layout decisions.[^ovdesign]

## 7. Toolkit comparison for these requirements

### Slint + Rust or C++

Official documentation provides the declarative UI language, layouts, data models, callbacks, custom controls and language integrations. This makes Slint a plausible host for structured session lists, source selectors, composition controls and provenance-labelled records.[^slint]

The fit is strongest when the application presents structured state rather than recreating a terminal. I have not established a ready-made, project-qualified Slint terminal integration. A text preview is not an interactive terminal emulator, and a Rust terminal core would still require integration and validation.

Slint's Android documentation covers both Rust and C++. Its mobile guidance explicitly requires application-level work for touch scrolling, keyboard accommodation and layout. Therefore, “Slint supports Android” is useful evidence, not a completed mobile-product decision.[^android][^mobile]

**My lean:** Slint for a structured desktop workbench and a possible cards/composition phone client, with independent acceptance tests on the actual devices.

### Qt + QTermWidget

QTermWidget is an embeddable Qt 6 terminal emulator. Its README explicitly lists BSD, Linux and OS X compatibility and a GPLv2-or-later project licence. That gives the desktop option an existing terminal component to qualify rather than a terminal to build.[^qterm]

For nabLarva, test it as the viewer of a persistent session. The terminal widget may own its viewer-side child process; the agent and broker must not become children whose lifetime ends with the GUI. Verify this on disposable sessions rather than assuming attachment is harmless.

Qt itself supports Android. That does **not** prove that QTermWidget provides a supported Android terminal path; the two claims must be kept separate.[^qtandroid][^qterm]

**My lean:** strongest alternative when the accepted desktop requirement is one window containing a real terminal. This is not a measured resource comparison or a licence-compatibility determination.

### Existing terminal/editor integration

The current wrapper explicitly permits useful zsh-layer increments while separate UI versus IDE integration remains open. Extending the existing surfaces is therefore a valid first increment, not a failure to build the “real app.”[^design]

A coherent command vocabulary and a cleaner navigation/composition path can be proved before selecting a GUI toolkit. That also provides the behaviour against which a graphical prototype should compete.

## 8. Requirements the UI must not erase

### 8.1 Payload bytes versus editable text

L17's approved grammar preserves the opaque body and its EOL. The display representation and the authoritative prepared payload should therefore be separate. Do not silently normalize line endings, whitespace or encoding on a view-only round trip. A deliberate edit must produce an explicitly revalidated draft.[^flag]

The same lock excludes `program` and `function` from allowed packet headers. A future picker must not invent new wire fields merely because the UI has a convenient dropdown. Any required metadata extension belongs to the owning contract.

### 8.2 Navigation identity versus delivery identity

Ovitmugen's map proposal distinguishes adapter details from its neutral navigation key and does not claim to identify the agent. A selected row is not proof that the same receiver is still present. Future delivery must use the checked binding and authority required by its own qualified contract.[^ovdesign][^flag]

Do not independently invent a final addressing schema inside the GUI. Show ambiguity and stale bindings; do not silently choose another pane.

### 8.3 Observation grade versus task state

Termbrana distinguishes `rendered_text`, `rendered_ansi`, `derived`, and a separately gated future `raw_pty` path. A UI must retain these distinctions. A tmux/Zellij view must not be relabelled as original PTY capture or complete conversation history.[^termbrana]

Likewise, connection, observed activity, possible input readiness, delivery and accepted task outcome are different facts. A badge or idle screen cannot create delivery permission or acceptance. L20 leaves the event envelope unadopted.[^flag]

### 8.4 Keys and focus

The shared KEYS CODE supplies meanings and reserves the frame/agent prefixes. Its navigation shortcuts belong to organ views, not to text-entry fields or the focused live terminal.[^architecture]

A GUI implementation should prove that typing `j`, `k`, `q`, `/` or `x` in a composition field inserts text rather than triggering navigation or removal. The corresponding terminal input must reach the terminal. Touch affordances should preserve the same action semantics without pretending the desktop keystrokes are a mobile design.

### 8.5 Close, disconnect and replay

View closure must not be implemented as process destruction. Lost connectivity should invalidate observations and affected bindings, not replay a previous delivery action. The phone remains an app-scoped client of host-resident processes.[^flag][^phone]

## 9. Documentation drift found

These are read-only findings, not edits or new locks:

1. `docs/ARCHITECTURE.md` retains a DRAFT r7/not-promoted header and describes the L17/P5 shared-framework tension as unresolved. `flag.md` L21 records the adopted amendment and a promotion pin. Read the architecture through L21; a future authorized reconciliation should update the stale framing without reopening the decision.[^architecture][^flag]
2. Termbrana's README still repeats the earlier narrow-integration wording. Apply L21 to the superseded phrases rather than treating the README as a later prohibition.[^termbrana][^flag]
3. Termbrana's README says the Phase 0 qualification evidence is uncommitted and awaits preservation. The owning Composer STATUS records completed preservation commits and pushes, while explicitly retaining the parked continuation and no deployment. The preservation wording has advanced; sourcing and delivery have not.[^termbrana][^composerstatus]

These differences matter because an agent reading only the overview could either forbid a permitted UI direction or assume unfinished work is ready to consume.

## 10. Recommended next experiment

**Proposed scope:** one read-only frontend slice, using existing interfaces where verified and explicitly labelled fixtures elsewhere. This review does not release it for execution.

Select one existing bed, inspect associated files, show a packet without changing it, and open its native terminal through the existing view boundary. Do not add a transport, a room journal, a session database, a sourcing system or a new observation protocol.

For the structured-UI branch, prototype the same workflow in Slint. For the terminal-in-window branch, qualify QTermWidget against an actual disposable tmux session. There is no need to implement both complete products before learning which requirement dominates.

### Planned acceptance checks

| Check | Required evidence |
|---|---|
| Standalone use | A useful tool/view runs without starting the room broker or whole application. |
| Lifetime | Viewer close, crash and reconnect leave the original process intact. |
| Ownership | View actions route through the view owner; observation and composition do not send. |
| Payload fidelity | Viewing/validating an existing packet preserves body bytes and EOL; explicit edits are revalidated. |
| Focus | Navigation shortcuts do not steal composition or terminal keystrokes. |
| Provenance | Source, grade, freshness and missing/uncertain state are visible and truthful. |
| Stale targets | Changed identity or missing target is visible; no fallback delivery or replay. |
| Layout | Representative horizontal and vertical desktop layouts are usable. |
| Mobile, when in scope | Actual-device keyboard, text selection, background/resume, rotation and reconnect are tested. |
| Resources | Compare startup, process-tree memory, CPU and responsiveness using equivalent workflows, not empty windows. |

Inspect the live `ia-sync` implementations and local diffs before writing an adapter. The map/events design is not a licence to implement the entire parked basement or sourcing gate as an incidental UI dependency.

## 11. AI HANDOFF

**Goal:** Determine how the earlier remote-workspace/UI recommendations fit the actual nabLarva architecture.

**Current state:** Read-only review of `core` at `fe64b099156ed96836256e82273f5f394545a4d8`; relevant governing documents, component docs, statuses and a probe-source excerpt inspected. No repository or workstation mutation.

**Decisions made:** None adopted. Recommendations: preserve existing owners; apply L21; evaluate Slint for structured views, Qt/QTermWidget for a terminal-centred desktop, and keep RustDesk outside the core. Remove delivery as an unnecessary prerequisite for a read-only UI experiment.

**Files changed:** One new conversation artifact, `07_NABLARVA_UI_FIT_REVIEW_2026-10-25.md`. The original seven-document pack and GitHub repository were not edited.

**Validation performed:** Repository source inspection and official toolkit documentation checks. Markdown metadata, heading/fence structure and source-reference consistency checked locally. No build, application test, benchmark, device test, source checkout validation or live session inspection performed.

**Open questions / risks:** Terminal-in-window versus structured companion UI; phone terminal versus cards; concrete shared-layer contracts; qualified delivery; actual deployed source; payload/keyboard/device behaviour; resource use and dependency licensing.

**Recommended next move:** Choose the required UI experience, inspect the existing `ia-sync` boundaries, and authorize only the matching read-only/fixture-backed prototype. Keep parked delivery/sourcing work parked unless separately released.

**Agent:** Wave

## 12. Sources

Repository links below are pinned to the inspected commit. External toolkit documentation was accessed for this review; its `latest` URLs can change. No source declaration is a substitute for a runtime test.

[^agents]: [AGENTS.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/AGENTS.md)

[^flag]: [.dev/session/flag.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/.dev/session/flag.md)

[^pulse]: [.dev/session/pulse.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/.dev/session/pulse.md)

[^contract]: [PROJECT.yaml](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/PROJECT.yaml)

[^architecture]: [docs/ARCHITECTURE.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/docs/ARCHITECTURE.md)

[^design]: [PROJECT-DESIGN.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/PROJECT-DESIGN.md)

[^phone]: [docs/organs/stridularium.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/docs/organs/stridularium.md)

[^termbrana]: [toolbox/termbrana/README.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/toolbox/termbrana/README.md)

[^ovstatus]: [.dev/session/ovitmugen-01-basement/STATUS.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/.dev/session/ovitmugen-01-basement/STATUS.md)

[^ovdesign]: [.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md)

[^composerstatus]: [.dev/session/composer-01-parse/STATUS.md](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/.dev/session/composer-01-parse/STATUS.md)

[^probe]: [toolbox/termbrana/crates/termbrana-zellij/src/main.rs](https://github.com/hruzam/nablarva/blob/fe64b099156ed96836256e82273f5f394545a4d8/toolbox/termbrana/crates/termbrana-zellij/src/main.rs)

[^slint]: [Slint guide and language integrations](https://docs.slint.dev/latest/docs/slint/).

[^android]: [Slint Android guide](https://docs.slint.dev/latest/docs/slint/guide/platforms/mobile/android/).

[^mobile]: [Slint mobile development considerations](https://docs.slint.dev/latest/docs/slint/guide/platforms/mobile/general/).

[^qterm]: [QTermWidget official README: purpose, platform coverage, licence and API](https://github.com/lxqt/qtermwidget).

[^qtandroid]: [Qt for Android](https://doc.qt.io/qt-6/android.html).
