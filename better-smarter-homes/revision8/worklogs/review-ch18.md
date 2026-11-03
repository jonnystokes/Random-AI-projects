# Review: chapter 18, Water Independence

Reviewer sub-agent for the orchestrator, 2026-11-03, 9:35 PM. The first chapter written under
WRITER_BRIEF.md v5 (skeleton chapter; Fable 5.1, 2026-10-29 to 2026-11-03). Judged against
REVIEW_CHECKLIST.md and brief v5. The chapter was read in full, start to finish, before any
judgment. No file other than this one was written.

## Summary

- Words: Revision 7 397 (skeleton) -> 15,781 (lint count; 12,907 prose words in stats.py).
- Sections: 11 skeleton headings -> 17 sections, 2 subheadings. Labels S/A/P/C 17/17/16/6.
- Code entries: 18 (18.3: 3, 18.8: 1, 18.9: 2, 18.10: 2, 18.12: 7, 18.14: 3), all three-part.
- Open items: 26 plus the Dropped bullet. Who decides: 19 rows. Decisions: 16 (7 decided,
  1 pending parcel, 1 pending engineer, 7 Jon to confirm). Records: 16.
- Research: 12 findings filed; 6 cross-chapter flags. [JON] markers 4 (one header marker and
  three specific questions); 1 [FIGURE].
- Lint: PASS, 0 FAIL, 0 WARN. Stats: average sentence 16.9; The/A/An openers 10.7 percent;
  Simple 14.5, Applied 14.0, Professional 20.2 (27 percent of Professional sentences over 25
  words); 30+ word sentences 6.8 percent.
- Verdict: **ITERATE.** The mechanical rules of v5 held cleanly (no Code semicolons, one
  cross-reference per section and none packed, generic "they", no hedged ranges, counts match
  their lists, the studies named by author and year, the plan's thresholds tagged). The prose
  rules v5 added for Professional did not hold: Professional repeats Simple or Applied in 12 of
  16 sections, with nine "therefore / for that reason / hence" sentences restating an Applied
  step and seven paragraphs closing on a line built to land. The "second value" rule failed at
  four points against Revision 8 text (17, 22, 4). The new pattern, which v5 does not reach, is
  internal incoherence of the system the chapter describes: the slow well's buffer sits in the
  rain cistern although the two waters "never join", and the cistern is sized to the whole
  household's demand although rain serves only toilets, laundry and garden. Chapters 25 and 30
  showed the same class of fault (internal contradictions), so it is a pattern. A second, smaller
  pattern is Open items written as the writer's diary.

## 1. Mechanical

**Lint and stats.** As above. Every gate passes. The lint missed, by wording: "the planning band
in the steps" (18.6), "Step 7's target" (18.15), "this kit is documented there as well as here"
(18.15); nine "therefore/for that reason/hence" restatements in Professional; "national practice
expects" (18.14) and "Cold-climate guidance from AquaBarrel and the permies.com cold-climate
thread" (18.7) as source classes; an imperative inside a Simple block (18.15, "Divide the gallons
left by the days until the rains usually return"); Professional/Code echo in paraphrase (18.3,
18.12, 18.14).

**Anatomy and numbering.** Complete and contiguous (18.1 to 18.17).

**Preservation.** The skeleton had no facts, only scope notes. Every scope note is honored by a
section or named in the Dropped bullet (instruction block, "Options, costs and trade-offs",
"Code and standards", "source blending", "cross-connection and backflow", "prior appropriation",
"exempt groundwater"). Holds.

**Spot values and every dollar figure** (answer file ch18 unless stated).

