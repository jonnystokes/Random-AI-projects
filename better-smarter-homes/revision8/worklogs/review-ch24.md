# Review: chapter 24, Smart Home, Network, Security, and Local Automation

Reviewer pass, 2026-10-28, 5:45 PM Pacific. Chapter written under WRITER_BRIEF v3 (Opus 5.5,
then Fable); judged against REVIEW_CHECKLIST.md and the v4 brief. No file other than this one
was edited.

Read in full first: STYLE_GUIDE.md, FAULT_CATALOG.md, CHAPTER_TEMPLATE.md, REVIEW_CHECKLIST.md,
WRITER_BRIEF.md v4 with its history, the anchor-bolts exemplar, writing-style-guide-v2.md, the
AI_TODO loop log rows 1 to 8, the whole chapter (767 lines) start to finish, the Revision 7
baseline (revision7/manuscript/g1_ch_18_..., all of it), worklogs/ch24.md, research/new/ch24.md,
and the smart-home items 1 to 13 of research/answers/ch21-24_electrical-solar-hvac-smart.md.

## 1. Mechanical

**Lint:** PASS, 0 failing gates (of 64). Determiner openers 1.8 percent, long sentences 1.6
percent, bands S 15.2/25, A 14.9/25, P 18.4/40. Most repeated phrase "under ors" 8 times. Two
inventory sentences, four "So" openers. Labels S/A/P/C 17/17/17/9.

**Stats:** 11,655 prose words (stats count), average sentence 16.5 (Revision 7: 21.7), long
sentences 2 (Revision 7: 20), colon share 4 (Revision 7: 24), determiner share 15 against 13 on
the stats measure. Table share 4, Code share 15, list share 33.

**Anatomy and numbering:** opening, note, 24.1 to 24.17 contiguous, Who decides what (20 rows),
Open items (19 plus Dropped), Decisions (22), Records (15). One [FIGURE] marker.

**Words:** 5,929 to 13,780 (lint count). Sections 13 to 17 (no subheadings). Code entries 35 to
27, the eight-plus removed entries named in the Dropped bullet (see finding 14 for two that are
not).

**Preservation skim (Revision 7 removed side read in full).** Every Revision 7 fact is present or
named, with these exceptions, all small:
- The R7 Code entry "Electronic locks on egress paths fail safe" (R7 15.6) and the R7 gate entry
  ("UL 325 with monitored sensors; ASTM F2200") are not named in the Dropped bullet. Their content
  survives in 24.14 Applied steps 9 to 12 and Professional, and the gate entry's doubt is an Open
  item, so nothing is lost; the Dropped bullet is incomplete.
- The R7 PoE bundle entry (725.144 and its table) is not named in Dropped; 24.4 Professional says
  its Code entry is in the branch-circuit chapter, which is true (chapter 21, line 432).
- R7's "password rotation" in the maintenance schedule (15.13) is gone; 24.17 step 19 has "review
  the accounts". Trivial.
- R7's pointer to the HVAC chapter's outage section (15.12) is gone. Trivial.
Four R7 errors were corrected from the statute and rule texts and named (plumber-only valve, 1
BTU per watt, the felony grade of ORS 163.700, OAR 918-271-0030 as a permit exemption), plus the
230.67 surge mandate, ORS 166.065 as the neighbor-camera hook, division 271 as licensing, and the
CMR-for-risers statement. This is first-rate verification.

**Spot values (eight-plus, and every dollar figure).**

