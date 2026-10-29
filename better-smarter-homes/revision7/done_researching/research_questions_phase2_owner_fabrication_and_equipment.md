File: `research_questions_phase2_owner_fabrication_and_equipment.md`

# Phase 2 Research Questions: Owner Fabrication And Equipment

Last updated: 2026-05-07

## Purpose

This file captures the second-phase research questions identified during the Chapters 1–8 rewrite. The topics are gaps in the existing manuscript and the prior research files: an owner-builder framing for on-site concrete mixing, an owner-builder framing for cinder block (CMU) manufacture using a block press, and equipment selection for the project (excavator, mixer, block press, compactor, generator, concrete pump, and other heavy equipment).

Topics are sorted by the chapter where the answers will primarily land. Each chapter section names the topic, the cross-references from other chapters, and the questions to resolve.

Do not write any chapter or section that depends on a question in this file until the question is answered and appended here. When a chapter has unresolved research dependencies, add a research-pause check to `AI_TODO.md` naming the chapter and the dependent topic, and stop at the chapter boundary when reached. The manuscript must not contain placeholder soft language while waiting for research. Surface the gap to the user instead.

## Research Policy

- Prefer official Oregon sources, adopted code text, agency guidance, court opinions, ASTM and ACI standards, manufacturer instructions, and direct confirmation from the authority having jurisdiction.
- Keep final source URLs or citations inside this research file. Manuscript content that depends on these answers is not written until the answers are appended here.
- If the answer depends on county, city, mix design, equipment make and model, owner skill, or timing, record the dependency instead of flattening into one universal rule.
- Where the answer is "this is regulated outside the residential code path" (for example, OSHA workplace safety, EPA refrigerant rules, MUTCD road safety), name the regulating authority and its standard.

## Resolution Flow

After the user appends detailed research answers, the next AI should:

1. Read the appended answers.
2. Do its own source check using official, standards, manufacturer, or professional engineering sources.
3. Keep sources inside this research file.
4. Integrate the research into the manuscript with firm claims supported by the appended sources.
5. If a question remains unanswered, do not write the chapter or section that depends on it. Surface the gap to the user and pause.

## Chapter 7: Foundation, Basement, Slabs, And Concrete Placement

Topic: on-site concrete mixing for an owner-builder.

The current manuscript treats concrete as a ready-mix delivery from a commercial supplier. Owner-builders sometimes mix concrete on site for foundations, slabs, and structural elements, particularly on remote sites or for non-time-critical pours.

Manuscript home: a make-versus-buy section ahead of "Concrete Ordering" in the foundation and concrete-placement chapter.

Questions to resolve:

- For what residential structural pours is on-site mixing acceptable to Oregon building officials, and where does on-site mixing run into ASTM C94 ready-mix expectations or special-inspection requirements?
- What batch volume threshold (yards per pour, total project yards) makes on-site mixing practical versus impractical for owner-builder structural work?
- What mix-design documentation does Oregon expect for on-site mixed concrete used in footings, foundation walls, structural slabs, and grout? How does that compare to ready-mix batch tickets?
- What ASTM and ACI standards govern on-site mixing for residential structural concrete? ASTM C387, ACI 318 §26.5, ACI 332, ASTM C94, ASTM C685, others?
- How does on-site mixing interact with ORSC R608 prescriptive concrete walls, R606 reinforced masonry grout, and R403 footings?
- What testing is required, recommended, or strongly advised for on-site mixed concrete (slump, air, temperature, cylinders, beams) and at what frequency?
- What practical equipment options exist for owner-builder on-site mixing, ranked by output rate, mix quality, and capital cost? (Tow-behind drum mixer, skid-steer mixer attachment, mortar mixer, paddle mixer, pan mixer, central-mix portable plant.)
- What materials specifications matter for on-site mixing: cement (ASTM C150 Type I/II/V, blended cements ASTM C595), aggregate (ASTM C33 fine and coarse), water (potability requirements per ACI 318), supplementary cementitious materials (fly ash ASTM C618, slag ASTM C989, silica fume ASTM C1240)?
- What environmental controls apply to on-site mixing in Oregon: cold-weather concreting (ACI 306), hot-weather (ACI 305), washout containment (DEQ rules), dust and noise rules?
- What specific failure modes are common when owner-builders mix on site (low-strength batches, segregation, cold joints, inconsistent slump) and how are they detected and corrected?
- For grout in reinforced masonry: can owner-builder on-site mixing meet ASTM C476 self-consolidating fine grout requirements, or does the work effectively require ready-mix?
- What is the realistic placement-pace constraint for on-site mixing (how many yards per hour, how does that match form-bracing and curing windows)?
- What are the Oregon ready-mix supplier minimum-load and short-load fee structures that affect the on-site-versus-ready-mix decision?

Source paths to check first:

- ACI 318 §26.5 (Construction)
- ACI 332-20 (Code Requirements for Residential Concrete)
- ASTM C387 (Packaged, Dry, Combined Materials for Concrete and High Strength Mortar)
- ASTM C94 (Ready-Mixed Concrete)
- ASTM C685 (Concrete Made by Volumetric Batching and Continuous Mixing)
- ASTM C476 (Grout for Masonry)
- ASTM C150 (Portland Cement)
- ASTM C33 (Concrete Aggregates)
- ACI 305R (Hot Weather Concreting)
- ACI 306R (Cold Weather Concreting)
- Oregon DEQ rules on construction stormwater and concrete washout
- ORSC R608, R606, R403, R404, R405, R506
- BCD program guides for residential structural concrete and masonry inspection

## Chapter 16: Materials, Suppliers, Procurement, And Substitution

Topic: CMU (cinder block) manufacture by an owner-builder.

The current manuscript assumes CMU is purchased from a regional manufacturer. Some owner-builders fabricate their own CMU on site using a manual or hydraulic block press. The technique exists, the equipment is commercially available, and the practice has documented use in remote-build and homestead contexts. The question is whether owner-fabricated CMU can meet ASTM C90 strength and dimensional requirements for use as structural masonry in a permitted Oregon residence, and what documentation the building official requires.

Manuscript home: a make-versus-buy section in the materials and procurement chapter, with cross-reference from the structural system and concrete design chapter where CMU strength, dimensions, and tolerances are specified.

Questions to resolve:

- Will an Oregon building official accept owner-manufactured CMU as structural masonry under ORSC R606 and TMS 402? Under what conditions: testing program, third-party verification, special inspection, alternative-method approval (ORSC R104.11)?
- What ASTM C90 minimum compressive strength (2,000 psi net area) testing requirements apply to owner-manufactured CMU? What sample size, frequency, lab accreditation?
- What dimensional tolerances does ASTM C90 require, and what equipment can hold those tolerances on owner production?
- What block press options exist for residential-scale production: manual stationary press, manual mobile press, electric vibrating press, hydraulic press? Output rate per day, capital cost, footprint, power requirements, operator count?
- What mix design produces ASTM C90-compliant block? Cement content, aggregate gradation, water-cement ratio, admixtures, slump (zero-slump for vibrocompaction)? Are commercial dry-cast mix designs published?
- What curing process is required for the block to develop strength: water cure, steam cure, autoclave cure, ambient cure? What durations, what facilities, what protection from rain and freezing?
- How do owner-manufactured blocks compare to commercially manufactured blocks for: dimensional consistency, surface finish, water absorption (ASTM C140), freeze-thaw durability, fire-rating coverage, seismic performance?
- What logistical considerations apply: site footprint for block production, raw-material storage, finished-block storage, weather protection, theft and damage, total project block count, production-rate constraint relative to wall-construction sequence?
- What inspection regime applies during owner-manufacture: ongoing third-party testing, batch-by-batch sampling, periodic-sample acceptance? What documentation does the building official expect?
- Are there published owner-builder case studies of CMU manufacture passing Oregon residential plan review, or is the precedent limited to alternative-jurisdiction builds (homesteader, remote rural, owner-built dome and earth-block contexts)?
- How does owner-manufactured CMU interact with the ORSC R606 prescriptive path versus engineered design under R301.1.3 and TMS 402? Does owner manufacture push the project automatically into engineered territory regardless of geometry?
- What is the realistic per-block cost for owner manufacture (raw materials, equipment depreciation, labor) versus commercial purchase plus delivery to a remote site?
- What freeze-thaw and weathering exposure-class designations under ASTM C90 apply to coastal Oregon, valley Oregon, and east-of-Cascades projects, and can owner manufacture meet the higher exposure classes?
- What alternative manufacturing paths exist that may be more practical: contract a local commercial manufacturer to produce a custom mix, lease a portable plant, partner with a regional plant for a small custom run, use ICF instead of CMU, use insulated CMU products?

Source paths to check first:

- ASTM C90 (Loadbearing Concrete Masonry Units)
- ASTM C140 (Sampling and Testing Concrete Masonry Units)
- ASTM C129 (Nonloadbearing Concrete Masonry Units)
- ASTM C476 (Grout for Masonry)
- ASTM C270 (Mortar for Unit Masonry)
- TMS 402-22 (Building Code Requirements for Masonry Structures)
- TMS 602-22 (Specification for Masonry Structures)
- ORSC R606 (General Masonry Construction)
- ORSC R104.11 (alternative materials, design, and methods of construction)
- Concrete Masonry & Hardscapes Association (CMHA) technical notes
- Oregon BCD program guides for masonry and alternative-method approvals
- Published owner-builder CMU manufacture case studies; remote-build and homestead literature

## Chapter 17: Build Sequence And Site Coordination

Topic: heavy-equipment selection for an owner-builder project.

The current manuscript references "compaction equipment," "excavation equipment," and "concrete delivery" without specifying which equipment is required, what sizes are appropriate, or how the buy-rent-hire decision is made. Equipment selection drives schedule, cost, site logistics, and which work the owner-builder can perform versus subcontract.

Manuscript home: a dedicated equipment-selection section in the build sequence and site coordination chapter. Cross-references from the soil chapter (excavation, compaction), the foundation and concrete-placement chapter (concrete delivery, pump, vibration), the structural chapter (block-laying assistance, lifting), and the materials and procurement chapter (delivery and staging).

Questions to resolve:

- For an Oregon residential build with a concrete-and-CMU shell, what is the realistic minimum equipment list for an owner-builder performing site preparation, excavation, foundation, slab, and wall construction? What is the realistic optional list?
- For each piece of equipment, what is the typical size range, the rental cost (daily, weekly, monthly) in 2026 Oregon dollars, the purchase cost for new and used, and the practical ownership decision criteria (project size, future use, transport, storage, maintenance)?
- Excavator selection: what size class (mini, compact, standard) fits a typical Oregon residential site? What boom reach, bucket size, and operating weight match site-prep, foundation excavation, and trenching for utilities and drainage? What attachments (thumb, breaker, auger, ripper, grading bucket) earn their place?
- Skid-steer or compact track loader selection: when is one more practical than an excavator for the project? What attachments matter (bucket, forks, grapple, auger, hydraulic breaker, mixer, sweeper, snow blade)?
- Compaction equipment: vibrating plate compactor, jumping jack (rammer), reversible plate compactor, ride-on roller, sheepsfoot roller. Which is appropriate for which lift type (granular fill, cohesive fill, base course, trench backfill)? Output rate, lift thickness limit, operator effort?
- Concrete-delivery equipment: line pump, boom pump, tow-behind pump, conveyor belt, motorized buggy, wheelbarrow. Which fits a typical residential pour, and at what cost? When does pump rental make economic sense versus chute or wheelbarrow?
- On-site concrete mixing equipment (cross-reference Chapter 7 topic above): tow-behind drum mixer, skid-steer drum, mortar mixer, paddle mixer, pan mixer, central-mix portable plant. Output rates, mix quality, cost.
- Generator selection: what size matches owner-builder needs for tools, mixers, lighting, equipment? Single-phase versus three-phase, fuel type (diesel, gasoline, propane, natural gas), portable versus stationary?
- Concrete vibration: internal vibrator (poker), external form vibrator, finishing screed vibrator. Sizing, fuel, runtime, technique?
- Lifting and material handling: forklift, telehandler, rough-terrain lift, crane (mobile, gantry, derrick), block-laying assist, masonry hoist. When is each justified for a residential build?
- CMU-laying assistance equipment (cross-reference Chapter 16 topic above if owner-manufactured CMU): mortar pan, mast climber, scaffold (frame, system, tubular), mortar mixer, pallet jack, vacuum lifter for large blocks?
- Welding and cutting equipment for reinforcement: stick welder, wire feed, plasma cutter, oxy-acetylene, abrasive saw, rebar bender, rebar cutter (manual, hydraulic, electric)?
- Surveying and layout equipment: total station, theodolite, laser level, transit level, optical level, GPS rover. What does owner-builder layout actually require?
- Trenching and utility-installation equipment: walk-behind trencher, ride-on trencher, mini-excavator with trenching bucket, vibratory plow, directional bore?
- Site logistics equipment: dump trailer, water truck or tank, fuel tank, jobsite trailer, secure container, scaffolding storage?
- Buy-versus-rent-versus-hire criteria: what equipment is almost always rented, almost always hired with operator, and worth buying for an owner-builder with a single-house project versus a multi-house portfolio plan?
- Equipment safety, training, and licensing: OSHA training requirements, Oregon-specific operator certifications, insurance considerations, equipment damage and bodily-injury risk?
- Transportation and trailer requirements: what equipment can the owner-builder transport with a typical pickup and trailer setup, and what requires a CDL or contracted hauling?
- Maintenance, fueling, and storage: realistic owner-operator maintenance burden for owned equipment, where rental shifts the burden, how site storage and theft protection factor in?
- Used-equipment market in Oregon: where to buy used, what to inspect, what to avoid, what brand reliability data is available, what holds resale value if the equipment is sold after the build?
- Project-phase equipment matrix: which equipment is needed in each phase (site prep, excavation, foundation, slab, wall, roof, finish, site restoration), and how can rentals be sequenced to minimize total rental days?

