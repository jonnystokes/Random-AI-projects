# Appendix E — Testing Procedures (continued)

*Part 4: MEP Commissioning and Verification*

This part covers the procedures for verifying that the Mechanical, Electrical, and Plumbing systems are working as designed. Where the previous parts cover materials (concrete) and conditions (soil, envelope, air, water), this part covers the systems that make the building work as a building.

The tests here are the post-installation verification — what's run AFTER each system is built but BEFORE final acceptance. Some are required by code (electrical GFCI testing, plumbing pressure tests). Others are best-practice for a well-designed system (HVAC airflow balance, hydronic commissioning).

The 11-element format continues:

- **E.30** — Plumbing Pressure Testing (water supply and DWV)
- **E.31** — Electrical Verification and Testing (continuity, polarity, GFCI/AFCI, insulation)
- **E.32** — Megger / Insulation Resistance Testing
- **E.33** — Grounding System Verification (CEE, bonding, fall-of-potential)
- **E.34** — HVAC Airflow Measurement and Balancing
- **E.35** — Heat Pump Commissioning (refrigerant charge, capacity, COP)
- **E.36** — Hydronic System Commissioning (radiant balance, loop flow)
- **E.37** — ERV Commissioning (CFM verification, recovery efficiency)
- **E.38** — Smart Home System Verification
- **E.39** — Integrated Whole-House Commissioning Checklist

---

## E.30 Plumbing Pressure Testing

**Purpose:**

Plumbing pressure tests verify that the water supply system has no leaks before it's covered with drywall and put into service. The drainage system is similarly tested to verify joints are watertight. Both tests are required for permit inspection in Oregon (per OPSC Section 312 and 712).

**Plain language:** Fill the system with pressurized water (or air for drainage), monitor for pressure loss over time. If the pressure stays stable, no leaks. If it drops, find the leak.

**When to perform:**

- **Water supply:** after rough-in plumbing complete, before drywall (required for inspection)
- **Drainage (DWV):** after rough-in DWV complete, before drywall
- **Final water supply:** after fixtures installed, before move-in
- **After any plumbing repair:** verify no new leaks

**Standards:**

- OPSC 312 — Pressure testing
- OPSC 712 — Drainage system testing
- IPC 312 (for jurisdictions using IPC instead of UPC) — same principles

**Equipment:**

```
WATER SUPPLY PRESSURE TEST:

[ ] Test gauge (0-300 psi) — $20-$50
   - Threaded fitting to attach to a hose bib or test tee
   - Liquid-filled gauge for stability
   
[ ] Test plug or test cap for system isolation
[ ] Pump (if needed for higher pressure than house pressure)
   - Hand pump or electric — $100-$300
   - For testing above municipal pressure (60-80 psi)

[ ] Garden hose for filling

DRAINAGE PRESSURE TEST:

[ ] Test plugs (inflatable plugs that block pipe ends) — $30-$80 per plug
   - Various sizes for different pipe diameters
   - Inflated with hand pump or shop vac
   
[ ] Test stack ball or rubber test ball for stack testing
[ ] Air pressure gauge (low-range, 0-15 psi or 0-30 psi)
[ ] Hand pump for pressurization

GENERAL:

[ ] Stopwatch or timer
[ ] Notebook for recording
[ ] Soap and water solution for leak detection (optional)
[ ] Pipe wrenches and tools for adjustments
```

**Safety considerations:**

```
[ ] Pressure tests use HIGH PRESSURES — water can spray hard if a fitting fails
[ ] Eye protection during pressurization
[ ] Don't exceed test pressure for extended periods
[ ] Test plugs can BLOW OUT if over-pressurized — never stand directly in line with one
[ ] Drain water carefully after tests (avoid flooding)
[ ] Air pressure tests on drainage:
   - LOWER pressure than water tests
   - But pressurized air in PVC can be dangerous if pipe fails
   - Don't exceed code-specified test pressure (typically 5 psi for DWV)
```

### E.30.1 Water Supply Pressure Test

**Pre-test setup:**

```
[ ] All rough-in plumbing complete
[ ] All branches and runs connected
[ ] All fixture stub-outs capped or valved closed
[ ] Water heater isolated (if present at rough-in stage)
[ ] System filled with water (purge all air)
[ ] No pressure regulator in test line (or PRV bypassed)
[ ] Test gauge installed at low point of system
```

**Procedure:**

```
1. CONNECT TEST GAUGE:
   - At a hose bib or test tee at the lowest point in the system
   - Inline T-fitting works if no test point exists

2. FILL SYSTEM WITH WATER:
   - Open all isolation valves
   - Open one fixture or hose bib at the highest point briefly to bleed air
   - Close that fixture once water flows
   - Verify water present at all parts of the system
   - Repeat air bleeding from multiple high points

3. PRESSURIZE:
   - Method 1: use building water pressure (60-80 psi typical)
     - Open the supply isolation valve
     - System pressurizes to incoming pressure
   - Method 2: pump up to test pressure
     - Hand pump or electric test pump
     - Pump until gauge reads test pressure
     - Test pressure: typically 100 psi for residential (verify with local code)

4. ISOLATE THE SYSTEM:
   - Close the supply isolation valve
   - System now isolated from supply
   - Pressure should stay stable

5. WAIT AND OBSERVE:
   - Note initial pressure exactly
   - Wait the test duration (typically 24 hours, sometimes 1 hour for rough-in)
   - Observe pressure at intervals (every hour or so for diagnostic purposes)

6. READ FINAL PRESSURE:
   - After test duration, read final pressure
   - Calculate pressure loss = initial - final

7. INTERPRET:
   - No pressure loss (within gauge accuracy ~1-2 psi) = PASS
   - Slight pressure loss (1-5 psi) = MINOR (could be temperature change; investigate)
   - Significant pressure loss (5+ psi) = FAIL (leak present)

8. IF PRESSURE LOSS:
   - Inspect ALL connections visually for water
   - Check stub-outs, valves, fittings
   - Use soap solution at suspect joints (bubbles indicate leaks)
   - Tighten or repair as needed
   - Re-test
```

