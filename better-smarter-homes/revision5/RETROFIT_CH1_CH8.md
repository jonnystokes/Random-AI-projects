File: `RETROFIT_CH1_CH8.md`

# Retrofit Plan For Chapters 1 Through 8

Last updated: 2026-05-07

## Purpose

This file is the working plan for retrofitting Chapters 1 through 8 against the current `writing_style_guide.md`.

Chapters 1 through 8 were expanded before the absolute no-personification rule landed. Apply the current style guide to all eight chapters before writing Chapter 9.

The retrofit must remove the personification issues described in `writing_style_guide.md`: inanimate things must not have intentions, feelings, opinions, preferences, demands, votes, interests, or human actions. Replace those sentences with language built around the real actor, mechanism, condition, evidence, or decision. Keep the prose readable through specificity, rhythm, and useful detail, not through emotional language applied to objects.

The retrofit also covers the warmer, grounded, informative voice; removal of reader-facing revision history; colon-format Code citations; removal of the old project acronym; and reduced theatricality.

This file can be deleted once the retrofit is complete and verified.

## Mechanical Passes

These passes can be run across all eight chapters with little or no voice judgment. They should happen before prose rewriting so the later passes start from a cleaner manuscript.

### 1. Code Citation Separator Pass

Change Code citation lines that use a hyphen separator into the colon format.

Example:

```text
ORSC R401.3 - drainage around foundations.
```

becomes:

```text
ORSC R401.3: drainage around foundations.
```

Why: `writing_style_guide.md`, `Code`, requires colon-format citations.

Source of change: recent style-guide update.

Verify:

```bash
rg -n "^[[:space:]]*- .* - " manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Then spot-check that ordinary prose hyphens were not changed incorrectly.

### 2. Old Project Acronym Search Pass

Search Chapters 1 through 8 for the old project acronym as a standalone token. Record every hit before rewriting.

Why: `writing_style_guide.md`, `Project-Specific Cleanup`, says the old acronym should be removed naturally from the manuscript.

Source of change: recent style-guide update.

Verify:

```bash
rg -n "\bOLD_ACRONYM_TOKEN\b" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Replace `OLD_ACRONYM_TOKEN` with the actual acronym when executing. Do not patch by swapping in a clumsy phrase. Sentences containing it need natural rewriting, so final fixes belong in the judgment pass.

### 3. Reader-Facing Revision-History Search Pass

Search for manuscript-development language:

- `old source`
- `old drafts`
- `source history`
- `source material`
- `current manuscript`
- `prior draft`
- `earlier draft`
- `this revision`

Why: `writing_style_guide.md`, `Project-Specific Cleanup`, says reader-facing text should not mention prior drafts, source material, revision history, or how the book was developed.

Source of change: audit of Chapters 1 through 7, Chapter 8 expansion review, and recent style-guide updates.

Verify:

```bash
rg -n "old source|old drafts|source history|source material|current manuscript|prior draft|earlier draft|this revision" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Most hits need rewriting, not simple deletion, because they often preserve useful technical corrections.

### 4. Fragile Navigation Search Pass

Search for internal book-navigation wording:

- `previous chapter`
- `next chapter`
- `See Chapter`
- `see Chapter`
- `Chapter [number]` when it refers to this book
- `later chapters`

Why: `writing_style_guide.md`, `Chapter References`, keeps manuscript text stable when chapters move.

Source of change: previous cross-reference cleanup and current style-guide ownership.

Verify:

```bash
rg -n "previous chapter|next chapter|[Ss]ee Chapter|later chapters|Chapter [0-9]+" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Do not change external source references such as ORSC chapters, OAR chapters, ACI chapters, NEC chapters, or ASHRAE chapters.

### 5. Banned Punctuation And Stock Phrase Pass

Search for em dashes, en dashes, and common stock phrases.

Why: `writing_style_guide.md`, `What The Voice Avoids`, and `Practical Construction Style`.

