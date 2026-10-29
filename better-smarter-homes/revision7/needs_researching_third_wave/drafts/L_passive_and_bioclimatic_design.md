# Wave 3 Pre-Research, Domain L: Passive And Bioclimatic Design

Agent L. Scope: using the sun, the site, and the concrete mass to cut the heating, cooling, and daylighting load before any mechanical equipment, PV array, or battery bank is sized. Covers solar orientation and building form, passive solar heating, daylighting, natural ventilation and night flushing, shading, comfort from radiant mass, and Passive House / superinsulation principles adapted to a high-mass concrete house.

**Manuscript chapters read before writing this file:** Envelope, Waterproofing, Thermal Performance, and Radon (sections 8.2 energy compliance, 8.4 wall insulation strategy, 8.7 roof assembly, 8.8 windows and doors, 8.14 ventilation coordination); HVAC, Ventilation, Humidity, and Air Quality (13.2 heating/cooling selection, 13.4 whole-house ventilation, 13.9-13.10 radiant floor and radiant cooling, 13.15 outage behavior and energy independence); Structural System and Concrete Design (6.1 structural goal); Land, Site, and Feasibility (3.2 climate and design loads, 3.7 topography/drainage/buildability); Interiors, Finishes, Accessibility, and Livability (14.2 room geometry, light, and ventilation).

**Sibling drafts checked:** D_problems_solutions_structure_envelope.md and E_problems_solutions_mep_energy_interiors_site.md, both grepped for passive/solar/shading/daylighting/thermal-mass/ventilation overlap. Two near-misses, noted so the merge step does not read them as duplicates: D's Q40 covers roof overhangs sized to protect masonry walls from wetting (a moisture-durability question), not solar shading; E's E29 covers the *control-system* answer to radiant-slab overheating (outdoor reset, slab sensors, low-mass alternative), which is the mechanical-side response to a problem this file's shading and glazing-ratio questions attack from the design side, before the control system has to compensate. E's E57 covers the *radon* passive stack, an unrelated use of the word "passive." No sibling draft covers solar orientation, glazing-ratio sizing, daylighting, natural ventilation, night flushing, or shading design; this is genuinely new ground.

**Proposed placement and section outline for a new chapter, "Passive and Bioclimatic Design":** the questions below assume a new chapter that sits early in Part II ("The House, System by System"), directly after Land, Site, and Feasibility and before Structural System and Concrete Design. The reasoning: orientation, building form, glazing ratio, and shading are whole-house design decisions made before the structural layout, the wall system, the envelope detailing, and the HVAC/solar equipment sizing are finalized, and the assignment's own framing is to cut the mechanical load before equipment is sized. A proposed section outline, for the structure-shaping step (R7-3), not a commitment:

1. Site and sun: reading the parcel's solar access (carries forward from Land, Site, and Feasibility)
2. Building form and orientation
3. Passive solar heating: glazing ratio, thermal mass, and the three system types
4. Daylighting
5. Natural ventilation and night flushing of the mass
6. Shading
7. Comfort from radiant mass and the adaptive comfort model
8. Passive House and superinsulation principles applied to a high-mass house
9. Feeding a reduced load into the structural, envelope, HVAC, and solar chapters

---

## Part 1: Gathered Understanding

### 1. Oregon and Willamette-Latitude Climate Context