**Data recording:**

```
WATER SUPPLY PRESSURE TEST:

Date: ______________  Time started: __________
Tester: ____________________

System under test:
[ ] Whole-house water supply
[ ] Cold water only
[ ] Hot water only
[ ] Specific zone: ____________________

Test parameters:
- Test pressure: ______ psi
- Test duration: ______ hours
- Method: [ ] Building pressure [ ] Pump

Initial pressure: ______ psi
Time after _____ hr: ______ psi
Time after _____ hr: ______ psi
Final pressure (after ___ hr): ______ psi

Pressure loss: ______ psi
PASS / FAIL: __________

If failed, leaks identified at:
1. ____________________________________
2. ____________________________________
[etc.]

Repairs made: ____________________________________
Retest scheduled: ______________
Final result: ______________
```

**Pass/fail criteria:**

- Per OPSC: 100 psi for 15 minutes minimum, no perceptible drop
- Pre-coverage: most jurisdictions require 24-hour test at 100 psi
- Tolerance: usually no drop allowed (some allow 1-5 psi for thermal effects)

**Common errors:**

```
ERROR: Air not bled from system
→ Air compresses; pressure appears to drop as air migrates
→ False fail
→ Fix: thoroughly bleed all air before pressurization

ERROR: Temperature change during test
→ Cold water warming = pressure rises (~1 psi per °F)
→ Warm water cooling = pressure drops
→ Fix: test in stable temperature; or measure water temp at start/end

ERROR: Test gauge inaccurate
→ Reads pressure loss that isn't real
→ Fix: use quality gauge; calibrate or verify

ERROR: Supply valve not fully closed
→ Building pressure feeding the test
→ Hides leaks
→ Fix: verify valve fully closed; physically isolate

ERROR: Slight leak past closed valve
→ Some valves don't seal perfectly
→ Pressure can rise during test (false PASS) or drop slightly
→ Fix: use ball valves with tested seal; or temporarily install plug
```

**What to do if it fails:**

```
1. Visual inspection of all accessible joints
2. Listen for hissing at joints
3. Apply soap solution at suspect joints (bubbles = leak)
4. Use thermal camera (cooling at leak point)
5. Most leaks are at:
   - Threaded connections (pipe to fitting; lacking sealant or under-tightened)
   - Solder joints (cold joints, contamination)
   - Push-fit connections (improperly seated)
   - Stub-outs (caps not fully tightened)
6. Repair the leak per appropriate method
7. Re-pressurize and retest
8. Document the chain
```

### E.30.2 Drainage Pressure Test

**Pre-test setup:**

```
[ ] All DWV piping installed
[ ] All vents extending to roof or sidewall
[ ] All fixture stub-outs in place
[ ] System ready to be sealed for testing
```

**Two methods — water test or air test:**

**Water test (more thorough but slower):**

```
1. Install test plug at the lowest point of the building drain (where it leaves the building)

2. Fill the entire DWV system with water from the highest opening:
   - Cap or plug all fixture openings except the highest
   - Pour water in from the highest open vent or fixture
   - Continue until water reaches the highest point of the system

3. Hold the water column for 15 minutes minimum (some jurisdictions 30 minutes)

4. Inspect all joints visually for water:
   - Drips
   - Wet spots
   - Slow seeps
   
5. Verify water level doesn't drop:
   - Mark the level at the start
   - Check at intervals
   - Stable = pass

6. Drain the system and remove plug
```

**Air test (faster, more common):**

```
1. Plug all openings of the system:
   - Test plugs at each fixture stub-out
   - Test ball at the building drain exit
   - Vent stack capped at top

2. Pressurize with air:
   - Hand pump or compressor through a test tee
   - To the test pressure (typically 5 psi)

3. Hold pressure for 15 minutes minimum

4. Listen for hissing at joints
   - Apply soap solution at suspect joints (bubbles = leak)

5. Verify no pressure loss:
   - Air gauge stable
   - Tolerance is typically 1 psi or less

6. Depressurize before removing plugs
```

**Pass/fail criteria:**

- Water test: no leaks, no level drop after 15 minutes
- Air test: no pressure loss after 15 minutes (or per local code)

**Common errors:**

```
ERROR: Test plug not fully seated
→ Air or water leaks past plug
→ Looks like system leak
→ Fix: properly seat all plugs

ERROR: Vent terminations not capped during air test
→ Air escapes through roof
→ Test cannot pressurize
→ Fix: cap all vents during test

ERROR: Glue joints not fully cured
→ Joints can leak during test even though correctly made
→ Fix: allow 24+ hours after solvent cement application before testing

ERROR: Plumbers tape on plug threads
→ Can fail at higher test pressures
→ Fix: use proper test plugs designed for the pressure
```

**What to do if it fails:**

```
1. Identify leak location:
   - Visual inspection (water test)
   - Listening (air test)
   - Soap solution
2. Common leak points:
   - Solvent-cement joints insufficiently glued
   - Hub-and-spigot joints (rubber gasket missing or pinched)
   - Compression fittings (under-tightened)
3. Repair the joint:
   - For solvent cement: cut out and re-glue (cannot just re-cement existing joint)
   - For gaskets: replace gasket
4. Allow cure time
5. Re-test
```

---

## E.31 Electrical Verification and Testing

**Purpose:**

After electrical work is complete, verify that:
- Every circuit is properly wired (no neutral-ground bonds, no shorts, no opens)
- Polarity is correct at every receptacle (hot, neutral, ground in right places)
- GFCI and AFCI breakers function correctly
- All grounding connections are continuous
- Insulation is intact (no damage to conductors)

This is the standard suite of post-installation electrical verification, run before drywall and again at final inspection.