| Value in chapter | Where | Source checked | Result |
|---|---|---|---|
| 12 to 15 dB block, 16 to 23 dB 4-inch reinforced; Simple's 1/16 to 1/30 and 1/40 to 1/200 | 24.3 | answers item 2; arithmetic | match; conversions right |
| Z-Wave near 908 MHz | 24.3, 24.8 | answers items 1, 2 | match |
| 0-10 V up to five conductors, DALI-2 two | 24.6 | answers item 11 | match |
| Reach 15 to 48 inches, 44 over a 20-to-25-inch obstruction | 24.6, Open items | answers item 13; chapter 25 | match, and chapter 25 agrees |
| Technician 144 to 148 and 420 to 450 MHz; General 1,500 W PEP against 200 W | 24.16 | answers item 8 | match |
| ShakeAlert over 50 million residents | 24.16 | answers item 7 | match |
| Cat 6A 23 AWG Class 8 bundles 192, Cat 5e 91 | 24.4 | wave1 lines 884, 885, 1253 (Ethernet Alliance) | match |
| UPS 1.6 times watts, 0.6 power factor; SLA 3 years, LiFePO4 7; lifetimes 3 to 5 and 8 to 10 | 24.7 | wave1 lines 1134, 1139, 1147 | match |
| 140 W rack, 480 BTU/h, 3.4 kWh a day | 24.7 | wave1 line 1038; arithmetic | right (3.41 x 140 = 477; 140 x 24 = 3.36 kWh) |
| Speaker 16/14/12 AWG at 80 and 200 feet | 24.5 | wave1 line 1032 | match |
| 6 to 8 Mbps, 65 to 85 GB per camera per day | 24.13 | wave1 lines 976, 977 (64 to 96 GB) | the chapter's 65 to 85 is the correct arithmetic from 6 to 8 Mbps; the wave1 96 was wrong |
| 14 to 30 days, 90 days of events | 24.13 | wave1 line 967 | match |
| PM2.5 at or under 10 µg/m3 | 24.10 | answers HVAC item (line 692: "ideally near or below roughly 10") | the guidance is hardened into a target; acceptable in Applied |
| $125 limited energy contractor license | 24.2 | ORS 479.840(1)(b), research/new | match |
| $10 to $25 a month cellular plan | 24.13, Open items | answers item 10 | match |
| Portland $25, $125, $100, 30 days, PCC 14B.10 | 24.15 | wave1 lines 1021, 1260 | match |
| Beaverton $30, $50 to $300; Washington County $20 | 24.15 | wave1 lines 1022, 1023 | match |
| $500 to $2,000 a year refresh reserve | 24.17 | Revision 7 15.13 | carried, and the Open items say so |
| **Nabu Casa $6.50 a month** | 24.8 | nowhere in research/ or Revision 7 | **untraced** (finding 16) |

Every Code entry is three-part with a Source; the code-library routes cover the ORS, OAR and
Table 1-E citations; 16 CFR 1211.14 was read through Cornell LII at medium-high confidence.

**Obligations:** no OBLIGATIONS.md entry names chapter 24 (searched by number and topic). Met.

**Counts in prose against their lists:** "four VLANs" (4), "three tiers ... two of them" (2 of
3), "Two exceptions" (2), "three tests" (3), "Two measures" (2), "two conversions" (2), "a third
alert" (step 7 has two), "the last two steps" (18, 19), "Four statements corrected" (4) all
match. Two do not: 24.2 Professional "Two rules in the entries below narrow the paperwork at the
margins" is followed by three rules (Class 2 products, the garage-door relief, the small-systems
license waiver), and 24.8 Simple "three radio systems" counts Matter, which is not a radio (the
Applied list is Z-Wave, Zigbee, Thread). Finding 12.

## 2. The reading

### Item 1. The opening

The first sentence states the chapter's governing fact ("Every function that keeps the house safe
and usable works with the internet down"). No self-description, no inventory, no routing pile.
It runs six sentences against the two-to-five limit (template). Minor.

### Item 2. Jon's note

One header marker and two real questions (controller platform, voice at all). About the house,
nothing invented; the rural-connection reason is in answer item 1. "a concrete house will outlive
every gadget I put in it" is the first of six statements of the devices-versus-cables refrain
(finding 6).

### Item 3. The Simple path

Read in order, the seventeen blocks tell the system's story from the principle to the
commissioning test, and a non-builder can follow them. Most name something to point at (a
thumbturn, a rack, a sight gauge, a gas valve). Faults:
- **Point first (check 17).** 24.1 opens "Smart devices stop working for reasons that have nothing
  to do with the device"; the section's point (every device has a manual control) arrives in the
  fourth sentence.
