# Chapter 6: Structural System and Concrete Design

A licensed engineer designs this structural shell, because the concrete floors and roof the thousand-year shell needs have no prescriptive path in Oregon's residential code. West of the Cascades the code's own tables stop at one story of reinforced block under a wood roof, and every above-grade concrete wall goes to the engineering standards. Cast concrete, reinforced concrete block and steel make up the shell. It is designed past the code's life-safety minimum, and detailed so that the laps, cover, grout and anchorage the calculations assume are the ones the inspector finds. Bearing values come from the soil chapter. Costs are 2026 figures unless a different year is given.

> **Jon's note.** [JON: drafted from the record, confirm or rewrite] I chose the engineered path because the shell I want has concrete floors and a concrete roof. The code's free tables give me concrete walls with wood above them. An engineer's fee buys the whole shell instead of the walls alone. I want margin above the life-safety line wherever the evidence supports it. Life safety means people get out, and I want the house repairable and lived in afterward. Nothing in the load path is wood. Where the code lets a manufacturer's stamp carry a truss or a floor joist, that is the fallback, not the plan. [JON: price solid grouting and full-height bars with the base wall, or only the code-minimum wall?] [JON: is a safe room in the plan, and which room?]

## 6.1 What the structure has to do

**Simple**

Every load on your house needs an unbroken path to the ground. Roof weight, snow, furniture and people push down. Wind and earthquakes push sideways, and the soil pushes against any wall below grade. Wind also pulls up on the roof. Each push has its own path. Roof weight goes into the walls, the walls carry it to the footings, and the footings spread it into the soil. Sideways force goes from each floor into the walls that brace it, then down. Where a wall stops short of the floor above, or a large opening cuts a floor, a path breaks. In this house every path is concrete and reinforced block from the roof to the soil.

**Applied**

1. Mark every bearing wall on the plans, with the roof and floor weight it receives.
2. Mark each floor support with its span and end conditions.
3. Mark each roof support with its eave and ridge geometry.
4. Mark the stair openings and every other hole in a floor.
5. Mark the large window and door openings, where the wall's continuity is interrupted.
6. Mark the wall lines that resist wind and earthquake, in both directions.
7. Mark where each wall line's load enters the soil.
8. Mark the utility routes through or around the structure.
9. Trace each load from where it lands to the foundation.
10. Treat any path the drawings do not show as a design gap.

**Professional**

Seven loads enter the structural calculation, and each has a source the drawings name.

| Load | Where the design value comes from |
|---|---|
| Dead load | The weights of the concrete, block, grout, finishes and fixed equipment shown on the drawings |
| Floor and roof live load | The residential code's live-load table (Code below) |
| Snow | The state ground-snow lookup, adjusted for the site's elevation, with drift checked at every roof step |
| Wind | The county's basic design wind speed, or its special-wind-region speed where the parcel falls inside one |
| Seismic | The parcel's seismic design category and the short-period spectral acceleration behind it |
| Soil and water pressure | The geotechnical report's lateral earth pressures and design groundwater level |
| Construction loads | The contractor's sequence: stacked pallets of block, grout pumps, a crane for planks, and formwork pressure |

Bearing walls stack floor over floor in one plane, and the wall lines run from foundation to roof without offsets. Each floor diaphragm ties into the walls through chord and collector steel, and a bond beam runs at each floor level and at the roof. Openings stay within the limits the path decision sets, and every footing is sized from the site's own soil values.

Such a building can be traced in section. Roof load passes to wall, floor to wall, wall to foundation and foundation to soil. Lateral force passes to the diaphragm, from diaphragm to shear wall and from shear wall to foundation. Thicker walls or slabs outside a defined load path add dead load, which raises the seismic demand, and add no capacity.

Recesses, projections and offset volumes do not trade away a prescriptive path on a western Oregon site, because the seismic category has already removed it. Inside the engineered path each offset still costs analysis and detailing. Under the residential code's irregularity conditions and under ASCE 7, an irregular building cannot use the simplest equivalent-lateral-force procedure, and each offset adds reinforcement, torsional demand and connection detailing. No percentage limit on articulation exists. Seven named conditions in the residential code define irregularity, and the engineer applies them to the actual floor plan.

**Code**

```
Floor live loads are fixed minimums.
  40 psf in living areas, 30 psf in sleeping areas, 40 psf on stairs plus a 300-pound point load, 40 psf on decks and balconies, 50 psf in garages plus 2,000-pound wheel loads.
  Source: ORSC Table R301.5 (2023 edition).
```

[FIGURE: load-path-section, a section through the house from roof to soil with the gravity path and the lateral path to each shear wall labeled]

## 6.2 Where the site puts the house: seismic category, wind and snow

**Simple**

Three numbers tied to the parcel's location decide how much of this design is engineered: its earthquake category, its wind speed and its snow load. Oregon's residential code puts the Willamette Valley, the I-5 corridor and the coast in its highest earthquake categories for houses. Most of eastern Oregon sits one step lower. Nine coastal and Coast Range counties carry a higher design wind speed than the rest of the state. Snow depends on elevation more than on region. Until a parcel is chosen, the design assumes the higher earthquake categories, because that is where most buildable western Oregon land sits.

**Applied**

1. Look up the parcel's category, wind speed and snow load on the Design Criteria Hub.
2. Keep the hub's report in the binder.
3. Near a category boundary on the code's map, run the ATC Hazards by Location tool.
4. Set it to ASCE 7-16, Risk Category II and Site Class D.
5. Read the short-period design acceleration, and record the category it falls in.
6. Check the special-wind-region figure, and use the county's special-wind-region speed inside one.
7. Read the ground snow load at the parcel's elevation.
8. Add the code's elevation adjustment where the parcel sits above the modeled elevation.
9. Record on the cover sheet which snow basis the design uses.

**Professional**

Oregon's category map and county table are the basis of the planning matrix below, and the lookup at the parcel's coordinates replaces it once a parcel exists.

| Region | Likely category | What the prescriptive tables still allow there |
|---|---|---|
| Eastern Oregon: the high desert and the Blue Mountains | C | Concrete walls under R608 within its limits, and masonry under R606 with the Category C rules |
| The Cascade Range and its inland slopes | C to D0 | R608 where the lookup returns C, one-story masonry elsewhere |
| The Willamette Valley margins and central Oregon | D0 | One story of reinforced block under a wood roof, with everything else engineered |
| Most of the Willamette Valley and the I-5 corridor | D1 | The same as D0, with the engineered path the practical default |
| The coast and parts of Lane, Douglas and Coos counties | D2 | The same, with stack bond, parapets and veneer ties under tighter rules |
| Special wind regions: nine coastal and Coast Range counties, and the Columbia Gorge | Varies | The prescriptive wind tables still cover the mapped speeds, and the engineered path takes a site-specific wind study |

Map and lookup tools agree because they draw on the same mapped ground motion, so a disagreement between them means the parcel sits on a category boundary. In Category E the design moves to the structural specialty code unless the calculation reclassifies the site to D2.

Two wind speeds appear in the county table. Every county has a basic design wind speed, and a second column applies to the parts of a county inside the mapped special wind region (Code below). In the Columbia River counties the two columns print the same speed. On the engineered path, ASCE 7 section 26.5.1 treats the mapped contour inside a special wind region as a starting value and requires a site-specific wind study by a qualified engineer.

Oregon's prescriptive snow design rests on the Structural Engineers Association of Oregon's electronic snow map, the source the residential code names. An elevation correction applies where the site stands above the map's modeled elevation. In 2025 the structural specialty code dropped that map for ASCE 7-22's national ground-snow geodatabase, read through the ASCE Hazard Tool or the Design Criteria Hub. Those values are strength-level, risk-targeted loads that cannot be compared line by line with the old map.

Per the Building Codes Division's bulletin on the change, the national average rise is near 12 percent, with some Oregon regions higher. Under ASCE 7-22 the thermal factor depends on the roof's insulation, so a well-insulated roof holds more snow in the calculation. Oregon's historic minimum roof snow load for sloped roofs went with the old map.

Statewide Alternate Method 26-01 lets a design under the 2023 residential code keep referencing the 2022 structural code through March 31, 2027. Which edition the design references is the engineer's call, recorded in the Oregon code and compliance map chapter, and the drawings state the edition and the snow basis. Ground snow from one edition is never combined with the load factors of the other. The 2022 values are allowable-stress loads and the 2025 values strength-level loads.

**Code**

```
The seismic design category comes from the code's map, verified at map boundaries by calculation.
  Figure R301.2.2.1, with boundary sites checked in the ATC hazards tool at ASCE 7-16, Risk Category II and Site Class D, and the reported SDS read against the category table.
  Source: ORSC R301.2.2.1 (2023 edition).

The short-period design acceleration fixes the category.
  Category C above 0.33g to 0.50g, D0 above 0.50g to 0.67g, D1 above 0.67g to 0.83g, D2 above 0.83g to 1.25g, and E above 1.25g.
  Source: ORSC Table R301.2.2.1.1 (2023 edition).

A site inside a special wind region uses the county's special-wind-region speed.
  120 mph in Benton, Clatsop, Coos, Curry, Douglas, Lane, Lincoln, Tillamook and Yamhill counties inside the mapped region, against basic design wind speeds of 94 to 103 mph statewide.
  Source: ORSC R301.2.1, Table R301.2 and Figure R301.2.1(1) (2023 edition).

Ground snow load comes from the state lookup, adjusted for elevation.
  The value at snowload.seao.org for the site, plus 0.007 to 0.07 psf per foot of elevation above the modeled elevation by region, with 36 psf the minimum for prescriptive design.
  Source: ORSC R301.2.3.1 and Table R301.2.3.1 (2023 edition).

Nonprescriptive design has its own minimum roof snow load.
  25 psf of roof snow, except where the load is determined under Section 1608 of the Building Code.
  Source: ORSC R301.2.3.1 (2023 edition).

Ground snow over 70 psf takes the structure out of the prescriptive chapters.
  Masonry and concrete construction follows the prescriptive chapters at 70 psf or less and is designed under R301.1.3 above it.
  Source: ORSC R301.2.3 (2023 edition).
```

## 6.3 The design-path decision

**Simple**

You can have this house designed two ways. For $4,000 to $10,000 an engineer designs exactly the house you want, concrete floors and roof included. Or you follow the code's pre-approved tables for free. On a western Oregon site they allow a single story of reinforced block under a wood roof and over wood floors. Every element the tables do not cover goes to the engineer anyway. Here that means the concrete floors, the concrete roof and every wall under them. This house takes the engineered way, because the thousand-year shell needs the concrete floors and roof.

**Applied**

1. Choose the path before the floor plan is fixed.
2. Take the engineered path wherever a floor or the roof is concrete.
3. Take the prescriptive path only for one story of block under a wood roof.
4. Retain a licensed Oregon structural engineer.
5. Order the geotechnical report before the structural design starts.
6. Give the engineer the design-criteria report, the footprint and the element list below.
7. Have the engineer mark each element's path on the drawings.
8. Hold that assignment through construction.
9. Submit the stamped drawings, the calculations and the special-inspection program with the permit application.

**Professional**

| Path | What it is | Where it fits | Where it is unavailable |
|---|---|---|---|
| Prescriptive | The code states the rule and the design stays inside its limits | Ordinary geometry inside the residential tables, Category C sites, one-story single-wythe masonry, conventional spans | Above-grade concrete walls outside Category C, masonry more than one story tall or under a concrete diaphragm in D0 to D2, concrete or masonry floors and roofs, oversized openings, irregular plans |
| Engineered | A licensed engineer designs and stamps the structural drawings under R301.1.3 | Most Oregon sites west of the Cascades, any nonstandard element, long spans, concrete floors and roofs | Nowhere, because it is the universal fallback |
| Alternative method | The building official approves a method that meets the code's intent by another route | Tested assemblies, FRP reinforcement, owner-made block, each subject to approval | Where the official does not accept the showing |

Three documents carry the engineer's stamp. They are the structural drawings (plans, sections, details and schedules), the calculations behind them, and the special-inspection program the engineered design invokes. A geotechnical engineer signs the soil report the foundation design rests on. By occupancy the house stays under the residential code throughout. Engineering the walls does not move the permit, the inspections or the certificate of occupancy to the structural specialty code. Only the design method becomes nonprescriptive. Under R301.1.3 and R301.2.2.5 it references the structural code's standards: PCA 100 or ACI 318 for above-grade concrete walls, and R608 only for a detached dwelling in Category C.

