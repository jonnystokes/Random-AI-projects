# AI TODO And Status

> Deprecated active workspace notice: Revision 3 structural cleanup is complete. Do not resume new work here unless the user explicitly asks. For future work, read `revision4/AI_TODO.md` and `revision4/AI_HANDOFF_PLANSMART.md`.

Last updated: 2026-04-29

## Compaction / Interruption Rule

This file must be accurate after every work batch. If a future session starts with no memory, it should:

1. Read this file first.
2. Read `AI_HANDOFF_PLANSMART.md` second.
3. Resume from the `Current Active Task` below.
4. Verify progress with the scan command listed for that task before deciding what remains.

Do not assume a previous session completed work unless it is checked off here and has a verification note.

## Recently Completed Batch

- [x] Appendix D testing procedure files.
  - Verification: scan returns only `OPSC Section 312 and 712` in `BSHappDTestingProceduresPart4MEP.md`, which is an external plumbing-code citation and should remain.
- [x] Appendix C inspection checklist files.
  - Verification: scan returns no `Section N` hits in either Appendix C file.
- [x] Appendix B materials reference files.
  - Verification: scan returns no `Section N` hits in either Appendix B file.
- [x] Appendix A code and standards reference.
  - Verification: scan returns only two external federal citations: `EPA Section 608` and `29 CFR 1926 Subpart P` sections.
- [x] Glossary cross-reference cleanup.
  - Verification: glossary has no `Section N` hits and no appendix-letter hits.
- [x] Chapter 4 reduction sub-batch 1.
  - Condensed `4.13 The High Water Table — Brief Treatment` and `4.17 Drainage — Where the Water Goes`.
  - Verification: Chapter 4 word count dropped from 11,111 to 10,015; headings still run 4.1-4.21; Chapter 4 reference scan returns no old numeric section references.

## Current Active Task

- [x] Revision 3 structural/material-placement polish only.
- User constraint: do not do editorial rewriting. Only fix structural bugs, stale seams, broken starts/ends, appendix correctness, TOC/heading consistency, and problems caused by chapter shuffling.
- Target files:
  - All `BSHch*.md`
  - All `BSHapp*.md`
  - `BSHfm01TableofContents.md`
  - `BSHglossary.md` only if structural references/placement are wrong
- First checks:

```bash
rg -n '^# |^## ' 'revision3'/BSHch*.md 'revision3'/BSHapp*.md 'revision3/BSHfm01TableofContents.md'
rg -n --glob 'BSH*.md' 'continued|Continued|next appendix|final appendix|Appendix B Supplement|Appendix C, Drainage|Section 0|End of Section|Appendix F|sec[0-9]|Section [0-9]' 'revision3'
rg -n --glob 'BSH*.md' '\bsee\s+[0-9]+\.[0-9]+|\bSee\s+[0-9]+\.[0-9]+|\bas discussed in\s+[0-9]+\.[0-9]+' 'revision3'
```

