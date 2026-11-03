# Chapter 6: Structural System and Concrete Design

A licensed engineer designs this structural shell, because the concrete floors and roof the thousand-year shell needs have no prescriptive path in Oregon's residential code. On most western Oregon sites the code's own tables stop at one story of reinforced block under a wood roof, and they send every above-grade concrete wall to the engineering standards. The shell is cast concrete, reinforced concrete block and steel, designed with margin above the code's life-safety minimum and detailed so that the laps, cover, grout and anchorage the calculations assume are the ones the inspector finds. The soil chapter supplies the bearing values the design starts from. Costs are 2026 figures unless a different year is given.

> **Jon's note.** [JON: drafted from the record, confirm or rewrite] I chose the engineered path because the shell I want has concrete floors and a concrete roof, and the code's free tables give me concrete walls with wood above them. The engineer's fee buys the whole shell instead of the walls alone. I want margin above the code's life-safety line wherever the evidence supports it, because the code's goal is that people get out, and mine is that the house is repairable and lived in afterward. Nothing in the load path is wood. Where the code lets a manufacturer's stamp carry a truss or a floor joist, that is the fallback, not the plan. [JON: do you want solid grouting and full-height bars priced with the base wall, or only the code-minimum wall?] [JON: is a safe room in the plan, and which room?]

## 6.1 What the structure has to do

**Simple**

Every load on your house needs an unbroken path to the ground. The roof's weight, snow, furniture and people push down. Wind and earthquakes push sideways, and the soil pushes against any wall below grade. Wind also pulls up on the roof. Each push has its own path. Roof weight goes into the walls, the walls carry it to the footings, and the footings spread it into the soil. Sideways force goes from each floor into the walls that brace it, then down. A wall that stops short of the floor above, or a floor cut by a large opening, breaks a path. In this house every path is concrete and reinforced block from the roof to the soil.

**Applied**

1. Before the structural design is finalized, mark every bearing wall on the plans, with the roof and floor weight each one receives.
2. Mark each floor support with its span and end conditions.
3. Mark each roof support with its eave and ridge geometry.
4. Mark the stair openings and every other hole in a floor.
5. Mark the large window and door openings, where the wall's continuity is interrupted.
6. Mark the wall lines that resist wind and earthquake, in both directions.
7. Mark where each wall line's load enters the soil.
8. Mark the utility routes through or around the structure, so no later penetration cuts a load path.
9. Trace each load from where it is applied to the foundation, and treat any path the drawings do not show as a design gap.

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

Bearing walls stack floor over floor in one plane, and the wall lines run from foundation to roof without offsets. Each floor diaphragm ties into the walls through chord and collector steel, and a bond beam runs at every floor and at the roof. Openings stay within the limits the path decision sets, and every footing is sized from the site's own soil values. A building that follows those rules can be traced in section: roof to wall, floor to wall, wall to foundation, foundation to soil, and lateral force to diaphragm, diaphragm to shear wall, shear wall to foundation. Thicker walls or slabs outside a defined load path add dead load, which raises the seismic demand, and add no capacity.

Recesses, projections and offset volumes do not trade away a prescriptive path on a western Oregon site, because the seismic category has already removed it. Inside the engineered path each offset still costs analysis and detailing. An irregular building under the residential code's conditions and under ASCE 7 cannot use the simplest equivalent-lateral-force procedure, and each offset adds reinforcement, torsional demand and connection detailing. No percentage limit on articulation exists. The conditions are the seven named in the residential code, applied by the engineer to the actual floor plan, and they are listed with the path decision.

**Code**

```
Floor live loads are fixed minimums.
  40 psf in living areas, 30 psf in sleeping areas, 40 psf on stairs plus a 300-pound point load, 40 psf on decks and balconies, 50 psf in garages plus 2,000-pound wheel loads.
  Source: ORSC Table R301.5 (2023 edition).
```

## 6.2 Where the site puts the house: seismic category, wind and snow

**Simple**

Three numbers tied to the parcel's location decide how much of this design is engineered: its earthquake category, its wind speed and its snow load. Oregon's residential code puts the Willamette Valley, the I-5 corridor and the coast in its highest earthquake categories for houses. Most of eastern Oregon sits one step lower. Nine coastal and Coast Range counties carry a higher design wind speed than the rest of the state. Snow depends on elevation more than on region, and the state's snow map has changed from a fifty-year-storm basis to one that targets an even risk of failure. Until a parcel is chosen, the design assumes the higher earthquake categories, because that is where most buildable western Oregon land sits.

**Applied**

1. Look up the parcel's seismic design category, wind speed and ground snow load on the Building Codes Division's Design Criteria Hub, and keep the report.
2. Where the parcel sits near a boundary on the code's category map, run the ATC Hazards by Location tool at the coordinates.
3. Set the tool to ASCE 7-16, Risk Category II and Site Class D, and read the short-period design acceleration.
4. Record the category that acceleration falls in, from the code's table.
5. Check the code's special-wind-region figure, and use the county's special-wind-region speed where the parcel falls inside one.
6. Read the ground snow load at the parcel's elevation, and add the code's elevation adjustment where the parcel sits above the modeled elevation.
7. Record on the cover sheet which snow basis the engineer designs to, the 2022 structural code's map or the 2025 code's ASCE 7-22 data.

**Professional**

The planning matrix below is read from the code's category map and the county table, and the lookup at the parcel's coordinates replaces it once a parcel exists.

| Region | Likely category | What the prescriptive tables still allow there |
|---|---|---|
| Eastern Oregon: the high desert and the Blue Mountains | C | Concrete walls under R608 within its limits, and masonry under R606 with the Category C rules |
| The Cascade Range and its inland slopes | C to D0 | R608 where the lookup returns C, one-story masonry elsewhere |
| The Willamette Valley margins and central Oregon | D0 | One story of reinforced block under a wood roof, with everything else engineered |
| Most of the Willamette Valley and the I-5 corridor | D1 | The same as D0, with the engineered path the practical default |
| The coast and parts of Lane, Douglas and Coos counties | D2 | The same, with stack bond, parapets and veneer ties under tighter rules |
| Special wind regions: nine coastal and Coast Range counties, and the Columbia Gorge | Varies | The prescriptive wind tables still cover the mapped speeds, and the engineered path takes a site-specific wind study |

The map and the lookup tools agree because they draw on the same mapped ground motion, so a disagreement between them means the parcel sits on a category boundary. A Category E site is designed under the structural specialty code unless the calculation reclassifies it to D2. The county table prints two wind speeds. Every county has a basic design wind speed, and Benton, Clatsop, Coos, Curry, Douglas, Lane, Lincoln, Tillamook and Yamhill counties carry a second, higher speed for the parts of each that fall inside the mapped special wind region. The Columbia River counties print the same speed in both columns. On the engineered path, ASCE 7's special-wind-region provision at section 26.5.1 treats the mapped contour as a starting value and asks for a site-specific wind study by a qualified engineer.

Oregon's prescriptive snow design rests on the Structural Engineers Association of Oregon's electronic snow map, the source the residential code names, with an elevation correction where the site stands above the map's modeled elevation. The 2025 structural specialty code dropped that map for ASCE 7-22's national ground-snow geodatabase, read through the ASCE Hazard Tool or the Design Criteria Hub. The new values are strength-level, risk-targeted loads that cannot be compared line by line with the old map. The Building Codes Division's bulletin on the change puts the national average rise near 12 percent, with some Oregon regions higher, and it makes the thermal factor depend on the roof's insulation, so a well-insulated roof holds more snow in the calculation. The same edition removed Oregon's historic minimum roof snow load for sloped roofs.

