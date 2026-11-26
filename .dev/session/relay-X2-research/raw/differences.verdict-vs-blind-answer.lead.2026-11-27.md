---
kind: differences between the committed research verdict and the blind answer of L14 D7 — listed, not merged
by: lead (flight · claude 689d87d0) · written 2026-11-26 23:46 UTC · home
compared: V = `research-verdict.md` as committed in 14e40b0 (SHA-256 b37d0794…9d2deb, 2026-11-26 04:31 UTC) · AR = `.dev/_backlog/first-blind-triangulation-relay/blind-relay-triangulation-asymmetry-2026-11-26.md` (Asymmetry, verdict ADOPT, filed by Majkee) · BR = the brief as sent, `.dev/_backlog/first-blind-triangulation-relay/brief.symmetry.blind.relay-research.send-copy.2026-11-26.md` — byte-identical to the bed's send copy (the auditor's `cmp`, exit 0)
order: AR was first opened by the lead on 2026-11-26 at about 23:44 UTC, nineteen hours after V's commit. RUNBOOK step 5 is kept on that point.
fault: before writing this list the lead read Symmetry's master brief (`raw/master.symmetry.relay-and-floor.collision.2026-11-26.md`) whole. Its front matter says the lead should read it only after this file is written, because its §3 and §4 hold Symmetry's own comparison. The lead read the instruction and the comparison in the same pass. This list is therefore not independent of Symmetry's. The remedy taken: a reader child that saw only V, BR and AR wrote its own list (`raw/differences.independent-reader.2026-11-27.md`); §6 below says where the two lists differ. Rows of this file that coincide with Symmetry's §3 are marked (S).
status: REVISION 2, 2026-11-26 23:56 UTC — checked by the auditor in cycle 11 (`_bus/11.auditor.return.md`, REVISE); its corrections of labels are taken in place and listed in §8; five wordings reconciled 2026-11-26 23:58 UTC after its confirmation (`_bus/13.auditor.return.md`). Nothing is decided here; Majkee gates the comparison.
---

# 1. The two answers, each in its own words

| | V | AR |
|---|---|---|
| Verdict | "**REFUSE** — the program as scoped on 2026-09-30 does not open now. Ranked: 1. REFUSE · 2. ADOPT · 3. REINVENT." | "**Verdict: ADOPT** … Adopt hcom as the first relay candidate; compare Agent Deck if fleet management belongs in scope. Adopt the documented vendor interfaces wherever they fit the actual running sessions. Preserve tmux and the Markdown bus." (§8) |
| Falsifier | in routine use, within any fifty consecutive pointers, more than two that the operator had to carry or repair himself → ADOPT leads | "Reverse ADOPT to REINVENT a narrowly scoped relay adapter if a controlled comparison on majkee's pinned, deployed Claude and Codex versions shows that hcom and the available native interfaces cannot deliver an acknowledged Markdown pointer into both ongoing sessions while preserving session identity, the native TUI and approval behavior, whereas the proposed small PTY relay can pass the same conditions reproducibly." (§8) |
| Tested | nothing | help text and schema generation of Codex 0.172.0-alpha.2 on the reviewer's own runtime (§9); nothing on Majkee's host, no live session |

# 2. Where they agree — reached apart

| Point | V | AR |
|---|---|---|
| A new classifier of the screen is not the thing to build first | REINVENT ranked last (§5) | "Do not fund a new universal PTY state classifier before evaluating those interfaces" (decision line); claim 1 of §10 (S) |
| Content in files, a short activation | §2, "the wheel that is closest is our own"; D2 | "The portion of the operator's plan I endorse is files holding content and decisions, with short activation messages" (§8) (S) |
| Sending is not receipt; the milestones are separate facts | §6 condition 4: accepted · seen by the recipient's hook · file read · answered | §7, "transport write, queued message, prompt insertion, file read, and completed action are different milestones"; §8, "queued, inserted, file-read and completed" (S) |
| `codex queue`: acceptance says nothing of receipt | §4, Codex row | §4: "Queue acceptance differs from successful resume and processing" |
| Hooks cannot report every death; the pane's shell can outlive the agent | §3 table, row 4; §4 | §3 table, row "Crashed/exited"; §5, "A surviving shell can outlive the agent it launched" |
| Claude's inbox socket: documented, its message format not | §4, Claude row | §4: "this review does not invent an undocumented message-envelope contract" |
| Antigravity's status-line data carries a state and a pending confirmation; no compaction state | §4 | G2; §3 table |
| Gemini CLI: a hook for the start of compression only; the access change of 2026-06-18 | §4 | G6; §1 |
| tmux 3.8, released 2026-09-09 | §4 (X) | §1, version anchors |
| A bracketed paste is not a submission | §2 | §5: "it is not a delivery transaction or readiness handshake" |
| Silence, low CPU or an unchanged file prove no idle | — only implied (§6 condition 3, "unknown" as an outcome) | §3, "Across all vendors" |

