# Chapter 15: Electrical: Branch Circuits, Wire Size, Voltage Drop, Lighting, Low Voltage, And Future Power

This chapter contains the circuits that leave the panel: the required and dedicated branch circuits, conductor sizing and voltage drop, receptacle placement, GFCI and AFCI protection, kitchen and wet-area circuits, lighting outlets and switching, smoke and carbon monoxide alarms, and the low-voltage and communications cabling. The electrical service chapter establishes the service, panels, grounding, surge protection, backup power, solar readiness, and EV service capacity; this chapter contains the power and signal distribution to the rooms.

The electrical code of record is the 2023 Oregon Electrical Specialty Code (OESC), the 2023 National Electrical Code (NEC) with Oregon amendments in Table 1-E, effective October 1, 2023, with a January 2025 errata. Oregon does not amend most residential dwelling branch-circuit provisions; the Table 1-E amendments that matter here modify GFCI and AFCI. Every value below that does not cite a specific Oregon amendment is 2023 NEC baseline. The edition in force is confirmed at permit time.

## 12.1 Branch-Circuit Plan And Granularity

A branch-circuit plan built room by room, with more circuits than the code minimum, keeps a single fault from taking down a large part of the house and makes a tripped breaker easy to trace. In a concrete house, where rerouting means cutting structure, the extra circuits and the accessible routing are planned before rough-in.

**Simple**

The service brings power into the house; branch circuits carry it from the panel to the rooms, lights, outlets, and equipment. Dividing the house into more circuits than the minimum keeps a problem in one room from darkening another. A tripped breaker then points to a small area instead of half the floor.

**Applied**

Build the circuit plan before rough-in:

- List every room, appliance, wet area, work area, outdoor outlet, and future load.
- Decide which loads get a dedicated circuit.
- Keep lighting off the same circuit as heavy plug loads where practical, so a tripped receptacle circuit does not also kill the lights.
- Group loads by use, risk, and serviceability so each shows on the panel schedule.
- Label the plan and match it to the panel directory.

**Professional**

This design uses more branch-circuit granularity than a minimum-code house: separate circuits by room and use, dedicated circuits for predictable loads, and a service-layer routing strategy that allows conductor replacement. The cost is more breakers, conductors, boxes, and panel space; the return is fault isolation, simpler maintenance, fewer nuisance shutdowns, and easier upgrades. Every added circuit still meets the same conductor-sizing, overcurrent, box-fill, derating, and labeling rules as a required circuit.

**Code**

```
Branch circuits follow the branch-circuit article.
  Required circuits, ratings, and protection.
  Source: NEC Article 210.

A dwelling has fixed required circuits.
  Small-appliance, laundry, bathroom, and the load-calculated general circuits.
  Source: NEC 210.11.

The Oregon amendments concentrate in GFCI and AFCI.
  The 2023 OESC is the 2023 NEC plus Table 1-E; NEC language not listed in the table is unamended; the edition in force is confirmed at permit application.
  Source: OAR 918-305-0100; OESC Table 1-E.
```

## 12.2 Conductor Ampacity And Wire Sizing

Conductor size is set by the load, the overcurrent device, the insulation and termination temperature rating, and any derating for bundled conductors or ambient heat. The small-conductor rule fixes the common branch-circuit sizes.

**Applied**

Size conductors from the load and the tables, not from habit:

- 14 AWG copper on a 15 A circuit, 12 AWG on 20 A, 10 AWG on 30 A (the small-conductor limits).
- Size a continuous load (three hours or more) and its breaker at 125 percent of the load.
- Derate when more than three current-carrying conductors share a raceway.
- Use copper for branch circuits; reserve aluminum for large feeders and service conductors with aluminum-rated terminals and antioxidant compound.
- Check voltage drop on long runs after the ampacity check (next section).

**Professional**

NEC Table 310.16 gives conductor ampacity. For circuits of 100 A and less the 60-degree-Celsius column governs the as-installed ampacity; the 75-degree column applies to larger circuits, and the 90-degree column is used only for derating math, not as the installed ampacity, where terminations are rated 60 or 75 degrees. NEC 240.4(D) caps the small conductors: 15 A on 14 AWG copper, 20 A on 12 AWG, 30 A on 10 AWG. Adjustment for more than three current-carrying conductors follows Table 310.15(C)(1): 80 percent for four to six, 70 percent for seven to nine, 50 percent for ten to twenty. Aluminum is code-acceptable at 6 AWG and larger and is standard for service and large feeders, but it is not used in 14 or 12 AWG branch circuits; the minimum branch-circuit conductor is 14 AWG copper.

