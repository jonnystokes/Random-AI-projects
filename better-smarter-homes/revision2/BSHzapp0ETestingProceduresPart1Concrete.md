# Appendix E — Testing Procedures

*Step-by-step procedures for every test run during the build*

This appendix is the working manual for every test referenced throughout the BSH Design and Engineering Documentation. Section 12 (Testing and Development Program) describes WHY each test is run and WHAT it tells us; this appendix describes HOW to run each one — equipment, setup, procedure, recording, interpretation, troubleshooting.

The format for each test is:

- **Purpose** — what we're trying to learn
- **When to perform** — at what point in the build
- **Standards** — the official testing standard, where one applies
- **Equipment** — what you need (with rough 2026 pricing)
- **Safety considerations** — hazards specific to this test
- **Pre-test setup** — what to do before starting
- **Procedure** — numbered steps to perform the test
- **Data recording** — what to write down (forms in Appendix F)
- **Pass/fail criteria** — what the result means
- **Common errors** — mistakes that produce bad data
- **What to do if it fails** — corrective action

The tests are organized in the same general sequence as the build:

**Part 1** — Concrete Testing (this part)
**Part 2** — Soil and Geotechnical Testing
**Part 3** — Envelope and Air Quality Testing
**Part 4** — MEP Commissioning and Verification

These tests are designed to be run by an owner-builder with reasonable mechanical aptitude, supported by equipment rental and (occasionally) third-party laboratory services. Where a test requires professional certification or specialty equipment beyond reasonable reach, that's noted explicitly with guidance on hiring it out.

---

# Part 1 — Concrete Testing

The concrete in this design is the bones of the building. It will outlast generations. Verifying that what arrives in the truck matches what was specified in the mix design is the difference between a 1,000-year building and a 50-year building. This part covers every concrete test relevant to a residential pour.

The tests progress from immediate (during pour) to delayed (lab-cured cylinders crushed weeks later). Every pour gets the immediate tests; cylinders are cast for delayed verification at design milestones.

---

## E.1 Slump Test (Workability)

**Purpose:**

The slump test measures the workability — basically the wetness — of fresh concrete. Slump is the most direct field measurement of consistency: too low (stiff) and the concrete won't flow into forms or around rebar; too high (soupy) and the water/cement ratio is too high, weakening the cured concrete. The slump value tells you immediately whether the concrete in the truck matches what was ordered.

**Plain language:** You fill a cone-shaped mold with concrete, lift the mold off, and measure how much the concrete pile slumps (sinks) downward. Stiff concrete barely moves; soupy concrete flattens out. The number of inches it slumps is the slump value.

**When to perform:**

- Every truck delivery on every pour
- Within 5 minutes of the truck arriving (before any water is added on site)
- Before placing concrete from that truck

**Standards:** ASTM C143 / C143M — Standard Test Method for Slump of Hydraulic-Cement Concrete

**Equipment:**

```
[ ] Standard slump cone (ASTM C143 compliant) — $40-$120
    - Top inside diameter: 4 inches (102 mm)
    - Bottom inside diameter: 8 inches (203 mm)
    - Height: 12 inches (305 mm)
    - With foot pieces for stabilizing
[ ] Tamping rod — $20-$40
    - 5/8 inch (16 mm) diameter
    - 24 inches (610 mm) long
    - Hemispherical (rounded) tip
[ ] Slump plate (smooth, flat, non-absorbent) — $30-$60
    - Or use a smooth piece of plywood (24x24 inches) with a sealed surface
[ ] Square-end shovel or scoop for filling
[ ] Tape measure or ruler (rigid, marked to 1/4 inch or 5 mm)
[ ] Cleanup water and brush
[ ] Notebook for recording
```

Total kit: about $100-$220.

**Safety considerations:**

- Wet concrete causes skin burns over time (alkaline, abrasive)
- Wear gloves and safety glasses
- The truck driver should be parked safely; you'll be working close to the chute

**Pre-test setup:**

```
[ ] Choose a flat, level location near the truck (within 10 feet)
[ ] Dampen the slump cone interior and the slump plate with water (not soaked, just damp — prevents concrete from sticking)
[ ] Have all tools at hand, ready to go
[ ] Notebook open with truck number, time, and weather noted
```

**Procedure:**