| Element or condition | Path on a D0 to D2 site | The rule behind it |
|---|---|---|
| Above-grade concrete walls | Engineered under PCA 100 or ACI 318 | R301.2.2.5, with R608 open only to detached dwellings in Category C |
| Masonry walls more than one story tall, or over 9 feet between lateral supports | Engineered under TMS 402 | R606.12.3.1, the wall system chapter's entry |
| Masonry walls under a concrete or hollow-core floor or roof | Engineered | R606.12.1.1 assumes wood or cold-formed steel diaphragms |
| A second story of any kind on a masonry wall | Engineered | Table R606.12.2.1 lists it as not permitted without design |
| Elevated concrete floors and roofs | Engineered under ACI 318 | No residential prescriptive section exists |
| Two-wythe loadbearing walls | Engineered | R606.13 gives bonding rules, and R606.12.3.1 still requires design in D0 to D2 |
| Irregular buildings | Engineered for the irregular story or portion | R301.2.2.6 |
| Ground snow over 70 psf | Engineered | R301.2.3 |
| Retaining walls over the code's height and load triggers | Engineered | R404.4 |
| Footings on fill, on soil the official judges under the clay value, or at bearing above the presumptive table | Engineered, or a soils investigation | R401.2 and Table R401.4.1, footnote b |
| Expansive soil | Designed under Section 1808.6 of the Building Code | R403.1.10 |
| Post-tensioned or prestressed elements | Engineered | No prescriptive provision |
| FRP reinforcement | Engineered, and GFRP excluded in D0 to D2 | ACI 440.11 |
| Steel beams under concrete floors | Engineered, or manufacturer-stamped where the jurisdiction accepts it | Local practice |
| A mezzanine over one-third of the room below | Counted as a story | R325.3 |

Four elements need no engineer on any site. R608 concrete walls qualify at a Category C site inside R608.2's limits. One story of masonry qualifies with the code's minimum reinforcement and no more than 9 feet between lateral supports. Footings qualify on the presumptive bearing values. Manufacturer-engineered trusses and I-joists qualify because their stamp is the engineering. Concrete floors or a concrete roof on any of them remove the exemption, because the prescriptive masonry and concrete sections assume light-frame floors and roofs above.

Massing choices are priced inside the engineered path, not as the loss of a free path. On a western Oregon site the seismic category has already removed the free path, so a recess or an offset volume costs analysis and detailing rather than a change of path. GFRP bar is a different case. Seismic category excludes it from the shell outright, because the bar is linearly elastic to failure and supplies none of the post-yield redistribution the higher categories assume (Code below). Even at a Category C site the structural walls, as the seismic force-resisting system, would exclude it.

Weighting durability as heavily as the load path does not change the path. Targeted stainless bar and a water-retaining structure designed to ACI 350 need an engineer regardless, and GFRP is unavailable in the likely categories. All three refine the material specification inside whichever path is chosen. One exception is narrow. Where an element qualifies for the prescriptive path on load grounds alone but carries a severe exposure class, it can tip toward engineered treatment. Prescriptive cover and mix assumptions were not written for severe exposure.

| Element | Engineered path | Prescriptive path on a D0 to D2 site |
|---|---|---|
| Foundation | Engineered from the geotechnical report, with concrete or reinforced masonry stem walls | Footings from Table R403.1 on presumptive bearing values, with the Category D footing reinforcement |
| Above-grade walls | Engineered concrete under ACI 318 or ACI 332, or reinforced masonry under TMS 402, two wythes permitted | One story of single-wythe reinforced block with the code's minimum reinforcement, or R608 concrete walls at a Category C site |
| Wall ties | Stainless, by the engineer's schedule | None for a single wythe |
| Floor system | Hollow-core precast planks or a cast-in-place one-way slab | Wood I-joists or open-web wood trusses, manufacturer-stamped |
| Roof system | A concrete deck with a protected membrane, or a concrete deck under standing-seam metal | Wood trusses under standing-seam metal roofing, manufacturer-stamped |
| Wall height | Per the design, commonly 9 to 10 feet in the rooms | 9 feet between lateral supports |
| Stories | Per the design | One |
| Diaphragm openings | Engineered, with chord and collector steel | Under the irregularity threshold |
| Fire performance | Concrete and masonry assemblies throughout | Concrete or block walls with wood floor and roof assemblies, rated where the code requires |
| Long-life alignment | The full concrete shell | Concrete walls and foundation, with floors and roof on shorter wood cycles |

**Code**

```
Irregular buildings leave the prescriptive seismic provisions for the irregular story or portion.
  Shear-wall offsets out of plane or in plane, floor or roof edges without lateral support, offset floor levels, and shear walls or braced lines not in two perpendicular directions.
  Source: ORSC R301.2.2.6 (2023 edition).

A large floor or roof opening between braced wall lines, or wood bracing in a masonry story, is also an irregularity.
  An opening over the lesser of 12 feet or half the least floor or roof dimension, or a story braced partly by wood or steel framing and partly by masonry or concrete walls.
  Source: ORSC R301.2.2.6 (2023 edition).

Prescriptive concrete walls under R608 are limited to low seismic categories, two stories and light-frame floors and roofs.
  Detached dwellings in Category A, B or C, two stories, a 60-foot plan, 32-foot floor and 40-foot roof spans, 10 psf floor and 15 psf roof dead loads, and 136 mph in Exposure C.
  Source: ORSC R608.2 (2023 edition).

A masonry wall under a second story is not a prescriptive element in Seismic Design Category D0 to D2.
  Solid wall length of 25 percent of the plan dimension in D0 and D1 and 30 percent in D2 for a one-story wall, and no prescriptive wall under a second story of any kind.
  Source: ORSC Table R606.12.2.1 (2023 edition).

Prescriptive story height is capped by wall material.
  Masonry 13 feet 7 inches of story and 12 feet of bearing-wall clear height, 8 feet more at a gable end, and ICF walls 11 feet 7 inches of story with 10 feet unsupported.
  Source: ORSC R301.3 (2023 edition).

GFRP reinforcing bar is excluded from the high seismic design categories.
  All members in Category A, members outside the seismic force-resisting system in B and C, no structural member in D, E or F, and under ICC-ES AC454 only A and B.
  Source: ACI 440.11-22; ICC-ES AC454.
```

## 6.4 Concrete walls

**Simple**

Poured concrete walls are steel bars inside a solid slab of concrete stood on edge. Bars take the pulling forces concrete cannot, and concrete protects the bars and carries the pushing forces. Three things decide how long it lasts: the concrete over the steel, the density of the mix, and where the shrinkage cracks open. Concrete shrinks as it dries, so a long wall cracks somewhere. Control joints are straight grooves cast into both faces that tell the crack where to be. Below ground, each joint gets a rubber or plastic strip cast across it, so water cannot follow the crack through the wall.

**Applied**

1. Have the engineer set control-joint spacing from wall height, reinforcement and restraint before forming.
2. Place a joint at every change in wall height or thickness, and at offsets and intersections.
3. Place joints beside openings, never through them.
4. In any wall that holds back water, cast a waterstop across each joint.
5. Seal the exposed groove of every joint with backer rod and sealant.
6. Check each wall's bar and joint spacing against its exposure class before the permit set.

**Professional**

ACI 318-19 is the general structural concrete code and the edition the 2023 residential code references, with ACI 318-25 now in circulation. ACI 332-20 is the residential concrete code. It holds prescriptive tables for footings, foundation walls, slabs on ground and above-grade walls within its scope, and a chapter on design for expansive soils. PCA 100-17 is the prescriptive manual the residential code names for above-grade concrete walls outside Category C, and it requires an explicit showing of compliance with its own tables. R608, the code's prescriptive section for above-grade concrete walls, assumes light-frame interior walls, floors and roofs. Planning values for an engineered exterior wall on this house are in the table below.

| Parameter | Planning value |
|---|---|
| Wall thickness | 8 inches minimum, 10 to 12 inches for taller walls or higher seismic demand |
| Concrete strength, f'c | 3,000 psi minimum, 4,000 psi for above-grade exterior walls, 5,000 psi for retaining walls and other high-stress elements |
| Reinforcing grade | Grade 60 to ASTM A615, or ASTM A706 low-alloy bar where seismic ductility governs |
| Vertical bars | No. 4 or No. 5 at 12 to 24 inches on center, two curtains in thicker walls |
| Horizontal bars | No. 4 at 12 to 24 inches on center, two curtains in thicker walls |

### Control joints and crack control in long walls

Tooled or formed into both faces, the groove of a control joint weakens the plane so the shrinkage crack forms there instead of at random. Vertical joints go at 2 to 3 times the wall height, with an outer bound near 10 to 12 feet for residential wall heights. That spacing comes from the Bureau of Reclamation's 2016 joint-spacing reference and the trade practice built on ACI 224R. Wall height, reinforcement ratio, restraint and expected shrinkage strain set the actual spacing, which the engineer fixes.

Joints also go where stress concentrates regardless of spacing: changes in wall height or thickness, offsets and intersections, beside window and door openings, and re-entrant corners.

Joints and shrinkage steel do two different jobs and are set together. Distributed horizontal bars do not prevent shrinkage cracking. They limit the width of the cracks that form between joints by spreading the strain across many fine cracks. Joint layout sets where the wall relieves its stress, and bar spacing sets how wide each crack opens. Closer bars and closer joints trade against each other in one calculation. ACI 318-19 controls flexural crack width through the bar-spacing limit of section 24.3 rather than a calculated width. ACI 224R-01 lists guide crack widths by exposure, from dry air to water-retaining service, and is the durability reference behind those spacing limits.

Every control joint is a deliberate discontinuity and a potential leak path. In a wall that resists water, which means a below-grade foundation wall, a retaining wall or a cistern wall, each joint takes a PVC, rubber or bentonite waterstop cast into it. Backer rod and sealant close the exposed groove so surface water cannot track to the bar. Above grade on a dry wall, a tooled or formed joint without a waterstop is the standard detail.

Exposure class is assigned wall by wall. Sustained ground contact or wind-driven rain can give one wall a more severe class than the rest of the house. Its bar spacing and joint layout are then checked against that class rather than against the house-wide table. At any wall classed severe, the shrinkage-and-temperature steel is checked against the concrete code's minimum distributed-steel ratios (Code below).

**Code**

```
Cast-in-place walls carry minimum distributed reinforcement in both directions.
  0.0012 longitudinal and 0.0020 transverse of the gross concrete area for deformed bars No. 5 and smaller with 60,000 psi yield, and 0.0015 and 0.0025 for other deformed bars.
  Source: ACI 318-19 Table 11.6.1.

Concrete foundation walls under above-grade concrete walls are engineered in the high seismic categories.
  In Category D0, D1 or D2 such walls follow ACI 318, ACI 332 or PCA 100, and plain walls under light framing stay within 8 feet of height and 4 feet of unbalanced backfill.
  Source: ORSC R404.1.4.2 (2023 edition).
```

[FIGURE: control-joint-waterstop, plan and section of a formed control joint in a below-grade wall, with the cast-in waterstop and the sealed groove]

## 6.5 Alternative forming systems and mixes

**Simple**

There is more than one way to form and mix a concrete wall. Here the default is rented or job-built forms that come off after the concrete cures. Stripped forms can be reused, and the bare face can be inspected before anything covers it. Each alternative changes one variable. Foam forms stay in the wall and double as insulation. Flowable mixes fill the forms without vibration. Tensioned cables replace some ordinary bar in a long floor span. Fibers in the mix control the fine early cracks. Fly ash or slag in place of some of the cement makes a denser mix that hardens more slowly. It is the mix this house uses.

**Professional**

| Option | What it changes | Trade-off against the default |
|---|---|---|
| Insulated concrete forms (ICF) | Stay-in-place foam forms combine formwork and continuous insulation in one trade sequence | The product line fixes the wall thickness and insulation value, and the foam stays in the wall, so the concrete face cannot be stripped and inspected |
| Self-consolidating concrete (SCC) | Superplasticizer admixtures, not added water, produce a mix that flows around congested reinforcement with little or no vibration | Higher cost per yard from the cementitious content and admixture dose, and formwork still designed for full hydrostatic pressure |
| Post-tensioned slab | Unbonded tendons stressed after cure pre-compress the slab, increasing clear span for a given depth over mild-steel reinforcement | Specialized stressing crews and equipment, and any future penetration risks cutting a stressed tendon |
| Fiber-reinforced concrete | Fibers in the mix control plastic-shrinkage cracking and improve impact and abrasion resistance | Supplementary only, because fibers do not replace primary reinforcement |
| SCM-rich low-carbon mix | 20 to 50 percent cement replacement with fly ash or slag densifies the pore structure and reduces embodied carbon | Slower strength gain, with 7 to 14 days of curing before stripping or loading against 3 days for a standard mix |

Self-consolidating concrete removes the vibration-skill dependency behind honeycombing in congested cages. Denver Concrete Vibrator's technical summary records it consolidating in ICF and other congested-reinforcement walls where stiffer mixes left voids. It does not reduce form pressure. It stiffens slowly during placement, so the form design assumes the full-hydrostatic case. Post-tensioning is not among the five floor options. Hollow-core precast and cast-in-place slab cover its span range without stressing crews, and a stressed tendon constrains every future penetration through the slab.

ICF is established in low-rise residential and disaster-resistant construction, as PNNL's Building America Solution Center guide records. Here it trades the default's direct surface inspection and reusable forms for a single combined forming-and-insulation step. This house's specified durability mix is the SCM-rich one. Its replacement rate densifies the pore structure and gives the largest cut in the mix's embodied carbon, because portland cement production is the dominant carbon dioxide source in concrete.

## 6.6 Reinforced masonry walls

**Simple**

Reinforced block walls are concrete block stacked in mortar with steel inside. Vertical bars run up through the hollow cores, and horizontal bars run along channel-shaped courses called bond beams. Every core that holds a bar is then filled solid with grout, a soupy concrete that locks the bar to the block. Together they make a grid of steel and concrete that does not burn, rot or feed insects. In an earthquake the steel holds the blocks together, and the bond beams hold each wall to its floors and roof. On most western Oregon sites the engineer designs this wall, because the code's tables end at one story.

