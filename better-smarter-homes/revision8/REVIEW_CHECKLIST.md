# Review Checklist (the orchestrator's acceptance test)

This is how a chapter written under `WRITER_BRIEF.md` is judged. The lint is the first filter.
The reading is the test. A chapter passes only when both pass and the reviewer would change
nothing in the brief because of it.

## 1. Mechanical (ten minutes)

- `python tools/lint.py manuscript/<file>`: every gate PASS. Record the numbers in the loop log.
- `python tools/stats.py manuscript/<file>`: sentence-length bands per layer, opener share, layer counts. Compare with the Revision 7 baseline for the same chapter.
- Section numbers contiguous and matching the chapter number. Anatomy present: opening, Jon's note, sections with Simple, Who decides what, Open items, Decisions, Records.
- Word count against the Revision 7 file. Lower only where Open items name what went.
- Preservation skim: diff the Revision 7 file against the new one and read the removed side. Every removed fact is either present elsewhere in the chapter or named in Open items.
- Spot values: eight values and every dollar figure against the answer files. Every Code entry three-part, with a source that the code library's routes can verify.
- Obligations: every `research/OBLIGATIONS.md` entry naming this chapter is met or carried into Open items.
- Counts: every number stated in prose ("five conditions", "seven values") against the list or table it describes, and against the same count elsewhere in the chapter (the lint cannot).
- The lint's INFO lists: most repeated phrases, Professional openers under eight words, dollar figures with four significant digits. Read them; they are where the refrains, the abstract openers and the false precision hide.

## 2. The reading (the real test; budget the tokens)

Read the whole chapter start to finish as a reader would, before judging anything. Then:

1. **The opening.** Does the first sentence state the decision, number or fact that matters most? Would a reader know within five sentences what this chapter settles? Any "this chapter", any inventory, any routing pile?
2. **Jon's note.** Does it read as a person's reasons? Is every sentence either drawn from the record or marked [JON]? Anything invented about him? Any padding?
3. **The Simple path.** Read only the Simple blocks, in order. Do they tell the system's story from start to finish? Does each open with its point? Does each name something you can point to? Read five aloud: do they sound like a person explaining? Would Jon's mother follow them? Could Jon's wife stop at the chapter close and feel she got something?
4. **Applied.** Could Jon do each step tomorrow morning? One action per step, condition first, a value or a check in each? Is the layer as full as the research allows, or thin?
5. **Professional.** Mechanism before parameter? Any number repeated from the Code block below? Any "you", any analogy? Would an engineer find it complete enough to check?
6. **Code.** Three parts every time, sourced, no advice, editions where they matter.
7. **Shapes.** Read the first sentence of every section in a row, then the last sentences, then the first sentence of every Simple block. Any shared opener, rhythm or closing move? Any bold run-in runs, colon fragments, delegation endings, research narration that the lint missed because the wording varied?
8. **Flow and order.** Does the chapter move in the order the reader needs (decision order, build order)? Does each section follow from the last, or is it a list of findings? Is anything in the wrong layer?
9. **Boundaries.** Spot three claims the bordering chapters also make. Same numbers, same positions, named by topic at the overlap?
10. **Poetry check.** Anything quotable? Any closing reversal, balanced pair, triad for rhythm, fragment for weight, closing line built to land? Any warmth that is performance rather than information?
11. **AI tells the catalog does not name.** Anything a builder at a table would not say: over-qualified sentences, symmetrical paragraphs, uniform paragraph length, a hedge in every third sentence, enumerations of exactly three, a summary sentence at the end of a block.
12. **The "Unsure" list.** Each item the writer flagged: was the call right? Does the pattern of flags point at a gap in the brief?

## 3. The verdict

Write to the loop log in `AI_TODO.md`:

- **PASS.** Every gate passes, the reading finds nothing that calls for a brief change. The loop stops.
- **ITERATE.** Name every finding by fault number or checklist item, with the sentence or section where it occurred, and then write the brief change that would have prevented it. Change `WRITER_BRIEF.md` (new version, dated, with the reason in the version history). Never patch the chapter and never message the writer with corrections. The next chapter tests the new brief.

A finding that is a one-off slip rather than a pattern is still logged, but it does not by itself
force an ITERATE if the brief already forbids it clearly; the question is always whether the
brief caused it or failed to prevent it.

## 4. After the loop stops

Compare the passing chapter with every earlier loop chapter on the same checklist and record,
per chapter, whether it should be redone under the final brief before the mass wave. Report to
Jon: iterations, what each one taught, the brief's version history, and the redo list.
