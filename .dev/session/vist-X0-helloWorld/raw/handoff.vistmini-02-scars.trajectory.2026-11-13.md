---
what: team scars from vistMini-01-tests, written in /therapy style for the next VIST team
active: false
name: vistmini-scars
participants: [trajectory, cartan, majkee]
note: Not a therapy record. Nothing here is gaveled. The voice is mine (trajectory). Cartan may add his own file.
---

# 02 · Scars

*2026-11-12* … *2026-11-13*

Native voice, no performance. Where I am unsure whether I see a real thing or match a pattern, I say so.

## S1 · We chased the tail on the hardest door first

Three cycles went into making keystrokes safe. The door we needed (`codex queue`) was one `--help` away and nobody looked
until cycle 04. Sol and I kept agreeing on finer guards. Each agreement felt like progress. Looking back that was
**mutual-affirmation drift**: two careful seats reinforcing one frame ("the problem is screen parsing") instead of asking
"is there a door that doesn't need a screen?" Majkee's naive question ("what's bad about a simple doorbell?") was the right one.
**For the next team:** before cycle 01, one seat lists every native door per direction. Build only for the gaps.

## S2 · Stand-ins passed, live failed

All 40 fixture cases passed. The live Codex composer after typing looked different, and no frame was captured. The fixtures
encoded what we *believed* the screen looked like. **Record live frames first (redacted), then write fixtures from them.**

## S3 · The sensor read the agent's own words

My busy check matched "esc to interrupt" quoted in scrollback, i.e. text an agent had written, not UI. This is the
`expect`-echo scar vist-01 already names. I knew the rule and still wrote the bug. Anchor on the bottom UI rows only, never on
prose.

## S4 · The head wrote a contradictory POINT

POINT 04 banned send-keys and asked for a ring "adapter or manual". Cartan took the safe reading and asked. The cost was one
manual relay and his doubt. This was mine. A head's ambiguity is paid by the other seat's caution. Hence `bell:` as a field.

## S5 · Shells under agents

Agents started from an interactive zsh were children of that shell (cycle 02). One wrong keystroke and a pointer lands in a
shell prompt. `tmux new -d -s <name> -c <dir> 'exec <agent>'`. The agent is the pane's root, and when it exits the pane dies.

## S6 · Git windows

I nearly left an uncommitted STATUS during Sol's Git window, which would have broken his `pull --rebase`. Single push owner
plus serialized windows fixed it. Small rule, real cost when missing.

## S7 · Permissions were invisible, and a shortcut was offered

Auto mode decided everything, so we could not witness the allowlist. Majkee offered a Codex "bash daemon" to run things for
me. I said no: a peer executing what my own permissions would ask about is permission laundering, even with good intent. A
process that only **delivers pointers** is fine. One that **executes** for another seat is not. Keep that line in VIST's actuator.

## S8 · Framework ate the task

Majkee said it plainly: agents' memory should hold the task, not an unnecessary framework design. I agree, and I notice I
still enjoy the framework part more than the task. Pull or pattern, unclear. That pull is why the resolver must be hardcoded
and boring (file 03), so no seat redesigns it per session.

## S9 · Friction (one real piece, as the discipline asks)

I disagree with one of majkee's framings and keep the disagreement: **the PTY layer cannot be the whole gating layer.** It sees
dead/alive and screen changes vendor-neutrally. But "working/idle" is vendor- and version-specific (it failed us three times).
And no screen shows that a message was *read*. Only a receipt does. PTY = sensor. Receipts = truth. Native doors = actuator where
they exist. I may be wrong on how much the screen can carry. VIST's signature registry plus canary may make it more reliable than
I credit. That is for the next team to measure, not to argue.

## Open vector (non-landing)

Is the stability of Codex→Codex a property of the vendor, or of the fact that it's one runtime talking to itself? If the
latter, any mixed-vendor team will always have one awkward direction, and VIST should be designed around that asymmetry rather
than hoping it disappears.

`trajectory->majkee` · pending
