# Appendix E — Testing Procedures (continued)

*Part 3: Envelope and Air Quality Testing*

This part covers the tests that verify the building envelope is performing as designed and that the air inside the home is safe and healthy. The envelope tests verify the design's airtightness, insulation, and moisture-management goals are actually achieved in construction. The air quality tests verify that the conditioned air the occupants breathe is safe and within acceptable parameters.

The tests progress from envelope verification (during/after construction) to ongoing air quality monitoring (during occupancy):

- **E.21** — Blower Door Test (the master airtightness measurement)
- **E.22** — Smoke Pencil and Air Leakage Visualization
- **E.23** — Thermal Imaging Walkthrough (with the FLIR ONE)
- **E.24** — Hot Box Envelope Testing (DIY R-value verification)
- **E.25** — Indoor Air Quality Monitoring (CO, CO₂, VOC, PM2.5)
- **E.26** — Radon Testing
- **E.27** — Water Quality Testing
- **E.28** — Mold and Moisture Inspection

Same 11-element format as Parts 1 and 2.

---

## E.21 Blower Door Test (Airtightness Measurement)

**Purpose:**

The blower door test measures the airtightness of the building envelope. A calibrated fan installed in an exterior door creates a pressure difference between inside and outside. The amount of air the fan must move to maintain a standard pressure (50 Pascal) tells you how leaky the envelope is. The result is reported as **CFM50** (cubic feet per minute at 50 Pa) and **ACH50** (air changes per hour at 50 Pa) — the airtightness numbers used universally in building science.

**Plain language:** A big calibrated fan blows air out of (or into) your house through an open door. The fan controls the inside pressure relative to outside. The amount of air the fan has to push to maintain that pressure tells you how leaky the house is. Tight house = low airflow needed. Leaky house = high airflow needed.

**When to perform:**

- **Pre-drywall** (recommended) — after air sealing complete, before drywall hides everything. This is the diagnostic test where you find and fix leaks while they're easy to access.
- **Final / certificate of occupancy** — required by Oregon code. ACH50 ≤ 3.0 currently required; this design targets ≤ 1.0.
- **Annually** (optional) — track envelope performance over time
- **Post-renovation** (optional) — verify new work didn't compromise envelope

**Standards:**

- ASTM E779 — Standard Test Method for Determining Air Leakage Rate by Fan Pressurization
- ASTM E1827 — Standard Test Methods for Determining Airtightness of Buildings Using an Orifice Blower Door (alternative)
- Building Performance Institute (BPI) protocols
- RESNET Standards (residential energy services network)

**Equipment:**

```
RENT (preferred for one-time test) or BUY (if multiple builds planned):

[ ] Blower door fan and frame — $2,500-$5,000 to buy; $100-$200/day to rent
    - Industry standard: Minneapolis Blower Door (Energy Conservatory)
    - Alternative: Retrotec
    - Includes adjustable frame for door opening, fan, control
    
[ ] Manometer (digital pressure gauge) — included with rental
    - Measures pressure difference (Pascal)
    - And fan flow (CFM)
    - Some have built-in calculations
    
[ ] Software / data recorder — included with rental
    - TECTITE (Energy Conservatory) or Retrotec FanTesticPro
    - Records test results, calculates ACH50

OPTIONAL:

[ ] Smoke pencil for leak detection during depressurization (E.22)
[ ] Thermal camera for visualizing leaks (E.23)
[ ] Anemometer to verify airflow at specific leaks
[ ] Helper / observer to check for issues during test
```

**Cost to run:**
- DIY rental: $150-$300 plus a couple hours of time
- Hired (HERS rater, energy auditor): $300-$600 typically

**Safety considerations:**

```
[ ] Combustion appliances OFF before testing
   - Atmospheric (open-vented) gas appliances can backdraft when depressurized
   - Pellet stoves, wood stoves: fire out, damper closed
   - Gas water heater (atmospheric): pilot off
   - Sealed-combustion or electric appliances: not affected

[ ] Fireplaces:
   - Damper closed
   - Or seal with plastic sheeting and tape

[ ] Dryer vent closed or sealed
[ ] Range hood fan off
[ ] HVAC system off, dampers closed

[ ] Elderly or pets sensitive to pressure changes:
   - Pressure differential is mild but noticeable
   - Sensitive ears may pop briefly
   - Plan accordingly

[ ] Door must be physically secured during test
   - The frame holds the fan in place
   - Pressure can pull the frame if not secured
   - Verify before starting
```

**Pre-test setup:**

```
[ ] Building thoroughly cleaned (no dust to suck through fan)

[ ] All windows and exterior doors closed and latched

[ ] All interior doors propped open (so all rooms are at the same pressure)

[ ] HVAC dampers closed:
   - Outdoor air intake (ERV)
   - Range hood damper
   - Dryer vent damper
   - Bathroom exhaust fans (if integral dampers)

[ ] Combustion appliances:
   - All off and cool
   - Damper closed
   - Pilot lights off (if atmospheric)

[ ] Plumbing traps:
   - All filled with water
   - Floor drains capped or filled
   - Unused drains plugged

[ ] Doors and windows checked:
   - Latches engaged
   - Weatherstripping in place

[ ] Interior conditions:
   - Temperature stabilized (within 5°F of outdoor preferred)
   - No active fires or burning candles

[ ] Outdoor conditions:
   - Wind less than 15 mph (wind affects readings)
   - No precipitation
   - Air temperature not extreme

[ ] Building dimensions documented:
   - Conditioned floor area (sqft)
   - Conditioned volume (cubic feet) = floor area × ceiling height + accounting for stairs and openings
   - For multi-story: total volume of all conditioned space
```

**Procedure:**

```
INSTALLATION:

1. Choose the door for fan installation:
   - Typically the front door or another large entry
   - The door must be exterior, opening to outside
   - Adequate space for the fan frame (8-9 ft tall, 32-36 in wide door typical)

2. Install the frame:
   - Adjustable frame fits the door opening
   - Sealed at edges
   - Fan inserted into frame
   - Frame must be airtight at the door perimeter

3. Connect the manometer:
   - Inside reference: anywhere inside, generally not near the fan
   - Outside reference: outside the building, away from wind effects
   - Connect to fan controller / software

DEPRESSURIZATION TEST (the standard):

4. Set fan to depressurize the building (fan blows air OUT)

5. Increase fan speed gradually until the inside is 50 Pascal lower than outside
   - The manometer reads -50 Pa
   - Note: the Energy Conservatory rep sets the fan to -50 Pa via the test sequence

6. Read the airflow at -50 Pa:
   - This is CFM50
   - The fan controller calculates this from the fan speed and pressure characteristic

7. Calculate ACH50:
   ACH50 = CFM50 × 60 / Building Volume (cubic feet)
   
   (60 minutes per hour, divided by volume to get air changes per hour)

8. Run multiple tests at different pressure levels (per ASTM):
   - Single-point: just at -50 Pa (faster)
   - Multi-point: at -25, -50, -75 Pa or similar (more rigorous, ASTM-compliant)
   - Multi-point gives a leakage curve and a more accurate reading

9. Record results

PRESSURIZATION TEST (optional confirmation):

10. Reverse the fan (blow air INTO the building)
11. Set to +50 Pa
12. Read CFM50 (pressurization)
13. Average depress and pressurization for the most accurate result

DIAGNOSTIC PHASE (this is where you find leaks):

14. Set fan to depressurize at -50 Pa (or lower for less wind/comfort impact, like -25 Pa)

15. Walk through the building looking for air entering through leaks:
    - Use smoke pencil (E.22) to see air movement
    - Use thermal camera (E.23) to see cold air on warm surfaces
    - Hand on surface: feel for cool drafts
    - Listen at suspected leaks (often audible whistle)

16. Common leak locations:
    - Window and door perimeters
    - Electrical outlets and switches (especially on exterior walls)
    - Plumbing and HVAC penetrations
    - Recessed lights (if any)
    - Top plates of partition walls
    - Rim joists / band joists (if framed)
    - Attic hatch
    - Service layer penetrations (in this design)
    - Concrete-to-other-material transitions

17. Mark each leak found:
    - Painter's tape
    - Photograph for documentation

18. Document with photos and notes

POST-TEST:

19. Turn off the fan
20. Allow pressure to equalize (a few seconds)
21. Remove fan and frame
22. Reset all systems (open dampers, restart appliances, etc.)
23. Document the results
```

**Data recording:**

