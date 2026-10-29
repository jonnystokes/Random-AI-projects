# Chapter 17: HVAC, Ventilation, Humidity, And Air Quality

This chapter specifies the mechanical systems that heat, cool, ventilate, dehumidify, and filter the house. It contains sections on the heating and cooling plant, the ground-loop options and their water-law consequences, whole-house balanced ventilation, local exhaust and range-hood makeup air, dryer exhaust, combustion appliances, fuel-gas piping and its Oregon pressure test, radiant floors and hydronic zoning, radiant cooling, humidity control, filtration, duct design and the mechanical room, outage behavior, and commissioning. Values are stated for the 2023 Oregon Residential Specialty Code; the provisions most likely to change under the anticipated 2026 edition are flagged where they appear.

## 13.1 Mechanical Code Framing

The residential code controls the mechanical design, and the mechanical specialty code fills only the gaps. Knowing which code owns a detail avoids designing to the wrong requirement.

**Simple**

The house's heating, cooling, and ventilation are governed by the residential code. That code contains its own mechanical and energy chapters. A separate mechanical code exists for larger buildings. It applies only to the few residential items the residential code does not address. Gas piping in a house also falls under the residential code, not the plumbing code. The values in this chapter come from the residential code in force at permit time.

**Professional**

ORSC R101.2 defers to the OMSC only for items the ORSC does not address and for a few narrow cases such as hydrogen-generating spaces. For a single-family house the ORSC mechanical block (Part V) and the energy provisions in Chapter 11 control the equipment, ventilation, duct, and combustion requirements. ORSC Chapter 24 (Part VI) controls fuel-gas piping, appliances, venting, and testing; the fuel-gas piping section of this chapter states the Oregon-amended rules and test criteria. Appendix AA (gas pipe sizing) is not adopted and is preempted from local adoption, so gas pipe sizing uses the Chapter 24 body tables (G2413).

The 2025 OMSC (2024 IMC and IFGC base, effective October 1, 2025, mandatory April 1, 2026) has no published summary of amendments as of July 2026. The amendment record is the board-approved September 2024 code review committee matrix together with the adoption filing (BCD 10-2025, amending OAR 918-440-0010). One matrix item is unresolved in print: the OMSC dwelling-unit outdoor-air coefficient in Section 403.3.2.1 (0.02 versus 0.03 times floor area), which the designer verifies in the printed codebook before sizing any ventilation under OMSC scope. That coefficient does not reach this house: ORSC M1505 governs dwelling ventilation directly.

**Code**

```
Residential mechanical and energy work on this house is designed to the residential code, not the mechanical specialty code.
  2023 ORSC (2021 IRC base, mandatory since April 1, 2024): mechanical in Part V, energy in Chapter 11, fuel gas in Chapter 24; the OMSC applies only to items the ORSC does not address.
  Source: ORSC R101.2 (2023 edition).

The mechanical specialty code edition that fills ORSC gaps is the 2025 OMSC.
  Based on the 2024 IMC and 2024 IFGC; effective October 1, 2025; mandatory April 1, 2026.
  Source: BCD permanent administrative order 10-2025 (OAR 918-440-0010).

The residential code edition is confirmed at permit application.
  A 2026 ORSC (2024 IRC base) is anticipated effective near October 1, 2026; the applicant confirms the governing edition with the building department.
  Source: BCD 2026 ORSC adoption timeline.
```

## 13.2 Heating And Cooling System Selection

The heating and cooling equipment is chosen from a room-by-room load calculation, sized to that load within the allowed oversize, and rated by the recognized standards. For a long-service all-electric house, a cold-climate heat pump is the default, and the concrete thermal mass lets the equipment run steadily rather than in large swings.

**Simple**

The concrete floors and walls store heat, so the indoor temperature changes slowly. The equipment runs at steady state rather than cycling on and off. The machine is sized from a real calculation of the house's heat loss and gain, not a rule of thumb. That keeps it from being either starved or oversized. For an all-electric house, a heat pump both heats and cools from one machine. An air-source unit runs roughly $8,000-$18,000 installed (2026). A ground-source system with drilled boreholes runs $25,000-$45,000.

**Applied**

- Calculate the heating and cooling loads room by room before selecting equipment.
- Select equipment from the manufacturer's performance data, sized to the calculated load within the allowed oversize, not by rule of thumb.
- Design the duct system and the registers to the load and the equipment.
- Choose a cold-climate air-source heat pump for western Oregon as the default; evaluate ground-source where the site and climate favor it, using the loop-option comparison in the ground-loop section.
- Treat the heat-generation plant as a defined interface (power, piping, condensate, clearance, noise, replacement path) so the house is not locked around one product too early. Document the interface at rough-in: hydronic supply and return connections, the dedicated 240-volt circuit (sized in the electrical service chapter), the condensate drain, and the reserved mechanical-room floor area.
- Record the plant decision with its life-cycle cost basis: installed cost, rated efficiency, expected service life, and replacement path.

**Professional**

ACCA Manual J is the referenced residential load-calculation method (ORSC M1401.3), Manual S governs equipment selection from expanded performance data within the oversize caps, Manual D governs the duct design, and Manual T governs register and grille selection. Air-source heat pumps are rated by AHRI 210/240 (SEER2 and HSPF2), and water- and ground-source units by AHRI 13256 and 870; ground-source design follows the CSA/ANSI/IGSHPA C448 series.

Installed-cost ranges for the plant options, from this project's earlier estimating files, restated for 2026:

| Plant option | Installed cost (2026) | Site fit |
|---|---|---|
| Cold-climate air-source heat pump | $8,000-$18,000 | Western Oregon default; mild winter design temperatures |
| Air-to-water heat pump (hydronic output) | $8,000-$18,000 equipment class | Direct hydronic supply to radiant loops; fewer installers |
| Closed-loop horizontal ground-source | $15,000-$30,000 | Rural sites with open trenchable ground |
| Closed-loop vertical ground-source | $25,000-$45,000 | Limited yard area, rocky or clay soil |
| Open-loop ground-source | $10,000-$20,000 | Ample groundwater; water-law conditions in the ground-loop section |

In western Oregon's mild winter design temperatures, a modern cold-climate air-source heat pump (HSPF2 of about 9.0 or higher) typically reaches a favorable life-cycle cost against a ground-source system given the ground-loop installation cost above. Eastern Oregon's colder design temperatures shift the balance toward ground-source. The radiant design targets supply water of about 95-120°F for heating and 55-60°F for cooling, and heat-pump efficiency rises as the heating supply temperature falls, which is the pairing logic between a heat pump and a high-mass radiant floor. A ductless heat pump at HSPF2 9.0 in the primary zone qualifies as Additional Measure 5 under the energy code, and high-efficiency plant options (air-source at HSPF2 8.5/SEER2 15.0 or ground-source at COP 3.5) qualify as Measure 1. Refrigerant charging and repair are regulated work performed by a certified technician, stated in the commissioning section.

**Code**

```
Heating and cooling loads must be calculated, not assumed.
  Room-by-room calculation per ACCA Manual J or approved equivalent; equipment selected within Manual S oversize caps; ducts per Manual D; registers per Manual T.
  Source: ORSC M1401.3 (2023 edition); ACCA Manuals S, D, and T.

Heat pump performance is rated by the recognized laboratory standards.
  Air-source: SEER2 and HSPF2 per AHRI 210/240. Water- and ground-source: AHRI 13256 and AHRI 870.
  Source: AHRI 210/240; AHRI 13256; AHRI 870.

Ground-source systems are designed and installed to the current ANSI standard.
  CSA/ANSI/IGSHPA C448 series, 2025 edition.
  Source: CSA/ANSI/IGSHPA C448:25.

High-efficiency equipment qualifies for the energy code's Additional Measures.
  Measure 1: gas furnace AFUE 94%, air-source heat pump HSPF 10.0/SEER 16.0 (HSPF2 8.5/SEER2 15.0), or ground-source COP 3.5. Measure 5: ductless heat pump at HSPF 10.0 (HSPF2 9.0) in the primary zone.
  Source: ORSC Table N1101.1(2), Measures 1 and 5 (2023 edition).
```

## 13.3 Ground Loops And The Open-Loop Water-Rights Path