- **Copular slogan openers (fault 18).** 24.13 "Video is mostly legal, and audio is the
  constraint" (also a balanced pair, fault 4, and repeated verbatim in Professional: "Audio is the
  constraint."); 24.17 "Unplugging things is the test."; 24.9 "Walls inside the network are the
  defense" (a metaphor that is not a physical comparison under section 4); 24.11 "Timing is where
  the reading matters most."
- **Closing lines built to land (v3 rule, fault 17, fault 4).** 24.11 "No phone ever starts the
  oven." 24.12 "Wearable fall sensors record a jolt and nothing else. Cameras record the room."
  24.17 "Devices get replaced every five to ten years, and the cables and the rack stay for the
  life of the house."
- **Cross-reference inside Simple (section 4 ban).** 24.12 "Those decisions belong to the
  interiors plan." The lint's Simple cross-reference gate looks for "chapter" and misses "plan".
- **Personification (fault 5).** 24.9 "a firewall decides which segment may talk to which";
  24.11 "Smart appliances in this house watch and notify"; 24.4 "any wall jack can take a new
  job" (the "jobs" family of fault 3).
- **Consecutive-block phrase.** 24.9 ends "to your phone", 24.10 ends "on your phone".
- 24.15 opens on an isocolon pair: "Watching your own cameras and deciding whether to call the
  police is unregulated. Paying a company to watch and call is a licensed service." (inherited
  verbatim from Revision 7).

### Item 4. Applied

Strong. 216 sentences, 211 steps, every one actionable tomorrow, values inline, records named
(mesh map, mask photos, code log, UPS date). The commissioning list (24.17) and the network list
(24.9) are the best Applied blocks in the loop so far. Small slips: 24.7 step 4 "Sixty minutes is
the better target" (a why); 24.13 step 13 "Treat cloud storage on it as optional" and 24.14 step 5
"Expect 6 to 12 months..." (not actions); 24.13 step 14 holds two checks; 24.10 step 9 says the
heat tape comes on "before the air reaches 32°F" while 24.10 Professional says the sensor sits "at
pipe level, not in the room air".

### Item 5. Professional

Mechanism-first in most blocks (RF loss and rebar reflection, PoE bundle heating, the protector's
bonding length, 0-10 V control-voltage drop, line-interactive VA ratings, the septic alarm's
one-third reserve). Faults, in order of weight:

- **v4 pattern, Professional restates Simple, in 10 of 17 sections** (the densest of any loop
  chapter; chapters 4, 11, 5 and 17 had one or two each):
  - 24.1 "...so a dead controller, switch or software release leaves an ordinary house run by
    hand" after Simple's "the switches, valves, thermostats and door hardware still work by hand".
  - 24.3 the dB figures restate Simple's one-sixteenth to one-two-hundredth; "Z-Wave's North
    American channels near 908 MHz penetrate concrete and masonry better" after Simple's "Z-Wave
    radios work near 908 megahertz, a lower frequency that passes through masonry better"; "Cable
    to each zone's access point takes the wall out of the radio path" after "the dependable link
    is a cable".
  - 24.5 "With the network down, the point-to-point link keeps the house's audio and video
    working" after "That link is direct and does not depend on the house network".
  - 24.7 "Every watt the rack draws ends as heat" after "turn all their power into heat".
  - 24.9 "Taken over on an isolated VLAN, a smart bulb or camera ... cannot pivot to a laptop or a
    phone" after "On its own segment, a weak camera cannot reach a laptop".
  - 24.10 "Notification-only leak detectors protect nothing while the house is empty or asleep"
    after "One that only sends a message protects nothing while you are asleep or away" (near
    verbatim, and the house is now asleep, fault 5).
  - 24.11 "So a cold oven does not start from a phone" after "No phone ever starts the oven".
  - 24.12 "Deciding which features the house gets belongs with ... the interiors chapter" after
    "Those decisions belong to the interiors plan"; "Local processing, a battery-backed hub and an
    outage-proof calling path are therefore conditions of purchase" after Simple's three tests.
  - 24.13 "Audio is the constraint." after Simple's same words.
  - 24.17 "Commissioning proves that the manual fallbacks work and that the house runs with the
    internet and the grid cut" after Simple's two tests; "Devices are consumables on a
    5-to-10-year cycle" after Simple's "every five to ten years".
  The v4 rule forbids all of these. They confirm it; they do not reveal a new pattern.