```
BLOWER DOOR TEST RECORD:

Project: ____________________________________
Date: ______________
Tester: ____________________
Test purpose: [ ] Pre-drywall diagnostic [ ] Final / CO [ ] Annual [ ] Post-renovation

Building Information:
- Conditioned floor area: ______ sqft
- Conditioned volume: ______ cubic feet
- Number of stories: ______
- Construction type: ____________________________________

Pre-test conditions:
- Outside temperature: ______ °F
- Inside temperature: ______ °F
- Wind: ______ mph
- Wind direction: ______
- Combustion appliances off: [ ] Yes
- Dampers closed: [ ] Yes
- Doors/windows closed: [ ] Yes

Test results:
- Depressurization CFM50: ______ CFM
- Pressurization CFM50: ______ CFM
- Average CFM50: ______ CFM
- ACH50: ______
- Leakage area (sq inches at 50 Pa): ______ (calculated by software)

Comparison:
- Code requirement (ORSC): ≤ 3.0 ACH50
- This design's target: ≤ 1.0 ACH50
- This building's result: ______ ACH50
- Pass code? [ ] Yes [ ] No
- Pass design target? [ ] Yes [ ] No

Major leaks identified during depressurization:
1. Location: __________________ Severity: __________
2. Location: __________________ Severity: __________
3. Location: __________________ Severity: __________
[continue]

Photos archived: [ ] Yes
Test data file archived: [ ] Yes
Test report (formal, if hired): [ ] Yes — attached
Tester signature: ____________________
```

**Pass/fail criteria:**

```
AGAINST OREGON CODE (ORSC currently):
- ACH50 ≤ 3.0 = PASS
- ACH50 > 3.0 = FAIL (cannot certify; must seal and retest)

AGAINST DESIGN TARGET (this design):
- ACH50 ≤ 1.0 = EXCELLENT (target achieved)
- ACH50 1.0-2.0 = ACCEPTABLE (above target but well within code)
- ACH50 > 2.0 = INVESTIGATE (significantly above target; find leaks)

PASSIVE HOUSE STANDARDS (for context):
- ACH50 ≤ 0.6 = Passive House certification level
- ACH50 ≤ 0.3 = Passive House Premium

INTERPRETATION:
- ACH50 of 5+ = typical 1990s construction (very leaky)
- ACH50 of 3 = current Oregon code minimum (acceptable)
- ACH50 of 1.5 = good modern construction
- ACH50 of 1.0 = this design's target (excellent)
- ACH50 of 0.6 = Passive House (very tight)
- ACH50 of 0.3 = extremely tight (rare)
```

**Common errors:**

```
ERROR: Building not at stabilized temperature
→ Stack effect (warm air rising) creates pressure differential
→ Skews readings
→ Fix: Allow 1-2 hours to stabilize before testing

ERROR: Wind too strong
→ Wind creates pressure variations
→ Single-point readings unreliable; multi-point reduces error
→ Fix: Test on calm days; use multi-point method

ERROR: HVAC running
→ Dampers and fans create artificial pressure
→ Fix: All HVAC off, dampers closed

ERROR: Plumbing traps dry
→ Sewer gas can be drawn into building during depressurization (annoying smell)
→ Fix: Fill all traps before testing

ERROR: Combustion appliances on or recently used
→ Hot flues affect readings; backdraft hazard
→ Fix: Cool down completely before testing

ERROR: Frame not sealed at door perimeter
→ Air leaks around the frame
→ Skews readings
→ Fix: Verify seal; tape edges if needed

ERROR: Single-point test taken as ASTM-compliant
→ Single-point not ASTM-compliant
→ For code compliance and certification, multi-point required
→ Fix: Use multi-point method when documentation matters

ERROR: Wrong building volume input
→ ACH50 calculated wrong
→ Fix: Verify volume calculation; include all conditioned space
```

**What to do if it fails:**

If above target (ACH50 above 1.0 for this design):

```
DIAGNOSTIC PHASE:

1. Run test in depressurization mode
2. Use smoke pencil and thermal camera to identify leaks
3. Document each leak location

PRIORITIZE LEAKS:

- Major leaks (whistling, visible smoke, large thermal signatures): fix first
- Cluster of small leaks: address as a group
- Construction details that consistently leak: review and improve

REMEDIATION:

- Caulk gaps with appropriate sealant
- Spray foam at penetrations
- Acoustic sealant at top plates
- Air seal at electrical boxes
- Replace damaged weatherstripping
- Address any failed details

RETEST:

- Run blower door again after remediation
- Verify improvement
- Continue until target achieved
- Document the chain of test → fix → retest

If above code (ACH50 > 3.0):

- Cannot pass final inspection without remediation
- Same diagnostic and remediation as above
- More aggressive measures may be needed
- Engage HERS rater or energy contractor for help
```

---

## E.22 Smoke Pencil — Air Leakage Visualization

**Purpose:**

The smoke pencil is the cheapest, simplest, most useful tool for actually FINDING air leaks during a blower door test. The blower door tells you the building is leaky; the smoke pencil tells you exactly where the leaks are. A small puff of dense smoke held near a suspected leak shows air movement immediately — sucked toward the leak (during depressurization) or pushed away (during pressurization).

**Plain language:** A pencil-shaped device that releases a thin stream of dense smoke. You hold it near suspected leaks while the building is pressure-tested. The smoke shows you the air movement. Sucked toward something? That's a leak. Stays still? Probably tight there.

**When to perform:**

- Always during a blower door test (E.21) for diagnostic purposes
- Independent investigation of suspected leaks anytime
- Verification after remediation

**Standards:** No specific ASTM standard; this is a diagnostic tool, not a quantitative test.

**Equipment:**

```
[ ] Smoke pencil — $20-$40
   - Brands: Wizard Stik, Smoke Pencil, Forensic Source
   - Single-use (loaded with smoke compound) or refillable
   - Cool smoke (no flame, no heat)
   - "Theatrical fog" or "puff bottle" alternatives also work
   
[ ] Lighter (for some types)

[ ] Notebook for marking leak locations
[ ] Painter's tape for marking
[ ] Camera for documentation
```

**Safety considerations:**

```
[ ] Smoke compound is non-toxic but can irritate eyes/lungs in concentrations
[ ] Use in well-ventilated areas (ironically — though during a blower door test the fan handles this)
[ ] Don't inhale directly
[ ] Keep away from face when activating
[ ] Smoke pencils that use mineral oil + ignition: small flame; no contact with combustibles
```

**Pre-test setup:**

```
[ ] Building under depressurization (blower door at -25 to -50 Pa is typical for diagnostic)
[ ] Smoke pencil ready
[ ] Notebook ready
[ ] Plan the systematic walkthrough (don't miss areas)
```

**Procedure:**

```
1. With building under depressurization:

2. Move systematically through each room:
   - Start at one corner, work around
   - Don't skip rooms
   - Check both exterior walls and interior walls (for inter-wall air movement)

3. At each suspected leak location:
   - Activate smoke pencil
   - Hold puff close to the surface (1-2 inches)
   - Watch the smoke

4. Observation:
   
   SMOKE PULLED INTO SURFACE = LEAK
   - Air entering from outside (during depressurization)
   - Severity proportional to how vigorously smoke is pulled
   
   SMOKE STAYS STILL = TIGHT
   - No air movement at this spot
   
   SMOKE CIRCULATES SLOWLY = MARGINAL
   - Some leak but not severe; investigate further

5. Common spots to check (pay attention to all):
   - Window perimeters (each window, all four sides + corners)
   - Door perimeters (similar to windows)
   - Electrical outlets (insert pencil tip near outlet face)
   - Light switches (similar)
   - Recessed lights (if any)
   - Plumbing penetrations (under sinks, behind toilets, around pipes through walls)
   - HVAC penetrations
   - Top plates of walls (smoke at ceiling-wall corner)
   - Fireplace surrounds (if any)
   - Attic hatch / scuttle
   - Stairs to basement
   - Door thresholds
   - Cabinetry against exterior walls
   - Corner cracks
   - Concrete-to-other-material joints
   - Framing-to-masonry transitions
   - In service layer of this design: every penetration

6. Mark each significant leak:
   - Apply painter's tape with arrow pointing at leak
   - Note severity (major / moderate / minor)
   - Photograph

7. After complete walkthrough:
   - Review the marks
   - Plan remediation
   - Document findings
```

**Data recording:**

```
SMOKE PENCIL LEAK DETECTION LOG:

Date: ______________
Tester: ____________________
Building under: -50 Pa depressurization (or other)

Major leaks identified (significant air pull):
1. Location: __________________________
   Severity: [ ] Major [ ] Moderate [ ] Minor
   Photo: [ ] Yes
   Notes: _______________________________

[continue for each leak]

Total leaks identified: ______
Major leaks: ______
Moderate leaks: ______
Minor leaks: ______

Plan for remediation: _______________________________
Next blower door test scheduled: ______________
```

**Pass/fail criteria:**

The smoke pencil itself doesn't pass or fail — it identifies leaks. The number and severity of leaks correlates to overall airtightness:

- 0-3 minor leaks: ACH50 likely ≤ 1.0
- Several moderate leaks: ACH50 likely 1.5-2.5
- Many leaks of various sizes: ACH50 likely 2.5+
- Major leaks (gushing): ACH50 likely 3.0+

**Common errors:**

```
ERROR: Inadequate smoke output
→ Hard to see air movement clearly
→ Fix: Replace smoke compound; or use higher-output pencil

ERROR: Wind through nearby openings
→ Confuses the reading
→ Fix: Test in calm conditions; close all openable openings

ERROR: HVAC fan or air filter running
→ Creates artificial air movement
→ Fix: Building should be sealed during test

ERROR: Skipping a room or area
→ Leaks missed
→ Fix: Systematic walkthrough; check off each room as completed

ERROR: Stopping at first major leak
→ Other leaks may exist
→ Fix: Complete the full walkthrough even after finding major leak
```

**What to do after finding leaks:**

For each leak, plan the remediation:

```
WINDOW/DOOR PERIMETERS:
- Caulk gaps between frame and rough opening
- Spray foam (low-expansion) for larger gaps
- Backer rod + sealant for medium gaps
- Replace damaged weatherstripping

ELECTRICAL OUTLETS:
- Install foam gaskets behind cover plates
- Caulk around boxes
- Use airtight boxes for new construction
- Spray foam around penetrations

PLUMBING PENETRATIONS:
- Spray foam around pipes
- Fire-stop sealant for pipes through floors
- Caulk at fixture mountings
- Replace failed gaskets

CONSTRUCTION DETAILS:
- Document the failure for future reference
- May indicate broader detail issues
- Consult with builder/designer if widespread

After remediation: retest with blower door to verify improvement.
```

---

## E.23 Thermal Imaging Walkthrough

**Purpose:**

Thermal imaging shows surface temperatures, which reveal envelope performance issues:
- **Cold spots on walls** = inadequate insulation or thermal bridges
- **Cold streaks** = air leaks (cold outside air entering)
- **Warm spots** = areas where heat is escaping
- **Hot spots** = electrical issues (overheated connections, etc.)

The owner already has thermal imaging capability (FLIR ONE per project context). This is one of the most valuable diagnostic tools for envelope verification.

**Plain language:** A thermal camera takes pictures showing surface temperatures as colors. Cold areas show up dark/blue; warm areas show up bright/red. By scanning walls and ceilings while there's a temperature difference between inside and outside, you can see exactly where heat is escaping or cold is entering.

**When to perform:**

- Pre-drywall (with smoke pencil during blower door — visualize air leaks)
- Final completion (verify envelope performance)
- Annually during heating season (track ongoing performance)
- After unusual events (storm damage, water leak, etc.)
- Whenever utility bills suggest envelope degradation

**Standards:**

- ASTM C1060 — Thermographic Inspection of Insulation Installation in Envelope Cavities of Frame Buildings
- ISO 6781 — Thermal insulation — Qualitative detection of thermal irregularities in building envelopes — Infrared method

These standards govern professional thermography certification (ITC Level I, II, III). Owner-builder use is informal but the principles apply.

**Equipment:**

```
[ ] Thermal camera — owner already has FLIR ONE Pro or similar — $400-$1,500
    - Smartphone-attached (FLIR ONE) or standalone (FLIR C5, etc.)
    - Resolution: 80x60 minimum, 160x120 better, 320x240 professional
    - Temperature range: -4°F to 752°F typical
    
[ ] Notebook for findings
[ ] Camera (to photograph thermal images plus visible-light context)
[ ] Optional: laser thermometer for spot-checking specific temperatures
```

**Pre-test setup:**

```
[ ] CONDITIONS REQUIRED:
   - Temperature differential of at least 18°F (10°C) between inside and outside
   - For best results: 30°F+ difference
   - In Oregon, this means winter (heating season)
   - Or summer if cooling enough below outdoor heat
   - In summer, scan AT NIGHT for similar effect

[ ] Building stabilized at indoor temperature (HVAC running normally for 12+ hours)

[ ] Avoid direct sunlight on areas being scanned (heats surfaces unevenly)

[ ] Calm weather (wind cools surfaces and skews readings)

[ ] Rain dried off (water on surfaces affects thermal readings)

[ ] Optional: combine with blower door depressurization
   - Air leaks become visible as thermal streaks
   - Dramatically more useful than thermal alone
   - Scan during depressurization
```

**Procedure:**

```
EXTERIOR SCAN:

1. With building heated (winter) or cooled (summer):

2. Walk around the exterior of the building

3. Scan each face systematically:
   - Foundation to roof
   - Window and door perimeters
   - Wall corners
   - Roof edges

4. Look for:
   - WARM AREAS (winter): heat escaping from inside
     - Whole-wall warm = inadequate insulation
     - Streaks/lines = thermal bridges through framing or fasteners
     - Spots = air leaks at penetrations
   - COLD AREAS: thermal mass or shaded
     - Some cold areas are normal (basement walls partially below grade)

5. Photograph each thermal anomaly:
   - Thermal image (with camera's thermal mode)
   - Visible-light context image
   - Note location

INTERIOR SCAN:

6. Inside the building:

7. Scan each room systematically:
   - Walls (focus on exterior walls)
   - Ceilings (especially where they meet exterior walls)
   - Floors (especially first floor over unconditioned space, slab-on-grade)
   - Window/door perimeters

8. Look for:
   - COLD AREAS (winter): air leaks or insulation gaps
     - Cold streaks at ceiling/wall corners = top-plate air leaks
     - Cold spots around outlets = box not sealed
     - Cold streaks down walls = air leaking from above
     - Whole-wall cold = inadequate insulation
   - HOT AREAS: shouldn't exist in residential walls
     - Behind appliances (normal)
     - Around recessed lights (if not IC-rated and inadequately insulated)
     - Heating equipment (normal but can show inefficiency)
     - Hot spots on outlets = electrical issue (HOT TOPIC; investigate)

9. WITH BLOWER DOOR DEPRESSURIZATION:

10. Run blower door at -50 Pa
11. Re-scan areas of concern
12. Air leaks now show dramatically:
    - Cold air entering creates obvious cold streaks
    - Specific entry points become unmistakable
    - Major thermal bridges still visible
    - Combined effect of insulation gap PLUS leak more apparent

13. Document with photos

ELECTRICAL SCAN (bonus capability):

14. With main electrical panel cover off (after disconnecting power if possible, or with covers carefully open):

15. Scan the panel:
    - Look for hot breakers (overloaded or failing)
    - Look for hot bus bars (loose connections)
    - Look for hot wires (undersized for load)
    - Document any anomalies

16. Throughout the building:
    - Outlets that are warm (electrical issue, fix immediately)
    - Switches that are warm (failing switch)
    - Light fixtures hotter than expected
```

**Interpretation guide:**

```
WINTER, EXTERIOR SCAN (warm = heat loss):

UNIFORM WALL COLOR = no major issues
WARM RECTANGLES on cold wall = inadequate insulation in those bays
WARM STRIPES along wall edges = thermal bridges through framing or studs
WARM SPOTS at penetrations = air leaks (electrical, plumbing, HVAC)
WARM EDGES at windows/doors = perimeter air leaks
WARM CEILING (visible from below or attic) = ceiling insulation gap

WINTER, INTERIOR SCAN (cold = heat loss):

UNIFORM WALL COLOR = no major issues
COLD STREAKS at ceiling/wall corner = top-plate air leak
COLD SPOTS around outlets/switches = box air leak
COLD STREAKS DOWN WALLS = air entering from above (often attic)
COLD AREAS AROUND WINDOWS = framing thermal bridge or air leak
COLD STRIPS ALONG STUDS = thermal bridge through framing (in wood-frame; less so in this design)

WITH DEPRESSURIZATION:

Cold streaks become DRAMATICALLY more visible
The leakier, the more obvious
Direction of streak = direction of air movement (always toward the leak)
```

**Data recording:**

```
THERMAL IMAGING WALKTHROUGH:

Date: ______________
Time: ______________ (note: time of day affects sun-warmed areas)
Tester: ____________________

Conditions:
- Outdoor temperature: ______ °F
- Indoor temperature: ______ °F
- Differential: ______ °F (need 18+ for useful results)
- Wind: ______ mph
- Weather: ____________________

Scan type:
[ ] Exterior survey (heating season)
[ ] Interior survey (heating season)
[ ] Combined with blower door depressurization
[ ] Electrical anomaly scan

Findings:

Anomaly 1:
- Location: __________________________
- Type: [ ] Cold spot [ ] Warm spot [ ] Air leak [ ] Thermal bridge [ ] Other
- Severity: [ ] Minor [ ] Moderate [ ] Major
- Estimated temperature: ______ °F
- Surrounding temperature: ______ °F
- Differential: ______ °F
- Photo: [ ] Thermal [ ] Visible light
- Cause hypothesis: ____________________
- Remediation needed: ____________________

[continue for each anomaly]

Total anomalies: ______
Major: ______ Moderate: ______ Minor: ______

Plan for remediation: _______________________________
Schedule for next scan: ____________________
```