| Value in the chapter | Trace | Result |
|---|---|---|
| WISY vortex $658, 280 microns, 2.78 L/s, 70/30 split | item 5, line 57 | Matches |
| Manufactured tanks $1,100 to $6,800 concrete, $800 to $6,000 poly; installed buried concrete $17,000 to $21,000 | ch17 answer item 20 (AquaBarrel, gototanks) | Values match. Attribution wrong: the chapter names "Design Transition Studio's price survey", which appears in no answer or research file; the second source is gototanks |
| Tank service life 20 to 30 years "by Storewel's and Kennedy Tank's comparisons" (18.7 table) | Nowhere in research/answers or research/new | Untraced. Brief "Do" 6: a finding not filed with a source does not go in the chapter |
| Ainsworth $750 (1983), $1,500 (2006) | research/new/ch18.md | Matches, year carried |
| Lining $5 to $20 per sq ft | item 36 | Matches |
| Consumables $300 to $500 a year | item 44 | Matches |
| Hydrofracturing $1,500 to $6,000, 70 to 90 percent, 35 to 1,000 percent | item 96, ch17 item 40 | Matches |
| Greywater fees $50 + $40, $534 + $50 | item 63, DEQ guide | Matches |
| Diverters $59, $65 to $70 (Applied $60 to $70) | item 66 | Matches |
| Composting toilets "Above $5,000", "hundreds to about $2,000" | item 71 | Matches; incinerating "hundreds to a few thousand dollars" untraced |
| Ecology zinc 114, 52, 57, 3.5 ug/L; tile pH 7.2 | item 1 | Matches |
| 0.62 gal/sq ft/in; 75 to 90 percent; 10 gal per 1,000 sq ft; pipe 0.36 gal/ft | TWDB, research/new | Matches; 4-inch 0.67 and 6-inch 1.5 recomputed and right |
| Worked example 39,680 gal; 21,600 gal; 16,000 to 30,000 gal | arithmetic | Right |
| 2,880 gal/day at 2 gpm; water 62.4 against concrete about 29 BTU/cu ft/F | arithmetic | Right |
| ACI 350 0.0024 against 0.0018 | item 116 | Traces, but the answer's source for 0.0024 is an Eng-Tips forum thread; the chapter names "CTLGroup's note ... and ACI's own listing". ACI 350's temperature-and-shrinkage table runs by joint spacing (as recalled, 0.0030 for Grade 60 under 20 feet). Verify; Open item |
| Biosand "2 to 7 log of E. coli, 97.9 to 99.8 percent" (18.10) | item 53 | Copied from the answer file, which is internally inconsistent: 97.9 to 99.8 percent is 1.7 to 2.7 log, and 7 log is 99.99999 percent. The sentence presents the two as one quantity (Fault 52) |
| ASTM D1253 "for filterable solids" (18.16) | item 105 | Copied from the answer file. ASTM D1253 is the residual-chlorine method; flag the answer file (medium confidence) |
| Melbourne "a dry-summer climate comparable to western Oregon's" (18.6) | item 19 | From the answer file. Melbourne's rain falls fairly evenly through the year; it is not a dry-summer climate. Cut the clause |
| NOAA Atlas 14 for the parcel (18.5, Open items) | item 3 | Oregon lies outside NOAA Atlas 14's published volumes (the Pacific Northwest still rests on NOAA Atlas 2 pending Atlas 15), and the OPSC sizes roof drainage from its own rainfall-rate table. Medium confidence; flag the answer file and verify before the step stands |

**Code entries.** Three-part, sourced, no semicolons. Source-line problems:
- 18.8 (OPSC 1601.9.2) and 18.10 (OPSC 1603.15, 1603.4) were read from the 2026 OPSC change
  summary (research/new/ch18.md). Brief v5: "a change summary ... is not the code, and an entry
  known only from one waits in Open items." The writer read the rule and broke it. The Source
  lines say "OPSC ... (2026 edition)" with no sign of the document read.
- 18.10's 1603.4 value line misstates the exception: "with no treatment for subsurface or
  nonsprinkled irrigation under 360 gallons of storage". Chapter 17's 1601.5 entry (and the change
  summary text in research/new) reads "no treatment for aboveground irrigation at 360 gallons or
  less of storage, or for subsurface or drip irrigation". Subsurface needs no treatment at any
  volume. Fault 50 as well as a wrong value.