**Code**

```
Conductor ampacity comes from the ampacity table.
  The 60-degree column governs circuits 100 A and less at standard terminations.
  Source: NEC Table 310.16.

Small conductors carry fixed overcurrent caps.
  14 AWG copper at 15 A, 12 AWG at 20 A, 10 AWG at 30 A.
  Source: NEC 240.4(D).

Continuous loads size at 125 percent.
  Branch-circuit conductor and overcurrent sizing, with continuous loads at 125 percent.
  Source: NEC 210.19; NEC 210.20.

Bundled conductors derate.
  80 percent for four to six current-carrying conductors, 70 percent for seven to nine, 50 percent for ten to twenty.
  Source: NEC Table 310.15(C)(1).
```

## 12.3 Voltage Drop

Voltage drop is advisory in the NEC, not an enforceable rough-in item, but a long run at the limit of its ampacity can still deliver poor performance to the equipment at the end. On long circuits this project upsizes the conductor to hold the recommended drop.

**Simple**

Wire has resistance, so a long run loses voltage between the panel and the far end. The code only recommends a limit. A motor at the end of a long undersized run starts weakly, runs hot, and wears out early. The fix on a long run is one size thicker wire, decided when the circuit is planned.

**Professional**

The voltage-drop guidance in NEC 210.19(A) is an informational note, not a mandatory rule: it recommends keeping branch-circuit drop under 3 percent and combined feeder-plus-branch drop under 5 percent, which at 120 V is about 3.6 V on the branch and 6 V total. An inspector cannot fail a rough inspection for voltage drop, but a long-service design treats the 3 percent recommendation as a working standard. A 20 A, 120 V circuit in 12 AWG copper is generally fine at 50 feet and can exceed 3 percent drop near 100 feet depending on load; the response is to upsize the run to 10 AWG. The drop is calculated as V = (2 × K × I × L) / CM, where K is 12.9 for copper, I is the load in amperes, L is the one-way run length in feet, and CM is the conductor circular-mil area. A conductor passes the ampacity test first, then the voltage-drop check.

**Applied: design-guidance conductor sizing (this project, applying NEC 210.19(A))**

| One-way run | 15 A circuit (14 AWG) | 20 A circuit (12 AWG) |
|---|---|---|
| Up to 50 ft | 14 AWG holds under 3 percent | 12 AWG holds under 3 percent |
| 50 to 100 ft | Upsize to 12 AWG for continuous or near-rated loads | Upsize to 10 AWG for continuous or near-rated loads |
| Over 100 ft | Calculate per circuit; upsize as the formula requires | Calculate per circuit; upsize as the formula requires |

This table is design guidance applying the NEC 210.19(A) informational note, not a code requirement. Any circuit that departs from it gets a project-specific calculation.

**Code**

```
The voltage-drop limit is advisory.
  Recommended maximum of 3 percent on a branch circuit and 5 percent on feeder plus branch; an informational note, not an enforceable requirement; this project designs to it.
  Source: NEC 210.19(A), informational note.

The drop is calculated, not estimated.
  V = (2 × K × I × L) / CM, with K = 12.9 for copper, I the load in amperes, L the one-way length in feet, and CM the conductor circular-mil area.
  Source: NEC Chapter 9, Table 8 conductor properties.
```

## 12.4 Required And Dedicated Circuits

The code sets a floor of required circuits, and predictable large or critical loads get their own dedicated circuit so an appliance does not lose power to an unrelated trip.

**Applied**

Provide the required circuits and a dedicated-circuit list before rough-in:

- At least two 20 A small-appliance circuits serving the kitchen and dining counters and the refrigerator.
- At least one 20 A laundry circuit and one 20 A bathroom receptacle circuit.
- Dedicated circuits for the range or cooktop, oven, dryer, dishwasher, disposal, water heater, well and booster pumps, any sump or sewage pump, the heat pump and air handler, the network rack, and EV charging.
- The refrigerator and a built-in microwave on their own 20 A circuits as best practice.

