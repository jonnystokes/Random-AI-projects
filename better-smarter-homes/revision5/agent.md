File: `agent.md`

# agent.md

Last updated: 2026-05-08

## Purpose

This is the compact entry file for Revision 5. Read it after compaction, summarization, restart, or when a new AI enters the project.

Keep startup context small. Do not read extra files unless the current task needs them.

## Fresh-Start Pointer

The fresh-start reading order lives in `AI_TODO.md`.

## Active Manuscript Location

```text
revision5/manuscript/
```

## Source Rule

Use these sources for manuscript content:

1. Current Revision 5 manuscript material.
2. Immediate predecessor material mapped in the source crosswalk.
3. Revision 3 source material.
4. Revision 2 source-history material.
5. User-provided research files, including the sources included by the research AI.
6. Direct web research only when the user asks or when a current claim must be checked.

Specific prior-revision source file paths live in `SOURCE_CROSSWALK.md`.

If a new research question or source needs to be saved, add it to the relevant `research_questions_*.md` file or ask the user where it belongs.

## Recovery Rule

Before ending a meaningful batch, update `AI_TODO.md` with:

- what changed
- files touched
- verification performed
- next action

Compaction can happen at any time. `AI_TODO.md` is the recovery anchor.
