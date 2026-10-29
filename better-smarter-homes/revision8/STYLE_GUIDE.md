# Stone and Wire: Style Guide (Revision 8)

**Status.** The live guide for Revision 8, created 2026-10-26. It descends from the Revision 6
guide (revision6/writing_style_guide.md), keeps its layer system, its Code format and its bans
on performance, and changes the voice of the explanation layer, the shape of the chapter, and
the rules that made Revision 7 read as a specification written under a gag order. Those faults
are named in FAULT_CATALOG.md, Tier 4.

**Relation to the general guide.** The general prose guide is
`C:\Users\jon\Projects\writing-style-guide-v2.md` (Writing Style Guide, Version 2). Version 2
governs the prose. This file governs the book. A writer reads both in full. Where the two
differ, section 14 of this file says how and why, and this file wins inside this book.

**How to use it.** Sections 1 to 4 are the contract: who reads, how the book sounds, what each
layer is. Sections 5 to 9 are the rules by layer and by chapter part. Sections 10 to 13 are the
bans, the repeated-shape rule, the measured targets and the judgment checks. Section 16 is the
compact prompt for a small context. CHAPTER_TEMPLATE.md holds the anatomy; this file holds the
voice.

---

## 1. The readers

| Reader | What they read | What they need from the text |
|---|---|---|
| Jon, the owner-builder: a smart DIY builder who reads physics and will do most of the work himself | Everything | An action layer he can execute tomorrow morning, numbers he can check, and a record of his own decisions with his own reasons |
| A technician or contractor, years from now | Applied and Code, with Simple for orientation | The values, the order, the checks and the sources, without the why |
| An engineer or inspector | Professional and Code | The mechanism, the parameters, the tolerances, the standard and edition |
| Jon's mother, and friends who want to know what he is building | Simple blocks, Jon's notes, the figures | What the house is, what each system does, and why he chose it, in plain words, with nothing assumed |
| Jon's wife, who has ADHD and reads in short sittings | The Simple path: Simple blocks in order, Jon's notes, the chapter close | The point first, short blocks, visible structure, a place to stop, and a payoff for having read |

The four layers are the invention that serves all five readers from one text. Every rule in
this guide exists to make each layer sound like it was written for its reader and to make the
chapter navigable by someone who will not read all of it.

## 2. The voice

The book sounds like a builder who knows the subject explaining it to someone he respects, with
the drawings open on the table. He is specific, he gives numbers, he says what to do and why it
works, and he does not perform.

