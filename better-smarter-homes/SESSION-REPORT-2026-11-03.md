# Session report: cloud session of 2026-10-28 to 2026-11-03

**Project:** Better Smarter Homes ("Stone and Wire"), Revision 8
**Repository:** `jonnystokes/Random-AI-projects`, folder `better-smarter-homes/`, branch `claude/sharp-shannon-tamgu5`
**Baseline:** commit `535be81` ("Add Better Smarter Homes (Stone and Wire) manuscript project"), the snapshot of theBook taken 2026-10-28
**Cost:** **this is what $100 of API tokens bought** (Jon's figure for the session's spend)
**Report written:** 2026-11-03, after the weekly Fable limit reset

---

## 1. Summary

| Area | Before (535be81) | After (now) |
|---|---|---|
| Revision 8 chapters written | 11 of 36 | 11 of 36 finished, plus 6 more in progress (partial drafts saved) |
| Chapters read in full and judged | 8 (loop rows 1 to 8) | 11 (rows 9, 10, 11 added: chapters 24, 25, 30) |
| Writer brief | v4 (untested) | v5 (eleven new rules), being tested on six chapters |
| Named writing faults | 46 | 54 (Tier 6, faults 47 to 54) |
| Lint gates (`tools/lint.py`) | about 60 | about 66 (six added, +216 lines of code) |
| Standing rules in `AI_TODO.md` | 11 | 15 (four rules that lived only in Jon's PC memory) |
| Loop report for Jon | none | `revision8/LOOP_REPORT.md` |
| New prose in the six in-progress chapters | 27,139 words (Revision 7 baseline) | 63,614 words in the files now |

AGENT-STATE.md's four next steps:

1. **Read chapters 24, 25, 30:** done.
2. **Loop report:** done.
3. **Test brief v5 on fresh Fable writers:** in progress. All six writers stopped on the weekly limit.
4. **Phases C to G:** not started.

## 2. Timeline

All times are Pacific.

| When | What |
|---|---|
| 2026-10-28, afternoon | Both repositories surveyed, and the project's instruction system read: CLAUDE.md, AI_TODO, AGENT-STATE, STYLE_GUIDE, WRITER_BRIEF, REVIEW_CHECKLIST, CHAPTER_TEMPLATE, FAULT_CATALOG, BOOK_STRUCTURE, research index, exemplar, lint. |
| about 5:00 PM | Standing rules 12 to 15 written into `AI_TODO.md`. Three reviewer agents dispatched in parallel for chapters 24, 25 and 30. |
| about 5:45 PM | All three reviews returned. Loop rows 9 to 11 logged. All three verdicts ITERATE. |
| about 5:50 PM | WRITER_BRIEF v5 written, FAULT_CATALOG Tier 6 added, and counts corrected in README and CLAUDE.md. A lint agent was dispatched. |
| about 6:00 PM | Lint v5 gates committed. |
| about 6:05 PM | Six Fable writers dispatched at effort max: chapters 6, 18, 20, 26, 33, 36. |
| about 6:10 PM | LOOP_REPORT.md and AGENT-STATE.md written, and the batch logged. |
| 2026-10-28 night to 10-29, about 2:00 AM | All six writers hit the weekly Fable limit and stopped mid-chapter. The limit reset 2026-11-03. |

## 3. Commits pushed

Six commits, 11 files, +1,337 / -8 lines:

| Commit | Content |
|---|---|
| `8852bf5` | Standing rules 12 to 15 |
| `d38758e` | Chapter 24 reviewed (row 9, `worklogs/review-ch24.md`) |
| `d1a9cd1` | Chapter 25 reviewed (row 10, `worklogs/review-ch25.md`) |
| `ca917cd` | Chapter 30 reviewed (row 11); WRITER_BRIEF v5; FAULT_CATALOG Tier 6; counts in README and CLAUDE.md |
| `1b925c8` | `tools/lint.py`: the v5 gates |
| `0a81c2f` | LOOP_REPORT.md, AGENT-STATE.md update, batch logged |

The six writers' partial chapters, worklogs and research files are committed with this report as a labeled work-in-progress snapshot, so they survive if the cloud container is reclaimed.

## 4. Work by category

### 4.1 Process and rules (the project's control system)

- **Four rules made durable.** They were in Jon's PC memory only and missing from the files that cloud sessions read. Now in `AI_TODO.md`:
  - 12: no button questions;
  - 13: the log is kept current as the work goes, with writers kept out of it because it is shared;
  - 14: writers run on Fable only;
  - 15: where the work happens, and how `C:\Users\jon\Projects\...` paths map onto this repository.
- **One process rule tightened.** No two writers in flight may border each other at all in the cross-reference graph. The 2026-10-27 exception for single-reference pairs is withdrawn. The reason: chapters 17, 24 and 25 ran together under that exception, and now disagree on decided values.
- **Batch selection by measurement.** A script counted every "the X chapter" reference between chapters in the current manuscript. The six-chapter batch has:
  - no pair with two or more references between them;
  - no two numeric neighbors;
  - no chapter bordering one due for a redo.
- **Stale facts corrected:**
  - The brief said "35 named faults" and the catalog has 54.
  - README.md and CLAUDE.md fault counts updated.
  - Session dates corrected from UTC to Pacific.

### 4.2 Review and quality control (the chapter loop)

Three chapters were read in full by reviewer agents against REVIEW_CHECKLIST.md. Each review:
- runs the lint and the stats;
- skims the chapter against its Revision 7 text for dropped content;
- checks eight values and every dollar figure against the answer files;
- checks obligations, counts and boundaries;
- answers the twelve reading items.

The reviews total about 14,800 words:

| Review | Words | Verdict | Highlights |
|---|---|---|---|
| `review-ch24.md` | about 5,300 | ITERATE, revision pass | 211 executable Applied steps, the strongest in the loop. 8 inherited errors corrected, including Oregon not adopting NEC 230.67 and 230.85. Professional repeats Simple in 10 of 17 sections. 20 pointer sentences. A gas-valve spec cited that the HVAC chapter lacks. |
| `review-ch25.md` | about 3,900 | ITERATE, revision pass after 17 and 24 | 13 Revision 7 values corrected from Oregon code text. Disagrees with 17 on the shower set point (110°F against 120°F) and with 24 on lighting control. A study credited to the wrong journal. |
| `review-ch30.md` | about 5,600 | ITERATE, revision pass | Technical half excellent: the lifting example, the hearing-protection (NRR) and noise-dose (A(8)) arithmetic and the 2024 AQI shift all recomputed and right. About 40 sentences narrating the research or naming vague sources. 6 figures that change what their source measured. Unsourced health thresholds. ORS 654.005(5)(b) missing. |

Loop rows 9 to 11 in `AI_TODO.md` carry the full findings, numbered by fault.

### 4.3 The writer brief and the fault catalog

**WRITER_BRIEF v5** adds eleven rules, each traced to evidence in at least two chapters or flagged as a candidate:

1. No semicolons in Code value lines. There were 149 across seven chapters, uncounted until now.
2. Source lines name the document actually read. A change summary or another state's reproduction of a code is not the code.
3. Professional repeats neither Simple nor Applied, and every Professional paragraph ends on its last fact. A repeats check runs before reporting.
4. A bordering chapter's decided value is the book's value. Never write a second one.
5. Point at the text at most once per section.
6. Cross-reference one chapter at a time, with no disguised references.
7. State the finding, never the search.
8. Name weak sources as what they are, and studies by author and year.
9. A figure keeps what its source measured.
10. A threshold the plan sets is the plan's choice, tagged (Jon to confirm).
11. Jon's note does not voice the chapter's recommendations as his promises.

**FAULT_CATALOG Tier 6** names faults 47 to 54:
- 47 Code Semicolon
- 48 Text Pointer
- 49 Packed Cross-Reference
- 50 Second Value
- 51 Search Narration
- 52 Shifted Measure
- 53 Unsourced Threshold
- 54 Borrowed Resolve

### 4.4 Tooling (`tools/lint.py`)

Six gates were added, 216 lines:

| Gate | Level |
|---|---|
| Semicolons in Code requirement and value lines | FAIL |
| Sections using "the entry below" more than once | FAIL |
| Sentences pointing at other parts of the chapter | review |
| Sentences naming two or more chapters | FAIL |
| Disguised cross-references | review |
| v5 search narration and source-class wording | FAIL |

Validation:
- The lint ran on all 36 chapters before and after the change, with no crashes.
- Every quoted example from the three reviews fires.
- About 30 hits across 15 chapters were spot-checked. Seven kinds of false positive were found and removed.
- Failing gates summed over all 36 chapters went from 420 to 472.

How the eleven Revision 8 chapters fare under the new lint:

| Chapter | Failing gates |
|---|---|
| 2 | 5 |
| 3 | 9 |
| 4 | 2 |
| 5 | 2 |
| 11 | 2 |
| 17 | 1 |
| 22 | 3 |
| 24 | 3 |
| 25 | 3 |
| 27 | 2 |
| 30 | 2 |

Under the loop rule, these chapters stay as written until the redo list is worked.

### 4.5 Manuscript writing (six chapters in progress, brief v5, Fable, effort max)

| Ch | Title | Baseline | Words then → now | Sections now | Code entries | State when the limit hit |
|---|---|---|---|---|---|---|
| 6 | Structural System and Concrete Design | Revision 7 text | 15,526 → 13,861 | 15 | 41 | Writing sections in plan order. The file is mid-rewrite: part new text, part old. Closing parts not written. |
| 18 | Water Independence | skeleton | 398 → 16,422 | 17 | 18 | **First draft complete**: 19 Who-decides rows, 26 Open items plus Dropped, 16 decisions, 16 records. Was starting the first lint (13 failing gates). |
| 20 | Electrical: Service, Panels, Grounding | Revision 6 text | 5,468 → 10,157 | 12 of 14 | 50 | 20.1 to 20.12 saved. Writing 20.13, 20.14, then the closing parts. |
| 26 | Developing the Site | skeleton | 385 → 3,750 | 4 | 5 | Early sections written. |
| 33 | Personal Project Finance | skeleton | 284 → 12,396 | 14 | 31 | All sections and the closing parts present (24 Open items). Writing was finishing before the lint. |
| 36 | Business and Brand Framework | Revision 6 text | 5,078 → 7,028 | 10 | 26 | Writing section by section. |
| | **Total** | | **27,139 → 63,614** | **72** | **171** | |

Chapter 6 shows fewer words than its baseline only because it is mid-rewrite. The lint's "not lower than Revision 7" gate will hold it to the baseline at finish.

None of the six is finished. Each still owes:
- its lint pass;
- its judgment checks;
- its research file or cross-chapter flags, where those are missing;
- its report.

None has been reviewed yet.

### 4.6 Research gathered

| Source | Content |
|---|---|
| `research/new/ch20.md` | 4,900 words: 24 findings, 6 cross-chapter flags |
| `research/new/ch36.md` | 5,400 words: 34 findings |
| Writer worklogs `worklogs/ch06, 18, 20, 26, 33, 36.md` | 12,400 words: plans, item maps, and the verification each writer did |
| Downloaded primary sources in the scratchpad (not in git) | Oregon Electrical Specialty Code (OESC) 2023 and 2026 Table 1-E, the ORSC 2023 amendment summary, statewide alternate methods (SAM) 09-01 and 26-01, Pacific Power's electric service requirements, the generator-connection guide, page images from the code books |

Highlights of the verification recorded in the worklogs:

- **Chapter 20** recomputed the load program. The Revision 7 figure of about 106,000 VA connected, near 250 A, counted the battery and the array as loads and the heat pump twice. The corrected program is 88,640 VA connected.
- **Chapter 6:**
  - read ORSC 2023 chapters 2, 3, 4, 6, 8, 9 and 44 from the UpCodes Oregon route;
  - read SAM 26-01 and the BCD design-snow-load bulletin in full;
  - read FEMA P-320, sixth edition (December 2024).
- **Chapter 18** checked the Oregon Water Resources Department (OWRD) exempt-use handout and these primary texts:
  - statutes ORS 537.545, 537.141, 537.515, 537.783, 447.118 and 454.605;
  - rules OAR 918-770-0080 and OAR 340-053-0060 to -0100;
  - DEQ General Permit 2401 and DEQ's homeowner graywater guide.
- **Chapter 33** read ORS chapter 87 (lien law, eleven sections) and the property-tax statutes ORS 308.007 to 308.210, 311.250 and 311.505, 309.100, plus insurance statutes.
- **Chapter 36** read ORS 701 (contractor licensing), 672 (engineering practice), 646 (unlawful trade practices), 63 (LLCs) and 317A (corporate activity tax) from the code library and online, plus OAR 812 (Construction Contractors Board rules), 437-002-1053 (Oregon OSHA) and federal copyright law in Title 17 of the U.S. Code.
- **Chapter 26** read the 2022 Oregon Fire Code's gate rules (503.6, D103.5), Oregon's fire-separation table (ORSC R302.1) and truss rule (R802.10), and the 2023 and 2026 ORSC chapter 1.

**One gap to know about.** The worklogs for chapters 6, 18, 26 and 33 say their findings were "filed in research/new/chNN.md", but those four files do not exist. The writers appear to have planned to write them and stopped first. The findings survive in the worklogs and, partly, in the chapter text. When those writers resume, each must write its research file before reporting.

## 5. Agent use

| Agent | Count | Model | Tokens (reported) | Result |
|---|---|---|---|---|
| Reviewers (chapters 24, 25, 30) | 3 | Opus | 280k, 302k, 264k | Complete |
| Lint updater | 1 | Opus | 176k | Complete |
| Chapter writers (6, 18, 20, 26, 33, 36) | 6 | Fable, effort max | not reported (stopped by the limit) | Stopped mid-chapter, work saved |
| Orchestrator (this session) | 1 | Opus | not itemized | Rules, brief, catalog, report, logging, commits |

Total, per Jon: **$100 of API tokens.** Most of it went to the six Fable writers. Each one reads about 40,000 words of project instructions plus its research before writing a word, and the writers ran at maximum effort as standing rule 1 requires.

## 6. Where things stand, and what comes next

1. **Resume the six writers.** Each saved its work and its worklog says where it stopped. In this cloud session, a stopped writer is resumed by sending it a message; on Jon's PC, it is resumed by copying its three transcript files. If a writer can't be resumed, a fresh Fable writer starts from the same chapter file and worklog. The partial chapter is the baseline, and the Revision 7 text is still the preservation check.
2. **As each writer reports:**
   - merge its cross-chapter flags into `_cross-chapter-flags.md`;
   - lint;
   - review in full;
   - log loop rows 12 onward;
   - commit and push.
3. **If the batch passes on v5's rules,** the loop stops and the mass wave (phase C) runs on v5. Then the redo list in LOOP_REPORT.md:
   - full redo of chapters 2 and 3;
   - revision passes on 24, 25 and 30;
   - a fix pass on 4, 5, 11, 17, 22 and 27.
4. **Still waiting for Jon's go-ahead:** the items in `BUGS.md`.
