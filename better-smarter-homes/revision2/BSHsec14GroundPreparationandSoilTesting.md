# Section 14 — Ground Preparation and Soil Testing

*The chapter under everything else — get this wrong and the rest doesn't matter*

This section covers what happens between picking the site and pouring concrete: understanding the dirt the building will sit on, testing it to know what you're dealing with, deciding whether the site can support the design you want, preparing the ground to accept the foundation, and dealing with soil problems when they appear.

The guiding philosophy: **the foundation rests on the soil, and the soil is the foundation of the foundation**; **a building lasts as long as its weakest layer**; **measure first, then decide, then build**; **most foundation failures are soil failures**; **good ground costs nothing extra to build on, and bad ground can be the difference between a $200,000 build and a $400,000 build that still settles**.

This is arguably the most important section in this entire document. Every other chapter assumes the soil under the building is sound. This chapter tells you how to verify that and what to do if it isn't.

---

## 14.1 Why the Ground Matters More Than Anything Else

**Plain language:** A building is only as good as what it sits on. The strongest concrete in the world fails if it's resting on dirt that gives way, swells in winter, sinks under load, or floods every spring. Most "foundation problems" are actually soil problems — the foundation didn't fail; the ground under it did. So before any concrete gets poured, the dirt has to be understood, evaluated, and prepared. This is the most important step in the whole build.

**Technical detail:** Why ground prep is the first-among-equals decision:

- **Cracks in foundations** are almost always caused by differential settlement (one part of the foundation moves more than another), expansive soil heaving, or frost action — all soil problems
- **Water in basements** is almost always caused by groundwater management failures — soil failing to drain, water table issues, or the wrong soil chosen for backfill
- **Doors and windows that won't close** in older houses signal foundation movement, which is signaling soil movement
- **Slabs that crack into multiple pieces** mean the soil under the slab moved differentially
- **Houses that lean** mean a portion of the foundation found softer ground than another portion

**The cost of getting it wrong:**
- A $5,000 site investigation that reveals expansive clay can save $50,000 in remedial work later
- A $15,000 soil improvement program before construction can prevent $200,000 in foundation repair after construction
- An undiagnosed soft spot under one corner of the building can cost the entire structure decades of life

**The cost of getting it right:**
- Most well-sited Oregon homes need only basic site preparation (a few thousand dollars in earthwork)
- Even challenging sites are usually buildable with proper preparation (a few tens of thousands more)
- Truly bad sites should be avoided in selection, not "fixed" during construction

**This section's promise:** By the end of this chapter, you will:
1. Know how to evaluate a site's soil before purchasing
2. Know how to verify it during the design phase
3. Know how to prepare the ground correctly for both basement and slab-on-grade construction
4. Know how to recognize and respond to soil problems
5. Know when to call a geotechnical engineer (and when not to)
6. Have actual practical skill with at least one field tool — the Dynamic Cone Penetrometer

---

## 14.2 What We're Actually Testing For — Core Concepts

**Plain language:** Before getting into tools and tests, we need to be clear about what questions we're trying to answer. The soil has to do five jobs: support the weight of the house, not move when wet or cold, drain water away, hold the sides of the excavation up while we build, and resist earthquakes without liquefying. Each of these is a different question with a different answer, and each needs a different test.

**Technical detail:** The questions soil must answer:

### Question 1 — Bearing Capacity

**What it means:** How much weight per square foot can the soil support without failing or settling more than allowable amounts?

**Units:** Pounds per square foot (psf) — the pressure the foundation puts on the soil.

**Typical residential foundation pressure:** 1,500–3,000 psf for a stick-frame house; 2,500–5,000 psf for a masonry/concrete home like this design (heavier).

**What we want:** Soil bearing capacity at least 2× the design load. So if the foundation puts 3,000 psf on the soil, we want soil that can carry at least 6,000 psf without trouble.

**Where it matters most:** Under foundation footings, under wall corners (highest concentrated loads), under any column or post.

### Question 2 — Settlement

**What it means:** How much will the soil compress over time under the load? Even soils that don't fail will compress somewhat. The question is whether it's a uniform 1/4 inch (acceptable) or a differential 4 inches across the building (catastrophic).

**Two kinds of settlement:**
- **Immediate settlement** — happens during/just after construction as soil compresses elastically
- **Consolidation settlement** — happens slowly over years/decades as water squeezes out of clay layers

**What we want:**
- Total settlement under 1 inch
- Differential settlement under 1/2 inch across the foundation
- All settlement complete within a few years of construction

### Question 3 — Stability and Side Slope Behavior

**What it means:** Can we dig a hole in this soil and have the walls stay up while we work? Does the soil hold its shape, or does it slump and collapse?

**Soil categories:**
- **Cohesive soils** (clays, silty clays) hold vertical walls for short periods — great for excavation
- **Granular soils** (sands, gravels) need to be sloped or shored — more excavation work
- **Loose granular** soils may need shoring even at modest depths

**What we want:** Excavation walls that hold long enough to do the foundation work, with reasonable safety. Or a clear plan for shoring/sloping if they won't.

### Question 4 — Drainage and Water Management

**What it means:** Where does water go in this soil? How fast? Does it accumulate? How high is the water table?

**Soil drainage categories:**
- **Free-draining** (gravel, coarse sand) — water moves through easily
- **Moderately draining** (loam, fine sand) — water moves but slowly
- **Poorly draining** (clay, silty clay) — water moves very slowly or not at all
- **Saturated zones** — soils permanently below the water table

**What we want:** Soil that either drains well or has a designed drainage system to handle its slow drainage. Water table well below the lowest point of the building (basement floor or slab).

### Question 5 — Expansion and Contraction

**What it means:** Does the soil change volume with moisture or temperature? Some clays swell up to 30% when wet, and they push hard enough to lift houses. Frost can heave saturated silt by a foot. We need to know what the soil does over the full annual cycle.

**Volume-changing soils:**
- **Expansive clays** (montmorillonite, smectite) — swell with water, shrink when dry
- **Collapsible soils** (some loess, some volcanic ash) — small amount of natural moisture, then collapse when wetted
- **Frost-susceptible soils** (silty soils with water available) — heave when freezing
- **Organic soils** — decompose, lose volume permanently

**What we want:** Soil whose volume stays stable through the seasons, OR active mitigation if the soil isn't stable.

### Question 6 — Seismic Behavior

**What it means:** What happens to this soil during an earthquake? Some saturated loose sands "liquefy" — they temporarily lose all bearing capacity and the building can sink, tilt, or even sink. Oregon has significant seismic risk from the Cascadia subduction zone.

**Seismic soil categories (per ASCE 7):**
- **Site Class A** — hard rock (best)
- **Site Class B** — rock
- **Site Class C** — very dense soil/soft rock
- **Site Class D** — stiff soil (most Oregon sites)
- **Site Class E** — soft clay (worst common)
- **Site Class F** — special soils (liquefiable, very organic, etc.)

**What we want:** Site Class C or D, no liquefaction concern. Or active mitigation if it's worse.

### Question 7 — Frost Susceptibility

**What it means:** When the soil freezes in winter, does it heave upward as ice lenses form? Does it freeze deep enough to affect the foundation?

**Frost depth in Oregon:**
- Coastal: 6–12 inches
- Willamette Valley: 12–18 inches
- Cascade slopes: 24–36 inches
- Central/Eastern Oregon: 24–48 inches
- High Cascades: 60+ inches

**What we want:** Foundations bear below frost depth. Soil under the slab is either non-frost-susceptible (gravel, clean sand) or kept dry enough (drainage) to not heave.

### How These Questions Combine

A site evaluation answers all seven questions. The tools and tests in this section are the means; the answers are the goal. A "good site" gets satisfactory answers to all seven. A "challenging site" has one or two issues that need engineering attention. A "bad site" has multiple problems and is best avoided.

---

## 14.3 Soil Types and How to Identify Them

**Plain language:** Different soils behave very differently. You can identify most soils by looking, feeling, and doing simple tests in the field. This is not soil science at the PhD level — it's enough to know whether you're dealing with sand, clay, silt, or something in between, and to predict roughly how the soil will perform.

**Technical detail:** The basic soil types and field identification:

### Soil Particle Size Categories (USCS — Unified Soil Classification System)

| Soil Type | Particle Size | Visible? |
|---|---|---|
| Boulders | > 12 inches | Obviously |
| Cobbles | 3–12 inches | Obviously |
| Gravel — Coarse | 3/4 – 3 inches | Easily |
| Gravel — Fine | #4 sieve – 3/4 inches | Easily |
| Sand — Coarse | #10 – #4 sieve (2–4.75 mm) | Just visible |
| Sand — Medium | #40 – #10 (0.4–2 mm) | Just visible |
| Sand — Fine | #200 – #40 (0.075–0.4 mm) | Barely visible |
| Silt | 0.002–0.075 mm | Not individually |
| Clay | < 0.002 mm | Microscope only |

**Most natural soils are mixtures.** A "sandy clay" is mostly clay with some sand. A "clayey gravel" is mostly gravel with some clay binding it. Field identification is about determining the dominant fraction and the secondary fractions.

### The Major Soil Categories for Building Purposes

**Gravel (G):**
- Coarse particles 1/4" or larger
- Drains well
- High bearing capacity when compacted
- Excellent for engineered fill
- Doesn't hold shape (caves easily in excavation)
- Common as river deposits, glacial outwash, weathered rock

**Sand (S):**
- Particles small enough to feel granular but you can see individual grains
- Drains well (especially clean sand)
- Good bearing capacity when compacted/dense
- Loose sand may need compaction
- Doesn't hold shape in excavation
- Common as beach deposits, river bars, dune deposits

**Silt (M for "mo," European notation):**
- Particles too fine to see individually but feel slightly gritty
- Drains slowly
- Moderate bearing capacity
- Frost-susceptible (the worst, actually) — silt with water freezes into ice lenses
- Often holds vertical walls in excavation but can collapse when saturated
- Common as wind-blown deposits (loess), lake deposits, slack-water flood deposits

**Clay (C):**
- Particles invisible without microscope
- Very poor drainage
- Variable bearing capacity (depends on consistency)
- Some clays expand and contract with moisture (the big problem)
- Holds shape in excavation
- Common as weathered bedrock product, lake deposits, marine sediments

**Organic soils (O):**
- Contains decomposed plant material
- Brown/black color, often with visible roots or peat
- Poor bearing capacity
- Continues to settle as organics decompose (decades)
- NOT a buildable soil — must be removed and replaced
- Common in wetlands, forest floors, old marshes

### Field Identification Tests (Owner-Builder Friendly)

**The Visual Test:**
- Look at color, particle size, layering
- Photograph and document
- Note any organic material (roots, leaves, dark color)

**The Dry Strength Test:**
- Take a small amount of dry soil
- Try to crush a pea-sized lump between fingers
- Crumbles easily = silty sand or sandy silt
- Resistance to crushing = increasing clay content
- Hard, can't be crushed = high-clay soil (and probably the kind that swells)

**The Ribbon Test (the most useful for clay identification):**
- Take a moist (not wet) sample, knead into a uniform consistency
- Roll between palms into a thread about 1/8 inch (3 mm) thick
- If the thread can't form at all = sand or silty sand
- If the thread breaks immediately = silt or low-plasticity clay
- If the thread can be rolled into a 3-inch ribbon and held flat without breaking = high-plasticity clay
- The longer the ribbon, the higher the clay content and (often) the worse the expansive behavior

**The Jar Test (sedimentation, for soil composition):**
- Fill a tall clear jar 1/3 full with soil
- Fill rest with water and a teaspoon of dish soap
- Shake vigorously for 1 minute
- Let settle for 24 hours
- After settling: gravel and sand at bottom (settle in seconds to minutes), silt above (settles in hours), clay above silt (settles over many hours), organic floats on top
- Measure the layers — gives a rough percentage of each soil type

**The Shake Test (for silt vs. clay):**
- Take a small ball of moist soil
- Shake it back and forth in your palm
- Silt: water comes to surface (shiny), then disappears when squeezed
- Clay: no surface water reaction
- Useful for quickly distinguishing silt and clay when they look similar

**The Smell Test:**
- Organic soils smell like compost or dirt
- Mineral soils smell like rock or are nearly odorless
- Sour or sulfurous smell = decomposing organic material, often saturated

**The Wet/Dry Cycle Observation (over a year):**
- Mark the soil surface near the proposed building site
- Photograph regularly through wet and dry seasons
- Look for cracking patterns when dry (high-shrinkage clay)
- Look for ponding patterns when wet (low drainage)
- Look for vegetation patterns (different plants = different soil moisture conditions)

### Putting It Together — The Site Soil Profile

Most building sites have soil layers, not uniform soil. A typical Oregon site might have:
- 0–6 inches: Topsoil (organic-rich, dark)
- 6–24 inches: Weathered subsoil (lighter color, different texture)
- 24–60 inches: Parent material (the original soil before weathering)
- Below 60 inches: Bedrock or older sediments

**The soil at building level is almost always NOT the topsoil.** Topsoil is removed before any structural work. The soil you build on is the subsoil and parent material — what's revealed after stripping the top.

Document the profile as you investigate:
```
Site: __________________________ Date: _______________
Location of test: _______________

Layer 1: Depth ___ to ___ inches
   Color: _________________
   Texture: _________________
   Consistency: _________________
   Organic content: _________________
   Notes: _______________________________________________

Layer 2: Depth ___ to ___ inches
   Color: _________________
   Texture: _________________
   Consistency: _________________
   Organic content: _________________
   Notes: _______________________________________________

[continue for each layer encountered]
```

---

## 14.4 The Dynamic Cone Penetrometer (DCP) — Complete Guide

**Plain language:** The DCP is a steel rod with a pointed tip on the bottom and a sliding hammer on top. You drop the hammer, the rod gets driven into the ground, and you measure how far it goes per drop. The number of drops to push the rod down a fixed distance tells you how dense and strong the soil is. It's the closest thing an owner-builder has to a real geotechnical test, and it's affordable, portable, and accurate enough for many residential decisions.

This subsection is the most detailed in this entire chapter because DCP testing is the single most useful skill an owner-builder can learn for ground evaluation. Read it all the way through. The investment of an hour reading and a few hundred dollars in equipment will inform decisions worth tens or hundreds of thousands of dollars over the life of the build.

### 14.4.1 What the DCP Is — Anatomy of the Tool

**The components:**

A standard DCP (per ASTM D6951) has these parts:

1. **Cone tip** — a hardened steel cone, typically 60° apex angle, about 20mm (3/4 inch) base diameter. This is what penetrates the soil. Replaceable; wears over time.

2. **Drive rod** — a steel rod, typically 16mm (5/8 inch) diameter, marked in millimeters or inches along its length. The rod connects the cone to the anvil. May be one piece or sectioned (assemble with threaded couplers).

3. **Anvil** — a heavy threaded fitting at the top of the rod where the hammer impacts. Transmits the hammer's energy to the rod.

4. **Hammer (drop weight)** — a steel sleeve that slides on a rod above the anvil. Standard mass is 8 kg (17.6 lb) for the small DCP, or 17.6 lb (8 kg) for the heavy DCP — yes, both standards exist; verify which you have. Lifted by hand and dropped under gravity.

5. **Drop guide rod** — a smaller rod above the anvil that the hammer slides on. The drop guide has a stop collar at a fixed height (575mm / 22.6 inches for standard DCP) so the hammer always drops the same distance.

6. **Handle** — a horizontal grip at the very top of the drop guide rod. The operator grasps this to hold the assembly plumb.

**The principle:**

Same hammer, same drop height, same drop distance = same impact energy every time. The ONLY variable is how soft or hard the soil is. Soft soil = many millimeters of penetration per blow. Hard soil = few millimeters per blow.

Very simple, very repeatable, very useful.

**Where to buy:**

- **Kessler DCP** — the U.S. industry standard, ~$1,500–$2,500
- **PILECO** — alternative, similar price
- **Vertek Standard DCP** — alternative
- **Imported / generic DCPs** — $400–$800 (verify they match ASTM D6951 specs)
- **Rental** — many geotechnical labs and equipment rental yards have them; ~$100–$200/day

**For owner-builder use, an imported generic at $400–$600 is fine.** The science is in the procedure and the data analysis, not in the brand.

### 14.4.2 The Science Behind the Numbers

**Plain language:** Every blow drives the cone a certain distance. We count blows per inch (or per 100mm) and use that number to predict bearing capacity, soil strength, and other properties. The conversions are well-established and published in industry standards.

**Technical detail:** The math:

**Step 1 — Penetration Index (PI)**

The most basic measurement: **PI = millimeters of penetration per blow**

Examples:
- PI = 10 mm/blow → 10mm down per blow → roughly medium-dense soil
- PI = 50 mm/blow → 50mm down per blow → loose or very soft soil
- PI = 2 mm/blow → barely moves → very dense, possibly bedrock

**Step 2 — California Bearing Ratio (CBR)**