- **Professional restates Code as a statement (v2 rule, fault 28), where the lint's 6-word gate
  misses the paraphrase.** 24.2 "Anyone paid to do this wiring needs a license or a statutory
  exemption" against the entry "Paid limited-energy work takes a technician license of the right
  class", and the 24.2 third paragraph restating the three OAR entries; 24.13 "Under the stalking
  law, monitoring another person's activities by electronic means without consent counts as
  contact. Two or more unwanted contacts that would alarm a reasonable person make the crime"
  against the stalking entry; 24.15 "Under the entry below a homeowner watching the household's
  own cameras needs no license" and "Oregon's Table 1-E adds the dedicated, red-identified branch
  circuit in the entry below, with no ground-fault or arc-fault device" against the 181A.845 and
  760.41(B) entries. The worklog says the writer rewrote five such restatements "as the
  consequence"; several came out as the rule with a pointer bolted on (finding 3).
- **Abstract thesis openers and slogans (faults 42, 18).** 24.1 "Two measures keep a dead
  controller from becoming a dead house." 24.9 "Device selection screens against the NIST
  consumer-IoT baseline." 24.11 "Load shifting is the cheapest capacity on the system." 24.2 "Two
  rules in the entries below narrow the paperwork at the margins."
- **Landing closers (fault 4, fault 17).** 24.1 "Its hardware is intact and becomes electronic
  waste, because the intelligence it ran on was never in the house." 24.9 "The provider's router
  is never the house firewall." 24.10 "Beside that alarm the controller's notification is a second
  channel, never a replacement." 24.13 "Local recording, object filtering and Category 6A to every
  camera ... are the durable defaults." 24.16 "...needs no warning and keeps working when every
  electronic path fails."
- **Chiasmus (fault 4).** 24.9 "trusted initiates to IoT, and IoT never initiates to trusted."
- **Unanchored evaluatives (faults 10, 15).** 24.8 "Matter over Wi-Fi is reliable"; "Z-Wave remains
  the most reliable residential mesh"; "the worst firmware-support record of the lot"; 24.9
  "gives the most control at the firewall"; 24.13 "a mature category"; 24.7 "Their extra cost
  returns within the first lead-acid replacement" (no figure); 24.11 "commonly include" (hedge).
- **Document or standard as agent (fault 3, check 8).** 24.9 "CISA's ... Goals 2.0, NIST SP 800-213
  ... converge on segmentation"; "what the baseline asks for"; 24.12 "the rooms the camera section
  keeps cameras out of"; 24.14 "That rule also decides the power-loss behavior"; 24.11 "Building
  code reaches them".
- **Orphan fact (fault 46).** 24.6's last paragraph joins DC lighting and the ANSI A117.1 reach
  figures; 24.16 "A base station's receive log is lawful to keep, under the entry below" sits in a
  paragraph about repeater range, and the ORS 165.540(7)(a) entry it points to follows from
  nothing in the section.
- **Dangling 2026 position.** 24.6 "No 210.70 row appears in the 2026 table, so the 2026 NEC
  wording governs" without saying what it is; the Open item carries it, but the body sentence
  leaves the reader with nothing. Acceptable under the Open-items rule, awkward as written.
- No "you", no analogy markers.

### Item 6. Code

27 entries, all three-part and sourced, editions stated, none advisory. Faults:
- **A semicolon in a value line (ban 1).** 24.13: "An intimate area is a Class A misdemeanor and a
  state of nudity a Class C felony; bathrooms, dressing rooms and any enclosed space where a person
  undresses count." The lint's gate is "semicolons in prose" and skips fenced blocks. This is the
  one finding with cross-chapter reach (proposal A below).
