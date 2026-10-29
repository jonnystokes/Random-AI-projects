> **AI AGENTS: DO NOT USE THIS FILE UNLESS JON TELLS YOU TO.**
> No AI may act on, build from, plan from or otherwise use the material in this file unless Jon (the
> user) has explicitly told it to. Coming across this file during other work is not permission. If you
> were not told to work from this file, leave it alone and carry on with your own task.

# External input: design improvements for Stone and Wire

**Date:** 2026-10-27. **For:** Jon. **Written by:** a Claude sub-agent (Opus 5.5), read-only on the
project apart from this file and `BUGS.md`.

**What I looked at.** `CLAUDE.md`, the top-level `README.md`, and in `revision8/`: `AI_TODO.md`,
`README.md`, `STYLE_GUIDE.md`, `CHAPTER_TEMPLATE.md`, `BOOK_STRUCTURE.md`, `REVIEW_CHECKLIST.md`,
`WRITER_BRIEF.md` (the figure rules), `FAULT_CATALOG.md` and `GLOSSARY_POLICY.md` (skimmed), both
exemplars, `tools/lint.py` (its parser). From the manuscript: the cover file, chapter 1, chapter 2 in
full, the opening of chapter 3, the inspection section of chapter 10, and the safety passages of
chapters 12 and 13. Also the July render tests in `revision7/rendered/`, the code library's
`README.md`, Jon's memory notes on the project and on his taste, the shelf builder
(`cool-tools/books/make_books.py` and its README), the reader's Markdown handling
(`Walker of Worlds/src/chapter.js`), and the pipeline notes `claude-workspace/tools/BOOK-DESIGN.md`
and `html2pdf.ps1`. I measured the manuscript with two small scripts, ran test builds of chapter 3
and of the whole current text through headless Chrome and Paged.js, and drew two mock-ups (paths at
the end). Outside sources are linked under each idea.

**What the project is, and what design covers here.** Stone and Wire (project name Better Smarter
Homes) is a field manual for one owner-built concrete and masonry house in Oregon. It is written for
five readers at once through four labeled layers (Simple, Applied, Professional, Code) and is meant
to come out as four editions from one Markdown source: PDFs through Pandoc, headless Chrome and
Paged.js, plus a copy on the cool-tools book shelf, where the reader app reads it aloud. Revision 8 is
mid-rewrite: chapters 2 to 4 are finished, nine more are being written, ten are still skeletons, and
the text runs to about 270,000 words. The prose rules are already worked out in depth (style guide,
fault catalog, lint), so this file leaves the prose alone. Here, design means what the reader sees
and uses (figures, safety notices, checklists, page layout, editions, registers) and how the book is
produced and kept (the build, its checks, its formats).

## The ideas at a glance

| # | Idea | Size | When |
|---|---|---|---|
| 1 | Figure markers in the chapters now, and drawing rules built on the control-layer "pen test" | small now, large later | now, and phase G |
| 2 | Make the PDF build wait for Paged.js and fail loudly when it does not finish | small | before phase G |
| 3 | Safety warnings in one fixed form, placed before the step | small | now (mass wave) |
| 4 | A one-page card for every hold point before concrete | medium | Inspection chapter, then build |
| 5 | One parser for the lint and the build, with the editions as a filter on it | medium | phase G |
| 6 | The Simple edition on the shelf as its own book, and the build's HTML published | small | after the Simple test |
| 7 | Page layout: a label column, a shorter line, layers that survive black-and-white printing | small | phase G |
| 8 | Fixed party names in "Answered by" and "Who decides", so the build prints a question list per meeting | small | now |
| 9 | A permanent number and a history for every recorded decision | small to medium | phase F |
| 10 | Draft and release builds, so unconfirmed [JON] lines are never published as Jon's words | small | phase G, and when the shelf switches to Revision 8 |
| 11 | Every Code Source line a link to the official text | small | phase G |
| 12 | Test the Simple path on its real readers | small | before the Simple edition |
| 13 | Keep the record in formats that outlast the software | small | phase G |

---

## 1. Get figure markers into the chapters now, and set the drawing rules