CBR is a standard measure of soil strength used worldwide. The DCP-to-CBR relationship is empirical (based on thousands of comparisons between DCP and laboratory CBR tests) and well-established:

```
log10(CBR) = 2.465 - 1.12 × log10(PI)
```

Or solved for CBR:
```
CBR = 292 / PI^1.12
```

Where:
- CBR is the California Bearing Ratio (percentage)
- PI is the DCP penetration index in mm/blow

Example calculations:

| PI (mm/blow) | CBR (%) | Soil Quality |
|---|---|---|
| 2 | 100+ | Very dense (bedrock-like) |
| 5 | 45 | Dense gravel, well-compacted |
| 10 | 21 | Good, dense soil |
| 20 | 10 | Medium-dense soil |
| 30 | 6 | Marginal residential soil |
| 50 | 4 | Soft, needs improvement |
| 80 | 2 | Very soft, unsuitable |
| 150 | 1 | Very poor, unsuitable |

**Step 3 — Bearing Capacity from CBR**

The relationship between CBR and bearing capacity is less direct. CBR was developed for road design (pavement support) and translates imperfectly to building foundations. However, useful rough correlations exist:

For shallow foundations on cohesionless soils (sand, gravel, sandy soils):
```
qa (allowable bearing pressure, psf) ≈ 30 × CBR + 250
```

For shallow foundations on cohesive soils (clays, silty clays):
```
qa (allowable bearing pressure, psf) ≈ 25 × CBR + 200
```

These give a **ballpark** figure. They are NOT a substitute for engineered geotechnical analysis on critical projects. But for an owner-builder verifying a site, they're a valuable sanity check.

Worked example:

Suppose your DCP test shows PI = 15 mm/blow consistently from 2 to 6 feet below grade. What does that mean?

- CBR = 292 / 15^1.12 = 292 / 19.3 = ~15%
- Estimated allowable bearing (cohesionless): 30 × 15 + 250 = 700 psf

That's marginal for a heavy masonry home (which puts 2,500–5,000 psf on the foundation). You'd need a wider foundation footing to spread the load, OR soil improvement, OR a different site.

If the same site shows PI = 5 mm/blow:
- CBR = 292 / 5^1.12 = 292 / 5.85 = ~50%
- Estimated allowable bearing: 30 × 50 + 250 = 1,750 psf

Better. Still marginal for heavy construction without a wide footing, but workable.

PI = 2 mm/blow:
- CBR = 292 / 2^1.12 = 292 / 2.17 = ~135%
- Estimated allowable bearing: 30 × 135 + 250 = 4,300 psf

Excellent — supports any residential foundation easily.

**Step 4 — Cumulative Plot (Depth vs. Blows)**

A single PI number isn't the whole picture. You want a profile showing how soil density changes with depth. Plot:

- X-axis: cumulative number of blows
- Y-axis: depth (with zero at top)

The slope of this curve at any depth tells you the soil strength at that depth:
- **Steep slope** (many mm gained per blow) = soft layer
- **Shallow slope** (few mm per blow) = dense layer
- **Vertical line** (no penetration despite many blows) = refusal — bedrock, hardpan, or buried obstacle

This profile is the most useful single output of DCP testing. It shows you exactly where any soft or hard layers are.

### 14.4.3 How to Use the DCP — Step by Step

**Plain language:** This is the complete procedure, written so a careful first-timer can do it right. Every step matters. Don't skip any.

**Step 1 — Site preparation:**

```
[ ] Identify your test location(s)
    — At least 3 tests within the planned building footprint
    — Plus one test outside the footprint as a baseline
    — Plus one test at any visibly different soil (color change, vegetation change, etc.)

[ ] Strip surface vegetation and topsoil
    — Remove sod, leaves, roots
    — Topsoil tells you nothing useful about bearing
    — Dig a small "starter hole" 4-8 inches deep with a shovel
    — Reach the actual subsoil before testing

[ ] Verify the spot is approximately level
    — Significant slope makes the rod want to go in at an angle
    — If the natural ground slopes, level a small platform with the shovel

[ ] Check that the spot is dry-ish
    — Standing water or saturated mud invalidates the test
    — Wait a few days after heavy rain before testing
    — Or test multiple times across different weather

[ ] Mark the spot with a flag or stake
    — You'll want to find this exact location later
    — GPS coordinates if you have a way to record them

[ ] Have your data sheet ready and a pen
    — A clipboard helps; a smartphone app also works
    — Sample data sheet is in Appendix F

[ ] Optional but recommended: a small bubble level
    — To verify the rod is plumb during testing

[ ] Optional: marker or chalk to mark the rod every 100mm
    — Saves measurement time during testing
```

**Step 2 — Setup:**

```
[ ] Assemble the DCP per manufacturer instructions
    — Cone tip threads onto the drive rod
    — Anvil on top of drive rod
    — Drop guide rod threads into anvil
    — Hammer slides over drop guide rod
    — Handle on top of drop guide rod

[ ] Verify the tip is sharp and undamaged
    — Replace if mushroomed or worn

[ ] Verify the rod is straight
    — Bent rod gives bad data and is hard to push down

[ ] Verify the hammer slides freely
    — No sticking or binding
    — If sticky, clean and lubricate per manufacturer

[ ] Position the cone tip on the test surface
    — Don't push the tip into the ground first; it should sit ON the surface for the first hit
    — Hold the rod plumb (vertical) — if you're not sure, use a small bubble level on the rod
```

**Step 3 — The seating drops:**

```
[ ] Position one person to operate the hammer
    — Standing to the side of the rod
    — Hand on the hammer, pulled up to the stop
    — Drop is GRAVITY ONLY — let go, don't push down

[ ] Position another person to hold the rod plumb
    — Both hands on the rod near the bottom
    — KEEP THE ROD VERTICAL throughout
    — Watch for any tendency to drift sideways

[ ] Operator: lift hammer to stop, release, let it fall
    — One drop = one blow
    — DO NOT push down on the hammer to "help" it
    — DO NOT release before reaching the stop

[ ] First few blows are "seating blows"
    — These get the cone fully into undisturbed soil
    — Typical convention: first 6 inches of penetration counts as seating, doesn't count toward data
    — Some operators use 100mm as the seating distance
    — Document the seating depth ("seated to 100mm in 4 blows")
```

**Step 4 — The actual test:**

```
[ ] After seating, begin recording
    — Operator delivers consecutive blows
    — Spotter records depth after each blow OR every group of blows
    — If recording per-blow, the data is finest but slower
    — If recording per 100mm or per inch, the data is coarser but faster

[ ] Common recording approach: blows per 100mm
    — Operator counts blows as they're delivered
    — When the rod has moved 100mm, spotter records the blow count and depth
    — Example: "0-100mm: 4 blows. 100-200mm: 6 blows. 200-300mm: 8 blows..."

[ ] Continue testing to design depth or refusal
    — Design depth: typically 4-6 feet below planned foundation level
    — Refusal: 50+ blows in a single 100mm interval = stop
    — Trying to push past refusal damages the equipment

[ ] If the rod won't penetrate at all early
    — Stop immediately
    — You've hit a rock, root, or hardpan
    — Move the test 2-3 feet sideways and try again
    — Or if hard layer is consistent across multiple tests, that's your hard layer

[ ] If the rod sinks 200+mm in one blow
    — You've hit a void or extremely soft layer
    — Document this and dig a test pit to investigate visually
```

**Step 5 — Sampling:**

```
[ ] As the rod is being withdrawn, look at what's coming up
    — Soil clinging to the rod tells you what you tested through
    — Note color changes at different depths
    — If possible, save samples in labeled bags for further field testing

[ ] If you used a hand auger before the DCP, you should have a soil profile already
    — DCP confirms the strength; auger samples confirm what kind of soil it is

[ ] After test: rod withdraws by hand pulling
    — Or use a "puller" tool — a clamp with a slide hammer that's the reverse of the drive hammer
    — A slide hammer puller with built-in jack is helpful for deep tests

[ ] Photograph the test hole, the rod, and the surrounding ground
    — Archive these with the test data
```

**Step 6 — Repeat:**

```
[ ] Move to next test location
    — Minimum 3 tests within building footprint
    — Plus tests in problem zones if any
    — Plus baseline test outside footprint

[ ] Tests should be within similar soil context
    — If you find drastically different results between tests, dig more tests in between
    — A site with one good test and one bad test isn't a "good site" — it's a site you don't yet understand

[ ] Maintain the data records carefully
    — Date, time, weather, location coordinates, who tested, what equipment
    — See Appendix F for the standard form
```

### 14.4.4 Mistakes to Avoid — The Pitfalls

The DCP is simple, but there are many ways to get bad data without realizing it. Avoid these:

**MISTAKE: Testing through topsoil.**
- Topsoil is loose, organic, and not what your foundation will sit on
- Strip topsoil first; DCP starts in the subsoil

**MISTAKE: Pushing on the hammer.**
- The science depends on free-fall energy
- Pushing down adds unmeasured force
- Result: artificially low blow counts (soil looks better than it is)

**MISTAKE: Lifting hammer past the stop.**
- The standard drop height is 575mm (22.6 inches) — fixed by the stop
- If you lift higher, you're delivering more energy than calibrated
- Result: artificially low blow counts

**MISTAKE: Letting hammer fall short.**
- Releasing before the stop means partial-energy blows
- Result: artificially high blow counts

**MISTAKE: Rod not plumb.**
- A tilted rod adds friction and gives bad readings
- A really tilted rod can bend
- Use a bubble level or have a partner check vertical alignment

**MISTAKE: Hammer not sliding freely.**
- Friction between hammer and guide rod absorbs energy
- Clean and lubricate the guide rod; replace worn parts
- If hammer "sticks" partway down, that drop didn't count

**MISTAKE: Testing in saturated soil.**
- Water lubricates particles, soil reads as much weaker than it really is
- Wait for the soil to drain after rain
- Or test multiple times across seasons to see the range

**MISTAKE: Testing through frozen ground.**
- Frozen soil reads as solid bedrock
- Useless data
- Wait for thaw, or test below frost line

**MISTAKE: Trusting one test.**
- Soil varies dramatically across small distances
- A single test could hit a buried rock (false high reading) or a buried organic pocket (false low reading)
- Always do at least 3 tests across the building footprint

**MISTAKE: Continuing past refusal.**
- 50+ blows in 100mm = stop
- The cone is bouncing on rock or hardpan
- You're not learning anything new and you risk damaging the equipment

**MISTAKE: Not documenting.**
- A test you didn't write down is a test you didn't do
- Date, location, weather, depth, blow counts, samples observed
- Photos and notes
- See Appendix F

**MISTAKE: Confusing units.**
- Some data is in blows per 100mm
- Some is in blows per inch (slightly different)
- Some is in mm per blow (the inverse of blows per 100mm × some factor)
- Be consistent and clear in your records

**MISTAKE: Skipping safety.**
- Eye protection — the hammer can launch dirt and rust
- Gloves — the rod gets banged repeatedly and can pinch
- Sturdy shoes — dropping the hammer assembly on your foot is a real risk
- Don't test alone if you can avoid it — operator + recorder is the proper crew

### 14.4.5 Reading the Data — Patterns to Look For

After collecting data from one or more tests, you have a list of cumulative depths and blow counts. Now interpret it.

**Plot the data:**

Always plot the data graphically — depth on Y-axis (zero at top, increasing downward), cumulative blows on X-axis. The shape of this curve tells the story.

**Pattern 1 — The "Good Site" Profile:**

Steady, fairly steep curve. About the same number of blows per unit depth all the way down. Density consistent or increasing slightly with depth.

```
0   ┤├──────
    ┤  ╲
    ┤   ╲
    ┤    ╲
2'  ┤     ╲
    ┤      ╲
    ┤       ╲
4'  ┤        ╲
    ┤         ╲
    └─────────────────
        Cumulative blows
```

Interpretation: Uniform soil, increasing density with depth (good). Suitable for typical residential foundation.

**Pattern 2 — The "Soft Layer" Profile:**

A "step" in the curve where the rod suddenly moves much faster.

```
0   ┤├──
    ┤  ╲
    ┤   ╲
    ┤    ╲    ← good soil to here
2'  ┤     ───────── ← soft layer
    ┤              ╲
    ┤               ╲
4'  ┤                ╲
    ┤                 ╲   ← good soil resumes
    └─────────────────
```

Interpretation: There's a soft layer at ~2 feet. Decision: either remove and replace this layer, or design a foundation that extends below it (deep footings, piers).

**Pattern 3 — The "Improving" Profile:**

Loose at the surface, denser with depth.

```
0   ┤├────
    ┤   ╲      ← loose surface
    ┤    ╲
    ┤     ╲
2'  ┤      ╲
    ┤       ╲       ← getting denser
    ┤        ╲
4'  ┤         ╲
    ┤          ╲    ← good bearing soil
    └──────────────
```

Interpretation: Common pattern. Top 1-2 feet may need stripping or compaction. Below that, good native soil. Most Oregon valley sites look like this.

**Pattern 4 — The "Refusal" Profile:**

Curve hits a wall and stops penetrating.

```
0   ┤├──
    ┤  ╲
    ┤   ╲
    ┤    ╲
2'  ┤     ╲
    ┤      ╲
    ┤       ╲
3'  ┤        ╲
    ┤         |  ← refusal — bedrock or hardpan
    ┤         |
    └─────────|─────
              ↑
              Vertical line: many blows, no penetration
```

Interpretation: Solid layer reached. Could be bedrock (great), hardpan (good), or a single boulder (problematic — try another test). Verify with a test pit if you can.

**Pattern 5 — The "Variable" Profile:**

Multiple soft and dense layers alternating.

```
0   ┤├─
    ┤  ╲
    ┤   ╲     ← dense
    ┤    ╲
1'  ┤     ───── ← soft
    ┤          ╲
    ┤           ╲   ← dense
2'  ┤            ╲
    ┤             ──── ← soft again
    ┤                 ╲
3'  ┤                  ╲
    └────────────────────
```

Interpretation: Layered soil. Likely sediments deposited in different conditions. May need engineering attention to determine which layer to bear on.

**Pattern 6 — The "Bad Site" Profile:**

Steep slope all the way down — soft soil throughout.

```
0   ┤├
    ┤ ╲
    ┤  ╲
    ┤   ╲
2'  ┤    ╲
    ┤     ╲
    ┤      ╲
4'  ┤       ╲   ← still soft
    ┤        ╲
    ┤         ╲
6'  ┤          ╲
    └──────────────
```

Interpretation: This is a bad site. Soft soil to 6+ feet means deep foundations, soil improvement, or finding a different site.

### 14.4.6 Comparing DCP to Professional Tests

The DCP is excellent but has limits. Here's how it compares to professional alternatives:

| Test | What It Measures | Cost | Depth | Typical Use |
|---|---|---|---|---|
| DCP | Penetration resistance | $400-$1500 to own | 1-2 m typical | Residential pre-construction, verification |
| Hand auger | Soil sampling | $100-$300 | 6 m possible | Soil identification, log preparation |
| SPT (Standard Penetration Test) | Blows for fixed sampler driven by 140 lb hammer falling 30" | $150-300 per location, hire driller | Any depth | Major construction, geotechnical investigation |
| CPT (Cone Penetrometer Test) | Continuous resistance log | $1000+ per location | 30+ m | Large commercial, specialty |
| Plate load test | Direct bearing measurement | $500-2000 per test | Surface | Verification of pad bearing |
| Lab CBR test | Soil strength on remolded sample | $200-400 per sample | Lab | Definitive strength testing |

**The DCP is the right tool when:**
- You need quick, multiple, repeatable readings across a site
- You're verifying field conditions before pouring
- You're comparing locations
- The project is residential scale
- You want to understand layers/depth profile

**The DCP is NOT the right tool when:**
- You need certified geotechnical engineering output for permits or large projects
- Soil is gravelly (cone bounces off gravels, gives false-high readings)
- You need samples for lab testing (use auger or boring)
- You need to investigate below 2 meters

### 14.4.7 When to Hire a Geotechnical Engineer

For most owner-builder residential projects on visibly normal sites, DCP plus visual investigation is enough. But there are situations where you should hire a licensed geotechnical engineer for a formal site investigation:

- **Ambiguous DCP results** that don't tell a clear story
- **Sites with signs of past landslides** (curved tree trunks, hummocky ground, scarps)
- **Sites with high water table** (within 5 feet of the surface)
- **Sites with visible expansive soil** (wide cracks in dry soil)
- **Sites with organic layers** under the building footprint
- **Sites with unusual fill** (debris, old foundations, demolition material)
- **Sites where structural engineer's preliminary review flags concerns**
- **Sites near existing structures showing settlement** (you might be in the same problem area)
- **Sites with steep slopes** (slope stability is its own subject)

A geotechnical engineering investigation typically costs $3,000–$15,000 and includes:
- Site reconnaissance
- Borings (drilled holes with samples) at key locations
- Lab testing on samples
- Engineering analysis and report
- Foundation recommendations