- OAR entries (340-044, 340-053, 690-230, 437-002, 918-770) were read on oregon.public.law
  "through a summarizer, with short quotations". The site reproduces the Secretary of State text,
  so the document is the rule; the reading was not. The values match the rules as commonly
  stated. Accept for this pass; verify each value line verbatim before freeze.
- 18.9's two OAR 437-002-0146 entries carry no subsection and no actor. The rule binds employers;
  Professional says so ("Oregon OSHA's confined-space rule binds employers") while the
  requirement line says "A tank is a permit-required confined space". Judgment check 9
  (requirement without an actor); the entry should open "When an employee enters ...".
- 18.8's only Code entry is the abandoned-tank rule, in the section on building the tank. The
  tank's construction entries wait in Open items (the OPSC tank sections not reprinted), which is
  right, but the section reads oddly. Not a fault.

**Obligations.** The water triad (3 / 17 / 18): the worklog draws the boundary well and the
chapter names Land and Plumbing Supply at the overlaps. In substance it breaks three times
against 17 (see section 9) and repeats 17 twice. Resilience (34) pulls from 18: the kit and the
NFPA 1142 calculation are named to Resilience, though 18.15 says "this kit is documented there as
well as here". Partly met.

**Counts.** All checked and right: four offices, four parts, three limits, three claims, four
wastewaters, three places, three lining classes, three ab anbar choices, three drilling firms,
two vendors, the Tier 1 permit's two limits.

**INFO lists.** "in writing" 7 times in the body (opening plus three is the rule); "stated in
the X chapter" 9 times (see finding 14). No four-digit dollar figures. Two "What ... is" clefts
(18.7 "What the owner-pour does not buy is ...", 18.15 "What the gauge produces is ...").

## 2. The reading: findings

Numbered; fault numbers from FAULT_CATALOG.md.

1. **NEW PATTERN: the system the chapter describes contradicts itself.** (a) Separation against
   one tank: 18.1 Simple "Rainwater runs in its own labeled pipes ... and it never joins the well
   water. Between the two sits a concrete cistern. It holds the summer's water, it evens out a
   slow well, and it keeps a fire reserve"; 18.11 Simple "All day the well trickles into it";
   Decisions "the slow well's peak-hour buffer counted inside it". Raw well water for drinking
   and nonpotable rain then share one tank, which is the blending chapter 17 decided against
   ("never join the well water"; OPSC 602.4 "joins no other source without approval"). (b)
   Sizing basis: 18.6 sizes the cistern to "Four people at 45 gallons a day ... 21,600 gallons",
   the whole indoor demand, though rain serves only toilets, laundry and garden and the plan leans
   to a composting toilet (which removes the toilets). 18.15 Simple "By August the tank is the
   only water you have" contradicts "The well supplies the drinking water". (c) 18.13 Applied 3
   "move the wet zone to the downhill side" against Professional "the wet zone is placed uphill on
   the plan". (d) 18.7 Applied 3 "Split the volume into two manifolded tanks" as an instruction,
   while Jon's note asks "one tank or two" and Decisions tag it (Jon to confirm); 18.7
   Professional "Below about 25,000 gallons one tank is cheaper per gallon"; 18.16 "which is the
   case for two tanks". (e) 18.15 Applied 12 "Keep an owner-built biosand filter with the kit,
   started 30 days before it is needed", for an emergency that cannot be dated. (f) 18.7 table:
   concrete tank "20 to 30 years" beside Simple "the one that fits a house meant to stand for
   centuries". No brief rule asks the writer to check the chapter's parts against one another or
   against the decided architecture. Chapter 25 (two internal contradictions) and chapter 30
   (check-in intervals, smoke steps, doubt trigger) had the same class of fault. Brief change
   proposed below.