**What to change.**

- *Now, while the mass wave runs.* The manuscript holds 2 figure markers in about 270,000 words,
  both in Land, Site, and Feasibility, and none in the finished Code and Legal chapters.
  `WRITER_BRIEF.md` says a marker "is the most you place" but never says where one belongs, so the
  writers place none. One line in the brief's figure rule would fix it: place a marker wherever the
  text gives two or more dimensions that relate to each other, a junction between two assemblies, a
  layout (parcel, room, panel, trench), or an order of assembly in space. If the loop should not
  change the brief for this, the same four tests can drive a marking pass in phase E that writes
  `research/figures.md` (id, chapter, section, what it shows, the values it must carry).
- *For the drawings (phase G),* add five rules to the Figures section of `BOOK_STRUCTURE.md`:
  1. Every envelope section (wall, foundation, slab edge, roof-wall junction, window opening) draws
     the four control layers as continuous lines in four fixed colors: rain, air, vapor, thermal.
     The drawing then is the pen test: where a line cannot be followed through a junction without
     lifting the pen, the detail has a gap, and the gap becomes an Open item for the engineer.
  2. Labels sit on the drawing beside the part, with a leader line, never as numbered keys below it.
  3. Cut materials use the standard drafting hatches (concrete stipple with small triangles, masonry
     45-degree lines, insulation, earth, gravel), with a one-page legend in the front matter for the
     family readers.
  4. Every dimension on a drawing is one the chapter states in Applied or Code. Nothing is drawn to
     look right.
  5. Each edition prints its own caption. `BOOK_STRUCTURE.md` plans four captions per figure.
     Stacked under one drawing in the Full edition, they would repeat each other, so the Full edition
     could print the Simple caption and let the labels carry the rest.
- The figure generator can stay small: one Python script per figure family reads a spec (layers,
  thicknesses, labels) and writes SVG with no library. The scratch demo `pen-test-demo.png`
  (made by `gen_section.py`, 80 lines) shows rule 1 on a generic enclosure, with the air line
  deliberately broken at the roof edge.

**Where it comes from.**

