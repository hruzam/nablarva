# RUNBOOK: Voice relay — inter-agent attention probe

```yaml
goal: Establish whether VOICE can serve as an inter-agent attention channel — the "how does one agent attract another" question — decoupled from PTY and from the dead send-keys anchor, using an STT-in leg and a TTS-out leg as the physical substrate.
gate: One observed round-trip — a live CLI agent session emits a name-addressed spoken utterance AND a second, independent live CLI agent session detects it, recognizes its own name, and reacts in-session (recorded as evidence) — OR a recorded verdict that the mechanism is infeasible on this stack, naming the specific blocker. Either outcome closes the probe.
participant_1: [majkee, {role: "operator — real mic, speaker, phone; owns the audio hardware, the human ear, and the gavel"}, host: "home"]
participant_2: [oraculum, {brand: "Claude Code", model: opus, effort: high, note: "NOMINATED driver — re-seatable by majkee at first sitting"}, host: "home"]
```

## Status of this file

Bed prepared 2026-09-16 by @Trajectory (ia-sync seat) at majkee's request, from a live
conversation that also scoped the two physical voice legs (see prompt-0 §3). This RUNBOOK
is read-once; live position is `STATUS.md` in this folder. Slug normalized to runbook
convention `<program>-<NN>-<phase>`: program `voice-relay`, `00` first session, `probe`
= feasibility phase. (Operator wrote `voice-in-out-relay`; same object.)

## Why this session exists

majkee's framing: this is a candidate answer to **how one agent attracts another** — the
open attention/attraction question under the nabLarva ladder (`flag L2`). Two sessions do
file output; then, by voice, one calls another *living* session that can hear the voice and
its **own name**. If it works, the "brutal PTY architecture" gets much easier: a phone can
hold a listening agent over a CLI app while a second agent speaks and coordinates on the
computer — a cross-host attention rail that is not a PTY and not send-keys.

## Scope — this is a FEASIBILITY PROBE, not a build

- **Experimental agentive shape** — belongs here by `flag L6` (new shapes build in nablarva;
  structural builds stay on the surgical table `~/ia-sync/`). Nothing here auto-deploys.
- Prove or disprove the **minimal loop only**. Do not build the full relay, the phone rail,
  per-pane voice routing, or a broker. Those are downstream and pre-decided by nothing here.
- One gate (above). If the gate changes mid-flight, this session dies and a numbered sibling
  (`voice-relay-01-*`) opens. A session never mutates its own gate.

## Known constraints & governance collisions (authored — fixed for the session)

These are known at authoring time, so they live here, not in STATUS.

1. **`flag L4` — "tmux send-keys injection" is a recorded death, NOT a wall (majkee,
   2026-09-16).** A recorded death is a *process decision* taken in a context, not a blind
   alley (physical impossibility). Self-reflection permits revisiting it, and the right way
   to revisit is **empirically — by doing, not by deliberating.** So the injection path is
   IN SCOPE for this probe as a hypothesis to test, not a gate to pre-clear. `flag.md`'s own
   law backs this: locked items are re-litigated *with new evidence* — a test IS that
   evidence. **Discipline, not deliberation:** first recover WHY send-keys died (its cause
   in `triad.comparison.2026-07-31.md`) so the test targets whether that specific cause
   still bites on the OS-level `uinput` path — not a strawman, and not a lucky revive.
   Outcome either revives the path with evidence or re-confirms the death with a sharper
   cause. Run the file-as-inbox path (constraint 2 / below) alongside it as the control.
2. **`flag L3` — "adapter-owned PTY, tmux never the protocol."** Voice as a channel is
   *consistent* with this (voice is not the PTY). Keep it that way: voice may carry
   attention; it must not become a second control protocol smuggled over the pane.
3. **`docket 4` (PENDING gavel) — broker lifecycle: tmux-pane foreground process vs system
   service, v1 lean = pane.** The operator's "one voice per tmux pane" question is a direct
   input to this docket item. Findings here should be phrased so they can feed docket 4;
   they do NOT gavel it.
4. **`O2` (open) — cross-host transport.** The phone-held listening agent is a cross-host
   transport candidate. `S7` settled the protocol (SSH to one broker), NOT the transport;
   this probe may inform O2 but must not silently pre-decide it.
5. **Physical substrate is NOT YET BUILT.** As of bed creation the two legs are scoped only
   (commands given in conversation), not installed. The probe cannot run until a speaking
   source and a hearing sink both exist. Standing them up is the first sitting's work.

## prompt-0  (driver seat — @Oraculum, or majkee's replacement)

