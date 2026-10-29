# Chapter 22: Solar, Battery, and Energy Independence

In the Willamette Valley a south-facing array makes 20 to 30 percent as much electricity in December as in July, depending on its tilt. December is also when the heat pump runs hardest, so the battery and the generator are sized to that month. Connected to the grid, the house runs on its battery through outages and buys from the utility through the dark months. Off the grid, it needs a battery bank sized for weeks of cloud or a generator that runs through the winter. Neither the federal credit nor Energy Trust's payments apply to an owner-installed system, and the property-tax exemption is the one incentive left to it.

> **Jon's note.** [JON: drafted from the record, confirm or rewrite] I want the power to be mine, as I want the water to be: panels on the roof, a battery in the house, and a generator for the storm that outlasts the battery. Battery storage comes first because it works for the house every day and needs no fuel. I would rather own parts I can replace one at a time than one cabinet that takes the whole system down when it fails. Panels, inverters and batteries will be replaced several times over the life of the concrete, so the roof anchors, the conduit and the panel space are built for that from the first pour. [JON: grid-tied with a battery, or fully off-grid? The parcel's extension quote decides the money, but which way do you lean?] [JON: how many days should the battery carry the house with no sun and no generator?]

## 22.1 The goal and the load list

**Simple**

Sizing a solar system starts with a list of what the house uses in a day. Each appliance draws some watts for some hours. Watts times hours gives watt-hours, and a thousand make one kilowatt-hour, the unit on a power bill. Ventilation fans, well-pump controls and network routers never switch off. Running all day, a 45-watt fan uses about as much as a 1,000-watt heater running for an hour. Cutting a kilowatt-hour from the daily list cuts a kilowatt-hour from the battery the house must buy. Food in a root cellar stays cool with no power, and water from a spring above the house needs no pump.

**Applied**

1. Build the load list in a spreadsheet before pricing any equipment.
2. Enter each load's watts, hours a day and months of use.
3. Multiply watts by hours and divide by 1,000 for each load's daily kWh.
4. Take refrigerators and freezers from the EnergyGuide label, kWh a year divided by 365.
5. Measure every always-on device with a plug-in energy meter over 24 hours.
6. Total the always-on watts, multiply by 24, and record the result as the daily floor.
7. Tag each load for outages as must run, run when the battery allows, or wait for the grid.
8. Schedule the water heater, the buffer fill, laundry and EV charging for 10 a.m. to 3 p.m.
9. Specify a heat-pump water heater with a CTA-2045 port, so a controller can run it from a solar signal.
10. Size the root cellar and pantry first, then the freezers, then their share of the battery.
11. Rerun the list when the passive design, the envelope and the appliances are final.
12. Save each version of the list, dated, in the project binder.

**Professional**

Any load that runs around the clock passes through the battery every night and every cloudy day, while a noon load draws on the array directly. Always-on watts therefore fix the smallest battery the house can use. In this house the ventilation unit is the largest continuous load, near 45 watts at the energy code's fan-efficacy limit. Hydronic circulators and control transformers come next. In an outage the heat pump, the largest load overall, runs only when the battery or the sun can carry it. Outage loads and restart checks for the mechanical plant are in the HVAC chapter.

Moving a kilowatt-hour into the hours the array produces keeps it out of the battery entirely. On a CTA-2045 controller, a heat-pump water heater stores midday output as hot water, and a tank one size above the peak-hour rule stores more. Well-pump buffer filling, laundry and EV charging shift the same way. Each shiftable load's daily kWh then moves out of the battery column, and the bank is repriced at the smaller size.

During an outage the well pump lifts every gallon on battery power, while a spring above the house delivers by gravity. Lifting 1,000 gallons through 100 feet of total head takes 0.31 kWh before pump and motor losses. Dividing that by the wire-to-water efficiency on the pump's curve gives the electrical energy. At EPA WaterSense's figure of 300 gallons a day for an average family and 300 feet of head, the lift alone is 0.28 kWh a day. Starting current sets a separate requirement, met by the inverter's surge rating or lowered by a soft-start or constant-pressure pump drive.

Chest freezers run at 80 to 150 watts and draw 600 to 1,200 watts for a moment as the compressor starts. Full and closed, one holds a safe temperature for 24 to 48 hours without power. Composting-toilet vent fans draw 1.4 to 2.5 watts (Sun-Mar and Separett ratings), 0.06 kWh a day at the high end. Incinerating toilets draw 1 to 2 kW through each burn cycle, a load sized from the chosen product's rating.

Passive design and the envelope cut the seasonal heating energy the array must supply. They do not cut the heat pump's design-day capacity, because the design hour is a cloudy winter night. Two sizes shrink with the seasonal energy: an array sized to annual use under net metering, and the generator's run hours in a long outage. Their size comes from an hourly energy model run with and without the passive measures.

## 22.2 The Oregon sun, month by month

**Simple**

In western Oregon a solar panel makes most of its year's power between April and September. At noon on the shortest day the sun stands 21 to 22 degrees above the horizon. Clouds cover three-quarters of the winter sky on average. Tilted steeply toward that low sun, a panel catches half again as much December light as one lying almost flat. Over a year the two make within 4 percent of each other. Low winter sun casts long shadows, so a tree or a shop south of the panels can shade them from November to February. A Douglas fir south of the array can reach 60 to 100 feet or more.

**Applied**

1. Run PVWatts (pvwatts.nlr.gov) for the parcel at tilts of 10, 45 and 60 degrees.
2. Record each run's monthly table with its date and inputs.
3. Size the array and the battery for the winter loads from the December figure, not the annual total.
4. Take a Solar Pathfinder reading at the chosen array site, at module height.
5. Trace each tree and structure on the chart and note its species or planned height.
6. Get each species' mature height from an arborist or OSU Extension.
7. Model trees at mature height and planned outbuildings at full height, in software or on the chart.
8. Record the shading loss for each month in percent, and reduce the PVWatts table by it.
9. Mark the array's solar envelope on the site plan, with the mature-height shadow lines.
10. File the PVWatts tables, the Pathfinder photograph and the traced chart in the binder.

**Professional**

PVWatts, run by the National Laboratory of the Rockies (named NREL until December 2025), models a typical meteorological year from the National Solar Radiation Database. Its output per kilowatt of panels at four Oregon locations, south-facing on an open rack with 14 percent system losses, appears in the table.