Mark each dedicated circuit on the plan, the panel schedule, and the as-built.

**Professional**

NEC 210.11(C) requires the two small-appliance circuits, the laundry circuit, and the bathroom circuit in addition to the calculated general-lighting-and-receptacle circuits. Code-required dedicated circuits include the electric range or cooktop (typically 50 A, 240 V per NEC 210.19 and 422), the electric dryer (30 A, 240 V), the water heater (sized to the equipment), and the EV charger (240 V per NEC 625.40). The dishwasher and disposal are best practice on separate 20 A circuits though the code does not mandate a dedicated circuit for the disposal. Heat-pump and mini-split circuits are sized per the equipment nameplate. A dedicated circuit protects uptime as much as capacity: a freezer does not trip with a countertop appliance, and a sewage pump is not hidden on a general basement circuit.

**Code**

```
The required dwelling circuits are fixed.
  Two 20 A small-appliance circuits, one 20 A laundry circuit, one 20 A bathroom circuit.
  Source: NEC 210.11(C).

Fixed appliances take rated circuits.
  Range or cooktop typically 50 A at 240 V; dryer 30 A at 240 V; each per its rating.
  Source: NEC 210.23; NEC 422.10.

EV supply equipment takes a dedicated circuit.
  One EVSE per dedicated branch circuit; capacity planning in the electrical service chapter.
  Source: NEC 625.40.

Equipment circuits follow the nameplate.
  Heat-pump, water-heater, and appliance circuits sized to the equipment nameplate and instructions.
  Source: NEC 110.3(B); the manufacturer's installation instructions.
```

## 12.5 Kitchen Circuits

The kitchen carries the densest load in the house. The two small-appliance circuits serve the counters and refrigerator, the countertop receptacle spacing is fixed by code, and the large appliances get their own circuits.

**Applied**

- Run at least two 20 A small-appliance circuits to the counters; these serve wall, floor, and countertop receptacles and the refrigerator, and carry no other outlets.
- Space countertop receptacles so no point along the counter wall is more than 24 inches from a receptacle (48 inches maximum spacing), and provide a receptacle for any counter space 12 inches or wider.
- Mount countertop receptacles on or not more than 20 inches above the counter; a below-counter receptacle no longer serves a countertop.
- Provide the island or peninsula receptacle on or above the surface, or install the provision for a future receptacle if none is installed now.
- Give the dishwasher and disposal their own 20 A circuits.

**Professional**

NEC 210.52(C) sets the countertop spacing (24 inches to a receptacle, receptacle required for a 12-inch or wider counter, on or within 20 inches above the surface, none required directly behind a range or sink). The 2023 NEC makes an island or peninsula receptacle optional (NEC 210.52(C)(2)): if none is installed, a provision for future addition is required, which some jurisdictions read as a stubbed junction box, so the local expectation is confirmed at rough-in. The refrigerator may share a small-appliance circuit but is placed on its own 20 A circuit here. Oregon struck the 2023 NEC 210.8(D) appliance-GFCI list entirely: Table 1-E rewrites 210.8(D) to require appliance GFCI per 422.5 only, and Oregon's 422.5 does not adopt the dishwasher item, so dwelling dishwasher, range, oven, dryer, and microwave circuits carry no code GFCI requirement in Oregon. One dependency survives: where a specific appliance's listing or installation instructions require GFCI, NEC 110.3(B) enforces the manufacturer's requirement, so the manufacturer's instructions are verified at appliance selection.

**Code**

```
The small-appliance circuits serve the counters only.
  Two or more 20 A circuits serving the kitchen, pantry, and dining counters and the refrigerator, with no other outlets.
  Source: NEC 210.11(C)(1).

Countertop receptacle spacing is fixed.
  No point along the counter wall more than 24 inches from a receptacle; any counter 12 inches or wider gets one; mounted on or within 20 inches above the surface; the island or peninsula receptacle is optional with a required future provision.
  Source: NEC 210.52(C); NEC 210.52(C)(2).

Oregon struck the appliance-GFCI list.
  Table 1-E rewrites 210.8(D) to require appliance GFCI per 422.5 only, striking the 2023 NEC's twelve-appliance list; Oregon's 422.5 does not adopt the dishwasher item, so dwelling dishwasher, range, oven, dryer, and microwave circuits carry no code GFCI requirement; an appliance whose listing requires GFCI still gets it.
  Source: OESC Table 1-E, 210.8(D) and 422.5 entries; NEC 110.3(B).
```

