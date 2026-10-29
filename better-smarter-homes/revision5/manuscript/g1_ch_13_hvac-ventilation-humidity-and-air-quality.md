# Chapter 13: HVAC, Ventilation, Humidity, And Air Quality

This chapter covers the mechanical systems that heat, cool, ventilate, dehumidify, and filter the house: the heating and cooling equipment, whole-house balanced ventilation, local exhaust, range-hood makeup air, dryer exhaust, combustion appliances, radiant floors, humidity control, filtration, duct design, the mechanical room, and commissioning.

For a one- and two-family dwelling in Oregon, the controlling code is the Oregon Residential Specialty Code (ORSC), not the Oregon Mechanical Specialty Code (OMSC). The 2023 ORSC (based on the 2021 IRC, mandatory since April 1, 2024) governs residential mechanical work directly through its mechanical block (Part V) and the energy provisions in Chapter 11. The 2025 OMSC (based on the 2024 IMC and IFGC, mandatory April 1, 2026) applies only to items the ORSC does not address. A 2026 ORSC is anticipated for adoption around October 1, 2026, which will renumber and amend several provisions; values below are given for the 2023 ORSC, and the ones most likely to change are flagged.

## 13.1 Mechanical Code Framing

The residential code controls the mechanical design, and the mechanical specialty code fills only the gaps. Knowing which code owns a detail avoids designing to the wrong requirement.

**Simple**

The house's heating, cooling, and ventilation are governed by the residential code, which has its own mechanical and energy chapters. A separate mechanical code exists for larger buildings and covers only the few residential items the residential code leaves out. The values in this chapter come from the residential code in force.

**Professional**

ORSC R101.2 defers to the OMSC only for items the ORSC does not address and for a few narrow cases such as hydrogen-generating spaces. For a single-family house the ORSC mechanical block (Part V) and the energy provisions in Chapter 11 control the equipment, ventilation, duct, and combustion requirements. Gas-piping design is addressed in ORSC Chapter 24 and Appendix AA, with the IFGC reaching residential work through the OMSC where the ORSC is silent; the specific gas-pressure-test acceptance criteria in those chapters are confirmed against the adopted text before a firm procedure is written.

**Code**

```
2023 ORSC Part V (mechanical) and Chapter 11 (energy): the controlling residential mechanical and energy code; based on the 2021 IRC, mandatory since April 1, 2024.
2025 OMSC (2024 IMC and IFGC): applies only to residential items the ORSC does not address; mandatory April 1, 2026.
ORSC R101.2: the residential code controls; the mechanical specialty code fills gaps.
A 2026 ORSC adoption is anticipated near October 1, 2026; confirm the edition at permit time.
```

## 13.2 Heating And Cooling System Selection

The heating and cooling equipment is chosen from a room-by-room load calculation, sized to that load within the allowed oversize, and rated by the recognized standards. For a long-service all-electric house, a cold-climate heat pump is the default, and the concrete thermal mass lets the equipment run steadily rather than in large swings.

**Simple**

The house has high thermal mass in its concrete, which holds temperature and lets the heating and cooling run gently and steadily. The heating and cooling machine is sized from a real calculation of the house's heat loss and gain, not from a rule of thumb, so it is neither starved nor oversized. For an all-electric house, a heat pump both heats and cools from one machine.

**Applied**

- Calculate the heating and cooling loads room by room before selecting equipment.
- Select equipment from the manufacturer's performance data, sized to the calculated load within the allowed oversize, not by rule of thumb.
- Design the duct system and the registers to the load and the equipment.
- Choose a cold-climate air-source heat pump for western Oregon as the default; evaluate ground-source where the site and climate favor it.
- Treat the heat-generation plant as a defined interface (power, piping, condensate, clearance, noise, replacement path) so the house is not locked around one product too early.

**Professional**

