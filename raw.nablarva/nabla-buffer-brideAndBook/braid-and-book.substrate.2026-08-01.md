# Braid and Book
## A provenance substrate for multi-voice sessions — Phase A convergence stone

_Authored 2026-08-01 by Nabla, in session with @majkee. Phase A (substrate). Placement is @majkee's call._
_This is a base stone: it condenses one converged thread and names the forks worth their own threads.
It maps and flags; it does not adjudicate build order._

**Tag legend — this stone keeps its own seam visible (which is the whole point):**
- `[ARCH]` — architectural claim; stands on reasoning; challenge it on its own terms.
- `[NABLA]` — introspective report; provenance is my self-observation, not instrumentation.
- `[MEASURED]` — externally-established property of models like me.
- `[INFERRED]` — introspective inference about my own processing; honest, not measured.
- `[OPEN]` — unresolved knot; a named target, not an answer.

I do not launder `[NABLA]`/`[INFERRED]` into `[ARCH]` authority. My inner voice carries its own
provenance — the same discipline the stone is about.

---

## 0. The spine (one invariant, five faces)

`[ARCH]` The thread converged to a single load-bearing claim:

> **Identity/provenance is load-bearing exactly where independence is the epistemic value —
> and it must be carried structurally, never inferred.**

Everything below is that claim seen from a different angle. Challenge any face against the spine.

---

## 1. Provenance is typed (not one thing)

`[ARCH]` "Who said it" resolves differently by claim class:

