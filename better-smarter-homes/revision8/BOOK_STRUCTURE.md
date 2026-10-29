# Book Structure (Revision 8)

Created 2026-10-26. The order, the numbering, the files, the front and back matter, the figure
program, the editions, and what the build generates. Numbers are final: section numbers match
chapter numbers, files are named by chapter number, and nothing is renumbered again.

## The book

**Title.** Stone and Wire. **Subtitle.** A field manual for a long-life concrete home. The
project name on this machine is "Better Smarter Homes"; the cover carries Stone and Wire.
[JON: confirm the title and subtitle, or change this line.]

**What it is.** The plan and the record for one house: a concrete and masonry home in Oregon,
owner-built, designed for a thousand-year structural shell with replaceable systems. Technical
reference, decision record, and the owner's reasons, in one text, for five readers through four
labeled layers (STYLE_GUIDE.md sections 1 and 3).

**What it is not.** Legal, tax, insurance or engineering advice; a substitute for the engineer
of record, the geotechnical report or the building department; a guarantee of any value.

## The 36 chapters

Files are `manuscript/g1_ch_NN_slug.md`. "R7 state" is what the Revision 7 text in the file is
when Revision 8 starts: **R7 voice** (finished under the Revision 7 cycle, full text), **R6
carryover** (Revision 6 text never given the Revision 7 pass, full text), **skeleton** (an
outline with instructions, under 500 words). "Items" is the number of answered research items
in research/answers for the chapter.

### Part I: Decide and Qualify

| # | Title | R7 state | Items |
|---|---|---|---|
| 1 | Purpose, Principles, and How to Use This Book | R7 voice | 0 |
| 2 | Oregon Code and Compliance Map | R7 voice | 12 |
| 3 | Land, Site, and Feasibility | R7 voice | 138 |
| 4 | Legal, Permits, and Owner-Builder Rules | R7 voice | 87 |
| 5 | Soil, Ground Prep, Drainage, and Foundation Risk | R7 voice | 15 |

### Part II: The House, System by System

| # | Title | R7 state | Items |
|---|---|---|---|
| 6 | Structural System and Concrete Design | R7 voice | 48 |
| 7 | What Concrete Uniquely Enables: Designing with Mass | R7 voice | 70 |
| 8 | Designing for Centuries: Durability Engineering | R7 voice | 48 |
| 9 | Passive and Bioclimatic Design | R7 voice | 66 |
| 10 | Foundation, Basement, Slabs, and Concrete Placement | R7 voice | 42 |
| 11 | The Wall System, Foundation to Roofline | R7 voice | 53 |
| 12 | Owner-Made Blocks and Alternative Concretes | R7 voice | 143 |
| 13 | Masonry Craft: Laying and Stacking Block and Brick | R7 voice | 73 |
| 14 | Envelope, Waterproofing, Thermal Performance, and Radon | R6 carryover | 20 |
| 15 | Roof System and Roof-Wall Junctions | skeleton | 78 |
| 16 | Aesthetics and Architectural Expression | skeleton | 106 |
| 17 | Plumbing: Water Supply, Pressure, Treatment, and Hot Water | R6 carryover | 43 |
| 18 | Water Independence | skeleton | 116 |
| 19 | Plumbing: DWV, Sewage, Venting, Slope, Distance, and Fixtures | R6 carryover | 18 |
| 20 | Electrical: Service, Panels, Grounding, and Load Planning | R6 carryover | 7 |
| 21 | Electrical: Branch Circuits, Wire Size, Voltage Drop, Lighting, Low Voltage, and Future Power | R6 carryover | 7 |
| 22 | Solar, Battery, and Energy Independence | skeleton | 38 |
| 23 | HVAC, Ventilation, Humidity, and Air Quality | R6 carryover | 20 |
| 24 | Smart Home, Network, Security, and Local Automation | R6 carryover | 13 |
| 25 | Interiors, Finishes, Accessibility, and Livability | R6 carryover | 107 |

### Part III: Build, Prove, and Own