ACCA Manual J is the referenced residential load-calculation method (ORSC M1401.3), Manual S governs equipment selection from expanded performance data within the oversize caps, Manual D governs the duct design, and Manual T governs register and grille selection. Air-source heat pumps are rated by AHRI 210/240 (SEER2 and HSPF2), and water- and ground-source units by AHRI 13256 and 870; ground-source design follows the CSA/ANSI/IGSHPA C448 series. In western Oregon's mild winter design temperatures, a modern cold-climate air-source heat pump (HSPF2 of about 9.0 or higher) typically reaches a favorable life-cycle cost against a ground-source system given the high ground-loop installation cost; eastern Oregon's colder design temperatures shift the balance toward ground-source. An open-loop ground-source system draws on groundwater and triggers Oregon Water Resources Department registration under ORS 537 and the OAR 690 rules, which is resolved before that path is chosen. A ductless heat pump at HSPF2 9.0 in the primary zone is a qualifying measure under the energy code's Additional Measure list. Refrigerant charging and repair are regulated work and are not owner-builder procedures.

**Code**

```
ORSC M1401.3: heating and cooling loads calculated per ACCA Manual J or an approved equivalent.
ACCA Manual S / D / T: equipment selection within oversize caps, duct design, and register selection.
AHRI 210/240: air-source heat pump and air-conditioner ratings (SEER2, HSPF2); AHRI 13256/870 for water- and ground-source.
CSA/ANSI/IGSHPA C448 series: ground-source heat pump design and installation.
ORS 537 and OAR 690: Water Resources Department registration for an open-loop ground-source system.
```

## 13.3 Whole-House Balanced Ventilation

Oregon requires balanced whole-house mechanical ventilation in every new dwelling. Exhaust-only ventilation is not acceptable. The continuous airflow is set by the residential code table or its formula, and the system supplies and exhausts within a close balance.

**Simple**

A tight house needs mechanical ventilation to bring in fresh air and remove stale air, because the envelope no longer leaks enough to do it on its own. Oregon requires a balanced system that both supplies fresh air and exhausts stale air in roughly equal amounts, rather than a fan that only pulls air out. A heat- or energy-recovery ventilator does this while recovering most of the heat from the air it exhausts.

**Applied**

- Provide a balanced ventilation system: paired supply and exhaust fans, a heat- or energy-recovery ventilator, or a central-fan-integrated supply interlocked with exhaust.
- Set the continuous airflow from the code table, or the formula CFM = (0.01 × floor area in square feet) + 7.5 × (bedrooms + 1).
- Balance supply to exhaust within 10 percent.
- Provide user-accessible manual override controls.
- Keep a continuously operating fan at 1.0 sone or quieter so it is not switched off for noise.
- Locate the outdoor intake away from exhaust terminations, the driveway, dryer vents, and dust.

**Professional**

ORSC M1505 sets the whole-house ventilation requirement and, per the BCD technical bulletin, disallows single-point exhaust-only systems that the base IRC would permit. The continuous rate comes from Table M1505.4.3(1) or the equivalent formula; intermittent operation is allowed under Table M1505.4.3(2) with runtime multipliers (four times the rate at 25 percent runtime, twice at 50 percent), and extrapolation beyond the table is not permitted. A heat-recovery ventilator providing at least 66 percent sensible efficiency at 1.6 CFM per watt combined fan efficiency, paired with a 2.75 ACH50 envelope, is the energy code's high-achievement measure. The heat-recovery-versus-energy-recovery choice turns on climate, humidity, the radiant-cooling strategy, and maintenance. ASHRAE 62.2-2022 is the best-practice design standard and does not conflict with the ORSC for a system designed to it, except that the ORSC does not grant the 62.2 blower-door infiltration credit.

**Code**

```
ORSC M1505: balanced whole-house mechanical ventilation required; exhaust-only not acceptable.
ORSC Table M1505.4.3(1): continuous airflow rate; formula CFM = (0.01 × floor area) + 7.5 × (bedrooms + 1).
ORSC Table M1505.4.3(2): intermittent-operation multipliers; no extrapolation beyond the table.
Balance within 10 percent supply-to-exhaust; manual override required; 1.0 sone limit for continuous fans.
ASHRAE 62.2-2022: best-practice design standard (ORSC does not grant the 62.2 infiltration credit).
```

## 13.4 Local Exhaust And Range-Hood Makeup Air

Kitchens and bathrooms need local exhaust to the outdoors, and a large kitchen exhaust needs makeup air so it does not depressurize the house or backdraft a combustion appliance.

**Simple**

Cooking and showering make grease, steam, odors, and moisture that a local fan sends outside. In a tight house, a powerful kitchen hood pulls so much air out that the house needs replacement air brought in, or it will pull air backward down other vents.