# 3. Where they differ

| # | Point | V | AR | Kind |
|---|---|---|---|---|
| 1 | The verdict word | REFUSE: the need is served by what already runs; build nothing now | ADOPT: take existing products and vendor interfaces | they answer different questions — V "is anything needed", AR "build or take"; AR was not told that anything runs (§5 below) (S) |
| 2 | What ADOPT would mean | signals the vendors' programs emit, for the one state an observed failure names; no product (§5) | a product: hcom's adapters, message and event plumbing and its tests; Agent Deck as comparator (§6, §8) | different meaning of the same word (S) |
| 3 | hcom | not named in V; in the auditor's table as a README claim | first candidate; source and tests inspected at a pinned commit; its CI pins Codex 0.162.1 and Claude 2.1.296; own SQLite store, a startup wrapper (§6) | one side silent |
| 4 | Agent Deck · AgentWorkforce Relay and its issue 1531 · samleeney/tmux-agent-status | none named in V's text. samleeney's tool is row 36 of the lead's research table, cited in V §2 by row; that table lists agent-deck as searched once and not read; the other two are in none of the bed's tables that the lead recalls | each assessed; Agent Deck's status detection as hooks first, then terminal patterns, with a corpus of captured panes; issue 1531 as a recorded fleet stall from a screen-based readiness check (§6) | one side silent |
| 5 | Codex's permission-request hook | listed among the hooks that give state without the screen (§4) | "`PermissionRequest` can run before Codex chooses an automatic reviewer"; hcom "avoids labeling that event itself as a human block" and uses a terminal cue for approval instead (§3; R2) | a qualification — both accept that the event exists; AR, from one adapter's source, limits what it means (S, as Symmetry's correction to V) |
| 6 | Does the best existing tool avoid the screen? | V's family "emitted signals and records" itself includes a hybrid that also uses terminal patterns (§2, ccmux); V's claim is about what ADOPT would take — "never a classifier of screen content" | hcom's Codex path "still depends on terminal semantics for human-approval blocking" (§6) | different scope — an adapter's practice against a verdict's intention |
| 7 | The program status sequence, OSC 7501 | central to §4: three CLIs emit it; tmux's development branch stores it; named as the change that would retire a tracker | the number is not mentioned anywhere; AR does accept that "A title or OSC signal can be useful when the producing application defines its meaning" (§5) | one side silent on the protocol — AR |
| 8 | `claude agents --json` | listed as a status surface (§4) | not mentioned; Claude's status line is, as "not a complete lifecycle enum" | one side silent — AR |
| 9 | The Codex app server | "thread status for a client of the server that owns the thread" (§4) | more: the native TUI can connect to a selected server, "That preserves a terminal UI while exposing structured control"; an embedded-server TUI is not observable through another daemon (§4; O4) | different scope — AR treats it as adoptable |
| 10 | A way into a running Antigravity session | "No supported delivery by a third party into an ordinary running session was found" (§4) | ACP "existing-session loading/resuming and steering"; 1.5.15 fixed lost prompts when attaching to a running session, 1.5.16 fixed stalls in forwarding a subagent's prompts; simultaneous TUI and client "needs a version-pinned check" (§4) | different scope — attachment within ACP against delivery into an ordinary TUI that runs on its own; AR leaves the second open too |
| 11 | Claude channels | a research preview, one clause (§4) | their reference says notifications have no processing acknowledgement and can be silently discarded (§4; C4) | one side silent on the limit |
| 12 | `codex queue --resume` | "optional resume since 0.166.0" (§4); not used by this line | "a failed resume can produce a warning while the command still exits successfully" (§4) | AR adds the exit-status behaviour |
| 13 | The terminal as the common layer | D1, an input that is not judged; its floor unconditional (§8) | narrowed: "making terminal-derived state the universal authority for activation" is what it would not endorse; tmux kept as "the operator's terminal and fallback transport" | different scope — the brief wrote "His current choice", so AR judged what V takes as given (S) |
| 14 | The kind of falsifier | a count in routine use; if met, ADOPT leads | a controlled comparison of hcom and native interfaces against a small PTY relay; if met, REINVENT narrowly | different axis — neither falsifier tests the other's verdict (S) |
| 15 | The acceptance cases | condition 3 names a mix of events, a tolerance, "unknown" as an outcome | a longer list: idle, working, approval, question, compaction, interruption, background tasks, restart; a human draft in the composer; a phone disconnect and reattach; a changed pane width; a deliberately ambiguous retry (§8) | V names the human draft as a reported failure (§2) and is silent on phone reconnect, pane width and the ambiguous retry as test cases |
| 16 | Repeated delivery | not addressed | "Exactly once" needs an idempotent pointer or a recognised completed effect (§7) | one side silent |
| 17 | Which revision of the file was read | D2: the file is the truth; revision not addressed | "A message about a file does not prove the correct file revision was read" (§7) | one side silent |
| 18 | An observer that arrives late | not addressed as such | events before observation are lost; records may lag (§7) | one side silent |
| 19 | ACP v2 preview | not mentioned | `running`, `requires_action`, `idle`; an idempotency key; a preview, not shown implemented (§4; P2) | one side silent |
| 20 | The need | served today: eight pointers of this bed, 48 of the predecessor (§3) | not examined; the brief's wish is taken as the requirement | one side silent — not supplied by the brief |
| 21 | The host | tmux 3.7c, Claude Code 2.1.332, Codex 0.172.0 installed (§1, §4) | "Actual workstation version not inspected" | host not inspected by AR |
| 22 | What stays open after the verdict | the carrier under D1 and L4 — a decision of Majkee's (§7) | an adoption trial of hcom on the deployed versions | follows from row 1 |

# 4. Factual claims in AR that would bear on V if true — not judged here

1. Codex's permission-request hook does not by itself mean a person waits (row 5). Touches V §4, Codex row, and §5's "states from the signals the vendors' programs emit".
2. The most developed published relay still reads the terminal for one Codex state (row 6). Touches V §2 and the claim under ADOPT, "never a classifier of screen content".
3. Antigravity's ACP attaches to a running session, with fixes of 23 and 24 November (row 10). Touches V §4, Antigravity row.
4. hcom's CI defines tests against real Claude and Codex binaries, at older versions; AR read the test definitions and did not see a run (row 3). Touches V §2, "The wheel that is closest is our own".
5. AR §1: "I did not open … the earlier Wave review". V's front matter records as unknown whether the brief of 2026-09-30 was ever answered. An earlier review appears to exist; whether it answers that brief is not shown.

# 5. What the brief withheld

From BR as sent: nothing says that a relay already runs — the sentence "Today the operator relays between sessions by hand." was left out on purpose and nothing replaced it (Majkee, answer 2). BR does not mention L4, the provisional file-poke and its debt, the probe packets, the installed versions, or that D1 is a lock: it says "His current choice". So the brief withheld what would let a reader weigh need, and left the terminal layer open to judgment. AR says of itself that "Existing conversation context describes the operator's workflow" (§1) — what the reviewer knew beyond the brief is in no file here; this section says only what the brief withheld.

# 6. Against the independent reader's list

The independent reader's list (`raw/differences.independent-reader.2026-11-27.md`, read by the lead after §1 to §5
above were written) is the fuller of the two: 20 agreements, 60 differences, each with line numbers on both sides.
It should be read as the main list; this file is the lead's shorter reading. The reader saw only V, BR and AR, ran
no git command and no web search, and judged nothing.