**Plain language:** Make sure every wire goes to the right place, every safety device works, and nothing is shorted or grounded improperly. Done with simple testers and methodical procedure.

**When to perform:**

- After rough-in electrical complete (before drywall)
- After all devices installed (before final inspection)
- Before any new occupant moves in (independent verification)
- After any electrical work or repair

**Standards:**

- NEC (current edition adopted by Oregon as OESC)
- NFPA 70B — Standard for Electrical Equipment Maintenance
- Manufacturer's testing instructions for specific devices

**Equipment:**

```
BASIC TESTING:

[ ] Receptacle tester — $15-$30
   - Three-light tester showing wiring status
   - Better units include GFCI test button
   - Brand: Klein, Fluke, Sperry

[ ] Multimeter — $50-$200
   - Voltage AC/DC, current, resistance
   - Better units include continuity, capacitance
   - Brand: Fluke, Klein, Greenlee

[ ] Non-contact voltage tester — $20-$60
   - Verifies presence of voltage without contact
   - Brand: Fluke, Klein, Southwire

[ ] Plug-in surge protector tester — $20-$40
   - Verifies SPD function

INTERMEDIATE TESTING:

[ ] Circuit tracer / breaker finder — $50-$200
   - Identifies which breaker controls which circuit

[ ] AFCI/GFCI tester — $30-$80
   - Specifically tests AFCI/GFCI function
   - Some receptacle testers include this

ADVANCED TESTING (rented or owned for multiple builds):

[ ] Megger / insulation tester — $300-$1,500
   - Tests insulation resistance
   - See E.32

[ ] Ground resistance tester — $300-$2,000
   - Tests grounding electrode resistance
   - See E.33

[ ] Power quality analyzer — $500-$5,000
   - Voltage stability, harmonics, etc.
   - Generally not needed for residential

SAFETY:

[ ] Safety glasses
[ ] Insulated rubber gloves (for work with energized circuits)
[ ] Insulating mat
[ ] Lockout/tagout kit — $30-$100
   - Padlocks and tags
   - For de-energizing circuits during work
```

**Safety considerations:**

```
[ ] LOCKOUT / TAGOUT during all rough-in electrical testing:
   - Main breaker OFF (or specific circuits OFF)
   - Padlock on the panel
   - Tag indicating "Do Not Energize"
   - Verify de-energized with multimeter before working

[ ] During energized testing (final verification):
   - Limit contact with conductors
   - Test devices only
   - Don't touch bare wires unless de-energized

[ ] AFCI/GFCI testing:
   - Will trip; have a way to reset
   - May trigger downstream protections

[ ] Use proper PPE
[ ] Two-person work for main panel testing
[ ] Verify the meter is rated for the voltage
```

**Pre-test setup:**

```
[ ] Wiring complete (rough-in or final)
[ ] All boxes accessible
[ ] Devices either installed or test pigtails ready
[ ] Panel directory accurate (which circuit is which)
[ ] All circuits labeled
[ ] Thermal imager available (E.23) for finding overheated connections later
```

### E.31.1 Receptacle Polarity and Grounding Test

```
1. With circuit energized:

2. Plug receptacle tester into each receptacle in the building

3. Read the indicator lights:
   - 3-light tester typically shows:
     - Two amber lights = wiring CORRECT
     - One amber, one off = various faults
     - All off = no power
     - Specific patterns indicate specific faults

4. Common fault indications:
   - Open ground = ground wire not connected
   - Open neutral = neutral wire not connected
   - Open hot = hot wire not connected
   - Hot/ground reverse = ground and hot swapped (DANGEROUS)
   - Hot/neutral reverse = polarity swapped (less dangerous but wrong)

5. Document each receptacle:
   - Pass / Fail
   - If fail, specific fault

6. For GFCI receptacles:
   - Press TEST button on the receptacle
   - Should trip (power off downstream)
   - Press RESET to restore
   - Verify downstream receptacles work after reset

7. For all GFCI-protected receptacles in the same circuit:
   - Press TEST on the GFCI receptacle (or breaker)
   - Verify all downstream receptacles lose power
```

### E.31.2 GFCI Testing

```
1. For every GFCI device (receptacle or breaker):

2. With circuit energized:
   - GFCI ready (RESET button pressed if applicable)

3. Press TEST button:
   - GFCI should trip immediately
   - Power should be removed from downstream

4. Verify downstream protection:
   - Plug a tester into a protected outlet
   - Tester should show no power
   - Or all lights off

5. Press RESET:
   - GFCI returns to ready state
   - Downstream restored

6. Plug-in tester GFCI test:
   - Some testers have a GFCI test button
   - Pressing simulates a ground fault
   - GFCI should trip
   - Tester verifies trip occurred

7. Document each GFCI:
   - Location
   - Pass/Fail
   - Test method used
```

### E.31.3 AFCI Testing

```
1. For every AFCI breaker:

2. With circuit energized:

3. Press TEST button on the breaker:
   - Breaker should trip
   - Verify downstream loss of power

4. Reset the breaker
5. Verify downstream restoration

6. AFCI tester (alternative):
   - Some plug-in testers simulate arc faults
   - Better than just the test button (which only tests the breaker mechanism)

7. Document each AFCI:
   - Location (panel, position)
   - Pass/Fail
```

### E.31.4 Voltage Verification

```
1. At each receptacle:

2. Measure voltage with multimeter:
   - Hot to neutral: should read 110-125 V (typical 120 V circuit)
   - Hot to ground: should read same as hot-to-neutral (within 1-2 V)
   - Neutral to ground: should read very low (0-3 V; higher indicates neutral issue)

3. For 240 V circuits (range, dryer, EV charger, etc.):
   - Hot to hot: 220-250 V
   - Hot to neutral: 110-125 V (each leg)
   - Hot to ground: same as hot to neutral

4. Document any out-of-range readings
```

### E.31.5 Continuity Testing (Equipment Grounds)

