---
doc: revision log r6 — correction to revision-log.r5 (architecture file only)
seat: houston · card: sitting · 2026-10-22
---

# Revision log r6

**ARCHITECTURE.draft.r6.md is WITHDRAWN. Do not witness it.** After writing it, I checked it
against r5's on-disk bytes and found three unintended differences. In each place r6 carries the
withdrawn r4's text instead of r5's:
- the §9 docket intro, r5 lines 406–410: rewrapped and reworded;
- the docket 4 working-default cell, r5 line 416;
- the docket 8 working-default cell, r5 line 419.

revision-log.r5.md's claim that r6 "changed on exactly these lines" is therefore false for r6. That
part of revision-log.r5 is superseded here. Its lock-proposals.r4 part stands.

**ARCHITECTURE.draft.r7.md is the candidate.** I built it from r5's on-disk text, read in full this
turn. It differs from r5 on exactly these lines:

| r5 line | old | new |
|---|---|---|
| 3 | `` `state: DRAFT r5 for majkee GO — …` `` | `` `state: DRAFT r7 for majkee GO — …` `` |
| 33 | `file keeps its name. Nabla.Tmux is the name of the chatbot that wrote it (said: majkee R9-1 N7).` | `file keeps its name. "Nabla.Tmux is chatbot name - same as her project" (said: majkee R9-1 N7).` |
| 103 | `   framework. L17 places shared mechanisms at a narrow integration boundary. A proposed L17` | `   framework. L17 places shared mechanisms at a narrow integration boundary. P5 in the lock` |
| 104 | `   amendment is P5 in the lock proposals. L17 holds unchanged until a GO names P5.` | `   proposals offers a reading (P5-a) or an amendment (P5-b). L17 holds unchanged until a GO names one of them.` |

The line count is unchanged at 482. The causes are as in revision-log.r5: the assay R8d note on N7,
and P5 becoming two alternatives.

Head check: `diff raw/ARCHITECTURE.draft.r5.md raw/ARCHITECTURE.draft.r7.md` should show only these
four changed lines (three hunks: 3, 33, 103–104). Any other hunk is a defect of mine.
