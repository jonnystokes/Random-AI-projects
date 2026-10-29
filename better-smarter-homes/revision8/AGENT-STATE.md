# Writer agents: state and how to carry on

Written 2026-10-28 so the work can continue on another computer.

## Where things stand

No writer is in the middle of anything. Every writer dispatched so far finished its chapter.
Each chapter, its worklog, its research file and its cross-chapter flags are committed. Nothing
is half-written.

| Chapter | Writer agent id | Brief | Model | State |
|---|---|---|---|---|
| 2 Oregon code and compliance map | a279f3abc4b086a01 | v1 | Fable | Done, read, loop row 1 |
| 3 Land, site and feasibility | a79dd94a7aa647569 | v2 | Fable | Done, read, loop row 2 |
| 4 Legal, permits and owner-builder rules | affa35d2a5715820e | v3 | Fable, then Opus | Done, read, loop row 3 |
| 5 Soil, ground prep, drainage | aaa005a81e4e8b87f | v3 | Fable, then Opus | Done, read |
| 11 The wall system | af5b755077ab0f633 | v3 | Fable, then Opus | Done, read |
| 17 Plumbing and water supply | ab5ad3bab4c151ddc | v3 | Opus, then Fable | Done, read |
| 22 Solar, battery and energy independence | aceb05fa4c06c9241 | v3 | Opus, then Fable | Done, read |
| 24 Smart home, network and security | aec4a300727fdc383 | v3 | Opus, then Fable | Done, read (row 9, review-ch24.md); revision pass due |
| 25 Interiors | a3ccc1465683b7aa9 | v3 | Opus, then Fable | Done, read (row 10, review-ch25.md); revision pass due after 17 and 24 |
| 27 Tools, equipment and the shop | a8ff377827e04cef1 | v3 | Opus, then Fable | Done, read |
| 30 The owner-builder's body and mind | a2c1d08749fac32fc | v3 | Opus, then Fable | Done, read (row 11, review-ch30.md); revision pass due |

The agent ids work only on Jon's Windows PC. That is where their transcripts are:
`C:\Users\jon\.claude\projects\C--Users-jon-Projects\d15f463d-24c9-4827-81fc-968b15964077\subagents\`.
Writers 24 and 30 also have copies in the folder for session 14282c9a-7a9b-4ba4-a512-1facaaf6413e.
On that PC, any of them can be resumed with SendMessage to its id. After a session change, first
copy its three files (`.jsonl`, `.meta.json`, `.prefix.json`) into the current session's
`subagents` folder.

## 2026-10-28 cloud session (GitHub copy, branch claude/sharp-shannon-tamgu5)

Steps 1 and 2 above are done: chapters 24, 25 and 30 read in full (loop rows 9 to 11), the brief
moved to v5, and the loop report is LOOP_REPORT.md. Step 3 is running: six writers on Fable, effort
max, under brief v5, started about 6:05 PM. Their agent ids live only in this cloud session; if it
ends, a new session restarts any unfinished chapter from its worklog (the chapter file holds
whatever was saved).

| Chapter | Brief | Model | State |
|---|---|---|---|
| 6 Structural system and concrete design | v5 | Fable | Writing |
| 18 Water independence (skeleton) | v5 | Fable | Writing |
| 20 Electrical service, panels, grounding | v5 | Fable | Writing |
| 26 Developing the site (skeleton) | v5 | Fable | Writing |
| 33 Personal project finance (skeleton) | v5 | Fable | Writing |
| 36 Business and brand framework | v5 | Fable | Writing |

## Carrying on from another computer

Agents can't be resumed off that PC, and none needs to be. Everything a writer knew is in the files:

- `revision8/AI_TODO.md` holds the standing rules, the loop log, the STATUS line and phases C to G plus F2.
- `revision8/WRITER_BRIEF.md` (version 4) is what a new writer is handed.
- `revision8/worklogs/chNN.md` holds each writer's plan, item map and decisions.
- `revision8/research/new/chNN.md` holds each writer's findings.
- `revision8/research/new/_cross-chapter-flags.md` holds every flag merged so far.

Next steps, in order:

1. Read chapters 24, 25 and 30 in full against `REVIEW_CHECKLIST.md`. Log each in the AI_TODO loop log.
2. Write the loop report for Jon: rounds, lessons, comparison, redo list.
3. Test brief v4 on a fresh batch of writers on Fable, no two sharing a file or a chapter boundary.
4. Continue with AI_TODO phases C to G, including F2: Jon's to-dos, then the last pass with Jon.

A new writer is started fresh from `WRITER_BRIEF.md`, with the same dispatch shape as the earlier ones:
its chapter file, answer files, bordering chapters and Revision 7 baseline. Writers always run on Fable.