A closed loop exchanges only heat with the ground; an open loop pumps groundwater itself, which puts the system under Oregon water law. The two paths differ in cost, in drilling, and in the agencies involved.

**Simple**

A closed-loop system buries sealed plastic pipe and circulates the same fluid forever. No water is taken from the ground. An open-loop system pumps real well water through the heat pump and then puts it back or discharges it. Taking groundwater is regulated by the state, even for heating. A closed loop needs no water right. An open loop can run without one only under a daily-volume exemption. The paperwork still gets filed, and the return well needs approval in advance.

**Applied**

- Use a closed-loop configuration as the default: horizontal trenches (4 to 8 feet deep) where open ground allows, vertical boreholes (200 to 400 feet deep, one per ton of capacity, typically 3 to 6 for a 3,000-square-foot house) where it does not.
- Before choosing open-loop, calculate the daily withdrawal: 5,000 gallons per day equals about 3.5 gallons per minute of continuous flow, so a continuous 4 gpm system already exceeds the exemption ceiling.
- For any open-loop system: file the well log, well-location map, and $300 exempt-use recording fee; obtain OWRD approval of the injection well (installation, well design, and receiving formation) before drilling; and design the discharge as reinjection to the source aquifer.
- Check whether the parcel sits in a critical groundwater area or other designated special-area standard before committing to any new well use.
- Verify glycol freeze protection in closed loops routed through unconditioned ground: propylene glycol concentration set at least 10°F below the design loop temperature, per IGSHPA practice.

**Professional**

**Jurisdiction.** Groundwater pumped for its thermal characteristics from a well with a bottom-hole temperature below 250°F is "geothermal fluid" under the groundwater code, administered by the Water Resources Department as low-temperature geothermal (ORS 537.515(4)); every residential open-loop system is far below that line.

**Water right or exempt use.** Pumping groundwater through a heat pump is an appropriation, so it requires a groundwater right unless it fits an ORS 537.545 exemption. The single industrial or commercial use exemption reaches 5,000 gallons per day, and OAR 690-230-0130(1) applies it expressly to low-temperature geothermal appropriation. The domestic exemption reaches 15,000 gallons per day, but OWRD's public guidance frames heat-exchange water as the industrial/commercial use. The defensible position: clearly exempt at or under 5,000 gpd; exempt between 5,000 and 15,000 gpd only if OWRD accepts a domestic classification for the site; permit-required above that. The down-hole heat-exchange exemption (ORS 537.545(1)(e)) covers fluid circulated inside a well without withdrawal; it is a closed-loop-in-well configuration, not the open-loop path. An exempt use still gets recorded: well log, location map, and the $300 recording fee (ORS 537.545(6)-(7)).

**Well construction.** Both the production well and any injection well are constructed to the water supply well standards (OAR 690-200 and 690-210, abandonment under 690-220) plus the low-temperature geothermal division (OAR 690-230: construction, start cards, well-head protection, pump testing of injection wells, temperature measurement).

**Reinjection versus surface discharge.** The disposal design is the regulatory fork. A standard disposal system adds nothing but heat and returns the effluent to the producing reservoir or another suitable reservoir, or puts it to a secondary beneficial use. A nonstandard system (storm sewer, drainage hole, direct discharge to land or surface water) makes the appropriation inferior to all subsequent consumptive rights and to standard-disposal appropriators. Upgrading to standard disposal restores the original priority date (OAR 690-230-0020, 690-230-0140).

**Injection-well approval.** No water supply well may be used for injection without prior OWRD approval of the installation, well design, and receiving formation (OAR 690-210-0070). ORS 537.783(3) requires a DEQ water pollution control facilities permit before reinjection begins, waivable by DEQ-commission agreement when the fluid returns uncontaminated to the reservoir it came from.

**The closed-loop contrast.** A closed-loop boring appropriates no groundwater, needs no water right, and is regulated only as a boring under OAR 690-240. That asymmetry is why open-loop is this project's conditional path, priced in the plant table but chosen only if the final site's groundwater, OWRD approvals, and county conditions all resolve in its favor.

**Code**

```
Groundwater pumped for heating or cooling is regulated as low-temperature geothermal fluid under state water law.
  Bottom-hole temperature below 250°F and depth under 2,000 feet: OWRD groundwater jurisdiction; at or above 250°F the well leaves the Water Rights Act (ORS chapter 522).
  Source: ORS 537.515(4); ORS 537.090; OWRD low-temperature geothermal program.

An open-loop system can run without a water right only under an exempt-use ceiling.
  Single industrial or commercial purpose up to 5,000 gallons per day exempt; domestic purposes up to 15,000 gpd exempt only where OWRD accepts that classification; well log, location map, and $300 recording fee required for exempt uses.
  Source: ORS 537.545(1)(d), (1)(f), (6)-(7); OAR 690-230-0130.

Production and injection wells are constructed to the water supply well standards plus the low-temperature geothermal rules.
  Construction per OAR 690-200 and 690-210; abandonment per OAR 690-220; low-temperature geothermal standards, start cards, and injection-well pump testing per OAR 690-230.
  Source: OAR 690-200; OAR 690-210; OAR 690-220; OAR 690-230.

An injection (return) well requires approval before use.
  Prior OWRD approval of installation, well design, and receiving formation; DEQ water pollution control facilities permit before reinjection, waivable when fluid returns uncontaminated to its source aquifer.
  Source: OAR 690-210-0070; ORS 537.783(3) (ORS 468B.050).

Surface discharge demotes the water right.
  Nonstandard disposal makes the appropriation inferior to subsequent consumptive rights and to standard-disposal appropriators; upgrading to standard disposal restores the original priority date.
  Source: OAR 690-230-0020; OAR 690-230-0140.

A closed-loop boring needs no water right.
  Regulated only as a boring: construction, maintenance, conversion, and abandonment rules.
  Source: OAR 690-240-0040 through 690-240-0049.
```

## 13.4 Whole-House Balanced Ventilation

Oregon requires balanced whole-house mechanical ventilation in every new dwelling. Exhaust-only ventilation is not acceptable. The continuous airflow is set by the residential code table or its formula, and the system supplies and exhausts within a close balance.

**Simple**

A tight house does not leak enough air to refresh itself. Mechanical ventilation brings in fresh air and removes stale air on purpose. Oregon requires a balanced system: fresh air supplied and stale air exhausted in roughly equal amounts. A fan that only pulls air out does not qualify. A heat-recovery ventilator does this while recovering most of the heat from the air it exhausts. The flow for this house is about 68 cubic feet per minute, running all the time. That is roughly the flow of one bathroom fan.

**Applied**

- Provide a balanced ventilation system: paired supply and exhaust fans, a heat- or energy-recovery ventilator, or a central-fan-integrated supply interlocked with exhaust.
- Set the continuous airflow from the code table, or the formula CFM (cubic feet per minute) = (0.01 × floor area in square feet) + 7.5 × (bedrooms + 1). For 3,000 square feet and four bedrooms: 30 + 37.5, about 68 CFM continuous; the code table bins run in 15-CFM steps from 30 to 165.
- For intermittent operation, multiply: twice the rate at 50 percent runtime, four times at 25 percent.
- Balance supply to exhaust within 10 percent.
- Provide user-accessible manual override controls.
- Keep a continuously operating fan at 1.0 sone (a loudness rating for fans; lower is quieter) or quieter so it is not switched off for noise.
- Supply fresh air to bedrooms, the living area, and the office; exhaust from bathrooms, the kitchen, and the laundry; provide transfer grilles or door undercuts so air can move between them.
- Locate the outdoor intake away from exhaust terminations, the driveway, dryer vents, and dust.

**Professional**

ORSC M1505 sets the whole-house ventilation requirement and, per the BCD technical bulletin, disallows single-point exhaust-only systems that the base IRC would permit. The continuous rate comes from Table M1505.4.3(1) or the equivalent formula; intermittent operation is allowed under Table M1505.4.3(2) with runtime multipliers, and extrapolation beyond the table is not permitted. ASHRAE 62.2-2022 is the best-practice design standard and does not conflict with the ORSC for a system designed to it, except that the ORSC does not grant the 62.2 blower-door infiltration credit.