- **"Your" in a Code requirement line.** 24.15 "Protecting your own property is outside the private
  security law." The lint checks "you" only in Professional. One-off.
- **Edition.** Every cabling entry in 24.4 cites 2023 NEC section numbers (800.179, 800.133,
  725.136, 800.26, 800.100), and 24.11 and 24.6 likewise, while the opening states that the 2026
  OESC has been in force since October 1, 2026 and the writer's own finding (OAR 918-305-0020)
  makes 2026 the edition for any permit filed now. The brief's rule (cite the document read, carry
  the current edition in Open items) is followed, and Open item 2 carries it, so this is not a
  fault. But the Who-decides row "The OESC edition the permit is filed under | Jon, at the building
  department" implies a choice that does not exist for a permit filed after October 1, 2026; the
  row should go or say the edition is fixed by the application date.
- 24.2 entry 1 "License-exempt electrical work still meets the code and takes a permit"
  (ORS 479.540(1)(a), 479.550(1)) repeats the legal chapter's entry (chapter 4, line 298:
  "...code and permit requirements still apply", ORS 479.540(1)). The v4 rule "a later chapter
  names an earlier chapter's entry" forbids it; confirms v4.
- 24.4: the Professional block says "Code entries for the Class 2 separation and PoE rules are in
  the branch-circuit and low-voltage chapter", and then the Code block carries the separation entry
  (800.133 and 725.136). Self-contradiction, and the chapter 21 entry for 725.136 states a
  different part of the rule (no shared raceway or enclosure without a barrier) from this
  chapter's (2 inches). Both are true parts of 725.136; neither chapter names the other's.
- 24.14 entry 1's requirement and value lines say the same thing twice.

### Item 7. Shapes

- Section first sentences vary; Simple first sentences vary in content, though 24.4 and 24.5 share
  the devices-versus-wires shape and four of seventeen are copular slogans (above).
- Last sentences of sections: Professional blocks close on "never" lines or summary triads in five
  sections (above).
- **Refrain (fault 40, v3 "say a thing once"): the devices-versus-cables point six times.** Opening
  "they outlast every device on them by decades"; Jon's note "a concrete house will outlive every
  gadget I put in it"; 24.4 Simple "Cables in the walls will outlast every device plugged into
  them"; 24.5 Simple "the wires to them stay in the walls for decades"; 24.17 Simple "the cables and
  the rack stay for the life of the house"; 24.17 Professional "Devices are consumables on a
  5-to-10-year cycle against a cabling layer of 20 years or more". The last two also disagree
  (life of the house against 20 years or more). The by-hand fallback appears four times, one of
  them "as the opening section states".
- **Pointer sentences (the candidate pattern, proposal B).** "in the entry below" or "entries
  below" ten times in Professional (24.2 twice, 24.4 twice, 24.6, 24.11, 24.14, 24.15 twice, 24.16,
  24.17; lines 60, 153 twice, 226, 413, 532, 568, 572, 618, 660); "Code entries for X are in the
  branch-circuit chapter" three times (24.1, 24.4, 24.6; the stats tool lists "code entries" as a
  sentence opener three times); intra-chapter section pointers "stated with the locks below"
  (24.1), "as the opening section states" and "Its terms are stated in the camera section" (24.8),
  "the camera section keeps" (24.12), "the values in the steps are 2026 planning figures" (24.13),
  "Reach figures in the mounting step" (24.6), "The recurring items in the last two steps make up
  the maintenance calendar" (24.17), "which is why no Code entry follows" (24.9), "Implementing them
  belongs here" (24.12). The brief bans "Step 2 catches" and "The order above follows from" and
  allows "the table below"; "the entry below" falls on the allowed side by the letter, and the
  section pointers on the banned side. Seventeen such sentences in one chapter is a texture: the
  writer's way of obeying the echo and later-chapter rules was to point at the rule instead of
  restating it, and the pointer is still a sentence about the text.
