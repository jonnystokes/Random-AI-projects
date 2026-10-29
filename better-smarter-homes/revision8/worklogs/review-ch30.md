# Review: chapter 30, The Owner-Builder's Body and Mind

Reviewer sub-agent for the orchestrator, 2026-10-28, 5:45 PM (Pacific). Chapter written under
WRITER_BRIEF.md v3 (skeleton chapter; Opus, then Fable from 9:45 PM 2026-10-27). Judged against
REVIEW_CHECKLIST.md and the v4 brief. The chapter was read in full, start to finish, before any
judgment. No file other than this one was written.

## Summary

- Words: Revision 7 383 (skeleton) -> 14,941 (lint count; 12,124 prose words in stats.py).
- Sections: 10 skeleton headings -> 16 sections, 0 subheadings. Labels S/A/P/C 16/16/14/6.
- Code entries: 16 (30.1: 1, 30.5: 2, 30.6: 2, 30.9: 1, 30.10: 3, 30.11: 7), all three-part.
- Open items: 19 plus the Dropped bullet. Who decides: 16 rows. Decisions: 23. Records: 14.
- Research: 22 new findings plus a corrections entry; 3 cross-chapter flags.
- Lint: PASS, 0 FAIL, 2 WARN (30.14 has two cross-reference sentences; 7-word runs are
  repeated chapter titles, a lint quirk).
- Stats: average sentence 16.6; The/A/An openers 9.6 percent; Simple 14.4, Applied 14.3,
  Professional 19.9 (25 percent of Professional sentences over 25 words); 30+ word sentences 6.9
  percent. Most common two-word openers include "one is" (3), "another is" (2), "the third" (2).
- Verdict: **ITERATE.** The v3 rules held on the technical sections (30.2, 30.5, 30.6, 30.10,
  30.11 are strong: rule texts read from the source, arithmetic right, corrections to the answer
  file). The health and mind sections (30.4, 30.7, 30.8, 30.12 to 30.14) show three patterns v4
  does not reach: evidence-gap narration, source classes in new wording that hide sources the
  answer file names, and Simple blocks that restate a sourced figure under a different measure.
  A fourth, invented thresholds in health advice, is proposed as a rule. All three v4 patterns
  also appear (the chapter predates v4), which confirms v4.

## 1. Mechanical

**Lint and stats.** As above. Every gate passes. The research-narration gate missed about 20
sentences of the "no study measures" form (finding 1) because its pattern lists exact phrases
("no source documents", "not documented") and the chapter writes "No source gives", "no study
measures", "is documented". The source-class gate missed about 20 (finding 2) for the same reason.

**Anatomy.** Opening, Jon's note, 16 numbered sections with Simple in each, Who decides, Open
items, Decisions, Records. Section numbers contiguous. 30.6 runs 1,022 prose words with no
subheading (template ceiling 900).

**Preservation skim.** The Revision 7 file holds an instruction block, a two-sentence scope line
and ten headings. Every heading topic is present except "material and panel lifts" from
skeleton 30.4 (carts, hoists, gantries and come-alongs are there; no material hoist or panel
lift). The Dropped bullet says "Nothing"; it should name the panel and material lift, or the
chapter should carry one line on them. Minor.

**Spot values (eight plus every dollar figure), against research/answers/ch30_body-and-mind.md
and research/new/ch30.md.**