**Applied**

- Exhaust each bathroom at a minimum of 50 CFM intermittent or 20 CFM continuous, and the kitchen at 100 CFM intermittent, to the outdoors.
- Terminate kitchen and bath exhaust outdoors with a backdraft damper and no screen, at least 3 feet from openings; do not terminate into an attic, soffit, ridge vent, or crawl space.
- Provide makeup air where any kitchen exhaust exceeds 400 CFM: approximately equal to the exhaust rate, with a damper meeting the code, discharging into the same room.
- Plan the hood, duct route, and makeup air before the cabinet layout is fixed.

**Professional**

ORSC M1505.5 and Table M1505.5 set the minimum local-exhaust capacities, and all kitchen and bath exhaust terminates outdoors (recirculation and attic, soffit, ridge, and crawl terminations are barred). The makeup-air rule (ORSC M1503/M1505) triggers when kitchen exhaust exceeds 400 CFM; below that threshold no makeup air is required. At or above it, makeup air approximately equals the exhaust, includes at least one damper meeting M1503.6.2, and discharges into the same room. The code does not require the makeup air to be tempered, though tempering is recommended for comfort and to prevent the pressure imbalance that can backdraft a combustion appliance. Capture efficiency, not appearance, drives the hood selection.

**Code**

```
ORSC M1505.5 and Table M1505.5: minimum local exhaust (bath 50 CFM intermittent / 20 continuous; kitchen 100 CFM intermittent), terminated outdoors.
ORSC M1503/M1505: kitchen makeup air required where exhaust exceeds 400 CFM; approximately equal to exhaust, damper per M1503.6.2, into the same room. Tempering recommended, not required.
Termination: backdraft damper, no screen, at least 3 feet from openings; no attic, soffit, ridge, or crawl termination.
```

## 13.5 Dryer Exhaust

The clothes-dryer exhaust is a smooth metal duct within a length limit, terminated outdoors. A condensing heat-pump dryer avoids the duct entirely and suits the airtight envelope.

**Applied**

- Use a smooth-interior metal duct, 4-inch nominal, 28-gauge minimum.
- Keep the equivalent duct length within 35 feet, deducting for elbows (about 5 feet per 90-degree and 2.5 feet per 45-degree elbow); design to 25 feet to stay ahead of the tightening national baseline.
- Use a listed transition duct no longer than 8 feet, not concealed.
- Terminate outdoors with a backdraft damper and no screen, at least 3 feet from openings.
- Label the equivalent length within 6 feet of the dryer connection where it exceeds 35 feet.
- Consider a condensing heat-pump dryer, which needs a condensate drain instead of a duct.

**Professional**

ORSC M1502 sets the dryer-exhaust rules. The equivalent length from the dryer to the terminal is limited to 35 feet excluding the transition duct, with elbow deductions per Table M1502.4.6.1. The transition duct is a single length no longer than 8 feet, listed and labeled to UL 2158A, and not concealed. Oregon's M1502.4.5 amendment prohibits domestic booster fans while permitting UL 705 dryer-exhaust duct power ventilators, which are commonly confused. A listed condensing heat-pump dryer is exempt from the duct requirement, removes a wall penetration and its exhaust imbalance, and drains condensate to an indirect waste per the appliance listing and the plumbing code. The 2024 IRC reduces the base equivalent length to 25 feet, so designing to 25 feet now avoids a rework if the 2026 ORSC adopts that baseline.

**Code**

```
ORSC M1502: dryer exhaust; smooth metal duct, 4-inch nominal, 28-gauge minimum; 35-foot equivalent length excluding transition, elbow deductions per Table M1502.4.6.1.
ORSC M1502.4.5 (Oregon amendment): domestic booster fans prohibited; UL 705 duct power ventilators permitted.
Transition duct: single length, 8 feet maximum, listed to UL 2158A, not concealed.
Termination: outdoors, backdraft damper, no screen, at least 3 feet from openings.
Condensing heat-pump dryer: duct-exempt when listed; condensate to indirect waste per OPSC and manufacturer.
```

## 13.6 Combustion Appliances: Solid Fuel And LP Gas