2. **v5 rule failed: Professional repeats Simple or Applied** (12 of 16 sections). Examples:
   18.1 "Sizing therefore follows the largest claim" (Applied 5, 6); 18.4 "That same chemistry
   makes a new cast concrete surface leach lime for its first years" (Simple's last sentence);
   18.5 "For that reason the fixed standpipe is sized for ordinary winter storms, and the first
   autumn storm is held out by hand" (Applied 9, 10); 18.6 "Demand binds in western Oregon"
   (Simple's first sentence); 18.8 Dancing Rabbit "Half again the estimated concrete went in"
   (Simple) and "Their correction for next time is a 2-by-4 wall on 16-inch centers under
   sheathing at least 3/4 inch thick" (Applied 1), and the same story a third time in the 18.17
   table; 18.9 "Two or three full empty-and-fill cycles pass before the water holds at 9 or
   below" (Simple and Applied 8, 9) and "most cleaning stays outside the tank altogether"
   (Applied 12); 18.10 "A spring train therefore starts with a spring box" (Applied 11, 12) and
   "the train ends at the lamp" (Simple); 18.11 "An attempt is therefore insurance ... The buffer
   is designed first, the attempt made, the yield re-tested" (Applied 5 to 7); 18.13 "For that
   reason the wet zone is placed uphill" (Applied 3), "Hence the diversion valve is a seasonal
   switch" (Simple); 18.14 "Neither the statute nor the installation rule sets an occupancy or
   bedroom limit" (Simple "no limit on how many people"); 18.15 the six-item behavior list
   (Simple and Applied 6); 18.16 "One roof and one conveyance path can fill both volumes" (Simple
   "One roof and one gutter can fill both volumes"). Nine "therefore / for that reason / hence"
   sentences in Professional; the brief names exactly this ("A 'therefore' sentence that restates
   an Applied step is cut") and the writer's repeats check did not catch it. The rule is clear;
   it needs a lint gate (below), not new words.
3. **v5 rule failed: Professional paragraphs end on a line built to land** (Faults 4, 1). 18.1
   "Its first sign is then a sick household rather than a cloudy tap."; 18.7 "Each of those three
   choices is the modern detail by another route"; 18.8 "For a shell meant to last with the house,
   the formed tank is the better-supported choice."; 18.11 "a tank sized only for the first
   covers nothing in a dry August"; 18.14 "a rural parcel absorbs that for decades"; 18.15 "that
   budget turns a tank into a habit"; 18.16 "which is the case for two tanks". Also isocolon in
   18.5 ("Sized for the October storm, a diverter wastes water all winter. Sized for a rinsed
   January roof, it under-diverts in October.") and 18.8 ferrocement "saves material and spends
   skilled labor in its place".
4. **v2 rule recurring: Professional restates Code in paraphrase** (Fault 28), which the 6-word
   gate misses. 18.3: all three entries are restated ("A heat-pump return well needs no
   individual permit once DEQ holds its registration"; "OWRD's low-temperature geothermal rule
   puts household heating and cooling inside the domestic exemption, under the domestic cap";
   "Reinjection also takes ... a DEQ pollution-control permit. DEQ may waive that permit by
   agreement"). 18.12: "Dishwasher, garbage-disposal and diaper wash water never join" and "Below
   the Tier 2 ceiling, a system connected to the septic system needs no land use compatibility
   statement" (entries 3 and 7). 18.14: "ORS 447.118 permits the occupant of a dwelling to install
   a compost toilet that meets the rules' minimums" (entry 1, verbatim in substance).
5. **v5 rule failed: second value** (Fault 50). (a) OPSC 1603.4's irrigation exception against
   chapter 17's 1601.5 entry (Code section above). (b) 18.1 Professional "Code adds a design
   professional and water-quality duties only where potable status is claimed" against chapter
   17's OPSC 1601.2 entry (a licensed plumbing contractor, certified rainwater designer or
   registered design professional for nonpotable systems, with two exceptions) and 17.19 Applied
   12. (c) Incinerating-toilet load: the Solar chapter's Revision 8 text states "1 to 2 kW through
   each burn cycle" (22, line 36); this chapter writes "several kilowatts" and its flag says the
   solar chapter "leaves the figure open", which it does not. A third value. (d) Sprinkler
   standard: 18.16 cites NFPA 13 for a house sprinkler reserve; the Legal chapter states that
   Oregon adopted NFPA 13D (2022) for one- and two-family dwellings and that NFPA 1142 lets the
   fire authority reduce the supply where the dwelling is sprinklered, which 18.16 omits. (e)
   Position: the gravity tap is (Jon to confirm) in chapter 17's Decisions; the opening states it
   as fact ("Nothing between that water and one indoor tap depends on electricity").
6. **v4 rule recurring: a later chapter repeats an earlier one's text** instead of naming it.
   18.1 Professional's Appendix K paragraph ("Under it a registered design professional or a
   person the building official accepts designs the system ... A rain train built to the same
   filtration and ultraviolet dose as the well's gives the same water without that claim")
   repeats 17.19 Professional. 18.11 "Raw well water that waits in the buffer loses any chlorine
   residual and grows biofilm on the walls, so the buffer is dosed and inspected as a treatment
   stage" repeats 17.5 almost word for word (and raw well water carries no residual to lose).
7. **v3 rule recurring: the opening, Jon's note and the first Simple block repeat one another.**
   Well for drinking and rain for toilets, laundry and garden (opening, note, 18.1 Simple); one
   cistern for dry season, buffer and fire reserve (opening, 18.1 Simple); one tap without power
   (opening, note, 18.1 Simple, 18.1 Applied 7, 18.7 Applied 10). The buffer-inside-the-volume
   rule is stated seven times (opening, 18.1 S/A/P, 18.11 S/A/P).
8. **v5 rule partly failed: text pointers** (Fault 48). "bring the indoor figure down to the
   planning band in the steps" (18.6); "Step 7's target is the plan's choice and Jon's to set"
   (18.15); "this kit is documented there as well as here" (18.15, also a duplication admitted
   in the text); "the field example" (18.8 Applied 11 and Professional); "the construction
   section" (Open items). Cross-references: held, one per section, none packed.
9. **v5 rule mostly held: name the source, state the finding.** Held: Imteaz et al. (2011),
   Vivek, Malghan and Mukherjee (2021), the Virginia WRRC 1998 survey, NC State Extension, vendors
   named as vendors. Failed: "because national practice expects a water closet in a dwelling"
   (18.14; the rule is ORSC R306.1, which the sentence should cite or the item should go to Open
   items); "Cold-climate guidance from AquaBarrel and the permies.com cold-climate thread" (18.7,
   a forum promoted to guidance); "In The Driller's survey article" (18.11, a trade magazine named
   in place of an author); "Field records support decades of service with maintenance and nothing
   longer" (18.8, search narration); untraced sources (Storewel, Kennedy Tank, Design Transition
   Studio). The VWRRC and NC State figures came from search summaries and carry no Open item.
10. **v5 rule mostly held: a figure keeps its measure** (Fault 52). Failed: biosand log and
    percent (above); "A mosquito needs a gap wider than a sixteenth of an inch" (18.9 Simple),
    which turns Alameda County's 1/16-inch mesh guideline into a fact of mosquito biology (the
    Mozzie Stoppa screen the chapter recommends is 955 microns, finer still).
11. **v5 rule held: thresholds the plan sets.** 0.80, 35 to 50 gallons, the yearly test, two
    tanks and the standpipe diverter are tagged and in Open items. Untagged: the 5,000-gallon line
    for cast-in-place (18.7 Applied 2), the monthly runoff pH test (18.4 Applied 7).
12. **v5 rule partly failed: borrowed resolve** (Fault 54). The note has one header marker and
    three real questions, good. But "When the power is out I still want to fill a bucket from a
    tap that runs by gravity" and "The rain is for toilets, laundry and the garden" voice two items
    chapter 17 tags (Jon to confirm) as Jon's settled wants, with no inline question.
13. **v3 rule recurring: (decided) on the chapter's own recommendations.** "The catchment surface
    is concrete, a TPO membrane ... or painted metal"; "Every tank opening is screened at 1/16
    inch ... entered only under the confined-space protocol"; "Greywater runs under the Tier 1
    general permit ... by gravity"; "The storage is a buried, roofed, opaque concrete tank designed
    to ACI 350" beside "(Jon to confirm) The owner-poured concrete tank over a manufactured one".
    Only the separation decision traces to a recorded choice (17's Decisions).
14. **Repeated shape: the v5 cross-reference sentence became a formula.** "X are stated in the Y
    chapter" 9 times (18.1, 18.2, 18.3, 18.7, 18.8, 18.12, 18.13, 18.15, 18.16), several with an
    inventory payload: "Water rights are stated in the land chapter, which covers the well's
    domestic exemption, the rooftop exemption, springs and ponds, the critical-area map and the
    driller's filing" (five items, and "covers" with a document as subject, Fault 3). The brief's
    repeated-shape rule already forbids it; a lint count would catch it.
15. **Open items written as a diary.** "the medians in the catchment table were taken from the
    answer file's extraction of the Ecology report, since the report's server refused this
    writer's download"; "the 2018 paper the answer file cited ... could not be opened, so the
    chapter cites Imteaz"; "the drain-waste-vent chapter's table gives as 3 to 5 kilowatts and the
    answer file as 1 to 2"; "which the change summary did not reprint". Three items open "Unknown:
    nothing in substance, but ...", which is not an unknown. Open items are reader-facing; "the
    answer file", "this writer" and "the chapter" are project process (Faults 23, 27, and the
    spirit of the "BSH" ban). Also in chapter 4 (one) and chapter 36 ("the case reporters refused
    this session"). Brief change proposed below.
16. **Simple-layer slips.** An imperative (18.15 "Divide the gallons left by the days ..., and you
    have the day's budget"); a five-item list (18.12 "showers, baths, bathroom sinks, the kitchen
    sink and the washing machine"); closers built to land (18.7 "the water never freezes and the
    ground under it never heaves"; 18.13 "In Oregon that winter switch makes the system legal
    year-round"; 18.17 "catches most of them ... catches the rest"); personification (18.3 "An open
    loop waits for a site"; 18.8 "it finds a crack a hairline wide"); unanchored "for a fraction of
    a new well's price" (18.11) where Professional has 50 to 70 percent; 18.9's Simple carries six
    topics (light, insects, alkalinity, testing, oxygen, entry).
17. **Stray history** (Fault 46). Bermuda's century of catchment law (18.4), the ab anbar
    paragraph (18.7), Thailand's jar programme twice (18.8, 18.9, "recorded the same lesson across
    millions of vessels"), "NFPA 13 has always accepted static sources" (18.16).
18. **Inventory sentences** (Fault 41). 18.12 "It costs land area, excavation, a liner, gravel
    media, reed management and a winter slowdown"; 18.15 the six behaviors; 18.5 "the days since
    the last rain, the debris load, the tree overhang, the roof's slope and the storm's
    intensity"; 18.12 Applied 5 (nine items in one step).
19. **Applied order and form.** 18.11 Applied 10 and 11 (ask drillers for basalt results, look up
    treated wells) come after the quote and the attempt (6, 7); they belong before. 18.5 first-flush
    steps 4 and 5 and 18.7 step 4 are statements, not actions. 18.6 Applied 14 "where the price per
    added day is too high" is unanchored (Fault 10). 18.4 Applied table cites "Ecology's test" and
    "the Texas manual", and 18.15 step 14 "per CDC's emergency guidance" (citations in Applied).
20. **Small technical points.** 18.4 Applied rules materials by "Potable intent" and step 2 "for
    water people will drink", though the plan claims no potable rain; the column should read for
    the nonpotable train. 18.10 rain "near pH 5.6" beside 18.4's measured "pH 4.6 to 5.2" Puget
    Sound rain, unexplained. 18.8 ferrocement: Type S mortar's lime is 1/4 to 1/2 part, not "a half
    to 1". 18.2 Applied 5 and 18.16 Applied 1 both ask the district for the reserve (said
    twice).

What held, and stays: the opening leads with the governing number (stored volume); decision
order (sizing before material, tank before treatment); Applied is deep and executable (the
first-flush sizing, the tightness test, confined-space entry, the greywater paperwork); every
count matches; arithmetic right; studies by author and year; the writer corrected the answer
file twice (the 2006 cistern price, the unverifiable 2018 paper) and caught the HVAC chapter's
misreading of ORS 537.545(1)(e); the six cross-chapter flags are specific and evidenced; Open
items carry three fields; the note has one header marker and three real questions.

## 3. Boundaries (checklist 2.9 and v5's second-value rule)

| Claim | Here | Bordering Revision 8 text | Result |
|---|---|---|---|
| Rain separate to the fixture, no potable claim | 18.1, Decisions | 17 Decisions (decided) | Same, named. But the shared cistern (finding 1a) undoes it |
| Rooftop collection needs no water right | named to Land | 3.11 entry ORS 537.141(1)(h) | Same, named, not repeated (v4 rule held) |
| Greywater tiers, no drainfield credit | 18.12, named to Land | 3.10 | Same; 3.10's entry is a pointer sourced to a fact sheet (Land's problem); 18.12 carries the rule-level entries |
| Irrigation-treatment exception | 18.10 entry 1603.4 | 17 entry 1601.5 | **Different** (finding 5a) |
| Designer for a nonpotable system | 18.1 Professional | 17 entry 1601.2 | **Different** (finding 5b) |
| Buffer tank as a treatment stage | 18.11 Professional | 17.5 | Same, but repeated in near-identical words (finding 6) |
| Storage-tank disinfection dose | named to 17 | 17.8 table, 50 to 250 mg/L | Same, named |
| Gravity tap | opening, 18.1 | 17 Decisions (Jon to confirm) | Position shifted to fact (finding 5e) |
| Fire reserve | tank side here, NFPA 1142 to Resilience | 3.11 and 17 to Resilience; 4.11 "Wastewater and well sizing is in the water independence chapter"; 4 NFPA 13D | Pointer split as flagged; **NFPA 13 against 13D** (finding 5d) |
| Cistern in the footprint | 18.7, named to Soil | 5.15, 5 Decisions (Jon to confirm) | Same, named, tag consistent |
| First flush to swales, 10 feet off the foundation, Jon to confirm near food | 18.5 | 5.14 Applied 8, 10, 11; 5 Decisions | Same |
| Composting fan 1.4 to 2.5 W | 18.14 | 22 line 36 | Same, named |
| Incinerating toilet load | "several kilowatts" | 22: 1 to 2 kW | **Different** (finding 5c) |

Older text, disagreements only: DWV 19.11 gives 3 to 5 kW for the incinerating toilet; DWV 19.13
states a "laundry-to-landscape exemption" for washer effluent with no pump, which 18.12 and 18.13
do not recognize (18 runs the washer line under the permit and the diverter); DWV 19.13 calls
Type 3 "indoor toilet flushing" (flagged by the writer). HVAC 23.3 reads ORS 537.545(1)(e) as a
closed-loop-in-well exemption against OWRD's handout (flagged), and carries its own ORS 537.783(3)
paragraph; 23's open-loop withdrawal step uses the 5,000 gpd commercial ceiling where 18 uses the
15,000 gpd domestic cap for household heating (OAR 690-230-0130(2)).

## 4. The writer's ten Unsure items

1. **Fire reserve split (17 / 34 / 4).** Right: the tank-side rule here, the NFPA 1142 calculation
   in Resilience, as 3 and 17 already say; chapter 4's pointer is the outlier and the flag is
   correct. Wrong in detail: NFPA 13D, not NFPA 13, and the sprinklered-reduction rule from 4.
2. **ORS 537.783(3) and DEQ Class V also in HVAC.** Keep them here: the skeleton puts open-loop
   water rights in this chapter and HVAC is Revision 6 text, whose rewrite names this one. But cut
   "the injection-well approval entries are stated in the HVAC chapter" (it announces the
   duplication) and the Professional restatement of all three entries.
3. **Seven greywater entries.** Right. Land's 3.10 entry is a fact-sheet pointer; these are the
   rule-level entries the subject needs. Cut the two Professional echoes; citing Table 2 "as
   reproduced in" the permit is honest and the Open item is right.
4. **Confined-space OAR without subsections.** Not enough: add the subsections and give the
   requirement line its actor (the rule binds an employer whose worker enters). The oxygen-first
   order as practice in Applied is right.
5. **Plan choices tagged (Jon to confirm).** Right as far as it goes; add the 5,000-gallon
   cast-in-place line and the monthly pH test, retag findings 13's four (decided) lines, and make
   18.7 Applied 3 conditional on Jon's tank choice.
6. **The 2006 $1,500 cistern.** Right: carried with its year, flag to 17 correct.
7. **Imteaz 2011; search-summary figures.** Right to replace the unverified 2018 paper. Cut "a
   dry-summer climate comparable to western Oregon's", which is wrong and came from the answer
   file. The VWRRC and NC State figures may stand in Professional, named, but each needs an Open
   item (document not read), which the chapter lacks.
8. **Solar's fan figure; incinerator.** Fan: right, it is the book's value. Incinerator: wrong;
   the Solar chapter states 1 to 2 kW, which is the book's value; flag DWV's 3 to 5 kW.
9. **Skeleton headings 11 to 17.** Right; decision order, and the Dropped bullet covers the folds.
10. **OARs via oregon.public.law.** Acceptable as the document (it reproduces the Secretary of
    State text); not acceptable as "read" when a summarizing fetch tool did the reading. Verify the
    value lines verbatim before freeze. The OPSC entries from the change summary are the real v5
    breach (Code section above), and the writer did not list them as Unsure.

Pattern of the flags: the writer was careful about sources and silent about the system's own
coherence; none of the ten asks whether the parts agree. That is the gap.

## 5. Proposed changes

**WRITER_BRIEF.md v6, two new rules under "Do" 2 (exact text):**

- **The system agrees with itself.** Before you report, write the chapter's system in five lines
  or fewer in your worklog: each source, what it serves, where it is stored, what sizes it, and
  which decided values from bordering chapters it rests on. Then read every section against those
  lines. A sizing that counts a load the system does not carry, a tank that holds two waters the
  chapter keeps apart, two sections that say opposite things about one choice, or an Applied step
  that directs a choice still tagged (Jon to confirm) is fixed before you report, or the conflict
  goes to Unsure. Chapter 18 shared the well's buffer with the rain cistern after saying the
  waters never join, and sized the cistern to the whole household's demand for rain that serves
  only toilets, laundry and garden; chapters 25 and 30 carried internal contradictions of the same
  kind.
- **Open items are for the reader.** An Open item states a fact the house still waits on. It
  never names the answer file, the writer, a session, a server that refused a download, a paper
  that could not be opened, or what the chapter cites instead; those go in your worklog and
  research file. An item whose Unknown is "nothing in substance" is not an Open item: if the value
  rests on a document not read in full, the Unknown is that document's exact figure.

**Lint (tools/lint.py), to enforce rules v5 already states:** a review gate for
"therefore / for that reason / hence" sentences in Professional (9 here); extend the text-pointer
gate to "in the steps", "Step N's", "as well as here", "the field example"; count "stated in the
... chapter" (9 here); an Open-items gate for "answer file|this writer|this session|refused|could
not be opened|nothing in substance"; flag an imperative opening a Simple sentence. Optional
clarification under the Source-line rule: "A page read through a summarizing fetch tool is not
read; quote each value line's number from the document's own text."

## 6. Redo before the mass wave

**Yes, from this text.** The Simple path tells a wrong story about the house (one shared tank for
drinking water and rain; a tank sized for the whole household), four values disagree with
Revision 8 chapters, and three Code entries rest on the change summary. The research, the Applied
procedures, the counts and the arithmetic stand; the fix is the architecture in 18.1, 18.6, 18.11
and 18.15, the Professional repeats, the second values and the Open-items wording. Run it after v6,
and after any answer-file corrections (biosand, D1253, Melbourne, Atlas 14) are filed.