```
1. With CIRCUIT DE-ENERGIZED (lockout):

2. Multimeter on continuity (or low-resistance ohms):

3. Test ground continuity:
   - One probe at the equipment ground in a remote receptacle
   - Other probe at the panel ground bus
   - Reading should be very low resistance (< 1 ohm)
   - Higher resistance indicates poor connection somewhere

4. Test for shorts:
   - One probe at hot, other at ground
   - Should read OPEN (no continuity) when nothing turned on
   - Continuity = a short

5. Document:
   - Each circuit's ground resistance
   - Any anomalies
```

**Data recording:**

```
ELECTRICAL VERIFICATION LOG:

Date: ______________
Tester: ____________________

CIRCUIT INVENTORY:

Circuit | Description | Breaker | AFCI? | GFCI? | Test | Notes
--------|-------------|---------|-------|-------|------|-------
1       | Kitchen 1   | 20A     | Y     | Y     | PASS |
2       | Kitchen 2   | 20A     | Y     | Y     | PASS |
3       | Bath 1      | 20A     | Y     | Y     | PASS |
[continue for each circuit]

RECEPTACLE TESTS:

Location | Receptacle Tester | GFCI Test | Voltage | Notes
---------|-------------------|-----------|---------|-------
Kitchen N | Pass              | Trips     | 121.2   |
[continue for each]

GROUNDING TEST:
Main panel ground bus to grounding electrode: ____ ohms
Subpanel A: ____ ohms (separate or bonded)
Subpanel B: ____ ohms

SUMMARY:
Total circuits: ______
Passed: ______
Failed: ______
Issues found and corrected: ____________________________________

Inspector signature: ____________________
```

**Pass/fail criteria:**

- All receptacles show correct wiring (per receptacle tester)
- All GFCI test successful (trip on test, reset properly)
- All AFCI test successful
- All voltages within ±5% of nominal
- All ground continuity readings < 1 ohm

**What to do if anything fails:**

For miswiring:
- Open the box
- Identify the wiring error
- Correct
- Re-test

For non-functional GFCI/AFCI:
- Verify circuit energized correctly
- Verify load connections (not line)
- Replace device if it doesn't function on test

For voltage issues:
- Investigate source of variation
- Loose connections common cause
- Improper sizing (rare)

---

## E.32 Insulation Resistance Testing (Megger)

**Purpose:**

The "megger" test (megohmmeter, brand-name became generic) measures the resistance between conductors and ground, between conductors of different circuits, etc. Healthy insulation reads many millions of ohms (megohms). Damaged or wet insulation reads much lower. Used to verify cable insulation hasn't been damaged during installation.

**Plain language:** Apply a high voltage (~500 V) between two points where there shouldn't be a connection. Measure how much current leaks through. High resistance = good insulation. Low resistance = damaged insulation, water intrusion, or improper installation.

**When to perform:**

- During or after rough-in (before drywall) for new installations
- When troubleshooting circuit issues
- Periodically for industrial equipment (less common in residential)

**Standards:**

- IEEE 43 — Recommended Practice for Testing Insulation Resistance
- NETA MTS — Maintenance Testing Specifications

**Equipment:**

```
[ ] Insulation resistance tester (megger) — $300-$1,500
   - Output voltages typically 250 V, 500 V, 1000 V (residential typically uses 500 V)
   - Reads megohms (MΩ)
   - Brands: Fluke, Megger, AEMC, Klein

[ ] Test leads (typically supplied with meter)
[ ] Lockout/tagout kit (CRITICAL for this test)
[ ] Discharge tool (or a known good resistor) for discharging cables after test
```

**Safety considerations:**

```
[ ] HIGH VOLTAGE: 500 V is enough to cause harmful shock
[ ] Always lockout/tagout the circuit being tested
[ ] Verify de-energized BEFORE applying test voltage
[ ] After test: discharge cable to ground before disconnecting
   - Cables store energy as a capacitor at 500 V
   - Can shock significantly even after meter is off
   - Discharge = touch all conductors briefly to ground

[ ] Don't test with anyone touching the cable being tested
[ ] Don't test in wet conditions
[ ] Wear insulated gloves
```

**Pre-test setup:**

```
[ ] Lockout/tagout the circuit
[ ] Verify de-energized with voltmeter
[ ] Disconnect any sensitive electronics (the test voltage can damage some devices)
   - GFCI/AFCI breakers: leave in panel but disconnect load wires
   - Surge protectors: disconnect
   - Electronics on the circuit: unplug
[ ] Identify ALL conductors to test:
   - Hot to ground
   - Neutral to ground
   - Hot to neutral
   - For multi-phase: each phase to each phase, each phase to ground
```

**Procedure:**

```
1. Connect meter to circuit:
   - One lead to one conductor
   - Other lead to another conductor or ground
   - Per the configuration being tested

2. Apply test voltage (500 V typical):
   - Press the test button
   - Hold for the test duration (1 minute typical)

3. Read resistance:
   - Initial reading climbs as charge builds
   - Stabilizes after 30-60 seconds
   - Record the stabilized reading

4. Multiple tests per circuit:
   - Hot conductor to ground
   - Neutral conductor to ground
   - Hot to neutral (with all loads disconnected)
   - Multi-conductor cables: each combination

5. Discharge the cable:
   - After releasing test voltage
   - Touch the test leads to ground briefly
   - Verify with voltmeter that voltage is dissipated

6. Move to next circuit
7. Document all readings
```

**Data recording:**

```
INSULATION RESISTANCE TEST:

Circuit: ____________________
Date: ______________
Test voltage: ______ V
Cable type: ____________________
Cable length: ______ ft

Hot to ground: ______ MΩ
Neutral to ground: ______ MΩ
Hot to neutral: ______ MΩ

Other multi-conductor combinations: ____________________

Pass / Fail: __________
Notes: _______________________________________________
```

**Pass/fail criteria:**