A solid-fuel stove has to be certified and can carry a removal obligation at sale, and LP-gas work requires a licensed installer with no owner-builder exemption. Any combustion appliance inside the thermal envelope is sealed-combustion with outdoor combustion air. The simplest tight-house strategy is all-electric, with combustion added only by deliberate choice.

**Applied**

- Specify only a current EPA- or DEQ-certified wood or pellet stove; a mechanical permit will not issue for an uncertified used stove.
- Plan for the removal-and-destruction obligation that attaches to an uncertified device at sale of the residence.
- Hire a licensed Oregon LPG installer for all LP-gas piping, container setting, and appliance connection; the owner-builder exemption does not cover LP work.
- Use sealed or direct-vent equipment, duct combustion air directly from outdoors for any sealed-combustion appliance inside the thermal envelope, and provide the manufacturer's clearances.
- Provide carbon monoxide alarms wherever a fuel-burning appliance, fireplace, or attached garage is present.

**Professional**

Solid-fuel devices are regulated by DEQ under OAR Chapter 340, Division 262 (authority ORS 468A.460 to 468A.515), separate from the building code. A new device must be EPA- or DEQ-certified at installation, an uncertified used stove cannot be sold or reinstalled, and at sale of a residence an uncertified device is removed and destroyed unless the buyer accepts the obligation in writing. Combustion-air and hearth requirements are in ORSC Chapter 17 and chimney and vent requirements in Chapter 18. LP-gas work is governed by ORS 480.430 to 480.460 and OAR 837-030 under the State Fire Marshal, with no homeowner exemption. The energy code (ORSC N1103) requires sealed combustion with combustion air ducted from outdoors for any appliance inside the thermal envelope, which is an energy requirement layered on the safety rules. The all-electric default avoids gas service, combustion-air conflicts, flue penetrations, and indoor combustion byproducts. Carbon monoxide alarm placement and wiring are detailed with the smoke and carbon monoxide alarm requirements in the branch-circuit chapter.

**Code**

```
OAR 340-262 (ORS 468A.460–468A.515): solid-fuel device certification; no permit for an uncertified used stove; removal-and-destruction at sale of an uncertified device.
ORSC Chapter 17 (combustion air) and Chapter 18 (chimneys and vents).
ORS 480.430–480.460 and OAR 837-030: LP-gas installation by a licensed installer; no homeowner exemption.
ORSC N1103: sealed combustion with outdoor-ducted combustion air for appliances inside the thermal envelope.
ORSC R315: carbon monoxide alarms where fuel-burning appliances, a fireplace, or an attached garage are present (see the branch-circuit chapter).
```

## 13.7 Radiant Floor Heating And Hydronic Zoning

A hydronic radiant floor heats the slab and radiates to the room, pairing naturally with a heat pump and a concrete structure. The tubing, insulation, loop design, and manifold access set its performance and its serviceability.

**Simple**

Radiant heating warms the floor, and the warm floor warms the room, so it feels comfortable without a fan blowing hot air. Warm-water tubing is cast into or fastened under the slab and fed from a manifold, and per-room zones let different rooms hold different temperatures. The manifolds, pumps, and valves are kept reachable, because they are the parts that get serviced.

**Applied**

- Use oxygen-barrier PEX or PEX-AL-PEX in any closed loop that contains ferrous components.
- Fasten tubing to mesh or clips at the design spacing (typically 6 to 12 inches on center) at the design depth, and photograph it before the pour.
- Provide continuous below-slab insulation (R-10 minimum, R-15 to R-20 best practice) and matching perimeter insulation at slab edges.
- Cap loop length per the manufacturer (typically 250 to 300 feet per half-inch loop) and give each loop isolation, balancing, and air-vent provisions at an accessible manifold.
- Pressure-test the tubing before the pour (typically 1.5 times working pressure, held at least 24 hours) and again after the pour.
- Keep the finish-floor R-value within the manufacturer's limit (about 2.0 to 2.5), and design a failed zone valve or actuator to be reachable without demolition.

**Professional**

