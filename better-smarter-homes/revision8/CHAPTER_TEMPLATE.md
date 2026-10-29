# Chapter Template (Revision 8)

Every chapter of Stone and Wire has the same anatomy. The anatomy is fixed so the build can find
the parts (the chapter card, the time estimate, the decision register and the layer map are all
generated from it) and so a reader who learns one chapter can use all of them. The prose inside
the anatomy is never the same shape twice; see STYLE_GUIDE.md section 11.

## The skeleton

```markdown
# Chapter 11: The Wall System, Foundation to Roofline

<Opening: two to five sentences. The first sentence states the decision, number or fact that
matters most in this chapter. No "this chapter", no list of contents, no cross-reference pile.>

> **Jon's note.** <Design-rationale note, first person, Jon's voice. Drafted from the recorded
> decisions. Every sentence only Jon can confirm carries a marker: [JON: confirm] or
> [JON: why this choice?]. Three to eight sentences.>

## 11.1 What the wall has to do

**Simple**

<40 to 120 words. The first sentence is the point of the section. Plain words. "You" is fine.
One framing question is allowed if the next sentence answers it. One physical comparison is
allowed under STYLE_GUIDE.md section 4. No code numbers, no citations, no cross-references.>

**Applied**

1. <One action per step, imperative, condition before action, value inline, check or record
   named where one exists. Under 25 words per step.>
2. ...

**Professional**

<Mechanism, parameters, tolerances, coordination rules. Third person. No "you". Does not
restate a number that the Code block below states.>

**Code**

```
<Requirement in one plain sentence.>
  <The exact limit, value, geometry, test or trigger.>
  Source: <book name and section, edition where it matters>.
```

[FIGURE: wall-section-single-wythe, cross-section from footing to bond beam with the four control layers labeled]

### A subheading in sentence case, when a section needs one

<Subheadings carry no numbers. Use them instead of runs of bold run-in paragraphs. A subheading
inside a layer stays in that layer. A subheading after the Code block starts a new part of the
section and opens with its own layer label; the lint flags unlabeled prose after a Code block.>

## 11.2 ...

## Who decides what

| Decision | Who decides | When, or what triggers it |
|---|---|---|
| Tie spacing and embedment for the cavity wall | Engineer of record | At the structural design, from the wind and seismic loads |
| ... | ... | ... |

## Open items

- **Topic in a few words.** Unknown: <what is not known>. Answered by: <the source, test, person
  or event that settles it>. Assumed meanwhile: <what the text assumes until then>.

## Decisions this chapter records

- (decided) <one line per decision, stated as the decision, not as a sentence about deciding>
- (pending parcel) ...
- (pending engineer) ...
- (Jon to confirm) ...

## Records to keep

- <one line per record: what goes in the project binder from this chapter>
```

## Rules for each part

**The chapter title.** Title case with articles, conjunctions and short prepositions lowercase:
"The Wall System, Foundation to Roofline". The number is the final number in BOOK_STRUCTURE.md
and never changes.

**The opening.** Two to five sentences of prose. It earns its place by stating what the reader
most needs to know before the sections: the default choice and why it is the default, the one
number that governs, or the fact that changes the reader's plan. It may name, once, by topic
name, where the engineering, the control-layer physics or the hand skills live. It never
inventories the chapter, never says "this chapter", and never routes the reader to four other
chapters in a row.

**Jon's note.** A blockquote beginning with the bold words "Jon's note." It is the one place in
the book written in the first person and the one place a reason may be personal. The writer
drafts it from the decisions and reasons the research and the Revision 7 text record, in plain
first person, and marks every sentence that only Jon can confirm. A note that has no markers is
Jon's own text and no agent edits it. A note never contains code citations, dollar figures the
body already states, or anything the writer invented about Jon's life or preferences. When the
record gives no reason for a choice, the note says so: "[JON: why the single-wythe default over
the cavity wall for this house?]" One note per chapter, after the opening. Three to eight
sentences.

**Sections.** Numbered N.k in order, headings in sentence case. Each section has a Simple block.
Procedural content is in Applied. Parameters, mechanisms and limits are in Professional. Rules
with a source are in Code. A section includes only the layers that add information; most have
two or three. A section runs 300 to 900 words of prose; beyond that, it gets subheadings or
splits into two sections. Tables and Code blocks do not count toward the prose budget.

**Subheadings.** Level-three headings in sentence case, no numbers. Use them wherever the
Revision 7 text had three or more consecutive bold run-in paragraphs.

**Figures.** A placeholder marker on its own line, `[FIGURE: short-id, one-line description]`,
wherever a drawing belongs. The writer does not draw and does not describe the drawing in the
prose. The build replaces the marker; BOOK_STRUCTURE.md lists the figure program.

**Who decides what.** One table, unnumbered heading, after the last numbered section. Every
decision the body hands to the engineer of record, the geotechnical engineer, the building
department, a lab, a supplier or Jon appears here once with its trigger. Because the table
exists, body paragraphs do not end by handing off; a hand-off sentence appears in the body only
where the reader must act (schedule the meeting, bring the list, make the call).

**Open items.** The only place a research gap may appear. Three fields per item. The body text
never says that something was not found, not documented or not located; it states what is
known, what the text assumes, and sends the gap here. Items from the Revision 7 ledger
(research/OBLIGATIONS.md) that belong to this chapter appear here too, resolved or still open.

**Decisions this chapter records.** A reference list, not a summary. One line per decision,
each tagged with exactly one status: (decided), (pending parcel), (pending engineer), (Jon to
confirm). The build collects these into the decision register. Nothing follows the records
list: no closing paragraph, no "next chapter" line.

**Records to keep.** One line per record: the photographs, test reports, logs, product data and
approvals this chapter adds to the project binder.

## Word budgets

| Part | Budget |
|---|---|
| Opening | 40 to 120 words |
| Jon's note | 60 to 200 words |
| Simple block | 40 to 120 words |
| Applied step | under 25 words |
| Professional block | 60 to 300 words; longer blocks get a subheading |
| Section prose | 300 to 900 words |
| Who decides what | one row per decision; no prose |
| Open items | one to three sentences per item |
| Chapter close | lists only |

## What the build generates from this anatomy

The chapter card (scope line from the opening, reading time from the word count, Simple-path
time from the Simple blocks, related chapters from the topic-name cross-references), the layer
map, the table of contents, the decision register, the index and the PDF bookmarks. The writer
writes none of these.
