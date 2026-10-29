# theBook bugs

Bugs noticed while working on the project, one entry each: date, where, evidence, likely cause.
Logged, not fixed. Fixes wait for Jon.

## 2026-10-27, design review agent (read-only)

- **The planned PDF path truncates long documents without an error.** Where: the build plan in
  `revision8/BOOK_STRUCTURE.md` ("Build pipeline") runs
  `C:\Users\jon\Projects\claude-workspace\tools\html2pdf.ps1 -PagedJs`, which prints after
  `--headless --virtual-time-budget=30000`. Evidence: on this PC's Chrome 156.0.8078.48, those
  flags printed Revision 8 chapter 3 (about 24,000 words) as a 3-page PDF in about one second,
  exit code 0, no message. A 600,000 ms budget gave the same 3 pages. The same HTML, printed by a
  script that waits for Paged.js's `after` hook, gave all 71 pages. Test files:
  `C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\63015815-f80a-4571-ad08-ea62bcad95da\scratchpad\design-thebook\ch03-html2pdf-flags.pdf`
  (3 pages) and `...\design-thebook\ch03-driver.pdf` (71 pages). Likely cause: the virtual time
  budget no longer holds the print until Paged.js's asynchronous pagination ends. The July 2026
  audit in `claude-workspace\tools\BOOK-DESIGN.md` used small test documents that finish at once.
- **Build tools the plan counts on are not installed.** Where: `revision8/BOOK_STRUCTURE.md` says
  only Pandoc must be reinstalled, while `claude-workspace\tools\BOOK-DESIGN.md` (2026-07-16) lists
  Typst 0.15, Ghostscript 10.07.1 (via Scoop) and pyphen as installed. Evidence (2026-10-27):
  PowerShell `Get-Command` finds no `pandoc`, `typst`, `gs` or `gswin64c`, `import pyphen` fails
  under the current Python 3.14, and there is no Scoop apps folder. Likely cause: the tools were
  removed, and Python was upgraded, after July.
- **The top-level README names the frozen revision as active.** Where: `README.md` lines 5 to 9
  ("revision7 - the active revision", "Only revision7 is edited"). Evidence: `CLAUDE.md` and
  `revision8/AI_TODO.md` make Revision 8 the active revision since 2026-10-26, and
  `revision7/NOTE-superseded-by-revision8-2026-10-26.md` says so. Likely cause: README not updated
  when Revision 8 started. (Also item 11 in `external-input-bug-find.md`.)
- **The fault count in two index files is out of date.** Where: `revision8/README.md` line 10 and
  `CLAUDE.md` line 18 say `FAULT_CATALOG.md` holds 35 faults. Evidence: `FAULT_CATALOG.md` now has
  Tier 5, items 36 to 46 (added 2026-10-26 per `revision8/AI_TODO.md`). Likely cause: Tier 5 was
  added after those lines were written.

## 2026-10-27, about 10:00 PM: fixed by the main session (Jon: "anything you need to fix, go ahead")

theBook went under git first (commit "Snapshot of theBook as of 2026-10-27, 9:30 PM"), so every
fix below is a separate, reversible commit.

- **Fixed from this file:** the top-level README now names revision8 as active and drops the
  missing `test\` folder; both fault counts read 46.
- **Recorded, still open:** the PDF truncation and the missing build tools are now stated in
  `revision8/BOOK_STRUCTURE.md` ("Build pipeline"). They are fixed when the build is set up.
- **Fixed from `external-input-bug-find.md`:** items 1 to 22, and Unsure items 1 and 2. Item 2:
  the renumber script is removed (git history keeps it), and its chapter list moved to
  `revision8/tools/chapters.py`. Item 3: chapter 10 reads "ASTM E1745 §7.1" again (the clause
  number is Revision 7's and still needs checking against the standard), and its three ranges read
  "§10.6-10.8" and "§10.5-10.6". Item 22: chapter numbers in body prose still fail; the rest of the
  file gets a review list that skips chapters of codes, standards and session laws, because those
  were most of the hits.
- **Still open from that file:** Unsure item 3 (the front matter's fenced author block, for the
  front-matter rewrite); items 23 to 29 (the `images\` scripts and logs, not part of Revision 8
  work); chapter 35's Code Source line "see the chapter 20 sources", left for that chapter's
  writer.
