File: `AI_TODO.md`

# Revision 4 TODO

Last updated: 2026-05-07

## Fresh-Start Reading Order

Read this file after compaction, summarization, restart, or when entering the project fresh.

Read only these files first:

1. `agent.md`
2. `REVISION4_DOC_INDEX.md`
3. `AI_HANDOFF_PLANSMART.md`
4. `REVISION4_STRUCTURE_PLAN.md`
5. `AI_TODO.md`

If editing or adding manuscript text, also read:

1. `writing_style_guide.md`
2. `REVISION4_SOURCE_CROSSWALK.md`

If doing glossary work, also read:

- `REVISION4_GLOSSARY_POLICY.md`

If working on a specific chapter, read only the matching `research_questions_*.md` file when the task needs it.

Read `designer_notes.md` only when the user asks for future HTML/PDF design guidance.

## Current Workflow

1. Work one chapter at a time unless the user redirects.
2. Preserve and grow useful material. Do not silently reduce, skip, or compress unique information without user approval.
3. Use `writing_style_guide.md` for all voice, layer, cross-reference, and manuscript-writing rules.
4. Use `REVISION4_SOURCE_CROSSWALK.md` for all mapped prior-revision source paths.
5. Use the relevant research file when the user has supplied research for the active chapter range.
6. Ask the user before expanding strange inherited ideas that may be outdated or abandoned.
7. Run focused verification after each writing batch.
8. Update this TODO after each meaningful batch.
9. Keep moving through the queue until the user pauses, redirects, or asks for review.

After the main chapters are expanded:

1. Create the code lookup chapter.
2. Build the glossary last.
3. Regenerate the table of contents after headings and chapter structure are stable.

## Active Batch

Current next manuscript task:

- Wait for user review of the Chapters 1 through 8 retrofit. If the user flags more style or personification issues, revise Chapters 1 through 8 again. Do not start Chapter 9 until the user explicitly confirms that the rewrite is acceptable.

Latest completed batch:

- Applied `RETROFIT_CH1_CH8.md` to Chapters 1 through 8.
- Removed or rewrote personification and over-emotional/object-emotional phrasing, including the Chapter 1 "argued with" and "stay interested" lines, the Chapter 3 "property has to work with" line, and similar object/personality phrasing around code, land, soil, water, concrete, foundations, structure, envelope, records, and drainage.
- Kept the rewrite readable through concrete construction language: design facts, evidence, mechanisms, approval paths, field checks, and responsible actors.
- Files touched: `manuscript/BSHch01PurposePrinciplesAndHowToUseThisBook.md`, `manuscript/BSHch02OregonCodeAndComplianceMap.md`, `manuscript/BSHch03LandSiteAndFeasibility.md`, `manuscript/BSHch04LegalPermitsOwnerBuilderRulesAndInspections.md`, `manuscript/BSHch05SoilGroundPrepDrainageAndFoundationRisk.md`, `manuscript/BSHch06StructuralSystemAndConcreteDesign.md`, `manuscript/BSHch07FoundationBasementSlabsAndConcretePlacement.md`, `manuscript/BSHch08EnvelopeWaterproofingThermalPerformanceAndRadon.md`, `AI_TODO.md`, and `CHANGELOG.md`.
- Verification performed: retrofit scans for Code citation separators, old acronym and revision-history terms, banned punctuation and stock phrases, fragile navigation, displayed-form patterns, and the no-personification regex from `RETROFIT_CH1_CH8.md`. The remaining navigation hits are chapter headings or external code/standard chapter citations. The remaining form hits are ordinary construction uses of "fill." The broad no-personification regex has reviewed false positives involving human actors, technical "work" usage, or physical construction behavior.

Previous completed batch:

- Renamed the retrofit plan to `RETROFIT_CH1_CH8.md` and brought Chapter 8 explicitly into scope because it was written before the no-personification rule landed.
- Strengthened `writing_style_guide.md` so readable prose comes from clear sequence, exact nouns, active verbs, useful comparisons, and specific construction detail, not from emotional language applied to objects or a cute, jolly, sentimental, over-cheerful tone.
- Updated this TODO so Chapter 9 stays blocked until the user confirms that the Chapters 1 through 8 rewrite is acceptable.
- Files touched: `writing_style_guide.md`, `AI_TODO.md`, `RETROFIT_CH1_CH8.md`, `REVISION4_DOC_INDEX.md`, and `CHANGELOG.md`.

Earlier completed batch:

- Expanded Chapter 8 into a larger envelope chapter using the current Revision 4 draft, mapped Revision 3 and Revision 2 envelope sources, the Chapter 8 range of `research_questions_ch05_ch08.md`, and official Oregon BCD/OHA checks for current energy, blower-door, and radon details.
- Added Oregon energy compliance mapping, 2023 ORSC envelope values, additional-measure and blower-door guidance, insulation-material and foam-protection guidance, above-grade wall tie and drainage limits, below-grade envelope interface, slab-edge continuity, roof/parapet details, radon county applicability, vapor/drying guidance, envelope testing, IAQ coordination, and pre-cover acceptance checks.
- Files touched: `manuscript/BSHch08EnvelopeWaterproofingThermalPerformanceAndRadon.md`, `AI_TODO.md`, and `CHANGELOG.md`.
- Verification performed: Chapter 8 and combined Chapters 1 through 8 scans for old acronym/revision history, banned punctuation and stock phrases, old Code citation separators, fragile navigation, and displayed-form patterns. Remaining form-pattern hits are ordinary construction uses of "fill."