Statewide Alternate Method 26-01 lets a design under the 2023 residential code keep referencing the 2022 structural code through March 31, 2027, and the Oregon code and compliance map chapter records the choice of edition as the engineer's. The drawings state the edition and the snow basis they use. A ground snow load from one edition is never combined with the load factors of the other, because the 2022 values are allowable-stress loads and the 2025 values are strength-level loads.

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

You can have this house designed two ways. An engineer designs exactly the house you want, concrete floors and roof included, for $4,000 to $10,000. Or you follow the code's pre-approved tables for free. On a western Oregon site they allow one story of reinforced block, nine feet between supports, under a wood roof and over wood floors. Every element the tables do not cover goes to the engineer anyway, and on this site that is the concrete floors, the concrete roof and every wall under them. This house takes the engineered way, because the thousand-year shell needs the concrete floors and roof.

**Applied**

1. Choose the path before the floor plan is fixed.
2. Take the engineered path for concrete floors and a concrete roof, and the prescriptive path only for a one-story block house under a wood roof.
3. On the engineered path, retain a licensed Oregon structural engineer, and order the geotechnical report before the structural design starts.
4. Give the engineer the parcel's design-criteria report, the footprint and the list of elements in the table below.
5. Have the engineer mark each element's path on the drawings, prescriptive, engineered or alternative method, and hold that assignment through construction.
6. Submit the stamped drawings, the calculations and the special-inspection program with the permit application.

**Professional**

| Path | What it is | Where it fits | Where it is unavailable |
|---|---|---|---|
| Prescriptive | The code states the rule and the design stays inside its limits | Ordinary geometry inside the residential tables, Category C sites, one-story single-wythe masonry, conventional spans | Above-grade concrete walls outside Category C, masonry more than one story tall or under a concrete diaphragm in D0 to D2, concrete or masonry floors and roofs, oversized openings, irregular plans |
| Engineered | A licensed engineer designs and stamps the structural drawings under R301.1.3 | Most Oregon sites west of the Cascades, any nonstandard element, long spans, concrete floors and roofs | Nowhere, because it is the universal fallback |
| Alternative method | The building official approves a method that meets the code's intent by another route | Tested assemblies, FRP reinforcement, owner-made block, each subject to approval | Where the official does not accept the showing |

The engineer signs the structural drawings (plans, sections, details and schedules), the calculations behind them, and the special-inspection program the engineered design invokes. The geotechnical engineer signs the soil report the foundation design rests on. By occupancy the house stays under the residential code throughout. Engineering the walls does not move the permit, the inspections or the certificate of occupancy to the structural specialty code. Only the design method becomes nonprescriptive, and under R301.1.3 and R301.2.2.5 it references the same standards the structural code uses: PCA 100 or ACI 318 for above-grade concrete walls, with R608 open only to a detached dwelling in Category C.

| Element or condition | Path on a D0 to D2 site | The rule behind it |
|---|---|---|
| Above-grade concrete walls | Engineered under PCA 100 or ACI 318 | R301.2.2.5, with R608 open only to detached dwellings in Category C |
| Masonry walls more than one story tall, or over 9 feet between lateral supports | Engineered under TMS 402 | R606.12.3.1, the wall system chapter's entry |
| Masonry walls under a concrete or hollow-core floor or roof | Engineered | R606.12.1.1 assumes wood or cold-formed steel diaphragms |
| A second story of any kind on a masonry wall | Engineered | Table R606.12.2.1 lists it as not permitted without design |
| Elevated concrete floors and roofs | Engineered under ACI 318 | No residential prescriptive section exists |
| Two-wythe loadbearing walls | Engineered | R606.13 gives bonding rules, and R606.12.3.1 still requires design in D0 to D2 |
| Irregular buildings | Engineered for the irregular story or portion | R301.2.2.6 (Code below) |
| Ground snow over 70 psf | Engineered | R301.2.3 |
| Retaining walls over the code's height and load triggers | Engineered | R404.4 |
| Footings on fill, on soil the official judges under the clay value, or at bearing above the presumptive table | Engineered, or a soils investigation | R401.2 and Table R401.4.1, footnote b |
| Expansive soil | Designed under Section 1808.6 of the Building Code | R403.1.10 |
| Post-tensioned or prestressed elements | Engineered | No prescriptive provision |
| FRP reinforcement | Engineered, and GFRP excluded in D0 to D2 | ACI 440.11 |
| Steel beams under concrete floors | Engineered, or manufacturer-stamped where the jurisdiction accepts it | Local practice |
| A mezzanine over one-third of the room below | Counted as a story | R325.3 |

Four things need no engineer. R608 concrete walls at a Category C site inside R608.2's limits, one story of masonry with the code's minimum reinforcement and no more than 9 feet between lateral supports, footings on the presumptive bearing values, and manufacturer-engineered trusses and I-joists, whose stamp is the engineering. Concrete floors or a concrete roof on any of them remove the exemption, because the prescriptive masonry and concrete sections assume light-frame floors and roofs above.

Massing choices are priced inside the engineered path, not as the loss of a free path. The seismic category has already removed the free path on a western Oregon site, so a recess or an offset volume costs analysis and detailing rather than a change of path. GFRP bar is a different case. Seismic category excludes it from the shell outright, because the bar is linearly elastic to failure and supplies none of the post-yield redistribution the higher categories assume (Code below). At a Category C site the structural walls, which are the seismic force-resisting system, would still exclude it.

Weighting durability as heavily as the load path does not change the path. The strongest durability options either need an engineer regardless (targeted stainless bar, a water-retaining structure designed to ACI 350) or are unavailable in the likely categories (GFRP), and they refine the material specification inside whichever path is chosen. One exception is narrow. An element that qualifies for the prescriptive path on load grounds alone, but carries a severe exposure class, can tip toward engineered treatment, because the prescriptive cover and mix assumptions were not written for severe exposure.

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

A large floor opening, or wood bracing in a masonry story, is also an irregularity.
  An opening exceeding the lesser of 12 feet or half the least floor or roof dimension between braced wall lines, and any story braced partly by wood or steel framing and partly by masonry or concrete walls.
  Source: ORSC R301.2.2.6 (2023 edition).

Prescriptive concrete walls under R608 are limited to low seismic categories, two stories and light-frame floors and roofs.
  Detached dwellings in Category A, B or C, two stories, a 60-foot plan, 32-foot floor and 40-foot roof spans, 10 psf floor and 15 psf roof dead loads, and 136 mph in Exposure C.
  Source: ORSC R608.2 (2023 edition).

A masonry wall under a second story is not a prescriptive element in Seismic Design Category D0 to D2.
  Solid wall length of 25 percent of the plan dimension in D0 and D1 and 30 percent in D2 for a one-story wall, and no prescriptive wall under a second story of any kind.
  Source: ORSC Table R606.12.2.1 (2023 edition).

Prescriptive story height is capped by wall material.
  13 feet 7 inches of story height and 12 feet of bearing-wall clear height for masonry, 8 feet more at a gable end, and 11 feet 7 inches of story with 10 feet unsupported for ICF walls.
  Source: ORSC R301.3 (2023 edition).

GFRP reinforcing bar is excluded from the high seismic design categories.
  All members in Category A, members outside the seismic force-resisting system in B and C, no structural member in D, E or F, and under ICC-ES AC454 only A and B.
  Source: ACI 440.11-22; ICC-ES AC454.