Radiant tubing follows ASTM F876/F877 (PEX) or F1281 (PEX-AL-PEX), with an EVOH oxygen barrier to DIN 4726 and chlorine resistance to ASTM F2023. An oxygen barrier is mandatory where any wetted part is ferrous (steel boiler, cast-iron circulator, steel manifold), because dissolved oxygen corrodes those parts; non-barrier tubing is acceptable only when every wetted ferrous part is replaced with brass, bronze, or stainless. Below-slab insulation drives response time, and each additional R-1 of finish floor cuts output by roughly 10 percent. The ORSC does not set a hydronic pressure-test value; that comes from the OPSC and the manufacturer. Hydronic water treatment (corrosion and scale inhibitor, biocide, pH buffering) protects the loop, and propylene glycol is used where tubing runs through unconditioned space. Per-room zoning adds valves, actuators, wiring, and balancing, so the manifold layout is designed for service access.

**Code**

```
ASTM F876/F877 (PEX), F1281 (PEX-AL-PEX): radiant tubing; EVOH oxygen barrier to DIN 4726; chlorine resistance ASTM F2023.
Oxygen-barrier tubing mandatory with any ferrous wetted component.
Below-slab insulation R-10 minimum (R-15 to R-20 best practice) with matching slab-edge perimeter insulation.
Hydronic pressure test per OPSC and manufacturer (typically 1.5 times working pressure, 24 hours, before and after the pour).
```

## 13.8 Radiant Cooling Feasibility

Radiant cooling is a fan-free, duct-free way to remove sensible heat, and western Oregon's moderate summer humidity makes it feasible with a paired dehumidification strategy. The controlling constraint is the dew point: a cooled surface below the interior dew point condenses water, which causes mold, slippery floors, and finish damage.

**Applied**

Before committing to radiant cooling, provide:

- Dew-point sensing at representative locations and supply water held above the dew point.
- A dedicated dehumidification system to hold the interior dew point down.
- Window contacts that interrupt cooling when a window opens.
- A floor-surface moisture sensor as a backstop.
- A small backup cooling system for design days when the latent load exceeds the dehumidifier.
- A pre-summer test of the full control sequence.

**Professional**

The radiant surface cannot fall below the interior dew point without condensation, mold, and slippery floors. ASHRAE 55 caps a cooled floor at about 64°F, and coastal western Oregon summer interior dew points run about 55 to 60°F at design conditions, leaving roughly 4 to 9°F of headroom, which is workable but tight. A ceiling radiant surface has more capacity because its comfort-based temperature limit is lower (about 55°F), but that raises the condensation risk if humidity is not controlled. The design supplies water typically 1 to 2°F above the measured or predicted dew point, uses the dew-point sensors, window interlocks, dehumidification, and floor-moisture backstop above, and provides backup cooling. Radiant cooling without dehumidification and backup is not a defensible default, because cooking, showers, and weather drive humidity excursions past the system.

**Code**

```
ASHRAE 55-2023: comfort surface-temperature limits (cooled floor about 64°F, cooled ceiling about 55°F).
ASHRAE Handbook, HVAC Systems and Equipment, Chapter 6 (Radiant Heating and Cooling): design constraints.
Design elements: supply water above dew point, dew-point sensors, window interlocks, dedicated dehumidification, floor moisture backstop, and backup cooling.
```

## 13.9 Humidity And Dehumidification

Indoor humidity is held in a comfort band year-round: dry enough in summer to prevent mold and dust mites, moist enough in winter to be comfortable. A whole-house dehumidifier sized to the latent load carries the summer side and protects any radiant-cooling system.

**Applied**

- Target 30 to 50 percent relative humidity year-round.
- Size a whole-house dehumidifier to the latent portion of the load calculation (commonly 70 to 130 pints per day for a well-built western Oregon house).
- Drain the dehumidifier condensate to an indirect waste, by gravity or a condensate pump.
- Manage moisture sources (showers, cooking, laundry, wet entry, and any leak) through exhaust, drainage, and maintenance, not by adding humidity in winter.

**Professional**

ASHRAE 55 places the comfort humidity band broadly between about 30 and 60 percent relative humidity; the practical residential target is 30 to 50 percent. Below 30 percent in winter dries occupants and wood; above 60 percent in summer encourages mold and dust mites. Dehumidifier sizing comes from the latent load in the Manual J, expressed in pints per day, and the condensate discharges to an indirect waste governed by the plumbing code. In a tight, well-insulated house paired with radiant cooling, the dehumidifier is the primary defense against the dew-point limit described in the radiant-cooling section, and its response is coordinated with the cooling control so the dew point is corrected before condensation forms.

**Code**

