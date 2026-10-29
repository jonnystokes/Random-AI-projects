> **Note for any AI reading this:** do not use the material in this file unless Jon, the user,
> explicitly tells you to. It is not an assignment: finding it while doing other work is not
> permission to fix, check or act on anything in it. (Added at Jon's request, 2026-10-27.)

# External input: bug find, theBook

**Written:** 2026-10-27, about 8:40 AM, by a bug-hunt agent (Claude Opus 5.5) reading the project cold.
**For:** whoever works on theBook next.
**Status:** nothing was changed; this file is the one thing written. Bugs marked "reproduced" were run; the rest were found by reading the code.
**Covered:** revision8's tooling read in full (`tools/lint.py`, `tools/stats.py`, `tools/renumber_from_r7.py`), the control docs it enforces (CHAPTER_TEMPLATE.md, STYLE_GUIDE.md sections 4 to 17, REVIEW_CHECKLIST.md, WRITER_BRIEF.md v3, BOOK_STRUCTURE.md), both exemplars, the top-level README.md and CLAUDE.md. Lint and stats were run on a snapshot of all 36 chapters taken at 7:50 AM (copied to the scratch folder, because writers are editing the live files), plus crafted test chapters. Manuscript-wide scans for numeric section references, chapter-number references, figure markers, numbering, BOMs and characters outside cp1252. **Second pass (about 6:30 PM, bugs 23 to 29):** the `images\` scripts `edge.py`, `sort_by_edge.py` and `analyze.py` read in full and run on copies of five sample images in a scratch folder (they are the project's only image code, and QA only: nothing makes, converts, places or captions images); all 238 image files surveyed read-only (format, size, colour mode, full decode, SHA-256, edge scores); the four prompt queues, three generation logs, `main/book-image-log.md`, the v4 missing-image audit and the v2 ideas list checked against the folders and each other; every image name with a section number mapped to the Revision 5 and Revision 8 headings; the workflow doc's shell recipes run read-only; every revision searched for image links (there are none: Revision 8 has 17 `[FIGURE: id, ...]` markers, each unique and on its own line). **Not covered:** a revision8 build (none exists yet; the shelf builder `cool-tools\books\make_books.py` still reads revision7 and was only read); research files; prose quality (out of scope); manuscript faults inside the nine chapters being rewritten now (4, 5, 11, 17, 22, 24, 25, 27, 30), which appear below only as evidence for tool bugs; whether the AI images in `images\` draw their subjects correctly (a job for Jon or the engineer, not an agent).