```
For new residential wiring:

> 100 MΩ: Excellent
50-100 MΩ: Good
10-50 MΩ: Acceptable
1-10 MΩ: Marginal — investigate
< 1 MΩ: Inadequate — find the problem

Note: Long cables read lower than short ones. The relationship is roughly:
- Doubling cable length halves the megger reading
- For very long cables, even healthy cables may read in tens of MΩ

Adjust acceptance based on cable length and condition.
```

**Common errors:**

```
ERROR: Sensitive electronics still connected
→ Test voltage damages sensitive equipment
→ Or low resistance reading from electronic components
→ Fix: disconnect all electronics before testing

ERROR: Wet conditions
→ Surface tracking gives false low readings
→ Fix: dry the cables; test in dry conditions

ERROR: Grounded conductors not isolated
→ Reading shows ground rather than conductor insulation
→ Fix: ensure all conductors are isolated; test one combination at a time

ERROR: Discharge skipped after test
→ Stored charge can shock person
→ Or damage equipment when reconnected
→ Fix: always discharge before disconnecting
```

**What to do if it fails:**

For low insulation resistance:
1. Inspect cables visually for damage
2. Inspect connections (especially in damp locations)
3. Check for water intrusion
4. Test segments of the circuit individually to isolate the problem
5. Replace damaged cables
6. Re-test

---

## E.33 Grounding System Verification

**Purpose:**

The grounding system is the safety net for the entire electrical installation. Verify:
- The grounding electrode (in this design: concrete-encased rebar / Ufer ground) has low resistance to earth
- All bonding connections are continuous
- All metallic systems are properly bonded to the ground

**Plain language:** The ground wire connects everything that's supposed to be at zero voltage to actual earth. Verify this connection is good — low resistance, continuous, fully bonded.

**When to perform:**

- After grounding system installation
- During rough-in inspection
- Annually for ongoing verification (especially in high-lightning areas)
- After lightning strikes or significant electrical events

**Standards:**

- NEC Article 250 — Grounding and Bonding (current edition)
- NETA standards for testing
- IEEE 81 — Standard for Measuring Earth Resistance

**Equipment:**

```
[ ] Earth ground tester / fall-of-potential tester — $300-$2,000
   - Commercial units: AEMC, Megger, Fluke
   - 3-pole or 4-pole testers
   - Battery powered, dedicated to ground testing

[ ] Ground rods (auxiliary; for testing):
   - Two auxiliary rods 3-5 feet long
   - With insulated handles for driving and removal
   - Often supplied with the tester

[ ] Test leads (typically supplied with tester)
[ ] Multimeter (continuity for bonding tests)
```

**Safety considerations:**

```
[ ] Don't test during thunderstorms (lightning danger)
[ ] Be aware of underground utilities when driving auxiliary rods
[ ] Call 811 for utility location before driving rods
[ ] Watch for traffic if testing near roads
[ ] Voltage on grounding system can be present from nearby ground faults
   - Use a voltmeter to check before contact
```

**Pre-test setup:**

```
[ ] Identify the grounding electrode location
[ ] Disconnect the grounding electrode from the panel:
   - This is required for accurate testing
   - Otherwise the panel acts as additional ground
   - Lockout/tagout the panel during disconnection

[ ] Plan auxiliary rod locations:
   - Rod #1 (current rod): 60-80 feet from electrode
   - Rod #2 (potential rod): 60% of the distance from electrode to current rod
   - In a straight line: electrode → potential → current
   - Soil moisture affects readings; test when soil is moist (not dry, not waterlogged)
```

**Procedure (Fall of Potential method, the standard):**

```
1. Drive auxiliary rod #1 (current rod) at 60-80 ft from grounding electrode

2. Drive auxiliary rod #2 (potential rod) at 60% of the distance to rod #1

3. Connect tester:
   - Lead 1 to grounding electrode
   - Lead 2 to potential rod (auxiliary #2)
   - Lead 3 to current rod (auxiliary #1)

4. Run the test:
   - Modern testers automate this
   - Press test button
   - Tester applies test current and measures voltage

5. Read resistance:
   - In ohms (Ω)
   - Lower is better

6. Verify accuracy:
   - Move potential rod to 70% of distance
   - Resistance should change very little
   - Move to 50% of distance
   - Resistance should also change very little
   - Significant changes indicate incorrect rod placement

7. Reconnect grounding electrode to panel

8. Document
```

**Data recording:**

```
GROUNDING ELECTRODE TEST:

Date: ______________
Tester: ____________________
Method: Fall-of-Potential (3-pole)

Site:
- Grounding electrode type: [ ] CEE/Ufer [ ] Ground rod [ ] Plate [ ] Other
- Electrode dimensions: ____________________
- Soil conditions: ____________________ (dry/moist/wet)

Test setup:
- Current rod distance: ______ ft
- Potential rod distance: ______ ft (60% of current)

Resistance reading: ______ Ω

Verification:
- At 50% distance: ______ Ω
- At 60% distance: ______ Ω (primary measurement)
- At 70% distance: ______ Ω

Variation acceptable: [ ] Yes [ ] No (if no, retest with better rod placement)

Pass / Fail: __________
Notes: _______________________________________________
```

**Pass/fail criteria:**

```
NEC requires either:
- Single grounding electrode with resistance ≤ 25 Ω, OR
- Two or more electrodes regardless of resistance (CEE counts as one)

Practical thresholds:
- < 5 Ω: excellent (commercial standard)
- 5-15 Ω: good (residential)
- 15-25 Ω: acceptable (NEC compliant for single electrode)
- 25-50 Ω: marginal (add additional electrode)
- > 50 Ω: investigate (poor connection or degraded electrode)

For this design's CEE (concrete-encased electrode):
- Typically reads very low (< 5 Ω) when properly installed
- The mass of conductive concrete provides excellent ground
```

**Bonding verification (separate from electrode testing):**