| Location (latitude) | Tilt, degrees | December, kWh per kW | July, kWh per kW | Year, kWh per kW | December per day, kWh per kW |
|---|---|---|---|---|---|
| Portland (45.5 N) | 10 | 28 | 158 | 1,085 | 0.9 |
| Portland (45.5 N) | 45 | 41 | 138 | 1,115 | 1.3 |
| Salem (44.9 N) | 10 | 31 | 168 | 1,159 | 1.0 |
| Salem (44.9 N) | 45 | 45 | 146 | 1,188 | 1.4 |
| Salem (44.9 N) | 60 | 45 | 123 | 1,086 | 1.5 |
| Eugene (44.1 N) | 10 | 31 | 161 | 1,144 | 1.0 |
| Eugene (44.1 N) | 45 | 43 | 139 | 1,160 | 1.4 |
| Medford (42.3 N) | 10 | 42 | 174 | 1,312 | 1.3 |
| Medford (42.3 N) | 45 | 61 | 149 | 1,356 | 2.0 |

PVWatts' December is an average of many Decembers. Overcast weeks deliver less than the table, and in this design the generator covers that shortfall instead of a larger battery. Tilt moves output between the seasons. At 45 degrees a Salem array makes 45 kWh per kilowatt in December against 31 at 10 degrees, with nearly the same annual total. At 60 degrees December gains nothing more and the year loses 9 percent. Medford's December output at 45 degrees runs 36 percent above Salem's at the same tilt.

Reflecting the whole sky onto a printed sun-path chart, the Solar Pathfinder shows in one reading which obstruction shades the array in which month, in any weather. Shading software built on a digital site model, such as the Solmetric SunEye's analysis or OpenSolar, can place a future obstruction at full height before it exists. Planned outbuildings have a known height and position. Trees are modeled at their species' mature height, not their height on the day of the reading. Under the solar access law the passive design chapter states, a neighbor's trees are held back only by a recorded easement or a local ordinance.

## 22.3 Off-grid, grid-tied or hybrid

**Simple**

Three setups are possible, and they differ in what happens when the power line goes dead. In a plain grid-tied system the inverter shuts off in an outage, to protect line crews. The house goes dark with its neighbors. Adding a battery and a switch that separates the house from the line makes a hybrid. Its important circuits keep running through the outage. Off the grid, the battery and a generator carry every winter night. In western Oregon an off-grid house either runs its generator through the darkest months or buys enough battery for weeks of cloud.

**Applied**

1. Get the serving utility's written line-extension quote for the parcel.
2. Price the grid path as the extension cost plus the monthly charges over the comparison period.
3. Price the hybrid as array, battery, inverters and installation, plus their replacements over the same period.
4. Price off-grid as an array and battery sized to December, the generator, its fuel and the same replacements.
5. Take the fuel figure from the generator's dispatch estimate.
6. Subtract any incentive still open at installation.
7. Compare the three totals over 30 years or the expected ownership, whichever is longer.
8. Record the comparison, its inputs and their dates in the binder.

**Professional**

Costs are 2026 figures unless a different year is given. Oregon installations averaged $2.40 per watt on EnergySage's October 2026 figures, near $30,000 for the average 12-kilowatt system before incentives. Installed batteries ran $1,100 to $1,200 per kWh of storage on EnergySage's national figures, so one 13.5 kWh unit costs near $16,000. Together they put a hybrid near $46,000 before replacements.

Grid service and solar compare over the life of the equipment, by the method the land chapter states: the extension quote and the monthly charges on one side, capital cost and replacements on the other. Off the grid, the solar side also carries the generator, its fuel and its maintenance. Under net metering the grid holds summer surplus as bill credit until the annual true-up, so a hybrid array is sized to annual use. Off the grid, surplus has nowhere to go once the battery is full, and the array is sized to December instead.

Writing at Practical Self Reliance, a Vermont off-grid homesteader described panels producing a surplus with the batteries full before noon for nine months of the year. Through the three coldest months the generator ran 10 to 15 times a month. That household found a grid connection's monthly charge cheaper than the propane. Monthly residential customer charges of $12 to $25 set the grid side of the same comparison here.

Battery autonomy costs the same for every added day, one day's critical load in usable kWh. A generator covers the rare multi-week stretch for the price of its fuel. This design sizes the battery for the outage days Jon chooses and leaves the longer stretch to the generator. Grid-tied inverters certified to IEEE 1547 and UL 1741 stop exporting when the utility voltage disappears, which is why a plain grid-tied array gives no outage power. A hybrid adds a listed transfer or microgrid device that opens the utility connection before the battery inverter forms its own grid.

## 22.4 How the parts connect

**Simple**

Panels make direct current, and the house runs on alternating current. An inverter converts one to the other. In a DC-coupled system, one inverter serves both the panels and the battery, so one failure stops both. In an AC-coupled system, each has its own inverter, and either keeps working when the other fails. Separate parts can be replaced one at a time, even with another maker's model. All-in-one cabinets install faster. When the inverter inside one fails, the panels and the battery both stop until the maker's part arrives.

**Applied**

1. Choose AC coupling, with separate PV and battery inverters.
2. Buy inverters and batteries whose parts and service are sold separately.
3. Put module-level electronics, microinverters or DC optimizers, on every roof module.
4. Choose a battery inverter with a listed transfer or microgrid interconnect function.
5. Confirm it has a generator input and a two-wire generator start contact.
6. Confirm each inverter's listing to UL 1741 Supplement SB and the battery's to UL 9540.
7. Draw the one-line diagram before ordering, with every source, inverter, disconnect, panel and the meter.
8. File the datasheets, the listings and the one-line diagram in the binder.

**Professional**

DC coupling charges the battery straight from the array through one converter. Clean Energy Reviews puts its charging efficiency at 96 to 99 percent, against 90 to 92 percent for AC coupling. In exchange, one inverter's failure stops both production and storage, and that inverter has to sit close to the battery. AC coupling gives up a few points of round-trip efficiency for separation. A failed battery inverter leaves the array producing, and inverters and batteries can sit in different rooms. Storage added years later needs no match to the original PV inverter's compatibility list.

All-in-one cabinets, holding the inverter, the charge controller and sometimes the battery, share the DC-coupled failure profile: one support contact and one part that stops everything. A component stack of separately sourced charge controller, inverter and battery costs more integration work at the start. Any one of its parts can then be replaced with an equivalent from another maker.

Microinverters convert each module's output to AC on the roof, so no high-voltage DC runs down to the house, and each module de-energizes itself when rapid shutdown is triggered. DC optimizers shut down at the module but keep a DC string to a central inverter. A microgrid interconnect device senses the loss of utility voltage, opens the connection to the utility, and lets the battery inverter form an isolated grid for the house. Oregon's amendment to NEC 705.50 puts customer-side microgrid equipment under the current electrical code. With the utility connection held open, the house can also run on its own array and battery before the utility grants permission to operate.

