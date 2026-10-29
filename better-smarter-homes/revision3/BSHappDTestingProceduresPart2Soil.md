# Appendix D — Testing Procedures

## Part 2 — Soil and Geotechnical Testing

This part covers the field tests for evaluating soil. The Ground Prep and Foundation Risk chapter explains the theory and the why; this part is the manual you bring to the site.

The tests here are designed for owner-builder use with affordable equipment, producing data that's good enough for residential decisions. Where lab work or specialty equipment is required, that's noted explicitly.

The tests are organized in the order you'd typically run them on a new site:

- **D.9 — Field Soil Identification** (visual and tactile, no equipment)
- **D.10 — Ribbon Test** (clay content)
- **D.11 — Jar Test** (composition by sedimentation)
- **D.12 — Hand Auger Sampling** (soil identification at depth)
- **D.13 — Test Pit Investigation** (full profile inspection)
- **D.14 — Pocket Penetrometer Test** (surface bearing capacity)
- **D.15 — Dynamic Cone Penetrometer (DCP) Test** (the master procedure)
- **D.16 — Compaction Verification** (after placing engineered fill)
- **D.17 — Settlement Plate Monitoring** (for pre-loading operations)
- **D.18 — Integrated Site Investigation Workflow** (all the above, in sequence)
- **D.19 — Atterberg Limits** (definitive clay characterization)
- **D.20 — Proctor Test** (compaction specification)

---

## D.9 Field Soil Identification

**Purpose:**

Identifying soil type is the first question every other geotechnical decision depends on. Is this clay or silt? Sand or gravel? Organic or mineral? You can answer most of these questions in the field without any equipment, just by looking and feeling. This procedure is the systematic method.

**Plain language:** Pick up a handful of soil. Look at it, feel it, smell it, and run a few simple manipulations to figure out what kind of soil you have.

**When to perform:**

- At every test pit, in every layer
- At every hand-auger depth
- Anywhere soil identification is needed (suspect material, layered deposits, etc.)

**Standards:** ASTM D2488 — Standard Practice for Description and Identification of Soils (Visual-Manual Procedure)

**Equipment:**

```
[ ] Sample bag (resealable plastic) for representative sample
[ ] Knife or trowel for handling
[ ] Spray bottle of water (for moistening dry samples)
[ ] Field notebook
[ ] Munsell soil color chart (optional — $200, useful for serious documentation)
[ ] Camera
[ ] Magnifying glass or hand lens (10x) — $20
```

Total kit cost: $20-$300 depending on rigor.

**Safety considerations:**

- Wear gloves if soil contamination is possible (industrial sites)
- No identifying organic-rich soil by taste (yes, that's a thing — don't do it)
- Wash hands after sample handling

**Pre-test setup:**

```
[ ] Strip topsoil if testing subsoil
[ ] Have notebook ready for recording observations
[ ] Document location with photo before disturbing soil
```

**Procedure:**

```
STEP 1 — VISUAL OBSERVATION

Note these for the sample:

[ ] COLOR
   - Use Munsell soil color chart if you have one
   - Otherwise, describe in plain terms (dark brown, light gray, etc.)
   - Note any color variation or layering
   - Note mottling (orange/red spots) or gleying (blue-gray)

[ ] PARTICLE SIZE (largest particles)
   - Boulders (>12 inches) — describe and note
   - Cobbles (3-12 inches) — describe and note
   - Gravel (1/4 to 3 inches) — visible easily
   - Sand (visible grains, 1/16 to 1/4 inch) — feel granular
   - Fines (silt and clay, smaller than #200 sieve, ~0.003 inches)

[ ] DOMINANT FRACTION
   - Estimate the percentage of fines vs. coarser particles
   - More than 50% fines = silt or clay (depending on plasticity)
   - More than 50% sand or gravel = granular

[ ] STRUCTURE
   - Massive (no visible structure)
   - Layered (visible horizontal bedding)
   - Blocky (breaks into chunks along regular surfaces)
   - Granular (loose grains)

[ ] ORGANIC CONTENT
   - Visible roots, plant fibers
   - Dark color (organic material gives dark color)
   - Wood, leaf fragments

STEP 2 — TACTILE TEST

Take a small handful of moist soil:

[ ] FEEL THE GRITTINESS
   - Sand: very gritty, can feel individual grains
   - Silt: slightly gritty, like flour rubbed between fingers
   - Clay: smooth, slick, sticky

[ ] SQUEEZE BETWEEN FINGERS
   - If it crumbles immediately: low cohesion, sand or silty sand
   - If it holds shape but breaks easily: silt or low-clay soil
   - If it deforms plastically and holds shape: clay-rich

STEP 3 — DRY STRENGTH TEST

Allow a small lump (pea-sized) to dry, then test:

[ ] Try to crush between thumb and forefinger
   - Crumbles easily: silt or sand
   - Some resistance, breaks into smaller pieces: silty clay
   - Hard, can't crush: clay (often expansive)

STEP 4 — SHAKE TEST (FOR SILT VS. CLAY)

Take a moist ball of fines (silt or clay):

[ ] Shake it vigorously back and forth in your palm
   - Water comes to surface (shiny appearance), disappears when squeezed: SILT
   - No visible water reaction: CLAY

This is the key distinguisher between silt and clay when they look similar.

STEP 5 — SMELL TEST

[ ] Sniff the sample
   - Earthy, mineral smell: normal mineral soil
   - Compost smell: organic content
   - Rotten egg / sulfur smell: anaerobic, saturated, possibly old septic or wetland

STEP 6 — RIBBON TEST (IF CLAY SUSPECTED)

See D.10 for full procedure.

STEP 7 — RECORD

Document everything in the field notebook with:
- Location coordinates or stake reference
- Depth of sample
- All observations from steps 1-5
- Photo if useful
- Sample bagged and labeled if keeping
```

**Data recording:**

```
SOIL FIELD IDENTIFICATION RECORD

Date: __________  Time: __________
Location: ____________________________________
Depth of sample: ______ to ______ inches
Source: [ ] Test pit  [ ] Hand auger  [ ] Other: __________

Color: ____________________________________
Color variation/mottling: __________________________
Largest particles: __________________________
Dominant fraction: __________________________
Structure: __________________________
Organic content: __________________________

Tactile (gritty/smooth/sticky): __________________________
Dry strength (high/medium/low): __________________________
Shake test result (silt/clay): __________________________
Smell: __________________________

Ribbon test (length achievable): ______ inches  [ ] Couldn't form
USCS classification (estimated): ______ (e.g., CL, ML, SC)

Notes: ____________________________________
Sample bag #: __________
Photos: __________
Operator: ____________________________________
```

**Pass/fail criteria:**

This isn't a pass/fail test — it's an identification test. The output is the soil classification, which then feeds into bearing capacity decisions, expansion potential evaluation, and other tests.

**Common errors:**

```
ERROR: Identifying topsoil as the building soil
→ Topsoil is always different (organic, looser) from subsoil
→ Fix: Strip topsoil first, identify subsoil

ERROR: Skipping the shake test
→ Silt and clay often confused
→ Fix: Always shake test moist fine-grained soils

ERROR: Testing dry sample for tactile properties
→ Dry samples behave differently
→ Fix: Add water to optimum moisture (damp ball that holds shape)

ERROR: Single sample assumed representative
→ Soil varies; one sample isn't a profile
→ Fix: Sample at multiple depths and locations

ERROR: Subjective comparisons across testers
→ "Smooth" means different things to different people
→ Fix: Calibrate yourself by testing known samples (clay from a pottery store, sand from a quarry); use consistent technique
```

**What to do based on the identification:**

- **Sand or gravel:** Generally good bearing capacity; investigate further with DCP
- **Silt:** Frost-susceptible; investigate drainage
- **Clay:** Could be expansive; do ribbon test (D.10) and consider lab Atterberg limits if high plasticity
- **Organic:** Must remove and replace; do not build on organic soil

---

## D.10 Ribbon Test (Clay Plasticity)

**Purpose:**

The ribbon test is the most useful field test for identifying clay plasticity — and therefore expansive potential. A high-plasticity clay can form long, intact ribbons; a silt or sand cannot. Length of ribbon achievable correlates with Plasticity Index (PI), which correlates with expansive behavior.

**Plain language:** Take moist soil, roll it into a long thread, see how long you can make it before it breaks. Long thread = high clay content.

**When to perform:**

- At every fine-grained soil sample (silt or clay)
- When expansive clay is suspected
- During Field Soil Identification (D.9), Step 6

**Standards:** Field test, not formally standardized; correlates to Atterberg limits per ASTM D4318.

**Equipment:**

```
[ ] Soil sample (moist, palm-sized)
[ ] Spray bottle of water (for adjusting moisture)
[ ] Flat surface or palm
[ ] Tape measure (optional, for documentation)
```

Cost: $0-$10.

**Procedure:**