The recovery-ventilator choice is between sensible-only heat recovery (HRV) and combined heat-and-moisture recovery (ERV). An HRV transfers temperature only: simpler core, lower cost, and it exhausts indoor moisture, which suits a cool climate in winter. An ERV also transfers moisture between the streams, rejecting 60 to 70 percent of incoming outdoor humidity in summer and retaining indoor humidity in winter. For this design the ERV is the selection wherever radiant cooling is built, because summer outdoor humidity raises the indoor dew point and the dew point is the radiant-cooling limit stated in that section. Without radiant cooling, an HRV meets the same code requirement at lower cost. Design targets above the code floor: 85 percent or better sensible recovery and 60 percent or better latent recovery, against the energy code's high-achievement measure of 66 percent sensible at 1.6 CFM per watt. Established residential units include the Zehnder ComfoAir, Panasonic Intelli-Balance, RenewAire, and Broan AI series. Ventilation ducts run rigid metal in trunks with short flex connections only at register boots, at trunk velocities of 600 feet per minute or less for quiet operation; sizing is stated in the duct-design section.

**Code**

```
Every new dwelling must have balanced whole-house mechanical ventilation.
  Single-point exhaust-only systems are not acceptable in Oregon; the base IRC configuration is amended out. Compliant configurations: paired supply and exhaust, HRV/ERV, or central-fan-integrated supply with interlocked exhaust.
  Source: ORSC M1505 (2023 edition); BCD technical bulletin, whole-house mechanical ventilation (June 2021).

The continuous ventilation rate comes from the code table or its formula.
  CFM = (0.01 × floor area in sq ft) + 7.5 × (bedrooms + 1); table values bin in 15-CFM steps from 30 to 165 CFM.
  Source: ORSC Table M1505.4.3(1) (2023 edition).

Intermittent ventilation uses runtime multipliers, without extrapolation.
  4 times the continuous rate at 25 percent runtime; 2 times at 50 percent; extrapolation beyond the table is not permitted.
  Source: ORSC Table M1505.4.3(2) (2023 edition).

The system must be balanced, controllable, and quiet enough to leave running.
  Supply within 10 percent of exhaust; user-accessible manual override; 1.0 sone maximum for continuously operating fans.
  Source: ORSC M1505 (2023 edition); BCD technical bulletin, whole-house mechanical ventilation (June 2021).

ASHRAE 62.2 is the best-practice design standard, without its infiltration credit.
  A system designed to ASHRAE 62.2-2022 satisfies ORSC M1505; the 62.2 Section 4.1.3 blower-door infiltration credit is not granted in Oregon.
  Source: ASHRAE 62.2-2022; ORSC M1505 (2023 edition).
```

## 13.5 Local Exhaust And Range-Hood Makeup Air

Kitchens and bathrooms need local exhaust to the outdoors, and a large kitchen exhaust needs makeup air so it does not depressurize the house or backdraft a combustion appliance.

**Simple**

Cooking and showering make grease, steam, odors, and moisture that a local fan sends outside. In a tight house, a kitchen hood at full power removes air faster than the envelope can replace it. The house then needs a matching intake, or the negative pressure pulls air backward down other vents.

**Applied**

- Exhaust each bathroom at a minimum of 50 CFM intermittent or 20 CFM continuous, and the kitchen at 100 CFM intermittent, to the outdoors.
- Size the hood to the cooktop: full cooktop width, with about 6 inches of overhang each side for a professional-style range. Select for capture efficiency, with variable speed and stainless baffle filters that clean in the dishwasher.
- Run the hood duct in rigid smooth-wall metal (6 to 10 inch round by hood airflow), short and straight, sloped slightly to the exterior.
- Terminate kitchen and bath exhaust outdoors with a backdraft damper and no screen, at least 3 feet from openings; do not terminate into an attic, soffit, ridge vent, or crawl space.
- Provide makeup air where any kitchen exhaust exceeds 400 CFM: approximately equal to the exhaust rate, with a damper meeting the code, discharging into the same room, interlocked to open when the hood runs.
- Plan the hood, duct route, and makeup air before the cabinet layout is fixed.

**Professional**

ORSC M1505.5 and Table M1505.5 set the minimum local-exhaust capacities, and all kitchen and bath exhaust terminates outdoors (recirculation and attic, soffit, ridge, and crawl terminations are barred). The makeup-air rule triggers when kitchen exhaust exceeds 400 CFM; below that threshold no makeup air is required. At or above it, makeup air approximately equals the exhaust, includes at least one damper meeting M1503.6.2, and discharges into the same room. The code does not require the makeup air to be tempered; tempering is a comfort decision. An untempered interlocked intake sized slightly below the hood rating (for example, 550 CFM of makeup air against a 600 CFM hood) holds the house neutral to slightly negative during cooking. Established hood makers include Broan, Vent-A-Hood, Zephyr, and Faber. Capture efficiency, not appearance, drives the hood selection. A smaller hood (200-300 CFM) exhausted through the ventilation system in boost mode avoids the makeup-air threshold entirely, at lower capture efficiency for heavy cooking; this project specifies a full hood because the household cooks, and the capture difference is the stated basis.

**Code**

```
Bathrooms and kitchens must have local exhaust to the outdoors.
  Bathroom: 50 CFM intermittent or 20 CFM continuous. Kitchen: 100 CFM intermittent. Recirculation does not satisfy the requirement.
  Source: ORSC M1505.5 and Table M1505.5 (2023 edition).

Exhaust must terminate outdoors, away from openings, without screens.
  Backdraft damper required; no screen at the termination; at least 3 feet from operable openings; no termination into an attic, soffit, ridge vent, or crawl space.
  Source: ORSC M1503 and M1505 (2023 edition).

Large kitchen exhaust requires makeup air.
  Trigger: kitchen exhaust exceeding 400 CFM. Makeup air approximately equal to the exhaust rate, at least one damper per M1503.6.2, discharged into the same room. Tempering is not required.
  Source: ORSC M1503 (2023 edition).
```

## 13.6 Dryer Exhaust

The clothes-dryer exhaust is a smooth metal duct within a length limit, terminated outdoors. A condensing heat-pump dryer avoids the duct entirely and suits the airtight envelope.

**Simple**

A dryer blows hot, wet, lint-filled air, and lint burns. A long, rough, or crushed duct collects lint, overheats the dryer, and can start a fire. The answer is a short, smooth metal duct, cleaned regularly. A heat-pump dryer condenses the moisture to a drain instead. It needs no duct and no hole through the wall.

**Applied**

- Use a smooth-interior metal duct, 4-inch nominal, 28-gauge minimum, with no screws or fasteners protruding into the duct interior (lint catches on the points).
- Keep the equivalent duct length within 35 feet, deducting for elbows (about 5 feet per 90-degree and 2.5 feet per 45-degree elbow); design to 25 feet because the 2024 IRC baseline is 25 feet and the 2026 ORSC may adopt it.
- Use a listed transition duct no longer than 8 feet, not concealed.
- Terminate outdoors with a backdraft damper and no screen, at least 3 feet from openings, sloped slightly to the exterior.
- Label the equivalent length within 6 feet of the dryer connection where it exceeds 35 feet.
- Clean the full duct at least annually; route it through the service layer with no concealed elbows.
- Consider a condensing heat-pump dryer, which needs a condensate drain instead of a duct and removes one envelope penetration.

**Professional**

ORSC M1502 sets the dryer-exhaust rules. The equivalent length from the dryer to the terminal is limited to 35 feet excluding the transition duct, with elbow deductions per Table M1502.4.6.1. The transition duct is a single length no longer than 8 feet, listed and labeled to UL 2158A, and not concealed. Oregon's M1502.4.5 amendment prohibits domestic booster fans while permitting UL 705 dryer-exhaust duct power ventilators, which are commonly confused. A conventional dryer exhausts roughly 150-225 CFM while running; in this envelope that imbalance is brief and the balanced ventilation system absorbs it, so no dedicated makeup air is designed for the dryer. A listed condensing heat-pump dryer is exempt from the duct requirement, removes a wall penetration and its exhaust imbalance, and drains condensate to an indirect waste per the appliance listing and the plumbing code. The parallel OMSC dryer provisions carry the long-standing Oregon amendment keeping fastener points out of duct interiors (OMSC 504.9.2, retained in the 2025 matrix); the same practice is specified here as workmanship.

**Code**