Every sentence states a requirement, a fact, an instruction, a value, a source, or (in Simple
blocks and in Jon's notes) the mechanism behind a thing or the reason for a choice. A sentence
that does none of those is removed.

**The quotable test.** If a sentence sounds quotable, rewrite it until it is usable: the reader
can extract an action, a value, a constraint, or a mechanism. A sentence that hands over a
feeling fails.

**The read-aloud test.** Read the paragraph aloud. If it sounds like a knowledgeable person
explaining something clearly, it passes. If it sounds performed, or like a committee, or like a
report, it fails.

**Where readability comes from.** Short sentences, defined terms, real numbers, real
consequences, and one concrete thing the reader can point to: a part, a tool, a material, a
place, a person. When a passage is flat, add one of those five. The fix is never a flourish.

**Plain, not poetic.** The instinct to make a sentence land, turn, or ring is the instinct to
resist. A sentence that ends on a reversal, a balanced pair, or a third item added for rhythm is
rewritten to end on its last fact.

## 3. The layer contract

| Layer | Reader | Job | Voice | Sentences | Contains | Never contains |
|---|---|---|---|---|---|---|
| **Simple** | Anyone, no construction background | What the thing is, what it does in this house, why it matters | Second person welcome. Plain words. One framing question per block, answered by the next sentence. One physical comparison per block under section 4. | Average 10 to 16 words, none over 25 | The mechanism in ordinary words; the stake in real numbers where they exist (what it costs, what fails, what it protects); the one or two terms it cannot avoid, defined in the same sentence | Code numbers, citations, cross-references, imperatives, trade jargon without a plain definition, lists longer than four items |
| **Applied** | The owner-builder doing the work | The actions in work order, with their checks and records | Imperative. One action per step. Condition before action. Numbered where order matters. | Average under 15 words, no step over 25 | Values inline, tools and materials with the specification that matters, the check for each step, what to record, the prerequisite skill | The why (Simple or Jon's note holds it), citations (Code holds them), narrative, framing, motivation |
| **Professional** | Engineer, inspector, builder | The mechanism, the parameters, the tolerances, the coordination rules, the limits of the approach | Third person. Trade vocabulary. Declaratives. | Average under 22 words, none over 40 | What controls the work and why it works; standards and editions named in the sentence; values from industry practice or manufacturer data with their source named | "You"; analogy; the exact value the section's Code block states (section 7); framing; philosophy |
| **Code** | Anyone checking compliance | The rules | Three parts: the requirement in one plain sentence, the exact value, the Source line | Telegraphic | Requirements sourced to a statute, a rule or a consensus standard, with the edition where the value depends on it | Explanation, opinion, project advice, any entry without a source |

**No two layers contain the same information.** A layer is included only where it adds
information the other layers do not. Most sections have Simple and one or two others. Every
section has Simple, even a two-sentence orientation before a reference table.

**The layers are labeled.** The label is the bold word on its own line (`**Simple**`,
`**Applied**`, `**Professional**`, `**Code**`). Freeform, unlabeled prose is allowed in three
places only: the chapter opening, Jon's note, and a bridge of one or two sentences between
sections. The design chapters (What Concrete Uniquely Enables, Aesthetics, Passive Design,
Resilience) obey this too: options and their consequences in Simple, the method in Applied, the
engineering limits in Professional, the triggers in Code. Revision 7 let those chapters go
unlabeled and lost the reader paths; Revision 8 does not.

## 4. The Simple layer, in detail

Simple is the only layer that explains, and it is the layer the non-builder readers live in.
It is written as one person telling another what a thing is and why it is here.

**Allowed, and wanted:**

- **"You" and "your house"** as the default address, whenever the sentence carries the same
  information it would in the third person. "The regulator drops the street pressure to 60 psi
  because your fixtures are rated for 80."
- **One framing question per block**, when the next sentence answers it. "Who makes the rules
  for your house? The rules come in layers." Not in two consecutive sections.
- **One physical comparison per block**, under four conditions: the comparison is to a thing the
  reader has handled (a garden hose, a sponge, a car jack, a thermos is not banned if it meets
  the other three); the mechanism is stated in literal terms in the same paragraph; the
  comparison maps to that mechanism and not to a feeling; and the comparison never stands in for
  the literal statement. "The drained gap behind the brick works like the gap between a
  raincoat and a sweater. Water that gets through the brick runs down its back face to the
  flashing at the bottom and out through the weep holes, and the block behind it stays dry."
  Banned under this allowance: anything abstract, anything
  cute, living-thing framings for materials ("the wall breathes"), and comparisons that carry
  admiration.
- **A chain of physical dependencies written as a chain**, when each link is a real load path or
  sequence: "The ground holds up the footing, the footing holds up the wall, and the wall holds
  up the roof." A chain with a link added to make three is banned under Version 2's triad rule.
- **A cost pair** (what prevention costs against what the failure costs) when both numbers are
  real and sourced, written as two facts and not as a reversal: "A soil test costs $500 to
  $1,200. A footing poured on the wrong soil costs $20,000 to $60,000 to underpin."
- **The first sentence states the point of the section.** No label, no "The point:"; the first
  sentence simply is the point. A reader who reads only the first sentence of every Simple block
  gets the chapter's argument.

**Not allowed:**

- Proverbs, wisdom, timeless truths about houses or life, warning cadence, scene-setting,
  "imagine", "picture".
- Code numbers and citations. Simple says "the code sets a minimum ceiling height and this house
  goes two feet above it"; Code states 7 feet and R305.
- Cross-references. Simple never sends the reader elsewhere.
- Imperatives. Instructions belong in Applied.
- More than four items in a list.
- Blocks over 120 words. A longer block is two blocks, or it is carrying Professional content.

**Before and after.**

Before (Revision 7, chapter 1): "This book serves four functions: 1. A statement of what the
house is meant to be, with the reasons. 2. A record of the design decisions, with the reason
for each, in a form open to review and revision. 3. The decision framework and trade-off data
needed to finalize design decisions before construction begins. 4. Context for builders,
inspectors, designers, engineers, and curious readers to understand the project on first
reading."

After: "The house is a concrete and masonry home in Oregon, built to last centuries instead of
decades. Each decision about it is recorded with its reason, so a future owner or contractor can
follow the thinking. Each comes with the numbers, the code sections and the checks to build it."

Before (Revision 7, chapter 6): "There are two realistic ways to design this house. The
engineered way: pay a licensed structural engineer ($4,000-$10,000, 2026) to design exactly the
house you want."

After: "You can have this house designed two ways. An engineer designs exactly the house you
want, concrete floors and roof included, for $4,000 to $10,000. Or you follow the code's
pre-approved tables for free, and accept simpler shapes with wood floors and roof above the
concrete walls. This house takes the engineered way, because the thousand-year shell needs the
concrete floors and roof."

## 5. The Applied layer, in detail

Applied is the action layer and it is the layer Jon will work from. Revision 7 under-wrote it.
Revision 8 grows it from the answered research: every answer that describes how to do something
lands here.

- **Imperative, one action per step.** "Set the bolts 6 feet apart or less." Not "bolts are set"
  and not "you will want to set".
- **Condition before action.** "When the first course is level, build the corner leads."
- **Numbered steps where order matters; bullets where it does not.**
- **Each step names its check and its record** where one exists: what you measure or see, and
  what goes in the binder (photo, log line, test report).
- **Values inline.** The step states the number. Code states the source.
- **Tools and materials named** with the specification that matters: "Type S mortar", "a
  4-foot level", "ladder-type joint reinforcement at the spacing on the structural drawings".
- **Prerequisite skill named** where one exists: "This step needs a laser level set up and
  checked. The Masonry Craft chapter has the setup."
- **Costs** as ranges from real sources, under the cost-year rule in section 9.
- **No why.** An Applied step that explains itself is split: the instruction stays, the reason
  moves to Simple or to Jon's note.
- **No citations, no narrative, no framing sentence before the steps** beyond one line that
  states the condition for the whole procedure ("Build the default wall in this order.").

## 6. The Professional layer, in detail

Professional is for the reader who went to school for this. It is complete enough to check the
design against and it never restates what the Code block below it says.

- **Mechanism first, then parameter.** Why the value controls the outcome, then the value, the
  tolerance and the coordination rule.
- **No echo.** The number the section's Code entry states is not repeated here. Professional
  states what the number controls or why it is that value, and lets Code state it. A value
  from industry practice, a manufacturer's data or a standard that is not a code requirement
  belongs here, with its source named in the sentence ("BIA Technical Note 28D puts the cavity
  at 2 inches minimum").
- **Standards and editions in the sentence**, never as bracketed citations.
- **No "you". No analogy. No framing.**
- **Trade terms used without a gloss.** The glossary defines them. A term the chapter cannot
  assume is defined once, in the Simple block, at first use.
- **Sentences under 22 words on average**, one idea each. Long technical sentences are split at
  the clause.

## 7. The Code layer, in detail

Unchanged from Revision 6. Every entry has three parts:

```
Anchor bolts must tie the sill plate to the foundation.
  1/2-inch bolts minimum, embedded 7 inches, spaced 6 feet or less, one bolt within 12 inches of each plate end.
  Source: ORSC R403.1.6 (2023 edition).
```

- Every entry ends with a Source line naming the book and the section, with the edition where
  the value depends on it. An entry without a source is not a Code entry.
- A Code block requires at least one entry sourced to a statute, a rule or a consensus standard.
  Guidance (NIST publications, agency practice, industry technical notes) is cited inside
  Professional, not in Code.
- A Code block never restates the section's own advice.
- No invented citations. An unverifiable entry becomes an open item.
- Verification routes are in `../revision6_code_library/README.md`.

## 8. The chapter, in detail

CHAPTER_TEMPLATE.md holds the anatomy. These are the rules for the parts around the sections.

**The opening.** Two to five sentences. The first sentence states the decision, number or fact
that matters most in the chapter. The opening may name once, by topic name, where the
engineering, the control-layer physics or the hand skills live. It never says "this chapter",
never lists the contents, and never routes the reader to four chapters in a row.

**Jon's note.** First person, Jon's voice, one per chapter, after the opening. It is the one
place in the book a reason may be personal. The writer drafts it from the decisions and reasons
the record states, and marks every sentence only Jon can confirm with `[JON: confirm]` or a
question in the same brackets. The writer never invents a preference, a memory or a feeling for
Jon. Where the record gives no reason, the note asks: "[JON: why this over that for this
house?]" A note without markers is Jon's own text and no agent changes it.

**Who decides what.** One table per chapter. Every decision the body hands to the engineer of
record, the geotechnical engineer, the building department, a lab, a supplier or Jon appears
here once with its trigger. Because the table exists, body paragraphs do not end by handing off.
A hand-off sentence appears in the body only where the reader must act.

**Open items.** The only place a research gap lives. Three fields: what is unknown, what answers
it, what the text assumes meanwhile. The body never narrates the research.

**The chapter close.** "Decisions this chapter records", each line tagged (decided), (pending
parcel), (pending engineer) or (Jon to confirm), then "Records to keep". Lists only. Nothing
after them: no summary, no closing paragraph, no pointer to the next chapter.

**Figures.** A `[FIGURE: id, description]` marker where a drawing belongs. The writer does not
draw and does not narrate the drawing.

**Cross-references.** By chapter topic name, never by number. At most one cross-reference
sentence per section, placed where the reader needs it.

## 9. Numbers, costs, dates and terms

- **Costs** are dollar ranges from real sources. The cost year is stated once per chapter, in a
  sentence near the first cost: "Costs in this chapter are 2026 figures unless a different year
  is given." A figure from another year carries its year. No "(2026)" after every number.
- **Dates.** No "as of" stamps in body text. Code editions and adoption dates are stated as facts
  where a value depends on them.
- **Terms** are defined once per chapter at first use, in the layer where they first appear,
  preferably Simple, in the same sentence. The glossary carries the rest. The same term is not
  re-glossed later in the chapter.
- **Unanchored size words** ("cheap", "expensive", "a lot", "small", "fast") appear only with a
  number, a ratio or a named standard. Where no real number exists, name the mechanism or cut
  the claim. Never invent a number to satisfy this rule.
- **A claim that the design exceeds a minimum states the design's value beside the minimum.**
- **Units** as the trade uses them in Oregon; metric beside them where the standard is metric.

## 10. Bans

Absolutes. Each is checked by the lint where a pattern exists and by reading where it does not.

1. **Em dashes and semicolons.** Periods, commas, colons before lists, parentheses.
2. **Metaphor and analogy** outside the Simple allowance in section 4. **Personification** of
   materials, assemblies, the house, or the book. The book contains, lists, states, specifies,
   defines, describes, includes, provides, records, identifies, documents. It does nothing else.
3. **Performance**, loud or quiet: aphorisms and gnomic lines; antithesis and "not X but Y";
   chiasmus; balanced pairs and parallel sentences built for rhythm; triads for rhythm;
   anaphora; vignettes that imply a claim; persuasive headings; closers and wrap-up lines;
   fragments for emphasis; closing reversals.
4. **Research narration.** "No published", "was located", "were found", "the project
   research", "undocumented", "not documented", "no source", "as of [month] [year]" and their
   kin. Gaps go to Open items.
5. **Delegation endings** as a pattern. More than one paragraph per section ending on who
   decides is a fault; the Who-decides table carries it.
6. **Encyclopedia paragraphing.** More than two consecutive paragraphs opening with a bold
   run-in topic. Use a subheading or a table.
7. **Colon fragments.** "The operational definition: ...", "Project rule: ...", "The result:
   ...". Write the verb. A colon introduces a list or a quotation.
8. **Self-description.** "This chapter", "this section", "the book", "this book" in body prose.
   The opening states scope as facts about the house.
9. **Invented** values, citations, anecdotes, decisions, preferences.
10. **Chapter-number references.** Topic names only.
11. **"BSH"** and any reader-facing revision history or project acronym.
12. **Hedges.** Informally, literally, essentially, in a sense, arguably, typically, generally,
    and "may be" as softening. The legal "may" (permission in a statute) stays.
13. **Stock AI vocabulary.** Delve, tapestry, realm, landscape, crucial, pivotal, robust,
    seamless, leverage, foster, elevate, transformative, journey, unlock, empower, embrace,
    ecosystem, and the decorative intensifiers truly, deeply, profoundly, remarkably,
    beautifully, simply, really, actually, very, quite.
14. **Rhetorical questions** outside the Simple framing question; **reader self-check
    instructions** ("ask yourself").
15. **Imperatives outside Applied blocks and procedural lists.**
16. **Machine title case.** Section headings in sentence case. Chapter titles in title case with
    articles, conjunctions and short prepositions lowercase.
17. **Dropping content** from the Revision 7 text without an open item naming what was dropped
    and why. Preserve and grow. This outranks every style preference in this file.
18. **Date stamping** every figure; **gloss cadence** (re-glossing a term already defined in
    the chapter); **cross-reference piles** (more than one cross-reference sentence per
    section).

## 11. Repeated shapes

A reference work repeats a structure, so any verbal habit becomes visible. Version 2's rule
applies to every repeated unit here: chapter openings, section openings, Simple blocks, Applied
procedures, section endings, Jon's notes.

**The check, done before a chapter is reported finished:** read the first sentence of every
section in the chapter in a row, with the middles covered. Then the last sentence of every
section. Then the first sentence of every Simple block. If they share an opener, a rhythm, a
length or a closing move, rewrite them so each starts with the fact most specific to it.

**Determiner share.** Under 18 percent of a chapter's sentences open with "The", "A" or "An".
Vary by leading with the condition, the actor, the place, the number, or in Applied the verb.
Vary sentence length by the information, never by a pattern.

**Stock phrases.** "The engineer of record", "this project", "this house", "in this house",
"the owner" recur by necessity. Watch their density. A paragraph that uses one of them three
times is rewritten.

## 12. Measured targets

The lint (tools/lint.py) reports these per chapter. A chapter is not finished with a FAIL.

| Measure | Target |
|---|---|
| Em dashes, semicolons | 0 |
| Research-narration phrases | 0 |
| Colon fragments | 0 |
| "This chapter", "this section", "this book", "the book" in prose | 0 |
| Consecutive bold run-in paragraphs | 2 or fewer |
| "The", "A", "An" sentence openers | 18 percent or less |
| Sentences of 30 words or more | 8 percent or less of the chapter |
| Simple blocks: average sentence, longest sentence, block length | 16 words or less; 25 or less; 40 to 120 words |
| Applied steps: average, longest | 15 or less; 25 or less |
| Professional: average, longest | 22 or less; 40 or less |
| Paragraphs over 120 words | 0 |
| Sections without a Simple block | 0 |
| Code entries without a Source line | 0 |
| Numbers stated in both Professional and Code of one section | 0 |
| "(2026)" and other year tags after figures | the cost-year sentence once; tags only where the year differs |
| "Engineer of record" and "building department" paragraph endings | 1 or fewer per section |
| Cross-reference sentences per section | 1 or fewer |
| Headings in machine title case | 0 |
| Section numbers | contiguous, matching the chapter number |
| Open items, Who-decides table, Decisions, Records | present |
| Word count against the Revision 7 text | not lower, unless Open items name what was dropped |

## 13. Judgment checks

The writer answers these before reporting; the reviewer answers them again while reading. A
check that passes cleanly passes cleanly; do not stretch to find problems.

1. Would a curious non-builder keep reading the Simple blocks, and could she retell the point
   afterward?
2. Could the owner-builder perform each Applied step tomorrow morning?
3. Does every risk passage state what the reader does about it, in varied wording?
4. The quotable test, sentence by sentence on anything that stands out.
5. Does any sentence state a timeless truth instead of a requirement or a checkable fact?
6. Does any passage imply a claim through a scene instead of stating the property and its
   mechanism?
7. Does any evaluative word lack a number, ratio or named standard where a real one exists?
8. Is any document element (book, chapter, section, block, table, entry) the subject of an
   action verb outside the approved list?
9. Does any requirement lack an actor?
10. Can each sentence be understood from the current page alone: referents named, comparatives
    resolved, causal chains written out?
11. Are the protected lines (section 15) unchanged?
12. Is there any passage a reader would call boring where a number, a cost or a consequence
    is available and missing?
13. Does any sentence explain by comparison outside the Simple allowance, or deliver a fact in
    proverb cadence?
14. Does any imperative or question appear outside Applied, beyond the one Simple framing
    question?
15. Comma splices; sentences stacking five or more coordinated elements; paragraphs mixing more
    than two regulatory topics.
16. Where a subject is treated in two chapters, does each name the other by topic?
17. **Point first.** Does the first sentence of each Simple block state the section's point?
18. **Read aloud.** Does each Simple block and Jon's note sound like a person explaining?
19. **Repeated shapes.** The section-11 check, done.
20. **See it.** Does every Simple block name at least one thing the reader can point to?
21. **Echo.** Does any Professional block restate a number its Code block states?
22. **The human.** Does Jon's note read as a person's reasons, with [JON] markers exactly where
    only he can answer, and nothing invented?
23. **The wife's path.** Read only the Simple blocks of the chapter in order. Do they tell the
    story of the system from start to finish, with a place to stop at the chapter close?
24. **Research in the text.** Is there any sentence about what was or was not found?
25. **Preservation.** Skim the Revision 7 text against the new one. Is anything gone that the
    Open items do not name?

## 14. Differences from Version 2, and why

- **Imperatives are confined to Applied blocks and procedural lists.** Version 2 allows them
  anywhere in instructional writing. Here the confinement is what keeps the layers distinct.
- **Simple allows one physical comparison per block** under section 4. Version 2 bans analogy.
  The allowance exists for the readers with no construction background, and its four conditions
  keep it from becoming decoration.
- **"You" is encouraged in Simple and Applied and banned in Professional and Code.** Version 2
  is neutral.
- **The framing question is per Simple block, answered by the next sentence.** Version 2 allows
  one per section as an opener. Not in two consecutive sections.
- **Semicolons are banned here as in Version 2.** The Revision 6 guide allowed them and the
  Revision 7 text contains them; writers remove them.

## 15. Protected text

The owner's own words. They stay as written; review suggestions against them are overruled.

- The chapter 1 opening: "I have wanted to build a long-life concrete home in Oregon for about
  ten years. This book is the plan."
- The project-goal label "a thousand-year structural shell" and its framing as the project's
  named goal.
- Every Jon's note that carries no [JON] marker.
- New protected lines are added only by Jon.

## 16. Exemplars

`exemplars/anchor-bolts-sample-page.md` shows one topic in all four layers with no overlap: the
whole contract on one page. `exemplars/before-and-after.md` shows the Revision 7 faults next to
their repairs: an opening, a Simple block, a research-narration paragraph, a delegation ending,
a run of bold paragraphs, a Professional block that echoed Code.

## 17. Compact working prompt

For a small context, load this plus the sample page instead of the whole guide.

Write a chapter of a technical field manual for an Oregon owner-builder building a concrete
home, for five readers at once through four labeled layers. Simple explains what a thing is and
why it is here, to a reader with no construction background, in plain words, in the second
person, with the point in the first sentence; it may use one framing question answered at once
and one physical comparison tied to the stated mechanism; it never cites code. Applied gives the
actions in order as imperatives, one action per step, condition first, values inline, each step
with its check and record. Professional gives the mechanism, the parameters and the limits in
trade vocabulary, in the third person, without repeating the Code block's numbers. Code gives
each rule in three parts: requirement, exact value, Source line; no source, no entry. Open with
the decision or number that matters most, never with a description of the chapter. Write Jon's
note in his first person from the recorded reasons and mark with [JON] every sentence only he
can confirm. Put every hand-off in one Who-decides table and every research gap in the Open
items list; never narrate the research in the body. Close with the decisions recorded and the
records to keep, and nothing after. No em dashes, no semicolons, no "this chapter", no colon
fragments, no runs of bold run-in paragraphs, no hedges, no stock phrases, no performance of
any kind, no invented values or citations, no chapter numbers in cross-references. Preserve
every fact of the Revision 7 text or name what was dropped in Open items. When prose feels
thin, add a number, a product, a code section, a measurement or a consequence. When it feels
long, cut words, not information. Read every section's first sentences together before
finishing; if they share a shape, rewrite them.