**Code**

```
Solar equipment carries the listings the residential code names.
  Modules to UL 1703 or to UL 61730-1 and 61730-2, inverters to UL 1741 and listed for utility interaction where grid-connected, and mounting systems to UL 2703.
  Source: ORSC R324.3.1 (2023 edition).
```

## 22.5 The array: where it sits and how it is held

**Simple**

The concrete roof can carry the array, but how the panels attach has to be settled before the roof is poured. Ballasted trays hold the panels down with concrete blocks and leave the roof membrane unbroken. Anchor plates cast into the concrete hold better in wind, and they fix the layout at the pour. Ground and pole mounts put the panels where snow can be brushed off from the ground. A pole can also tilt them toward the winter sun. Flat on a roof, panels catch about a third less December light than steep ones on a pole.

**Applied**

1. Fix the array's size, layout and attachment before the roof shop drawings are issued.
2. Give the engineer of record the array weight, the rack footprint and the foot loads.
3. For ballast, get the rack maker's ballast layout for the site's wind speed and exposure.
4. Check each rack foot's load against the strength of the pavers and insulation under it.
5. Keep rack feet, ballast and trays clear of roof drains, scuppers and their flow paths.
6. For anchors, set embed plates or sleeves at the rack maker's grid before the pour, tied into the deck steel.
7. Where the final layout is uncertain, cast anchors for a fixed starter array and leave the rest of the zone for ballast.
8. Lay out the fire pathways on three sides of the array, and keep boxes and disconnects out of them.
9. Bridge any raceway that crosses a pathway on the flat roof.
10. For a ground or pole mount, get engineered footings and trench its conduit with the other site trenches.
11. Photograph every embed and anchor before the pour, and file the photos with the roof drawings.

**Professional**

Ballasted racks resist uplift and sliding with dead weight. They leave the membrane unbroken, which keeps the roofing warranty intact and lets the array grow later without new roof work. Their cost is dead load, which the roof design carries from the first drawing. On a protected-membrane roof the rack feet bear on pavers over the insulation, so the insulation board's compressive strength limits the foot load. Cast-in anchors (embed plates, sleeves or threaded inserts tied into the deck reinforcing) resist more uplift without added weight, and the roof's waterproofing detail seals them when it is designed. Their grid is fixed at the pour, and moving it later means coring through a finished, waterproofed deck.

A steeper rack presents more area to the wind and needs more ballast or anchorage, and the PVWatts table lists what a low tilt costs in December. Oregon's prescriptive rooftop path, with its weight and attachment limits and BCD's checklist form 440-5952, covers only light-frame roofs that already exist. On a concrete roof the array's weight and wind loads enter the structural design from the first drawing, and the roof chapter specifies the membrane, flashing and embed details.

A ground array needs no roof penetration and adds no roof load, cleans and clears of snow from the ground, and puts the inverter at grade. Its costs are yard area and a longer conductor run to the panel. A pole mount gathers the foundation work into a few footings and can carry a seasonal tilt adjustment. Rapid shutdown applies to PV circuits on or in buildings, so only the part of a ground array's circuit that enters the house falls under it. On a standing-seam metal roof, non-penetrating clamps such as S-5!'s hold the rack, and the same clamp line serves snow guards and fall-protection anchors.

[FIGURE: pv-roof-layout, plan of the flat concrete roof with the array zone, fire pathways on three sides, roof drains, and the cast-in anchor grid for the starter array]

**Code**

```
A rooftop array and the roof under it are designed for the array's loads.
  Gravity and wind loads by engineered design under R301.1.3 or ORSC Chapter 8, with prescriptive installation limited to existing conventional light-frame roofs.
  Source: ORSC R324.4.1 (2023 edition).

The roof under the array is checked for two load cases.
  Dead load with the array plus snow load, and dead load without the array plus roof live load or snow load, whichever is greater.
  Source: ORSC R324.4.1.1 (2023 edition).

The array takes the roof's fire classification.
  Same fire classification as the roof assembly required by R902.
  Source: ORSC R324.4.2 (2023 edition).

Fire fighters get pathways around the array.
  Pathways at least 36 inches wide along at least three sides of the solar roof plane, over structurally supported area, measured from the roof edge.
  Source: ORSC R324.6.8.1 (2023 edition).

The array keeps clear of roof features and serviced equipment.
  No obstruction of vents, skylights or drains, and at least 30 inches of clearance around mechanical equipment that needs service.
  Source: ORSC R324.6.5 and R324.6.6 (2023 edition).
```

## 22.6 The battery bank

**Simple**

Lithium iron phosphate packs are the home battery sold today, because they last thousands of cycles and do not burn the way phone batteries can. Below freezing they cannot be charged safely. Charging a frozen cell plates metallic lithium inside it, and the damage is permanent. Its management electronics refuse charge below about 32 °F, so a cold battery stops taking power from the panels until it warms. Inside the house's conditioned space it never gets that cold. A pack in a shed needs insulation and a small heater, and the heater runs on the battery's own power in the darkest weeks.

**Applied**

1. Install the battery inside the conditioned envelope, in a utility room, basement or garage.
2. Keep it out of sleeping rooms and any closet or space that opens into one.
3. Multiply the autonomy days by the daily critical-load kWh for the usable kWh, then divide by the rated depth of discharge for the nameplate.
4. Buy packs rated 20 kWh or less each and keep the room's total at 40 kWh or less.
5. Where a shed is the only place, buy a self-heating pack or add a thermostat-controlled heater sensing at the pack.
6. Set the heater to hold the pack at 41 to 50 °F and add its watts to the always-on load list.
7. Set the generator-start threshold at 20 to 30 percent state of charge.
8. Confirm the battery is listed to UL 9540 and marked for residential dwelling units.
9. Add a smoke alarm in the battery room, interconnected with the house alarms.
10. Keep the maker's installation, operation and decommissioning instructions beside the battery.
11. Record the battery's cycle count and capacity reading each January.

**Professional**

Lithium plating below 0 °C occurs at any charge rate, so slowing the charge is no workaround, and the battery management system's low-temperature cutoff is the protection. Discharge is tolerated to about -20 °C. Charge acceptance returns only when the cells warm, and charging itself warms them. A self-heating pack carries elements that bring the cells above the cutoff before current flows. In a shed, a heater sized to the enclosure draws through the same low-sun weeks that drain the bank, and its energy belongs in the load list.

Usable energy is nameplate energy times the rated depth of discharge, and the warranty's cycle count assumes that depth. Lead-acid packs tolerate cold charging but deliver fewer cycles at a shallower depth of discharge, which is why lithium iron phosphate is the residential default. EnergySage's 2026 figures put installed storage at $1,100 to $1,200 per kWh before incentives.