```
Dryer exhaust runs in smooth metal duct within an equivalent-length limit.
  Smooth-interior metal duct, 4-inch nominal, 28-gauge (0.0157 inch) minimum; 35-foot maximum equivalent length excluding the transition duct, with elbow deductions per the table (about 5 feet per 90-degree elbow, 2.5 feet per 45-degree).
  Source: ORSC M1502 and Table M1502.4.6.1 (2023 edition).

Domestic booster fans are prohibited in Oregon; listed duct power ventilators are not.
  Booster fans: prohibited. Dryer-exhaust duct power ventilators listed to UL 705: permitted.
  Source: ORSC M1502.4.5 (2023 edition, Oregon amendment).

The transition duct is short, listed, and visible.
  Single length, 8 feet maximum, listed and labeled to UL 2158A, not concealed within construction.
  Source: ORSC M1502 (2023 edition); UL 2158A.

The termination goes outdoors with a damper and no screen.
  Backdraft damper; no screen; at least 3 feet from openings. Where equivalent length exceeds 35 feet, a permanent label states it within 6 feet of the dryer connection.
  Source: ORSC M1502 (2023 edition).

A listed condensing (heat-pump) dryer is exempt from the duct requirement.
  Condensate drains to an indirect waste per the appliance listing and the plumbing code.
  Source: ORSC M1502 (2023 edition); OPSC Chapter 8 (indirect wastes, 2023 edition).
```

## 13.7 Combustion Appliances: Solid Fuel And LP Gas

A solid-fuel stove has to be certified, an uncertified stove triggers a removal obligation at sale, and LP-gas work requires a licensed installer with no owner-builder exemption. Any combustion appliance inside the thermal envelope is sealed-combustion with outdoor combustion air. The simplest tight-house strategy is all-electric, with combustion added only by deliberate choice.

**Simple**

Burning fuel indoors uses up air and makes exhaust gases, including carbon monoxide. A tight house does not leak enough air to feed a fire safely on its own. So any stove or fireplace here gets its own outdoor air duct and a sealed vent. The cleanest answer is an all-electric house with no flame in it. This project treats a wood stove as an option for heat during power outages, not as a main heater.

**Applied**

- Specify only a current EPA- or DEQ-certified wood or pellet stove; a mechanical permit will not issue for an uncertified used stove.
- Check the exemption categories before assuming certification applies: pre-1940 antique stoves with high market value, cookstoves, and central wood-fired furnaces are exempt classes.
- Plan for the removal-and-destruction obligation that attaches to an uncertified device at sale of the residence; the seller holds it unless the buyer accepts it in writing, with a 30-day post-closing cure window.
- Provision the stove even if it is deferred: a listed chimney penetration location and a hearth area, recorded on the drawings, cost far less at design time than a retrofit through a concrete roof.
- Hire a licensed Oregon LPG installer for all LP-gas piping, container setting, and appliance connection; the owner-builder exemption does not cover LP work.
- Use sealed or direct-vent equipment, duct combustion air directly from outdoors for any combustion appliance inside the thermal envelope, and provide the manufacturer's clearances.
- Provide carbon monoxide alarms wherever a fuel-burning appliance, fireplace, or attached garage is present.

**Professional**

Solid-fuel devices are regulated by DEQ under OAR Chapter 340, Division 262 (authority ORS 468A.460 to 468A.515), separate from the building code. A new device must be EPA- or DEQ-certified at installation, an uncertified used stove cannot be sold or reinstalled in Oregon, and at sale of a residence an uncertified device is removed and destroyed unless the buyer accepts the obligation in writing. Pellet stoves are solid-fuel devices under the same certification rules, with more lenient treatment in the wood-burning curtailment program outside PM nonattainment areas. During air-stagnation advisories local curtailment can bar burning; residences where the stove is the sole heat source, and low-income households, are exempt from curtailment, which is one reason the outage-heat role stated in the outage section does not conflict with the rule. Combustion-air and hearth requirements are in ORSC Chapter 17 and chimney and vent requirements in Chapter 18. LP-gas work is governed by ORS 480.430 to 480.460 and OAR 837-030 under the State Fire Marshal, with no homeowner exemption; the fuel-gas piping section states the piping and test rules that apply once gas exists. The energy code (ORSC N1103) requires sealed combustion with combustion air ducted from outdoors for any appliance inside the thermal envelope, which is an energy requirement layered on the safety rules. The all-electric default avoids gas service, combustion-air conflicts, flue penetrations, and indoor combustion byproducts. Carbon monoxide alarm placement and wiring are detailed with the smoke and carbon monoxide alarm requirements in the branch-circuit chapter.

**Code**

```
A new solid-fuel stove must be emissions-certified before it can be installed.
  EPA- or DEQ-certified at installation; no sale or reinstallation of an uncertified used stove; no mechanical permit for one. Exempt classes: antique stoves (pre-1940, high market value), cookstoves, central wood-fired furnaces.
  Source: OAR 340-262-0450, 340-262-0500, 340-262-0600 (ORS 468A.460-468A.515).

An uncertified device must be removed and destroyed when the residence sells.
  Seller's obligation unless the buyer accepts it in writing; 30-day post-closing cure period.
  Source: OAR 340-262-0700.

Burning can be curtailed during air-stagnation advisories.
  Local curtailment programs; exemptions for sole-source-heat residences and low-income households; pellet stoves treated more leniently outside PM nonattainment areas.
  Source: OAR 340-262-0800.

Combustion air and venting follow the residential code's dedicated chapters.
  Combustion air: ORSC Chapter 17. Chimneys and vents: ORSC Chapter 18. Hearth and clearance per the listing and Chapters 17-18.
  Source: ORSC Chapters 17 and 18 (2023 edition).

LP-gas work requires a licensed installer; there is no homeowner exemption.
  Piping, container setting, and appliance connection by an Oregon-licensed LPG installer under State Fire Marshal rules.
  Source: ORS 480.430-480.460; OAR 837-030.

Appliances inside the thermal envelope must be sealed-combustion with outdoor air.
  Combustion air ducted directly from outdoors; sealed or direct-vent equipment.
  Source: ORSC N1103 (2023 edition).

Carbon monoxide alarms are required where a combustion source exists.
  Fuel-burning appliance, fireplace, or attached garage triggers the requirement; placement and wiring are specified in the branch-circuit chapter.
  Source: ORSC R315 (2023 edition); ORS 105.836.
```

## 13.8 Fuel-Gas Piping And The Oregon Pressure Test

Gas piping in a dwelling is governed by the residential code's fuel-gas chapter, not the plumbing code, and Oregon replaced the national test criteria with its own. The rules below apply to any natural-gas or LP piping this house ever gets; an all-electric build never triggers them.

**Simple**

If the house ever gets gas, propane is the usual rural case. The new piping is filled with pressurized air and watched before any gas flows. Oregon's test is stricter than the national model: 10 pounds per square inch, held 15 minutes, with no visible drop on the gauge. The gas supplier is not allowed to turn on gas until the rough piping inspection has passed.

**Applied**

- Obtain the gas piping permit under the residential code (it rides the mechanical/gas permit, not the plumbing permit), and schedule the rough piping inspection before any piping is covered, concealed, or connected to an appliance.
- Test with air, nitrogen, carbon dioxide, or inert gas; never oxygen.
- For a standard-pressure system (under 14 inches water column): pressurize to at least 10 psi and hold at least 15 minutes with no perceptible drop. For welded piping or systems above 14 inches water column: at least 60 psi for 30 minutes.
- Use a manometer or a calibrated pressure-measuring device; a mechanical gauge must be a 15-psi or 30-psi gauge for standard systems (100-psi gauge for higher-pressure systems), and the pressure source is isolated before the test reading.
- Leave every joint, including welds, exposed during the test.
- Disconnect appliances rated below the test pressure and cap their outlets; appliances rated at or above it may be isolated at their shutoff valves.
- Retest any piping affected by later work; minor repairs and additions may instead be leak-checked with noncorrosive leak-detecting fluid or another approved method.
- Bury exterior gas piping at least 18 inches deep.
- Install a sediment trap only where the appliance manufacturer's instructions require one.
- For LP systems, the licensed installer may test, inspect, and purge under NFPA 58 instead.

**Professional**