```
1. Multimeter on low-ohm continuity

2. Test continuity from grounding bus to:
   - Water pipe (within 5 ft of entry, NEC 250.104)
   - Gas pipe (if any)
   - Structural steel (if any)
   - Other metallic systems

3. Reading should be very low (< 1 Ω)

4. Visual inspection:
   - Bonding clamps tight
   - No corrosion at connections
   - Continuous path from each metallic system to grounding bus

5. Document each bonding connection
```

**What to do if it fails:**

For high electrode resistance:
1. Verify proper testing technique (rod placement)
2. Investigate electrode condition:
   - For CEE: visual inspection of the rebar stub above slab
   - For ground rod: check for corrosion, drive deeper if possible
3. Add supplemental electrode:
   - Additional ground rod 6+ ft from existing
   - Connect to existing grounding electrode conductor
4. Retest
5. Document

For poor bonding continuity:
1. Inspect the connection
2. Clean corrosion
3. Tighten clamps
4. Replace damaged jumpers
5. Retest

---

## E.34 HVAC Airflow Measurement and Balancing

**Purpose:**

Verify that HVAC system delivers the design airflow to each room, the duct system isn't undersized or restricted, and the air handler is operating at design specifications.

**Plain language:** Measure how much air comes out of each register and goes into each return. Compare to the design. Adjust dampers to balance — every room gets the right amount.

**When to perform:**

- After ductwork installation, before drywall (to find duct issues)
- After fixture installation (final balancing)
- Annually (verify continued performance)
- After any HVAC changes (renovation, equipment replacement)

**Standards:**

- ACCA Manual D — Residential Duct Systems
- ACCA Manual T — Air Distribution Basics
- ASHRAE 152 — Method of Test for Determining the Design and Seasonal Efficiencies of Residential Thermal Distribution Systems

**Equipment:**

```
[ ] Anemometer / flow hood — $200-$1,500
   - Capture hood: covers a register, measures airflow directly
   - Flow grid: held in front of register
   - Hot wire anemometer: measures velocity (CFM = velocity × area)
   - Brand: TSI, Alnor, Dwyer

[ ] Manometer (digital) — $50-$300
   - Static pressure measurement
   - Useful for system diagnosis

[ ] Smoke pencil (E.22) — for flow visualization

[ ] Tape measure (for register dimensions)
[ ] Notebook
```

**Pre-test setup:**

```
[ ] HVAC system operating at design conditions:
   - Compressor running (cooling) or heat exchanger heating
   - Air handler at full speed (or set to commissioning speed)
   - All zones calling

[ ] All dampers in design position:
   - Should be wide open initially
   - Documenting starting position

[ ] All return ducts open (no blocked returns)

[ ] Filter installed (slightly used; not brand new clean, not dirty)

[ ] Building doors closed (HVAC working as system)

[ ] Flow hood calibrated per manufacturer
```

**Procedure:**

```
SYSTEM-LEVEL TESTING:

1. Total system airflow:
   - Measure airflow at the air handler (or sum of all supplies)
   - Compare to design CFM
   - Significant difference indicates ducts undersized, restricted, or air handler issue

2. Static pressure:
   - Measure with manometer at supply plenum
   - Compare to design (typically 0.5" w.c. for residential)
   - High static = restricted airflow

3. Return CFM:
   - Sum of return CFM should equal supply CFM (within 5%)
   - Significant difference = leakage or imbalance

INDIVIDUAL REGISTER TESTING:

4. At each supply register:
   - Place flow hood over register
   - Wait for steady reading (5-15 seconds)
   - Read CFM
   - Compare to design CFM for that location

5. At each return register:
   - Same process
   - Verify return air collection

ROOM-LEVEL VERIFICATION:

6. With doors closed:
   - Verify each room's supply and return are roughly balanced
   - Or that pressure differential is acceptable
   - Use manometer to measure room-to-room pressure

DAMPER ADJUSTMENT (BALANCING):

7. If individual registers are off:
   - Adjust damper at the branch
   - Re-measure
   - Iterate until each register is at or near design CFM

8. Document final positions
```

**Data recording:**

```
HVAC AIRFLOW BALANCE LOG:

Date: ______________
Tester: ____________________
System status: ____________________ (cooling/heating/fan only)
Outdoor temperature: ______ °F

System totals:
- Total supply CFM: ______ (design: ______)
- Total return CFM: ______ (design: ______)
- Static pressure at supply plenum: ______ in. w.c. (design: ______)

REGISTER MEASUREMENTS:

Location           | Design CFM | Measured CFM | After Adjust | Damper Position
-------------------|------------|--------------|--------------|----------------
Master Bed Supply  | 100        | 80           | 100          | 75% open
Master Bed Return  | 100        | 95           | 100          | full
[continue for each register]

Total imbalance addressed: ____________________
Final balance achieved: [ ] Yes [ ] No

Notes: ____________________________________
```

**Pass/fail criteria:**

- Each register within ±10% of design CFM = ACCEPTABLE
- Each register within ±5% of design CFM = EXCELLENT
- Significant deviations (> 20%) = INVESTIGATE

**What to do if values are off:**

For low total CFM:
- Filter dirty? Replace
- Coil dirty? Clean
- Duct restriction? Investigate
- Air handler speed setting?
- Static pressure too high? Larger ducts or smoother airflow needed

For uneven distribution:
- Use damper adjustments to balance
- If can't balance with dampers, ductwork undersized (major rework)
- Consider zone control if pattern is inherent to use

---

## E.35 Heat Pump Commissioning

**Purpose:**

Verify the ground-source (or air-source) heat pump is operating at design specifications: refrigerant charge correct, compressor functioning, capacity at design conditions.

**Plain language:** Run the heat pump, measure key parameters (temperatures, pressures, current draw), compare to manufacturer specs. Adjust if needed.

**When to perform:**

- Initial commissioning after installation
- Annually for verification
- After any service or repair

**Standards:**