Source of change: standing manuscript rule and updated style-guide cleanup.

Verify:

```bash
rg -n "—|–|delve|tapestry|realm|landscape|it is important to note|ultimately|not just .*, but|crucial|pivotal|robust|seamless|leverage|foster|elevate|navigate|transformative" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Use judgment before changing technical uses of words that may be legitimate in context.

### 6. Displayed Forms Pass

Search for blank-form patterns, fill-in fields, or form-like templates.

Why: `writing_style_guide.md`, `Forms And Records`, and `designer_notes.md`, `Forms Policy`, say forms may be referenced but not displayed.

Source of change: long-standing user rule preserved in the current documentation.

Verify:

```bash
rg -n "____|\\[blank\\]|fill in|form below|template|Name:|Date:|Signature:" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Do not remove normal checklists or record descriptions. Only displayed forms are out.

## Judgment Passes

These passes require reading and rewriting. Do not strip useful information just because a sentence has old style.

### 1. Remove Personification Completely

Remove every personification issue described in `writing_style_guide.md`, `Absolute Rule: No Personification`.

Inanimate things do not have intentions, feelings, opinions, preferences, demands, votes, interests, personalities, or human actions. This applies to the book, manuscript, chapter, house, property, site, land, soil, materials, systems, code, weather, water, concrete, tools, drawings, records, and every other inanimate noun.

Rewrite around the real actor, mechanism, condition, evidence, or decision.

Examples:

```text
The property has to work with zoning.
```

should become:

```text
The design must account for zoning.
```

```text
The site is telling you to change the footprint.
```

should become:

```text
The test results indicate that the footprint should change.
```

Caution: do not replace personification with bland filler. Keep the sentence useful and readable by naming concrete evidence, physical behavior, design constraints, approval paths, craft decisions, or the person responsible for the action.

### 2. Warm The Voice And Reduce Theatricality

Change emotional, figurative, metaphorical, or exaggerated language into grounded explanation.

Underlying rule: `writing_style_guide.md`, `Core Voice`, `What The Voice Avoids`, `Absolute Rule: No Personification`, and `Project-Specific Cleanup`.

Use warmth through specifics. Keep practical interest. Remove theatricality, scolding, jolly overstatement, and dramatic flourish.

Caution: do not flatten the book into sterile prose. The goal is not blandness. The goal is a knowledgeable person explaining real work clearly.

### 3. Replace Punch-Line Closers With Technical Endings

Remove manufactured closers, callbacks, aphoristic final lines, and endings that exist mainly for effect.

Underlying rule: `writing_style_guide.md`, `Chapter Endings`.

Technical chapters can stop when the information stops: after the last step, source, inspection point, tolerance, record, or decision.

Caution: do not remove useful final checks. A closing checklist item can stay if it carries work.

### 4. Remove Reader-Facing Revision History While Preserving Knowledge

Rewrite passages that mention old drafts, source material, source history, current manuscript state, or revision decisions.

Underlying rule: `writing_style_guide.md`, `Project-Specific Cleanup`.

Many of these passages contain important corrections. Preserve the corrected guidance and remove only the revision trail.

Example pattern:

```text
The old source favored a thick insulation strategy...
```

should become a reader-facing technical statement about insulation strategy, limits, and approved design.

Caution: do not delete source-derived technical ideas merely because their sentence mentions an earlier draft.

### 5. Remove The Old Project Acronym Naturally

Rewrite sentences that use the old project acronym. Replace the thought with natural language: this house, the concrete home, the project, the owner-builder, the manuscript, or the specific system.

Underlying rule: `writing_style_guide.md`, `Project-Specific Cleanup`.

Caution: do not perform blind acronym replacement. Some passages, especially the brand and LLC material, may need a careful rewrite or user confirmation about what brand language still belongs.

### 6. Reframe Risk Passages With A Path Forward

For risk-heavy passages, use the current pattern:

```text
One issue is...
The cleaner path is...
```

