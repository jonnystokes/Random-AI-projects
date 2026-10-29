# PlanSmart Handoff Instructions

> Deprecated active workspace notice: Revision 3 structural cleanup is complete. Do not use this as the active plan for new work unless the user explicitly asks. Future work should start in `revision4/` by reading `revision4/AI_TODO.md` and `revision4/AI_HANDOFF_PLANSMART.md`.

Last updated: 2026-04-29

## Mission

Continue turning the book from a numbered "section" manuscript into a chapter-based book. The active working copy is `revision3/`. The source copy is `revision2/` and should stay unchanged unless the user explicitly asks otherwise.

The user wants structural cleanup first, not a deep style rewrite yet. Keep edits pragmatic: fix broken organization, broken references, obvious AI/revision residue, and heading/TOC problems. Avoid expanding the manuscript unless a short bridge sentence is needed.

## Context-Saving Strategy

Do not reread the whole book into context unless absolutely necessary. Use targeted scans and line windows:

- Use `rg --files` to list files.
- Use `rg -n '^#|^##|^###' 'revision3'` for structure.
- Use `nl -ba file | sed -n 'start,endp'` for only the surrounding context needed.
- Use the generated table of contents as the first map, then inspect only files with search hits.
- Keep `revision2/` as source-of-truth for original wording only when a target chapter looks corrupted or missing.
- Prefer one chapter-sized task at a time and update `AI_TODO.md` before moving to a new area.

## Compaction-Safe Work Protocol

Assume compaction or interruption can happen after any command. Before starting each new work area:

1. Update `AI_TODO.md` with the active task, target files, planned scan, and expected completion check.
2. Work in the smallest useful batch, usually one appendix part, one chapter, or one reference pattern.
3. After editing, run a targeted verification scan for that batch.
4. Update `AI_TODO.md` again with what changed, what scan was run, and what remains.
5. Only then move to the next batch.

If resuming after memory loss, read only these files first:

1. `revision3/AI_TODO.md`
2. `revision3/AI_HANDOFF_PLANSMART.md`
3. The specific file named in the current active task

Do not reload the full manuscript unless the TODO says a broad review is the active task.

## Current Target Structure

Front matter:

- `BSHfm00CoverandIntro.md`
- `BSHfm01TableofContents.md`

Main book:

- Chapter 1: `BSHch01PurposeandPrinciples.md`
- Chapter 2: `BSHch02LandSiteandFeasibility.md`
- Chapter 3: `BSHch03LegalPermitsandInspections.md`
- Chapter 4: `BSHch04SoilGroundPrepandFoundationRisk.md`
- Chapter 5: `BSHch05StructuralDesign.md`
- Chapter 6: `BSHch06EnvelopeWaterandThermalPerformance.md`
- Chapter 7: `BSHch07PlumbingSystems.md`
- Chapter 8: `BSHch08ElectricalPowerandLighting.md`
- Chapter 9: `BSHch09HVACVentilationandAirQuality.md`
- Chapter 10: `BSHch10InteriorsFinishesandLivability.md`
- Chapter 11: `BSHch11SmartHomeandNetworkSystems.md`
- Chapter 12: `BSHch12BuildSequence.md`
- Chapter 13: `BSHch13TestingCommissioningandQualityControl.md`
- Chapter 14: `BSHch14DocumentationMaintenanceandFutureUpgrades.md`
- Chapter 15: `BSHch15BusinessandBrandFramework.md`

Back matter:

- `BSHappACodeandStandardsReference.md`
- `BSHappBMaterialsReferencePart1.md`
- `BSHappBMaterialsReferencePart2.md`
- `BSHappCInspectionChecklistsPart1.md`
- `BSHappCInspectionChecklistsPart2.md`
- `BSHappDTestingProceduresPart1Concrete.md`
- `BSHappDTestingProceduresPart2Soil.md`
- `BSHappDTestingProceduresPart3EnvelopeandAir.md`
- `BSHappDTestingProceduresPart4MEP.md`
- `BSHglossary.md`

## Source Mapping

- Old Section 0 -> Chapter 1.
- Old Section 1 -> Chapter 2.
- Old Sections 2 and 3 -> Chapter 3.
- Old Section 14 -> condensed Chapter 4, with detailed test/procedure material moved or left in appendices.
- Old Section 4 -> Chapter 5.
- Old Section 5 -> Chapter 6.
- Old Section 6 -> Chapter 7.
- Old Section 7 -> Chapter 8.
- Old Section 8 -> Chapter 9.
- Old Section 9 -> Chapter 10.
- Old Section 10 -> Chapter 11, with upgrade/maintenance strategy moved to Chapter 14.
- Old Section 11 -> Chapter 12, with project binder/documentation and contingency material moved to Chapter 14.
- Old Section 12 -> Chapter 13.
- Old Section 13 -> Chapter 15.
- Old Appendix A Glossary -> `BSHglossary.md` at the end, not in the middle.
- Old Appendix B Code Reference -> Appendix A.
- Old Appendix C Materials -> Appendix B.
- Old Appendix D Inspection Checklists -> Appendix C.
- Old Appendix E Testing Procedures -> Appendix D.

## Rules From The User

- Keep Business and Brand as a main chapter for now.
- Do not create the missing internal Appendix F. Remove internal references to it.
- Remove all `End of Section` markers.
- Replace main-book references to old section/chapter numbers with chapter names or topic wording.
- Do not accidentally rewrite external references such as NEC chapters, OAR chapters, ORSC chapters, ASHRAE chapters, OPSC appendices, or ORSC appendices.
- Appendix references can be updated after the chapter structure is finalized, but obvious wrong main-book appendix letters should be converted to topic wording now.
- The order should feel natural: planning, site, legal, ground/foundation risk, design, systems, build, testing, documentation, business.