- AHRI 330 — Sound Rating
- AHRI 340/360 — Performance Rating
- IGSHPA Standards (for ground-source systems)
- Manufacturer's commissioning documentation

**Equipment:**

```
THIS WORK REQUIRES EPA 608 CERTIFICATION FOR REFRIGERANT WORK
(Owner-builder cannot legally do refrigerant work without this)

[ ] Refrigerant gauge manifold — $200-$800 (certified tech only)
[ ] Vacuum pump (for service work)
[ ] Refrigerant scale (for charging)
[ ] Thermometer / clamp meter — $50-$200
[ ] Anemometer (for airflow — see E.34)
[ ] Temperature/humidity sensor for entering and leaving air
[ ] Watt meter for power consumption
[ ] Notebook and manufacturer documentation
```

**Owner-builder role:**

You hire an EPA 608 certified technician for refrigerant work. Your role:
- Verify the technician documents the commissioning
- Receive and file the commissioning report
- Verify ongoing operation per the report
- Annual review of operation

**What the technician does (for context):**

```
1. Verify refrigerant charge:
   - Manufacturer specifies subcooling and superheat targets
   - Measure liquid line and suction line temperatures
   - Calculate subcooling and superheat
   - Adjust refrigerant if needed

2. Verify operation:
   - Compressor current draw at design
   - Temperature differential across coils
   - Pressures within spec

3. Calculate capacity:
   - Airflow × temperature differential × specific heat × density
   - Compare to nameplate capacity
   - Calculate COP (heating) or EER (cooling)

4. Document everything in commissioning report
```

**Owner-builder verification (annual):**

```
1. Visual inspection:
   - No oil stains (refrigerant leak indicator)
   - Coils clean
   - Fans operating
   - No unusual sounds

2. Operational test:
   - Run cycle in heating mode
   - Run cycle in cooling mode
   - Verify thermostat function

3. Document any anomalies
4. Schedule technician visit if issues found
```

**Pass/fail criteria:**

For ground-source heat pump:
- COP heating ≥ 3.5 at design conditions
- EER cooling ≥ 15
- All temperatures within manufacturer spec
- Power consumption within nameplate range

---

## E.36 Hydronic System Commissioning

**Purpose:**

Verify the radiant floor heating system: each loop carries design flow, each zone reaches setpoint, manifolds and pumps function correctly.

**Plain language:** Check that each radiant loop has the right water flow, and that each zone heats evenly. Adjust valves to balance.

**When to perform:**

- After installation, before tile/finish floor
- After radiant pour, before furniture/use
- Annually for verification

**Standards:**

- ASHRAE Handbook — HVAC Applications, Chapter 6 (Radiant Heating and Cooling)
- IAPMO standards for hydronic systems
- Manufacturer's commissioning documentation

**Equipment:**

```
[ ] Manifold flow indicators (often built into manifolds)
[ ] Thermometer (clamp-on or surface)
[ ] Manometer for system pressure
[ ] Pressure gauge for loop testing
[ ] Notebook and design specifications
```

**Pre-commissioning setup:**

```
[ ] System pressure tested per manufacturer (typically 100 psi for 24 hours)
[ ] System filled with water (ideally distilled, with corrosion inhibitor per spec)
[ ] All air purged from loops (run pump with bleed valves open)
[ ] Pumps energized and operating
```

**Procedure:**

```
1. PRESSURE TEST (verify earlier inspection):
   - System holds pressure
   - No leaks at fittings or manifold

2. FLOW VERIFICATION:
   - At each manifold, observe flow indicators
   - All loops should have flow
   - Compare to design flow rates per loop

3. BALANCING:
   - Adjust flow rate at each loop's setting valve
   - Higher flow = more heat to that loop's area
   - Lower flow = less heat
   - Iterate based on temperatures achieved

4. ZONE OPERATION:
   - Bring each zone to operating temperature
   - Verify thermostat operation
   - Verify zone valves open/close on demand
   - Verify pump operates only when zones call

5. SURFACE TEMPERATURE:
   - With system at design output:
   - Floor surface temperature in each room
   - Should be 75-85°F typically
   - Variations indicate flow imbalance

6. SETPOINT VERIFICATION:
   - Set each zone thermostat to setpoint
   - Verify room reaches setpoint
   - Cycle off when setpoint achieved
   - Cycle on when temp drops

7. DOCUMENT:
   - All flow settings
   - Surface temperatures by area
   - Any imbalances and adjustments made
```

**Pass/fail criteria:**

- Each loop flowing at design rate (within 10%)
- Each zone reaches setpoint
- Surface temperatures uniform within zone (within 5°F)
- System pressure stable
- No leaks

---

## E.37 ERV Commissioning

**Purpose:**

Verify the Energy Recovery Ventilator delivers the designed ventilation rate, with proper recovery efficiency and balanced airflows.

**Plain language:** Measure how much air comes in (fresh) and goes out (stale), verify the heat exchanger works (recovers heat from outgoing air), and verify the system is balanced.

**When to perform:**

- After installation
- After commissioning (initial setup)
- Annually for verification

**Standards:**

- ASHRAE 62.2 — Ventilation rates
- HVI (Home Ventilating Institute) certifications
- Manufacturer's commissioning documentation

**Equipment:**

```
[ ] Anemometer (E.34) for airflow at supply and exhaust
[ ] Temperature/humidity sensor
[ ] Power meter (Kill-A-Watt) for unit power consumption
[ ] Manometer for static pressure
[ ] Notebook and design specs
```

**Procedure:**