or a natural equivalent.

Underlying rule: `writing_style_guide.md`, `Risk And Problem Pattern`.

Every problem should leave the reader with a practical next step, workaround, safer version, or better alternative.

Caution: do not remove real warnings. The goal is capability, not softness.

### 7. Layer Value Pass

Check each `Simple`, `Applied`, `Professional`, and `Code` block against the current layer rules.

Underlying rule: `writing_style_guide.md`, `Reader Layers`, `Layer Shape`, `Simple`, `Applied`, `Professional`, and `Code`.

All four layers can remain where each adds value. Fewer layers are fine where the missing layers would be filler.

Caution: do not cut layers for the sake of minimalism. The retrofit is about value and clarity, not shrinking the book.

### 8. Preserve Code Specificity

Keep Code blocks citation-based. Add colon format where needed. Do not turn Code into general caution prose.

Underlying rule: `writing_style_guide.md`, `Code`, and `Authority And Uncertainty`.

Caution: do not invent missing citations during retrofit. If a needed citation is missing and cannot be verified from accepted sources, mark it for research.

### 9. Remove Or Reword Development-Process Material In Chapter 1

Chapter 1 contains project-origin and AI-tool material. The current style guide says reader-facing text should not discuss how the book was developed.

Underlying rule: `writing_style_guide.md`, `Project-Specific Cleanup`.

Caution: preserve the true project vision and long-life-home purpose. Remove development-process explanation only where it makes the book feel like a revision artifact.

## Suggested Order Of Passes

1. Run mechanical search passes and save hit lists.
2. Standardize Code citation separators.
3. Remove or rewrite old project acronym hits.
4. Remove or rewrite reader-facing revision-history hits.
5. Fix fragile internal navigation.
6. Run the banned punctuation and stock phrase pass.
7. Remove personification across Chapters 1 through 8 using the examples and rule text in `writing_style_guide.md`.
8. Do the per-chapter voice retrofit, starting with the sections that had audit notes.
9. Do layer-value review in technical chapters.
10. Do final verification scans.
11. Update `AI_TODO.md` and `CHANGELOG.md`.

## Per-Chapter Notes

### Chapter 1: Purpose, Principles, And How To Use This Book

- Needs the same drama reduction as the rest of the manuscript.
- Review personal manifesto voice against the current warmer, grounded style.
- The opening may mention how the book came into being. Review against `Project-Specific Cleanup`.
- Preserve the long-life skeleton and replaceable-service-generation idea.
- Preserve the explanation of how reader layers work, but keep it brief and non-repetitive.

### Chapter 2: Oregon Code And Compliance Map

- Mostly functions as an orientation/reference map.
- Review any "standard for the rest of the book" or "later chapters" wording against `Chapter Endings` and `Chapter References`.
- Preserve rule-stack tables, code-lane tables, approval-path distinctions, and project-binder logic.

### Chapter 3: Land, Site, And Feasibility

- Audit found several personifying or dramatic lines around land, property, roads, water, and trucks.
- Keep the feasibility filter, severity table, utility checks, septic and water checks, title checks, and purchase-decision review.
- Tone down theatrical phrasing while keeping the practical energy.

### Chapter 4: Legal, Permits, Owner-Builder Rules, And Inspections

- Review brand, LLC, and old-acronym language carefully.
- This chapter has important legal distinctions. Preserve the resale-timing correction, trade-scope map, legal risk triage, permit rhythm, inspection gates, CO/TCO distinction, and forms policy.
- Avoid softening legal limits into vague advice.

### Chapter 5: Soil, Ground Prep, Drainage, And Foundation Risk

- This is the heaviest tone lift.
- Audit noted strong personification and risk-heavy language around soil, water, pride, lies, and walk-away decisions.
- Preserve the soil kit, field workflow, screening matrix, DCP limits, pocket penetrometer limits, Atterberg/PI thresholds, drainage hierarchy, soil-improvement options, and Code citation lists.
- Keep the chapter practical. Do not remove risk; pair risk with action.