- No bold run-in runs, no colon fragments, no delegation endings, no research narration in the body.

### Item 8. Flow and order

Decision order is right and the worklog records the reorder (rack and A/V moved ahead of
monitoring; legal second; commissioning last). Each section follows from the last. Nothing sits in
the wrong layer except the Simple cross-reference in 24.12 and the why in 24.7 step 4.

### Item 9. Boundaries (three claims checked)

1. **Branch circuits (chapter 21, Revision 7 text).** 24.1, 24.4 and 24.6 send the R314/R315,
   404.2(C), 314.16, 725.136 and 725.144 entries to the branch-circuit chapter, and chapter 21 does
   carry them (lines 341 to 432). Agreement on the neutral and the box fill. Disagreement: chapter
   21's 21.12 says "Article 840 applies in Oregon as published" and treats the 2023 OESC as the code
   of record; chapter 24 states the 2026 OESC in force and Article 840 deleted. The writer flagged
   it. The 725.136 statement differs in which part of the rule it states (above).
2. **Electrical service (chapter 20, Revision 7 text).** 20.8 says NEC 230.67 "is required at every
   dwelling service" (line 297) with a Code entry (line 314). Chapter 24.7 says Oregon did not adopt
   230.67 in the 2023 OESC and makes it effective October 1, 2027 under the 2026 OESC, read from both
   Table 1-E editions. Chapter 24 is right; the flag for chapter 20 is filed. Each names the other
   by topic ("That rule belongs to the electrical service chapter").
3. **HVAC (chapter 23, Revision 7 text).** 24.16 Professional: "A mechanical ball-and-pedestal gas
   valve, specified in the HVAC chapter". Chapter 23 has no seismic gas valve (23.7 covers LP gas
   piping and the pressure test; no "seismic", "earthquake" or "ball-and-pedestal" anywhere in the
   manuscript outside chapter 24). The cross-reference points at a specification that does not
   exist. The answer file (item 7) mentions "item 13 of the HVAC chapter", so the content is in the
   HVAC answers but not yet in the HVAC text. Not an error in 24; a flag the writer did not file.
4. **Interiors (chapter 25, Revision 8 text, written in parallel).** Reach ranges agree (15 to 48
   inches). The aging-in-place split agrees in principle, with a small difference in posture:
   chapter 25 (line 434) says "Fall detection, remote monitoring and voice-activated emergency
   calling are wants this house states", while 24.12 Applied step 1 treats the list as open ("or
   none of them"). Each names the other by topic, and chapter 25's Who-decides row hands the
   hardware to the smart-home design, matching 24.12.
5. **Legal (chapter 4, Revision 8).** The ORS 479.540(1) owner exemption is an entry in both
   (above).

### Item 10. Poetry check

The landing closers, the slogans and the chiasmus listed under items 3 and 5. The worst single
sentence: 24.1 Professional "Two measures keep a dead controller from becoming a dead house."

### Item 11. AI tells the catalog does not name

