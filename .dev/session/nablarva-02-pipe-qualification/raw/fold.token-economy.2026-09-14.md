---
kind: head note — fold of symmetry's token-economy brief into this bed's scope
author: oraculum (cSharp)
date: 2026-09-14
source: raw/brief_nablarva-token-economy_2026-09-14.md (symmetry, informative, not design; placed by majkee)
authority: none
---

# Token economy — what folds, what parks

- **Bus reader reads the bus, not head state** (brief §6 underlined) — resolves the design of the
  "living-dub-memory" flusher: a flat reader over `_bus/` filenames + frontmatter is cheap and
  cache-neutral; reading a head's own transcript/state re-enters the cache-break problem. The
  2026-09-14 field test (21 files, ~2,300 lines, ~85k tokens) read too much content; the next
  flusher reads presence + frontmatter + STATUS `holds:`/`next:` only, Haiku-tier.
- **A handoff carries a state change, not an acknowledgement** — already law here (POINT stays
  acknowledgement-free; RETURN is the receipt). Vindicates no-ack-file.
- **Append-only markdown with a stable header** keeps the reader's prefix cacheable — matches
  immutable `NN.<seat>.<kind>.md` receipts and revisions-as-new-files.
- **Brake belongs on context growth, not exchange count** — matches STATUS-as-short-snapshot and
  the 501-line scar; the head's cost is its own accumulation, not the bus.
- **Harbour = one cold call per compaction** — accepted cost; not a mechanism in this bed.
- Parks: loop budgets; hub file for a third/fourth head; notification transport (hooks vs polling)
  — the last is bed 02's own question, answered by the private-server route, not by this brief.