## How To Find Remaining Breakage

Run these scans after any meaningful batch of edits:

```bash
rg -n --glob 'BSHch*.md' '\b[Ss]ection\s+[0-9]+|\b[Ss]ections\s+[0-9]+|\bsee\s+[0-9]+\.[0-9]+|\bSee\s+[0-9]+\.[0-9]+|\bfrom\s+[0-9]+\.[0-9]+|\bAppendix\s+F\b|End of Section|Section 0|this chapter\.[0-9]|chapter\.[0-9]' 'revision3'
rg -n --glob 'BSHch*.md' '\b[Tt]his section\b|\bsection covers\b|\bsection is\b|\bsection describes\b|\bsection helps\b|\bsection lays out\b' 'revision3'
rg -n --glob 'BSH*.md' 'End of Section|Section 0|Appendix F' 'revision3'
rg -n '^# |^## |^### ' 'revision3'
```

For appendix-letter references, separate internal book references from external code references:

```bash
rg -n --glob 'BSHch*.md' '\bAppendix [A-Z]\b' 'revision3'
```

Leave examples like `ORSC Appendix F` and `OPSC Appendix K` alone unless the user explicitly asks for external-code citation cleanup.

## Replacement Method

When a numeric reference is found in a main chapter:

1. Read 5-15 lines before and after the hit.
2. Decide whether it is internal book structure or external law/code/standard.
3. If internal, replace with a named chapter or topic phrase.
4. If external, preserve it.
5. If it points to appendix material and the new appendix letters are unstable, use topic wording such as `the inspection checklists appendix` or `the testing procedures appendix`.

Examples:

- `See Section 7` -> `See the Electrical Power and Lighting chapter`.
- `See Section 14.13` -> `See the soil improvement discussion`.
- `see Appendix D` when it means old inspection checklists -> `see the inspection checklists appendix`.
- `NEC Chapter 7` -> leave unchanged.
- `ORSC Appendix F` -> leave unchanged because it is an external code appendix.

## Editing Priorities

Highest impact, easiest first:

- Remove old section-language residue.
- Remove internal Appendix F references.
- Fix broken TOC and heading names.
- Fix duplicated or skipped heading numbers within each chapter.

Next:

- Verify each chapter opens and closes like a chapter, not an extracted section.
- Move short misplaced paragraphs to the chapter where the reader expects them.
- Keep Chapter 4 shorter than the old soil-testing section; detailed procedures belong in Appendix D or checklist appendices.

Later, after user review:

- Full appendix cross-reference renumbering.
- Deeper prose rewrite for AI tone.
- Style pass for repetition, unnatural transitions, and overexplaining.
- Build a final front-matter/back-matter package.

## Current Recommended Next Sequence

The user narrowed the current phase to material-placement review and structural improvement only. Do not do the later AI-tone/style pass, broad editorial reduction, or Revision 4 expansion yet.

Revision 3 structural/material-placement cleanup is complete. Back-matter cross-reference cleanup is complete except for preserved external citations.

Completed:

- Appendix D testing procedures, except one preserved external OPSC citation.
- Appendix C inspection checklists.
- Appendix B materials references.
- Appendix A code and standards reference, except preserved external EPA/CFR citations.

Completed final structural polish targets:

1. Fixed heading hierarchy issues caused by the section-to-chapter conversion.
2. Fixed appendix part dividers so each file has one top-level appendix heading.
3. Fixed Appendix C inspection sequence numbering/map glitches caused by the shuffle.
4. Fixed Appendix D procedure numbering from old `E.x` to current `D.x`.
5. Ran final structural scans.
6. Verified every `BSH*.md` file has exactly one top-level H1.
7. Verified the TOC chapter-section entries match actual chapter section headings.
8. Verified Appendix C inspections run #1-#27 and Appendix D procedures run D.1-D.39.
9. Verified no `End of Section`, `Section 0`, old `Appendix E`, old internal `Appendix F`, old `E.x` procedure references, `secXX` filenames, or stale glossary appendix labels remain.

Next, after user approval/review, begin Revision 4 planning. Do not start Revision 4 until the user explicitly provides that full direction.

Preserved `Section N` hits after cleanup are external citations only: `EPA Section 608`, `29 CFR 1926` sections, and `OPSC Section 312 and 712`. Preserved `Appendix F` hit is `ORSC Appendix F`, an external code appendix. Do not remove these unless the user asks to remove external-code citations too.

## Verification Expectations

Before saying the reorganization pass is complete, run:

```bash
for f in 'revision3'/*.md; do printf '%s\t' "$f"; wc -w < "$f"; done
rg -n --glob 'BSHch*.md' '\b[Ss]ection\s+[0-9]+|\b[Ss]ections\s+[0-9]+|\bsee\s+[0-9]+\.[0-9]+|\bSee\s+[0-9]+\.[0-9]+|\bfrom\s+[0-9]+\.[0-9]+|\bAppendix\s+F\b|End of Section|Section 0|this chapter\.[0-9]|chapter\.[0-9]' 'revision3'
rg -n --glob 'BSHch*.md' '\b[Tt]his section\b|\bsection covers\b|\bsection is\b|\bsection describes\b|\bsection helps\b|\bsection lays out\b' 'revision3'
rg -n --glob 'BSH*.md' 'End of Section|Section 0|Appendix F' 'revision3'
rg -n '^# |^## ' 'revision3'
```

If a scan returns hits, inspect the context instead of replacing blindly.