**Applied**

1. Lay the block in running bond, each unit overlapping the one below by half.
2. Use stack bond only where the engineer designs it.
3. Grout solid every cell that holds a bar.
4. Grout the whole stem wall solid where the drawings call for it.
5. Run bond beams at the foundation top, at every floor and at the roof.
6. Add a mid-height bond beam in any wall taller than 12 feet.
7. Use open-end or cut-web units at every bond-beam course, so the horizontal bars run continuous.
8. Leave a cell open for a niche only where the engineer marks it on the wall schedule.
9. Never run a niche through a bond-beam or joint-reinforcement course.

**Professional**

On an engineered wall TMS 402 governs the design and TMS 602 the construction. Oregon's 2023 residential code references the 2016 editions of both, and the 2022 editions are current, so the drawings name the edition the engineer designed to. The table lists the planning values an engineered block wall starts from here.

| Parameter | Planning value |
|---|---|
| Wall thickness, nominal | Eight-inch block for bearing walls, ten- or twelve-inch block for taller walls or higher seismic demand |
| Mortar | Type S portland cement-lime, with Type M the higher-strength option for severe exposure |
| Grout | ASTM C476 fine or coarse, 2,000 psi at 28 days, placed at 8 to 11 inches of slump |
| Reinforcing grade | Grade 60 to ASTM A615, or ASTM A706 where seismic ductility governs |
| Vertical bars | No. 5 at 2 to 4 feet on center, by wall height and seismic category |
| Bond beam bars | Two No. 5 continuous in each bond-beam course |
| Lap length, planning | 48 bar diameters, 30 inches for a No. 5 bar, with the engineer's schedule governing |
| Joint reinforcement | 9-gauge ladder type every other course, for crack control |

In Seismic Design Category D0 to D2 the code's prescriptive masonry path is narrow. R606.12 applies the seismic requirements to masonry and leaves anchored veneer out of them. One-story walls within the code's limit between lateral supports can be built to the minimum reinforcement without design, on a wood or cold-formed steel diaphragm, and the wall system chapter states that entry. Everything taller, and everything under a concrete floor or roof, is designed under TMS 402. Figures R606.11(1) to (3) show the anchorage and reinforcement details by category. Masonry cement and Type N mortar are barred from the lateral force-resisting system because both give the wall less strength and less bond than the permitted mortars (Code below).

| Bond beam location | Purpose |
|---|---|
| Top of the foundation wall | Ties the foundation steel to the wall steel above |
| Top of the wall at each floor level | Anchors the floor diaphragm and transfers lateral load into the wall |
| Top of the wall at the roof | Anchors the roof structure or roof diaphragm |
| Mid-height course in a wall over 12 feet tall | Crack control and stiffness |
| Above and below large openings | Carries the forces that concentrate around the opening |

Running bond is the default coursing for this house. Stack bond aligns the units and leaves the head joints continuous, so no unit overlap interrupts a vertical crack. For that reason the code adds horizontal steel in any wall laid with less than a quarter-unit head-joint offset, and more of it in Category D2. Joint reinforcement at the spacing in the table already meets the lower of those rules without change.

On the prescriptive minimum, only the cells with bars are grouted, and the cells between bars stay hollow. Those are the only candidates for deliberate use as a storage or display niche. No niche may interrupt a bond-beam course or a joint-reinforcement course. Its clean placement is a pocket bounded above and below by those courses and on each side by grouted, reinforced cells. Bars concentrate at openings, corners and bond-beam intersections, so the as-designed layout controls and the engineer confirms candidate cells from the wall schedule. Where the house adopts solid grouting of every cell, no open cell remains.

**Code**

```
Masonry bearing walls have a minimum thickness.
  8 inches nominal for bearing walls more than one story high, and 6 inches for solid masonry walls of one-story dwellings and garages.
  Source: ORSC R606.4.1 (2023 edition).

Masonry walls in Seismic Design Category D0 or D1 carry minimum reinforcement in both directions.
  Steel totaling 0.002 of the gross section with at least 0.0007 in each direction, at 48 inches maximum in solid-grouted open-end or full-head-joint hollow units and 24 inches in other masonry.
  Source: ORSC R606.12.3.2 (2023 edition).

The minimum bar at the maximum spacing is fixed by wall thickness.
  No. 5 at 48 inches each way for an 8-inch wall (0.183 square inch per foot total, 0.064 each way), No. 4 for a 6-inch wall, No. 6 for 10- and 12-inch walls.
  Source: ORSC Table R606.12.3.2 (2023 edition).

Shear-wall reinforcement spacing tightens with wall size.
  Vertical and horizontal bars at the smallest of one-third the wall length, one-third the wall height or 48 inches, with vertical steel at least one-third of the shear steel, hooked around the vertical bars.
  Source: ORSC R606.12.3.2.1 (2023 edition).

Mortar in the lateral force-resisting system is restricted in the high seismic categories.
  Type M or S portland cement-lime or mortar cement in D0, D1 and D2, with Type N mortar and masonry cement excluded from that system.
  Source: ORSC R606.2.8.3 and R606.12.3.4 (2023 edition).

Masonry laid in stack bond takes added horizontal steel.
  0.0007 of the vertical cross-section in bed joints or bond beams spaced 48 inches or less, wherever head joints offset less than a quarter of the unit length.
  Source: ORSC R606.3.7.2 (2023 edition).

Stack bond in Seismic Design Category D2 takes more steel and solid grout.
  0.0015 of the gross section at 24 inches maximum outside the lateral force-resisting system and 0.0025 at 16 inches within it, solid grouted in open-end units or two wythes of solid units.
  Source: ORSC R606.12.4.1 and R606.12.4.2 (2023 edition).

Anchor bolts in hollow masonry sit in grouted cells.
  The cells in the courses receiving the bolt are grouted solid.
  Source: ORSC R606.11 (2023 edition).
```

## 6.7 Wall ties and mixed metals

**Simple**

In a cavity wall, short steel ties cross the gap and hold the brick to the block. Each tie carries a few square feet of brick against wind and shaking, and it spends its whole life in a damp cavity. Two different metals touching in wet mortar pass an electric current between them, and the more reactive one corrodes to protect the other. Zinc coating wired to bare steel is eaten away doing that, and the protection it was bought for is gone. This house uses one metal per wall, bars, chairs and tie wire included, and stainless steel wherever any stainless is used.

**Professional**

What a tie does depends on the wall's classification, and the classification is written on the drawings by name. Anchored veneer carries only its own weight and passes wind and seismic load to the block through the ties. Noncomposite (cavity) walls share the lateral load between the wythes in proportion to their stiffness. Composite walls act as one section through ties or headers designed for shear across the collar joint.

On this house the cavity-wall alternative is read as anchored veneer unless the engineer classifies it otherwise. Its veneer tie schedule, the corrosion-protection minimums and the code's cavity limits are stated in the wall system chapter. For a wall the engineer classifies as noncomposite, the residential code's multiple-wythe rules at R606.13.2 set the values in the table below.

| Tie type in a noncomposite cavity wall | Wall area per tie | Maximum spacing |
|---|---|---|
| Rigid 3/16-inch wire ties | One per 4-1/2 square feet | 24 inches vertical and 36 inches horizontal, with added ties around openings at 3 feet, within 12 inches of the opening |
| Adjustable ties | One per 2.67 square feet | 24 inches each way, with 1-1/4 inches of bed-joint offset at most, 1/16 inch of play, and two 3/16-inch pintle legs |
| Joint reinforcement cross wires, No. 9 gage or heavier | One cross wire per 2.67 square feet | 16 inches vertical |

TMS 402 bars drip bends in wire ties, because the bend lowers the tie's lateral capacity, so the flashing and weeps handle the water that reaches the ties. Stainless ties at the schedule's frequency form point thermal bridges over 0.5 to 1 percent of the wall area. That bridging drops a 4-inch rigid-foam cavity from R-26 to R-23 effective. Thermally broken ties (Halfen FM, Bekaert Murfor THERM, Wagner ThermaTIE) recover most of that loss where the thermal target needs it.

### Mixed metals in one element

Galvanized and black steel in electrical contact inside one element form a documented galvanic couple. Per the American Galvanizers Association, once the zinc has depassivated in the concrete's alkaline pore water it acts as a sacrificial anode for the adjacent bare steel. It is consumed protecting that steel, which defeats the reason the galvanizing was specified. Where mixing cannot be avoided, a dielectric barrier goes at the contact point. Tie wire matches the bar, 16.5-gauge or heavier galvanized wire on galvanized bar and stainless wire on stainless bar.

Stainless against carbon steel is a milder couple. Per the Specialty Steel Industry of North America's stainless rebar guidelines, the coupled corrosion rate is low enough that distress is unlikely within a 75-year design life. Some current practice therefore no longer isolates black bar from stainless. This house's design horizon runs past that 75-year study horizon, so the all-stainless rule stands.

### Glass-fiber bar and composite ties

GFRP bar as primary reinforcement is excluded from this shell by seismic category. In the narrow case of an element outside the lateral system at a Category C or lower site, its detailing differs from steel's throughout. Composite-Tech, a composite-industry vendor, puts development lengths at 1.3 to 1.6 times steel's for a comparable force in its explainers. It puts tension laps at 1.3 times the development length under ACI 440.1R-15, with 40 to 60 bar diameters common in practice, and bond resting on sand-coated or helically wrapped surfaces. Those are a vendor's planning figures, and the engineer details any GFRP element against the ACI 440.11-22 text itself, hooks included.

FRP ties are an engineered alternative, not a prescriptive option. ICC-ES AC125 covers externally bonded FRP for strengthening, not new ties. AC454 covers FRP bars in concrete in Seismic Design Category A or B. TMS 402-22 Appendix D introduces composite reinforcement for masonry partition walls, not for loadbearing exterior cavity walls. Any commercial FRP tie enters a permit only with a current ICC-ES report and the building official's approval under the code's alternative-materials provision.

## 6.8 Reinforcement detailing: laps, cover, hooks and grout

**Simple**

Steel strengthens concrete only where the two are joined over enough length, and only while the concrete keeps water off the bar. Where one bar ends and the next begins, the two overlap for a set length. Force passes from one to the other through the concrete between them. Each bar also needs a set thickness of concrete between it and the weather, called cover. In a block wall the grout does both jobs, so it has to fill every cell completely. Most field mistakes are small and permanent: a bar settled against the form, a lap a few inches short, a cell with a void. Checks before each pour catch them while they can still be fixed.

**Applied**

1. Measure bar size and spacing against the drawings, bay by bay, before concrete is ordered.
2. Measure cover with a rule or a cover meter.
3. Expect 3 inches against earth, 2 inches on exposed faces and 1-1/2 inches inside.
4. Measure every lap and hook.
5. Check that laps are staggered where the drawings stagger them.
6. Chair horizontal bars every 2 to 4 feet on plastic or concrete chairs sized to the cover.
7. Put no metal chair at an exposed face.
8. Tie every other crossing at least, and every crossing where the crew will walk.
9. Walk the cage for bent or stepped-on bars after the last trade leaves it.
10. Check embeds and sleeves against the structural and mechanical drawings for conflicts with the bars.
11. Have a second person sign the checklist.
12. Photograph the final condition before calling for concrete.
13. Send field congestion to the engineer as a request for information.
14. Substitute no bar on site.

**Professional**

Detailing is what lets the reinforcement develop the strength the design assumes, and a short lap, lost cover or a missing hook invalidates the calculation at that point. ACI 318-19 section 25.4 and TMS 402's development provisions are the engineering basis of the lap values below, and the engineer's schedule on the drawings governs over them.

| Detail | Planning value |
|---|---|
| Lap length, No. 5 bar in 8-inch block at an f'm of 2,000 psi | 48 bar diameters, 30 inches |
| Lap length, No. 4 bar in the same wall | 48 bar diameters, 24 inches |
| Footing-to-stem-wall dowel | A 90-degree standard hook at the footing bottom, 14 inches into the stem wall, as the foundation chapter details |
| Grout strength | 2,000 psi at 28 days |
| Grout slump | 8 to 11 inches, the upper end for self-consolidating fine grout |
| Bar size on this house | No. 4 and No. 5 throughout, with No. 6 at isolated heavy locations |

Inspectors verify the placement at the footing inspection, the foundation-wall inspection and, for grouted block, before each grout pour. Field placement fails in five recurring ways, each with a known control.

| Failure | How it happens | Control |
|---|---|---|
| Lost cover | Chairs undersized, crushed by foot traffic or concrete weight, or omitted, so bars settle toward the form face, and carbonation and chloride reach the steel sooner than the cover was sized to allow | Plastic or concrete chairs at the specified cover, and cover measured before the pour |
| Congestion | Bars, dowels, embeds and bond-beam steel converging at wall-footing intersections, corners and openings, blocking aggregate and the vibrator | Bar-to-bar clearance checked against the maximum aggregate size at the detailing stage, and field congestion sent to the engineer as a request for information |
| Wrong laps | Laps shorter than the development length, or stacked at one location instead of staggered, concentrating a weak, congested zone at one section | Laps located away from maximum-moment regions on the drawings, never moved in the field |
| Displaced bars | Foot traffic, placement equipment and the pour pushing bars off position | Chairs at close spacing, ties at every other crossing or every crossing in traffic, and a pre-pour walk for bent bars |
| Wrong supports | Chairs sized close to the cover instead of to it, or metal chairs at an exposed face, which become corrosion initiation points | Plastic or concrete-block (dobie) chairs sized to the exact cover |