```
ASHRAE 55: indoor comfort humidity band; practical residential target 30 to 50 percent RH.
Dehumidifier sized to the Manual J latent load (pints per day).
OPSC: condensate discharge to an indirect waste.
```

## 13.10 Filtration And Air Quality

Filtration removes particulates, and source control keeps them out of the air in the first place. A MERV 13 filter is the best-practice floor, with a dedicated high-efficiency unit for wildfire smoke.

**Applied**

- Filter the ventilation and air-handling systems at MERV 13 minimum, sized so the filter bank does not choke the equipment, and locate the filter for easy access.
- Add a HEPA bypass or a stand-alone HEPA unit per main living zone for wildfire-smoke events.
- Control sources: low-VOC finishes, hard-surface floors, sealed-combustion appliances, a range-hood interlock, entry and mudroom zoning, and an outdoor air intake located away from driveways and dryer vents.

**Professional**

The ORSC does not mandate a filter efficiency, but MERV 13 is the best-practice floor and is referenced by ASHRAE 62.2 addenda; it captures most pollen, smoke fines, and bacteria-sized particles. The filter bank, fan capacity, and design airflow are sized together so MERV 13 does not overload the air handler. A fully installed HEPA filter imposes too high a static-pressure penalty for a typical residential air handler, so a HEPA bypass or a stand-alone unit is the practical answer for serious smoke events. Source control matters as much as filtration; a good system cannot correct stored chemicals, wet materials, or combustion products released indoors.

**Code**

```
Filtration: MERV 13 minimum best practice (ORSC does not mandate a MERV); sized to maintain airflow.
Wildfire smoke: HEPA bypass or stand-alone HEPA per living zone.
Source control: low-VOC finishes, sealed combustion, range-hood interlock, and intake siting away from contaminant sources.
```

## 13.11 Duct Design And Mechanical Room

With radiant systems carrying most of the heating and cooling, the ducts mainly move ventilation air, so they can be smaller, but they are still designed, sealed, kept inside the thermal envelope, and made accessible. The mechanical room provides the clearances, drainage, and sound isolation the equipment needs.

**Applied**

- Design the duct system per Manual D; use rigid metal in primary trunks and limit flex to short branch lengths, fully extended and unkinked.
- Seal duct joints with listed mastic or UL 181B-FX tape, keep ducts inside the thermal envelope, and keep dampers and filters accessible.
- Reserve mechanical-room space for the heat-pump plant, manifolds, pumps, expansion tank, HRV or ERV, dehumidifier, filters, condensate drain, and any water heater or treatment, with the required working clearances.
- Provide a floor drain or condensate sump for condensing equipment and the dehumidifier, vibration isolation on pumps and air handlers, and sound isolation where the room adjoins sleeping areas.
- Label equipment with model, serial, install date, and system volumes, and post a wall diagram and maintenance log.

**Professional**

Ducts inside the thermal envelope are the energy-code default; a duct outside the envelope requires the specified deeply-buried configuration with R-8 duct insulation and the associated floor and vapor-barrier assembly. Duct sealing follows ORSC M1601.4 (listed mastics or UL 181B-FX tape). The mechanical room provides the listing's working clearance (typically 30 inches at the front, 24 inches at the sides), a condensate drain path, and vibration and sound isolation near sleeping areas, and it is laid out so the heat pump, ventilator, water heater, dehumidifier, and controls can each be replaced during the life of the building. The electrical code requires 36 inches of depth and 30 inches of width in front of equipment likely to be serviced energized, which is coordinated against the mechanical clearances so the two do not conflict.

**Code**

```
ORSC M1601 and Manual D: duct design; rigid metal trunks, short flex branches.
ORSC M1601.4: duct sealing with listed mastic or UL 181B-FX tape.
ORSC N1103: ducts inside the thermal envelope as the default; R-8 insulation for ducts outside.
Mechanical-room clearances per equipment listing; condensate drain per OPSC; NEC 110.26 electrical working space coordinated with mechanical clearances.
```

## 13.12 Energy-Code Integration And Controls

The mechanical design is verified against the energy code through the blower-door test, the sealed-combustion and duct-location rules, and a required smart thermostat. Equipment control runs locally so the house keeps heating, cooling, and ventilating without an internet connection; smart-home features add dashboards and alerts on top of that, not as a single point of failure.