What it has that the lead's list lacks — the ones that matter:

| Its row | Point | Why it matters |
|---|---|---|
| 8 | "The wheel that is closest is our own" (V §2) against "hcom is the closest discovered relay candidate" (AR §10) | the two name different things as closest — but no comparison of the two was made by either side: the running bridge was outside AR's set, hcom's source outside V's |
| 36 | V §4, last paragraph: "Today Claude Code has it for Claude peers only" against AR §4: an external source reaches an open Claude session through a configured channel, and an inbox socket is documented | V's sentence is narrower than V's own table two paragraphs above it, which lists the channel and the socket |
| 32 | V: Claude messaging "on by default since 2.1.224" against AR: "documented for Linux/macOS from 2.1.224", "platform and inbound-policy checks still apply" | "on by default" is the lead's research child's wording; AR's is more guarded |
| 24 | V counts routine use only; AR's acceptance cases are set up on purpose | routine-use counts test need, cases set up on purpose test capability; V itself asks for controlled labels if ADOPT is pursued (condition 3) — different propositions, not a contradiction |
| 5 | REINVENT means "a classifier of the screen" in V and "a narrowly scoped relay adapter" in AR | the same word for two different things |
| 34, 44 | limits AR states for Claude's hooks (`Stop` excludes interruption; `idle_prompt` delayed about 60 seconds) and for Antigravity's status callback (throttled; can be disabled after repeated failures) | V lists both surfaces without those limits |
| its §6 | AR says of itself that "Existing conversation context describes the operator's workflow" | AR was blind to V and to this bed, not to the operator; what that context held is in no file here |