### Chapter 6: Structural System And Concrete Design

- Audit noted reader-facing revision history: old source material, old drafts, old source, source history, and current manuscript framing.
- The ending reads partly as book-system meta. It should stop where the technical information stops.
- Review old-acronym hits and project-default wording.
- Preserve structural concepts, engineered-design posture, wall assembly classification, source-derived alternatives, floor/roof options, service-layer classification issues, and structural hold points.

### Chapter 7: Foundation, Basement, Slabs, And Concrete Placement

- Audit noted reader-facing revision history around slab stack, insulation strategy, and source treatment.
- Review old-acronym hits and project-default wording.
- Preserve foundation-type decisions, inspection rhythm, slab stack, vapor/radon control, under-slab insulation, waterproofing/drainage sequence, concrete ordering, testing, curing, backfill, and record logic.
- Keep concrete placement detail. Do not move it into Chapter 8 during this retrofit.

### Chapter 8: Envelope, Waterproofing, Thermal Performance, And Radon

- Chapter 8 was expanded before the absolute no-personification rule landed, so it is explicitly in scope for this retrofit.
- Search for personification around the envelope, walls, water, vapor, air, insulation, foam, flashing, drainage, radon, code, tests, assemblies, and details.
- Preserve Oregon energy, blower-door, radon, vapor, drying, waterproofing, drainage, thermal-bridge, slab-edge, roof/parapet, inspection, and record guidance.
- Keep the chapter readable through concrete details and good sequencing. Do not make the envelope, water, vapor, air, code, or materials sound emotional, friendly, hostile, interested, demanding, or alive.

## Do Not Lose

Preserve these through the retrofit:

- technical content
- code citations and source lists
- decision frameworks
- severity tables
- risk triage tables
- soil and site screening matrices
- utility, septic, water, access, title, and zoning checks
- owner-builder legal distinctions
- inspection timing
- CO/TCO distinction
- forms policy
- record and binder guidance
- DCP limitations
- pocket penetrometer limitations
- Atterberg and PI guidance
- drainage hierarchy
- foundation and slab stack logic
- vapor retarder and radon readiness guidance
- envelope, waterproofing, thermal performance, blower-door, radon, vapor, drying, and IAQ coordination guidance
- structural engineered-design posture
- wall, floor, roof, service-layer, and hold-point concepts
- concrete ordering, testing, placement, curing, and backfill guidance

Retire old-style punch lines when they conflict with the new guide, but do not retire the information they carried.

Compress language only when it removes duplicate expression. Do not reduce knowledge.

## Final Verification

After retrofit, run at least these checks:

```bash
rg -n "\bOLD_ACRONYM_TOKEN\b|old source|old drafts|source history|source material|current manuscript|prior draft|earlier draft|this revision" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
rg -n "—|–|delve|tapestry|realm|landscape|it is important to note|ultimately|not just .*, but|crucial|pivotal|robust|seamless|leverage|foster|elevate|navigate|transformative" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
rg -n "previous chapter|next chapter|[Ss]ee Chapter|later chapters|Chapter [0-9]+" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
rg -n "____|\\[blank\\]|fill in|form below|template|Name:|Date:|Signature:" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
rg -n "\b(book|manuscript|chapter|house|property|site|land|soil|materials?|systems?|code|weather|water|concrete|tools?|drawings?|records?|envelope|walls?|vapor|air|insulation|foam|flashing|assemblies|details?)\b.{0,100}\b(tells?|telling|asks?|demands?|wants?|needs?|argues?|argued|agrees?|fights?|welcomes?|invites?|cares?|interested|has to work with)\b" manuscript/g1_ch_0{1,2,3,4,5,6,7,8}_*.md
```

Replace `OLD_ACRONYM_TOKEN` with the actual old acronym when executing.

Review all hits manually. External code and standard chapter references can remain.