**Applied**

- Design the envelope and mechanical systems to the energy-code air-leakage target and document the blower-door result.
- Provide a local-first thermostat and controls whose primary function does not depend on cloud connectivity.
- Monitor the basics: room temperature and humidity, system mode, filter status, pump and fan faults, water leaks, condensate problems, ventilation boost, and dehumidifier runtime.
- Use alerts for real faults, and keep required equipment operation independent of the smart-home layer.

**Professional**

ORSC Chapter 11 sets the energy framework. The prescriptive air-leakage limit is 3.25 ACH50 (N1104.8.2); the high-achievement measure pairs 2.75 ACH50 with a heat-recovery ventilator at 66 percent sensible efficiency. Ducts are inside the thermal envelope by default, sealed combustion with outdoor combustion air is required for any appliance inside the envelope, and a smart thermostat is required (N1105.4.1.2). The blower-door result is documented on the BCD residential blower-door form and submitted before the certificate of occupancy; the ORSC does not require a separate duct-leakage test in the general path, though some Additional Measures include duct-leakage limits. For a house designed to function without an internet connection, a thermostat whose primary control depends on cloud connectivity is rejected in favor of a local-first control, which is a market-availability constraint rather than a code requirement. Control logic for hydronic zoning, ventilation, dehumidification, and radiant cooling matters as much as the hardware, because poor control causes short cycling, humidity drift, or condensation even when the equipment is sized correctly. The voluntary Oregon Residential Reach Code (ENERGY STAR Single-Family New Homes) is an available alternative to Chapter 11 where an ENERGY STAR label is wanted, at the cost of a rater and added verification.

**Code**

```
ORSC N1104.8.2: prescriptive air leakage 3.25 ACH50; high-achievement measure 2.75 ACH50 with a 66 percent sensible HRV.
ORSC N1103: ducts inside the thermal envelope; sealed combustion with outdoor combustion air.
ORSC N1105.4.1.2: smart thermostat required.
Blower-door result on the BCD residential form, submitted before the certificate of occupancy.
2023 Oregon Residential Reach Code (voluntary, HB 3409): ENERGY STAR Single-Family New Homes alternative to Chapter 11.
```

## 13.13 Commissioning And Records

The mechanical systems are commissioned so they meet their design performance, and the records prove the load calculation, the balance, and the equipment startup. The code acceptance trail is a floor; a private commissioning checklist confirms the system performs as designed, and the first year is a tuning period.

**Applied**

Before accepting the system, verify and retain:

- Equipment matches the approved design and is installed to the manufacturer's instructions.
- Ducts are sealed and accessible, hydronic loops are labeled, and manifolds are reachable.
- Pumps run, valves operate, and thermostats control the correct zones.
- Ventilation supply and exhaust are balanced, and the range hood and makeup air operate together.
- The dryer exhaust is clear and condensate drains.
- The Manual J, S, and D documentation, the concealment inspection of the dryer duct and combustion-air paths, and the blower-door result on the BCD form are on file before the certificate of occupancy.
- A private commissioning record covers hydronic pressure-test logs, glycol concentration, flow at each manifold loop, air balance at each register, dehumidifier capacity, dew-point sensor calibration, and radiant control-sequence verification.
- Retest and tune after the first winter and first summer.

**Professional**

The ORSC does not impose a commercial-style commissioning regime, so its acceptance trail is the load documentation, the concealment inspections, the blower-door result, equipment installed to the manufacturer's instructions, the smart thermostat, and the HRV or duct-leakage documentation where an Additional Measure is claimed. The private commissioning checklist is what makes the balanced ventilation, radiant, dehumidification, and control systems meet the performance design, and its results stay in the permanent house file with the equipment manuals and startup records. The building mass, occupant load, ventilation settings, and control logic reveal themselves over the first year, which is why seasonal tuning is planned rather than treated as a defect.

**Code**

```
ORSC acceptance trail: Manual J/S/D with permit; dryer-duct and combustion-air concealment inspection; blower-door result before the certificate of occupancy; equipment per manufacturer instructions; smart-thermostat verification; HRV or duct-leakage documentation where an Additional Measure is claimed.
Records to retain: load calculations, balance report, blower-door form, equipment manuals and startup records, and the private commissioning checklist.
```
