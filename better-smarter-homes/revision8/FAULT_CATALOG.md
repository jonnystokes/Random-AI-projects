# The Fault Catalog (Revision 8)

Created 2026-10-26 from the owner-supplied catalog in revision7/PROBLEMS_AND_GOALS.md (the
twenty-two faults, Tiers 1 to 3, reproduced unchanged) plus a fourth tier for the faults the two
reviews of 2026-10-26 found in the finished Revision 7 chapters. This catalog is the project's
shared vocabulary. A writer or reviewer names a fault by its number and name. A violation of any
item is an error of the same severity as a wrong code citation: it is fixed, not weighed against
readability.

The writing rules that prevent these faults are in STYLE_GUIDE.md. The lint in tools/lint.py
catches the pattern-shaped ones; the rest are caught by reading.

**The one-paragraph history.** Revision 2 was a plain, friendly, specific manual with weak code
depth. Revision 4 deleted half the book and replaced the loss with rhetorical performance.
Revision 5 rebuilt the technical content and drifted into long-sentence committee prose.
Revision 6 killed the performance and wrote the book as pure instruction and fact, under a
four-layer system, with the catalog below as its law. Revision 7 kept that law and finished
thirteen chapters to it. Two independent reviews on 2026-10-26 found the result free of the old
faults and full of new ones: the voice of a specification written under a gag order. Flat,
impersonal, narrating its own research, handing every risk to the engineer, every chapter the
same shape, and the explanation layer forbidden to explain. Revision 8 keeps the substance, the
sources and the four layers, and corrects the voice. Tier 4 names what it corrects.

## The Complete Catalog Of Writing Problems (Canonical Reference)

Added 2026-07-12 (owner-supplied). This is the authoritative, technically-termed catalog of every writing problem identified across all revision cycles, ordered most to least obnoxious. Each entry names the problem, defines it with the technical terminology the project uses, gives the canonical example from the text, states why it is obnoxious, and states the resolution. This terminology is the shared vocabulary: use these names when flagging or fixing a fault. The lint battery and judgment checks in `writing_style_guide.md` enforce these; this catalog is the reasoning behind them.

### Tier 1: Structural Register Violations

These broke the document's identity as a technical specification by importing the wrong genre's conventions.

**1. Gnomic Declarative (Aphoristic Wisdom Claim).** A sentence that asserts a timeless, universal truth about the world in a form that sounds like a proverb, rather than stating a verifiable claim or a deontic requirement. Operates in the alethic mode (necessary truths) when the document requires the deontic mode (obligations, permissions) or the declarative-factual mode. *Example:* "A house is the sum of thousands of small decisions." *Why obnoxious:* it performs gravitas instead of delivering information; it cannot be verified, tested, or acted upon; it signals a design manifesto rather than a construction manual. *Resolution:* functional claims that state what the document does, not what a house is. "This book records them, with their reasons, because recorded decisions can be built, inspected, and repaired by people other than the person who made them."

**2. Theatrical Vignette (Compressed Narrative Ellipsis).** A sentence that stages a hypothetical future scene with the reader as protagonist, implying a document property by showing the reader in a pleasant scenario rather than stating the property directly. Relies on conversational implicature rather than assertion. *Example:* "You can hand one chapter to a contractor or an inspector and have a useful conversation. You can look up a single decision years from now without rereading the rest." *Why obnoxious:* back-cover blurb language; offers the emotional payoff of easy retrieval without naming the mechanism; "hand" is an affective verb performing intimacy; "years from now" is scene-setting, not a verifiable property. *Resolution:* document-property claims that name the mechanism. "Each chapter is self-contained. Cross-references use topic names, and the code lookup appendix and the glossary list individual topics for direct lookup."