- Completion check: TODO should list structural/material-placement fixes made, scans run, and any remaining intentional external-code citations.
- Current structural scan findings to resolve:
  - [x] Chapter 1 used `### 1.x` headings directly under the chapter title. Fixed to `## 1.x`.
  - [x] Appendix C part dividers used top-level `# Part N` headings inside files that already have `# Appendix C`. Fixed to `## Part N`.
  - [x] Appendix C Foundation sequence was structurally out of order: `Inspection #10 — Concrete Pour Witness` appeared between #6 and #7. Kept the chronology and renumbered/map-fixed the foundation inspections to run #5-#10 cleanly.
  - [x] Appendix D was moved from old Appendix E but still used `E.1`-style procedure numbers and in-text cross-references. Converted Appendix D procedure numbers and local procedure references from `E.` to `D.`.
  - [x] Appendix D Part 1 had `# Part 1 — Concrete Testing`; Parts 2-4 used italic part subtitles. Standardized part dividers as `## Part N`.
  - [x] Appendix A had several malformed headings from old-number cleanup (`####  4 — ...`, duplicate title lines, duplicate horizontal rules). Cleaned the affected headings and seams.
  - [x] Appendix B split files had unclear hierarchy. Added explicit Part 1/Part 2 headings and nested material-category headings under them.
  - [x] Front matter and TOC had structural mismatches: `About This Book` was a second H1, and Chapter 1 had no TOC section list. Fixed both.
  - [x] Chapter starts/ends had a few shuffle seams: duplicate Chapter 3 subtitle, extra Chapter 4 separator, missing Chapter 14 chapter-style subtitle/separator, stale glossary `Section references` wording, and extra blank lines at the end of Appendix D Part 4.
  - [x] Appendix D Part 2 and Part 3 procedure lists omitted newly present procedures (`D.19`, `D.20`, `D.29`). Added those list entries and demoted the `D.19 + D.20 Combined Workflow` heading to a subsection so top-level procedure numbering runs cleanly.
  - [x] Re-run full TOC/heading/stale-reference scans after these fixes.
    - TOC vs actual chapter-section headings: no differences.
    - One-H1-per-file check: every `BSH*.md` file reports exactly one top-level `#` heading.
    - Stale seam scan returns only `ORSC Appendix F` in Chapter 6, which is an external code appendix and should remain.
    - Old numeric-reference scan returns only external citations: `OPSC Section 312 and 712`, `EPA Section 608`, and `29 CFR 1926 ... Sections 1926.650 through 1926.652`.
- Last completed sub-batches:
  - Appendix A sections 2-4, covering ORS, OAR, and ORSC references through the energy-efficiency subsection. Verification: Appendix A raw `Section N` hits dropped from 162 to 114.
  - Appendix A sections 5-8, covering electrical, plumbing, mechanical, and energy references. Verification: Appendix A raw `Section N` hits dropped from 114 to 51.
  - Appendix A sections 9-13, covering industry standards, federal regulations/resources, and code-compliance strategy. Verification: Appendix A now has only two preserved external federal citations.
  - Glossary lines 1-400. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 324 to 298.
  - Glossary lines 401-800. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 298 to 255.
  - Glossary lines 801-1200. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 255 to 208.
  - Glossary lines 1201-1600. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 208 to 164.
  - Glossary lines 1601-2000. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 164 to 126.
  - Glossary lines 2001-2400. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 126 to 92.
  - Glossary lines 2401-2800. Verification: no `Section N` hits remain in that range; glossary raw hits dropped from 92 to 47.
  - Glossary lines 2801-end. Verification: no `Section N` hits remain in glossary; two stale glossary appendix pointers were also changed to topic wording.
- Chapter 4 review scan:
  - Chapter 4 is 11,111 words before reduction.
  - Largest candidate sections: 4.3 Soil Types (1,023), 4.13 High Water Table (985), 4.17 Drainage (965), 4.2 Core Concepts (919), 4.5 Site Evaluation (869), 4.9 Excavation (832), 4.11 Soil Problems (827), 4.8 Slab-on-Grade (758), 4.7 Basement (701).
  - First reduction target chosen: 4.13 and 4.17 because they contain procedure/checklist detail and overlap with Envelope/Drainage material.
- Chapter 4 reduction sub-batch 1 completed:
  - `4.13 High Water Table` reduced from 985 words to 399.
  - `4.17 Drainage` reduced from 965 words to 455.
  - Chapter 4 total word count reduced from 11,111 to 10,015.
  - Heading continuity verified: Chapter 4 still runs 4.1-4.21.
  - Chapter 4 old-reference scan returns no hits.

## Action Plan Crosscheck Against User's Pasted Plan

### Done

- [x] Freeze the new chapter list and names.
- [x] Keep Business and Brand as a main chapter, now Chapter 15.
- [x] Create a crosswalk from old section numbers to new chapter/topic names in `AI_HANDOFF_PLANSMART.md`.
- [x] Convert main headings from `Section` to `Chapter`.
- [x] Rename target files so `revision3/` no longer uses `secXX` filenames.
- [x] Renumber main chapter section headings under the new chapter numbers.
- [x] Regenerate the main table of contents as `BSHfm01TableofContents.md`.
- [x] Move the glossary to the end as `BSHglossary.md`, not Appendix A.
- [x] Remove `End of Section` markers from generated target files.
- [x] Remove or rewrite references to the missing internal Appendix F. The only remaining `Appendix F` hit is `ORSC Appendix F`, an external code reference in Chapter 6.
- [x] Replace the main-book old numbered references found by the focused scan. Current main-book scan reports only external code appendix references and one physical `wall section` phrase.
- [x] Preserve external references such as `ORSC Appendix F`, `OPSC Appendix K`, NEC/OAR/ORSC/ASHRAE chapter references, and code sections.