ORSC Chapter 24 (Part VI) governs fuel-gas piping systems, appliances, venting, and combustion air for dwellings, from the point of delivery to the outlet of the appliance shutoff valves (G2401.1). The OPSC contains no fuel gas: OAR 918-750-0110(3) strikes the model plumbing code's fuel-gas chapter, and the statutory definition of plumbing (ORS 447.010(6)) omits fuel gas entirely, so the permit is a gas/mechanical permit under ORSC R105.1. Appendix AA is not adopted and is preempted from local adoption; sizing uses the G2413 body tables.

Oregon deleted the model testing and purging sections (G2417.4.2 through G2417.7.3.1) and replaced the model test pressure rule (1.5 times working pressure, 3 psig minimum, 10 minutes) with its own G2417.4.1. Systems under 14 inches water column test at not less than 10 psi for not less than 15 minutes with no perceptible drop. Welded piping and systems above 14 inches water column test at not less than 60 psi for 30 minutes. NFPA 58 governs LP testing, inspection, and purging as an exception. A standard residential system runs 7 to 11 inches water column supply pressure, below the 14-inch threshold, so the 10 psi/15 minute criterion is the working rule. The gauge rule (G2417.4) replaces the model's five-times-test-pressure scale rule with fixed sizes: manometer or calibrated device; mechanical gauges at 15 or 30 psi for standard systems and 100 psi above the threshold. Oregon also added rough and final piping inspections (G2417.1.1.1 and G2417.1.1.2) and bars the serving gas supplier from turning on gas or meters before the rough piping inspection is approved (G2401.2.1). Other Oregon amendments in the chapter: minimum burial depth modified to 18 inches (G2415.12), sediment traps only where the manufacturer's instructions require them (G2419.4), and the bonding section deleted in favor of the electrical code (G2411.1), where the CSST bonding rules of the grounding chapter take over. The 2026 ORSC review committee recommends retaining every Chapter 24 Oregon amendment, including the test criteria, so the values are expected to carry forward; the edition is confirmed at permit time.

**Code**

```
Residential fuel-gas piping is governed by the residential code, not the plumbing code.
  ORSC Chapter 24 covers piping from the point of delivery to the appliance shutoff outlets, including design, materials, installation, testing, and inspection; the OPSC's model fuel-gas chapter is not adopted.
  Source: ORSC G2401.1 (2023 edition); OAR 918-750-0110(3); ORS 447.010(6).

Gas piping work requires a permit under the residential code.
  Erecting, installing, altering, repairing, removing, converting, or replacing a gas system requires the ORSC permit (the gas/mechanical permit).
  Source: ORSC R105.1 (2023 edition).

Oregon's pressure test replaces the national model criteria.
  Systems under 14 inches water column: at least 10 psi held at least 15 minutes, no perceptible drop. Welded piping or systems above 14 inches water column: at least 60 psi for 30 minutes. Exception: NFPA 58 procedures for LP systems.
  Source: ORSC G2417.4.1 (2023 edition, Oregon amendment).

The test gauge is specified, and the pressure source is isolated.
  Manometer or calibrated pressure-measuring device; mechanical gauges: 15-psi or 30-psi gauge for systems at or under 14 inches water column, 100-psi gauge above it.
  Source: ORSC G2417.4 (2023 edition, Oregon amendment).

The test medium is inert; joints stay exposed; low-rated appliances come off.
  Air, nitrogen, carbon dioxide, or inert gas; oxygen prohibited. Joints and welds exposed during the test. Appliances rated below test pressure disconnected and outlets capped; appliances rated at or above it may be isolated at their shutoff valves.
  Source: ORSC G2417.2, G2417.3, G2417.3.3, G2417.3.4 (2023 edition).

Rough and final gas piping inspections are required, and gas stays off until rough approval.
  Rough inspection before piping is covered, concealed, or connected; final inspection after concealment and attachment of appliances or shutoff valves; the gas supplier may not turn on gas or meters before rough-inspection approval.
  Source: ORSC G2417.1.1.1, G2417.1.1.2, G2401.2.1 (2023 edition, Oregon amendments).

Later work triggers a retest of the affected piping.
  Piping worked on after the test is retested; minor repairs and additions may be inspected and leak-checked with noncorrosive leak-detecting fluid or other approved methods.
  Source: ORSC G2417.1.2 (2023 edition).

Exterior gas piping is buried at least 18 inches deep.
  Minimum burial depth 18 inches (Oregon amendment to the model depth).
  Source: ORSC G2415.12 (2023 edition, Oregon amendment).

Gas pipe sizing uses the chapter's body tables; the sizing appendix is not adopted.
  Appendix AA is not adopted and is preempted from local adoption; sizing per the G2413 tables.
  Source: ORSC R101.2.3.2 and G2413 (2023 edition).
```

## 13.9 Radiant Floor Heating And Hydronic Zoning

A hydronic radiant floor heats the slab and radiates to the room, pairing naturally with a heat pump and a concrete structure. The tubing, insulation, loop design, and manifold access set its performance and its serviceability.

**Simple**

Radiant heating warms the floor, and the warm floor warms the room. The house feels comfortable with no fan blowing hot air. Warm-water tubing is cast into or fastened under the slab. A manifold (a header with a valve for each loop) feeds the tubing. Per-room zones let different rooms hold different temperatures at the same time. The manifolds, pumps, and valves stay reachable, because they are the parts that get serviced. The tubing itself, once cast in, is expected to outlast the equipment feeding it.

**Applied**

- Use oxygen-barrier PEX or PEX-AL-PEX in any closed loop that contains ferrous components.
- Build the floor in this sequence where a topping slab is used: structural slab, insulation layer, tubing fastened at the design spacing, then a 1.5-to-2-inch fiber-reinforced topping slab encapsulating the tubing.
- Fasten tubing to mesh or clips at the design spacing and depth: 6 inches on center in high-output areas (bathrooms, entries, room perimeters at exterior walls), 9 to 12 inches in standard living areas. Photograph the layout before the pour.
- Provide continuous below-slab insulation (R-10 minimum, R-15 to R-20 best practice) and matching perimeter insulation at slab edges.
- Cap loop length per the manufacturer (typically 250 to 300 feet per half-inch loop) and give each loop isolation, balancing, flow-meter, and air-vent provisions at an accessible manifold, with isolation valves at each manifold takeoff so one manifold can be serviced without draining the system.
- Pressure-test the tubing before the pour (typically 1.5 times working pressure or 100 psi, held at least 24 hours) and again after the pour.
- Balance loops to the design flow, on the order of 0.6 gpm per 100 square feet of heated floor at a 10°F loop temperature drop, and record the setting for each loop.
- Keep the finish-floor R-value within the manufacturer's limit (about 2.0 to 2.5); wall-to-wall carpet over radiant defeats the output and is excluded here.
- Design a failed zone valve or actuator to be reachable without demolition.

**Professional**

Radiant tubing follows ASTM F876/F877 (PEX) or F1281 (PEX-AL-PEX), with an EVOH oxygen barrier to DIN 4726 and chlorine resistance to ASTM F2023; established lines include Uponor AquaPEX, Rehau RAUPEX, and Viega. An oxygen barrier is mandatory where any wetted part is ferrous (steel boiler, cast-iron circulator, steel manifold), because dissolved oxygen corrodes those parts; non-barrier tubing is acceptable only when every wetted ferrous part is replaced with brass, bronze, or stainless. Design temperatures: supply water 95-120°F with about a 10°F drop across each loop, and floor surface temperatures of 75-85°F at design output; above the mid-80s occupants report the floor as uncomfortably warm. Lower supply temperatures raise heat-pump efficiency, so the design pushes supply temperature down by adding tube density rather than up. Below-slab insulation drives response time, and each additional R-1 of finish floor cuts output by roughly 10 percent. The ORSC does not set a hydronic pressure-test value; that comes from the manufacturer's instructions, and the commissioning section records the logs.

Per-room zoning is a hardware chain: a thermostat per room, a motorized zone valve per loop group at the manifold, a manifold controller (Uponor, Rehau, and Viega each supply their own) coordinating the valves, and a primary circulator that runs when any zone calls. A 3,000-square-foot house zones out at roughly 11 to 17 zones across two floors and a basement. The thermostat backbone is wired 24-volt control cable pulled at rough-in: wired thermostats have service lives of 20 or more years against 5 to 10 for network-dependent devices. A smart interface layers on top of the wired backbone without becoming a failure point, consistent with the controls section. Zones merge in software (two thermostats driving one loop group); splitting a zone later requires a spare loop and manifold port, so loops are laid out room-by-room even where rooms are initially controlled together. Hydronic water treatment (corrosion and scale inhibitor, biocide, pH buffering) protects the loop, and propylene glycol is used where tubing runs through unconditioned space.

