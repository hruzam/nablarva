---
artifact: ptyra-stenograph
date: 2026-09-17/18
event_typology:
  +: device marker (phone/pc) or recovery after repeat
  ?: uncertain attribution or wording; preserve uncertainty
  S1: notice a POINT / output / attention request
  S2: locate or open path / target UI
  S3: copy path or material
  S4: switch window / app / screen / arc / tab
  S5: paste
  S6: Enter / send / confirm
  S7: type anything extra / compose reply
  S8: notice RETURN / response exists
  S9: switch and tell / relay onward
  W: waiting / reading / thinking; not counted as carry
participants:
- Majkee: human gate / operator
- ptyra: stenographer
- Trajectory: Claude Code session in Arc "tunnel"
- Cartan: main Codex agent
- AstroBlade: Codex sub-agent, primarily observed through Cartan/main UI
recording_scope: continuous voice work observation
special_events:
  flush: emit stenograph artifact
  rewind: return to beginning while tape remains running
  X3: pause
  X4: resume
  X5: stop / end recording
status: flushed
stop_marker: X5
time_basis: elapsed session time as spoken by Majkee
time_quality: verbatim where stated; obvious chronology conflicts
  preserved and flagged
---

# ptyra stenograph --- continuous work record

> **Reader note --- concurrency / apparent duration**
>
> Majkee often keeps multiple sessions visible side-by-side in columns
> on a wide monitor. A short notification, Bash confirmation, completion
> notice, or other attention request may be handled with one or two
> clicks and then he immediately returns to the task already in
> progress. He may therefore inspect or service another session without
> a full context switch. The log can make operations look longer than
> they actually took because speaking every action while simultaneously
> reading, typing, deciding, and switching windows materially slows the
> human workflow. Where Majkee could not conveniently narrate every
> micro-action, the record preserves the higher-level action rather than
> inventing missing steps.

## Context carried into this segment

The live experiment is a first practical one-direction bridge from
Claude Code CLI to a living Codex session without MCP. Claude Code can
invoke a specific Bash mechanism that reaches the live Codex side. The
Codex endpoint was initially constrained/read-only as part of the test
cage. The next design problem is session selection: resume an existing
long-lived Codex session or create a new one, preferably behind a
tmux-backed script. A long-lived session preserves tunnel history but
risks token bloat and stale context.

The operator is comparing different session lifetimes and model-role
shapes. Claude Code is treated as benefiting from shorter sessions;
Codex has so far behaved well across longer sessions and compaction.
Trajectory is the Claude Code-side session discussing the tunnel/session
mechanism. In the Codex runbook arc, Cartan is the main agent and
AstroBlade a senior-coder sub-agent. AstroBlade normally speaks through
the main Codex UI; attribution can therefore be epistemically uncertain.

## Stenograph

### Earlier carry-over from the preceding voice slot

-   **\~1:46 elapsed --- W / S8.** In Arc Tunnel 10 / code-directory
    session, Majkee reads the agent output aloud/closely after a sent
    message.
-   **\~1:50 elapsed --- S4 → S6.** Switch to Arc Runbook / AstroBlade
    because a Bash confirmation is waiting. Presses `Y` / confirms, lets
    the process continue, then returns to the Arc tunnel/Trajectory
    work.
-   Voice input is deliberately avoided for the agent reply at this
    point so it does not interfere with ptyra logging; Majkee types
    instead.

### Pause and explanatory interlude

-   **1:54 --- S7.** Still replying to the Arc tunnel session /
    Trajectory report.
-   **1:55 --- X3 PAUSE.** Recording paused so Majkee can explain the
    work context to ptyra without mixing explanation with measured
    actions.
-   During pause, Majkee explains:
    -   Claude Code → Codex is currently a one-direction tunnel.
    -   It is the first genuinely useful live bridge in this experiment
        without MCP.
    -   Goal is a multisession, cross-brand CLI orchestration organism
        using his own thin/window tooling where possible.
    -   Codex endpoint was deliberately sandboxed/read-only during
        testing.
    -   Desired next step is a tmux-backed choice between resuming a
        known long-running Codex session and creating a fresh one.
    -   Long history is useful for reconstruction but can introduce
        token bloat/staleness.
    -   Trajectory is being consulted on this mechanism; sometimes
        Trajectory asks the Codex endpoint about Codex-specific
        behavior.
    -   Role/model economy matters: stronger reasoning for architecture;
        cheaper/middle models may be sufficient for implementation.