A concrete utility room exceeds the one-hour separation NFPA 855 seeks for an indoor installation. Residential lithium iron phosphate packs produce no hydrogen in charging and need no mechanical ventilation under the residential code's rule for gassing chemistries. Repurposed electric-vehicle modules and other unlisted assemblies need the building official's approval and stay out of the house. The storage circuit, its disconnect and the transfer function follow the electrical code's storage and standby articles.

**Code**

```
A home battery is a listed energy storage system.
  Listed and labeled to UL 9540, with an exception for approved repurposed electric-vehicle batteries outdoors or in a detached shed at least 5 feet from walls, lot lines and public ways.
  Source: ORSC R329.2 (2023 edition).

Battery location is limited to four kinds of space.
  Detached garages and accessory structures, separated attached garages, outdoors or on exterior walls 3 feet from doors and windows, and enclosed utility or storage spaces with finished or noncombustible surfaces; never sleeping rooms.
  Source: ORSC R329.4 (2023 edition).

Battery size is capped per unit and per location.
  20 kWh per unit; 40 kWh total in utility closets, basements and storage spaces; 80 kWh in garages, accessory structures, on exterior walls or outdoors.
  Source: ORSC R329.5 (2023 edition).

Battery rooms get fire detection.
  Smoke alarms per R314 in the room, or a listed interconnected heat detector where a smoke alarm cannot be installed.
  Source: ORSC R329.7 (2023 edition).

The battery's documents stay with it.
  The manufacturer's installation, operation, maintenance and decommissioning instructions kept near the equipment, and a label with the service provider's contact information.
  Source: ORSC R329.11 (2023 edition).
```

## 22.7 Backup generation

**Simple**

When a storm or a cloudy stretch outlasts the battery, the generator takes over. A controller watches the battery's charge and starts the engine when it falls to a set level. The generator then charges the battery and runs the house at the same time, and shuts off when the battery is full. Propane keeps for years in its tank, where gasoline goes stale in months. A starter battery that has gone flat is the most common reason a standby generator fails to start. Engine exhaust carries enough carbon monoxide to kill in a closed shed, so the exhaust pipe runs outside.

**Applied**

1. Size the generator at about twice the inverter's continuous rating, then check it against the inverter's maximum AC input current.
2. Choose propane fuel and an engine rated for it.
3. Choose a unit with a two-wire start contact and wire it to the inverter's generator-start output.
4. Set the start threshold at the battery's chosen low charge and a minimum run time that avoids short cycling.
5. Place the generator per NFPA 37 and the maker's clearances, exhaust pointed away from doors and windows.
6. Give a shed a low intake vent and a high outlet vent sized to the maker's airflow figure, and run the exhaust through the wall.
7. Hire a licensed LP installer for the tank, regulator and gas piping.
8. Set a 125-to-500-gallon tank 10 feet from the house and the lot line, a 501-to-1,000-gallon tank 25 feet.
9. Keep the starter battery on a float charger and stock a spare.
10. Run the generator under load monthly, and change oil and filters by the maker's hour intervals.
11. Stock oil and air filters, spark plugs, and the wear parts the service manual names.
12. Log every run, with its hours and fuel, in the binder.

**Professional**

Two-wire start closes a dry contact when state of charge crosses the inverter's threshold, and any generator wired for two-wire start answers it. Communication-based start exchanges fuel level, run hours and fault codes over a maker's data link and permits load-based starting. Its cost is matched equipment from one maker for the generator's service life. Open-transition transfer, break before make, de-energizes the house for a moment between sources and is what NEC 702 transfer equipment is built around. Closed transition parallels the two sources briefly and needs utility coordination.

In a dispatch cycle the critical loads run on the battery, topped up by whatever the array makes. When state of charge falls to the threshold, the generator starts, carries the house and recharges the bank, then stops at the high threshold or after its minimum run. On a partial-cloud winter day that may happen daily or every few days. Daily fuel burn is the maker's gallons-per-hour figure at the running load fraction, times the hours the cycle calls for. A 20-to-24-kilowatt residential standby unit burns about 2 gallons of propane an hour at half load and 3.6 to 4 at full load.

A low-yield well's buffer tank lowers the generator's peak. Filling the tank at a steady trickle, the pump never starts at full inrush on every open tap, and the generator is sized to the running load instead.

Propane derates an engine 10 to 15 percent against gasoline and keeps indefinitely in a sealed tank, with no stabilizer and no rotation. Stabilized gasoline keeps one to three years and untreated gasoline three to six months, and ethanol-free fuel keeps better in small engines. Diesel keeps 18 to 24 months, two to five years with a stabilizer and biocide, and its failure mode is microbial growth and water rather than gum.

NFPA 58, which the State Fire Marshal enforces, separates an above-ground tank of 125 to 500 gallons by 10 feet from important buildings and buildable property lines. A 501-to-1,000-gallon tank sits 25 feet off, and an underground tank 10 feet at any size, per the Propane Deal and CF Insurance distance tables. The multi-week fuel reserve, the tank size it needs and the fuel store's place on the site plan are in the resilience chapter, with the transfer equipment in the electrical service chapter and the shed itself in the site-development chapter.

Rural users report stale fuel gumming the carburetor, a flat starter battery, and bearing wear from long runs as the three common failures. Drained fuel systems, float charging and hour-based service answer them in turn.

**Code**

```
A standby source that connects loads automatically carries them.
  Full automatically connected load, or an energy management system under Article 130; manual load management permitted in one- and two-family dwellings.
  Source: OESC 702.4(A)(2) (2026 edition, Oregon amendment).

A fixed generator sits in an approved location.
  Installed per its listing, the manufacturer's instructions and the Electrical Code.
  Source: ORSC R330.1 (2023 edition).

LP gas work is licensed, with no owner exemption.
  Installing, extending, altering or repairing LP gas appliances or piping requires an LP gas installation license from the State Fire Marshal.
  Source: ORS 480.432(1).
```

## 22.8 Incentives and the installer path

**Simple**

Most of the money that once paid for home solar is gone for a house built now. The federal 30 percent credit ended for installations finished after 2025. Energy Trust of Oregon pays $2,500 toward a home array and up to $5,000 toward a battery. Those payments go only to customers of the two investor-owned utilities, and only when one of its approved contractors does the work. The state's rebate program is fully reserved for 2026 and also requires an approved contractor. One incentive survives for an owner-built system. Oregon does not tax the value the panels add to the house, under a law that runs through the tax year beginning in 2029.

**Applied**