```

## 6.4 Concrete walls

**Simple**

A poured concrete wall is steel bars inside a solid slab of concrete stood on edge. The bars take the pulling forces concrete cannot, and the concrete protects the bars and carries the pushing forces. Three things decide how long it lasts: the concrete over the steel, the density of the mix, and where the shrinkage cracks open. Concrete shrinks as it dries, so a long wall cracks somewhere. A control joint is a straight groove cast into both faces that tells the crack where to be. Below ground, each joint gets a rubber or plastic strip cast across it, so water cannot follow the crack through the wall.

**Applied**

1. Have the engineer set the control-joint spacing from wall height, reinforcement and restraint before the forms are built.
2. Place a joint at every change in wall height or thickness, at offsets and intersections, and beside openings, never through them.
3. In any wall that holds back water, cast a PVC, rubber or bentonite waterstop across each joint.
4. Seal the exposed groove of every joint with backer rod and sealant.
5. Cross-check each wall's bar spacing and joint spacing against that wall's exposure class before the drawings go to permit.

**Professional**

ACI 318-19 is the general structural concrete code and the edition the 2023 residential code references, with ACI 318-25 now in circulation. ACI 332-20 is the residential concrete code, with prescriptive tables for footings, foundation walls, slabs on ground and above-grade walls within its scope, and a chapter on design for expansive soils. PCA 100-17 is the prescriptive manual the residential code names for above-grade concrete walls outside Category C, and it requires an explicit showing of compliance with its own tables. R608, the code's prescriptive section for above-grade concrete walls, assumes light-frame interior walls, floors and roofs. The table below gives the planning values an engineered exterior wall on this house starts from.

| Parameter | Planning value |
|---|---|
| Wall thickness | 8 inches minimum, 10 to 12 inches for taller walls or higher seismic demand |
| Concrete strength, f'c | 3,000 psi minimum, 4,000 psi for above-grade exterior walls, 5,000 psi for retaining walls and other high-stress elements |
| Reinforcing grade | Grade 60 to ASTM A615, or ASTM A706 low-alloy bar where seismic ductility governs |
| Vertical bars | No. 4 or No. 5 at 12 to 24 inches on center, two curtains in thicker walls |
| Horizontal bars | No. 4 at 12 to 24 inches on center, two curtains in thicker walls |

### Control joints and crack control in long walls

Concrete shrinks as it dries, and a long wall with no joints cracks at random. A control joint is a plane deliberately weakened by a groove tooled or formed into both faces, and the shrinkage crack forms there instead. The Bureau of Reclamation's 2016 joint-spacing reference and the trade practice built on ACI 224R space vertical joints at 2 to 3 times the wall height, with an outer bound near 10 to 12 feet for residential wall heights. The engineer sets the actual spacing from wall height, reinforcement ratio, restraint and expected shrinkage strain. Joints also go where stress concentrates regardless of spacing: changes in wall height or thickness, offsets and intersections, beside window and door openings, and re-entrant corners.

Joints and shrinkage steel do two different jobs and are set together. The distributed horizontal bars do not prevent shrinkage cracking. They limit the width of the cracks that form between joints by spreading the strain across many fine cracks. Joint layout sets where the wall relieves its stress, and bar spacing sets how wide each crack opens, so closer bars and closer joints trade against each other in one calculation. ACI 318-19 controls flexural crack width through the bar-spacing limit of section 24.3 rather than a calculated width. ACI 224R-01 lists guide crack widths by exposure, from dry air to water-retaining service, and is the durability reference behind those spacing limits.

A control joint is a deliberate discontinuity and a potential leak path. In a wall that resists water, a below-grade foundation wall, a retaining wall or a cistern wall, each joint takes a PVC, rubber or bentonite waterstop cast into it, and the exposed groove is sealed with backer rod and sealant so surface water cannot track to the bar. Above grade on a dry wall, a tooled or formed joint without a waterstop is the standard detail.

The exposure class is assigned wall by wall. A wall in sustained ground contact, or one facing wind-driven rain, can carry a more severe class than the rest of the house, and its bar spacing and joint layout are checked against that class rather than against the house-wide table. At any wall classed severe, the shrinkage-and-temperature steel is checked against the minimum ratios in ACI 318-19 Table 11.6.1 at that wall (Code below).

**Code**

```
Cast-in-place walls carry minimum distributed reinforcement in both directions.
  0.0012 longitudinal and 0.0020 transverse of the gross concrete area for deformed bars No. 5 and smaller with 60,000 psi yield, and 0.0015 and 0.0025 for other deformed bars.
  Source: ACI 318-19 Table 11.6.1.

Concrete foundation walls under above-grade concrete walls are engineered in the high seismic categories.
  In Seismic Design Category D0, D1 or D2 such walls comply with ACI 318, ACI 332 or PCA 100, while plain walls under light framing stay within 8 feet of height and 4 feet of unbalanced backfill.
  Source: ORSC R404.1.4.2 (2023 edition).