Post-installed adhesive anchors correct a missed dowel or anchor bolt, and the governing document is product-specific. Hole size, embedment, cleaning and dispensing come from the product's ICC-ES evaluation report and the manufacturer's printed instructions it references, never from a generic embedment ratio. Simpson Strong-Tie SET-3G (ESR-4057) is listed for post-installed anchors and reinforcing-bar connections in cracked and uncracked concrete under static, wind and seismic load. Hilti HIT-RE 500 V3 (ESR-3814) is the equivalent system. Using the wrong drill-bit diameter, or skipping the hole cleaning, voids the tested capacity even where a generic ratio is satisfied. Reports are revised on renewal, so the crew works from the one current at installation.

This house's bar schedule tops out at No. 5, with No. 6 at isolated heavy locations. Manual benders are rated to No. 6 or heavier by model, and manual cutters stop near No. 4. Powered cutter-benders rated to No. 6 or 1-inch bar cut and bend faster at foundation-schedule volume. Rent against buy is decided from the final bar schedule's total footage and local rental rates.

**Code**

```
Grout is placed in lifts with limits on height and timing.
  Lifts of 8 feet maximum, placed within 1-1/2 hours of mixing water, consolidated during placing and reconsolidated after the excess water is absorbed, with pours over 8 feet placed in 64-inch lifts under special inspection.
  Source: ORSC R606.3.5.1 (2023 edition).

Cleanouts open the bottom course of tall pours.
  Where the building official requires them, cleanouts at the bottom course for each pour over 64 inches, spaced 32 inches or less in solid-grouted masonry, sealed after inspection and before grouting.
  Source: ORSC R606.3.5.2 (2023 edition).

Reinforcement in masonry keeps a minimum cover.
  Joint reinforcement 5/8 inch from an exposed face, other bars one bar diameter and not less than 3/4 inch, and 2 inches where exposed to weather or soil.
  Source: ORSC R606.3.4 (2023 edition).

Cast-in-place concrete keeps a minimum cover over its bars.
  3 inches cast against ground, 2 inches exposed to weather or ground for No. 6 and larger bars, 1-1/2 inches for No. 5 and smaller, and 3/4 inch in walls and slabs not exposed.
  Source: ACI 318-19 Table 20.5.1.3.1.

Post-installed anchors and dowels follow their evaluation report.
  Hole diameter, depth, cleaning method and dispensing equipment per the product's current ICC-ES report and the instructions it references, with SET-3G listed for 2,500 to 8,500 psi concrete under ESR-4057.
  Source: ICC-ES ESR-4057; ICC-ES ESR-3814; ORSC R301.1.3 (2023 edition).
```

## 6.9 Formwork, placement defects and cast-in embeds

**Simple**

Fresh concrete behaves as a heavy fluid until it stiffens. It presses outward on the forms, it traps air unless it is vibrated, and it bonds poorly to concrete that has already begun to set. Most placement defects trace to one of those three facts. Honeycomb is a pocket where the mortar never filled between the stones. Cold joints are the weak seams left where a late truck met concrete that had started to harden. Blowouts start at a form tie that let go near the bottom of the pour, where the pressure is highest. Form design, vibration method and delivery timing are the fixes, and all three are settled before the first truck arrives.

**Applied**

### Consolidation and placement

1. Limit free fall to 3 to 4 feet.
2. Use a drop chute or tremie pipe for taller forms.
3. Insert the vibrator on a grid pattern, a few inches into the lift below.
4. Hold each insertion 5 to 15 seconds, until the large bubbles stop rising.
5. Withdraw the vibrator slowly.
6. Keep the vibrator off the form face.
7. Stop before paste rises to the surface.
8. Learn the mix's initial-set time for the day's temperature before the pour.
9. Keep truck intervals inside that window.
10. Stage a backup vibrator, and on a pump pour a backup pump.
11. When a lift must stop, stop at a planned construction joint.
12. Roughen the joint, and dowel or bond it as the drawings show.
13. Treat any bulge in a form as a stop-work signal.

### Forms, before the pour

1. Use a manufactured forming system.
2. Set tie spacing from the maker's pressure tables for the pour rate and concrete temperature.
3. Tape, gasket or tight-fit every panel joint.
4. Space the ties tightest at the base of the pour, where the pressure is highest.
5. Brace the panels to the ground or to a finished slab with kickers and diagonals.
6. Walk every brace before the truck arrives.
7. Slow the pour rate in cold weather.

### Embeds and anchor bolts

1. Wire anchor bolts, or a template holding several, to the tied reinforcement.
2. Never fasten a bolt to the forms.
3. Check the bolt layout against the sill-plate drawing just before the pour.
4. Recheck bolt position and top-of-concrete elevation as the last truck finishes.
5. Check every embed plate against the structural drawing's location, elevation and orientation.
6. Run a written embed, sleeve and dowel checklist against the structural and mechanical drawings.
7. Have a second person check it before calling for concrete.
8. Photograph the final pre-pour condition of every embed.

**Professional**

Fresh concrete loads a vertical form with a lateral pressure equal to the lesser of two values. One is full hydrostatic pressure, the unit weight times the pour height. The other is a reduced value that depends on how fast the mix stiffens. Faster placement and colder concrete both raise the design pressure. ACI 347R, the formwork guide, contains the pressure formulas. ACI Committee 347 recommends a factor of safety of 2.0 on form ties, as the For Construction Pros series by KB Engineering reports. Exact coefficients sit in the purchased guide, and the forming system maker's published tables are the working reference on site.

Blowouts are tie failures far more often than panel failures. One tie under-specified or over-spaced for the actual pressure lets go near the base of the pour. Its load shifts to the neighboring ties, and the failure unzips upward. Bulging means the tie-and-wale system is consuming its safety margin. Misalignment traces to external bracing that transfers horizontal thrust poorly, so the whole form assembly walks during the pour instead of deflecting and springing back.

Honeycomb, the stony pockets where mortar failed to fill between coarse aggregate, has five documented causes in Graniterock's technical notes on surface defects:

- congested reinforcement in narrow forms
- segregation from excessive free fall
- a fine-to-coarse aggregate ratio that leaves too little mortar
- a mix too stiff to flow around the bars
- consolidation that levels the concrete without finishing the release of trapped air

Sand streaking, a sand-rich and cement-poor smear on the formed face, comes from bleed water migrating up the form face and washing out paste. An air-entrained mix bleeds less and streaks less. Cold-joint prevention is scheduling. Retarders extend the set window in hot weather, accelerators shorten it in cold weather, and the delivery interval is planned around the window the day's mix has.

Where an anchor bolt is missed despite the checklist, a post-installed anchor corrects it. Sill-plate anchor rules, footing reinforcement and the grounding electrode cast into the footing are stated in the foundation chapter, on its pre-pour list. Missing or misoriented embed plates cost more, because a plate is a unique engineered connection, and correcting one means cutting and doweling new work rather than substituting an anchor. A missed bolt and a misplaced plate are both documented as corrections, never planned as practice.

## 6.10 Openings: lintels and diaphragm continuity

**Simple**

Every opening cuts a path the loads were using, and something has to carry them around it. Over a window or door, a lintel does that. It can be a steel angle, a precast concrete beam, or a block course filled with grout and bars. Its ends must rest far enough onto solid, grouted block to pass the load down. Stair openings do the same thing to a floor, and a floor also works as the house's horizontal earthquake brace. Bars cut by the opening are replaced around its edges. Past a certain size, one hole puts the whole story into engineered design.

**Applied**

1. Have the engineer size every lintel in the block wall from the load above it.
2. Bear each lintel at least 4 inches on cells grouted solid.
3. Set each bearing in a full mortar bed.
4. Run the bond beam's bars past each opening for the development length the drawings give.
5. Add the trim, diagonal and chord bars around each slab opening before the pour.
6. Keep stair openings under the irregularity threshold.
7. Past it, have the engineer design the story's diaphragm with chords and collectors.

**Professional**

Masonry over an opening rests on a lintel of steel, reinforced concrete or reinforced masonry, or on an arch, each designed for the load it carries (Code below). CMHA's Lintel Design Manual TR91B tabulates load-rated spans for precast lintels and for grouted lintels built of U-shaped units, and its TEK 14-08B states the bearing minimum that TMS 402 sets.

Bearing ends land on solidly grouted cells. How many jamb cells are grouted, and whether the jamb takes bars, follows from the lintel's end reaction. A 10-foot-class opening, the garage or barn door case, carries roof, wall and snow load that puts the lintel past a nominal angle and into a sized steel member or a published-table masonry lintel. Steel-angle lintels under the brick veneer have their own span table in the residential code, stated in the wall system chapter.

In a cast-in-place slab diaphragm, the bars the opening interrupts are replaced beside it, half above and half below the opening at the slab edges. Two No. 5 diagonal bars at each corner, lapped 4 feet into the uninterrupted slab, are the engineer's typical corner detail. Continuous chord steel of No. 5 at minimum runs along the opening's edge with a 40-bar-diameter lap, and the slab keeps its minimum reinforcement ratio throughout. ACI 318-19's slab and diaphragm provisions govern those details.

In a block wall, a bond beam interrupted by an opening takes supplementary bars developed on each side of it, two No. 5 at minimum with a 48-bar-diameter lap. Continuous bars above and below the opening extend 24 inches past its edges. Past the irregularity threshold, the story's diaphragm is designed with collector and chord reinforcement in place of a trim detail.

**Code**

```
Masonry over an opening bears on a designed lintel or arch.
  A steel lintel, a reinforced concrete or masonry lintel, or a masonry arch, designed to support the load imposed.
  Source: ORSC R606.10 (2023 edition).
```

## 6.11 Floor systems

**Simple**

Floors here can be concrete poured in place, factory concrete planks craned into position, concrete over steel, or factory-engineered wood. Concrete floors last as long as the walls and need the engineer. Wood floors are the low-cost prescriptive route and have the shortest life. For the engineered shell the default is hollow-core plank. Planks are factory-cast concrete slabs with round voids through them. A crane sets them, and a thin layer of poured concrete on top ties them together. Bare concrete floors are loud underfoot in the room below. Floating a finish floor over a resilient mat fixes that without touching the structure.

**Applied**

1. Size a cast-in-place slab early at a depth of span over 24.
2. Size hollow-core at span over 40.
3. For a 24-foot span, plan a 12-inch cast-in-place slab or an 8-inch hollow-core plank.
4. Confirm crane access and delivery turning room for planks before the floor system is fixed.
5. File the wood joist or truss maker's evaluation report and span tables with the permit.
6. Over any occupied room, specify a floating finish floor on a resilient underlayment.

**Professional**

| Path | Description | Strengths | Limits |
|---|---|---|---|
| Cast-in-place reinforced concrete one-way slab | A 6- to 10-inch slab on bond beams or steel beams, No. 4 or No. 5 bars in two directions to the ACI 318 minimums, continuous into the walls | Highest mass, longest design life, the best fire and sound performance, one material with the walls | Significant formwork, engineered design, long pours |
| Hollow-core precast planks with a 2- to 3-inch topping | 6- to 12-inch planks, designed and stamped by the manufacturer, with a cast-in-place topping for diaphragm continuity | Fast erection, comparable longevity, the industry standard for concrete houses, spans of 16 to 32 feet | Engineered for the project and stamped by the maker, with crane and delivery access required |
| Composite concrete on metal deck over steel beams or bar joists | A 3-1/2- to 6-inch topping on composite deck, on W-section beams or bar joists | Long spans, easy mechanical chases, reasonable cost | Steel enters the structural shell, with a 50- to 75-year structural design life as drawn |
| Manufacturer-engineered wood I-joists | 9-1/2 to 16 inches deep, to the maker's span tables, continuous over bearing walls or beams | Lowest cost, fast install, the maker's stamp carrying the engineering | Wood, with a shorter design life and vulnerability to fire and water |
| Manufacturer-engineered wood floor trusses | 12 to 24 inches deep, open web, designed and stamped by the maker | Long spans, integrated mechanical chases, the maker's stamp | Wood, with the same vulnerabilities as I-joists |

For the engineered shell, hollow-core precast is the primary path at spans of 16 to 32 feet. Cast-in-place one-way slab is the alternative at shorter spans, where single-material formwork is simpler than a crane day. Behind the planks stands the PCI Manual for the Design of Hollow Core Slabs and Walls, the industry design manual, and the maker's stamped shop drawings and erection sequence go in the permit file. Elevated structural slabs are designed under ACI 318-19's slab chapters, never under the slab-on-ground provisions of ACI 332-20.

On the prescriptive path, wood I-joists or open-web wood trusses are the default. Their maker's product evaluation report and span tables go in with the permit, and the stamp does the engineering.