**Code**

```
Radiant tubing conforms to the recognized material standards.
  PEX: ASTM F876/F877. PEX-AL-PEX: ASTM F1281. Chlorine resistance: ASTM F2023. Oxygen barrier: DIN 4726.
  Source: ASTM F876/F877; ASTM F1281; ASTM F2023; DIN 4726.

Closed loops with ferrous components require oxygen-barrier tubing.
  EVOH-barrier PEX or PEX-AL-PEX, or every wetted ferrous component replaced with brass, bronze, or stainless.
  Source: DIN 4726; tubing manufacturer installation requirements (Uponor, Rehau, Viega).

Tubing is pressure-tested before and after the pour.
  Typically 1.5 times working pressure or 100 psi, held at least 24 hours; the ORSC specifies no hydronic test value.
  Source: manufacturer installation instructions; ORSC (no hydronic test value specified, 2023 edition).

Floor surfaces and comfort conditions follow the comfort standard.
  Thermal comfort conditions, including surface-temperature and humidity limits, per ASHRAE 55.
  Source: ASHRAE 55-2023; ASHRAE Handbook, HVAC Systems and Equipment, Chapter 6.
```

## 13.10 Radiant Cooling Feasibility

Radiant cooling is a fan-free, duct-free way to remove sensible heat, and western Oregon's moderate summer humidity makes it feasible with a paired dehumidification strategy. The controlling constraint is the dew point: a cooled surface below the interior dew point condenses water, which causes mold, slippery floors, and finish damage.

**Simple**

The same floor loops that heat in winter can run cool water in summer. The limit is the dew point (the temperature at which moisture in the air condenses on a surface). A floor colder than the room's dew point collects water, and a wet floor means mold and slipping. So the system monitors humidity constantly and keeps the floor warmer than the dew point. A dehumidifier keeps the dew point low enough for the cool floor to do useful work.

**Applied**

Before committing to radiant cooling, provide:

- Dew-point sensing at representative locations and supply water held above the dew point.
- A dedicated dehumidification system to hold the interior dew point down.
- Window contacts that interrupt cooling when a window opens.
- A floor-surface moisture sensor as a backstop.
- A small backup cooling system for design days when the latent load exceeds the dehumidifier.
- A pre-summer test of the full control sequence.

**Professional**

The radiant surface cannot fall below the interior dew point without condensation, mold, and slippery floors. ASHRAE 55 caps a cooled floor at about 64°F, and coastal western Oregon summer interior dew points run about 55 to 60°F at design conditions, leaving roughly 4 to 9°F of headroom, which is workable but tight. The design supplies water typically 1 to 2°F above the measured or predicted dew point and uses the dew-point sensors, window interlocks, dehumidification, and floor-moisture backstop above, with backup cooling behind them.

The capacity arithmetic sets the system's role. A cooled floor removes about 10 to 15 BTU per hour per square foot of active surface, so 2,000 square feet of active floor supplies roughly 20,000 to 30,000 BTU per hour, about 2 tons. Peak sensible cooling load for a well-built 3,000-square-foot western Oregon house runs about 24,000 to 36,000 BTU per hour, so the floor supplies roughly 60 to 90 percent of the peak. The remainder comes from dehumidified ventilation air, from the thermal mass absorbing and delaying the afternoon peak, and from small fan coils on the same chilled-water loop in the highest-gain rooms (the kitchen, the primary bedroom for sleep, and rooms with large south glazing). Heating-to-cooling changeover is a seasonal, system-level event because the same tubing carries hot or chilled water, not both; shoulder-season rooms that disagree are handled through ventilation air temperature rather than by flipping the hydronic system. A ceiling radiant surface has more capacity because its comfort limit is lower (about 55°F), but that raises the condensation risk. This design's ceilings are structural concrete, so ceiling radiant remains a possible later addition as hung panels on the same hydronic loop rather than cast-in tubing. Radiant cooling without dehumidification and backup is not a defensible default, because cooking, showers, and weather drive humidity excursions past the floor's capacity.

**Code**

```
Cooled-surface temperatures are limited by the comfort standard.
  Cooled floor: about 64°F minimum. Cooled ceiling: about 55°F. Surfaces stay above the interior dew point at all times.
  Source: ASHRAE 55-2023.

Radiant cooling design constraints follow the engineering handbook chapter.
  Supply water above dew point, dew-point sensing, window interlocks, dedicated dehumidification, floor-moisture backstop, and backup cooling.
  Source: ASHRAE Handbook, HVAC Systems and Equipment, Chapter 6 (Radiant Heating and Cooling).
```

## 13.11 Humidity And Dehumidification

Indoor humidity is held in a comfort band year-round: dry enough in summer to prevent mold and dust mites, moist enough in winter to be comfortable. A whole-house dehumidifier sized to the latent load carries the summer side and protects any radiant-cooling system.

**Simple**

Showers, cooking, laundry, and breathing all add water to the air. In a tight house that moisture has nowhere to go unless the ventilation removes it. Without ventilation, indoor humidity in a tight house climbs to 60-80 percent, and windows drip and mold follows. The target band is 30 to 50 percent relative humidity all year. The ventilator removes most of the excess, and a dehumidifier handles the humid weeks of summer.

**Applied**

- Target 30 to 50 percent relative humidity year-round, with the dehumidifier's humidistat set at 45 to 50 percent.
- Size a whole-house dehumidifier to the latent portion of the load calculation (commonly 70 to 130 pints per day for a well-built western Oregon house).
- Drain the dehumidifier condensate to an indirect waste, by gravity or a condensate pump.
- Manage moisture sources (showers, cooking, laundry, wet entry, and any leak) through exhaust, drainage, and maintenance, not by adding humidity in winter.

**Professional**

ASHRAE 55 places the comfort humidity band broadly between about 30 and 60 percent relative humidity; the practical residential target is 30 to 50 percent. Below 30 percent in winter dries occupants and wood; above 60 percent in summer encourages mold and dust mites. In winter the ERV's moisture transfer retains indoor humidity that ventilation would otherwise strip from a tight envelope, and if winter humidity still runs high the ventilation rate rises or the dehumidifier runs briefly. In summer the ERV rejects 60 to 70 percent of incoming outdoor moisture, and the dehumidifier removes the remainder of the latent load. Sizing comes from the latent load in the Manual J, expressed in pints per day; established ducted whole-house units include Ultra-Aire, Santa Fe, and Honeywell, located in the mechanical room and discharging to an indirect waste governed by the plumbing code. In a tight, well-insulated house paired with radiant cooling, the dehumidifier is the primary protection for the dew-point limit stated in the radiant-cooling section, and its control is coordinated with the cooling control so the dew point is corrected before condensation forms. A basement wine or food-storage area that wants a different band (55 to 70 percent for wine) gets its own small unit and setpoint rather than a compromise on the house band.

**Code**

```
Indoor humidity is held in the comfort band.
  Comfort range about 30 to 60 percent relative humidity per the standard; practical residential target 30 to 50 percent.
  Source: ASHRAE 55-2023.

The dehumidifier is sized to the calculated latent load.
  Latent load from the Manual J calculation, in pints per day; 70 to 130 pints per day is the common range for a well-built western Oregon house.
  Source: ACCA Manual J (latent load); manufacturer capacity ratings.

Dehumidifier and cooling condensate discharge to an indirect waste.
  Gravity drain or condensate pump to an indirect waste receptor.
  Source: OPSC Chapter 8 (indirect wastes, 2023 edition).
```

## 13.12 Filtration And Air Quality

Filtration removes particulates, and source control keeps them out of the air in the first place. A MERV 13 filter is the best-practice floor, with a dedicated high-efficiency unit for wildfire smoke.

**Simple**

MERV is a filter rating; higher numbers catch smaller particles. A MERV 13 filter catches most pollen, smoke particles, and bacteria-sized dust. Wildfire smoke is the hard case, because its particles are tiny and the events last days. For smoke weeks, a HEPA unit (a still finer filter) goes in each main living zone. It removes the fine particles that pass the main filter. Source control keeps pollution out in the first place: low-fume finishes, no indoor flames, and a range hood that runs whenever the stove does.