```

## 6.5 Alternative forming systems and mixes

**Simple**

There is more than one way to form and mix a concrete wall. The default here is rented or job-built forms that come off after the concrete cures. Stripped forms can be reused, and the bare face can be inspected before anything covers it. Each alternative changes one variable. Foam forms stay in the wall and double as insulation. A flowable mix fills the forms without vibration. Tensioned cables replace some ordinary bar in a long floor span. Fibers in the mix control the fine early cracks. A mix with fly ash or slag in place of some of the cement is denser and slower to harden, and it is the mix this house uses.

**Professional**

| Option | What it changes | Trade-off against the default |
|---|---|---|
| Insulated concrete forms (ICF) | Stay-in-place foam forms combine formwork and continuous insulation in one trade sequence | The product line fixes the wall thickness and insulation value, and the foam stays in the wall, so the concrete face cannot be stripped and inspected |
| Self-consolidating concrete (SCC) | Superplasticizer admixtures, not added water, produce a mix that flows around congested reinforcement with little or no vibration | Higher cost per yard from the cementitious content and admixture dose, and formwork still designed for full hydrostatic pressure |
| Post-tensioned slab | Unbonded tendons stressed after cure pre-compress the slab, increasing clear span for a given depth over mild-steel reinforcement | Specialized stressing crews and equipment, and any future penetration risks cutting a stressed tendon |
| Fiber-reinforced concrete | Fibers in the mix control plastic-shrinkage cracking and improve impact and abrasion resistance | Supplementary only, because fibers do not replace primary reinforcement |
| SCM-rich low-carbon mix | 20 to 50 percent cement replacement with fly ash or slag densifies the pore structure and reduces embodied carbon | Slower strength gain, with 7 to 14 days of curing before stripping or loading against 3 days for a standard mix |

Self-consolidating concrete removes the vibration-skill dependency behind honeycombing in congested cages, and Denver Concrete Vibrator's technical summary records it consolidating in ICF and other congested-reinforcement walls where stiffer mixes left voids. It does not reduce form pressure. It stiffens slowly during placement, so the form design assumes the full-hydrostatic case. Post-tensioning is not among the floor options this house ranks, because hollow-core precast and cast-in-place slab cover its span range without stressing crews, and a stressed tendon constrains every future penetration through the slab.

ICF is established in low-rise residential and disaster-resistant construction, as PNNL's Building America Solution Center guide records. For this house it trades the default's direct surface inspection and reusable forms for a single combined forming-and-insulation step. The SCM-rich mix is this house's specified durability mix. The same replacement rate that densifies the pore structure gives the largest cut in the mix's embodied carbon, because portland cement production is the dominant carbon dioxide source in concrete.

## 6.6 Reinforced masonry walls

**Simple**

A reinforced block wall is concrete block stacked in mortar with steel inside it. Vertical bars run up through the hollow cores, and horizontal bars run along channel-shaped courses called bond beams. Every core that holds a bar is then filled solid with grout, a soupy concrete that locks the bar to the block. The finished wall is a grid of steel and concrete that does not burn, rot or feed insects. In an earthquake the steel holds the blocks together, and the bond beams hold the walls to the floors and roof. On most western Oregon sites the engineer designs this wall, because the code's own tables stop at one story.

**Applied**

1. Lay the block in running bond, each unit overlapping the one below by half, unless the engineer designs a stack-bond wall.
2. Grout solid every cell that holds a bar, and the whole stem wall where the drawings call for it.
3. Run a bond beam at the top of the foundation wall, at every floor level and at the roof.
4. Add a mid-height bond beam in any wall taller than 12 feet.
5. Use open-end or cut-web units at every bond-beam course, so the horizontal bars run continuous.
6. Leave no cell open for a niche unless the engineer marks it on the wall schedule, and never through a bond-beam or joint-reinforcement course.

**Professional**

On an engineered wall TMS 402 governs the design and TMS 602 the construction. The 2023 residential code references the 2016 editions of both, and the 2022 editions are current, so the drawings name the edition the engineer designed to. The table gives the planning values an engineered wall on this house starts from.

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

The code's prescriptive masonry path in Seismic Design Category D0 to D2 is narrow. R606.12 applies the seismic requirements to masonry and leaves anchored veneer out of them. A wall one story tall, with the code's limit between lateral supports, can be built to the minimum reinforcement without design, on a wood or cold-formed steel diaphragm, and the wall system chapter carries that entry. Everything taller, and everything under a concrete floor or roof, is designed under TMS 402. The code's figures give the anchorage and reinforcement details by category, and the code bars Type N mortar and masonry cement from the lateral force-resisting system because both give the wall less strength and less bond than portland cement-lime or mortar cement mortar.

| Bond beam location | Purpose |
|---|---|
| Top of the foundation wall | Ties the foundation steel to the wall steel above |
| Top of the wall at each floor level | Anchors the floor diaphragm and transfers lateral load into the wall |
| Top of the wall at the roof | Anchors the roof structure or roof diaphragm |
| Mid-height course in a wall over 12 feet tall | Crack control and stiffness |
| Above and below large openings | Carries the forces that concentrate around the opening |

Running bond is the default coursing. Stack bond, with its units aligned and its head joints continuous, has no unit overlap to interrupt a vertical crack, so the code adds horizontal steel in any wall laid with less than a quarter-unit head-joint offset, and more of it in Category D2. The joint reinforcement in the table already meets the lower of those rules without change.

On the prescriptive minimum, only the cells with bars are grouted, and the cells between bars stay hollow. Those are the only candidates for deliberate use as a storage or display niche. A niche cannot interrupt a bond-beam course or a joint-reinforcement course, so the clean placement is a pocket bounded above and below by those courses and on each side by grouted, reinforced cells. The as-designed bar layout controls, because bars concentrate at openings, corners and bond-beam intersections, and the engineer confirms candidate cells from the wall schedule. Where the house adopts solid grouting of every cell, no open cell remains.

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

In a cavity wall, short steel ties cross the gap and hold the brick to the block. Each tie carries a few square feet of brick against wind and shaking, and it spends its whole life in a damp cavity. Two different metals touching in wet mortar pass an electric current between them, and the more reactive one corrodes to protect the other. A zinc coating wired to bare steel is eaten away doing that, and the protection it was bought for is gone. The rule for this house is one metal per wall, bars, chairs and tie wire included, and stainless steel wherever any stainless is used.

**Professional**

The tie's job depends on the wall's classification, and the classification is written on the drawings by name. An anchored veneer carries only its own weight and passes wind and seismic load to the block through the ties. A noncomposite (cavity) wall shares the lateral load between the wythes in proportion to their stiffness, and a composite wall acts as one section through ties or headers designed for shear across the collar joint. The cavity-wall alternative on this house is read as anchored veneer unless the engineer classifies it otherwise, and the wall system chapter carries the veneer tie schedule, the corrosion-protection minimums and the code's cavity limits. For a wall the engineer classifies as noncomposite, the residential code's multiple-wythe rules at R606.13.2 give the table below.

| Tie type in a noncomposite cavity wall | Wall area per tie | Maximum spacing |
|---|---|---|
| Rigid 3/16-inch wire ties | One per 4-1/2 square feet | 24 inches vertical and 36 inches horizontal, with added ties around openings at 3 feet, within 12 inches of the opening |
| Adjustable ties | One per 2.67 square feet | 24 inches each way, with 1-1/4 inches of bed-joint offset at most, 1/16 inch of play, and two 3/16-inch pintle legs |
| Joint reinforcement cross wires, No. 9 gage or heavier | One cross wire per 2.67 square feet | 16 inches vertical |

TMS 402 bars drip bends in wire ties, because the bend lowers the tie's lateral capacity, so the flashing and weeps handle the water that reaches the ties. Stainless ties at the schedule's frequency form point thermal bridges amounting to 0.5 to 1 percent of the wall area, which drops a 4-inch rigid-foam cavity from R-26 to R-23 effective. Thermally broken ties (Halfen FM, Bekaert Murfor THERM, Wagner ThermaTIE) recover most of that loss where the thermal target needs it.

### Mixed metals in one element

Galvanized and black steel in electrical contact inside one element form a documented galvanic couple. The American Galvanizers Association describes the mechanism: once the zinc has depassivated in the concrete's alkaline pore water, it acts as a sacrificial anode for the adjacent bare steel and is consumed protecting it, which defeats the reason the galvanizing was specified. The working rule is one metallurgy per structural element, including chairs, spacers and tie wire, all black, all galvanized or all stainless. Where mixing cannot be avoided, a dielectric barrier goes at the contact point, and the tie wire matches the bar, 16.5-gauge or heavier galvanized wire on galvanized bar and stainless wire on stainless bar.

The stainless-and-carbon couple is a milder case. The Specialty Steel Industry of North America's stainless rebar guidelines find the coupled corrosion rate low enough that distress is unlikely within a 75-year design life, and report that some current practice no longer isolates black bar from stainless bar. This house's design horizon runs past that 75-year study horizon, so the all-stainless rule stands.

### Glass-fiber bar and composite ties

GFRP bar as primary reinforcement is excluded from this shell by seismic category. In the narrow case of an element outside the lateral system at a Category C or lower site, its detailing differs from steel's throughout. A composite-industry vendor's explainers (Composite-Tech) put development lengths at 1.3 to 1.6 times steel's for a comparable force, tension laps at 1.3 times the development length under ACI 440.1R-15, with 40 to 60 bar diameters common in practice, and bond resting on sand-coated or helically wrapped surfaces. Those are planning figures from a secondary source, and the engineer details any GFRP element against the ACI 440.11-22 text itself, hooks included.

FRP ties are not a prescriptive option. ICC-ES AC125 covers externally bonded FRP for strengthening, not new ties. AC454 covers FRP bars in concrete in Seismic Design Category A or B. TMS 402-22 Appendix D introduces composite reinforcement for masonry partition walls, not for loadbearing exterior cavity walls. A commercial FRP tie enters a permit only with a current ICC-ES report and the building official's approval under the code's alternative-materials provision.

## 6.8 Reinforcement detailing: laps, cover, hooks and grout

**Simple**

Steel strengthens concrete only where the two are joined over enough length, and only while the concrete around the bar keeps water away from it. Where one bar ends and the next begins, the two overlap for a set length, so the force passes from one to the other through the concrete between them. The bar also needs a set thickness of concrete between it and the weather, called cover. In a block wall the grout does both jobs, so the grout has to fill every cell completely. Most field mistakes are small and permanent: a bar that settled against the form, a lap a few inches short, a cell with a void. The checks before each pour catch them while they can still be fixed.

**Applied**

1. Measure bar size and spacing against the drawings, bay by bay, before concrete is ordered.
2. Measure cover directly or with a cover meter: 3 inches against earth, 2 inches on any exposed face, 1-1/2 inches inside.
3. Measure every lap and hook, and check that laps are staggered where the drawings stagger them.
4. Support horizontal bars every 2 to 4 feet on plastic or concrete chairs sized to the cover, with no metal chair at an exposed face.
5. Tie every other crossing at least, and every crossing where the crew will walk.
6. Walk the cage for bent or stepped-on bars after the last trade leaves it.
7. Check embeds and sleeves against the structural and mechanical drawings for conflicts with the bars.
8. Have a second person sign the checklist, and photograph the final condition before calling for concrete.
9. Send any field congestion to the engineer as a request for information, and substitute no bar on site.

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

The placement is verified at the footing inspection, the foundation-wall inspection and, for grouted block, before each grout pour. Field placement fails in five recurring ways, each with a known control.

| Failure | How it happens | Control |
|---|---|---|
| Lost cover | Chairs undersized, crushed by foot traffic or concrete weight, or omitted, so bars settle toward the form face, and carbonation and chloride reach the steel sooner than the cover was sized to allow | Plastic or concrete chairs at the specified cover, and cover measured before the pour |
| Congestion | Bars, dowels, embeds and bond-beam steel converging at wall-footing intersections, corners and openings, blocking aggregate and the vibrator | Bar-to-bar clearance checked against the maximum aggregate size at the detailing stage, and field congestion sent to the engineer as a request for information |
| Wrong laps | Laps shorter than the development length, or stacked at one location instead of staggered, concentrating a weak, congested zone at one section | Laps located away from maximum-moment regions on the drawings, never moved in the field |
| Displaced bars | Foot traffic, placement equipment and the pour pushing bars off position | Chairs at close spacing, ties at every other crossing or every crossing in traffic, and a pre-pour walk for bent bars |
| Wrong supports | Chairs sized close to the cover instead of to it, or metal chairs at an exposed face, which become corrosion initiation points | Plastic or concrete-block (dobie) chairs sized to the exact cover |

A missed dowel or anchor bolt is corrected with a post-installed adhesive anchor, and the governing document is product-specific. The hole diameter, depth, cleaning method and dispensing equipment come from the product's ICC-ES evaluation report and the manufacturer's printed instructions it references, never from a generic embedment ratio. Simpson Strong-Tie SET-3G (ESR-4057) is listed for post-installed anchors and reinforcing-bar connections in cracked and uncracked concrete under static, wind and seismic load, and Hilti HIT-RE 500 V3 (ESR-3814) is the equivalent system. The wrong drill-bit diameter, or skipped hole cleaning, voids the tested capacity even where a generic ratio is satisfied, and the crew works from the report current at installation, because reports are revised on renewal.

The bar schedule tops out at No. 5, with No. 6 at isolated heavy locations. Manual benders are rated to No. 6 or heavier by model, manual cutters stop near No. 4, and powered cutter-benders rated to No. 6 or 1-inch bar cut and bend faster at foundation-schedule volume. Rent against buy is decided from the final bar schedule's total footage and local rental rates.

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
  3 inches cast against and in permanent contact with ground, 2 inches exposed to weather or ground for No. 6 and larger bars and 1-1/2 inches for No. 5 and smaller, and 3/4 inch in walls and slabs not exposed.
  Source: ACI 318-19 Table 20.5.1.3.1.

Post-installed anchors and dowels follow their evaluation report.
  Hole diameter, depth, cleaning method and dispensing equipment per the product's current ICC-ES report and the instructions it references, with SET-3G listed for 2,500 to 8,500 psi concrete under ESR-4057.
  Source: ICC-ES ESR-4057; ICC-ES ESR-3814; ORSC R301.1.3 (2023 edition).
```