Bare concrete slabs perform poorly against footfall. Commercial Acoustics' and AcousPlan's rating guides put a bare 4-inch reinforced slab near Impact Insulation Class 25 and a bare 8-inch slab near 28. Footsteps on an unfinished concrete floor are therefore audible in the room below. Floating the finish floor on a resilient underlayment of rubber, cork or a rated acoustic mat decouples the walking surface from the slab, and the interiors chapter selects that assembly with the finishes. Under a hard finish a resilient mat reaches a class of 50 to 60, and underlayment plus carpet 65 to 75. Each product publishes the points it adds over the bare slab.

**Code**

```
On the prescriptive masonry path, the floor and roof diaphragms are wood panels on wood or cold-formed steel framing.
  Wood structural panels fastened to wood framing per Table R602.3(1), or to cold-formed steel floor or roof framing per Tables R505.3.1(2) and R804.3, with blocked panel edges.
  Source: ORSC R606.12.1.1 (2023 edition).
```

## 6.12 Roof structure

**Simple**

Your roof is two things with two lifespans. Its structure should last as long as the walls. Its weather surface is replaced two or three times in a century. Keeping them separate means the second never damages the first. On a concrete deck the membrane comes off and goes back on without touching the structure. Oregon's roof collapses on record broke at the connections under drifted snow, not in the framing. That is why the connections get the engineer's attention here.

**Applied**

1. Have the engineer check snow drift at every parapet, valley and roof step.
2. Slope a concrete deck at least 1/4 inch per foot to its drains.
3. Give each drained area an overflow.
4. On the truss option, read the required uplift from the code's table.
5. Select a connector rated at or above it.
6. Where the house deck meets a separate structure's metal roof, run an expansion joint from roof to foundation.
7. Raise an 8-inch curb at the joint on the roof.
8. Cast in anchor plates for future solar racking, or plan ballasted racks.

**Professional**

| Path | Description | Design life of the structure | Design life of the weather surface | Fit |
|---|---|---|---|---|
| Concrete deck with a protected membrane roof (PMR) | An 8-inch cast-in-place slab or hollow-core with a 2- to 3-inch topping, a fully adhered modified-bitumen, EPDM, TPO or PVC membrane, 4 to 6 inches of XPS or polyiso above it, and river-rock or paver ballast | 100 years and more | 30 to 50 years for the membrane, replaceable without disturbing the structure | The primary roof, engineered |
| Concrete deck under a sloped wood-framed false roof | The same deck, with treated sleepers carrying a 3:12 to 6:12 frame under metal or slate | 100 years and more | 50 to 70 years for 24-gauge standing seam, 75 to 150 for natural slate | The alternate where slope is wanted, engineered, at higher cost |
| Wood truss roof on the bond beam | Manufacturer-engineered trusses at two-foot spacing, bearing on the bond beam | 50 to 80 years for the truss assembly | 50 to 70 years for metal, 15 to 30 for asphalt shingle | The prescriptive option, with the maker's stamp carrying the engineering |

Asphalt shingles are rejected on both paths, because a 15-to-30-year surface does not belong on a shell with a multi-century life. Flat concrete decks slope to drains at every low point and carry an overflow wherever a parapet could trap water. ASCE 7-16 section 8.4 is the ponding-instability check. Assembly, parapet and edge detail, and the drainage design are stated in the roof system chapter. Future solar racking on a concrete deck is either cast-in anchor plates set at design time or ballasted racks on the finished membrane roof. Ballasted racks add no penetrations, and their foot loads are checked against the insulation's compressive strength.

On the truss option the code's uplift table lists the force each truss-to-wall connection must resist, by wind speed, exposure, spacing, span and pitch. At or under the table's threshold the standard fastening schedule serves without a rated connector. Above it, a load-rated tie is selected from the maker's evaluation report. Every Oregon county's design wind speed falls within the table's range, so catalog hardware meets the demand outside the special wind regions. Inside one, or anywhere on the engineered path, the connection design moves to the engineer with the rest of the roof.

### Oregon snow failures on record

Three documented collapses in Oregon set the design lesson. In December 2008 an east Multnomah County warehouse failed with 3 to 5 feet of drifted snow at the parapets and 2 to 3 feet over the field, and 24 trusses came down. Rad, Afghan and Lewis's 2018 forensic report from Portland State University found four causes. Load exceeded the design value, drift piled against tall parapets beyond the design assumption, and construction defects were present. Each failing truss then shed load to its neighbor, and the collapse progressed. Of the failed trusses, 18 failed at connection welds and 6 by concrete breakout at the connection.

In November 2014 a northern Oregon manufacturing plant lost 80,000 square feet of a 400,000-square-foot roof under snow, freezing rain and temperatures near minus 20°F. StructureMag's article on the collapse records it. In 2025 North Medford High School's gymnasium roof collapsed under a reported 350 tons of snow, per KOIN and KGW.

Concrete decks have no truss connections to fail. On the truss option the connections sit inside the maker's stamped design, against the site's ground snow load from the lookup. Drift is checked at every parapet, valley and roof step in the actual geometry, because the 2008 collapse followed drift beyond the design assumption.

### Where a concrete deck meets a metal roof

Where the main house's concrete deck meets a standing-seam metal roof over an attached but structurally separate garage or shop, an expansion joint is standard. Nystrom's roof-to-roof joint guidance and the IIBEC Ohio Valley fact sheet on roof decks each name two conditions that require it. Both are present here, a change of deck material and a heated building meeting an unheated one.

Such a joint runs from rooftop to foundation with parallel structural elements on each side, so each section moves on its own. A roof-level cover alone does not decouple the two structures. At roof level the detail is a raised curb with a flexible cover spanning the gap. Whether the wall-to-wall connection needs the same full-height treatment is set when the attachment is designed.

Gutters, downspouts and any first-flush diverter fail by freezing while full of water, not by structural overload. Their sizing and freeze protection belong to the rainwater-catchment design. Ice dams at the eave trace to roof heat loss rather than to the structure. Snowmelt adds to the annual catchment yield on a delayed schedule, at lower peak flow than rain.

**Code**

```
Truss and rafter connections resist the tabulated wind uplift.
  Uplift per connection from Table R802.11 by basic design wind speed from 110 to 140 mph, exposure, spacing, span and pitch, with the standard fastening schedule allowed at 200 pounds or less.
  Source: ORSC R802.11 and Table R802.11 (2023 edition).

The standard fastening schedule also serves a steep, modest roof in light wind.
  Basic wind speed of 115 mph or less, Exposure B, a pitch of 5:12 or steeper, a span of 32 feet or less, and spacing of 24 inches or less.
  Source: ORSC R802.11 (2023 edition).

A flat roof drains at each low point and overflows wherever water could be trapped.
  Overflow drains the size of the primary drains with inlets 2 inches above the low point, or scuppers three times the drain size and at least 4 inches high, sized under the Plumbing Code.
  Source: ORSC R903.4 and R903.4.1 (2023 edition).
```

## 6.13 Service layer and story classification

**Simple**

Service layers are hollow spaces between floors that carry the pipes, wires and ducts. Oregon's code sorts any such space by its height and by how people get into it, and the sorting decides which rules apply. Reached through panels, a shallow sealed space is a concealed space. Tall enough to walk into, with a ladder and lights, it is a story in its own right. Anything in between is argued over at plan review, and the argument slows the permit. This house uses one of the two clean cases and nothing in between.

**Professional**

Oregon's residential code defines a story from floor surface to floor surface and sets its own rules for habitable space, under-floor space, concealed space and mezzanines (Code below). By its clear height and its access, a service layer falls into one of them.

| Classification | What it is | Consequence |
|---|---|---|
| Habitable space | Space used for living, sleeping, eating or cooking | The ceiling-height, light, ventilation, escape and heating rules apply, so a service layer is never classified habitable |
| Under-floor or crawl space | Space below the lowest occupied floor, entered through a sized access opening | Ventilation or conditioned-crawl provisions, a ground vapor retarder, no heating |
| Concealed space | Space that is not occupied and is entered only for inspection or maintenance | Fireblocking and draftstopping where the construction is combustible, and the mechanical code's material limits where it serves as a return-air plenum |
| Mezzanine | An intermediate level within a room, under the code's area limit | Part of the room below, not a separate story |

Where a service layer is large enough for a person to enter, some building officials classify it as a mezzanine, an attic or a story. That classification is argued case by case. Two classifications avoid the argument. Under 30 inches clear and reached only through removable panels, a concealed plenum has no story consequence. At 4 feet clear or more, with ventilation, lighting and a permanent ladder or stair, a conditioned mechanical level is counted and designed as a story. Those two heights are the plan's own thresholds, not code numbers, and the house picks one of the two.

**Code**

```
A story runs from the top of one floor to the top of the floor or roof above.
  The portion of a building between the upper surface of a floor and the upper surface of the floor or roof next above, with the topmost story ending at its ceiling or roof.
  Source: ORSC R202 (2023 edition).

Habitable space has a minimum ceiling height.
  7 feet for habitable space, hallways and the parts of basements containing them, and 6 feet 8 inches for bathrooms, toilet rooms and laundry rooms.
  Source: ORSC R305.1 (2023 edition).

A mezzanine stays part of the room below within height and area limits.
  7 feet clear above and below the mezzanine floor, and an aggregate area not over one-third of the room's floor area, one-half in a sprinklered dwelling.
  Source: ORSC R325.2 and R325.3 (2023 edition).

Under-floor spaces have a sized access opening.
  18 by 24 inches through a floor, or 16 by 24 inches through a perimeter wall, with an areaway of the same size where the wall opening is below grade.
  Source: ORSC R408.4 (2023 edition).

Fireblocking and draftstopping apply to combustible construction.
  Fireblocking cuts off concealed draft openings between stories and at the roof in wood-framed construction, and draftstops limit a concealed floor-ceiling space to 1,000 square feet.
  Source: ORSC R302.11 and R302.12 (2023 edition).
```

## 6.14 Concrete durability and mix discipline

**Simple**

Concrete fails over decades for two main reasons. Water reaches the steel and rusts it, and rust takes up more room than steel, so it cracks the concrete from inside. Freeze and thaw cycles pry at any water trapped in the pores. Long-life concrete counters both. Its mix holds less water, plus fly ash or slag that keeps filling the pores for years. Its steel gets more concrete over it, and its curing runs a week or two instead of three days. One trade-off comes with the dense mix. In a fire it can spall, because steam cannot escape through it, and a small dose of plastic fibers gives the steam a way out.

**Applied**

1. Ask the concrete supplier for the aggregate source's alkali-silica service record and any test reports.
2. Order an ASTM C1567 test on the actual aggregate, cement and SCM dose.
3. Run it before the mix design is final.
4. Raise the SCM dose or change the SCM where the test result requires it.
5. File the result in the binder with the mix submittal.
6. Have the engineer assign each element's exposure class from the geotechnical report.
7. Show the classes on the drawings.
8. Specify polypropylene monofilament fibers in the fire-exposed structural elements the engineer names.

**Professional**

ACI 318-19 organizes concrete durability by exposure class, and the mix parameters scale to the most severe class an element carries.

| Exposure | Classes | Concern |
|---|---|---|
| Freeze-thaw | F0 none, F1 moderate, F2 severe, F3 severe with deicing salts | Frost damage in saturated freeze-thaw cycling |
| Sulfate | S0 to S3 | Sulfate attack on the cement paste |
| Water | W0, W1 in contact with water, W2 where low permeability is required | Permeability and water transmission |
| Corrosion | C0, C1, C2 severe with chlorides | Reinforcement corrosion in chloride environments |

Above grade in mild exposure, an Oregon long-life house takes F1, S0, W0 and C1. Below grade in contact with soil that may be aggressive, it takes F1 or F2, S1, W1 or W2, and C1 or C2 by the chloride exposure. Footings and below-grade walls are the elements that can reach the severe classes, and their classification comes from the geotechnical report's soil and groundwater chemistry. Above-grade walls take the mild baseline.

Two elements are classified separately at design time. Exterior-exposed slab edges sit closer to the below-grade condition than to the interior baseline, and any water-retaining structure is classified on its own. Severe classes do not by themselves call for corrosion-resistant bar. ACI 318-19's class system is calibrated for uncoated steel, with mix and cover as the primary protection. Coated or stainless bar is an added layer where the measured chloride exposure makes mix and cover insufficient for the target life, as the durability chapter sets out.

### The five mechanisms

Carbonation is atmospheric carbon dioxide reacting with the alkaline hydration products and lowering the pore-fluid pH. When the carbonation front reaches the bar, the passive oxide film that protects steel at high pH breaks down and ordinary corrosion begins. Its rate scales with permeability, so a low-w/c, well-cured mix slows it. Chloride ions diffuse through the pore structure. At a threshold concentration at the bar they break down the passive film locally, even without carbonation, and the pitting that follows is harder to detect than uniform corrosion. Low w/c and SCM densification slow the diffusion, and added cover lengthens the path.

Sulfates from soil or groundwater react with calcium aluminate hydrates to form expansive ettringite and gypsum, which crack the paste from within. That attack is on the paste, not the steel, and Type II or V cement or SCM replacement is the response for the S1 to S3 classes. In alkali-silica reaction, cement alkalis react with reactive silica in some aggregates to form a gel that absorbs water and expands. Map cracking is the classic symptom, and the reaction is aggregate-specific.

Freezing water expands near 9 percent, and the hydraulic pressure fractures paste over repeated cycles. Entrained air voids give the expanding water relief space, which is the air-content requirement in the F1 to F3 classes. In the field the mechanisms couple: freeze-thaw cracking opens new chloride paths, so measured deterioration runs faster than the single-mechanism rates.