## 12.6 Receptacle Placement

General-room receptacle spacing keeps a cord reachable from any point along a wall so rooms do not depend on extension cords. Placement is decided while the walls are open, which in a concrete house means before masonry, furring, and finishes fix the route.

**Applied**

- Space general receptacles so no point along a wall line is more than 6 feet from a receptacle (12-foot maximum spacing).
- Provide a receptacle for any wall space 2 feet or wider.
- Add receptacles for the planned bed, desk, sofa, television, chargers, cleaning equipment, and exterior decorations.
- Provide at least one outdoor receptacle at the front and back, a garage receptacle, a hallway receptacle for halls 10 feet or longer, and receptacles in basements and at the laundry.
- Use tamper-resistant receptacles throughout the dwelling and weather-resistant receptacles with in-use covers outdoors.

**Professional**

NEC 210.52(A) sets the general spacing (no point along the wall more than 6 feet from a receptacle, any wall 2 feet or wider gets one). NEC 210.52 also requires the countertop, bathroom, laundry, garage, basement, hallway, and outdoor receptacles, NEC 210.8(F) covers the outdoor dwelling outlets, and NEC 406.12 requires tamper-resistant receptacles in dwellings with NEC 406.9 governing weather-resistant devices and in-use covers in wet locations. More receptacles are easier to live with but still need correct boxes, conductors, protection, and panel capacity.

**Code**

```
General receptacle spacing is fixed.
  No point along a wall line more than 6 feet from a receptacle; any wall 2 feet or wider gets one.
  Source: NEC 210.52(A).

Outdoor, garage, basement, and hallway receptacles are required.
  Front and back outdoor receptacles, garage and basement receptacles, and hallway receptacles per the section.
  Source: NEC 210.52(E); NEC 210.52(G); NEC 210.8(F).

Receptacle types match the exposure.
  Tamper-resistant throughout the dwelling; weather-resistant devices with in-use covers in damp and wet locations.
  Source: NEC 406.12; NEC 406.9.
```

## 12.7 GFCI Protection

Ground-fault circuit-interrupter protection guards against shock in wet and grounded areas. Oregon amends the 2023 NEC GFCI list in several places, so the Oregon rules govern here rather than the unamended national text.

**Simple**

A GFCI shuts a circuit off in a fraction of a second when current leaks to ground. Current leaking to ground is what happens when a person becomes part of the circuit. It is required in the wet and grounded areas of the house, where that leak is most likely.

**Applied**

Provide GFCI protection, per the Oregon-amended list, at:

- Bathrooms, garages, outdoors, crawl spaces, and unfinished basement areas.
- Kitchen receptacles that serve the countertop surfaces.
- Laundry areas and within 6 feet of any sink.
- The countertop, wet-bar, and similar receptacles.

Provide it at the breaker or the first receptacle. A single receptacle dedicated to a sump pump does not require GFCI; a duplex receptacle at a sump pump does. A receptacle serving only a permanently installed security system may omit GFCI if labeled "not GFCI protected."

**Professional**

NEC 210.8(A) governs dwelling GFCI, and the Oregon Table 1-E amendments narrow several items from the 2023 NEC: basement GFCI is limited to unfinished, non-habitable portions rather than all basements; kitchen GFCI is limited to receptacles serving the countertop surfaces rather than all kitchen receptacles; and the exception for listed HVAC equipment expires September 1, 2026, after which HVAC receptacles require GFCI. The sump-pump carve-out permits a single dedicated receptacle without GFCI while requiring it on a duplex, and Oregon's 422.5 extends the same treatment to sewage pumps. On appliances, Oregon struck the entire 2023 NEC 210.8(D) twelve-item list and pointed the section to 422.5, whose dishwasher item reads "Not adopted by the State of Oregon": a dwelling dishwasher circuit, hardwired or cord-and-plug, needs no GFCI under the 2023 OESC. The kitchen location rules do not catch the under-counter receptacle either, because Oregon limits kitchen GFCI to receptacles serving countertop surfaces and did not adopt the sinks-and-food-preparation item, and the January 2025 errata added an exception for a labeled single appliance receptacle in a dedicated space. Manufacturer-required GFCI still applies through NEC 110.3(B).