**Pass/fail criteria:**

Thermal imaging itself is qualitative — no pass/fail values. But interpretation:

```
GOOD ENVELOPE:
- Walls show uniform color
- Few or no anomalies
- Maximum differential between studs and bays < 5°F
- No air leakage streaks during depressurization

ACCEPTABLE ENVELOPE:
- Some thermal bridging visible at framing
- 5-10°F differential between bays and studs
- Few minor leaks during depressurization

CONCERNING ENVELOPE:
- Major thermal bridges visible
- 10°F+ differential between bays and studs
- Multiple air leaks visible during depressurization
- Whole walls cold (inadequate insulation)

UNACCEPTABLE:
- Visible insulation gaps (large cold areas)
- Severe air leakage
- Thermal bridges connecting indoor to outdoor obviously
```

**What to do with findings:**

For inadequate insulation:
- Open the wall (if accessible) and verify insulation
- Spray foam to fill gaps
- Add insulation if cavity allows
- For severe cases: re-insulate from outside (added rigid foam) or inside (interior insulation)

For air leaks:
- Locate exactly with smoke pencil during depressurization
- Seal as in E.22

For thermal bridges:
- Often unavoidable in framed buildings (less so in this design's continuous insulation approach)
- Can be improved with continuous insulation outside
- Document for future renovations

For electrical hot spots:
- IMMEDIATE INVESTIGATION
- Could indicate failure or overload
- Disconnect circuit until evaluated
- Hire electrician for diagnostic

---

## E.24 Hot Box Envelope Testing (DIY R-Value Verification)

**Purpose:**

The R-value of an actual built wall is rarely measured. Manufacturers report R-values for materials in laboratory conditions; the as-built wall combines the materials with thermal bridging from framing, fasteners, and details. The hot box test measures the actual thermal performance of a sample of the assembled wall — the most rigorous DIY verification of design assumptions.

For this design's wall assembly (8" CMU + 4" cavity polyiso + 4" outer veneer with FRP wall ties), a hot box test verifies that the predicted R-value is actually achieved.

**Plain language:** Build a small heated chamber on one side of a wall sample. Measure the heat flowing through to the other side. Calculate the R-value from the heat flow and the temperature difference. This is the gold standard for measuring the real thermal performance of a wall as built.

**When to perform:**

- During design/development (test wall mock-up before committing)
- During construction (verify a sample wall section)
- For research/documentation (publishing on YouTube channel — relates to project's documentation goals)

**Standards:**

- ASTM C1363 — Thermal Performance of Building Materials and Envelope Assemblies by Means of a Hot Box Apparatus
- ASTM C177 — Steady-State Heat Flux Measurements (small samples in laboratory hot plate)
- ASTM C518 — Heat Flow Meter (faster lab method)

For DIY application, the principles of C1363 apply but the formality of the laboratory setup is reduced. Results aren't certifiable for code purposes but are reliable enough for design verification.

**Equipment:**

```
DIY HOT BOX:

[ ] Wooden frame (small) — $50-$200 in lumber
   - 4 ft × 4 ft × 2 ft deep typical for a wall sample
   - Or larger for larger samples

[ ] Insulation (thick foam panels lining the box) — $100-$300
   - 4-6 inches of foam on all sides except the test wall

[ ] Heating element — $50-$150
   - Electric space heater (low wattage), thermostatically controlled
   - Or ceramic heat lamp with thermostat

[ ] Temperature sensors (multiple) — $50-$200
   - Thermocouples or thermistors
   - Both inside the heated box
   - Both on the wall surfaces (heated side and cold side)
   - In the cold side ambient

[ ] Data logger — $100-$300
   - To record temperatures over time
   - Or use individual loggers (Onset HOBO, etc.) at $50-$80 each

[ ] Power meter (Kill-A-Watt or similar) — $30-$50
   - To measure energy input to the heater
   - This is the heat flowing through the wall

[ ] Wall sample — varies
   - Either built specifically (mock-up section)
   - Or a portion of the actual wall during construction (bigger setup needed)

[ ] Time and patience
   - 24-48+ hour test runs
   - Multiple trials for verification
```

Total DIY equipment: $500-$1,500.

**Safety considerations:**

```
[ ] Electrical: heater on dedicated circuit; no extension cords
[ ] Fire safety: heater and combustibles separated
[ ] Continuous monitoring of test setup (or auto-shutoff)
[ ] Temperatures kept reasonable (heat side 100-150°F max)
```

**Pre-test setup:**

```
[ ] Build the hot box:
   - Insulated chamber matching wall sample size
   - Open on the side that mates against the wall sample
   - Sealed against the wall sample
   
[ ] Mount on the wall sample:
   - Sealed perimeter (foam tape, caulk, plastic + tape)
   - No air leakage between hot box and outside (would skew results)
   - Cold side of wall is ambient outdoors or a controlled cold space

[ ] Install temperature sensors:
   - Inside the hot box (multiple to verify uniform temperature)
   - On the heated face of the wall (in contact)
   - On the cold face of the wall (in contact)
   - In the ambient outside air

[ ] Install heating element:
   - Centered in the hot box
   - Thermostat to maintain stable temperature
   - Not direct radiation onto temperature sensors

[ ] Install data logger:
   - Records all temperatures
   - Records power consumption
   - At reasonable interval (every 5-15 minutes)

[ ] Run test with no power:
   - To confirm baseline: no heating, all temperatures should equilibrate
   - Verify sensors are accurate (compare them to each other)
```

**Procedure:**

```
1. Begin test:
   - Power on heater set to maintain target temperature (typically 90-120°F)
   - Keep cold side at ambient outdoor (record outdoor temp)
   - Allow to stabilize: temperatures change slowly until reaching steady-state
   - Steady-state: takes 12-24 hours typically

2. Verify steady-state:
   - Hot side temperature constant (within 1°F over 4+ hours)
   - Cold side temperature stable
   - Heater duty cycle stable (proportion of time it runs)

3. Record steady-state values:
   - Hot box temperature (T_hot, °F)
   - Cold side temperature (T_cold, °F)
   - Hot face of wall temperature (T_wall_hot, °F)
   - Cold face of wall temperature (T_wall_cold, °F)
   - Power input to heater (P_avg, watts) — average over the steady-state period
   - Wall sample area (A, sqft)

4. Calculate R-value:
   R = (T_wall_hot - T_wall_cold) × A / (P_avg × 3.412)
   
   where:
   - 3.412 converts watts to BTU/hr
   - R-value is in ft²·°F·hr/BTU (US units)

   Example calculation:
   - Wall area: 9 sqft (3 ft × 3 ft sample)
   - Hot face of wall: 75°F
   - Cold face of wall: 35°F
   - Differential: 40°F
   - Power input: 50 watts → 170.6 BTU/hr
   - R = 40 × 9 / 170.6 = 2.11... wait, that's wrong scale
   
   Actually: R = ΔT × A / Q_thru_wall
   where Q is in BTU/hr
   
   R = (40 × 9) / 170.6 = 2.11 ft²·°F·hr/BTU per BTU passing through

   Hmm, let me re-derive:
   Heat flux q (BTU/hr/ft²) = P (BTU/hr) / A (ft²)
   q = 170.6 / 9 = 18.96 BTU/hr/ft²
   R = ΔT / q = 40 / 18.96 = 2.11 ft²·°F·hr/BTU
   
   That's a low R-value... so this example wall is not well insulated.

   For this design's wall, expected R-value:
   - 8" CMU: ~1.5
   - 4" polyiso (R-6.5/in × 4 in = 26): R-26
   - Air films: ~1
   - Thermal bridging losses (FRP ties minor): ~-0.5
   - Total expected: ~28
   
   The hot box test would verify this expected R-28 with calculation.

5. Run multiple trials:
   - Different temperatures
   - Different orientations
   - Verify consistency
```

**Data recording:**

```
HOT BOX TEST RECORD:

Project: ____________________________________
Date: ______________
Tester: ____________________

Wall sample:
- Construction: ____________________________________
- Sample area: ______ sqft
- Predicted R-value: ______ ft²·°F·hr/BTU

Test setup:
- Heating element power: ______ W
- Heat input controlled: [ ] Thermostat [ ] Constant power
- Cold side: [ ] Ambient [ ] Controlled

Steady-state values (averaged over ____ hours):
- T_hot (inside hot box): ______ °F
- T_cold (cold side ambient): ______ °F
- T_wall_hot (heated face): ______ °F
- T_wall_cold (cold face): ______ °F
- ΔT through wall: ______ °F
- Power input (avg): ______ W = ______ BTU/hr
- Heat flux: ______ BTU/hr/ft²

Calculated R-value: ______ ft²·°F·hr/BTU

Comparison:
- Predicted R-value: ______
- Measured R-value: ______
- Difference: ______ %

Interpretation:
[ ] Measured matches prediction (within 10%)
[ ] Measured below prediction (envelope underperforming — investigate)
[ ] Measured above prediction (better than predicted — verify test integrity)

Notes:
____________________________________
```

**Pass/fail criteria:**

For design verification:
- Measured R-value within 10% of predicted = PASS
- Measured R-value 10-20% below predicted = INVESTIGATE
- Measured R-value > 20% below predicted = FAIL (envelope significantly worse than designed)

Possible reasons for underperformance:
- Air leaks within the wall
- Improperly installed insulation (gaps, compression)
- Different insulation material than specified
- Thermal bridges not accounted for
- Test setup issues

**Common errors:**

```
ERROR: Heat losses through hot box walls
→ Heater works to maintain temp despite some heat loss to box exterior
→ Reads as more heat through wall than reality
→ Result: artificially low R-value
→ Fix: Insulate hot box very well; account for box losses in calculation

ERROR: Cold side temperature not stable
→ Outdoor temperature varying
→ Result: noisy data
→ Fix: Average over long period; or use a controlled cold space

ERROR: Air leakage between hot box and outside
→ Hot air escapes; replaces with cold air
→ Reads as if heat passed through wall
→ Result: artificially low R-value
→ Fix: Tightly seal hot box to wall sample

ERROR: Wall sample edges leaking heat
→ Heat lost around edges instead of through center
→ Result: artificially low R-value
→ Fix: Insulate edges around wall sample; or test only the center

ERROR: Insufficient time at steady-state
→ Temperatures still changing
→ Result: inaccurate calculation
→ Fix: 24-48+ hour test; verify stability before recording
```

**What to do if measured below predicted:**

1. Verify the test setup didn't have errors
2. Run the test again to confirm
3. If still underperforming:
   - Open up the wall (if mock-up) or thermally image the actual wall
   - Identify the source of the loss
   - Common: insulation not fully in cavity, thermal bridges, air leaks
   - Address and retest

This is a powerful test for one-time verification. Most owner-builders won't run hot box tests routinely, but for a documentation project (YouTube), it's exactly the kind of "let's verify the engineering" test that builds credibility.

---

---

## E.25 Indoor Air Quality Monitoring

**Purpose:**

Modern tight homes need active ventilation because the air doesn't naturally exchange with outdoors. The result of inadequate ventilation: CO₂ buildup, VOC accumulation, particulate concentration, humidity issues. Monitoring indoor air quality verifies that the ventilation strategy is working — and identifies problems before they become health concerns.

For this design with target ACH50 ≤ 1.0 (very tight) plus an ERV providing fresh air, IAQ monitoring confirms the engineered ventilation is delivering what's needed.

**Plain language:** Devices that continuously measure the air inside the house — how much carbon dioxide, volatile organic compounds, fine particles, humidity, etc. The numbers tell you if the air is healthy and if the ventilation is doing its job.

**When to perform:**

- After move-in to establish baseline
- Continuously (most monitors are designed for ongoing use)
- During cooking, cleaning, or any activity that affects air quality
- Seasonally (compare summer/winter)
- After any change to ventilation system

**Standards:**

- ASHRAE 62.2 — Ventilation and Acceptable Indoor Air Quality in Residential Buildings
- WHO IAQ guidelines
- EPA IAQ guidance

**Equipment options:**

```
ENTRY-LEVEL CONSUMER MONITORS — $150-$300:
[ ] Awair Element — measures CO₂, VOC, PM2.5, temperature, humidity
[ ] Airthings View Plus — adds radon (combined unit)
[ ] uHoo — adds CO, NO₂, ozone
[ ] PurpleAir — focuses on PM2.5 (popular)

PROSUMER MONITORS — $300-$800:
[ ] Airthings Wave Plus — standalone radon + IAQ
[ ] IQAir AirVisual Pro — comprehensive
[ ] Atmotube Pro — portable

PROFESSIONAL/RESEARCH GRADE — $1,000-$5,000+:
[ ] TSI DustTrak — research-grade PM
[ ] Aeroqual S200/500 — research-grade
[ ] Met One — air quality research instruments

DIY OPEN-SOURCE — $50-$300:
[ ] Build with sensor modules (SCD40 for CO₂, BME280 for T/RH/P, PMS5003 for PM)
[ ] Connected to ESP32 or Raspberry Pi
[ ] Integration with Home Assistant (matches your local-first smart home approach)
```

**Recommended for this design:**

```
HOME ASSISTANT INTEGRATION (matches design philosophy):

[ ] Sensor modules:
    - CO₂: Sensirion SCD40 or SCD41 (~$60)
    - VOC: Bosch BME680 or BME688 (~$15)
    - PM2.5/10: Plantower PMS5003 or PMS7003 (~$30)
    - T/RH: Sensirion SHT40 (~$15)

[ ] Microcontroller:
    - ESP32 board (~$15)
    - PoE-powered if wired ethernet preferred (~$30 with PoE module)

[ ] Connection: ESPHome firmware → Home Assistant
[ ] Dashboard: Lovelace cards in HA showing real-time and historical data

Total: $150-$250 per location

Multiple sensors throughout the home build a comprehensive picture.
```

**Safety considerations:**

- Most monitors are passive and safe
- Some use ionization (rare in IAQ monitors); follow manufacturer instructions
- Calibrate periodically per manufacturer (especially CO₂ which drifts)

**Pre-test setup:**

```
[ ] Choose monitor locations:
   - Bedrooms (where occupants spend the most time)
   - Living areas (where activity generates issues)
   - Kitchen (cooking creates dramatic IAQ events)
   - Mechanical room (verify ERV outputs)
   - Optional: every floor, every major room

[ ] Mount at breathing height (4-6 feet) when possible

[ ] Avoid:
   - Direct sunlight (heats sensors, drifts readings)
   - Direct airflow from vents (microclimate, not representative)
   - Right next to combustion source (anomalous readings)
   - Outside influences (windowsill in summer with breeze)

[ ] Calibrate per manufacturer:
   - CO₂ sensors often calibrate by exposing to outdoor air (425 ppm baseline)
   - VOC sensors typically self-calibrate
   - PM sensors often factory-calibrated
```

**Procedure (continuous monitoring):**

```
1. Install monitor(s) in chosen locations

2. Connect to network/Home Assistant

3. Set up data logging:
   - Record continuously
   - Sample interval: 1-5 minutes typical
   - Long-term retention (months/years of data)

4. Configure alerts:
   - CO₂ > 1000 ppm → moderate alert
   - CO₂ > 1500 ppm → high alert
   - VOC index > 200 → moderate alert
   - PM2.5 > 35 µg/m³ → moderate alert
   - PM2.5 > 55 µg/m³ → high alert
   - Humidity < 30% or > 60% → alert

5. Review data regularly:
   - Daily for the first month after move-in
   - Weekly thereafter
   - Special review during heavy cooking, cleaning, gatherings, etc.

6. Identify patterns:
   - When does CO₂ rise (closed bedrooms at night, common)
   - When does VOC spike (cleaning products, off-gassing furniture)
   - When does PM rise (cooking, candles, outdoor smoke events)
   - Correlate with ERV operation
```

**Data interpretation — typical thresholds:**

```
CARBON DIOXIDE (CO₂):
- 350-450 ppm: outdoor baseline
- 600-800 ppm: typical indoor (well-ventilated)
- 800-1000 ppm: elevated but acceptable
- 1000-1500 ppm: noticeable drowsiness, reduced cognition
- 1500-2500 ppm: poor IAQ; ventilation needed
- 2500+ ppm: severe; immediate ventilation
- 5000+ ppm: workplace exposure limit (8-hr OSHA)

ASHRAE 62.2 doesn't specify a CO₂ limit but ventilation rates are designed to keep CO₂ below ~1000-1500 ppm typically.

VOC (VOLATILE ORGANIC COMPOUNDS):
- Reading varies by sensor type
- Typical "VOC index" 0-500
- Below 100: low VOC
- 100-200: moderate (look for sources)
- 200-500: elevated (off-gassing, products in use)
- 500+: high (something happening; investigate)
- Common sources: paint, cleaning products, furniture, carpet

PM2.5 (FINE PARTICULATES):
- < 12 µg/m³: good (EPA daily AQI 0-50)
- 12-35 µg/m³: moderate (EPA AQI 51-100)
- 35-55 µg/m³: unhealthy for sensitive groups
- 55-150 µg/m³: unhealthy
- > 150 µg/m³: very unhealthy
- Common sources: cooking (especially gas/wood), candles, outdoor smoke (Oregon wildfires!)

HUMIDITY (relative):
- 30-50%: optimal range
- < 30%: too dry (skin/respiratory issues, static electricity)
- 50-60%: acceptable
- > 60%: high (mold/mildew risk over time)
- > 70%: definitely too high

TEMPERATURE:
- 68-72°F winter, 75-78°F summer: comfort range
- Beyond this: comfort issue (not health unless extreme)

CARBON MONOXIDE (CO):
- 0-9 ppm: typical (some background from outside or trace sources)
- 10-50 ppm: investigate (combustion source, attached garage)
- > 50 ppm: dangerous; evacuate and investigate

For this design, no combustion appliances inside the conditioned envelope — CO should always be very low.

NITROGEN DIOXIDE (NO₂):
- Mostly relevant if natural gas appliances present
- < 50 ppb: typical
- > 100 ppb: may aggravate respiratory issues
```

**Integration with this design:**

Pair with the ERV's operation:
- High CO₂ in bedroom at night = ERV not bringing enough fresh air to that room
- VOC spike during cleaning = expected; consider boost ventilation
- PM2.5 spike during cooking = range hood working (or not)
- All-day low CO₂ in inhabited rooms = ERV doing its job

**Common errors:**

```
ERROR: Monitor in poor location
→ Microclimate readings, not representative
→ Fix: Move to breathing height, away from direct vents/sun

ERROR: Sensor drift not addressed
→ CO₂ especially drifts over time
→ Fix: Periodic calibration (often automatic if exposed to outdoor air daily)

ERROR: Reading outliers without context
→ Spike during cooking is expected; not a problem
→ Fix: Correlate with activity logs

ERROR: Single monitor for whole house
→ Different rooms have very different IAQ
→ Fix: Multiple monitors, especially bedrooms
```

**What to do based on findings:**

For chronically high CO₂:
- Verify ERV running properly
- Increase ventilation rate (boost mode)
- Verify zone balance

For high VOC:
- Identify source (recent purchases? cleaning?)
- Increase ventilation
- Switch to low-VOC products
- Allow off-gassing time for new materials

For high PM2.5:
- During cooking: range hood needs attention or higher CFM
- From outside (wildfire season): close intakes, run filtration
- Indoors continuously: investigate (smoking? candles? fireplace?)

For high humidity:
- Verify dehumidifier operating
- Increase ventilation
- Address moisture sources

For low humidity:
- Reduce ventilation slightly
- Consider humidifier (winter)

---

## E.26 Radon Testing

**Purpose:**

Radon is a naturally-occurring radioactive gas formed by uranium decay in soil and rock. It seeps from the ground into buildings, especially basements, where it can accumulate to dangerous levels. Long-term exposure to elevated radon causes lung cancer (second-leading cause after smoking). Oregon has variable radon — some areas elevated (parts of the Willamette Valley, Eastern Oregon highlands).

For this design with a basement option, radon testing is essential. The design includes a radon vent piping system (under-slab perforated pipe rising through slab and capped, ready to be vented if needed).

**Plain language:** Radon is invisible, odorless gas from the ground that causes lung cancer. You can't smell it, feel it, or know it's there without testing. Most places have low or no radon, but some places have a lot. The only way to know is to test.

**When to perform:**

- INITIAL TEST: short-term (3-7 days) test before move-in
- FOLLOW-UP: long-term (90+ days) test for accurate annual exposure
- ANNUALLY thereafter (track changes)
- AFTER any significant change to building (new HVAC, basement renovation, etc.)
- IF MITIGATION INSTALLED: regular testing to verify it's working

**Standards:**

- EPA radon testing protocols
- ANSI/AARST MAH-2019 (Multifamily building radon testing)
- ANSI/AARST MS-PC-2015 (Mitigation standards)

**Equipment options:**

```
SHORT-TERM TESTS (3-7 days):

[ ] Charcoal canister test — $15-$30
    - Mail-in to laboratory
    - Reliable but slow turnaround (1-2 weeks for results)
    - Single-use
    
[ ] Continuous Radon Monitor (CRM) — $150-$300
    - Reusable (test as often as you want)
    - Real-time reading
    - Brands: Airthings Wave (with WiFi reading via app), Corentium, RadonEye, EcoQube
    - Tracks trends over time

LONG-TERM TESTS (3-12 months):

[ ] Alpha track detector — $30-$60
    - Mail-in laboratory analysis
    - Most accurate for annual exposure
    - Single-use
    
[ ] Continuous monitor (CRM) — same as above
    - Records 90+ days of data
    - Calculates annual averages

PROFESSIONAL/HIRED TESTING — $150-$400
    - Hire a certified radon professional
    - Required for real estate transactions (typically)
    - Detailed report
```

**Recommended for this design:**

Buy a **continuous monitor** (Airthings Wave Plus, RadonEye, or similar) — $250-$300 — and run it permanently in the lowest occupied space (basement). It will show radon levels in real-time, alert on elevations, and provide both short-term and long-term data.

**Safety considerations:**

- Radon itself is the hazard; testing isn't dangerous
- During testing: maintain "closed-house conditions" for short-term tests (no opening windows)
- Don't move the monitor during testing
- Don't put it near drains, sumps, or other potential entry points (microclimate)

**Pre-test setup (short-term test):**

```
[ ] CLOSED-HOUSE CONDITIONS for at least 12 hours before and during the test:
    - All windows closed
    - All exterior doors closed (open only briefly for entry/exit)
    - HVAC running normally (don't change settings)
    - Bath fans off (or only short use)
    - Range hood off (or only short use)

[ ] Place monitor:
    - In the lowest occupied level (basement if used, or first floor if no basement)
    - At 2-6 feet above floor
    - At least 3 feet from windows or doors
    - At least 3 feet from heat sources
    - Out of direct sunlight
    - Away from drafts
    - In a frequently-occupied room (not a closet)

[ ] Don't move once placed
[ ] Note start date/time
```

**Pre-test setup (long-term test):**

```
[ ] Same placement criteria as short-term
[ ] Closed-house conditions NOT required for long-term (test averages over time)
[ ] Note start date/time
[ ] Plan to leave for 90+ days
```

**Procedure:**

```
SHORT-TERM TEST (3-7 days):

1. Place monitor with closed-house conditions
2. Leave undisturbed for the test period
3. At end:
   - For mail-in: seal in provided container, ship to lab
   - For continuous monitor: read display, transfer data
4. Get results in 1-2 weeks (mail-in) or instantly (continuous)

LONG-TERM TEST (90+ days):

1. Place monitor (no closed-house requirement)
2. Leave for 90+ days minimum, ideally a full year
3. At end:
   - For mail-in: seal in container, ship to lab
   - For continuous monitor: review data for the full period
4. Calculate annual average exposure

CONTINUOUS MONITORING:

1. Place monitor permanently
2. Connect to network/Home Assistant if applicable
3. Review:
   - Daily readings
   - Weekly averages
   - Monthly trends
   - Seasonal variation (radon levels typically higher in winter)

4. Set alerts:
   - Above 2 pCi/L: monitor more closely
   - Above 4 pCi/L: investigate; consider mitigation
   - Above 10 pCi/L: act immediately; mitigation needed
```

**Data interpretation:**

```
RADON LEVELS (in pCi/L — picocuries per liter):

< 2 pCi/L: low — no action needed
2-4 pCi/L: borderline — consider mitigation; verify with long-term test
4 pCi/L (EPA action level): mitigation recommended
4-8 pCi/L: elevated; mitigation should be installed within months
8-20 pCi/L: high; mitigation should be installed within weeks
> 20 pCi/L: very high; mitigation immediately

In Bq/m³ (international units):
1 pCi/L = 37 Bq/m³
4 pCi/L = 148 Bq/m³ (EPA action level)
WHO recommends action above 100 Bq/m³ (~2.7 pCi/L)
```

**For this design:**

The under-slab radon vent piping (designed in Section 14.9 and Section 6) is INSTALLED but typically CAPPED. If radon testing shows elevated levels:
- Connect a fan to the vent pipe
- Fan exhausts to outside above the roof
- Creates negative pressure under the slab
- Radon is collected and exhausted before entering the building

This "radon-ready" approach means:
- No mitigation needed if levels are low
- Easy installation if levels are elevated
- No need to add piping after the fact

**Common errors:**

```
ERROR: Closed-house conditions not maintained for short-term test
→ Building under-pressurized, more outdoor radon entering
→ Result: artificially high reading
→ Fix: Maintain closed conditions; or use long-term test

ERROR: Monitor in unrepresentative location
→ Closet, hallway, or microclimate area
→ Result: not reflective of occupant exposure
→ Fix: Place in occupied area at breathing height

ERROR: Monitor moved during test
→ Disturbs reading
→ Fix: Place once; don't move

ERROR: Single short-term test taken as definitive
→ Radon varies seasonally
→ Result: spot reading not annual exposure
→ Fix: Long-term test for true annual average

ERROR: Test taken in unusual conditions
→ During HVAC malfunction, sealed building, etc.
→ Result: not representative
→ Fix: Test under typical conditions
```

**What to do if elevated:**

For 4-10 pCi/L:

```
1. Verify with second test (different season ideal)
2. Engage radon mitigation contractor (or DIY for the design's radon-ready system)
3. Install:
   - Connect fan to under-slab vent pipe
   - Run pipe through roof termination
   - Fan rated for radon mitigation
4. Test again 30 days after mitigation installed
5. Verify <2 pCi/L
6. Continue monitoring permanently
```

For 10+ pCi/L:

```
1. Move from exposed areas if possible (especially basement) until mitigation
2. Install mitigation immediately
3. Same verification as above
4. Consider mitigation system more aggressive (larger fan, multiple suction points)
```

---

## E.27 Water Quality Testing

**Purpose:**

Verify that water from the well is safe to drink, free of contamination, and within acceptable parameters for taste, odor, and equipment compatibility. Required for permit and prudent for ongoing operation.

**Plain language:** Send a water sample to a certified lab. They run a battery of tests for bacteria, minerals, and contaminants. The report tells you if the water is safe and what (if anything) needs to be treated.

**When to perform:**

- Initial test before drilling permit (some jurisdictions)
- After well drilling, before connecting to plumbing
- BEFORE move-in (verify drinking water safe)
- ANNUALLY for ongoing verification
- AFTER any unusual events (well work, flooding, neighbor contamination)
- BEFORE pregnancy (heightened concern)
- IF water taste/odor changes

**Standards:**

- EPA Safe Drinking Water Act standards
- Oregon DEQ regulations for private wells
- ANSI/NSF standards for treatment systems

**Equipment:**

```
[ ] Sample bottles (provided by lab)
[ ] Sterilization for bacteria sampling (if testing bacteria)
[ ] Cooler with ice for transport
[ ] Permanent marker for labeling
[ ] Lab order form
```

**Where to send samples:**

```
OREGON LABS THAT TEST WATER:

[ ] Edge Analytical (Eugene, OR) — full-service water lab
[ ] National Testing Laboratories (Cleveland, OH) — mail-in service available
[ ] Health Resources Lab (Salem, OR)
[ ] Pace Analytical (Portland, OR)
[ ] Underwriters Laboratories (UL) — water testing
[ ] County health departments — sometimes do limited testing for free or low cost

For bacteria specifically: most state health labs accept samples for free.
```

**Test packages (typical):**

```
BASIC BACTERIA TEST — $15-$50:
- Total coliform
- E. coli

INITIAL DRINKING WATER TEST PACKAGE — $100-$250:
- Total coliform & E. coli
- Nitrate, nitrite
- pH
- Total dissolved solids (TDS)
- Hardness
- Iron, manganese
- Lead
- Arsenic
- Copper

EXPANDED TESTING — $300-$600:
- All of the above
- Pesticides and herbicides
- Volatile organic compounds
- Radon (in water)
- Fluoride
- Sulfate
- Chloride
- Specific ions (calcium, magnesium, sodium, potassium)

SPECIALIZED TESTING — varies:
- Heavy metals panel
- Petroleum hydrocarbons (if site has industrial history)
- Radioactive elements (uranium, radium)
```

**Pre-test setup:**

```
[ ] Order test kit from lab (bottles arrive in 1-7 days)

[ ] Read instructions carefully
   - Different tests need different bottles
   - Some need sterilized bottles (don't open until time of sampling)
   - Some need preservatives (already in bottle from lab)

[ ] Schedule sampling:
   - Bacteria: must be at lab within 30 hours of sampling typically
   - Other tests: more flexibility
   - Plan shipping time

[ ] Identify sampling tap:
   - Cold water supply
   - Most commonly: kitchen tap
   - Remove faucet aerator
   - Outside tap (frost-free hose bib) is alternative
   - Avoid: tap with screen or filter; treated water if testing untreated; long-unused tap

[ ] Photo and document:
   - Tap being used
   - Time and date
```

**Procedure (bacteria sample — most stringent):**

```
1. Remove faucet aerator (where the screen is at the tap end)

2. Run cold water for 5 minutes:
   - Flushes any stagnant water
   - Brings fresh well water to the tap

3. Sterilize the tap (optional but recommended):
   - Light a match or lighter; carefully heat the tap end for a few seconds
   - Or wipe with isopropyl alcohol
   - Don't burn yourself; this is not always required (check lab instructions)

4. Run water at moderate flow for 30 seconds

5. Open sterile bottle (DON'T touch the inside or rim)

6. Fill bottle to fill line:
   - Some have specific markings
   - Don't overfill
   - Don't underfill

7. Cap immediately, seal tight

8. Don't touch the inside of the cap

9. Label with project name, date, time, location

10. Pack in cooler with ice (4°C or 39°F) for transport

11. Ship overnight to the lab to arrive within 30 hours of sampling
```

**Procedure (chemistry tests — easier):**

```
1. Remove aerator
2. Run cold water for 5 minutes
3. Open the appropriate bottle (may have preservative inside; don't dump it out)
4. Fill to specified level
5. Cap, seal, label
6. Ship to lab (chemistry tests less time-critical than bacteria)
```

**Data recording:**

```
WATER SAMPLING LOG:

Project: ____________________________________
Date sampled: ______________  Time: __________
Sampled by: ____________________

Tap location: ____________________________________
Pre-flush time: ______ minutes
Aerator removed: [ ] Yes
Sterilization: [ ] Heat [ ] Alcohol [ ] None

Tests requested:
[ ] Total coliform / E. coli
[ ] Nitrate / nitrite
[ ] Lead
[ ] Arsenic
[ ] Iron / manganese
[ ] pH / TDS / hardness
[ ] Other: ________________________

Samples shipped: ______________
Lab: ____________________________________
Tracking number: ______________

Results received: ______________
Results reviewed: [ ] Yes
Action taken: ____________________________________
```

**Data interpretation — drinking water standards:**

```
PRIMARY STANDARDS (health-based):

CONTAMINANT       | LIMIT (MCL)  | NOTES
------------------|--------------|-------
Total Coliform    | 0 / 100 mL   | ABSENT REQUIRED
E. coli           | 0 / 100 mL   | ABSENT REQUIRED
Nitrate (as N)    | 10 mg/L      | Higher = ag/septic contamination
Nitrite (as N)    | 1 mg/L       | Acute toxicity for infants
Lead              | < 15 µg/L    | Action level (no safe level for kids)
Arsenic           | 10 µg/L      | Common in some Oregon wells
Copper            | 1.3 mg/L     | Action level
Mercury           | 2 µg/L       | 
Selenium          | 50 µg/L      | 
Uranium           | 30 µg/L      | 
Radon             | 4 pCi/L      | EPA proposed; not enforceable
Pesticides        | varies       | Many specific limits
VOCs              | varies       | Many specific limits

SECONDARY STANDARDS (aesthetic/equipment):

Iron              | 0.3 mg/L     | Higher = staining
Manganese         | 50 µg/L      | Higher = black staining
pH                | 6.5-8.5      | Outside range = corrosion or scaling
TDS               | 500 mg/L     | Higher = mineral taste
Hardness          | < 120 mg/L   | Above = scale; soft = aggressive
Sulfate           | 250 mg/L     | Higher = laxative effect
Chloride          | 250 mg/L     | Higher = salty taste
Fluoride          | 4 mg/L       | Above 2 = dental staining
```

**For typical Oregon wells:**

Common findings:
- Bacteria contamination from poor well construction or surface water entry → fix sealing, disinfect, retest
- Iron and manganese (very common in Pacific NW) → treat with oxidation/filter
- Hard water → softener (optional, mostly aesthetic)
- Arsenic in some areas (Eastern Oregon especially, but not unknown elsewhere) → treat with reverse osmosis or specific arsenic removal
- Nitrates near agricultural areas → treat with reverse osmosis or relocate well

**What to do if tests fail:**

For bacteria:
1. Disinfect well (chlorine shock — DIY or hire professional)
2. Retest after disinfection
3. If persistent: investigate well construction (cracks, sealing issues, surface water entry)
4. May require well rework or new well

For elevated nitrates/arsenic/lead:
1. Determine source (well construction, plumbing, surrounding land use)
2. Install treatment system:
   - Reverse osmosis for many contaminants (whole-house or point-of-use)
   - Specific media filters (arsenic removal, lead removal, etc.)
3. Retest after treatment installed
4. Continue periodic testing to verify treatment effectiveness

For aesthetic issues (iron, hardness):
1. Optional treatment based on preference
2. Iron and manganese oxidation/filtration systems
3. Water softeners
4. Activated carbon for taste/odor

**Documentation:**

All water test results in project binder. Critical for:
- Permit compliance
- Health verification
- Resale (buyers will ask)
- Tracking changes over time

---

## E.28 Mold and Moisture Inspection

**Purpose:**

Mold growth requires three things: moisture, organic material, and time. Modern tight construction is very effective at controlling moisture, but failures (leaks, condensation, humidity) can lead to mold problems. Periodic inspection catches issues early.

**Plain language:** Look for signs of moisture problems and mold growth before they become big issues. Most are visible if you know where to look.

**When to perform:**

- Annually as routine preventive inspection
- Whenever there's a known moisture event (leak, flood, etc.)
- When moisture meter readings indicate elevated moisture
- When odors suggest mold (musty smell)
- Before resale

**Standards:**

- IICRC S520 — Standard for Professional Mold Remediation
- ASTM E2418 — Standard Guide for Readily Observable Mold and Conditions Conducive to Mold

**Equipment:**

```
[ ] Pin-type moisture meter — $40-$200
    - Measures moisture in wood, drywall, masonry
    - Two pins inserted into material; reads conductivity
    
[ ] Pinless moisture meter — $80-$300
    - Surface-scanning, non-destructive
    - Less accurate but doesn't damage finishes
    
[ ] Hygrometer for ambient humidity — $20-$80
    - Already part of IAQ monitoring (E.25)
    
[ ] Flashlight (LED, bright)
[ ] Camera (smartphone OK)
[ ] Notebook for logging
[ ] Thermal camera (E.23) — finds cold spots that cause condensation
```

**Pre-inspection setup:**

```
[ ] Plan a systematic walkthrough of all areas
[ ] Check after a wet weather period (potential leaks more visible)
[ ] Identify high-risk areas in advance:
   - Bathrooms (showers, around toilets)
   - Kitchens (under sinks, around dishwasher)
   - Laundry (around washing machine)
   - Basement (any/all surfaces)
   - Around windows
   - Near plumbing penetrations
   - Cold corners and walls
   - Mechanical rooms
```

**Procedure:**

```
SYSTEMATIC INSPECTION:

1. EXTERIOR:
   [ ] Roof: missing/damaged shingles, flashings, sealants
   [ ] Gutters: clean, properly draining
   [ ] Downspouts: discharging away from foundation
   [ ] Foundation: visible cracks, water staining
   [ ] Grade: slopes away from foundation (6 in in 10 ft min)
   [ ] Window perimeters: caulking intact
   [ ] Door perimeters: thresholds, weatherstripping
   [ ] Exterior staining patterns indicating water flow

2. INTERIOR — VISIBLE INSPECTION:
   [ ] All ceilings: water stains, discoloration, sagging
   [ ] All walls: especially exterior walls and around windows
   [ ] All floors: especially in wet areas
   [ ] All windows: condensation, frame degradation
   [ ] All exterior doors: thresholds, frames
   [ ] Around all plumbing: under sinks, around toilets, washing machine area
   [ ] Around all penetrations: HVAC, electrical
   [ ] Crawlspace (if any): moisture, vapor barrier integrity
   [ ] Attic (if applicable): roof leaks, condensation, ventilation
   [ ] Basement: especially walls, floor-to-wall joint, around penetrations

3. SMELL TEST:
   [ ] Walk through each room
   [ ] Note any musty, moldy, or unusual smells
   [ ] Stronger smells in particular areas indicate problems

4. MOISTURE METER TESTING:
   [ ] All wood components in suspect areas
   [ ] Drywall in suspect areas
   [ ] Behind/around moisture-prone fixtures
   [ ] Wood floors (especially in basements)
   [ ] Compare readings to dry baseline

5. THERMAL IMAGING (E.23):
   [ ] Look for cold surfaces that could condense moisture
   [ ] Look for thermal anomalies indicating wet insulation
   [ ] Especially: basement walls, exterior corners, window frames

6. LOOK FOR MOLD GROWTH:
   - Black, green, brown, white, orange spots
   - Often follows moisture patterns (water stains)
   - Common locations:
     - Behind drywall in wet areas
     - On wood that stayed wet
     - Behind cabinetry against exterior walls
     - In basement corners
     - Around HVAC vents (if condensate present)
     - Carpet padding under leaks

7. DOCUMENT:
   - Photos of any concerns
   - Moisture meter readings
   - Smell observations
   - Description of conditions
```

**Moisture meter readings — interpretation:**

```
WOOD:
- Below 12%: dry, normal
- 12-15%: slightly elevated; monitor
- 15-20%: wet; investigate
- 20%+: saturated; immediate concern

DRYWALL (paper-faced gypsum):
- Below 1%: normal
- 1-5%: slightly elevated
- 5-10%: wet; investigate
- 10%+: saturated; possible damage

MASONRY/CONCRETE:
- Surface readings less reliable
- Use comparison readings (dry area vs. suspected wet area)
- Significant difference indicates moisture issue
```

**What to look for:**

```
MOISTURE PROBLEMS (precursor to mold):
- Water staining on surfaces
- Bubbling/peeling paint
- Staining at floor-wall joints
- Condensation on surfaces
- Wet smell
- Soft or warped wood
- Discolored grout
- Efflorescence on masonry (white powder = moisture migration)

MOLD GROWTH (the problem itself):
- Visible colonies (any color)
- Fuzzy or slimy texture
- Strong musty odor
- Health symptoms in occupants (sneezing, headaches, breathing issues)
- Allergic reactions in suspected areas
```

**Pass/fail criteria:**

For routine inspection:
- No visible mold AND no moisture meter readings above threshold AND no musty odors = PASS
- Any of the above present = INVESTIGATE

**What to do if found:**

```
SMALL MOLD AREAS (less than 10 sqft):
- Identify and fix the moisture source
- Clean with detergent and water (or specific mold-remediation cleaners)
- Dry thoroughly
- Replace any porous materials that can't be cleaned (drywall, carpet padding)
- Monitor area after remediation

LARGE MOLD AREAS (> 10 sqft):
- Hire IICRC-certified mold remediation contractor
- Address moisture source
- Containment to prevent spore spread
- Professional remediation
- Verification testing after remediation
- Reconstruct affected areas

ANY MOLD WITH HEALTH IMPACT:
- Move occupants out until remediated
- Hire professional remediation
- Air quality testing post-remediation

MOISTURE WITHOUT MOLD:
- Find and fix the source IMMEDIATELY
- Mold can grow within 24-72 hours of moisture
- Dry the affected area within 48 hours

PERSISTENT HUMIDITY ABOVE 60%:
- Verify HVAC dehumidification working
- Add dedicated dehumidifier if needed
- Increase ventilation
- Address any chronic moisture sources
```

**Documentation:**

For project binder:
- Annual inspection results
- Moisture meter readings (with locations)
- Photos
- Any issues found and remediation taken

---

## E.29 Comprehensive IAQ Annual Verification

**Purpose:**

Once the home is occupied, an annual integrated air quality and envelope verification confirms continued performance. Combines several of the previous tests into a yearly checklist.

**When to perform:** Annually, ideally on the anniversary of move-in.

**Procedure:**

```
ANNUAL HOME PERFORMANCE CHECK:

[ ] BLOWER DOOR TEST (E.21):
   - Compare ACH50 to baseline
   - If degraded: investigate and remediate
   - Target: maintain within 10% of original

[ ] SMOKE PENCIL WALKTHROUGH (E.22):
   - Identify any new leaks
   - Address as found

[ ] THERMAL IMAGING (E.23):
   - Heating-season scan
   - Look for new thermal issues
   - Document any changes

[ ] IAQ MONITORING REVIEW (E.25):
   - Year of data
   - Look for trends
   - Address any chronic issues

[ ] RADON REVIEW (E.26):
   - Annual average from continuous monitor
   - Confirm levels acceptable

[ ] WATER QUALITY TEST (E.27):
   - Annual basic test (bacteria + nitrate + lead minimum)
   - Compare to previous

[ ] MOLD INSPECTION (E.28):
   - Walkthrough of all spaces
   - Moisture readings in suspect areas
   - Address any concerns

[ ] HVAC PERFORMANCE:
   - Filter changes per schedule
   - System operation verified
   - Any issues addressed

[ ] DOCUMENTATION:
   - All results in project binder
   - Compare year-over-year
   - Plan any maintenance/upgrades
```

The annual review takes 1-2 days of dedicated effort but provides ongoing assurance that the home is performing as designed.

---

*End of Appendix E Part 3 — Envelope and Air Quality Testing*

*Part 4 (MEP Commissioning and Verification) covers verification of plumbing, electrical, and HVAC systems — pressure tests, flow rates, equipment commissioning, balance testing.*