Older completed batch:

- Retrofitted Chapters 1 through 7 against the current `writing_style_guide.md`.
- Removed old-acronym prose references, reader-facing revision-history language, fragile internal navigation wording, theatrical lines, and non-colon Code citation separators.
- Preserved technical content, tables, decision frameworks, citation lists, inspection gates, and record logic.
- Files touched: `manuscript/BSHch01PurposePrinciplesAndHowToUseThisBook.md`, `manuscript/BSHch02OregonCodeAndComplianceMap.md`, `manuscript/BSHch03LandSiteAndFeasibility.md`, `manuscript/BSHch04LegalPermitsOwnerBuilderRulesAndInspections.md`, `manuscript/BSHch05SoilGroundPrepDrainageAndFoundationRisk.md`, `manuscript/BSHch06StructuralSystemAndConcreteDesign.md`, `manuscript/BSHch07FoundationBasementSlabsAndConcretePlacement.md`, `AI_TODO.md`, and `CHANGELOG.md`.
- Verification performed: retrofit scans for old acronym/revision history, banned punctuation and stock phrases, fragile navigation, displayed-form patterns, and old Code citation separators. Remaining hits were expected external code/standard chapter citations, chapter headings, and ordinary construction uses of "fill."

Setup for Chapter 9:

0. Do not start Chapter 9 until the user explicitly confirms that the Chapters 1 through 8 rewrite produced by `RETROFIT_CH1_CH8.md` is acceptable.
1. Read `manuscript/BSHch09PlumbingWaterSupplyPressureTreatmentAndHotWater.md`.
2. Read the Chapter 9 row in `REVISION4_SOURCE_CROSSWALK.md`.
3. Read `research_questions_ch09_ch12.md` only around the Chapter 9-relevant material.
4. Expand the chapter without deleting useful information.
5. Keep the chapter focused on water supply, pressure, storage, treatment, filtration, softening, hot water, circulation, pumps, backflow, private well or utility coordination, shutoffs, freeze protection, records, and concrete-specific plumbing routing concerns.
6. Avoid duplicating DWV, sewage, venting, slope, cleanout, and fixture-drain details that belong in the next plumbing chapter.
7. Verify the result and update this file.

## Active Chapter Queue

- [x] Apply `RETROFIT_CH1_CH8.md` to Chapters 1 through 8, including removal of all personification issues described in `writing_style_guide.md`.
- [ ] User review/acceptance of the Chapters 1 through 8 rewrite before Chapter 9 begins.
- [x] Chapter 1: Purpose, Principles, And How To Use This Book
- [x] Chapter 2: Oregon Code And Compliance Map
- [x] Chapter 3: Land, Site, And Feasibility
- [x] Chapter 4: Legal, Permits, Owner-Builder Rules, And Inspections
- [x] Chapter 5: Soil, Ground Prep, Drainage, And Foundation Risk
- [x] Chapter 6: Structural System And Concrete Design
- [x] Chapter 7: Foundation, Basement, Slabs, And Concrete Placement
- [x] Chapter 8: Envelope, Waterproofing, Thermal Performance, And Radon
- [ ] Chapter 9: Plumbing Water Supply, Pressure, Treatment, And Hot Water
- [ ] Chapter 10: Plumbing DWV, Sewage, Venting, Slope, Distance, And Fixtures
- [ ] Chapter 11: Electrical Service, Panels, Grounding, And Load Planning
- [ ] Chapter 12: Electrical Branch Circuits, Wire Size, Voltage Drop, Lighting, Low Voltage, And Future Power
- [ ] Chapter 13: HVAC, Ventilation, Humidity, And Air Quality
- [ ] Chapter 14: Interiors, Finishes, Accessibility, And Livability
- [ ] Chapter 15: Smart Home, Network, Security, And Local Automation
- [ ] Chapter 16: Materials, Suppliers, Procurement, And Substitution
- [ ] Chapter 17: Build Sequence And Site Coordination
- [ ] Chapter 18: Inspection And Approval Sequence
- [ ] Chapter 19: Testing, Commissioning, And Quality Control
- [ ] Chapter 20: Documentation, Maintenance, And Future Upgrades
- [ ] Chapter 21: Business And Brand Framework
- [ ] Chapter 22: Standards And Reference Index
- [ ] Chapter 23: Code Lookup And Compliance Cross-Reference
- [ ] Chapter 24: Glossary
- [ ] Final table of contents regeneration

Notes:

- Chapter order and final structure live in `REVISION4_STRUCTURE_PLAN.md`.
- Source paths live in `REVISION4_SOURCE_CROSSWALK.md`.
- Historical completion notes live in `CHANGELOG.md`.