**3. Metaphoric Overextension (Conceptual Metaphor System Drift).** The persistent use of verbs and nouns from a single metaphorical domain — typically physical transport and containment — to describe information relationships, creating an implicit model of the document as a physical object moved through space rather than a structured data store presenting information. *Examples:* "Every chapter that touches a regulated system carries the controlling code sections"; "No two layers carry the same content"; "The chapter's code citations, tolerances, and records requirements travel with it"; "This book has four jobs." *Why obnoxious:* it is not one sentence but the underlying metaphor system generating dozens of problematic sentences; "carry," "touch," "travel," "jobs" are verbs of motion, contact, transport, and employment applied to text; the document is a structured data store, not a person, vehicle, or worker; the metaphor system is fundamentally at odds with the specification register. *Resolution:* verbs of containment, listing, and presentation. "Every chapter about a regulated system lists the controlling code sections." "No two layers contain the same information." "Each chapter includes the code citations." "This book serves four functions."

**4. Rhetorical Schemes as Decorative Devices.** Classical figures of speech — chiasmus, isocolon, antithesis, anaphora used for rhythmic effect — whose primary function is aesthetic balance rather than denotational transfer. The sentence sounds quotable; information density per word is low. *Examples:* "A cheap choice that causes hidden long-term damage is not cheap. An expensive choice that protects the shell for decades may be the cheaper choice over time." (chiasmus + antithesis); "build the shell so it can stay, and route the service systems so they can change" (isocolon); "Internet improves the house. Internet does not run the house." (isocolon + antithesis); "Concrete tolerates compressive load. It tolerates differential movement poorly." (isocolon + antithesis). *Why obnoxious:* these are poetry, prioritizing euphonic balance over denotational precision; a contractor cannot extract an action, a value, or a constraint. *The test:* can the sentence be replaced with a declarative that conveys the same technical content in fewer words with more precision? If yes, the scheme was decoration. *Resolution:* direct declaratives. "Cost comparisons span the full service life: a hundred-year component is compared against five twenty-year replacements, at the same total horizon." "Design the structural shell for permanence. Route service systems for replacement access."

**5. Personification.** Attributing human qualities, actions, or agency to inanimate objects, materials, assemblies, or documents; includes biological metaphors applied to non-living systems. *Examples:* "A section gets a supporting element only when it earns its place." (section as person earning a right); "The binder is the house's instructions for its future self." (house as person with a self); "Electronics in the house die of abandonment, not exhaustion." (electronics as living things that die); "Adding thickness elsewhere does not compensate for the gap." (thickness as agent that compensates). *Why obnoxious:* the most persistent vestige of the old register; it sneaks in when the text reaches for accessible language in the `Simple` layer; it anthropomorphizes the building, the document, and the materials, creating an implicit narrative where none belongs. *Resolution:* statements of physical fact. "A supporting element is included where a section requires comparison data." "The binder is the reference for future occupants and contractors." "Electronics become obsolete when the manufacturer stops supporting them, not when the hardware wears out." "Adding thickness elsewhere does not close a gap in a control layer."

### Tier 2: Semantic And Syntactic Problems

Problems within individual sentences that create ambiguity, category errors, or unnecessary abstraction.

**6. Patient-Verb Agreement Failure Under Conjunction Reduction (Zeugma Without Intent).** Conjoining multiple verbs under a shared subject where each verb selects for a different semantic patient (ontological category of object), forcing the reader to silently reinterpret the subject for each verb. Distinguished from intentional zeugma (a figure of speech) by being unintentional and confusing. *Example:* "Recorded decisions can be built, inspected, and repaired by people other than the person who made them." *Why obnoxious:* it crosses an ontological boundary without signalling the transition; decisions can be recorded, reviewed, revised, documented, communicated, but not built, inspected, or repaired — the physical work is what gets built; the sentence collapses the precondition (the recorded decision) and the work product (the construction) into one noun phrase, then applies the predicates of the work product to the precondition. *Resolution:* split the predicates and supply the missing patient. "The record is what makes the work transferable. With the decision and its reason written down, a contractor can build what the decision specifies without meeting the person who decided it. An inspector can check the built work against the written specification instead of against someone's memory. Years later, whoever makes a repair can follow the original reasoning."