```
1. ERV running at design speed:

2. AIRFLOW VERIFICATION:
   - Supply CFM (incoming fresh air at the unit's supply outlet)
   - Exhaust CFM (outgoing stale air at the unit's exhaust outlet)
   - Compare to design (per ASHRAE 62.2)
   - Should match within 10%

3. BALANCE:
   - Supply CFM should equal exhaust CFM (within 5%) for balanced ventilation
   - Or designed unbalance per spec
   - Adjust dampers if needed

4. RECOVERY EFFICIENCY:
   - Measure temperatures:
     - Outdoor air entering
     - Supply air leaving (after passing through heat exchanger)
     - Indoor air entering (returning to ERV)
     - Exhaust air leaving (after passing through heat exchanger)
   - Calculate sensible recovery efficiency:
     SRE = (T_supply - T_outdoor) / (T_indoor - T_outdoor) × 100%
   - Compare to manufacturer specification

5. STATIC PRESSURE:
   - Verify external static pressure within unit's design range
   - High static = restricted ducts; low static = oversized ducts

6. POWER CONSUMPTION:
   - Power at design speed
   - Compare to nameplate
   - Higher than expected = inefficiency or restriction

7. CONTROL VERIFICATION:
   - Boost mode operation (when activated)
   - Defrost cycle (in heating season)
   - Any economizer or bypass functions

8. DOCUMENT
```

**Pass/fail criteria:**

- Supply CFM within ±10% of design
- Exhaust CFM within ±10% of design
- Supply and exhaust balanced within ±5%
- Sensible recovery efficiency ≥ 70% (typical for residential ERV)
- All controls functional

---

## E.38 Smart Home System Verification

**Purpose:**

Verify the smart home (Home Assistant) system is functional, all integrations work, automations function correctly, and the system is reliable.

**Plain language:** Test every smart device, every automation, every dashboard. Make sure everything works together as designed.

**When to perform:**

- After initial setup
- After significant changes (new devices, updates)
- Periodically as routine verification

**Equipment:**

```
[ ] The smart home system itself (Home Assistant or chosen platform)
[ ] Phone/tablet for app access
[ ] Notebook for tracking devices and automations
[ ] Multimeter for verifying device power (if needed)
```

**Procedure:**

```
DEVICE INVENTORY:

1. List all connected devices:
   - Switches and outlets
   - Sensors (motion, contact, environmental)
   - Cameras
   - Locks
   - HVAC integration
   - Energy monitoring
   - Voice assistants
   - Each with: status, last seen, firmware version

2. Verify each device:
   - Responds to commands
   - Reports status
   - Battery level (if applicable)

NETWORK VERIFICATION:

3. WiFi:
   - Coverage in all areas
   - Speeds adequate
   - All clients connected

4. Wired (if applicable):
   - All ports functional
   - Speeds at expected rates

AUTOMATION TESTING:

5. Run each automation:
   - Verify trigger conditions detected
   - Verify actions execute
   - Verify any conditions/branches work
   - Document any issues

INTEGRATION TESTING:

6. HVAC integration:
   - Thermostat reports to system
   - System can control thermostat
   - Schedules work

7. Camera integration:
   - Live view works
   - Recording works
   - Notifications work

8. Energy monitoring:
   - Real-time data
   - Historical data
   - Reports accurate

DASHBOARD VERIFICATION:

9. All dashboards load
10. All cards show data
11. All controls functional

UPDATES:

12. All firmware up to date
13. All integrations updated
14. Backup configuration

DOCUMENT EVERYTHING.
```

**Pass/fail criteria:**

- All devices connected and responsive
- All automations functional
- All dashboards working
- No communication errors
- No security alerts

---

## E.39 Whole-House Commissioning Checklist

**Purpose:**

The integrated, comprehensive checklist that ties together all the testing and verification across the whole project. The "we're ready to occupy" verification.

**Procedure (final commissioning):**

```
PHASE 1 — STRUCTURAL/CONCRETE:
[ ] All concrete strength tests passed (E.4)
[ ] Foundation drainage operational
[ ] Slab(s) cured and stable

PHASE 2 — ENVELOPE:
[ ] Blower door test ≤ 1.0 ACH50 (E.21)
[ ] Thermal imaging shows no major issues (E.23)
[ ] All air leakage remediated

PHASE 3 — PLUMBING:
[ ] Pressure tests passed (E.30)
[ ] All fixtures functional
[ ] Hot water at every fixture
[ ] Drain functions verified

PHASE 4 — ELECTRICAL:
[ ] All circuits verified (E.31)
[ ] All GFCI/AFCI tested
[ ] Grounding system tested (E.33)
[ ] Megger tests passed (E.32)

PHASE 5 — HVAC:
[ ] Heat pump commissioned (E.35)
[ ] Airflow balanced (E.34)
[ ] Hydronic balanced (E.36)
[ ] ERV commissioned (E.37)
[ ] Each zone heats and cools properly

PHASE 6 — AIR QUALITY:
[ ] IAQ monitors installed and reading (E.25)
[ ] Radon test below action level (E.26)
[ ] No mold or moisture issues (E.28)

PHASE 7 — WATER:
[ ] Water quality tests passed (E.27)
[ ] Treatment systems operational
[ ] Pressure regulation verified

PHASE 8 — SMART HOME:
[ ] All devices connected (E.38)
[ ] All automations functional
[ ] Backup configuration saved

PHASE 9 — DOCUMENTATION:
[ ] All test reports filed
[ ] All commissioning reports filed
[ ] All warranties and manuals organized
[ ] Project binder complete

READY FOR OCCUPANCY: [ ] Yes  [ ] No

Notes: ____________________________________________
```

The completed Whole-House Commissioning forms part of the home's permanent record. It demonstrates that every system was verified before occupancy — invaluable for resale, for ongoing operation, and for personal confidence.

---

*End of Appendix E Part 4 — MEP Commissioning and Verification*

*This completes Appendix E. Together, Parts 1-4 form a comprehensive testing manual covering every test referenced throughout the BSH Design and Engineering Documentation: from concrete cylinder casting at the start of construction through whole-house commissioning at occupancy.*

*The next and final appendix is **Appendix F — Templates and Forms**, providing the actual fillable forms referenced throughout this document: DCP test sheet, site investigation log, concrete pour log, pressure test record, blower door test record, and many more.*