1. Confirm which utility serves the parcel before counting any incentive.
2. On PGE or Pacific Power service, get a trade-ally bid for the array and battery, and a materials-only price for the same equipment.
3. Compare the bid, less $2,500 and the battery payment, against the materials price plus the permit fees.
4. Check Energy Trust's current offers and the state program's reservation status in the install year.
5. Keep the equipment invoices and the final-inspection record in the binder for the assessor.

**Professional**

Under the federal statute an expenditure counts as made when the installation is completed, so a system finished in 2026 earns none of the old credit. Energy Trust's 2026 residential offers are in the table. Its program rules require installation by an approved, active solar trade ally and exclude customer self-installed systems. Cooperative and municipal customers are outside its programs.

| Offer, 2026 | PGE customers | Pacific Power customers |
|---|---|---|
| Solar for Homes | $2,500 flat | $2,500 flat |
| Solar Within Reach (income-qualified) | $0.90 per watt, to $5,500 | $0.90 per watt, to $5,500 |
| Battery Storage for Homes | $400 per kWh, to $5,000 | $320 per kWh, to $4,000 |
| Battery storage, income-qualified | $520 per kWh, to $6,500 | $440 per kWh, to $5,500 |

The Oregon Department of Energy's Solar + Storage Rebate Program paid $0.20 to $0.50 per watt for standard-income households and $1.80 per watt for low- and moderate-income households, each capped at $5,000. Storage earned $300 per kWh to $2,500. Both required an ODOE-approved contractor. The program reopened June 15, 2026 and closed when its $1.1 million was reserved.

A hired installation on PGE or Pacific Power service therefore starts with up to $7,500 in payments against a labor bill. The materials-only route keeps the labor and loses the payments, and the two are compared on the same equipment list. Whichever route is taken, the added value is exempt from property tax under ORS 307.175 while the exemption lasts.

**Code**

```
The federal residential clean energy credit has ended.
  No credit for expenditures made after December 31, 2025, an expenditure being made when the original installation is completed.
  Source: 26 U.S.C. 25D(h) and 25D(e)(8)(A), as amended by Public Law 119-21.

A net metering facility is exempt from property tax.
  The value added by a net metering facility or a system primarily designed to offset onsite electricity use is exempt, for tax years beginning through July 1, 2029.
  Source: ORS 307.175(2) and (4); Oregon Laws 2011, chapter 656, section 4(3), as amended through 2023.
```

## 22.9 Permits and the electrical code

**Simple**

Every solar and battery system takes an electrical permit, and a roof array takes a structural permit as well. The electrical code's rules for solar exist for the firefighter on the roof and the electrician at the panel. One switch outside the house has to bring the roof wiring down to a safe voltage within half a minute. Panels keep making power as long as the sun is on them, and a switch at the ground cannot stop that. The rule is met by electronics on each panel that cut its output when the switch is thrown. Oregon adopted a new edition of the electrical code on October 1, 2026.

**Applied**

1. Apply for the electrical permit and the structural permit together, with the one-line diagram, the array layout and the rack maker's load data.
2. Put microinverters or optimizers on every module, so each shuts down at the roof.
3. Mount the rapid-shutdown initiator outdoors with the service disconnect, and label it.
4. Bond the array's equipment grounding conductors to the house grounding electrode system, with any added grounding electrode conductor 6 AWG copper or larger.
5. Put the PV disconnect, the battery disconnect and the source directory at the service equipment.
6. Keep every rooftop box and disconnect out of the fire pathways.
7. Call the inspector for the rough-in before the conduit is covered, and for the final with the labels in place.
8. Keep the inspection record and the equipment listings in the binder for the utility application.

**Professional**

The 2026 Oregon Electrical Specialty Code took effect October 1, 2026, on the 2026 National Electrical Code with Oregon's Table 1-E amendments, which left the solar, interconnection and storage articles almost unamended. An owner may wire a residence he owns and does not intend to sell or rent, under his own permit, and that licensing exemption does not reach LP gas work. A roof array that leaves the prescriptive path, which this concrete roof does, is valued for its structural permit on the racking, rails, mounts and the labor to set them, with the modules and inverters excluded.

Rapid shutdown protects a firefighter who cuts into a roof or wall with conductors behind it. A string of modules in series produces several hundred volts of direct current in daylight, and a switch at the service cannot de-energize the string above it. Module-level power electronics meet the limit inside the array boundary by de-energizing at each module. A PV hazard control system listed to UL 3741 meets it with a string design. Oregon's single amendment extends the function to an existing array when one is added to it. Ground arrays whose conductors never enter the house, and arrays on open detached structures, fall outside the rule in the 2023 text.

Oregon declined the article's commissioning section in both the 2023 and 2026 editions, so no formal commissioning record is a code requirement here. The battery's listing, its locations and its size limits are in the residential code's energy storage section. The point of interconnection at the panel, the busbar's 120 percent rule, a supply-side connection and a listed power control system are the electrical service chapter's subject and carry its entries.

In the 2026 edition the storage article's own connection section was deleted, most battery backup now falls under the optional standby article, and the load-calculation and energy-management articles moved to Articles 120 and 130. Labeling of the shutdown switch and the source directory follows the code, and the local fire marshal's expectations for placards and access are confirmed at permit time.

**Code**

```
A PV system takes an electrical permit and a structural permit.
  Electrical components under an electrical permit; the structural permit for a non-prescriptive installation valued on racking, mounts, rails and installation labor, excluding modules and inverters.
  Source: OAR 918-050-0180(1)(b) and (2).

Rooftop PV circuits shut down to a safe voltage.
  Controlled conductors outside the array boundary (1 foot from the array) at 30 volts or less within 30 seconds; inside the boundary 80 volts or less, or a listed PV hazard control system.
  Source: NEC 690.12(B) (2023 edition, values per IAEI's summary of the section); OESC 690.12 adopts it with the existing-array clause.

Adding to an existing array brings the old array under rapid shutdown.
  A rapid shutdown function is provided for the existing system; 690.12(B)(2) does not apply to the existing system.
  Source: OESC 690.12, Table 1-E (2026 edition).

The array's grounding electrode conductor has a minimum size.
  Sized per 250.66 and not smaller than 6 AWG copper or 4 AWG aluminum, with array equipment grounding conductors bonded to the grounding electrode system.
  Source: OESC 690.47(A), Table 1-E (2026 edition).

DC arc-fault protection covers PV direct-current circuits.
  Listed PV arc-fault circuit protection on PV dc circuits on or in a building, coordinated so shutdown and arc detection do not interfere.
  Source: NEC 690.11 (2023 edition).
```

## 22.10 Interconnection, net metering and permission to operate

**Simple**