**7. Periphrastic Circumlocution (Hedged Predicates).** Multiple words where fewer would do, often combined with epistemic hedging that declines to assert what the sentence appears to assert. The text watches itself talk. *Examples:* "Informally, the target is a thousand-year shell."; "Not every detail will literally last that long."; "may be the cheaper choice over time"; "The point is that". *Why obnoxious:* it undermines authority; "informally" signals that what follows is not a real specification; "literally" is a colloquial intensifier, not a technical qualifier; "may be" declines to assert; "the point is that" is metadiscursive self-commentary. *Resolution:* direct assertions. "The project's named goal is a thousand-year structural shell. The operational definition: every structural decision is evaluated against a multi-century service life." If a claim cannot be made without hedging, it is removed, not hedged.

**8. Semantic Bleaching Through Abstract Nominalization.** Replacing concrete referents with abstract nouns derived from verbs or adjectives, creating evaluative language that gestures toward a material fact without stating it. *Example:* "The long-life target is the part of the house that is difficult or destructive to replace." *Why obnoxious:* "target" is a metaphor; "difficult or destructive to replace" is a judgment, not a specification; the sentence gestures toward a material fact (concrete is hard to demolish) but wraps it in evaluative language that softens the claim; a specification would say which components have which design service lives. *Resolution:* "The long-life requirement applies to the components that are difficult or destructive to replace: the foundation, the structural concrete and reinforced masonry, the major load path from roof to foundation to soil, and the envelope assemblies that protect the structural shell from water, vapor, and freeze-thaw cycles."

**9. Contrastive Negation (Dialogic Trace).** Negating something not asserted in the prior sentence, implying an expected default that the text is rejecting. The negation performs identity ("we are not like those other houses") rather than conveying specification. *Example:* "There is no wood framing in the structural system." *Why obnoxious:* the text argues with an imagined interlocutor; the specification should state the materials positively and let the absence of wood be implicit unless the exclusion has regulatory consequences that need flagging. *Resolution:* recast as a positive specification with functional justification. "The structural system contains no wood framing; this exclusion determines the code path, the fire behavior, and the engineering requirements throughout the book."

**10. Scalar Implicatures Without Anchored Referents.** Unanchored comparative adjectives that imply a scale without stating the reference point, value, or range. *Examples:* "Overbuilding these costs little during the build. Fixing them afterward costs a lot."; "Most parts of a house wear out sooner by design." *Why obnoxious:* "little" relative to what budget? "a lot" relative to what threshold? "sooner" than what? The reader cannot act on a scalar implicature without knowing what it scales against. *Resolution:* numerical ranges or ratios. "The added cost during construction is a fraction of the correction cost after burial or loading." "The following components have design service lives shorter than the structural shell."

### Tier 3: Register And Consistency Problems

Milder problems that create local tonal friction or ambiguity without breaking the document's identity.

**11. Modal Ambiguity (Passive-Aggressive Deontics).** Stating requirements in a grammatical form that hovers between declarative and imperative, creating uncertainty about whether the text describes what will happen, states a design rule, or issues a specification. *Example:* "Service systems carry the opposite requirement: routed for access, labeled for identification..." *Why obnoxious:* normative ventriloquism — the text attributes the requirement to an abstract entity ("the requirement") rather than stating who requires what. *Resolution:* imperative mood with concrete verbs and clear agents. "Route all service systems for access. Label all service components for identification by a future owner."

**12. Deontic Hedge.** Stating a requirement in a form that grants permission rather than imposing an obligation, using "may" where "must" or an imperative is appropriate. *Example:* "A system may be only as complicated as the work requires." *Why obnoxious:* it sounds like a compromise negotiated with a complexity-loving adversary; the principle is simplicity and the expression should be a constraint. *Resolution:* "Add complexity only when a simpler system cannot meet the requirement."

**13. Promotional Peritext (Blurb Language).** Copy that belongs on a back cover or product page, addressing the reader's purchase anxiety rather than specifying a document property. *Example:* "You can hand one chapter to a contractor or an inspector and have a useful conversation." *Why obnoxious:* it sells the book rather than describing it; it offers a social outcome ("useful conversation") without establishing the causal mechanism. *Resolution:* state the document property that enables the outcome. "Each chapter includes the code citations, tolerances, and records requirements for its system, so a subcontractor, engineer, or inspector can work from that chapter alone."