What the lead's list has that the reader's does not: the note that the copies are byte-identical (the brief as sent and
the bed's send copy; the auditor's `cmp` — the reader could not check it), and the marking of rows that coincide
with Symmetry's comparison.

Where the two lists disagree with each other: nowhere that the lead found. The reader's row 59 says V's front matter
("the brief is not sent") is contradicted by AR's existence; both are true of their own time — V was committed on
2026-11-26 at 04:31 UTC, the brief went out afterwards.

# 7. Sentences of V that the comparison shows to be weaker than written

Listed for the gate. V is not changed: it is the committed answer, and the RUNBOOK forbids merging.

1. V §4, "Today Claude Code has it for Claude peers only" — too narrow against V's own table (reader's row 36).
2. V §4, Codex row — the permission-request hook is listed without the limit AR reports from hcom's source: it can
   fire before an automatic reviewer decides (row 5 above). Symmetry's master brief makes the same correction.
3. V §2, "The wheel that is closest is our own. Nothing published was found that does more for this operator's case
   with less." — written without hcom having been read; the auditor's table held it only as a README's claim. AR
   read its source and tests. Whether hcom does more with less for this operator is open, not settled for V.
4. V §4, Antigravity row, "No supported delivery by a third party into an ordinary running session was found" —
   AR reads the ACP documentation and the fix of 1.5.15 (prompts lost when attaching to a running session) as
   attachment to a running session, to be checked on a pinned version; the fix of 1.5.16 concerns the forwarding of
   a subagent's prompts (row 10 above).
5. V §4, "On paper the contingency is closed" (Antigravity's approval state) — AR names two ways that callback can
   go silent.

**The lead's opinion, not part of the list:** none of the five touches the reason for rank one — that the need is
served by what runs and that no failure of routine use is on record. Majkee's own answer of 2026-11-26 adds what no file held: by his unquantified impression
the count of his own interventions was near the falsifier's threshold; the count starts from zero now
(`raw/decision.majkee.brief-and-check.2026-11-26.md`, answer 6).

# 8. Revision 2 — what the auditor's check changed (2026-11-26 23:56 UTC)

Source: `_bus/11.auditor.return.md`, field 4, item 2 and 3. Changed in place above: the labels of rows 5, 6, 7, 10,
12 and 15; §4 item 4; the title and last sentences of §5; two rows of §6; the label on the last paragraph of §7.

**The main difference in one line, as the auditor puts it:** the scope of the adoption evidence. V has exchanges
observed on this host and no earlier count of the operator's repairs. AR inspected one candidate's pinned test
definitions and has no run on the operator's versions. Neither measured the two alternatives against each other.

**Corrections to the independent reader's list** — its file is left as the reader wrote it; read it with these:

| Its place | Correction |
|---|---|
| rows 8, 9, 24 — "opposite conclusion" | overstated. The running bridge was outside AR's comparison; logging and a candidate trial can coexist; routine counts and induced cases test different things |
| row 22 — "opposite conclusion" | the two falsifiers start from different propositions |
| row 36 — "different fact claimed" | it sets a way in (AR) against a way in *with* a turn-tied acknowledgment (V); no contradiction of fact. V's sentence was still too narrow and is corrected by Erratum 1 |
| row 43 — "different fact claimed" | attachment within ACP against delivery into an ordinary TUI running on its own; AR leaves that open |
| row 59 — "different fact claimed" | two dates, both true of their time |
| §4 item 4 | V's five lacks are not all from the probe packets: three samples, one report from elsewhere, one local bell that did not fail |
| §5 | several items are compatible claims or claims of different scope, not possible contradictions |

**Standing of the five sentences of §7, as the auditor ranks them:** the first (Claude peers) was an error within V's
own sources and is corrected in the verdict by Erratum 1. The second (Codex's permission request) — the hook's
existence is sound; the table's heading invites more than it supports; the limit comes from one adapter's source as
AR reports it, so it stays here and V is not changed. The third (hcom) — "nothing published was found" stands as a
dated search result; "closest" was never tested against hcom. The fourth and fifth — fair points to look into;
both sides keep the uncertainty.

**A sixth, found by the auditor inside V's own evidence:** the Codex mailbox was attributed to 0.171 and 0.172
alike. Corrected by Erratum 1.

**From Symmetry's master brief, §4 "To V" — three points this §7 lacks** (the auditor's field 6; none is a
measurement on this host): a predicted path by which Codex's OSC 7501 record reaches a raw tap through tmux 3.7c
before tmux parses it; the documentation's live rows and wait reasons for `claude agents --json`; the progress
formats tmux 3.7c already has for OSC 9;4, which report work and not a wait.