With the array connected, the meter counts power in both directions. Each month the utility bills the difference. At the two investor-owned utilities any surplus becomes a credit on the next bill at the price the house pays. In March the year resets, and unused credit goes to the utility's low-income customers. Every Oregon utility, cooperatives included, must allow this for a home-sized system. Before the inverter may send power onto the line, the utility reviews the application, inspects if it chooses, and grants permission to operate. Until then the system runs with the utility connection open or not at all.

**Applied**

1. Download the serving utility's interconnection application and standard agreement.
2. Submit the application with the one-line diagram, equipment spec sheets, the listings and the planned start date.
3. Answer the utility's completeness list within 10 business days.
4. For a cooperative or municipal utility, follow its own tariff and timelines.
5. Install a lockable, visible-break disconnect within 10 feet of the meter where the inverter output exceeds 7.2 kW AC.
6. Sign and return the interconnection agreement at least 10 business days before the planned start.
7. After the final electrical inspection, send the signed inspection record and request permission to operate.
8. Give the utility five business days' notice of the start date and wait for any inspection it requires.
9. Keep the utility breaker open until written permission arrives.
10. Each year open the utility disconnect, confirm the inverter stops exporting, and log the test.
11. Keep the agreement, the permission letter and seven years of test records in the binder.

**Professional**

Net metering law reaches every electric utility in the state. Investor-owned utilities follow the Public Utility Commission's division 39 rules. Cooperatives, people's utility districts and municipal utilities follow the statute under their own governing bodies, which set the fees above the minimum charge and the annual true-up. The statute lets a utility value excess kilowatt-hours at avoided cost, while the Commission's rules give PGE and Pacific Power customers retail-value credit, so the credit depends on the utility.

Under the Commission's rules a home array is a Tier 1 application, an inverter-based facility under the size limits in the Code block, screened against the small-generator criteria of division 82. The utility answers on completeness in three business days and on screening in ten, with approval deemed after twenty days of silence. Within three business days of a pass it says whether an inspection and an agreement are required. A failed screen opens an options meeting, a supplemental review or a Tier 4 impact study. On a shared circuit the utility may also limit aggregate generation, which no applicant can see in advance.

The rules fix the utility's review deadlines, and the queue from final inspection to the meter swap is what runs long. WattMonk and EnergyScape Renewables, two permitting services, report 6 to 12 weeks from application to permission to operate on a straightforward residential system nationally, longer with storage. WattMonk also reports that over 90 percent of applications contain errors needing revision, and that self-installed systems stall most often because no installer chases the paperwork. A complete package at submission, one-line diagram, spec sheets, listings and the signed inspection record, is the owner's answer to that. A battery inverter with a microgrid interconnect device can run the house islanded before permission, since permission covers parallel operation and export.

**Code**

```
Every Oregon electric utility must allow net metering for a home system.
  Interconnection through a standard meter registering flow in two directions, for facilities of 25 kilowatts or less, at public utilities, people's utility districts, municipal utilities and cooperatives.
  Source: ORS 757.300(1)(b), (2)(a) and (8).

The minimum monthly charge is not raised for a customer-generator.
  No fee that raises the minimum monthly charge above other customers in the rate class, unless the Commission or the governing body authorizes one after public comment.
  Source: ORS 757.300(2)(c).

Excess generation is credited to the next bill at retail.
  Excess kilowatt-hours applied as a cumulative credit at the full retail rate for each kilowatt-hour rate component; the annual cycle ends with the March billing month.
  Source: OAR 860-039-0055(1) and (2).

Unused credit leaves the account in March.
  Remaining credit at the end of the annual cycle goes to the utility's low-income assistance programs at avoided cost, with no payment to the customer-generator.
  Source: OAR 860-039-0060(1) and (2); ORS 757.300(3)(d).

A home array gets Tier 1 review on a fixed clock.
  Inverter-based facility of 50 kW generation and 25 kW export or less: screening result within 10 business days of the completeness notice, deemed approved after 20 business days.
  Source: OAR 860-039-0030(1), (3) and (4).

Tier 1 review carries no application fee.
  No application or other fee for Tier 1; Tier 2 up to $50 plus $1 per kilowatt.
  Source: OAR 860-039-0045(1) and (2).

The utility gets a visible disconnect at the meter.
  A lockable load-break switch showing open or closed, readily accessible, within 10 feet of the meter, waived for inverter systems of 7.2 kW AC or less on 240-volt single-phase service.
  Source: OAR 860-039-0015(2) and (2)(a)(A).

Equipment is certified to the interconnection standards.
  IEEE 1547 (2018) and IEEE 1547.1 (2020) for installation and operation; UL 1741 Third Edition Supplement SB (2021) for Tier 1 and Tier 2 eligibility.
  Source: OAR 860-039-0015(1) and 860-039-0020(1).

After approval the utility may require only limited tests.
  An annual disconnection test confirming the inverter stops delivering power, manufacturer tests, IEEE 1547 post-installation tests, and tests after a major component changes model; written records kept seven years.
  Source: OAR 860-039-0050(3) and (4).
```

## 22.11 Problems and solutions

**Simple**

Nearly every solar trouble in Oregon starts with a system sized for the summer meeting its first December. The panels made a surplus in July, the battery sat full by noon, and in the dark weeks the generator ran every other day. A second cause is cold. A battery in an unheated shed stops charging below freezing, in the same weeks the sun is weakest. The third is paperwork. A finished system can sit idle for months waiting on a utility that never received a complete application. Each has a fix, and most of the fixes cost less before the pour than after.

**Applied**

| Problem | What you see | What to do |
|---|---|---|
| Winter starvation | Generator starts daily from November to February | Size the battery and generator from the December PVWatts figure, tilt the array 45 degrees, shift loads to midday |
| Cold battery refuses charge | State of charge stays low on sunny cold days, the charger shows no current | Move the pack indoors, or heat the enclosure to 41 to 50 °F with the sensor on the pack |
| Battery heater drains the bank | Shed heater runs all night in December | Put the pack inside the conditioned envelope |
| Phantom loads empty the battery overnight | Morning state of charge lower than the load list predicted | Meter every always-on device, move the strays off the critical panel |
| Plain grid-tied array goes dark in an outage | Sun on the roof, no power in the house | Add the battery inverter with a microgrid interconnect device |
| Permission to operate stalls | Final inspection passed, no letter from the utility for months | Submit the one-line, spec sheets, listings and signed inspection record together, then call the interconnection desk every two weeks |
| Generator will not start | Clicking or slow cranking, or a gummed carburetor after a quiet year | Float-charge the starter battery, run under load monthly, burn propane |
| Trees grow into the sun path | Pathfinder trace shows new shading at mature height | Keep the mature-height shadow lines on the site plan, plant low species south of the array, or buy a recorded solar easement |
| Ballast crushes the roof insulation | Low spots and ponding at rack feet on the protected-membrane roof | Check foot loads against the insulation's compressive strength, spread them on pavers, keep drains clear |
| Adding panels triggers the old array | Inspector requires rapid shutdown on the first array too | Put module-level electronics on the first array from the start |
| Solar gate dies in winter | Gate battery flat under fog or tree-filtered light | Add a second panel and a larger battery |