### Resume

-   **2:20 stated --- X4 RESUME.** Majkee resumes the measured process.\
    **? Time note:** subsequent spoken elapsed times go backward (2:10,
    2:12, etc.). They are preserved as spoken rather than silently
    corrected.

-   **after resume --- S7 → S6.** Reply to Trajectory is composed and
    sent.

-   **S4.** Switch to Arc Runbook.

-   **S8 / W.** Read AstroBlade/Codex response. Output is short/dense.

-   **S4.** Switch to tab 2, the runbook testing area.

-   **2:10 stated --- test.** Testing in tab 2.

-   **\~2:12 --- S4.** Result is good; application window/process is
    closed. Return to tab 1 / Arc Runbook / AstroBlade.

-   **2:15 --- S7.** Writing feedback in the UI.

-   **2:17 --- S6.** Feedback message sent.

-   **2:18 --- S4 → W.** Switch to Arc Tunnel / Trajectory and begin
    reading a longer response about maintaining sessions.

-   **2:19 --- interrupt / S4 → S6 → S4.** Temporarily switch to Arc
    Runbook / AstroBlade to approve a confirmation needed for tests,
    then return to Arc Tunnel / Trajectory.

-   **2:20 --- W.** Continue reading Trajectory output.

-   **2:25 --- S7.** Compose reply to Trajectory in terminal UI.

-   **message sent --- S6.**

-   **2:28 --- S4.** Switch, within the same terminal but another
    column/session, to Arc Runbook / AstroBlade.

-   **2:29 --- S8.** Read the response to the previous request.

-   **2:29 --- S4.** Switch to tab 2 testing area for a simple test.

-   **test sequence --- S7 / S6.** Set up the application window, issue
    command(s) in the testing terminal, click through several UI/tools,
    inspect behavior.

-   **2:32 --- test PASS.** Application behavior matches Majkee's
    intention. Close the terminal application and return to tab 1 / Arc
    Runbook.

-   **\~2:34 stated in speech as "two hours session, four minutes" ---
    S7.** Give positive completion feedback to AstroBlade and move
    toward the session's `/therapy` reflection mode.

### Therapy / sub-agent inheritance experiment

Majkee explains the local `/therapy` convention: at the end of a work
session, human and agent reflect on obligations, decisions, mistakes,
improvements, and the collaboration itself, with the metaphor of both
parties taking therapist/patient seats. The purpose is not merely
conversational: useful recurring lessons/scars can later be distilled
into a thin reincarnation/startup layer so future agent incarnations
inherit selected experience without loading the whole historical
context.

-   **S7 → S6.** Ask whether `/therapy` can operate with AstroBlade as a
    Codex sub-agent rather than only with Cartan, the main agent.
-   **W / S8.** Wait and observe the Codex UI while it searches/works
    out whether the skill is inherited by the sub-agent.
-   Initial indication: direct inheritance is uncertain; if the
    sub-agent cannot actually see the skill, having Cartan merely speak
    "on behalf of" AstroBlade risks becoming theater rather than genuine
    sub-agent reflection.
-   **2:38 stated --- S4 → W.** Because the therapy check may take time,
    switch to Arc Tunnel / Trajectory and read more terminal output.
-   **S4 / attention glance.** Majkee notices both sessions side-by-side
    in terminal columns. Small notifications can be serviced without
    abandoning the primary reading task.
-   **2:44 --- process note.** Majkee anticipates the voice slot may end
    soon and plans to use the remaining time, then flush a stenograph
    and begin another voice slot rather than be interrupted
    mid-recording.
-   **S4 → S8.** Switch back to Arc Runbook / AstroBlade to finish the
    shorter/easier job before returning to the deeper Trajectory work.
-   **problem observed.** AstroBlade, speaking through Cartan, reports
    that the new therapy skill is not visible to her. Possible remedy:
    finish/restart the Codex session so the skill is loaded, then test
    whether enough sub-agent memory survives through the main agent to
    perform meaningful therapy.
-   **2:46 --- S7.** An alternative is considered; Majkee types directly
    into the AstroBlade-facing UI.
-   Clarification logged: **Cartan and AstroBlade share the same
    Arc/session UI.** Cartan is the main Codex agent; AstroBlade is a
    sub-agent. Codex's native interaction normally surfaces the
    sub-agent through the main UI, although Majkee can sometimes
    address/break into the sub-agent directly. Thus "Cartan", "main
    agent", and "AstroBlade" may describe two voices in one visible
    session rather than separate windows.