## 6.9 Formwork, placement defects and cast-in embeds

**Simple**

Fresh concrete behaves as a heavy fluid until it stiffens. It presses outward on the forms, it traps air unless it is vibrated, and it bonds poorly to concrete that has already begun to set. Most placement defects trace to one of those three facts. Honeycomb is a pocket where the mortar never filled between the stones. A cold joint is the weak seam left where a late truck met concrete that had started to harden. A blowout is a form tie that let go at the bottom of the pour, where the pressure is highest. The fixes are the form design, the vibration method and the delivery timing, and all three are settled before the first truck arrives.

**Applied**

### Consolidation and placement

1. Limit free fall to 3 to 4 feet, and use a drop chute or tremie pipe for taller forms.
2. Insert the vibrator on a grid pattern, a few inches into the lift below.
3. Hold each insertion 5 to 15 seconds, until the large bubbles stop rising, then withdraw it slowly.
4. Keep the vibrator away from the form face, and stop before paste rises to the surface.
5. Learn the mix's initial-set time for the day's temperature before the pour, and keep truck intervals inside it.
6. Stage a backup vibrator, and on a pump pour a backup pump.
7. When a lift must stop, stop at a planned construction joint, roughened and doweled or bonded as the drawings show.
8. Treat any bulge in a form as a stop-work signal.

### Forms, before the pour

1. Use a manufactured forming system with the maker's pressure and tie-spacing tables for the pour rate and concrete temperature.
2. Tape, gasket or tight-fit every panel joint.
3. Space the ties tightest at the base of the pour, where the pressure is highest.
4. Brace the panels to the ground or to a finished slab with kickers and diagonals, and walk every brace before the truck arrives.
5. Slow the pour rate in cold weather.

### Embeds and anchor bolts

1. Wire anchor bolts, or a template holding several at spacing, to the tied reinforcement, never to the forms.
2. Check the bolt layout against the sill-plate drawing just before the pour, and recheck position and top-of-concrete elevation as the last truck finishes.
3. Check every embed plate against the structural drawing's location, elevation and orientation.
4. Run a written embed, sleeve and dowel checklist against the structural and mechanical drawings, checked by a second person, before calling for concrete.
5. Photograph the final pre-pour condition of every embed.

**Professional**

Fresh concrete loads a vertical form with a lateral pressure equal to the lesser of full hydrostatic pressure, the unit weight times the pour height, or a reduced value that depends on how fast the mix stiffens. Faster placement and colder concrete both raise the design pressure. ACI 347R, the formwork guide, holds the pressure formulas, and ACI Committee 347 recommends a factor of safety of 2.0 on form ties, as the For Construction Pros series by KB Engineering reports. The exact coefficients sit in the purchased guide, and the forming system maker's published tables are the working reference on site.

Blowouts are tie failures far more often than panel failures. A tie under-specified or over-spaced for the actual pressure lets go near the base of the pour, its load shifts to the neighboring ties, and the failure unzips upward. Bulging means the tie-and-wale system is consuming its safety margin. Misalignment traces to external bracing that transfers horizontal thrust poorly, so the whole form assembly walks during the pour instead of deflecting and springing back.