| Parameter | Standard residential concrete | Long-life target on this house |
|---|---|---|
| f'c at 28 days | 2,500 to 3,000 psi | 4,000 psi minimum, 5,000 psi for severe exposure |
| Maximum w/c ratio | 0.55 | 0.45, and 0.40 for severe exposure |
| Air content where freeze-thaw exposed | 4 to 6 percent | 5 to 7 percent |
| Cement type | I/II | I/II with supplementary cementitious materials |
| Supplementary cementitious materials | Optional | 20 to 30 percent Class F fly ash (ASTM C618) or 30 to 50 percent slag (ASTM C989) |
| Cover to reinforcement | Code minimum | Code minimum plus 1/2 inch for severe exposure |
| Curing | 3 days | 7 days minimum, 14 days for SCM mixes |

Fly ash, slag and silica fume reduce permeability over time, raise chemical resistance and lower the heat of hydration. They also slow setting and strength gain, which the construction schedule plans around.

### Verifying the aggregate against alkali-silica reaction

Alkali-silica control is tested on this house's materials, never assumed. ASTM C1567 is an accelerated mortar-bar test of the actual aggregate, cement and candidate SCM dose together, read against the standard's expansion threshold (Code below). Shafaatian and others' 2013 study of fly ash in that test put the minimum effective replacement at 15 to 35 percent by ash source. The mechanisms were alkali dilution and binding, reduced transport and altered gel chemistry. That range sits largely inside the fly ash and slag replacement the mix already specifies, and the overlap is not proof for this house's materials. Where the test requires a higher dose or a different SCM, the mix specification changes to match.

### Fire spalling, the dense mix's trade-off

Heated concrete generates internal vapor pressure as pore water vaporizes, and a low-permeability concrete cannot vent it fast enough, so a surface layer detaches violently. NIST's overview of high-strength concrete at high temperature and the 2022 critical review of fire spalling in high-strength concrete both record explosive spalling in the 250 to 400°C range. Permeability is the governing variable in both, and both find that raising the w/c ratio reduces the risk, the opposite direction from every other durability rule.

This house's 4,000-to-5,000 psi, 0.40-to-0.45 w/c, SCM-densified mix is therefore the susceptible profile. Fire exposure matters at a structural element under sustained fire that must still carry load afterward, meaning the structural walls and any structural floor or roof slab.

Polypropylene monofilament fibers at low dosage, in the low single-digit pounds per cubic yard, are the documented mitigation. They melt in fire and leave fine channels that vent the vapor gradually. That is a separate application from shrinkage-control fibers, no substitute for any reinforcement, and specified for the fire-exposed structural elements the engineer names.

**Code**

```
Every structural member is assigned exposure classes, and its mix follows the most severe one.
  Freeze-thaw F0 to F3, sulfate S0 to S3, water W0 to W2 and corrosion C0 to C2, each class setting a maximum w/cm, a minimum f'c, an air content and cementitious limits.
  Source: ACI 318-19 sections 19.3.1.1 and 19.3.2.1.

An aggregate, cement and SCM combination passes the accelerated mortar-bar test below a fixed expansion.
  0.10 percent expansion at 16 days after casting, measured on the project's own aggregate, cement and SCM dose.
  Source: ASTM C1567.
```

## 6.15 Fiber reinforcement: what it may and may not do

**Simple**

Fibers mixed into concrete are short strands of steel or plastic spread through the whole batch. They hold closed the fine cracks that open in the first days, and they toughen a floor against dropped tools. In a fire the plastic ones melt and let steam out. What they cannot do is replace the steel bars. Bars carry a known pull along a known line, and fibers carry a small, unmeasured share in every direction. On this house fibers are an addition to the reinforcement in slabs and fire-exposed elements, never a substitute for it.

**Professional**

ACI 544.4R-18 draws the boundary between the two uses. Fibers can supplement and reduce conventional reinforcement where continuous reinforcement is not essential to safety and integrity. That means slabs on ground, pavements, overlays, shotcrete linings, slabs on piles and some precast units. They do not replace primary flexural reinforcement in residential structural members under the code. Industrial slab-on-ground design uses fiber concrete as primary reinforcement under ACI 360R and the United Kingdom's TR 34. ACI 318-19 admits steel fibers as minimum shear reinforcement in a narrow class of beams (Code below). For the structural shell, fibers are supplementary.

Three uses fit this house, each with a dose. Macro-synthetic or steel fibers at 3 to 7 pounds per cubic yard go into slabs on ground for plastic-shrinkage control, impact and abrasion resistance, and as a supplement to temperature-and-shrinkage steel. The primary reinforcement, No. 4 at 16 inches each way in a typical residential slab, is still placed as the engineer specifies.

Steel fibers at 25 to 50 pounds per cubic yard serve as designed shear reinforcement only in an element the engineer designs for it. Polypropylene monofilament fibers at low dosage go into the fire-exposed structural elements for spalling mitigation. No submittal for this house states that fibers replace bars, that no reinforcing is required where fibers are used, or that fiber concrete removes the need for primary reinforcement.

**Code**

```
Steel fibers may serve as minimum shear reinforcement only within fixed limits.
  Normalweight concrete with an f'c of 6,000 psi or less, a member depth of 24 inches or less, factored shear under the limit the table sets, and the fiber mix accepted by flexural test.
  Source: ACI 318-19 Table 9.6.3.1 and section 26.12.7.1.
```

## 6.16 Seismic performance: the field evidence

**Simple**

Unreinforced masonry is the deadliest common building type in earthquakes. Its walls are stacked units with nothing tying them to each other or to the floors and roof. During shaking, an unanchored wall face separates from the building and falls. Reinforced, grouted, anchored masonry behaves differently. Steel ties the courses into one unit, and the bond beams tie the walls to the floors and roof. In Chile in 2010, houses built that way stood beside similar houses that did not. Investigators traced the difference to small details at the joints, not to how much wall each one had.

**Professional**

Unreinforced masonry lacks both continuity and diaphragm anchorage. Under shaking, the out-of-plane inertia of an unanchored wall has no load path into the diaphragm above, which is the dominant recorded collapse mechanism for the type. Anchoring the floor and roof diaphragms to the walls converts each wall from an independently vibrating mass into a braced element of the structure. Saunders Seismic's retrofit guide and Simpson Strong-Tie's retrofit blog both record that anchorage as the first and most effective retrofit step for existing unreinforced buildings.

Here the walls are reinforced and grouted, with diaphragm anchorage through the bond beams, so the mechanism is designed out provided the detailing is executed as drawn. Four field conditions reintroduce it into a nominally reinforced wall. They are partial grouting thinner than the design assumed, a bond beam interrupted at an opening, an ungrouted void at a congested bond-beam intersection, and an unverified tie-down.

Chile's 2010 Maule earthquake, magnitude 8.8, produced the clearest comparison for reinforced and confined masonry. Brzev, Astroza and Moroni's 2010 reconnaissance report and Astroza, Moroni, Brzev and Tanner's 2012 paper on engineered masonry in that earthquake record physically adjacent, nominally similar masonry buildings with sharply different outcomes. Some stood undamaged while their neighbors were severely damaged or partly collapsed. Nameable details made the difference, rather than wall quantity, material strength or apparent design intent:

- missing or inadequate ties at the joint zones between confining elements
- absent ties in end columns, concentrating damage in the joint zone
- absent ties at beam-to-column joints combined with short anchorage, producing joint shear failure
- longitudinal bars buckling where tie size and spacing could not restrain them under load reversal

Across the surveyed stock, most one- and two-story confined-masonry dwellings were undamaged, and so were most three- and four-story confined-masonry buildings. Several reinforced and partially confined three- and four-story buildings suffered extensive damage, and two partially confined three-story buildings collapsed. This house's specification closes those modes at the design level: continuous vertical bars in grouted cells, bond beams developed past every opening, and laps and cover to the development rules. Field execution is the remaining exposure, because the Chilean surveys record buildings where the designed reinforcement existed on paper and a placement gap undid it. Hold points and pre-pour checks target the joint zones and anchorage points where similar buildings diverged.

## 6.17 Voluntary upgrades beyond the code minimum

**Simple**

Oregon's earthquake rules are written so that the people inside survive. Afterward the building itself may be damaged past repair. This house designs above that line. Each option adds steel, grout or engineering analysis beyond the minimum. Some of them a block crew can do with the tools it already has. Filling every cell with grout, running each vertical bar in one piece from footing to roof, and doubling the horizontal wire are three. Others are research ideas, such as a wall that rocks on its base and recenters itself. Those need the engineer to invent the detail for this house.

**Applied**

1. Price solid grouting against the reinforced-cells baseline from the mason's quote on the wall schedule.
2. Price the four detailing upgrades per linear foot from the rebar supplier and the mason.
3. Ask the engineer where a continuous rod tie adds margin.
4. Expect the answer at wall segments between large openings, short returns and low-margin overturning lines.
5. State the performance target, above life safety, in the engineer's brief.
6. Say whether a resiliency rating is wanted.

**Professional**

### Solid grouting of every cell

This house's baseline grouts every reinforced cell. Grouting every cell, reinforced or not, is standard West Coast seismic practice, and partial grouting is the accepted cost-saving norm in lower-seismic regions. The shake-table study "Seismic Performance Assessment of Partially Grouted, Nominally Reinforced Concrete-Masonry Structural Walls" finds that full grouting improves ductility, damage pattern and post-peak behavior. A 2023 test program on partially grouted walls with different horizontal reinforcement types agrees. Both treat a partially grouted wall as a different structural system rather than a cheaper equal, and neither supplies a single multiplier transferable to this wall geometry.

Terrapin Construction Group's cost page for May 2026 puts the grout-fill increment at $2 to $4 per square foot of wall face over a hollow wall. It puts solid-grouted reinforced walls at $22 to $26 per square foot in coastal high-seismic markets, and the Pacific Northwest's installed range at $22 to $32. Per-wall figures take a mason's quote against the actual wall schedule.

### Ductile detailing at first construction

Four upgrades use the same crew, tools and trade as the code-minimum wall:

- vertical bars at closer spacing, No. 5 at 24 inches against the code's No. 5 at 48 inches for an eight-inch wall
- full-height continuous vertical bars where stock length and story height allow, removing the lap zones and their congestion
- joint reinforcement in every course instead of every other course, doubling that material and its laying time
- added dowels at the wall-to-bond-beam interfaces beyond the required minimum

Each is a material-and-labor increment, not a new skill. Per-linear-foot figures for any of them take a mason's and a rebar supplier's quote against the wall schedule. Until then the grout increment above is the nearest order-of-magnitude reference.

### A continuous tension tie at every wall segment

Proprietary continuous-rod systems, Simpson Strong-Tie's Strong-Rod among them, run a coupled rod from roof level to foundation anchorage. Overturning and uplift are then resisted as one designed tension path. They were developed for multi-story light-frame construction. Fully grouted, continuously reinforced block or concrete walls already contain more continuous mass and steel than the framing those systems supplement. Here the applicable version of the upgrade is continuity in the wall's own vertical bars. Discrete rods remain candidates at wall segments between large openings, at short wall returns, and on wall lines where the overturning calculation approaches the code demand. Pricing follows a take-off once the engineer has sized the demand at each line.

### Wall density as a design check

Wall density per unit floor is the shear-wall area in each direction divided by the floor area. Moroni, Astroza and Acevedo's 2004 study of Chilean masonry housing reports the correlation Astroza and others drew between it and damage after the 1985 Llolleo earthquake. Light damage went with densities above 1.15 percent, moderate with 0.85 to 1.15, and severe with 0.50 to 0.85. In their database, density exceeded 1.15 percent in 69 percent of the reinforced masonry buildings, and in 57 percent of those built during the 1990s. Any building under 0.85 percent they flag as a concern.

Those figures are calibrated to Chilean confined and reinforced masonry. They do not transfer numerically to reinforced block designed under TMS 402, which works through load paths and reinforcement ratios instead. Long, continuous shear-wall lines rather than short segments between openings are the working proxy here.

### A named performance target

ASCE 41-23's performance levels, Operational, Immediate Occupancy, Life Safety and Collapse Prevention, are written for evaluating and retrofitting existing buildings. Their concept transfers as an owner's brief, and the engineer reaches a higher-than-code target through conventional over-design: higher reinforcement ratios, tighter drift limits and conservative detailing margins. Under the U.S. Resiliency Council's rating system, Safety, Damage (repair cost) and Recovery (time to regain function) are each scored from one to five stars, for new and existing buildings. It is a rating and verification system, not a design standard, and it runs separately from the permit.

No general cost premium for above-code seismic performance is published. One Christchurch commercial building in the Canterbury Earthquakes Royal Commission's report on low-damage technologies had a net construction saving near 7 percent from a schedule three months shorter. That figure is specific to that project's technology.

### Rocking walls and sliding base isolation

Two low-damage concepts remain design concepts rather than selectable options. Post-tensioned rocking walls come from the PRESSS program at the University of California San Diego, extended by New Zealand's Pres-Lam work after Christchurch. Such a wall rocks on its foundation, recenters through unbonded tendons and dissipates energy in replaceable steel elements. Residential adaptations are mature in engineered timber and not in reinforced block or cast concrete.