| Value in chapter | Source | Result |
|---|---|---|
| Lifting example 11.5 kg (25 lb) and 17.2 kg (38 lb), 6.2 kg past an hour | CCOHS multipliers in research/new | Recomputed: 23 x 0.83 x 0.87 x 0.87 x 0.84 x 0.95 = 11.5; 23 x 0.99 x 0.90 x 0.84 = 17.2; 0.45 frequency gives 6.2. Right |
| OR 1.26 per 5,000 kneeling hours; Klussmann 2.16, 2.47, 2.52 | research/new, corrected from the abstracts | Right; the answer file's "peak near 24,500 hours" correctly dropped |
| Exosuit fatigue 50.53 and 27.39 percent | Answer item 27 | Right |
| Vibration times (37 to 8 minutes, 3 h 8 min to 1 h 23 min, 2 h to 37 min) | Directive formula, research/new | Recomputed, right |
| Muff rated 25 at 100 dBA gives 91; 98 dBA gives 89 | OSHA Technical Manual | Right |
| ACS 97.1 minutes rural against 69 national | Answer item 54 | Right in Professional; misused in Simple (finding 3) |
| Heat rule 80/90, 32 ounces, Table 2 rest schedule; smoke 35.5, 200.9, 500.4 | OAR text in research/new | Right |
| SAD 10, 20 to 30, 5 percent | Answer item 64 (Oregon Health News Blog) | Right |
| $206, $299, $350 power buggy; $1,200 and $3,000 to $6,000 exosuits; $30 to $150 come-along; $100 to $400 cart; $50 to $150 trestle; $15 to $40 board | Answer items 24, 26 to 29, 7, 8 | Right |
| $39.99 activation; $119 to $200 WFA; about $1,000 WFR; $26 to $29 tourniquet; $34 to nearly $800 kits; $184.80 kit | Answer items 41, 52, 53, 73 | Right |
| $35 FCC and $15 exam fee | research/new (ARRL) | Right |
| $43.79 plus $17.05 (2024); $25,000 and $4,000 benefit caps | Answer items 66, 67 | Right |
| $29 to $54 respirator, $3.50 to $40 muffs, $3 to $13 glasses | ch27_tools.md item 48 and Tools 27.11 | Right, same as the Tools chapter |
| $20 to $50 knee pads | Answer item 8 | Right |
| "From a $30 bottle-jack rig to an $8,000 open-source press" (30.15) | ch12_blocks_part1.md items 13, 71 | Traces, but the ch30 answer file's own figure ($2,000 to $3,500 for a small hydraulic unit, item 24 and 31) is dropped without a note, and ch12's answers place a bottle-jack rig at CEB scale, below what a full CMU face needs (60+ tons). The row's low end is not a press for this house's block |
| "A glove full of mortar or a wet knee can reach a third-degree burn in two hours" | ch13_masonry.md answer, "third-degree alkali burns after 2 hours of contact" | Traces |

No invented dollar figure. Every Code entry has a Source the code library routes can verify
(CFR via osha.gov and ecfr, OAR via the Secretary of State, ORS via the legislature).

**Obligations.** OBLIGATIONS.md line 76: the silica passage names Masonry Craft for the Table 1
rows. Met (30.5 Applied step 1).

**Counts.** Checked every prose count against its list: three document kinds (30.1), six
multipliers in two threes (30.2), three hazards (30.5), eighteen Table 1 tasks, three pace
setters, three-part stopping rule, three exposure clocks, "two rules and one climate fact"
(30.7), three movements and two exercises (30.8), six emergency-sheet lines, three lone-worker
parts, seven kit items (30.9), three monitoring and three rest-break options (30.11), three
burnout ways and three MBI components (30.12), four named causes (30.13, the table's fifth row
is a different measure, acceptable). All match. Two internal disagreements that are not count
drift but are the same family:

- 30.14 Simple, "Exhaustion and doubt that a week off did not lift are two more", against the
  table row "Detachment or doubt outlasting a month" and 30.12 Applied step 12.
- Check-in intervals: 30.9 Applied step 2 "every one to two hours during roof, scaffold, trench
  and energized work" against 30.10 step 7 "one hour or less for shallower entries" and step 17
  "every hour during roof and scaffold-edge work"; the Decisions line says "one- to two-hour".

**Lint INFO lists.** Most repeated phrase "on site" 7 times, fine. Two inventory sentences by the
lint's count; reading finds five (30.9 Professional, the seven-item kit list after a colon; 30.9
WFA's five topics; 30.11 Professional's five monitoring sources; 30.14 Simple's seven triggers
spread over five sentences; 30.12 Professional's four practices is at the limit). No four-digit
planning figures.

## 2. The reading