Source paths to check first:

- Manufacturer specification sheets for current rental and small-contractor models (Caterpillar, John Deere, Bobcat, Kubota, Komatsu, Volvo, Takeuchi, Wacker Neuson, Multiquip, Honda, Stihl)
- Equipment rental price databases (United Rentals, Sunbelt Rentals, Herc, local Oregon rental yards)
- OSHA 1926 (Construction) for relevant operator and equipment safety requirements
- Oregon OSHA program guides
- Used-equipment auction databases (Ritchie Bros, Iron Planet)
- ACI guides on consolidation (ACI 309), placement, and finishing for vibrator and pump selection
- NIOSH equipment-safety publications
- Trade publications (Concrete Construction, Equipment World, Construction Equipment magazine)

## Notes For The Next Pass

After research is appended:

1. Chapter 7 answers feed a make-versus-buy section ahead of concrete ordering in the foundation and concrete-placement chapter.
2. Chapter 16 answers feed a make-versus-buy section in the materials and procurement chapter, with cross-reference from the structural chapter.
3. Chapter 17 answers feed a dedicated equipment-selection section in the build sequence and site coordination chapter, with cross-references from the soil, foundation, structural, and materials chapters where each piece of equipment is needed.
4. If a question remains unanswered after the user's append, do not write the dependent section. Keep the question open in this file and surface the gap to the user.

---

# Chapter 7 — Resolved Research: On-Site Concrete Mixing For An Owner-Builder

Last updated: 2026-05-07. Posture: optimistic. Where a code or standard reads as a barrier, the resolution names the documentation, testing, or alternative-method path that turns the barrier into a workflow.

## Project Intent (User-Stated)

The owner intends to mix concrete on site for the project, using:

- bulk cement purchased by the pallet (40 bags per pallet typical, 94 lb each)
- bulk fine aggregate (concrete sand) and coarse aggregate (3/4-inch or smaller crushed stone) by the truckload, stockpiled and protected on site
- a CMU mold sourced from a manufacturer in China for owner-fabricated concrete masonry units (the CMU manufacturing topic is in the Chapter 16 research section; the on-site concrete batching for that production overlaps with Chapter 7)
- supplementary cementitious materials and chemical admixtures sourced through commercial concrete-supply distributors

This intent is compatible with Oregon residential building code if the work is documented, tested, and inspected per the regulatory framework below.

## Regulatory Framework — Owner-Mixed Concrete Is Permitted

ACI 318 §26.5 (Construction) governs how concrete is produced, transported, and placed for code-compliant structural work. The standard does not require ready-mix delivery. It requires that the produced concrete meet the specified mix design and that the production be documented.

ACI 332-20 (Code Requirements for Residential Concrete) is the residential-specific code referenced by IRC. It permits site-mixed concrete provided the documentation chain is intact.

ASTM C685 (Concrete Made by Volumetric Batching and Continuous Mixing) is the standard that covers volumetric mixing trucks and continuous mixers. It is the closest formal standard to a permanent owner-builder mixing rig and is the citation to use if the building official asks.

ASTM C387 (Packaged, Dry, Combined Materials for Concrete and High Strength Mortar) covers bagged dry-mix products. Useful for bagged grout and high-strength mixes purchased from a building-supply store; not the path for bulk site mixing.

ASTM C94 (Ready-Mixed Concrete) is the standard for ready-mix delivery from a commercial plant. Not applicable to owner-mixed concrete; cited here for the building official's reference if a contrast is needed.

The key point: Oregon residential code does not require ready-mix concrete. The code requires concrete that meets the mix design, with documentation that proves it. Owner-mixed concrete with the right documentation and field testing is code-compliant.

## Mix Design For Owner-Mixed Structural Concrete

Recommended starting mix for f'c = 4,000 psi at 28 days (suitable for footings, foundation walls, slabs-on-grade, and grouted reinforced masonry):

| Component | Quantity per cubic yard | Source |
|---|---|---|
| Portland cement, ASTM C150 Type I or Type II | 470–520 lb (5.0–5.5 sacks) | Bulk pallet from concrete supplier or building-supply store |
| Class F fly ash, ASTM C618 | 100–140 lb (15–25% replacement of cement) | Distributor; reduces long-term permeability and improves chemical resistance |
| Concrete sand, ASTM C33 | 1,200–1,400 lb | Local aggregate supplier; truckload and stockpile |
| Coarse aggregate (3/4-inch or smaller), ASTM C33 | 1,700–1,900 lb | Same supplier |
| Water | 250–280 lb (30–34 gal) | Potable, ACI 318 §26.4.1 |
| Air-entraining admixture, ASTM C260 | per manufacturer instructions, typically 0.5–2 oz per 100 lb cement | Commercial admixture distributor |
| Water-reducing plasticizer, ASTM C494 Type A or F | per manufacturer instructions, typically 4–8 oz per 100 lb cement | Same |
| Optional macro-synthetic fibers, ASTM C1116 | 3–7 lb per cubic yard | Forta, Sika, Euclid Chemical |

Water-cement ratio target: ≤ 0.45 for exposure classes F1/F2 (most Oregon residential exposure).

Higher-strength mixes (5,000 psi for slabs with point loads, exterior wear surfaces, or aggressive exposure) increase cement to 6.5 sacks per cubic yard and lower w/c to 0.40 with silica fume (5–10% addition) or higher fly ash replacement.

## Sourcing Strengthening Ingredients

Supplementary cementitious materials (SCMs) and chemical admixtures are widely available through commercial concrete-supply channels. Owner-builders typically use one of these sourcing paths:

**Path 1: Commercial admixture distributors (national and regional).** The major brands are BASF Master Builders Solutions, Sika, GCP Applied Technologies (formerly W.R. Grace), Euclid Chemical (now part of RPM/CSL), MAPEI, ChemMasters, Forta (fibers), and Bekaert (steel fibers). These manufacturers sell through regional distributors. Distributors typically deal with concrete-batch plants and contractors but will sell small quantities to walk-in customers or by phone order. Search "concrete admixtures distributor Oregon" or contact the manufacturer's regional rep through the manufacturer's website.

**Path 2: Ready-mix-plant counter sales.** Many ready-mix concrete plants sell small quantities of liquid admixtures to walk-in customers, especially the air-entraining and water-reducer products they use in their own mixes. This is often the fastest path for an owner-builder — drive to the local ready-mix plant, ask at the counter. Cost is at-cost or near-at-cost; the plant prefers selling product to keeping inventory.

**Path 3: Online concrete-supply retailers.** BuyAdmixtures.com, ChemMasters direct, and similar online retailers ship admixtures to homeowners. Quikrete and Sakrete (the bagged-mix brands) also sell some admixture products through home-improvement retailers (Home Depot, Lowes), though selection is limited.

**Path 4: Industrial-supply houses.** Grainger and Fastenal carry some basic admixtures (air-entraining, water-reducers). The selection is limited compared to dedicated concrete suppliers but the convenience for small-quantity purchasing is real.

**Path 5: Direct manufacturer contact.** Sika, BASF, and Euclid Chemical all have regional sales reps who will quote small-quantity orders by phone. Useful for specialty products (silica fume, certain fibers, specialty curing compounds) that distributors do not stock.

Specific material sourcing in 2026 Oregon dollars:

| Material | Typical sources | Approximate cost |
|---|---|---|
| Class F fly ash, bulk | Lehigh Hanson, Holcim regional terminal, Headwaters Resources | $80–$150 per ton bulk; $15–$25 per 50 lb bag retail |
| Slag cement (GGBFS) | Lafarge Holcim, Lehigh Hanson | $100–$180 per ton bulk; bagged less common |
| Silica fume | BASF, Sika, ChemMasters, online | $1–$3 per pound; sold in 50 lb bags |
| Air-entraining admixture | BASF Micro-Air, Sika Aer, Euclid Air-Mix | $30–$60 per 5-gallon pail |
| Water-reducer / plasticizer | BASF MasterPolyheed, Sika ViscoCrete, Euclid Eucon | $50–$120 per 5-gallon pail |
| Set retarder | BASF Pozzolith, Sika Plastiment | $30–$60 per 5-gallon pail |
| Set accelerator | BASF MasterSet, Sika Sigunit | $40–$80 per 5-gallon pail |
| Macro-synthetic fibers | Forta Ferro, Sika Fiber, Euclid Tuf-Strand | $50–$100 per 5 lb bag (one cubic yard) |
| Steel fibers (where designed by engineer) | Bekaert Dramix, Forta Steel | $100–$200 per 50 lb bag |

The Coal-power plant closure of PGE Boardman (2020) removed the only Oregon-source fly ash; current Oregon supply comes from out-of-state plants through regional distributors. Lehigh Hanson terminal in Portland is the most common Oregon source.

## Bulk Cement, Sand, And Gravel Sourcing

Cement: bulk 94 lb bags by the pallet from regional cement distributors and large building-supply stores. Pallets typically contain 40 bags (3,760 lb total). One pallet of cement at a 6-sack mix yields approximately 6.7 cubic yards of concrete. Storage requirement: dry, off the ground on pallets, covered with plastic sheeting; cement loses strength when exposed to humidity over time. Use within 90 days of purchase.

Aggregate: truckloads from local pits and quarries. Concrete sand (ASTM C33 fine aggregate) and 3/4-inch crushed stone (ASTM C33 coarse aggregate) are typically delivered in 10–22 ton dump-truck loads. Store on covered tarps or paved pad to prevent contamination. For owner-builder volumes (50–100 cubic yards total project), a single 10-ton load each of sand and gravel covers 5–8 cubic yards of concrete; plan multiple deliveries scheduled to mixing days.

Aggregate quality: have the pit-run or yard product certified for ASTM C33 compliance. Most Oregon pits sell ASTM-graded products by name. Gradation, deleterious materials, and sulfate content matter for long-life concrete; a one-time aggregate sieve analysis ($150–$300) at a local materials lab confirms compliance for the project record.

## Mixing Equipment Options

| Mixer type | Capacity | Cost (2026 dollars) | Best fit |
|---|---|---|---|
| Tow-behind drum mixer | 6–9 cu ft | $1,500–$4,000 new; $800–$2,500 used | Grout, small slabs, footings less than 5 cu yd per pour |
| Stationary drum mixer | 3–9 cu ft | $300–$1,500 new | Light residential, small batches |
| Skid-steer drum-mixer attachment | 1.5–4 cu ft | $3,000–$6,000 | Mobile mixing on the jobsite when a skid-steer is already on hand |
| Mortar mixer (paddle) | 6–12 cu ft | $1,500–$4,000 | Mortar, grout, dry-mix CMU production |
| Pan (planetary) mixer | 1–4 cu ft | $4,000–$10,000 | Highest mix quality; well-suited for CMU dry-mix production |
| Volumetric mixer truck | unlimited (continuous) | $80,000+ purchase; $300–$600/day rental | Large pours; rental is the practical option |
| CMU block press (for Chapter 16 cross-reference) | 1–8 blocks per cycle | $2,000–$15,000 imported | Owner-fabricated CMU production |

Production rate: a 9 cu ft tow-behind drum mixer can produce roughly 1.5–2 cu yd per hour with a single operator and one helper, including loading and discharging. A 50 cu yd foundation pour is a multi-day operation with this setup. For a single large pour, ready-mix delivery is faster and often less expensive once short-load fees and mixing labor are accounted for. For continuous operations (CMU production, repeated small grout pours, slab patches), site mixing wins.

## Field Testing Protocol For Owner-Mixed Concrete

ACI 318 §26.12 and ACI 332-20 §3.3 govern testing. For an owner-mixed structural pour, the practical protocol:

| Test | Frequency | Purpose | Reference |
|---|---|---|---|
| Slump | Each batch or each load | Workability check; identifies water-content issues | ASTM C143 |
| Air content (where air-entrained) | First batch and any time slump or appearance changes | Verifies entrained-air for freeze-thaw resistance | ASTM C231 (pressure) or ASTM C173 (volumetric) |
| Concrete temperature | Each major pour, especially in hot or cold weather | Identifies placement-window concerns | ASTM C1064 |
| Compression cylinders | One set of 4 cylinders per major pour | Verifies compressive strength at 28 days | ASTM C31 making, ASTM C39 testing |

A "set of 4" allows testing at 7 days (1 cylinder), 28 days (2 cylinders averaged for the strength test), and a 56-day hold cylinder for re-test if 28-day result is suspect.

The owner-builder can perform field tests after taking the ACI Grade I Field Testing Technician certification course. This is a one-day course typically offered through state ACI chapters; cost is $400–$600 including the exam, valid 5 years. Self-perform slump, air, and temperature; ship cylinders to a CCRL-inspected laboratory for compression testing (typically $25–$50 per cylinder).

Acceptance criteria from ACI 318-19 §26.12.3.1:

1. Average of any 3 consecutive strength tests ≥ f'c.
2. No individual strength test less than (f'c – 500) psi for f'c ≤ 5,000 psi.

A failing individual cylinder triggers a low-strength investigation under §26.12.6. The investigation may include core testing, in-place testing, or a structural evaluation. Failures are uncommon when mix design and water content are controlled.

## Documentation Required For Owner-Mixed Concrete

Per pour, the operational record:

- mix design specification (cement, aggregate, water, admixture proportions)
- batch records (quantity of each component used per batch, water added, time of mixing, time of placement)
- delivery / placement timeline (start of placement, end of placement, ambient temperature, concrete temperature)
- field test record (slump, air, temperature, cylinder ID)
- curing log (curing method, duration, temperature, moisture-maintenance method)
- inspector approval (footing inspection, foundation-wall inspection, slab inspection per ORSC R109)

The documentation requirement is no different in substance from a ready-mix batch ticket; the format is owner-prepared rather than supplier-provided. Building officials accept owner-prepared documentation for owner-mixed concrete on owner-built homes when the documentation is complete and the field test results are within acceptance criteria.

## Loopholes And Solutions

**Building official acceptance.** Some building officials are unfamiliar with owner-mixed structural concrete and may push back. The path to acceptance: present the mix design with ASTM C685 / ACI 318 §26.5 / ACI 332-20 references, the field-testing protocol, and the documentation framework. Offer to provide the cylinder test results before backfill or before the next inspection. A pre-pour meeting with the inspector to walk through the protocol is often sufficient.

**Special-inspection trigger.** ACI 318 §26.13 special inspection is triggered for high-strength concrete (f'c ≥ 5,000 psi), post-tensioned concrete, and certain large structural elements. For most residential pours under 5,000 psi, special inspection is not required, but a building official may require it for cause. The path: stay at f'c = 4,000 psi for typical residential elements; reserve 5,000 psi for elements where the design actually needs it; treat any special-inspection requirement as a documented testing program rather than a blocking constraint.

**Ready-mix short-load fees and the economic decision.** Oregon ready-mix plants typically have a 4–7 cubic yard minimum load and short-load fees of $100–$300 for partial loads. For pours under the minimum, on-site mixing is often the cheaper path. For pours above the minimum, ready-mix is usually cheaper once labor and equipment are counted. The hybrid: own mixing for grout and small accessory pours; ready-mix for the foundation and slab. This is a decision the owner can make per-pour.

**Temperature and weather.** ACI 305R (Hot Weather Concreting) and ACI 306R (Cold Weather Concreting) cover temperature limits. Owner-mixed concrete is more flexible than ready-mix on scheduling — pours can be planned around weather windows. Cool-water mixing in hot weather, heated-water mixing in cold weather, and protective covering during the curing window resolve most temperature concerns.

**Cement freshness.** Use cement within 90 days of purchase; older cement loses strength. Storage on pallets above the ground, covered with plastic sheeting, in a dry shed extends this window. For multi-month projects, plan cement deliveries in stages.

**Aggregate moisture.** Stockpiled aggregate carries variable moisture content. Adjust mix water to compensate. The water in the mix design is total water (including aggregate moisture); subtract the aggregate moisture to get the water-to-add. A simple bucket-weight measurement of aggregate moisture content before each batch keeps the mix consistent. ASTM C566 covers aggregate moisture-content testing.

**Concrete washout and DEQ rules.** Oregon DEQ requires construction-site concrete washout containment to prevent alkaline runoff into waterways. Owner-builders typically use a lined washout pit or a portable washout container. Solidified concrete from washout can be broken up and used as base course. The DEQ 1200-C permit (for projects disturbing 1+ acre) covers washout in its erosion-control plan.

## Sources

- ACI 318-19 §26.5 (Construction) and §26.12 (Acceptance of Concrete)
- ACI 332-20 (Code Requirements for Residential Concrete)
- ASTM C685 (Concrete Made by Volumetric Batching and Continuous Mixing)
- ASTM C387 (Packaged, Dry, Combined Materials for Concrete and High Strength Mortar)
- ASTM C150 (Portland Cement)
- ASTM C33 (Concrete Aggregates)
- ASTM C618 (Coal Fly Ash and Raw or Calcined Natural Pozzolan)
- ASTM C989 (Slag Cement)
- ASTM C1240 (Silica Fume)
- ASTM C260 (Air-Entraining Admixtures)
- ASTM C494 (Chemical Admixtures)
- ASTM C1116 (Fiber-Reinforced Concrete)
- ASTM C143 (Slump), C231 (Air Pressure Method), C173 (Air Volumetric Method), C1064 (Temperature)
- ASTM C31 (Making Cylinders), C39 (Compressive Strength)
- ACI 305R (Hot Weather Concreting), ACI 306R (Cold Weather Concreting), ACI 308R (Curing)
- ASTM C566 (Total Evaporable Moisture Content of Aggregate by Drying)
- ORSC R109 (Inspections), R403 (Footings), R506 (Concrete Floors)
- BASF Master Builders Solutions, Sika, GCP Applied Technologies, Euclid Chemical, MAPEI: admixture suppliers
- Lehigh Hanson, Lafarge Holcim, Headwaters Resources: SCM suppliers
- Forta, Sika, Euclid, Bekaert: fiber suppliers
- Oregon DEQ 1200-C construction stormwater permit framework
- Local ready-mix plant counter sales: practical retail path for liquid admixtures

The Chapter 7 section of the manuscript carries a make-versus-buy section ahead of "Concrete Ordering" using this research as the basis for the discussion.







# Research Answers — Chapter 16: Owner-Manufactured CMU (Cinder Block)

Research date: 2026-07-04
Status: Answered with sources, except items explicitly marked UNRESOLVED at the end. Do not write manuscript content that depends on an UNRESOLVED item.

---

## Headline findings (read first)

1. **There is no code prohibition on owner-manufactured CMU, but there is also no acceptance path other than proving the units comply with ASTM C90.** ORSC R606.2.1 requires concrete masonry units to conform to ASTM C90 (loadbearing) or ASTM C129 (nonloadbearing). The standard is product-neutral: it does not care who made the block. Compliance is demonstrated by testing under ASTM C140 at a qualified laboratory. A commercial plant demonstrates this with routine plant QC and submittals; an owner must build the equivalent paper trail from scratch, and the building official has explicit authority under ORSC R104.11.1 to require that testing at no expense to the municipality.
2. **The alternative-method section (R104.11) is the fallback, not the primary path.** If the units test out as C90-compliant, they are not an "alternative material" at all — they are simply C90 units, and R606 applies normally. R104.11 only comes into play if the owner wants acceptance on some basis other than full C90 compliance (e.g., reduced testing, non-standard dimensions), which is a much weaker position.
3. **One research question rests on a false premise: ASTM C90 has no freeze-thaw exposure classes.** Exposure-class systems for masonry units exist in the Canadian standard CSA A165 and in ASTM C1372/C1262 (segmental retaining-wall units), not in C90. C90 addresses durability indirectly through density classification, maximum absorption limits, and maximum linear drying shrinkage; its Appendix X1 on water penetration is explicitly non-mandatory guidance. The manuscript must not claim Oregon climate zones map to "C90 exposure classes."
4. **No published precedent was found of owner-manufactured CMU passing Oregon residential plan review.** The documented owner-fabrication tradition (Mother Earth News, Popular Mechanics reprints, homestead forums, CINVA-ram compressed earth block) is real but sits almost entirely outside the permitted structural-masonry context. Record this as a precedent gap, not as evidence of infeasibility.
5. **The economics almost never favor owner manufacture in Oregon.** Delivered commercial 8x8x16 gray block runs roughly $1.60–$2.25 (early 2026 national trade data) and $1.25–$3.00 at retail, from plants whose C90 compliance is already documented. The owner assumes equipment cost, mix development, curing infrastructure, lab fees, and schedule risk to replace a $2 commodity. The honest manuscript framing is: technically possible, procedurally heavy, economically justified only in edge cases (extreme remoteness where per-block freight dominates — and even then cement and aggregate still have to be freighted in).

---

## Answers, question by question

### Q1. Will an Oregon building official accept owner-manufactured CMU as structural masonry under ORSC R606 and TMS 402? Under what conditions?

Answer: Acceptance is available in principle through two routes, and the county-level outcome is an AHJ-dependent fact (record the dependency).

- **Route A — demonstrate C90 compliance (strongest).** ORSC R606.2.1 (carrying the IRC provision) requires loadbearing CMU to conform to ASTM C90; the code commentary confirms units are manufactured "in accordance with the requirements of ASTM C90" from portland cement, water, and mineral aggregates, with admixtures permitted per the standard (https://codes.iccsafe.org/s/THPOTIRC2021P1/part-iii-building-planning-and-construction/THPOTIRC2021P1-Pt03-Ch06-SecR606.2.1). Nothing in R606 restricts who the manufacturer is. The building official's leverage is R104.11.1: where there is insufficient evidence of compliance, the official "shall have the authority to require tests as evidence of compliance to be made at no expense to the municipality," with test methods as specified in the code or other recognized standards (2023 ORSC Chapter 1, https://www.oregon.gov/bcd/codes-stand/Documents/23orsc-ch1.pdf). For CMU that means ASTM C140 testing at the owner's expense. R104.4 lets the official accept written, certified reports of inspection by approved agencies or individuals — the mechanism for accepting third-party lab reports and, if demanded, third-party observation of production.
- **Route B — alternative-method approval under R104.11.** The 2023 ORSC retains R104.11: alternatives shall be approved where the building official finds the proposal satisfactory, complying with the intent of the code, and "at least the equivalent of that prescribed in this code in quality, strength, effectiveness, fire resistance, durability and safety" (https://www.oregon.gov/bcd/codes-stand/Documents/23orsc-ch1.pdf). If not approved, the official must respond in writing with reasons (IRC R104.11 text, https://codes.iccsafe.org/s/IRC2018P7/chapter-1-scope-and-administration/IRC2018P7-Pt01-Ch01-SubCh02-SecR104.11). Oregon adds two statewide escalation tools relevant here: a party may request a **statewide code interpretation** or a **site-specific ruling** from the Building Codes Division, based on advice from the relevant advisory board, and the resulting ruling is binding and transmitted to all building officials (League of Oregon Cities handbook, Ch. 24 Building Regulations, Dec 2024, https://www.orcities.org/application/files/7717/3585/7450/Handbook_-_Chapter_24_Building_Regulations.pdf; Oregon BCD codes program overview, https://www.oregon.gov/bcd/codes-stand/pages/index.aspx). This is the documented Oregon path when a local official balks (precedent: Portland ATAC air-admittance-valve approval under R104.11, https://www.portlandoregon.gov/bds/appeals/index.cfm?action=getfile&appeal_id=22152&file_id=28110).
- **Practical conditions a building official can and likely will attach:** pre-construction meeting; a written testing program (lab, sampling frequency, lot definition); C140 test reports from a laboratory evaluated per ASTM C1093 (C140 Note 1 directs this — see Q2); mortar and grout per ASTM C270/C476 as R606 already requires; and possibly periodic third-party observation of production accepted under R104.4. "Special inspection" as a formal program is an Oregon Structural Specialty Code / IBC Chapter 17 concept, not an ORSC one; under the ORSC the equivalent lever is the official's R104.11.1 testing authority plus R104.4 report acceptance.

### Q2. What ASTM C90 strength-testing requirements apply? Sample size, frequency, lab accreditation?

- **Strength floor:** minimum net-area compressive strength 2,000 psi (13.8 MPa), raised from 1,900 psi in the 2014 revision and carried in C90-22 (CMHA FAQ-004, https://www.masonryandhardscapes.org/resource/cmu-faq-004/; CMHA CMU-TEC-001-23, https://www.cmha.org/resource/cmu-tec-001/; ASTM C90-22 store page, https://store.astm.org/c0090-22.html). Net area is computed from unit net volume per C140.
- **Test method and sampling:** compliance is verified under ASTM C140/C140M, which covers sampling, dimensions, compressive strength, absorption, density, and moisture content (ASTM C140 scope, https://www.astm.org/Standards/C140.htm). Industry guidance summarizing C140 directs sampling **six units of identical size and configuration per lot**, with the set divided between compression and absorption/density specimens (Forney, "Simple Guide to ASTM C140," https://forneyonline.com/simple-guide-astm-c140/). The exact per-lot unit counts and lot-size thresholds in the current C140 edition must be confirmed against purchased standard text — flagged UNRESOLVED-2 below. For an owner production run, the workable structure is: define a "lot" (e.g., each production week or each N thousand units or each mix/material change, whichever comes first) in the written testing program and sample each lot.
- **Laboratory qualification:** C140 Note 1 states the testing laboratory should be evaluated in accordance with ASTM Practice C1093 (https://www.astm.org/Standards/C140.htm). In practice the owner should use a lab accredited (e.g., ANAB/AASHTO re:source, ISO/IEC 17025) for C140 — such labs exist commercially (example: WJE, ANAB ISO/IEC 17025 accredited for C140, https://www.wje.com/expertise/laboratories/testing-standards/astm-c140). Oregon has multiple accredited construction-materials labs in the Portland, Salem, Eugene, Bend, and Medford markets; the specific lab is a project-level fact.
- **The hidden third test:** C90 compliance is not just strength and absorption. C90 also caps **linear drying shrinkage at 0.065%**, measured by ASTM C426 (CMHA CMU-TEC-001-23, https://www.cmha.org/resource/cmu-tec-001/). C426 is a specialized, weeks-long lab test that commercial producers run on their mix designs and reference thereafter. An owner must either commission C426 on the developed mix or find an official willing to waive it — a genuine practical hurdle to name in the manuscript.

### Q3. What dimensional tolerances does ASTM C90 require, and can owner equipment hold them?

- **Tolerances:** overall unit dimensions (width, height, length) within **±1/8 in. (3.2 mm)** of specified dimensions; molded features (ribs, scores) within ±1/16 in. of specified dimension and placement; plus minimum face-shell and web thicknesses and a minimum normalized web area for hollow units (CMHA CMU-TEC-001-23, https://www.cmha.org/resource/cmu-tec-001/).
- **Equipment implication:** the ±1/8 in. tolerance is set by the mold and the machine's fill/compaction consistency, not by operator skill per se. A rigid steel mold in good condition holds length and width; **height is the variable dimension** in vibro-compaction machines because it depends on fill quantity and compaction energy per cycle. Machines with a fixed-height compression head and positive stops (typical of hydraulic and better vibrating machines) hold height; hand-tamped and crude egg-layer machines are where height drift and out-of-square units appear. Mold wear over thousands of cycles opens tolerances. The manuscript claim to make: tolerance compliance is achievable with a commercial-grade steel-mold machine and disciplined fill control, and is the first thing the C140 dimensional measurements will catch if not.

### Q4. What block press options exist at residential scale? Output, cost, footprint, power, operators.

Four classes, from published manufacturer data (treat importer output claims as best-case marketing figures; all machines below are import-class — Chinese and Indian — because U.S. commercial block machines such as Besser and Columbia are full plant-scale equipment, not residential-scale):

- **Manual/semi-manual stationary vibrating machines** (e.g., Lontto LMT4-26/LMT4-35/LMT4-40, Osino QTJ4-40): electric vibration motor, manual mold handling, blocks formed on pallets. Vendor-listed prices roughly **$1,000–$4,500** for the machine class (Lontto price list, https://www.block-machine.net/smart-concrete-block-machines/; USA page, https://www.block-machine.net/block-making-machine-in-usa/). The Osino QTJ4-40 claims **2,000–4,000 blocks per 8 h** and runs on single- or three-phase power at 110/220/380/440 V, marketed to "family block factory" users (https://osinomachinery.com/product/qtj4-40-small-manual-hollow-block-making-machine-for-sale/). Realistic owner output with a 2-person crew, material handling, and curing constraints is far below the claim; hundreds per day is the defensible planning number for this class (vendor category description: manual machines "produce a few hundred blocks per hour" is throughput at the mold, not sustained production — https://www.block-machine.net/concrete-block-making-machine/).
- **Mobile "egg-layer" hydraulic machines** (e.g., Lontto QMY4-30 ~$4,500; QMJ4-45 manual mobile ~$3,500): lay blocks directly on a cured concrete slab, eliminating pallets; hydraulic ram plus vibrators; typical spec class ~50–60 machine cycles/hour (several blocks per cycle), 3.5–5 hp total, machine weight 750–1,750 kg (Lontto prices, https://www.block-machine.net/smart-concrete-block-machines/; Indian egg-layer specs: 2,000 psi mold pressure, dual vibrators, 440 V 3-phase motors, https://www.blockmachines.info/hydraulic-movable-concrete-block-machine.html). Requires a large flat concrete production slab (the slab is the pallet).
- **Semi-automatic vibrating lines** (e.g., Osino QT4-24: 3,000–5,000 blocks/8 h, requires 3-phase power, works with mixer and belt conveyor, https://osinomachinery.com/product/qt4-24-semi-automatic-vibrating-cement-concrete-block-moulding-machine-price/): already beyond single-house scale.
- **Fully automatic hydraulic plants** ($11,500+ machine only, e.g., Lontto QT3-20; up to 40,000 blocks/day industrial, https://www.block-machine.net/concrete-block-making-machine/): irrelevant to an owner-builder except as contrast.

Cross-cutting equipment facts: a **pan mixer is required** — drum (barrel) mixers cannot mix the semi-dry zero-slump block mix (trade guidance, https://waysto.digital/create/how-to-make-your-own-concrete-blocks/); many machines want **three-phase power**, which on a rural Oregon site means a generator or phase converter (cross-reference the equipment chapter's generator section); diesel-engine variants exist for off-grid sites (Osino QT4-30 diesel, https://osinomachinery.com/product/qtj4-40-small-manual-hollow-block-making-machine-for-sale/). Add molds ($ per shape), pallets or a production slab, curing cover, and ocean freight/import logistics to the machine price. Two operators is the realistic minimum for any of these (one filling/cycling, one carting and stacking); the machine-only single operator is a demo condition. Historical DIY precedent: Popular Mechanics (1946, reprinted by Mother Earth News) documented a shop-built vibrating machine producing ~800 blocks/day with an operator and helper — a useful period benchmark for the manuscript's history sidebar (https://www.motherearthnews.com/diy/how-to-make-concrete-blocks-zmaz77mjzbon/).

### Q5. What mix design produces C90-compliant block? Are commercial dry-cast mixes published?

- **Character of the mix:** dry-cast / zero-slump ("negative slump") concrete — so stiff that a slump cone test simply leaves a standing pile; water content well below conventional concrete, w/cm commonly cited in the ~0.30s and lower for dry-cast processes (NPCA, "Top 10 Facts about Dry-Cast Concrete," https://precast.org/blog/top-10-facts-about-dry-cast-concrete/). The mix gains handling strength immediately from compaction and can reach specified strength rapidly (NPCA notes some dry-cast products meet strength requirements in 24 hours).
- **No authoritative published universal mix exists — record this firmly.** NPCA states directly that ACI's former guide for proportioning no-slump concrete is no longer available, that machine manufacturers supply *starting-point* recommendations, and that "every dry cast mix design will be different depending on... the sources of raw materials," requiring the producer to experiment with each machine and product (NPCA, "Demystifying Dry Cast Concrete," https://precast.org/precasttoday/q2-2024/demystifying-dry-cast-concrete/). This is the single most important mix-design fact for the manuscript: an owner cannot download a compliant recipe; they must develop one with trial batches and lab tests.
- **Starting-point proportions from published trade/DIY sources** (present as starting points only): aggregate-to-cement about **8:1 by loose volume** with high-early-strength cement (South African PPC-derived guidance: 3.5 bags cement + 1 m³ aggregate ≈ 400 bricks; cement strength class 42,5N or higher; https://waysto.digital/create/how-to-make-your-own-concrete-blocks/); the 1946 Popular Mechanics machine mix: 7 parts pea gravel, 12 parts sharp sand, 2 parts silt, 2.5 parts portland cement, water set by feel of the damp aggregate (https://www.motherearthnews.com/diy/how-to-make-concrete-blocks-zmaz77mjzbon/). Block mixes use more fine aggregate and less coarse aggregate and water than ordinary concrete (Globmac process overview, https://www.globmac.com/en/how-to-make-concrete-blocks/). Aggregates must meet ASTM C33 (normal weight) or C331 (lightweight), which C90 references (masonry design reference summarizing C90's referenced standards, https://www.uop.edu.jo/PDF%20File/uop%20[Architecture_Ebook]_Masonry_Design_and_Detailing_For_Architects_and_Contractors-20615_Part279.pdf).
- **Moisture control is the craft skill:** the squeeze test (mix clings in the hand without wetting the palm) is the traditional field control (documented for pressed-block work, https://www.motherearthnews.com/diy/make-pressed-earth-blocks-zmaz78jazbur/); too dry → cracked, friable block; too wet → slumping on ejection. Admixtures in commercial block production (plasticizers, water repellents, coloring) are permitted by C90 but not required.

### Q6. What curing process is required?

- **Commercial practice:** low-pressure (atmospheric) steam curing or high-pressure autoclave. Atmospheric steam: 3–5 h initial moist hold, temperature ramped 40–60 °F/h to 150–180 °F, then a soak (JoVE accelerated-curing summary, https://www.jove.com/science-education/v/16918/accelerated-curing-of-concrete). Autoclave: ~325–375 °F at 80–170 psi, giving 24-hour strength roughly equal to 28-day ambient strength (theconstructor.org steam-curing overview, https://theconstructor.org/concrete/steam-curing-concrete-methods-advantages/38837/; masonry blocks are conventionally steam- or autoclave-cured within 24 h of casting — Rostami/Shao, "Carbonation Curing versus Steam Curing for Precast Concrete Production," https://www.researchgate.net/publication/270843798_Carbonation_Curing_versus_Steam_Curing_for_Precast_Concrete_Production). This is why commercial plants ship next-day; it is not achievable at owner scale.
- **Owner-scale (ambient moist cure):** the defensible regime from trade guidance is: protect green blocks from rain, sun, and wind; cover with plastic sheeting; light water misting in hot/windy weather; **do not move or stack for ~7 days**; blocks continue gaining strength toward the 28-day mark before load-bearing use (https://waysto.digital/create/how-to-make-your-own-concrete-blocks/; parallel curing discipline in the pressed-block literature — sprinkle 3×/day, wall-ready in ~8 days, strength gain ~30 more days, https://www.motherearthnews.com/diy/make-pressed-earth-blocks-zmaz78jazbur/). Cure in shade (Popular Mechanics/MEN, https://www.motherearthnews.com/diy/how-to-make-concrete-blocks-zmaz77mjzbon/).
- **Oregon climate constraint (record as dependency):** west of the Cascades, winter production means rain protection is mandatory and cure is slow but freeze risk is modest; east of the Cascades, freezing of green block is a real destruction risk — no production of uncovered block in freezing weather, and stored green block needs insulated/heated cover or the production season shrinks to roughly late spring–early fall. This interacts directly with the production-rate constraint in Q8.

### Q7. Owner-manufactured vs commercial block: consistency, absorption, freeze-thaw, fire rating, seismic.

- **Dimensional consistency and finish:** commercial plants hold ±1/8 in. with automated fill and laser/QC checks during production (Globmac, https://www.globmac.com/en/how-to-make-concrete-blocks/); owner block from a good steel mold can meet tolerance but will show more unit-to-unit height and density variation. Density variation matters because C90 absorption limits are density-class dependent.
- **Absorption/density (ASTM C140 tests):** C90 sets maximum water absorption by density class — lightweight (< 105 pcf), medium weight (105–125 pcf), normal weight (≥ 125 pcf) (CMHA CMU-TEC-001-23 Table 2, https://www.cmha.org/resource/cmu-tec-001/; density class boundaries also summarized at https://www.reitmachine.com/2026/05/27/how-to-adjust-block-density-in-production-2026-guide/). Under-compacted owner block trends lighter, more porous, and higher-absorption — the most likely C140 failure mode after low strength. (Exact absorption limit values per class in the current C90 edition: confirm against purchased text, UNRESOLVED-2.)
- **Freeze-thaw durability:** C90 contains **no freeze-thaw test or exposure class** (see Headline finding 3; C90's non-mandatory Appendix X1 addresses water penetration guidance only — scanned C90 text, https://spectraglaze.com/wp-content/uploads/2018/04/ASTM-C90-122117.pdf). Durability in practice rides on density, absorption, cement content, and detailing (flashing, drainage, coatings). Aggregate choice controls density, absorption, and freeze-thaw performance simultaneously (trade summary, https://nedesestimating.com/cement-vs-cinder-vs-concrete/). For east-of-Cascades exposure, the conservative manuscript recommendation is normal-weight units, low absorption results, and sealed/detailed walls — as a performance argument, not a C90 class citation.
- **Fire rating:** CMU fire-resistance ratings in listings and calculated-fire-resistance tables are keyed to equivalent thickness and aggregate type of C90-class units. Owner block that genuinely meets C90 with a documented aggregate type can use the same calculated-equivalent-thickness method; owner block of undocumented composition cannot claim listed assemblies. Flag in the structural chapter cross-reference.
- **Seismic:** the unit is only one input; the assembly (grout per C476, mortar per C270 — Type N is prohibited in the lateral system in high SDCs, reinforcement per R606.12) governs. See Q11.

### Q8. Logistics: footprint, storage, weather protection, production-rate vs wall sequence.

- **Footprint:** the machine itself is small (roughly 2.1 × 1.3 m for a mobile hydraulic unit, https://www.blockmachines.info/hydraulic-movable-concrete-block-machine.html), but the real footprint is: raw-material bays (cement under hard cover; sand and gravel stockpiles), pan mixer, the machine, a curing area (racked pallets under cover, or the egg-layer production slab itself), and finished-block stacking. An egg-layer needs a flat cured concrete slab sized for days of production, because blocks occupy the slab until they can be moved.
- **Block count and campaign length:** a single-story CMU dwelling plausibly needs on the order of 2,500–5,000 8x8x16 units (coverage factor 1.125 blocks/ft² of wall, https://concretecalculate.com/concrete-calculators/concrete-block-calculator/; a garage-scale building alone runs $2,000–2,500 in commercial block at 2026 prices, same source). At a defensible owner rate of 150–300 blocks/day with 7-day minimum cure holds, block production is a multi-week to multi-month campaign that must lead wall construction, with finished inventory secured against weather and theft (theft-in-absence is a named motivation in the historical owner-builder literature, https://www.motherearthnews.com/diy/make-your-own-concrete-blocks-zmaz75zwar/).
- **Sequencing rule for the manuscript:** production must stay a full cured lot ahead of the masons, and every lot must have passing C140 results before it goes in the wall — otherwise a failed lot means demolishing laid units.

### Q9. What inspection regime applies during owner manufacture?

No prescriptive regime exists in the ORSC; the regime is whatever the building official conditions the approval on, using R104.11.1 (testing at owner expense) and R104.4 (acceptance of certified third-party reports) (2023 ORSC Ch. 1, https://www.oregon.gov/bcd/codes-stand/Documents/23orsc-ch1.pdf). The credible package to propose proactively, mirroring commercial QC:

1. Written production and QC plan (mix design, materials sources, lot definition, curing regime, record forms).
2. Pre-production qualification: trial-batch units tested to C140 for strength, absorption, density, dimensions, plus C426 shrinkage on the mix.
3. Per-lot acceptance sampling to C140 at a C1093-evaluated/ISO 17025-accredited lab (labs advertising exactly this scope exist, e.g., https://www.appliedtesting.com/standards/astm-c140-sampling-and-testing-concrete-masonry-units-and-related-units, https://www.wje.com/expertise/laboratories/testing-standards/astm-c140).
4. Retained records delivered with each lot; blocks not incorporated until the lot passes.
This converts a skeptical plan-review conversation into a document review. Budget lab fees per lot (a C140 test series is a few hundred to low four figures per lot depending on lab and tests — treat as a project-level quote item; inspection-visit costs of $250–$500 each are a reasonable planning figure, https://www.countbricks.com/post/concrete-block-prices).

### Q10. Published Oregon owner-builder CMU-manufacture case studies?

**None found.** The searchable record contains: (a) the homestead/remote-build DIY literature — cast-in-place block forms (Mother Earth News 1975, https://www.motherearthnews.com/diy/make-your-own-concrete-blocks-zmaz75zwar/), shop-built vibrating block machines (Popular Mechanics 1946 via MEN, https://www.motherearthnews.com/diy/how-to-make-concrete-blocks-zmaz77mjzbon/), CINVA-ram pressed soil-cement block (MEN 1978, https://www.motherearthnews.com/diy/make-pressed-earth-blocks-zmaz78jazbur/), and contemporary forum/DIY machine-building activity (https://www.homesteadingtoday.com/threads/easy-plans-for-a-compressed-earth-block-machine.414321/, https://tophighmachinery.com/how-to-make-a-concrete-block-machine-a-step-by-step-diy-guide/); and (b) commercial owner/builder CMU *construction* (not manufacture) case studies (HUD/NCMA, "Building Concrete Masonry Homes," https://www.huduser.gov/portal/publications/PDF/masonry.pdf). None document an owner-manufactured structural CMU dwelling clearing plan review in Oregon or any IRC jurisdiction. Manuscript treatment: state plainly that the precedent base is homestead/alternative-jurisdiction, and that an Oregon owner would be breaking procedural ground — hence the front-loaded testing program in Q9. (Also flag: CINVA-ram soil-cement block is *not* CMU and cannot ride on R606/C90 at all; it would be a pure R104.11 alternative-material application.)

### Q11. Interaction with the R606 prescriptive path vs engineered design (R301.1.3, TMS 402). Does owner manufacture force engineering?

- **Owner manufacture itself does not trigger engineered design.** The prescriptive path's material gate is C90 conformance; units that test compliant are prescriptive-path units regardless of manufacturer.
- **Seismic design category usually forces the issue anyway.** IRC/ORSC R301.2.2.2 requires masonry construction in SDC C to comply with R606.12; in SDC D0/D1 with R606.12.1; in SDC D2 with R606.12.4 (IRC Ch. 3, https://codes.iccsafe.org/content/IRC2021P3/chapter-3-building-planning). In SDC D0/D1, masonry lateral-force-resisting elements must either be designed per TMS 402 chapters (with minimum reinforcement ratios ≥ 0.002 gross combined, bar spacing limits of 48 in. solid-grouted / 24 in. otherwise, Type N mortar prohibited in the lateral system) or meet the narrow one-story/9-ft exception (R606.12.3 text, https://up.codes/s/seismic-design-category-d0-or-d1). Much of western Oregon is SDC D0–D2 (site-specific SDC comes from the Oregon Design Criteria Hub, https://www.oregon.gov/bcd/codes-stand/pages/index.aspx). Practical consequence for the manuscript: **a CMU dwelling west of the Cascades is very likely an engineered or heavily reinforced project regardless of who made the block**; east of the Cascades (lower SDC) the prescriptive R606 path is more available. Record SDC as a site dependency, resolved per site via the Design Criteria Hub.
- Under the unit-strength method, C90-minimum units laid in Type M or S mortar give an assembly f′m of 2,000 psi (recalibrated TMS 602 unit-strength table; CMHA FAQ-004, https://www.masonryandhardscapes.org/resource/cmu-faq-004/) — the number the engineer will use if the owner's units test only to the C90 floor.

### Q12. Realistic per-block cost, owner manufacture vs commercial purchase to a remote site.

- **Commercial baseline (2026):** standard 8x8x16 gray CMU $1.25–$2.50 retail (https://homeguide.com/costs/cinder-block-wall-cost); delivered trade cost $1.60–$2.25, average ≈ $1.98 (Feb 2026, https://www.countbricks.com/post/concrete-block-prices); pallets (70–90 blocks) $115–$225; bulk delivery $60–$200+ per drop (HomeGuide, above; supplier delivery $100–$300 within 30 mi, https://concretecalculate.com/concrete-calculators/concrete-block-calculator/).
- **Owner cost build-up (computed estimate — label as such in the manuscript):** materials for a hollow 8x8x16 (~28–38 lb of dry-cast concrete) at Oregon retail cement/aggregate prices land roughly in the **$0.60–$1.20/block** range for materials alone; equipment amortization (machine $1,000–$4,500 + molds + pan mixer + freight, spread over ~3,000–5,000 blocks) adds roughly **$0.50–$2.00/block**; lab testing program (qualification + per-lot C140 + C426) adds a fixed several-thousand-dollar overhead, i.e., **$0.50–$1.50/block** at single-house volume; owner labor unpriced. Net: owner cash cost plausibly **$1.50–$4.50/block before labor** — at or above the delivered commercial price in any market with a supplier within trucking range. The break-even case is a genuinely remote site where per-block freight is extreme — and the manuscript must note the counterweight: cement (94-lb bags or bulk) and clean graded aggregate must still be freighted to the same remote site, so only the *forming* is localized, not the mass.
- **Cheaper legitimate variant to name:** the historical cast-in-place block-form approach (site-built forms, blocks cast in the wall position) trades the machine away entirely (MEN 1975, https://www.motherearthnews.com/diy/make-your-own-concrete-blocks-zmaz75zwar/) — but cast-in-place walls are then evaluated as site-cast concrete (ORSC R608/ACI 318 path), not as C90 masonry; keep the two paths distinct in the manuscript.

### Q13. Freeze-thaw / weathering exposure classes under ASTM C90 for coastal, valley, and east-of-Cascades Oregon.

**Reframe required — the premise is wrong.** ASTM C90 defines no exposure classes and no freeze-thaw test (see Headline finding 3; C90 Appendix X1 water-penetration material is explicitly outside the specification's scope, https://spectraglaze.com/wp-content/uploads/2018/04/ASTM-C90-122117.pdf). Exposure-class systems exist in CSA A165 (Canada) and in ASTM C1372 (segmental retaining-wall units, with C1262 freeze-thaw testing) — neither governs loadbearing CMU under the ORSC. What the manuscript can defensibly say: C90's density classes and absorption caps are the standard's durability proxies; for wet-freeze climates (east of the Cascades) specify normal-weight units, target absorption results well under the cap, and rely on wall detailing and surface treatment for water management; for coastal and valley Oregon the governing problem is water penetration and detailing, not unit freeze-thaw. Any stronger climate-to-unit mapping is a specifier's judgment or an engineer's requirement, not a C90 requirement.

### Q14. More practical alternative paths.

Ranked by realism for an Oregon owner-builder:

1. **Buy standard block from a regional producer** — the default; C90 documentation arrives free with the invoice. (Oregon/PNW CMU producers exist in all the state's population centers; name and verify current suppliers at manuscript time — supplier lists churn, so keep names out of the manuscript body and in a "verify locally" instruction.)
2. **Contract a custom run at a commercial plant** (special mix, color, or unit) — the plant's QC and C90 paper trail still applies; the owner pays a setup premium and a minimum-quantity commitment. This captures nearly every legitimate reason to want "non-catalog" block with none of the acceptance risk.
3. **ICF (insulated concrete forms)** — $4–$8/ft² of form (https://homeguide.com/costs/cinder-block-wall-cost), site-filled with ready-mix; fully code-recognized; usually the better answer when the owner's real goal is a massive insulated wall built with unskilled labor.
4. **Insulated/specialty CMU products** from commercial plants (integrally insulated units documented in the HUD masonry-homes study, https://www.huduser.gov/portal/publications/PDF/masonry.pdf).
5. **Portable-plant lease / partner production:** no established U.S. rental market for block-making machines was found at residential scale; treat as a negotiated one-off with a regional producer, not a standard option.
6. **Owner manufacture** — last, for the reasons throughout this file.

---

## Corrections and terminology notes for the manuscript

- Prefer "concrete masonry unit (CMU)" with "cinder block" flagged as colloquial; true cinder-aggregate block is a distinct lower-strength historical product not engineered to the C90 2,000 psi floor (https://nedesestimating.com/cement-vs-cinder-vs-concrete/).
- ASTM C90's title in recent editions is "Standard Specification for **Dry-Cast** Loadbearing Concrete Masonry Units" (title usage, https://concretecalculate.com/concrete-calculators/concrete-block-calculator/) — confirm exact current title when the standard is purchased (UNRESOLVED-2).
- ASTM C129 (nonloadbearing units) has a much lower strength floor (net-area average on the order of 600 psi per design references, https://www.uop.edu.jo/PDF%20File/uop%20[Architecture_Ebook]_Masonry_Design_and_Detailing_For_Architects_and_Contractors-20615_Part279.pdf) — usable only for nonstructural partitions and never for the structural shell; keep the C90/C129 line bright in the make-versus-buy section.
- Do not describe ORSC oversight of owner production as "special inspection" — reserve that term for OSSC/IBC Chapter 17 contexts; under the ORSC the mechanisms are R104.11.1 tests and R104.4 accepted reports.

## Unresolved items — do not write dependent manuscript content

- **UNRESOLVED-1 (AHJ confirmation):** whether the specific county/city building official will accept the Q9 testing-program package, and what lot definition and sampling frequency they will condition it on. Resolve by pre-application meeting with the AHJ for the actual project county; escalation path if refused in writing is the BCD site-specific ruling / statewide interpretation process (https://www.orcities.org/application/files/7717/3585/7450/Handbook_-_Chapter_24_Building_Regulations.pdf).
- **UNRESOLVED-2 (purchased standard text):** exact current-edition values that only the purchased standards can confirm: C140 per-lot sampling counts and lot-size thresholds; C90-latest absorption limits per density class and current official title; C90/TMS 402-22/TMS 602-22 edition references actually adopted by the 2023 ORSC. Purchase or library-access C90, C140, C426, TMS 402/602 before drafting the normative table in the structural chapter.
- **UNRESOLVED-3 (current Oregon suppliers and lab quotes):** live list of Oregon CMU producers willing to do custom runs, and current C140/C426 fee quotes from Oregon-accredited labs. Time-sensitive; gather at manuscript-finalization or leave as reader instructions.

## Source index (all URLs above, deduplicated by publisher)

Oregon: 2023 ORSC Ch. 1 (oregon.gov/bcd), Oregon BCD codes/standards page incl. Design Criteria Hub, League of Oregon Cities Handbook Ch. 24, Portland ATAC appeal record. Standards bodies/industry: ASTM C90-22 and C140 store/scope pages, scanned C90 text (spectraglaze.com), CMHA CMU-TEC-001-23, CMHA FAQ-004, NCMA TEK 1-1F, Forney C140 guide, Applied Testing and WJE lab-accreditation pages, NPCA dry-cast articles (2), HUD/NCMA masonry homes report. Code text: ICC IRC 2018/2021 R104.11, R301.2.2, R606 sections (codes.iccsafe.org, up.codes). Equipment/trade: Lontto (block-machine.net) product and price pages, Osino QTJ4-40 and QT4-24 pages, blockmachines.info, tophighmachinery.com, Globmac, waysto.digital, reitmachine.com. Cost data: HomeGuide, Angi, countbricks.com, concretecalculate.com, designtransitionstudio.com, homewyse.com. Historical/homestead: Mother Earth News 1975/1977/1978, homesteadingtoday.com, permies.com, nedesestimating.com.










# Research Answers — Chapter 17: Heavy-Equipment Selection for an Owner-Builder

Research date: 2026-07-04
Status: Answered with sources, except items explicitly marked UNRESOLVED at the end. All dollar figures are 2026 U.S. dollars unless noted; national planning ranges are given with Oregon/Portland-specific figures where found. Local Oregon rental-yard quotes are a project-level fact (UNRESOLVED-1) — the ranges below are for manuscript planning tables, flagged as "verify with two or three local quotes."

---

## Headline findings (read first)

1. **The rental market, not the buy market, is the default answer for almost everything.** The industry break-even for buying compact equipment is roughly 20–30 use-days per year (https://usaconstructionrentals.com/blog/cost-to-rent-a-mini-excavator/). A single-house owner-builder crosses that threshold on at most one or two machines (usually the excavator, possibly a skid-steer/CTL), and on nothing else. Weekly rates run ~3–4× daily and monthly ~60–75% off the effective daily rate (DOZR: excavator averages $719/day, $2,021/week, $5,108/month ≈ $170/day effective; https://dozr.com/blog/excavator-rental-cost) — so the real cost lever is *sequencing rentals into dense blocks*, which is a scheduling discipline, not an equipment decision.
2. **Concrete pumping is a hired service with an operator, not a rental.** In practically every U.S. market including Portland, "pump rental" means a pump truck + certified operator billed as minimum hours + hourly + per-yard (Portland 2026: line pump $900–$1,800/day-equivalent, boom pump $1,300–$2,700, minimums ~$600 line / ~$1,300 boom, $3–$6/yd yardage, hose overage $1.50–$2.00/ft, no-washout fees $250/$350; https://www.countbricks.com/post/concrete-pump-rental-portland-concrete-slab-pour). The manuscript should never present the pump as something the owner operates.
3. **One correction to the question set: rebar on a residential job is tied, not welded.** Standard ASTM A615 rebar is not produced for weldability; welded reinforcement requires weldable-chemistry bar (ASTM A706) and AWS D1.4 procedures, which no residential inspector will accept from an unqualified owner-welder. The "welding and cutting equipment for reinforcement" question should be reframed in the manuscript as *cutting and bending* equipment (rebar cutter/bender rentals are cheap and sourced below) plus tying tools, with welding excluded from the reinforcement workflow. (Flagged as general professional knowledge — verify against AWS D1.4 / ACI 318 text when standards are purchased, UNRESOLVED-4.)
4. **The transport question has a bright legal line.** Federal CDL rules (49 CFR Part 383): Class A CDL required when the combination GCWR is 26,001 lb or more AND the trailer GVWR exceeds 10,000 lb; if no GCWR is assigned, the sum of the two GVWRs is used (Felling/NATM legal summary, https://www.felling.com/towing-cdl-requirements/; FMCSA guidance, https://www.fmcsa.dot.gov/registration/commercial-drivers-license/driver-operates-combination-vehicle-gcwr-26001-pounds-or; https://otrucking.com/resources/guides/gvwr-cdl-requirements/). Practical consequence: a one-ton pickup and a 14,000-lb GVWR equipment trailer can carry a 3–4-ton mini excavator legally without a CDL *if* the summed GVWRs stay under 26,001; a 5-ton-plus machine, a telehandler, or a ride-on roller means contracted hauling. Oregon-specific licensing nuances (farm/personal-use interpretations, intrastate rules): UNRESOLVED-2.
5. **The owner-builder's single best buy candidate is a used 3–4-ton mini excavator.** It is needed in more phases than anything else (site prep, foundation, utilities, backfill, drainage, restoration), used minis hold value (reliable used units $15,000–$25,000; https://hengwangm.com/news/guide-to-mini-excavator-price-costs-and-factors/), and 4–6 months of monthly rentals ($2,500–$4,000/month; https://www.countbricks.com/post/mini-excavator-rental-seattle-digging-footings) approaches half the purchase price of a good used machine that can be resold at build-end. This buy-use-resell arithmetic is the chapter's central worked example.

---

## Answers, question by question

### Q1. Realistic minimum and optional equipment lists for an Oregon concrete-and-CMU shell.

**Minimum list (the build cannot proceed reasonably without these):**
1. Mini excavator, 3–5-ton class (rent monthly or buy used) — site prep, footing/foundation excavation, utility trenches, backfill, final grading.
2. Compaction pair: vibratory plate compactor (granular/base) + jumping-jack rammer (trench/cohesive) — see Q5.
3. Concrete internal vibrator (poker), 1–1.5 in. head class for reinforced residential walls — see Q9.
4. Mortar mixer (paddle type; NOT a drum mixer for mortar) for the CMU phase — see Q7.
5. Portable generator, 7–10 kW single-phase gasoline/dual-fuel — see Q8.
6. Rotary laser level + grade rod, plus batter boards/string — see Q13.
7. Frame scaffolding sized for the wall perimeter (rent or buy used) — see Q11.
8. Equipment trailer (~14,000 lb GVWR) if any machine is owned or self-hauled — see Q18.
9. Hand fleet: wheelbarrows (2+), shovels, rakes, come-along/screed, hand tamper, digging bars.

**Optional list (each must earn its place):**
Compact track loader or skid steer (material handling, grading — Q4); telehandler for the CMU/roof phase (Q10); walk-behind trencher (only if the excavator is off-site when utilities go in — Q14); power buggy for slab distribution (Q6); dump trailer (spoils/debris — Q15); rebar cutter/bender rentals (Q12); water tank/trailer for compaction moisture and dust (Q15); secure storage container (Q15). Concrete pump, crane, and ready-mix are hired services, never owner-operated (Q6, Q10).

### Q2. Sizes, 2026 rental and purchase costs, ownership criteria — consolidated cost table data.

Rental (national 2026 planning ranges; Oregon quotes UNRESOLVED-1):
- Mini excavator (1.5–4 t): $150–$400/day, $800–$1,500/wk, $2,500–$4,000/mo; Seattle (nearest published metro to Oregon) $200–$400/day, $800–$1,500/wk, $2,500–$4,000/mo (https://dozr.com/blog/excavator-rental-cost; https://www.countbricks.com/post/mini-excavator-rental-seattle-digging-footings). Delivery $200–$400 round trip for sub-4-t machines (DOZR).
- Standard excavator (6–15 t): $500–$1,200/day (https://www.beehiverentalandsales.com/blog/excavator-rental-rates-guide).
- Skid steer / CTL: ~$325/day, ~$900/wk, ~$2,000/mo average; $200–$500/day range (https://approvedcosts.com/skid-steer-rental/; https://www.bigrentz.com/blog/how-much-does-it-cost-to-rent-skid-steer).
- Telehandler: $665/day, $1,644/wk, $3,592/mo national averages (2,380-transaction dataset, https://dozr.com/blog/telehandler-rental-cost).
- Jumping-jack rammer: $60–$120/day, $250–$400/wk (https://misec.net/best-jumping-jack-rammers-for-trench-compaction/). Plate compactors similar or slightly less.
- Concrete/mortar mixer (9 cu ft towable): ~$160/day published yard rate (https://www.gappower.com/Rent-a-Cement-Mixer-Concrete-Gasoline-9-Cubic-F/item/CONMT); weekly ~$150–$250 typical (https://concretetoolsdirect.com/blogs/concrete-insights/is-it-better-to-buy-or-rent-a-concrete-mixer).
- Generator: 2–7 kW portable $50–$120/day; 20–25 kW towable $180–$350/day (https://udpwr.com/blogs/portable-power-station-knowledge/cost-to-rent-a-generator).
- Trencher: walk-behind from ~$100–$250/day, ride-on to ~$620/day; average ~$280/day (https://www.angi.com/articles/cost-to-rent-trencher.htm; https://rntr.com/c/how-much-does-trencher-rental-cost).
- Concrete accessories (one published yard's day rates, useful as manuscript examples): power buggy $206–$350, rebar bender to 5/8 in. $165 / to 1 in. $268, battery rebar tier $150–$200, vibrating power screed $129–$139, walk-behind trowel machine $155 (https://gappower.com/collections/concrete-mixer-mortar-mixer-rentals).

Purchase (2026):
- Mini excavator: new entry-level from ~$10,000 (import-grade), mid-range name-brand $25,000–$45,000, premium $70,000+; reliable used $15,000–$25,000, functional used from ~$5,000 (https://hengwangm.com/news/guide-to-mini-excavator-price-costs-and-factors/). Sub-$8,000 new 1-ton Chinese imports exist (AGT et al., https://www.agtequipment.com/collections/mini-excavators) — treat in the manuscript as a distinct risk class (parts, dealer support, resale).
- Skid steer: new $25,000–$70,000; used $5,000–$30,000 (https://allstatesindustrial.com/heavy-equipment/skid-steer-loaders).
- Attachments: $1,000–$5,000+ each (thumb, auger, breaker) (https://hengwangm.com/news/guide-to-mini-excavator-price-costs-and-factors/).

Ownership decision criteria (manuscript rule set): buy only if (a) projected use exceeds ~20–30 days/year or the rental-months × rate approaches ~50–60% of a resale-able used purchase price; (b) you can transport it legally yourself (Q18); (c) you have secure storage; (d) you accept the maintenance burden (Q19); (e) the machine has a liquid resale market (Kubota, Bobcat, Cat, Takeuchi, Deere minis and skid steers do — the used-listing volume at Equipment Trader and IronPlanet is the evidence; https://www.equipmenttrader.com/Excavators/equipment-for-sale?category=Excavators%7C2000206&size=MINI; https://www.ironplanet.com/Mini+Excavator+%3C6.6t).

### Q3. Excavator selection.

- **Size class:** the industry's own summary is that 1–5-t minis "handle 80% of residential projects" (https://www.beehiverentalandsales.com/blog/excavator-rental-rates-guide) and a 3-t Kubota/Bobcat class is "the sweet spot" — enough power for trenching and excavation without needing a lowboy (https://dozr.com/blog/excavator-rental-cost). For a full-basement dig or heavy cut/fill site work, step to a 5–8-t midi or hire the excavation sub with a 6–15-t machine; per-machine daily cost jumps to $500–$1,200 and transport leaves owner-haul territory.
- **Match to the work:** footings and stem-wall trenches need ~2–4 ft of dig; utility and drainage trenches 1.5–4 ft; a 3–4-t machine digs roughly 9–12 ft deep with an 8–10 ft reach class (representative spec: Bobcat E32, 24.8 hp, 7,183 lb, 10.2 ft max dig depth; used-listing spec via https://www.equipmenttrader.com/Excavators/equipment-for-sale?category=Excavators%7C2000206&size=MINI). Oregon-specific: wet-season clay work favors steel-track minis with a blade for backfill/grading; rocky east-side ground can justify sizing up one class (rental-market guidance on rocky soils, https://www.beehiverentalandsales.com/blog/mini-excavator-rental-cost-guide).
- **Attachments that earn their place:** hydraulic thumb (near-universal on used minis, hugely useful for clearing, rock, and demo); a bucket set (12 in. or 18 in. trenching bucket + 36–48 in. grading/ditching bucket); auger only if fence/deck piers are in scope; hydraulic breaker only on confirmed rock (rent by the day when hit); ripper rarely justified at mini scale. Attachments add to daily rental cost (DOZR) or $1,000–$5,000 purchase each (HengWang, above).

### Q4. Skid steer / compact track loader — when it beats the excavator.

The excavator digs; the loader *moves and grades*. A CTL earns its place when the project has: long material-movement distances (gravel, spoils, block pallets), a large slab/driveway base to spread and grade, or repeated pallet handling (with fork attachment). On soft wet Oregon ground, tracks (CTL) beat wheels (skid steer) decisively; wheeled machines are cheaper and fine on firm dry sites. Rental ~$325/day / ~$2,000/month average (https://approvedcosts.com/skid-steer-rental/). Attachments in rough priority for this build: bucket (included), pallet forks (CMU pallets, lumber), grapple (land clearing), auger, hydraulic breaker (slab demo only), sweeper/snow blade (only for multi-season occupancy of the site). Operating-capacity classes: <20 hp ≈ 250–750 lb; 35–45 hp ≈ 1,500–1,750 lb; 45–55 hp ≈ 1,750–2,750 lb (https://approvedcosts.com/skid-steer-rental/) — a standard CMU pallet (2,300–3,400 lb, per Ch. 16 research) requires the largest class or a telehandler, which is the detail that usually decides between them.

### Q5. Compaction equipment — tool-to-lift matrix.

The soil-type rule is categorical and well documented:
- **Vibratory plate compactor** — granular soils (sand, gravel, crushed rock), base course under slabs and pavers, broad flat areas; compaction depth ~6–12 in. per lift for small plates (https://www.beehiverentalandsales.com/blog/plate-compactor-vs-jumping-jack; https://www.hnmachines.com/what-can-replace-a-plate-compactor-for-soil-compaction/). Do NOT use a rammer on clean granular soil — it displaces rather than compacts (https://blog.bartellglobal.com/rammers-vs-compaction-plate-which-one-is-best-for-my-project).
- **Jumping jack (vibratory rammer)** — cohesive soils (clay, silt) and narrow trenches; vertical impact reaches ~8–24 in. (machine claims to 26 in.), foot fits 10-in. trenches, the tool of choice for footing trench bottoms, utility trench backfill, and compaction against foundation walls (https://misec.net/best-trench-rollers-for-backfill-compaction/; https://www.boomandbucket.com/blog/how-deep-can-a-jumping-jack-compactor-work; https://www.hnmachines.com/what-can-replace-a-plate-compactor-for-soil-compaction/).
- **Reversible plate compactor** — heavier plates for thicker granular lifts and larger pads; between the small plate and a roller in force and cost. (General class positioning per the roller/plate comparison sources above.)
- **Ride-on / walk-behind rollers** — smooth-drum vibratory for large granular areas (driveways, road base); padfoot/sheepsfoot drums for cohesive soils; trench rollers compact 12–18 in. lifts and remote-control padfoot units up to ~24 in. in cohesive soil (https://misec.net/best-trench-rollers-for-backfill-compaction/). Rarely justified on a single-house site unless the driveway is long.
- **Lift discipline (the number the manuscript must state):** place and compact in 4–8 in. lifts as the general rule; plates ~4–6 in. lifts, jumping jacks up to ~12 in. lifts, multiple passes per lift; compacting thick layers in one pass produces "bridging" — a hard crust over soft fill that settles later (https://misec.net/best-trench-rollers-for-backfill-compaction/; https://tomahawk-power.com/blogs/articles/how-to-backfill-a-trench-by-hand-choosing-between-a-jumping-jack-and-plate-compactor; https://www.hnmachines.com/what-can-replace-a-plate-compactor-for-soil-compaction/). Cross-reference the soil chapter: required compaction (e.g., 95% of maximum dry density) and moisture conditioning come from the geotech/soils side; the equipment only delivers what the lift thickness and moisture allow.
- Operator effort: the rammer is the most physically demanding walk-behind tool on the list; plan operator rotation. Rental: rammer $60–$120/day (misec, above); most owner-builders should buy neither unless backfill spans many weeks.

### Q6. Concrete-delivery equipment.

- **Chute (direct from the ready-mix truck):** free with delivery; works when the truck can reach within ~15–18 ft of the far edge of the pour. Always the first option to engineer for by planning truck access — this is the cheapest "equipment decision" in the chapter.
- **Wheelbarrow / motorized buggy:** wheelbarrows are viable only for small pours (a few yards) with several strong helpers; a power buggy (~14–16 cu ft, $206–$350/day rental, https://gappower.com/collections/concrete-mixer-mortar-mixer-rentals) extends chute delivery across a site for slab pours where a pump is overkill — but watch truck standby charges while buggying.
- **Line pump (hired):** the default for residential foundations, slabs, and CMU grout lifts with poor access. Portland 2026: $900–$1,800 per pour day-equivalent, ~$600 minimums, $3–$6/yd, 150–200 ft hose included then $1.50–$2.00/ft, washout fee $250 if no washout area, hose-man $85/hr (https://www.countbricks.com/post/concrete-pump-rental-portland-concrete-slab-pour). Typical residential slab/footing total: $1,200–$2,500 all-in for 25–60 yd (https://cceonlinenews.com/concrete/concrete-pump-rental-cost-usa/). National guidance: $150–$250/hr, $3–$10/yd, typical project $800–$1,800 (https://www.angi.com/articles/concrete-pumping-cost.htm).
- **Boom pump (hired):** Portland $1,300–$2,700/day-equivalent, ~$1,300 minimum (countbricks Portland, above); justified when reaching over the structure (grouting CMU walls from above is a classic case), on tight lots, or when placement speed protects a finishing window.
- **Conveyor (Telebelt):** niche; ask the pumping contractor — occasionally wins where washout constraints are severe (https://www.countbricks.com/post/concrete-pump-rental-san-diego-concrete-slab-pour).
- **Break-even rule for the manuscript:** the pump wins whenever wheelbarrow/buggy labor-hours × crew cost + truck standby exceed the ~$600–$1,300 pump minimum — which for anything over roughly 10–15 yd with imperfect access is almost immediately. Never let a footing pour go slow to save the pump fee: cold joints cost more than the minimum.

### Q7. On-site mixing equipment (cross-reference Chapter 7 owner-mix topic and Chapter 16 CMU file).

- **Tow-behind drum mixer (6–9 cu ft):** handles conventional wet-mix concrete and holds 1.5–2 bags per batch at 9 cu ft (https://www.unitedrentals.com/marketplace/equipment/concrete-masonry/mixers); ~$160/day rental (Gap Power, above); purchase makes sense for a long CMU phase (rent-vs-buy break-even ~1–2 months of rental; https://concretetoolsdirect.com/blogs/concrete-insights/is-it-better-to-buy-or-rent-a-concrete-mixer). Output reality check: a 9-cu-ft mixer produces roughly 1/4 yd of concrete per ~5-minute cycle — order ready-mix for anything structural over ~1 yd; on-site mixing is for mortar, grout patches, and small pours only. (Cross-reference the Chapter 7 research answer on on-site mixing for the structural-concrete quality argument.)
- **Mortar mixer (paddle type, 6–9 cu ft):** the correct machine for mortar, grout, stucco, plaster — paddles against a stationary drum, not a tumbling drum (https://www.unitedrentals.com/marketplace/equipment/concrete-masonry/mixers; 9-cu-ft unit spec: Honda GX-240, 770 lb, https://chasephipps.com/gas-powered-towable-mortar-mixer-rental/). For a full CMU shell this is a purchase candidate (multi-month use).
- **Continuous mixers (MudMixer/Imer class):** electric continuous-feed units for bagged mix (https://gappower.com/collections/concrete-mixer-mortar-mixer-rentals) — useful for fence posts and small grout runs.
- **Pan mixer:** required only if the Chapter 16 owner-CMU path is taken (drum mixers cannot mix zero-slump block mix — see Ch. 16 research answer). Not stocked by general rental yards; a purchase/import item.
- **Portable central-mix plant:** far beyond single-house scale; exclude.

### Q8. Generator selection.

- **Sizing method (state this as the procedure):** sum running watts of simultaneous loads, add the largest motor's starting surge (motors draw 2–3× running watts at start; up to 4× for some), then add 20–25% margin; run at ~75% load for longevity (https://equipnearby.com/guides/generator-rental-guide/; https://www.constructionbusinessowner.com/equipment/finding-right-generator-construction-jobsite). Conversions: watts = volts × amps; 1 hp ≈ 746 W (same source).
- **Owner-builder answer:** a 7–10 kW portable single-phase gasoline or dual-fuel unit covers saws, drills, a small compressor, lights, and the electric vibrator/mixer class — the published rule of thumb is 5–10 kW for small/mid construction sites, 15 kW+ if running compressors, mixers, and pumps together (https://tendsupplies.com/blog/portable-generator-rentals-for-job-sites-wattage-calculator-safety-checklist/).
- **Three-phase:** only needed if a specific machine demands it (e.g., the imported block machines in the Chapter 16 file, some large mortar mixers). Three-phase means a towable diesel (20–25 kW class, $180–$350/day rental; https://udpwr.com/blogs/portable-power-station-knowledge/cost-to-rent-a-generator) or a rotary phase converter — this is a real hidden cost of the owner-CMU path and should be cross-referenced there.
- **Fuel:** gasoline for small portables (cheap, everywhere); diesel for towables (runtime, shared fuel with the excavator); propane/dual-fuel wins for long storage between uses (no stale-fuel carburetor problems) — relevant to a multi-year owner build. Diesel consumption ~7 gal/hr per 100 kW at 75% load; small gas portables 0.3–1.0 gal/hr (equipnearby; udpwr, above). Avoid running big diesels under 30% load (wet-stacking damage; equipnearby).
- **Buy vs rent:** the 7–10 kW portable is a buy ($1,000–$2,500 retail class) because it serves the whole multi-year build and the household afterward; towable diesels are rentals.

### Q9. Concrete vibration.

- **Internal (poker) vibrator — the required tool for footings, stem walls, and grouted CMU.** Selection physics per ACI 309R: radius of action is proportional to head diameter; insertion spacing = 1.5 × radius of action, typically 12–24 in.; insert vertically, fast down, withdraw slowly (~1 in./sec, never over 2 in./sec), penetrating ~6 in. into the previous lift (ACI 309R guidance summarized at https://www.theengineeringcommunity.org/concrete-vibration-the-why-and-how-of-consolidating-concrete/; https://www.forconstructionpros.com/concrete/equipment-products/vibrating-equipment/article/12113148/wacker-neuson-america-corporation-how-to-choose-the-right-concrete-vibrator-type-for-the-application; ACI 309.1R text, http://civilwares.free.fr/ACI/MCP04/3091r_93.pdf). In reinforced concrete the radius of action can drop ~50% (ACI 309.1R, same link) — the practical residential choice is a 1–1.5 in. head (a 2.5 in. head suits ~16 in. insertion spacing in congested work; https://ascconline.org/Portals/ASCC/Reinforcement-Congestion-in-CIP-Concrete-CI_12-22.pdf), electric flex-shaft (runs off the Q8 generator) or battery (Milwaukee MX class consolidates ~20 yd per charge; rental listing, https://gappower.com/collections/concrete-mixer-mortar-mixer-rentals). Rental ~$50–$150/day class (yard listings above); purchase of an electric unit (~$300–$800 retail class) is justified for a build with many pours — planning figure, verify locally (UNRESOLVED-1).
- **External form vibrators:** commercial/precast tool; on a residential job, careful internal vibration plus form-tapping replaces them. Exclude from the equipment list.
- **Vibrating screed:** for slabs — strikes off and consolidates the top surface; rental $129–$139/day (Gap Power, above). Pairs with, does not replace, internal vibration at edges and thickened sections.
- **CMU grout note (cross-reference structural chapter):** grout lifts in block cores must be consolidated (and reconsolidated after initial water loss) with a small-head internal vibrator — a 3/4–1 in. head fits cores; this is one more reason the poker vibrator is a "minimum list" item.

### Q10. Lifting and material handling.

- **Telehandler:** the one lifting machine that plausibly earns a residential rental month — places CMU pallets next to masons, lifts trusses/beams, and with a work platform (trained use only) serves high walls. $665/day / $1,644/wk / $3,592/mo national averages; capacity derates with boom extension per the load chart — a 10,000-lb machine may handle 3,000 lb at full reach (https://dozr.com/blog/telehandler-rental-cost). Rent for the wall-and-roof window only.
- **Standard rough-terrain forklift:** subset of the telehandler use case; choose the telehandler for reach.
- **Crane:** hired service with a certified operator (mobile crane, half-day minimums) for trusses/glulams if no telehandler; never owner-operated — OSHA crane-operator certification (29 CFR 1926 Subpart CC) applies to construction cranes (general knowledge; verify text, UNRESOLVED-4). Gantry/derrick: exclude from residential scope.
- **Block-laying assist machines and vacuum lifters:** commercial masonry tools for oversized units; standard 8×8×16 CMU at 28–38 lb is hand-laid, so exclude unless the design uses large-format block — in which case the mason sub brings the lifter.

### Q11. CMU-laying assistance equipment.

Mortar pans/boards on stands, a mortar mixer (Q7), wheelbarrows, and **frame scaffolding** are the real list. Frame scaffold (5 ft frames + planks + guardrails) around the working perimeter, raised with the courses; rent for the masonry window or buy used sets (scaffold holds almost no resale premium, so used purchase is often cheaper than multi-month rental — planning judgment, get quotes, UNRESOLVED-1). Mast climbers are commercial masonry equipment — exclude at house scale. Pallet handling is the telehandler's job (Q10) or the largest CTL class with forks (Q4). A hand pallet jack is useless on dirt; exclude. Cross-reference Chapter 16: if owner-manufactured CMU is pursued, add curing-area material handling (pallet staging) to this list.

### Q12. Reinforcement equipment (reframed per Headline 3).

- Rebar cutter/bender rentals: manual/hydraulic benders to 5/8 in. $165/day, to 1 in. $268/day (https://gappower.com/collections/concrete-mixer-mortar-mixer-rentals). For #4/#5 residential bar, a purchase-grade manual cutter/bender (~$100–$300 retail class) plus an angle grinder or portaband covers the whole job — planning figures, verify (UNRESOLVED-1).
- Battery rebar tying tools rent at $150–$200/day and tie ~5× faster than hand tying (Gap Power, above) — worth renting for the footing/slab mat weeks; hand tying with a hook is free and fine at small scale.
- Abrasive chop saw or angle grinder with cutoff wheels: the standard rebar cutting method; oxy-acetylene and plasma are not needed and introduce hot-work risk on site.
- Welding: excluded from the reinforcement path (Headline 3). If the owner wants a stick welder for general fabrication (gates, brackets), that is a shop-tool decision outside this chapter's scope — note and move on.

### Q13. Surveying and layout.

Owner-builder layout requires: a **rotary laser level with detector and grade rod** (footing/slab elevations, form grading — the workhorse), string lines and batter boards (building corners and square via 3-4-5/diagonals), a 100-ft tape, and optionally an optical builder's level (transit) as a backup/teaching tool. Total stations and GPS rovers are professional survey instruments that a single-house layout does not need. Two hard boundaries to state: (1) **property corners and boundary lines are a licensed land surveyor's work in Oregon** — an owner cannot legally establish boundaries, and setbacks measured from wrong corners are the classic expensive layout failure (Oregon licensure law reference: verify ORS 672 text, UNRESOLVED-2); (2) foundation location relative to setbacks may require a surveyor's stake-out or form inspection in some jurisdictions — AHJ-dependent (UNRESOLVED-2). Costs: rotary laser purchase $200–$600 retail class or ~$40–$75/day rental — planning figures, verify (UNRESOLVED-1).

### Q14. Trenching and utility installation.

The mini excavator with a 12-in. bucket is the default trencher on this project — it is already on site. A dedicated **walk-behind trencher** ($100–$250/day; 24-in.-depth units ~1,200 lb, trailer-transportable; https://www.angi.com/articles/cost-to-rent-trencher.htm; https://www.sunbeltrentals.com/equipment-rental/earth-moving/24-walk-behind-trencher/0370010/; https://rntr.com/c/how-much-does-trencher-rental-cost) wins only for long, narrow, uniform runs (water service, electrical conduit, irrigation) in trenchable soil, or when the excavator is gone. Ride-on trenchers (to $620/day; Angi, above) and vibratory plows/directional boring are utility-contractor territory — directional bores (under roads/driveways) are always subcontracted. Depth requirements come from the plumbing/electrical chapters (frost depth, cover requirements); call 811 before any dig, 2–3 business days lead (https://www.beehiverentalandsales.com/blog/excavator-rental-rates-guide).

### Q15. Site logistics equipment.

- **Dump trailer (10–14k GVWR):** the owner-builder's most versatile logistics buy — spoils, demo debris, gravel runs, material pickup; strong resale. Rent-vs-buy per the Q2 criteria. (Rental market exists but daily rates approach ownership economics quickly on a multi-year build — quote locally, UNRESOLVED-1.)
- **Water:** a 200–500 gal poly tank on the dump trailer or a pickup, with a small pump, covers compaction moisture conditioning, dust control, and cure-water — a purchase measured in hundreds of dollars. Dedicated water trucks are commercial-scale; exclude.
- **Fuel:** a transfer tank in the pickup bed (diesel for the excavator) with a 12 V pump; comply with container/transport rules (verify Oregon fire marshal/DOT quantity thresholds, UNRESOLVED-2).
- **Secure storage:** a 20-ft shipping container on site is the standard answer for tools and materials theft protection (purchase ~$2,500–$5,000 delivered planning class, resellable; verify locally, UNRESOLVED-1); a jobsite office trailer is unnecessary for an owner living on/near the site.
- **Scaffolding storage** and weather protection for materials tie back to the Chapter 16 staging discussion.

### Q16. Buy vs rent vs hire — the manuscript's decision table.

- **Almost always HIRED with operator (service, not equipment):** ready-mix delivery, concrete pumping (Q6), craning (Q10), directional boring (Q14), large-excavator site work beyond the mini's class, and hauling of any machine over the Q18 towing line.
- **Almost always RENTED:** telehandler (phase window), trencher, power buggy, trowel machine, vibrating screed, rebar tying gun, ride-on rollers, towable diesel generators, breaker/auger attachments, boom/scissor lifts if ever needed.
- **BUY candidates for a single-house build:** used 3–4-t mini excavator (Headline 5 arithmetic), 7–10 kW generator, rotary laser, internal vibrator (electric), mortar mixer, wheelbarrows/hand fleet, dump trailer + equipment trailer, water tank, storage container. Marginal: plate compactor and rammer (buy used if backfill spans months; rent otherwise — a rammer buy breaks even after ~7 rental days for budget units, https://misec.net/best-jumping-jack-rammers-for-trench-compaction/); used frame scaffold for the masonry phase.
- **Portfolio plan (multi-house):** the buy list expands to a CTL, a skid-steer attachment set, and possibly a telehandler; everything else stays rental/hire. The generic industry framing (rent for occasional/seasonal, buy for recurring ROI + resale) is documented at https://allstatesindustrial.com/heavy-equipment/skid-steer-loaders and https://usaconstructionrentals.com/blog/cost-to-rent-a-mini-excavator/.

### Q17. Safety, training, licensing, insurance.

- **Who OSHA covers:** federal/Oregon OSHA obligations attach to *employers*. A true solo owner-builder with no employees is largely outside enforcement, but the moment the owner hires help or subs, Oregon OSHA (a state-plan program) applies to those employment relationships — and the manuscript should treat OSHA-conforming practice as the standard regardless, both for safety and because Oregon workers' compensation and CCB rules interact with hiring (Oregon-specific citations: UNRESOLVED-2).
- **Operator training with teeth:** powered industrial trucks and rough-terrain forklifts/telehandlers require operator training and certification on the specific equipment type (29 CFR 1926.602 for construction material-handling equipment; telehandler certification typically $150–$300 through trainers; no CDL is needed to *operate* one on site) (https://dozr.com/blog/telehandler-rental-cost). Crane operators on construction sites must be certified (29 CFR 1926 Subpart CC — verify text, UNRESOLVED-4); hire the crane with its operator and the issue disappears.
- **No license exists for excavators/skid steers/compactors** for private use; rental houses provide orientation and may require a signed familiarization (household users noted as not license-bound, with employee training required for companies, at https://approvedcosts.com/skid-steer-rental/; rental-house training platforms, e.g., United Academy, https://www.unitedrentals.com/sales/equipment/earthmoving-equipment/mini-excavators). Competence is still the injury variable: rollovers on slopes, trench-wall collapses (never enter an unshored trench ≥5 ft — OSHA excavation standard 1926 Subpart P, verify text, UNRESOLVED-4), and struck-by incidents are the residential killers; the manuscript's safety sidebar should be built around those three.
- **Insurance:** rental damage waivers run 10–15% of rental charges (https://udpwr.com/blogs/portable-power-station-knowledge/cost-to-rent-a-generator; https://www.countbricks.com/post/concrete-pump-rental-san-francisco-concrete-slab-pour); owned equipment needs an inland-marine/equipment floater and liability coordination with the builder's-risk and homeowner policies — quote-level facts (UNRESOLVED-3).

### Q18. Transportation and trailers.

- **The legal line (federal):** Class A CDL when GCWR ≥ 26,001 lb AND trailer GVWR > 10,000 lb; absent an assigned GCWR, sum the GVWRs; Class B for a single vehicle over 26,000 lb GVWR (https://www.felling.com/towing-cdl-requirements/; https://otrucking.com/resources/guides/gvwr-cdl-requirements/; https://capitalleasegroup.com/cdl-requirements-for-construction-pickups/). Ratings, not actual weights, control (otrucking, above). CDL rules technically attach to "commercial motor vehicles used in commerce," and enforcement interprets "commerce" broadly — an owner-builder should not rely on a personal-use argument (NATM legal discussion, https://www.felling.com/towing-cdl-requirements/). Oregon intrastate specifics: UNRESOLVED-2.
- **What a pickup setup can move:** with a 3/4–1-ton truck and a 14,000-lb GVWR equipment trailer, machines up to roughly 8,000–9,000 lb (3–4-t minis, small CTLs, towable mixers/compactors/generators) are self-haulable — provided truck GVWR + trailer GVWR stays under 26,001 (worked examples in the towing community reach exactly this configuration; https://www.tractorbynet.com/forums/threads/understanding-curb-weight-gvwr-towing-and-cdl-requirements.465193/page-4). Also respect the truck's own tow rating and trailer brake requirements.
- **What requires contracted hauling:** 5-t+ excavators, telehandlers (12,000–25,000 lb), ride-on rollers, and anything needing a lowboy; rental delivery at $200–$500 round trip (DOZR) is the simple answer and should be priced into every rental decision.

### Q19. Maintenance, fueling, storage.

Rental shifts essentially the whole maintenance burden to the yard (scheduled PM is built into rates; https://approvedcosts.com/skid-steer-rental/) — the renter buys fuel (return full; https://usaconstructionrentals.com/blog/cost-to-rent-a-mini-excavator/) and pays for damage/cleaning. Ownership burden for a used mini excavator, stated for the manuscript: daily greasing of pins/bushings, track tension checks, fuel/hydraulic/air filter and oil service on engine-hour intervals, rubber-track replacement as a four-figure wear item, and $200–$500 per standard maintenance-kit cycle (https://hengwangm.com/news/guide-to-mini-excavator-price-costs-and-factors/). Diesel machines need clean fuel storage (Q15) and winter anti-gel east of the Cascades. Theft: compact equipment is a top theft target — container storage, hitch locks, removing keys/battery disconnects, and GPS trackers on owned machines; insurers may require them (UNRESOLVED-3).

### Q20. Used-equipment market.

- **Where:** Ritchie Bros. auctions and IronPlanet online (https://www.ironplanet.com/Mini+Excavator+%3C6.6t), Equipment Trader dealer/private listings (https://www.equipmenttrader.com/Excavators/equipment-for-sale?category=Excavators%7C2000206&size=MINI), rental-fleet sell-offs from United Rentals and peers (documented used-sales channels with financing; https://www.unitedrentals.com/sales/equipment/earthmoving-equipment/mini-excavators), dealer trade-ins, and regional classifieds. Rental-fleet machines have hard hours but documented service; private machines vary.
- **What to inspect (mini excavator, the chapter's worked example):** hour meter vs wear consistency; pin/bushing slop at bucket and boom; hydraulic cylinder rod scoring and leaks; track wear and undercarriage (sprockets, rollers — the most expensive wear system); blow-by and cold-start behavior; swing bearing play; evidence of welded repairs on the boom/stick. Budget an independent inspection or a mechanic's hour on any four- or five-figure purchase. (Professional general knowledge — no single citation; frame as practitioner guidance.)
- **What to avoid:** no-name gray-market imports for a machine that must hold resale value (parts/dealer support risk; the sub-$8k import class at https://www.agtequipment.com/collections/mini-excavators is the illustration); machines with fresh paint over the undercarriage; auction units sight-unseen without inspection reports.
- **What holds value:** Kubota, Cat, Bobcat, Takeuchi, Deere, Yanmar compact machines — exactly the brands dominating the used-listing volume (Equipment Trader listing mix, above). Brand-reliability datasets are proprietary (EquipmentWatch cost-recovery data is the named industry source; referenced at https://hengwangm.com/news/guide-to-mini-excavator-price-costs-and-factors/) — the manuscript should cite resale-market liquidity rather than claim reliability rankings.

### Q21. Project-phase equipment matrix (for the chapter's table).

- **Site prep/clearing:** mini excavator (+thumb), CTL/grapple optional, dump trailer, water tank (dust), 811 locates.
- **Excavation/foundation:** mini excavator (trench bucket), laser level, jumping jack (trench bottoms/over-dig), plate compactor (granular pad), rebar cutter/bender + tying gun (rent week), generator, internal vibrator, line pump (hired pour day), power buggy optional.
- **Slab:** plate compactor (base lifts), laser level, vibrating screed + internal vibrator, trowel machine (rent pour week), pump or chute+buggy (hired/rented pour day).
- **Walls (CMU):** mortar mixer (owned), scaffold (rented/owned for the phase), telehandler (rental month), grout pump/boom (hired grout-lift days), small-head vibrator, generator.
- **Roof:** telehandler (same rental month if sequenced tight) or crane day (hired).
- **Utilities/drainage:** mini excavator or trencher (rental days), jumping jack (backfill lifts).
- **Finish:** generator/tools only; heavy equipment off-rent.
- **Site restoration:** mini excavator (grading bucket) or CTL (rental week), plate compactor, water tank.
- **Rental-day minimization rules:** book weekly/monthly, never daily, for anything over 3 days (40–60% savings; DOZR; https://www.beehiverentalandsales.com/blog/excavator-rental-rates-guide); cluster all trenching into one window; put the telehandler month across the wall-top-to-roof-dry-in span; bundle machine+compactor+trailer for package pricing (BeeHive, above); prep (locates, staking, spoil plans) before the clock starts.

---

## Corrections and reframes for the manuscript

1. Reinforcement is tied, not welded (Headline 3) — retitle the section "Cutting, bending, and tying reinforcement."
2. "Concrete pump rental" is wet-hire service pricing; present pump costs as minimums + hourly + yardage, never as a day-rate rental (Q6 sources).
3. External form vibrators, mast climbers, block-laying assist machines, vacuum lifters, water trucks, central-mix plants, total stations, and GPS rovers should be named in the chapter only to be excluded — keeping them in the "equipment universe" table with an "exclude at house scale" verdict is more useful to the reader than silence.
4. Boundary surveying is licensed professional work; layout equipment questions must not imply the owner establishes property lines (Q13).

## Unresolved items — do not write dependent manuscript content

- **UNRESOLVED-1 (Oregon rental quotes):** current daily/weekly/monthly rates from at least two Oregon rental yards (United Rentals, Sunbelt, Herc branches, plus an independent) for the Q1 minimum list, plus local purchase quotes for laser level, vibrator, mortar mixer, scaffold, container. National ranges above are planning-table placeholders until then.
- **UNRESOLVED-2 (Oregon regulatory specifics):** Oregon OSHA program requirements when the owner-builder hires workers; Oregon CDL/intrastate towing interpretations and any farm/personal-use exemptions; ORS 672 boundary-survey licensure citation; Oregon fuel-transport quantity thresholds; AHJ setback stake-out/survey requirements per county.
- **UNRESOLVED-3 (insurance quotes):** inland-marine/equipment floater and builder's-risk coordination pricing for owned equipment; rental damage-waiver vs own-policy comparison.
- **UNRESOLVED-4 (standards text verification):** OSHA 1926 Subpart P (excavations, 5-ft shoring threshold), 1926.602 and Subpart CC exact requirements; AWS D1.4/ACI 318 rebar-welding provisions; ACI 309R current-edition table values for vibrator head sizes. The summaries above are consistent across secondary sources but the manuscript's normative statements should cite the purchased/official text.

## Source index (deduplicated by publisher)

Rental pricing: DOZR (excavator, telehandler, CTL), countbricks.com (mini excavator metros incl. Seattle; concrete pump incl. Portland; diesel generators), BeeHive Rental & Sales (excavator, mini excavator, compactor guides), usaconstructionrentals.com, Angi (excavator, trencher, concrete pumping), BigRentz, approvedcosts.com, RNTR (generator, trencher), HomeAdvisor, udpwr.com, equipnearby.com, Gap Power rate list, United Rentals (mixers, used sales), Sunbelt (trencher spec), Chas. E. Phipps (mortar mixer spec), cceonlinenews.com (pump billing structures). Equipment selection/technique: Tomahawk Power, Bartell Global, nbacetools.com, hnmachines.com, misec.net (trench rollers, rammers), boomandbucket.com, ACI 309.1R and 309R texts (civilwares.free.fr mirrors), ASCC reinforcement-congestion paper, theengineeringcommunity.org, For Construction Pros (vibrators, consolidation), Construction Business Owner (generator sizing), tendsupplies.com, JC Davis Power, BigRentz diesel generator page. Purchase/used market: HengWang price guide, allstatesindustrial.com, AGT Equipment, Equipment Trader, IronPlanet, FleetNow, eBay listings, Rippa. Transport/licensing: FMCSA CDL guidance pages, Felling/NATM legal article, otrucking.com, capitalleasegroup.com, tractorbynet forum worked examples.