**Code**

```
Dwelling GFCI locations follow the Oregon-amended list.
  Bathrooms, garages, outdoors, crawl spaces, and unfinished non-habitable basement areas; kitchens only at receptacles serving countertop surfaces; the sinks-and-food-preparation item (210.8(A)(7)) is not adopted; the listed-HVAC exception expires September 1, 2026; a labeled single receptacle in a dedicated appliance space is exempt at several locations (errata Exception No. 5, January 1, 2025).
  Source: OESC Table 1-E amendments to NEC 210.8(A).

Sump and sewage pumps have a defined carve-out.
  A labeled single dedicated receptacle is exempt; a duplex receptacle requires GFCI; a security-system single receptacle is exempt when labeled "not GFCI protected."
  Source: OESC Table 1-E, 210.8(A) and 422.5(A)(6) entries.

The appliance-GFCI list is struck in Oregon.
  210.8(D) requires appliance GFCI per 422.5 only; Oregon's 422.5 does not adopt the dishwasher item; manufacturer-required GFCI still applies.
  Source: OESC Table 1-E, 210.8(D) and 422.5 entries (23oesc-table1-E.pdf, oregon.gov/bcd); NEC 110.3(B).
```

## 12.8 AFCI Protection

Arc-fault circuit-interrupter protection reduces fire risk from arcing in wiring and cords. Oregon carves several areas out of the 2023 NEC AFCI list, so the Oregon rules control where AFCI is and is not required.

**Simple**

An AFCI breaker detects the electrical signature of an arc: current jumping a gap at a damaged wire, a loose terminal, or a crushed cord. Arcs start fires inside walls, where nothing is visible until the fire is established. The breaker opens the circuit at the arc signature instead of waiting for enough current to trip an ordinary breaker.

**Applied**

Provide AFCI protection, per the Oregon-amended list, on the 120 V, 15 and 20 A circuits serving:

- Bedrooms, living rooms, family rooms, parlors, dens, libraries, sunrooms, recreation rooms, closets, and finished basements.

Oregon does not require AFCI on branch circuits serving:

- Hallways, kitchen receptacles, and laundry areas.
- Dining-room GFCI-protected receptacles.
- Circuits serving an appliance that is fastened in place or not easily moved.

Use a combination AFCI breaker as the standard method ($40-$60 per breaker against about $10 for a standard breaker, 2026) and plan the protection when the circuit is designed, not at final inspection.

**Professional**

NEC 210.12(B) sets the baseline AFCI list, and the Oregon Table 1-E amendment removes hallways, kitchens, laundry areas, dining-room GFCI receptacles, and circuits to fixed or fastened appliances from it. The combination AFCI breaker is the dominant field method; the other listed methods carry wiring-distance caps and depend on listed devices that are not always available. A 120 V smoke alarm on a branch circuit is an outlet under the code and is subject to AFCI wherever the circuit serves an AFCI-required area; the Article 760 fire-alarm exception applies to low-voltage fire-alarm systems with control panels, not to 120 V residential smoke alarms, so smoke-alarm circuits in Oregon are planned as AFCI-required.

**Code**

```
AFCI locations follow the Oregon-amended list.
  Required on 120 V, 15 and 20 A circuits in bedrooms, living and family rooms, parlors, dens, libraries, sunrooms, recreation rooms, closets, and finished basements; not required (Oregon amendment) in hallways, kitchen receptacles, laundry areas, dining-room GFCI receptacles, or circuits to fixed or fastened appliances.
  Source: OESC Table 1-E amendments to NEC 210.12(B).

The combination breaker is the standard method.
  A combination-type AFCI breaker protects the full circuit; the alternative listed methods carry wiring-distance caps.
  Source: NEC 210.12(A).
```

## 12.9 Bathroom, Laundry, Basement, Garage, And Outdoor Circuits

The wet and outdoor zones combine higher shock risk with harsher environments, so their circuits pair the right protection with location-rated devices, enclosures, and covers.

