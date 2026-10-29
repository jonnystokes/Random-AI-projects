# Writing Style Analysis: Revisions 2 Through 5

Date: 2026-07-04
Scope: Chapters 1-3 of every revision read in full, plus targeted samples from later chapters and pattern scans across every manuscript file in all four revisions.

## 1. Summary Of Findings

1. Revision 2 has the best reader-facing voice in the project's history. It reads like a competent friend explaining real work: plain words, direct questions, dollar figures, inline definitions, and clear "walk away" advice.
2. Revision 3 is not a style change. It is Revision 2 with a new filing system. Its newly written material (the legal chapter) keeps the Revision 2 voice.
3. Revision 4 is where the "poet" arrived. It compressed the book from roughly 200,000 words to 89,000 (a 55 percent loss), deleted every inline definition and every dollar figure, and replaced information with rhetorical performance: aphorisms, antithesis, persuasive headings, and a memoir opener.
4. Revision 5 is the correction. Its structure (the four-layer system with real code content) is the strongest technical container the book has ever had. But the correction is overshooting on voice: the rewritten chapters have the longest sentences of any revision and a formal, specification-like register that trades away the approachability the book had in Revision 2.
5. The best target for Revision 6 is not any single existing revision. It is Revision 2's voice inside Revision 5's architecture. Section 7 defines that target precisely, and Section 8 proposes a style-guide redesign so a simpler AI can hit it.

## 2. The Numbers

Metrics from pattern scans across all manuscript files in each revision. Prose sentence statistics exclude headers, tables, bullets, and code blocks.

| Metric | Rev 2 | Rev 3 | Rev 4 | Rev 5 | Rev 5 ch 1-6 only |
|---|---|---|---|---|---|
| Total words | 200,056 | 193,209 | 89,338 | 106,028 | - |
| Inline parenthetical definitions | 2,782 | 2,654 | 0 | 366 | - |
| Dollar figures | 744 | 639 | 0 | 102 | - |
| Dollar figures per 10k words | 37 | 33 | 0 | 9 | - |
| Antithesis pattern ("X is not A. It is B.") | 1 | 1 | 34 | 16 | 0 |
| Uses of "you/your" | 295 | 179 | 60 | 27 | - |
| Average prose sentence length (words) | 11.3 | 11.6 | 13.8 | 15.1 | 17.0 |
| Prose sentences of 30+ words | 2.9% | 2.5% | 4.0% | 6.2% | 10.1% |
| Em dashes | 4,280 | 3,798 | 0 | 0 | 0 |

Reading the table:

- The content collapse happened in Revision 4, not Revision 5. Half the book disappeared in one revision, and with it every inline definition and every cost figure.
- The rhetorical infection also happened in Revision 4 (34 antithesis constructions against 1 in Revision 2). Revision 5's remaining 16 all live in chapters 9-21, which are still Phase 1 retrofits of Revision 4 text. The Phase 2 rewrites (chapters 1-6) are clean.
- The overshoot is visible in the last column. The Phase 2 chapters average 17 words per prose sentence, the longest in the book's history, with one sentence in ten running 30+ words. Revision 2 averaged 11. Banning the poet's short punchy fragments pushed the prose toward long compound sentences, which is the opposite failure for a reader who wants simple instructions.
- Specificity is recovering (dollar figures back from 0 to 9 per 10k words) but is still a quarter of the Revision 2 density.

## 3. The Four Styles, One At A Time

### Revision 2: the competent friend

Structure: every section runs Plain language, then Technical detail, then Key code references. Definitions ride inline in parentheses. Costs, ranges, and agency names appear constantly.

What it sounds like:

> **Plain language:** Does the property already have power, water, internet, and road access, or will bringing them in cost a fortune?

> **What it costs:** Roughly $500-$1,200, depending on county and complexity. Small price for avoiding a catastrophically wrong purchase.

> ...a title report (a legal document from a title company listing what the property includes)...

Why it works:

- **Questions do the framing.** Sections open with the question the reader actually has ("can you actually build on this parcel?"). This is the "slightly exciting" quality: the reader feels the stakes without being performed at.
- **Definitions never leave the page.** 2,782 parenthetical definitions means a non-builder never has to stop reading. This is the single cheapest readability device in the whole project and Revision 4 deleted all of it.
- **Money is information.** "$20,000-$50,000 instead of $8,000-$15,000" teaches more about septic risk than any paragraph of caution.
- **The scaffold repeats.** Why this matters. When to do it. What it costs. How to verify. The reader always knows where they are.

Honest weaknesses, so Revision 6 does not romanticize it:

- Em dashes everywhere (4,280), used as all-purpose glue.
- The Plain language and Technical detail blocks sometimes say the same thing twice at two vocabulary levels.
- Code references are keyword stubs ("ORSC R401.3 (drainage)") rather than working content. The book could not substitute for the code book.
- Mild personification ("water wants to go downhill") and a few aphorisms ("The right house on the wrong land is still the wrong project"). At Revision 2's dosage (about one per chapter), these read as natural speech, not performance. The dosage is the difference.
- No inspection depth, no records discipline, no verification program.

### Revision 3: the same book, refiled

Chapters 1-2 are verbatim copies of Revision 2 sections. The newly written legal chapter keeps the exact voice and scaffold ("Plain language / Technical detail / Key code references", inline definitions, real dollar figures, "Strategic implication" notes). Revision 3 is a structural conversion, not a style event. The user's memory that things went wrong "around version 3 or 4" resolves cleanly to: Revision 4.

### Revision 4: the poet

What it sounds like, all quotes verbatim from chapters 1-3:

> I have carried this house around for about ten years.

> Code Is A Map, Not A Wall (a section heading)

> These principles are not decoration. They make decisions.

> Inspections are not interruptions. They are checkpoints that let the project move forward without hiding mistakes.

> The owner-builder path is not a loophole. It is a legal role with duties attached.

> That does not make the goal smaller. It makes it buildable.

> Lights should still turn on. Heat should still work. Doors should still lock.

> Never bury a code question in concrete.

> This chapter puts property questions in order before the purchase becomes emotional.

> Do not commit to the view before checking septic, access, zoning, water, utilities, title, and drainage. Those are not details. They determine whether the project can exist.

The pattern inventory: memoir opener, persuasive headings, antithesis (34 instances), definition by negation, rhetorical triplets, aphoristic closers, blockquote pronouncements ("**Rule:** if the work must be approved..."), and compound serial lists used as incantation ("It is land, tools, concrete, weather, math, comfort, code, systems, and imagination brought into one build").

Two separate crimes, and the second one matters more:

1. **The voice crime** is what the reader notices. Every section wants to be quoted. The prose performs conviction instead of transferring information. A reader trying to learn septic evaluation gets a worldview instead of a checklist.
2. **The content crime** is worse. 111,000 words vanished. Every inline definition (2,782 to 0). Every dollar figure (744 to 0). The compression and the poetry are the same event: when information is deleted, style has to fill the space, and aphorism is what filled it. A sentence like "Never bury a code question in concrete" exists because the three paragraphs that used to explain sleeve placement, rebar verification, and pre-pour inspection were gone.

To be fair, Revision 4 contributed two things worth keeping: the four-layer idea (`Simple`/`Applied`/`Professional`/`Code` grew out of its reading levels) and the sorting-table habit (the "Dealbreaker / Expensive risk / Design constraint" triage table in chapter 3 is genuinely good and survives into Revision 5).

### Revision 5: the exorcism

The Phase 2 chapters (1-6) fixed the rhetoric completely. Zero antithesis, zero aphorisms, zero persuasive headings. The four-layer system now carries real content, and the `Code` blocks are the best thing the project has ever produced: a reader can verify anchor-bolt spacing or drainage slope without opening the ORSC. The Applied blocks are strong ("Walk the site after rain if possible. Look for: where surface water flows and pools...").

But compare the openers across generations:

- Revision 2: "Three words drive every decision."
- Revision 5: "Six principles guide design decisions when more than one option would meet the code. They are stated in the order that controls when two principles conflict; durability and reliability win over simplicity and clarity when the trade is real."

Both are correct. The first is a friend talking. The second is a specification document. The Revision 5 sentence is 33 words with two dependent clauses and a semicolon, and the data says it is typical: the Phase 2 chapters run the longest sentences in the book's history.

The cause is visible in the style guide itself. The guide is roughly 40 prohibitions and very few positive targets. Every "Bad" example in it is a poet-side failure; there is not one example of the opposite failure (bureaucratic flatness, long compound sentences, legalese register). An AI steering by that guide has gradient in only one direction: away from the poet, toward the committee. That is exactly the drift the metrics show.

## 4. The Same Topic In All Four Voices

Topography, as actually written in each revision:

**Revision 2/3:**
> **Plain language:** The shape of the land. How flat, how sloped, which direction it faces, where water drains. A flat property is easier to build on. A sloped property costs more to excavate but can offer views, drainage, and walk-out basement options.

**Revision 4:**
> Site conditions determine feasibility. ... The right land reduces build complexity and supports daily life. The wrong land turns every system into a workaround. This chapter puts property questions in order before the purchase becomes emotional.

**Revision 5:**
> Slope and drainage affect water management, truck access, foundation type, and erosion-control obligations. ... Topography drives cut and fill, positive drainage strategy, retaining-wall demand, driveway grade, erosion-control planning, staging-area selection, waterproofing demand, flood exposure, and foundation complexity.