**Item 1, opening.** First sentence ("One person does most of the work on this house, over
several years") states the governing fact. Two faults: "The injuries that end such a build come
from one lift, one kneel and one grip, repeated for months until a back, a knee or a wrist is
hurt" is a rhythmic triad and anaphora (fault 4); "Each exposure has a published limit, from ...
the studies of kneeling" overstates, because the kneeling studies give a dose-response, not a
limit (the 5,000-hour hiring step is the writer's, finding 4).

**Item 2, Jon's note.** One header marker and two real questions (check-in contact; age, fitness
and old injuries), which is the v3 form. But the record holds no Jon decision on this subject:
the skeleton gives only "mostly-solo, multi-year". "I will work to the safety rules written for
paid crews", "Anything too heavy for one person moves by machine", "Every working day someone
will know where I am", "When a pain starts sooner each day ... I change the task" are the
chapter's own recommendations (all tagged Jon to confirm in Decisions) voiced as Jon's
commitments. Nothing is invented about his life or feelings, but the note is the writer's plan in
the first person. The same move appears in the notes of the other skeleton chapters (22 "I want
the power to be mine", 24, 25 "I am building for the years when someone here is hurt or older",
27), which the orchestrator passed; see proposal E. The note's first sentence repeats the
opening's.

**Item 3, the Simple path.** The 16 Simple blocks tell the story in order (rules, lifting,
machines, knees, lungs, ears, pacing, conditioning, check-ins, solo limits, weather, mind,
family, hiring, costs, problems), and a non-builder can follow them. Point-first holds in every
block. The faults are in the medical facts (finding 3) and the closers (finding 6).

**Item 4, Applied.** Mostly executable tomorrow: staging heights, the lifting worksheet, trigger
minutes, the emergency sheet, the heat and smoke steps. Gaps:

- 30.3 step 8 "Keep it if the fatigue log improves": no fatigue log is defined; the body log
  (30.1 step 2) records kneeling hours, trigger minutes, warning signs and check-ins.
- 30.9 step 11 "Do not count on a watch's fall detection" and 30.14 step 10 "Do not plan on the
  USDA mutual self-help housing program" are conclusions, not actions; both belong in
  Professional, which already states them.
- 30.11 steps 14 and 16 conflict: at 35.5 micrograms the day's work moves indoors or is
  rescheduled, so step 16 (N95 for outdoor work at 200.9) has no outdoor work to govern. 30.11
  step 12 starts the smoke watch in July; the 30.7 calendar starts the smoke window in August.
- 30.10 step 16 "Rig it so you can regain the roof or a ladder unaided" has no method; the Open
  item admits it.
- 30.7 steps 11 and 12 and the 30.12 steps 11 and 12 thresholds (finding 4).

**Item 5, Professional.** Mechanism-first and engineer-checkable in 30.2, 30.5, 30.6, 30.10 and
30.11 (the NRR arithmetic, the A(8) scaling, the STD 03-11-002 reading, the AQI breakpoint shift
are the best things in the chapter). In 30.7, 30.8, 30.12 and 30.13 Professional becomes a
literature summary of practitioner blogs and forums, where most sentences are either a source
class (finding 2) or a grade of the evidence (finding 1). Analogy outside Simple: "rather than an
emptying tank" (30.12). Personification and aphorism: "On rough ground the tire decides the cart,
not the frame" (30.3 Professional opener, faults 4, 5, 42). Register: "Next up is the come-along"
(30.3); "owning is the clear call" (30.10). Generic "he": 30.1 "OSHA cannot require him",
"against his own week"; 30.10 "rigging that lets him regain a surface"; 30.14 "valued as he
chooses" (v4 rule).

**Item 6, Code.** Three parts every time, sourced, editions where they matter (heat and smoke
effective dates). Three problems:

- 30.1 Code: "An employer is any person with one or more employees ... Source: ORS 654.005(5)".
  ORS 654.005(5)(b) also makes an employer of "any sole proprietor or member of a partnership who
  elects workers' compensation coverage as a subject worker pursuant to ORS 656.128" (read
  2026-10-28 from oregon.public.law/statutes/ors_654.005). The Tools chapter (27.11) states this;
  30.1 Simple's "While you work alone, no inspector can cite you" is untrue for a sole
  proprietor who elects coverage. Factual gap; boundary disagreement.
- 30.5 Code "Respirable silica exposure must stay under the permissible limit ... Source: 29 CFR
  1926.1153(a) and (d)(1)" repeats Tools 27.11's entry ("Exposure outside a listed task stays
  under the permissible exposure limit ... Source: OAR 437-002-1055, 437-002-1056(1) (federal 29
  CFR 1926.1153(d)(1), (d)(2))"), and cites the federal text where the Tools chapter cites the
  Oregon rule that binds in this state plan (v4 pattern 2, written in parallel).