### Revision 3 Structural Closure

- [x] Full appendix/back-matter cross-reference cleanup for old `Section N` references. Appendices A, B, C, D, and glossary are clean except for preserved external citations.
- [x] Full glossary cross-reference cleanup for old `Section N` references and stale appendix-letter references.
- [x] Final pre-Revision-4 structural scan completed on 2026-04-29:
  - File set is as expected: front matter, Chapters 1-15, Appendices A-D, glossary, and AI handoff files.
  - Every `BSH*.md` file has exactly one top-level H1.
  - TOC chapter-section entries match actual chapter section headings.
  - Appendix C inspections run #1-#27.
  - Appendix D procedures run D.1-D.39.
  - No `End of Section`, `Section 0`, old `Appendix E`, old internal `Appendix F`, old `E.x` procedure references, `secXX` filenames, or stale glossary appendix labels remain.
  - Remaining old-number scan hits are preserved external citations only.

### Deferred To Revision 4 / Not A Revision 3 Blocker

- Chapter 3 legal/licensing detail may later move partly to appendix/back matter.
- Chapter 4 is still long at about 10,014 words and may later be split, expanded, or layered.
- Chapter 6 thermal testing detail may later be moved partly to Appendix D or re-layered.
- Chapter 8 wire schedule/spec-style material may later move partly to an appendix.
- Appendix material may later be promoted into main chapters if Revision 4 needs easy/medium/advanced topic layers.
- Full AI-tone/style editing was intentionally not done in Revision 3 closure.
- Final publishing polish can wait until Revision 4 structure is known.

## Current Reference Cleanup Status

- Main chapters: focused internal-reference scan is clean except for `ORSC Appendix F`, which is an external code reference and should remain.
- Main chapters: generic old `this section` scan only finds `defined wall section` in Chapter 12, which is a physical construction phrase and should remain.
- Main chapters: appendix-letter scan only finds external code appendices:
  - `OPSC Appendix K` in Chapter 7.
  - `ORSC Appendix F` in Chapter 6.
- All BSH files: raw old `Section N` reference count is currently 3, all preserved external citations:
  - `EPA Section 608` in Appendix A.
  - `29 CFR 1926` sections in Appendix A.
  - `OPSC Section 312 and 712` in Appendix D Part 4.
- Bare numeric-reference scan (`see 7.12`, `See 10.13`, etc.) returns no hits across BSH files.
- `End of Section` / `Section 0` scan returns no hits.
- `Appendix F` scan returns only `ORSC Appendix F` in Chapter 6, an external code appendix that should remain.
- Raw old `Section N` references by file:
  - `BSHappACodeandStandardsReference.md`: 2 preserved external federal citations.
  - `BSHappDTestingProceduresPart4MEP.md`: 1 preserved external OPSC citation.
  - `BSHglossary.md`: 0.

## Completed After Current Session Resumed

- Added the compaction/interruption protocol to `AI_HANDOFF_PLANSMART.md` and this TODO.
- Added an explicit active-task checkpoint format so future sessions know what to scan before resuming.
- Cleaned Appendix D old internal section references:
  - Part 1 Concrete: `per Section 4` -> Structural Design chapter wording.
  - Part 2 Soil: old Section 14, 14.4, 14.4.4, 14.11, 14.13, 14.13.1, 14.13.3, 14.16, and 14.20 references -> Ground Prep/Foundation Risk topic wording or removed where redundant.
  - Part 3 Envelope and Air: `Section 14.9 and Section 6` -> Ground Prep/Foundation Risk chapter and Envelope chapter wording.
