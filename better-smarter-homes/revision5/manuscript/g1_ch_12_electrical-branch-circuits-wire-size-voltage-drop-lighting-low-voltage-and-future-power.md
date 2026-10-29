# Chapter 12: Electrical: Branch Circuits, Wire Size, Voltage Drop, Lighting, Low Voltage, And Future Power

This chapter covers the circuits that leave the panel: the required and dedicated branch circuits, conductor sizing and voltage drop, receptacle placement, GFCI and AFCI protection, kitchen and wet-area circuits, lighting outlets and switching, smoke and carbon monoxide alarms, and the low-voltage and communications cabling. The service, panels, grounding, surge protection, backup power, solar readiness, and EV service capacity are established in the electrical service chapter; this chapter delivers power and signal to the rooms.

The electrical code of record is the 2023 Oregon Electrical Specialty Code (OESC), the 2023 National Electrical Code (NEC) with Oregon amendments in Table 1-E, effective October 1, 2023, with a January 2025 errata. Oregon does not amend most residential dwelling branch-circuit provisions; the Table 1-E amendments that matter here modify GFCI and AFCI. Every value below that does not cite a specific Oregon amendment is 2023 NEC baseline. Confirm the edition in force at permit time.

## 12.1 Branch-Circuit Plan And Granularity

A branch-circuit plan built room by room, with more circuits than the code minimum, keeps a single fault from taking down a large part of the house and makes a tripped breaker easy to trace. In a concrete house, where rerouting is expensive, the extra circuits and the accessible routing are planned before rough-in.

**Simple**

The service brings power into the house; branch circuits carry it from the panel to the rooms, lights, outlets, and equipment. Dividing the house into more circuits than the minimum means a problem in one room does not darken another, and a tripped breaker points to a small area instead of half the floor.

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
NEC Article 210: branch circuits; required circuits, ratings, and protection.
NEC 210.11: required branch circuits for a dwelling (small-appliance, laundry, bathroom, and the load-calculated general circuits).
2023 OESC (NEC 2023 + Table 1-E): the adopted code; Oregon amends mainly GFCI and AFCI (see those sections). Confirm the edition at permit time.
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
NEC Table 310.16: allowable ampacity of insulated conductors; 60-degree column governs circuits 100 A and less at standard terminations.
NEC 240.4(D): small-conductor overcurrent limits (14 AWG = 15 A, 12 AWG = 20 A, 10 AWG = 30 A copper).
NEC 210.19 and 210.20: branch-circuit conductor and overcurrent sizing; continuous loads at 125 percent.
NEC Table 310.15(C)(1): adjustment factors for more than three current-carrying conductors in a raceway.
```

## 12.3 Voltage Drop

Voltage drop is advisory in the NEC, not an enforceable rough-in item, but a long run at the limit of its ampacity can still deliver poor performance to the equipment at the end. On long circuits this project upsizes the conductor to hold the recommended drop.

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
NEC 210.19(A) informational note: recommended maximum voltage drop of 3 percent on a branch circuit and 5 percent on feeder plus branch. Advisory, not mandatory.
Voltage-drop formula: V = (2 × K × I × L) / CM; K = 12.9 for copper.
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
NEC 210.11(C): required small-appliance (two 20 A), laundry (20 A), and bathroom (20 A) circuits.
NEC 210.23 and 422.10: branch-circuit ratings for fixed appliances; range/cooktop 50 A / 240 V typical, dryer 30 A / 240 V.
NEC 625.40: dedicated EV supply-equipment circuit (see the electrical service chapter for capacity planning).
Manufacturer instructions: heat-pump, water-heater, and appliance circuits sized to the equipment nameplate.
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

NEC 210.52(C) sets the countertop spacing (24 inches to a receptacle, receptacle required for a 12-inch or wider counter, on or within 20 inches above the surface, none required directly behind a range or sink). The 2023 NEC makes an island or peninsula receptacle optional (NEC 210.52(C)(2)): if none is installed, a provision for future addition is required, which some jurisdictions read as a stubbed junction box, so the local expectation is confirmed at rough-in. The refrigerator may share a small-appliance circuit but is placed on its own 20 A circuit here. Whether the 2023 NEC 210.8(D) expansion of GFCI to clothes dryers, wall ovens, cooktops, and microwaves has been adopted in Oregon is not confirmed in the available Table 1-E excerpts; confirm the appliance-GFCI status with the Building Codes Division before the rough-in rather than assuming either way.

**Code**

```
NEC 210.11(C)(1): two or more 20 A small-appliance circuits serving the kitchen, pantry, and dining counters and the refrigerator; no other outlets.
NEC 210.52(C): countertop receptacle spacing (24 in to a receptacle, 12-in counter requires one, on/within 20 in above surface, island/peninsula receptacle optional per 210.52(C)(2) with a future provision).
NEC 210.8(D): 2023 NEC GFCI expansion to dryers, ovens, cooktops, and microwaves; Oregon Table 1-E adoption unconfirmed, verify with BCD before rough-in.
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
NEC 210.52(A): general receptacle spacing (6 feet to a receptacle, 2-foot wall requires one).
NEC 210.52(E)/(G) and 210.8(F): outdoor, garage, and basement receptacles.
NEC 406.12: tamper-resistant receptacles in dwellings; NEC 406.9: weather-resistant devices and in-use covers in damp/wet locations.
```

## 12.7 GFCI Protection

Ground-fault circuit-interrupter protection guards against shock in wet and grounded areas. Oregon amends the 2023 NEC GFCI list in several places, so the Oregon rules govern here rather than the unamended national text.

**Simple**

A GFCI shuts a circuit off in a fraction of a second when current leaks to ground, which is what happens when a person becomes part of the circuit. It is required in the wet and grounded areas of the house, where that leak is most likely.

**Applied**

Provide GFCI protection, per the Oregon-amended list, at:

- Bathrooms, garages, outdoors, crawl spaces, and unfinished basement areas.
- Kitchen receptacles that serve the countertop surfaces.
- Laundry areas and within 6 feet of any sink.
- The countertop, wet-bar, and similar receptacles.

Provide it at the breaker or the first receptacle. A single receptacle dedicated to a sump pump does not require GFCI; a duplex receptacle at a sump pump does. A receptacle serving only a permanently installed security system may omit GFCI if labeled "not GFCI protected."

**Professional**

NEC 210.8(A) governs dwelling GFCI, and the Oregon Table 1-E amendments narrow several items from the 2023 NEC: basement GFCI is limited to unfinished, non-habitable portions rather than all basements; kitchen GFCI is limited to receptacles serving the countertop surfaces rather than all kitchen receptacles; and the exception for listed HVAC equipment expires September 1, 2026, after which HVAC receptacles require GFCI. The sump-pump carve-out permits a single dedicated receptacle without GFCI while requiring it on a duplex. Whether Oregon adopted the NEC 210.8(D) appliance-GFCI expansion, and the exact GFCI status of the dishwasher circuit under the amended framework, are not confirmed in the available Table 1-E excerpts and are verified with the Building Codes Division before rough-in.

**Code**

```
NEC 210.8(A) with Oregon Table 1-E amendments:
  - GFCI in bathrooms, garages, outdoors, crawl spaces, and unfinished/non-habitable basement areas.
  - Kitchens: only receptacles serving countertop surfaces (Oregon amendment).
  - Unfinished basements only (Oregon amendment to item 5).
  - Listed HVAC equipment exception expires September 1, 2026.
  - Sump pump: single dedicated receptacle exempt; duplex requires GFCI (Oregon amendment).
  - Security-system single receptacle exempt if labeled "not GFCI protected."