Compared to building cost (often $200,000+), this is small money for major risk reduction. **When in doubt, hire it out.**

---

*End of Section 14 Part 1. Part 2 (other tools, basements, slabs, soil improvement, water tables, Oregon soils, clay) continues.*

## 14.5 Other Site Investigation Tools

**Plain language:** The DCP measures soil strength. But you also need to know what KIND of soil you have and what's lurking beneath the surface that the DCP can't tell you. A few other tools work alongside the DCP to give a complete picture.

### 14.5.1 Test Pits — The Most Underrated Tool

A test pit is a hole. You dig it with a shovel or, better, with the same mini-excavator you'll use for the foundation work. You climb in (carefully) or look in from the edge, and you SEE what the soil looks like at depth.

**Why test pits matter:**
- DCP gives numbers; test pits give understanding
- You see soil layers, color changes, root channels, water seepage
- You can sample at any depth
- You can see what the soil does in profile (does it crack? does it crumble? does it hold a vertical face?)
- You can identify problems the DCP won't reveal — buried roots, cobbles, organic pockets, old fill

**Test pit specifications:**

For evaluating a building site:
- **Depth:** Reach below the deepest planned foundation — for a basement build, that's 8-10 feet; for a slab build, 4-6 feet
- **Width:** Wide enough to safely look in (3-4 feet)
- **Length:** Long enough to see soil layering changes (4-8 feet)
- **Number:** Minimum 2-3 across the building footprint, more if site is variable

**Safety FIRST in test pits:**

```
[ ] DO NOT enter a pit deeper than 4 feet without shoring or sloping
[ ] DO slope the sides at 1:1 (45°) for unsupported pits
[ ] DO NOT have anyone in the pit while equipment is operating nearby
[ ] DO have a plan to get out — ladder, ramp, or cut steps
[ ] DO check for utilities before digging — call 811 (Oregon Utility Notification Center)
[ ] DO have a spotter if anyone is in the pit
[ ] DO consider water — pits can fill if you hit a perched water table
[ ] DO backfill promptly if you don't need the pit anymore
```

**OSHA 29 CFR 1926 Subpart P** addresses excavation safety. For owner-builder use, the practical takeaway: **never trust an unshored vertical excavation more than 4 feet deep**, especially in granular or saturated soils.

**What to look for in a test pit:**

```
[ ] Soil layers visible (record colors and depths)
[ ] Texture change with depth
[ ] Roots — if you see them deeper than 6 feet, this is unusual; investigate
[ ] Organic material (dark soil, plant matter, smell)
[ ] Water seepage — look at the walls; water entering means perched water or water table
[ ] Cracks in clay soils (indicates expansion potential)
[ ] Old fill or debris (broken concrete, brick, old pipes, demolition material)
[ ] Bedrock (hard refusal at depth)
[ ] Hardpan (a dense compressed layer, often near the bottom of the weathering zone)
[ ] Boulders (you'll need to plan for them)
[ ] Mottling (orange/red spots in clay = past saturation, indicates water table reaches that depth seasonally)
[ ] Smell (rotten egg = sulfur in saturated soils; earthy = normal)
```

**Test pit photography:**

- Photograph each side of the pit
- Place a tape measure in the pit for scale
- Mark soil layers with a knife or trowel before photographing
- Take a "profile" photo with you pointing out the layers
- Save photos with the date, location, and pit number

**The test pit is the field-trip version of geology class.** No lab is going to tell you what you can see by looking.

### 14.5.2 Hand Auger — Sampling Without Major Excavation

A hand auger is a short post-hole-digger-like tool with a screw or bucket head that pulls up a soil sample from the depth you turn it to.

**Types:**

- **Bucket auger** — cylindrical bucket on a rod, 2-4 inch diameter; turns down, pulls soil up
- **Spiral / screw auger** — more like a giant drill bit; for harder soils
- **Edelman auger** — Dutch design, very effective in clays
- **Open auger** — for sands and granular soils

**Why use one:**

- Sample at specific depths without digging a full pit
- Get clean samples for ribbon testing, jar testing, lab work
- Verify soil layering between test pit locations
- Reach depths a DCP rod can't reveal soil identity for

**How to use:**

```
[ ] Strip topsoil from test location
[ ] Lower auger straight into hole
[ ] Turn clockwise to advance (typically 4-6 inches per turn cycle)
[ ] Withdraw without rotating
[ ] Empty soil sample into a labeled bag with depth noted
[ ] Re-insert and continue to next depth
[ ] Continue to design depth or refusal
```

**For typical residential investigation:** 3-meter (10-foot) hand auger kits cost $300-600. They're harder than they look — turning a 3-meter rod through clay is genuine physical work.

### 14.5.3 The Hand Auger + DCP Combination

The two tools complement each other perfectly:

- **Hand auger** reveals what the soil IS at each depth
- **DCP** reveals how strong the soil is at each depth

Run them at adjacent test locations (2-3 feet apart) and you have:
- A complete profile of soil types from top to design depth
- A complete profile of soil strength
- The two together tell you whether the strength is adequate for the soil type

This combination at 3-5 test locations across a building footprint is essentially what a low-end geotechnical investigation provides — at maybe 5% of the professional cost.

### 14.5.4 Other Tools and Tests

**Compaction tester (for engineered fill):**

After you place fill and compact it, you need to know if compaction is adequate. The standard test is the **Standard Proctor** or **Modified Proctor** test, run in a lab from a soil sample. The result tells you the maximum density at optimum moisture for that soil. Field testing then verifies you achieved 95% (or whatever spec) of that maximum.

For owner-builder use, **simpler field tests** include:
- **Plate load test** — drop a 10-pound steel ball on the compacted surface; measure the bounce dimple
- **Penetrometer** (small handheld pocket penetrometer) — pushes a small rod into the surface and reads resistance
- **DCP on the compacted fill** — same DCP you used for site investigation, now used to verify your fill is dense

**Moisture meter:**

For checking the moisture content of soil at compaction time. Soils compact best at optimum moisture content (varies by soil; rule of thumb is "just damp enough to hold a ball when squeezed but break apart with light pressure").

**Sieves:**