```
1. Place the slump cone on the slump plate, large opening down

2. Stand on the foot pieces to hold the cone in place

3. Fill the cone in three layers, each approximately 1/3 of the volume:
   
   LAYER 1 (bottom 1/3):
   - Scoop concrete from the truck chute (or a wheelbarrow that just received concrete)
   - Sample from the middle of the discharge stream, not the start or end
   - Fill the cone to roughly 1/3 height
   - Tamp 25 times with the rod
   - Tamping pattern: distribute the strokes across the entire layer
   - Tamp into the bottom layer fully (rod should reach the slump plate)
   
   LAYER 2 (middle 1/3):
   - Add concrete to roughly 2/3 height
   - Tamp 25 times
   - Tamp through this layer and approximately 1 inch into the layer below
   
   LAYER 3 (top 1/3):
   - Slightly overfill the cone
   - Tamp 25 times
   - Tamp through this layer and approximately 1 inch into the layer below
   
4. Strike off the top:
   - Use the tamping rod, held flat across the top of the cone
   - Roll the rod back and forth, smoothing the surface flush with the cone top
   - Remove excess concrete

5. Lift the cone:
   - Stand off the foot pieces
   - Lift the cone STRAIGHT UP in 5-10 seconds
   - Smooth, steady motion — no twisting, no jerking
   - Set the empty cone aside, top down (so it doesn't trap concrete)

6. Measure:
   - Place the cone (or the rod) horizontally across the original cone position
   - Measure from the top of the displaced concrete to the underside of the rod
   - Read the slump in inches and quarter-inches

7. Record the result on the form (Appendix F)
```

**Data recording:**

```
SLUMP TEST RECORD:

Date: ______________  Time: __________
Truck #: __________   Load # of __ for this pour
Concrete temperature: ______ °F
Air temperature: ______ °F
Mix design: ____________________________________
Slump measured: ______ inches
Target slump: ______ inches (per mix design)
Within tolerance? [ ] Yes  [ ] No
Notes: _______________________________________________
Operator: _______________________________________________
```

**Pass/fail criteria:**

The mix design specifies a target slump and tolerance. Typical residential mixes:
- Target slump: 4 inches
- Tolerance: ±1 inch (range 3-5 inches acceptable)

For pumped concrete:
- Higher slump typical (5-7 inches)
- Tolerance: ±1.5 inches