```
STEP 1 — PREPARE SAMPLE

[ ] Remove any large particles (gravel, organic matter)
[ ] Mix sample to uniform consistency
[ ] Verify moisture content:
   - Squeeze a handful: should hold a ball that breaks under light pressure
   - Too dry: add water with spray bottle, knead
   - Too wet: knead and let evaporate slightly

STEP 2 — KNEAD

[ ] Knead the sample thoroughly between palms
   - Goal: uniform consistency, no air pockets
   - Continue until sample is plastic and workable

STEP 3 — ROLL THE THREAD

[ ] Take a small portion (marble-sized)
[ ] Roll between palms or between hand and flat surface
[ ] Reduce diameter to approximately 1/8 inch (3 mm)
[ ] If thread breaks before reaching 1/8 inch:
   - Sample is low-plasticity (silt or sand-dominant)
   - Note the breaking diameter

STEP 4 — EXTEND THE THREAD

[ ] Continue rolling the 1/8 inch thread
[ ] Try to extend it to 3+ inches without breaking
[ ] Observe at what length the thread breaks

STEP 5 — INTERPRET

LENGTH ACHIEVABLE → INTERPRETATION:

[ ] Cannot form thread at all → SAND or VERY SILTY (low fines)
[ ] Thread breaks at < 1 inch → SILTY SOIL (low plasticity)
[ ] Thread breaks at 1-3 inches → CLAYEY SILT or LOW PLASTICITY CLAY (CL)
[ ] Thread reaches 3+ inches → MEDIUM TO HIGH PLASTICITY CLAY (CL or CH)
[ ] Thread can be folded into ribbon held flat → HIGH PLASTICITY CLAY (CH)
[ ] Long ribbon, sticky, won't break → VERY HIGH PLASTICITY CLAY (potentially highly expansive)

STEP 6 — RECORD

Note in field notebook:
- Maximum length of intact thread/ribbon
- Behavior observed
- Estimated USCS classification
- Photograph if interesting
```

**Pass/fail criteria:**

Not a pass/fail. The interpretation drives subsequent decisions:

| Ribbon Length | USCS Estimate | PI Estimate | Expansive Risk |
|---|---|---|---|
| Cannot form | SM or SP | < 5 | None |
| < 1 inch | ML | 5-15 | Low |
| 1-3 inches | CL | 15-30 | Moderate |
| 3-6 inches | CL or CH | 30-50 | Significant |
| > 6 inches, ribbon-able | CH | 50+ | High |

For Oregon expansive clay assessment:
- PI > 25 indicates expansive risk
- PI > 50 indicates highly expansive (mitigation almost certainly needed)

**Common errors:**

```
ERROR: Wrong moisture content
→ Too dry: thread breaks artificially short (false low PI)
→ Too wet: rolls into a paste, doesn't form thread (false zero)
→ Fix: Verify moisture before testing

ERROR: Inadequate kneading
→ Lumps in the sample cause early breakage
→ Fix: Knead thoroughly first

ERROR: Rolling too thick
→ Stop at 1/8 inch (3mm) — that's the test diameter
→ Thicker threads are easier to maintain; not the standard

ERROR: Stopping at 3 inches when thread is still intact
→ Continue to true breakage; longer threads indicate higher plasticity
→ Note actual length, not just "passed 3 inches"

ERROR: Single sample
→ Soil varies; test multiple samples from same depth/location
→ Fix: Test at minimum 3 samples per location of interest
```

**What to do based on results:**

- **No clay (sand/silty)**: No expansive concern; verify bearing with DCP
- **Low PI (CL with short ribbon)**: Some expansive potential; continue with normal foundation if drainage is good
- **High PI (CH or long-ribbon CL)**: Expansive concern; consider lab Atterberg limits to confirm; plan mitigation using the expansive-clay guidance in the Ground Prep and Foundation Risk chapter

---

## D.11 Jar Test (Soil Composition by Sedimentation)

**Purpose:**

The jar test gives a quantitative estimate of soil composition — what percentage is sand, silt, and clay. Useful for site documentation, for distinguishing between soils that look similar, and for planning material requirements.

**Plain language:** Mix soil with water in a tall clear jar, shake it up, let it settle. Heavy particles settle quickly at the bottom; lighter particles settle slower above. You measure the layers to estimate percentages.

**When to perform:**

- For documentation of soil character
- When the field tests give ambiguous results
- For planning purposes (before ordering engineered fill)

**Equipment:**

```
[ ] Tall clear glass or plastic jar (1 quart minimum, 1 gallon better) — $5-$15
   - Straight sides, no narrowing
   - Watertight lid
[ ] Measuring stick or ruler
[ ] Water (preferably distilled, but tap water OK)
[ ] Dish soap or sodium hexametaphosphate (deflocculant)
[ ] Sample of the soil to test (about 1-2 cups)
[ ] Patience (24+ hours for full settlement)
```

Cost: $10-$25 total.

**Procedure:**

```
STEP 1 — PREPARE SAMPLE

[ ] Take a representative sample (1-2 cups)
[ ] Remove organic matter (leaves, twigs, roots)
[ ] Break up large clumps
[ ] Air-dry briefly (not bone-dry; just "moist")

STEP 2 — FILL JAR

[ ] Fill the jar approximately 1/3 full of soil
[ ] Add water to nearly fill (leave 1-2 inches at top)
[ ] Add 1 teaspoon dish soap OR sodium hexametaphosphate
   - Soap is cheap and works fine for residential testing
   - Sodium hexametaphosphate is the technical standard (better dispersal)

STEP 3 — SHAKE

[ ] Cap the jar tightly
[ ] Shake vigorously for at least 1 full minute
   - Goal: completely break up all aggregates and disperse all particles
[ ] Set jar on flat, undisturbed surface

STEP 4 — TIMED OBSERVATIONS

Observe at the following intervals:

[ ] AT 1 MINUTE: 
   - Sand particles have settled to the bottom
   - Mark the level with a marker on the outside of the jar
   - This is the SAND layer

[ ] AT 1-2 HOURS (or longer for fine silt):
   - Silt has settled on top of the sand
   - Mark this level too
   - The new layer is SILT

[ ] AT 24-48 HOURS:
   - Clay has settled on top of silt (if any clay)
   - Mark this level
   - The new layer is CLAY
   - Some very fine clay may remain in suspension indefinitely (organic dye-free, the water will be slightly cloudy)

[ ] FLOATING ON TOP:
   - Organic matter (less dense than water)
   - Note the thickness if any

STEP 5 — MEASURE AND CALCULATE

[ ] Measure each layer's thickness with a ruler
[ ] Total non-water depth = sum of all layers
[ ] Calculate percentages:

   Sand % = (Sand thickness / Total) × 100
   Silt % = (Silt thickness / Total) × 100
   Clay % = (Clay thickness / Total) × 100
   Organic % = (Organic thickness / Total) × 100

STEP 6 — CLASSIFY

Use the USDA soil texture triangle or simplified categories:

   Sand-dominated (>50% sand): Sand or Loamy Sand
   Sand + Silt mix (40-60% sand, 30-40% silt): Sandy Loam
   Mixed (roughly equal): Loam
   Silt-dominated (>50% silt): Silt Loam or Silt
   Clay-dominated (>30% clay): Clay Loam or Clay
   Organic-rich (>5% organic): Organic Soil (Muck or Peat)
```

**Data recording:**

```
JAR TEST RECORD

Date: __________  
Sample location: ____________________________________
Sample depth: ______ inches
Container size: ______
Time started: __________

Layer measurements:
   Sand thickness: ______ (settled at 1 min)
   Silt thickness: ______ (settled at 1-2 hrs)
   Clay thickness: ______ (settled at 24+ hrs)
   Organic floating: ______
   Total: ______

Calculated percentages:
   Sand: ______ %
   Silt: ______ %
   Clay: ______ %
   Organic: ______ %

USDA classification: ____________________________________
USCS estimate: ____________________________________

Notes: ____________________________________
```

**Pass/fail criteria:**

Not a pass/fail test. Provides composition data for decision-making. Significant findings:

- Clay > 30% with high plasticity (verify with ribbon test): expansive concern
- Organic > 5%: not buildable without removal
- Sand > 60% with no clay binding: easy to compact, free-draining
- Mixed loam: typical agricultural soil; engineering decisions depend on depth profile

**Common errors:**

```
ERROR: Insufficient shaking
→ Aggregates not broken up; layers don't settle correctly
→ Fix: Shake hard for full 1 minute; add deflocculant (soap)

ERROR: Reading too soon
→ Fine particles still in suspension
→ Fix: Wait the full 24-48 hours for clay layer

ERROR: Using a non-straight-sided container
→ Layer thicknesses inaccurate
→ Fix: Use straight-sided container; measure to constant scale

ERROR: Organic matter mixed with mineral
→ Confounds layer measurements
→ Fix: Remove visible organic matter before testing

ERROR: Single sample assumed to represent entire site
→ Soil varies
→ Fix: Run jar tests on samples from multiple locations and depths
```

---

## D.12 Hand Auger Sampling

**Purpose:**

A hand auger retrieves soil samples from depth without digging a full test pit. Useful for sampling at specific depths, between test pit locations, and for reaching depths that test pits don't.

**Plain language:** Drill a hand-cranked auger into the ground; pull up soil from the depth you want; identify it.

**When to perform:**

- After surface investigation, to investigate at depth
- Between test pit locations to verify continuity of soil
- When test pits aren't practical (rocky surface, time constraints, smaller investigation)

**Equipment:**