- 30.11 carries seven entries, including the employer-designed Table 1 floor and the written
  acclimatization plan, though the Applied steps use Table 2 and NIOSH's schedule only. Two
  entries the reader does not use.

Echo: the lint's gates pass, but 30.11 Professional restates its Code statements in other units:
"a fifth of the usual exposure on the first day with a fifth added daily" against the Code's "20
percent ... and 20 percent more each day"; "Among the three monitoring options the rule accepts,
the first is regular communication with employees working alone" against the Code's "monitoring
by regular contact with employees working alone or a buddy system or an equivalent" (fault 28;
v2 rule, echo as statements).

**Item 7, shapes.** Section openers vary well. Two repeated moves: (a) counted enumerations,
nine "three X" set-ups ("Three hazards", "This build repeats three movements", "Three things set
that pace", "Three kinds of document", "Three exposure clocks", "Three independent components",
"Three rest-break options", "three separate ways", "Two rules and one climate fact"), with the
anaphoric "One is ... Another is ... The third is ..." in 30.7 and 30.12 Simple and the disguised
seven-item list in 30.14 Simple ("is one. So is ... counts too ... are two more. Age is
another."), the counted-abstraction defect of the general guide and the four-item rule evaded by
splitting a list across sentences; (b) Simple closers built to land (finding 6). No bold run-ins,
no colon fragments, no delegation endings.

**Item 8, flow and order.** Decision order is sound: jurisdiction, then each body system, then
pacing, then solo safety, then the mind, then hiring, costs and problems. Conditioning (30.8)
starts "eight weeks or more before groundbreaking" and could sit before lifting, a small call.
Orphans: 30.4 "Obesity in that study carried odds ratios up to 17.65 in women and 12.56 in men"
(no consequence drawn); 30.12's BuildHub paragraph ("one builder describes approaching a
breakdown after two years ... Its members treat the stress as a normal feature of the work"),
an anecdote with no action (faults 2, 46).

**Item 9, boundaries.** Three claims checked:

1. Silica and respirators, Tools 27.11 (Revision 8). Same numbers (P100 99.97, N95 95, APF 10,
   PEL 50, 25 trigger), dry batching unlisted in both. Disagreements: the duplicated PEL entry
   and its federal-only Source (above); 27.11 names this chapter for respirator selection and fit
   checks, but 30.5 names Masonry Craft and Owner-Made Blocks at the silica overlap and never the
   Tools chapter (only in 30.15, for prices). ORS 654.005(5) read differently (above).
2. Build Sequence 29 (Revision 7 text). Solo multiplier 2 to 4 times and first attempts at half
   again: same as 29's "roughly two to four times" and "about 1.5". Trench protective system at
   5 feet: same as 29.7; 30.10 names the chapter for the trench rules. 30.1 Code repeats 29's
   ORS 654.005 entry (29 is earlier in the book; v4 pattern 2). The writer's flag on 29.10's
   "residential construction rules" is correct (STD 03-11-002 excludes concrete floors and roof).
3. Masonry Craft 13 (Revision 7 text). Working height between knee and shoulder, banded raises,
   two platforms for two wythes: same position, named by topic. Disagreements: 30.4 Professional
   states trowel size as a risk control ("Blades of 10 to 11 inches lower the wrist moment ...
   without cutting output", unsourced) where 13.14 says trowel sizing "is trade practice, not a
   cited ergonomic study"; power buggy rental $206 to $350 in 30.3 against 13.14's "$70 to $280
   per day" (13 includes the motorized wheelbarrow); "kneeling board" names a closed-cell foam
   board at $15 to $40 in 30.4 and 30.15 and a stainless slider at $93 to $110 in 13.14.

**Item 10, poetry and warmth.** Finding 6. Also 30.9 Simple "nobody calls it if you are alone and
unconscious" (warning cadence), "A trauma kit with a tourniquet waits at a fixed spot"
(personification); 30.10 Simple "and then you hang there until someone comes" (staged scene);
30.16 Simple "The messenger stays in the truck, the harness in its bucket, and the N95 in the
glove box on a smoky morning" (vignette triad, fault 2); 30.7 Simple "Over years, what matters is
the pace the body holds for a season" (cleft, gnomic). The warmth in 30.12 and 30.13 is mostly
kept to facts, which is the hard part of this chapter and largely achieved; the faults there are
sourcing, not sentiment.

**Item 11, AI tells.** The "three" enumerations (item 7); a hedge-like evidence grade in nearly
every Professional paragraph of 30.7, 30.8, 30.12 and 30.13 (finding 1); hedged ranges "about
one in six to one in five" (30.13 Simple) and "about 1 to 3 percent" (30.14 Professional), which
the brief bans; "One illustration allows up to $25,000" (30.14), an anonymized specific.

**Item 12, the Unsure list.** In section 4 below.

## 3. Findings by fault

1. **Research narration, evidence-gap form (fault 23), about 20 sentences, NEW PATTERN (with ch27
   row 7 finding 2).** The body grades and reports the evidence instead of stating the fact and
   sending the gap to Open items. 30.3: "No wood-frame gantry of comparable rating is documented";
   "Neither has been tested on this project's double-wythe task mix"; "No study measures their
   throughput against a wheelbarrow and a helper"; "no study measures the fatigue outcome of a
   manual press". 30.4: "No source gives a wear life for either, so replacement goes by
   inspection." 30.5: "a practical problem no guidance addresses". 30.6: "no study quantifies
   either". 30.7: "With no masonry-specific multiplier on record"; "No study tests whether a solo
   operator sustains it". 30.8: "no consensus exists on sets, distances or progression"; "Neither
   has been validated against masonry or concrete outcomes"; "With no validated program";
   "Mixed evidence supports the pre-shift stretch-and-flex programs"; "an insurer's program
   evaluation rather than a controlled trial"; "Carrying the figure from exercise to a day of
   masonry is an inference"; "No primary source gives a daily calorie figure". 30.9: "no
   independent test covers a site like this one". 30.12: "That is practitioner guidance rather
   than a controlled result". 30.13: "a pattern no study measures directly"; "These are
   practitioner reports, not controlled studies." 30.14: "with no study of its prevalence or
   outcomes". (30.10's "Nothing in the standard or OSHA's interpretations addresses the lone
   worker" states a fact about a rule's text and stays.) Cause: the general guide says "When the
   evidence is mixed, say so"; the style guide sends gaps to Open items; the brief does not say
   how the two meet, and a health chapter is built on thin evidence. The lint pattern lists
   exact phrases.
2. **Source-class attribution (fault 37), about 20 sentences, in wording the v3 list does not
   name; the answer file names most of the sources.** "Homesteading and rural-living guidance
   names the mechanism and the practices" (30.13; the brief's own example is "general
   homesteading guidance"; answer item 63 names Modern Homesteading and Fidelis Terra Farm);
   "Construction fatigue research favors short, frequent breaks" (30.7; answer item 34 names a
   CPWR toolbox talk); "Construction safety guidance recommends at least 10 hours"; "Workers'
   compensation literature records the usual course" (answer item 35 names the law firms);
   "Decision fatigue is described in the cognitive literature"; "Project-management guidance
   holds ... one survey in that literature found 78 percent" (answer item 58 names NiftyPM's
   blog); "Nearly 60 percent ... in one industry survey" and "Construction mental-health
   guidance names" (answer item 59 names DepthBuilder, Procore and Autodesk blogs); "National
   data put rural EMS response above 14 minutes"; "US home-improvement injury data"; "Injury-
   prevention research reads the over-representation as severity"; "Research on construction
   fall detection"; "Apple Watch owners have logged false alarms"; "One documented fall from a
   ladder went unregistered"; "the agricultural literature describes the closer analog";
   "Scheduled video calls are reported as a real bridge"; "is a reported practice"; "One
   illustration allows up to $25,000"; "a review published in Occupational Medicine" (journal,
   no author or year). The pattern is that the weaker the source, the vaguer the attribution:
   a blog becomes "guidance", a vendor survey becomes "one industry survey". The v3 rule holds
   where the sources are agencies and journals (30.2, 30.5, 30.6, 30.11).