A small sieve set (#4, #10, #40, #100, #200) lets you do basic gradation analysis on a sample. Run water and a sample through, see what sticks to each sieve, calculate percentages.

**The owner-builder soil tool kit:**

The complete starter kit for a serious owner-builder doing their own investigation:

```
[ ] Dynamic Cone Penetrometer (DCP) — $400-$1,500
[ ] 3-meter hand auger kit — $300-$600
[ ] Pocket penetrometer (for surface tests) — $50-$150
[ ] Soil moisture meter — $30-$100
[ ] Bubble level for verifying rod plumb — $20
[ ] Sieve set (5 standard sizes) — $100-$300
[ ] Plumb bob — $20
[ ] Tape measure (50 ft) — $30
[ ] Camera with date stamp — already have
[ ] Test pit shoring kit (or rent) — $300-$1,000
[ ] Quality shovels, trowels, scrapers — $100
[ ] Field notebook and pencils — $20
[ ] Sample bags (Ziploc-type, lots) — $20
[ ] Marker, masking tape — $20
[ ] Hand level (for grade work) — $50

Total starter kit: $2,000-$5,000
```

This kit is rentable from geotechnical and equipment rental yards if you don't want to own. Owning is sensible if you're planning multiple builds.

---

## 14.6 The Site Evaluation Procedure — Walkthrough

**Plain language:** Here's the complete procedure for evaluating a site, from first walkthrough to "decision to build" verification. Follow it in order. Skip nothing.

### Phase 1 — Pre-Purchase Drive-By

Before making an offer:

```
[ ] Visit the site at least twice — once dry weather, once wet weather if possible
[ ] Note the surrounding landscape — high points, low points, drainage patterns
[ ] Look for visible water (springs, ponds, wet areas, rushing creeks nearby)
[ ] Check vegetation patterns (different vegetation can indicate different soil moisture)
[ ] Look for cracking patterns in nearby soils (expansive clay clue)
[ ] Look at neighboring buildings — are they sound? Cracks? Settlement?
[ ] Talk to neighbors — what do they know about the soil here?
[ ] Note any standing water after rain
[ ] Note any natural drainage features (creeks, gullies, ditches)
[ ] Photograph everything
```

### Phase 2 — Owner Contingency Investigation (After Offer, Before Close)

During your due diligence period (typically 30-60 days):

```
[ ] Order a Phase I Environmental Site Assessment if any history of industrial use
[ ] Get a copy of any soil reports or geotechnical work done previously
[ ] Order a survey if not provided (legal boundaries, topography)
[ ] Check the FEMA flood map for the parcel
[ ] Check the Oregon DOGAMI landslide map (DOGAMI = Department of Geology and Mineral Industries)
[ ] Visit the county geologist or soils office for any local information
[ ] Check the Oregon Water Resources Department for nearby well logs (free online)
    - Well logs reveal water table depth, soil layers from drillers' notes
    - Look at logs from wells within 1/4 mile of the property
[ ] Walk the property with a shovel and a DCP if you can access it
    - Even a few test points before purchase can reveal showstoppers
```

### Phase 3 — Detailed Site Investigation (After Close, Before Design Finalization)

Once the property is yours:

```
[ ] Walk the proposed building location with a tape measure and stake out the footprint
[ ] Mark the four corners with stakes
[ ] Mark the proposed foundation perimeter with string
[ ] Within this footprint, plan 4-6 DCP test locations (corners and middle)
[ ] Plan 2-3 test pit locations
[ ] Plan hand auger sampling between DCP locations

[ ] FIRST: Strip topsoil from each test location
    - Small starter holes 4-8 inches deep with shovel
    - Stockpile topsoil for later landscape use

[ ] Run DCP tests at each location
    - Document carefully (use Appendix F template)
    - Photograph each test
    - Record GPS or surveyed coordinates

[ ] Hand auger sample at intermediate points
    - Pull samples at 6, 12, 24, 48 inch depths minimum
    - Bag and label each sample

[ ] Dig test pits
    - At least one within the footprint
    - One at the deepest planned foundation depth
    - Visually log soil layers
    - Photograph profile
    - Take samples from each layer

[ ] Field-test samples
    - Ribbon test on samples that look clay-like
    - Jar test on representative samples
    - Smell test
    - Strength test by hand

[ ] Document everything
    - Site map showing test locations
    - DCP plots
    - Test pit profiles with photos
    - Sample bags labeled
    - Field notes

[ ] Synthesize the findings
    - What soil type is dominant?
    - What's the bearing capacity at the proposed foundation depth?
    - Are there problem layers? Where?
    - Where's the water table?
    - Are there expansive soils?
    - Is the site uniform or variable?
```

### Phase 4 — Decision and Engineering

Based on the investigation:

```
[ ] Compare findings to the design assumptions
    - Does the foundation design (mat slab + extended edge) work with this soil?
    - Does the basement design work?
    - Are there changes needed?

[ ] If the findings are clearly good: proceed with the original design

[ ] If the findings show problems: 
    - Consult with a structural engineer about foundation modifications
    - Consult with a geotechnical engineer if problems are significant
    - Consider soil improvement strategies (Section 14.13)
    - Consider redesign (smaller building, different foundation, different siting)

[ ] If the findings show major problems:
    - Reconsider the site
    - Or accept the major investment in soil improvement
    - Or consider a different design (e.g., pole/pier instead of mat slab)
```

### Phase 5 — Pre-Construction Verification

Even after design is final, verify conditions during initial excavation:

```
[ ] As excavation proceeds, watch for unexpected conditions
    - Soil different from what you tested
    - Water you didn't expect
    - Soft layers you didn't find
    - Old fill or debris
    - Boulders that don't move

[ ] If anything unexpected: STOP
    - Document with photos
    - Take samples
    - Run additional DCP tests if practical
    - Consult with engineer if significant
    - Don't pour concrete on a foundation system that doesn't match the design assumptions

[ ] Run final DCP tests on the prepared subgrade before pouring
    - Verify compaction of any engineered fill
    - Verify no soft spots remain
    - Document with photos and the DCP profile
```

---

## 14.7 Bearing Capacity by Soil Type — Reference Tables

**Plain language:** Different soils have different bearing capacities. These tables give the typical ranges you can expect. Use them as ballpark figures and verification — actual project bearing capacity should come from your DCP, test pit observations, and engineering analysis.

### Allowable Bearing Pressures — Code Reference (ORSC R401.4)

Oregon Residential Specialty Code provides these prescriptive bearing values:

| Soil Type | Allowable Bearing (psf) |
|---|---|
| Crystalline bedrock | 12,000 |
| Sedimentary or foliated rock | 4,000 |
| Sandy gravel and gravel (GW, GP) | 3,000 |
| Sand, silty sand, clayey sand, silty gravel, clayey gravel (SW, SP, SM, SC, GM, GC) | 2,000 |
| Clay, sandy clay, silty clay, clayey silt, silt and sandy silt (CL, ML, MH, CH) | 1,500 |

These are conservative prescriptive values. Actual capacity may be higher with engineering analysis.

### Typical DCP / Field Test Results by Soil Description

| Soil Description | DCP PI (mm/blow) | CBR (%) | Estimated Bearing (psf) | Adequate for Residential? |
|---|---|---|---|---|
| Solid bedrock | 0-2 (refusal) | 100+ | 10,000+ | Excellent |
| Dense gravel/cobble | 2-4 | 50-100+ | 3,000-7,000 | Excellent |
| Compacted engineered fill | 4-8 | 25-50 | 1,500-3,000 | Good |
| Dense sand | 4-7 | 30-60 | 2,000-4,000 | Good |
| Stiff clay | 6-12 | 15-30 | 1,500-2,500 | Good (verify expansion) |
| Medium dense sand | 8-15 | 12-25 | 800-1,800 | OK with wider footings |
| Medium clay | 12-25 | 8-15 | 600-1,200 | Marginal — verify carefully |
| Loose sand | 20-40 | 5-10 | 400-800 | Marginal — needs improvement |
| Soft clay | 30-50 | 4-7 | 300-600 | Inadequate — needs improvement |
| Very soft clay | 50+ | 2-4 | <300 | Unsuitable |
| Organic / peat | varies | 1-3 | <200 | Unsuitable — must remove |

### Interpreting Your Site Results

Take your DCP data, convert to PI (millimeters per blow), look up the column, and you have a quick sanity check. Then compare to the ORSC prescriptive values for the soil type your visual inspection identified.

If they agree: you're confident in the soil character.
If they disagree: investigate further. Probably the soil isn't what you thought, or the strength isn't typical for that soil type.

---

## 14.8 Building a Basement — What the Soil Must Do

**Plain language:** A basement is a giant hole in the ground that has to stay open during construction, support tens of tons of structure, drain water year-round, and not heave or settle for the building's life. The soil has to be able to do all of this. Most Oregon sites can have basements; some can't. Here's how to tell.

### What a Basement Demands of the Soil

**1. Stable excavation walls during construction**

You're going to dig a hole 8-10 feet deep, leave it open for weeks while building the walls, and then backfill against the new walls. The hole has to stay open.

- **Cohesive soils (clays, silty clays, well-compacted soils):** Hold vertical walls for limited time periods (days to weeks). Best for basement excavation.
- **Granular soils (loose sand, silt):** Won't hold vertical. Need sloping (1:1 minimum) or shoring (sheet piles, soldier piles, etc.).
- **Saturated soils:** Won't hold any wall configuration; collapse rapidly.

**2. Adequate bearing capacity for foundation walls and slab**

A basement wall transmits roof, floor, and wall loads through itself to the soil. The soil at footing depth must support these loads with adequate margin.

- Mat slab in this design distributes loads broadly — most soils support a mat
- Concentrated wall loads (without spread footings) need stronger soil
- Soil under interior columns needs careful evaluation if any are present

**3. Lateral earth pressure resistance**

The basement walls are pushed against by the soil OUTSIDE the basement. This pressure increases with depth (hydrostatic-like) and is dramatically increased if the soil is saturated. The walls must be designed to resist this.

For typical basement walls:
- Dry granular soil: ~30 psf per foot of depth (active pressure)
- Wet granular soil: ~60-80 psf per foot of depth
- Clay soils: variable, can be much higher
- Saturated soil with hydrostatic head: very high

**4. Drainage to keep the basement dry**

Water in soil moves toward the basement. The drainage system (perimeter drain, gravel envelope, drainage mat — see Section 4 and 5) carries this water away. The soil's natural drainage characteristic affects how hard the system has to work.

- **Free-draining soil:** Easy. Drainage system handles light load.
- **Slow-draining soil (clay):** Hard. Backfill with gravel for the first several feet around foundation; design extensive drainage; verify daylighting.
- **Saturated zone (water table above basement floor):** Don't build a basement here unless you have an extreme commitment to pump systems and waterproofing.

**5. Frost depth deeper than basement footing**

The footing of a basement is automatically below frost depth (8 feet down vs. Oregon's 1-3 foot frost depth). Frost is rarely a basement issue.

**6. No expansive soil at basement walls**

Expansive clays (especially Willamette Valley alluvial clays in some areas) push outward against basement walls when wet, and can cause cracking and inward movement. If the soil is expansive, mitigation is needed (see Section 14.16).

### Site Conditions That Allow a Basement

A "basement-friendly" site has:

- Bearing capacity 2,000+ psf at basement footing depth
- Cohesive enough soil that excavation walls hold (or budget for shoring)
- Water table 12+ feet below grade (so 4+ feet below basement floor)
- No expansive clays (or active mitigation)
- Reasonable drainage characteristic
- Stable site (not landslide-prone)
- Clear path for drain daylighting (slope away from basement)

### Site Conditions That Prevent a Basement

A "basement-hostile" site has:

- Water table 8 feet or less below grade — basement floor would be in or near saturated zone
- Bedrock at 4-8 feet — would require expensive blasting/cutting
- Major expansive clay (high plasticity index, visible shrink-crack patterns)
- No way to daylight the drainage (low spot in landscape)
- Adjacent active landslide
- Liquefaction-prone soil with high seismic risk
- Very loose sand that won't hold an excavation

### What to Do Instead of a Basement

If the site can't support a basement, options include:

- **Slab-on-grade with no basement** — see 14.9
- **Crawl space (conditioned)** — short height, mechanical access, similar mat or strip foundation
- **Pier/post foundation** — building elevated on piers or posts (see 14.13)

---

## 14.9 Slab-on-Grade — What the Soil Must Do

**Plain language:** A slab-on-grade is a concrete slab poured directly on the ground (with proper preparation underneath). Easier than a basement and works on a wider range of sites. But the soil prep is critical.

### What a Slab-on-Grade Demands of the Soil

**1. Bearing capacity for the slab plus structure**

The slab spreads building loads over a wide area, so bearing pressures are usually modest. But the soil under the slab must support without significant settlement.

- 1,500+ psf typically adequate for residential slab-on-grade
- Higher for masonry/concrete construction (this design)

**2. Uniform support**

The big risk for a slab is differential settlement — one part settles more than another. The slab is rigid; it cracks if the soil under it moves unequally.

- Uniform native soil = best
- Uniform engineered fill = good (when properly placed and compacted)
- Patchy, mixed, or undocumented soil = trouble

**3. Drainage**

A slab can't get wet from below or it'll crack and degrade over time.

- Vapor barrier under slab (10-15 mil polyethylene) is essential
- Capillary break (clean coarse stone) below the vapor barrier
- Drainage away from the slab's edge

**4. Frost protection**

The edge of a slab-on-grade is the most vulnerable to frost heave. Two strategies:

- **Frost-protected shallow foundation (FPSF)**: extend insulation horizontally 2-4 feet beyond the slab edge to keep the soil under the slab from freezing
- **Conventional thickened edge below frost depth**: Standard footing extends below frost line at the slab perimeter

This design uses FPSF principles with the under-slab insulation extending out under the building edge.

**5. Stable subgrade (no organics, no unmanaged fill)**

Topsoil and organic soils MUST be removed. They will decompose, settle, and crack the slab.

### The Slab-on-Grade Subgrade Sequence

This is the actual soil prep for a slab-on-grade home. Each layer matters.

```
GROUND PROFILE FOR SLAB-ON-GRADE (BOTTOM TO TOP):

1. Undisturbed native soil (or properly compacted engineered fill)
   - Bearing capacity verified by DCP and visual inspection
   - All organics removed
   - All loose material compacted

2. Compacted gravel base course
   - 4-12 inches of 3/4-inch minus crushed rock
   - Compacted in 6-inch lifts to 95% Proctor
   - Provides drainage and uniform support

3. Capillary break layer
   - 4 inches of clean 1+ inch crushed rock with no fines
   - Stops moisture from wicking up

4. Vapor barrier
   - 10-15 mil polyethylene sheet
   - All seams lapped 6+ inches and taped
   - Continuous; sealed at penetrations

5. Under-slab insulation
   - Type XIV EPS, 4 inches in two staggered 2-inch layers
   - Insulation extends to slab edge
   - For frost-protected shallow foundation, insulation extends 2-4 feet horizontally beyond slab edge under the soil

6. Optional second vapor barrier
   - Above insulation, recommended for radiant slabs

7. Radiant tubing (if hydronic radiant heat)

8. Reinforcement (rebar grid or welded wire fabric, plus fiber reinforcement)

9. Concrete slab

10. Floor finish (polished concrete, tile, engineered wood, etc.)
```

### Site Preparation Sequence — Slab-on-Grade

```
PHASE 1 — STRIP

[ ] Strip topsoil to expose subsoil (typically 4-12 inches)
[ ] Remove all organic material (roots, stumps, leaves)
[ ] Stockpile topsoil for later landscape use (don't lose it)

PHASE 2 — INVESTIGATE

[ ] Run DCP tests across building footprint
[ ] Compare to design requirements
[ ] If soft spots found: identify their extent

PHASE 3 — REMEDIATE (if needed)

[ ] Soft spots: dig out to firm soil, replace with engineered fill
[ ] Wet areas: drain or replace
[ ] Variable soil: bring to uniform condition

PHASE 4 — SHAPE

[ ] Cut to design grade (typically a few inches below finished slab elevation)
[ ] Verify with surveying that the surface is at design elevation across the footprint
[ ] Shape the surface — slight slope to perimeter for drainage during construction is helpful

PHASE 5 — COMPACT

[ ] Compact the subgrade with a plate compactor or roller
[ ] Run multiple passes
[ ] Verify compaction with DCP or pocket penetrometer
[ ] Re-test after wet weather (compaction can settle if ground re-wets)

PHASE 6 — BASE COURSE

[ ] Place gravel base course in 6-inch lifts
[ ] Compact each lift before placing the next
[ ] Final surface to design elevation, level
[ ] Final compaction verified

PHASE 7 — LAYERED PREP

[ ] Capillary break layer
[ ] Vapor barrier
[ ] Insulation
[ ] (Per Section 4 sequence)

PHASE 8 — REINFORCEMENT AND POUR

[ ] Per Section 4
```

---

## 14.10 Excavation — The Work and What to Look For

**Plain language:** When you sit down at the excavator (or supervise the operator), here's what to look for as the dirt comes up. Every shovelful is data.

### Equipment Selection

For a typical residential building:

| Excavator Size | Operating Weight | Reach (typical) | Best For |
|---|---|---|---|
| Mini (1-2 ton) | 2,000-5,000 lb | 6-8 ft | Landscape, tight access, small trenches |
| Compact (3-4 ton) | 6,000-9,000 lb | 10-12 ft | Foundation work, small basements, drainage |
| Mid (5-8 ton) | 11,000-18,000 lb | 13-16 ft | Typical residential basements, mat slabs |
| Standard (10-15 ton) | 22,000-33,000 lb | 18-22 ft | Larger basements, commercial-scale residential |

**For this design's typical excavation (3,000 sqft footprint, 8-10 ft basement depth):**
- Estimated excavation: 800-1,200 cubic yards
- Recommended: 8-10 ton excavator with operator (rented), 1-2 weeks
- Or: 4-5 ton excavator owned/rented for owner-builder, 3-6 weeks

**For owner-builder use:**
- A 4-5 ton class is the smallest practical machine for basement work
- Smaller (mini) is fine for site prep, slab-on-grade, drainage trenches
- Rent a bigger machine for the basement dig itself; do ongoing work with your owned machine

### What to Look for as Soil Comes Up

```
COLOR CHANGES:
[ ] Topsoil = dark brown/black (organic, removed)
[ ] Subsoil = often lighter, browns or reds
[ ] Subsoil with red mottling = past saturation (water table reaches here)
[ ] Gray/blue subsoil = currently or recently saturated
[ ] Gradient from dark to light to gray = transition zones

TEXTURE CHANGES:
[ ] Sandy/granular = drains well
[ ] Clay (sticky, holds shape) = poor drainage
[ ] Mixed (loamy) = moderate
[ ] Increasing density with depth = good (compacted by overburden)
[ ] Decreasing density with depth = bad (organic layer below, or water effect)

ORGANIC LAYERS:
[ ] Visible roots, especially deep ones = continued biological activity
[ ] Decomposed plant material = organic layer, must be removed
[ ] Wood pieces (buried) = old fill, old structure remnants
[ ] Sour/sulfur smell = anaerobic decomposition

WATER:
[ ] Wet soil = perched water or near water table
[ ] Water entering excavation walls = perched water on hard layer above
[ ] Water rising in excavation bottom = hit the water table — STOP
[ ] Springs visible = active water flow, document, plan for

OBSTRUCTIONS:
[ ] Boulders = mark, possibly leave or break with hammer attachment
[ ] Buried debris = old foundation, dump fill — investigate, possibly redesign
[ ] Buried pipes or cables = stop, contact 811, locate before continuing
[ ] Buried tanks = environmental concern, get professional help

LAYER CHANGES:
[ ] Sharp boundary between soil types = natural soil layering, document
[ ] Sharp boundary with debris in it = old fill horizon
[ ] Smooth transition over depth = single soil with weathering profile

ROOT CHANNELS:
[ ] Old root channels filled with topsoil = preferential paths for water in clay
[ ] Visible large root channels = past trees; consider underground decay paths
```

### When to Stop and Reassess

**ANY of these conditions warrants stopping and reassessing:**

```
[ ] Water rising in the excavation
[ ] Soil dramatically different from your DCP / test pit findings
[ ] Excavation walls slumping or cracking
[ ] Buried structures, pipes, or debris
[ ] Soft, squishy soil where firm was expected
[ ] Wood, decomposed organic, or peat layer
[ ] Strong smells (sulfur, gasoline, solvent)
[ ] Strange soil colors (very black, deep blue, white-gray)
[ ] Unexpected boulders or rock layer
[ ] The excavation doesn't match the design plan in any meaningful way
```

When you stop, document with photos, record the location and depth, and decide whether you need engineering input before continuing. Most of the time these are minor issues you can solve quickly. Sometimes they're showstoppers requiring redesign. Either way, knowing matters.

### Excavation Profile — How to Dig the Hole Right

For a basement excavation:

```
DESIGN EXCAVATION DEPTH:
- Basement floor finished elevation
- Plus slab thickness (8 in typical)
- Plus insulation (4 in)
- Plus capillary break (4 in)
- Plus base course (6-12 in)
- Plus a few inches working room

= Approximately 24-30 inches deeper than basement floor

OVER-EXCAVATION:
- 6-12 inches beyond foundation perimeter for working room and waterproofing access
- 1:1 to 1:1.5 slope on excavation walls (granular soils may need flatter)
- Or vertical walls if cohesive soil and shoring used

DRAINAGE:
- Bottom of excavation should slope to one corner during construction
- That corner is where any water collects and is pumped out
- Sump pump on hand for unexpected water

UTILITIES:
- Locate underground utilities BEFORE digging (call 811)
- Excavate carefully near utilities; hand-dig the last few feet

INSPECTIONS:
- Pre-footing/pre-pour inspection (see Appendix D)
- BEFORE backfill, after foundation pour and waterproofing
```

---

## 14.11 Compaction — The Science and the Practice

**Plain language:** When you place fill or even when you disturb native soil, the soil is loose. A loose soil settles under load. To prevent this, you compact the soil — push it together so the particles are tightly packed and won't reorganize under load. Done right, this turns the fill into engineered ground that performs as well as good native soil. Done wrong, the fill will continue to settle for decades after you build on it.

### The Concept of Optimum Moisture and Density

Soils compact to maximum density at a specific moisture content called **optimum moisture content**. Less moisture: particles don't slide past each other. More moisture: water occupies space the particles need to fill. The optimum is in between.

For most soils: optimum moisture is 8-15% by weight, looking like "damp" — when you squeeze a handful, it holds a ball but breaks apart with light pressure.

The standard test that establishes this is the **Proctor test** (Standard Proctor or Modified Proctor). The output is:
- Maximum dry density (lb/ft³ or kg/m³)
- Optimum moisture content (%)

For owner-builder fill operations, you'll usually use **values estimated from soil type** rather than running a Proctor test:

| Soil Type | Approximate Maximum Dry Density (lb/ft³) | Approximate Optimum Moisture (%) |
|---|---|---|
| Well-graded gravel (GW) | 130-145 | 5-8 |
| Poorly-graded sand (SP) | 105-115 | 10-14 |
| Silty sand (SM) | 115-130 | 10-14 |
| Lean clay (CL) | 105-120 | 12-18 |
| Fat clay (CH) | 90-110 | 18-30 |
| Crushed rock (3/4" minus) | 130-145 | 5-8 |

**Target compaction is typically 90-95% of maximum dry density.** Below 90% the fill won't perform well; above 95% can be hard to achieve in the field.

### Compaction Equipment

For different fill quantities and conditions:

**Hand tampers ("jumping jacks"):**
- 5-10 inch wide rectangular base
- Vibrates and pounds simultaneously
- Best for tight spots, around foundation walls, in trenches
- Rentable at $50-100/day
- Slow but effective for small areas

**Plate compactors:**
- 18-30 inch wide flat plate
- Vibrates downward
- For most owner-builder fill operations, this is the workhorse
- Single-direction (foreward) or reversible (forward and back)
- Rentable at $50-100/day for single-direction, $100-200/day for reversible
- Owned: $1,000-3,000 new

**Sheepsfoot rollers:**
- Drum with protruding feet
- Best for clayey soils
- Towed behind tractor
- Rentable, used for large operations

**Smooth drum rollers:**
- Heavy smooth steel drum
- Best for granular soils, finished surfaces
- Rentable, larger projects

**Pneumatic tire rollers:**
- Multiple rubber tires
- Versatile, can do most soils
- Larger projects

**For owner-builder use:** Plate compactor + jumping jack covers nearly everything you'll need.

### The Compaction Process

```
STEP 1 — PLACE FILL IN LIFTS

[ ] Lift = a single layer of fill placed before compaction
[ ] Lift thickness depends on equipment:
    - Hand tamper: 4-6 inch lifts
    - Plate compactor: 6-8 inch lifts
    - Larger equipment: 8-12 inch lifts
[ ] DO NOT place a thick lift and try to compact all at once — only the surface compacts

STEP 2 — VERIFY MOISTURE

[ ] Squeeze a handful of soil
[ ] If it crumbles immediately = too dry; add water
[ ] If water squeezes out = too wet; allow to dry
[ ] Aim for "moist enough to hold a ball briefly"
[ ] Sprinkler or hose to add water; don't soak

STEP 3 — COMPACT

[ ] Multiple passes — single pass rarely achieves target compaction
[ ] Plate compactor: 4-6 passes typical for granular soils, 8-12 for clays
[ ] Move methodically — overlap each pass by 50%
[ ] In confined areas, switch directions on alternate passes

STEP 4 — VERIFY

[ ] Look at the surface
    - Dense, hard, "ringing" under boot impact = good
    - Boot footprints visible = inadequate
[ ] DCP test
    - PI < 8 mm/blow on compacted fill = excellent
    - PI 8-15 mm/blow = adequate for most residential fill
    - PI > 15 mm/blow = needs more compaction
[ ] Pocket penetrometer (for cohesive soils)
    - 4+ tsf reading = adequate
    - Less = inadequate

STEP 5 — REPEAT FOR EACH LIFT

[ ] Place next lift
[ ] Verify moisture
[ ] Compact
[ ] Verify
[ ] Continue until at design elevation
```

### Compaction Around Foundations

A special case — compacting backfill around foundation walls:

- USE jumping-jack hand tampers (not plate compactors)
- Lifts of 6 inches or less
- Don't compact too aggressively — can damage waterproofing membrane
- Use granular material (sand, gravel) as backfill in the first 12-24 inches against the wall
- Native clay backfill higher up is OK if compacted properly

### Common Compaction Failures

**FAILURE: Lifts too thick**
- Symptom: Surface compacts, deeper material doesn't
- Result: Slow long-term settlement
- Fix: Re-do with proper lift thickness

**FAILURE: Wrong moisture content**
- Symptom: Compactor "bounces" on dry soil, or "pumps" on wet soil
- Result: Inadequate density
- Fix: Add or remove water, re-compact

**FAILURE: Wrong soil type**
- Symptom: Soil contains large rocks, organics, varied sizes
- Result: Voids, settling, weak fill
- Fix: Use proper engineered fill — uniform, graded, organic-free

**FAILURE: Inadequate equipment**
- Symptom: Hand-tamping a large area
- Result: Inconsistent density
- Fix: Right equipment for the area

**FAILURE: Skipped verification**
- Symptom: "It looked compacted"
- Result: Years of unexpected settling after construction
- Fix: ALWAYS verify with DCP or pocket penetrometer

---

## 14.12 Soil Problems — The Catalog

**Plain language:** Beyond just "soft soil," there are specific kinds of soil problems with specific symptoms and specific fixes. Knowing them by name helps you recognize them in the field.

### Problem 1 — Insufficient Bearing Capacity

**Symptoms:** Soft soil, high DCP penetration index, pocket penetrometer reading low, soil deforms easily under hand pressure.

**Causes:**
- Naturally weak soil (recent alluvium, organics, very loose sand)
- Disturbed soil (recent earthwork that wasn't compacted)
- Saturated soil
- Decomposing organic content

**Fixes:**
- Over-excavate and replace with engineered fill (Section 14.13)
- Improve in place with compaction or stone columns
- Bypass with deep foundations (piers, piles)

### Problem 2 — Excessive Settlement

**Symptoms:** Compressible soil that continues to lose volume under load. Common in organic soils, peats, very soft clays.

**Causes:**
- High organic content
- Compressible clay layers
- Recent (geologically) deposits
- Decaying material

**Fixes:**
- Identify and remove organic/compressible layers
- Pre-load the soil (place heavy material before construction to "use up" the settlement)
- Vertical drains to accelerate consolidation
- Bypass with deep foundations

### Problem 3 — Expansive (Shrink/Swell) Soil

**Symptoms:** Soil cracks open in dry seasons, swells with moisture. Plasticity index >25. Foundation movement.

**Causes:**
- Specific clay minerals (montmorillonite, smectite)
- Marine or lake deposits
- Common in some Willamette Valley alluvial soils

**Fixes:**
- Avoid the site if possible
- Over-excavate and replace top 3-5 feet
- Stiffened slab foundation (post-tensioned or thick reinforced)
- Pier-and-grade-beam foundation (raise structure off the soil)
- Moisture control around the foundation
- Lime stabilization (chemical treatment)

### Problem 4 — Collapsible Soil

**Symptoms:** Soil with low natural moisture and high void ratio. Stable when dry, suddenly collapses when wetted.

**Causes:**
- Wind-blown silt (loess)
- Some volcanic ash deposits
- Salt-cemented soils

**Fixes:**
- Pre-wet and compact the soil
- Compact in lifts as described
- Avoid creating concentrated water sources (downspouts, leaks) that could trigger collapse

### Problem 5 — Frost-Susceptible Soil

**Symptoms:** Frost heave in winter — soil lifts upward as ice lenses form.

**Causes:**
- Silty soils with available water
- Saturated zone within frost depth
- Capillary water rising from below

**Fixes:**
- Foundation footings below frost depth
- Capillary break under slab
- Drainage to remove water from frost zone
- Replace silt layer with non-frost-susceptible (clean gravel)

### Problem 6 — Liquefaction-Prone Soil

**Symptoms:** Saturated, loose, fine sand. During an earthquake, water pressure between particles makes the soil flow like a liquid. Buildings sink, tilt, or collapse.

**Causes:**
- Loose, saturated sand (especially from recent geological deposits)
- High water table
- Significant seismic risk (most of Oregon)

**Fixes:**
- Densify the soil (compaction, stone columns, dynamic compaction)
- Drain the soil (lower water table)
- Use deep foundations through the liquefiable layer to firm soil
- Avoid the site

Liquefaction is most dangerous along Oregon's coast, in some Willamette Valley alluvial flats, and near the Columbia River. The Oregon DOGAMI maintains liquefaction susceptibility maps.

### Problem 7 — Variable / Inconsistent Soil

**Symptoms:** DCP results vary widely across the building footprint. Test pits show different soil at different locations.

**Causes:**
- Geological complexity (fluvial deposits, debris flow deposits)
- Past human activity (old fill, demolition)
- Local features (buried streams, roots from removed trees, etc.)

**Fixes:**
- Investigate thoroughly — many test points
- Bring all areas to a consistent prepared subgrade
- Engineered fill across the entire footprint
- Foundation design that accommodates variation (mat slab is good for this)

### Problem 8 — Old Fill / Anthropogenic Soils

**Symptoms:** Buried debris, broken concrete, old structures, demolition waste. Random voids and weak spots.

**Causes:**
- Site previously used as a dump
- Old building demolished and the foundation buried
- Unmanaged fill from previous earthwork

**Fixes:**
- Investigate aggressively — many test pits
- Remove all fill and replace with engineered fill
- Bypass with deep foundations (rare for residential)
- Avoid the site if extent is too large

### Problem 9 — Slope Stability Issues

**Symptoms:** Curved tree trunks, leaning fence posts, hummocky surface, scarps in the slope, water seeping from slope face.

**Causes:**
- Past or active landsliding
- Slope angle exceeding the angle of repose for the soil
- Saturation of clay layers
- Removal of vegetation that was holding soil

**Fixes:**
- AVOID the site for residential construction unless you really know what you're doing
- Engineered slope stabilization (retaining walls, drainage, soil nails, etc.) — expensive
- Build up-slope of the unstable area
- Check the DOGAMI Statewide Landslide Information Database (SLIDO) before purchasing

### Problem 10 — Karst / Soluble Bedrock

**Symptoms:** Sinkholes, caves, voids in limestone bedrock.

**Causes:**
- Limestone or other soluble bedrock dissolving
- Eastern Oregon basalts can have lava tubes (similar effect)

**Fixes:**
- Geological investigation before purchase
- Specialty foundation if proceeding (shallow with grade beam over voids, or deep to competent rock)
- Avoid sites with active subsidence

---

## 14.13 Soil Improvement — Making Bad Ground Buildable

**Plain language:** Sometimes the soil under your site isn't great, but the site is great in every other way — the location, the view, the price, the access. There are real solutions to make weak soil strong enough to build on. The solutions range from million-dollar specialty operations to weekend owner-builder work, and the right choice depends on the problem, the budget, and how much soil needs improving. This section covers all of them, organized from least to most owner-builder-friendly.

### Why Soil Improvement Matters

Three reasons to improve soil rather than abandon a site:

1. **The site is otherwise excellent** — view, location, access, price all favorable
2. **The problem is local, not site-wide** — a soft spot, an old fill area, an organic layer; not the whole property
3. **The improvement cost is less than the cost of finding a better site** — sometimes a $20,000 soil fix is cheaper than starting the search over

Three reasons to NOT improve soil and instead find a different site:

1. **The problem is site-wide and severe** — entire property has 15 feet of compressible peat
2. **The improvement cost approaches new construction cost** — million-dollar fixes for a $300,000 house
3. **The improvement involves ongoing risk** — active landslide, liquefaction-prone, persistent groundwater, etc.

### The Hierarchy of Soil Improvement

Soil improvement methods, from cheapest and simplest to most complex and expensive:

| Method | Owner-Builder DIY? | Typical Cost (per home) | Best For |
|---|---|---|---|
| Over-excavation and replacement | Yes (small extent) | $5,000 - $50,000 | Local soft spots, shallow problems |
| Compaction of existing soil | Yes | $1,000 - $5,000 | Loose granular soils |
| Pre-loading | Yes (with patience) | $2,000 - $20,000 | Compressible clays |
| Lime/cement stabilization | Specialty contractor | $10,000 - $40,000 | Expansive clays, weak soils |
| Stone columns | Specialty contractor | $30,000 - $100,000 | Loose sands, weak fine-grained soils |
| Rammed aggregate piers (Geopier) | Specialty contractor | $30,000 - $80,000 | Variable soils, compressible layers |
| Helical piers | Owner-builder possible with rented equipment | $15,000 - $40,000 | Localized weak areas, retrofit, slope sites |
| Driven piles | Specialty contractor | $50,000 - $150,000 | Deep weak layers, heavy structures |
| Drilled shafts (caissons) | Specialty contractor | $50,000 - $200,000 | Very deep bearing, heavy loads |
| Vibroflotation | Specialty contractor | $50,000 - $200,000 | Liquefiable sands |
| Dynamic compaction | Specialty contractor | $50,000 - $200,000 | Large areas of loose granular fill |
| Grouting (chemical, jet) | Specialty contractor | $50,000 - $300,000 | Complex problems, voids |

I'll go through each one in detail.

### 14.13.1 Over-Excavation and Replacement — The Owner-Builder Workhorse

**The concept:** Dig out the weak soil. Replace it with engineered fill that you compact properly. The replaced material is now strong enough to build on. This is the simplest, most foolproof, and most owner-builder-friendly method when the weak layer isn't too deep.

**When it works:**
- Soft layer is shallow (less than 6 feet typically)
- Soft area is local rather than site-wide
- You have space to dump the excavated material
- You can source quality fill (gravel pit nearby)

**When it doesn't work:**
- Weak layer is too deep to economically excavate
- Water table is in the way (excavation fills with water)
- Replacement material is unavailable

**The procedure:**

```
PHASE 1 — DEFINE THE PROBLEM AREA

[ ] Run DCP tests across the building footprint
[ ] Identify the limits of the weak zone
[ ] Determine how deep the weak layer goes (DCP plus test pit)
[ ] Calculate volume to be removed

PHASE 2 — EXCAVATE

[ ] Strip topsoil first (save it; you'll use it elsewhere)
[ ] Excavate the weak material
[ ] Continue down to verifiably firm native soil
[ ] DCP-test the excavation bottom to confirm
[ ] Excavate slightly past the building footprint perimeter (typically 1:1 slope around the edge)
[ ] If walls are unstable, slope at 1:1.5 or shore them
[ ] Stockpile the excavated material — may be useful for landscape, may be waste

PHASE 3 — VERIFY THE BOTTOM

[ ] DCP test the bottom of the excavation
[ ] Confirm bearing capacity adequate (>2,000 psf for typical residential)
[ ] If bottom is still soft, excavate deeper
[ ] If bottom is wet, drain or pump

PHASE 4 — PLACE ENGINEERED FILL

[ ] Specify the fill material
    - Most common: 3/4-inch minus crushed rock
    - Alternative: pit-run (mixed sand and gravel from a quarry)
    - For drainage: clean coarse gravel
    - For density: any well-graded mineral soil with limited fines (passing #200 sieve <12%)
[ ] Source from local quarry or pit
[ ] Order quantity = excavation volume × 1.1 (compaction allowance)

[ ] Place in lifts (8-inch maximum)
[ ] Wet to optimum moisture (the squeeze-and-crumble test from 14.11)
[ ] Compact each lift to 95% Proctor density
[ ] Verify compaction with DCP (PI <8 mm/blow on each lift)

[ ] Continue until at design subgrade elevation
[ ] Final compaction verified across the entire footprint

PHASE 5 — TRANSITION

[ ] Where engineered fill meets undisturbed native soil at the perimeter, transition gradually
[ ] If the native soil is also adequate, this transition is straightforward
[ ] If the native soil is borderline, extend the engineered fill further to ensure consistent support

PHASE 6 — DOCUMENT

[ ] Photo log of the excavation and replacement
[ ] DCP profiles before and after
[ ] Quantity of fill placed
[ ] Compaction test results for each lift
[ ] Map of where the engineered fill is located (you'll want to know in 50 years)
```

**Cost example:**

For a 30-foot by 40-foot weak zone, 4 feet deep:
- Volume to remove and replace: 30 × 40 × 4 = 4,800 cubic feet = 178 cubic yards
- Excavation cost (small contractor or owner labor with rented mini-excavator): $3,000-$8,000
- Fill material: 200 cubic yards × $25/yard delivered = $5,000
- Compaction equipment rental: $500-$1,500
- Plus owner labor: 80-120 hours
- **Total: $10,000-$20,000 for the home itself**

**Why this is the owner-builder favorite:**
- No specialty equipment needed (your mini excavator + rented plate compactor)
- No engineering analysis required (provided you replace fully and compact properly)
- Foolproof — you SEE the problem soil leaving and the good soil arriving
- Documented and defensible at resale

### 14.13.2 In-Place Compaction

**The concept:** Sometimes the soil is just loose, not actually weak. Compacting it in place — without removing and replacing — densifies it enough to build on. Works for granular soils (sand, gravel) where the issue is looseness rather than fundamental weakness.

**When it works:**
- Loose sand or gravel
- The grain structure is fine; just need to push particles closer together
- Surface accessible for compaction equipment

**When it doesn't work:**
- Cohesive soils (clay) — compaction by surface vibration is much less effective
- Saturated soils — water doesn't compress
- Organic soils — compaction doesn't address the fundamental decomposition
- Loose layer below a stiffer surface layer (compaction energy doesn't reach it)

**Methods:**

**Surface vibratory compaction:**
- Heavy plate compactor or roller
- Surface treatment for upper 12-18 inches
- Same as fill compaction but applied to existing soil
- Owner-builder friendly with rented equipment

**Dynamic compaction (the heavy version):**
- A heavy weight (10-30 tons) is dropped from a crane (40-100 feet)
- Densifies soil to 30+ feet depth
- Specialty contractor only
- $50,000-$200,000 typical for a building site
- Used for liquefiable sand or large fill areas

**Vibroflotation:**
- A vibrating probe is inserted into the ground
- Densifies surrounding sand by vibration
- Can densify to 50+ feet depth
- Specialty contractor only
- Common for liquefaction mitigation

**Compaction grouting:**
- Cement grout is pumped into the ground at high pressure
- Pushes surrounding soil aside, densifying it
- Specialty contractor only
- For very specific situations

**For owner-builder use:** Surface vibratory compaction with rented equipment is the only practical option. Effective for the upper 18-24 inches; not effective deeper.

### 14.13.3 Pre-Loading (Surcharging)

**The concept:** Compressible clay soils settle slowly under load. Place a heavy temporary load on the site BEFORE building, let the clay settle for months or years, then remove the load and build on the now-pre-settled soil.

**When it works:**
- Compressible clay layers
- You have time (this is a months-to-years process)
- You have material for the surcharge (often the dirt from the basement excavation, piled high)

**When it doesn't work:**
- Need to build quickly
- No place to put the surcharge material
- Soil that doesn't consolidate (peat, organic soils settle for decades; pre-loading isn't enough time)

**The procedure:**

```
PHASE 1 — CALCULATE THE SURCHARGE

[ ] Estimate the building's eventual load
[ ] Add 50-100% safety margin
[ ] Calculate the volume of soil/gravel needed for that load over the site
[ ] Ensure access for placing it

PHASE 2 — PLACE THE SURCHARGE

[ ] Strip topsoil
[ ] Place the surcharge in a single mass over the building footprint
[ ] Often a square or circular mound 5-15 feet tall

PHASE 3 — MONITOR

[ ] Settlement plates installed (just steel plates with a vertical pipe rising up)
[ ] Survey the settlement plates monthly
[ ] Track the settlement curve

PHASE 4 — WAIT

[ ] Settlement is logarithmic — fast at first, slowing exponentially
[ ] Wait until 90% of expected settlement has occurred
[ ] Typically 6-18 months

PHASE 5 — REMOVE

[ ] Remove the surcharge
[ ] Begin construction
[ ] Foundation now sits on pre-consolidated soil that won't settle further
```

**Vertical drains can speed this up.** PVD (prefabricated vertical drains, sometimes called "wick drains") are pushed into the ground at intervals; they accelerate water drainage from the clay, accelerating consolidation. Reduces pre-load time from years to months. Specialty contractor; typically only on large projects.

**For owner-builder use:** Pre-loading without vertical drains is feasible if you have time and material. Practical example: dig the basement, pile the spoils on the building footprint of FUTURE expansion areas, let it sit while you build the main house, then remove the surcharge for the future addition.

### 14.13.4 Chemical Stabilization (Lime, Cement)

**The concept:** Mix a binder (lime or cement) into the soil to chemically improve it. Lime reacts with clay particles to reduce plasticity and increase strength. Cement bonds particles together. The result is a cement-stabilized soil that's much stronger and less moisture-sensitive than the natural soil.

**When it works:**
- Expansive clays (lime is the classic treatment)
- Marginal soils that need a strength bump
- Surface treatment of subgrade for a slab

**When it doesn't work:**
- Very organic soils (chemicals don't react well with organics)
- Very wet soils (chemicals don't mix and react properly)
- Granular soils with no clay (lime needs clay to react with)

**Process for lime stabilization:**

```
[ ] Test soil to confirm clay content >25%
[ ] Determine optimum lime content (typically 3-7% by weight)
[ ] Spread quicklime or hydrated lime over surface (powder form)
[ ] Mix into upper 8-18 inches with rotary mixer (specialty equipment)
[ ] Add water if needed
[ ] Compact
[ ] Let cure (lime needs days to weeks to react)
[ ] Test improved properties before construction
```

**For owner-builder use:** This is specialty contractor territory. Equipment is industrial. Chemicals are caustic and require safety equipment. But for a site with significant expansive clay, this can be a cost-effective alternative to over-excavation.

**Cost:** $10,000-$40,000 for a residential building footprint, depending on depth and area.

**Cement stabilization** works similarly but with Portland cement instead of lime. Better for soils with less clay; produces a stronger but more brittle result.

### 14.13.5 Stone Columns / Aggregate Piers

**The concept:** Drill or push holes into the weak soil at a regular grid. Fill the holes with compacted aggregate (gravel). The aggregate columns transfer building loads through the weak soil to firmer underlying material. Also drains the surrounding weak soil and confines it laterally.

**When it works:**
- Loose sand
- Soft clay
- Variable fill
- Need to support a structure on weak surface soils with firmer soils 10-30 feet down

**When it doesn't work:**
- Very deep weak layers (>40 feet)
- Heavy structures (industrial; residential is fine)
- No firmer layer below

**Specialty contractor methods:**

**Vibro-replacement stone columns:**
- A vibrating probe creates a hole
- Stone is fed in and compacted as the probe withdraws
- Diameter 24-36 inches
- Spacing 6-10 feet on center
- 15-30 feet deep typical

**Geopier rammed aggregate piers:**
- A drilled shaft is filled with stone in lifts
- Each lift is hammered (rammed) with a beveled tamper
- Creates very dense, high-modulus aggregate columns
- Diameter 24-30 inches
- Spacing 6-10 feet on center
- 15-30 feet deep typical
- Trademarked process; many regional contractors

**For owner-builder use:** Specialty contractor only. The equipment (vibratory probes, drilling rigs, ramming hammers) is industrial. But the result — a building site supported on engineered aggregate columns — can be the right answer for a problem site.

**Cost:** $30,000-$100,000 for a residential building footprint.

### 14.13.6 Helical Piers — The Owner-Builder Friendly Deep Foundation

**The concept:** A steel shaft with helical (screw-shaped) plates is rotated into the ground until it reaches firm soil or a target torque. The piers extend through the weak soil to a competent layer below. The building is supported on the piers via a grade beam or pile cap.

**When it works:**
- Weak surface soils with firmer soils within 30 feet
- Slope sites where excavation is difficult
- Retrofits where you need to underpin existing foundations
- Sites with limited access for big equipment

**When it doesn't work:**
- No firm bearing layer within reasonable depth
- Very dense gravels or boulders that block screw penetration
- Heavy structural loads exceeding pier capacity (rare for residential)

**The process:**

```
PHASE 1 — DESIGN

[ ] Geotechnical investigation determines firm layer depth
[ ] Structural engineer designs the pier layout
    - Typical: piers under each foundation wall corner and at intervals along walls
    - 5-10 feet spacing typical
[ ] Pier capacity calculated based on torque-to-capacity correlations
    - Most piers rated 20,000-50,000 lb (10-25 tons) capacity
    - Multiple helices for higher capacity

PHASE 2 — INSTALLATION

[ ] Hydraulic torque motor mounted on a small tracked machine or excavator arm
[ ] Each pier rotated into the ground
[ ] Torque monitored during installation
[ ] When target torque achieved, installation stops
[ ] Pier extension shafts added as needed for greater depth

PHASE 3 — STRUCTURAL CONNECTION

[ ] Pier caps installed at top of each pier
[ ] Reinforced concrete grade beam connects pier caps
[ ] Grade beam supports the foundation walls
[ ] Building constructed on the grade beam normally

PHASE 4 — VERIFICATION

[ ] Each pier's torque-capacity record documented
[ ] Test piers loaded to verify capacity (sometimes done on first installations)
```

**For owner-builder use:**
- Helical pier installation equipment can be rented (rare in some markets, common in others)
- The hydraulic torque motor mounts on a standard mini-excavator arm
- The piers themselves are sold by manufacturers and arrive in segments
- Installation is more accessible than other deep foundation methods
- A determined owner-builder with rental equipment and engineering support can install their own piers

**Cost:**
- Specialty contractor: $15,000-$40,000 for a residential building
- Owner-builder with rented equipment + materials: $8,000-$20,000

**Brands and suppliers:**
- **CHANCE (Hubbell)** — major helical pier manufacturer
- **MagnumPiering** — alternative
- **Earth Contact Products** — alternative
- **IDEAL Foundation Systems** — alternative
- Local contractors in most regions; may sell to owner-builders

### 14.13.7 Driven Piles

**The concept:** Long structural elements (steel, concrete, wood, or composite) hammered or pressed into the ground until they reach firm bearing. The building is supported on the piles. Used for very heavy structures or very deep weak layers.

**Types:**
- Timber piles (rare in residential except waterfront)
- Steel H-piles
- Concrete-filled steel pipe piles
- Precast concrete piles

**When it works:**
- Deep weak layers (firm soil 30-100 feet down)
- Heavy structures
- Marine or waterfront

**When it doesn't work:**
- Most residential applications (overkill)
- Sites with restrictions on noise (driving piles is loud)
- Sites with adjacent vibration-sensitive structures

**For owner-builder use:** Not practical. The equipment is large and specialized. Cost is high. Other methods nearly always make more sense for residential.

### 14.13.8 Drilled Shafts (Caissons)

**The concept:** Large-diameter holes (24-72 inches) drilled deep into the ground, typically to bedrock. Filled with reinforced concrete. The building rests on the drilled shafts.

**When it works:**
- Need to reach bedrock at significant depth
- Heavy structures
- Very weak overburden soils

**When it doesn't work:**
- Most residential (overkill)
- High water table during drilling
- Restricted access for drilling rig

**For owner-builder use:** Not practical. Specialty drilling equipment required.

### 14.13.9 Pole / Pier Foundations — The Lightweight Option

**The concept:** Instead of a continuous foundation, support the building on a series of point loads — concrete piers or wood poles. Especially common for elevated buildings, hillside construction, and high-water-table sites where you want to lift the building above the water.

**When it works:**
- Variable surface soils
- High water table situations
- Steep terrain
- Sites where you want to elevate the structure

**When it doesn't work:**
- Heavy concrete/masonry buildings (this design) — point loads are very high
- Sites where mass thermal benefits matter (you lose ground contact)

**For this design specifically:** A pole/pier foundation conflicts with the design's emphasis on continuous concrete contact and thermal mass. But for a future variant or alternative siting, it's an option.

**For owner-builder use:**
- Drilling holes (12-36 inches diameter) is feasible with rented equipment
- Pier construction is straightforward concrete work
- Connection to grade beam or floor structure is engineering-driven

### 14.13.10 Choosing the Right Soil Improvement Strategy

A decision framework:

```
1. Is the problem local (small area) or site-wide?
   - Local: over-excavation and replacement
   - Site-wide: more involved methods

2. Is the weak layer shallow (<6 ft) or deep?
   - Shallow: over-excavation is cheap
   - Deep: piers, columns, or stabilization

3. Is the issue low strength or unfavorable behavior (expansion, etc.)?
   - Low strength: replacement, compaction, or piers
   - Expansion: chemical stabilization, replacement, or design adaptation
   - Liquefaction: densification specialty methods

4. What's the budget?
   - $5-20k: Over-excavation, replacement, in-place compaction
   - $20-50k: Helical piers (DIY) or chemical stabilization
   - $50-100k: Specialty methods (stone columns, etc.)
   - $100k+: Major foundation engineering

5. What's the timeline?
   - Immediate construction: helical piers, replacement, mechanical methods
   - Have time: pre-loading, allowing settlement to occur

6. What's the equipment available?
   - Just a mini-excavator: replacement, compaction
   - Plus rented helical pier installer: + helical piers
   - Specialty contractor: any method
```

**Most owner-builder situations resolve to one of these:**
- **Mostly good site, local problem:** over-excavation and replacement (do yourself)
- **Variable site needing strength:** helical piers (rent equipment, hire engineer)
- **Expansive clay:** lime stabilization (hire specialty contractor) OR over-excavation and replacement of upper layer (do yourself)
- **Bad site:** find a different site

---

## 14.14 The High Water Table — Brief Treatment

**Plain language:** A high water table is one of the most challenging site conditions for residential construction. The fundamentals are unforgiving: water finds every weakness, and the higher the water table, the harder and more expensive everything becomes. A site with a 5-foot water table CAN be built on, but the cost and risk make it almost always the wrong answer compared to picking a different site. Here's the brief treatment of why and what's possible.

### What "High Water Table" Means

The water table is the level below which the soil is saturated with groundwater. A "high" water table is one within reach of your foundation:

- **Below 15 feet** — Generally not a concern
- **8 to 15 feet** — Manageable; basement still possible with good waterproofing
- **5 to 8 feet** — Difficult; basement is risky and expensive
- **Below 5 feet** — Avoid; even slab-on-grade has challenges
- **At surface** — Essentially unbuildable without extreme measures

### Why High Water Tables Are Hard

The physics:

1. **Hydrostatic pressure** — Water at depth has weight. A basement floor 5 feet below the water table experiences ~310 psf (5 ft × 62.4 lb/ft³) of upward pressure. The walls experience similar lateral pressure. This pressure is constant and never goes away.

2. **Water finds every flaw** — A 1/16-inch crack in a concrete wall under water pressure becomes a continuous leak. Waterproofing must be flawless.

3. **Buoyancy / uplift** — A basement is a hollow box. Water below it tries to float it. An empty basement on a high water table can literally pop up out of the ground.

4. **Construction is hard** — Excavating below the water table requires constant pumping. Mud, instability, walls collapsing.

5. **Soil weakens** — Saturated soil has lower bearing capacity than the same soil dry. The site evaluation may have been done in dry season; wet season changes everything.

6. **Frost heave amplified** — Saturated soil within frost depth heaves more.

### The Basement on a High Water Table — What It Takes

If you absolutely must build a basement on a site with a 5-foot water table:

**Engineering requirements:**
- Reinforced concrete basement walls and floor designed to resist hydrostatic pressure
- Floor slab must resist uplift (often by anchoring to deep piers or by relying on building weight)
- Continuous external waterproofing membrane (not damp-proofing) — the highest grade
- Internal drainage system as a backup
- Continuous interior dehumidification

**Construction requirements:**
- Dewatering during excavation (well points, sump pumps, or a perimeter dewatering system)
- Excavation walls fully shored — soil under the water table doesn't hold itself up
- Concrete poured underwater in extreme cases (tremie concrete)
- Multiple layers of waterproofing
- Drainage gravel envelope all around

**Permanent operational requirements:**
- Sump pump(s) running, possibly continuously
- Backup pumping (battery and/or generator)
- Dehumidification
- Regular inspection for leaks
- Vapor barrier integrity
- Water alarm

**Cost premium:**
A high-water-table basement might cost 3-5× a normal basement. A $50,000 basement becomes $150,000-$250,000.

### Failure Modes — What Goes Wrong

Things that happen on basements with high water tables:

- **Hydrostatic leaks** — Water finds the smallest flaw in the waterproofing, eventually
- **Floor cracking from uplift** — When the pump fails and the basement floods, the empty floor lifts
- **Structural movement** — Walls bow inward over decades of pressure
- **Mold and humidity problems** — Even with excellent dehumidification, moisture is constant
- **Pump failure floods** — One blown circuit during a thunderstorm and the basement is full
- **Buoyancy failure** — Empty unfinished basement during construction lifts and rotates

### The Slab-on-Grade on a High Water Table

A slab-on-grade is more forgiving but still has challenges:

- **Capillary moisture** — Water rises through soil by capillary action. Continuous capillary break required.
- **Vapor pressure** — Vapor barrier must be excellent.
- **Differential settlement** — Saturated soil consolidates over time; the slab follows.
- **Subgrade weakness** — Saturated soils are weaker; need careful preparation.

For a high-water-table site, slab-on-grade is dramatically more practical than a basement. Still possible. Still requires:
- Elevated finished floor (often with engineered fill bringing the building above the water table)
- Continuous capillary break and vapor barrier
- Excellent perimeter drainage
- Sometimes a pumped sub-slab drainage system

### When to Just Walk Away

**Walk away from a site if:**
- Water table is consistently within 5 feet of the surface
- Adjacent properties show water problems
- The site has visible groundwater discharge (springs, wet spots)
- Drainage out of the site is not possible (low spot in landscape)
- The cost of dealing with the water table exceeds the cost of a different site

**There is no virtue in being clever about a wet site.** The simplest solution to a high water table is finding a different lot. Spend the savings on a better build elsewhere.

### Site Assessment for Water Table

Before purchasing, evaluate water table:

```
[ ] Visit in wet season (winter/spring in Oregon) and dry season
[ ] Test pits dug to 8+ feet — observe water level after sitting open for 24 hours
[ ] Check well logs for nearby properties (Oregon Water Resources Department database)
[ ] Examine soil for signs of past saturation:
    - Mottling (orange/red spots in soil) = water table reaches this depth seasonally
    - Gleying (gray/blue color) = currently or recently saturated
    - Strong sulfur smell = anaerobic, definitely wet
[ ] Examine vegetation:
    - Cattails, reed canary grass, willow trees = wet
    - Healthy oak, pine, douglas fir = drier
[ ] Check FEMA flood map and DOGAMI map
[ ] Talk to neighbors about basement leakage, sump pump operation, etc.
[ ] In extreme cases, install a piezometer (a measuring well) and monitor over a year
```

Save yourself the heartbreak. Walk a site through the wet season before you buy.

---

## 14.15 Oregon-Specific Soil Conditions

**Plain language:** Oregon is geologically diverse. The soils west of the Cascades (where most population lives) are very different from soils east of the Cascades. Within each region, more variation. Knowing what to expect in each region — and what problems are common — speeds up site evaluation and helps you avoid showstoppers.

### The Major Geological Regions of Oregon

```
     Coast Range — sandstone, basalt, slumpy clay soils
     Willamette Valley — alluvial silts and clays, ancient flood deposits
     Cascade Range — basalts, andesites, volcanic ash, glacial deposits
     High Cascades — recent volcanics, glacial deposits, pumice
     Klamath Mountains (SW) — granitic, sedimentary, complex
     Basin and Range (SE) — basalt, pumice, fault block geology
     Columbia Basin (NE) — basalt, loess (wind-blown silt)
     Blue Mountains (NE-Central) — basalt, glacial deposits
     Owyhee Plateau (SE) — basalt, rhyolite, volcanic ash
```

Each has typical soil types and typical building challenges.

### Coast Range — The Wet Side

**Geology:** Marine sedimentary rocks (sandstone, shale, mudstone), some basalt, weathered to deep clay-rich soils.

**Typical soil profile:**
- Topsoil: 6-12 inches of organic-rich brown loam
- Subsoil: 2-6 feet of red-brown clay (weathered from rock)
- Saprolite: weathered rock (still has rock structure but soft)
- Bedrock: sandstone or basalt

**Common challenges:**
- **Slope instability** — The wet, clay-rich, deep soils on slopes have a long history of landsliding. Coast Range is the highest landslide region in Oregon.
- **High groundwater** — Wet climate (60-100 inches of rain), poor drainage, high water tables in low areas.
- **Expansive clays** — Some marine-origin clays show shrink-swell behavior.
- **Soft soils** — Thick weathered profiles can mean weak surface soils.

**Building advice:**
- Definitely do test pits and DCP testing
- Investigate slope stability seriously — DOGAMI's SLIDO database is essential
- Plan for drainage everywhere
- Consider over-excavation of upper clay layer for slab-on-grade
- Basements possible on flat sites with good drainage; risky on slopes

**Specific avoid signals:**
- Curved tree trunks (slope movement)
- Hummocky ground
- Springs or seeps
- Visible past slide deposits
- Steep slopes adjacent to building site

### Willamette Valley — Where Most Oregonians Live

**Geology:** A tectonically subsiding valley filled with alluvial sediments. Thick deposits from ancient Missoula Floods (catastrophic ice-age flooding). Recent stream and river deposits along major rivers.

**Typical soil profile:**
- Topsoil: 6-18 inches of agricultural-quality loam
- Subsoil: Variable
  - Higher elevations: well-drained loam
  - Lower elevations: clay-rich soils, often with seasonal wet conditions
  - Near rivers: mixed alluvial sands, silts, clays
- Older flood deposits at depth (often gravelly, sometimes clay-rich)

**Common challenges:**
- **Expansive clays** — Many Willamette Valley sites have moderately to highly expansive clays. The "Willamette silt" is famous for this.
- **Seasonal wet conditions** — Heavy clays don't drain. Many valley soils are saturated in winter and dry/cracked in summer.
- **Variable conditions** — Old streamcourses, point bars, oxbow lakes, all visible in soil profile, all different conditions.
- **Liquefaction potential** — Saturated alluvial sands can liquefy in major earthquakes (Cascadia subduction zone risk).

**Building advice:**
- Test pits and DCP essential
- Watch for expansive clay symptoms (look up the soil series at NRCS Web Soil Survey)
- Consider expansive-soil mitigation (lime stabilization, replacement, or specific foundation design)
- Drainage is critical — your design includes good drainage but verify the site permits it
- For a site with high expansive clay, a stiffened slab or pier-and-grade-beam might be better than the mat slab in this design's standard configuration
- Liquefaction unlikely to be major concern at most valley sites but worth checking DOGAMI maps

**The "Willamette silt" specifically:**
- Wind-blown silt deposited on the eastern valley benches
- Variable plasticity — can be expansive, can be collapsible
- Very widespread; many homes are built on it successfully
- Common surface soil; first 2-4 feet often need attention

### Cascade Foothills (West Slope)

**Geology:** Mostly basalt, andesite, and other volcanic rocks. Glacial deposits at higher elevations. Lots of weathered rock.

**Typical soil profile:**
- Topsoil: 6-18 inches
- Subsoil: 1-6 feet of weathered volcanic rock (clay to silt loam)
- Saprolite: variable depth
- Bedrock: basalt or andesite

**Common challenges:**
- **Hard rock surprises** — A test pit may show 3 feet of soil over solid rock; excavation hits bedrock unexpectedly
- **Variable depths** — Soil depth varies dramatically across short distances
- **Steep terrain** — Many sites are sloped; slope stability and drainage challenges
- **Springs** — Water tables in fractured bedrock create surface springs

**Building advice:**
- Multiple test pits to map bedrock surface
- Plan for excavation difficulty (rock breaking, blasting in extreme cases)
- Plan for drainage from up-slope sources

### High Cascades and Recent Volcanic Areas

**Geology:** Recent volcanic deposits — pumice, scoria, ash, lava flows, breccia.

**Typical soil profile:**
- Pumice (lightweight, highly porous volcanic rock fragments)
- Volcanic ash deposits (very fine, dust-like material)
- Lava flow surfaces or breccia (broken lava chunks)

**Common challenges:**
- **Pumice and ash are unique** — Lightweight, very porous, can be collapsible when wetted
- **Lava tubes** — Hollow voids in basalt flows (rare but real risk in central Oregon)
- **Frost is severe** at higher elevations
- **Cold climate issues** — Long building season, deep frost penetration

**Building advice:**
- Specific concerns about ash deposits — they may collapse if saturated, may need pre-wetting and compaction
- Investigate for lava tubes if in active volcanic areas
- Frost depth design carefully (4+ feet at higher elevations)

### Eastern Oregon (Basin and Range, Columbia Basin, Owyhee, Blue Mountains)

**Geology:** Predominantly basalt bedrock with thin to moderate soil cover. Often capped with loess (wind-blown silt) in the Columbia Basin region. Volcanic deposits in central and southern parts.

**Typical soil profile:**
- Loess: 2-30+ feet of fine wind-blown silt (Columbia Basin especially)
- OR thin soil over basalt bedrock (most other areas)
- Occasional alluvium in valleys

**Common challenges:**
- **Loess specifics** — Loess is collapsible when wetted. A site that's dry and stable may collapse if a downspout dumps water in the wrong place.
- **Basalt at shallow depth** — Excavation may require rock-breaking
- **Cold climate** — Deep frost (4-5 feet)
- **Dry climate** — Soil dries hard, may need wetting for compaction
- **Wind erosion** during construction

**Building advice:**
- Loess collapse mitigation: pre-wet and compact the site before construction
- Don't allow concentrated water near the foundation
- Bedrock is great bearing where it's at the surface; expensive to excavate where covered

### Reading the Oregon Soil Survey

The **NRCS Web Soil Survey** is a free online tool. Enter any Oregon address and you get:
- Soil series at that location (dozens of named series in Oregon)
- Soil texture
- Drainage class
- Shrink-swell potential
- Slope
- Erosion characteristics
- Limitations for "dwellings without basements" and "dwellings with basements"

This is the FIRST resource to check when evaluating any Oregon site. Free, comprehensive, professionally curated.

URL: websoilsurvey.nrcs.usda.gov

For example, looking up a typical Willamette Valley site might return:
- Soil: "Woodburn silt loam"
- Slope: 0-3%
- Shrink-swell: Moderate
- Drainage: Moderately well drained
- Limitations for dwellings with basements: Severe (wetness, shrink-swell)
- Limitations for dwellings without basements: Moderate (shrink-swell)

That's actionable information before you ever drive to the site.

---

## 14.16 Expansive Clay — The Deep Dive

**Plain language:** Expansive clay is the most common soil problem for Oregon residential construction, especially in the Willamette Valley. It's a clay that swells with moisture and shrinks when dry. The volume changes are enough to lift houses, crack foundations, and ruin slabs. Knowing how to identify it, evaluate it, and build on it (or around it) is essential.

### What Makes Clay Expansive

Clay particles are tiny flat plates. Some clay minerals (montmorillonite, smectite, bentonite) have a layered crystal structure with positively-charged metal ions sandwiched between negatively-charged silicate sheets. Water molecules slip into these layers, pushing them apart and expanding the crystal. The amount of expansion depends on the mineral type and the water available.

**Highly expansive clays** can change volume by 10-30% between dry and wet. A 4-foot-thick layer of expansive clay can heave 6-12 inches.

**Low expansive clays** (like kaolinite) change volume only slightly.

### Identifying Expansive Clay in the Field

**Visual clues:**
- Wide cracks in dry soil — patterns of polygonal cracks 1-3 inches wide are classic
- "Slickensides" in test pit walls — shiny, smooth surfaces from past expansion/contraction
- Color often dark gray-brown, dark red-brown, or black-brown
- Clay-rich appearance and feel

**Field tests:**
- **Ribbon test** (Section 14.3) — long ribbons (3+ inches) without breaking = high clay content; possibly expansive
- **Plasticity** — Take a moist clay ball, squeeze and roll. High plasticity = high clay content
- **Drying behavior** — Take a sample, let it dry, observe shrinkage. Expansive clays shrink visibly and crack

**Lab tests (definitive):**
- **Atterberg limits** — Plasticity Index (PI) > 25 indicates expansive potential
- **Free swell test** — Sample is dropped into water; the volume increase indicates expansion potential
- **Linear shrinkage** — Sample is dried and the shrinkage measured
- **Specific lab tests** for expansive index

For owner-builder field investigation, the visual clues plus the ribbon test plus the plasticity feel are usually enough to identify problem clay.

### Where Expansive Clay Is Found in Oregon

**Common in:**
- Willamette Valley, especially older flood deposits and lake bed sediments
- Coast Range, weathered marine clays
- Some Columbia Basin areas

**Less common in:**
- Recent volcanic areas
- Glacial outwash plains
- River bottom alluvium (more variable)

### How Expansive Clay Damages Houses

**Heave** (lifting):
- Saturated clay swells, pushing the foundation upward
- Differential heave (some areas more than others) cracks foundations
- Walls move; doors and windows stick
- Slab cracks in spider patterns

**Settlement** (sinking):
- When clay dries, it shrinks and the foundation sinks
- Foundation cracks, walls separate

**Lateral pressure**:
- Wet clay against basement walls can exert tremendous lateral pressure
- Walls bow inward, eventually crack

**The cycle**:
- Expansive clay swells in winter (wet), shrinks in summer (dry)
- Annual cycle of foundation movement
- Cumulative damage over years

### Why Expansive Clay Is Worse Some Places Than Others

**Climate effects:**
- Areas with strong wet/dry seasonal cycle = worst (summer dry then winter wet repeatedly)
- Areas with consistently wet climate = less of a problem (clay stays expanded)
- Areas with consistently dry climate = less of a problem (clay stays contracted)
- Pacific Northwest (Oregon Willamette Valley specifically) = worst case scenario climatically — 4-month dry summer followed by wet winter

**Site effects:**
- Trees nearby — trees dry the soil under them; their removal can rewet and trigger expansion
- Drainage — concentrated water (downspouts, leaks) creates localized wet spots
- Foundation type — slab-on-grade more vulnerable than deep foundations
- Construction season — building during dry season locks in dry soil; subsequent wetting causes maximum expansion

### Building on Expansive Clay — Strategies for Slab-on-Grade

When you can't avoid building on expansive clay, multiple strategies exist:

**Strategy 1 — Over-excavation and replacement:**

Standard approach. Remove the upper 3-5 feet of expansive clay. Replace with non-expansive engineered fill (clean sand, gravel, or crushed rock).

```
[ ] Identify the depth of "active" expansive clay layer
    - Typically affected to 3-5 ft depth in Oregon climate
    - Below this, moisture is more stable
[ ] Excavate to that depth across the entire building footprint
[ ] Extend at least 3 feet beyond the foundation perimeter
[ ] Backfill with non-expansive engineered fill
[ ] Compact in lifts (Section 14.11)
[ ] Build on the engineered fill
```

This is the most reliable approach. The building sits on stable engineered material that doesn't change volume.

**Cost:** Excavation and replacement of upper 4 feet over a 3,000 sqft building = ~$15,000-$30,000.

**Strategy 2 — Lime stabilization:**

Mix lime into the clay to chemically reduce its expansive behavior.

```
[ ] Test the soil to confirm it responds to lime
[ ] Specialty contractor mixes 4-7% lime into upper 18-24 inches
[ ] Compact, allow to cure
[ ] Build on stabilized soil
```

**Cost:** $15,000-$40,000 depending on area.

**Strategy 3 — Stiffened slab foundation:**

Build a slab so stiff that it bridges over the differential heave. Common in Texas and other expansive-soil regions.

- **Post-tensioned slab** — Cables under tension throughout the slab. Very stiff. Cracks reduced.
- **Beam-and-slab** — Reinforced beams under the slab in a grid pattern create a deep beam structure.

For this design's mat foundation, you can incorporate stiffener beams in a grid pattern, effectively creating a beam-and-slab system. Engineering required.

**Strategy 4 — Drained, isolated foundation:**

Surround the foundation with a moisture-control system to keep the soil moisture content as uniform as possible.

- Vapor barrier on the OUTSIDE of the foundation walls extending horizontally several feet from the foundation
- Drainage system to remove excess water
- No trees within 1 distance of foundation depth (a 10-foot deep foundation = no trees within 10 feet)
- Limited landscape watering near the foundation

**Strategy 5 — Pier-and-grade-beam foundation:**

Lift the structure off the expansive soil entirely.

- Drilled piers extend through the active expansive clay zone to firmer soil below
- Reinforced concrete grade beam connects the piers
- Building constructed on the grade beam
- A void space (or compressible material) under the grade beam allows clay to swell upward without lifting the building

**Cost:** $30,000-$60,000.

### Building on Expansive Clay — Strategies for Basement

A basement on expansive clay is harder than slab-on-grade because the basement walls are exposed to the full depth of expansive soil pressure.

**Strategy 1 — Reinforced basement walls designed for high lateral pressure:**

The structural design accounts for clay pressure (much higher than typical granular soil).

- Walls poured thicker (10-12 inches typical instead of 8)
- Heavy reinforcement
- Continuous bond beams

**Strategy 2 — Drainage to limit moisture variation:**

The most important measure for basement walls.

- Continuous gravel envelope outside walls
- Drainage mat against the walls
- Perimeter drain at the footing
- Daylight or pumped outlet
- Grade slopes away from foundation

**Strategy 3 — Insulation to limit thermal-driven moisture migration:**

Continuous insulation reduces the seasonal temperature swing in the soil adjacent to the foundation, which reduces moisture migration cycles.

**Strategy 4 — Avoid backfilling with native expansive clay:**

The first 12-24 inches of backfill against the foundation should be non-expansive engineered fill. Native expansive clay can be used higher up.

**Strategy 5 — Pre-treat the wall surface:**

Some installations include a slip-plane treatment on the exterior wall surface — a smooth, low-friction coating that allows the clay to slide against the wall as it expands, rather than transferring full lateral force.

### Acceptance Criteria — When Is Expansive Clay Acceptable?

In some areas of the Willamette Valley, virtually every building site has some expansive clay. Total avoidance isn't always practical.

**Acceptable conditions:**
- Plasticity Index 25-50 (moderate expansive)
- Active layer less than 5 feet deep
- Drainage works
- Landscape doesn't impose extreme moisture cycles
- Standard foundation with minor enhancements is adequate

**Marginal conditions:**
- Plasticity Index 50-75 (high expansive)
- Active layer 5-8 feet deep
- Drainage moderate
- Need for over-excavation and replacement OR specific foundation design

**Unacceptable conditions (find another site):**
- Plasticity Index >75 (very high expansive)
- Active layer >8 feet deep
- No drainage path
- Site already showing damage to existing structures

### Indications of Trouble in Existing Buildings

If you're evaluating a site with existing structures or near existing structures showing damage, check for these signs of expansive soil problems:

- **Stair-step cracks in masonry walls** (45-degree cracks)
- **Doors that won't close in winter or summer** but work in the other season
- **Cracks in basement floors** (linear or in a spider pattern)
- **Drywall cracks at corners** of doors and windows
- **Patio slabs separated from house** in a tilted way
- **Sidewalks heaved or sunken** along the lot

Visible damage on neighbors' properties is your warning. A new build won't be magically immune.

---

## 14.17 Frost Protection — A Specific Subset of Ground Prep

**Plain language:** When water in the soil freezes, it expands. If the freezing zone reaches under your foundation, ice forming in the soil pushes the foundation upward — sometimes evenly (lifting the whole building), sometimes unevenly (cracking it). Frost protection means keeping the freeze line below the foundation, OR keeping the soil dry enough that there's no water to freeze.

### How Frost Heave Works

The mechanism:

1. Cold weather drives a "freezing front" downward into the soil
2. As soil freezes, free water becomes ice (volume increase ~9%)
3. Frost-susceptible soils ALSO have a second mechanism: capillary water continues to feed the freezing front, building thick ice lenses that lift the soil dramatically more than the simple 9% expansion

The key variables:
- **Freezing depth** — how deep does the soil freeze in winter?
- **Soil type** — silty soils form ice lenses (frost-susceptible); clean gravels and sands don't
- **Water availability** — without water, no ice forms; capillary water rising from below makes the worst heave

### Frost Depth in Oregon

Oregon's frost depths vary substantially:

| Region | Typical Frost Depth | Design Frost Depth (Code) |
|---|---|---|
| Coastal | 6-12 inches | 12 inches |
| Willamette Valley | 12-18 inches | 18 inches |
| Cascade slopes (lower) | 18-24 inches | 24 inches |
| Cascade slopes (higher) | 24-36 inches | 36 inches |
| Eastern Oregon (lower) | 24-36 inches | 36 inches |
| Eastern Oregon (higher) | 36-48 inches | 48 inches |
| Mountain locations | 48-60 inches | 60 inches |

**Always verify the design frost depth with the local building department** — they have the official number for the jurisdiction.

### Frost-Susceptible Soils

Frost susceptibility (the tendency to form ice lenses) depends on soil type:

**Most frost-susceptible:**
- Silt and silty soils (CLASSIC frost-heave material)
- Fine sand with silt fines
- Glacial till

**Moderately frost-susceptible:**
- Medium sand
- Sandy clay
- Clay

**Not frost-susceptible:**
- Clean gravel
- Coarse sand
- Crushed rock with no fines

The reason: frost lenses need to draw capillary water up. Coarse soils don't have capillary action. Silty soils have lots of capillary action and are the worst.

### Strategies for Frost Protection

**Strategy 1 — Foundations Below Frost Line (Conventional):**

Standard residential approach: bury the foundation footing below the design frost depth.

```
[ ] Determine design frost depth for jurisdiction
[ ] Foundation footing extends to that depth or deeper
[ ] Frost can heave the soil ABOVE the footing without affecting the footing
[ ] Building is structurally protected
```

For this design:
- Mat foundation: the entire mat is at one depth (basement floor level for a basement build, or near grade for a slab build)
- For a slab build, the edges of the mat extend below grade for frost protection
- For a basement build, the foundation is automatically below frost

**Strategy 2 — Frost-Protected Shallow Foundation (FPSF):**

Modern technique: instead of digging deep, insulate the soil so it doesn't freeze under the foundation.

```
[ ] Foundation placed at shallow depth (12-18 inches typical)
[ ] Rigid foam insulation extends horizontally outward from the foundation 2-4 feet
[ ] Insulation keeps geothermal warmth in the soil under the foundation
[ ] Soil under insulation doesn't freeze even when air temperature does
[ ] Building is protected without deep excavation
```

This design uses FPSF principles in conjunction with mat foundation. The under-slab insulation extends out under the perimeter to protect the slab edge.

**FPSF design parameters (from ASCE 32 / NAHB Frost Protected Shallow Foundations Guide):**
- Air-freezing index for the location (degree-days below freezing)
- Soil thermal conductivity
- Insulation thickness and placement
- Building's heat input (for heated structures, helps protect the soil)

For Oregon FPSF:
- Western Oregon: minimal insulation extension required (mild climate)
- Eastern Oregon (cold): 2-4 ft horizontal insulation extension
- Cascade Mountains: 4-6 ft horizontal insulation extension
- Foundation insulation under the slab is essential regardless

**Strategy 3 — Drainage to Eliminate Water:**

If the soil can't get wet, it can't form ice lenses.

```
[ ] Continuous drainage under and around the foundation
[ ] No standing water, no perched water tables
[ ] Capillary break (clean coarse rock, no fines) under any slab
[ ] Slope grade away from foundation
```

This is what every well-designed foundation does anyway. Combined with Strategy 1 or 2, frost is reduced or eliminated.

**Strategy 4 — Replace Frost-Susceptible Soil:**

If the native soil is silty (worst frost-susceptible), replace it with non-frost-susceptible material under the foundation.

```
[ ] Excavate native silty soil from under and around foundation footprint
[ ] Replace with clean coarse sand or gravel
[ ] No water can rise through this fill (no capillary action)
[ ] Building sits on stable, non-heaving soil
```

This is essentially the same as the over-excavation and replacement strategy, motivated by frost concerns rather than just bearing.

### Frost Protection in This Design

This design's frost protection strategy combines all four approaches:

1. **Foundation depth** — Basement build: foundation is below frost (8+ ft below grade). Slab build: thickened mat edge extends below frost depth.

2. **FPSF principles** — Under-slab insulation extends to and slightly past foundation perimeter, providing horizontal insulation.

3. **Drainage** — The full drainage system (perimeter drain, gravel envelope, slope grade away) eliminates water near the foundation.

4. **Material selection** — Engineered base course (clean crushed rock with no fines) under the slab is non-frost-susceptible.

**Result:** The foundation itself is always below frost depth. The soil under the foundation is non-frost-susceptible. Even at extreme cold, no frost heave is possible.

### Frost Protection During Construction

A subtle issue: if you pour foundations during winter and stop work for the season, frost can damage uncompleted work.

```
[ ] If construction stops with foundation exposed:
    - Cover with hay bales or insulation
    - Or pour the slab to enclose the basement
    - Or delay critical pours until spring
[ ] If pouring during cold weather:
    - Use admixtures that protect against freezing
    - Heat the concrete and the work area
    - Insulating blankets after pour
[ ] Don't pour onto frozen ground (very common cause of damage)
```

---

## 14.18 Drainage — Where the Water Goes

**Plain language:** Almost every soil problem has water at its core. Expansive clay swells with water. Frost heave needs water to make ice. Soft soil is soft because of water. Slope failures happen when water destabilizes the slope. Liquefaction needs saturated sand. Settlement happens as water squeezes out of clay. Get the water under control and you've solved most problems before they start.

### The Site Drainage Hierarchy

Multiple levels of water control work together:

**Level 1 — Macro-scale drainage (the site):**
- The land slopes such that water flows AWAY from the building site
- Upslope water is intercepted and redirected
- Wet areas drained with surface ditches or French drains

**Level 2 — Building-perimeter drainage:**
- Grade slopes away from foundation
- Surface water from the roof discharges to gutters and downspouts
- Downspouts extend at least 5 feet from the foundation
- Below-grade perimeter drain (drain tile) collects subsurface water

**Level 3 — Below-foundation drainage:**
- Capillary break under the slab (clean coarse rock with no fines)
- Vapor barrier on top of capillary break
- Sometimes a sub-slab drainage system (especially if water table is borderline)

**Level 4 — Surface-of-soil drainage:**
- Gutters and downspouts handle roof water
- Surface drainage handles overland flow
- Patio and driveway slopes shed water

**Level 5 — Groundwater control:**
- Pumping if necessary
- Curtain drains intercepting upslope groundwater
- Foundation drainage system as backup

### Site Drainage Assessment

Before construction:

```
[ ] Site survey including topography (1-foot contours preferred)
[ ] Identify drainage patterns from upslope sources
[ ] Identify low points and drainage paths leaving the site
[ ] Check upstream water sources (springs, ditches, neighbor runoff)
[ ] Plan to keep water moving past the site, not stopped at it

GRADE PLANNING:
[ ] Building site at a high point of the lot OR
[ ] Building site graded to be a high point relative to immediate surroundings
[ ] Drainage path away from foundation in all directions
[ ] No "punchbowl" conditions where water collects against the building

INTERCEPT UPSLOPE WATER:
[ ] If site is downslope of an upslope source:
    - French drain or curtain drain along the upslope side
    - Pipe or swale to redirect water around the building
    - Don't try to "stop" upslope water; redirect it
```

### The Building Perimeter Drainage System

For this design's basement (described in detail in Section 4):

```
COMPONENTS:

1. Perimeter drain tile (4-inch perforated PVC)
   - Located at the footing elevation
   - Slopes 1/4 in per foot toward outlet
   - Wrapped in filter fabric
   - Surrounded by 12+ inches of drainage gravel

2. Drainage mat against waterproofing membrane
   - Continuous from footing to grade
   - Channels water down to perimeter drain
   - Cosella-Dörken DELTA-MS or equivalent

3. Filter fabric over gravel before backfill
   - Prevents soil fines from clogging gravel envelope

4. Backfill (granular for first 12-24 inches against wall, native above)

5. Final grade slopes away from foundation 6 inches in 10 feet minimum

6. Outlet:
   - Daylight at low point of the property OR
   - Sump pit with battery-backup pump OR
   - Combined approach
```

For slab-on-grade (no basement):

```
COMPONENTS:

1. Capillary break under slab (4 inches of 1+ inch crushed rock with no fines)

2. Vapor barrier above capillary break (10-15 mil polyethylene)

3. Foundation perimeter drain (optional but recommended)
   - At the elevation of the slab base
   - Drains to daylight

4. Surface drainage at grade
   - Slope grade away from foundation
   - Gutters and downspouts at roof
   - Downspout extensions or splashpads

5. Subsurface drainage if needed (high water table sites)
   - French drain perimeter
   - Or full sub-slab drainage system
```

### Roof Drainage Specifically

Roof water is a HUGE volume that lands at the foundation if not controlled:

For a 3,000 sqft roof, a 1-inch rain event = 1,870 gallons of water. Multiply by Oregon's rainfall, and we're talking tens of thousands of gallons per year landing right next to the building.

```
[ ] Gutters at every roof edge
[ ] Downspouts at corners
[ ] Downspouts discharge AT LEAST 5 feet from the foundation
    - Splashpads
    - Underground pipes carrying water to a drainage point
    - Rainwater cistern (this design's strategy)
[ ] No downspout dumps water against the foundation
[ ] In freezing climates, downspout discharge points must not freeze and back up
```

### Drainage to Daylight vs. Sumps

The ideal drainage outlet is "daylight" — a point on the surface lower than the drain inlet, where water flows out by gravity.

**Daylight drainage advantages:**
- No moving parts
- Works during power outages
- Extremely reliable
- Inexpensive

**Daylight drainage requirements:**
- Adequate slope from foundation drain to daylight outlet
- Outlet protected from clogging (rodent screen, filter fabric)
- Outlet not in a place where the discharged water creates a problem

**When daylight isn't possible:**
- Site is at a low point with no lower elevation accessible
- Outlet would discharge onto neighboring property (need easement)
- Distance is too far for practical pipe runs

**Sump pump systems:**
- Sump pit at the low point of the foundation drain
- Submersible pump activated by water level
- Pumps water to the surface or to a discharge point
- Battery backup pump for power outages
- Generator for extended outages

**Sump pump reliability requirements:**
- Primary AC pump
- Secondary battery-backup pump (different switch type so both don't fail simultaneously)
- Monitoring with alarm
- Annual testing
- Discharge pipe with check valve
- Discharge to a place where water can dissipate

A reliable sump pump system can run a basement on a high-water-table site, but it's a permanent operational dependency. One failure during the wrong storm can flood a basement.

---

## 14.19 Integration with the Rest of the Design

**Plain language:** Sections 14 (this section), 4 (Structural Design), and 5 (Envelope and Thermal) work together. The foundation rests on the soil; the soil's quality determines the foundation's design; the foundation determines the envelope's interface with the ground. This section makes the integration explicit.

### Soil → Foundation Decisions

The site investigation results affect the foundation design:

| Soil Condition | Foundation Adaptation |
|---|---|
| Excellent (>3,000 psf bearing, uniform) | Standard mat foundation as designed in Section 4 |
| Good (2,000-3,000 psf bearing, mostly uniform) | Standard mat with verification |
| Marginal (1,500-2,000 psf, some variation) | Wider mat, additional reinforcement, possibly soil improvement |
| Poor (<1,500 psf, variable) | Soil improvement required, OR helical piers + grade beam, OR deeper foundation |
| Expansive clay | Over-excavation, OR stiffened slab, OR pier-and-grade-beam |
| High water table | Different foundation type (slab-on-grade preferred), OR major waterproofing investment |
| Frost-susceptible | Engineered fill replacement, OR FPSF design |
| Liquefiable | Soil improvement (densification), OR deep foundations |

### Foundation → Envelope Decisions

The foundation type affects how the envelope interfaces with the ground:

**Mat foundation with basement (this design's primary):**
- Continuous insulation layer below entire slab
- Continuous waterproofing on basement walls
- Drainage system at footing
- Insulation on basement walls (interior or exterior)

**Mat foundation, slab-on-grade (no basement):**
- Insulation under slab (with FPSF perimeter extension)
- Slab-edge insulation
- No waterproofing required (above water table)
- Drainage at slab edge optional

**Pier-and-grade-beam foundation:**
- Insulation in the floor structure (rigid foam under or between joists)
- Skirting at the perimeter to reduce wind washing
- Different envelope intersection at grade

### Site → Building Layout

The site characteristics may influence the building footprint and orientation:

- **Solar access:** Building oriented with good solar gain on southern face
- **Slope:** Building set into slope to minimize cut and fill, OR placed on level area
- **Drainage:** Building placed at high point of buildable area
- **Access:** Building location considers driveway approach, fire access
- **Vegetation:** Existing trees considered (shade benefit, root system risk)
- **Views:** Where possible, building positioned for views without compromising other criteria

---

## 14.20 The Site Decision Framework — Go / No-Go

**Plain language:** After all the investigation, you need to make a decision: build here or look elsewhere. Here's a framework for making that decision based on the data you've collected.

### Site Acceptance Levels

**LEVEL A — Excellent Site (Build with Confidence):**
- Bearing capacity 2,500+ psf throughout
- Soil uniform across building footprint
- Water table 15+ feet below grade
- No expansive clay (or low PI)
- No frost issues
- No slope stability concerns
- Drainage path clear
- Frost depth straightforward
- Predicted construction: standard mat foundation as designed

**LEVEL B — Good Site (Standard Build with Verification):**
- Bearing capacity 1,500-2,500 psf typical
- Some variation in soil
- Water table 10-15 feet below grade
- Possibly moderate expansive clay
- Drainage requires attention but feasible
- Predicted construction: standard mat foundation, some soil prep, careful drainage

**LEVEL C — Challenging Site (Engineered Solution Required):**
- Bearing capacity 1,000-1,500 psf typical
- Significant variation
- Water table 6-10 feet below grade
- Notable expansive clay or other soil issue
- Drainage requires major attention
- Predicted construction: soil improvement, possible foundation modifications, geotechnical and structural engineering input

**LEVEL D — Difficult Site (Consider Carefully):**
- Bearing capacity 500-1,000 psf typical
- Major soil issues (expansive, soft, organic)
- Water table 3-6 feet below grade
- Site-wide problems
- Predicted construction: deep foundations, major soil improvement, expensive engineering, premium build cost

**LEVEL E — Don't Build:**
- Bearing capacity <500 psf
- Active landslide
- Water table at or near surface
- Severe expansive clay
- Very organic soils
- Predicted construction: not economical for residential

### The Decision Process

```
DATA COLLECTION COMPLETE:
[ ] DCP profiles documented
[ ] Test pits described and photographed
[ ] Hand auger samples identified
[ ] Soil maps consulted (NRCS Web Soil Survey)
[ ] Hazard maps consulted (DOGAMI SLIDO, FEMA flood, liquefaction)
[ ] Water table depth determined
[ ] Drainage assessed

ANALYSIS:
[ ] Site classified Level A, B, C, D, or E based on criteria above

DECISION:
[ ] Level A or B: Proceed with confidence at standard cost
[ ] Level C: Engage geotechnical engineer for site-specific analysis
   - Cost-benefit: budget the engineering and improvements
   - Decide: proceed with the documented strategy, or look elsewhere
[ ] Level D: Strongly consider alternative sites
   - Get formal cost estimate for the engineering and remediation
   - Compare to additional cost of finding a better site
   - Document the decision rationale
[ ] Level E: Do not build — find a different site
```

### Documenting the Decision

Whatever you decide, document the rationale:

```
SITE DECISION RECORD:

Property: __________________________________________
Date of decision: ___________
Decision maker(s): ___________________________________

Site classification: [ ] Level A  [ ] Level B  [ ] Level C  [ ] Level D  [ ] Level E

Investigation data summary:
- DCP results: ____________________________________
- Test pit findings: ______________________________
- Water table: ___ feet below grade
- Soil type(s): ____________________________________
- Major concerns: __________________________________

Decision: [ ] Proceed  [ ] Decline  [ ] Conditional

If proceeding:
- Foundation modifications: _________________________
- Soil improvement plan: ____________________________
- Engineering input required: _______________________
- Estimated additional cost: $______________________

If declining:
- Reasons: _________________________________________
- Alternative sites being considered: _______________

Filed in project binder: [ ] Yes
```

This record protects you (and informs future builders) — a thoughtful, documented site decision is part of the professional foundation of the project.

---

## 14.21 Summary — The Twelve Principles of Ground Preparation

A condensed reference for everything in this section:

**1. Investigate before you commit.** Use DCP, test pits, hand auger, NRCS Web Soil Survey, DOGAMI maps. Spend $1,000-$5,000 to investigate a $300,000+ build.

**2. Multiple data sources beat single tests.** A DCP test, a test pit, and a hand auger sample together tell more than any single test alone.

**3. Soil varies — test multiple locations.** Minimum 3 DCP locations within the building footprint. More if the site is variable.

**4. Visit the site in different seasons.** Wet season reveals drainage and water table issues that dry season hides.

**5. Topsoil never bears the building.** Strip topsoil before any structural decision. The subsoil is what matters.

**6. Bearing capacity is the first metric.** A building that doesn't have soil to support it doesn't have a foundation. 2,000+ psf for residential, 2,500+ for masonry/concrete.

**7. Water control is the second metric.** Drainage, water table, surface flow, capillary water — get water under control or no foundation strategy works.

**8. Compaction matters and must be verified.** Place fill in proper lifts, at proper moisture, with proper equipment. Verify with DCP after compaction.

**9. Expansive clay is a major Oregon issue.** Especially Willamette Valley. Identify it (visual, ribbon test, Atterberg limits if formal). Mitigate it (over-excavation, stabilization, foundation design).

**10. The DCP is the owner-builder's superpower.** Affordable, portable, accurate, repeatable. Learn to use it correctly. Make it part of your verification at every soil decision.

**11. Hire a geotechnical engineer when in doubt.** $5,000-$15,000 of professional analysis can prevent $100,000 of remediation. Especially for Level C/D sites.

**12. Document everything.** DCP profiles, test pit photos, sample bags, decision records. The site investigation file is part of the home's permanent record. Future you will need it.

---

## 14.22 Quick-Reference Decision Tree

For when you're standing on a piece of property trying to decide:

```
START

Is the surface obviously wet, mucky, or showing standing water in dry weather?
├── YES → Water table or drainage problem; investigate carefully or pass
└── NO → Continue

Are there visible cracks in the soil during dry weather (3+ inch wide)?
├── YES → Expansive clay; investigate further before committing
└── NO → Continue

Are there signs of past slope movement (curved trees, hummocky ground, scarps)?
├── YES → Landslide-prone; pass unless professionally assessed
└── NO → Continue

Run a quick DCP (3-5 tests across building footprint).

Average DCP penetration in the depth range of interest (typically 2-6 feet):
├── PI < 5 mm/blow throughout → Excellent (Level A); proceed
├── PI 5-10 mm/blow throughout → Good (Level A/B); proceed
├── PI 10-20 mm/blow throughout → Marginal (Level B/C); investigate further
├── PI 20-40 mm/blow → Poor (Level C/D); soil improvement needed
└── PI > 40 mm/blow → Very poor (Level D/E); strongly consider passing

Is there a ground water observation in test pits within 8 ft of surface?
├── YES → Water table issue; expensive to handle
└── NO → Continue

Is the soil consistent across the building footprint (DCP profiles similar)?
├── YES → Single design strategy works
└── NO → Variable conditions; need to engineer for the worst case

Final decision:
- All checks favorable: Proceed with confidence
- Minor issues: Engineer the solution; proceed with documentation
- Major issues: Hire geotechnical engineer for formal assessment
- Multiple major issues: Consider alternative sites
```

---

*End of Section 14 — Ground Preparation and Soil Testing*

*This is the longest section in this document because it's the most consequential. Get this right and everything else has a chance. Get this wrong and the rest of the build is fighting against the soil for the building's life. Reread this section before site selection. Reread it before excavation. Reread it before any concrete is poured. The cost of attention here is small; the cost of inattention is enormous.*
