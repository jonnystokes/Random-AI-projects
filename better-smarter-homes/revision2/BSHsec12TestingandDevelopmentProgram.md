# Section 12 — Testing and Development Program

*Prove it before you pour it — the home as laboratory*

This section covers the research and testing work that happens BEFORE and DURING the build. The main design answers "what should be built"; this program answers "are we sure this works?" Concrete mixes get tested for strength. Fiber reinforcement gets proven. Insulation R-values get verified. Wall assemblies get mocked up at full scale. The testing program turns the design from a set of educated guesses into a set of verified facts.

The guiding philosophy: **test before committing**; **destructive testing reveals what calculation can't**; **DIY testing using published methods is accessible, rigorous, and cheap**; **every home built teaches the next one**; **document everything so the knowledge compounds across builds**.

---

## 12.1 Why a Testing Program

**Plain language:** Every major design decision in this document is based on calculations, published research, and industry standards. But there's a gap between textbook and reality — between "a 7-inch slab with fibers at 1% volume should carry X load" and "this specific slab, made with this specific mix, in this specific climate, actually carries X load." Closing that gap with hands-on testing before committing a whole house to those assumptions is the difference between engineering and speculation.

**Technical detail:** Core testing principles:

- **Test the specific conditions of this build** — concrete mix, local sand, local climate, specific fiber products — not generic averages
- **Use published, peer-reviewed testing methods** where possible — DIY doesn't mean improvised
- **Document every test** — test method, conditions, measurements, results, interpretation
- **Accept surprises** — if a test contradicts design assumptions, the design changes, not the test
- **Test in time to act on the results** — testing happens BEFORE design is final, not after construction is underway
- **Build up the testing program over time** — every test creates reference data for future tests and future builds

**What testing does NOT replace:**
- **Licensed professional engineering** — a stamped structural design still defines the minimum; testing validates and refines, doesn't replace
- **Code compliance** — code is the floor; testing proves the design meets or exceeds it
- **Inspection** — testing is the owner's quality assurance, inspections are the jurisdiction's

**What testing DOES add:**
- **Confidence** — the owner-builder knows, from hands-on evidence, that every decision is sound
- **Refinement** — testing reveals which design parameters can be tightened and which need buffer
- **Learning** — each test builds the owner-builder's intuition for materials and systems
- **Documentation** — testing produces a body of evidence that supports the design story (useful for resale, for future builds, for the BSH brand)

---

## 12.2 Testing Program Overview

**Plain language:** The testing program has five main tracks: concrete, insulation, air sealing, radiant performance, and full-scale assemblies. Each track has multiple tests, each test has a purpose, and the results from each test feed back into the design. Most testing happens during the "pre-construction" phase (before the foundation pour) and the "first build" phase (using the first home as a validator).

**Technical detail:** Testing tracks:

| Track | Primary Purpose | Testing Phase | DIY Feasibility |
|---|---|---|---|
| Concrete mix design | Validate strength, workability, cost | Pre-construction | High |
| Fiber reinforcement | Validate crack resistance, flexural capacity | Pre-construction | High with destructive testing |
| Slab thickness | Validate load capacity of thin fiber-reinforced slabs | Pre-construction | Moderate |
| Insulation R-value | Verify thermal performance of specific products | Pre-construction, ongoing | High with DIY hot box |
| Wall thermal bridging | Validate assembly-level R-value, not just component | During construction | Moderate with thermal camera |
| Air sealing | Measure envelope tightness | During construction | High with blower door |
| Radiant response | Tune heating and cooling response | Post-installation | High with logging thermometer |
| Full-scale wall mockup | Proof-of-concept for the full assembly | Pre-construction | Moderate |

**Testing timeline (relative to build):**

- **Year −2 to Year −1 (before breaking ground):** concrete mix tests, fiber tests, wall mockup, insulation R-value bench tests
- **Year −1 to Year 0 (design-finalization and permit phase):** destructive slab tests, final mix specification, architectural revisions based on test results
- **Year 0 to Year 3 (construction):** in-situ testing during construction — thermal camera surveys, blower door tests, pressure tests on systems
- **Year 3+ (post-occupancy):** performance monitoring, energy use tracking, comparison against design targets
- **Year 5+ (next build):** carry forward the results, refine the design, new tests as new questions arise

---

## 12.3 Concrete Mix Design Testing