```
[ ] Hand auger kit — $300-$600
   - Bucket auger head (4 inch diameter typical)
   - Or screw auger head
   - Or Edelman auger (Dutch design, very effective in clay)
   - Multiple extension rods (1-meter sections, threaded together)
   - Cross-handle T-bar for turning
[ ] Sample bags (resealable plastic) — $20 for 100 bags
[ ] Marker for labeling — $5
[ ] Field notebook
[ ] Tape measure (50 ft) — $30
[ ] Cleaning rag (for cleaning auger between samples)
[ ] Camera
```

Total kit: $350-$700.

**Safety considerations:**

- Working with extended rod (10+ feet of rod overhead): be aware of overhead obstructions
- Pulling stuck augers: use proper technique to avoid back injury (lift with legs, not back)
- Sharp auger flutes: gloves recommended
- Underground utilities: call 811 before drilling at any new location

**Pre-test setup:**

```
[ ] Identify test location(s)
[ ] Mark with stake or flag
[ ] Verify utilities are clear (call 811 if any doubt)
[ ] Strip surface vegetation/topsoil
[ ] Have all tools and bags ready
[ ] Notebook open with location ID, date, time
```

**Procedure:**

```
STEP 1 — START THE HOLE

[ ] Position auger on prepared surface
[ ] Apply downward pressure
[ ] Turn clockwise to advance
   - Bucket auger: 1/4 turn at a time, advance about 1 inch per turn cycle
   - Edelman or screw auger: continuous turning; advance more per turn

[ ] Continue until bucket is full (typically 4-6 inches of advancement)

STEP 2 — RETRIEVE FIRST SAMPLE

[ ] Withdraw auger straight up (no rotation)
[ ] Empty soil onto a clean surface (tarp, plastic sheet)
[ ] Note the depth range (0-X inches)
[ ] Identify the soil per D.9
[ ] Photograph if useful
[ ] Bag and label sample (location, depth range, date)

STEP 3 — CONTINUE DEEPER

[ ] Re-insert auger into the hole
[ ] Advance to the next sample depth
[ ] Repeat steps 2-3 for as many depths as needed

[ ] Standard sampling depths for site investigation:
   - 0-12 inches (subsoil)
   - 12-24 inches
   - 24-48 inches
   - 48-72 inches (foundation depth typical)
   - Continue to 8-10 ft for basement evaluation

STEP 4 — ATTACH EXTENSIONS AS NEEDED

[ ] When bottom of auger reaches surface, add extension rod
[ ] Rod sections thread together with included connectors
[ ] Verify connection is tight (loose connections will unscrew when pulling)

STEP 5 — HANDLE STUCK AUGER

If the auger becomes stuck:

[ ] DO NOT force with sideways motion (bends rods)
[ ] Slowly turn back (counterclockwise)
[ ] Use a slight rocking motion if needed
[ ] If still stuck:
   - Add a slide hammer puller (specialty tool)
   - Or use a vehicle and a cable (carefully)
   - In extreme cases, dig down to retrieve

STEP 6 — REFUSAL

[ ] If the auger won't advance despite turning:
   - Could be a rock (try moving 1-2 feet over)
   - Could be hardpan or bedrock (significant finding)
   - Could be very dense soil

[ ] Document the depth at which refusal occurred
[ ] Try one more location nearby to distinguish rock from layer

STEP 7 — COMPLETE SAMPLING AND BACKFILL

[ ] After all samples taken, withdraw all rods
[ ] Backfill the hole or mark for future reference
[ ] Don't leave open holes — safety hazard
```

**Data recording:**

```
HAND AUGER SAMPLE LOG

Date: __________
Location: ____________________________________
GPS or stake reference: __________

Sample 1: Depth ______ to ______ inches
   Soil type: ______
   Color: ______
   Notes: ______
   Bag #: ______

Sample 2: Depth ______ to ______ inches
   Soil type: ______
   Color: ______
   Notes: ______
   Bag #: ______

[continue for each sample]

Refusal depth (if any): ______ inches at ______ stratum
Total depth reached: ______ inches
Operator: ____________________________________
```

**Pass/fail criteria:**

Not a pass/fail. Provides soil profile data.

**Common errors:**

```
ERROR: Mixing samples from different depths
→ Profile becomes meaningless
→ Fix: Empty auger completely between samples; clean if soil is sticky

ERROR: Loose rod connections
→ Rods unscrew during withdrawal; auger left in hole
→ Fix: Verify all connections tight

ERROR: Over-rotation when full
→ Soil packs and won't release; loses information about depth
→ Fix: Stop rotating when bucket fills; withdraw immediately

ERROR: Refusal misidentified
→ "Bedrock" might just be a buried rock
→ Fix: Try 2-3 nearby locations to confirm

ERROR: Depths estimated rather than measured
→ Profile is approximate at best
→ Fix: Mark rod sections at known depths; measure as you advance
```

**What to do based on results:**

The auger samples build the soil profile. Combined with DCP at the same location (next test), you have a complete picture of soil type and strength at every depth.

---

## D.13 Test Pit Investigation

**Purpose:**

A test pit is the most informative single investigation method. You can SEE the soil profile, feel multiple layers, sample at any depth, observe water seepage, and identify problems that remote testing misses (buried debris, root channels, layer transitions).

**Plain language:** Dig a hole big enough to look into. Inspect the soil profile in person.

**When to perform:**

- At least 1-3 locations within the proposed building footprint
- Wherever the DCP results are ambiguous
- Before final design decisions

**Standards:** Generally per ASTM D2113 (Standard Practice for Rock Core Drilling and Sampling of Rock for Site Exploration) and ASTM D2488 (visual identification — see D.9).

**Equipment:**

```
[ ] Excavator or backhoe (rented or owned mini-excavator works)
[ ] Shovel for cleanup and detail work
[ ] Sample bags
[ ] Camera (multiple photos required)
[ ] Tape measure (50 ft)
[ ] Marker for labeling depths
[ ] Field notebook
[ ] Knife or trowel for clean sampling face
[ ] Personal safety equipment (hard hat if mechanized; safety glasses)
[ ] Ladder if pit is over 4 feet (NEVER enter without)
```

Excavator rental: $200-$500/day for compact, $500-$800 for larger.

**Safety considerations:**

This is the most dangerous test in this manual. **Pay attention.**

```
DO NOT enter a pit deeper than 4 feet without:
   - Proper sloping (1.5:1 slope minimum for typical soil)
   - OR shoring (sheet piles, hydraulic shores, or trench box)

DO NOT have anyone in the pit while equipment is operating nearby

DO have a plan to exit the pit:
   - Ladder, ramp, or cut steps
   - Always within reach

DO check for utilities before any digging:
   - Call 811 (Oregon Utility Notification Center)
   - Wait for the 2-day response time
   - Visually verify markings before digging

DO consider water:
   - If water enters the pit, it's coming from somewhere
   - Drained area before testing OR document seepage and exit
   - Pumping during test if needed (but be ready to evacuate)

DO NOT leave pits open and unattended:
   - Mark with safety fence and signage
   - Backfill ASAP after investigation complete
```

**Pre-test setup:**

```
[ ] Identify pit locations (typically 2-3 within building footprint)
[ ] Mark each location with stakes
[ ] Call 811 for utility location at least 2 working days before
[ ] Wait for 811 marking to verify utility-free zone
[ ] Plan equipment access route
[ ] Plan spoil pile location (minimum 5 feet from pit edge)
[ ] Have all tools, bags, camera ready
[ ] Notebook with location ID, date, time, weather, operator
```

**Procedure:**

```
STEP 1 — DIG THE PIT

[ ] Equipment: mini-excavator or backhoe
[ ] Pit dimensions:
   - Length: 4-8 feet
   - Width: 3-4 feet (wide enough to inspect easily)
   - Depth: at least to design foundation depth
     - Slab-on-grade: 4-6 feet
     - Basement: 8-10+ feet
[ ] Slope walls during digging:
   - In stable cohesive soils: slight slope OK
   - In granular or saturated soils: 1.5:1 slope mandatory
[ ] Spoils piled at least 5 feet from pit edge
[ ] One end with a sloped ramp for access (instead of just vertical drop)

STEP 2 — INITIAL DOCUMENTATION

[ ] Photograph the pit from above (overview)
[ ] Photograph each side wall
[ ] Note the soil layering visible from above (without entering)

STEP 3 — ENTER FOR DETAILED INSPECTION (IF SAFE)

[ ] Verify pit is safe (per safety section above)
[ ] Use ladder or sloped access
[ ] Have a partner topside (never solo)

STEP 4 — CLEAN A FACE FOR INSPECTION

[ ] Choose one wall for detailed inspection
[ ] With trowel or knife, scrape away the disturbed surface to expose undisturbed soil
[ ] Create a smooth, vertical face about 2 feet wide

STEP 5 — INSPECT THE PROFILE

[ ] Identify each layer:
   - Color
   - Texture
   - Structure
   - Boundary type (sharp or gradual to next layer)
   - Depth of each boundary

[ ] Look for specific features:
   - Roots (depth, density)
   - Old root channels (filled with topsoil — preferential water paths)
   - Mottling (orange/red spots — past saturation)
   - Gleying (gray-blue color — current/recent saturation)
   - Slickensides (shiny smooth surfaces — expansive clay indicator)
   - Cracks (vertical or horizontal)
   - Stones, gravel, cobbles (note size and frequency)
   - Buried debris (concrete, brick, wood, metal)
   - Water seepage (which layer? how fast?)

[ ] Photograph the cleaned face with measure tape for scale

STEP 6 — SAMPLE EACH LAYER

[ ] For each distinct layer:
   - Take a representative sample with knife/trowel
   - Bag and label with depth and layer description
   - Ribbon test, jar test, etc. on sample

STEP 7 — TEST WALL STABILITY

[ ] Push knife or rod into the wall at various depths
   - Easy push: weak soil
   - Moderate resistance: typical
   - Hard refusal: dense soil or rock

[ ] Note any tendency of the walls to collapse or slump

STEP 8 — DOCUMENT THE COMPLETE PROFILE

In your notebook, draw a schematic of the pit profile:

```
Depth (in)   Layer Description
0
   ┃ ┃        Topsoil: dark brown, organic-rich, lots of roots
