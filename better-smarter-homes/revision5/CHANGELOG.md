File: `CHANGELOG.md`

# Revision 5 Changelog

Last updated: 2026-07-09

This file holds historical notes that no longer belong in the active TODO. It is the project-wide historical log; Revision 6 batches are recorded here too.

## 2026-07-10 External-Review Polish Pass, Chapters 2-7

- The user ran chapters 2-7 through the external reviewer (`revision6/deepseek review.md`); every chapter's verdict was "ready," with tuning observations. Sixteen fixes applied across the six chapters (itemized in `revision6/AI_TODO.md`): residual aphorisms and one isocolon removed, one Code-entry fossil verb fixed, the septic cost claim anchored to its table's endpoints, an insurance generalization qualified, the ready-mix strength table reconciled to the project's 4,000 psi standard, IPC 1107 secondary-drainage citation added, and five small practical gaps closed (mixed-soil compaction, AFI lookup source, sump backup comparison, cold-weather strength verification, special-inspector trigger pointer). Two reorganization suggestions (splitting 7.13 out; shrinking 4.10) logged as open user decisions; no content moved or cut. Verification sweep clean. Session closed at 93% context, 48% five-hour.

## 2026-07-10 R6-3 Run One: Chapters 2-7 Complete

- On the user's "write the rest of the book" green light (following the external reviewer's ship-it verdict on chapter 1), completed the Revision 6 treatment of chapters 2 through 7 in one session, with the full lint battery, fossil grep, and Source-line verification after each chapter, and a live burn check (context window and 5-hour usage) after each chapter per the user's monitoring protocol.
- Chapters 2-3: excavation passes (fourteen fossil fixes total; already in the Revision 6 register from calibration).
- Chapter 4 (legal): full treatment; all 8 Code blocks to three-part format (~44 entries); duplicated Professional paragraph removed; 3 Simple blocks added; ORSC R105.5 permit-expiration research integrated; ORS 447.060(1)(a) companion cite added; 12 long sentences split.
- Chapter 5 (soil): full treatment; 6 Code blocks converted; ASTM D4318 withdrawal noted at both citations; 2 Simple blocks added; the twelve principles rewritten off the aphorism register; geotech consult cost anchored.
- Chapter 6 (structural): full treatment; 11 Code blocks converted; 3 Simple blocks added (design-path costs, CMU definition, concrete durability); ACI 318 edition caveat carried forward.
- Chapter 7 (foundation/concrete, the book's largest at 14,860 words): full treatment; 18 Code blocks converted with zero missing sources; 3 Simple blocks added; the owner-mixed concrete research preserved intact.
- Burn record: session spanned context 71% to 90% and 5-hour 23% to 44%; per-chapter context cost ran 5-10%. Stopped before chapter 8 per the user's rule (the next chapter no longer fits with verification and handoff margin). The statusline was patched this session to persist its payload for on-demand checks, with the command saved to persistent memory.
- Files touched: `revision6/manuscript/` chapters 2-7, `revision6/AI_TODO.md` (per-chapter ledger entries and next-session pointer), this changelog.

## 2026-07-10 Final Polish After Third External Review (R6-2c)

- Third external review on the root-metaphor-corrected chapter 1: register rated roughly 95% pure. The user protected three items as his own words, now listed in the style guide's Owner's Voice section: the first-person opening sentence pair, "This book is the plan," and the "thousand-year structural shell" goal label. External-review suggestions against protected lines are overruled by standing owner decision.
- The review's central finding, a verb-object agreement failure ("Recorded decisions can be built, inspected, and repaired by people other than the person who made them" attaches work verbs to an information noun), produced two new style guide sections: Verb-Object Agreement and The Reader's Context (referents named in-sentence, causal chains written out, no cross-paragraph anaphora), plus judgment checks 10-12 and `IMPROVEMENT_PLAN.md` Issue 12.
- Chapter 1 repaired and expanded, information only: the transferability paragraph now states the full chain (record to contractor to inspector to future repairer); Revision 2's structural means for the thousand-year goal restored (low-permeability concrete, pozzolanic admixtures, corrosion-protected reinforcement, generous rebar cover); shorter-lived components and service-system design rules reformatted as vertical lists with context and a pointer to the maintenance chapter; the durability worked example moved from the principle row to a standalone line; the wood exclusion recast as "the absence of wood framing determines the applicable code path, fire-behavior assumptions, and engineering requirements"; the metadiscursive Applied verb-list sentence deleted.
- Verification: zero text-as-agent fossils, standard battery clean, protected lines intact, 2,175 words at a 15.9-word prose average.
- Files touched: `revision6/writing_style_guide.md`, `revision6/IMPROVEMENT_PLAN.md`, `revision6/AI_TODO.md`, `revision6/manuscript/g1_ch_01_...md`, this changelog, and the persistent-memory note.

## 2026-07-10 Root-Metaphor Correction After Second External Review (R6-2b)

- The user ran the corrected chapter 1 through the external reviewer again. The reviewer's unified diagnosis: the fix removed the rhetorical schemes but kept the conceptual metaphor system that generates them; the text still treated the book as a person (carrying, answering, having jobs, saying), information as a physical object (traveling, being handed), the reader as a staged character, and specifications as performances (contrastive negation, permission-hedges, requirements attributed to abstract entities). The user's order: follow the diagnosis without exception; the book does not do anything.
- Added The Root Metaphors section to `revision6/writing_style_guide.md`: the book is a structured reference (document elements only contain, list, state, specify, define, describe, include, provide, record, identify, document); information is present or absent, never moving; the reader is an agent executing tasks (imperatives permitted, staged scenes banned); specifications are stated, not performed (positive statement over contrastive negation, actor-plus-action requirements, no permission-hedges). Added the fossil table (carry/answer/give/travels/jobs/runs-on/sooner/by-design with corrections), three lint patterns, two judgment checks, and corrections to the guide's own exemplars.
- Updated `IMPROVEMENT_PLAN.md` (Issue 11) and `PROBLEMS_AND_GOALS.md` (root-metaphor layer added to the failure history).
- Rewrote chapter 1 only, per the user's instruction: four functions as noun phrases; service-system rules as actor-plus-action imperatives; the wood-framing exclusion stated once with its regulatory consequence; the layer table's question column replaced with "Information provided" noun phrases; reading patterns restated as document properties; gnomic and unanchored lines removed ("A build runs on...", "wear out sooner by design"); headings renamed to Supporting Elements, Contents By Chapter Range, and Out Of Scope. Content preserved: all tables, lists, and facts, including the seismic-design row and third-party-handoff pattern from the first review.
- Verification: zero text-as-agent fossils (grep), document-subject verb audit clean against the approved list, standard lint battery clean, 1,974 words at a 14.4-word prose average.
- Chapters 2 and 3 still predate these rules and are queued for the same excavation after the user reviews chapter 1.
- Files touched: `revision6/writing_style_guide.md`, `revision6/IMPROVEMENT_PLAN.md`, `revision6/PROBLEMS_AND_GOALS.md`, `revision6/AI_TODO.md`, `revision6/manuscript/g1_ch_01_...md`, this changelog, and the persistent-memory note.

## 2026-07-10 Register Correction After External Review (R6-2a)

- The user ran the new chapter 1 past an external reviewer (DeepSeek), which identified quiet performance that the surface-pattern lint missed: gnomic wisdom lines ("A house is the sum of thousands of small decisions"), balanced pairs and chiasmus ("Internet improves the house. Internet does not run the house."; "A cheap choice that causes hidden long-term damage is not cheap"), isocolon ("build the shell so it can stay, and route the service systems so they can change"), hedge stacks ("Informally... literally"), unanchored size words ("costs little... costs a lot"), and vignettes implying claims without stating them ("You can hand one chapter to a contractor and have a useful conversation"). The user's standing order: remove the performance, keep the instructions.
- Rebuilt `revision6/writing_style_guide.md`: new Voice Target (every sentence states a requirement, a fact, an instruction, a value, or a source; two permitted modes; the quotable-to-usable test), the generalized performance ban (function, not surface pattern), new contract items (property plus mechanism, no unanchored size words with a no-invention guard, no conversational hedging, metadiscourse confined to overviews), per-layer register rules (explanation lives only in Simple and design-rationale notes), a quiet-performance example table built from the calibration failures, re-audited exemplars (two of the guide's own examples carried the disease), extended lint patterns (hedges, self-narration, anaphora screen, size words) and an expanded judgment checklist, and a rewritten compact working prompt.
- Updated `IMPROVEMENT_PLAN.md` (Issue 10: quiet performance, with overcorrection guards) and `PROBLEMS_AND_GOALS.md` (three failure modes, one root: sentences written for admiration instead of use).
- Re-passed chapters 1-3: chapter 1 fully rewritten, including DeepSeek's content suggestions (third-party-handoff reading pattern added, seismic-design row added to the at-a-glance table, principles-versus-habits distinction stated, capitalization consistency checked); chapters 2 and 3 corrected in place, fifteen performance instances rewritten (inspector antithesis, "make it heavier" negation, killer-questions phrasing, easement/February epigram, July/January epigram, utility vignette, and others). Energy-independence expansion flagged as an open design question for the user, not written.
- Verification: extended lint battery clean across all three chapters (zero em dashes, antithesis, decorative intensifiers, stock phrases, BSH, hedges, self-narration, unanchored size words outside established band names); every `Code` entry retains its three-part format with Source line; prose sentence averages 14.8/14.6/15.1 words with remaining 30-plus-word sentences being genuine list-carriers.
- Files touched: `revision6/writing_style_guide.md`, `revision6/IMPROVEMENT_PLAN.md`, `revision6/PROBLEMS_AND_GOALS.md`, `revision6/AI_TODO.md`, the three chapter files, this changelog, and the persistent-memory working-style note.

## 2026-07-10 Revision 6 Calibration Batch: Chapters 1-3 Rewritten (R6-2)

- Rewrote `revision6/manuscript/` chapters 1, 2, and 3 into the Revision 6 voice on the user's go signal, in the main session without sub-agents. This is the calibration batch; work stops here for the user's review before any further chapters.
- Voice results: prose sentence averages 13.9/14.3/15.0 words (the Revision 5 group ran 17.0; Revision 2, the benchmark, ran 11.3); sentences of 30 or more words at 4.1/2.5/3.3 percent (Revision 5: 10.1; Revision 2: 2.9). Direct address restored at dosage; chapter openers rewritten off the serial-list formula; the chapter 1 numbering gap (missing 1.4) closed.
- Format results: every `Code` entry across all three chapters converted to the three-part format (requirement, exact value, Source line), script-verified with zero entries missing a source; chapter 1's four-layer section now teaches the new format with the anchor-bolt example; chapter 2's 2.7 rewritten to match. Simple blocks restored (chapter 3: six, adding title/rights, utilities, septic, and topography; chapter 2: four). Layer echo deleted (chapter 2's 2.4 duplicated path definitions).
- Research integrated: the wildfire-map repeal and R327 local-opt-in rule (chapter 3 climate, zoning checklist, purchase review, and a Code entry); the 2026 perpetual septic operation-and-maintenance contract obligation (chapter 3 septic section and Code block); current code editions with 2026-edition notes and the Table 1-E amendment date (chapter 2); the owner-builder no-three-year-clock rules as a citation list (chapter 2).
- Content preservation: all tables, lists, citations, cost ranges, and facts carried forward; word counts 2,399 to 2,308, 3,695 to 3,387, and 5,419 to 5,185, with the deltas from echo deletion and shorter connective prose, plus new research content added.
- Lint battery: zero em dashes, antithesis, decorative intensifiers, stock phrases, project-name abbreviations, or citation-free Code entries; four decorative intensifiers found and fixed during the pass; eight over-length sentences found and broken up; personification screen hits reviewed and confirmed as human-subject false positives.
- Files touched: `revision6/manuscript/g1_ch_01_...`, `g1_ch_02_...`, `g1_ch_03_...`, `revision6/AI_TODO.md`, this changelog.

## 2026-07-10 Folder Rename And Sub-Agent Throttle

- Renamed `revision6/need_researching/` to `revision6/done_researching_second_wave/` per the user: the second research wave is complete, so the folder name is now past tense and parallel to `done_researching/`. Updated all current-doc references (root `CLAUDE.md`, `revision5/AI_TODO.md`, and the five `revision6/` control docs); entries below this one keep the old name as historical record.
- Recorded the user's sub-agent throttle decision in root `CLAUDE.md`, the Revision 6 TODO standing rules, and persistent memory: at most three background agents at once (one or two preferred) so the user can pause between launches. Context: the 14-agent research burst consumed the user's entire 5-hour token allowance; his estimate puts subscription processing at roughly 200x cheaper than equivalent API pricing, but pausability matters more than parallel speed.

## 2026-07-09 Revision 6 Research Pass Complete (R6-1.5)

- Ran the full research pass on `revision6/need_researching/research_questions_revision6.md` using 14 parallel background research agents (all launched simultaneously; no concurrency limit encountered). All 26 items answered: 13 SETTLED, 13 SETTLED-WITH-EDITION, zero blocked or malformed. Each answer verified for format (Answered header, inline sources, single status tag from the fixed list) and merged into the research file directly below its item; per-item answer files preserved in `revision6/need_researching/answers/`.
- Corrections to earlier research assumptions discovered by the pass: Oregon Table 1-E strikes the entire NEC 210.8(D) appliance-GFCI list and un-adopts dishwasher GFCI in 422.5(A); SB 83 (2025) repealed the statewide wildfire hazard map, making ORSC R327 local-opt-in (five adopting jurisdictions to date); Oregon's adopted G2417.4.1 gas test is 10 psi for 15 minutes (60 psi for 30 minutes welded), not the model 3 psi for 10 minutes; the CO-alarm at-sale trigger is ORS 105.838 (not ORS 476.725); 2025 Or Laws ch. 78 changes only PEO terminology in ORS 701.010 (sale rules verbatim unchanged, diffed); ORS 12.135 renumbered by 2025 c.578 (10-year residential repose, HOA window added); the 2023 ORSC does not reference ICC A117.1 anywhere (accessibility attaches via OSSC; cite A117.1-2017; no 2024 edition exists, only Supplement 1); OAR 340-071-0132 (new, effective 2026-01-01) requires a perpetual septic O&M contract with certified provider and a 30-day transition at sale; ASTM D4318 withdrawn 2026 with no replacement; base NISTIR 8259 withdrawn April 2026, superseded by IR 8259 Rev. 1; no EV-ready or solar-ready requirement reaches one- and two-family dwellings (ORS 455.417 scope; solar-ready appendix state-preempted); Oregon CMV/CDL threshold is weight-based with no commerce element (Class A CDL to tow a 26,001+ lb combination even personally); UpCodes found serving pre-amendment R310.1 text (lag documented; official PDFs control).
- Library additions found during the pass: `25omsc-matrix.pdf` (the live but unlinked 2025 OMSC amendment matrix) and `calculator-orsc-tradeoff.xlsx` (the BCD envelope trade-off workbook for the concrete-roof UA path); README updated.
- Files touched: `revision6/need_researching/research_questions_revision6.md` (status note + 26 merged answers), `revision6/need_researching/answers/` (26 new files), `revision6/AI_TODO.md`, `revision6_code_library/` (2 additions + README), this changelog.
- Next action: the R6-2 calibration batch (chapters 1-3) awaits the user's go signal. Nothing blocks it.

## 2026-07-09 Revision 6 Environment Build (R6-1)

- Created `revision6/`: `manuscript/` copied forward from `revision5/manuscript/` (file names unchanged), `done_researching/` holding copies of the seven answered research files, and `need_researching/research_questions_revision6.md` consolidating every unresolved flag from those files into 26 researchable items (two tiers, several answerable from documents already downloaded) plus standing not-external-research tags (AHJ design-pass list, professional-review list, purchase-only standards, time-sensitive quotes, closeout self-audit). Improved the research-AI instructions: fixed named status tags replacing the inconsistent per-pass UNRESOLVED numbering, a check-the-library-first rule, and a consistent answer format.
- Applied the user's decision "no BSH abbreviation": removed the BSH glossary row from the Revision 6 manuscript copy (the only remaining manuscript instance); added the project-name rule and a `\bBSH\b` lint check to the Revision 6 style guide. Revision 5 files unchanged.
- Moved the three root `REVISION6_*` docs into `revision6/` as its control docs: `writing_style_guide.md` (the new style instructions), `WRITING_STYLE_ANALYSIS.md`, `IMPROVEMENT_PLAN.md`; wrote `revision6/PROBLEMS_AND_GOALS.md` (problems in every previous revision and the Revision 5 → 6 changes) and `revision6/agent.md`; created `revision6/AI_TODO.md` as the active recovery anchor and reduced `revision5/AI_TODO.md` to a closed-out pointer.
- Expanded `revision6_code_library/`: ORS chapters 12, 447, 671 added (now 15 chapters), full OAR rule text for 340-071 (onsite wastewater, 2026 rules), 340-073, and 918-305 from the SOS database, DEQ minimum-separation-distances table, BCD blower-door reporting form, and the slab-edge insulation technical bulletin. README updated.
- Updated root `CLAUDE.md` to the new layout.
- Verification: consolidated unresolved blocks extracted and cross-checked from all seven research files (`UNRESOLVED` grep counts: ch17-20 49, ch21-24 20, phase2 29, plus the four Limits sections in ch05-08/ch09-12/ch13-16); `\bBSH\b` grep across `revision6/manuscript/` returns zero hits; all downloads size- and format-checked (the one failed PDF, the DEQ combined rules document, was replaced by the full SOS rule text).

## 2026-07-09 Revision 6 Preparation Session (No Manuscript Changes)

- Audited the completed 21-chapter Phase 2 manuscript against Revisions 2, 3, and 4. Findings recorded in root `REVISION6_IMPROVEMENT_PLAN.md`: sentence bloat in the newest chapters (26.4-word average, 34.9% of sentences 30+ words in Ch 9–21), Simple-layer collapse in Ch 11–21 (one Simple block per chapter against 13–15 of each other layer), quota-pattern layer echo, 28 citation-free `Code` blocks concentrated in Ch 20/21/15, cost framing still at roughly a quarter of the Revision 2 density, near-zero direct address, and mild personification creep in the 2026-07-09 batch. Strengths confirmed: technical substance, research integrity, Ch 9 and Ch 16 as structural models.
- Updated root `REVISION6_STYLE_GUIDE.md` with the owner's expanded four-layer audience definitions, a three-part `Code` entry format (requirement, exact point, source line), anti-quota and layer-echo rules, and new lint checks.
- Built root `revision6_code_library/`: downloaded the free official Oregon documents (ORSC Chapter 1 PDF, ORSC/OESC/OMSC/OSSC errata and amendment PDFs, the full 2025 OEESC, 12 ORS chapter HTML files, 5 OAR division indexes) and verified working online routes for the copyrighted code text (UpCodes serves full ORSC/OESC section text and is machine-readable; ICC and IAPMO viewers are browser-only). See its `README.md`.
- Rewrote `AI_TODO.md` as the Revision 6 process anchor: Revision 5 chapters complete, appendices/front matter deferred to closeout, five-phase Revision 6 plan with a three-chapter calibration gate. The detailed Revision 5 batch history that previously lived in the TODO is preserved in this changelog (entries below).
- Files touched: `AI_TODO.md`, `CHANGELOG.md`, root `CLAUDE.md`, root `REVISION6_STYLE_GUIDE.md`, new root `REVISION6_IMPROVEMENT_PLAN.md`, new root `revision6_code_library/`. No manuscript files changed.

## 2026-07-09 Phase 2 Rewrite Of Chapters 10–21 (All Chapters Now Drafted)

- Rewrote Chapters 10 through 21 from their Phase 1 versions into Phase 2 form, following the pattern set by Chapters 1–9: labeled four-layer blocks, colon-format `Code` blocks carrying real Oregon and national code sections, topic-based cross-references, and removal of the Phase 1 aphorisms and antithesis. With Chapter 9 (rewritten 2026-07-07), all 21 chapters are now drafted in Phase 2 form.
- Each chapter grew substantially (roughly doubling): Ch 10 ~5,500, Ch 11 ~4,600, Ch 12 ~4,600, Ch 13 ~4,900, Ch 14 ~5,300, Ch 15 ~4,500, Ch 16 ~3,200 (information-dense standards library), Ch 17 ~4,800, Ch 18 ~3,900, Ch 19 ~4,200, Ch 20 ~4,000, Ch 21 ~3,400 words.
- Research basis: the answered verification passes in `research_questions_ch09_ch12.md`, `ch13_ch16.md`, and `ch17_ch20.md` (including the Ch 19, 20, and 21 passes the user appended 2026-07-09), plus the CMU and equipment research in `research_questions_phase2_owner_fabrication_and_equipment.md`. No fabricated citations.
- Correction recorded: an earlier session incorrectly reported Ch 12, 19, 20, and 21 research as missing. That was a detection error (a grep for level-1 `# Chapter` headers missed a level-2 `## Chapter 12` answered pass and the later-appended passes). The user confirmed and completed the 19/20/21 passes; all four chapters were then written from the answered research.
- Respected every UNRESOLVED flag in the research: local/AHJ items (energy path, county checklists, reach codes, rental quotes, wildfire-map designation) framed as verify-locally; product- and counterparty-specific items (manufacturer startup, insurer/lender terms) framed as collect-at-spec/confirm-with-agent; purchased-standard exact values and standards editions framed as confirm-before-normative-use; and all legal, tax, and insurance decisions in Chapters 20 and 21 routed to an attorney, CPA, or agent with no firm claims.
- Key guardrails honored: OPSC/OESC citations (not ORSC plumbing/electrical) in the testing chapter; blower door as one of two compliance options; owner-performed concrete tests have no acceptance standing; do-it-yourself soil testing is screening only; refrigerant work routed to EPA 608 and backflow to a certified tester; no fake certification claims; the business entity owns only intangibles and never the house or construction; the plan library sold as unstamped single-build-license reference material with the architecture/engineering title rules observed.
- Verified with the style scans across Chapters 9–21: no em dashes, no old acronym or personal-name leaks, no forbidden decorative intensifiers. Minor fixes applied during the pass (a compressed antithesis in Ch 13, a handful of "very"/"simply"/"actually" instances, one em dash and one "actually" in Ch 21).
- Files touched: `manuscript/g1_ch_10_...` through `g1_ch_21_...` (12 chapters), plus `manuscript/g1_ch_09_...`, `g1_ch_03_...`, `g1_ch_04_...`, `g1_ch_08_...` (earlier in the run), `AI_TODO.md`, and `CHANGELOG.md`.

## 2026-07-07 Chapter 9 Phase 2 Rewrite; BSH Expanded To Better Smarter Homes

- User lifted the Chapter 9 acceptance gate and directed the Phase 2 rewrite to continue.
- Rewrote `g1_ch_09_plumbing-water-supply-pressure-treatment-and-hot-water.md` from the Phase 1 version (3,761 words) into a Phase 2 chapter (about 7,900 words). Preserved all prior coverage; upgraded every `Code` block from vague "verify with the current OPSC" prose into colon-format citations carrying real 2023 OPSC, ORSC Chapter 11, OAR, ASSE, NSF, and AWWA/ASTM sections and their content.
- Source basis: the current Revision 5 chapter, the answered Chapter 9 verification pass in `research_questions_ch09_ch12.md`, and the Chapter 9 crosswalk row. No fabricated citations. Code edition anchored to the 2023 OPSC (effective February 9, 2024, based on the 2021 UPC); the 2026 OPSC and 2026 ORSC heat-pump provisions are noted as in-progress and not written against.
- New section structure 9.1–9.18 covering supply boundary, wet-zone planning, source selection, service and distribution sizing, well system controls, indoor potable storage, tiered water testing, the sequential treatment train, pressure control, pipe materials, water hammer, hot water generation (HPWH), Legionella/scald temperature architecture, demand-control recirculation, backflow, rainwater and outdoor water, freeze protection, and inspection/commissioning/records.
- Removed the Phase 1 style violations (aphoristic closers, emotional "feel"/"sound cheap" language) and referred to the project as "Better Smarter Homes"/"this project" rather than the acronym.
- Verified with the style scans: no em dashes, acronym leak, displayed forms, or banned intensifiers/personification after fixes.
- Expanded "BSH" to "Better Smarter Homes" in the Chapter 4 legal-marketing table (ORS 672.007 section) per the user's decision. A glossary definition entry for "BSH" remains in `g2_app_02_glossary.md` for the later glossary audit; flagged for the user.
- Files touched: `manuscript/g1_ch_09_...md`, `manuscript/g1_ch_04_...md`, `AI_TODO.md`, `CHANGELOG.md`.

## 2026-07-07 Phase 2 Chapters 7–8 Confirmed, Research Pauses Cleared, Ch 1–8 Scan Pass

- Cleared the stale research pause on Chapter 7. The "Resolved Research: On-Site Concrete Mixing For An Owner-Builder" section in `research_questions_phase2_owner_fabrication_and_equipment.md` is answered, sourced, and verified, with no blocking UNRESOLVED items. The dependent make-versus-buy material is already written into manuscript section 7.13 (`Make-Versus-Buy: Ready-Mix Or Owner-Mixed Concrete`), integrating mix design, bulk sourcing, mixing equipment, field testing, documentation, the building-official path, and washout, with a colon-format Code block.
- Confirmed Chapters 7 and 8 are drafted in Phase 2 form (labeled four-layer blocks, colon-format Code blocks, topic-based cross-references, topic-stating overviews). Chapter 7 is 14,846 words; Chapter 8 is 7,919 words. This Phase 2 work and the research integration were completed by prior sessions that did not update `AI_TODO.md` or this changelog; this entry records them and resynchronizes the recovery anchor.
- Cleared the stale research pauses on Chapter 16 (owner-manufactured CMU) and Chapter 17 (heavy-equipment selection). Both are answered and sourced in the same research file, with a small number of items still flagged UNRESOLVED at the end of each section; those items gate only their dependent manuscript claims, not the chapters as a whole.
- Ran the verification scans across Chapters 1–8 for em dashes, old project acronym, displayed forms, blockquote pronouncements, fragile navigation, stock AI phrases, persuasive headings, decorative intensifiers, and personification.
- Fixed three decorative-intensifier hits: "truly unpaid" in Chapter 4 (rewritten to "unpaid ... no wages and no in-kind compensation"), "very different bands" in Chapter 3 (dropped "very"), and "very little inherent insulating value" in Chapter 8 (dropped "very").
- Reviewed and kept the standard technical uses of "very" (NRCS "very poorly drained" drainage class, geotechnical "very stiff clay," ACI 318 "very severe" sulfate class S3, "very low thermal conductivity" for FRP ties) and the substantive "actual/actually" contrasts.
- Flagged one open question for the user: whether the "BSH" brand abbreviation in the Chapter 4 legal-marketing table (ORS 672.007) should be expanded to "Better Smarter Homes." Left unchanged pending the user's decision.
- Files touched: `AI_TODO.md`, `CHANGELOG.md`, and manuscript Chapters 3, 4, and 8.

## 2026-05-08 Control Filename Prefix Removed

- Removed the old revision prefix from the copied control docs, leaving `DOC_INDEX.md`, `STRUCTURE_PLAN.md`, `SOURCE_CROSSWALK.md`, and `GLOSSARY_POLICY.md`.
- Updated active documentation references, startup instructions, handoff pointers, research notes, findings files, and folder paths to use the prefix-free filenames.
- Rebuilt `SOURCE_CROSSWALK.md` so each current Revision 5 target shows its immediate predecessor path, Revision 3 source path, Revision 2 source-history path, and active Revision 5 research notes.
- Left the active manuscript queue unchanged.

## 2026-05-07 Chapter 1-8 No-Personification Retrofit Applied

- Applied `RETROFIT_CH1_CH8.md` to Chapters 1 through 8.
- Rewrote personified and over-emotional object language around the book, property, site, land, soil, code, water, concrete, foundation, structure, envelope, records, and drainage.
- Replaced the known failures in Chapter 1 and Chapter 3, including "argued with," "stay interested," and "property has to work with."
- Kept technical content, tables, Code citations, decision frameworks, inspection gates, and record logic intact.
- Verified with the retrofit scans for citation separators, old acronym and revision-history terms, banned punctuation and stock phrases, fragile navigation, displayed-form patterns, and no-personification terms. Remaining navigation hits are chapter headings or external code/standard chapter citations; remaining form hits are ordinary construction uses of "fill"; broad no-personification regex hits were reviewed as false positives.
- Updated `AI_TODO.md` so Chapter 9 remains blocked until the user confirms the Chapters 1 through 8 rewrite is acceptable.

## 2026-05-07 Chapter 1-8 Retrofit Scope Tightened

- Renamed `RETROFIT_CH1_CH7.md` to `RETROFIT_CH1_CH8.md` so Chapter 8 is explicitly in scope before Chapter 9 begins.
- Updated `AI_TODO.md` so the active manuscript task is to apply `RETROFIT_CH1_CH8.md` to Chapters 1 through 8, including removal of every personification issue described in `writing_style_guide.md`.
- Strengthened `writing_style_guide.md` so readable prose comes from clear sequence, exact nouns, active verbs, useful comparisons, and specific construction detail, not emotions applied to objects or cute, jolly, sentimental, over-cheerful tone.
- Updated `DOC_INDEX.md` to point to the Chapter 1-8 retrofit plan.

## 2026-05-07 No-Personification Style Rule Added

- Diagnosed Chapter 1 and Chapter 3 personification as a mismatch between broad warmth/positive-voice guidance and the absence of a loud no-personification rule in `writing_style_guide.md`.
- Added a prominent `Absolute Rule: No Personification` section to `writing_style_guide.md`.
- Reworded nearby Core Voice lines so warmth and curiosity belong to the writer/prose, not to inanimate subjects.
- Added no-personification checks to Standing Lessons, Pre-Submission Check, and the compact working prompt.
- Updated `AI_TODO.md` to pause further chapter writing and block Chapter 9 until the user is satisfied with the current rewrite.

## 2026-05-06 Chapter 8 Expansion Completed

- Expanded `manuscript/g1_ch_08_envelope-waterproofing-thermal-performance-and-radon.md` from 507 lines to 746 lines.
- Integrated mapped Revision 3 and Revision 2 envelope source material, Chapter 8 research notes, and current official Oregon BCD/OHA checks for residential energy, blower-door, and radon requirements.
- Added Oregon energy compliance mapping, envelope value table, additional-measure and blower-door guidance, insulation-material and foam-protection guidance, wall tie limits, below-grade envelope interface, slab-edge continuity, roof/parapet treatment, radon county applicability, vapor/drying guidance, envelope testing, IAQ coordination, and pre-cover acceptance checks.
- Kept the below-grade waterproofing split with the foundation chapter to avoid duplicating the full R405/R406 foundation sequence.
- Verified Chapter 8 and combined Chapters 1 through 8 with style and cleanup scans; remaining displayed-form-pattern hits are ordinary construction uses of "fill."
- Updated `AI_TODO.md` so Chapter 9 expansion is the next active manuscript task.

## 2026-05-06 Chapter 1-7 Style Retrofit Completed

- Retrofitted Chapters 1 through 7 to the current warmer, grounded `writing_style_guide.md`.
- Standardized Chapter 5 Code citation separators from hyphen format to colon format.
- Removed old-acronym prose references from Chapters 4 through 7.
- Rewrote reader-facing revision-history language in Chapters 1, 4, 6, and 7 while preserving the technical guidance.
- Reworked fragile navigation wording, selected section headings, and theatrical phrasing in Chapters 1 through 7.
- Verified the retrofit with the scans from the original Chapter 1-7 retrofit plan, now superseded by `RETROFIT_CH1_CH8.md`; remaining navigation/form hits are expected external code or standard chapter citations, chapter headings, and ordinary construction uses of "fill."
- Updated `AI_TODO.md` so Chapter 8 expansion is the next active manuscript task.

## 2026-05-06 Documentation Cleanup

- Condensed `AI_TODO.md` to fresh-start order, workflow, active batch, queue, and next action.
- Condensed `AI_HANDOFF_PLANSMART.md` to mission, recovery protocol, and pointers.
- Condensed `agent.md` to purpose, source rule, and recovery rule.
- Condensed `DOC_INDEX.md` to the documentation role table.
- Condensed `designer_notes.md` to layout, label, color, forms, and production-source guidance.
- Kept `writing_style_guide.md`, `GLOSSARY_POLICY.md`, `STRUCTURE_PLAN.md`, and `SOURCE_CROSSWALK.md` unchanged.

## 2026-05-06 Chapter 1-7 Retrofit Planning

- Added the original Chapter 1-7 retrofit plan, now superseded by `RETROFIT_CH1_CH8.md`.
- Updated `AI_TODO.md` so the retrofit is the immediate active task before Chapter 8 expansion.
- Added the retrofit file to `DOC_INDEX.md`.

## 2026-05-06 Style Guide Direction Change

- Rebuilt `writing_style_guide.md` into a shorter guide with a warmer, grounded, informative voice.
- Removed the old sharper-voice emphasis that no longer matched the new warmer technical style.
- Added practical risk handling: name the issue, then give the cleaner path, workaround, solution, or next step.
- Added the rule that reader-facing text should not expose revision history or manuscript-development commentary.
- Added colon-format citation guidance for Code blocks.
- Added guidance to remove the old project acronym naturally from future manuscript work.

## Manuscript Expansion History

- Chapters 1 through 7 have been expanded once in Revision 5.
- Chapter 1 was rewritten into a shorter orientation chapter and kept mostly single-voice.
- Chapter 2 was rewritten as a code and compliance map, not as a code-reference appendix.
- Chapter 3 was rewritten as the land, site, and feasibility filter.
- Chapter 4 was expanded as the legal, permit, owner-builder, and inspection chapter.
- Chapter 5 was expanded as the first deep technical soil and ground-prep chapter, then repaired after the layer-collapse audit.
- Chapter 6 was expanded as the structural system and concrete design chapter.
- Chapter 7 was expanded as the foundation, basement, slab, and concrete placement chapter.
- Chapter 8 is the next expansion target unless the user redirects.

## Earlier Setup History

- Revision 5 control documentation was created.
- Active manuscript files were moved into `revision5/manuscript/`.
- File and folder names were normalized to remove spaces.
- Research files were created by chapter range.
- A source crosswalk was created so future sessions can find mapped source paths without guessing.
- The first-pass Revision 5 manuscript scaffold was found to be too small and is being expanded chapter by chapter.

2026-07-10 (Revision 6, R6-3 batch: chapters 8-12). Chapter 8 (envelope) full rewrite under the user's new expansion mandate: 7,918 to ~11,480 words, 12 old-format Code blocks converted to 62 three-part sourced entries, Simple 1 to 9 blocks, costs 4 to 39 figures, new wildfire-hardening section (R327 local adoption), UA trade-off calculator method integrated, stale R613 and R318-adjacent citations corrected. Same day: fourth external review round produced five hard style rules (no analogies in any layer, no personification of materials, no imperatives outside Applied, no proverb-cadence facts, no rhetorical questions), codified in revision6/writing_style_guide.md (Prohibited Rhetorical Devices) with lint additions; chapters 6-8 fixed to match (thermos analogy, bread analogy, load-path self-check removed). Chapters 9-12 (plumbing supply, DWV, electrical service, branch circuits) targeted-edit treatment: all 60 Code blocks converted to 194 three-part sourced entries (script-verified complete), Simple layers roughly doubled, costs added from Revision 2 mining (backflow tiers, service-upgrade retrofit, SPD, AFCI premiums, septic anchors), dropped research details landed (vault-drainage amendment, contact-tank sizing, DEQ 29-2025 effluent-pump/variance/ADU detail, grounding-electrode alternatives, worked load total), and the second-wave Table 1-E findings integrated into chapter 12, replacing both verify-with-BCD hedges: Oregon struck the NEC 210.8(D) appliance-GFCI list (dishwashers not adopted at 422.5), Article 840 unamended. Battery, Simple-cap, and Source-line verification clean on all five chapters. Details in revision6/AI_TODO.md.

## R6-3c: Chapters 13-21 full Revision 6 treatment (2026-07-11)

Nine chapters completed across two sessions on 2026-07-11, finishing the R6-3 chapter phase: every chapter of the book now carries the Revision 6 register, the three-part sourced `Code` format, restored `Simple` layers, and the settled second-wave research. Per-chapter records are in `revision6/AI_TODO.md`. Headline items: chapter 13 (HVAC) full rewrite (+140%) with the new open-loop water-rights and Oregon fuel-gas-test sections and the Independence-to-energy outage section; chapter 14 anti-scald citations corrected to the UPC-family sections (OPSC 408.3/409.4) and the R310 amendment stated from the local PDF; chapter 16 rebuilt around the owner-manufactured-CMU decision with the full testing path and economics; chapter 17 landed the survey licensure line, the Oregon weight-based CDL trap, and the OSHA attachment rules; chapter 19 corrected the gas test (Oregon 10 psi/15 min), the Additional Measure value (2.75 ACH50), and the backflow public-versus-private-well split, and pinned the standards editions; chapter 20 resolved the ORS 12.135, Magnuson-Moss, and EV/solar-ready items and landed the 2026 septic O&M contract regime and HB 3525; chapter 21 landed the seven statute pins including the intent-to-sell presumptions and the verified no-holding-period negative. Verification per chapter: full lint battery, Simple 25-word cap with under-14 averages, and the Source-line completeness script (65/45/37/19/40/26/31/22/27 sourced entries, chapters 13-21). Sixth external review verdict on chapter 13: ready; its two observations fixed same day.