Honeycomb, the stony pockets where mortar failed to fill between coarse aggregate, has five documented causes in Graniterock's technical notes on surface defects:

- congested reinforcement in narrow forms
- segregation from excessive free fall
- a fine-to-coarse aggregate ratio that leaves too little mortar
- a mix too stiff to flow around the bars
- consolidation that levels the concrete without finishing the release of trapped air

Sand streaking, a sand-rich and cement-poor smear on the formed face, comes from bleed water migrating up the form face and washing out paste, and an air-entrained mix bleeds less and streaks less. Cold-joint prevention is scheduling. Retarders extend the set window in hot weather, accelerators shorten it in cold weather, and the delivery interval is planned around the window the day's mix has.

Where an anchor bolt is missed despite the checklist, a post-installed anchor corrects it. A missed or misoriented embed plate is more consequential, because a plate is a unique engineered connection, and correcting one means cutting and doweling new work rather than substituting an anchor. Both are documented as corrections, never planned as practice. The sill-plate anchor rules, the footing reinforcement and the grounding electrode cast into the footing are the foundation chapter's, and that chapter's pre-pour list is where those items are checked.

## 6.10 Openings: lintels and diaphragm continuity

**Simple**

Every opening cuts a path the loads were using, and something has to carry them around it. Over a window or door, a lintel does that: a steel angle, a precast concrete beam, or a block course filled with grout and bars that spans the gap. Its ends must rest far enough onto solid, grouted block to pass the load down. A stair opening does the same thing to a floor, and a floor also works as the house's horizontal earthquake brace. Bars cut by the opening are replaced around its edges. Past a certain size, one hole puts the whole story into engineered design.

**Applied**

1. Have the engineer size every lintel in the block wall from the load above it.
2. Bear each lintel at least 4 inches on cells grouted solid, in a full mortar bed.
3. Run the bond beam's bars past each opening for the development length the drawings give.
4. Add the trim, diagonal and chord bars around each slab opening as drawn, before the pour.
5. Keep stair openings under the irregularity threshold, or have the engineer design the story's diaphragm with chords and collectors.

**Professional**

Masonry over an opening rests on a steel lintel, a reinforced concrete or masonry lintel, or an arch, each designed for the load it carries (Code below). Three lintel types serve the block wall: a steel angle or fabricated beam, a precast reinforced concrete lintel, and a reinforced grouted lintel block, U-shaped units carrying bars and grout. CMHA's Lintel Design Manual TR91B tabulates load-rated spans for the masonry types, and its TEK 14-08B gives the bearing minimum that TMS 402 sets. Bearing ends land on solidly grouted cells, and the number of grouted jamb cells and any jamb bars follow from the lintel's end reaction. A 10-foot-class opening, the garage or barn door case, carries roof, wall and snow load that puts the lintel past a nominal angle and into a sized steel member or a published-table masonry lintel. Steel-angle lintels under the brick veneer have their own span table in the residential code, stated in the wall system chapter.

In a cast-in-place slab diaphragm, the bars the opening interrupts are replaced beside it, half above and half below the opening at the slab edges. The engineer's typical detail adds two No. 5 diagonal bars at each corner with a 4-foot lap into the uninterrupted slab, continuous chord steel along the opening's edge of No. 5 at minimum with a 40-bar-diameter lap, and the slab's minimum reinforcement ratio throughout. ACI 318-19's one-way and two-way slab chapters and its diaphragm chapter govern those details. In a block wall, a bond beam interrupted by an opening takes supplementary bars developed on each side of it, two No. 5 at minimum with a 48-bar-diameter lap, and the continuous bars above and below the opening extend 24 inches past its edges. A stair opening longer than the irregularity threshold puts the whole story into engineered design, with collector and chord reinforcement in place of a trim detail.

**Code**

```
Masonry over an opening bears on a designed lintel or arch.
  A steel lintel, a reinforced concrete or masonry lintel, or a masonry arch, designed to support the load imposed.
  Source: ORSC R606.10 (2023 edition).
```

## 6.11 Floor systems

**Simple**

A floor here can be concrete poured in place, factory concrete planks craned into position, concrete over steel, or factory-engineered wood. Concrete floors last as long as the walls and need the engineer. Wood floors are the low-cost prescriptive route and have the shortest life. For the engineered shell the default is hollow-core plank: factory-cast concrete slabs with round voids through them, set by crane and topped with a thin layer of poured concrete that ties them together. A bare concrete floor is loud underfoot in the room below. A floating finish floor over a resilient mat fixes that without touching the structure.

**Applied**

1. Size each span early at a depth of span over 24 for a cast-in-place slab and span over 40 for hollow-core.
2. For a 24-foot span, plan a 12-inch cast-in-place slab or an 8-inch hollow-core plank.
3. Confirm crane access and delivery turning room for planks before the floor system is fixed.
4. On the prescriptive path, file the joist or truss maker's evaluation report and span tables with the permit.
5. Over any occupied room, specify a floating finish floor on a resilient underlayment with the interior finishes.

**Professional**

| Path | Description | Strengths | Limits |
|---|---|---|---|
| Cast-in-place reinforced concrete one-way slab | A 6- to 10-inch slab on bond beams or steel beams, No. 4 or No. 5 bars in two directions to the ACI 318 minimums, continuous into the walls | Highest mass, longest design life, the best fire and sound performance, one material with the walls | Significant formwork, engineered design, long pours |
| Hollow-core precast planks with a 2- to 3-inch topping | 6- to 12-inch planks, designed and stamped by the manufacturer, with a cast-in-place topping for diaphragm continuity | Fast erection, comparable longevity, the industry standard for concrete houses, spans of 16 to 32 feet | Engineered for the project and stamped by the maker, with crane and delivery access required |
| Composite concrete on metal deck over steel beams or bar joists | A 3-1/2- to 6-inch topping on composite deck, on W-section beams or bar joists | Long spans, easy mechanical chases, reasonable cost | Steel enters the structural shell, with a 50- to 75-year structural design life as drawn |
| Manufacturer-engineered wood I-joists | 9-1/2 to 16 inches deep, to the maker's span tables, continuous over bearing walls or beams | Lowest cost, fast install, the maker's stamp carrying the engineering | Wood, with a shorter design life and vulnerability to fire and water |
| Manufacturer-engineered wood floor trusses | 12 to 24 inches deep, open web, designed and stamped by the maker | Long spans, integrated mechanical chases, the maker's stamp | Wood, with the same vulnerabilities as I-joists |

For the engineered shell, hollow-core precast is the primary path at spans of 16 to 32 feet, and the cast-in-place one-way slab is the alternative at shorter spans where single-material formwork is simpler than a crane day. The PCI Manual for the Design of Hollow Core Slabs and Walls is the industry design manual behind the planks, and the maker's stamped shop drawings and erection sequence go in the permit file. Elevated structural slabs are designed under ACI 318-19's one-way and two-way slab chapters, never under the slab-on-ground provisions of ACI 332-20. On the prescriptive path, wood I-joists or open-web wood trusses are the default, and the owner submits the maker's product evaluation report and span tables with the permit, the stamp doing the engineering.

