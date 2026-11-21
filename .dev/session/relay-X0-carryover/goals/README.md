# goals/ — small independent goal files (provisional try)

Majkee, 2026-11-21: goals as little independent files that can be forked or changed during a run, and later tried through a vendor
harness or a nablarva shape. This is an **uncanonical try in this bed only**. It replaces no guide and no other bed's RUNBOOK.
Words: `../raw/decision.majkee.open-bed.2026-11-21.md` (D3.5).

## Rules (few, on purpose)

1. **One goal, one file:** `G<n>.<slug>.md`. A file must make sense alone: why, done-when, evidence, bounds.
2. **A goal can change at any time.** Edit the file, raise `rev`, add one line under `## Changes` saying what and why. Git keeps the old text.
3. **Fork instead of bending.** A new finding that changes the aim becomes a new file with `forked_from: G<n>`; the old one gets `state: superseded-by G<m>` or `dropped` with the reason.
4. **A goal never releases itself.** `release:` says what Majkee must release before it runs (L21). `none` only for reading and writing documents inside this bed.
5. **STATUS says which goal is running.** A goal file holds no "next action"; `../STATUS.md` does.
6. **Only the pen holder edits goal files.** Other seats propose changes in their RETURN.
7. **Done means evidence.** `state: done` needs the file named in `evidence:` to exist and a non-author check when the goal says so.

States: `draft` → `open` (Majkee or the pen holder agreed it is worth doing) → `running` → `done` | `dropped` | `superseded-by G<m>`.

## Index

| Goal | One line | State | Release |
|---|---|---|---|
| [G0](G0.umbrella.md) | Majkee's umbrella goal for the relay organ | open | — |
| [G1](G1.party-binding.md) | The party is bound: who, where, which door, which bell | running | none |
| [G2](G2.export-verified.md) | The carry-over export is checked by a non-author | running | none |
| [G3](G3.door-inventory.md) | Which door works per direction on today's versions | draft | needs Majkee |
| [G4](G4.u01-unknown-view-fixture.md) | U01: find one genuine unknown native view, or report MISSING | draft | needs Majkee |
| [G5](G5.receiver-policy-contract.md) | U03–U06: one candidate receiver contract and oracle sheet | draft | none to draft |
| [G6](G6.u02-exit-race.md) | U02: receiver exits between text and Enter | draft | needs Majkee |
| [G7](G7.retire-file-poke.md) | Replace the provisional file-poke and retire it | draft | needs Majkee |

Shared practice used here: `~/reposoma/raw.guides/bus/res/file-poke.md` (provisional). Its retirement debt is carried by this bed
through the line ledger `../../relay-X.ledger.md` (G7).