**Applied**

- Bathrooms: a 20 A receptacle circuit, GFCI-protected receptacles, exhaust fan, and any heated floor or bidet seat on their planned circuits.
- Laundry: a 20 A circuit for the washer, the dryer circuit, and any heat-pump laundry equipment.
- Basement: mechanical-equipment circuits, shop-tool circuits, and sump or sewage-pump circuits separate from general receptacles.
- Garage: tool, opener, freezer, and lighting circuits, with the reserved EV provision.
- Outdoors: receptacles, lighting, pumps, gates, and cameras on weather-rated devices with in-use covers.

Identify wet-area and outdoor circuits clearly at the panel.

**Professional**

Wet and outdoor circuits coordinate the load, the environment, the protection device, the enclosure rating, the receptacle type, and the cover. NEC 210.8 sets the GFCI locations (with the Oregon amendments above), NEC 406.9 requires weather-resistant receptacles and in-use covers in damp and wet locations, and luminaires and equipment are listed for damp or wet locations per NEC 410.10. An indoor-rated device under a roof overhang is not automatically acceptable outdoors; the fixture and receptacle carry the location listing the exposure requires.

**Code**

```
Wet-area protection follows the amended GFCI list.
  Bathrooms, laundry areas, basements, garages, and outdoor receptacles per the Oregon-amended locations.
  Source: NEC 210.8(A) and (F), as amended by OESC Table 1-E.

Devices match the location.
  Weather-resistant receptacles with in-use covers in damp and wet locations; luminaires listed for the exposure.
  Source: NEC 406.9; NEC 410.10.
```

## 12.10 Lighting Outlets And Switching

Every habitable room and traffic area gets a switched lighting outlet, closets follow the fixture-clearance rules, and new switch boxes get a neutral so smart controls can be added without rewiring. The residential energy code sets the high-efficacy lamp requirement.

**Applied**

- Provide at least one wall-switched lighting outlet in every habitable room, the kitchen, bathrooms, hallways, stairways, the garage, and at exterior egress doors.
- Switch stairways and long halls from both ends.
- Provide a neutral conductor at every switch box for smart-switch compatibility.
- Keep closet fixtures to the permitted types and clearances.
- Use high-efficacy (LED) fixtures; the energy code requires them in most rooms.

**Professional**

NEC 210.70 requires the switched lighting outlets. NEC 404.2(C) requires a grounded (neutral) conductor at switch locations for new construction, so every switch box is wired with a neutral (the added 14/3 or 12/3 cost is minor against lifetime smart-switch compatibility). NEC 410.16 governs closet lighting: incandescent fixtures with exposed lamps are prohibited, enclosed LED or fluorescent fixtures are permitted, and the fixture keeps a 12-inch clearance from the nearest storage. NEC 410.10 sets the damp and wet location listings. NEC 314.16 governs box fill: a standard 18-cubic-inch single-gang box holds about nine 14 AWG or eight 12 AWG conductors after device and grounding allowances, which is checked at multi-circuit and four-way switch boxes. The residential energy code (ORSC N1107.2) requires at least 90 percent of permanently installed luminaires in kitchens, bathrooms, laundry rooms, dining rooms, and living rooms to be high-efficacy, which LED fixtures meet.

**Code**

```
Switched lighting outlets are required room by room.
  Habitable rooms, kitchen, bathrooms, halls, stairs, garage, and exterior egress doors.
  Source: NEC 210.70.

Every new switch box carries a neutral.
  A grounded conductor at switch locations in new construction.
  Source: NEC 404.2(C).

Closet luminaires are restricted.
  Exposed incandescent lamps prohibited; enclosed fixtures permitted with a 12-inch clearance from storage.
  Source: NEC 410.16.

Box fill is calculated.
  An 18-cubic-inch single-gang box holds about nine 14 AWG or eight 12 AWG conductors after device and grounding allowances.
  Source: NEC 314.16.

Most fixed lighting must be high-efficacy.
  At least 90 percent of permanently installed luminaires in kitchens, bathrooms, laundry, dining, and living rooms.
  Source: ORSC N1107.2.
```

## 12.11 Smoke And Carbon Monoxide Alarms