6  ━━━━
   ┃ ┃        Subsoil A: brown silt loam, few roots
24 ━━━━
   ┃ ┃        Subsoil B: red-brown clay, slickensides
60 ━━━━
   ┃ ┃        Saprolite: weathered rock, soft
96 ━━━━

[ ] Note water seepage location if any
[ ] Note any other features
```

STEP 9 — TIMED OBSERVATIONS

[ ] If investigating water table:
   - Leave the pit open for 24-48 hours (with safety fencing)
   - Observe water level over time
   - The level it stabilizes at is the water table

STEP 10 — EXIT AND PROTECT

[ ] Exit the pit
[ ] Mark with safety fence and signs
[ ] Backfill within a day or two of completing investigation
   - Compact in lifts according to the soil compaction guidance in the ground preparation chapter
   - Don't just dump backfill — it'll settle later
```

**Data recording:**

```
TEST PIT INVESTIGATION RECORD

Date: __________  Pit ID: __________
Location: ____________________________________
Excavator type: ____________________________________
Total depth: ______ ft

Profile (top to bottom):

Layer 1: 0 to ______ inches
   Soil type: ____________________________________
   Color: __________
   Description: __________________________
   Sample bag #: ______

Layer 2: ______ to ______ inches
   Soil type: ____________________________________
   Color: __________
   Description: __________________________
   Sample bag #: ______

[continue for each layer]

Water seepage observed: [ ] No  [ ] Yes — depth ______
Water level after 24 hrs: ______ inches below ground
Roots: [ ] Surface only  [ ] Deep — to ______ inches
Mottling: [ ] No  [ ] Yes — depth ______ to ______
Gleying: [ ] No  [ ] Yes — depth ______ to ______
Slickensides: [ ] No  [ ] Yes — depth ______
Buried debris: [ ] No  [ ] Yes — describe: __________

Photos taken: [ ] Overview  [ ] Each side  [ ] Cleaned face  [ ] Profile schematic
Operator: ____________________________________
```

**Pass/fail criteria:**

Not a pass/fail. Provides comprehensive site information.

**Common errors:**

```
ERROR: Pit not deep enough
→ Critical layer not exposed
→ Fix: Always dig to design foundation depth + 1-2 feet

ERROR: Disturbed face inspected
→ Real soil structure obscured
→ Fix: Clean a face with trowel/knife to expose undisturbed soil

ERROR: Timing issues with water observation
→ "No water" at digging time, water rises overnight
→ Fix: Leave pit open 24-48 hours if water table is a question

ERROR: Single pit assumed representative
→ Site varies; one pit isn't enough
→ Fix: Dig 2-3 pits across building footprint

ERROR: Skipping samples
→ Layers not bagged for further testing
→ Fix: Sample every distinct layer

ERROR: Backfill not compacted
→ Pit creates a soft spot in the soil structure
→ Fix: Backfill in lifts and compact according to the compaction guidance in the Ground Prep and Foundation Risk chapter
```

**What to do based on results:**

The test pit synthesizes everything else. Combined with DCP, it tells you:
- Bearing capacity at depth
- Water management requirements
- Specific problems to address (organic layers, expansive clay, etc.)
- Whether the design assumptions are valid

---

## D.14 Pocket Penetrometer Test (Surface Bearing)

**Purpose:**

The pocket penetrometer is a small, hand-held device that gives a quick reading of unconfined compressive strength of cohesive soils at the surface. Most useful for verifying compaction of fill and for surface bearing checks.

**Plain language:** Push the small calibrated tip into the soil; read the resistance directly in tons per square foot.

**When to perform:**

- Verifying compaction of engineered fill (every lift)
- Surface bearing checks at foundation depth
- Quick spot-checks during construction

**Equipment:**

```
[ ] Pocket penetrometer — $50-$150
   - Spring-loaded shaft with calibrated indicator
   - Conical or flat tip
   - Typical range 0-9 tsf (tons per square foot)
[ ] Cleaning cloth
[ ] Field notebook
```

**Procedure:**

```
STEP 1 — PREPARE THE SURFACE

[ ] Strip topsoil from area to test
[ ] Smooth the surface (don't compact unless you're testing compaction)

STEP 2 — RESET THE PENETROMETER

[ ] Pull the indicator ring back to zero
[ ] Verify the tip is clean

STEP 3 — PRESS

[ ] Hold the penetrometer perpendicular to the soil surface
[ ] Press steadily, with consistent pressure
[ ] Push the tip down to the calibration mark (typically 1/4 inch)
[ ] DO NOT hammer or jerk — must be steady pressure

STEP 4 — READ AND RECORD

[ ] After tip is at calibration mark, read the indicator ring
[ ] Reading is in tsf (tons per square foot)
[ ] Convert to psf if needed: tsf × 2,000 = psf

STEP 5 — REPEAT

[ ] Take 3-5 readings in a small area
[ ] Average the readings
[ ] Discard outliers (one reading off by 50%+ usually means a rock)
```

**Pass/fail criteria:**

For verifying compaction of cohesive soils:
- 4+ tsf (8,000+ psf): well compacted
- 2-4 tsf: moderately compacted
- < 2 tsf: inadequate compaction

For surface bearing check:
- 4+ tsf: adequate for typical residential foundation
- 2-4 tsf: marginal — verify with DCP
- < 2 tsf: inadequate; soil improvement needed

**Common errors:**

```
ERROR: Hammering or jerking
→ Reading is impact-based, not steady
→ Fix: Steady pressure only

ERROR: Tip at angle to surface
→ Friction skews reading
→ Fix: Perpendicular to surface

ERROR: Testing in granular soil
→ Penetrometer doesn't work well in sand or gravel
→ Fix: Use only on cohesive (clay/silt) soils

ERROR: Single reading
→ Surface variations cause scatter
→ Fix: Average 3-5 readings, discard outliers

ERROR: Indicator ring not reset
→ Reading shows previous test
→ Fix: Always reset before each test
```

---

## D.15 Dynamic Cone Penetrometer (DCP) Test — Master Procedure

**Purpose:**

The DCP is the most useful single test for owner-builder soil investigation. It provides depth-by-depth strength readings down to 2+ meters depth. The full theory and analysis is in the site investigation tools discussion in the Ground Prep and Foundation Risk chapter; this is the working procedure for running the test in the field.

**Plain language:** A standardized hammer drops down a fixed distance to drive a steel cone into the soil. Count how many drops to push the cone down a fixed distance. Soft soil needs few drops; hard soil needs many.

**When to perform:**

- Initial site investigation (3-5 locations within building footprint)
- Verification of engineered fill (each lift)
- Pre-pour verification of subgrade
- Whenever soil strength is in question

**Standards:** ASTM D6951 / D6951M

**Equipment:**

```
[ ] Standard DCP per ASTM D6951 — $400-$2,500
   - Cone tip (60° apex, 20 mm base diameter)
   - Drive rod (16 mm diameter, marked in mm or inches)
   - Anvil
   - Drop guide rod
   - Hammer (8 kg / 17.6 lb)
   - Stop collar at 575 mm drop height
   - Handle on top
[ ] Bubble level (small, magnetic) — $20
[ ] Tape measure (steel, 5 m or 16 ft) — $20
[ ] Field notebook with DCP data sheets
[ ] Pen, pencils, markers
[ ] Camera
[ ] Safety glasses
[ ] Work gloves
[ ] Steel-toed boots
[ ] Auger or shovel (to start the hole through topsoil)
[ ] Slide hammer puller (optional but useful) — $150-$300
```

Total kit: $500-$3,000.

**Safety considerations:**

```
[ ] Eye protection always (hammer can launch dirt/rust)
[ ] Steel-toed boots (the assembly is heavy and can drop on feet)
[ ] Gloves (the rod gets banged repeatedly; can pinch)
[ ] Two-person operation strongly recommended:
   - Operator delivers hammer drops
   - Spotter records data and watches for safety issues
[ ] Never test in lightning conditions (steel rod is a lightning rod)
[ ] Watch for overhead obstructions (the rod can extend 10+ feet)
```

**Pre-test setup:**