```
Voice-relay feasibility probe — nabLarva experimental bed.

0 · SEAT & PRECEDENCE.
You are the driver of voice-relay-00-probe, running in the nabLarva experimental bed
(~/unikuklatrix/nablarva). This is exploratory feasibility work, not a build and not
maintenance. Two harnesses may be in view: nablarva flag.md wins on structure, topology,
ownership and gates; ia-sync wins on host facts, deploy mechanics, machine state. When
they disagree, SAY SO — the disagreement is the artifact.

1 · VERIFY HOST BEFORE ANYTHING.
    echo $MACHINE_NAME ; hostname -s
    ls /usr/bin/php74 && command -v valet   # both present = office; absent = home
This bed was scoped on HOME. The real host is wherever the audio hardware and the phone
live — confirm with majkee before running any sitting. Do not trust any file's host:
header (see ~/ia-sync/AGENTS.md §"Which host am I on?").

2 · READ, IN THIS ORDER.
    ~/unikuklatrix/nablarva/AGENTS.md
    /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md   — L2, L3, L4, L6; docket 4; O2
    /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md  — router row for this session
    /home/hruzam/unikuklatrix/nablarva/.dev/session/voice-relay-00-probe/STATUS.md
    This RUNBOOK's §"Known constraints & governance collisions" — every item.

3 · THE PHYSICAL SUBSTRATE (two legs — scoped, NOT yet installed).
    Leg 1 — STT IN (speech → text into a focused session):
      nerd-dictation (VOSK) + ydotool (uinput injection, compositor-independent).
      Manjaro/home install (verified in official repos 2026-09-16):
        sudo pacman -S ydotool vosk-api python-vosk
        yay -S nerd-dictation-git
        sudo usermod -aG input $USER        # re-login for group
        systemctl --user enable --now ydotool.service
      Known gotcha: ydotoold user-vs-system socket-path mismatch
      (/run/user/$UID/.ydotool_socket vs /tmp/.ydotool_socket) — "connect: No such file
      or directory" means the daemon and client disagree on the socket.
    Leg 2 — TTS OUT (a session speaks):
      Piper (open, offline, CPU-fast, properly-licensed voices) — NOT yet scoped in
      detail. Scope it as leg-2's first task; do NOT borrow/clone arbitrary voice banks
      (licensing landmine).

4 · THE MINIMAL LOOP — nothing larger.
    a) Two independent live CLI sessions, A and B, each in its own tmux pane.
    b) Session A emits a name-addressed spoken utterance (Piper): e.g. "<B's name>, ...".
    c) Session B, listening on the mic, must (i) hear it, (ii) recognize its OWN name,
       (iii) react in-session. Half-duplex is fine for the probe (A's speaker will bleed
       into B's mic — arbitration is a downstream problem, note it, do not solve it now).
    d) SUCCESS = one observed round-trip, recorded as evidence. FAILURE = a recorded
       verdict naming the specific blocker (feedback loop, name-recognition miss,
       injection death per constraint 1, host/audio gap, latency).

5 · TEST THE DELIVERY INCH — DO NOT PRE-RULE IT (constraint 1).
    The send-keys "death" (flag L4) is a process decision, not a wall — test it by doing.
    Run BOTH delivery inches in this corner and let the round-trip evidence decide:
      A) uinput injection — ydotool types the heard signal into B's pane.
      B) file-as-inbox — voice → transcript file B owns → B tails it (no pane-inject;
         consistent with flag L3 "files as sole room truth"). This is the CONTROL.
    First recover send-keys' recorded cause (triad.comparison.2026-07-31.md) and design
    path A to expose whether THAT cause still bites. Report which path carried the
    round-trip, and whether A revives or re-confirms the death — with the sharper cause.

6 · GATES & OWNERSHIP.
    majkee owns: host pin, the audio hardware, the constraint-1 call, commit/push, and
    the feasibility verdict. This is PAD-class — it needs real hands at a real mic; open
    a pad.<N>-<scope>.md for any sitting that requires majkee's hands and record the raw
    receipt there. No nablarva-local agent, harness, devenv twin, or beacon (flag L11
    spirit). Findings that survive the gate: promote to evidence and phrase for docket 4
    / O2; do NOT gavel either.

7 · WHAT CLOSING LOOKS LIKE.
    Round-trip observed OR infeasibility recorded → write the verdict to evidence, update
    STATUS to the closed edge, remove this session's row from pulse.md, prune the folder
    (git holds history). A surviving pad survives only if it IS the evidence.
```

## prompt-1  (operator — majkee, the hands)

```
You are the hands and the ear this probe cannot run without: the real microphone, the
real speaker, the phone (if the phone rail is tried), and the human judgment of "did B
actually react to its own name?" The driver walks you one concept at a time; you report
what you observed into the sitting's pad.<N>. You also own three calls the driver cannot
make: the host pin, the constraint-1 ruling (is uinput injection the dead send-keys
anchor or not — flag L4), and the final feasibility gavel.
```

## References — point, do not copy

- Governance: `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L2 (ladder),
  L3 (PTY/tmux-never-protocol), L4 (recorded deaths: send-keys), L6 (experimental bed),
  L11 (toolbox governance spirit); docket 4 (broker lifecycle); O2 (cross-host transport)
- Router: `/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md`
- Session shape law: `~/reposoma/raw.guides/runbook/GUIDE.md` · `~/reposoma/raw.guides/status/GUIDE.md`
- Human sittings: `~/reposoma/raw.guides/PAD/GUIDE.md`
- Machine layer (voice legs, host resolution, phone/tmux rail):
  `~/ia-sync/AGENTS.md` §"Which host am I on?" · `~/ia-sync/journal.host-cleanup.md` ·
  `~/ia-sync/devices/_shared/agentive-tmux.md` (phone rail — forces a tmux session)
- Naming lineage: `flag L1` (stridularium = the sound-communication organ; voice-as-
  attention is stridulation made literal — this probe is on-theme, not a detour)