**14. Rhetorical Question as Self-Check.** An instruction to the reader to perform a mental exercise, addressed to the reader's thought process rather than stating a requirement. *Example:* "For each load, ask: where does it go next? If the answer is not obvious from the drawings, the design is not ready." *Why obnoxious:* a pedagogical device in a document that otherwise states requirements; the surrounding prose is declarative while this sentence addresses the reader's internal monologue. *Resolution:* "Trace each load from its point of application to the foundation. If the path is not shown on the drawings, the design is incomplete."

**15. Evaluative Adjectives Performing Value Judgments.** Adjectives that express the author's assessment of a material, system, or design choice rather than stating a measurable property. *Examples:* "The fragile layer is buried under the durable ones." (PMR roof); "The concrete deck underneath is untouched."; "The equipment can run gently and steadily." *Why obnoxious:* the text performs enthusiasm for the design choice; "fragile" and "durable" are relative judgments; "gently" is an anthropomorphic adverb; "untouched" implies a benefit without stating it. *Resolution:* state material properties and design outcomes without value-judgment adjectives. "The membrane is protected from UV, foot traffic, and impact by the insulation and ballast above it. When the membrane reaches the end of its service life, the ballast and insulation are removed, the membrane is replaced, and the concrete deck requires no repair."

**16. Explanatory Analogy.** Comparing a building system to an unrelated consumer product or everyday object to explain its function, rather than stating the physics directly. *Example:* "A thermos bottle keeps coffee hot because an insulating wall wraps the metal liner, with the liner on the inside. This wall repeats that arrangement." *Why obnoxious:* a teaching move for a classroom, not a specification; it introduces a second object the reader must hold in mind, then maps properties from the familiar object to the unfamiliar assembly; the physics can be stated directly. *Resolution:* "Placing insulation outside the structural wall keeps the concrete at conditioned temperature. Placing insulation inside the wall exposes the concrete to outdoor temperature cycles and loses the thermal-mass benefit."

**17. Admonitory Declarative (Proverb-Form Claim).** A sentence that states a truth about building physics in a form that sounds like earned wisdom, typically with a "No X does Y" or "X is not Y" structure echoing proverbial syntax. *Example:* "No thickness of material elsewhere compensates for the gap." *Why obnoxious:* structurally a wisdom claim — the form signals "a lesson learned from experience" rather than "a physical fact"; the content is correct physics but the form must match the specification register. *Resolution:* "A gap in a control layer is a discontinuity. Adding thickness elsewhere does not close a gap in a control layer."