A bare concrete slab performs poorly against footfall. Commercial Acoustics' and AcousPlan's rating guides put a bare 4-inch reinforced slab near Impact Insulation Class 25 and a bare 8-inch slab near 28, so footsteps on an unfinished concrete floor are audible in the room below. The correction is a floating finish floor on a resilient underlayment of rubber, cork or a rated acoustic mat, which decouples the walking surface from the slab. A resilient mat under a hard finish reaches a class of 50 to 60, and underlayment plus carpet 65 to 75, with each product publishing the points it adds over the bare slab. The assembly changes nothing in the structural slab, and the interiors chapter selects it with the finishes.

**Code**

```
On the prescriptive masonry path, the floor and roof diaphragms are wood panels on wood or cold-formed steel framing.
  Wood structural panels fastened to wood framing per Table R602.3(1), or to cold-formed steel floor or roof framing per Tables R505.3.1(2) and R804.3, with blocked panel edges.
  Source: ORSC R606.12.1.1 (2023 edition).
```

## 6.12 Roof structure

**Simple**

Your roof is two things with two lifespans. The structure that holds it up should last as long as the walls. The weather surface on top is replaced two or three times in a century. The design keeps them separate so the second never damages the first. On a concrete deck the membrane comes off and goes back on without touching the structure. Oregon's roof collapses on record broke at the connections under drifted snow, not in the framing, which is why the connections get the engineer's attention here.

**Applied**

1. Have the engineer check drift at every parapet, valley and roof step against the load standard's drift provisions.
2. Slope a concrete deck at least 1/4 inch per foot to drains, with an overflow for each drained area.
3. For the truss option, read the required uplift from the code's table, and select a connector rated at or above it.
4. Where the house deck meets a separate structure's metal roof, run an expansion joint from roof to foundation, with an 8-inch roof curb.
5. Cast in anchor plates for future solar racking, or plan ballasted racks that need no penetration.

**Professional**

| Path | Description | Design life of the structure | Design life of the weather surface | Fit |
|---|---|---|---|---|
| Concrete deck with a protected membrane roof (PMR) | An 8-inch cast-in-place slab or hollow-core with a 2- to 3-inch topping, a fully adhered modified-bitumen, EPDM, TPO or PVC membrane, 4 to 6 inches of XPS or polyiso above it, and river-rock or paver ballast | 100 years and more | 30 to 50 years for the membrane, replaceable without disturbing the structure | The primary roof, engineered |
| Concrete deck under a sloped wood-framed false roof | The same deck, with treated sleepers carrying a 3:12 to 6:12 frame under metal or slate | 100 years and more | 50 to 70 years for 24-gauge standing seam, 75 to 150 for natural slate | The alternate where slope is wanted, engineered, at higher cost |
| Wood truss roof on the bond beam | Manufacturer-engineered trusses at two-foot spacing, bearing on the bond beam | 50 to 80 years for the truss assembly | 50 to 70 years for metal, 15 to 30 for asphalt shingle | The prescriptive option, with the maker's stamp carrying the engineering |

Asphalt shingles are rejected on both paths, because a 15-to-30-year surface does not belong on a shell with a multi-century life. A flat concrete deck slopes to drains at every low point, carries an overflow wherever a parapet could trap water, and is checked for ponding instability under ASCE 7-16 section 8.4. The roof system chapter holds the assembly, the parapet and edge detail, and the drainage design. On a concrete deck, future solar racking is either cast-in anchor plates set at design time or ballasted racks on the finished membrane roof, which add no penetrations and whose foot loads are checked against the insulation's compressive strength.

On the truss option the code's uplift table gives the force each truss-to-wall connection must resist, by wind speed, exposure, spacing, span and pitch. At or under the table's threshold the standard fastening schedule serves without a rated connector, and above it a load-rated tie is selected from the maker's evaluation report. Every Oregon county's design wind speed falls within the table's range, so catalog hardware meets the demand outside the special wind regions. Inside one, or anywhere on the engineered path, the connection design moves to the engineer with the rest of the roof.

### Oregon snow failures on record

Three documented collapses set the design lesson. An east Multnomah County warehouse failed in December 2008, with 3 to 5 feet of drifted snow at the parapets and 2 to 3 feet over the field, and 24 trusses came down. Rad, Afghan and Lewis's 2018 forensic report, from Portland State University, found load above the design load, drift against tall parapets beyond the design assumption, construction defects and progressive collapse as each failing truss shed load to its neighbor. Of the failed trusses, 18 failed at connection welds and 6 by concrete breakout at the connection. A northern Oregon manufacturing plant lost 80,000 square feet of a 400,000-square-foot roof in November 2014 under snow, freezing rain and temperatures near minus 20°F, as StructureMag's article on the collapse records. North Medford High School's gymnasium roof collapsed in 2025 under a reported 350 tons of snow, per KOIN and KGW.

The documented mechanism is connection margin and drift load at parapets and roof discontinuities, not the framing material. A concrete deck has no truss connections to fail, and the truss option is manufacturer-engineered with its connections inside the stamped design, against the site's ground snow load from the lookup. The engineer checks drift at every parapet, valley and roof step in the actual geometry, because the 2008 collapse followed drift beyond the design assumption.

### Where a concrete deck meets a metal roof

An expansion joint is standard where the main house's concrete deck meets a standing-seam metal roof over an attached but structurally separate garage or shop. Nystrom's roof-to-roof joint guidance and the IIBEC Ohio Valley fact sheet on roof decks each name two conditions that require it, and both are present here: a change of deck material, and a heated building meeting an unheated one. The joint runs from rooftop to foundation with parallel structural elements on each side, so each section moves on its own, and a roof-level cover alone does not decouple the two structures. The roof-level detail is a raised curb with a flexible cover spanning the gap. Whether the wall-to-wall connection needs the same full-height treatment is set when the attachment is designed.

Gutters, downspouts and any first-flush diverter fail by freezing while full of water, not by structural overload. Their sizing and freeze protection are part of the rainwater-catchment design, ice dams at the eave trace to roof heat loss rather than to the structure, and snowmelt adds to the annual catchment yield on a delayed schedule at lower peak flow than rain.

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

A service layer is a hollow space between floors that carries the pipes, wires and ducts. The code sorts any such space by its height and by how people get into it, and the sorting decides which rules apply. A shallow sealed space reached through panels is a concealed space. A space tall enough to walk into, with a ladder and lights, is a story in its own right. Anything in between is argued over at plan review, and the argument slows the permit. This house uses one of the two clean cases and nothing in between.

**Professional**

The residential code defines a story from floor surface to floor surface and sets its own rules for habitable space, under-floor space, concealed space and mezzanines (Code below). A service layer falls into one of them by its clear height and its access.

| Classification | What it is | Consequence |
|---|---|---|
| Habitable space | Space used for living, sleeping, eating or cooking | The ceiling-height, light, ventilation, escape and heating rules apply, so a service layer is never classified habitable |
| Under-floor or crawl space | Space below the lowest occupied floor, entered through a sized access opening | Ventilation or conditioned-crawl provisions, a ground vapor retarder, no heating |
| Concealed space | Space that is not occupied and is entered only for inspection or maintenance | Fireblocking and draftstopping where the construction is combustible, and the mechanical code's material limits where it serves as a return-air plenum |
| Mezzanine | An intermediate level within a room, under the code's area limit | Part of the room below, not a separate story |

Where a service layer is large enough for a person to enter, some building officials classify it as a mezzanine, an attic or a story, and the classification is argued case by case. Two classifications avoid the argument. The first is a concealed plenum of 30 inches clear or less, reached only through removable panels, with no story consequence. The second is a conditioned mechanical level of 4 feet clear or more, with ventilation, lighting and a permanent ladder or stair, counted as a story and designed as one. The band between them is the plan's own threshold, not a code number, and the house picks one of the two.

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