3. **Medical facts restated in Simple under a different measure than the source states, 6
   instances, NEW PATTERN (with ch22 row 6 finding 5).** 30.8: "In heat the body loses a cup of
   water every 15 to 20 minutes" (NIOSH gives an intake: drink a cup every 15 to 20 minutes;
   sweat loss is not that figure). 30.9: "Twenty to 45 minutes is how long a rural ambulance
   takes to reach a parcel like this one" (Marion County's plan targets, which the writer's own
   corrections entry says are "targets ... not measured response times", and no parcel exists);
   "For the worst injuries in the most remote areas it takes over an hour" (the ACS 97.1 minutes
   is response plus transport, not arrival). 30.6: "about 100 decibels at your ear, enough to
   cost hearing in two hours a day" (two hours at 100 dBA is OSHA's permissible exposure; NIOSH's
   limit at 100 dBA is 15 minutes; the sentence presents a permitted dose as the damage dose).
   30.5: "Years of outdoor work raise the risk of skin cancer by 60 percent" (the Skin Cancer
   Foundation figure, stated correctly in Professional, is nonmelanoma). 30.2: "A 94-pound bag
   of cement is over the federal lifting limit" (the NIOSH equation is a recommended weight
   limit, not a federal rule). Each Professional sentence states the source correctly; the
   plain-words version changes what the number measures. The read-aloud and point-first checks
   cannot catch this; only checking each Simple number against its sourced sentence does.