- Verified Appendix D now has only one `Section N` hit: `OPSC Section 312 and 712` in Part 4 MEP, which is an external plumbing-code citation and should remain.
- Cleaned Appendix C old internal section references:
  - Project-binder `Section 1`, `Section 3`, `Section 6`, and `Section 11.6` references -> binder-tab wording.
  - Main-book `Section 3`, `Section 6`, `Section 7`, `Section 4`, and `Section 8.11` references -> named chapter/topic wording.
  - Verified both Appendix C files now have no `Section N` hits.
- Cleaned Appendix B old internal section references:
  - Part 1 structural, envelope, plumbing, interiors, and testing references -> named chapter/topic wording.
  - Part 2 electrical, HVAC, smart-home, interiors, tools, and testing references -> named chapter/topic wording.
  - Appendix B internal `Section 5 of Part 1` / `Section 5.2 of Part 1` references -> local Part 1 topic wording.
  - Verified both Appendix B files now have no `Section N` hits.
- Cleaned Appendix A sub-batch 1:
  - ORS/OAR/ORSC `Where referenced` lines were changed from old section numbers to named chapter/topic references.
  - Actual external ORS/OAR/ORSC chapter and rule labels were preserved.
  - Verification: Appendix A old `Section N` hits dropped from 162 to 114.
- Cleaned Appendix A sub-batch 2:
  - Electrical, plumbing, mechanical, and local energy-code `Where referenced` lines were changed from old section numbers to named chapter/topic references.
  - Actual external NEC/OPSC/OMSC/ORSC chapter, article, appendix, and code labels were preserved.
  - Verification: Appendix A old `Section N` hits dropped from 114 to 51.
- Cleaned Appendix A sub-batch 3:
  - Industry standards, federal resources, and code-compliance strategy references were changed from old section numbers to named chapter/topic references.
  - Actual external `EPA Section 608` and `29 CFR 1926` section citations were preserved.
  - Verification: Appendix A now has only two `Section N` hits, both external federal citations that should remain.
- Cleaned glossary sub-batch 1:
  - Lines 1-400 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 1-400; glossary raw hits dropped from 324 to 298.
- Cleaned glossary sub-batch 2:
  - Lines 401-800 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 401-800; glossary raw hits dropped from 298 to 255.
- Cleaned glossary sub-batch 3:
  - Lines 801-1200 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 801-1200; glossary raw hits dropped from 255 to 208.
- Cleaned glossary sub-batch 4:
  - Lines 1201-1600 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 1201-1600; glossary raw hits dropped from 208 to 164.
- Cleaned glossary sub-batch 5:
  - Lines 1601-2000 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 1601-2000; glossary raw hits dropped from 164 to 126.
- Cleaned glossary sub-batch 6:
  - Lines 2001-2400 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 2001-2400; glossary raw hits dropped from 126 to 92.
- Cleaned glossary sub-batch 7:
  - Lines 2401-2800 old section references were changed to named chapter/topic references.
  - Verification: no `Section N` hits remain in glossary lines 2401-2800; glossary raw hits dropped from 92 to 47.
- Cleaned glossary sub-batch 8:
  - Lines 2801-end old section references were changed to named chapter/topic references.
  - Two stale glossary appendix pointers were changed to topic wording: `Appendix B Supplement` -> code and standards appendix; `Appendix C, Drainage` -> Drainage.
  - Verification: glossary has no `Section N` hits and no appendix-letter hits.
- Ran broad final reference scans:
  - All BSH `Section N` hits: only 3 external citations remain.
  - All BSH bare numeric references like `see 7.12`: no hits.
  - All BSH `End of Section` / `Section 0`: no hits.
  - All BSH `Appendix F`: only external `ORSC Appendix F`.

## Completed Before This Handoff File

- Created the revised book in `revision3/`.
- Preserved `revision2/` as the original source.
- Converted the main old sections into chapters.
- Kept Business and Brand as Chapter 15.
- Moved the glossary to final back matter as `BSHglossary.md`.
- Reassigned appendices:
  - Old Code Reference -> Appendix A.
  - Old Materials Reference -> Appendix B.
  - Old Inspection Checklists -> Appendix C.
  - Old Testing Procedures -> Appendix D.