Concrete fails over decades for two main reasons. Water reaches the steel and rusts it, and rust takes up more room than steel, so it cracks the concrete from inside. Freeze and thaw cycles pry at any water trapped in the pores. Long-life concrete counters both. The mix holds less water, plus fly ash or slag that keeps filling the pores for years. The steel gets more concrete over it, and the curing runs a week or two instead of three days. One trade-off comes with the dense mix. In a fire it can spall, because steam cannot escape through it, and a small dose of plastic fibers gives the steam a way out.

**Applied**

1. Ask the concrete supplier for the aggregate source's alkali-silica service record and any test reports.
2. Order an ASTM C1567 test on the actual aggregate, cement and SCM dose before the mix design is final.
3. Raise the SCM dose or change the SCM where the test result requires it.
4. File the result in the binder with the mix submittal.
5. Have the engineer assign an exposure class to every element from the geotechnical report, and show it on the drawings.
6. Specify polypropylene monofilament fibers in the fire-exposed structural elements the engineer names.

**Professional**

ACI 318-19 organizes concrete durability by exposure class, and the mix parameters scale to the most severe class an element carries.

| Exposure | Classes | Concern |
|---|---|---|
| Freeze-thaw | F0 none, F1 moderate, F2 severe, F3 severe with deicing salts | Frost damage in saturated freeze-thaw cycling |
| Sulfate | S0 to S3 | Sulfate attack on the cement paste |
| Water | W0, W1 in contact with water, W2 where low permeability is required | Permeability and water transmission |
| Corrosion | C0, C1, C2 severe with chlorides | Reinforcement corrosion in chloride environments |

Above grade in mild exposure, an Oregon long-life house takes F1, S0, W0 and C1. Below grade in contact with soil that may be aggressive, it takes F1 or F2, S1, W1 or W2, and C1 or C2 by the chloride exposure. Footings and below-grade walls are the elements that can reach the severe classes, and their classification comes from the geotechnical report's soil and groundwater chemistry. Above-grade walls take the mild baseline. Two elements are classified separately at design time: an exterior-exposed slab edge sits closer to the below-grade condition than to the interior baseline, and any water-retaining structure is classified on its own. A severe class does not itself call for corrosion-resistant bar. The exposure-class system is calibrated for uncoated steel with mix and cover as the primary protection, and coated or stainless bar is an added layer where the measured chloride exposure makes mix and cover insufficient for the target life, as the durability chapter sets out.

### The five mechanisms

Carbonation is atmospheric carbon dioxide reacting with the alkaline hydration products and lowering the pore-fluid pH. When the carbonation front reaches the bar, the passive oxide film that protects steel at high pH breaks down and ordinary corrosion begins. The rate scales with permeability, so a low-w/c, well-cured mix slows it. Chloride ions diffuse through the pore structure, and at a threshold concentration at the bar they break down the passive film locally, even without carbonation, producing pitting that is harder to detect than uniform corrosion. Low w/c and SCM densification slow the diffusion, and added cover lengthens the path.

Sulfates from soil or groundwater react with calcium aluminate hydrates to form expansive ettringite and gypsum, which crack the paste from within. That attack is on the paste, not the steel, and Type II or V cement or SCM replacement is the response for the S1 to S3 classes. In alkali-silica reaction, cement alkalis react with reactive silica in some aggregates to form a gel that absorbs water and expands, with map cracking as the classic symptom, and the reaction is aggregate-specific. Freezing water expands near 9 percent, and the hydraulic pressure fractures paste over repeated cycles. Entrained air voids give the expanding water relief space, which is the air-content requirement in the F1 to F3 classes. In the field the mechanisms couple: freeze-thaw cracking opens new chloride paths, so measured deterioration runs faster than the single-mechanism rates.

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

Alkali-silica control is tested, never assumed. ASTM C1567 is an accelerated mortar-bar test of the project's own aggregate, cement and candidate SCM dose together, read against the standard's expansion threshold (Code below). Shafaatian and others' 2013 study of fly ash in that test put the minimum effective replacement at 15 to 35 percent by ash source, through alkali dilution and binding, reduced transport and altered gel chemistry. That range sits largely inside the fly ash and slag replacement the mix already specifies, and the overlap is not proof for this house's materials. Where the test requires a higher dose or a different SCM, the mix specification changes to match.

### Fire spalling, the dense mix's trade-off

Heated concrete generates internal vapor pressure as pore water vaporizes, and a low-permeability concrete cannot vent it fast enough, so a surface layer detaches violently. NIST's overview of high-strength concrete at high temperature and the 2022 critical review of fire spalling in high-strength concrete both record explosive spalling in the 250 to 400°C range, name permeability as the governing variable, and find that raising the w/c ratio reduces the risk, the opposite direction from every other durability rule. The 4,000-to-5,000 psi, 0.40-to-0.45 w/c, SCM-densified mix is therefore the susceptible profile. The exposure that matters is a structural element under sustained fire that must still carry load afterward: the structural walls and any structural floor or roof slab. The documented mitigation is polypropylene monofilament fibers at low dosage, in the low single-digit pounds per cubic yard, which melt in fire and leave fine channels that vent the vapor gradually. That is a separate application from shrinkage-control fibers, no substitute for any reinforcement, and specified for the fire-exposed structural elements the engineer names.

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

Fibers mixed into concrete are short strands of steel or plastic spread through the whole batch. They hold closed the fine cracks that open in the first days, they toughen a floor against dropped tools, and in a fire the plastic ones melt and let steam out. What they cannot do is replace the steel bars. A bar carries a known pull along a known line, and a fiber carries a little in every direction. On this house fibers are an addition to the reinforcement in slabs and fire-exposed elements, never a substitute for it.

**Professional**

ACI 544.4R-18 draws the boundary. Fibers can supplement and reduce conventional reinforcement where continuous reinforcement is not essential to safety and integrity: slabs on ground, pavements, overlays, shotcrete linings, slabs on piles and some precast units. They do not replace primary flexural reinforcement in residential structural members under the code. Industrial slab-on-ground design uses fiber concrete as primary reinforcement under ACI 360R and the United Kingdom's TR 34, and ACI 318-19 admits steel fibers as minimum shear reinforcement in a narrow class of beams (Code below). For the structural shell, fibers are supplementary.

Three uses fit this house. Macro-synthetic or steel fibers at 3 to 7 pounds per cubic yard go into slabs on ground for plastic-shrinkage control, impact and abrasion resistance, and as a supplement to temperature-and-shrinkage steel, with the primary reinforcement, No. 4 at 16 inches each way in a typical residential slab, still placed as the engineer specifies. Steel fibers at 25 to 50 pounds per cubic yard serve as designed shear reinforcement only in an element the engineer designs for it. Polypropylene monofilament fibers at low dosage go into the fire-exposed structural elements for spalling mitigation. No submittal for this house states that fibers replace bars, that no reinforcing is required where fibers are used, or that fiber concrete removes the need for primary reinforcement.

**Code**

```
Steel fibers may serve as minimum shear reinforcement only within fixed limits.
  Normalweight concrete with an f'c of 6,000 psi or less, a member depth of 24 inches or less, factored shear under the limit the table sets, and the fiber mix accepted by flexural test.
  Source: ACI 318-19 Table 9.6.3.1 and section 26.12.7.1.
```
