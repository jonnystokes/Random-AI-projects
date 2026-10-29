# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a book manuscript, not a software project. The book is "Stone and Wire" (project name: "Better Smarter Homes"): a technical owner-builder manual for building a long-life concrete home in Oregon, written for five readers at once through four labeled layers (Simple, Applied, Professional, Code). There is no build, lint, or test suite for software. The executable code is the manuscript tooling in `revision8/tools/` and the image QA scripts in `images/`.

The project maintains its own AI-instruction system inside the active revision folder. Those files are authoritative. This file only tells you where they are.

## Start Here

The active revision is **Revision 8** (created 2026-10-26: every chapter rewritten to the Revision 8 standard from the frozen Revision 7 text). On any fresh start, read these files in `revision8/` in this order, and nothing else until the task requires it:

1. `AI_TODO.md` — the recovery anchor: status, the chapter loop log, the batch log, the immediate next action
2. `README.md` — the folder map
3. `STYLE_GUIDE.md` — the book's own guide: readers, voice, the layer contract, bans, measured targets, judgment checks. **Required in full before writing or judging any manuscript text.** It governs the book; the general prose guide `C:\Users\jon\Projects\writing-style-guide-v2.md` governs the prose and is also required in full. In this repository a copy sits at `writing-style-guide-v2.md` next to this file; use it wherever a revision8 file gives the `C:\` path.
4. `FAULT_CATALOG.md` — the 54 named writing faults (22 inherited from Revision 6, 13 found in Revision 7, and 19 found in the Revision 8 chapter loop on 2026-10-26 and 2026-10-28). A violation of any item ranks with a wrong code citation.
5. `CHAPTER_TEMPLATE.md` — the anatomy every chapter has
6. `BOOK_STRUCTURE.md` — the 36 chapters in final order, front and back matter, figures, editions, what the build generates
7. `WRITER_BRIEF.md` and `REVIEW_CHECKLIST.md` — how a chapter is written and how it is judged

Before ending a meaningful batch of work, update `revision8/AI_TODO.md` with what changed, files touched, verification performed, and the next action. Historical batch records for earlier revisions live in `revision7/AI_TODO.md` and `revision5/CHANGELOG.md`.

## Revision Layout

Revisions are full snapshots; each was copied forward from the previous one. Only Revision 8 is edited.

- `revision8/manuscript/` — the active manuscript: 36 chapter files under **final** numbering (`g1_ch_NN_slug.md`; section numbers match chapter numbers), `g0_fm_*` front matter, `g2_app_*` appendices.
- `revision8/research/` — every piece of research the project has gathered, indexed in `research/INDEX.md`: the Wave 3 answers (per chapter, the authority for values), the question bank, the two older waves, the obligations ledger carried from Revision 7, and `new/` for findings made during Revision 8.
- `revision8/worklogs/` — one worklog per chapter writer.
- `revision8/tools/` — `lint.py` (the measured gates), `stats.py` (prose shape, a folder or one chapter), `chapters.py` (the final chapter order and each chapter's Revision 7 source; the lint reads it). The one-time renumber script that built the folder was removed on 2026-10-27; git history keeps it.
- `revision7/` — frozen. Its manuscript is the baseline every Revision 8 rewrite starts from and is never edited. Its control docs describe the Revision 7 process. Note: on 2026-10-26 another session replaced `revision7/writing_style_guide.md` with the US History book's guide; the Revision 6 copy (`revision6/writing_style_guide.md`) is the real ancestor of the Revision 8 style guide.
- `revision6_code_library/` — downloaded official Oregon code documents and the tested online routes for verifying citations. Read its `README.md` before verifying or adding any `Code` entry.
- `revision6/` and earlier — frozen source history, not read during Revision 8 work except the Revision 6 style guide for history and the revision 2 and 3 glossaries at closeout.

## Non-Negotiable Working Rules

- Do not silently reduce, compress, or skip manuscript material. Preserve and grow; anything dropped from the Revision 7 text is named in the chapter's Open items.
- Never invent citations, values, anecdotes, decisions or reasons. Unverifiable material becomes an Open item. `Code` entries use the three-part format: requirement, exact value, Source line.
- Reference other chapters by topic name, never by number.
- Research gaps live only in a chapter's Open items list; the body never narrates the research.
- "Jon's note" in each chapter is first person, drafted from the record, with `[JON]` markers on anything only Jon can confirm; a note without markers is Jon's text and no agent edits it.
- The project name is written out; the abbreviation "BSH" is banned from manuscript text.
- Run `python revision8/tools/lint.py <chapter>` on every finished chapter and fix every FAIL; then do the judgment checks in `STYLE_GUIDE.md` section 13. The lint is the floor, not the standard.
- Writers run in parallel when no two in flight share a file or a chapter boundary (`revision8/AI_TODO.md`, standing rule 1). The chapter loop corrects the brief, never the agent or its chapter.
- No backups or copies of files; revision7 is the frozen baseline. theBook is a git repository (since 2026-10-27, local only, `images/` ignored): commit after each batch of work, and restore a damaged file from git rather than from a copy.
- Do not edit `revision7/` or earlier revisions, except `revision5/CHANGELOG.md` (the project-wide historical log) when Jon asks.

## Image Generation Pipeline

`images/` holds AI-generated illustrations organized as `version_1/` through `version_4/`, with a 100-prompt queue in `version_4/prompts/image-prompts.jsonl`. Per `revision8/BOOK_STRUCTURE.md`, AI image generation is not used for technical figures (those are scripted line drawings reviewed by Jon and the engineer). The queue is not a source for the book: 99 of its 100 rows are technical section plates, written against Revision 5 numbering. Mood, cover or family-page art, if Jon wants any, would need a new queue. The procedure is in `images/IMAGE_GENERATION_WORKFLOW.md`; the QA scripts run from `images/`:

```bash
cd images
python edge.py version_3/SOME_IMAGE.png            # perimeter color check against #F9F5EC
python sort_by_edge.py version_3                    # bucket a folder by max edge distance
python analyze.py IMG.png OUT.png                   # visualize color-distance issues
```

Known faults in these scripts and the image logs are items 23 to 29 of `external-input-bug-find.md`; they are not fixed.