**18. Copular Identity Slogan.** A sentence using the copula "is" to collapse a complex relationship into an equation, prioritizing pithiness over precision. *Example:* "This book is the plan." *Why obnoxious:* the book is not the plan; it documents the plan; the slogan is memorable at the cost of accuracy. *Resolution:* "This book documents the plan." (Kept in the final text at the author's instruction as a personal framing device; this is the sole owner-protected exception, listed in the style guide's Owner's Voice section.)

**19. Metadiscursive Self-Commentary.** The text commenting on its own structure, purpose, or stylistic choices rather than performing its function. *Examples:* "The point is that..."; "What this means is..."; "Its verbs are physical: walk, dig, mark, measure..."; "The project's named goal is...". *Why obnoxious:* the text watches itself talk; a table of contents and headings provide navigation while the body text provides content; the text should not explain what it is doing while doing it. *Resolution:* remove the commentary and let the content stand. "The structural shell is designed for a thousand-year service life. The operational criterion: every structural decision is evaluated against a multi-century horizon."

**20. Format Drift (Code Block Structure).** Deviation from the established three-part `Code` block format (requirement statement, exact limit or value, source citation) within a chapter or across chapters. *Example:* a bulleted reference-list format instead of the three-part rule statement (chapter 8, earlier revision). *Why obnoxious:* it breaks internal consistency; a reader who learns the format in chapter 1 expects it throughout, and a different format forces re-learning how to read `Code` blocks. *Resolution:* enforce the three-part format uniformly across all chapters. (Companion rule, seventh review: a `Code` block requires at least one statute, rule, or consensus-standard source; guidance-only blocks fold into `Professional`.)

**21. Section-Numbering Duplication.** Two distinct topics carrying the same section number, usually from a copy-paste or reorganization artifact. *Example:* vapor control and window/door installation both labeled section 8.10 (chapter 8, earlier revision). *Why obnoxious:* it breaks the cross-reference system — "see section 8.10" becomes ambiguous and the table of contents becomes unreliable. *Resolution:* assign unique section numbers to distinct topics.

**22. Missing `Simple` Block.** A section that jumps directly from a heading to a `Professional` block without a `Simple` layer, where the topic's complexity or the surrounding structure suggests one would help. *Example:* section 21.5 (Entity, Tax, And Insurance) had no `Simple` block. *Why obnoxious:* mild; the four-layer system permits omitting layers, but a dense `Professional` block on entity structure and tax treatment benefits from a one-sentence `Simple` orientation. *Resolution:* add a `Simple` block, or confirm the omission is intentional per the layer rules. (Seventh-review standing rule: every dense reference table and every all-`Professional` section gets a two-or-three-sentence `Simple` orientation block.)


### Tier 4: Revision 7 Faults (found 2026-10-26)

These did not exist in the earlier revisions because the earlier revisions had the opposite
problem. They are the faults of a text written to satisfy Tiers 1 to 3 and nothing else. Counts
are from the 27 written chapters of Revision 7, about 200,000 words of prose.

**23. Research Narration (Provenance Leak).** A sentence that reports the state of the writer's
research instead of stating the fact or the instruction. *Examples:* "No published number fixes
the sit-time window." "The project research confirmed these principles only from publisher and
review summaries." "No built Oregon precedent for any of the three forms was identified." 183
instances. *Why obnoxious:* the reader is handed the writer's notebook; it marks the text as
assembled from a research pass; it buries the usable instruction under the history of looking
for it. *Resolution:* state what is known and what to do. "Set the sit-time window by
observation and record it in the production log." A gap the reader must know about goes to the
chapter's Open items list, in its three-field format, never into the body.

**24. Delegation Ending (Hand-off Cadence).** Paragraph after paragraph closing on the same
move: "the engineer of record decides", "the owner confirms with the building department",
"verified before the permit set". *Examples:* "The engineer of record makes the final acceptance
decision." "The applicant confirms the treatment with the building department at a
pre-application meeting before the floor plan is fixed." 91 paragraphs end this way; "confirm"
and "verify" appear about 570 times. *Why obnoxious:* a template beat; the book reads as
liability text; the reader loses track of who decides what because everything is delegated
everywhere. *Resolution:* one "Who decides what" table per chapter. The body states the fact and
moves on. A hand-off sentence appears only where the reader must act.

**25. Encyclopedia Paragraphing (Bold Run-in Runs).** Pages of paragraphs that each open with a
bold topic and a period and connect to nothing. *Examples:* "**Cantilevers.** Reinforced concrete
permits..." "**Point loads.** A masonry heater..." "**Sulfur concrete.** Elemental sulfur is
melted..." 279 such paragraphs in the Revision 7 chapters, in runs of five to twelve. *Why
obnoxious:* it is a knowledge base dumped into a chapter; nothing tells the reader what matters,
what comes first, or how the items relate; it is the shape generated text takes when it has a
list of findings and no argument. *Resolution:* a subheading in sentence case with prose under
it, or a comparison table where the items are parallel options. At most two consecutive run-in
paragraphs anywhere.

**26. Colon Fragment (Slide Syntax).** A noun phrase, a colon, and the content, with the verb
left for the reader to supply. *Examples:* "The operational definition: every structural
decision is evaluated against a multi-century service life." "Project rule: non-chloride
wherever steel is present." "The documented detail has three parts:" 182 instances. *Why
obnoxious:* presentation-deck syntax; it reads as bullet points written across the page; it is
one of the most reliable signatures of generated prose. *Resolution:* write the verb. "Every
structural decision is evaluated against a multi-century service life." A colon introduces a
list or a quotation and nothing else.

**27. Self-Description Opener.** A chapter that opens by describing itself: "This chapter
specifies the assembly of the exterior wall: what gets built, in what order... It contains:"
followed by a list of seven to thirteen items, then a paragraph routing the reader to four other
chapters. Every written chapter in Revision 7 opens this way; "this chapter" appears 205 times
in the book. *Why obnoxious:* the book talks about itself before it talks about the house; the
identical shape across thirty-six chapters is the strongest single template signal in the
manuscript; the reader learns nothing in the first two hundred words. *Resolution:* open with
the decision, number or fact that matters most. State scope as facts about the house. Related
material is named once, by topic, where the reader needs it.

**28. Layer Echo.** The Professional block restating the numbers the Code block below it
states. *Example:* the escape-opening section of the interiors chapter gives 5.7 square feet, 24
inches, 20 inches and the 44-inch sill in Professional and again in Code. *Why obnoxious:* it
breaks the book's own rule that no two layers contain the same information; the reader reads
the fact twice and learns nothing the second time; it is the sign of a writer filling a quota
of labels. *Resolution:* Professional states the mechanism and the reason the value is what it
is (a firefighter in gear, a person crawling out, a child who should not need a chair). Code
states the value and the source.

**29. Label Drought.** Sections with no Simple block; chapters with ten thousand words and no
Applied or Professional labels. *Example:* What Concrete Uniquely Enables has eleven Simple
blocks, zero Applied, zero Professional, and about ten thousand words of unlabeled prose in the
Professional register. *Why obnoxious:* it breaks the reading paths chapter 1 promises; the
non-builder has nowhere to go after the first paragraph of each section; the builder has no
action list; the layer filter in the reader has nothing to filter. *Resolution:* every section
has a Simple block. Procedural content is labeled Applied. Parameters and limits are labeled
Professional. Freeform prose is confined to the opening, Jon's note, and short bridges.

**30. Gloss Cadence.** A parenthetical definition every 150 to 200 words, in the same shape, with
the same terms re-glossed in chapter after chapter. *Examples:* "the bond beam (the reinforced,
grouted top course that ties the wall together)" defined five times across the book; "a wythe
(one vertical thickness of masonry)". Five to seven glosses per thousand words. *Why
obnoxious:* a uniform tic that interrupts every paragraph; the reader who knows the term is
slowed and the reader who does not is told once per chapter anyway. *Resolution:* define a term
once per chapter at first use, in the Simple block where possible; the glossary carries the
rest; a Professional block uses the trade term without a gloss.