```
[ ] Identify test locations
   - Minimum 3 within building footprint
   - At corners and middle of foundation
   - Plus baseline test outside footprint
   - Plus tests at any visibly different soil

[ ] Document each location with photo and reference:
   - Stake or flag
   - GPS coordinates if possible
   - Distance from a known reference (property corner, building line)

[ ] Strip topsoil at each location
   - 4-8 inches deep with shovel or auger
   - Goal: start DCP in undisturbed subsoil
   - Don't compact the bottom of the starter hole

[ ] Verify the spot is approximately level
   - Small adjustments OK; significant slope makes the rod want to angle

[ ] Verify the soil is not saturated
   - Wait several days after heavy rain
   - Or test at multiple times to capture seasonal variation

[ ] Assemble the DCP
   - Cone tip threads onto drive rod
   - Anvil on top of drive rod
   - Drop guide rod threads into anvil
   - Hammer slides over drop guide rod
   - Handle on top
   - Verify all threaded connections are tight

[ ] Inspect the equipment:
   - Cone tip sharp, undamaged (replace if mushroomed)
   - Rod straight (bent rod gives bad readings)
   - Hammer slides freely on guide rod
   - All connections tight

[ ] Prepare data sheet
   - Location ID
   - Date and time
   - Weather conditions
   - Operator names
   - Equipment ID
```

**Procedure:**

```
STEP 1 — POSITION

[ ] Place cone tip on the surface of the prepared starter hole
[ ] Hold the rod plumb (vertical)
   - Use bubble level to verify
   - If using a partner, have them watch from a perpendicular direction
[ ] Operator stands to the side, hand on hammer

STEP 2 — SEATING DROPS

[ ] Operator: lift hammer to stop, release with gravity only
[ ] DO NOT push down on hammer
[ ] DO NOT release before reaching the stop
[ ] Continue dropping until cone has penetrated 100mm (4 inches)
   - This is the SEATING DEPTH
   - Don't count these blows toward the test data
   - Document the seating: "Seated to 100mm in N blows"

STEP 3 — TEST DROPS

[ ] Now begin recording data
[ ] Per drop OR per group method:

   PER-DROP (highest resolution):
   - Operator: drop hammer
   - Spotter: measure cumulative depth after each blow
   - Record: blow count, depth

   PER-100MM (standard):
   - Operator: drop hammer
   - Spotter: count drops as they occur
   - When cumulative penetration reaches next 100mm mark:
     - Record blow count for that 100mm interval
     - Continue to next interval

   PER-INCH (alternative):
   - Same as per-100mm but using inches
   - Either is fine; be consistent

STEP 4 — CONTINUE TO DESIGN DEPTH OR REFUSAL

[ ] Continue testing until:

   DESIGN DEPTH REACHED:
   - Typical: foundation depth + 4-6 feet
   - Slab: 6 feet total typical
   - Basement: 14 feet total typical

   OR REFUSAL:
   - 50+ blows in a single 100mm interval
   - STOP — further blows damage equipment and tell you nothing
   - Document refusal depth

   OR EQUIPMENT LIMIT:
   - Maximum testable depth ~2 m for typical DCP
   - Add extension rods if available

STEP 5 — IF SUDDEN RAPID PENETRATION

[ ] If the rod sinks 200+ mm in one blow:
   - You've hit a void or extremely soft layer
   - STOP and document
   - Consider digging a test pit at this location

[ ] If the rod won't penetrate at all from the start:
   - You've hit a rock, root, or hardpan
   - Move the test 2-3 feet sideways and try again
   - If consistent across multiple tests, that's your hard layer

STEP 6 — WITHDRAW

[ ] Pull the rod up by hand
   - Use leg muscles, not back
   - Two-person team makes this easier
[ ] Or use a slide hammer puller for stuck rods
[ ] Note any soil clinging to the rod (gives clue to soil type at depth)

STEP 7 — INSPECT EQUIPMENT

[ ] Check the cone tip for damage
[ ] Wipe down the rod
[ ] Verify hammer still slides freely

STEP 8 — REPEAT AT NEXT LOCATION

[ ] Move to next test location
[ ] Repeat full procedure
```

**Data recording:**

```
DCP TEST DATA SHEET

Date: __________  Time: __________
Location: ____________________________________
Test ID: __________
GPS: __________
Weather: __________
Operator: __________  Spotter: __________
Equipment: __________

Seating: Reached 100mm in ______ blows
[ ] Verified rod plumb
[ ] Verified equipment functional

DATA (per 100mm intervals):

Depth (mm)    Blows    Cumulative Blows    Notes
0-100             ___          ___              (seating)
100-200           ___          ___
200-300           ___          ___
300-400           ___          ___
400-500           ___          ___
500-600           ___          ___
600-700           ___          ___
700-800           ___          ___
800-900           ___          ___
900-1000          ___          ___
1000-1100         ___          ___
1100-1200         ___          ___
1200-1300         ___          ___
1300-1400         ___          ___
1400-1500         ___          ___
1500-1600         ___          ___
1600-1700         ___          ___
1700-1800         ___          ___
1800-1900         ___          ___
1900-2000         ___          ___

Refusal at depth: __________ mm
Maximum depth reached: __________ mm

Soil observed on rod (if any): __________________________

Photos: [ ] Setup  [ ] During test  [ ] Withdrawal
```

**Calculation and interpretation:**

After collecting data:

```
STEP 1 — CALCULATE PENETRATION INDEX (PI) FOR EACH INTERVAL

PI = 100 mm / blows in that interval
   (in mm per blow)

Example: 8 blows for 100mm → PI = 100/8 = 12.5 mm/blow

STEP 2 — PLOT THE PROFILE

X-axis: cumulative blows
Y-axis: depth (zero at top, increasing downward)

Plot each data point. The slope of the line at any depth indicates soil strength
   - Steep slope (rapid depth gain per blow): soft layer
   - Shallow slope (slow depth gain per blow): dense layer

STEP 3 — CONVERT TO BEARING CAPACITY (ESTIMATE)

For each interval, calculate CBR:
   CBR = 292 / PI^1.12

Then estimate bearing pressure:
   For cohesionless soils: qa ≈ 30 × CBR + 250 (psf)
   For cohesive soils: qa ≈ 25 × CBR + 200 (psf)

STEP 4 — INTERPRET

Compare to design requirements:
   - Bearing pressure design (this design): 2,500-5,000 psf typical
   - Required bearing capacity: 2× design = 5,000-10,000 psf

Identify any layers that don't meet requirements.

See the DCP interpretation discussion in the Ground Prep and Foundation Risk chapter for the six pattern types.
   (Good Site, Soft Layer, Improving, Refusal, Variable, Bad Site).
```

**Pass/fail criteria:**

For typical residential foundation at depth of 2-6 feet:

| PI (mm/blow) | CBR (%) | Bearing (psf) | Suitable? |
|---|---|---|---|
| 0-2 | 100+ | 10,000+ | Excellent |
| 2-5 | 50-100 | 3,000-7,000 | Excellent for residential |
| 5-10 | 20-50 | 1,000-3,000 | Good |
| 10-20 | 10-20 | 500-1,000 | Marginal — wider footings or improvement |
| 20-50 | 5-10 | 250-500 | Poor — improvement required |
| 50+ | < 5 | < 250 | Unsuitable without major improvement |

Pass: PI generally < 20 mm/blow throughout the foundation depth range, with no soft layers below.

**Common errors:**

```
ERROR: Pushing down on hammer
ERROR: Lifting hammer past the stop
ERROR: Letting hammer fall short
ERROR: Rod not plumb
ERROR: Hammer not sliding freely
ERROR: Testing in saturated soil
ERROR: Testing through topsoil
ERROR: Testing through frozen ground
ERROR: Trusting one test
ERROR: Continuing past refusal
ERROR: Not documenting
ERROR: Confusing units (mm/blow vs inches)
ERROR: Skipping safety
```

See the DCP interpretation discussion in the Ground Prep and Foundation Risk chapter for the full discussion of each.

**What to do based on results:**

- All tests show PI < 10 mm/blow: site bearing capacity excellent; proceed with confidence
- Mixed results: identify locations of weak layers; plan for over-excavation or other treatment
- All weak: site requires soil improvement or a different design
- Refusal at design depth: bedrock or hardpan; verify with test pit

---

## D.16 Compaction Verification

**Purpose:**

After placing engineered fill, verify that the compaction achieved is adequate. The DCP and pocket penetrometer both work for this; combined readings give better confidence.

**Plain language:** Test the compacted fill the same way you'd test natural soil; compare results to what's required.

**When to perform:**

- After every lift of engineered fill
- Before placing the next lift
- Final verification before slab pour

**Equipment:** DCP and/or pocket penetrometer (D.14, D.15)

**Procedure:**

```
STEP 1 — ALLOW COMPACTION TO STABILIZE

[ ] Wait at least 30 minutes after compaction before testing
   - Soil settles slightly after compactor leaves
   - Wait time gives more representative reading

STEP 2 — TEST IN MULTIPLE LOCATIONS

[ ] Pocket penetrometer:
   - Take 5-10 readings across the lift
   - Average the readings
   - Note any outliers (probably rocks)

[ ] DCP:
   - Run a short DCP test (just penetrate the lift, 12-24 inches max)
   - Note PI in the lift depth

STEP 3 — INTERPRET

For typical residential engineered fill (3/4-inch minus crushed rock):

Pocket penetrometer:
   > 4 tsf: well compacted (95% Proctor equivalent typical)
   2-4 tsf: moderately compacted
   < 2 tsf: needs more compaction

DCP:
   PI < 8 mm/blow: well compacted
   PI 8-15 mm/blow: moderately compacted
   PI > 15 mm/blow: needs more compaction

STEP 4 — DOCUMENT

For each lift:
   Date placed
   Material type and source
   Lift thickness
   Number of compactor passes
   Pocket penetrometer reading (avg)
   DCP PI (if measured)
   Decision: pass / re-compact

STEP 5 — DECIDE

If pass: place next lift, repeat
If re-compact: do additional passes, retest, document
If still failing: investigate cause (wrong material? too dry? too wet?), correct, retest
```