Line numbers in chapter files are from the 7:50 AM snapshot. The test scripts are in the bug-hunt scratch folder (`...\scratchpad\bug-hunt\thebook\tests\`), if anyone wants to rerun them.

## Summary

| # | Severity | Where | Bug |
|---|---|---|---|
| 1 | high | tools/lint.py:609-616 | Lint crashes (UnicodeEncodeError) when its output is redirected, piped or run from the Bash tool; chapter 10 crashes on default options |
| 2 | high | tools/renumber_from_r7.py:87-100 | Running the "one-time" script again silently replaces the whole Revision 8 manuscript with Revision 7 text; no git, no backups |
| 3 | medium | manuscript ch 10:458, 825, 886, 1564 | The renumber script rewrote a standard's clause ("ASTM E1745 §7.1" is now "§10.1") and half-converted three section ranges |
| 4 | medium | tools/lint.py:417-423 | Chapter-title case check ignores everything before a subtitle colon ("Designing For Centuries" passes) |
| 5 | medium | REVIEW_CHECKLIST.md:10, tools/stats.py:10-11 | The checklist runs stats.py on one file; stats.py only reads folders, so it prints empty tables and exits 0 |
| 6 | medium | tools/stats.py:61-65 | stats.py files every sentence under a `###` subheading as "freeform": a third of chapter 3's Professional prose is missing from its Professional band |
| 7 | medium | tools/lint.py:80-81 | `words()` counts "$4,000", "0.5" and "R403.1.6" as several words: false FAILs on Code value lines in 11 chapters |
| 8 | medium | tools/lint.py:304 | The Applied target is per step (25 words); lint measures sentences, so chapter 4 passes with 9 steps over 25 words |
| 9 | medium | tools/lint.py:71, 338-353 | The echo gate cannot see "12-inch", "2%" or "12 in.", so the exemplar's own echo passes |
| 10 | medium | exemplars, STYLE_GUIDE.md:147 | The exemplars break the rules they teach: echo on the sample page, semicolons and "what follows" in the "After" models, "This book" in a model Simple block |
| 11 | medium | README.md:5-9 | The top-level README says revision7 is the active revision and "Only revision7 is edited"; revision7 is the frozen baseline |
| 12 | low | tools/lint.py:117-172 | Prose after a Code block (a subheading under it, as the template shows) is filed under Code, so the Professional gates skip it |
| 13 | low | tools/lint.py:268-282 | Bold run-in runs are counted across subheadings, layer labels, Code blocks and sections |
| 14 | low | tools/lint.py:28 | The sentence splitter cuts at "No.", "v.", "U.S." and does not cut before "$", "**", curly quotes or "§" |
| 15 | low | tools/lint.py:53 | The "text-as-agent fossils" FAIL gate fires on physical sentences ("a block holds its shape", "the next layer covers the work") |
| 16 | low | tools/lint.py:65 | The pointer-Source gate accepts only lowercase "section": "Clean Air Act Section 608" and "UL 858, Section 47A" fail |
| 17 | low | tools/lint.py:472-477 | "One comparison per Simple block" is counted per section, so two blocks with one comparison each FAIL |
| 18 | low | tools/stats.py:112-116 | stats.py's "written chapters" totals include the nine skeletons; the book's top sentence opener is "_to research" |
| 19 | low | tools/stats.py:2, 10 | stats.py's usage line names a file that does not exist; with no argument it crashes |
| 20 | low | tools/lint.py:28, 110-115 | A Jon's note of two paragraphs is read as one long sentence across the paragraph break |
| 21 | low | tools/lint.py:87 | A file saved with a UTF-8 BOM fails the numbering gate ("no '# Chapter N:' heading") |
| 22 | low | tools/lint.py:221-222, 467 | Chapter-number references are only checked in body prose; tables, Code blocks, Open items and the note are never checked |
| 23 | medium | images/edge.py:85, images/sort_by_edge.py:54 | The edge QA scripts crash when their output is not a UTF-8 console (Bash tool, redirect, pipe); sort_by_edge.py then sorts nothing |
| 24 | medium | images/ file names, images/version_4/prompts/image-prompts.jsonl | Image names and the v4 queue use Revision 5 numbering: 41 of the 49 numbered v4 images no longer match their Revision 8 section, and the resume pointer names the wrong section |
| 25 | medium | CLAUDE.md:52, revision8/BOOK_STRUCTURE.md:139-141 | The docs call the v4 queue mood, cover and family-page art; 99 of its 100 rows are technical section plates, the kind the book bans from AI |
| 26 | medium | images/IMAGE_GENERATION_WORKFLOW.md:47, 82 | The workflow's prompt fetch needs jq and its output search needs Codex, neither on this PC; the search exits 0 with nothing found |
| 27 | low | images/sort_by_edge.py:65-67 | Re-running the bucket sort keeps old copies: a replaced image shows up in two buckets |
| 28 | low | images/analyze.py:42-44 | analyze.py never writes the output file it is given; its gamma-1 "unchanged" copy is one unit darker in places |
| 29 | low | images/version_3/generation-log.md:8, 24; images/version_2/image-generation-ideas.md:3 | The v3 log still calls its finished queue current, the ideas file names a folder that does not exist, and two main/ images are unlogged |

## Bugs

### 1. Lint crashes when its output is not a UTF-8 console
- **Severity:** high
- **Status:** reproduced (Bash tool, and PowerShell with the output redirected to a file and piped to Select-String, on the snapshot)
- **Where:** `revision8/tools/lint.py:609-616` (the print calls; nothing sets the output encoding)
- **What goes wrong:** lint prints chapter lines in its DETAILS. When stdout is not a console (the Bash tool, `> lint.txt`, `| Select-String`), Python on this PC encodes output as cp1252, and a chapter line holding a character outside cp1252 kills the run with a traceback. The gate table prints, the DETAILS stop partway, the verdict line ("FAIL: N failing gate(s)") never prints, and with several files on one command line the files after the crash are never linted. Chapter 10 crashes on default options (its details hold "≥"); chapters 6 and 23 crash with `--all`; chapter 5 (being rewritten now) holds "≥", "≈", "φ", "→" and "−" too. A passing chapter with a WARN detail containing such a character would also exit 1, which reads as a failure. Writers run the lint as part of every chapter (WRITER_BRIEF.md item 7), and agents on this PC often run commands through the Bash tool, whose output is not a console.
- **Evidence:** from `revision8`: `python tools/lint.py manuscript/g1_ch_10_foundation-basement-slabs-and-concrete-placement.md > out.txt` gives exit 1, 71 lines, and `UnicodeEncodeError: 'charmap' codec can't encode character '\u2265' in position 67` at line 616 of lint.py (`C:\Users\jon\Projects\theBook\revision8\tools\lint.py` in the project), `print(f"    {d}")`. Same result in PowerShell without the harness's PYTHONIOENCODING, both redirected and piped. In a plain console window there is no crash (Python writes to the console in Unicode).
- **Fix direction:** `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` at the top of `__main__` (same for stats.py).

### 2. Re-running renumber_from_r7.py wipes the Revision 8 manuscript
- **Severity:** high (needs someone to run it, but nothing stops them and nothing can undo it)
- **Status:** reproduced on a throwaway copy in the scratch folder, never on the project
- **Where:** `revision8/tools/renumber_from_r7.py:87-100` (`main()` writes every chapter and the three other files unconditionally); usage line in its docstring, line 4
- **What goes wrong:** the script's docstring still gives "Usage (from anywhere): python revision8/tools/renumber_from_r7.py", and it prints a handy report (bare-reference counts per chapter), so someone wanting that report may run it. It overwrites all 36 chapter files with the converted Revision 7 text: no check that the destination already holds rewritten chapters, no prompt, exit 0. theBook is not a git repository and the project rule is no backups, so the finished chapters 2 to 4 and every in-flight writer's work would be lost.
- **Evidence:** copy of the snapshot, then `python <copy>/revision8/tools/renumber_from_r7.py`: exit 0; chapters 2, 3, 4 went from 65,846 / 154,012 / 121,535 bytes to 34,798 / 130,661 / 105,883 bytes, and chapter 2 opens "This chapter identifies the source of every rule..." (the Revision 7 text) again. `git -C theBook rev-parse` gives "not a git repository".
- **Fix direction:** refuse to write when a destination file exists unless `--force`, or retire the script now that it has run.

### 3. The renumber script corrupted a standard's clause number in chapter 10
- **Severity:** medium
- **Status:** reproduced (Revision 7 text against the Revision 8 file; the live file still has it at 8:37 AM)
- **Where:** `revision8/manuscript/g1_ch_10_foundation-basement-slabs-and-concrete-placement.md:458`, also lines 825, 886, 1564; cause in `revision8/tools/renumber_from_r7.py:78`
- **What goes wrong:** `convert()` rewrites every `§OLD.k` in a chapter to the new chapter number, whether it is a book section or a clause of an outside standard. In old chapter 7 (now 10), "permeance ≤ 0.03 perms after conditioning per ASTM E1745 §7.1" became "per ASTM E1745 §10.1". It now reads as a valid standard citation, so a writer fixing "stale section references" is unlikely to notice it, and the book's rule is never to invent a citation. The same regex half-converted three ranges: "§7.6-7.8" became "§10.6-7.8" (lines 825 and 886) and "§7.5-7.6" became "§10.5-7.6" (line 1564). AI_TODO.md says bare old numbers were left in chapters 10, 12 and 21 for the writers; the second half of each range is one of those, but the first half was converted, so each range now runs from a new number to an old one. The E1745 clause is not covered by that note.
- **Evidence:** `revision7/manuscript/g1_ch_07_foundation-basement-slabs-and-concrete-placement.md:458` has "ASTM E1745 §7.1"; Revision 8 line 458 has "ASTM E1745 §10.1". An audit of every `§OLD.k` the script rewrote (all renumbered chapters) found this the only standard clause it changed; the others were book-section references.
- **Fix direction:** restore "§7.1" (after checking the clause against E1745), and write the two ends of each range in the new numbering or by topic.

### 4. Chapter-title check skips everything before a subtitle colon
- **Severity:** medium
- **Status:** reproduced (lint on the snapshot, and on a crafted heading)
- **Where:** `revision8/tools/lint.py:417-423` (gate "headings in machine title case")
- **What goes wrong:** for a chapter heading, `text` is already the title without "Chapter N:" (CHAPTER_RE group 2, line 136). The code splits it again at the first colon and checks only what follows, so a main title before a subtitle colon is never checked. Chapter 8's heading "Designing For Centuries: Durability Engineering" gets no finding at all. Chapter 26's "Developing The Site: Shop, Block-Yard, And Outbuildings" is flagged only for "And", so once a writer fixes "And" the lint passes with "Developing The Site" still in the heading. BOOK_STRUCTURE.md has "Designing for Centuries" and "Developing the Site", and the build is to generate the table of contents and running heads from these headings.
- **Evidence:** lint on chapter 8 lists heading findings from line 5 on, none for line 1. A crafted chapter titled "Designing For Centuries: Durability Engineering" passes the gate; the same title without the subtitle ("Designing For Centuries") fails with "chapter title capitalizes 'For'".
- **Fix direction:** check the whole title, allowing a capital only on the first word after a colon.

### 5. The checklist's stats command gives an empty report
- **Severity:** medium
- **Status:** reproduced
- **Where:** `revision8/REVIEW_CHECKLIST.md:10`; `revision8/tools/stats.py:10-11`
- **What goes wrong:** the checklist says to run `python tools/stats.py manuscript/<file>` and compare the bands with the Revision 7 baseline. stats.py treats its argument as a folder and globs `g1_ch*.md` inside it, so a file path yields no files: it prints the headings, empty tables and "TOTAL WORDS (prose sentences, written chapters): 0", and exits 0. The reviewer gets no numbers and no error.
- **Evidence:** `python tools/stats.py manuscript/g1_ch_03_land-site-and-feasibility.md` prints empty tables, exit 0. `python tools/stats.py manuscript` works.
- **Fix direction:** accept a file or a folder (or change the checklist line to the folder and say how to pick out one chapter).

### 6. stats.py moves subheaded text out of its layer
- **Severity:** medium
- **Status:** reproduced (chapter 3 and 4, lint's parser against stats.py on a folder holding only that chapter)
- **Where:** `revision8/tools/stats.py:61-65`
- **What goes wrong:** stats.py resets the layer to "freeform" at every line starting with "#", including `###` subheadings inside a section. The template puts subheadings inside layers (chapter 3 has 14, and none is followed by a new layer label). lint.py keeps the layer across subheadings, so the two tools disagree, and the per-layer bands the checklist asks the reviewer to compare are wrong for any subheaded chapter.
- **Evidence:** chapter 3: lint's parser finds 489 Professional sentences; stats.py reports Professional n=333 and moves the other 156 (32 percent) to freeform. Chapter 4: 287 against 274.
- **Fix direction:** reset the layer only at `#` and `##` headings, as lint.py does.

### 7. Lint's word count splits numbers, failing lines that are within the limit
- **Severity:** medium
- **Status:** reproduced (crafted value line; measured on every chapter)
- **Where:** `revision8/tools/lint.py:80-81` (`words()`), used by every length gate
- **What goes wrong:** the regex `\b[\w'$%-]+\b` stops at commas, periods, slashes and parentheses, so "$4,000" and "0.5" count as two words, "R403.1.3.5" as four, "A/B/C" as three. The Code value-line gate ("over 35 words") then fails lines that are well under 35 words, and the sentence-length gates run high in exactly the sentences that carry numbers, which in this book is most of Applied and Professional.
- **Evidence:** a crafted value line of 34 words ("Footings 12 inches wide ... per R403.1.3.5.") is reported as 43 words, FAIL. On the real chapters, 17 Code value lines in 11 chapters are reported over 35 but have 35 words or fewer by spaces, for example 25.9 (lint 36, actual 27), 32.4 (38 against 29), 8.3 (42 against 31), 14.8 (40 against 32), 36.4 (40 against 31). Two are in chapter 3 (3.5: 37 against 35; 3.10: 45 against 35), so the loop log's "24 of 80 Code value lines over 35 words" for chapter 3 counts at least two that are not.
- **Fix direction:** count whitespace-separated tokens, or let the token regex take digits joined by `,` `.` `/`.

### 8. The Applied step limit is not checked
- **Severity:** medium
- **Status:** reproduced (measured on chapters 2 to 4)
- **Where:** `revision8/tools/lint.py:304` (`band("Applied", 15, 25)` measures sentences); the target is in STYLE_GUIDE.md section 12 ("Applied steps: average, longest: 15 or less; 25 or less") and CHAPTER_TEMPLATE.md ("Under 25 words per step"; word budget "Applied step: under 25 words")
- **What goes wrong:** the guide says the lint reports these targets per chapter, but the gate measures Applied sentences, not steps. A step of two or three sentences passes however long it is.
- **Evidence:** chapter 4 passes every gate with 9 Applied steps over 25 words (up to 33, for example line 764: 33 words, longest sentence 25); chapter 3 has 6 (up to 32 words, line 919), chapter 2 has 4 (up to 37 words, line 303).
- **Fix direction:** measure each Applied list item as a whole, beside the sentence band.

### 9. The echo gate cannot see the usual ways of writing a value
- **Severity:** medium
- **Status:** reproduced (crafted sections, and the exemplar)
- **Where:** `revision8/tools/lint.py:71` (`UNIT_NUMBER`), used at 338-353
- **What goes wrong:** the gate looks for the same number-plus-unit in Professional and Code. "12-inch" (the normal form before a noun) never matches because the regex allows only spaces between the number and the unit. The "%" and "in." alternatives can never match at all: the trailing `\b` after a non-word character needs a word character next, and a space or period follows in real text. So "a 2% slope" in Professional beside "2%" in Code passes, while the same text with "2 percent" fails, as it should.
- **Evidence:** crafted: Professional "2% per run" and Code "2%" PASS; "2 percent" in both FAIL (correct); "12 in." in both PASS. `UNIT_NUMBER.finditer("The 12-inch end distance")` finds nothing. The anchor-bolt exemplar, whose Professional restates the Code block's 12-inch end distance and 3 by 3 by 0.229-inch washer, passes both echo gates. Code blocks with "%" or "in." values exist in chapters 5, 10 and 23.
- **Fix direction:** allow a hyphen between number and unit, drop the trailing `\b` for "%" and "in.", and normalize "percent"/"%" and "inches"/"inch"/"in." before comparing.

### 10. The exemplars break the rules they teach
- **Severity:** medium
- **Status:** read, and checked with lint's own patterns
- **Where:** `revision8/exemplars/anchor-bolts-sample-page.md:34-36, 43, 50-51`; `revision8/exemplars/before-and-after.md:24, 117, 121`; `revision8/STYLE_GUIDE.md:135, 147`
- **What goes wrong:** writers read these first and are told to model on them. The sample page, "the model a writer holds while writing any section", restates two Code values in Professional ("The 12-inch end distance", "(3 by 3 by 0.229 inch)" against the Code line's "one bolt within 12 inches of each plate end, 3x3x0.229-inch plate washers") and then says Professional explains the values "without repeating them". The "After" chapter opening in before-and-after.md has a semicolon and "what follows" (line 24), both banned, both lint FAILs; the "After (Professional)" model has two semicolons (lines 117 and 121). STYLE_GUIDE.md's model "After" Simple blocks say "This book is for one house" (line 135) and "This book takes the engineered way" (line 147, a chapter 6 Simple block), which the self-description gate fails.
- **Evidence:** lint's SELF_DESCRIPTION regex matches "This book" and "what follows"; the semicolon gate counts any ";" outside fences and tables. The echo in the sample page is visible by reading, and passes the lint only because of bug 9.
- **Fix direction:** repair the models; they are copied.

### 11. The top-level README sends readers to the frozen revision
- **Severity:** medium
- **Status:** read and checked against the folders
- **Where:** `theBook/README.md:5-9`; also `theBook/CLAUDE.md:61`
- **What goes wrong:** README.md, the project's index, says "`revision7\` - the active revision (`AI_TODO.md` is the recovery anchor)" and "Only revision7 is edited". Revision 8 has been the active revision since 2026-10-26, and revision7 is the frozen baseline every rewrite starts from (it carries `NOTE-superseded-by-revision8-2026-10-26.md`). The R8-0 batch log says CLAUDE.md was repointed; README.md was not. A person or agent following README.md would edit the baseline. Both files also describe a root `test\` folder (121 MB, "edge-QA bucket output") that does not exist.
- **Evidence:** `ls theBook` shows no `test` folder; README.md line 9 reads "Only revision7 is edited."
- **Fix direction:** point README.md at revision8 and drop the `test\` lines.

### 12. Prose after a Code block is filed under Code
- **Severity:** low
- **Status:** reproduced (crafted section; measured on all chapters)
- **Where:** `revision8/tools/lint.py:117-172` (the layer changes only at a layer label or a numbered section; a fence and a `###` subheading leave it as is)
- **What goes wrong:** text after a Code block, before the next label, is treated as Code-layer prose, so the 'you' in Professional gate, the Professional and Applied bands, the Professional short-opener list and the echo gates skip it. CHAPTER_TEMPLATE.md's skeleton shows exactly this layout: a `###` subheading after the Code block and figure.
- **Evidence:** crafted: "When you find water in the trench, you pump it out..." under a subheading after a Code block passes 'you' in Professional; the same text after a **Professional** label fails. Real: 49 paragraphs in chapter 7 and 17 in chapter 9 (Revision 7 text, not yet rewritten) are read as Code-layer prose; chapters 2 to 4 have none.
- **Fix direction:** end the Code layer at the closing fence, or at a subheading.

### 13. Bold run-in runs are counted across headings and labels
- **Severity:** low
- **Status:** reproduced (crafted sections)
- **Where:** `revision8/tools/lint.py:268-282`
- **What goes wrong:** headings, layer labels, tables and Code blocks produce no paragraph, so they never reset the run counter. STYLE_GUIDE.md section 10 item 6 says to fix a run with "a subheading or a table", but two bold paragraphs under one subheading and one under the next still count as a run of three and FAIL. The same happens across a **Professional** label, a Code block or a section boundary.
- **Evidence:** crafted "### Wells / **Yield.** / **Depth.** / ### Septic / **Soil.**" FAILs ("run starting at line 17"); two bold Applied paragraphs then a bold Professional paragraph FAIL. Real: chapter 7's run at line 350 is two bold paragraphs on either side of a Code block.
- **Fix direction:** reset the run at any heading, label, fence or table.

### 14. The sentence splitter cuts and joins in the wrong places
- **Severity:** low
- **Status:** reproduced (crafted Simple block; real review lists)
- **Where:** `revision8/tools/lint.py:28` (`SENT_SPLIT`)
- **What goes wrong:** a sentence is cut after any period followed by a capital or digit, so "No. 26-01", "Reeves v. Yamhill County" and "U.S. Forest" become two sentences; and a sentence is never cut before one that starts with "$", "**", a curly quote, "§" or "_", so two sentences merge. Every sentence gate inherits this.
- **Evidence:** chapter 2's review list shows "Statewide Alternate Method No." (lines 311 and 313) as a Professional paragraph opening on a 4-word sentence; 16 case citations in chapters 2 to 4 are cut at "v.". Crafted: "...for a house. $500 of that money pays for the plan review..." is read as one 28-word Simple sentence and FAILs the 25-word maximum; starting the second sentence with a word instead passes. Chapter 13 line 480 has a sentence starting with "§13.4's" that merges with the one before.
- **Fix direction:** protect the abbreviations already listed in `ABBR` (line 66), and add `$ * § _` and curly quotes to the split lookahead.

### 15. The text-as-agent gate fails physical sentences
- **Severity:** low
- **Status:** reproduced (lint `--all` on the snapshot)
- **Where:** `revision8/tools/lint.py:53` (`FOSSILS`), FAIL gate at 465
- **What goes wrong:** the pattern treats "block", "layer", "table", "section" and "entry" as document elements, but in this book they are mostly things: a concrete block, a drainage layer, a water table. Physical sentences fail a FAIL gate meant for "the chapter says".
- **Evidence:** chapter 12 line 297, "A pressed lime-pozzolan block holds its green shape" ('block hold'); chapter 14 line 512, "before the next layer covers the work" ('layer cover').
- **Fix direction:** require a document word before it ("this block", "the table below"), or make the gate a WARN.

### 16. The pointer-Source gate is case-sensitive about "section"
- **Severity:** low
- **Status:** reproduced (all Code entries on the snapshot)
- **Where:** `revision8/tools/lint.py:65` (`SECTION_LEVEL` has `\bsection \d+`, lowercase, no `re.I`)
- **What goes wrong:** a Source line that names a section with a capital S and no dotted number is called a pointer to a whole body of law, a FAIL.
- **Evidence:** "Source: Clean Air Act Section 608 technician certification (EPA)." (chapter 23) and "Source: UL 858, Section 47A." (chapter 24) are flagged.
- **Fix direction:** `[Ss]ection \d+`.

### 17. One comparison per Simple block is counted per section
- **Severity:** low
- **Status:** reproduced (crafted section)
- **Where:** `revision8/tools/lint.py:472-477`
- **What goes wrong:** the rule is "one physical comparison per block" (STYLE_GUIDE.md section 4), but the gate adds up comparison sentences per section. A section with two Simple blocks (under two subheadings) and one comparison in each FAILs. Chapter 4 already has sections with two Simple blocks (21 Simple labels in 17 sections).
- **Evidence:** crafted section 9.1 with "### Mass / **Simple** / ...like a warm stone..." and "### Glass / **Simple** / ...like a one-way door..." gives "Simple blocks with 2+ comparisons: 9.1: 2", FAIL.
- **Fix direction:** count per block, using `simple_blocks`.

### 18. stats.py counts the skeletons in its "written chapters" totals
- **Severity:** low
- **Status:** reproduced
- **Where:** `revision8/tools/stats.py:112-116` (book totals are updated for every file; only the per-file print at line 121 skips skeletons)
- **What goes wrong:** the book-wide sections are labeled "written chapters" but include the nine skeleton chapters' instructions.
- **Evidence:** `python tools/stats.py manuscript`: the most common sentence opener in the whole book is "_to research" (94), exactly the 94 "_To research and write._" lines in the skeletons; TOTAL WORDS is 208,271 against 205,994 for the 27 printed rows.
- **Fix direction:** skip skeleton files before adding to the book totals.

### 19. stats.py's usage line is wrong, and it crashes without an argument
- **Severity:** low
- **Status:** reproduced
- **Where:** `revision8/tools/stats.py:2, 10`
- **What goes wrong:** the docstring says `python -I prose_stats.py <manuscript folder>`; there is no prose_stats.py ("can't open file"). Run with no argument, it dies with `IndexError: list index out of range` instead of printing the usage.
- **Fix direction:** correct the name; check `sys.argv` like lint.py does.

### 20. A two-paragraph Jon's note reads as one long sentence
- **Severity:** low
- **Status:** reproduced (crafted note); no chapter has a multi-paragraph note today
- **Where:** `revision8/tools/lint.py:28` and the paragraph joining at 110-115
- **What goes wrong:** a blockquote's lines, including the bare ">" line between paragraphs, are joined into one paragraph, and the splitter does not cut before ">". The last sentence of the first paragraph and the first of the second become one sentence.
- **Evidence:** crafted note "...without a furnace running all day. / > / > I chose concrete because..." is reported as a 30+ word sentence ("sentences of 30+ words (%)" 20.0, FAIL in the crafted chapter).
- **Fix direction:** flush the paragraph at a bare ">" line.

### 21. A UTF-8 BOM breaks the numbering gate
- **Severity:** low
- **Status:** reproduced (crafted file); no manuscript file has a BOM today
- **Where:** `revision8/tools/lint.py:87` (`read_text(encoding="utf-8")` keeps the BOM, so `^# Chapter` does not match line 1)
- **What goes wrong:** a chapter saved with a BOM (Windows PowerShell 5.1's `Set-Content -Encoding UTF8`, some editors) fails with "no '# Chapter N:' heading" and "sections with the wrong chapter number" for every section.
- **Fix direction:** read with `encoding="utf-8-sig"` (stats.py too).

### 22. Chapter-number references are checked only in body prose
- **Severity:** low
- **Status:** reproduced (scan of every file)
- **Where:** `revision8/tools/lint.py:221-222, 467` (the gate scans `body_text_lines`, which leave out tables, Code fences, closing sections and the note)
- **What goes wrong:** the rule "Reference other chapters by topic name, never by number" covers the whole manuscript, but a number in a Who-decides table, an Open item, a Code entry or Jon's note is never flagged. One stale case exists now: chapter 35 line 249, a Code Source line, "see the chapter 20 sources in the research record"; in Revision 8 numbering, chapter 20 is the electrical service chapter, and the research answers are now filed by Revision 8 chapter number. (That line will also fail the pointer gate when chapter 35 is rewritten.) All other hits outside body prose are code-book or session-law chapters, which are fine.
- **Fix direction:** run the chapter-number pattern over tables and closing sections too.

## Unsure

- The pointer-Source gate (lint.py:526-529) fails 104 Source lines that name a whole standard by designation ("ASTM D2487", "ASTM D2488; ASTM D2487") and chapter 2's "Statewide Alternate Method No. 26-01". The gate's name says "a chapter, division or ordinance", which these are not; STYLE_GUIDE.md section 7 asks for "the book and the section". Someone should decide which rule the gate enforces.
- CHAPTER_TEMPLATE.md's own figure example wraps over two lines, while the rule says the marker sits "on its own line"; a line-based marker replacer in the future build would miss a wrapped marker. The two markers in the manuscript today (chapter 3) are single lines.
- `manuscript/g0_fm_00_cover-and-intro.md` puts the author line and the AI acknowledgment inside a ```markdown fence, so any Markdown build shows them as a monospace code block with literal `**` and `---`. The front matter is to be rewritten in phase D, so this may not matter.

## Second pass: the images scripts

**Written:** 2026-10-27, about 6:30 PM, by a second bug-hunt agent (Claude Opus 5.5), read-only like the first. Scripts were run only on copies in its scratch folder, `C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\84bb1221-dfa4-4698-a697-071346fcbacf\scratchpad\bug-hunt\thebook-2\`, which also holds the check scripts (`image_survey.py`, `queue_check.py`, `audit_check.py`, `section_map.py`) and their output.

**What the image code is.** Three QA scripts in `images\`, written on the old Linux machine in May 2026. `edge.py` measures how far the outermost ring of pixels is from the page colour #F9F5EC; `sort_by_edge.py` copies every image of a folder into a bucket folder named after its worst edge pixel; `analyze.py` writes exaggerated-difference copies of one image. Nothing in the project makes, converts, places or captions images: they were made by Codex's built-in image tool from the JSONL prompt queues, and no manuscript in any revision links one (Revision 8 has `[FIGURE: id, ...]` markers only, by design). The image files themselves are sound: all 238 are real PNGs that decode fully (RGB, no alpha), the v4 queue's rows 1 to 63 each have their file under the queue's name, and the 47 bucket copies in `version_2/qa_edge_buckets/` match their originals and sit in the right buckets.

### 23. The edge QA scripts crash when their output is not a UTF-8 console
- **Severity:** medium
- **Status:** reproduced (Bash tool, and PowerShell with the harness's PYTHONIOENCODING removed, on copies)
- **Where:** `images/edge.py:85` (also 96 and 98); `images/sort_by_edge.py:54` (also 70 and 75)
- **What goes wrong:** both scripts print box-drawing lines ("─"), bars ("█") and an arrow ("→"), none of which exists in cp1252, the encoding Python uses on this PC when its output goes to a pipe or a file. From the Bash tool, or with `>` or `|`, `edge.py` prints the size and "Max dist" lines and then dies with a traceback (exit 1, no table), and `sort_by_edge.py` dies before its loop: nothing is sorted and no bucket folder is made. The resume instructions for the paused v4 pass say to run `python edge.py` on every generated PNG (`images/version_4/generation-log.md:20`), and agents on this PC often run commands through the Bash tool. A console window and the PowerShell tool (which sets PYTHONIOENCODING) are fine. Same cause as bug 1. Two side effects: `edge.py` writes 24-bit colour codes whether or not its output is a terminal, so captured output is full of `ESC[48;2;249;245;236m`; and `sort_by_edge.py` prints each image's line inside its `try`, after the copy, so under an encoding that has "─" but not "→" (cp437) every image is reported as "SKIP ... can't encode character" although each was copied and is counted in "Done. N images sorted".
- **Evidence:** from a scratch copy of `images\`, Bash tool: `python edge.py version_4/ch05_s55_field-testing-each-test-proves-v4.png` prints "Max dist: 58.40", the table header, then `UnicodeEncodeError: 'charmap' codec can't encode characters in position 2-91: character maps to <undefined>` at line 85, exit 1; with `PYTHONIOENCODING=utf-8`, exit 0 and all 14 lines. `python sort_by_edge.py version_4` fails the same way at line 54, exit 1, and `version_4/qa_edge_buckets` is never created; with UTF-8 it sorts 3 images into 2 buckets. PowerShell: `python edge.py ... > out.txt` exit 1; `python sort_by_edge.py version_3 | Select-String Done` exit 1. With `PYTHONIOENCODING=cp437`: "SKIP stone-and-wire-cover-concept.png: 'charmap' codec can't encode character ..." and then "Done. 1 images sorted into 1 buckets", with the copy in `d_420_to_430/`.
- **Fix direction:** `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` at the top of each script, as for bug 1; print the per-image line outside the `try`.

### 24. Image names and the v4 queue use Revision 5 chapter and section numbers
- **Severity:** medium
- **Status:** checked by script (`section_map.py`: the section number in each name, and each v4 queue row's `scope`, looked up in the Revision 5 headings and then in the Revision 8 chapter that now holds that material)
- **Where:** the file names in `images/version_2/`, `version_3/` and `version_4/`; `images/version_4/prompts/image-prompts.jsonl` (fields `chapter`, `scope`, `filename`); `images/version_4/generation-log.md:11-13`
- **What goes wrong:** every image is named `chNN_sNNN_...` after the May 2026 (Revision 5) numbering. The name, and for v4 the queue row's `scope` behind it, are the only link between an image and its place in the book, and both carry the old numbers. Revision 8 renumbered the chapters (old 7 and 8 are now 10 and 14) and added and moved sections, and nothing in the project maps the images' old numbers to the new ones. Anyone placing images by name puts most of them in the wrong section, and the resume pointer for the paused v4 pass names the wrong section.
- **Evidence:**
  - Of the 63 v4 images already made, 49 carry a section number. 8 still match number and title in Revision 8. 16 now sit at another number: `ch06_s610_roof-structure-v4.png` (Roof Structure is now 6.12; 6.10 is "Formwork, Placement Defects, And Cast-In Embeds"), `ch06_s66_reinforced-masonry-walls-v4.png` (now 6.7; 6.6 is "Alternative Concrete Systems And Mixes"), `ch03_s39_purchase-decision-review-v4.png` (now 3.21; 3.9 is "Utilities and solar access"). 25 have no heading of that title left in the chapter. The other 14 carry no section number at all, 13 of them with the slug doubled (`ch04_brand-llc-separation-pattern_brand-llc-separation-pattern-v4.png`).
  - The log's next item, "Chapter 6, section 6.17, The Structural Standard" (`ch06_s617_structural-standard-v4.png`), is section 6.23 now; 6.17 is "Seismic Performance: The Field Evidence".
  - The 45 files named `ch07_` or `ch08_` (32 and 10 in version_2, 3 in version_3), and 36 of the 37 queue rows still to make, now belong under chapters 10 and 14, and some under other chapters entirely. The 18 `ch07_s713_*` images include block making and laying (`block-press-cavity`, `cmu-drying-rows`, `first-course-string`, `mortar-joint-tool`), which Revision 8 covers in chapter 12 (12.6 Presses And Compaction At Owner Scale) and chapter 13 (13.6 Laying The Inner Wythe), while 10.13 is "Below-Grade Special Spaces: Root Cellar And Cistern".
  - Of the 83 version_2 and version_3 names with a section number, 23 still match; 43 moved, and 17 no longer have a heading of that title.
- **Fix direction:** keep a map from each image to its Revision 8 section (or name images by figure id, as BOOK_STRUCTURE.md does for the drawings), and correct the log's resume pointer.

### 25. The docs call the v4 queue mood and cover art; it holds technical section plates
- **Severity:** medium
- **Status:** read, and the 100 prompts counted by asset type
- **Where:** `CLAUDE.md:52`; `revision8/BOOK_STRUCTURE.md:139-141`; `images/version_4/generation-log.md:17`
- **What goes wrong:** both docs say the 100-prompt queue is "for mood, cover and family-page art only, if Jon wants it", right after BOOK_STRUCTURE.md rules out AI for technical figures because "it draws flashing the wrong way round and makes it look right". The queue is the opposite: one row is cover art and the other 99 are plates for numbered technical sections. An agent asked for mood art from the queue, following the log ("Resume at queue item 64"), would generate exactly the figures the book forbids. The 62 section images already made from it are of the same kind.
- **Evidence:** the "Asset type" of the 100 prompts: 36 "scientific educational construction cutaway plate", 36 "clear educational infographic diagram with realistic construction objects", 10 "record-keeping and construction documentation field plate", 9 "architectural field-manual illustration", 8 "realistic construction field-tool educational plate", 1 "primary cover art for the book". Rows still to make include row 73, "7.9.2 Frost-Protected Shallow Foundation" ("FPSF geometry diagram with AFI-based wing insulation, heated/unheated separation, slope away"), and row 87, "8.2.2 Table N1101.1(1) Prescriptive Envelope Requirements" ("Envelope R/U-value callout house").
- **Fix direction:** say in both docs what the queue holds and that it is retired for technical content, or write a separate queue for mood, cover and family-page art.

### 26. The workflow's generation recipe does not run on this PC
- **Severity:** medium
- **Status:** reproduced (both shell recipes, read-only, from the Bash tool)
- **Where:** `images/IMAGE_GENERATION_WORKFLOW.md:47, 75, 82, 93, 95`; the usage lines `images/edge.py:102`, `images/sort_by_edge.py:36`, `images/analyze.py:52`
- **What goes wrong:** the workflow was written for Codex on the old Linux machine and not updated in the July move (only `main/book-image-log.md` was annotated then). Its prompt fetch pipes through `jq`, which is not installed here, so it prints nothing, and the sub-agent pattern requires that exact command (line 93). The image tool's output folder `${CODEX_HOME:-$HOME/.codex}/generated_images` does not exist (no `codex` command, no CODEX_HOME, no `C:\Users\jon\.codex`), and the `find ... | sort -n | tail -5` pipeline that should report the new PNG (line 95) exits 0 with nothing, which reads as "no new image" rather than an error. The scripts' usage lines say `python3`, which on this PC is the Microsoft Store alias (a 0-byte App Execution Alias, with no Store Python installed); not run, because it can open the Store. The `python` commands in CLAUDE.md do work (Python 3.14 with Pillow 13 and numpy 2.5).
- **Evidence:** `sed -n '64p' version_4/prompts/image-prompts.jsonl | jq -r '.prompt'` gives `/usr/bin/bash: line 1: jq: command not found`, no output, PIPESTATUS 0 127. `find "${CODEX_HOME:-$HOME/.codex}/generated_images" -type f -name '*.png' -newermt "@$START_TS" -printf '%T@ %p\n' | sort -n | tail -5` gives `find: '/c/Users/jon/.codex/generated_images': No such file or directory` and exit 0. PowerShell `Get-Command jq` and `Get-Command codex` find nothing.
- **Fix direction:** fetch the prompt with Python (`json.loads` on line N), and write down which image tool is used on this PC now and where it saves.

### 27. Re-running the bucket sort keeps old copies in their old buckets
- **Severity:** low
- **Status:** reproduced (copies of three v4 images in the scratch folder)
- **Where:** `images/sort_by_edge.py:65-67` (copies into the bucket; never clears or checks the output folder)
- **What goes wrong:** each run adds copies and removes none. The v4 flow gives a rejected image's replacement the same queue filename (`images/version_4/generation-log.md:22-23`, workflow line 58), so if the folder was sorted before the replacement, the rejected image stays in its high bucket beside the replacement in a low one, and the run's summary does not mention it. A reviewer opening the high bucket sees an image that is no longer in the folder. The workflow's example `python sort_by_edge.py version_2 version_2/qa_edge_buckets` (line 121) would also write a second tree, `qa_edge_buckets/d_*`, beside the existing `qa_edge_buckets/buckets_v2/d_*`.
- **Evidence:** first run: `d_010_to_020` (2 images) and `d_050_to_060` (`ch05_s55_field-testing-each-test-proves-v4.png`, 58.40). After overwriting that file with another image and sorting again: "Done. 3 images sorted into 1 buckets", but the folder holds 4 files in 2 buckets, `d_050_to_060/ch05_s55_...` (the old image, SHA-256 starting b2cc187f) and `d_010_to_020/ch05_s55_...` (the new one, 2dac37d6).
- **Fix direction:** empty the output folder at the start of a run, or write a report (name, score, bucket) instead of copies.

### 28. analyze.py never writes the file it is given, and its "unchanged" copy is changed
- **Severity:** low
- **Status:** reproduced (copy of `version_3/ch07_s715_vibrator-wall-cutaway-v3.png`)
- **Where:** `images/analyze.py:44` (output names), `images/analyze.py:42` (the cast to 8 bits truncates), `images/analyze.py:52` (usage)
- **What goes wrong:** the usage line and the workflow (lines 114 and 122) say `analyze.py IMAGE.png OUTPUT.png`, but the script writes `OUTPUT_g001.png` and `OUTPUT_g050.png` and never `OUTPUT.png`, so anything that opens the file it named finds nothing. Gamma 1 is meant to leave the image as it was, but the float maths gives values like 117.99998 for 118 and `astype(np.uint8)` cuts them down, so the `_g001` file is one unit darker in about 1 percent of its pixels.
- **Evidence:** `python analyze.py version_3/ch07_s715_vibrator-wall-cutaway-v3.png version_3/qa/ch07_s715_vibrator-wall-cutaway-v3-edge.png` prints "Saved ...-edge_g001.png" and "Saved ...-edge_g050.png"; `...-edge.png` does not exist. Against the input, `_g001` has 62,649 channel values one lower, in 21,163 of 1,572,864 pixels; pixel (581, 52) is (118, 111, 107) in the input, (117.99998, 110.99998, 106.99998) before the cast and (117, 110, 106) as saved.
- **Fix direction:** document the two suffixes (or write OUTPUT.png itself as the strong view), and round with `np.rint` before the cast.

### 29. Two image logs point at the wrong queue or folder, and a third misses two images
- **Severity:** low
- **Status:** read and checked against the folders
- **Where:** `images/version_3/generation-log.md:3, 8, 24`; `images/version_2/image-generation-ideas.md:3`; `images/main/book-image-log.md`
- **What goes wrong:** the version 3 log still calls its queue the "current default prompt queue" and says "For future generation, read one row from `version_3/prompts/image-prompts.jsonl`", while the workflow (line 40) and CLAUDE.md make the version 4 queue current and all 82 version 3 rows are already made (each has a v2 or v3 file); an agent that opens version_3 first could regenerate finished images. The v2 ideas file says "Version one archive: `images/version-one/`"; the folder is `images/version_1/`. `main/book-image-log.md` logs 21 of the 23 images in `main/`: `stone-and-wire-book-table-01.png` and `stone-and-wire-book-table-02.png` have no entry, so their theme and source are not recorded.
- **Fix direction:** one line each.

### Unsure (second pass)

- `edge.py`'s colour codes in a classic console window (conhost rather than Windows Terminal): Python does not switch on colour-code handling itself, so they may print as raw text there. Not tested, because it needs a window.