Smoke and carbon monoxide alarms in new construction are hardwired, interconnected, and battery-backed, placed by the residential code. In Oregon their 120 V circuits are treated as AFCI-required.

**Simple**

Smoke alarms in a new house run on house power, keep a backup battery, and connect to each other. When one sounds, all of them sound, so a basement fire wakes someone sleeping two floors up. Carbon monoxide alarms are wired the same way. Carbon monoxide has no smell, and the interconnected alarms are the only warning.

**Applied**

- Place smoke alarms in each sleeping room, immediately outside each sleeping area, and on every story including basements and habitable attics.
- Place carbon monoxide alarms outside each sleeping area, on every level including basements, and in or within 15 feet of each bedroom.
- Hardwire all alarms at 120 V with battery backup and interconnect them so one alarm sounds all.
- Wire interconnected alarms with three-conductor cable (14/3 or 12/3) for the interconnect signal.
- Use combination smoke-and-CO alarms at shared locations.

**Professional**

ORSC R314 sets the smoke-alarm locations and requires hardwired, interconnected, battery-backup alarms listed to UL 217 in new construction; wireless listed alarms may satisfy interconnection. ORSC R315 and ORS 476.725 set the carbon monoxide alarm locations and require hardwired, interconnected alarms listed to UL 2034 where the dwelling has fuel-burning appliances, a fireplace, or an attached garage, which a house with an LP generator, an LP appliance, or an attached garage will have. A 120 V smoke alarm is an outlet subject to AFCI where the circuit serves an AFCI-required area, so these circuits are planned as AFCI in Oregon; no dedicated circuit is required, and the alarms are commonly powered from a lighting circuit in a frequently used area.

**Code**

```
Smoke alarms are placed, powered, and interconnected by rule.
  In each sleeping room, outside each sleeping area, and on every story; hardwired 120 V with battery backup, interconnected, listed to UL 217.
  Source: ORSC R314.

Carbon monoxide alarms accompany fuel appliances or an attached garage.
  Outside each sleeping area, on every level, and within 15 feet of each bedroom; hardwired and interconnected in new construction, listed to UL 2034.
  Source: ORSC R315; ORS 476.725.

Smoke-alarm circuits are planned as AFCI.
  A 120 V smoke alarm is an outlet subject to AFCI where its circuit serves an AFCI area; the low-voltage fire-alarm exception does not cover 120 V residential alarms.
  Source: NEC 210.12; NEC Article 760.
```

## 12.12 Low-Voltage, Network, And Communications Wiring

Low-voltage cabling carries data, cameras, alarms, thermostats, and controls. This chapter sets the installation and separation rules; the specific network, camera, and automation product choices and topology are handled in the smart home and local automation chapter, which references these rules.

**Applied**

- Run low-voltage cabling in separate conduits or pathways from line-voltage wiring.
- Home-run data cables to the network rack and label both ends before the walls close.
- Use plenum-rated cable in air-handling spaces, riser-rated cable in vertical shafts, and general-purpose cable elsewhere.
- Plan drops for the internet entry, the rack, wireless access points, offices, entertainment locations, cameras, doorbells, thermostats, and any wired sensors, plus a spare pathway.
- Do not use copper-clad aluminum for Ethernet.

**Professional**

NEC 725.136 requires Class 2 and Class 3 circuits to be separated from power circuits, not sharing a raceway or enclosure without a barrier, with a limited exception for cable that solely connects to the equipment its power conductors serve. Cable listing follows location: plenum (CMP), riser (CMR), or general-purpose (CM) under Article 800 for communications and Article 725 for control and signaling. Power over Ethernet is addressed by NEC 840.160 and 725.144, with standard four-pair cable carrying up to 60 watts before additional thermal ratings apply, and copper-clad aluminum is not permitted for Ethernet. The 2023 NEC reorganized these articles: Class 1 moved to Article 724 and the Class 2 and Class 3 cable listings moved to Article 722, so any older commentary is checked for shifted article numbers. No Oregon Table 1-E item amends Article 840 or the low-voltage articles beyond one workmanship amendment at 800.24(A), so the 2023 NEC baseline governs this work in Oregon. Scope boundary: this chapter states installation method and separation; the smart home chapter states product selection and system topology.

**Code**