**31. Date Stamping.** "(2026)" after every dollar figure, 78 times; "as of July 2026" in body
text. *Why obnoxious:* noise at that density; a book that time-stamps every number reads as a
report, and the report date will be wrong the day after it is printed. *Resolution:* the cost
year stated once per chapter, near the first cost ("Costs in this chapter are 2026 figures
unless a different year is given"); a different year marked only where it differs; adoption and
edition dates stated as facts where the value depends on them.

**32. Machine Title Case.** Every word of a heading capitalized, including "To", "And", "Of" and
"The". *Examples:* "The Wall System, Foundation To Roofline"; "Site-To-SDC Matrix"; "What The
Wall Must Do". *Why obnoxious:* no human typographer sets headings this way; it reads as
generated at a glance, before a word is read. *Resolution:* section headings in sentence case;
chapter titles in title case with articles, conjunctions and short prepositions lowercase.

**33. Cross-Reference Pile.** Four or more chapters named in one paragraph, each with "the X
chapter contains...". *Example:* the land chapter's opening names the soil, legal, water
independence and site-development chapters in four consecutive sentences before its first
section. *Why obnoxious:* a routing table written as prose; the reader is sent away before being
told anything. *Resolution:* at most one cross-reference sentence per section, placed where the
reader needs it, by topic name.

**34. Determiner Monotony.** Thirty percent of sentences open with "The" or "A"; "It is", "This
is", "That is", "There are" as openers; sentence after sentence of subject-verb-object
declaratives of the same length. *Why obnoxious:* the flat beat of a specification; the reader
hears the pattern instead of the content; Version 2 names it under The AI Cadence. *Resolution:*
lead with the condition ("When the first course is level..."), the actor, the place, the number,
or in Applied the verb. Keep "The" and "A" openers under 18 percent of a chapter's sentences.
Vary sentence length by the information.

**35. The Missing Human.** The first person appears once in 265,000 words, in the first
sentence, and never again; no reason is ever given as a person's reason; every choice is stated
as an institutional fact. *Why obnoxious:* a personal plan with no person in it reads as
generated, because it was; the family reader has no one to listen to; the owner's actual
reasons, which are the most transferable thing in the book, are absent. *Resolution:* Jon's note
in every chapter, first person, drafted from the record and marked [JON] where only he can
confirm, protected once he has.

### Tier 5: Revision 8 Loop Faults (found 2026-10-26, chapters 2 and 3)

These appeared in chapters written to the Revision 8 brief, after Tiers 1 to 4 were banned. They
are finer-grained than Tier 4 because the coarse faults were gone. Counts are from chapter 3
(23,800 words, 80 Code entries) unless stated.

**36. Pointer Entry.** A Code entry whose value line points at a body of law instead of stating a
rule. *Examples:* "Counties zone rural land under state framework law. / County comprehensive
plans and zoning... all sit under one chapter of statute. / Source: ORS chapter 215." "Timber
harvest and riparian work follow the forest practice rules. / Source: OAR chapter 629." 13 of 80
entries. *Why obnoxious:* it pads the Code layer with entries no inspector could check; it dresses
a cross-reference as a requirement. *Resolution:* one Professional sentence with the citation in
it. A Code entry has a number, a date, a named condition or a yes or no, read from the rule's own
text.

**37. Source-Class Attribution.** A figure hung on an anonymous class of sources: "secondary
sources report", "industry sources", "general homesteading guidance", "documented examples",
"independent-agent reporting", "in the published cases"; and its cousin, the anonymized specific:
"at least one county", "at least one investor-owned utility". 11 and 2 instances. *Why
obnoxious:* research narration in a new coat; the reader is told that someone somewhere said it; a
named source would be checkable and an unnamed one is decoration. *Resolution:* name the source in
the sentence, or state the figure as a planning figure and carry the doubt in Open items; name the
county or the utility the source names.

**38. Hedged Range.** "about", "roughly" or "approximately" before a range: "roughly $600 to
$2,700", "about $733 to $2,333 per acre". 29 hedges before numbers, most before ranges. *Why
obnoxious:* a range is already approximate; the doubled hedge is the writer flinching twice, and
with false precision ("$2,333", "$44,535", "$3,993 across 21 listings") it reads as a machine
summarizing a spreadsheet. *Resolution:* cut the hedge before any range; round planning figures
from guides and listings to two significant figures; exact figures are for fees, statutory limits,
test results and quotes.

**39. Instruction Close.** A Simple block that ends on what the reader does rather than on a fact:
"You read it in full, with the documents it points to, before the title contingency expires." "You
price the change before the offer, from a walk on the ground after rain." 8 of 21 Simple blocks.
*Why obnoxious:* the imperative ban evaded with a second-person declarative; the same closing beat
block after block; Applied's job done twice. *Resolution:* Simple ends on the fact about the land or
the house; the action lives in Applied.

**40. Refrain.** A phrase that is the chapter's thesis repeated until it is a tic: "in writing" 23
times, "before the offer" 19, "before closing" 12, "a clean result is only a screen" 6. *Why
obnoxious:* the reader hears the drum instead of the content; it is how a model keeps a theme alive
without an argument. *Resolution:* the opening says it; the body says it at most three more times,
where the stake is highest; elsewhere the fact stands without the tag.

**41. Inventory Sentence.** Six to nine nouns strung on commas as a sentence: "Distance affects
labor productivity, subcontractor willingness, delivery cost, inspection scheduling, emergency
response, utility options, the resale pool and owner fatigue." "Water feasibility joins the same
plan with well yield, pump curve, static level, drawdown, storage, treatment, pressure, freeze
protection and backup power." About twelve. *Why obnoxious:* a bulleted list with the bullets
removed; nothing in it is ranked or related; the reader cannot hold it. *Resolution:* four items
at most in prose; longer lists go in a table or bullets, or are cut to the ones that matter here.

**42. Abstract Thesis Opener.** A Professional paragraph that opens by equating two abstractions:
"Septic feasibility is a layout problem." "Utility feasibility sets early geometry." "Title review
and site feasibility are one exercise." "Resource-zone dwelling restrictions reach underwriting
through buildability." "Fixed-and-free comes first, and paid-and-slow starts in parallel." *Why
obnoxious:* a slide title; nothing a person could watch happen; compression that reads as
cleverness and conveys nothing until the next sentence explains it. *Resolution:* open with the
thing and what it does: "The drainfield, its reserve area, the well and the house have to fit on
one plan with the setbacks between them."

**43. Count Drift.** A number stated in prose that disagrees with the list it describes, or with
itself elsewhere: "Five conditions end a land purchase" in the opening and "Six items can end the
purchase" in the closing section; "six hazards" over a seven-row table. *Why obnoxious:* the
reader counts, finds the mismatch, and stops trusting the numbers that matter. *Resolution:* every
count in prose is checked against its list before the section is saved and used identically
through the chapter.

**44. Meta-Pointer.** Self-description that avoids the banned words: "What follows is the
screening a parcel passes..." "Below is the purchase on one page..." "Nothing here is new, because
each item is stated in full in an earlier section." "The order above follows from..." "Step 2
catches..." *Why obnoxious:* item 27 by another route; the book narrating its own layout.
*Resolution:* state the fact; the only allowed pointers are to furniture on the same page ("the
table below").

**45. Marker Wall.** A Jon's note with "[JON: confirm]" after every sentence, nine in a row. *Why
obnoxious:* the note stops being a voice and becomes a form; the one specific question in it
("which counties?") is lost among eight rubber stamps. *Resolution:* when the whole note is
inferred, one marker at the head; inline markers only for specific questions.

**46. Orphan Fact and Stray History.** A true sentence appended where it follows from nothing (a
permit portal at the end of a list of truck-access checks; neighbor water-sharing closing the
water-rights section), and history that changes nothing the reader does (a company's 2020 land
trades, an agency's 1977 price reports, a regional pilot that ended without result). *Why
obnoxious:* preserve-and-grow leftovers; the reader feels the seam and reads a report. *Resolution:*
give the fact its own place (a table row, a short paragraph under a subheading) or drop it and list
it under Dropped; history earns a clause only when it explains a rule the reader must follow.

### Summary By Frequency

Across all revision cycles, the most persistent faults by how often they appeared:

1. **Personification** (Tier 1, item 5): in every chapter's early drafts through Revision 6, most stubborn in Simple layers.
2. **Metaphoric overextension** (item 3): the "carry, touch, travel, jobs" verb family, pervasive before Revision 6.
3. **Research narration** (item 23): 183 instances in the finished Revision 7 chapters.
4. **Encyclopedia paragraphing** (item 25): 279 run-in paragraphs in the Revision 7 chapters.
5. **Colon fragments** (item 26): 182 instances.
6. **Delegation endings** (item 24): 91 paragraph endings.
7. **Self-description openers** (item 27): every chapter.
8. **Gnomic declaratives** (item 1): concentrated in chapter 1, excised early.
9. **Rhetorical schemes** (item 4): chapter 1 principles and structural descriptions, excised in Revision 6.
10. **Layer echo** (item 28) and **label drought** (item 29): the carryover chapters and the new Revision 7 chapters respectively.