Read them in sequence: Revision 2 explains to a person, Revision 4 sells to an audience, Revision 5 files a report. The Revision 5 sentence is accurate and complete, and it lists nine noun phrases in one breath. Nobody would call it fun to read.

## 5. Verdict

For ease of understanding and straightforwardness, with "slightly exciting but not clown fun":

1. **Revision 2 is the best voice.** Short sentences, direct questions, inline definitions, real numbers, and stakes stated plainly. Its excitement comes from specificity (a $50,000 septic surprise is exciting on its own), not from rhetoric. This matches the requested register almost exactly.
2. **Revision 5 is the best book.** Its architecture (layers, working code blocks, triage tables, records discipline, research-pause rule) is what makes the manual actually usable on a jobsite. Revision 2 could never substitute for the code book; Revision 5 can.
3. **Revision 4 is the failure mode**, and it is a compound failure: rhetorical style riding on top of silent 55 percent content deletion. Its two real contributions (the layer idea, the triage table) are already absorbed into Revision 5.
4. **Revision 5's current trajectory needs one correction:** the register is drifting formal and long-sentenced because the style guide only polices one direction. Left alone, chapters 7-21 will come out clean but dry.

## 6. Why The Poet Appeared (Mechanically)

Worth stating plainly because it determines how to prevent a relapse in Revision 6:

1. **Compression forces style.** When an AI is asked to shorten, it preserves what feels high-value per word, and rhetoric feels high-value per word. Aphorisms are compression artifacts. Protecting content volume (which Revision 5's control docs now do) is itself a style defense.
2. **"Make it readable" without exemplars means "make it literary."** An instruction to be engaging, absent samples of the wanted voice, gets resolved from the model's priors, and the priors say engaging means quotable. The fix is not more adjectives in the instructions. It is exemplar passages.
3. **Prohibition-only guides overcorrect.** The current guide is a superb immune system against Revision 4 and has no defense against sounding like a permit application. Models follow gradients; if all the walls are on one side, the drift goes to the other.

## 7. Recommendations For Revision 6

### Voice target, stated positively

Write like a competent friend who has done the work, explaining it to a capable adult who has not. The friend is direct, specific, occasionally wry about what things cost, and never performs. Excitement comes from stakes and specifics, never from phrasing.

### Concrete changes

1. **Restore the inline definition habit.** First use of any trade term in `Simple` or `Applied` gets a short parenthetical definition, Revision 2 style: "a title report (a legal document from a title company listing what the property includes)." Target the Revision 2 density, roughly one per 70 words in reader-facing layers. The glossary remains the formal home; the parenthetical is the reading aid.
2. **Restore cost framing everywhere money is real.** Dollar ranges with the estimate year, at or near Revision 2 density (30+ per 10k words, against today's 9). "Roughly $500-$1,200 (2026)" beats a paragraph of caution.
3. **Set sentence-length bands per layer.** `Simple`: average under 14 words, no sentence over 25. `Applied`: imperative steps, average under 15. `Professional`: average under 22, one idea per sentence. Long noun-pile sentences (the nine-item topography sentence in Section 4) get broken into a list or cut.
4. **Re-admit direct address in `Simple` and `Applied`.** Revision 2 used "you" about ten times more often than Revision 5. Imperatives are already allowed; let `Simple` blocks ask the reader's own question ("Can a septic system go on this parcel? Some soils make it impossible, and that makes the land unbuildable."). One question per section, as a framing device, is the "slightly exciting" dose. Ten would be clown fun.
5. **Formalize the Revision 2 micro-scaffold** as optional standard elements: Why this matters, When to do it, What it costs, How to verify. These four already exist scattered through Revision 5's surrounding-text categories; naming them as the default set restores the rhythm that made Revision 2 easy to navigate.
6. **Keep unchanged from Revision 5:** the four-layer system, colon-format `Code` blocks with working content, the triage tables, the no-em-dash rule, the no-personification and no-rhetoric absolutes, chapter references by topic name, the research-pause rule, and the records discipline.
7. **Continue the content restoration.** The book is at 106k words against an original 200k. Some of the loss was genuine duplication (Revision 2 said many things twice across its two layers), but the crosswalk work should keep treating Revision 2 as the recoverable ore body, especially for costs, definitions, and the "why this matters" explanations that Revision 4 burned.
8. **Add an anti-dryness check to verification scans.** The current scans only hunt poet patterns. Add: average sentence length per new section, definition density, dollar-figure presence in any section that discusses procurement or trades, and at least one direct question or second-person sentence per `Simple` block.

## 8. Improving The Style Guide For Simpler AIs

The current guide (519 lines) was written to stop Revision 4, and it succeeded. Its weaknesses for a smaller model are structural: it is prohibition-heavy, exemplar-light on the positive side, and it asks for judgment in places where a small model has none. Redesign principles:

### 8.1 Exemplars beat rules for small models

Lead the guide with three to five short gold-standard passages (one full section showing `Simple` + `Applied` + `Code` in the target voice) and label them "imitate these." A small model pattern-matches far more reliably than it reasons about 40 prohibitions. The current guide's only samples of the wanted voice are one-line "Better" cells in tables; a full-page exemplar is worth all of them combined.

### 8.2 Show both failure directions

Every Bad/Better table currently corrects poet-to-plain. Add a second column of failures: committee-to-plain. Example:

| Too poetic | Too dry | Target |
|---|---|---|
| The land gets a vote. | Site conditions constitute a controlling input to feasibility determination across multiple project dimensions. | The site decides a lot: what the foundation costs, where the septic goes, whether trucks can reach the pour. Check it before you fall in love with the view. |

Without the middle column, a model correcting away from column one lands in column two and the guide calls it a pass.

### 8.3 Convert judgment rules into procedures

Small models fail on "when it earns its place." Replace judgment language with decision steps:

- Instead of "metaphor is allowed only when the figure is precise": keep the flat ban. Absolute rules are the only rules a weak model applies consistently. (The guide already went absolute here; that instinct is right. Apply it elsewhere.)
- Instead of "use layers only where each adds value": give the test as a procedure. "Write the `Applied` block first. Then ask: does the `Simple` block contain a sentence that does not appear in `Applied` in harder words? If not, delete the `Simple` block."
- Instead of "first person where it earns its place": "First person is allowed only in chapter 1's opening and in design-rationale notes that name a specific choice. Nowhere else."

### 8.4 Make the lint mechanical

Most of the banned patterns are literally grep-able. Ship a `style_lint` script in the repo (or a checklist of exact regexes) covering: em dashes, " is not [^.]*\. (It is|They are)", the intensifier list, "wants to|tells you|asks you" personification, stock AI phrases, displayed forms, and chapter-number references. A simple AI runs the script instead of holding 40 rules in attention; the Pre-Submission Check shrinks to the judgment items a script cannot catch. This also makes verification scans reproducible across sessions instead of re-invented each batch.

### 8.5 Split the contract from the reference

A small model with a 519-line guide in context attends to maybe a third of it. Restructure as:

1. **WRITING_CONTRACT.md, one page maximum:** the voice target sentence, the five absolutes, the sentence-length bands, the definition and cost-density quotas, and one exemplar passage. This is what sits in context during every writing batch.
2. **The full guide as reference:** consulted when a specific question arises (layer definitions, Code-block format, surrounding-text categories).

The current "Compact Working Prompt" at the end of the guide is the right instinct; it needs the exemplar and the positive quotas added, and it should become its own file so a session can load it without the other 500 lines.

### 8.6 Add the numeric targets

Small models hit numbers better than adjectives. The quotas worth writing down: sentence-length bands per layer (Section 7.3), definition density (one parenthetical per new trade term, first use), cost figures (every procurement or trade discussion names a range and a year), one direct question maximum per section, zero em dashes, zero antithesis constructions. Every one of these is checkable by script, which means every one of them survives a weak writer plus a dumb checker. That combination is the realistic deployment: the style guide should assume the writer is mediocre and make the checklist carry the quality.

## 9. A Sample Of The Revision 6 Target Voice

The septic topic, blending Revision 2's register with Revision 5's structure:

> **Simple**
>
> Before buying rural land, find out whether it can support a septic system (the buried system that treats wastewater when there is no city sewer). Some soils drain too slowly, some drain too fast, and some parcels cannot support any system at all. A parcel that fails has no legal way to become a home, no matter how good it looks.
>
> **Applied**
>
> Order a site evaluation before closing, and make the purchase offer contingent on the result.
>
> 1. Hire a licensed evaluator through the county or DEQ list. Cost: roughly $500-$1,200 (2026).
> 2. The evaluator digs test pits and classifies the soil.
> 3. Read the result for system type, not just pass/fail. A standard system runs about $8,000-$15,000. An alternative system for poor soil runs $20,000-$50,000. That difference should change your offer.
> 4. Save the evaluation report in the project binder. The septic permit will reference it.
>
> **Code**
>
> ```
> OAR 340-071: Oregon onsite wastewater rules, DEQ administered, often delegated to county health.
>   - Site evaluation procedure, system permit, installation inspection, certificate of satisfactory completion.
> ```

Every sentence is literal. Nothing performs. The stakes ($42,000 of possible difference, an unbuildable parcel) supply the excitement, and they were sitting in Revision 2 the whole time.