**Applied**

- Filter the ventilation and air-handling systems at MERV 13 minimum, sized so the filter bank does not choke the equipment, and locate the filter for easy access.
- Add a HEPA bypass or a stand-alone HEPA unit per main living zone for wildfire-smoke events.
- Control sources: low-VOC finishes, hard-surface floors, sealed-combustion appliances, a range-hood interlock, entry and mudroom zoning, and an outdoor air intake located away from driveways and dryer vents.

**Professional**

The ORSC does not mandate a filter efficiency, but MERV 13 is the best-practice floor and is referenced by ASHRAE 62.2 addenda; it captures most pollen, smoke fines, and bacteria-sized particles. The filter bank, fan capacity, and design airflow are sized together so MERV 13 does not overload the air handler. A fully installed HEPA filter imposes too high a static-pressure penalty for a typical residential air handler, so a HEPA bypass or a stand-alone unit is the practical answer for serious smoke events. Source control sets the base pollutant load that filtration then works against: stored chemicals, wet materials, and combustion products released indoors reach the occupants before any filter sees them.

**Code**

```
The residential code sets no minimum filter efficiency for dwelling ventilation.
  Filter selection is a design decision; MERV 13 is the best-practice minimum referenced for residential filtration.
  Source: ORSC M1505 and Chapter 11 (2023 edition, no filtration minimum stated); ASHRAE 62.2-2022 addenda.
```

## 13.13 Duct Design And Mechanical Room

With radiant systems carrying most of the heating and cooling, the ducts mainly move ventilation air, so they can be smaller, but they are still designed, sealed, kept inside the thermal envelope, and made accessible. The mechanical room provides the clearances, drainage, and sound isolation the equipment needs.

**Simple**

Because the floors do the heating and cooling, the only ducts in this house move fresh air. A forced-air house hides 1,500 to 3,000 cubic feet of ductwork in its walls and attic. This house needs about 200 to 400 cubic feet, all inside the insulated shell and all reachable. Every machine lives in one mechanical room, so noise, drains, and repairs stay in one place. When a machine wears out in twenty years, it comes out through the door it went in through.

**Applied**

- Design the duct system per Manual D; use rigid metal in primary trunks (10 to 12 inch round at 600 feet per minute or less) and 4-to-6-inch branches, limiting flex to short final connections, fully extended and unkinked.
- Seal duct joints with listed mastic or UL 181B-FX tape, keep ducts inside the thermal envelope, and keep dampers, cleanout ports, and filters accessible.
- Reserve mechanical-room space for the heat-pump plant, manifolds, pumps, expansion tank, HRV or ERV, dehumidifier, filters, condensate drain, and any water heater or treatment: 8 by 10 feet minimum, 10 by 14 feet for a well-equipped system, with a 32-inch minimum door and full ceiling height.
- Provide a floor drain or condensate sump for condensing equipment and the dehumidifier, vibration isolation on pumps and air handlers, and sound isolation where the room adjoins sleeping areas.
- Do not return air to the ventilation system from the mechanical room itself; any refrigerant leak or chemical odor there stays out of the living-space air path.
- Label equipment with model, serial, install date, and system volumes, and post a wall diagram and maintenance log in the room.

**Professional**

Ducts inside the thermal envelope are the energy-code default; a duct outside the envelope requires the specified deeply-buried configuration with R-8 duct insulation and the associated floor and vapor-barrier assembly. Duct sealing follows ORSC M1601.4 (listed mastics or UL 181B-FX tape); duct leakage in a typical forced-air house with attic or crawl-space ducts wastes 20 to 30 percent of heating and cooling output, and an all-inside, ventilation-only layout removes that loss category. The mechanical room provides the listing's working clearance (typically 30 inches at the front, 24 inches at the sides), a condensate drain path, and vibration and sound isolation near sleeping areas. Equipment noise runs about 50-55 dB for a heat-pump compressor, 45-50 dB for a heat-pump water heater, and 35-45 dB for a ventilator fan; an insulated wall assembly with a solid-core door keeps that noise out of the living space. The room is laid out so the heat pump, ventilator, water heater, dehumidifier, and controls can each be replaced during the life of the building. The electrical code requires 36 inches of depth and 30 inches of width in front of equipment likely to be serviced energized, which is coordinated against the mechanical clearances so the two do not conflict.

**Code**

```
Ducts are designed to the referenced method and sealed with listed materials.
  Design per ACCA Manual D; joints sealed with listed mastic or UL 181B-FX tape.
  Source: ORSC M1601 and M1601.4 (2023 edition); ACCA Manual D.

Ducts inside the thermal envelope are the energy-code default.
  Ducts outside the envelope require the specified deeply-buried configuration with R-8 duct insulation and the associated assembly.
  Source: ORSC N1103 (2023 edition).

Working space around equipment is preserved.
  Equipment listing clearances (typically 30 inches front, 24 inches sides); electrical working space 36 inches deep by 30 inches wide at equipment likely to be serviced energized.
  Source: equipment listing; OESC/NEC 110.26 (2023 edition).

Condensate has a drainage path.
  Floor drain, condensate sump, or pump to an indirect waste for condensing equipment and the dehumidifier.
  Source: OPSC Chapter 8 (indirect wastes, 2023 edition).
```

## 13.14 Energy-Code Integration And Controls

The mechanical design is verified against the energy code through the blower-door test, the sealed-combustion and duct-location rules, and a required smart thermostat. Equipment control runs locally so the house keeps heating, cooling, and ventilating without an internet connection.

**Simple**

The energy code checks the mechanical design mostly at one event: the blower-door test. That test measures how much the envelope leaks. The code also requires a smart thermostat. In this house the controls work on the local wiring and network. Heating, cooling, and ventilation continue with no internet connection; the internet only adds dashboards and alerts.

**Applied**

- Design the envelope and mechanical systems to the energy-code air-leakage target and document the blower-door result on the state form.
- Provide a local-first thermostat and controls whose primary function does not depend on cloud connectivity, on the wired 24-volt backbone stated in the radiant section.
- Monitor the basics: room temperature and humidity, system mode, filter status, pump and fan faults, water leaks, condensate problems, ventilation boost, and dehumidifier runtime.
- Route alerts by severity: immediate notification for loss of heat, water leaks, or carbon monoxide; a daily summary for filters due and zones missing setpoint; a monthly report for energy and runtime trends.
- Keep required equipment operation independent of the smart-home layer.

**Professional**

ORSC Chapter 11 sets the energy framework. The prescriptive air-leakage limit is 3.25 ACH50 (N1104.8.2); the high-achievement measure pairs 2.75 ACH50 with a heat-recovery ventilator at 66 percent sensible efficiency and 1.6 CFM per watt. Ducts are inside the thermal envelope by default, sealed combustion with outdoor combustion air is required for any appliance inside the envelope, and a smart thermostat is required (N1105.4.1.2). The blower-door result is documented on the BCD residential blower-door form and submitted before the certificate of occupancy; the ORSC does not require a separate duct-leakage test in the general path, though some Additional Measures include duct-leakage limits. Blower-door procedure, equipment, and costs are stated in the envelope chapter.

The control architecture has three levels. Equipment controllers (heat pump, ventilator, manifold controllers, dehumidifier humidistat) run their machines locally and are the only level required for operation. An integration controller (a dedicated hydronic control such as Tekmar, or a local automation server) coordinates them: it reads the room thermostats, sequences heating and cooling calls, adjusts ventilation speed, and runs the dew-point logic from the radiant-cooling section. The dashboard layer displays trends and sends the alerts; it is the only level connected to the internet, and its failure changes nothing about heating, cooling, or ventilation. A thermostat whose primary control depends on cloud connectivity is rejected in favor of a local-first control, which is a market-availability constraint rather than a code requirement. Control logic for hydronic zoning, ventilation, dehumidification, and radiant cooling is a design deliverable alongside the hardware selection, because poor control causes short cycling, humidity drift, or condensation even when the equipment is sized correctly. The smart-home chapter states the network, logging, and remote-access design. The voluntary Oregon Residential Reach Code (ENERGY STAR Single-Family New Homes) is an available alternative to Chapter 11 where an ENERGY STAR label is wanted, at the cost of a rater and added verification.

