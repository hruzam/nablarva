---
session: nablarva-01-design
author: oraculum (cSharp, status_owner)
date: 2026-09-12
scope: every keeper named; preservation commands proposed; nothing executed, moved, or pruned
authority: "majkee's GO (chat, 2026-09-12) closed the gate; commit/prune authority is requested below, not assumed"
---

# Promotion manifest — nablarva-01-design

The cSharp scar (protocol §The four scars, 4): before any prune, an explicit manifest listing
EVERY `raw/` keeper. This bed's `raw/` has three files; all three are keepers. The bed is
untracked in git as of writing — no locator exists until the preservation commit lands.

## Keepers and destinations

| Path (bed-relative) | Owner | Disposition |
|---|---|---|
| `raw/design.r1.md` | cartan | KEEP unchanged (immutable revision, sha256 `b43d10ae…6814a`). Becomes the **founding reference of the sibling RUNBOOK** (`nablarva-02-<phase>` cites its preserved locator). ADR candidate `docs/decisions/0001-first-brick-relay-design.md` — pointer-only, drafted by the head **only on majkee's word** (canon: agents draft, majkee locks). |
| `raw/oraculum.experience-transfer.2026-09-12.md` | oraculum | KEEP; majkee carries it to the next cSharp (protocol §Transfer ritual). No project-level therapy artifact exists; not folded anywhere; history is its home. |
| `raw/promotion-manifest.md` | oraculum | KEEP (this file). |
| `_bus/01.oraculum.point.md` · `_bus/01.cartan.return.md` · `_bus/01.oraculum.verdict.md` | oraculum / cartan / oraculum | KEEP unchanged; history via the preservation commit. Never transplanted into mail or an archive. |
| `RUNBOOK.md` (repaired 2026-09-12, `repaired:` field) · `STATUS.md` (final replacement snapshot) | oraculum | KEEP; the commit pins the post-repair RUNBOOK hash that VERDICT 01 left unpinned. |
| `../GLOSS.nablarva.md` | operator learning file | NOT in the bed; survives at the session root for the whole nablarva part (gloss GUIDE); untracked today — include in the same commit. |
| `../pulse.md` router row | oraculum | Keep until preserved; remove in the prune step (same or later commit). |

Outside the bed, not this manifest's to decide: `meshup/nablarva-01-design/` (Cartan's holding
copy, brief, `cartan.reading-notes.md`) — untracked; majkee decides its git disposition.
`.dev/session/runbook-tool-00/MOVED.md` and `_mail/houston/inbox/…` — other owners' dirt.

## Durable conclusions already in their homes

- The design, its evidence and its acceptance test: `raw/design.r1.md` (pinned).
- The audit and its corrections of the head's surfaces: `_bus/01.oraculum.verdict.md`.
- The operator's understanding: `../GLOSS.nablarva.md`.
- No canon, skill, agent, source, or runtime state was changed by this session.

## Preservation — proposed exact commands (majkee or a @delta, after majkee's `commit ok`)

Bed-scoped, nothing else staged; L12: plain `git pull`/`push` on `core`, never `--rebase`.

```sh
cd /home/hruzam/unikuklatrix/nablarva
git status --short                      # expect: M pulse.md · ?? bed · ?? GLOSS · (others untouched)
git add .dev/session/nablarva-01-design .dev/session/GLOSS.nablarva.md .dev/session/pulse.md
git diff --cached --stat                # expect only those paths
git commit -m "nablarva-01-design: gate CLOSED (GO on design.r1 b43d10ae) — bed, VERDICT 01, GLOSS, router row"
git rev-parse HEAD                      # = the preservation locator; paste into the sibling RUNBOOK and here
```

After the locator exists (majkee's separate word for prune):

```sh
cd /home/hruzam/unikuklatrix/nablarva
# remove the nablarva-01-design row from .dev/session/pulse.md (one line), then:
git rm -r .dev/session/nablarva-01-design
git add .dev/session/pulse.md
git commit -m "nablarva-01-design: pruned after preservation <locator>; router row removed"
```

No push is proposed here; push and home carry are majkee's git ops (flag L12), with their own
evidence. The `.dev/session/runbook-tool-00/MOVED.md` stub and `_mail/` remain untouched.

## Preservation receipt

_empty — filled by the head only after the commit is observed (`git log -1 -- .dev/session/nablarva-01-design`), never before._