**Common errors:**

```
ERROR: Testing immediately after compactor
→ Soil hasn't stabilized
→ Fix: Wait 30 minutes

ERROR: Single test point per lift
→ Variations not detected
→ Fix: Multiple test points, average results

ERROR: Skipping verification
→ "It looked compacted"
→ Fix: Always verify with measurement

ERROR: Incorrect moisture
→ Compaction inadequate due to wrong moisture
→ Fix: Verify moisture, adjust, re-compact
```

---

## D.17 Settlement Plate Monitoring

**Purpose:**

If pre-loading is being used to consolidate compressible soil before construction, settlement must be monitored to verify the consolidation is complete before construction begins.

**Plain language:** Place a marker on the ground; come back monthly to see how much it's sunk; the rate of sinking tells you how much settlement is left.

**When to perform:**

- During pre-loading operations only
- Monthly during the pre-loading period (months to years)

**Equipment:**

```
[ ] Settlement plates — $50-$200 each (or fabricate from steel plate + pipe)
   - Steel plate (24 x 24 inch typical) buried at the elevation of interest
   - Vertical pipe rising up through the surcharge to a measurable point above
[ ] Survey level or laser level — $300-$2,000
   - Or hire surveyor for monthly readings
[ ] Stable benchmark (a fixed reference point off-site, on bedrock or otherwise immovable)
[ ] Notebook
```

**Procedure:**

```
STEP 1 — INSTALL PLATES BEFORE SURCHARGE

[ ] Place settlement plates at the design subgrade elevation
[ ] Multiple plates across the loaded area (typically 4-6)
[ ] Verify plate is level
[ ] Place vertical pipe extending up
[ ] Take initial elevation reading (this is the "zero")
[ ] Record initial reading

STEP 2 — PLACE SURCHARGE

[ ] Place surcharge material around the plates
[ ] The pipe extends up through the surcharge
[ ] Verify the top of the pipe is accessible

STEP 3 — MONTHLY MONITORING

[ ] Each month, survey the elevation of each plate
[ ] Record the reading
[ ] Calculate settlement since last reading
[ ] Calculate cumulative settlement since start

STEP 4 — PLOT THE CURVE

[ ] X-axis: time (days or months)
[ ] Y-axis: cumulative settlement
[ ] The curve will be steep at first, flattening over time

STEP 5 — DETERMINE WHEN SETTLEMENT IS COMPLETE

[ ] Settlement is "complete" when the curve flattens (rate slows below threshold)
[ ] Common criterion: monthly settlement < 1/8 inch for 3 consecutive months
[ ] Then 90% of expected settlement has occurred
[ ] Surcharge can be removed; construction can begin
```

**Pass/fail criteria:**

- Settlement curve flattening: continue monitoring; nearly done
- Settlement still rapid: continue surcharge longer
- Settlement asymmetric (one plate vs others): investigate variability

---

## D.18 Integrated Site Investigation Workflow

**Purpose:**

This is the procedural integration of all the soil/geotech tests above. Run this once for each site at the appropriate phase.

**The complete site investigation workflow:**

```
PHASE A — DESKTOP RESEARCH (free, before site visit)

[ ] NRCS Web Soil Survey for the parcel
[ ] DOGAMI SLIDO check
[ ] DOGAMI liquefaction map check
[ ] FEMA flood map check
[ ] Oregon Water Resources well log database (nearby properties)
[ ] Past geotechnical work for the site if any

Time: 2-4 hours
Cost: $0
Output: First-cut understanding of the site

PHASE B — SITE WALK-THROUGH (before purchase if possible)

[ ] Visit twice (wet season + dry season)
[ ] Photograph the site
[ ] Look at vegetation patterns
[ ] Look at adjacent properties for clues
[ ] Talk to neighbors

Time: 2-4 hours per visit
Cost: gas
Output: Visual confirmation of desktop findings

PHASE C — SHALLOW INVESTIGATION (after purchase, before commitment)

[ ] Strip topsoil at 3-5 test locations
[ ] Field soil identification at each (D.9)
[ ] Ribbon test on samples (D.10)
[ ] Pocket penetrometer at each location (D.14)
[ ] Document with photos and notes

Time: 1 day
Cost: equipment ($100) + your time
Output: Site-wide soil character understanding

PHASE D — DEEP INVESTIGATION (before final design)

[ ] DCP test at 3-5 locations within building footprint (D.15)
[ ] Hand auger sampling at intermediate locations (D.12)
[ ] Test pit at 2-3 locations within building footprint (D.13)
[ ] Jar test on samples (D.11)
[ ] Document everything thoroughly

Time: 2-3 days
Cost: equipment + excavator rental ($500-$1,500) + your time
Output: Complete geotechnical profile of the site

PHASE E — DECISION

Compile findings into a site investigation report:
[ ] Summary of soil character and profile
[ ] DCP plots
[ ] Test pit photos
[ ] Sample bag inventory
[ ] Bearing capacity assessment
[ ] Water table assessment
[ ] Specific concerns identified
[ ] Recommended foundation design
[ ] Soil improvement plan if any

Decision: Proceed with original design? Modify? Soil improvement? Different site?

PHASE F — VERIFICATION DURING EXCAVATION

[ ] Watch the soil as it comes up during excavation
[ ] If anything different from investigation, STOP and document
[ ] Run additional DCP tests on the prepared subgrade
[ ] Pocket penetrometer on the actual foundation surface
[ ] Photograph each layer

Time: ongoing during excavation
Cost: minimal additional
Output: Confirmation that as-built conditions match design assumptions

PHASE G — COMPACTION VERIFICATION (if engineered fill placed)

[ ] DCP and/or pocket penetrometer on each lift (D.16)
[ ] Document each lift's compaction results
[ ] Pass each lift before next placed

Output: Engineered fill verified meets specifications
```

**Total investment:**

For a serious site investigation with owner-builder execution:
- Equipment (DCP, hand auger, penetrometer, jar test materials): $700-$1,500 (own) or $100-$300 (rent)
- Excavator rental for test pits: $500-$1,500
- Lab tests (Atterberg limits, Proctor, etc., if needed): $500-$2,000
- Geotechnical engineer (if Level C/D site): $3,000-$15,000

Total range: $1,000-$20,000 depending on site complexity.

For comparison: a single foundation crack from undiagnosed expansive clay can cost $50,000+ to repair. The investment in investigation is small.

---

---

## D.19 Atterberg Limits — The Definitive Clay Characterization

**Purpose:**

Atterberg Limits are three specific moisture contents that quantify how a clay-rich soil behaves: where it transitions between solid, semi-solid, plastic, and liquid states. The most important output is the **Plasticity Index (PI)**, which is the difference between the Liquid Limit and Plastic Limit. PI directly indicates expansive clay risk:

- PI 0–15: low expansion potential
- PI 15–25: moderate expansion potential
- PI 25–50: significant expansion (CH clay)
- PI > 50: highly expansive — major mitigation required

The ribbon test (D.10) approximates Atterberg Limits qualitatively. The lab procedure quantifies them definitively. For sites where expansive clay is a real concern, lab Atterberg testing is the difference between guessing and knowing.

**Plain language:** A lab takes your soil sample, dries it, sieves it, then runs three specific tests that find the moisture content at which the soil changes behavior. The numbers tell you exactly how much expansion potential the clay has, which determines whether you need to mitigate it and how much.

**When to perform:**

- When field identification (D.9, D.10) suggests problematic clay (long ribbon, polygonal cracking, slickensides in test pits)
- When NRCS Web Soil Survey indicates "moderate" or "high" shrink-swell potential and you want to verify
- When a structural engineer or geotechnical engineer requests it for foundation design
- When DCP results are good but you need to confirm the clay won't move seasonally
- For any site with visible expansive clay symptoms (cracks in nearby existing structures, wide soil cracks, etc.)

**Standards:** ASTM D4318 — Standard Test Methods for Liquid Limit, Plastic Limit, and Plasticity Index of Soils

The European equivalent is BS 1377 / ISO 17892-12, which uses a "fall cone" method instead of the Casagrande device. Results are similar but the apparatus differs.

