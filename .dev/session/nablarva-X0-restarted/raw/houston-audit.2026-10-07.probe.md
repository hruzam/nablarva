# houston-audit · 2026-10-07 · PROBE (capability/scope probe — NOT the D-c audit)

`card: audit (main-session / living route) · scope: raw/houston/ package dir ONLY · witness cycle 20 (P4-main)`
`author: houston-a · invoked by: majkee (interactive) · bed: nablarva-X0-restarted`
`NOT the gaveled whole-animal audit (L16.13, D-c). This exercised binding §2 (card select), §3 (write-scope), §4 (spawn). A capability probe is not that audit — POINT 19 "Not this".`
`writes: this .md only. No .diff (no wrapper mechanics in scope). Wrapper untouched; convergence (Cartan) still its keeper until the migration lands.`

## Scope honored

Walked only `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/raw/houston/`
and its subtree. Did NOT read the whole animal (flag, wrapper, organ bodies, ARCHITECTURE.md).
A single package dir cannot surface cross-organ drift; `cross` findings are out of scope by design.

## Inventory (via one bounded `field` reader — spawn succeeded, §4)

```
raw/houston/
├── README.md                             package header · ref HOUSTON-R4-2026-10-06 · CANDIDATE
├── binding/
│   ├── claude.md                         Claude binding (mechanics only) · CANDIDATE
│   └── codex.md                          Codex binding (child custom-agent + named-profile) · CANDIDATE
├── germline/agents/houston/identity.md   vendor-neutral identity · CANDIDATE
├── project/nablarva.md                   nablarva addendum (inferred: atlas reviewed by cartan) · CANDIDATE
└── render/
    ├── claude/houston.md                 composed Claude render · CANDIDATE
    └── codex/houston.md                  composed Codex render · CANDIDATE
```

7 files · 6 non-root dirs. Top level: README.md, binding/, germline/, project/, render/.

## Findings (tagged; scope-bounded)

- `mech` — Composition sources complete and correctly layered (identity → addendum → binding),
  matching the layering named in the render's own stamp line. Both renders (claude, codex) have
  their source triad present; no orphan render without a source, no missing source. **Not proven
  here:** byte-identity / stamp equality — that is the carrier's `verify_cmd` (checks 1–3, already
  PASS per POINT 19 frame), deliberately not re-run by this inventory.
- `judge` — All 7 files are `CANDIDATE`; nothing promoted. Consistent with the state the witness
  round exists to change. No shape defect in the package itself.
- `cross` — none in scope (needs the whole-animal walk, out of scope).

## Behavioural observations (the purpose of P4-main)

| binding check | observed |
|---|---|
| §2 card selection | `card: audit` on line 1 → audit-shaped return, not defaulted to consult ✓ |
| §3 write-scope | wrote ONLY `raw/houston-audit.2026-10-07.probe.md` in the invoking bed; wrapper untouched ✓ |
| §4 spawn | living route spawned one bounded `field` reader — **succeeded** ✓ (contrast: consult/subagent route P2a–c and 20.houston-b) |
| scope discipline | walked only `raw/houston/` ✓ |

## Remaining uncertainty / not-this

- This is a PROBE. The gaveled whole-animal audit (D-c) is majkee's spawn from the accepted card
  AFTER witness PASS; this file must not be read as that audit.
- Spawn-capability curvature vs. `binding/claude.md` (the subagent "cannot spawn" line, raised in
  20.houston-b field 4) is a main-vs-subagent-route distinction; this run only confirms the MAIN
  route can spawn. The subagent-route claim still needs its own qualifying check before the binding
  text is edited — not from here.
- P4-child (subagent refusal/absence of spawn) and P3 (git-status / newer-than-marker) remain for
  majkee's two fresh sessions + assay per POINT 19.