- Richard Mayer's principles of multimedia learning: people learn more from words with pictures
  than from words alone, and more when each label sits next to the part it names (his "spatial
  contiguity" principle). [Cambridge Handbook of Multimedia Learning chapter](https://resolve-he.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E),
  [one-page summary of Mayer 2020](https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf).
- Joseph Lstiburek, [BSI-001 "The Perfect Wall"](https://www.buildingscience.com/documents/insights/bsi-001-the-perfect-wall)
  (Building Science Corporation, 2010): four control layers, ranked rain, air, vapor, thermal.
- Lstiburek's design-review habit, from the
  [Perfect Wall, Roof and Slab podcast](https://greenbuildingadvisor.com/article/the-perfect-wall-roof-and-slab-building-science-podcast)
  (Green Building Advisor, 2009): his staff trace each control layer around the building section
  with a pen of its own color, and every place the pen must leave the paper is a flaw to fix.
- The common drafting hatches as CAD libraries name them (ANSI31 for masonry, AR-CONC for concrete):
  [a hatch-pattern reference](https://blog.draftsperson.net/material-hatch-patterns/). The US
  National CAD Standard is the formal home of these symbols. I could not fetch it.

**Why it fits.** A concrete house fails at its junctions and its dimensions, which are the things
words carry worst. The family readers get the most from pictures, and engineers and inspectors check
details on drawings, not in paragraphs. `BOOK_STRUCTURE.md` already chose scripted line drawings
over AI images because AI "draws flashing the wrong way round". The pen-test rule makes each section
drawing a check as well as an illustration.

**Size.** Small for the marker rule. Large for the drawings themselves (likely 40 to 80), which
phase G already plans.

**Cost or risk.** A wrong drawing is worse than none, so the planned review by Jon and the engineer
stays. Markers placed now cost a writer a few minutes per chapter. Markers placed later cost a
re-read of every chapter.

---

## 2. Make the PDF build wait for Paged.js, and fail loudly when it does not finish

**What I found (test runs on this PC, 2026-10-27).** The build plan uses
`claude-workspace/tools/html2pdf.ps1 -PagedJs`, which prints after Chrome's
`--virtual-time-budget=30000`. On today's Chrome (156) the budget does not hold the print until
Paged.js finishes. Chapter 3 came out as a 3-page PDF in about one second, exit code 0, no message.
A 600-second budget gave the same 3 pages. The same chapter, printed by a small script that waits
for Paged.js's own "finished" hook, came out whole: 71 pages, laid out in 2.1 seconds. The whole
current manuscript (36 chapters, front matter and appendices, about 270,000 words) laid out to 867
letter pages in 47 seconds and printed in 11 seconds, using the Paged.js 0.4.3 copy vendored in
claude-workspace. Paged.js is fast enough. The wait is what is broken. (Logged in `BUGS.md`.)

**What to change.**

- Drive Chrome through its DevTools protocol instead of the command-line print. The scratch
  `driver.mjs` (60 lines, Node 24, no packages) does it: open the page, wait for the Paged.js
  `after` hook, then call `Page.printToPDF` with `preferCSSPageSize`, `printBackground` and
  `generateDocumentOutline`. The last option produced PDF bookmarks for every section and
  subheading in the test, which `BOOK_STRUCTURE.md` lists among the things the build generates. The
  PDF came out tagged without asking.
- After printing, check the output and refuse to publish on any miss: the page count above a floor,
  and the last heading of the last file present in the `pdftotext` output. Say which check failed,
  in plain words.
- Keep Paged.js pinned at the vendored 0.4.3. Its last stable npm release is July 2023 (the newest
  beta is October 2024) while work continues on GitHub, and two open issues would hit this book: a
  0.5 beta made layout many times slower ([#247](https://github.com/pagedjs/pagedjs/issues/247)),
  and the current main branch hangs on pages with several `break-inside: avoid` tables
  ([#340](https://github.com/pagedjs/pagedjs/issues/340)). The book has 174 tables, and
  `BOOK-DESIGN.md`'s rules of thumb put `break-inside: avoid` on every one.
- Before phase G, reinstall what `BOOK-DESIGN.md` lists as installed but is gone (see `BUGS.md`):
  Pandoc, and pyphen for Python 3.14 if hyphenation is wanted. Typst or Ghostscript only if idea 13's
  PDF/A is wanted.

**Where it comes from.** The test runs above (files listed at the end). Release history from the
[npm registry entry for pagedjs](https://registry.npmjs.org/pagedjs) and the
[Paged.js repository](https://github.com/pagedjs/pagedjs). Alternatives checked the same way:
[Typst](https://typst.app/docs/reference/pdf/) (0.15.1, July 2026), a typesetter with its own markup
that Pandoc can write, and Vivliostyle ([CLI 11.4.0](https://registry.npmjs.org/@vivliostyle/cli),
October 2026), a maintained CSS paged-media engine. Neither is needed for speed.

**Why it fits.** Jon's rule is that a chosen setting that fails must fail and say why. The current
path fails silently, and would hand a 3-page "book" to the shelf or a printer with exit code 0.

**Size.** Small.

**Cost or risk.** Chrome's protocol options can change between versions. The post-print check
catches that.

---

## 3. Give safety warnings one fixed form, placed before the step

**What to change.** Add a fifth block type to `STYLE_GUIDE.md` and `CHAPTER_TEMPLATE.md`, allowed
only inside Applied. An example built from the Masonry Craft chapter's own text:

> **WARNING.** Wet cement is caustic (pH 12.9) and causes deep chemical burns after about 2 hours of
> contact, often without pain. Wear nitrile or butyl gloves, and wash any contact off with clean
> water at once.

- A signal word, then the hazard, the consequence and how to avoid it, in two sentences at most,
  with the chapter's own number where one exists.
- WARNING for serious injury or death (silica dust, trench collapse, falls, energized conductors,
  dropped loads, caustic burns). CAUTION for minor or moderate injury. Property damage gets no
  notice. It is ordinary Applied content.
- Placed directly before the step it governs. When a hazard covers a whole procedure (silica in
  every cutting step), one notice heads the procedure instead.
- The build gathers every notice into one list by build stage, at the front of Part III or in The
  Owner-Builder's Body and Mind, and prints notices in the Full and Site editions. The Simple
  edition keeps its own plain sentence about the risk.
- The lint checks each notice: signal word present, two sentences or fewer, followed by a numbered
  step or heading a procedure.

**Where it comes from.**

- ANSI Z535.6, the US standard for safety information in product manuals, sorts the safety
  messages in a manual into four kinds: directives about other messages, grouped messages, section
  messages and embedded messages placed in a procedure
  ([In Compliance Magazine, April 2024](https://incompliancemag.com/ansi-z535-6-manuals-in-focus/)).
  A message names the hazard, what happens if it is ignored, and how to avoid it, under a signal
  word: DANGER, WARNING, CAUTION, or NOTICE for property damage
  ([Clarion Safety's guide to Z535.6](https://clarionsafety.com/safety-resources/machinery/understanding-ansi-z535-6-a-guide-to-safety-information-in-product-manuals-and-materials)).
- ASD-STE100, Simplified Technical English (the aerospace maintenance-manual standard), starts a
  safety instruction with a command or a condition
  ([summary](https://en.wikipedia.org/wiki/Simplified_Technical_English),
  [ASD-STE100 FAQ](https://www.asd-ste100.org/STE_faq.html)).

**Why it fits.** Jon will do most of the work himself, the dangerous parts included: cutting block,
mixing, trenching, lifting. Chapters 12 and 13 state these hazards well, but in prose sections and
bold run-ins (Masonry Craft section 13.12, the hazards section of Owner-Made Blocks), away from the
steps where the hazard happens. The whole manuscript has one line that starts with a signal word.
Applied's "no why" rule would strip a warning's consequence. This block keeps it, in a fixed short
form. The style guide's ban on "warning cadence" targets performance, and a fixed-format notice is
the opposite of performance.

**Size.** Small as a rule, applied as chapters 10 to 13, 26, 27, 29 and 30 are rewritten anyway.

**Cost or risk.** Too many notices teach readers to skip them. Keep them to injury hazards and let
the lint count them per chapter.

---

## 4. A one-page card for every hold point before concrete

**What to change.** In the Inspection and Approval Sequence chapter, each gate that comes before
something that cannot be undone (footing pour, wall grout or pour, foundation backfill, under-slab
pour, rough-in cover, insulation cover, roof membrane cover) gets a short Applied list, "Before you
call for the inspection", of nine items at most. The nine are the items that cannot be fixed after
the pour, each with its record (the photograph with the inspection card in frame, the batch
ticket). The build prints each list as a half-letter card for the binder and the site. The long
lists stay in their chapters: the 19-item footing self-check in Foundation section 10.4 remains the
reference, and the card is the pause.

The cards are used "do, then confirm": the work follows the chapter, then at the pause point
(before calling the inspector, before ordering the truck) every line on the card is confirmed.

**Where it comes from.**

- Atul Gawande, *The Checklist Manifesto* (2009): a checklist works at a defined pause point, comes
  in two kinds (read-and-do, or do-then-confirm), and stays short. He reports Boeing's checklist
  designer keeping lists to five to nine items. Summary of the two kinds:
  [Sketchplanations](https://sketchplanations.com/read-do-do-confirm-checklists).
- In construction quality planning a hold point is an agreed point where work stops until a
  decision lets it go on (BSRIA's definition, via
  [Designing Buildings](https://www.designingbuildings.co.uk/wiki/Hold_point)).
- Chapter 10 already names the field sources for the content: Oregon BCD's "Cite It Write It"
  checklist and Marion County's footing and foundation checklist.

**Why it fits.** The book says it in its own Simple text: for a concrete house, an hour after the
pour nothing can be changed. The binder and the photographs are already planned (Code and Compliance
section 2.9). A card in a sheet protector is what gets used on a muddy site, and a 900-page PDF is not.

**Size.** Medium. Choosing the nine items per gate is judgment, done once in the Inspection chapter.

**Cost or risk.** Duplication, if a card were ever edited by hand. The card is generated from the
chapter's list and never edited on its own, in line with the rule that furniture is generated.

---

## 5. One parser for the lint and the build, with the editions as a filter on it

**What to change.** Build the phase G furniture generator on the `Chapter` class in
`tools/lint.py`, which already parses chapters, sections, layer labels, Code entries and the four
closing lists. For each edition it writes Pandoc Markdown in which:

- each layer is a fenced div (`::: {.layer .simple}`) made from its bold label, so the stylesheet can
  style it and an edition can drop it.
- each Code entry becomes three styled lines (requirement, value, Source). Left alone, Pandoc prints
  the fenced Code blocks as monospace code that does not wrap, and 779 of the 3,775 Code lines today
  run over 110 characters.
- each `[FIGURE: id, ...]` marker becomes a figure slot, or a visible placeholder while the drawing
  does not exist.
- each topic-name cross-reference ("the Masonry Craft chapter") becomes a link, and in print gets its
  page number from Paged.js's `target-counter` (verified in `BOOK-DESIGN.md`). The prose rule
  (topic names, never numbers) is untouched.

The chapter cards, the decision register, the open-items lists (idea 8), the figure index and
Appendix B come from the same parse. Pandoc then only converts. Writers change nothing: the bold
labels stay the source syntax.

**Where it comes from.** DITA, the OASIS standard for technical documentation, calls this
conditional processing, or profiling: one source, filtered at build time for each audience or
deliverable ([DITA 1.3 specification](https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/archSpec/base/condproc.html)).
Quarto does the same inside Pandoc Markdown with `.content-visible` divs
([Quarto docs](https://quarto.org/docs/authoring/conditional.html)). Pandoc's built-in Lua filters
can do it inside Pandoc with no extra installs, and a filter deletes an element by returning an empty
list ([Pandoc Lua filters](https://pandoc.org/lua-filters.html)). That is the alternative if the
generator should live in Pandoc rather than Python.

**Why it fits.** One parser means the lint's view of a chapter and the published book cannot drift
apart. It keeps the build small and in Python, where Jon's other tools are, and it is the mechanism
that `BOOK_STRUCTURE.md`'s "generated, never hand-written" furniture needs.

**Size.** Medium.

**Cost or risk.** Low. The parser gets a second user, so a lint change could break the build, and a
build run alongside the lint catches it.

---

## 6. Put the Simple edition on the shelf as its own book, and publish the build's HTML

**What to change.**

- In `cool-tools/books/make_books.py`, add an edition filter on the same parse and publish the Simple
  edition (Simple blocks, Jon's notes, chapter closes) as its own shelf book beside the full one,
  once the Simple test in `BOOK_STRUCTURE.md` passes. Site and Professional can follow. The reader
  needs no change, and its planned layer filter can come later, or never.
- Publish the build's HTML (the page before Paged.js) as a one-file web edition with four layer
  check boxes. The shelf reader turns Markdown into plain text so it can read aloud (`softenMd` in
  the reader's `chapter.js`), so drawings and table layout will only ever show in the HTML and PDF
  editions. The whole current text made a 2 MB HTML file in the test build.

**Where it comes from.** Diátaxis, a widely used documentation framework, holds that different needs
call for different documents, and that blurring the boundaries between them causes most
documentation problems ([Diátaxis in five minutes](https://www.diataxis.fr/start-here/)). DITA
profiling (idea 5) produces one deliverable per audience from one source.

**Why it fits.** Jon's wife reads in short sittings and his mother wants the plain story. A separate
Simple book on the shelf gives them a 5-to-7-hour book they can also listen to, with its own place
kept, instead of a 20-hour book behind a filter. It is small, and it needs no new machinery.

**Size.** Small.

**Cost or risk.** Two (later four) shelf entries, each with its own reading place. The shelf still
calls the book "Better Smarter Homes" while the cover file says Stone and Wire, pending Jon's
confirmation of the title.

---

## 7. Page layout: a label column, a shorter line, and layers that survive black-and-white printing

**What to change** in the "Typography and layer visibility" section of `BOOK_STRUCTURE.md`. The
scratch mock-up `sample-layout.png` sets the anchor-bolt sample page this way.

- **Line length** of 65 to 80 characters. The July test render
  (`revision7/rendered/chapter-02__chromium__p1.png`) runs about 110 characters per line at 11 point
  on letter paper with 0.85-inch margins. On letter, a 1.25-inch label column at the left of a
  5.6-inch text column gives about 72 to 78 characters at 11 to 11.5 point.
- **Layer labels in the column,** level with the first line of their block, each with its own mark
  (open circle for Simple, open square for Applied, filled square for Professional, diamond for
  Code) as well as its color and rule, so the layers stay distinct in black-and-white printing and
  for a color-blind reader.
- **Simple** set ragged-right, half a point larger, with its first sentence in bold. The style guide
  already promises that "a reader who reads only the first sentence of every Simple block gets the
  chapter's argument", and bold makes that path visible.
- **Applied** steps with a check box in the Site edition.
- **Code** in a ruled box in the text face: requirement bold, value regular, "Source" in small caps
  and the citation as a link (idea 11).
- **Running head:** the chapter title on one side and the current section number and title on the
  other (Paged.js `string-set`), instead of the Part. Appendix B, the decision register and the index
  cite sections, so the pages should show them.
- **Simple edition settings:** line spacing at least 1.5, no justification, no more than 80
  characters per line.

**Where it comes from.**

- Butterick's Practical Typography: 45 to 90 characters per line, line spacing 120 to 145 percent of
  the point size, 10 to 12 point for print
  ([line length](https://practicaltypography.com/line-length.html),
  [key rules](https://practicaltypography.com/summary-of-key-rules.html)).
- WCAG 2.2, success criterion 1.4.8: lines no wider than 80 characters, text not justified, line
  spacing at least one and a half within paragraphs
  ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html)).
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/): margin notes keep related material beside
  the text instead of sending the eye to the bottom of the page.
- Robert Horn's Information Mapping: a short, informative label on every block of information, so a
  reader can scan for the block he needs
  ([Horn's 2001 talk](https://faculty.washington.edu/farkas/TC510-Fall2011/Horn-DocsWithFuture.pdf),
  [structured writing](https://en.wikipedia.org/wiki/Structured_writing)).
- Christopher Alexander's *A Pattern Language* (1977) sets each pattern's problem and its solution in
  bold, so the essentials read on their own.

**Why it fits.** Five readers scan the same page for different blocks. A label column turns finding
"my" layer into a glance down the margin. The family readers get the friendliest setting in the
Simple edition, and the Full edition stays dense.

**Size.** Small (stylesheet).

**Cost or risk.** The label column costs pages, perhaps 10 to 15 percent on letter. Bold first
sentences are a taste call. Try them on one chapter with the Simple readers (idea 12) first.

---

## 8. Fixed party names in "Answered by" and "Who decides", so the build prints a question list per meeting

**What to change.** In `CHAPTER_TEMPLATE.md` and the brief: the "Answered by:" field of an Open item
and the "Who decides" cell begin with one name from a fixed list kept in `BOOK_STRUCTURE.md`, then
free text. A first list, drawn from chapters 2 to 4: Building official, Plan reviewer, Engineer of
record, Geotechnical engineer, County planning, County sanitarian or DEQ, OWRD or watermaster, Title
company, Lender, Insurer, Utility, Testing lab, Supplier, Jon. Events too: Parcel chosen,
Pre-application meeting, First production week. The build then prints "Questions for the
pre-application meeting", "Questions for the engineer of record" and so on: every Open item and
pending decision for that party, by chapter, each with its "Assumed meanwhile" line. Jon walks in
with one list and walks out with answers to log.

**Where it comes from.** The request-for-information (RFI) log of construction administration (the
AIA G716 form is the usual template): every open question is numbered, addressed to one party and
tracked until answered. The web-search budget ran out before I could fetch a source for this.

**Why it fits.** Chapters 2 to 4 already hold 77 Open items and 59 Who-decides rows. Across 36
chapters that is likely 700 to 900 questions. A keyword tally could not place 34 of the 77
"Answered by" lines with any party, so free text will not sort reliably. A fixed first word costs
the writers nothing.

**Size.** Small.

**Cost or risk.** It changes the brief during the mass wave. Chapters written before it get the
field normalized in the phase E pass.

---

## 9. Give each recorded decision a permanent number and a history

**What to change.** The generator gives every line under "Decisions this chapter records" an ID the
first time it sees it (D04-07: chapter 4, seventh decision). It keeps the ID, the text, the status
and the date of each status change in a generated file beside the manuscript, so no date enters the
prose. The register prints superseded decisions too, struck through, pointing to the ID that
replaced them. IDs appear only in the register and the Who-decides tables, never in body prose, and
are never reused.

**Where it comes from.** Michael Nygard's
["Documenting Architecture Decisions"](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
(2011), the origin of architecture decision records: records are numbered in sequence, numbers are
never reused, each record carries a status (proposed, accepted, deprecated, superseded), and a
reversed decision stays in the record, marked superseded.

**Why it fits.** `BOOK_STRUCTURE.md` calls the book "the plan and the record for one house", and
chapter 1 says the record is what lets a contractor or a future owner follow the reasoning. Chapters
2 to 4 hold 56 decisions (28 decided, 16 Jon to confirm, 8 pending parcel, 4 pending engineer). Most
of the pending ones will change once there is a parcel and an engineer, and without IDs and dates the
register cannot show what changed, or when.

**Size.** Small to medium.

**Cost or risk.** Matching a reworded line to its old ID needs care. The generator flags a line it
cannot match instead of guessing.

---

## 10. Draft and release builds, so unconfirmed [JON] lines are never published as Jon's words

**What to change.** Two build modes. *Draft:* [JON] markers print highlighted, and a "Waiting on
Jon" page lists every marker with its chapter and sentence, which doubles as Jon's to-do list for the
notes. *Release* (the PDF editions and the shelf): a Jon's note that still carries a marker is left
out and listed in the build output, the way `make_books.py` already lists skeleton chapters it
leaves out. Or the build stops. Nothing is stripped silently.

**Where it comes from.** Publishing's author queries: the copyeditor's questions to the author are
all answered before pages go to press (*The Chicago Manual of Style*, chapter 2, on manuscript
editing). Named from knowledge, not fetched.

**Why it fits.** Chapters 2 to 4 already carry 16 markers, and every chapter will have some. The
shelf reader drops only the History Book's `hb-note` comments, so once the shelf switches to
Revision 8 it would read "JON: confirm" aloud to Jon's family. And a note with markers is a draft of
Jon's voice, not his text (CLAUDE.md).

**Size.** Small.

**Cost or risk.** None beyond a few lines in the build.

---

## 11. Make every Code Source line a link to the official text

**What to change.** The build links each Source line to the official text wherever a steady route
exists: ORS to the Legislature's chapter page (for example
[ORS chapter 455](https://www.oregonlegislature.gov/bills_laws/ors/ors455.html), checked today, 2025
edition), OAR to the Secretary of State's rule page, BCD and DEQ documents to their oregon.gov
addresses, the specialty codes to the free ICC viewer at chapter level. The routes are already
tested and listed in `revision6_code_library/README.md`. A link check in the build fails on a dead
link. Print is unchanged.

**Where it comes from.** The official publishers' own pages above, and the book's own rule (chapter
1) that the official sources remain the legal authority.

**Why it fits.** On site, with a phone and the PDF, the step from the book's restatement to the
governing text becomes one tap. It also serves the inspector reading the Professional edition.

**Size.** Small.

**Cost or risk.** Deep links into the ICC viewer change and need a browser, so link those at chapter
level only.

---

## 12. Test the Simple path on its real readers before building the Simple edition

**What to change.** `BOOK_STRUCTURE.md`'s Simple test is a reading of one chapter's Simple blocks in
order, done by the reviewer. Add one step: give that chapter's Simple path to Jon's mother and to his
wife, separately. Afterwards ask each to say what the system does and why Jon chose it, and note
where she stopped or read twice. Fifteen minutes each. Log the findings like a loop finding, against
the brief.

**Where it comes from.** Plain-language practice tests a document with its intended readers rather
than by formula: ISO 24495-1:2023 (plain language, governing principles) and the testing section of
the US Federal Plain Language Guidelines. Named from knowledge. The search budget ran out before I
could fetch either.

**Why it fits.** Judgment check 1 in the style guide ("Would a curious non-builder keep reading the
Simple blocks, and could she retell the point afterward?") is now answered by an AI reviewer
imagining those readers. Two real readers answer it directly, at no cost.

**Size.** Small.

**Cost or risk.** None.

---

## 13. Keep the record in formats that outlast the software

**What to change.** Each release writes, beside the editions:

- a dated archive zip with the Markdown source, the figure SVGs and a manifest of SHA-256 hashes.
- the Full edition as PDF/A where possible, otherwise as a tagged PDF with embedded fonts (the
  Chrome path gives tagged PDF by default, as tested, while PDF/A needs Typst or Ghostscript,
  neither of which is installed now).
- an edition line on the copyright page of every output (build date and a short source hash), so any
  printed copy can be matched to the source it came from.
- one printed Full edition on acid-free paper for the house binder.

**Where it comes from.** The Library of Congress
[Recommended Formats Statement for textual works](https://www.loc.gov/preservation/resources/rfs/text.html)
lists PDF/A (ISO 19005) and PDF/UA among its preferred formats and asks for embedded fonts. Typst
writes PDF/A and PDF/UA-1 natively ([Typst PDF docs](https://typst.app/docs/reference/pdf/)).

**Why it fits.** The house is built around a thousand-year structural shell, and its record should
not depend on a reader app or a build tool surviving. Code and Compliance section 2.9 already puts a
paper set in a fireproof box with digital copies in two places, and this decides what those copies are.

**Size.** Small.

**Cost or risk.** PDF/A means a second tool. Without it, a tagged PDF plus the source zip covers most
of the value.

---

## Checked and already right

- The four-layer split, filtered into editions, is what the DITA standard calls profiling: the
  industry's way of serving several audiences from one source.
- The Applied rules match Simplified Technical English's procedure rules (one instruction per
  sentence, the imperative). STE caps a procedural sentence at 20 words. The book's cap is 25, which
  could tighten if Jon wants.
- Scripted line drawings rather than AI images: the pen test in idea 1 only works on drawings with
  exact geometry.
- The Who-decides table and Records to keep give each hand-off and each record one home, which is
  what makes ideas 4, 8 and 9 cheap to generate.

## Sample output made for this file (scratch folder, not in the project)

- `C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\63015815-f80a-4571-ad08-ea62bcad95da\scratchpad\design-thebook\sample-layout.png`:
  idea 7's page layout on the anchor-bolt sample page (source `sample.html` in the same folder).
- `C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\63015815-f80a-4571-ad08-ea62bcad95da\scratchpad\design-thebook\pen-test-demo.png`:
  idea 1's control-layer rule on a generic enclosure (source `gen_section.py`).
- `C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\63015815-f80a-4571-ad08-ea62bcad95da\scratchpad\design-thebook\driver.mjs`:
  idea 2's wait-then-print driver. Its output for the whole current manuscript is `book-driver.pdf`
  (867 pages) in the same folder, beside the truncated `ch03-html2pdf-flags.pdf` (3 pages).
- `md2html.py` and `print.css` in the same folder: the throwaway converter and stylesheet used for the
  timing test, not a proposal for the real build. `survey.py` and `furniture.py` produced the counts
  quoted above.

## Limits of this review

- The web-search budget (shared by every agent this session) ran out partway, so the sources for
  ideas 8, 10 and 12, and the paper-permanence standards in idea 13, are named but were not fetched.
- I did not assess the reader app's planned layer filter (the reader belongs to another project), the
  AI art queue in `images/`, or the glossary design in `GLOSSARY_POLICY.md`.
- The counts come from regex scans of a manuscript that writers were editing during the review,
  so treat them as close, not exact.