NEC 210.8(D): appliance GFCI expansion; Oregon adoption unconfirmed, verify with BCD.
```

## 12.8 AFCI Protection

Arc-fault circuit-interrupter protection reduces fire risk from arcing in wiring and cords. Oregon carves several areas out of the 2023 NEC AFCI list, so the Oregon rules control where AFCI is and is not required.

**Applied**

Provide AFCI protection, per the Oregon-amended list, on the 120 V, 15 and 20 A circuits serving:

- Bedrooms, living rooms, family rooms, parlors, dens, libraries, sunrooms, recreation rooms, closets, and finished basements.

Oregon does not require AFCI on branch circuits serving:

- Hallways, kitchen receptacles, and laundry areas.
- Dining-room GFCI-protected receptacles.
- Circuits serving an appliance that is fastened in place or not easily moved.

Use a combination AFCI breaker as the standard method and plan the protection when the circuit is designed, not at final inspection.

**Professional**

NEC 210.12(B) sets the baseline AFCI list, and the Oregon Table 1-E amendment removes hallways, kitchens, laundry areas, dining-room GFCI receptacles, and circuits to fixed or fastened appliances from it. The combination AFCI breaker is the dominant field method; the other listed methods carry wiring-distance caps and depend on listed devices that are not always available. A 120 V smoke alarm on a branch circuit is an outlet under the code and is subject to AFCI wherever the circuit serves an AFCI-required area; the Article 760 fire-alarm exception applies to low-voltage fire-alarm systems with control panels, not to 120 V residential smoke alarms, so smoke-alarm circuits in Oregon are planned as AFCI-required.

**Code**

```
NEC 210.12(B) with Oregon Table 1-E amendments:
  - AFCI required on 120 V, 15/20 A circuits in bedrooms, living/family rooms, parlors, dens, libraries, sunrooms, recreation rooms, closets, and finished basements.
  - AFCI not required (Oregon amendment) in hallways, kitchen receptacles, laundry areas, dining-room GFCI receptacles, or circuits to fixed/fastened appliances.