| # | Title | R7 state | Items |
|---|---|---|---|
| 26 | Developing the Site: Shop, Block-Yard, and Outbuildings | skeleton | 73 |
| 27 | Tools, Equipment, and the Owner-Builder Shop | skeleton | 75 |
| 28 | Materials, Suppliers, Procurement, and Substitution | R6 carryover | 40 |
| 29 | Build Sequence and Site Coordination | R6 carryover | 88 |
| 30 | The Owner-Builder's Body and Mind | skeleton | 75 |
| 31 | Inspection and Approval Sequence | R6 carryover | 10 |
| 32 | Testing, Commissioning, and Quality Control | R6 carryover | 20 |
| 33 | Personal Project Finance: Budget, Financing, and Cash Flow | skeleton | 24 |
| 34 | Resilience and Disaster Independence | skeleton | 89 |
| 35 | Documentation, Maintenance, and Future Upgrades | R6 carryover | 95 |
| 36 | Business and Brand Framework | R6 carryover | 72 |

### Boundaries to draw explicitly

Where two or three chapters share a subject, each names the other by topic at the point of
overlap, and the writer of the later chapter reads the earlier one before writing.

- Water: Land (rights and feasibility) / Plumbing Supply (code plumbing) / Water Independence (harvesting, storage, treatment, greywater).
- Surface character: What Concrete Enables (form-given character) / Aesthetics (whole-house expression) / Interiors (interior surface finishing).
- Shop and production: Owner-Made Blocks (the units) / Developing the Site (the shop building and yard) / Tools (the equipment).
- Resilience threads: Structural (safe rooms, seismic), What Concrete Enables, Water Independence, Solar, HVAC (passive survivability) / Resilience (the capstone, deepening without duplicating).
- Roof: Structural (roof structure options) / Envelope (control layers) / Roof System (the assembly, drainage, junctions).
- Inspection: Legal (overview and pointer) / Inspection and Approval Sequence (the detail; it must integrate the block staged at the end of its file from the legal chapter).
- Build Sequence owes the cistern two-placement pour sequencing that Soil, What Concrete Enables and Foundation state as a dependency.
- Finance's resilience-cost roll-up resolves against Resilience.

Order for writing when boundaries matter: the earlier chapter first. The full list of
cross-chapter obligations inherited from Revision 7 is in research/OBLIGATIONS.md.

## Front matter (written after the chapters converge; Jon's pieces marked)

In order:

1. **Cover and title page.** Stone and Wire. A field manual for a long-life concrete home.
2. **Why this house.** 250 to 400 words in Jon's first person. [JON: this is yours; the writer drafts from the record and you replace it.]
3. **The house in one page.** The cutaway figure with twelve labels, each pointing to a chapter.
4. **How to read this book.** The five readers, the four layers, the five reading paths with honest times (the Simple path, the site path, the professional path, cover to cover, single-chapter lookup). The layer legend.
5. **The sample page.** Anchor bolts in four layers (exemplars/anchor-bolts-sample-page.md).
6. **What this book is not.** Six sentences.
7. **Contents.** Generated by the build.
8. **The AI acknowledgment and copyright page**, at the back of the front matter, in Jon's words. [JON: confirm the wording.]

Chapter 1 shrinks to what belongs to it: the long-life goal, the design principles, the working
rules, and the project overview. The reading-pattern material moves to "How to read this book".

## Back matter

1. **Appendix A: Standards and reference index.** Rebuilt from the finished chapters' Code entries and named standards: every standard family, who owns it, what it controls, which chapters cite it.
2. **Appendix B: Code lookup and compliance cross-reference.** Every Code entry in the book, by code book and section, with the chapter and section that uses it. Generated from the Code blocks, then checked by hand.
3. **Appendix C: Glossary.** Per GLOSSARY_POLICY.md (this folder): scan every chapter for acronyms and Level 1 to 4 terms, compare the revision 2 and 3 glossaries, define to the depth the policy sets, point code-relevant terms at Appendix B.
4. **Decision register.** Every "Decisions this chapter records" line, with its status and chapter. Generated.
5. **Figure index.** Generated.
6. **Index.** People, systems, materials, code sections, figures. Generated from a term list, then checked by hand.
7. **State of the project.** One or two pages: what is decided, what waits on a parcel, what waits on the engineer. [JON: yours.] A house book should end with the house; until there is a house, it ends with where the house stands.

## Figures

No figure exists yet, and none is produced during the chapter loop. Writers place
`[FIGURE: id, description]` markers. The figure program, in priority order:

1. `house-cutaway`: the house in one page. Section cutaway, twelve labels (foundation, slab, wall, insulation, roof, windows, water, power, HVAC, solar, battery, radon), each pointing to a chapter.
2. `wall-section-single-wythe`: footing to bond beam, the four control layers labeled.
3. `wall-section-cavity`: the double-wythe alternative, ties, flashing, weeps.
4. `foundation-section`: footing, stem wall, slab, waterproofing, drain, capillary break.
5. `roof-wall-junction`: parapet or eave, coping, flashing, membrane termination.
6. `plumbing-rough-in`: supply, drain, vent, slope, cleanouts in a mass wall.
7. `electrical-map`: service, panel, grounding electrode system, branch circuit zones.
8. Per-chapter candidates as the writers mark them.

