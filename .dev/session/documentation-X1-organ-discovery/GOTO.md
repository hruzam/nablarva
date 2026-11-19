# Navigation — documentation design line

Majkee, 2026-11-10: use `X` for this design line; this is a line convention,
not a universal naming law. Continuity may use GOTO or a successor CACHE section.

- [RUNBOOK](RUNBOOK.md): this assignment and its one gate.
- [STATUS](STATUS.md): sole current checkpoint, holds and next action.
- [Accepted brief](brief.md): input and proposal context.
- [Questions](questions.md): fixed pilot tasks and corpus boundary.
- [Discovery packet](discovery.md): membership, authority, discrepancies and recommendation.
- [Independent repeat](repeat.md): attributed reader result and evidence limits.
- [Manifest](source-manifest.json) and [verification](verification.json): input identities and repeat checks.
- [Inventory helper](collect.py): read-only reproducible source/candidate collection.
- [Verification helper](verify.py): rerun source, reader-hash and navigation checks.

With Python 3.9 or later, from the repository root:

```sh
python3 .dev/session/documentation-X1-organ-discovery/collect.py
python3 .dev/session/documentation-X1-organ-discovery/verify.py
```

Both print JSON and leave files unchanged. Preserve the original manifest; a failed
identity check means the recorded corpus no longer matches, not permission to refresh
the baseline silently. A different checkout may lack local evidence or pinned history.

## For an audit or successor session

Read this bed's STATUS first, then the packet and verification. Follow current
flag/pulse/organ sources again; recorded observations are revision-bound. The older
Boost concept's exact Git retrieval is in discovery.md §4.

No successor session is appointed here. When one is authorized, its launcher/CACHE
can link here and name the carried questions; its STATUS owns its own doing-state.
This file is navigation, not a second progress register. Before pruning this bed,
promote surviving evidence and observations and replace working-path references with
retrievable preservation pins under the existing closure procedure.