Low-cost sliding isolation places a low-friction plane between foundation and superstructure with a stop against excess travel. Habieb, Milani, Tavio and Milani's 2017 case study of a single-story masonry house found marble-on-marble and marble-on-geosynthetic interfaces cutting roof acceleration by up to half. The system is not code-recognized in Oregon, and the published designs leave the service crossings, plumbing and wiring across a plane built to move, unresolved for a serviced house. Either concept requires the engineer to develop, analyze and stamp a project-specific design, with nonlinear dynamic analysis, before it can enter a permit submittal.

## 6.18 Safe rooms and hardened options

**Simple**

Safe rooms are built to a tested shelter standard. People inside one survive extreme wind and flying debris even if the rest of the building fails. In a wood-framed house the safe room is a separate reinforced box built inside it, and the box is most of the cost. This house's shell is already reinforced concrete and block. Here the added work is mostly a rated door, a rated vent, and any local reinforcement the engineer finds the room still needs. Tested doors cost $2,500 to $3,200, and an ordinary door undoes the room.

**Applied**

1. Have the engineer check the candidate room's walls, slab and roof against the shelter loads.
2. Set the door-frame threshold anchors and any local footing bars at the foundation pre-pour holds.
3. Place the frame's anchor pattern and any added wall bars at the wall pre-pour hold.
4. Set the vent embeds and any roof bars at the pre-cover holds.
5. Install the rated door and frame to the maker's tested instructions.
6. Have that installation signed off against those instructions.
7. Read the state's tsunami inundation map for the parcel before any inundation design is discussed.

**Professional**

FEMA P-320, sixth edition, December 2024, prices a new-construction safe room built to its design plans at $12,700 to $16,100 for an 8-by-8-foot room and $25,600 to $34,500 for a 14-by-14-foot room. Those figures cover materials, labor, sales tax and a 15 percent contingency, and they exclude the door assembly. They derive from RS Means 2019 national averages adjusted by producer price indexes. Prefabricated steel rooms of 4 by 6 feet retail at $5,500 to $6,700 shipped 300 miles and installed, with site preparation averaging $1,000 in 2021. Every one of those plans assumes an independent reinforced concrete or masonry box inside a wood-framed house.

On this shell the engineer's load check decides whether the room's walls, slab and roof already meet the shelter loads, and the answer may be that they do. The door and frame assembly and the vent are listed, tested products, not field-built items. Independent anchorage applies where the shelter standard requires the room to be isolable from building racking. Shelter-standard wall and door values and the choice of room are stated in the What Concrete Uniquely Enables chapter. The marginal figure comes from that load check and the quotes for the door, the vent and any added work.

Built at first construction, a safe room follows the shell's pour sequence, with its items added to the checklists at the existing hold points. One verification is added. The rated door and frame are signed off against the manufacturer's tested installation documentation, because installation outside those instructions voids the assembly's rating.

### Tsunami siting

FEMA P-646, third edition, 2019, is guidance for community vertical-evacuation refuges, not a single-family requirement anywhere in Oregon. Its structural concepts transfer voluntarily to a house sited inside a mapped inundation zone. Breakaway lower-level wall panels detach before loading the primary structure. Open ground-floor construction lets water and debris pass. Structural elements below the inundation level are designed for the hydrodynamic and debris-impact loads of ASCE 7-16's tsunami provisions. Whether the parcel sits inside a zone is read from the current map of the Oregon Department of Geology and Mineral Industries (DOGAMI), before any of it becomes a live design question.

### Dome and vault geometry

Monolithic dome homes run $100 to $250 per square foot, or $160,000 to $500,000 by size and finish, on HomeGuide's and the Monolithic Dome Institute's 2026 figures. That range overlaps high-end conventional concrete construction. In the institute's own commentary, financing is the largest hurdle, because lenders prefer one general contractor presenting one complete proposal and dome construction adds a specialist builder to an owner-managed job. Appraisers lack comparable sales, and dome homes sit on the market longer than conventional houses. Curved walls complicate cabinetry, furniture placement and acoustics, and the response, custom built-ins, adds cost beyond the base figures.

Oregon precedent exists at institutional scale in the twin Monolithic Domes of Portland's City Bible Church, in use since 1991. Residential dome-contractor availability in Oregon is confirmed by inquiry at build time. One domed or barrel-vaulted safe room inside an otherwise rectilinear house would put a compression shell over a small span and avoid the whole-house financing and layout drawbacks. That hybrid is a design concept, priced by a specialty-forming quote against the room size and the shelter loads.

**Code**

```
A storm shelter or safe room in a dwelling is built to the shelter standard.
  Storm shelters, detached or built as safe rooms within buildings for refuge from tornadoes and hurricanes, comply with ICC 500 in addition to the code.
  Source: ORSC R323.1 (2023 edition); ICC 500-2020.
```

## 6.19 Water-retaining structures

**Simple**

Stored water presses on every face of a cistern all the time, and the wall must not leak. Concrete cisterns, buried or at grade, are therefore designed to their own rules. Their cracks have to stay finer than a dry wall's. In an earthquake the stored water sloshes and adds force. Groundwater pushes an empty tank upward when the water table stands above its base. Those four conditions have their own design standards, separate from the ones for the house's walls.

**Professional**

Water-retaining structures are designed to the environmental-structures standards, not the dry-wall assumptions behind the house's walls. ACI 350 governs the structure: sustained hydrostatic load on every face, liquid-tightness, and crack-width control tighter than a dry wall's serviceability limit.

ACI 350.3 governs the seismic design of liquid-containing structures, with impulsive and convective (sloshing) hydrodynamic forces, the tank's vibration periods, sloshing wave height and soil-structure interaction. Its scope covers concrete structures storing water, with no lower size bound, so no size exemption removes a residential cistern from it. Whether the engineer applies the full method or treats the stored water as added seismic mass in the main analysis is a scale judgment for the specific tank. AWWA D110 and D115 apply to prestressed wire-wrapped and tendon-stressed tanks, a municipal-scale method, and do not apply at residential scale.

Size, siting and plumbing of the cistern are stated in the water independence chapter. Dancing Rabbit Ecovillage's published owner-built cistern used No. 6 bars wired on a 1-foot grid and doweled into the base slab. That is a reference point for the conversation with the engineer, not a design value, because the schedule depends on the tank's height, wall thickness and edge restraint. Every control or construction joint in a water-retaining wall takes a cast-in waterstop and a sealed exposed face. For flotation, the empty tank is checked and held down with dead weight, anchors or a relief detail sized for it.

## 6.20 Structural hold points

**Simple**

Work stops at a hold point until someone has looked at it and signed. Before every pour, the inspector sees the steel, the embeds and the forms, because after the pour none of it can be checked. Before every grout lift in a block wall, the same is true of the bars in the cells. Where the drawings say so, the engineer and a special inspector join the inspector. Missed inspections cannot be made up afterward, so the schedule is built around them.

**Applied**

| Hold point | What is verified | Who signs |
|---|---|---|
| Footing, before the pour | Bearing surface, footing geometry, reinforcement, anchor bolts, embeds, the grounding electrode | The building inspector, and the engineer on an engineered foundation |
| Foundation wall, before the pour | Reinforcement, vertical bar continuity from the footing, anchor bolts, sleeves, dampproofing readiness | The building inspector |
| Foundation drainage and waterproofing, before backfill | Drain rock, the perimeter drain, membrane continuity, the capillary break | The building inspector |
| Slab subgrade, before the pour | Compaction, capillary break, vapor retarder, soil-gas retarder where required, under-slab insulation, sleeves | The building inspector |
| Block wall, before each grout pour | Bar size, location, spacing and lapping, cleanouts and grout space | The building inspector, and a special inspector where the pour exceeds the code's lift height |
| Concrete delivery | Mix conformance, slump, air, temperature, the batch ticket | The engineer on engineered work, and a special inspector where required |
| Floor and roof level | Bond beam continuity, tie-down anchors, embeds for the floor or roof system | The building inspector |
| Floor diaphragm, before cover | Reinforcement in a cast slab, shop drawings for precast, the maker's stamp for engineered wood | The building inspector, and the engineer for an engineered diaphragm |
| Roof structure, before cover | Truss installation to the maker's drawings, anchorage, diaphragm continuity | The building inspector |
| Safe-room door and frame, where one is built | Installation and anchorage against the door maker's tested instructions | The engineer, or a special inspector where the design assigns it |

1. Add the safe-room anchors and door-frame embeds to the wall and foundation pre-pour lists.
2. Add a sleeve for a future generator, propane or fuel-oil supply line.
3. Add a cast-in plate or bolt pattern for a communications mast.
4. Size the mast plate for the site's wind load.
5. Add a manual backup pump's access sleeve where the water system has a well.
6. Check every embed on those lists with a template, a second signature and a photograph.

**Professional**

Special inspection is a program of the structural specialty code, and the base residential code does not operate one. Here it applies where the engineered design invokes it, with grouted block under TMS 602's inspection levels and the concrete categories of ACI 318-19 section 26.13 among the triggers, or where the building official requires it. The engineer defines the program in the construction documents, and the readiness criteria for each hold point are in the inspection chapter.

Oregon's 2026 residential code adds a concrete-specific inspection of its own under R109.1.5.3. In Seismic Design Category D0, D1, D2 and E, reinforced masonry, ICF and conventionally formed concrete walls are inspected after the embedded systems and bars are in place and before grout or concrete. That inspection verifies bar size, location, spacing and lapping and, for masonry, the cleanouts and grout space.

Cast in during the scheduled pours, a resilience embed costs a sleeve or a plate. Added after cure, the same item is a post-installed anchor or a core drill through reinforced work.

## 6.21 The documents behind the structure

**Simple**

Two kinds of documents govern the structure. Oregon's residential code is law, and the state structural code stands behind it for anything the engineer designs. Standards from the concrete, masonry, steel and testing bodies sit below them. They supply the design rules and the material and test methods the code adopts by reference. Most of those standards are sold, not published free. Your engineer's copy is the working text. The drawings name the edition used, because the code references one edition and the publishers sell a newer one.

**Professional**

| Document | What it governs here | Edition |
|---|---|---|
| Oregon Residential Specialty Code (ORSC) | The prescriptive rules, loads, inspections and the path decision | 2023 (2021 IRC base), with the 2026 edition (2024 IRC base) in phase-in to April 1, 2027 |
| Oregon Structural Specialty Code (OSSC) | Nonprescriptive design loads and provisions, through the residential code's definition of Building Code | 2022 (ASCE 7-16) under Statewide Alternate Method 26-01, or 2025 (ASCE 7-22) |
| ASCE 7 | Load combinations, snow and drift, wind, seismic, tsunami, ponding | 7-16 with Supplement 1 in the 2023 ORSC, 7-22 in the 2025 OSSC |
| ACI 318 | Structural concrete design, cover, development, durability classes, inspection categories | 318-19 referenced, 318-25 in circulation |
| ACI 332 | Residential concrete: footings, foundation walls, slabs on ground, above-grade walls in scope, expansive soils | 332-20 |
| PCA 100 | Prescriptive above-grade concrete walls outside Category C | 100-17 |
| TMS 402 and TMS 602 | Masonry design and construction, including veneer, grout, inspection levels and weather rules | 402-16 and 602-16 referenced, 2022 editions current |
| ACI 224R | Guide crack widths by exposure | 224R-01, reapproved 2008 |
| ACI 347R | Formwork pressure and tie design | Current guide |
| ACI 305R, 306R and 308R | Hot weather, cold weather and curing | Current guides |
| ACI 544.4R and ACI 360R | Fiber reinforcement limits, slabs on ground | 544.4R-18, 360R |
| ACI 350 and 350.3 | Water-retaining structures and their seismic design | Current editions |
| ACI 440.11 and 440.1R | GFRP design and detailing | 440.11-22, 440.1R-15 |
| ICC 500, FEMA P-361, FEMA P-320, FEMA P-646 | Storm shelters and safe rooms, tsunami refuge concepts | ICC 500-2020, P-361 fifth edition, P-320 sixth edition (December 2024), P-646 third edition (2019) |
| ASTM A615, A706, A580, A82, A951 | Reinforcing bar, low-alloy bar, stainless wire, carbon wire, joint reinforcement | Current |
| ASTM C90, C476, C270, C140 | Loadbearing units, grout, mortar, unit testing | C90-16a and C476-18 referenced |
| ASTM C150, C595, C33, C618, C989, C1240, C260, C494, C94 | Cements, aggregate, fly ash, slag, silica fume, admixtures, ready-mixed concrete | Current |
| ASTM C172, C143, C231, C39, C1567, C1116, C1609 | Sampling, slump, air content, cylinders, alkali-silica reactivity, fiber concrete and its flexural test | Current |
| CMHA TEK 12-01B, 16-04A, 16-01A, 14-08B and TR91B | Ties, cavity walls, multi-wythe walls, lintels | Current |
| BIA Technical Notes 28D and 44B | Brick veneer over block, veneer anchorage | 28D June 2018 |
| PCI Manual for the Design of Hollow Core Slabs and Walls | Hollow-core plank design | MNL-126 |
| ICC-ES ESR-4057 and ESR-3814, AC125 and AC454 | Adhesive anchors and post-installed bars, FRP acceptance criteria | Reports current at installation |
| Bureau of Reclamation, Joint Spacing for Concrete Structures | Control-joint spacing in walls | 2016 |
| Statewide Alternate Method 26-01 | Continued reference to the 2022 OSSC under the 2023 ORSC | Issued January 20, 2026 |