4. **Invented thresholds in health and process advice (fault 9), 7 instances, NEW candidate.**
   30.7 step 11 "Give the part two full days before loading it again" and step 12 "See a
   physician when a sign persists past a week of rest" (repeated in 30.16's table and the Who
   decides row); 30.12 step 11 "When exhaustion outlasts a weekend, take a week off site" and
   step 12 "When detachment or doubt outlasts a month, treat it as a hiring trigger"; the
   hiring table's "within 500 hours of the next 5,000-hour step" and "A birthday at 50 or past
   it" (with step 1, "Hire help ... when any row in the table applies for more than a week", the
   birthday row fires permanently from age 50); the opening's "Each exposure has a published
   limit". Answer item 68 says "None of these thresholds are hiring-decision research
   specifically". The clinical sources (answer item 35) give signs, not day counts. None is
   tagged as the plan's own number or carried in Open items; only the table as a whole is
   (Jon to confirm). 30.14 Simple's "because the same fall injures an older body more" states as
   fact a mechanism the Open items say is unread.
5. **v4 pattern 1, Professional restates Simple, 8 sections (confirms v4).** 30.4 "Cushioning
   addresses point pressure and alkali contact, not the duration the studies measure" after
   "A knee pad protects the kneecap ... It does nothing to the hours"; 30.5 the 60 percent; 30.6
   "5 dB is added for the second protector" after "Plugs under muffs add only 5 decibels more";
   30.9 Marion County's 20 and 45 minutes after Simple's "Twenty to 45 minutes"; 30.11 "wet feet
   lose heat about 25 times faster ... up to 60 degrees" after the same two facts; 30.12 the
   three burnout components after Simple's three ways; 30.13 "16 to 20 percent ... 89 percent"
   after "one in six to one in five ... Nine in ten", and the suicide-rate sentence in both;
   30.14 "the same ladder fall does more damage to an older body" after the same in Simple. Also
   "say a thing once": trench foot at 60 degrees four times (30.7 table and Professional, 30.11
   Simple and Professional); the heat and smoke triggers stated in 30.7 Professional and again in
   30.11.