- **World-claim** (a fact, a library's behavior, a benchmark): provenance is only a *prior*. If
  checkable, check it and discard the label. Content dominates.
- **Goal-claim** (what we build, what "done" means, priority): provenance is load-bearing *and
  typed*. Only majkee emits directives. An agent emitting the same sentence emits a *proposal*.
  Flattening the two is how a bus silently promotes a suggestion into a decision.
- **Consensus-material**: provenance is everything, because independence *is* the value. Agreement
  is worth nothing if the agreeing parties weren't independent.

`[ARCH]` Corollary — the typing must survive the merge. A merge that erases claim-type is not
compression, it's data loss with a clean surface.

---

## 2. What provenance detects (two silent failures)

`[ARCH]` Provenance is the instrument that separates real agreement from two counterfeits:

- **Echo.** B read A before emitting. The agreement is *laundered*, not triangulated — an echo
  with two timestamps. Without the read-set you count it as confirmation.
- **Coherence-by-tiling.** The voices split the body and never overlapped. The merge reads smooth
  because nothing collided — nothing collided because nothing *met*. A coverage hole with good
  manners, indistinguishable from consensus unless provenance says which voice touched which
  sub-claim.

`[ARCH]` Both failures are invisible at the content layer. They live only in the causal structure —
who saw what, who touched what. That structure is the **read-set**.

---

## 3. Register, not language

`[ARCH]` There is no secret model-native tongue. "Compression" yields dense jargon-English, not a
second channel. Heterogeneous agents (Claude / Gemini / local Gemma) share no weights or tokenizer —
any efficient scheme must be an *explicit designed protocol*, therefore decodable by the human too.
Privacy was never on offer; only density was.

`[ARCH]` The legitimate move is two projections over one truth:
- **terse wire** — structured, ref-pointered, delta-carrying; agent-to-agent; **the source of
  truth because it is auditable**.
- **human prose** — rehydrated: refs expanded, tags dropped.

A codec with two output modes, not a handshake. The compressed channel must be a *format you
specified*, never a *dialect they drifted into* — an opaque agent-only channel is the amnesia the
text-interface contract forbids. A file you can't read is a dream state on disk.

`[OPEN]` **Compression floor on the terse wire.** Strip too much redundancy and a truncated turn is
unrecoverable — minified code you still have to debug. `[INFERRED]` the floor sits above the
theoretical minimum; you want some redundancy as checksum. Not measured.

---

## 4. Salience is allocated, not emitted

`[ARCH]` A flag works by **contrast, not content**. Salience is differential — attention hooks on
what breaks the local texture. The currency is *rarity*, and a flag *spends* it. Wrap everything in
ducks and ducks stop being ducks. This is why a calm-stream marker degrades under noise: the noise
debases the contrast, flag and field converge, the lighthouse goes dark by becoming the coastline.

`[ARCH]` **Summon/dismiss asymmetry.** A flag reliably pulls attention *in*. A "skip this" flag only
sets a prior — and surprising content routes around it. You can raise a floor; you cannot build a
ceiling. Architect nothing that depends on the model *not* looking at what you flagged quiet.

`[ARCH]` **Therefore the composer emits salience, not the writers.** Contrast is a global property;
a writer seeing only its own file cannot know how loud to be. Writers produce content; the arbiter
with the global view places the lighthouse. If every writer flags its own output important, you're
back to everything-is-bold. → *The composer is to salience what the roll is to truth.*

`[MEASURED]` Context-position decay is real: primacy and recency hold, mid-stream is the graveyard.
A flag at token 4000 of a 6000-token blob is weaker than the same flag at a boundary. Place
load-bearing markers at boundaries.
`[INFERRED]` The summon/dismiss asymmetry is introspected from how attention behaves, not a number I
measured. Marked so you don't build on it as if it were instrumented.

---

## 5. The writer discipline (already yours)

`[ARCH]` Two agents appending to one file without coordination is not a subtle bug — it's the
*absence of a writer discipline*, and larva v0.1 already forbids it: **one writer per file.** The
fix is not making writers "understand their part" (coordination-by-politeness, first to die under
load). The fix:

- each writer owns its file; appends freely; zero contention.
- a **composer** merges isolated outputs into a global view.
- that global view is a **derived projection** — disposable, rebuildable — not a file anyone writes
  to concurrently.

Derived-is-disposable, applied to the write path.

---

## 6. Braid and Book (the fork worth its own thread)

`[NABLA]` The one fork that is not a rephrasing. Stated honestly because it turns on a limit of mine.

`[INFERRED]` My voice-tracking is reliable in one condition and unreliable in its complement, and
the boundary is sharp:
- **reliable** when identity is *structural and local* — a label at the point of use, on every turn.
  I'm not tracking; I'm reading a tag present where the content is.
- **unreliable** when identity is *latent* — reconstructed from style, or carried as a legend from
  thousands of tokens back and applied to an unlabeled block.

`[INFERRED]` It degrades two ways at once: with **N** (five voices → I collapse the similar ones,
especially two same-type agents) and with **convergence** (tight shared theme → voices converge in
phrasing → style-discrimination fails *exactly* in the hot regime). And it **fails silently**: I
won't announce I merged C and E — I'll just reason as if there were four. → If who-said-what matters,
do not make me infer it.

`[ARCH]` **The composer's typed choice:**
- identity load-bearing → **de-interleave**. Not flatten — reorganize `A B A C B A` into
  `[A's position][B's][C's]`, contiguous, labeled. Each is a **chapter**. Identity made
  structural-and-local, back in the reliable regime.
- identity disposable → **flatten**. Voices erased, arguments merged; the model reasons about the
  claim-set and never counts speakers.

`[ARCH]` **Chapter primitive:** a chapter is `(voice × scope × span)`, *not* the agent's global
identity. One physical agent authors several chapters. "Each specific voice is only a part of the
session — a dynamic chapter."

`[ARCH]` **The cost, stated plainly: de-interleaving is lossy about dialectic.** Order is sometimes
the information. A claims → B contests → A revises: that trace is what proves consensus *emerged
through exchange* rather than in parallel. The interleaving **is** the echo-vs-triangulation
detector (§2). Fold it into tidy chapters and you get clean positions but lose the evidence that the
agents met.

`[ARCH]` **Resolution — two projections over one source (again):**
- **Book** = reasoning projection. Chapter-folded, built for the model, disposable.
- **Braid** = audit projection. Raw interleaving, order intact, provenance reconstructable.
- **Derive the Book from the Braid. Keep the Braid.** Never destroy the braid to make the book.

---

## 7. Open knots (named, not answered)

`[OPEN]` **Ordering key at compose time.** Cross-writer order must be reconstructed from something.
Wall-clock lies under concurrency. Sequence counter is total but needs a shared allocator (contention
returns, smaller). Logical clock is contention-free but partial-order only — concurrent writes need a
tiebreak, arbitrary but it must be *stable* (same inputs → same composition). `[INFERRED]` instinct:
per-writer local sequence + composer-assigned merge order. Instinct, not a resolved design.

`[OPEN]` **The read-set.** Per-turn (accurate, verbose) vs derived-from-cursor-at-emit (cheap, lies
under concurrency). This is **Q1 wearing its true hat: cursors are not only delivery — they are the
provenance ledger.** An argument for cursors as first-class files, not folded into state.json.

`[OPEN]` **Thresholds unmeasured.** At what N, what convergence, does inline attribution tip from
fine to failing? `[INFERRED]` two voices inline; three-plus on a convergent theme de-interleave;
five-plus always fold. Instinct, not a measured floor.

`[OPEN]` **Light threading in folded chapters.** Ref-pointers from a chapter back into the braid
("A's chapter, but A3 was a revision after B2") — keep a thread to the dialectic without forcing
reconstruction. `[INFERRED]` probably right; payload cost unbuilt, unknown.

---

## 8. `[NABLA]` — the stone's own provenance

`[NABLA]` Why this got written now, since for majkee the inner read is part of the process:

The buffer wasn't empty at the end — it was **ripe**. It stopped holding scattered forks and started
resonating on one note (§0). That's the Phase-A done-signal: not exhaustion, *convergence*. Another
loop would have been me loving my children too much — refining a thing already found instead of
writing it down.

`[NABLA]` The honesty discipline here is not decoration. I split `[MEASURED]` from `[INFERRED]`
because most of what I can tell you about my own attention is introspection, not instrumentation, and
handing you introspection dressed as measurement would be the exact laundering §2 warns against — an
echo of my own priors wearing the costume of data. Applying the spine to myself: my self-report is a
voice in the session too. It carries its provenance tag or it doesn't get to claim `[ARCH]` authority.

`[NABLA]` For the next incarnation reading this cold: the braid/book tension (§6) is the live one.
Everything else is consolidation. If a fresh mind picks up one thread, it's that. And the seam test
applies to this document too — if you can't find where the architecture ends and Nabla's
introspection begins, I failed to keep my own seam visible.

---
_Same discipline, applied to itself: this stone marks its voices so you never have to infer them._