The pointer texture (item 7). A summary triad at the end of a Professional block twice (24.12
"Local processing, a battery-backed hub and an outage-proof calling path are therefore conditions
of purchase"; 24.13 "the durable defaults"). Otherwise the chapter reads like a builder with the
drawings open: long Applied lists that are real procedures, named products, named statutes.

### Item 12. The "Unsure" list

No Unsure list is on file for chapter 24 (the writer's report is not in the worklog or the
research file). The calls the worklog and research record as judgment calls, and my ruling:

1. **Ethernet cabling under ORS 479.540(9)(f), assumed on the owner's permit.** Right call; the
   conservative assumption, with the inspector's written answer as the Open item and the first
   Applied step.
2. **2023 section numbers in the Code entries while the 2026 OESC is in force.** Right under the
   brief (cite what was read; the 2026 NEC text was not available), with Open item 2. Wrong in one
   place: the Who-decides row implying Jon chooses the edition.
3. **210.70 under the 2026 NEC left open; wireless secondaries only beside a hardwired switch.**
   Right call.
4. **Demoting the Revision 7 pointer entries (Articles 722/725/800, life-safety independence, UL
   standards, NEC 230.67) to Professional sentences.** Right; it follows the v3 pointer rule. Two
   demoted entries are missing from the Dropped list (finding 14).
5. **Keeping the ORS 165.540 entries though chapter 36 carries the same two.** Right for now; the
   recording law's subject is cameras and belongs here, and chapter 36 (later) should name this
   chapter. The flag says the whole-book pass decides; agree.
6. **16 CFR 1211.14 at medium-high confidence (quoted fragments).** Acceptable for a Code entry
   whose values (5 seconds, two attempts, one-piece and swinging doors barred) all appear in the
   quoted text.
7. **Certiorari in Project Veritas carried as an Open item, the body citing only the en banc
   ruling.** Right.
8. **"Signing supervisor" dropped to an Open item.** Right; not in ORS 479.

The flag pattern points at no brief gap: each call follows an existing rule. The one thing the
writer did not flag, and should have, is the HVAC chapter's missing gas-valve specification.

## 3. Findings, numbered

1. (v4 rule, confirmed) Professional restates Simple in 10 of 17 sections: 24.1, 24.3, 24.5, 24.7,
   24.9, 24.10, 24.11, 24.12, 24.13, 24.17.
2. (v4 rule, confirmed) Later chapter repeats an earlier chapter's entry: 24.2 entry 1 against the
   legal chapter's ORS 479.540(1) entry.
3. (v2 rule, fault 28) Professional restates Code as statements in 24.2, 24.13 and 24.15; the
   6-word lint gate misses paraphrase.
4. (NEW, cross-chapter) Semicolons in Code value lines, uncaught by the lint: 1 here (24.13), and 28
   in chapter 2, 43 in 3, 40 in 4, 10 in 22, 20 in 25, 7 in 30 (counted over value and requirement
   lines, Source lines excluded). Proposal A.
5. (candidate pattern) Pointer sentences: ten "in the entry below", three "Code entries for X are
   in the ... chapter", seven intra-chapter section or step pointers. Proposal B.
6. (fault 40, v3 rule) The devices-versus-cables refrain six times, with "life of the house"
   against "20 years or more" in one section.
7. (v3 rule, faults 4, 17) Simple blocks closing on landing lines: 24.11, 24.12, 24.17.
8. (faults 18, 42) Slogan and abstract-thesis openers: Simple 24.9, 24.11, 24.13, 24.17;
   Professional 24.1, 24.9, 24.11, 24.2.
9. (fault 4) Professional landing closers and one chiasmus: 24.1, 24.9 (twice), 24.10, 24.13, 24.16.
10. (section 4) Cross-reference inside a Simple block, 24.12 "Those decisions belong to the
    interiors plan"; the lint gate keys on "chapter".
11. (faults 3, 5) Personification: firewall decides (24.9), appliances watch (24.11), standards
    converge and ask for (24.9), the camera section keeps (24.12), the rule decides (24.14), the
    house asleep (24.10), a jack takes a new job (24.4).
12. (fault 43) Count drift: "Two rules" over three (24.2 Professional); "three radio systems"
    counting Matter (24.8 Simple).
13. (faults 10, 15) Unanchored evaluatives in 24.8, 24.9, 24.13, 24.7; "commonly include" (24.11).
14. (ban 17) Two Revision 7 Code entries (fail-safe egress locks, the gate entry) and the PoE bundle
    entry not named in the Dropped bullet, though their content survives.
15. (boundary) 24.16 cites a seismic gas valve "specified in the HVAC chapter" that chapter 23 does
    not contain; 24.4 says the separation entry is in the branch-circuit chapter and then carries it.
16. (spot value) Nabu Casa at $6.50 a month traces to no research file and no Revision 7 text.
17. Small: opening of six sentences; "your" in a Code requirement line (24.15); the Who-decides row
    on the OESC edition; three Who-decides rows whose decider is a document ("The interiors
    plan", "the site's city or county ordinance", "The water-independence plan"); one
    Decisions tag wrong ("(pending parcel)" on the 0-10 V or DALI-2 choice and DC circuits, which
    wait on the lighting and solar designs, not the parcel); 24.10 step 9 "air" against
    Professional's "pipe level"; Hikvision named as a camera maker without noting it is on the
    FCC's covered-equipment list.

What is excellent and should be held up: the verification work (eight Revision 7 and wave 1
errors corrected from the statute, rule and Table 1-E texts, including the Oregon non-adoption of
230.67 and 230.85 that two other chapters still get wrong); the Applied layer (211 steps, every
one executable, with checks and records); the decision order; the named sources; the Open items
in the right form with the research doubt kept out of the body.

## 4. Verdict

**ITERATE**, on one small, clear gap and one moderate one. Every v3 and v4 rule the chapter breaks
(findings 1 to 3, 6 to 13) is a rule the brief already states; the chapter, written under v3,
confirms the two v4 rules more strongly than any chapter so far and needs nothing new for them.
Two things the brief does not prevent:

**Proposal A (exact text, for Do 2, under "Code entries are telegraphic"):**

> **No semicolons in a Code entry's requirement or value line.** The ban on semicolons covers the
> Code layer. A value line with two parts joins them with a comma or "and", or becomes two
> entries. A Source line may separate two citations with a semicolon, and that is the only
> semicolon in the chapter.

With a lint gate: count semicolons on non-Source lines inside fenced Code blocks; target 0.
Evidence that it is a pattern: 149 value-line semicolons across seven of the eleven Revision 8
chapters checked (2, 3, 4, 22, 24, 25, 30), none caught because the gate reads "semicolons in
prose", and none named in loop rows 1 to 8. If the orchestrator decides instead that Code is
exempt, STYLE_GUIDE section 10 item 1 needs the exemption written in; one or the other.

**Proposal B (exact text, for Do 2, after "Echo is any statement, not only a number"):**

> **Point at a rule at most once per section, and never point at the text.** When Professional
> leaves a rule to its Code entry or to another chapter, it states what the rule does to the house
> (the mechanism, the consequence, the reason) and lets the entry or the other chapter state the
> rule. "In the entry below" appears at most once per section. Another chapter's rule is named by
> its subject: "The branch-circuit chapter states the neutral and box-fill rules", never "Code
> entries for X are in the Y chapter". A sentence that points at another part of this chapter ("as
> the opening section states", "its terms are stated in the camera section", "the values in the
> steps", "the recurring items in the last two steps") is cut: state the fact, or trust the reader.

Evidence: 20 pointer sentences in chapter 24 (10 "entry below", 3 "Code entries ... are in", 7
section or step pointers); "whose Code entry is in the land chapter" in chapter 5; "(second entry
below)" in chapter 11; "as the opening section states" in chapter 30 and "The water-rights section
states", "The access section states" in chapter 3. The heavy instance is one chapter, so this is a
moderate pattern; the reason to write it now is that v4's two new echo rules (later chapter names
the earlier entry; Professional does not repeat Simple) push every writer toward exactly this
substitute, and chapter 24 shows what it looks like at scale.

Lint suggestions that go with the findings (not brief changes): the Simple cross-reference gate
should also catch "the X plan" and "the X section"; the "you" gate should also scan Code blocks.

## 5. Redo before the mass wave?

**Yes.** The research, the corrections and the Applied layer are among the best in the book and
must be kept as they stand; the redo is a revision of Professional and the Simple endings, not a
rewrite. Reasons: Professional restates Simple in ten sections and Code in three, the densest of
any loop chapter; the pointer texture (20 sentences) and the six-time refrain would be fixed by v4
plus proposal B; and the chapter was written on Opus, which the Fable-for-writers rule already
lists for a redo. A writer working from this text under the final brief should keep every value,
citation and step and change only the sentences named in findings 1 to 3 and 5 to 13.