- Created `BSHfm01TableofContents.md`.
- Removed `End of Section` markers during generation.
- Replaced many main-book numeric references with named chapter/topic references.
- Condensed old soil Section 14 into Chapter 4 and moved/left detailed testing procedure material in appendices.
- Created Chapter 14 from documentation, maintenance, future upgrade, contingency, and project-binder material.
- Fixed early heading-numbering issues in Chapters 1, 4, and 13.
- Removed internal references to the missing Appendix F during generation.

## Current Cleanup Batch

- [x] Create context-saving handoff files.
- [x] Replace remaining old whole-chapter `this section` wording in main chapters where it means the old manuscript section.
- [x] Convert the wrong main-book `see Appendix D` inspection-checklist reference in Chapter 4 to topic wording.
- [x] Remove leftover internal `Appendix F` references from Appendix D testing files.
- [x] Preserve external code references such as `OPSC Appendix K` and `ORSC Appendix F`.
- [x] Run final scans for broken internal numeric references, old section markers, Appendix F references, and heading structure.
- [x] Update this TODO with the exact verification results.

## Completed After This Handoff File Was Created

- Created `AI_HANDOFF_PLANSMART.md`.
- Created this `AI_TODO.md`.
- Edited Chapters 2, 3, 4, 5, 6, and 12 to replace old structural `this section` wording with `this chapter`, `this discussion`, or `this part of the chapter` as appropriate.
- Changed Chapter 4's old `see Appendix D` inspection reference to `see the inspection checklists appendix`.
- Removed Appendix D references to the missing internal `Appendix F`:
  - Concrete testing intro and checklist references.
  - Soil testing data-recording headings and DCP data sheet reference.
  - Final Appendix D Part 4 note that pointed to a nonexistent templates appendix.
- Changed two old Appendix D references to old main sections into topic wording:
  - Old Section 12 testing-program reference -> Testing, Commissioning, and Quality Control chapter.
  - Old Section 14.11 compaction reference -> soil compaction guidance in the ground preparation chapter.

## Latest Verification Results

- Main chapter numeric-reference scan reports only `ORSC Appendix F` in Chapter 6. This is an external code appendix and should remain.
- Main chapter generic `this section` scan reports only `defined wall section` in Chapter 12. This is a physical wall-section reference and should remain.
- Main chapter appendix scan reports only external code appendices:
  - `OPSC Appendix K` in Chapter 7.
  - `ORSC Appendix F` in Chapter 6.
- Whole BSH-file `Appendix F` scan reports only `ORSC Appendix F` in Chapter 6.
- Heading scan shows Chapters 1-15 in order, with Chapter 4 running 4.1-4.21 and Chapter 13 running 13.1-13.13.
- Latest sampled word counts after structural polish: Chapter 4 is 10,014 words, glossary is 25,334 words, Appendix A is 14,623 words, and Appendix D Part 2 is 11,831 words.

## Known Remaining Watch Items

- Appendix files have been cleaned of old internal `Section N`, old `Appendix E`, and old internal `Appendix F` references found by the structural scans. Remaining `Section N` hits are preserved external-code citations.
- Main chapters and appendices may still use the word `section` correctly for physical wall sections, binder sections, code sections, local subsections, or tool/material categories. Do not blindly replace every instance.
- `ORSC Appendix F` in Chapter 6 is an external code reference, not the missing internal Appendix F.
- `OPSC Appendix K` in Chapter 7 is an external code reference.
- Chapter 4 is still long. It was reduced from the original soil/testing section, but it may need a later editorial reduction pass after the structure is accepted.
- The current phase is structural/material-placement polish only. Do not start the full editorial tone pass or Revision 4 expansion until the user explicitly starts that phase.

## Suggested Next Work Areas

- Wait for user review of Revision 3 structural polish.
- After user approval, start Revision 4 planning using the user's detailed Revision 4 vision.
- Later Revision 4 work may revisit Chapter 4 length, difficulty-level layering, appendix expansion, and tone/style, but that was intentionally not done in this batch.