**Professional**

Most rows of the table share a mechanism. Array output falls to a fifth or a third of its summer value in December while heating load peaks, and anything sized to the annual average meets that month short. A Vermont household's record of 10 to 15 generator starts a month through the coldest quarter is the pattern, and that household's move to grid service was its answer. Cold charging compounds it, because the pack's charge cutoff holds through the same weeks.

A self-installed system stalls at permission to operate because no installer of record chases the utility, so the owner does. The off-grid gate at the driveway, whose design is in the site-development chapter, fails the way the house would at the scale of one panel and one small battery. Gate kits in this climate therefore get a panel larger than the kit's rating.

## 22.12 The outage plan and future power

**Simple**

When the line goes dead, the battery inverter opens the connection to the utility within a fraction of a second. The house keeps running on its own, though not all of it. The well pump, the ventilation fan, the refrigerator and freezers, the controls and a few lights run on the battery all night. The heat pump runs when the sun or the battery can carry it, and the concrete holds its warmth for days in between. The range, the dryer and the car charger wait for the grid. Years from now the panels and the battery will be replaced, and the array may grow. The roof, the conduit and the panel keep room for that.

**Applied**

| Tier | Loads | Where they land |
|---|---|---|
| 1, always | Well pump, freeze protection, refrigerator and freezers, ventilation, controls, network, egress lighting | Critical-loads panel, battery day and night |
| 2, when the battery allows | Heat pump, heat-pump water heater, circulators, main living and kitchen lights | Critical-loads panel, scheduled by state of charge and daylight |
| 3, grid only | EV charging, range, dryer, shop circuits, decorative and exterior lighting | Main panel, off during an outage |

1. Build the critical-loads panel from the tier table and label it.
2. Set the inverter to shed Tier 2 at a low state of charge and restore it in daylight.
3. Run a 2-inch spare conduit with a pull string from the panel to the roof zone, and a second to the ground-mount site.
4. Reserve two breaker spaces in the main panel for the array and the battery.
5. Leave room on the roof zone and in the battery room for a second pack and more modules.
6. Connect an electric vehicle as backup only through a listed bidirectional charger, interconnected as a battery is.
7. Write the outage plan into the binder, with the backed-up loads, the manual overrides, and the hours each source runs them.
8. Test the plan once a year by opening the main breaker, and log what ran and for how long.

**Professional**

A critical-loads panel lets a smaller battery and inverter carry the loads that matter, while whole-home backup needs continuous and surge capacity for the heat pump and the car charger as well. Which to build is a capacity decision, not a code requirement, and spare panel space defers it. The continuous mechanical load is near 45 watts of ventilation plus circulators and transformers, with the heat pump as the discretionary load and the mass releasing stored heat while it is shed.

Oregon's amendment to the optional standby article lets a dwelling manage automatically connected load by hand instead of by an energy management system. Monitoring of state of charge, load status and temperatures during an outage is in the smart-home chapter, and the outage drill for the mechanical plant is in the HVAC chapter.

Oregon's solar-ready provisions bind a new dwelling built without a renewable system or an active permit for one, and a house permitted with its array meets them in the building. Their raceway is sized for one future circuit. The 2-inch spare conduit exceeds it because a second circuit pulled later through an empty conduit costs a pull string's worth of labor, while one cut through cured concrete costs a core drill and a patch.

Bidirectional chargers for vehicle-to-home use are listed as their own equipment and interconnect under the same articles as a battery. In 2026 the hardware ran $2,000 to $7,300 before installation.

**Code**

```
A new dwelling without an array is built solar-ready.
  A 4-by-4-inch metal junction box within 24 inches of the main panel, a 3/4-inch nonflexible metal raceway with pull string to a capped roof termination or the attic, marked "RESERVED FOR SOLAR".
  Source: ORSC R324.7.2 and R324.7.3 (2023 edition).

The main panel reserves space for a future array.
  Space for a dual-pole breaker for solar and a second dual-pole breaker, labeled "RESERVED FOR FUTURE SOLAR", unless a renewable energy system is installed or permitted with the dwelling.
  Source: ORSC R324.7.4 and R324.7.2 Exception 1 (2023 edition).

An electric vehicle may power the house temporarily.
  Use of an owner's or occupant's electric vehicle to power the dwelling, parked in a garage or outdoors, per the vehicle manufacturer's instructions and the Electrical Code.
  Source: ORSC R329.10 (2023 edition).
```

## Who decides what

| Decision | Who decides | When, or what triggers it |
|---|---|---|
| Grid-tied hybrid or off-grid | Jon | After the serving utility's written extension quote and the three-way comparison |
| Days of battery autonomy, and the generator-start threshold | Jon | At the load list, before equipment is priced |
| Array size, tilt and location (roof, ground or pole) | Jon, from the load list, the PVWatts runs and the Pathfinder reading | At the site plan, when the solar envelope is locked |
| AC-coupled component stack, microinverters or optimizers | Jon | Before the one-line diagram is drawn |
| Roof load design for the array, embed grid or ballast weight, and the deck reinforcing around the embeds | Engineer of record, with the rack maker's engineering data | At structural design, before the roof shop drawings |
| Ballast layout and wind design for the rack | Rack manufacturer's engineering, reviewed by the engineer of record | At array design, from the site wind speed and exposure |
| Mature tree heights for the shading model | Arborist or OSU Extension, by species | At the Pathfinder reading |
| Energy model with and without the passive measures | Energy modeler or HVAC designer | After orientation, glazing and shading are final |
| Trade-ally installation or owner installation | Jon | After a trade-ally bid and a materials price on the same equipment list |
| Interconnection tier, inspection, agreement and permission to operate | Serving utility | Application after the one-line diagram; permission after the final electrical inspection |
| Cooperative or municipal net-metering terms | The utility's governing body | At application |
| Fire-service labeling and access beyond the code's minimum | Local fire marshal or building official | At permit time |
| Generator model, ventilation airflow and clearances | Generator manufacturer's data, the installer | At equipment selection |
| Propane tank size, placement and setbacks | Licensed LP installer, with the fire marshal on local amendments | At site plan, from the fuel-reserve calculation in the resilience chapter |
| Acceptance of an interlock kit or a transfer switch | Local electrical inspector | Before the kit is bought, per the electrical service chapter |