For high-performance mixes (this design's pozzolanic blend with superplasticizer):
- Slump can vary widely depending on plasticizer dosing
- Mix design will specify; verify with supplier

**FAIL criteria:**
- Slump more than 1 inch above target → too wet (water added or excess plasticizer)
- Slump more than 1 inch below target → too stiff (low water or improper mixing)
- "Shear slump" (one side falls off) → concrete not properly mixed or too dry → re-run test on a fresh sample

**Common errors:**

```
ERROR: Cone not held still during filling
→ Concrete shifts; slump reading inaccurate
→ Fix: Stand FIRMLY on foot pieces

ERROR: Tamping not uniform
→ Some areas over-consolidated, others under
→ Fix: Distribute 25 strokes evenly across the layer

ERROR: Cone lifted with twist or sideways motion
→ Concrete pile lopsided; reading invalid
→ Fix: Lift straight up, smooth motion

ERROR: Cone lifted too fast or too slow
→ Standard is 5-10 seconds total
→ Too fast can shock the concrete; too slow allows segregation
→ Fix: Practice the motion before the truck arrives

ERROR: Sampling from start or end of truck discharge
→ First and last concrete in a load is not representative
→ Fix: Sample from the middle of the discharge stream

ERROR: Concrete left in cone or shovel from previous test
→ Old concrete contaminates new sample
→ Fix: Wash thoroughly between tests

ERROR: Cone or plate dry
→ Concrete sticks; readings inaccurate
→ Fix: Pre-dampen all surfaces

ERROR: Working too slowly
→ Concrete sets up between filling and lifting
→ Fix: Complete the test within 2-1/2 minutes total
```

**What to do if it fails:**

If slump is **too high** (too wet):
- DO NOT accept this load if outside tolerance
- Communicate with the truck driver and the batch plant
- The driver may add cement to thicken (with permission)
- If unrecoverable, the load may be rejected; document the rejection

If slump is **too low** (too stiff):
- The driver may add water (with permission, and only up to design limits)
- Adding water on-site is recorded on the batch ticket
- If the concrete is already partially set, rejection may be necessary

If you have **doubts**:
- Run the test again on a fresh sample from the same truck
- Two failed slump tests on the same truck = reject the load

Document everything. The batch ticket from the truck plus your slump test record creates the project's quality control file.

---

## E.2 Air Content Test (Optional but Recommended for This Design)

**Purpose:**

Measures the percentage of entrained air in fresh concrete. Entrained air is essential for freeze-thaw resistance — tiny air bubbles give expanding ice somewhere to go without cracking the concrete. Insufficient air leads to surface scaling and cracking after years of freeze-thaw cycles. Excessive air weakens the concrete.

**Plain language:** A small chamber is filled with concrete, sealed, and pressurized. The amount of air compression tells you how much air is in the concrete.

**When to perform:**

- Every truck if specified by the mix design
- Random truck spot-checks for routine pours
- Always for exterior concrete exposed to freeze-thaw cycles

**Standards:** ASTM C231 / C231M — Standard Test Method for Air Content of Freshly Mixed Concrete by the Pressure Method

**Equipment:**

```
[ ] Type B pressure-method air meter — $400-$1,200
    - Includes calibrated chamber, pump, and gauge
[ ] Tamping rod — same as slump test
[ ] Strike-off bar — typically supplied with air meter
[ ] Mallet or rubber hammer — $20
[ ] Wash water and brush
[ ] Notebook
```

**Safety considerations:**

- The pressurized chamber holds 30-50 psi briefly
- Manufacturer's instructions cover safety
- Eye protection always

**Pre-test setup:**

```
[ ] Calibrate the meter according to manufacturer instructions
    - Before first use of the day
    - After any drop or rough handling
    - Periodic verification with known air content sample
[ ] Pre-dampen the chamber interior
```

**Procedure:**

The exact procedure varies by meter brand, but the general process is:

```
1. Sample concrete from the middle of truck discharge

2. Fill the bottom chamber (the "container") in three layers:
   - Layer 1: about 1/3 full, tamp 25 times, tap sides with mallet 10-15 times to release entrapped air
   - Layer 2: about 2/3 full, tamp 25 times, tap sides
   - Layer 3: slightly overfilled, tamp 25 times, tap sides

3. Strike off the top using the strike-off bar
   - Sawing motion to leave a smooth, level surface flush with the rim

4. Clean the rim of the container thoroughly
   - Any concrete remaining will prevent a good seal

5. Attach the cover (top assembly) and clamp tightly
   - The seal must be airtight; verify clamps are secure

6. Add water through the petcocks until water flows out the opposite petcock
   - This fills the space above the concrete with water (no trapped air)

7. Close all petcocks

8. Pump air into the upper chamber to the initial pressure mark
   - Read the gauge: should read at the calibration point

9. Press the main release valve (transfers pressure to the concrete chamber)
   - The gauge needle moves to the new equilibrium
   - This new reading is the apparent air content

10. Read and record the air content as a percentage

11. Release pressure, open chamber, dump and clean
```

**Data recording:**

```
AIR CONTENT TEST RECORD:

Date: ______________  Time: __________
Truck #: __________
Air content measured: ______ %
Target air content: ______ % (per mix design)
Within tolerance? [ ] Yes  [ ] No
Notes: _______________________________________________
Operator: _______________________________________________
```

**Pass/fail criteria:**

For exterior concrete in freeze-thaw exposure:
- Target: 5-7% air content
- Tolerance: ±1.5%

For interior concrete with no freeze-thaw exposure:
- Air content less critical (1-3% acceptable; specified by mix design)

For pumped concrete:
- Slightly higher target (6-8%) since pumping reduces air content slightly

**Common errors:**

```
ERROR: Inadequate consolidation
→ Trapped air voids read as entrained air
→ Fix: Tamp thoroughly; tap sides to release entrapped air

ERROR: Poor seal at chamber rim
→ Pressure leaks; reading invalid
→ Fix: Clean rim thoroughly; ensure clamps tight

ERROR: Calibration drift
→ Reading off by 0.5-1.0%
→ Fix: Calibrate at start of day

ERROR: Sampling from end of truck discharge
→ Last concrete may have lost air during transport
→ Fix: Sample from middle stream
```

**What to do if it fails:**

- Air too low: communicate with batch plant; may indicate insufficient air-entraining admixture
- Air too high: typically caused by over-mixing or excessive admixture
- Reject loads outside tolerance for critical exposure conditions

---

## E.3 Concrete Cylinder Casting (Compressive Strength Sample Preparation)

**Purpose:**

Casting cylinders is the preparation step for compressive strength testing (E.4). Cylinders are 6×12 inch (or 4×8 inch) molded concrete samples that are cured under controlled conditions and crushed at specified ages (typically 7, 14, 28, and 90 days) to verify that the concrete reached design strength.

**Plain language:** You fill cylindrical molds with samples of the concrete from the truck. Those molds are protected and shipped to a lab, where they're crushed at specific ages. The pressure required to crush them tells you how strong the concrete is.

**When to perform:**

- Every major pour of structural concrete
- One set of 4 cylinders per 50 cubic yards or per pour day, whichever is more
- A set of 4 = enough to crush at 7, 14, 28, and 90 days

**Standards:**

- ASTM C31 / C31M — Standard Practice for Making and Curing Concrete Test Specimens in the Field
- ASTM C39 / C39M — Standard Test Method for Compressive Strength of Cylindrical Concrete Specimens (the lab crushing — see E.4)

**Equipment:**

```
[ ] Cylinder molds — $5-$15 per mold
    - Plastic single-use molds (most common, disposable)
    - Or steel reusable molds
    - 6"×12" standard, or 4"×8" for some applications
    - Tight-fitting lids
[ ] Tamping rod — same as slump test
[ ] Mallet for tapping
[ ] Strike-off tool (trowel or float)
[ ] Marker (Sharpie) for labeling
[ ] Curing box or shaded location
[ ] Wet burlap or moist towels for initial cure
[ ] Plastic wrap or wet cloth covering
[ ] Cooler or insulated container (optional, for transport)
[ ] Clipboard with labels and forms
```

Cost per set of 4 cylinders: about $40 in molds plus $20 in supplies = $60 per pour event.

**Safety considerations:**

- Same as slump test
- Cylinder transport: cured cylinders are heavy (15-20 lb each)

**Pre-test setup:**

```
[ ] Prepare 4 molds per set
[ ] Pre-label each mold with:
    - Project name
    - Pour date
    - Truck number
    - Cylinder set number
    - Test age (7d, 14d, 28d, 90d)
    - Cylinder number (1 of 4, 2 of 4, etc.)
[ ] Set molds on a level, stable surface
[ ] Position near where slump test is being run (same location)
```

**Procedure:**

```
1. Sample concrete:
   - Same source as slump and air tests (middle of truck discharge)
   - Use a wheelbarrow or large bucket to hold the sample
   - Take enough for 4 cylinders (about 0.5 cubic feet)
   - Mix briefly with shovel to ensure uniformity within sample

2. Fill cylinder molds in TWO layers (for 4×8 cylinders) OR THREE layers (for 6×12 cylinders):
   
   PER LAYER (whether 2 or 3 layers):
   - Fill the mold approximately equally
   - Tamp 25 times (for 4" cylinders) or 25 times per 1/3 of the area (for 6" cylinders)
   - Tap mold sides 10-15 times with the rod or mallet to release entrapped air
   - Final layer: slightly overfill

3. Strike off top:
   - Use a trowel or strike-off bar
   - Smooth the top surface flush with the mold rim
   - Top should be flat for proper compressive testing later

4. Cap the mold:
   - Press the lid on tight
   - Verify no leaks at the lid edge

5. Label the cylinder:
   - Project name
   - Date and time
   - Truck number
   - Cylinder number and set
   - Test age (7d, 14d, 28d, 90d)
   - Initials of person casting

6. Initial curing (first 16-72 hours):
   - Keep cylinders in a stable, moderately warm location
   - Target temperature: 60-80°F
   - Avoid temperature extremes
   - Avoid vibration or jarring (the cylinders are still curing)
   - Avoid direct sunlight (can overheat)
   - Cover with wet burlap or moist cloth to prevent surface drying

7. Transport to lab:
   - After 24-48 hours (cylinder is hardened enough to handle)
   - Pack carefully (foam padding, secure containers)
   - Maintain moist conditions during transport
   - Deliver to the testing lab the same day

8. Lab handles cylinders for the rest of their life:
   - Standard moist-cure conditions (100% humidity, 73°F)
   - Cylinders crushed at scheduled ages
   - Strength results sent back as report
```

**Data recording:**

```
CYLINDER CASTING RECORD:

Pour: ____________________________________
Date: ______________  Time: __________
Truck #: __________
Cylinder set: __________
Mix design: ____________________________________
Slump at time of casting: ______ inches
Air content (if measured): ______ %
Concrete temperature: ______ °F
Number of cylinders cast: ______
Test ages requested: 7d, 14d, 28d, 90d (other: ________)

Lab receiving cylinders: _____________________________
Date delivered to lab: __________
Operator: _____________________________
```

**Pass/fail criteria:**

The cylinders themselves don't pass or fail. They produce results in the lab (E.4 below) that pass or fail. The casting itself must meet ASTM C31 — proper sample technique, proper curing, intact molds.

**Common errors:**

```
ERROR: Inadequate consolidation
→ Voids in cylinder; lab strength readings low (false fail)
→ Fix: Tamp 25 times per layer; tap sides

ERROR: Top not struck off level
→ Lab cuts/grinds top before testing, but uneven top means lab work
→ Fix: Trowel level

ERROR: Mold leaks during initial cure
→ Concrete dries out from top; weakens cure
→ Fix: Tight lids; covered storage

ERROR: Cylinders dropped or jarred during initial cure
→ Internal cracks form; lab strength low
→ Fix: Stable storage location

ERROR: Cylinders left in sun
→ Temperature spikes; cure improper
→ Fix: Shaded, controlled-temperature storage

ERROR: Cylinders frozen
→ Concrete may not have reached enough strength to resist freezing
→ Fix: Don't pour in freezing weather without protections; if cold, store cylinders heated

ERROR: Mislabeled cylinders
→ Lab can't connect cylinder to pour
→ Fix: Label with full information; verify before sending to lab

ERROR: Long delay before lab delivery
→ Curing conditions outside laboratory standard from too long
→ Fix: Deliver within 24-48 hours
```

**What to do if it fails:**

The casting itself rarely "fails" if procedures are followed. Issues typically appear in lab results (E.4).

If a mold cracks or leaks before transport:
- Remove and re-cast on a fresh sample
- Document the issue in the project log

---

## E.4 Compressive Strength Test (Lab Procedure)

**Purpose:**

The compressive strength test crushes a cured cylinder to determine its compressive strength in psi (or MPa). This is the most fundamental concrete strength measurement. The 28-day strength is the design parameter most concrete is specified by; later ages confirm continued strength gain.

**Plain language:** The lab puts your cylinder in a giant press and squeezes until it crushes. The pressure at the moment of failure is the compressive strength. Higher number = stronger concrete.

**Note: This test is run BY THE LAB.** The owner-builder's role is casting cylinders (E.3), submitting them, and interpreting the results report. This subsection covers what you receive from the lab and how to interpret it.

**When to perform:**

- 7 days after pour (for early indication)
- 14 days after pour (for intermediate progress)
- 28 days after pour (the design strength milestone)
- 90 days after pour (for long-term verification, especially with pozzolanic mixes)

**Standards:** ASTM C39 / C39M — Standard Test Method for Compressive Strength of Cylindrical Concrete Specimens

**Equipment (lab's responsibility):**

- Calibrated compression testing machine (rated to 250,000 lbs or higher)
- Calipers for measuring cylinder dimensions
- Sulfur or unbonded caps for end preparation
- Calibration verification records

**The lab's procedure (for reference):**

```
1. Remove cylinder from curing room
2. Measure diameter and length (verify it matches the order)
3. Cap the ends (sulfur capping or unbonded neoprene caps) to ensure even loading
4. Place in compression testing machine
5. Apply load at controlled rate (20-50 psi per second)
6. Continue until cylinder fractures
7. Record:
   - Maximum load applied (lbs)
   - Cross-sectional area (square inches)
   - Calculate compressive strength: f'c = Load / Area
8. Photograph the failure pattern (helps identify any anomalies)
9. Issue report
```

**Interpreting lab results:**

The lab returns a report with:

```
LAB REPORT FORMAT (typical):

Sample ID: __________ (the cylinder you submitted)
Date cast: __________
Date tested: __________
Age at test: ______ days
Diameter: ______ inches
Cross-sectional area: ______ sq inches
Maximum load: ______ lbs
Compressive strength: ______ psi
Failure pattern: ______ (Type 1, 2, 3, 4, 5, or 6 per ASTM C39)
Notes: _____________________________
```

**Pass/fail criteria:**

For this design's pozzolanic high-performance mix:
- 7-day target: 50-60% of design strength (~2,500-3,000 psi for 5,000 psi design mix)
- 14-day target: 70-80% of design strength (~3,500-4,000 psi)
- 28-day target: 100%+ of design strength (5,000 psi minimum)
- 90-day target: 110-130% of design strength (5,500-6,500 psi)

The pozzolanic mix continues gaining strength longer than typical Portland-cement-only concrete, so 90-day strength is meaningfully higher than 28-day.

**ACI 318 acceptance criterion** (the formal code-based criterion):
- Average of any 3 consecutive strength tests ≥ design strength (f'c)
- No individual test more than 500 psi below f'c (for designs ≤ 5,000 psi)

For residential, individual test results matter more than averages (you typically don't have many tests). Pass criterion in practice:
- 28-day strength meets or exceeds design (5,000 psi for this design)
- Multiple cylinders from same pour show consistency (within 10% of each other)
- 90-day strength continues gaining

**Failure pattern interpretation (from ASTM C39 visual catalog):**

- **Type 1** — well-formed cone on one or both ends — IDEAL fracture pattern
- **Type 2** — well-formed cone on one end, vertical cracks through cap — GOOD
- **Type 3** — columnar vertical cracking through both ends, no cones — ADEQUATE but suggests testing issue
- **Type 4** — diagonal fracture — SUGGESTS LOADING ISSUE
- **Type 5** — side fractures at top or bottom — SUGGESTS CAPPING ISSUE
- **Type 6** — similar to Type 5 but extending — SUGGESTS CAPPING ISSUE

For interpretation: Type 1 and 2 are normal. Types 3-6 suggest the test had issues; the strength reading may not be reliable. Discuss with the lab.

**What to do if it fails:**

If 28-day strength is below design:

1. **Verify the test was valid:**
   - Was the cylinder properly cast (E.3)?
   - Was the cylinder properly cured?
   - Was the lab procedure proper?
   - Failure pattern Type 1 or 2?

2. **If the test seems valid:**
   - Don't panic — strength continues gaining for pozzolanic mixes
   - Wait for 56-day or 90-day test
   - If multiple cylinders all read low, structural concern

3. **If multiple cylinders are below design at 28 days:**
   - Communicate with structural engineer
   - Communicate with concrete supplier
   - Possible analysis options:
     - Core sampling of the actual structure (drill out a sample, test it)
     - Non-destructive testing (Schmidt hammer, ultrasonic)
     - Load testing of the structure
     - Acceptance based on actual loads (sometimes design strength is conservative)
   - In severe cases: structural strengthening (added rebar, jacketing, etc.)

4. **Document everything:**
   - The strength readings
   - The lab report (including failure type)
   - The investigation
   - The acceptance decision
   - Cross-references to mix design and batch tickets

This documentation matters at resale (showing the engineering acceptance) and for any future structural questions.

---

## E.5 Flexural Strength Test (For Slab Verification)

**Purpose:**

Compressive strength is the standard measure but doesn't fully capture how concrete performs in slabs and beams, where bending (flexure) governs. The flexural strength test measures the concrete's resistance to bending, expressed as the modulus of rupture (MR). For slabs in this design, this is a more relevant strength measure than compressive strength alone.

**Plain language:** A small concrete beam is supported at two points and loaded at two more points until it cracks across the bottom. The pressure at cracking, divided by the beam dimensions, gives the flexural strength.

**When to perform:**

- For slab pours where flexural performance is critical
- Optional for foundation pours if compressive strength is the design parameter
- Required for fiber-reinforced concrete (where flexural performance is the design goal — see E.6)

**Standards:** ASTM C78 — Standard Test Method for Flexural Strength of Concrete (Using Simple Beam with Third-Point Loading)

**Equipment:**

```
[ ] Beam molds — $25-$60 per mold
    - 6 × 6 × 21 inch standard
    - Plastic or steel
[ ] Same tamping, finishing, labeling tools as cylinder casting
[ ] Lab equipment (lab's responsibility):
    - Flexural testing machine with third-point loading apparatus
    - Calibrated and certified
```

**Procedure:**

The owner-builder's role is casting beams (similar to cylinders but rectangular). The lab does the actual flexural test.

For casting:

```
1. Sample concrete (same as cylinder casting)

2. Fill beam mold in two layers:
   - Each layer roughly equal
   - Tamp with rod (1 stroke per 2 square inches of layer area)
   - Tap sides to release entrapped air

3. Strike off and finish top

4. Label and protect

5. Cure same as cylinders

6. Transport to lab
```

The lab procedure (for reference):

```
1. Place beam on supports (15 inches apart for 6×6×21 beam)
2. Apply load at two points, equally spaced from supports (5 inches from each support)
3. Increase load until beam fractures
4. Record peak load
5. Calculate modulus of rupture:

   MR = (3 × P × L) / (2 × b × d²)
   
   Where:
   - MR = modulus of rupture (psi)
   - P = peak load (lbs)
   - L = span between supports (inches)
   - b = beam width (inches)
   - d = beam depth (inches)
```

**Pass/fail criteria:**

Typical flexural strength values:
- For 5,000 psi design compressive strength: flexural strength typically 600-800 psi
- Rule of thumb: flexural strength ≈ 7.5 × √(f'c)
- For 5,000 psi: 7.5 × √5000 = 530 psi minimum, 750 psi typical

Project specifications should state the target flexural strength explicitly.

**What to do if it fails:**

Same as compressive strength failure:
- Verify test validity
- Investigate the mix and curing
- Consider non-destructive verification of in-place strength
- Engage structural engineer for resolution

---

## E.6 Fiber-Reinforced Concrete Test (Critical for This Design's Floors)

**Purpose:**

This design uses steel + polypropylene fiber reinforcement in floor slabs (per Section 4). Fiber-reinforced concrete has different failure behavior than plain concrete: after the concrete cracks, the fibers carry load across the crack, providing post-crack ductility (the ability to deform without complete failure). The standard flexural test (E.5) measures only the peak load; for fiber-reinforced concrete, what matters is also the **residual strength at specified deflections after cracking**.

**Plain language:** Same flexural beam test as E.5, but with fiber-reinforced concrete, the lab also measures how much load the beam continues to carry after it cracks. A plain concrete beam fails completely at peak load; a fiber-reinforced beam keeps carrying load through fiber bridging across the crack.

**When to perform:**

- Required for verification of fiber dosing in floor slab pours
- One set of beams per major slab pour (multiple in series for high-importance areas)

**Standards:** ASTM C1609 / C1609M — Standard Test Method for Flexural Performance of Fiber-Reinforced Concrete (Using Beam With Third-Point Loading)

**Equipment:**

```
Owner-builder casting:
[ ] Beam molds — same as E.5
[ ] Same tamping, finishing tools

Lab testing (responsibility of lab):
[ ] Closed-loop deflection-controlled flexural testing machine
[ ] Linear variable differential transformer (LVDT) for deflection measurement
[ ] Data acquisition system
```

This test requires more sophisticated lab equipment than the standard C78 flexural test. Verify the lab can run C1609 before submitting samples — not all general construction labs do.

**Procedure (owner-builder casting):**

Same as E.5 with one critical addition:

```
1. BEFORE filling mold, verify fiber dose:
   - The mix design specifies fiber dose (typically 25-40 lb/cy of steel fibers + 1-3 lb/cy of polypropylene)
   - Confirm with batch ticket
   - Visual inspection: fibers should be uniformly distributed in fresh concrete (no clumps, no visible separation)

2. Cast beams as in E.5

3. Note any unusual fiber behavior:
   - Fiber clumps ("hedgehogs") — indicate poor mixing
   - Fibers floating to surface — indicate too-wet mix
   - Fibers settling — indicate too-stiff mix
   - Document any issues
```

The lab procedure (for reference):

```
1. Test setup same as C78 (third-point loading)

2. Apply load while monitoring deflection
   - Continue past peak load
   - Continue measuring as the beam deflects further
   - Record load at:
     - First-crack deflection (typically L/600 or 1/100 inch for 18 inch span)
     - L/600 deflection (post-peak)
     - L/150 deflection (continued post-peak)

3. Calculate:
   - First-peak strength (similar to C78 modulus of rupture)
   - Equivalent flexural strength (post-peak load / first-peak load × 100%)
   - Toughness (area under the load-deflection curve)
```

**Data recording:**

```
FIBER-REINFORCED CONCRETE TEST:

Pour ID: ____________________
Mix design fiber dose: ____ lb/cy steel; ____ lb/cy polypropylene
Verified on batch ticket: [ ] Yes

Beam dimensions: ___ × ___ × ___ inches
First-peak strength: ______ psi
Residual strength at L/600: ______ psi
Residual strength at L/150: ______ psi
Equivalent flexural ratio (Re,3): ______ %
Toughness: ______ in-lb

Pass/fail per project specifications: [ ] Pass  [ ] Fail
```

**Pass/fail criteria:**

For typical fiber dose (35 lb/cy steel + 1.5 lb/cy poly):
- First-peak strength: 600-900 psi (typical)
- Residual strength at L/150: 30-50% of first-peak (Re,3 of 30-50%)
- Toughness: significantly higher than plain concrete

Project specifications should state explicit thresholds. Work with the structural engineer to establish acceptance values appropriate to the slab design.

**Common errors:**

```
ERROR: Inadequate fiber dose
→ Reduced post-crack performance
→ Detected by low residual strength readings
→ Fix: Verify dose at the batch plant; communicate with supplier

ERROR: Fiber clumps
→ Localized over-reinforcement and weak adjacent areas
→ Detected by inconsistent test results between beams
→ Fix: Better mixing at the plant

ERROR: Wrong fiber type
→ Polypropylene-only or steel-only mix when both were specified
→ Different post-crack behavior
→ Detected by visual inspection of cross-sections after testing
→ Fix: Verify fiber type at the batch plant
```

**What to do if it fails:**

For floor slab fiber concrete:
- Fiber failure is rare if mix design is followed
- If it does fail, structural review is needed
- Possible remedies:
  - Strengthen with topping (additional reinforcement and concrete)
  - Accept with reduced load capacity
  - In extreme cases: replace the slab section

Document all results with the structural engineer's review and acceptance.

---

## E.7 Concrete Pour Quality Control — Integrated Workflow

**Purpose:**

This is the integrated procedure that combines all the concrete tests (E.1 through E.6) into the actual workflow at a real pour. The individual tests are run in sequence and combined with documentation, photography, and decision-making.

**Plain language:** When the trucks arrive and pour begins, here's the sequence to follow so all the testing happens efficiently and the documentation is complete.

**When to perform:**

Every major concrete pour:
- Foundation pour
- Wall grouting
- Slab pours (each level)
- Topping slabs

**Equipment:** All equipment from E.1-E.6, plus:

```
[ ] Camera (smartphone OK) for documentation photos
[ ] Project clipboard with all forms
[ ] Tape measure for verifying placement
[ ] Pen, markers
[ ] Thermometer for concrete temperature
[ ] Watch for timing
[ ] Cooler with water for crew (long pours)
[ ] Cleanup supplies (water, brushes, rags)
```

**Pre-pour preparation (1-3 days before):**

```
[ ] Verify mix design and pour schedule with supplier
[ ] Confirm pumper truck if needed
[ ] Verify all forms and rebar inspection passed
[ ] Verify all embeds (sleeves, conduit, anchors) in place
[ ] Verify weather forecast (no rain in next 24 hours; temperature 40-90°F preferred)
[ ] Pre-position all testing equipment near the pour location
[ ] Pre-label cylinder molds and beam molds
[ ] Brief any helpers on their role
[ ] Print all test forms (Appendix F)
[ ] Ensure cleanup water available
```

**Day-of pour workflow:**

```
PRE-POUR (just before first truck):

[ ] Photo: Forms ready, rebar in place, embeds visible
[ ] Verify weather is acceptable
[ ] Tools and forms in place
[ ] Notebook: starting time, weather, pour ID

EVERY TRUCK:

[ ] Note arrival time
[ ] Photograph batch ticket (Truck #, time, mix, amount)
[ ] Verify mix design matches order
[ ] Sample for slump test (E.1)
[ ] Take air content reading if specified (E.2)
[ ] Note concrete temperature with thermometer
[ ] Truck driver notes any water added on-site
[ ] If first truck or designated test trucks: cast cylinders (E.3) and beams if applicable (E.5/E.6)

DURING PLACEMENT:

[ ] Verify concrete is being placed and consolidated properly
[ ] No segregation (rocks separating from paste)
[ ] Vibrating (if applicable) is per spec (avoid over-vibration)
[ ] Concrete reaches all corners and embeds
[ ] No water added to surface during finishing

DURING FINISHING:

[ ] Photo: pour in progress
[ ] Verify finishing per spec (broomed, troweled, polished, etc.)
[ ] No additions of water on the surface
[ ] No premature foot traffic

POST-POUR:

[ ] Cylinders moved to initial cure location
[ ] Curing measures in place (wet burlap, plastic, curing compound, sealed concrete)
[ ] Photos: completed pour
[ ] All forms completed
[ ] Total cubic yards verified against estimate

NEXT-DAY:

[ ] Cylinders inspected for proper hardening
[ ] Cylinders to lab if 24-48 hours old
[ ] Pour log completed with notes
```

**Data recording (master log):**

```
CONCRETE POUR LOG:

Pour ID: ____________________________________
Date: ______________
Pour location: ____________________________________
Total cubic yards: ______
Mix design: ____________________________________
Concrete supplier: ____________________________________

Truck #1:
- Arrival: ______
- Slump: ______ in (target ____ ± 1 in)
- Air content: ______ % (if measured)
- Concrete temp: ______ °F
- Water added on-site: ______ gal
- Cylinders cast? [ ] Yes  [ ] No
- Beams cast? [ ] Yes  [ ] No

Truck #2:
[same fields]

[continue for each truck]

Pour started: ______
Pour completed: ______
Curing method: ____________________________________
Crew: ____________________________________
Notes / issues: ____________________________________

Cylinders sent to lab: [ ] Yes  Date: ______
Lab name: ____________________________________

Photos archived: [ ] Yes
```

The completed pour log goes in the project binder with all batch tickets, slump test records, and eventual lab strength reports stapled together.

---

## E.8 In-Place Concrete Testing (For Existing or Just-Cast Concrete)

**Purpose:**

After concrete is cured, sometimes verification is needed without crushing cylinders. In-place testing methods give an estimate of strength of the actual installed concrete (not just the lab samples).

**When to perform:**

- When cylinder results are unexpected
- For older concrete being verified
- For acceptance after suspect pour conditions

**Methods:**

**E.8.1 Schmidt Hammer (Rebound Hammer):**

A spring-loaded hammer is pressed against the concrete surface; the rebound is measured. Higher rebound = harder concrete = higher strength (estimated).

```
Equipment: Schmidt hammer — $300-$1,500
Procedure:
1. Calibrate against the manufacturer's anvil
2. Press against clean, smooth concrete surface
3. Take 10-15 readings in a small area
4. Discard outliers, average remaining
5. Convert rebound number to estimated strength using calibration curve

Accuracy: ±15% typical. For estimation, not certification.
```

**E.8.2 Ultrasonic Pulse Velocity (UPV):**

A pulse of high-frequency sound is sent through the concrete; the time to traverse a known distance gives the pulse velocity. Faster velocity = denser concrete = higher strength (estimated).

```
Equipment: UPV tester — $1,500-$5,000
Procedure:
1. Apply transducers to opposite sides of concrete element
2. Measure time of pulse transit
3. Calculate velocity (distance / time)
4. Convert to estimated strength using calibration curve

Accuracy: ±10-15% typical. Better than Schmidt hammer.
```

**E.8.3 Core Sampling:**

A diamond core drill removes a cylindrical sample from the cured concrete. The core is then crushed in a lab.

```
Equipment: 
- Diamond core drill — rented, $200-$500/day
- 3-inch or 4-inch diamond bit — $200-$500
- Water supply for cooling
- Lab to test the core

Procedure:
1. Mark the location on the structure
2. Set up the core drill
3. Drill while running cooling water
4. Extract the core (typically 6-12 inches long)
5. Patch the hole with non-shrink grout
6. Send core to lab for compressive strength testing

Accuracy: most accurate of the in-place methods (essentially equivalent to a cylinder test, but on concrete that actually went into the building)
```

Cores are the gold standard for resolving disputes about in-place strength. They are also destructive — you're drilling into your structure. Used sparingly.

**E.8.4 Maturity Method:**

If the temperature of the concrete during curing is monitored, the maturity method estimates strength based on temperature × time. Useful for early-age decisions (when can forms be removed, when can we apply load).

```
Equipment: Concrete temperature data loggers — $50-$200 each
Procedure:
1. Embed temperature loggers in the pour
2. Record temperature over time
3. Calculate maturity index (typically Nurse-Saul or Arrhenius)
4. Estimate strength from maturity using mix-specific calibration

Accuracy: depends on calibration; ±10-15% with proper calibration.
```

**When to use which method:**

- Estimating early-age strength: maturity method
- Routine verification: Schmidt hammer
- Better non-destructive: UPV
- Authoritative verification: core sampling
- Decision support: any of the above

In-place testing is rarely needed for residential concrete unless cylinder results are unexpected. Maturity is most useful for decision-making during construction (form stripping, slab loading).

---

*End of Appendix E Part 1 — Concrete Testing*

*Part 2 (Soil and Geotechnical Testing) continues with the procedural counterpart to Section 14 — DCP, hand auger sampling, pocket penetrometer, field soil identification.*