NEC 210.12(A): combination AFCI breaker is the standard compliance method.
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
NEC 210.8(A)/(F): GFCI in bathrooms, laundry, basements, garages, and outdoors (Oregon-amended list).
NEC 406.9: weather-resistant receptacles and in-use covers in damp/wet locations.
NEC 410.10: luminaires listed for damp or wet locations as the exposure requires.
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
NEC 210.70: switched lighting outlets required in habitable rooms, kitchen, bathrooms, halls, stairs, garage, and at exterior egress.
NEC 404.2(C): grounded (neutral) conductor required at switch locations in new construction.
NEC 410.16: closet luminaire types and 12-inch storage clearance; exposed incandescent lamps prohibited.
NEC 314.16: box-fill calculation (about nine 14 AWG or eight 12 AWG conductors in an 18-cubic-inch box after allowances).
ORSC N1107.2: at least 90 percent high-efficacy luminaires in kitchens, baths, laundry, dining, and living rooms.
```

## 12.11 Smoke And Carbon Monoxide Alarms

Smoke and carbon monoxide alarms in new construction are hardwired, interconnected, and battery-backed, placed by the residential code. In Oregon their 120 V circuits are treated as AFCI-required.

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
ORSC R314: smoke alarms in each sleeping room, outside each sleeping area, and on each story; hardwired 120 V with battery backup, interconnected, listed to UL 217.
ORSC R315 and ORS 476.725: carbon monoxide alarms outside each sleeping area, on each level, and within 15 feet of each bedroom; hardwired and interconnected in new construction, listed to UL 2034.
NEC 210.12: 120 V smoke-alarm circuits treated as AFCI-required where the circuit serves an AFCI area; the Article 760 exception does not cover 120 V residential smoke alarms.
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

NEC 725.136 requires Class 2 and Class 3 circuits to be separated from power circuits, not sharing a raceway or enclosure without a barrier, with a limited exception for cable that solely connects to the equipment its power conductors serve. Cable listing follows location: plenum (CMP), riser (CMR), or general-purpose (CM) under Article 800 for communications and Article 725 for control and signaling. Power over Ethernet is addressed by NEC 840.160 and 725.144, with standard four-pair cable carrying up to 60 watts before additional thermal ratings apply, and copper-clad aluminum is not permitted for Ethernet. The 2023 NEC reorganized these articles: Class 1 moved to Article 724 and the Class 2 and Class 3 cable listings moved to Article 722, so any older commentary is checked for shifted article numbers. The line between this chapter and the smart-home chapter is that installation method and separation are here, and product selection and system topology are there.

**Code**

```
NEC 725.136: separation of Class 2 and Class 3 circuits from power circuits (no shared raceway or enclosure without a barrier).
NEC Article 800 / 722: communications cable listing by location (CMP plenum, CMR riser, CM general).
NEC 840.160 and 725.144: Power over Ethernet up to 60 watts on standard four-pair cable; copper-clad aluminum not permitted for Ethernet.
2023 NEC reorganization: Class 1 to Article 724, Class 2/3 cable listings to Article 722; verify article numbers in older references.
```

## 12.13 Service-Layer Routing And Future Circuits

Concrete makes a buried conductor route expensive to change, so branch circuits favor accessible service-layer conduit, and spare conduit with pull strings reserves capacity for circuits added long before the structure wears out.

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
NEC 314.29: junction and pull boxes accessible without removing building finish or structure.
NEC 314.16 and Chapter 9 tables: box fill and raceway fill.
NEC 300.4 and 300.5: physical protection of conductors and minimum cover.
NEC 314.23 and 300.11: box and raceway support.
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

At final, test each GFCI and AFCI device, check receptacle polarity and grounding, verify switch legs and lighting controls, and record the results.

**Professional**

Branch-circuit commissioning reviews the panel schedule and breaker types, tests the GFCI and AFCI devices, checks receptacle polarity and grounding, verifies switch legs and lighting-control operation, tests low-voltage continuity, and certifies network cabling where specified. The as-built record captures the circuit list, conductor sizes, protection types, and low-voltage pathways, and any field deviation from the plan is documented so a later diagnosis starts from fact rather than assumption.

**Code**

```
OAR 918-305: rough-in and final electrical inspection; the permit posted near the panel.
NEC 210.8 and 210.12: GFCI and AFCI protection verified at final per the Oregon-amended list.
NEC 110.26 and 408: working clearance and panel labeling.
Records to retain: panel schedule, circuit and conductor list, device test results, low-voltage as-built, and pre-cover photographs.
```