## Open items

- **2026 electrical code text.** Unknown: the 2026 NEC's section numbers and wording for rapid shutdown (690.12), PV arc-fault protection (690.11), the busbar rule (705.12), the power control system section (705.13) and the storage disconnect (706.15 and 705.20). Answered by: the 2026 NEC read-only text through an NFPA account, read against Table 1-E. Assumed meanwhile: the 2023 numbers and values, with the Oregon amendments quoted from the 2026 table.
- **Arc-fault threshold.** Unknown: the dc voltage at which 690.11 requires PV arc-fault protection. Answered by: the 2026 NEC text. Assumed meanwhile: that a microinverter array has no dc circuit the section reaches.
- **2026 residential code numbers.** Unknown: whether R324 and R329 keep their numbers and values in the 2026 Oregon Residential Specialty Code. Answered by: the Building Codes Division's 2026 summary of amendments or the integrated codebook. Assumed meanwhile: the 2023 text, usable on a permit through March 31, 2027.
- **Propane tank setbacks.** Unknown: the current NFPA 58 edition's separation table, the 2,000-gallon bracket, and any local amendment. Answered by: the NFPA 58 text or the LP installer's reading of it, and the fire marshal. Assumed meanwhile: 10 feet for 125 to 500 gallons and 25 feet for 501 to 1,000 gallons, from two secondary tables that agree.
- **Generator shed ventilation.** Unknown: NFPA 37's ventilation requirement in square inches or CFM for the chosen engine. Answered by: the generator manufacturer's enclosure data sheet, and NFPA 37 if purchased. Assumed meanwhile: the manufacturer's airflow figure governs the vents.
- **Battery enclosure design.** Unknown: the insulation value and heater wattage that hold a pack above freezing in an outbuilding at the parcel's design temperature, and their cost. Answered by: a heat-loss calculation for the chosen shed and pack. Assumed meanwhile: the pack sits inside the conditioned envelope and the question does not arise.
- **The serving utility.** Unknown: whether the parcel is served by PGE, Pacific Power or a cooperative, and that utility's net-metering tariff, queue time and circuit limits. Answered by: the parcel. Assumed meanwhile: the Commission's rules for an investor-owned utility.
- **Line-extension comparison.** Unknown: the parcel's written extension quote and the three-way cost result. Answered by: the serving utility's quote and the load list, run through the three-way comparison. Assumed meanwhile: a grid-tied hybrid.
- **Incentives in the install year.** Unknown: Energy Trust's 2027 offers, whether the state rebate program reopens, and whether a trade-ally bid less the payments beats a materials-only install. Answered by: the programs' pages in the install year and two prices on the same equipment list. Assumed meanwhile: no payment reaches an owner-installed system.
- **Energy model.** Unknown: the array and battery sizes with and without the passive measures. Answered by: an hourly energy model of the final design, run twice. Assumed meanwhile: an array sized to the annual load list and a battery sized to the autonomy days.
- **Dispatch estimate.** Unknown: daily fuel burn and generator run hours in a partial-cloud winter, and the autonomy days Jon chooses. Answered by: the generator's fuel curve, the load list and the December PVWatts figure, after equipment selection. Assumed meanwhile: a propane standby generator at about twice the inverter's continuous rating.
- **PVWatts for the parcel.** Unknown: the parcel's own monthly table, and the central and eastern Oregon figures the demonstration key could not fetch. Answered by: a PVWatts run at the parcel's coordinates. Assumed meanwhile: the Salem figures as the valley planning case.
- **Fire-service expectations.** Unknown: the local fire marshal's placard and access requirements beyond the code's pathways and labels. Answered by: the fire marshal at permit time. Assumed meanwhile: the residential code's pathways and the electrical code's labels.
- **Ballast on the protected-membrane roof.** Unknown: the rack foot load the roof's insulation and pavers can carry. Answered by: the roof design and the insulation's compressive strength, in the roof chapter. Assumed meanwhile: ballast is feasible on the reinforced zone.
- **Incinerating toilet.** Unknown: the burn-cycle wattage of any product chosen. Answered by: the product's rating. Assumed meanwhile: a composting toilet with a fan under 3 watts.
- **Dropped from Revision 7.** The skeleton's instruction block for the Revision 7 writer, which pointed at files that no longer exist. No other Revision 7 text existed.

## Decisions this chapter records

- (decided) Battery storage is the primary backup, and a generator covers only the outage that outlasts the battery.
- (pending parcel) Grid-tied hybrid or off-grid, decided from the extension quote and the three-way comparison.
- (Jon to confirm) The battery and the generator are sized to the December PVWatts figure, not the annual average.
- (Jon to confirm) The number of days the battery carries the critical loads without sun or generator.
- (Jon to confirm) An AC-coupled component stack with separate PV and battery inverters, parts sold separately.
- (Jon to confirm) Module-level power electronics on every roof module.
- (Jon to confirm) Lithium iron phosphate chemistry, with the pack inside the conditioned envelope.
- (Jon to confirm) A propane standby generator with two-wire auto-start, sized at about twice the inverter's continuous rating.
- (pending engineer) The roof's array load, and cast-in anchors for a fixed starter array with ballast for expansion.
- (Jon to confirm) The array tilted near 45 degrees where the mount allows it.
- (Jon to confirm) Load shifting: a heat-pump water heater on a CTA-2045 controller, and well-pump filling, laundry and EV charging in the solar window.
- (pending parcel) Trade-ally installation or owner installation, from two prices on the same equipment list.
- (decided) The array's solar envelope is locked sixth in the site plan, with mature-height shadow lines.
- (Jon to confirm) A 2-inch spare conduit from the panel to the roof zone and a second to the ground-mount site.

## Records to keep

- Every dated version of the load list, with the always-on floor and the tier assignments.
- The PVWatts tables for the parcel, the Pathfinder photograph, the traced sun-path chart and the monthly shading loss.
- The three-way cost comparison with the utility's written extension quote and its date.
- The one-line diagram, equipment datasheets, listings and the array layout.
- Photographs of every embed and anchor before the pour, the rack maker's ballast or anchor design, and the engineer's load letter.
- The electrical and structural permits and every inspection record.
- The interconnection application, the signed agreement, the permission-to-operate letter and seven years of annual disconnection tests.
- The generator run log, the maintenance log by engine hours, and the LP installer's documents.
- The battery manufacturer's instructions kept at the unit, and the January capacity readings.
- Incentive applications, equipment invoices and the assessor's exemption record.