**Plain language:** The specific concrete mix for this build (pozzolanic blend with silica fume, calcium nitrite corrosion inhibitor, low water-cement ratio — see Section 4) exists in textbooks and industry papers but isn't the same as the mix the local ready-mix plant has delivered a thousand times. Before committing a whole foundation to this mix, test batches get made and tested for strength, workability, and finish characteristics.

**Technical detail:** Concrete mix testing program:

**Test batches:**

**Batch 1 — Design mix (target recipe):**
- **Cement:** 25% Type I/II Portland + 25% fly ash + 5% silica fume (by weight of cementitious materials)
- **Aggregate:** local 3/4 inch coarse aggregate + local concrete sand
- **Water-cement ratio:** 0.38 (below 0.40 target)
- **Admixtures:** calcium nitrite (at manufacturer's dose), water-reducing admixture (plasticizer)
- **Purpose:** validate the primary design mix

**Batch 2 — Reference mix (standard residential):**
- **Cement:** 100% Type I/II Portland
- **W/C:** 0.45
- **No admixtures**
- **Purpose:** baseline for comparison — how much better is the design mix?

**Batch 3 — Value-engineered mix (cost-reduced):**
- **Cement:** 30% Portland + 30% slag + 0% silica fume
- **W/C:** 0.42
- **Admixtures:** only corrosion inhibitor
- **Purpose:** if the design mix proves overkill, the VE mix might be good enough

**Batch 4 — Fiber-reinforced mix (for slabs):**
- **Design mix as Batch 1, plus:**
- **Steel fibers:** 40 lb/yd³ (Dramix or equivalent)
- **Polypropylene fibers:** 1.5 lb/yd³ (Forta-Ferro or equivalent)
- **Purpose:** validates the fiber-reinforced floor slab design

**Batch sizes:**
- **Small batches:** 1–2 cubic feet each (mixed on-site in a portable mixer)
- **Enough for:** multiple test cylinders, small slab samples for destructive testing, mockup sections

**Standard test specimens:**

**Compressive strength cylinders (ASTM C31 / C39):**
- **6 inch diameter x 12 inch tall cylinders** cast in plastic molds
- **Cured in water bath at 73°F** (standard curing)
- **Tested at:**
  - 7 days (typical 65% of 28-day strength)
  - 14 days (typical 85%)
  - 28 days (design strength)
  - 56 days (continued gain with pozzolanic mixes)
  - 90 days (long-term strength)
- **How many:** 3 cylinders per test age per batch = 15 per batch = 60 total across 4 batches
- **Test method:** compression testing machine applies axial load until failure; peak load / cross-section area = compressive strength

**Where to get cylinders tested:**
- **Commercial concrete testing lab** — every metro area has one; cost $25–$50 per cylinder crush
- **Local community college civil engineering department** — may have a testing machine and a faculty member willing to help
- **University engineering department** — often offers testing services; good relationship-building for owner-builder credibility
- **NOT DIY** — compression testing requires specialized equipment

**Flexural (bending) strength beams (ASTM C78):**
- **6 x 6 x 20 inch beams** for third-point loading test
- **For the fiber-reinforced mix specifically** — flexural strength is where fibers matter most
- **Tested at:** 28 days
- **How many:** 3 beams per fiber-reinforced batch

**Slump test (ASTM C143):**
- **Measures workability** — cone filled with concrete, inverted, concrete "slumps" — slump distance indicates plasticity
- **Target slump for this design:** 4–6 inches (flowable but not watery)
- **DIY-able** — a slump cone costs $50–$100; anyone can do the test

**Air content test (ASTM C231 or C173):**
- **Target:** 4–7% entrained air for freeze-thaw resistance
- **Measurement device:** air meter (pressure method or volumetric)
- **Cost:** $500–$1,500 for the device; sometimes borrowable from the concrete supplier

**Testing schedule:**
- **Week 1:** cast all test specimens from all four batches on the same day
- **Week 2:** first slump and air tests; 7-day cylinder break
- **Week 4:** 28-day cylinder break (primary data point)
- **Week 8:** 56-day cylinder break
- **Week 13:** 90-day cylinder break

**Results documentation:**
- **Spreadsheet with every cylinder** — batch number, age at test, failure load, compressive strength
- **Graphs** — strength vs. age for each batch, comparison between batches
- **Photos** — every cylinder at break showing failure mode

**Decision criteria:**
- **Design mix must exceed** 5,000 psi at 28 days (well above code minimum of 3,000 psi for most structural concrete)
- **If batch 1 fails to meet target,** iterate: adjust W/C ratio, change admixture dose, change supplier
- **If batch 1 greatly exceeds target,** consider VE version (Batch 3) for non-critical applications like backfill walls
- **Fiber-reinforced mix must show** at least 25% increase in flexural strength over unreinforced

---

## 12.4 Fiber Reinforcement Testing

**Plain language:** Steel and polypropylene fibers mixed into concrete are supposed to dramatically improve crack resistance and the concrete's ability to hold together after first crack. The key test is destructive bending — break a beam and see how the fibers change its behavior. An unreinforced beam snaps cleanly. A fiber-reinforced beam cracks but holds together, sometimes carrying more load after the first crack than before it.

**Technical detail:** Fiber testing program:

**Fiber types under test:**

- **Steel fibers (Dramix 3D, 4D, or 5D — Bekaert):** hooked-end steel, 50–60 mm long, highest performance, most common
- **Macro synthetic fibers (Forta Ferro, Grace Strux):** polyolefin, similar geometric characteristics to steel, non-rusting
- **Micro synthetic fibers (polypropylene microfiber):** very fine, thousands per pound, for plastic shrinkage crack control

**Test program:**

**Mix variants for fiber comparison:**
1. **Control** — no fibers
2. **Steel fibers only** (40 lb/yd³)
3. **Macro synthetic only** (6 lb/yd³)
4. **Dual reinforcement** — steel + micro synthetic (40 lb/yd³ steel + 1.5 lb/yd³ PP)

**Test specimens:**

**Flexural beams (primary test):**
- **6 x 6 x 20 inch beams, third-point loading** (ASTM C1609 for fiber-reinforced concrete specifically)
- **Measures:** first-crack strength, peak strength, post-crack residual strength at various deflections
- **Interpretation:**
  - **Control beam:** sharp load drop at first crack → brittle failure
  - **Fiber beam:** load holds or increases after first crack → ductile failure (fibers are working)
  - **Toughness index** quantifies the fiber contribution

**Impact test (punch-through):**
- **6 x 6 x 1.5 inch slab samples**, supported at corners
- **Steel ball or hammer dropped from known height**
- **Count impacts until first crack, until failure**
- **Purpose:** real-world toughness — simulates dropped tools on a floor
- **DIY-able** — a sledgehammer and a measured drop distance

**Crack propagation observation:**
- **Induce a crack** in each specimen (notched beam, or loaded to first crack)
- **Photograph the crack** — in a fiber beam, you see individual fibers bridging the crack and holding it closed
- **Visual confirmation** that fibers are doing their job

**Shrinkage crack test:**
- **Rectangular restrained slab** (long and narrow, held at both ends while curing)
- **Observe for cracks over 28 days**
- **Unreinforced slabs typically develop shrinkage cracks as they cure**
- **Fiber-reinforced slabs should develop fewer or no cracks**

**Fiber-finish quality:**
- **Subjective evaluation** — does the fiber concrete finish smoothly? Do fibers stick up at the surface? Are fibers visible in troweled slabs?
- **Affects:** aesthetic acceptability for polished concrete floors
- **Mitigation if needed:** top-dressing with an unreinforced topping; additional troweling; using only synthetic fibers in visible areas

**Documentation:**
- **Photo series** during loading (if possible) showing crack development and fiber bridging
- **Load-deflection curves** from the flexural tests
- **Impact counts** from impact tests
- **Shrinkage crack records** — photos, crack widths, timing

**Interpretation for design:**
- **If dual reinforcement (steel + synthetic)** performs notably better than steel alone in both strength and appearance, use the dual mix
- **If synthetic fibers alone** are sufficient and avoid the rust concerns of steel fibers at surfaces, consider them for visible slabs
- **If unreinforced is shown to be badly brittle in impact and shrinkage**, the fiber investment is clearly justified

---

## 12.5 DIY Hot Box — Measuring Insulation R-Value

**Plain language:** The advertised R-value of an insulation product is measured in a controlled lab. Real-world R-value depends on installation quality, compression, age, moisture, and how the insulation is assembled with other materials. A DIY hot box — inspired by the one University of Oregon architecture students have built for teaching — lets the owner measure the actual R-value of specific products and assembly configurations using tools that cost a few hundred dollars.

**Technical detail:** DIY hot box construction and protocol:

**Hot box concept:**
- **Heated chamber on one side** of the test wall (controlled warm temperature)
- **Cold chamber on the other side** (controlled cold, ideally outdoor in winter for large temperature difference)
- **Known heat input** to the hot side
- **Steady-state temperature measurements** on both sides of the test wall
- **R-value calculated** from heat flux and temperature difference

**Basic hot box build:**

**Hot chamber:**
- **Insulated box** 4 x 4 x 4 feet — exterior plywood with rigid foam insulation lining (R-40 minimum in the chamber walls so most heat goes through the test sample, not out the sides)
- **Resistance heater inside** — a small electric space heater, measurable wattage
- **Watt meter on the heater's power cord** — Kill-A-Watt or similar ($20-40)
- **Temperature probe inside chamber** — K-type thermocouple with data logger, or smart sensor with Home Assistant integration

**Test sample holder:**
- **Square frame** sized to hold a sample of wall/assembly — 2 x 2 feet for small samples, 4 x 4 feet for larger
- **Sealed at edges** with weatherstripping and tape — no air leakage around the sample
- **Removable** to swap samples

**Cold side:**
- **For winter outdoor testing:** the hot box sits outside, with the cold side exposed to outdoor air
- **For year-round testing:** the cold side is inside a second insulated chamber with a window air conditioner providing cooling
- **Temperature probe on cold side** — matched to hot-side probe

**Wall surface thermometry (the Matthias Wandel / Bo's Boring Blog method):**
- **Infrared thermometer** (non-contact, $30–$50) or thermal imaging camera
- **Measure:** hot surface temp (Th), cold surface temp (Tc), and ambient air temps on each side (Ta_hot, Ta_cold)
- **R-value formula (Bo's Boring Blog — woodgears.ca reference):**
  - **R = ((Th − Tc) / (Ta_hot − Th)) × 0.68 + 0.68**
  - **Derivation:** based on convective heat transfer coefficient of 0.68 for still indoor air
  - **Applies to:** small samples in calm conditions, after the system has reached steady state

**Test protocol:**

**Step 1 — Sample preparation:**
- **Cut sample** to fit the hot box opening
- **Install in the holder** with edge sealing
- **Acclimate** — let the sample reach room temperature (24 hours if previously stored elsewhere)

**Step 2 — Reach steady state:**
- **Turn on heater** set to maintain 100°F inside the hot chamber
- **Wait 4–8 hours** for temperatures to stabilize (check every hour until surface temps are changing less than 0.5°F per hour)

**Step 3 — Measurement:**
- **Record all temperatures** — Ta_hot, Th (hot surface of sample), Tc (cold surface of sample), Ta_cold
- **Record power input** — heater wattage integrated over the measurement period
- **Take multiple readings** — 5 measurements, 10 minutes apart, averaged

**Step 4 — Calculation:**
- **Simple method (Bo's formula):** R = ((Th − Tc) / (Ta_hot − Th)) × 0.68 + 0.68
- **Heat-flux method (more rigorous):** R = (Ta_hot − Ta_cold) / Q, where Q is heat flux in BTU/hr/sqft
- **Cross-check:** the two methods should agree within 20%

**Samples to test:**
- **Manufacturer A polyiso, 2 inch** — verify claimed R-13
- **Manufacturer B polyiso, 2 inch** — compare
- **XPS foam, 2 inch** — verify claimed R-10
- **EPS Type IX, 4 inch** — verify claimed R-16
- **Mineral wool, 3.5 inch** — verify claimed R-15
- **Assembly sample:** full wall section including CMU, air gap, foam, CMU — the REAL assembly R-value

**Accuracy expectations:**
- **DIY hot box vs. lab-grade ASTM C177 guarded hot plate:** within 10-15% typically
- **Sufficient for design decisions** — whether product A beats product B, whether assembly R is close to design
- **Not sufficient for published research** — but the owner-builder isn't publishing

**Reference:**
- **University of Oregon's Energy Studies in Buildings Laboratory** — published student hot-box projects as inspiration
- **Bo's Boring Blog** (associated with Matthias Wandel's woodgears.ca) — the IR thermometer method detailed
- **ASTM C177** — the full lab standard, useful to read for context

---

## 12.6 Thermal Bridging and Assembly Testing

**Plain language:** An insulation board has an R-value. A wall built from that insulation has a lower R-value because heat finds paths around the insulation — through studs, ties, fasteners. Thermal imaging reveals these bridges. A thermal camera (which the owner already has) is the single best tool for validating that the design's careful attention to thermal bridging (FRP wall ties instead of steel, continuous insulation layers) is actually working in the built assembly.

**Technical detail:** Thermal bridging testing:

**Tool:** infrared thermal camera (the owner has one — either standalone unit or smartphone-attachment like FLIR ONE, Seek, or similar)

**Test conditions:**
- **Large temperature difference indoor-to-outdoor** — at least 20°F, ideally 40°F
- **Steady-state conditions** — 6+ hours after last significant temperature change
- **No direct sunlight** on the surface being imaged (sun heats the surface locally, obscures thermal signal)
- **Best time:** evening in winter, with heat on inside; or early morning in summer, with AC on

**Test protocol:**

**Whole-wall imaging:**
- **Image the interior face of exterior walls** from corner to corner
- **Look for cooler regions** on the interior surface in winter (heat escaping = warmer on outside, cooler on inside)
- **Common bridges:**
  - **Window and door perimeters** — check flashing and foam seals
  - **Wall ties** — if using steel ties in masonry cavity, they show as vertical lines; with FRP ties, they should NOT show (validating the FRP choice)
  - **Rim joists** — where floor meets exterior wall
  - **Electrical boxes** — can be thermal bridges if not sealed
  - **Service layer penetrations** — any pipe or duct through the envelope
  - **Roof-to-wall junctions**
  - **Floor-to-foundation junctions**

**Documentation:**
- **Photograph every exterior wall** — thermal image + visible-light image of same location
- **Annotate thermal images** with temperature at notable points
- **Date and time** of imaging — thermal conditions matter for comparison

**Blower-door-assisted imaging:**
- **Run a blower door test** (see 12.7) putting the house under 50 Pa of depressurization
- **With outside air at a different temperature**, any leak location shows as a cool spot on interior walls (winter) or warm spot (summer)
- **Identifies air leaks** that thermal imaging alone might miss (a small gap might not transfer much heat conductively but leaks a lot of air when pressurized)

**Assembly-level R-value estimation:**
- **With a thermal camera and known indoor/outdoor temperatures, the surface-temperature method estimates effective R-value of the whole assembly**
- **R_effective = (T_indoor − T_outdoor) × 0.68 / (T_indoor − T_interior_surface)**
- **Compared to design calculations** — if actual R is much lower than designed, there's a bridging or installation issue to investigate

**Specific thermal bridging concerns to verify in this design:**
- **FRP ties in the masonry cavity** — should show NO thermal signature (proving the choice over steel)
- **Foundation-to-wall transition** — insulation should be continuous
- **Window frames** — triple-pane, thermally-broken frames should show even temperature distribution
- **Roof-to-wall parapet or eave** — common bridging location
- **Service layer electrical penetrations** through the envelope wall at the interconnect box — verify sealing

**When to image:**
- **After insulation installation, before drywall** — verify insulation is complete and even
- **After drywall and finish** — verify no ghost bridging showing through finish
- **First winter of occupancy** — verify design performance in actual use
- **Whenever moisture or cold spots are noticed** — diagnostic tool throughout the life of the house

---

## 12.7 Blower Door Testing

**Plain language:** A blower door is a big fan that temporarily mounts in a doorway, sealing the frame and blowing air out of the house. The fan creates a measurable pressure difference. The more air the fan has to move to maintain that pressure, the leakier the house is. This is the gold standard for quantifying how airtight the envelope actually is. Code requires a blower door test in Oregon; this design aims for performance far better than code.

**Technical detail:** Blower door testing:

**Equipment:**
- **Blower door kit** (Retrotec or The Energy Conservatory / Minneapolis Blower Door) — $2,500–$5,000 to own, $200–$500 per day to rent
- **Fan, pressure gauge, frame, cloth panel** — the kit
- **Laptop or phone app** for data logging

**Two common test methods:**

**Method A — Single-point test (ACH50):**
- **Depressurize the house to 50 Pa below outdoor**
- **Measure the airflow** needed to maintain this pressure
- **Divide by the house volume** to get Air Changes per Hour at 50 Pa (ACH50)
- **Simple, quick, good for verification**

**Method B — Multi-point test (more rigorous):**
- **Test at multiple pressures** (10, 25, 50, 75 Pa)
- **Fit the data to a power curve** — airflow = C × (pressure)^n
- **Reports:** airflow at 50 Pa, infiltration coefficient, leakage coefficient
- **Better for research or code compliance with detail**

**Performance targets:**
- **Code minimum (Oregon):** 3.0 ACH50 for new residential construction
- **This design target:** ≤ 1.0 ACH50 (well below code, approaching passive-house level)
- **Passive House certification target:** ≤ 0.6 ACH50
- **Conventional new home performance:** 4-7 ACH50
- **Older homes:** 10-20 ACH50

**Test protocol:**
- **Close all exterior doors and windows**
- **Open all interior doors**
- **Close all HVAC intake dampers and turn off combustion appliances**
- **Set up blower door in main entry**
- **Run the test**
- **Record the result**
- **With thermal camera running during the test**, leak locations are visible (see 12.6)

**When to test:**
- **During rough-in** (after air sealing but before drywall) — easy to access and fix leaks
- **After drywall** — check that drywall work didn't introduce leaks
- **Final test** — before occupancy, for compliance and record
- **Annually thereafter** — track envelope performance over time (envelopes typically get leakier as houses age)

**Common leak locations:**
- **Electrical box penetrations** (see Section 7's conduit strategy — reduces this issue significantly)
- **Plumbing penetrations** (see Section 6)
- **HVAC duct penetrations to outside** (see Section 8 — minimized by all-inside-envelope ducts)
- **Rim joist areas**
- **Window and door perimeters**
- **Attic access hatches (not applicable here — no attic)**
- **Chimney or vent penetrations** (minimal in all-electric design)

**Documentation:**
- **ACH50 result** at each test
- **Date, outdoor temp, wind conditions** during test
- **Leak locations** identified during the test (with thermal imaging)
- **Remediation record** — what was fixed, and follow-up test result

---

## 12.8 Radiant Floor Response Testing

**Plain language:** Radiant floors respond slowly compared to forced-air heating. The key performance questions are: how long does it take to raise a cold room to comfortable? How long does it take to cool down when heat is turned off? How well does each zone hold its setpoint when adjacent zones are at different temperatures? These are questions that can only be answered by running the system and measuring.

**Technical detail:** Radiant floor testing:

**Pre-commissioning tests** (from Section 8.14):

**Pressure test:**
- **Fill each radiant loop with water at 100 psi**
- **Hold for 24 hours**
- **No pressure loss** indicates no leaks
- **Failure:** repair joints, retest

**Flow test:**
- **With the system balanced and pumping,** measure flow in each zone (flow meters on manifolds)
- **Target:** design flow rate ±10%
- **Adjust** balancing valves as needed

**Post-commissioning tests:**

**Heat-up time test (per zone):**
- **Start with room at outdoor ambient temperature**
- **Set zone thermostat to 70°F** (or comfortable target)
- **Measure:** how long until room reaches 68°F, 69°F, 70°F
- **Target for a well-designed radiant system:** 2–4 hours to reach setpoint from a 10°F deficit at design outdoor temperature
- **Repeat for each zone**

**Cool-down time test (per zone):**
- **Start with room at 70°F**
- **Turn zone off**
- **Measure:** how long until room drops 1°F, 2°F, etc.
- **Target:** slow decay (many hours) — indicates good envelope and thermal mass working together

**Zone independence test:**
- **Set adjacent zones to very different setpoints** (e.g., 65°F and 75°F)
- **Measure:** do both zones reach and hold their respective setpoints?
- **If cross-talk is significant** (zone A pulls zone B), the wall between them needs better insulation or the control needs tuning

**Comfort survey:**
- **Subjective evaluation** at various times, in various weather
- **Questions:** are floors uniformly warm? Are there cold spots near windows? Is any room consistently less comfortable than others?
- **Data feeds back** into design tweaks (add a loop, increase flow, add window treatment)

**Energy use monitoring:**
- **Heat pump energy use** per day/week (see Section 10.9 energy monitoring)
- **Radiant loop pump energy** per day
- **Heat delivered** (from delta-T across supply and return × flow × specific heat) per day
- **COP calculation:** heat delivered / electrical energy input — should be 3.5 or better for a ground-source heat pump

**Seasonal tests:**
- **Shoulder season:** does the system handle the heating / cooling changeover smoothly?
- **Deep winter:** can the system maintain setpoint on the coldest day? What's the heat pump COP at low outdoor temperatures?
- **Deep summer:** does radiant cooling work without condensation? How much supplemental cooling is needed?
- **Extended power outage simulation:** how long does the house hold temperature without heat? (Thermal mass paying off.)

---

## 12.9 Water and Plumbing System Testing

**Plain language:** Water systems are tested for leaks before opening valves to the house, for pressure before taking them off the pressure test, and for flow rates to verify that the design delivers the promised performance (hot tub can be filled, multiple showers can run simultaneously, etc.). Continuing tests monitor water quality over time.

**Technical detail:** Water system testing:

**Pressure tests:**
- **Water supply system at 100 psi for 24 hours** — the standard pressure test
- **Test each section separately** before opening to the rest of the system
- **Every joint inspected** during the test for drips or sweating

**Flow rate tests:**
- **Kitchen sink alone:** measure gpm with a bucket and stopwatch
- **Primary bathroom shower:** measure gpm
- **Two showers simultaneous:** measure combined flow
- **Hot tub fill (if installed):** measure time to fill; verify matches design (see Section 6)
- **All faucets open simultaneously:** this is the design-basis peak — verify the house delivers

**Hot water delivery tests:**
- **Time from cold to hot at furthest fixture** — with recirculation loop, should be under 5 seconds
- **Temperature at fixture** — verify thermostatic mixing delivers design temp (120°F at fixtures, 140°F stored)
- **Sustained hot water** — run full flow for 15+ minutes; temperature should stay stable

**Water quality tests (baseline and ongoing):**
- **Well water test** at first use (baseline) — bacteria, pH, hardness, iron, manganese, arsenic, nitrates
- **Annual retest** recommended
- **Post-treatment test** — water AFTER softener, filter, UV — verify treatment is working
- **Tank sediment** — annual inspection of water heater and cistern for sediment buildup

**Leak detection:**
- **Nightly water meter reading** — any overnight consumption (when no fixtures in use) indicates a leak
- **Home Assistant integration** (see Section 10.9) — automatic alert on continuous flow
- **Visual inspection** — every accessible pipe, quarterly

**Backflow prevention:**
- **Test any backflow preventers** annually per manufacturer (outdoor hose bibs, irrigation, etc.)

---

## 12.10 Full-Scale Wall Mockup

**Plain language:** Before laying one block of the actual house, the owner-builder builds a 6-foot-tall, 4-foot-wide section of the complete wall assembly: foundation, inner CMU, cavity insulation, FRP ties, outer CMU, window opening, flashing details. This mockup is built in the backyard or a temporary location, stays in place during the main build, gets weather-exposed for a full year, and serves as a physical test of every detail of the design.

**Technical detail:** Wall mockup program:

**Mockup build:**
- **Small concrete pad** (4 x 4 feet, 6 inches thick) — serves as a mini-foundation
- **Complete wall section:** all layers (inner CMU, cavity with insulation and ties, outer CMU)
- **Include a window opening** — verify the window installation sequence
- **Include a utility penetration** — verify sealing works
- **Cap the top** with a small bond beam course — verify the top detail

**Time required:** 2–4 weekends to build

**What the mockup proves:**
- **Block laying technique** — the owner-builder practices the skill on a small scale
- **Insulation and tie installation** — verify the process works as designed
- **Window flashing** — test the detailing before committing to the main house
- **Air sealing details** — apply sealant, confirm material compatibility, look for issues
- **Visual appearance** — see the finished wall before the whole house commits to it
- **Moisture management** — observe over a year in rain/sun to verify drainage and drying

**Tests on the mockup:**

**Visual inspection over a year:**
- **After every rain** — any water entry? Any pooling? Any leakage to the inside face?
- **After freeze-thaw cycles** — any mortar cracking? Any block spalling?
- **After hot summer** — any delamination of insulation from surfaces?
- **After UV exposure** — any degradation of exterior finishes?

**Thermal performance test (with the DIY hot box concept scaled up):**
- **Build a heated chamber on the interior face of the mockup** — simulate winter
- **Measure surface temperatures** with thermal camera or IR thermometer
- **Calculate the assembly R-value**
- **Verify** matches design expectation (target R-40 for the full assembly)

**Air leakage test:**
- **Seal the edges of the mockup** as it would be in the main house
- **Small fan creating pressure difference**
- **Look for air leaks** with thermal imaging or smoke
- **Verify sealing details** work

**Destructive test at end (optional):**
- **After full evaluation,** break the mockup apart deliberately
- **Observe:** how did the insulation actually bond? How did the ties engage? Any unexpected water paths?
- **Document** — photos, notes, lessons learned

**Results inform the main build:**
- **Techniques refined** before committing
- **Material choices validated** (or changed)
- **Details adjusted** based on what was learned
- **Confidence built** in the overall design

**Cost of the mockup:**
- **Materials:** $500–$1,500
- **Time:** 2–4 weekends
- **Value:** potentially saves tens of thousands in the main build by catching issues early

---

## 12.11 Post-Occupancy Performance Monitoring

**Plain language:** Once the house is lived in, it becomes the ultimate test of the design. Energy use, comfort, any problems that emerge, and the evolution of every system over years — all get tracked and compared against design goals. This data is gold for the next build.

**Technical detail:** Ongoing monitoring:

**Energy use tracking (from Section 10.9):**
- **Monthly review** of total energy use
- **Annual comparison** to design targets (kWh per year per sqft for heating, cooling, water heating, all other)
- **Weather normalization** — compare to heating degree days and cooling degree days to isolate building performance from weather variation
- **Trend detection** — are any systems drifting toward inefficiency?

**Comfort tracking:**
- **Temperature and humidity logging** in every room, continuous
- **Subjective comfort notes** — how does each room feel in each season?
- **Guest feedback** — visitors often notice things residents have adapted to

**Water use tracking:**
- **Daily total consumption**
- **Leak detection** (continuous-flow anomalies)
- **Comparison to design expectation** — if using more than expected, why?

**Moisture and mold vigilance:**
- **Seasonal inspections** of high-risk areas — basement, bathrooms, kitchen
- **Humidity data from all rooms** — are any rooms consistently too humid?
- **Visible inspection for any mold growth** — early detection prevents spread

**System longevity tracking:**
- **Log every component replacement** — when did the well pump go? The water heater element? The ERV filter?
- **Compare to manufacturer expected lifespan**
- **Look for pattern** — does a specific system fail faster than others?

**Annual home report:**
- **Yearly review document** summarizing the past year of performance
- **Compared to previous years** — trends visible
- **Updated in the project binder** (see Section 11.17)
- **Used to refine** the design for future builds or adjustments to this one

---

## 12.12 The Knowledge Compound Effect

**Plain language:** Every test done, every measurement logged, every lesson learned makes the next home better. BSH Home #1 is both the home and the laboratory. BSH Home #2 benefits from every finding. By BSH Home #10, the program has decades of accumulated testing data, refined designs, and proven techniques.

**Technical detail:** Knowledge management across builds:

**Per-build documentation package (the "build dossier"):**
- **Design at final-permit stage** (plans, specs, calculations)
- **Test results from pre-construction** (concrete mixes, insulation, mockup)
- **Build photos and logs**
- **Inspection records**
- **Commissioning data** (HVAC, plumbing, electrical)
- **As-built drawings**
- **Post-occupancy performance data** (first 1, 3, 5 years)

**Cross-build reference library:**
- **Test data from every build** aggregated in a searchable database
- **Performance comparisons** — build #1 energy use vs. build #2
- **Design iterations** — what changed from build to build, and why
- **Problem reports and solutions** — if something failed in build #3, build #4 has the fix built in

**Knowledge shared externally:**
- **The BSH brand content** (see Section 13) — YouTube videos, blog posts, documentation — turns the private knowledge into public contribution
- **Open designs** — the philosophy and details are shareable (nothing proprietary in the sense of trade secrets; the value is in the work of implementing them well)

**The compound effect:**
- **Build #1: 100% learning** — every system is being done for the first time
- **Build #2: 40% learning + 60% refinement** — most systems are familiar, some are being improved
- **Build #5: 10% learning + 90% refinement** — the builds get faster, cheaper, and better
- **Build #10: the owner-builder is effectively a master of this specific building system** — quality and efficiency are optimized

**Personal development tracking:**
- **Skill log** — new techniques learned per build
- **Time-per-task tracking** — how long does each phase take? (Improves with practice)
- **Physical investment** — tools acquired, equipment mastered

---

*End of Section 12 — Testing and Development Program*