- The project's likely site latitude band, the Willamette Valley corridor, runs about 44-45.6 degrees north: Eugene 44.12N, Salem 44.92N, Portland 45.60N (unverified; general geodata sites). The envelope chapter already states the governing climate zones: 4C marine west of the Cascades, 5B continental east.
- Winter cloud cover in the Willamette Valley is heavy: one general climate summary reports average cloud cover above 80 percent in the coldest months, about 26 cloudy days in a typical January, and as few as 4-5 hours of sunshine per day in winter (unverified; general regional climate summary sites, not a primary NOAA dataset). This matters directly for passive solar sizing: a design rule calibrated to a sunnier climate will overstate what this site's winter sun can deliver.
- Statewide solar insolation figures found: roughly 4.03 average sun-hours per day statewide, about 4.63 for the Portland area (unverified; solar-industry marketing sources, not NREL's National Solar Radiation Database directly). A direct NSRDB or PVWatts pull for the actual parcel coordinates would replace this with a verified number.
- Summer is a different climate: long daylight hours, clearer skies away from the coast, and the 2021 Pacific Northwest heat dome (Portland reached 116 degrees F) showed the region's historical assumption of "no air conditioning needed" no longer holds. One attribution study is reported to credit roughly 2 degrees F of that event to climate change, with future recurrence projected to rise sharply under continued warming (unverified; USDA Climate Hub and general news coverage). This raises the stakes on shading and night-flush design, not just winter solar gain.
- The Oregon coast and the Coast Range carry a persistent summer marine fog layer that reduces solar access near the coast even in the warm season (unverified; general regional climate sources). A coastal or near-coastal site needs its own solar-access check independent of the valley numbers above.
- Cold-air pooling in valley and basin sites, and increased wind exposure on ridgelines, are already documented in the Land, Site, and Feasibility chapter's Topography, Drainage, And Buildability section; this file's site-analysis material builds on that rather than repeating it.
- Prevailing wind in the Willamette Valley is reported to align north-south with the valley's own terrain (unverified; general climate-station summaries); a seasonal breakdown (summer vs. winter prevailing direction) was not found in this research pass and is a real gap.

### 2. Solar Geometry And Site Analysis Method And Tools

- Basic solar altitude formula found in multiple passive-solar design sources: the sun's altitude at solar noon on the winter solstice is approximately 90 minus the latitude minus 23.5 degrees; on the summer solstice it is approximately 90 minus the latitude plus 23.5 degrees. Applied to a Willamette Valley latitude near 45 degrees (unverified computation, pending the actual parcel's exact latitude): winter-solstice noon sun altitude is approximately 21-22 degrees, summer-solstice noon sun altitude is approximately 68-69 degrees.
- Building orientation tolerance from true south is reported inconsistently across sources: one range states up to 15-20 degrees off true south loses little effectiveness; another states up to 30 degrees still retains over 90 percent efficiency; a third states 15-30 degrees off costs about 15 percent of the optimum (unverified, conflicting ranges, flagged for whoever answers this so the manuscript picks one sourced figure rather than averaging unverified ranges).
- Site analysis tools and instruments found:
  - Solar Pathfinder: an analog, non-electronic reflective-dome instrument, roughly $300-500 (unverified), that shows every shading obstruction (trees, buildings, terrain) as a reflection traced directly onto a latitude-specific sun-path diagram; works in any weather because it does not depend on the actual sun being visible at the time of the survey.
  - Solmetric SunEye: an electronic equivalent with a fisheye lens.
  - Pilkington Sun Chart and Sun Peg Chart: printed sun-path charts specific to a latitude band; the University of Oregon's own Baker Lighting Lab lists a Sun Peg Chart calibrated to 44 degrees north, which matches the Willamette Valley almost exactly, a real Oregon-specific resource.
  - Heliodon (including a low-cost "bowling ball heliodon" variant): a physical model-testing device that simulates the sun's path over a scale model of the site or building.
  - Free web tools: sun-path diagram generators (an example found: Andrew Marsh's 3D sun-path web app) that plot altitude and azimuth for any latitude and date without special hardware.
- Applied site-analysis method implied by these tools: survey the actual candidate parcel across seasons (not just on a sunny day), specifically checking winter solstice solar access since that is the worst case for a heating-dominated climate, and record every obstruction (neighboring trees, terrain, structures) that a Solar Pathfinder or equivalent reveals, before finalizing the house footprint and orientation.

### 3. Building Form, Compactness, And Orientation

- Surface-to-volume ratio (S/V) drives heat loss and gain independent of insulation level: less exposed surface per unit of enclosed volume means less area for heat to cross. One source gives a typical single-family house S/V around 0.8-1.0 per meter, with a Passive House target at or below 0.8 per meter (one source cites 0.5 per meter) (unverified, ranges vary by source).
- A related metric, the Heat Loss Form Factor (envelope area divided by net floor area), runs 0.5-5 across ordinary buildings; Passive House design aims for 3 or below (unverified).
- A real design tension exists between compact form (minimizes total heat loss, favors the Passive House ethos) and elongated east-west form (maximizes south-wall area for solar gain, favors classic passive solar doctrine). One source cites an optimum elongation near a 1:1.3 aspect ratio along the east-west axis (unverified); this is a genuine trade-off to lay out for the owner rather than resolve with an invented number.
- This overlaps directly with the Land, Site, and Feasibility chapter's existing guidance ("positioning the long axis east-west... allows south-facing glass to collect the most even light across the day," found in general Oregon daylighting design sources, unverified) and should extend it into an actual footprint and massing recommendation once the site is fixed.

### 4. Passive Solar Heating: The Three System Types

Passive solar heating literature consistently describes three distinct system types, useful as a side-by-side option set for the owner:

| Type | Mechanism | Fit for this project |
|---|---|---|
| Direct gain | South glazing admits sun directly into the occupied space; interior mass (floor, walls) in the direct sun path absorbs and re-releases the heat | Matches the project's existing radiant concrete floor and the interior chapter's allowance for exposed bare concrete finish; simplest and cheapest type |
| Indirect gain (Trombe wall) | An unglazed, uninsulated mass wall sits directly behind south glass with a 5-15 cm air gap and floor/ceiling vents; the wall itself, not the room, absorbs the sun, then releases heat into the room by radiation and by convective airflow through the vents | A genuine option for an owner making the wall's own units, but it breaks from the whole-house continuous-exterior-insulation wall strategy at that one location and needs its own detailing where it meets the insulated wall on either side |
| Isolated gain (attached sunspace/solarium) | A glazed room, sometimes doubling as a small greenhouse, captures a large glazed area's solar gain and can be shut off from the main house by a door or operable vents, avoiding the nighttime heat-loss penalty of that glazing being part of the main envelope | Real overheating risk in an all-glass room without its own shading and venting; a genuine "creative but real" option worth costing against a conventional sunroom addition |

- Trombe wall specifics found: wall thickness commonly 8-16 inches (20-41 cm) of concrete or solid masonry; air gap between glass and wall 5-15 cm; vents at floor and ceiling level so heated air convects into the room while cool room air is drawn back into the gap (unverified; multiple secondary Trombe-wall explainer sources). Wall thickness below this range loses storage capacity; above it delays heat release enough to hurt evening comfort.

### 5. Glazing Ratios And Thermal Mass Sizing (DOE/NREL Rules Of Thumb)

- The most-cited industry rule of thumb (traced to a DOE/NREL "Passive Solar Design Strategies: Guidelines for Home Building" series from the 1980s, including a volume specifically for Eugene, Oregon that this research could not directly fetch due to a network restriction on nrel.gov in this environment; flagged for direct retrieval later): south-facing glazing at 7-12 percent of conditioned floor area for a direct-gain system. Below 7 percent is called "sun tempering," described below. Above 12 percent risks overheating without substantial added thermal mass.
- Mass sizing rule paired with the above: for every square foot of south glazing above the 7 percent baseline, add 3-6 square feet of 4-inch-thick masonry or concrete mass in the direct sun path (unverified, same source family).
- A different, simpler mass rule found elsewhere: total exposed mass area should equal about 6 times the south-glazing area (unverified; a secondary summary site that may be a simplification of the rule above rather than an independent rule; the two should be reconciled against the actual primary DOE document before either goes in the manuscript).
- Mass thickness effectiveness: returns diminish beyond about 4 inches for a directly sun-struck masonry or concrete surface; thicker mass stores more heat but releases it too slowly to be useful on the same day-night cycle (unverified, multiple secondary sources).
- East and west glazing recommended at under 5 percent of floor area, to limit low-angle morning and afternoon sun that is hard to shade and mostly a summer-comfort liability rather than a winter-heating asset (unverified).
- "Sun tempering" versus full passive solar: sun tempering is simply orienting the long wall toward true south and shifting window area that would have gone elsewhere onto the south face, at south glazing around 7 percent of floor area or less, with no added thermal mass and no added construction cost since it just redistributes windows already in the budget; it is credited with roughly 20-30 percent of annual heating demand from the sun. Full passive solar design (direct gain, indirect gain, or isolated gain, properly massed) is credited with 50-80 percent of annual heating demand from the sun, but adds real construction cost and design complexity (unverified; general passive-solar comparison sources).
- The open, genuinely unresolved question for this specific project: the DOE rules above were largely developed and calibrated in the 1980s across a range of US climates, many sunnier than the Willamette Valley's documented winter cloud cover (Part 1, section 1). Whether the standard 7-12 percent glazing and 3-6x mass rule pays for itself in a climate with 4-5 winter sun-hours a day and 80-percent winter cloud cover, versus simply spending the same money on more envelope insulation and letting the already-specified heat pump and radiant floor carry the load, is not answered anywhere in this research pass and is the central research-and-design question this new chapter should resolve.

### 6. The Passive-Solar-Design Debate (Real Practitioner Disagreement)

Two independent, experienced sources found during this research directly challenge the DOE rules of thumb above. Both are real positions from people who have designed and monitored actual passive solar houses, not fringe opinions, and the disagreement between them and the DOE guidelines is itself useful content for the owner.

- One source (a Green Building Advisor article attributed to a practitioner, Peter Powell, citing 35 years and over 60 designed passive solar homes) argues: fixed overhangs sized to block only high summer sun are "ugly, unnecessary, and counterproductive" in his experience, because over half of the solar radiation striking glass at a high summer sun angle is already reflected away by the glass itself and by low-e coatings, so the overhang is blocking a small remaining fraction while also cutting valuable spring and fall sun; south glazing can comfortably run 15-20 percent or more of floor area, even 30 percent or more in south-facing rooms specifically, provided the heat is actively moved by small fans into hidden thermal mass (his examples: hollow masonry walls, hollow floor slabs) rather than relying on direct floor-slab conduction alone; and deciduous trees are an unreliable shading strategy because bare winter branch structure still blocks a meaningful share of low winter sun, and in his region leaves do not drop until November, after many cool days have already passed when solar gain would have helped (unverified, one practitioner's stated experience, not a controlled study).
- A second, independent source (a different Green Building Advisor article, attributed to Brian Knight) argues passive solar can be done at zero added construction cost, through smart redistribution of a house's window budget onto the south face rather than adding expensive thermal mass; recommends a simple universal overhang rule (overhang set about 12 inches above the window top, projecting about 18 inches) as adequate for most US latitudes, which directly conflicts with the latitude-specific "overhang factor" method found elsewhere (Part 1, section 11); recommends maximizing fixed (non-operable) windows since they cost less and perform better, with only one operable sash per room for ventilation; and specifically warns that ICF and autoclaved aerated concrete should not be expected to deliver a meaningful thermal-mass benefit unless the mass sits entirely inside the insulation line, which is directly relevant to this project's own wall assemblies.
- Both sources converge on the same underlying caution: treat the 1980s DOE rules of thumb as a starting point to be locally recalibrated, not a formula to apply blindly, and prioritize the airtight, continuously insulated envelope first, since free solar heat is of limited value if the envelope leaks it back out. This matches the Passive House / PHIUS logic in the next section.

### 7. Passive House / Superinsulation Principles For A High-Mass Concrete House

- PHIUS (Passive House Institute US) departed from the original German Passivhaus standard in 2015 specifically to be climate-specific: rather than one fixed global performance number, PHIUS+ targets are derived per climate zone using the NREL BEopt tool, calibrated against national construction costs and regional energy costs (unverified; PHIUS-related secondary sources).
- The Pacific Northwest is reported as one of the more successful North American regions for Passive House adoption, because its marine climate is close to the climate the original German Passivhaus standard was developed for (unverified; PHIUS-adjacent secondary sources). A monitored Passive House project in Salem, Oregon was referenced in a PHIUS blog post that this research could not directly retrieve (the link redirected to the PHIUS blog's current index rather than the specific article); this is a real, local, monitored precedent worth chasing down directly in the answering phase, since it would give this project verified local performance data instead of national or European figures.
- Passive House's own overheating criterion: indoor temperature must not exceed 25 degrees C (77 degrees F) for more than 10 percent of occupied annual hours; the standard mitigation stack is thermal mass plus effective shading (deep horizontal overhangs on south glazing, angled vertical fins on east and west glazing) plus night ventilation, with combined strategies working better than any single one alone (unverified; Passive House / Passipedia secondary sources).
- The real tension to flag for the owner: classic Passive House doctrine tends to treat thermal mass as a secondary, minor comfort factor, because a superinsulated, airtight envelope already keeps indoor temperature nearly constant regardless of how much mass is present. This project instead already treats concrete mass as a first-class element: the HVAC chapter credits the mass for letting the heat pump "run steadily rather than in large swings" and for slow temperature decay during a power outage; the interiors chapter allows exposed bare concrete specifically "where the thermal mass and the look both work." The open research question this new chapter should resolve is where high mass earns its cost beyond what superinsulation alone would already deliver (specifically: multi-day power-outage resilience, night-flush summer cooling, and buffering the radiant floor's slow response) and where the marginal dollar is better spent on more insulation or better windows than on maximizing exposed interior mass area for its own sake.

### 8. Daylighting

- Code minimum is already set in the Interiors, Finishes, Accessibility, And Livability chapter (room geometry section) and the envelope chapter: 8 percent of floor area in glazing for natural light, 4 percent openable, per ORSC R303, with mechanical ventilation as a substitute. This chapter's daylighting content goes beyond that code floor toward genuinely useful daylight distribution and glare control, which the code section does not address at all.
- Window-to-wall ratio (WWR) guidance found: 25-40 percent is commonly cited as the balance point between daylight benefit and heat loss/gain; one source found no additional daylighting benefit above about 60 percent WWR; another recommends a 35 percent minimum for residential; a study on low-rise residential buildings found a 22 percent WWR paired with a 0.45 visible-transmittance glazing gave balanced results; ratios above 40 percent are reported to need external shading or adjustable-opacity glazing to control glare and heat gain (unverified, ranges vary meaningfully by source and climate, need reconciling).
- Clerestory windows (glazing set high in a wall, above eye level, often at a roofline step): daylight penetration into the room is reported at roughly 1.5-2.5 times the window-head height; best solar-heating placement aims the clerestory at a thermal mass wall about 1-1.5 times that wall's own height away (for a 12-foot wall, roughly 12-18 feet away) (unverified). North-facing clerestories give steady, glare-free light without a heat-gain or overheating problem; south-facing ones need their own small overhang, sized the same way as any other south window, or they become a glare and overheating source precisely because they sit above normal sightlines and are easy to forget when shading is designed.
- Light shelves (a horizontal reflective surface splitting a tall window, blocking direct glare at eye level below while bouncing daylight onto the ceiling above): shelf depth is reported to roughly equal the height of the glass above it; daylight throw reaches about 2.5 times the window-head height, up to 4 times in more elaborate designs; performance depends on a light-colored, high-reflectance ceiling to actually distribute the bounced light (unverified).
- Roof monitors (a raised, clerestory-glazed strip running along a roof ridge, historically from 19th-century factories and greenhouses): specifically useful for a deep floor plan where the room's center is too far from any exterior wall for side windows to reach; can face north for steady glare-free light or be paired with its own overhang if oriented south.
- Glare-control options beyond shading devices: interior blinds and shades, low-e or spectrally-selective glazing coatings (already specified generally in the envelope chapter's window section, without a stated per-orientation SHGC strategy), light-colored interior finishes that diffuse rather than reflect direct glare, and electrochromic (electronically tintable) glazing as a higher-cost, largely unexplored-in-this-manuscript option.
- Solar heat gain coefficient (SHGC) by orientation, a strategy not currently in the envelope chapter beyond its blanket statement that "SHGC remains a design choice": general guidance found recommends a relatively higher SHGC on south glazing to capture useful winter heat (commonly cited around 0.40-0.55 for a passive-solar-forward design, versus roughly 0.25-0.40 general residential guidance found elsewhere) paired with lower SHGC (below about 0.25-0.30) on east and, especially, west glazing where solar heat gain is a near-pure liability in this climate's warming summers (unverified, ranges vary by source, and this differs from a single blanket SHGC choice across all orientations).

### 9. Natural Ventilation

- Cross-ventilation room-depth rule of thumb: reliable up to a room depth of about 2.5 times the floor-to-ceiling height for single-sided ventilation (one window wall only); up to about 5 times the floor-to-ceiling height where true cross ventilation or stack assistance is present (unverified).
- "20 percent window rule": target openable window area at about 20 percent of the room's floor area for effective natural ventilation, with the openable area biased toward the prevailing wind direction where known (unverified).
- Stack effect and the solar chimney: a vertical shaft, ideally sited on the south side and finished dark inside to absorb heat and strengthen the buoyancy-driven draft, pulls warm air upward and out at the top while drawing replacement air in through low openings elsewhere in the house. Reported performance: stack ventilation alone reaches roughly 20 percent of a comparable cross-ventilation flow rate at night, 40-45 percent under some daytime conditions, and up to 100 percent on still days when cross ventilation has no wind to work with; combined with cross ventilation, total ventilation rate is reported to increase 22-36 percent (unverified; one conference-paper-level secondary source).
- Oregon code context already established in the envelope and HVAC chapters: Oregon requires balanced, continuous, mechanical whole-house ventilation (ORSC M1505) and explicitly disallows exhaust-only systems; the ASHRAE 62.2 blower-door infiltration credit is not granted. Natural ventilation in this project is therefore necessarily a supplemental, occupant-controlled strategy for shoulder-season comfort and night flushing, layered on top of the code-required mechanical system, never a substitute for it. The envelope chapter's Ventilation Coordination section already states the general mechanical/envelope split; it does not yet mention natural or operable-window strategies at all, which is a direct gap this new chapter fills and should cross-reference back into that section.

### 10. Night Flushing Of The Thermal Mass

- Mechanism: exposed mass (a concrete floor, an exposed CMU or concrete wall) absorbs and buffers daytime heat gain; at night, cooler outdoor air is moved through the house, by cross ventilation, stack effect, or a powered fan, to strip that stored heat back out of the mass before the next day's solar and internal gains begin the cycle again.
- Three real requirements for this to work, all worth stating plainly to the owner: a meaningful day-to-night outdoor temperature swing (diurnal range); mass surfaces that are actually exposed, not carpeted, not buried under furniture, not covered by an insulating finish; and a way to move enough night air, whether passive (high and low operable openings working together) or a powered whole-house fan.
- Whole-house fan sizing found: roughly 2-3 CFM per square foot of conditioned floor area, meaning a 3,000-square-foot house in that range needs roughly 6,000-9,000 CFM; a night-purge target runs about 18-24 air changes per hour, versus about 12-15 ACH for gentler continuous cooling; attic or exhaust venting needs roughly 1 square foot of net free vent area per 750 CFM of fan capacity; installed cost for a residential whole-house fan system runs about $900-$2,400 (2026) (unverified, commercial/industry sources, need independent verification before use as a manuscript cost figure).
- A genuine, unaddressed problem-and-solution pair: leaving windows open overnight for night flushing is a real security exposure, and this project already carries an independence and resilience emphasis elsewhere in the book. General home-security sources report roughly a quarter of burglary entries occur through ground-floor windows nationally (unverified, not Oregon-specific, and rural-crime rates differ from the urban data these figures likely come from). Solutions found in general building-science and security literature: place the night-flush openings high, at clerestory height or high operable sash, out of reach from grade; use lockable window restrictors or security stays that hold a sash open only a few inches, enough for airflow but not entry; install retractable, lockable security grilles over larger operable openings; or sidestep the problem with a powered whole-house fan plus secured, small, high, or below-sightline intake vents so no full-size window has to stand open at all overnight. This is a real point of friction between the passive-cooling strategy and the project's stated independence and resilience goals, and deserves an explicit resolution rather than silence.
- An open, site-specific question this research could not answer: whether the Willamette Valley's marine-influenced summer climate produces a diurnal temperature swing large enough to make night flushing worthwhile, as distinct from Oregon's high-desert climate zone 5B side, which very likely has a strong enough swing. This needs an actual NOAA/NWS station data pull for the specific candidate site, not a general claim.

### 11. Shading Design

- Two conflicting overhang-sizing methods were found, and the conflict itself is worth carrying into the question bank rather than silently picking one:
  - A latitude-specific "overhang factor" table, multiplied by the vertical distance from the windowsill to the underside of the overhang, gives an overhang depth that provides full shade at solar noon on the summer solstice and full sun at solar noon on the winter solstice. Reported example factors: 0.29 at 40 degrees north, 0.37 at 44 degrees north (close to the Willamette Valley), 0.45 at 48 degrees north (unverified, table sourced from online passive-solar overhang calculators, not a primary engineering reference).
  - A separate, simpler rule states an overhang set about 12 inches above the window top, projecting about 18 inches, works adequately across most US latitudes (unverified, from the Brian Knight source in section 6 above), which directly contradicts the latitude-specific method's premise that overhang depth should scale with latitude.
- Fixed horizontal overhangs work well only on south-facing glazing, where the sun is high in the sky at the times of day that matter. They do very little for east- and west-facing glazing, where the sun sits low in the sky in the morning and afternoon regardless of season; the standard answer for east/west glare and heat control is a vertical fin or angled louver (brise-soleil) instead of a horizontal overhang.
- External shading devices block roughly 90-96 percent of incident solar heat; internal blinds or shades on the same window block roughly 70-85 percent, because an external device rejects the heat before it ever reaches the glass, while an internal device absorbs solar energy and re-radiates a share of it back into the room as heat (unverified; UK solar-shading industry and academic secondary sources). This is a real, quantified reason to specify exterior shading over interior blinds wherever cost allows, not just a stylistic preference.
- Device options found, laid out as a real option set:
  - Brise-soleil: fixed or adjustable louvered fins, vertical or horizontal, angled to the local sun geometry.
  - Exterior roller shutters or shades: the standard European Passive House answer, motorized or manual, rolling down over the glazing from outside; not common in US residential practice but directly transferable.
  - Awnings: fixed or retractable fabric shading, typically over a single window or door.
  - Pergolas: an open lattice structure, often paired with deciduous vines so the shading thickens through summer growth and drops with the leaves in winter, a combined structural-and-planting solution rather than a pure hardware solution.
  - Deciduous trees and shrubs: covered separately below.
- Deciduous tree shading, with a real caution attached: full summer canopy blocks high summer sun effectively, but the contrarian source in section 6 above reports that bare winter branch structure still blocks a meaningful share of low winter sun even with the leaves down, and that leaf drop in his climate lags into November, after cool days when solar gain would already have helped, a timing mismatch worth checking against actual Willamette Valley deciduous species and typical leaf-drop dates rather than assuming the textbook "leaves fall exactly when needed" story. Placement guidance found: keep deciduous trees slightly north of the point on the ground where the winter sun would otherwise be blocked, and favor the south end of a tree line so some low spring and fall sun still reaches the building (unverified).
- Cost data found: exterior shutter installation averages roughly $231-$356 per shutter, about $819 typical for a whole house; functional (not purely decorative) shade or storm shutters run about $275-$1,200 per window installed; decorative-only shutters run $50-150 per window (2026, unverified, general contractor-cost-guide sources). Brise-soleil installation labor is reported around one hour per square meter of device, with total cost highly dependent on the specific site and system (unverified).

### 12. Comfort: Mean Radiant Temperature And Operative Temperature

- Mean radiant temperature (MRT) is the area-weighted average temperature of every surface a person exchanges radiant heat with: floor, walls, ceiling, windows. It is distinct from air temperature and is not currently defined anywhere in the manuscript (checked the glossary, which defines "thermal mass" but not MRT or operative temperature).
- Operative temperature, the practical comfort metric, is approximately the average of air temperature and MRT at the low air speeds typical of a residential interior.
- A specific, often-repeated radiant-heating industry claim: an occupant comfortable at 72 degrees F air temperature in a forced-air house may be equally comfortable at a lower air temperature, commonly cited around 68 degrees F, in a radiant-floor house, because the warm floor surface raises MRT and therefore operative temperature without raising air temperature (unverified; radiant-heating industry sources, not a controlled study found in this pass). If verified, this is a genuinely useful, concrete number for the owner: a lower thermostat setpoint at equal comfort, with a direct energy-cost implication.
- ASHRAE 55's adaptive comfort model, already cited in the HVAC chapter for the radiant-cooling surface-temperature limits, has a broader relevance this chapter should surface: it extends the acceptable indoor temperature range specifically for naturally-ventilated spaces with occupant control over openings, tying the acceptable range to the prevailing outdoor mean temperature rather than one fixed setpoint. The 2020 edition's 90-percent-acceptability central comfort line is reported to run roughly 20.9-28.2 degrees C depending on outdoor conditions (unverified). This model applies exactly to the shoulder-season condition this chapter's natural-ventilation and shading content targets, where the mechanical system is not the sole comfort driver and the occupant's own window and shade operation is doing real comfort work; the HVAC chapter does not currently connect its ASHRAE 55 citation to this adaptive, naturally-ventilated case at all.
- This chapter's contribution sits upstream of the HVAC chapter's radiant-cooling section: the radiant-cooling section already treats south-glazing-driven heat gain as a design input that a dehumidification and backup-cooling system must be sized to absorb; the shading and glazing-ratio content in this file reduces that gain before the radiant-cooling equipment in the HVAC chapter is ever sized, which is the assignment's own framing.

### 13. Worldwide Vernacular And Creative Precedent

- Windcatchers (Persian/Iranian badgir, Egyptian malqaf, Emirati barjeel): a vertical tower that catches wind at height and channels it down into the building, in some traditional designs passing over an underground water reservoir or pond for evaporative pre-cooling. One study is reported to find up to a 73 percent cooling-load reduction when a windcatcher is paired with evaporative cooling in a hot arid climate (unverified). Less directly transferable to Oregon's marine climate given the humidity difference, but the underlying stack-and-wind-capture principle scales down: a small operable cupola or roof monitor can do double duty as a daylight source (section 8 above) and a ventilation stack (section 9 above) without the full traditional tower form.
- Thick-wall thermal-lag construction: adobe, rammed earth, and stone walls roughly 18-24 inches thick are reported to produce a heat-transfer time lag from exterior to interior surface of roughly 8-16 hours, used throughout Mediterranean, Middle Eastern, and Southwestern US vernacular building to keep interiors cool through the hottest part of the day and release stored warmth into the evening. Specific figures found: rammed earth at 400-600mm thickness gives an 8-12 hour lag; massive stone or earth gives 12-16 hours; one Mediterranean case study measured a 6.6-hour average lag with about a 6 degrees C reduction in indoor temperature swing (unverified, ranges vary by source and are not Oregon-specific). This is directly relevant to any portion of this project's masonry or concrete wall that is left uninsulated and sun-exposed, whether intentionally (a Trombe wall, section 4 above) or as an unheated auxiliary structure (a shop or block-yard building, flagged as a separate "Developing the Site" research area and not duplicated here).
- Earthship-style annualized thermal storage and earth-sheltering: ground temperature is reported to "annualize" to a nearly constant year-round value at roughly 20 feet of depth (unverified), which is the physical basis for earth-sheltered and heavily-bermed design. This overlaps directly with the separately flagged "What Concrete Uniquely Enables" expansion area (earth-sheltering and berming named there explicitly) and should cross-reference that area rather than duplicate it; this chapter's distinct contribution would be the passive-solar glazing and airflow design that pairs with an earth-sheltered or heavily-massed design, not the structural or waterproofing side of earth-sheltering itself.
- Attached sunspace or solarium: already covered as the "isolated gain" system type in section 4 above; worth restating here as a genuinely buildable, creative option that also solves a second problem (a year-round or three-season plant-growing space), which matters for a self-sufficiency-minded owner-builder, with the real documented risk being summer and fall overheating in an all-glass room that lacks its own independent shading and venting.
- Trombe wall as a specific option for an owner making the owner's own masonry units: already covered in section 4 above; worth restating here because it is the one passive-solar system type that most directly rewards this specific project's make-your-own-block focus, since a Trombe wall is, physically, just a dedicated uninsulated mass wall behind glass, buildable with the same owner-made CMU or brick the rest of the house uses, at the cost of breaking the whole-house continuous-exterior-insulation strategy at that one wall.

### 14. Site Legal And Regulatory Considerations (Solar Access)

- Oregon has a Solar Access Act, cited in search results as ORS 105.880 through 105.909, allowing a property owner to establish a recorded solar easement across a neighboring property that defines the three-dimensional space that must stay free of new shade-casting construction or vegetation (unverified; found via statute-index search snippets, not read directly in the primary ORS text; strongly recommend direct verification against the actual statute, consistent with the project's source-priority rule, before any manuscript citation).
- ORS 227.190 and ORS 215.044 are reported to authorize, but not require, cities and counties to adopt solar access ordinances and to regulate construction that would block solar energy devices; Portland and Ashland were specifically named in search results as jurisdictions with local solar access ordinances affecting new subdivision design (unverified).
- No general statewide rule appears to restrict a neighbor's existing or future trees from shading a parcel; protection depends either on a solar easement the owner proactively records, or on a local ordinance the specific jurisdiction happens to have adopted (unverified). For a rural owner-builder, this means a neighboring parcel's tree growth on the south side is a real, generally unregulated long-term risk to a passive solar design's winter solar access, unless addressed either by a recorded easement or by confirming sufficient south-side buffer within the purchased parcel itself.
- A provision in a planned community's declaration or bylaws that prohibits installing or using solar panels is reported to be void and unenforceable under Oregon law (found cited as ORS 94.778) (unverified). This specifically names solar energy panels; whether it extends to passive-solar design choices like glazing area or building orientation, as opposed to PV or solar-thermal hardware specifically, is a separate, unanswered legal question.
- This overlaps the Land, Site, and Feasibility chapter's existing purchase-decision review, which already lists "solar orientation works, if solar is in the plan" as a check item and covers slope orientation for winter solar gain in its Topography section; this chapter's contribution is the specific legal mechanism (easements, ordinances) available to protect that orientation decision once the house is built, which the land chapter does not currently mention at all.

### 15. Interplay With Mechanical, Solar-Electric, And Battery Sizing

- This is the assignment's central framing question, and it is currently addressed only implicitly in the manuscript. The HVAC chapter's heating and cooling system selection section already states the concrete thermal mass "lets the equipment run steadily rather than in large swings," and prices the heat-pump plant options; its outage-behavior section already credits the mass and the tight envelope for slow indoor temperature decay during a power outage; its radiant-cooling feasibility section already treats south-glazing heat gain as a design input requiring dehumidification and backup-cooling capacity. None of these sections currently states the design sequence explicitly: orient and shape the building, size and place the glazing, design the shading and the mass, and only then run the Manual J load calculation that feeds equipment selection, so that the load calculation already reflects the passive design's benefit rather than a generic default assumption.
- A direct, currently-missing feedback loop worth making explicit: an oversized south (or, worse, west) glazing choice made for a view or an aesthetic reason directly inflates the heat-pump tonnage named in the HVAC chapter, the PV array size and the battery bank size named in the Solar, Battery, and Energy Independence chapter, and the radiant-cooling backup capacity named in the HVAC chapter's cooling-feasibility section. Stating that chain explicitly lets the owner weigh a glazing or shading decision in equipment-dollar terms, not only comfort terms.
- A genuine, unanswered research question, not resolved anywhere in this pass: a defensible rule-of-thumb figure for how much heat-pump capacity, and therefore dollar cost, a well-executed passive design (correct orientation, correct glazing ratio, correct shading) can reasonably be expected to remove from the Manual J load, calibrated to Oregon's specific heating-degree-day and winter-cloud-cover numbers rather than a generic national figure, given the real disagreement documented in section 6 above between DOE's rule-of-thumb guidance and practicing designers' contrarian experience. This is worth a dedicated research answer before the new chapter is written, since it is the number that actually justifies (or does not justify) the added construction cost of a serious passive solar strategy over simply superinsulating and undersizing nothing.

### 16. Landscaping And Site Microclimate Modification

- Windbreak design: a row or belt of evergreen trees or shrubs on the north or northwest side of the house, sized and spaced to reduce winter wind chill and infiltration-driven heat loss without blocking summer cooling breezes from other directions. General landscape-literature spacing guidance found runs in multiples of the mature windbreak height, commonly cited in the range of 2-5 times the mature height for the setback from the structure (unverified; needs an Oregon-specific horticultural or agricultural-extension source and species list, not found in this pass).
- Deciduous shading trees on south, east, and west sides: already covered in section 11 above under Shading Design; the landscaping angle adds species selection and Oregon-specific planting guidance, not found in this research pass and worth a dedicated question.
- This overlaps the Land, Site, and Feasibility chapter's existing Topography section, which already covers wind exposure at the parcel scale (ridgelines versus valleys) and cold-air pooling; the landscaping content here is the finer-grained, buildable follow-on once the parcel and the house footprint are both fixed, not a repeat of the site-selection material.
- Evaporative or water-feature cooling (a courtyard pool, a misting system) fits Oregon's high-desert climate zone 5B side of the state far better than the humid marine zone 4C side; a minor, site-dependent option rather than a default recommendation for the likely west-of-Cascades site.

### 17. Cost Summary Table (All Figures Unverified, 2026 Unless Noted)

| Item | Range found | Source type |
|---|---|---|
| Solar Pathfinder site-analysis tool | $300-500, one-time | Solar-industry retail |
| Sun tempering (window redistribution only) | $0 added cost | Passive-solar secondary sources |
| Full passive solar direct gain with added mass | Not quantified in this pass; flagged as a research gap | -- |
| Whole-house fan, installed | $900-$2,400 | Contractor-cost-guide sources |
| Exterior functional shutters, per window installed | $275-$1,200 | Contractor-cost-guide sources |
| Exterior decorative shutters, per window | $50-150 | Contractor-cost-guide sources |
| Exterior shutters, whole-house typical total | ~$819 | Contractor-cost-guide sources |
| Brise-soleil installation labor | ~1 hour per square meter of device | Solar-shading industry sources |
| Automated clerestory/skylight window actuator | Hardware found on retail sites; no installed-cost figure found | Flagged as a research gap |

### 18. Cross-Reference Map (To Prevent Duplication At The Merge Step)

- Envelope, Waterproofing, Thermal Performance, and Radon, section 8.4 (Wall Insulation Strategy): already states the core mass-placement rule (insulation outside the structural wall keeps the concrete at conditioned temperature and preserves the thermal-mass benefit). This new chapter builds on that rule; it does not re-derive it.
- Envelope chapter, section 8.8 (Windows And Doors): already sets the code-minimum U-factor and SHGC framing ("SHGC remains a design choice"). This new chapter's per-orientation SHGC strategy (section 8 above) is new material, not a repeat.
- Envelope chapter, section 8.14 (Ventilation Coordination): already splits envelope-side and mechanical-side ventilation responsibilities, but does not mention natural or operable-window ventilation at all. This new chapter's natural-ventilation and night-flush content (sections 9-10 above) is new material that should cross-reference back into that section.
- HVAC chapter, section 13.2 (Heating And Cooling System Selection): already credits thermal mass for steady equipment operation. This new chapter supplies the missing "why" and the missing design sequence (section 15 above).
- HVAC chapter, section 13.10 (Radiant Cooling Feasibility): already treats south-glazing gain as a design input for backup cooling capacity. This new chapter's shading and glazing-ratio content reduces that input upstream.
- HVAC chapter, section 13.15 (Outage Behavior And Energy Independence): already credits mass and envelope tightness for outage resilience. This new chapter does not repeat that; it notes the connection in section 7 above (where mass earns its cost).
- Land, Site, and Feasibility, section 3.2 (Climate And Design Loads) and 3.7 (Topography, Drainage, And Buildability): already cover slope orientation for winter solar gain, cold-air pooling, and wind exposure at the parcel scale, and already list "solar orientation works, if solar is in the plan" as a purchase-decision item. This new chapter is the detailed follow-on once a parcel is chosen, not a repeat of the feasibility-stage material.
- Interiors, Finishes, Accessibility, and Livability, section 14.2 (Room Geometry): already sets the ORSC R303/R304/R305 code minimums for daylight and ventilation. This new chapter's daylighting content (section 8 above) starts above that code floor.
- Sibling draft D's Q40 (overhangs protecting masonry from wetting) and sibling draft E's E29 (radiant-slab overheating control) and E57 (radon passive stack): related by name only; genuinely different questions, noted above so the merge step does not collapse them together.
- Adjacent flagged expansion areas not duplicated here: "What Concrete Uniquely Enables" (earth-sheltering, berming, cast-in mass storage) and "Developing the Site" (shop and block-yard siting); this file cross-references both where the overlap is real (section 13 above) without absorbing their scope.

---

## Part 2: Candidate Research Questions

### Site Analysis And Solar Geometry

**L1. What is the actual solar-noon altitude at the winter and summer solstice for this project's specific candidate parcel latitude, computed and verified rather than assumed from a generic Willamette Valley figure?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]
Leads: winter noon altitude approximately 90 minus latitude minus 23.5 degrees, summer approximately 90 minus latitude plus 23.5 degrees; unverified computation for a 44-45 degree latitude gives roughly 21-22 degrees winter, 68-69 degrees summer.

**L2. Which sun-path analysis tool or method (Solar Pathfinder, Solmetric SunEye, a printed sun-peg chart, or a free web sun-path tool) is the right fit for a mostly-solo owner-builder doing the site's own solar-access survey, and what does each actually cost and require in skill?**
Lands in: Passive and Bioclimatic Design (new chapter)
[TOOLS] [COST] [METHOD]
Leads: Solar Pathfinder roughly $300-500, analog, works in any weather; University of Oregon's Baker Lighting Lab keeps a 44-degree-north sun-peg chart, a real Oregon-calibrated resource worth contacting directly.

**L3. What NOAA or NWS station data exists for the actual candidate site's diurnal (day-night) summer temperature swing, and does it support night-flush cooling as a real strategy for this specific site, as opposed to a general Willamette Valley assumption?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]

**L4. What NREL NSRDB or PVWatts solar-resource data exists for the exact candidate parcel coordinates, replacing the generic statewide and Portland-area sun-hour figures found in general web sources?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Solar, Battery, and Energy Independence
[METHOD]

**L5. How much does actual measured winter cloud cover and sun-hour data for the Willamette Valley (a verified NOAA climate normal, not a marketing-site summary) undercut the DOE passive-solar glazing-ratio guideline, and what glazing ratio does that data actually support?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]
Leads: general sources report over 80 percent average winter cloud cover and 4-5 winter sun-hours per day for the valley, unverified against a primary NOAA source.

**L6. What is the prevailing wind direction for the Willamette Valley by season (not just an annual average), and how does it change the siting of operable windows for cross ventilation versus the siting of a windbreak for winter wind protection?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility
[METHOD]

### Building Form And Orientation

**L7. What building footprint and aspect ratio actually balances this project's two competing goals: a compact, low-surface-area form that minimizes total heat loss (the Passive House priority) against an elongated east-west form that maximizes south-wall area for solar gain (the classic passive-solar priority)?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Structural System and Concrete Design
[METHOD] [OWNER-DESIGN-CHOICE]
Leads: one source cites an optimum elongation near 1:1.3 along the east-west axis, unverified; Passive House form-factor targets run at or below about 0.8 per meter surface-to-volume, unverified.

**L8. Does a two-story or partial-basement massing change the surface-to-volume calculation enough to change the compact-versus-elongated recommendation for this specific house program, given the project's daylight-basement and multi-story options already discussed in the foundation chapter?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Foundation, Basement, Slabs, and Concrete Placement
[METHOD]

**L9. How does a masonry or concrete gable end, versus a hip roof, change shading self-obstruction on east and west walls, and does the roof form chosen for structural or aesthetic reasons in the structural and wall-system chapters accidentally help or hurt the passive design?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Structural System and Concrete Design, The Wall System
[METHOD]

### Passive Solar Heating: Types, Glazing Ratio, And Thermal Mass

**L10. What does the actual primary source, DOE/NREL's "Passive Solar Design Strategies: Guidelines for Home Building, Eugene, Oregon" volume, state for this exact climate, and how does it reconcile with the generic 7-12 percent glazing rule found in secondary summaries?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]
Leads: the document exists at a nrel.gov URL that this research pass could not fetch due to a network restriction; retrieve directly, by download or an alternate mirror, before writing the chapter.

**L11. For this house's actual floor area and room program, what south-glazing area (in square feet, not just a percentage) and what interior exposed-mass area does the DOE rule of thumb actually produce, run as a real worked calculation rather than left as an abstract percentage?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD]

**L12. Given the direct disagreement found between DOE's rule-of-thumb glazing ratio (7-12 percent) and a practicing designer's contrarian claim (15-30 percent workable with active mass-charging fans), which position holds up against actual monitored-building data, and is there a monitored example in a comparably cloudy climate to Oregon's?**
Lands in: Passive and Bioclimatic Design (new chapter)
[PROBLEM-SOLUTION] [TEST-TO-PROVE]

**L13. Is a Trombe wall, built from the owner's own manufactured CMU or brick, a cost-justified option for this specific house, and what does it cost in dollars and in the wall's own detailing complexity against simply extending the standard continuous-exterior-insulation wall with a larger south-glazing area instead?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Owner-Made Blocks and Alternative Concretes, The Wall System
[COST] [METHOD] [CREATIVE-IDEA]

**L14. What does a Trombe wall's air gap and vent detail need to be, specifically for an Oregon climate with mold and moisture risk in mind, given the gap is a sealed convective cavity that could trap condensation if not detailed correctly?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[PROBLEM-SOLUTION] [METHOD]

**L15. What is a realistic, sourced construction-cost premium, in dollars per square foot, for a full direct-gain passive solar design (extra glazing plus extra exposed mass) over the project's current default wall and window specification, a number this research pass could not find?**
Lands in: Passive and Bioclimatic Design (new chapter)
[COST]

**L16. Is an attached sunspace or solarium, sized to double as a plant-growing space, a better return for this owner's self-sufficiency goals than an equivalent-cost direct-gain glazing increase spread across ordinary rooms, and what does a sunspace actually cost to build onto a concrete house (2026)?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Interiors, Finishes, Accessibility, and Livability
[CREATIVE-IDEA] [COST] [OWNER-DESIGN-CHOICE]

**L17. What SHGC value, specifically, should the project specify for south-facing windows versus east- and west-facing windows, replacing the envelope chapter's current blanket statement that SHGC is an unconstrained design choice with an actual recommended value pair and its cost difference at the window order?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD] [COST]
Leads: general sources suggest higher SHGC (roughly 0.40-0.55) for south glazing, lower (below roughly 0.25-0.30) for east and especially west, unverified and needs a manufacturer-catalog and Oregon-climate-specific check.

### Daylighting

**L18. What clerestory placement, sized against this house's actual room depths and ceiling heights, delivers usable daylight to the deepest rooms in the plan (an interior bathroom, a windowless hallway, a great room center) without the code-minimum 8 percent glazing already satisfying the requirement on paper but leaving the room visually dark?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Interiors, Finishes, Accessibility, and Livability
[METHOD]

**L19. Does a light shelf make sense on this project's south-facing windows given the already-specified deep overhangs and the interior finish palette, or does the overhang alone already block the shelf's own daylight-bounce function?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [PROBLEM-SOLUTION]

**L20. What window-to-wall ratio, room by room, actually fits this house's program, reconciling the 25-40 percent general daylighting optimum against the higher heat-loss cost of a concrete/masonry wall assembly where every additional square foot of glazing replaces a much better-insulated wall assembly?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD] [OWNER-DESIGN-CHOICE]

**L21. Is a roof monitor a viable daylighting option on this project's specified roof assemblies (the protected-membrane roof or the wood-truss roof already detailed in the envelope chapter), and what does it cost in additional roof penetrations, structural framing, and waterproofing detail against a comparable skylight?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD] [COST] [PROBLEM-SOLUTION]

**L22. What glare-control device (interior blind, exterior shade, light shelf, or a spectrally-selective coating) is actually most cost-effective at the specific window sizes and orientations this house is likely to use, priced against each other rather than discussed only in the abstract?**
Lands in: Passive and Bioclimatic Design (new chapter)
[COST] [METHOD]

**L23. What visible transmittance (VT) value should this project target alongside its already-specified U-factor and SHGC values, since a window chosen purely for U-factor and SHGC can still deliver poor daylight quality?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD]

### Natural Ventilation And The Stack Effect

**L24. What specific room-by-room operable-window layout achieves true cross ventilation in this house's actual floor plan, once one exists, rather than the generic "20 percent window rule" left as an abstraction?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD]

**L25. Is a dedicated solar chimney (as opposed to relying on the existing roof form or an operable clerestory) worth the added construction cost and roof penetration for this specific house, given the stack-effect performance figures found are all from other climates and building types?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [COST] [PROBLEM-SOLUTION]

**L26. How does the code-required whole-house balanced mechanical ventilation system (ORSC M1505, already specified in the HVAC chapter) interact with occupant-operated natural ventilation: does opening windows during a shoulder-season day upset the HRV/ERV's balance or efficiency, and should the system have an automatic window-open sensor cutout?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[PROBLEM-SOLUTION] [METHOD]

**L27. What insect-screening and weather-sealing approach keeps a night-flush-sized operable opening (larger than a typical window vent) usable through an Oregon summer without admitting insects, wildfire smoke, or wind-driven rain during a sudden weather change?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[PROBLEM-SOLUTION] [MATERIALS/INGREDIENTS]

**L28. During a wildfire-smoke event, already a real Pacific Northwest summer condition, how does the owner override the night-flush and natural-ventilation strategy back to sealed mechanical filtration without a manual, error-prone nightly decision?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[PROBLEM-SOLUTION] [METHOD]

### Night Flushing And The Exposed Mass

**L29. What CFM and air-change target does this specific house's floor area and exposed mass actually need for an effective night purge, replacing the generic 2-3 CFM per square foot rule with a number tied to this house's actual thermal mass and glazing load?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[METHOD]

**L30. Is a powered whole-house fan, a passive stack-and-cross-vent-only strategy, or a hybrid the right choice for this project, weighed on installed cost, electrical load (relevant to the off-grid/battery sizing chapter), noise, and the security problem raised below?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Solar, Battery, and Energy Independence
[OWNER-DESIGN-CHOICE] [COST] [PROBLEM-SOLUTION]

**L31. What is the actual, resolved answer to the night-flush-versus-security conflict for a rural Oregon owner-builder: lockable window restrictors, retractable security grilles, high clerestory-only openings, or a sealed house with a powered fan and secured low vents, priced and compared rather than left as an open list?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Legal, Permits, and Owner-Builder Rules
[PROBLEM-SOLUTION] [COST] [OWNER-DESIGN-CHOICE]

**L32. Does exposing more interior concrete or CMU specifically to enable night flushing (rather than covering it with a finish material, an option the interiors chapter already allows) change the acoustic, cleaning, or comfort character of a room enough to matter, and has any real owner-builder documented that trade-off?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Interiors, Finishes, Accessibility, and Livability
[REAL-WORLD-EXPERIENCE] [PROBLEM-SOLUTION]

**L33. What finish-floor covering choices (already limited by the radiant-floor R-value cap in the HVAC chapter) also happen to be compatible with, or actively hostile to, night-flush thermal mass exposure, since a covered slab cannot flush heat the same way an exposed one can?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Interiors, Finishes, Accessibility, and Livability, HVAC, Ventilation, Humidity, and Air Quality
[PROBLEM-SOLUTION] [METHOD]

### Shading Design

**L34. Which overhang-sizing method, the latitude-specific "overhang factor" table or the simpler universal 12-inch/18-inch rule, actually produces a better result for this project's specific latitude, and can this be resolved with an authoritative source rather than left as two competing unverified claims?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]

**L35. What vertical fin or louver (brise-soleil) design actually controls east and west glare and heat gain on this house, given fixed horizontal overhangs are established as ineffective for those orientations, and what does a fixed brise-soleil system cost against a comparable exterior roller shade?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [COST]

**L36. Is an exterior roller shutter system (the standard European Passive House shading answer) available from a US or Pacific Northwest supplier at a reasonable cost and lead time for an owner-builder, or is it effectively a custom-import item for this project?**
Lands in: Passive and Bioclimatic Design (new chapter)
[COST] [MATERIALS/INGREDIENTS] [TOOLS]

**L37. What Oregon-native or well-adapted deciduous tree species actually fit the passive-solar shading role (dense summer canopy, open winter branch structure, leaf-drop timing that matches the start of the local heating season), given the contrarian source's specific critique that branch structure and leaf-drop timing often do not match the textbook description?**
Lands in: Passive and Bioclimatic Design (new chapter)
[MATERIALS/INGREDIENTS] [REAL-WORLD-EXPERIENCE]

**L38. What is the real-world maintenance and failure history of a pergola-plus-deciduous-vine shading system in a wet Oregon climate: does the wood or the vine structure rot, does the vine actually grow densely enough to shade effectively within a reasonable number of years, and what vine species are reported to work?**
Lands in: Passive and Bioclimatic Design (new chapter)
[REAL-WORLD-EXPERIENCE] [PROBLEM-SOLUTION] [MATERIALS/INGREDIENTS]

**L39. Given exterior shading is reported to outperform interior blinds by a wide margin (roughly 90-96 percent versus 70-85 percent of solar heat blocked), does that gap justify specifying exterior shading as the default for every south, east, and west window in this house, rather than treating interior blinds as adequate, and what is the added dollar cost of doing so across the whole house?**
Lands in: Passive and Bioclimatic Design (new chapter)
[COST] [METHOD]

**L40. Can a motorized exterior shade or shutter be run on a simple sun-and-temperature-triggered automation, consistent with the project's local-first smart-home approach described in the smart-home chapter, without adding a cloud-dependent or subscription-dependent product to the house?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Smart Home, Network, Security, and Local Automation
[METHOD] [PROBLEM-SOLUTION]

### Comfort From Radiant Mass

**L41. What is the actual, sourced relationship between radiant-floor surface temperature, mean radiant temperature, and a defensible lower thermostat setpoint for this house, replacing the unverified industry claim of "68 degrees F radiant feels like 72 degrees F forced air" with a real number or a real range?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[TEST-TO-PROVE] [METHOD]

**L42. How does the ASHRAE 55 adaptive comfort model's extended temperature range for naturally-ventilated, occupant-controlled spaces apply specifically to this house's shoulder-season operation (natural ventilation and shading doing the comfort work, mechanical system not the sole driver), and should the HVAC chapter's thermostat setpoint schedule change seasonally to reflect it?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[METHOD]

**L43. Does exposed interior concrete or CMU mass, at the surface temperatures this house's passive and radiant design would produce, ever create a mean-radiant-temperature discomfort in the other direction, an interior surface too cool in deep winter before the radiant floor has fully charged the room, and how is that cold-mass startup period managed?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[PROBLEM-SOLUTION] [METHOD]

### Passive House And Superinsulation Principles

**L44. What are the actual, monitored performance numbers from the Salem, Oregon Passive House project referenced by PHIUS, and what does its documented design (glazing ratio, shading, mass strategy, actual measured overheating hours) suggest for this project, as the closest real local precedent found in this research pass?**
Lands in: Passive and Bioclimatic Design (new chapter)
[TEST-TO-PROVE] [REAL-WORLD-EXPERIENCE]

**L45. Does the PHIUS+ climate-specific target for the Willamette Valley's climate zone exist as a published number, and how does it compare to this project's already-specified envelope performance (the Measure 7 blower-door and HRV targets in the envelope chapter)?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD]

**L46. Where, specifically, does this project's concrete thermal mass earn its cost beyond what the already-specified superinsulated envelope alone would deliver: is it the multi-day outage-resilience benefit already described in the HVAC chapter, the night-flush summer-comfort benefit, the radiant-floor response-buffering benefit, or some combination, and can that be stated as a design decision with its basis rather than an unquantified assumption that "mass is good"?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[METHOD] [OWNER-DESIGN-CHOICE]

**L47. Does the Passive House overheating criterion (indoor temperature above 25 degrees C for no more than 10 percent of occupied annual hours) apply usefully to this project as a design check, and if so, what combination of this project's own shading, glazing ratio, and night-flush strategy is needed to actually meet it, run as an explicit check rather than assumed?**
Lands in: Passive and Bioclimatic Design (new chapter)
[METHOD] [TEST-TO-PROVE]

### Legal And Regulatory: Solar Access

**L48. What does the actual text of ORS 105.880 through 105.909 require to establish a solar easement across a neighboring parcel, what does it cost in legal fees to record one, and is it a realistic tool for a rural owner-builder buying raw land rather than a subdivision lot?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility; cross-ref Legal, Permits, and Owner-Builder Rules
[CODE] [COST] [NOT-RESEARCHABLE-PRO likely for the drafting step]

**L49. Does the county where the candidate parcel sits have a local solar access ordinance under ORS 227.190 or ORS 215.044, and if not, what does that absence mean in practice for the owner's ability to protect the house's winter solar access from future neighboring construction or tree growth?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility
[CODE] [NOT-RESEARCHABLE-AHJ]

**L50. Does ORS 94.778's protection against HOA/CC&R solar-panel restrictions extend to passive-solar design elements (glazing area, orientation, roof form) as opposed to PV or solar-thermal hardware specifically, for any candidate parcel that turns out to sit inside a planned community or has recorded CC&Rs?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility
[CODE] [NOT-RESEARCHABLE-PRO]

### Interplay With Mechanical, Solar-Electric, And Battery Sizing

**L51. What defensible, Oregon-climate-calibrated rule-of-thumb figure exists (or can be derived) for the heat-pump tonnage, and therefore dollar cost, a well-executed passive design removes from the Manual J load, replacing the generic and contested national figures found in this research pass?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref HVAC, Ventilation, Humidity, and Air Quality
[METHOD] [COST] [TEST-TO-PROVE]

**L52. Should the HVAC chapter's Manual J load calculation section state explicitly that the calculation is run only after the building's orientation, glazing ratio, and shading are finalized, as an added procedural step, so a reader does not run Manual J against a placeholder design and then find the passive design decisions made later invalidate the equipment sizing?**
Lands in: HVAC, Ventilation, Humidity, and Air Quality; cross-ref Passive and Bioclimatic Design (new chapter)
[METHOD]

**L53. How much smaller can the PV array and battery bank named in the Solar, Battery, and Energy Independence chapter reasonably be, in watts and dollars, once the heating and cooling load is reduced by a well-executed passive design, run as an explicit before-and-after comparison rather than left unstated?**
Lands in: Solar, Battery, and Energy Independence; cross-ref Passive and Bioclimatic Design (new chapter)
[METHOD] [COST]

**L54. Does the radiant-cooling feasibility section's stated need for "small fan coils... in the highest-gain rooms (the kitchen, the primary bedroom for sleep, and rooms with large south glazing)" shrink or disappear entirely if this new chapter's shading and glazing-ratio guidance is followed, and should that section be revised once the passive-design chapter exists?**
Lands in: HVAC, Ventilation, Humidity, and Air Quality; cross-ref Passive and Bioclimatic Design (new chapter)
[METHOD]

### Landscaping And Site Microclimate

**L55. What Oregon-native or well-adapted evergreen species and what specific spacing and distance-from-house guidance actually work as a winter windbreak for a Willamette Valley or high-desert site, replacing the generic "2-5 times mature height" rule found in this research pass with an Oregon-specific figure?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility
[MATERIALS/INGREDIENTS] [METHOD]

**L56. Does a windbreak sized to protect the house from winter wind also risk blocking useful summer cross-ventilation breeze from the same general direction, and how is that trade-off actually resolved on a real site rather than left as an abstract tension?**
Lands in: Passive and Bioclimatic Design (new chapter)
[PROBLEM-SOLUTION] [OWNER-DESIGN-CHOICE]

**L57. For a high-desert eastern Oregon site (climate zone 5B), does a small courtyard water feature or evaporative element make a measurable comfort difference in the dry summer heat, and what does it cost against its water-use implication for a project with a stated water-independence goal?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Land, Site, and Feasibility
[CREATIVE-IDEA] [COST] [OWNER-DESIGN-CHOICE]

**L58. What outbuilding or landscape element placement (a detached shop, a garden wall, a berm) can double as a wind-block or a summer-shade device for the house itself, combining the site-development work already flagged under "Developing the Site" with this chapter's bioclimatic goals rather than treating them as separate projects?**
Lands in: Passive and Bioclimatic Design (new chapter)
[CREATIVE-IDEA]

### Worldwide And Creative Precedent

**L59. Is a small operable roof monitor or cupola, doing double duty as a daylighting device and a stack-effect ventilation outlet, buildable on this project's specified roof assemblies (protected-membrane concrete deck or wood-truss roof) at a reasonable cost, combining two of this chapter's strategies into one built element?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[CREATIVE-IDEA] [METHOD] [COST]

**L60. Does a scaled-down windcatcher-like element (a small operable tower or vent stack, without the traditional evaporative-cooling pond) offer any real benefit in Oregon's marine climate, or is the humidity difference from its arid-climate origin enough to make it not worth adapting?**
Lands in: Passive and Bioclimatic Design (new chapter)
[CREATIVE-IDEA] [PROBLEM-SOLUTION]

**L61. What do actual owner-builder forums and off-grid community documentation (not architecture-firm marketing material) report as the real, lived problems with a DIY passive solar or Trombe-wall retrofit or new build: what broke, what overheated, what the builder would do differently?**
Lands in: Passive and Bioclimatic Design (new chapter)
[REAL-WORLD-EXPERIENCE] [PROBLEM-SOLUTION]

**L62. Given the project's own thousand-year structural-shell goal, does a Trombe wall's glazing (a component with a much shorter service life than the concrete behind it, similar to the roof membrane's planned-replacement logic already established in the envelope chapter) need its own planned-replacement detail, and has anyone documented a multi-decade-old Trombe wall's actual glazing replacement?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[REAL-WORLD-EXPERIENCE] [PROBLEM-SOLUTION]

### Testing And Verification

**L63. What is a practical, owner-executable way to verify the as-built passive design is performing as intended (a simple data-logging thermometer set in the exposed mass and at a representative room location, tracked through a full year) rather than assuming the design works because the sizing rules were followed?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Testing, Commissioning, and Quality Control
[TEST-TO-PROVE] [METHOD] [TOOLS]

**L64. Does the pre-cover photography and records discipline already established in the envelope chapter (photographing window rough openings, flashing steps) need a passive-design-specific addition, such as photographing shading-device sightlines or clerestory placement before the roof closes in, so a decision made at the design stage is actually verifiable as built?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Envelope, Waterproofing, Thermal Performance, and Radon
[METHOD]

**L65. What does a one-year post-occupancy check of the passive design actually look like in practice: tracking indoor temperature swing through a full heating and cooling season against the design assumptions, and what threshold result would tell the owner the shading or glazing needs a correction (adding a shade, planting a tree) after the fact?**
Lands in: Passive and Bioclimatic Design (new chapter); cross-ref Documentation, Maintenance, and Future Upgrades
[TEST-TO-PROVE] [METHOD]

---

Question count: 65, grouped into 12 sub-topics (site analysis and solar geometry; building form and orientation; passive solar heating types/glazing/mass; daylighting; natural ventilation and stack effect; night flushing and exposed mass; shading design; comfort from radiant mass; Passive House/superinsulation principles; legal/solar access; interplay with mechanical/solar-electric/battery sizing; landscaping/microclimate; worldwide/creative precedent; testing and verification).