## Who decides what

| Decision | Who decides | When, or what triggers it |
|---|---|---|
| The design path for each element | Engineer of record, with Jon | At structural design, from the parcel's category and the element |
| Which OSSC edition and snow basis the nonprescriptive design references | Engineer of record | At structural design, stated on the drawings |
| The seismic design category, wind speed and ground snow load | The lookup at the coordinates, confirmed by the engineer | Once a parcel is chosen |
| A site-specific wind study | Engineer of record | When the lookup places the parcel inside a special wind region |
| Analysis method and detailing for any irregularity | Engineer of record | From the floor plan |
| Control-joint spacing and bar spacing at each wall, by its exposure class | Engineer of record | Structural design |
| Exposure class of each element | Engineer of record, from the geotechnical report | Before the mix is specified |
| The SCM type and dose on alkali-silica grounds | The C1567 result, applied by the engineer | Before the mix design is final |
| Lintel sizes and grouted jamb cells | Engineer of record | When the openings are drawn |
| Floor system and plank bearing | Engineer of record, with the plank maker | Structural design |
| Drift loading at parapets, valleys and roof steps | Engineer of record | Roof design |
| Truss connectors on the prescriptive path | The code's table and the maker's evaluation report | Before trusses are ordered |
| The expansion joint at an attached structure | Engineer of record | When the attachment is designed |
| Service-layer classification | Jon, with the plan reviewer | Before the floor plan is fixed |
| Candidate cells for niches | Engineer of record, from the wall schedule | Structural design |
| Polypropylene fibers for spalling | Engineer of record | Mix specification |
| Solid grouting, continuous bars and the other detailing upgrades | Jon, from the mason's and supplier's quotes | Before the wall schedule is final |
| A continuous rod tie at any wall segment | Engineer of record | Structural design |
| A performance target above life safety, and a USRC rating | Jon, in the engineer's brief | Before structural design starts |
| Whether a safe room's existing walls, slab and roof meet the shelter loads | Engineer of record | Before the room is priced |
| Tsunami-zone design concepts | Jon, with the engineer, after the DOGAMI map is read | Site selection |
| Cistern design, full sloshing analysis or added mass | Engineer of record | Once the tank's size is fixed |
| The special-inspection program | Engineer of record, enforced by the building official | On the construction documents |
| Cleanouts and special inspection for tall grout pours | Building official, through the permit | Plan review |
| The post-installed anchor product | Engineer of record | At the first missed embed |
| Steel beams under concrete floors, stamped or engineered | Building official | Plan review |

## Open items

- **2026 code numbers.** Unknown: whether R301.2.2, R301.2.3, R301.3, R323, R404, R606, R608, R802 and R903 keep their numbers and text in the 2026 residential code, built on the 2024 IRC. Answered by: the integrated 2026 codebook. Assumed meanwhile: the 2023 numbers and text, usable on a permit through March 31, 2027.
- **ACI 318-19 tables cited.** Unknown: the verbatim text of Tables 11.6.1, 19.3.2.1, 20.5.1.3.1 and 9.6.3.1 and section 26.12.7.1, in a purchased standard. Answered by: the engineer's copy. Assumed meanwhile: the values stated, from the standard's published structure and secondary summaries.
- **ACI 224R crack widths.** Unknown: the inch values of Table 4.1 by exposure, in a scanned copy that could not be read. Answered by: a text copy of ACI 224R-01. Assumed meanwhile: the spacing-based control of ACI 318-19 governs, with the table as the durability reference behind it.
- **ACI 347R pressure coefficients.** Unknown: the exact lateral-pressure formula coefficients. Answered by: the forming-system maker's tables for the system rented or bought. Assumed meanwhile: the full-hydrostatic case and a factor of safety of 2.0 on ties.
- **ACI 440.11 reading.** Unknown: the standard's own text on members outside the seismic force-resisting system in Category D, which the durability chapter treats as an open reading. Answered by: the engineer against ACI 440.11-22. Assumed meanwhile: no GFRP in any structural member in D0 to D2, per the StructureMag summary.
- **GFRP detailing figures.** Unknown: development and lap multipliers from the standard itself, known here from a vendor's explainer. Answered by: ACI 440.11-22. Assumed meanwhile: 1.3 to 1.6 times steel's development length as a planning range for the narrow Category C case.
- **Primary roof drain sizing.** Unknown: the Oregon plumbing code section that sizes primary roof drains under the 2026 edition. Answered by: the 2026 OPSC, Chapter 11. Assumed meanwhile: drains at each low point under R903.4, sized by the plumbing designer.
- **Return-air plenum rule.** Unknown: the Oregon mechanical code section limiting materials in a return-air plenum. Answered by: the 2025 OMSC. Assumed meanwhile: a service layer used as a plenum takes noncombustible or listed materials.
- **The snow lookup's status.** Unknown: whether snowload.seao.org, the source the 2023 residential code names, is still maintained (it did not resolve from this machine on October 29, 2026), and which source the 2026 residential code names. Answered by: the Building Codes Division's design-criteria page and the 2026 codebook. Assumed meanwhile: the Design Criteria Hub for both editions, with the engineer stating the basis.
- **Special wind region footnote.** Unknown: the text of Table R301.2's footnote on which parts of a listed county take the special-wind-region speed. Answered by: the printed 2023 ORSC table. Assumed meanwhile: the mapped region on Figure R301.2.1(1).
- **Engineering fee.** Unknown: the source of the $4,000 to $10,000 structural fee, a Revision 7 planning figure. Answered by: two quotes from Oregon structural engineers. Assumed meanwhile: that range for a custom two-story house of 2,500 to 3,500 square feet.
- **Per-wall grout and detailing costs.** Unknown: the cost of solid grouting and of each detailing upgrade per linear foot on this wall schedule. Answered by: the mason's and rebar supplier's quotes. Assumed meanwhile: Terrapin's $2 to $4 per square foot grout increment as the order of magnitude.
- **Safe-room marginal cost.** Unknown: the cost of the door, vent and any added work in an already-reinforced shell. Answered by: the engineer's shelter-load check and quotes. Assumed meanwhile: a figure well under the FEMA plan costs, which price the whole box.
- **Tie thermal bridging.** Unknown: a named source for the 0.5 to 1 percent point-bridge area and the R-26 to R-23 derating, carried from Revision 7. Answered by: the tie maker's thermal data or a hygrothermal calculation. Assumed meanwhile: those planning figures.
- **Impact sound inside one dwelling.** Unknown: whether the Oregon residential code sets any impact-insulation rating for a floor within a single dwelling. Answered by: the 2023 and 2026 ORSC text. Assumed meanwhile: none, with the rating a comfort specification.
- **Sliding-isolation friction values.** Unknown: the measured friction range for the tested interface pairs, reported in a review of low-cost isolation materials that was not read (Revision 7 gave 0.15 to 0.35). Answered by: that review, named. Assumed meanwhile: the mechanism only.
- **Wall density transfer.** Unknown: any validated wall-density check for reinforced block in high seismic categories. Answered by: a project-specific study, if one is ever commissioned. Assumed meanwhile: the regularity strategy as the proxy.
- **Service-layer thresholds.** Unknown: a code basis for the 30-inch plenum limit and the 4-foot mechanical-level floor. Answered by: the plan reviewer at the pre-application meeting. Assumed meanwhile: those two values as the plan's choice (Jon to confirm).
- **Special-inspection triggers.** Unknown: the exact triggers the engineer's program will carry (Revision 7 named concrete above 4,000 psi, which no code section read supports). Answered by: the construction documents. Assumed meanwhile: grouted block above the code's lift height and the ACI 318-19 categories.
- **Control-joint spacing.** Unknown: the spacing the engineer sets for each wall. Answered by: the structural design. Assumed meanwhile: 2 to 3 times the wall height, within 10 to 12 feet.
- **Dome hybrid and dome builders.** Unknown: any built example of a single domed safe room inside a rectilinear concrete house, and whether a residential dome contractor works in Oregon. Answered by: a specialty-forming quote and direct inquiry. Assumed meanwhile: a concept, unpriced.
- **Dropped from Revision 7.** The contents-list opening and its two routing paragraphs, replaced by facts about the house. The three-story masonry maximum cited to R301.2.2.7, which limits wood, cold-formed steel and panel buildings and says nothing about masonry. The claim that prescriptive single-wythe masonry reaches 10 feet and three stories in D0 and D1, contradicted by R606.12.3.1 and Table R606.12.2.1. The 50 psf stair live load, corrected to 40 psf from Table R301.5. The 5-foot grout-lift threshold, replaced by the code's 8 feet and 64 inches. The Columbia Gorge "over 130 mph" claim, contradicted by Table R301.2. The 15-foot eave-to-ridge limit and the "70 to 80 percent" long-life figure, which no source supports. The 4,000 psi special-inspection trigger. The TMS 402 stack-bond ratio of 0.00028, known only from a code summary and replaced by the Oregon code's own ratios. The "Chilean code minimum of 0.85 percent", which the paper does not state. The IPC roof-drain citations, since Oregon's plumbing code is the OPSC. The FEMA P-320 figures of an earlier edition. The "4 feet for SDC D2 two-story" anchor-bolt rule, which R403.1.6.1 states as 4 feet for buildings over two stories. The anchor-bolt, footing-reinforcing and grounding-electrode Code entries, which the foundation chapter carries. The eight-line structural standard, whose lines are now Decisions. The "acceptable" and "not acceptable" fiber wording lists, now one sentence of fact. The forum answer on a 124-inch lintel span. The "Does not require PE: wood-framed walls under R602" line, since the shell has none.

## Decisions this chapter records

- (decided) The structural shell is designed by a licensed engineer under the nonprescriptive path.
- (decided) The shell is cast concrete, reinforced concrete block and steel, with wood only as a manufacturer-stamped truss or joist on the prescriptive fallback.
- (decided) Every load has a drawn path to the soil before the design is finalized.
- (decided) Every assembly is designed to a referenced standard, and the drawings name the edition.
- (decided) The design path for each element is chosen at design time and held through construction, and a field change to approved structural work is a design change.
- (decided) Removable-form cast-in-place concrete and reinforced block are the default wall construction.
- (decided) Running bond is the default coursing.
- (decided) Bond beams run at the top of the foundation wall, at every floor and at the roof, and every reinforced cell is grouted.
- (decided) Hollow-core precast is the primary floor at spans of 16 to 32 feet, with a cast-in-place slab at shorter spans.
- (decided) A concrete deck with a protected membrane roof is the primary roof, and asphalt shingles are rejected.
- (decided) The long-life mix: 4,000 psi minimum, 0.45 maximum water-cement ratio, SCM replacement, and 7 days of curing.
- (decided) One metallurgy per structural element, and all stainless wherever any stainless is used.
- (decided) The structure is designed with margin above the code's life-safety minimum where the evidence supports it.
- (decided) Fibers are supplementary and never a substitute for primary reinforcement.
- (decided) Every control joint in a water-resisting wall takes a cast-in waterstop.
- (pending parcel) The seismic design category, wind speed and ground snow load.
- (pending parcel) Whether the parcel lies in a special wind region or a mapped tsunami zone.
- (pending engineer) The OSSC edition and snow basis the drawings reference.
- (pending engineer) Control joints, exposure classes, lintels, laps and covers for each element.
- (pending engineer) Whether a safe room's shell already meets the shelter loads.
- (pending engineer) The cistern's structural design.
- (Jon to confirm) Solid grouting of every cell.
- (Jon to confirm) Full-height continuous vertical bars, joint reinforcement in every course, and added dowels at the bond beams.
- (Jon to confirm) A performance target above life safety in the engineer's brief, and whether a USRC rating is sought.
- (Jon to confirm) A safe room, and which room.
- (Jon to confirm) The service-layer classification: a plenum of 30 inches or less, or a mechanical level of 4 feet or more counted as a story.
- (Jon to confirm) Polypropylene fibers in the fire-exposed structural elements.
- (Jon to confirm) The resilience embeds: a fuel-line sleeve, an antenna mount and a manual well-pump access.
- (Jon to confirm) The C1567 test ordered on the actual materials before the mix is final.

## Records to keep

- The parcel's design-criteria report and any ATC tool printout, with the category, wind speed and ground snow load.
- The stamped structural drawings, the calculations and the special-inspection program, with the edition statement on the cover sheet.
- The geotechnical report, named on the drawings.
- The exposure-class assignment for each element, on the drawings.
- The C1567 test report and the mix submittal.
- The pre-pour checklists with the second signature, and the photographs of every cage and embed.
- Grout pour logs, cleanout inspections and special-inspection reports.
- Batch tickets, slump, air and cylinder results for every delivery.
- The lintel schedule and its bearing details.
- The plank maker's stamped shop drawings and erection sequence, or the truss maker's drawings and evaluation report.
- Connector and anchor evaluation reports, at the revision current when installed.
- The safe-room door's installation sign-off against the maker's instructions.
- Any statewide alternate method relied on, cited on the cover sheet.