```
Low-voltage circuits stay separated from power.
  Class 2 and Class 3 circuits share no raceway or enclosure with power circuits without a barrier.
  Source: NEC 725.136.

Cable listing follows location.
  Plenum (CMP), riser (CMR), or general-purpose (CM) listing per the communications and signaling articles.
  Source: NEC Article 800; NEC Article 722.

Power over Ethernet has thermal limits.
  Up to 60 watts on standard four-pair cable before additional ratings apply; copper-clad aluminum is not permitted for Ethernet.
  Source: NEC 840.160; NEC 725.144.

Article 840 applies in Oregon as published.
  No Table 1-E item amends Article 840; the only NEC Chapter 8 amendment is 800.24(A) (cable support and workmanship, with a plenum cable-tie listing sentence); the 2023 NEC moved Class 1 to Article 724 and the Class 2 and 3 cable listings to Article 722, so older references carry shifted numbers.
  Source: OESC Table 1-E (800.24(A) entry); 2023 NEC Chapter 8.
```

## 12.13 Service-Layer Routing And Future Circuits

A conductor route buried in concrete cannot be changed without cutting the structure, so branch circuits favor accessible service-layer conduit, and spare conduit with pull strings reserves capacity for circuits added long before the structure wears out.

**Applied**

Route branch circuits by preference:

1. Accessible service-layer conduit.
2. Interior partition walls where future change is likely.
3. Planned concrete-wall sleeves or conduits where the route is fixed.
4. Concealed slab runs only where there is no better option and the design approves it.

Install pull strings in every spare conduit, label both ends with the destination and intended use, and keep junction boxes accessible.

**Professional**

Branch-circuit routing accounts for conductor replacement, pull length, bend count, junction-box access, box and raceway fill, support spacing, physical protection, firestopping, air sealing, and separation from plumbing and low-voltage systems. Treating conduit as part of the long-service strategy matters most in a concrete house, where the electrical components will be replaced several times over the life of the structure. Junction boxes are not buried; pull points stay accessible.

**Code**

```
Junction boxes stay reachable.
  Accessible without removing building finish or structure; no buried boxes.
  Source: NEC 314.29.

Fill is calculated for boxes and raceways.
  Box fill per the box-fill rules; raceway fill per the Chapter 9 tables.
  Source: NEC 314.16; NEC Chapter 9, Tables 1 and 4 through 8.

Conductors are protected and supported.
  Physical protection and minimum cover; box and raceway support per the support rules.
  Source: NEC 300.4; NEC 300.5; NEC 314.23; NEC 300.11.
```

## 12.14 Inspection, Testing, And Records

Branch-circuit work is inspected at rough-in and final, and the panel directory, device testing, and as-built record let a future owner or electrician work on the system without opening walls.

**Applied**

Before cover, verify and photograph:

- Boxes mounted and accessible, conductors protected, routes matching the plan.
- Location-rated devices and covers in wet and outdoor areas.
- GFCI and AFCI protection installed where the Oregon-amended rules require it.
- Smoke and CO alarm wiring coordinated and interconnected.
- Low-voltage cabling separated and labeled.
- Panel schedule matching the field wiring.

At final, test each GFCI and AFCI device, check receptacle polarity and grounding, verify switch legs and lighting controls, and record the results. AFCI breakers test at the panel with the breaker's test button; GFCI protection tests at whichever device provides it, the receptacle or the breaker.

**Professional**

Branch-circuit commissioning reviews the panel schedule and breaker types, tests the GFCI and AFCI devices, checks receptacle polarity and grounding, verifies switch legs and lighting-control operation, tests low-voltage continuity, and certifies network cabling where specified. The as-built record captures the circuit list, conductor sizes, protection types, and low-voltage pathways, and any field deviation from the plan is documented so a later diagnosis starts from fact rather than assumption.

**Code**

```
Rough-in and final inspections gate the work.
  Rough-in before cover, final before energized use; the permit posted near the panel.
  Source: OAR 918-305.

Protection devices are verified at final.
  GFCI and AFCI per the Oregon-amended lists, tested at final.
  Source: NEC 210.8 and 210.12, as amended by OESC Table 1-E.

Clearance and labeling are confirmed.
  Working clearance maintained and the panel directory accurate.
  Source: NEC 110.26; NEC Article 408.
```