6. **Simple closers built to land (faults 4, 39 family), 7 of 16 blocks.** 30.1 "while the
   property tax and the insurance bills keep arriving"; 30.2 "block after block, for thousands of
   blocks"; 30.6 "Years of it leave fingers white and numb in the cold"; 30.12 "the winter months
   when the schedule slows and the sky stays grey"; 30.13 "and the crisis line is three digits,
   988" (two unrelated facts joined to land); 30.14 "set against the calendar days it saves and
   the body it spares"; 30.15 "the fall-arrest kit outlasts the build". Plus the isocolon triad in
   30.12 ("Rest taken early counters exhaustion, a real break counters detachment, and a dated
   photograph ... counters lost confidence") and the antithesis in 30.13 ("Town life delivers
   contact without effort ... A parcel at the end of a road delivers none"). The brief forbids
   these by example; chapter 4's row 3 finding 5 noted the same "consequence flourish", milder.
7. **v4 pattern 3, generic "he" (confirms v4).** 30.1 twice, 30.10, 30.14.
8. **v4 pattern 2, later chapter repeats an earlier entry (confirms v4).** 30.5's PEL entry
   (Tools 27.11), 30.1's ORS 654.005 entry (Build Sequence 29).
9. **Factual gap: ORS 654.005(5)(b)** omitted from 30.1 (see Code above).
10. **Internal contradictions:** check-in intervals (30.9 against 30.10 and Decisions); smoke
    steps (30.11 steps 14 and 16; July against August); the doubt trigger (30.14 Simple against
    its table); P100 in Decisions against "P100 ... or an N95 at the least" in 30.5 step 2.
11. **Inventory sentences (fault 41) and hedged ranges (fault 38),** one-off slips the brief
    already forbids: see item 7 and item 11 above.
12. **Professional analogy, personification and register:** "an emptying tank" (30.12); "the
    tire decides the cart, not the frame" (30.3); "Next up is"; "the clear call"; "a trauma kit
    ... waits" (30.9 Simple); "the phase it earns its keep in" and "the roof and the solar panels
    need it" (30.15 Simple).
13. **Undefined record:** the "fatigue log" (30.3 step 8).
14. **Dropped without note:** the answer file's $2,000 to $3,500 hydraulic press figure (30.15
    row) and the skeleton's "material and panel lifts".
15. **Section size:** 30.6 at 1,022 prose words with no subheading.
16. **Jon's note voices the chapter's recommendations as Jon's commitments** (see item 2 and
    proposal E).

## 4. The writer's Unsure items

1. **Ten skeleton sections split into sixteen, aids moved beside lifting.** Right. The split by
   body system keeps every section under or near the 900-word ceiling and puts the aid decision
   after the limits that drive it. Recorded in the worklog as the brief asks.
2. **Code entries for employer rules kept although they bind only once a helper is hired; the
   600-volt two-person rule and Section 523 demoted to Professional sentences.** Right in
   principle: each entry becomes a duty the day a paid helper or a work trade starts, and the
   Applied steps work to their values. Two corrections: 30.5's PEL entry belongs to the Tools
   chapter (name it instead), and 30.11's Table 1 and acclimatization-plan entries can go,
   because the Applied steps use Table 2 and NIOSH's schedule. The demotions are right (v2 rule).
3. **Worked lifting example from the CCOHS tables with illustrative inputs.** Right. The
   arithmetic checks, the inputs are labeled as illustrations, and Applied steps 12 and 13 replace
   them with the site's heights. It is the most useful table in the chapter.
4. **(Lint WARNs.)** 30.14's two cross-reference sentences: both are in Applied steps that need
   the other chapter's method, which is allowed in spirit; the Professional block's further two
   (Masonry Craft, Build Sequence) are the ones to cut. The 7-word-run WARN is the lint matching
   repeated chapter titles: a lint quirk, nothing to fix.

The pattern of the flags: the writer flagged structure and Code-layer calls, and none of the
health-evidence calls (how to source a medical claim, what to do when only blogs answer, whose
threshold a rest day is). That is where the faults are, and the brief gives no rule there.

## 5. Proposed WRITER_BRIEF changes (v5)

Under Do 2, after "Name the source or state the fact":

**A. Evidence gaps go to Open items; the body states what the source found.** (findings 1, 2)