**Code**

```
The envelope must meet the air-leakage limit, verified by blower-door test.
  Prescriptive limit 3.25 ACH50 (air changes per hour at 50 pascals); Additional Measure 7: 2.75 ACH50, third-party tested, with ventilation heat recovery at 66 percent sensible efficiency minimum and 1.6 CFM per watt.
  Source: ORSC N1104.8.2; Table N1101.1(2), Measure 7 (2023 edition).

Ducts stay inside the envelope, and indoor combustion appliances are sealed.
  Ducts inside the thermal envelope as the default; sealed combustion with outdoor-ducted combustion air for appliances inside the envelope.
  Source: ORSC N1103 (2023 edition).

A smart thermostat is required.
  Thermostat meeting the smart-thermostat provision; local-first control is a project selection on top of the requirement.
  Source: ORSC N1105.4.1.2 (2023 edition).

The blower-door result is filed before occupancy.
  Result documented on the BCD residential blower-door form and submitted to the building official before the certificate of occupancy.
  Source: ORSC Chapter 11 (2023 edition); BCD residential blower-door form.

A voluntary reach code exists as an alternative energy path.
  2023 Oregon Residential Reach Code: ENERGY STAR Single-Family New Homes Version 3.2 (Rev. 13) with on-site verification; applicant's election, jurisdictions cannot require it.
  Source: 2023 Oregon Residential Reach Code (HB 3409, 2023).
```

## 13.15 Outage Behavior And Energy Independence

This project's independence principle extends to energy: the house keeps its occupants safe and comfortable through a power outage, and the mechanical design is what makes that true. The concrete mass, the tight envelope, the small ventilation load, and one non-electric heat source together define the outage behavior.

**Simple**

When the power fails in a normal house, the furnace stops and the temperature falls within hours. Here the concrete has been storing heat all along, and the tight envelope loses it slowly. The indoor temperature falls over days. The fans and pumps that keep air fresh draw about as much power as a light fixture. A battery or a generator can carry that load. A wood stove, if the option is exercised, heats with no electricity at all.

**Applied**

- Put the ventilation unit, the hydronic circulators, the controls, and the monitoring on the backed-up circuits defined in the electrical service chapter's backup-power provisions.
- Verify the heat pump's restart behavior after an outage: automatic restart, no fault latch requiring a service call, and inrush within the backup source's rating.
- Record the outage plan in the house documentation: which loads are backed up, where the manual overrides are, and how long the backup source runs them.
- Test outage behavior annually: open the main breaker, confirm the backed-up circuits carry the ventilation and controls, confirm the systems restart cleanly on restoration, and log the test.
- If the wood-stove option is exercised, keep it usable: dry fuel stored, chimney swept, and the hearth kept clear.

**Professional**

The passive half of outage performance is the structure itself: the thermal mass stores heat and the envelope (3.25 ACH50 prescriptive, 2.75 under the high-achievement measure) limits the loss rate, so the indoor temperature decays slowly toward outdoor conditions instead of tracking them. The same mass supports grid-flexible operation in normal service: the plant can heat the mass during low-rate hours and coast through peak hours, a control schedule rather than added hardware.

The active half is load prioritization. The ventilation unit is the largest continuous need and it is small: at the energy code's 1.6 CFM-per-watt measure, the roughly 68 CFM continuous rate computed in the ventilation section draws on the order of 45 watts. The hydronic circulators and control transformers are the other continuous loads, and ventilation, circulation, and controls together fit within the battery or generator capacity specified in the electrical service chapter. The heat pump itself is the discretionary load, run when the backup source has capacity and shed when it does not. With the heat pump shed, the radiant mass keeps releasing its stored heat, and a certified wood stove (specified in the combustion-appliance section) provides heat with no electrical input. Sole-source-heat residences are exempt from DEQ burning curtailment, so the stove remains usable in an advisory. During an extended outage with mechanical ventilation down, operable windows provide interim ventilation; the balanced system resumes automatically on restoration. Smart-home monitoring of the outage (state of charge, load status, temperatures) is specified in the smart-home chapter.

## 13.16 Commissioning And Records

The mechanical systems are commissioned so they meet their design performance, and the records prove the load calculation, the balance, and the equipment startup. The code acceptance trail is a floor; a private commissioning checklist confirms the system performs as designed, and the first year is a planned tuning period.

**Simple**

Commissioning means measuring what was built and adjusting it until it matches the design. Every loop gets its flow checked, every register gets its airflow measured, and every control gets exercised. The records go in the permanent house file. They prove the system worked on day one, which matters at resale and every time something drifts later.

**Applied**

Before accepting the system, verify and retain:

- Equipment matches the approved design and is installed to the manufacturer's instructions.
- Ducts are sealed and accessible, hydronic loops are labeled, and manifolds are reachable.
- Pumps run, valves operate, and thermostats control the correct zones; each zone reaches setpoint and cycles off.
- Ventilation supply and exhaust are measured at every register with a flow hood ($200-$1,500 to buy, and rentable) or measured at the unit, balanced within 10 percent of each other and within 10 percent of design at each register (5 percent is the better target).
- Recovery performance spot-checked: sensible recovery efficiency = (supply temperature − outdoor temperature) ÷ (indoor temperature − outdoor temperature) × 100, compared against the manufacturer's rating.
- Static pressures checked with a digital manometer ($50-$300); loop temperatures and current draw checked with a clamp meter ($50-$200) (2026 tool prices).
- The range hood and makeup air operate together; the dryer exhaust is clear; condensate drains.
- The Manual J, S, and D documentation, the concealment inspection of the dryer duct and combustion-air paths, and the blower-door result on the BCD form are on file before the certificate of occupancy.
- A private commissioning record covers hydronic pressure-test logs, glycol concentration, flow at each manifold loop, air balance at each register, dehumidifier capacity, dew-point sensor calibration, and radiant control-sequence verification.
- Retest and tune after the first winter and first summer.

**Professional**

The ORSC does not impose a commercial-style commissioning regime, so its acceptance trail is the load documentation, the concealment inspections, the blower-door result, equipment installed to the manufacturer's instructions, the smart thermostat, and the HRV or duct-leakage documentation where an Additional Measure is claimed. Refrigerant work sits outside the owner-builder scope: charging, recovery, and repair require an EPA Section 608 certified technician. The owner's role is to receive, review, and file the technician's commissioning report (subcooling and superheat against the manufacturer's targets, capacity check, power draw), then verify operation annually against it. Performance targets from this project's design files: heating COP of 3.5 or better and cooling EER of 15 or better annualized for a ground-source plant; recovery at 85 percent sensible and 60 percent latent or better; every loop within 10 percent of design flow; floor surface temperatures uniform within 5°F inside a zone. The private commissioning checklist is what makes the balanced ventilation, radiant, dehumidification, and control systems meet the performance design, and its results stay in the permanent house file with the equipment manuals and startup records. Measured performance over the first heating and cooling seasons shows the interaction of building mass, occupancy, ventilation settings, and control logic, so the first year is scheduled as a tuning period. The schedule: re-balance after the first winter and first summer, then annually check the heat-pump report items, clean the ventilator core, and inspect the manifold connections.

**Code**

```
The load calculation and duct design are part of the permit record.
  Manual J, S, and D documentation submitted with the permit application.
  Source: ORSC M1401.3 (2023 edition); ACCA Manuals J, S, D.

Concealed mechanical work is inspected before cover.
  Dryer duct, combustion-air paths, and gas rough piping inspected before concealment; gas final inspection after appliance connection.
  Source: ORSC R109 inspection provisions; G2417.1.1.1 and G2417.1.1.2 (2023 edition).

The blower-door result and thermostat verification close out the energy trail.
  Blower-door result on the BCD residential form before the certificate of occupancy; smart-thermostat verification; HRV efficiency or duct-leakage documentation where an Additional Measure is claimed.
  Source: ORSC N1104.8.2, N1105.4.1.2, Table N1101.1(2) (2023 edition); BCD residential blower-door form.

Refrigerant work requires federal technician certification.
  Charging, recovery, and repair of the refrigerant circuit by an EPA Section 608 certified technician; the commissioning report is retained in the house file.
  Source: Clean Air Act Section 608 technician certification (EPA).
```