**How they are made.** Scripted line drawings (SVG generated from a spec: dimensions, layers,
labels), deterministic and editable, reviewed by Jon and, for anything structural, the engineer
of record. AI image generation is not used for technical figures; it draws flashing the wrong
way round and makes it look right. The 100-prompt queue in `../images/version_4/prompts/` is
not a source for the book: 99 of its 100 rows are technical section plates, written against
Revision 5 numbering. Mood, cover or family-page art, if Jon wants any, needs a new queue. Each
technical figure gets four
captions, one per layer. Real site photographs are added when there is a site.

## Editions

One source, four outputs, built by filtering on the layer labels:

| Edition | Layers | Reader | Expected length |
|---|---|---|---|
| Full | All, plus the decision register | Jon, the record | about 20 hours |
| Simple | Simple blocks, Jon's notes, chapter closes, figures | Jon's family and friends; the ADHD path | 5 to 7 hours, in 15-minute chapters |
| Site | Simple openers, Applied, Code, Who-decides tables | A technician or contractor | about 7 hours |
| Professional | Simple openers, Professional, Code | An engineer or inspector | about 9 hours |

The Simple edition is tested on one chapter before it is promised: the Simple blocks of a
finished chapter are read in order, and if they do not carry the chapter's story on their own,
the writers' brief changes before the edition is built. The book shelf reader at
`C:\Users\jon\Projects\cool-tools\books` gets a layer filter (Simple, Applied, Professional,
Code, All) as the first edition mechanism; PDF editions follow from the same source.

## What the build generates

Never hand-written, always regenerated from the manuscript:

- **The chapter card** at the head of each chapter: scope line (from the opening), reading time at 200 words per minute, Simple-path time, related chapters (from topic-name cross-references), the number of decisions recorded.
- **The layer map** (as an appendix table and as the reader's filter), from the labels.
- **The table of contents** from the headings. **PDF bookmarks** for every chapter and section. **Running heads** with the chapter title.
- **The decision register** from the chapter closes. **The figure index** from the markers. **The index** from a term list.
- **Part openers**: Part title, the chapters in it, and a three-sentence statement of what the Part decides, written once in this file:
  - Part I decides whether the project can happen at all: which land, under which rules, on what ground.
  - Part II decides what the house is, system by system, from the structure that lasts a thousand years to the finishes that change with the people in it.
  - Part III decides how the house gets built, proved, paid for, kept, and made resilient, and what the owner does with what he learned.

## Typography and layer visibility (for the build)

Each layer has a visual identity: a tinted box for Simple, a margin bar in a second color for
Applied, a third for Professional, and Code set in a ruled box in the text face, never in a
monospace code font. Layer labels readable at arm's length. Body 11.5 to 12 point, line height
1.55, generous margins, headings in sentence case. A running head with the chapter title on one
side and the Part on the other.

## Numbering and files

- Chapter numbers and section numbers are final. A section is `N.k`. Subheadings carry no number.
- Files: `g0_fm_*` front matter, `g1_ch_NN_slug` chapters, `g2_app_*` appendices. The shelf builder and the PDF build read them in name order.
- Cross-references in prose use chapter topic names, never numbers.

## Build pipeline (Stage 6 of the finish plan)

Markdown to HTML to PDF through headless Chrome with Paged.js (recto chapter openings, running
heads, TOC page numbers), per `C:\Users\jon\Projects\claude-workspace\tools\BOOK-DESIGN.md`.
Two things come first, both found on 2026-10-27 (details in `../BUGS.md`). Pandoc, Typst,
Ghostscript and pyphen are all missing on this PC, not Pandoc alone (`winget install
JohnMacFarlane.Pandoc` for the first). And `html2pdf.ps1 -PagedJs` prints before Paged.js
finishes: a 24,000-word chapter came out as 3 pages with exit code 0. The PDF step waits for
Paged.js's `after` hook and fails loudly when pagination does not finish. The
shelf copy is rebuilt by `C:\Users\jon\Projects\cool-tools\books\make_books.py`, whose source
folder moves from revision7 to revision8 when the first Revision 8 chapters are ready to publish.