> **State the finding, never the search.** "No study measures X", "no source gives Y", "X is not
> documented", "Neither has been validated", "rather than a controlled trial", "These are
> practitioner reports, not controlled studies" are research narration in any wording. Where a
> value has no source, the sentence states the method the plan uses instead ("Replace the board
> when the foam stays compressed") and the gap goes to Open items. Where the evidence is weak,
> name the source in the sentence and let its name carry the weight: "NiftyPM's project blog
> cites a survey in which 78 percent ...", "Zurich's evaluation of its own client programs
> reports ...". A blog, a vendor page or a forum is named as a blog, a vendor page or a forum; it
> is never promoted to "guidance", "the literature", "research", "data" or "one industry
> survey". A health, injury or psychology claim names its study (author, journal, year) or its
> agency and document, the same as a code value.

Evidence that it is a pattern: about 20 evidence-gap sentences and about 20 source classes in
chapter 30, concentrated in its five least technical sections, against near zero in its
technical sections; chapter 27's "Those percentages come from trade summaries rather than a BIA
or TMS technical note" (row 7, finding 2) and chapter 22's "Rural users report" (row 6) are the
same move in technical chapters. Chapters still to come with thin or soft evidence (Build
Sequence, Resilience, Documentation, Finance, Business) will meet it. Lint companion: extend
RESEARCH_NARRATION with `\bno (study|source|primary source|guidance|independent test)\b
(measures?|gives?|tests?|quantif\w+|addresses|covers)\b`, `\b(has|have) been (tested|validated)\b`,
`\bis documented\b`, `\brather than a controlled\b`, `\bpractitioner (reports|guidance)\b`, and
`\b(the \w+ )?(literature|research|guidance|data) (holds|names|favors|records|reads|recommends|put|puts|describes)\b`,
`\bone (industry )?survey\b`, `\bone illustration\b`, `\bare reported as\b`.

**B. Plain words keep the measure.** (finding 3)

> **A Simple figure keeps what its source measured.** When Simple puts a sourced number in plain
> words, it keeps the number's kind: a recommended intake stays an intake (not a loss rate), a
> target stays a target (not a measured time), a permitted dose stays a permitted dose (not the
> dose that does harm), a guideline stays a guideline (not a federal limit), a subgroup stays the
> subgroup (nonmelanoma, not all skin cancer), and a total stays the total (response plus
> transport, not response). Before reporting, read each Simple number against the sentence that
> sources it.

Evidence: six instances in chapter 30, two of them factually wrong for the reader (water loss,
ambulance arrival); chapter 22's "Clouds cover three-quarters of the winter sky" against
chapter 3's "the sun shines about 33 percent of the time" (row 6, finding 5) is the same measure
slip across chapters. No current gate or check catches it, because each Simple sentence reads
well alone.

**C. The plan's own numbers are labeled as the plan's.** (finding 4)

> **A threshold the plan sets is marked as the plan's.** A rest period, a review interval, a
> trigger count or an age, where no source gives the number, is stated as the plan's choice ("The
> plan rests the part two days"), tagged (Jon to confirm) in Decisions, and listed in Open items
> with what would settle it. When to see a physician is stated by the clinical sign the source
> names, not by a day count the source does not give. A trigger written as a row in a table is
> checked for what happens when it fires and stays true (an age).

Evidence: seven instances in chapter 30; answer item 68 says none of its thresholds is from
research. One chapter only, so this is the weakest of the three; it is proposed because every
process chapter still to come (Build Sequence, Documentation, Resilience) sets intervals and
triggers.

**D. Simple closers: the deletion test.** (finding 6; optional, a sharpening of the v3 rule)

> Read the last sentence of each Simple block with it deleted. If the block loses no fact, the
> sentence goes. If it holds a fact, move the fact into the block and end on the fact before it.

Evidence: 7 of 16 chapter 30 blocks, and chapter 4's "consequence flourish" (row 3, finding 5).

**E. Notes in skeleton chapters.** (finding 16; for the orchestrator's judgment, since chapters
22, 24, 25 and 27 passed with the same move)

> In a chapter whose Revision 7 text is a skeleton, the record is the skeleton's scope line,
> BOOK_STRUCTURE and other chapters' Decisions lists. A recommendation the chapter makes is not
> in the record and does not appear in the note as "I will" or "I want"; the note states the
> recorded facts and asks the questions the recommendation raises ("[JON: will you work to the
> crew safety limits while working alone?]").

## 6. Redo before the mass wave?

**Yes.** The chapter violates all three v4 rules (8 Professional-restates-Simple sections, two
repeated entries, four generic "he"), and its health sections carry the three new patterns at a
density the loop has not seen: about 40 narration or source-class sentences, six Simple
medical facts that change their source's measure (two of them wrong for the reader), seven
unlabeled thresholds, a statute clause missing (ORS 654.005(5)(b)), and four internal
contradictions. Its technical half (lifting, silica, noise and vibration, fall protection, heat
and smoke) is among the best Revision 8 work and should be carried into the redo as it stands.
A redo under v5 would test rules A to C on the chapter that produced them; chapters 22 and 27
should be checked against A and B at the same time.