-   **2:50 --- W / S8.** Waiting for and reading the therapy response.
-   AstroBlade asks an epistemic question. Majkee initially considers
    the content itself nonessential to the action log.
-   **2:52 --- recovery.** Voice session briefly drops for only a few
    seconds, then returns; no material work gap.
-   **2:52 --- S7.** Replying to AstroBlade in Arc Runbook. Majkee notes
    that maintaining exact arc/session names while simultaneously
    reading, reasoning, typing, and narrating is cognitively expensive.
    ptyra should preserve uncertainty rather than fabricate a name when
    attribution is unclear.
-   **2:59 --- S6.** Response to AstroBlade completed/sent; AstroBlade
    begins thinking.
-   Majkee explains the "reincarnation / scars" mechanism:
    -   therapy material is collected over sessions;
    -   recurring lessons can be distilled later;
    -   only a thin selected layer is inherited into a future
        incarnation/startup file;
    -   aim is to prevent repetitive mistakes and misunderstandings
        without context overload;
    -   the inherited layer can also encode practical knowledge of
        Majkee's working/communication habits;
    -   example discipline: do not merely believe that something is
        written somewhere---go inspect/read the file yourself.
-   **3:03 --- W / S8.** Read a larger-than-usual AstroBlade therapy
    output: what she "has on her heart" and what should enter therapy.
-   **3:07 --- S8 / ?.** Another Codex block arrives. Attribution is
    uncertain: probably Cartan for much of it, with possible AstroBlade
    portions indicated by UI color. Majkee can sometimes recognize
    AstroBlade by content/style but cannot reliably distinguish every
    utterance.
-   Discussion turns to whether Cartan and AstroBlade are too similar:
    -   Majkee was recently new to Codex sub-agent mechanics.
    -   Cartan is the main higher-reasoning agent coordinating
        sub-agents.
    -   AstroBlade was independently created as a
        senior-coder/implementer on a similarly capable model.
    -   Their model capability is therefore nearly the same; the
        practical distinction is mostly role/scope.
    -   In Claude Code, Majkee already uses a hierarchy where
        expensive/high-reasoning capacity handles
        architecture/escalation and middle models execute
        implementation, with one-shot stronger advice available when
        needed.
    -   Question for therapy: should AstroBlade become a
        lighter/middle-model implementer while Cartan remains the
        architecture/coordination brain?
-   **\~3:13 stated --- X? special pause.** Majkee pauses the measured
    action to ask ptyra for an opinion on the role/model split.
-   ptyra suggests treating it as a small empirical test: move
    AstroBlade toward the lighter implementation role on a bounded
    scenario and observe whether implementation quality and role
    separation remain sound.
-   **3:14 --- advisory interlude ends.**
-   **3:16 --- X4 RESUME.** Logging resumes.
-   **3:16 --- S7.** Continue typing the reply to Cartan/AstroBlade in
    Arc Runbook, incorporating the model-role question.
-   **3:18 --- X5 STOP.** Majkee explicitly ends this stenograph
    recording. He plans to switch out of voice mode, obtain the
    timestamped protocol, then start a separate voice session for a
    different purpose so voice-to-agent drafting does not contaminate
    the measurement log.

## Observations preserved for the next run

1.  **Do not infer a full context switch from every glance.**
    Side-by-side columns allow cheap attention checks and confirmations.
2.  **Reading/waiting is real work but not a carry.** Mark it `W`; do
    not inflate S-event counts.
3.  **Attribution inside Codex can be uncertain.** Cartan/main UI may
    relay AstroBlade; color or style is evidence, not proof. Use `?`
    where necessary.
4.  **Narration has measurement overhead.** The act of narrating can
    make the observed workflow materially slower, especially when typing
    and speech compete for attention.
5.  **Preserve spoken timestamps.** Do not repair contradictory elapsed
    times silently; flag them.
6.  **Therapy is part of the reincarnation mechanism.** It is intended
    to yield selected transferable experience/scars, not a full-session
    memory dump.
7.  **X5 is the stop boundary for this artifact.** `flush` means emit
    the stenograph output after the stop.

## End marker

**3:18 elapsed --- X5 STOP → FLUSH**

Recording closed by Majkee. No events after X5 belong to this
measurement artifact.