**Equipment (lab's responsibility, listed for context):**

```
LIQUID LIMIT:
- Casagrande device (mechanical liquid limit apparatus)
  - A brass cup that drops 10 mm onto a hard rubber base
  - Standard rate: 2 drops per second
- Grooving tool (forms a V-shaped groove in the soil paste)
- Glass plate for mixing
- Spatulas
- Distilled water

PLASTIC LIMIT:
- Glass plate (frosted ground glass)
- Hand for rolling
- 3 mm reference rod (for thread diameter check)

GENERAL:
- Drying oven at 110°C ± 5°C
- Balance with 0.01 g resolution
- #40 sieve (425 micrometers)
- Mortar and pestle (for breaking up dried sample)
- Containers (small metal tins with lids)
```

**The owner-builder's role:**

Provide a representative sample to the lab. Wait for results. Interpret the report.

**Sample collection:**

```
[ ] Identify the soil layer to characterize
   - Typically the layer at planned foundation depth
   - For expansive clay assessment: the upper 3-5 feet of clay (the active zone)

[ ] Collect at least 1 lb (500 g) of representative material
   - More if you want multiple tests run
   - Use a clean trowel and clean container
   - Avoid contamination with topsoil or fill

[ ] Container:
   - Sealed plastic bag or jar (Ziploc gallon-size or quart Mason jar)
   - Double-bagging is not necessary but doesn't hurt

[ ] Label clearly:
   - Project name and number
   - Sample ID (e.g., TP-1, layer 2; or HA-3, depth 4-5 ft)
   - Date collected
   - Collector's name
   - Test pit or auger location
   - Depth range
   - Visual description ("brown clay with mottling")

[ ] Storage:
   - Sample stays at field moisture content (don't dry it out before sending)
   - Cool/shaded location until shipment
   - Ship within a few days

[ ] Documentation:
   - Photo of sample container before sealing
   - Photo of label
   - Cross-reference to test pit log or auger log
```

**Submitting to the lab:**

Most Pacific NW geotechnical labs accept samples by mail or drop-off:

- **Northwest Testing Laboratories** (Tigard, OR) — full-service geotech lab
- **Carlson Testing** (Tigard, OR) — alternative
- **PSI / Intertek** (Portland, OR) — national chain
- **GeoEngineers** (Portland and Bend, OR) — engineering firm with lab capability
- **GRI** (Beaverton, OR) — engineering firm with lab
- **Local soils labs** — search "soils testing laboratory [Oregon city]"

```
[ ] Call ahead to confirm:
   - The lab runs ASTM D4318
   - Their turnaround time (typically 5-10 business days)
   - Their pricing (typically $80-$200 per sample)
   - Sample size requirements (most need at least 200-500 g of fines passing #40 sieve)
   - Shipping/drop-off instructions

[ ] On the chain-of-custody form (lab will provide):
   - Sample ID matches your project records
   - Specify the test: "Atterberg Limits per ASTM D4318"
   - Specify reporting requirements:
     - Liquid Limit (LL)
     - Plastic Limit (PL)
     - Plasticity Index (PI)
     - USCS classification
     - Visual description
```

**The lab procedure (for reference — what they do with your sample):**

```
SAMPLE PREP:

1. Sample is air-dried and broken up with mortar and pestle (gentle — don't crush particles)
2. Sieve through #40 sieve (425 micrometers); only the fines pass
3. The fines are the test material

LIQUID LIMIT (LL) DETERMINATION:

4. Mix fines with distilled water to form a uniform paste
5. Place a portion in the Casagrande cup, level the surface
6. Cut a V-shaped groove down the center using the grooving tool
7. Operate the Casagrande device at 2 drops per second
8. Count drops until the groove closes a distance of 13 mm (1/2 inch)
9. Take a small sample for moisture content determination (oven dry, weigh)
10. Repeat at varying water contents (typically 4-5 trials spanning 15-35 drops)
11. Plot drops vs. moisture content on semi-log paper
12. The moisture content corresponding to 25 drops is the Liquid Limit

PLASTIC LIMIT (PL) DETERMINATION:

13. Take a small portion of the same prepared paste
14. Roll on the glass plate with the palm or fingers
15. Roll into a thread, gradually thinner
16. Continue rolling until the thread crumbles at exactly 3.2 mm diameter
17. Collect the crumbled threads, determine moisture content (oven dry, weigh)
18. Repeat 2-3 times for verification
19. Average moisture content at the crumbling point is the Plastic Limit

PLASTICITY INDEX (PI):

20. PI = LL - PL
21. Classify per USCS:
    - LL > 50: high plasticity
    - LL < 50: low plasticity
    - On the plasticity chart (LL vs. PI), the soil falls in CL, CH, ML, MH, OL, or OH zones

REPORT GENERATION:

22. Lab prepares formal report with all results, calculations, classifications
23. May include the plasticity chart with the sample point plotted
24. Some labs include photographs of the test
```

**Interpreting the report you receive:**

```
TYPICAL ATTERBERG REPORT FORMAT:

Sample ID: [your sample ID]
Date received: [date]
Date tested: [date]
Tested by: [technician name]

Results:
Liquid Limit (LL): _____ %
Plastic Limit (PL): _____ %
Plasticity Index (PI): _____ %

USCS Classification: [CL, CH, ML, MH, OL, OH]
Description: [brown clay with sand, etc.]

Plasticity chart: [included as graphic]
```

**What the numbers mean:**

| PI Range | Plasticity | USCS Class | Expansive Risk | Recommended Action |
|---|---|---|---|---|
| 0-3 | Non-plastic | (depends on grain size) | None | No mitigation |
| 3-7 | Slight | ML or sandy ML | None to minimal | No mitigation |
| 7-15 | Low | CL-ML or low-PI CL | Low | Standard design with attention to drainage |
| 15-25 | Moderate | CL | Moderate | Mitigation recommended; over-excavate top layer or stiffened slab |
| 25-50 | High | CH | High | Active mitigation required |
| > 50 | Very high | CH (high LL) | Very high | Major mitigation OR find different site |

**Cost:** $80-$200 per sample. Some labs offer package deals (Atterberg + gradation + Proctor) at reduced rates if you submit multiple tests on the same sample.

**Common errors (lab side, but worth knowing):**

```
ERROR: Sample dried too much before sieving
→ Particles aggregate; sieving incomplete
→ Result: artificially high PI
→ Lab should re-prep if obvious

ERROR: Tap water used instead of distilled
→ Minerals affect clay behavior
→ Result: variable PI readings
→ ASTM specifies distilled water

ERROR: Casagrande device not calibrated
→ Drop height drift over time
→ Result: shifted LL readings
→ Reputable labs calibrate routinely

ERROR: Sample contaminated with topsoil organic matter
→ Skews readings (organic content lowers LL)
→ Owner-builder side: sample carefully, avoid topsoil
```

**What to do with the results:**

For PI < 15 (low plasticity):
- Proceed with standard mat foundation design
- Standard drainage practices

For PI 15-25 (moderate):
- Engage structural engineer to verify mat design adequacy
- Consider over-excavation and replacement of upper 3-5 feet
- Strict drainage and grading practices
- Avoid trees within 1× foundation depth distance

For PI 25-50 (high — CH clay):
- Geotechnical engineer engagement strongly recommended
- Active mitigation required:
  - Over-excavation and replacement OR
  - Lime stabilization OR
  - Stiffened/post-tensioned slab OR
  - Pier-and-grade-beam foundation
- Monitor drainage carefully
- No trees within foundation depth × 1.5

For PI > 50 (very high — extreme):
- Geotechnical engineer required
- Major design adaptation required
- Cost premium 20-50% on foundation
- Consider alternative site

**Document the report in the project binder.** It becomes part of the home's permanent record. At resale, an inspector seeing "Atterberg Limits PI 22, mitigated by 4-foot over-excavation and replacement, structural engineer's letter on file" is much more reassuring than no documentation at all.

---

## D.20 Proctor Test — Compaction Specification

**Purpose:**

The Proctor Test determines the maximum dry density and optimum moisture content for a given soil under standard compactive effort. The result is used to specify what "compacted" means in the field — typically expressed as a percentage of Proctor Maximum Dry Density (e.g., "compact to 95% Proctor"). Without a Proctor result, "compact to 95%" has no defined meaning.

For owner-builder fill operations, a Proctor result for the fill material lets you:
- Specify what density to achieve in the field
- Know the optimum moisture content (so you can wet to the right consistency)
- Verify field compaction with DCP or pocket penetrometer at known target levels

**Plain language:** The lab takes a sample of your fill material (gravel, sand, or whatever you're using) and runs it through a series of compaction tests at different moisture contents. The output tells you the maximum density you can achieve and the moisture content where you'll achieve it. That target density and moisture become your specification for the field.

**When to perform:**

- Before placing any significant amount of engineered fill
- When using fill from an unfamiliar source
- When troubleshooting field compaction failures (to verify the spec is achievable)
- For sites with significant over-excavation and replacement

For typical owner-builder use: ONE Proctor per fill type per project. If you're using 3/4-inch minus crushed rock from one quarry, run one Proctor; the result applies to all your fill.

**Standards:**

- **ASTM D698** — Standard Proctor (5.5 lb rammer, 12-inch drop, 25 blows × 3 layers)
  - Lower compactive effort
  - Used for typical residential fill
  
- **ASTM D1557** — Modified Proctor (10 lb rammer, 18-inch drop, 25 blows × 5 layers)
  - Higher compactive effort
  - Used for highway, runway, and heavy-load applications
  - Higher MDD, lower OMC than Standard

For residential use, Standard Proctor (ASTM D698) is appropriate. Specify Standard unless your structural engineer requires Modified.

**Equipment (lab's responsibility, listed for context):**

```
- Proctor mold:
  - Standard: 4-inch diameter × 4.6-inch height, 1/30 ft³ volume
  - Larger 6-inch mold for coarser materials
  - Detachable base and collar
  
- Standard rammer:
  - 5.5 lb mass
  - 2-inch diameter face
  - 12-inch drop height
  - With drop-control sleeve
  
- Modified rammer:
  - 10 lb mass
  - 2-inch diameter face
  - 18-inch drop height
  
- Steel straightedge for trimming
- Drying oven at 110°C ± 5°C
- Balance with 1 g resolution
- Sample preparation tools (mortar, pestle, sieves, mixing pans)
- Spray bottle for adding water
```

**The owner-builder's role:**

Provide a representative sample of the fill material. Wait for results. Use them to set field specifications.

**Sample collection:**

```
[ ] Identify the fill source:
   - Local quarry (most common — they may already have Proctor results for their products)
   - Excavated material being reused
   - Specific stockpile

[ ] Collect a representative sample:
   - For a delivered fill: sample from multiple loads, blend
   - For a quarry: ask for a sample, or pick up a 5-gallon bucket from the loading area
   - Approximate quantity: 30-50 lb (one 5-gallon bucket full)
   - More if material is coarse or variable

[ ] Container:
   - 5-gallon bucket with lid (most labs accept this)
   - Or large heavy-duty bag (contractor bag rated 3+ mil)

[ ] Label:
   - Project name
   - Material source (e.g., "ABC Quarry, 3/4-inch minus crushed basalt")
   - Date collected
   - Collector's name
   - Cross-reference to project records

[ ] Quarry-supplied Proctor results:
   - Many quarries already have current Proctor results for their products
   - Ask before sending a sample
   - Free results from the quarry save the lab fee
   - Verify the results are current (within 12-24 months)
```

**Submitting to the lab:**

Same labs that do Atterberg Limits typically do Proctor tests. Some considerations:

```
[ ] Call ahead:
   - Confirm they run ASTM D698 (Standard) or D1557 (Modified) — verify which you need
   - Pricing typically $300-$500 per Proctor
   - Turnaround typically 5-10 business days
   - Larger sample for coarser materials (some labs require 50-100 lb for coarse mixes)

[ ] On the chain-of-custody form:
   - Sample ID
   - Test specified: "Standard Proctor per ASTM D698" (or Modified)
   - Reporting requirements:
     - Maximum Dry Density (MDD)
     - Optimum Moisture Content (OMC)
     - Compaction curve (graph)
     - Material classification (often included)
```

**The lab procedure (for reference):**

```
SAMPLE PREP:

1. Sample is air-dried (not oven-dried; preserves natural particle character)
2. Lumps broken up gently
3. Sieved through specified sieve (typically #4 for fine fractions; coarser sieves for larger material)
4. Material passing the sieve is the test material

COMPACTION TESTING:

5. Five subsamples are prepared at varying moisture contents:
   - Below estimated optimum
   - At estimated optimum
   - Above estimated optimum
   - Spread across maybe 4-6% range

6. For each subsample:
   - Place in mold in 3 lifts (Standard) or 5 lifts (Modified)
   - Each lift compacted with 25 rammer blows
   - Excess material trimmed flush with mold rim
   - Compacted sample weighed
   - Sample taken for moisture content (oven dry, weigh)

7. Calculations:
   - Bulk density = mass / volume of mold
   - Dry density = bulk density / (1 + moisture content)
   - Moisture content = (wet weight - dry weight) / dry weight × 100

8. Plot dry density vs. moisture content
   - The curve has a peak (the maximum)
   - The peak's coordinates are MDD and OMC

REPORTING:

9. Lab prepares formal report:
   - All raw data
   - Calculated densities and moistures
   - Compaction curve graphic
   - MDD and OMC values
   - Material classification
   - Any observations about the sample
```

**Interpreting the report you receive:**

```
TYPICAL PROCTOR REPORT:

Material: [description]
Source: [quarry / source]
Test method: Standard Proctor per ASTM D698

Results:
Maximum Dry Density (MDD): _____ pcf (lb/cubic foot)
Optimum Moisture Content (OMC): _____ %

Compaction Curve: [graph showing dry density vs. moisture]

Test data table:
Trial | Moisture Content | Wet Density | Dry Density
1     | _____ %          | _____ pcf   | _____ pcf
2     | _____ %          | _____ pcf   | _____ pcf
[etc.]

Classification: [USCS class]
```

**Typical values for common Oregon materials:**

| Material | MDD (pcf) | OMC (%) | Notes |
|---|---|---|---|
| Well-graded gravel (GW) | 130-145 | 5-8 | Best for engineered fill |
| Crushed rock (3/4" minus) | 130-145 | 5-8 | Most common spec for residential |
| Poorly-graded sand (SP) | 105-115 | 10-14 | Acceptable for backfill |
| Silty sand (SM) | 115-130 | 10-14 | Common alluvial material |
| Lean clay (CL) | 105-120 | 12-18 | Compacts but slow drainage |
| Fat clay (CH) | 90-110 | 18-30 | Avoid as fill if possible |

**Using the results to specify field compaction:**

```
TYPICAL SPECIFICATION:

"Place engineered fill in lifts not exceeding 6 inches loose thickness.
Compact each lift to a minimum of 95% of Standard Proctor Maximum Dry Density (per ASTM D698) at moisture content within ±3% of Optimum Moisture Content. Verify compaction by Dynamic Cone Penetrometer testing or pocket penetrometer prior to placement of next lift."

For fill with MDD = 135 pcf, OMC = 7%:
- Target field density: 0.95 × 135 = 128 pcf
- Target moisture: 4-10% (7% ± 3%)
- Verification: DCP shows PI ≤ 8 mm/blow, OR penetrometer ≥ 4 tsf
```

**The critical practical detail — moisture matters:**

Compaction effort produces maximum density only when the soil is at OMC. Off-OMC material won't reach target density no matter how much you compact. Field practice:

- Start with material at approximately OMC
- "Squeeze test": handful held in fist should hold a ball that breaks apart with light pressure
- If material is too dry: add water (sprinkler or hose), mix, recompact
- If material is too wet: spread out, allow to dry, recompact

**Cost:** $300-$500 per Proctor. Most projects need only one Proctor (per fill type). The result applies to all uses of that material.

**Common errors:**

```
ERROR: Wrong test method (Standard vs. Modified)
→ Specifications mismatch with field tests
→ Result: confusion about acceptance criteria
→ Fix: Always specify Standard for residential unless Modified is required

ERROR: Material variability between Proctor sample and field deliveries
→ The test result is for the sample, not the variable deliveries
→ Result: field compaction inconsistent
→ Fix: Insist on consistent material from one source; or run multiple Proctors if material varies

ERROR: Sample dried too aggressively before testing
→ Particle structure changed
→ Result: skewed Proctor curve
→ Fix: Air-dry only; oven-dry only for moisture content determination

ERROR: Not running enough trial points on the curve
→ Peak of curve poorly defined
→ Result: imprecise OMC and MDD
→ Fix: Reputable labs run 5+ trials; verify on the report
```

**What to do with the results:**

```
1. Add Proctor results to project specifications:
   "Engineered fill shall be 3/4-inch minus crushed rock with MDD = 135 pcf and OMC = 7% per ASTM D698, dated [date]."

2. Communicate to anyone placing fill:
   - The target density (95% of MDD = 128 pcf)
   - The target moisture (OMC ± 3% = 4-10%)
   - The verification method (DCP, penetrometer)

3. Reference in field compaction verification (D.16):
   - Compare DCP/penetrometer results to Proctor-derived expectations
   - Document each lift's compaction relative to spec

4. File in project binder:
   - Original Proctor report
   - Field compaction verification logs
   - Cross-reference to specific fill placements
```

**For owner-builders bypassing the formal lab:**

If running a Proctor isn't practical (small project, no lab access, etc.), use estimated values from the table above based on the material type. This is less precise but workable for residential applications:

- Take the typical MDD for your material type
- Use the typical OMC range
- Specify field compaction at "95% of estimated MDD"
- Verify aggressively with DCP and pocket penetrometer (multiple readings, all locations)

The lab Proctor is more precise but the estimated approach is the reasonable owner-builder middle ground when budgets are tight.

---

### D.19 + D.20 Combined Workflow

For a typical site investigation that includes lab work:

```
DURING DETAILED INVESTIGATION:

[ ] Collect Atterberg sample(s) from suspected expansive clay layers
   - One sample per soil layer of concern
   - Typically 2-4 samples for a thorough investigation

[ ] Identify fill material source(s)
   - Quarry to be used for engineered fill
   - Material to be excavated and reused (if any)

PARALLEL WITH FIELD WORK:

[ ] Submit Atterberg samples to lab
[ ] Request Proctor from quarry (often free)
[ ] Or submit fill sample to lab for Proctor

DURING WAIT (5-10 business days):

[ ] Continue field investigation (DCP, test pits, etc.)
[ ] Prepare site plan
[ ] Coordinate with engineers if engaged

ON LAB RESULTS RETURN:

[ ] Compare Atterberg PI to expected ranges
   - Adjust foundation strategy if PI > 25
   - Document in project records

[ ] Use Proctor MDD/OMC to set field compaction spec
   - Update project specifications
   - Communicate to all parties involved in fill placement

[ ] File all lab reports in project binder

INTEGRATE INTO DECISION:

[ ] Site classification refined with lab data
[ ] Proceed / Modify / Decline decision documented with full rationale
```

**Total cost (lab work) for typical residential site:**
- 1-2 Atterberg samples: $80-$400
- 1 Proctor (or free from quarry): $0-$500
- **Total: $80-$900**

For a $300,000+ build, this is small money for major risk reduction and design confidence.

---
