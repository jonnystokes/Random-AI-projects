# Chapter 6: Structural System And Concrete Design

This chapter contains the structural design:

- the load path and the design-path decision (engineered or prescriptive)
- the concrete and reinforced-masonry wall assemblies, with wall ties and reinforcement detailing
- formwork, placement quality, and cast-in embeds
- the floor and roof options
- concrete durability, mix discipline, and the fire trade-off
- the seismic performance evidence and the voluntary upgrades beyond the code minimum
- safe rooms, hardened-structure options, and water-retaining structures
- the structural hold points where work stops for sign-off

The structural shell consists of concrete, masonry, and steel reinforcement, with no wood framing, subject to two practical exceptions. Manufacturer-engineered wood-truss roofs and wood-I-joist floors are options on the prescriptive design path, where the manufacturer's stamp replaces the structural-engineering line item. The trade-offs are in §6.4.

The Soil, Ground Prep, Drainage, And Foundation Risk chapter provides the soil class and the bearing assumption the foundation design starts from. The Foundation, Basement, Slabs, And Concrete Placement chapter contains the construction detail (excavation, forming, embeds, slab stack, concrete ordering, placement, curing). This chapter is the design layer between them.

## 6.1 The Structural Goal

The building has to carry every imposed load down to the soil and back up through the bracing system, with margins that make sense for a multi-century design horizon.

**Simple**

A house has weight pulling down (gravity, snow, furniture, occupants). Sideways forces push on it too (wind, earthquakes, soil against basement walls). High wind also pulls upward on the roof. Every one of those forces needs a continuous path to the ground that nothing along the way breaks under. The structural design specifies those paths.

**Applied**

Before structural design is finalized, mark the load path on the drawings:

- bearing walls (where roof and floor weight comes down)
- floor supports (joists, slabs, beams, with span and end conditions)
- roof supports (trusses, rafters, slab, with eave and ridge geometry)
- stair openings (where the floor diaphragm is interrupted)
- large window and door openings (where wall continuity is interrupted)
- shear-resisting wall lines (where lateral wind and seismic loads are anchored)
- foundation reactions (where loads enter the soil)
- planned utility routes through or around structure (so penetrations don't cut load paths)

Trace each load from its point of application to the foundation. If the path is not shown on the drawings, the design is incomplete.

**Professional**

The structural system requires a complete gravity and lateral load path. Dead load, live load, roof live load, snow load, wind load, seismic load, soil pressure, hydrostatic pressure, and construction loads are collected, transferred through floors and walls as primary elements, resisted by the lateral system, and anchored at the foundation.

For this project, the structural strategy is regularity:

- aligned bearing walls stacked floor over floor
- continuous reinforced wall lines without offsets
- floor diaphragms tied to wall elements through chord and collector reinforcement
- bond beams or ring beams at key levels
- controlled openings sized within prescriptive or engineered limits
- foundation elements designed from site-specific ground information

The building should be traceable in section: roof to wall, floor to wall, wall to foundation, foundation to soil, lateral force to diaphragm, diaphragm to shear wall, shear wall to foundation.

Mass without a defined load path adds cost without adding capacity.

**Code**

```
Every dwelling must be designed for the code's loads, using local values.
  Baseline gravity, snow, wind, seismic, and flood loads, with site-specific values from the jurisdiction's climatic and geographic table; the Design Criteria Hub confirms values for participating jurisdictions.
  Source: ORSC R301; Table R301.2(1); oregon.gov/bcd Design Criteria Hub.

Elements beyond the prescriptive limits must be engineered.
  Accepted engineering practice, with the engineer of record stamping the drawings and calculations.
  Source: ORSC R301.1.3.

Seismic design category triggers the reinforcement rules.
  SDC D0, D1, and D2 require expanded reinforcement for foundations, walls, and diaphragms; above-grade concrete walls in those categories must comply with PCA 100 or be designed under ACI 318 (ACI 332-20 addresses the same residential scope).
  Source: ORSC R301.2.2; ORSC R301.2.2.5.

Irregular buildings lose the prescriptive path for the whole story.
  Offsets in vertical lateral elements, large diaphragm openings, mass irregularities, and wood framing above masonry or concrete each trigger engineered analysis.
  Source: ORSC R301.2.2.6.

Live loads are fixed minimums.
  40 psf habitable rooms, 30 psf sleeping rooms, 50 psf stairs; higher values for decks, garages, and storage.
  Source: ORSC R301.5.

Engineered designs use the national load standard.
  Load combinations, snow shape coefficients, wind pressures, and seismic spectral values.
  Source: ASCE 7.
```

## 6.2 The Design-Path Decision

A concrete-and-masonry residence in Oregon takes one of three design paths. The path determines the plan submittal, the inspection regime, and whether a licensed structural engineer is required.

**Simple**

There are two realistic ways to design this house. The engineered way: pay a licensed structural engineer ($4,000-$10,000, 2026) to design exactly the house you want. That includes concrete floors and a concrete roof. The prescriptive way: follow the code's pre-approved rules for free. That path limits the design to simpler shapes and swaps the concrete floors and roof for factory-engineered wood parts. The engineered way delivers the full thousand-year shell; the prescriptive way delivers the concrete walls and foundation with wood above.

**Professional**

| Path | What it is | Best fit | When it is unavailable |
|---|---|---|---|
| Prescriptive | The code provides direct rules; the design fits inside the listed limits | Ordinary geometry inside ORSC tables; SDC C territory; single-wythe masonry; conventional spans | SDC D0/D1/D2 above-grade concrete walls; double-wythe loadbearing walls; concrete or masonry roofs; oversized openings; nonstandard heights |
| Engineered | A licensed professional designs and stamps the structural drawings | Most Oregon sites west of the Cascades; any nonstandard element; long spans; concrete floors and roofs | None; engineered design is the universal fallback |
| Alternative method | The building official approves a method that meets the intent of the code by another approved route | Innovative systems, tested assemblies, FRP reinforcement, owner-manufactured CMU subject to approval | Where the official does not accept the showing |

The first decision the project needs to make is whether to engineer or to constrain the design to the prescriptive envelope. Both paths are legitimate. The trade-offs are real.

**Engineered path**

- a licensed Oregon structural engineer designs and stamps the drawings
- a geotechnical engineer typically participates for non-trivial foundations
- the design accommodates concrete floors, concrete roofs, double-wythe walls, large openings, and nonstandard geometry
- the project includes engineering cost (typically $4,000–$10,000 for a custom 2-story 2,500–3,500 sq ft home in 2026 Oregon dollars, plus $1,500–$3,500 for a geotechnical investigation)
- delivers the full long-life concrete-shell vision

**Prescriptive path**

- the project is constrained to ORSC Chapter 4 (foundations) and Chapter 6 (walls) prescriptive tables
- foundations follow R403/R404 with R403.1.3 SDC reinforcement
- above-grade walls follow R606 (reinforced masonry) or R608 (above-grade concrete, SDC C only) or PCA 100
- floors and roofs use manufacturer-engineered wood I-joists or wood trusses (the manufacturer's stamp carries the engineering, not the homeowner)
- no double-wythe loadbearing walls; no concrete or masonry roof; no concrete floors
- delivers approximately 70–80% of the long-life concrete-shell vision; concrete floors and roof are the highest-engineering-cost elements and are dropped on this path

The Build Sequence And Site Coordination chapter discusses the cost framing. The chapter assumes the engineered path for the technical depth. The prescriptive-path constraints are flagged at each section so a reader choosing that path knows where the differences appear.

Weighting durability as heavily as the seismic and gravity load path does not change this decision. The engineered path is already the practical default for most western Oregon sites on seismic grounds alone (§6.3, §6.4). The strongest durability options either require an engineer of record regardless (targeted stainless reinforcement, a water-retaining structure designed to ACI 350) or are unavailable in this project's likely seismic design categories (GFRP primary reinforcement, §6.4). Durability choices refine material specification and detailing within whichever path is chosen. One narrow exception exists. An element that qualifies for the prescriptive path on load grounds alone, but carries a severe exposure classification (§6.15), can tip toward engineered treatment. The prescriptive cover and mix assumptions were not written for severe exposure.

## 6.3 Site-To-SDC Matrix

Seismic Design Category controls many prescriptive limits in this chapter. Oregon SDC by region (approximate; confirm at the site):

| Region | Typical SDC | Effect on prescriptive options |
|---|---|---|
| Eastern Oregon (high desert, Blue Mountains) | C | Most prescriptive options open; ORSC R608 above-grade concrete walls available |
| Cascade range and inland slopes | C to D0 | R608 mostly available; R606 prescriptive available with seismic supplements |
| Willamette Valley margins, central Oregon | D0 | R608 unavailable; R606 prescriptive available with seismic supplements; PCA 100 path available |
| Most of Willamette Valley, I-5 corridor | D1 | Same as D0 with stricter reinforcement; engineered path is the practical default |
| Coastal Oregon, parts of Lane/Douglas/Coos counties | D2 | Tightest prescriptive limits; many prescriptive options unavailable; engineered path is the practical default |
| Special wind regions (Columbia Gorge, parts of Oregon coast) | varies + > 130 mph wind | Engineered design typically required regardless of SDC due to wind |

Verify the site SDC at oregon.gov/bcd Design Criteria Hub or via the ATC Hazards by Location tool (asce7hazardtool.online).

Special wind regions carry an added rule. Inside a mapped special wind region, the mapped wind-speed contour is a starting value, not a design value: ASCE 7 §26.5.1 requires the ultimate design wind speed to be set by a site-specific meteorological analysis by a qualified engineer. Whether a parcel sits inside a special wind region is checked with the same two lookups above, at the parcel coordinates, once a specific parcel is selected. A site inside a special wind region, or a site the lookup shows above 140 mph, is designed for wind by the engineer of record; the prescriptive wind tables stop at 140 mph (§6.12).

## 6.4 What Must Be Engineered

Items that require licensed structural engineering, organized by certainty.

**Definitely requires PE (no prescriptive path otherwise):**

- above-grade concrete walls in SDC D0/D1/D2 (most of Oregon)
- two-wythe loadbearing CMU/CMU or CMU/brick assembly (no IRC prescriptive path exists)
- cavity walls beyond TMS 402 prescriptive limits (cavity > 4-5/8" without 2"-airspace exception, or > 6-5/8")
- reinforced masonry walls in SDC D0/D1/D2 designed beyond ORSC R606 prescriptive
- retaining walls > 4 ft tall or with surcharge or soil pressure > 30 pcf-equivalent
- footings on engineered fill, on weak soil (qa < 1,500 psf), or with bearing pressure > 2,000 psf
- any structural element using FRP reinforcement (per ICC ESR submittal)
- structural concrete floor diaphragms (CIP or hollow-core with topping)
- concrete or masonry roofs, regardless of slope
- buildings classified as irregular under ORSC R301.2.2.6

**Almost certainly requires PE:**

- sites with PI > 15 expansive soil (engineered foundation per ACI 332 Chapter 12 or equivalent)
- sites in mapped landslide hazard, liquefaction, or unstable slope
- story height > 11 ft 7 in
- ground snow load > 70 psf
- wall heights > 10 ft for any prescriptive type
- any post-tensioned or prestressed element
- any element where the project specification deviates from ORSC R608/R606 prescriptive

**May or may not require PE depending on jurisdiction:**

- steel beams supporting concrete floors (some jurisdictions accept manufacturer-stamped designs; others require PE)
- stair openings > 50% of floor width (irregularity threshold)
- mezzanines > 1/3 floor area of room below

**Does not require PE for a strict-prescriptive build:**

- wood-framed walls under ORSC R602 (not used in this project's structural shell)
- ORSC R608 above-grade concrete walls in SDC C only
- ORSC R606 masonry within prescriptive bar size and spacing limits in SDC ≤ C
- ORSC R403 footings using Table R403.1 presumptive bearing values
- manufacturer-engineered wood trusses and I-joists (the manufacturer's stamp carries the engineering)

For a long-life concrete-and-masonry home in any part of Oregon west of the Cascade Range, the structural system as a whole almost always requires PE involvement. The engineer signs:

1. a geotechnical report or site review for foundations
2. the structural drawings (plans, sections, details, schedules)
3. calculations supporting the structural drawings
4. a special-inspection program where required (an OSSC/IBC-scoped program invoked through the engineered design, not by the base residential code; typical triggers are grouted CMU, structural concrete with f'c > 4,000 psi, and post-tensioned elements; scoping detail in §6.22)

**Massing articulation on the engineered path.** For most western Oregon sites, the SDC alone (§6.3) already places this project on the engineered path. Recesses, projections, and offset volumes therefore do not trade away a prescriptive path the project still held. Irregularity classification still matters within the engineered path. An irregular building under ORSC R301.2.2.6 and ASCE 7 generally cannot use the simplest equivalent-lateral-force procedure and requires a more rigorous analysis method, and each offset adds reinforcement, detailing, and torsional design demand. Massing articulation is priced as analysis and detailing cost inside the engineered path, not as the loss of the prescriptive path. No general percentage limit on articulation exists; the thresholds are the qualitative irregularity conditions of R301.2.2.6, applied by the engineer of record to the actual floor plan.

**GFRP reinforcement is excluded by seismic category, not merely engineered.** ACI 440.11, the GFRP structural-concrete design standard, permits GFRP bars for all elements only in SDC A, and for elements outside the seismic force-resisting system in SDC B and C. It does not permit GFRP in any structural member in SDC D and above, the group containing the residential D0, D1, and D2 categories. ICC-ES AC454 is stricter: FRP bars in SDC A or B only. The basis is ductility: GFRP is linearly elastic to failure, with no post-yield redistribution, which seismic design in the higher categories assumes. For every likely site in this project's §6.3 matrix at D0 or above, GFRP primary reinforcement is unavailable anywhere in the structural shell. At an SDC C site it would remain limited to elements outside the seismic force-resisting system, which excludes the structural walls in this design. FRP wall ties are a separate, narrower topic (§6.8).

## 6.5 Concrete Walls

The concrete-wall design is governed by ACI 318 (general) or ACI 332 (residential-specific) when engineered, and by PCA 100 or ORSC R608 when prescriptive.

### Engineered concrete walls

**Professional**

- ACI 318 is the general structural concrete code
- ACI 332-20 is the residential-specific code with prescriptive tables for footings, foundation walls, slabs-on-ground, and above-grade walls in scope
- PCA 100 is referenced by ORSC R301.2.2.5 for above-grade exterior concrete walls in SDC D0/D1/D2

Common engineered exterior concrete wall:

| Parameter | Typical value |
|---|---|
| Wall thickness | 8 in. minimum, 10–12 in. for taller walls or higher seismic |
| Concrete strength | f'c = 3,000 psi minimum; 4,000 psi typical for above-grade exterior; 5,000 psi for retaining or other higher-stress applications |
| Reinforcement grade | Grade 60 (ASTM A615) typical; A706 preferred for seismic ductility |
| Vertical reinforcement | #4 or #5 at 12–24 in. on center, two curtains for thicker walls |
| Horizontal reinforcement | #4 at 12–18 in. on center, two curtains for thicker walls |
| Cover (exposed to weather or earth) | 2 in. exposed; 3 in. cast against earth |
| Cover (not exposed) | 1.5 in. |

### Prescriptive concrete walls

**ORSC R608 (SDC C only):**

- detached one- and two-family dwellings only
- specific limits on wall height, opening size, and reinforcement
- not applicable for most western Oregon sites (SDC D0+)

**PCA 100 (all SDC):**

- prescriptive engineering manual that requires explicit demonstration of compliance with its tables
- more detailed plan submittal than R608 but available where R608 is not
- referenced by ORSC R301.2.2.5

### Control joints and crack control in long walls

Concrete shrinks as it dries. A long wall with no joints cracks at random, uncontrolled locations. A control joint (a deliberately weakened plane, tooled or formed into both wall faces) concentrates the shrinkage crack at a planned, straight location instead.

Vertical control joints are commonly spaced at 2 to 3 times the wall height, with an outer bound near 10-12 ft for typical residential wall heights. The engineer of record sets the actual spacing from wall height, reinforcement ratio, restraint conditions, and expected shrinkage strain; the governing tables are in ACI 224R, a purchased report. Joints are also placed at stress concentrators regardless of the spacing rule: changes in wall height or thickness, wall offsets and intersections, near (not through) window and door openings, and re-entrant corners.

Joints and shrinkage steel serve two different functions and are set together. Distributed horizontal temperature-and-shrinkage reinforcement (the horizontal bars in the table above) does not prevent shrinkage cracking; it limits the width of the cracks that form between joints by distributing the strain across many fine cracks. Joint layout sets where the wall relieves stress; steel spacing sets how wide each crack opens. Closer bar spacing and closer joint spacing trade off against each other, so the engineer sets both in one pass, not independently.

A control joint is a deliberate discontinuity and a potential leak path. In any wall that resists water (a below-grade foundation wall, a retaining wall, a water-retaining structure per §6.20), each joint takes a waterstop (a PVC, rubber, or bentonite strip cast into the joint). The exposed groove is sealed with backer rod and sealant so surface water cannot track to the reinforcement. Above grade on dry walls, a tooled or formed joint without a waterstop is standard.

Current ACI 318 controls flexural crack width indirectly, through maximum reinforcement-spacing limits, not through a designer-calculated crack width. ACI 224R lists guide crack widths by exposure condition, from dry air through water-retaining service; the exact values are in the purchased report and are the durability reference behind the spacing limits.

**Code**

```
Engineered concrete design follows the general concrete code.
  Cast-in-place walls, slabs, beams, columns, footings, retaining and foundation walls, anchorage, development length, lap splice, cover, and exposure classes. Confirm the edition Oregon references at permit application; ACI 318-19 and 318-25 are both in circulation.
  Source: ACI 318 (edition per Oregon adoption at permit time).

Residential concrete has its own code with prescriptive tables.
  Footings, foundation walls, slabs-on-ground, above-grade walls in scope, and Chapter 12 expansive-soil design.
  Source: ACI 332-20.

Two prescriptive routes exist for above-grade concrete walls.
  PCA 100 (all SDC, referenced by ORSC R301.2.2.5) and ORSC R608 (SDC C only, with limits on height, openings, and reinforcement).
  Source: PCA 100; ORSC R608; ORSC R301.2.2.5.

Foundation walls have prescriptive tables.
  Flat and braced configurations, with SDC D0-D2 reinforcement at R404.1.4.
  Source: ORSC R404.

The material standards for the mix and the steel.
  Reinforcing bars (A615 Grade 60 typical; A706 low-alloy preferred for seismic ductility), Portland cement, ready-mixed concrete, and air-entraining and chemical admixtures.
  Source: ASTM A615/A615M; ASTM A706; ASTM C150; ASTM C94; ASTM C260; ASTM C494.

Exposure classes set the mix parameters.
  Freeze-thaw (F0-F3), sulfate (S0-S3), water (W0-W2), and corrosion (C0-C2) classes each set minimum f'c, maximum w/c, air content, cement type, and supplementary cementitious materials.
  Source: ACI 318 Chapter 19 exposure-class system.
```

## 6.6 Alternative Concrete Systems And Mixes

The project's default wall construction is removable-form cast-in-place concrete and reinforced CMU. Five alternatives recur in owner-built concrete construction. Each changes the formwork, the mix, or the reinforcement method, with distinct buildability, cost, and durability consequences.

**Simple**

There is more than one way to form and mix a concrete wall. The default here is rented or job-built forms that come off after curing. Stripped forms can be reused, and the bare concrete face can be inspected directly. The main alternatives change one variable each. Foam forms stay in the wall and double as insulation. A flowable mix fills the forms without vibration. Tensioned cables replace some ordinary bar in long floor spans.

**Professional**

| Option | What it changes | Trade-off against the default |
|---|---|---|
| Insulated concrete forms (ICF) | Stay-in-place foam forms combine formwork and continuous insulation in one trade sequence | The product line fixes the wall thickness and insulation value; the foam stays in the wall, so the concrete face cannot be stripped and inspected |
| Self-consolidating concrete (SCC) | Superplasticizer admixtures (not added water) produce a mix that flows around congested reinforcement with little or no vibration | Higher cost per yard from higher cementitious content and admixture dosage; formwork is still designed for full hydrostatic pressure |
| Post-tensioned slab | Unbonded tendons stressed after cure pre-compress the slab, increasing clear span for a given depth over mild-steel reinforcement | Requires specialized stressing crews and equipment; any future penetration risks cutting a stressed tendon |
| Fiber-reinforced concrete | Fibers added to the mix control plastic-shrinkage cracking and improve impact and abrasion resistance | Supplementary only; fibers do not replace primary reinforcement (§6.16) |
| SCM-rich low-carbon mix | 20-50% cement replacement with fly ash or slag densifies the pore structure and reduces embodied carbon | Slower strength gain; 7-14 day curing before stripping or loading, against 3 days for a standard mix (§6.15) |

SCC directly addresses the consolidation failure modes in §6.10: it removes the vibration-skill dependency behind honeycombing in congested cages, and it is documented to consolidate adequately in ICF and other congested-reinforcement applications where stiffer mixes performed poorly. SCC does not reduce form pressure. It stiffens slowly during placement, so form design assumes the full-hydrostatic case.

Post-tensioning is absent from this project's floor-system ranking (§6.11) because hollow-core precast and cast-in-place slab cover the project's span range without stressing crews, and because a stressed tendon constrains every future penetration through the slab.

ICF is established in low-rise residential and disaster-resistant construction. For this project it trades the default's direct surface inspection and reusable forms for a single combined forming-and-insulation step.

The SCM-rich mix is the project's specified durability mix (§6.15). The same replacement rate that densifies the pore structure also gives the largest reduction in the mix's embodied carbon, because Portland cement production is the dominant carbon dioxide source in concrete.

## 6.7 Reinforced Masonry Walls

Reinforced concrete masonry units (CMU) form the primary above-grade wall option for this project on the prescriptive path, and a frequent choice on the engineered path. ORSC R606 governs prescriptive masonry; TMS 402-22 governs engineered masonry.

**Simple**

A reinforced CMU wall is concrete block stacked in mortar. Steel bars run vertically through the hollow cores and horizontally through special channel courses. The cores holding steel then get filled solid with a soupy concrete called grout. The finished wall is a steel-reinforced concrete grid. It does not burn, rot, or feed insects, and in an earthquake the steel holds the blocks together.

### Engineered masonry walls (TMS 402)

**Professional**

| Parameter | Typical value for residential |
|---|---|
| Wall thickness (nominal) | 8 in. minimum for bearing walls; 10–12 in. for taller walls or higher seismic |
| Mortar | Type S Portland cement-lime per ORSC R606.2.8.3; Type M is the higher-strength option for severe exposure |
| Grout | ASTM C476 fine or coarse, 8 in. minimum slump (10–11 in. preferred for self-consolidating fine grout); minimum 2,000 psi at 28 days |
| Reinforcement grade | Grade 60 (ASTM A615) typical; A706 for seismic ductility |
| Vertical reinforcement | #5 at 24–48 in. on center, depending on wall height and SDC |
| Bond beam reinforcement | 2-#5 horizontal continuous in bond beam course |
| Lap length | 48 db (30 in. for #5 bar); covers conservative cases and avoids designer-by-designer variability |
| Grout lift | 5 ft maximum to avoid cleanout requirement and special-inspection trigger; ORSC R606.3.5.1 allows 8 ft maximum but cleanouts and special inspection apply above 5 ft |
| Cover | 2 in. exposed to weather or earth; 1.5 in. not exposed; 3 in. cast against earth |
| Joint reinforcement | 9-gauge ladder type at 16 in. vertical (every other course) for crack control |

### Prescriptive masonry walls (ORSC R606)

In SDC D0/D1, single-wythe reinforced CMU is the practical prescriptive choice for this project:

- 8 in. nominal CMU minimum thickness for bearing walls
- wall height ≤ 10 ft (R301.3 height limit; cap at 9 ft for safety margin)
- single-wythe construction (no prescriptive path for double-wythe loadbearing)
- vertical reinforcement: minimum #4 at 48 in. on center; spec #5 at 32–48 in. for stiffness
- horizontal reinforcement: bond beam at top of wall, at each floor level, and at top of foundation
- joint reinforcement at every other course (16 in. vertical)
- mortar: Type S (R606.2.8.3 requires Type M or S in D0/D1/D2)
- grout: ASTM C476, lifts ≤ 5 ft
- lap length: 48 db (30 in. for #5)
- grout fill: solid grout all reinforced cells; for D0/D1 stem walls, fully grouted
- maximum 3 stories above grade plane (R301.2.2.7)
- ½ in. gypsum board interior fastened per Table R702.3.5

### Bond beam strategy

Bond beams provide horizontal continuity, anchor floor and roof diaphragms, and control crack propagation.

| Bond beam location | Purpose |
|---|---|
| Top of foundation wall (turn-down or stem-wall top) | Tie foundation reinforcement to above-grade wall reinforcement |
| Top of wall at each floor level | Anchor floor diaphragm; transfer lateral loads |
| Top of wall at roof level | Anchor roof structure or roof diaphragm |
| Mid-height intermediate course (walls > 12 ft tall) | Crack control; stiffness |
| Above and below large openings | Resist concentration of forces around openings |

Bond beams require open-end (knock-out web) units or standard units with cut webs to allow continuous horizontal reinforcement.

### Bond pattern

Running bond (each unit overlapping the unit below by half its length) is the default coursing for this project. Stack bond (units aligned vertically, head joints continuous) leaves continuous vertical head joints with no unit overlap to interrupt a vertical crack, so both codes add horizontal reinforcement for it. The prescriptive rule is 9-gauge joint reinforcement at 16 in. maximum vertical spacing (ORSC R606.8.1); the joint-reinforcement spacing already specified above meets it without change. The engineered rule is horizontal reinforcement of at least 0.00028 times the gross vertical cross-sectional area at 48 in. maximum spacing, satisfied by bond beams or joint reinforcement (TMS 402). On running bond, R606.8.1 does not apply.

### Ungrouted cells as storage or display niches

On the prescriptive minimum, only reinforced cells are grouted, so the cells between vertical bars remain hollow. Those unreinforced cells are the only candidates for deliberate open use as a niche. A niche cannot interrupt a bond-beam course or a joint-reinforcement course; the clean placement is a pocket bounded vertically by those courses and horizontally by reinforced, grouted cells. The as-designed bar layout controls, not the generic spacing number, because bars concentrate at openings, corners, and bond-beam intersections. The engineer of record confirms candidate cells from the actual wall schedule; a builder does not self-determine them. Where the project adopts the solid-grouting upgrade (§6.18), no ungrouted cells remain and this option is unavailable.

**Code**

```
Engineered masonry follows the masonry code and its specification.
  Design under TMS 402 (wall classifications at 5.1.4, anchors and ties at 5.1.6); construction under TMS 602 (grout placement, mortar, cleaning, inspection).
  Source: TMS 402-22; TMS 602-22.

Prescriptive masonry follows the residential code's masonry section.
  Grout proportions at Table R606.2.12; grout placement at R606.3.5.1 with an 8-foot lift maximum and cleanouts required above 5 feet.
  Source: ORSC R606.

High seismic categories restrict the mortar.
  Type M or S Portland cement-lime is required for the lateral force-resisting system in SDC D0-D2; Type N is excluded there.
  Source: ORSC R606.2.8.3.

The masonry materials each have a standard.
  Loadbearing units (2,000 psi minimum net-area compressive strength), grout (fine and coarse proportions, 8-inch minimum slump, 10-11 inches for self-consolidating fine grout), mortar types M/S/N/O, unit sampling and testing, reinforcing bars, and joint reinforcement.
  Source: ASTM C90; ASTM C476; ASTM C270; ASTM C140; ASTM A615; ASTM A706; ASTM A951.

Three stories above grade plane is the prescriptive maximum.
  Source: ORSC R301.2.2.7.

Stack-bond masonry takes its own horizontal-reinforcement minimum.
  Prescriptive: 9-gauge joint reinforcement in bed joints at 16 inches maximum on center. Engineered: 0.00028 times the gross vertical cross-sectional area, at 48 inches maximum spacing, by bond beams or joint reinforcement. Running bond is exempt.
  Source: ORSC R606.8.1 (2023 edition); TMS 402-22.
```

## 6.8 Wall Ties For Cavity Walls

Where the project uses any cavity-wall construction (single-wythe CMU with exterior insulation and a separate exterior cladding wythe, or any double-wythe assembly), the tie system controls the structural connection between wythes, the corrosion durability, and the thermal-bridging penalty.

This project's prescriptive path uses single-wythe CMU with continuous exterior insulation and rainscreen cladding (no second loadbearing wythe). The tie discussion below applies primarily to engineered double-wythe configurations and to brick-veneer assemblies.

**Professional**

| Parameter | Specification |
|---|---|
| Tie material | ASTM A580 Type 304 or 316 stainless steel; carbon-steel (ASTM A82) acceptable for non-coastal applications with protective coating; mixing stainless and carbon steel creates galvanic corrosion |
| Wire size | Minimum W2.8 (3/16 in. diameter) for cavities > 4-5/8 in. up to 6-5/8 in.; minimum W1.7 (9 gauge) for cavities ≤ 4-5/8 in. |
| Spacing, adjustable ties | Maximum 16 in. horizontal × 24 in. vertical |
| Spacing, non-adjustable ties | Maximum 36 in. horizontal × 36 in. vertical |
| Frequency | Minimum 1 tie per 4.5 sq ft of wall (W2.8); 1 per 2.67 sq ft for W1.7; 1 per 1.77 sq ft for adjustable |
| Cavity width (prescriptive) | Maximum 4-5/8 in., or up to 6-5/8 in. with 2 in. airspace and 3/16 in. wire |
| Drip | No drip bend (reduces lateral-load capacity); use separate flashing/weep system |
| Galvanic isolation | All-stainless if any stainless is used |

**Thermal bridging:** stainless ties at the spec frequency create roughly 0.5–1% point thermal bridge, dropping a 4-inch rigid foam cavity from R-26 to about R-23 effective. For aggressive R-value targets, specify thermally-broken ties (Halfen FM, Bekaert Murfor THERM, Wagner ThermaTIE). The Envelope, Waterproofing, Thermal Performance, And Radon chapter takes the envelope-side detail.

**Mixed metallurgy:** galvanized and black (uncoated) steel in electrical contact within one element form a documented galvanic couple. The zinc coating acts as a sacrificial anode and is consumed protecting the adjacent black steel, which defeats the reason the galvanizing was specified. The working rule is one metallurgy per structural element, including chairs, spacers, and tie wire: all black, all galvanized, or all stainless. Where mixing is unavoidable, place a dielectric barrier at the contact point and match the tie wire to the bar (16.5-gauge or heavier galvanized tie wire on galvanized bar; stainless tie wire on stainless bar). For the stainless-and-carbon couple specifically, current corrosion literature finds the coupled corrosion rate low enough that distress is unlikely within a 75-year design life, and some current guidance no longer specifies isolation between black and stainless bar. This project's design horizon exceeds that 75-year study horizon, so the all-stainless rule in the table stands.

**GFRP bars** as primary reinforcement are excluded by seismic design category (§6.4). For the narrow case of a non-lateral element at an SDC C or lower site, the detailing differs from steel throughout. Development lengths run roughly 1.3-1.6 times steel's for a comparable design force. Tension laps run at least 1.3 times the development length (ACI 440.1R-15), with typical laps near 40-60 bar diameters. Bond depends on sand-coated or helically wrapped surfaces. Those figures are planning-level values from secondary sources; the engineer of record details any GFRP element directly against the current ACI 440.11 text, including hook details, which no secondary source states reliably.

**FRP ties** are not the prescriptive default. AC125 covers externally bonded FRP for strengthening (not new construction ties). AC454 covers FRP rebar in concrete (limited to SDC A or B). TMS 402-22 Appendix D introduces composite reinforcement for masonry partition walls (explicitly partition, not loadbearing exterior cavity walls). Commercial FRP ties exist but require ICC ESR submittal and per-project building-official approval. Treat FRP ties as an engineered alternative requiring documentation, not a prescriptive option.

**Code**

```
Tie spacing, size, and frequency come from the masonry code.
  Anchor and tie requirements, with composite, noncomposite, and veneer-wall provisions.
  Source: TMS 402-22 section 5.1.6.

The tie wire materials each have a standard.
  Stainless wire (Type 304 and 316), cold-drawn carbon-steel wire, and joint reinforcement.
  Source: ASTM A580; ASTM A82; ASTM A951.

FRP products enter only through evaluation reports.
  The FRP acceptance criteria address strengthening (AC125) and internal rebar limited to SDC A-B (AC454); an FRP tie product requires a current ICC ESR and, typically, per-project building-official approval.
  Source: ICC AC125; ICC AC454; ICC ESR program.

GFRP bars are excluded from the high seismic design categories.
  ACI 440.11 permits GFRP for all elements in SDC A, and for elements outside the seismic force-resisting system in SDC B and C; SDC D and above (the residential D0, D1, and D2 categories) are excluded. AC454 limits FRP bars to SDC A and B.
  Source: ACI 440.11; ICC AC454.

The industry references for cavity-wall and veneer ties are public.
  Anchors and ties, noncomposite (cavity) wall design, multi-wythe walls, and the brick-veneer companion notes.
  Source: CMHA TEK 12-01B; CMHA TEK 16-04A; CMHA TEK 16-01A; BIA Tech Note 28D; BIA Tech Note 44B.
```

## 6.9 Reinforcement, Grout, And Lap Lengths

Detailing controls how reinforcement develops the strength the design assumes. Wrong lap lengths, wrong cover, or missing hooks invalidate the calculations.

**Simple**

Steel strengthens concrete only where the two are joined over enough length. The bar also needs enough concrete covering it. The table below lists the overlap lengths, cover depths, and grout rules this project uses. The checks after it are how a crew catches placement mistakes before the pour makes them permanent.

**Professional**

| Detail | Typical residential value |
|---|---|
| Lap length, #5 in 8 in. CMU at f'm = 2,000 psi | 48 db = 30 in. |
| Lap length, #4 in 8 in. CMU at f'm = 2,000 psi | 48 db = 24 in. |
| Cover (exposed to earth) | 3 in. for cast-in-place concrete cast against earth; 2 in. otherwise exposed to weather |
| Cover (CMU exposed) | 2 in. |
| Cover (CMU not exposed) | 1.5 in. |
| Joint reinforcement cover (CMU) | 5/8 in. exposed; 1/2 in. not exposed |
| Hook | 90° standard hook for foundation reinforcement turning up into stem wall; minimum 14 in. extension into stem wall |
| Tie spacing during pour | At every other crossing minimum; chairs and spacers maintain cover |
| Grout lift maximum (avoid cleanout/special inspection) | 5 ft |
| Grout lift maximum (allowed by R606.3.5.1) | 8 ft, with cleanouts at base when grout pour exceeds 5 ft |
| Grout strength at 28 days | 2,000 psi minimum |
| Grout slump | 8 in. minimum for masonry; 10–11 in. for self-consolidating fine grout |

Reinforcement placement is verified at each footing inspection, foundation-wall inspection, and (for grouted CMU walls) at each grouting cycle. The Inspection And Approval Sequence chapter contains the inspection detail.

### Field placement failures and pre-pour verification

Rebar placement fails in the field in five recurring ways:

- **Lost cover.** Chairs and spacers undersized, crushed by foot traffic or concrete weight, or omitted, letting bars settle toward the form face. Reduced cover shortens the time before carbonation and chloride fronts reach the steel (§6.15).
- **Congestion.** Bars, dowels, embeds, and bond-beam steel converging at wall-footing intersections, corners, and openings. Congestion blocks aggregate flow and vibrator access, the honeycombing mechanism in §6.10. Bar-to-bar clearance is checked against the maximum aggregate size at the detailing stage per the ACI 318 spacing rules; field-discovered congestion goes to the engineer as a request for information, never an ad hoc bar substitution.
- **Wrong laps.** Laps shorter than the required development length, or laps stacked at one location instead of staggered, which concentrates a weak, congested zone at one section. Locating laps away from maximum-moment regions is the engineer's decision, not a field choice.
- **Displaced bars.** Foot traffic, placement equipment, and the pour itself pushing bars off position. The controls: chairs or spacers about every 2-4 ft on horizontal bars, ties at every other crossing minimum (every crossing in high-traffic zones), and a pre-pour walk that looks specifically for bent or stepped-on bars.
- **Wrong supports.** Chairs sized close to the specified cover instead of exactly to it, or metal chairs at an exposed face, which become corrosion initiation points. Plastic or concrete-block (dobie) chairs sized to the exact cover are the standard.

Pre-pour verification uses a written checklist, a second person's sign-off before concrete is ordered, and photographs of the final condition. The checklist lists:

- bar size and spacing against the drawings
- cover, by direct measurement or cover meter
- lap lengths and locations, and hooks
- chair spacing
- embed and sleeve conflicts

The hold points in §6.22 are where the inspector repeats these checks.

### Post-installed anchors and dowels

A missed dowel or anchor bolt is corrected with a post-installed epoxy anchor, and the governing document is product-specific. The hole diameter, hole depth, hole-cleaning method, and dispensing equipment come from the selected product's ICC-ES evaluation report (ESR) and the manufacturer's printed installation instructions it references, not from generic embedment ratios. Two current products match this project's uses. Simpson Strong-Tie SET-3G (ESR-4057) is listed for post-installed anchorage and reinforcing-bar connections in cracked and uncracked concrete from 2,500 to 8,500 psi, for static, wind, and seismic loads, and is accepted for engineered submittal under ORSC R301.1.3. Hilti HIT-RE 500 V3 (ESR-3814) is the equivalent adhesive anchor and post-installed rebar system. Using the wrong drill-bit diameter or skipping the specified hole cleaning voids the tested capacity even where a generic ratio is satisfied. ESRs are revised on renewal; the field crew works from the ESR current at installation, not an archived copy.

The bar schedule above tops out at #5, with #6 at isolated heavy locations. Manual benders are rated to #6 or higher depending on model; manual cutters commonly top out near #4, and powered cutter-benders rated to #6 or 1 in. bar cut and bend faster at foundation-schedule volume. Rent-versus-buy is decided from the final bar schedule's total footage and current local rental rates.

**Code**

```
High-seismic footings carry a fixed reinforcement pattern.
  Bottom horizontal #4 placed 3-4 inches from the footing bottom; top horizontal #4 within 12 inches of the stem-wall top; vertical #4 at 4 feet maximum on center, standard-hooked to the footing bottom and extending 14 inches into the stem wall.
  Source: ORSC R403.1.3 (SDC D0-D2).

The footing contains the grounding electrode.
  Uncoated #4 bar minimum, 20 feet long, encased in at least 2 inches of concrete near the footing bottom (the UFER ground).
  Source: ORSC R403.1.8.

Anchor bolts tie sill plates to the concrete.
  1/2-inch minimum diameter, 7-inch embedment, 6 feet maximum on center (4 feet for SDC D2 two-story), within 12 inches of plate ends, with 3x3x0.229-inch plate washers.
  Source: ORSC R602.11.

Grout lifts have height limits and inspection triggers.
  8-foot maximum lift; cleanouts at the wall base when the pour exceeds 5 feet; special inspection during grouting when the pour exceeds 8 feet; cleanout sizing and consolidation per the masonry specification.
  Source: ORSC R606.3.5.1; TMS 602.

Lap lengths come from the development rules.
  Development and lap splice of deformed bars, the engineering basis for the lap tables above.
  Source: ACI 318 section 25.4.

Post-installed anchors and dowels follow the product's evaluation report.
  Hole diameter, hole depth, hole cleaning, and dispensing equipment per the specific product's ICC-ES report and the manufacturer's printed installation instructions it references; current examples are ESR-4057 (SET-3G) and ESR-3814 (HIT-RE 500 V3).
  Source: ICC-ES ESR-4057; ICC-ES ESR-3814; ORSC R301.1.3.
```

## 6.10 Formwork, Placement Defects, And Cast-In Embeds

Concrete quality is set during placement. The recurring field problems fall into three families: consolidation defects (honeycombing, surface voids, sand streaking, cold joints), formwork failures (blowouts, bulging, misalignment, leaking joints), and embed drift. Each has a known mechanism and a known prevention. The Foundation, Basement, Slabs, And Concrete Placement chapter contains the full field procedure; this section states the mechanisms and the controls that belong in the structural design and the pre-pour checks.

**Simple**

Fresh concrete acts as a heavy fluid until it stiffens. It presses outward on the forms, it traps air unless vibrated, and it bonds poorly to concrete that has already begun to set. Most placement defects trace to one of those three facts. The fixes are form design, vibration technique, and delivery timing. All three are decided before the truck arrives.

**Applied**

Consolidation and placement:

1. Limit concrete free-fall to 3-4 ft; use a drop chute or tremie for taller forms.
2. Insert the vibrator on a grid pattern, penetrating a few inches into the previous lift.
3. Hold each insertion 5-15 seconds, until large air bubbles stop rising, then withdraw slowly.
4. Do not over-vibrate near the form face; over-vibration segregates the mix and washes paste from the surface.
5. Learn the mix's initial-set time for the day's temperature before the pour. Keep truck-to-truck intervals inside that window. Stage a backup vibrator and, on pump pours, a backup pump.
6. When a lift must stop, stop at a planned construction joint: roughened surface, with dowels or a bonding agent where the engineer specifies. An accidental stop past initial set is a cold joint, a visible and structurally weak plane.
7. Treat any form bulging as a stop-work signal, not a cosmetic issue.

Forms, before the pour:

1. Use a manufactured forming system with the manufacturer's published pressure and tie-spacing tables for the actual pour rate and expected concrete temperature.
2. Tape, gasket, or tight-fit every panel joint; a leaking joint bleeds paste and leaves sand streaks and washed-out fines.
3. Space ties tightest at the base of the pour, where pressure is highest; uniform top-to-bottom spacing under-ties the critical zone.
4. Brace the panels to ground or completed slab with kickers and diagonals, and walk every brace before the truck arrives.
5. Slow the pour rate in cold weather; a cold mix stiffens slowly and holds fluid pressure longer.

Embeds and anchor bolts:

1. Wire anchor bolts, or a template holding several bolts at spacing, to the tied reinforcement, not to the forms. Forms flex during the pour; tied rebar holds position.
2. Verify bolt layout against the actual sill-plate drawing immediately before the pour. Re-check bolt position and top-of-concrete elevation as the last truck finishes; bolts settle and drift during finishing.
3. Check every embed plate against the structural drawing's exact location, elevation, and orientation, not a generic spacing rule.
4. Run a written embed, sleeve, and dowel checklist against the structural and MEP drawings, checked by a second person, before calling for concrete.
5. Photograph the final pre-pour condition; after placement the as-built embed position cannot be directly verified.

**Professional**

Fresh concrete loads vertical forms with a lateral pressure equal to the lesser of full hydrostatic pressure (concrete unit weight times pour height) or a reduced value based on the stiffening rate. Faster placement and colder concrete both raise the design pressure. ACI 347, the formwork guide, contains the pressure formulas, and ACI Committee 347 recommends a factor of safety of 2.0 on form ties. The exact pressure coefficients are in the purchased standard; the forming-system manufacturer's published tables state the corresponding limits for the specific system and are the working reference on site.

Blowouts are usually tie failures, not panel failures: a tie under-specified or over-spaced for the actual pressure, most often near the base of the pour. Once one tie fails, its load redistributes to the adjacent ties and the failure progresses upward. Bulging indicates the tie-and-wale system is consuming its safety margin. Misalignment traces to external bracing that transfers horizontal thrust poorly, letting the whole form assembly shift during the pour.

Honeycombing (stony pockets where mortar failed to fill between coarse aggregate) has five documented causes:

- congested reinforcement in narrow forms
- segregation from excessive free-fall
- an improper fine-to-coarse aggregate ratio
- a mix too stiff to flow around bars
- incomplete consolidation that levels the concrete without completing de-aeration

Sand streaking (a sand-rich, cement-poor smear on the formed face) is caused by bleed water migrating up the form face and washing out cement paste; air-entrained mixes bleed less and streak less. Cold-joint prevention is scheduling: retarders extend the set window in hot weather, accelerators shorten it in cold weather, and the delivery interval is planned around the actual window.

Where an anchor bolt is missed despite the checklist, retrofit options exist: post-installed anchors per §6.9. A missed or misoriented embed plate is more consequential; a plate is a unique engineered connection, and correcting one typically means cutting and doweling new work rather than substituting a retrofit anchor. Retrofits are documented as corrections, not planned as practice.

## 6.11 Floor Systems

Floor systems are the structural element with the broadest range of options for a concrete-and-masonry house.

**Simple**

A floor here can be concrete poured in place, factory concrete planks craned into position, concrete over steel, or factory-engineered wood. The table compares the five options. Concrete floors last longest and require engineered design; wood floors are the low-cost prescriptive route.

Five viable paths, ranked by alignment with the long-life concrete philosophy:

| Path | Description | Strengths | Limits |
|---|---|---|---|
| Cast-in-place reinforced concrete one-way slab | 6–10 in. slab on bond beams or steel beams, #4 or #5 reinforcement in two directions per ACI 318 minimums, full continuity into walls | Highest mass; longest design life; best fire/sound; most consistent with concrete philosophy | Requires significant formwork; PE-designed; long pours |
| Hollow-core precast concrete planks with 2–3 in. CIP topping | 6–12 in. plank depth, manufacturer-designed and stamped, CIP topping provides diaphragm continuity | Fast erection; comparable longevity; industry-standard for concrete homes; long spans 16–32 ft | PE-designed for the project; manufacturer-stamped product; access required for delivery and crane placement |
| Composite concrete on metal deck on steel beams or bar joists | 3.5–6 in. topping over composite deck, on W-section beams or LH/SLH bar joists | Long spans; mechanical chases easily accommodated; reasonable cost | Introduces steel into the structural shell; 50–75 year structural design life as drawn |
| Manufacturer-engineered wood I-joists | 9-1/2 to 16 in. depth, manufacturer span tables, continuous over bearing walls or beams | Lowest cost; fast install; manufacturer's stamp carries the engineering | Wood; shorter design life; vulnerable to fire and water |
| Manufacturer-engineered wood floor trusses | 12 to 24 in. depth open-web, manufacturer-designed and stamped | Long spans; integrated mechanical chases; manufacturer's stamp | Wood; same vulnerabilities as I-joists |

For the engineered-path full concrete shell, hollow-core precast is the recommended primary path for spans 16–32 ft, with cast-in-place one-way slab as the alternative for shorter spans (≤ 16 ft) where formwork simplicity justifies a single material.

For the prescriptive path, manufacturer-engineered wood I-joists or open-web wood trusses are the practical default. The manufacturer carries the engineering stamp; the homeowner submits the manufacturer's product evaluation report (PER) and span tables with the permit submittal.

**Span-to-depth ratios for early sizing:**

- CIP one-way slab: span / 24 for typical residential loads
- hollow-core: span / 40 for typical residential loads
- so 24 ft span requires 12 in. CIP slab or 8 in. hollow core

**Impact sound:** a bare concrete slab rates poorly for impact noise. IIC (Impact Insulation Class, the ASTM E492/E989 rating of how much impact noise a floor-ceiling assembly blocks) runs roughly 25 for a bare 4 in. slab and roughly 28 for a bare 8 in. slab; footsteps on an unfinished concrete floor are clearly audible in the room below. The correction is a floating finish floor: a resilient underlayment (rubber, cork, or a rated acoustic mat) decouples the finish surface from the slab. A resilient mat under a hard finish reaches roughly IIC 50-60; resilient underlayment plus carpet reaches roughly IIC 65-75. Underlayment products publish a Delta IIC value, the points the product adds over the bare-slab baseline. The assembly is owner-installable and changes nothing in the structural slab design. Model-code IIC minimums apply to attached-dwelling separations; whether the ORSC imposes any minimum on a single-family interior floor is confirmed at permit time. For this project the rating is a comfort specification at any floor over an occupied room, selected with the interior finishes.

**Code**

```
Engineered concrete floors follow the slab chapters.
  One-way and two-way slab design: cover, reinforcement ratios, deflection limits; openings take trim, boundary, and diagonal reinforcement. Elevated structural slabs use ACI 318, never the residential slab-on-ground provisions.
  Source: ACI 318 Chapters 7 and 8; ACI 318 sections 7.7 and 11.7; ACI 332-20 (slab-on-ground scope only).

Hollow-core precast has an industry design manual.
  Source: PCI Manual for the Design of Hollow-Core Slabs and Walls.

Floor live loads are fixed minimums.
  40 psf habitable rooms, 30 psf sleeping rooms, 50 psf stairs (with a 300 lb concentrated load), 40 psf decks (60 psf in some occupancies).
  Source: ORSC R301.5, with ASCE 7 behind the engineered combinations.

Manufacturer-engineered systems submit their own engineering.
  Wood I-joists under ICC ESR product evaluation reports; open-web trusses with manufacturer-stamped shop drawings; hollow-core precast with stamped shop drawings and erection sequence.
  Source: the product's ICC ESR or manufacturer-stamped drawings, filed with the permit.
```

## 6.12 Roof Structure

Roof structure is the highest-risk durability item if specified wrong. The structural shell is designed for multi-century life; the roofing surface is designed for 30-80 years. The roof framing must satisfy both design lives.

**Simple**

The roof structure and the roof's weather surface have different lifespans. The structure is designed to last as long as the walls. The weather surface is replaced on a schedule. The table compares the three structural options on both lifespans. Snow is the load that has collapsed Oregon roofs, and the failures on record broke at connections, not in the framing members.

| Path | Description | Design life of structure | Design life of weather surface | Suitability |
|---|---|---|---|---|
| Concrete deck + protected membrane roof (PMR) | 8 in. CIP slab or hollow-core with 2–3 in. topping; modified bitumen, EPDM, TPO, or PVC fully adhered membrane; 4–6 in. XPS or polyiso insulation; ballast (river rock or concrete pavers) | Concrete deck: 100+ years | Membrane: 30–50 years; replaceable without disturbing structure | Best alignment with long-life philosophy; engineered design required |
| Concrete deck + sloped wood-framed false roof | Concrete deck as above; treated 2x sleepers supporting sloped framing (3:12–6:12) with metal or slate roofing | Concrete deck: 100+ years | Metal panel (24-gauge standing seam): 50–70 years; natural slate: 75–150 years | Decouples weather barrier from structure; higher cost; engineered design required |
| Wood-framed truss roof on bond beam | 2x truss assembly at 24 in. on center, manufacturer-engineered, on bond beam top of wall | Truss assembly: 50–80 years | Metal panel: 50–70 years; asphalt shingle: 15–30 years (rejected for this project) | Most familiar to local trades; prescriptive path option; manufacturer carries the engineering stamp |

**Roof selection guidance:**

- engineered path: concrete deck + PMR for the primary roof, with concrete deck + standing-seam metal as the alternate where slope is required for visual or snow-shed reasons
- prescriptive path: wood truss roof + standing-seam metal roofing on synthetic underlayment over plywood sheathing; eave-to-ridge ≤ 15 ft; manufacturer-engineered trusses with manufacturer's stamp
- both paths reject asphalt shingles for this project's design horizon (15–30 year service life is incompatible with the structural shell's design life)

**Drainage spec:**

- minimum 1/4 in. per ft slope on flat concrete decks
- minimum two roof drains per primary drainage area (IPC 1106)
- overflow scupper or secondary drainage sized for the 100-year storm with the primary drain blocked (IPC 1107)
- ASCE 7 ponding-instability check on concrete deck
- snow load per OSU/SEAO snow lookup tool with 25 psf minimum

**Solar integration:** a concrete deck simplifies future PV addition. Cast-in anchors or attachment plates for racking are embedded at design time. Ballasted PV racks on a PMR-protected concrete deck avoid through-roof penetrations entirely, which preserves the membrane's service life.

**Truss-to-wall uplift connections (prescriptive path):** ORSC Table R802.11 lists the uplift capacity the truss-to-wall connection must provide, tabulated by ultimate design wind speed (110-140 mph), exposure category, truss spacing, roof span, and pitch. Where the tabulated uplift is 200 lb or less, the standard fastening schedule of Table R602.3(1) applies without a rated connector. Above that, a load-rated hurricane tie is selected from the manufacturer's evaluation report to meet or exceed the tabulated value. For Oregon sites outside the special wind regions, catalog tie hardware meets the tabulated demands. Inside a special wind region, or above 140 mph, the connection design moves to the engineer of record with the rest of the roof (§6.3).

**Oregon snow failures on record:** three documented collapses set the design lesson.

- East Multnomah County warehouse, December 2008. Truss roof designed to the 1997 UBC, completed 2001. Witnesses reported 3-5 ft of drifted snow at the parapets and 2-3 ft over the field; 24 trusses collapsed. The forensic investigation found actual load above design load, wind drift against tall parapets beyond the design assumption, construction defects, and progressive collapse as each failing truss shed load to its neighbor. Of the failed trusses, 18 failed at connection welds and 6 by concrete breakout at the connection: the connections failed, not the truss members.
- Northern Oregon manufacturing plant, November 2014. Snow followed by freezing rain and temperatures near -20°F collapsed roughly 80,000 sq ft of a 400,000 sq ft roof.
- North Medford High School gymnasium, 2025. The gymnasium roof collapsed under a reported 350 tons of accumulated snow.

The documented failure mechanism is connection margin and drift load at parapets and roof discontinuities, not the base framing material. This project's roof options sit outside that mechanism: a concrete deck has no truss connections to fail, and the truss option is manufacturer-engineered with the connections inside the stamped design, against site-specific ground snow load from the OSU/SEAO lookup. The engineer of record checks drift loading at every parapet, valley, and roof step in the actual roof geometry against the ASCE 7 drift provisions; the 2008 collapse followed drift accumulation beyond the design assumption.

**Where a concrete deck meets a metal roof:** a structural expansion joint is standard practice where the main house's concrete PMR deck meets a standing-seam metal roof over an attached but structurally separate garage or shop. Two conditions each require the joint, and both are present here: a deck-material change, and a heated building meeting an unheated one. The joint runs from rooftop to foundation with parallel structural elements on each side, so each section moves independently; a roof-level cover alone does not decouple the two structures. The roof-level detail is a raised curb, roughly 8 in. minimum above the roof surface, with a flexible cover spanning the gap. Whether the wall-to-wall connection at the attachment needs the same full-height treatment is set by the engineer of record when the attachment is designed.

**Catchment hardware is a separate design.** Gutters, downspouts, and any first-flush diverter (a catchment fitting that discards the first, dirtiest roof runoff) fail by freezing while full of water, not by structural overload. Their sizing and freeze protection are part of the rainwater-catchment design, and ice dams at the eave trace to roof heat loss, an envelope detail, not to the roof structure; the snow-load design in this section resolves neither. Snowmelt adds to annual catchment yield on a delayed schedule and at lower peak flow than rain; that yield calculation is part of the water-independence planning once a site is chosen.

**Code**

```
The prescriptive wood roof path follows the residential framing sections.
  Rafter and ceiling-joist span tables, sheathing per Table R803.1, and vented or unvented assembly rules.
  Source: ORSC R802; ORSC R803; ORSC R806.

Roof coverings have material-specific rules.
  Metal panel roofing at R905.10; low-slope roofs beyond the residential covering sections follow the commercial chapter and the industry low-slope references.
  Source: ORSC R905; IBC Chapter 15; SPRI and NRCA technical references.

Engineered concrete roofs use the slab chapters and the load standard.
  Slab design per the concrete code; snow shape coefficients, drift, and partial loading per the load standard; site ground snow load from the state lookup.
  Source: ACI 318 Chapters 7 and 8; ASCE 7; snowload.seao.org.

Flat roofs need sized drains plus overflow.
  Primary roof-drain sizing per the plumbing model code, with secondary (overflow) drainage sized for the 100-year storm with the primary drain blocked.
  Source: IPC 1106 (primary); IPC 1107 (secondary).

Truss-to-wall connections resist the tabulated uplift.
  Required uplift capacity by ultimate design wind speed (110-140 mph), exposure category, truss spacing, roof span, and pitch; at 200 lb or less, the standard fastening schedule applies without a rated connector.
  Source: ORSC Table R802.11; ORSC Table R602.3(1).
```

## 6.13 Stair Openings And Diaphragm Continuity

An opening interrupts the in-plane diaphragm. Trim reinforcement around the opening restores the load path.

**Simple**

A stair opening cuts a hole in a floor that also works as the building's horizontal earthquake brace. The bars the opening interrupts are replaced around its edges. Openings past a size threshold put the whole story into engineered design.

**Professional**

For CIP concrete slab diaphragms (ACI 318 §7.7 and §11.7):

- trim bars: replace bars interrupted by the opening, distributed half above and half below the opening at slab edges
- diagonal bars at corners: 2-#5 at each corner, 4 ft lap into the uninterrupted slab
- boundary reinforcement: continuous chord steel along the edge of the opening; #5 minimum, 40 db lap
- minimum reinforcement ratio: per ACI 318 §11.6 (0.0012 for typical slab thickness)

For reinforced CMU walls and bond-beam continuity (TMS 402 §5.1.1):

- bond beams interrupted by openings need supplementary reinforcement with development length on each side
- minimum 2-#5 in bond beam, 48 db lap on each side of the opening
- continuous bars at top and bottom of openings, extending 24 in. minimum past the opening edge

**Diaphragm-irregularity threshold:** ORSC R301.2.2.6 lists openings in floor diaphragms exceeding certain dimensions as irregularity conditions that trigger engineered design for the entire story. Stair openings with the long dimension > 12 ft or > 50% of diaphragm width should be designed by the structural engineer with full diaphragm collector and chord reinforcement, not by reference to a prescriptive trim detail.

**Code**

```
Slab openings take trim and shear reinforcement.
  Trim bars around openings, special shear reinforcement, and the minimum slab reinforcement ratio.
  Source: ACI 318 sections 7.7, 11.7, and 11.6.

Large diaphragm openings trigger engineered design.
  Openings exceeding the stated thresholds are irregularity conditions for the entire story.
  Source: ORSC R301.2.2.6.

Bond beams stay continuous past openings.
  Supplementary reinforcement with development length on each side.
  Source: TMS 402-22 section 5.1.1.
```

## 6.14 Service Layer And Story-Height Classification

A service layer (a horizontal void between floors used for mechanical, electrical, and plumbing routing) interacts with the structural design and the code definition of "story." Mismanagement of service-layer height creates plan-review problems.

**Simple**

A service layer contains the pipes, wires, and ducts between floors. The code classifies it by its height and its access. The wrong height range turns it into an argued-over story at plan review. Two classifications avoid the argument: a shallow sealed plenum, or a full mechanical level counted as a story.

**Professional**

ORSC R202 defines a "story" as the portion of a building between the upper surface of a floor and the upper surface of the floor or roof above. The classification of a service layer depends on its height and accessibility.

| Classification | Height and access | Code consequences |
|---|---|---|
| Habitable space (R202) | Used for living, sleeping, eating, cooking | Triggers ceiling-height (R305: 7 ft minimum), light/ventilation (R303), egress (R310, R311), and heating (R303.10) requirements. Do not classify a service layer as habitable. |
| Crawl space (R408) | Below the lowest occupied floor; height typically < 4 ft with limited access | Requires ventilation or conditioned-crawl provisions; 18 in. × 24 in. minimum access opening; vapor retarder over earth; no heating required. |
| Concealed space / plenum / interstitial space | Not occupied; not regularly accessed except for inspection or maintenance | Fireblocking required at floor/wall intersections per R302.11; if used as a return-air plenum, IMC restrictions on combustible materials apply. |
| Mezzanine (R325) | Within the room volume below; ≤ 1/3 floor area of the room below | Counts as part of the room below, not a separate story. |

The plan-review trap: if the service layer is large enough that a person can enter it (typically > 4 ft height OR > 30 in. × 36 in. cross-section access), some building officials classify it as a mezzanine, an attic, or a story.

**Two clean classifications for this project:**

1. **Concealed plenum.** Service layer ≤ 30 in. clear height, accessed only through removable panels. No story implications; fireblocking and draftstopping per R302.11/R302.12.
2. **Conditioned mechanical level.** Full crawl-space-style mechanical level with ventilation, lighting, permanent ladder or stair, ≥ 4 ft clear height. Counts as a story.

The middle ground (30–72 in. clear height) is the trap that gets argued case-by-case at plan review and slows permits. Pick one of the two clean classifications.

**Code**

```
The story definition controls the classification.
  A story is the portion of a building between the upper surface of a floor and the upper surface of the floor or roof above.
  Source: ORSC R202.

Concealed spaces require fireblocking and draftstopping.
  Fireblocking at floor and wall intersections; draftstopping in floor-ceiling assemblies.
  Source: ORSC R302.11; ORSC R302.12.

Habitable classification triggers the habitability rules.
  7-foot minimum ceiling height, light and ventilation, emergency escape openings, and means of egress.
  Source: ORSC R305; R303; R310; R311.

Mezzanines and crawl spaces have their own definitions.
  A mezzanine at or under one-third of the room's floor area counts as part of the room below; crawl spaces take ventilation or conditioned-crawl provisions with an 18x24-inch minimum access.
  Source: ORSC R325; ORSC R408.

A plenum used for return air restricts the materials in it.
  Combustible-material restrictions apply to return-air plenums.
  Source: OMSC plenum provisions.
```

## 6.15 Concrete Durability And Mix Discipline

Concrete designed to last centuries requires deliberate mix design and placement discipline. Standard residential concrete is designed for roughly 50-year service. Long-life concrete adds margins on permeability, reinforcement protection, and thermal stability.

**Simple**

Concrete fails over decades for two main reasons. Water reaches the steel and rusts it, and rust expands and cracks the concrete from inside. Freeze-thaw cycles pry at any water trapped in the pores. Long-life concrete counters both. The mix is denser: less water, plus additives such as fly ash that fill the pores over time. The steel gets more concrete cover, and the curing runs longer. The upgrade adds a premium per truckload, and it extends the service life of the one part of the house that cannot be replaced.

**Professional: exposure-class targets**

ACI 318 organizes concrete durability by exposure class. Mix-design parameters scale to the highest applicable class.

| Exposure | Class | Concern |
|---|---|---|
| Freeze-thaw | F0 (none) / F1 (moderate) / F2 (severe, no salts) / F3 (severe, with salts) | Frost damage in saturated freeze-thaw cycling |
| Sulfate | S0 / S1 (moderate) / S2 (severe) / S3 (very severe) | Sulfate attack on cement paste |
| Water | W0 / W1 (in contact) / W2 (low-permeability required) | Permeability and water transmission |
| Corrosion | C0 / C1 / C2 (severe; with chlorides) | Reinforcement corrosion in chloride environments |

For an Oregon long-life house above grade in mild exposure: F1, S0, W0, C1. For below-grade walls in contact with soil with potentially aggressive soils: F1 or F2, S1, W1 or W2, C1 or C2 depending on chloride exposure.

Element by element: footings and below-grade walls in soil contact are the elements that can reach the severe classes. Their actual classification comes from the geotechnical report's soil and groundwater chemistry (the Soil, Ground Prep, Drainage, And Foundation Risk chapter). Above-grade walls take the mild baseline. Two elements are absent from the table and are classified by the engineer of record at design time. Exterior-exposed slab edges sit closer to the below-grade condition than to the interior baseline. Any water-retaining structure is classified separately (§6.20).

Exposure class is assigned per element and wall location, and the reinforcement spacing and control-joint layout at each wall are cross-checked against that wall's own class rather than applied uniformly (§6.5). At any wall classified severe, the engineer verifies the shrinkage-and-temperature steel ratio against the ACI 318 minimum at that wall, not only at the diaphragm openings where §6.13 already requires it.

A severe classification does not itself trigger corrosion-resistant reinforcement. The exposure-class system is calibrated for uncoated black steel with the mix and cover responses as the primary protection. Epoxy-coated, galvanized, or stainless bar is an added layer, specified where the engineer judges mix and cover insufficient for the 100-plus-year target against the measured chloride exposure (metallurgy-mixing rules in §6.8).

**Professional: deterioration mechanisms**

The exposure classes correspond to five mechanisms, and each mix parameter in the next table counters a named mechanism:

- **Carbonation.** Atmospheric carbon dioxide reacts with the alkaline hydration products and lowers the pore-fluid pH. When the carbonation front reaches the bar, the passive oxide layer that protects steel at high pH breaks down and ordinary corrosion begins. The rate scales with permeability, so the low-w/c, well-cured mix slows it.
- **Chloride ingress.** Chloride ions diffuse through the pore structure; at a threshold concentration at the bar surface they break down the passive layer locally, even without carbonation, producing pitting corrosion that is harder to detect than uniform corrosion. Low w/c and SCM densification slow the diffusion; added cover lengthens the path.
- **Sulfate attack.** Sulfates from soil or groundwater react with calcium aluminate hydrates to form expansive ettringite and gypsum, which crack the paste from within. This attacks the cement paste, not the steel; Type II/V cement or SCM replacement is the response for classes S1-S3.
- **Alkali-silica reaction (ASR).** Cement alkalis react with reactive silica minerals in some aggregates, forming a gel that absorbs water and expands; map cracking is the classic symptom. ASR is aggregate-specific; the verification procedure is below.
- **Freeze-thaw.** Pore water expands roughly 9 percent on freezing, and the internal hydraulic pressure fractures paste over repeated cycles. Entrained air voids give the expanding water relief space; that relief is the air-content requirement in classes F1-F3.

The mechanisms couple in the field: freeze-thaw cracking opens new chloride ingress paths, so measured deterioration runs faster than the single-mechanism rates the classes tabulate separately.

**Mix-design parameters for long-life concrete:**

| Parameter | Standard residential | Long-life target |
|---|---|---|
| f'c at 28 days | 2,500–3,000 psi | 4,000 psi minimum (5,000 psi for severe exposure) |
| Maximum w/c ratio | 0.55 | 0.45 (0.40 for severe) |
| Air content (freeze-thaw exposed) | 4–6% | 5–7% |
| Cement type | I/II | I/II with SCM |
| Supplementary cementitious materials | Optional | 20–30% fly ash (Class F, ASTM C618) or 30–50% slag (ASTM C989) replacement |
| Cover to reinforcement | Code minimum | Code minimum + 1/2 in. additional for severe exposure |
| Curing | 3 days | 7 days minimum, 14 days preferred for SCM mixes |

Pozzolanic admixtures (fly ash, slag, silica fume) reduce permeability over time, increase chemical resistance, and reduce heat of hydration; all favorable for long-life concrete. They also extend setting and strength-gain time, which has to be planned into the construction schedule.

### ASR verification for the project's aggregate

ASR control is aggregate-specific, so it is tested, not assumed. ASTM C1567 is the test: a roughly 16-day accelerated mortar-bar test of the project's actual aggregate, cement, and candidate SCM dosage together, read against the standard's 0.1 percent expansion acceptance threshold. Published fly-ash results put the minimum effective replacement at roughly 15-35 percent depending on the ash source. That range sits largely inside the 20-30 percent fly ash and 30-50 percent slag replacement already specified above. The overlap is not proof for this project's materials. If the project's own test result requires a higher dosage or a different SCM type, the mix specification changes to match the test.

**Applied**

1. Ask the concrete supplier for the aggregate source's ASR service record and any existing test reports.
2. Order, or obtain from the supplier, an ASTM C1567 test on the actual aggregate-cement-SCM combination before finalizing the mix design.
3. File the result in the project binder with the mix submittal.

### Fire spalling: the dense-mix trade-off

The durability mix has a documented fire trade-off. Heated concrete generates internal vapor pressure as pore water vaporizes. Low-permeability concrete cannot vent that pressure fast enough through its own pore structure, and a surface layer detaches violently (explosive spalling, documented in the 250-400°C range). High-strength, low-permeability mixes are more susceptible than ordinary residential concrete for exactly that reason, and research records that raising the w/c ratio reduces spalling risk, the opposite direction from every other durability rule in this section. This project's 4,000-5,000 psi, 0.40-0.45 w/c, SCM-densified mix is therefore the susceptible profile. The exposure that matters is a structural element under direct, sustained fire that must still carry load afterward: structural walls and any structural concrete floor or roof slab. The documented mitigation is polypropylene monofilament fibers at low dosage (low single-digit lb per cubic yard in the fire-engineering literature): the fibers melt in fire and leave fine channels that vent the vapor pressure gradually instead of explosively. This is a separate application from the shrinkage-control fibers in §6.16, is not a substitute for any reinforcement, and is specified by the engineer of record for the fire-exposed structural elements.

**Code**

```
Durability requirements scale with exposure class.
  Maximum w/c ratio, minimum f'c, and air-entrainment requirements per class; residential materials and mix design in the residential code's own chapter.
  Source: ACI 318 Chapter 19; ACI 332-20 Chapter 4.

Hot weather, cold weather, and curing each have a guide.
  Temperature, humidity, and curing controls in heat; freeze protection and minimum temperatures in cold; curing methods and durations.
  Source: ACI 305R; ACI 306R; ACI 308R.

The mix ingredients each have a standard.
  Portland and blended cements, aggregates, fly ash and natural pozzolans, slag cement, silica fume, air-entraining and chemical admixtures, and the ready-mixed concrete specification.
  Source: ASTM C150; C595; C33; C618; C989; C1240; C260; C494; C94.

The fresh and hardened tests each have a standard.
  Sampling, slump, pressure-method air content, and cylinder compressive strength.
  Source: ASTM C172; C143; C231; C39.
```

## 6.16 Fiber Reinforcement: Boundaries

Fiber-reinforced concrete (FRC) has legitimate uses but is not a replacement for primary structural reinforcement.

**Professional**

ACI 544.4R-18 sets the boundary: fibers can supplement and reduce conventional reinforcement in applications where continuous reinforcement is not essential to safety and integrity (slabs-on-ground, pavements, overlays, shotcrete linings, slabs-on-piles, some precast units). Fibers do not replace primary flexural reinforcement in residential structural members under code.

ACI 318 admits steel fibers as shear reinforcement in specific contexts (§11.4.6.1), and industrial slab-on-ground design routinely uses FRC as primary reinforcement under TR 34 (UK) and ACI 360R. For the residential structural shell, FRC is supplementary, not primary. Polypropylene monofilament fibers dosed for fire-spalling mitigation (§6.15) are a further supplementary use inside the same boundary.

**Acceptable manuscript framing:**

- "Fiber-reinforced concrete used to control plastic shrinkage cracking, improve impact and abrasion resistance, and supplement temperature-and-shrinkage reinforcement."
- "Macro-synthetic or steel fibers added to slabs-on-ground at 3–7 lb/yd³ for crack control; primary structural reinforcement (#4 at 16 in. on center each way for typical residential slab) per the engineer of record."
- "Steel fiber dosage of 25–50 lb/yd³ may be used as designed shear reinforcement per ACI 318 §11.4.6.1 in elements where designed by a registered engineer."

**Not acceptable:**

- "Fibers replace rebar."
- "No reinforcing required when fibers are used."
- "FRC eliminates need for primary reinforcement."

**Code**

```
The fiber guide draws the primary-versus-supplementary line.
  Where fibers may serve as primary reinforcement (slabs-on-ground, pavements, overlays) versus supplementary only (residential structural members).
  Source: ACI 544.4R-18.

Steel fibers as shear reinforcement are engineering-controlled.
  Permitted in defined contexts under the concrete code; slab-on-ground design under the industry guide.
  Source: ACI 318 section 11.4.6.1; ACI 360R.

The fiber materials and tests have standards.
  The FRC material specification and the third-point flexural performance test.
  Source: ASTM C1116; ASTM C1609.
```

## 6.17 Seismic Performance: The Field Evidence

Post-earthquake reconnaissance connects the reinforcement and anchorage rules in this chapter to observed building outcomes. The evidence identifies which details separated standing buildings from failed ones.

**Simple**

Unreinforced masonry is the deadliest common building type in earthquakes. Its walls are stacked units with nothing tying them to each other or to the floors and roof. During shaking, an unanchored wall face separates from the building and falls. Reinforced, grouted, anchored masonry behaves differently. The steel ties the courses into one unit. The bond beams tie the walls to the floors and roof. Every reinforcement rule in this chapter serves one of those two connections.

**Professional**

Unreinforced masonry lacks both continuity and diaphragm anchorage. During shaking, an unanchored wall's out-of-plane inertia has no connection to the diaphragm above; the wall face separates and falls, the dominant recorded URM collapse mechanism. Anchoring the floor and roof diaphragms to the walls converts each wall from an independently vibrating mass into a braced element of the structure, and is recorded as the most effective single retrofit step for existing URM buildings. This project's walls are reinforced and grouted, with diaphragm anchorage through the bond-beam system (§6.7), so the URM mechanism is designed out, provided the detailing is executed as drawn. Partial grouting thinner than the design assumption, a bond beam interrupted at an opening, an ungrouted congestion void at a bond-beam intersection, and an unverified tie-down each reintroduce a URM-like discontinuity into a nominally reinforced wall.

The 2010 Maule, Chile earthquake (magnitude 8.8) produced the clearest documented comparison for reinforced and confined masonry. Reconnaissance teams found physically adjacent, nominally similar masonry buildings with sharply different outcomes: some undamaged, immediate neighbors severely damaged or partially collapsed. The difference traced to nameable details, not to wall quantity, material strength, or apparent design intent:

- missing or inadequate ties (stirrups) at the joint zones between confining elements
- absent ties in end columns, concentrating damage in the joint zone
- absent ties at beam-to-column joints combined with inadequate anchorage length, producing joint shear failure
- longitudinal bars buckling where tie size and spacing could not restrain them under load reversal

Across the surveyed stock, most one- and two-story confined-masonry dwellings were undamaged, and the severe damage and the two recorded collapses concentrated in buildings with weak confinement and tie detailing.

This project's specification closes those documented modes at the design level: continuous vertical reinforcement in grouted cells (§6.7); bond beams held continuous past openings, with development length on each side (§6.13); and laps and cover per the ACI 318 development rules (§6.9). The remaining exposure is field execution. The Chile surveys record buildings where the designed reinforcement existed on paper and a placement gap undid it. The hold points in §6.22 and the pre-pour verification in §6.9 and §6.10 target exactly the joint zones and anchorage points where similar buildings diverged.

## 6.18 Voluntary Upgrades Beyond The Code Minimum

Code seismic design targets life safety. This project adds structural margin above that target where the evidence supports it. The upgrades below are ordered from settled practice to research concepts; each states its cost where a real figure exists and its open dependency where one does not.

**Simple**

The code's earthquake rules are written so occupants survive; the building itself may be damaged beyond repair. This project designs above the life-safety minimum. The options below add steel, grout, or engineering analysis beyond the minimum. Some have firm evidence and known costs. Others are research concepts that would need this project's engineer to develop.

**Solid grouting of every cell.** The specification in §6.7 grouts all reinforced cells. Grouting every cell, reinforced or not, is standard West Coast seismic practice; partial grouting is the accepted cost-saving norm in lower-seismic regions. Test literature records that full grouting improves ductility, damage pattern, and post-peak behavior, and treats partially grouted walls as a structurally different system rather than a cheaper equal; the literature does not supply a single transferable performance multiplier. Cost guides put the grout-fill increment at roughly $2-4 per square foot of wall face, with solid-grouted reinforced CMU walls at roughly $22-26 per square foot installed (2026 contractor cost guides). A per-wall figure requires a mason's quote against the actual wall schedule.

**Ductile detailing at first construction.** Four upgrades use the same crew, tools, and trade as the code-minimum wall:

- vertical bars at closer spacing (for example #5 at 24 in. on center against the prescriptive minimum #4 at 48 in.)
- full-height continuous vertical bars where stock length and story height allow, eliminating lap-splice zones and their congestion
- joint reinforcement at every course instead of every other course, doubling that material and its laying time
- added dowels at wall-to-bond-beam interfaces beyond the required minimum

Each is a material-and-labor increment, not a new skill. No defensible per-linear-foot dollar figure exists without a mason and rebar-supplier quote against the project's wall schedule; the grout-increment figure above is the nearest order-of-magnitude reference.

**A continuous tension tie at every wall segment.** Proprietary continuous-rod systems (Simpson Strong-Tie Strong-Rod and equivalents) run a coupled rod from roof level to foundation anchorage, resisting overturning and uplift as one designed tension path. They were developed for light-frame wood construction. A fully grouted, continuously reinforced concrete or CMU wall already contains more continuous mass and reinforcement than the light framing those systems supplement. The applicable version of this upgrade here is continuity in the wall's own vertical bars (the second item above). Discrete rod systems are candidates at wall segments interrupted by large openings, at short wall returns, and at wall lines where the overturning calculation approaches the code demand. Whether to specify them is the engineer of record's determination, and pricing requires a take-off after the demand is sized.

**Wall density as a design check.** Chilean reconnaissance after the 1985 Llolleo earthquake found that confined-masonry buildings with shear-wall area of at least roughly 1.15 percent of floor-plan area per direction avoided severe damage. The Chilean code minimum is commonly cited near 0.85 percent. A follow-up study found only about 57 percent of a 1990s-era building stock reached the 1.15 percent threshold. The figure is calibrated to confined masonry (unreinforced panels confined by cast-in-place tie columns and tie beams poured after the panels are laid) and does not transfer numerically to reinforced CMU. No codified wall-density check exists for reinforced CMU or concrete residential design. The project's working proxy is the regularity strategy in §6.1: long, continuous shear-wall lines rather than short segments between openings.

**A named performance target.** The ASCE 41 performance levels (Operational, Immediate Occupancy, Life Safety, Collapse Prevention) are written for evaluating and retrofitting existing buildings, not for new design. The concept transfers as an owner's brief: the engineer of record reaches a higher-than-code target through conventional over-design (higher reinforcement ratios, tighter drift limits, conservative detailing margins). A purpose-built voluntary framework for new construction exists: the U.S. Resiliency Council rating system scores Safety, Damage (repair cost), and Recovery (time to regain function) on a one-to-five-star scale, for owners specifying performance above the code minimum. USRC is a rating and verification system, not a design standard, and the ORSC permit process runs separately. No general cost-premium figure for above-code seismic performance is published. One documented Christchurch low-damage commercial building reported a roughly 7 percent net construction-cost saving from a three-month-shorter schedule; that figure is specific to that project's technology and is not a transferable premium or saving.

**Rocking walls and sliding base isolation.** Two low-damage concepts from the research literature are design concepts requiring project-specific engineering, not selectable options. Post-tensioned rocking walls (the PRESSS program, extended by New Zealand's post-Christchurch Pres-Lam work) let a wall rock on its foundation, recenter through unbonded tendons, and dissipate energy in replaceable steel elements. The residential adaptations are mature in engineered timber. No built residential reinforced-CMU or cast-in-place concrete application is documented. Low-cost sliding base isolation (a low-friction plane between foundation and superstructure, with measured friction coefficients of roughly 0.15-0.35 across tested material pairs such as marble on high-density polyethylene) is documented for small masonry houses in developing countries. It is not code-recognized in Oregon, and the published designs leave the service crossings (plumbing and wiring crossing a plane designed to move) unresolved for a modern serviced house. Either concept requires the engineer of record to develop, analyze, and stamp a project-specific design, likely including nonlinear dynamic analysis, before it could enter a permit submittal.

## 6.19 Safe Rooms And Hardened-Structure Options

**Simple**

A safe room is a room built to a tested shelter standard. The standards are ICC 500 (the code standard) and FEMA P-361 (the federal guidance). The room protects occupants from extreme wind and flying debris even if the rest of the building fails. In a wood-framed house, a safe room is an independent reinforced box added inside it. This house's shell is already reinforced concrete and masonry. The added work here is mostly the rated door, a rated vent, and any needed local reinforcement.

**Professional**

FEMA P-320 prices a new-construction residential safe room at roughly $9,400-$13,100 for an 8 by 8 ft room and $18,900-$25,500 for a 14 by 14 ft room (2026, current FEMA P-320 edition). Those figures assume the standard case, an independent reinforced concrete or masonry box built within a wood-framed house, so most of the cost is the box itself. With this project's shell already reinforced concrete and CMU designed for high-seismic Oregon, the marginal items are:

- an ICC 500-rated door and frame assembly, a specific tested product
- a debris-impact-rated vent assembly for ventilation
- any locally added reinforcement or connection detail the engineer of record determines the room needs beyond the house's ordinary structural design (possibly none; whether the room's walls, roof, and slab already meet the ICC 500 design loads is checked, not assumed)
- independent anchorage detailing where ICC 500 requires the room to be isolable from building racking, an engineer's design decision

No published source prices the marginal case with an already-reinforced host; every published figure assumes the wood-frame baseline. The project's number comes from the engineer's ICC 500 load check followed by a quote for the door, the vent, and any identified added work.

**Construction sequence.** A first-construction safe room follows the pour sequence in §6.22 with safe-room items added at the existing hold points:

- door-frame threshold anchors and any local footing reinforcement, at the footing and foundation-wall pre-pour holds
- the frame's manufacturer-specified anchor pattern and any added wall reinforcement, at the wall pre-pour hold
- vent embeds and any roof reinforcement, at the pre-cover holds

One added verification step is required: the rated door and frame installation is signed off against the door manufacturer's tested installation documentation, because installation outside those instructions voids the assembly's rating. The hold-point table in §6.22 includes this step.

**Tsunami siting.** FEMA P-646 is guidance for community vertical-evacuation refuge structures, not a single-family requirement anywhere in Oregon. Its structural concepts transfer voluntarily to a home sited inside a mapped inundation zone:

- breakaway lower-level wall panels engineered to detach before loading the primary structure
- open ground-floor construction that lets water and debris pass through
- design of below-inundation structural elements for the hydrodynamic and debris-impact loads of ASCE 7-16 Chapter 6

Whether the parcel sits inside a mapped zone is read from the current DOGAMI (Oregon Department of Geology and Mineral Industries) tsunami-inundation map before any of this becomes a live design question.

**Dome and vault geometry.** Monolithic dome homes run roughly $100-250 per square foot, roughly $164,000-$500,000 total depending on size and finish (2026 cost guides), overlapping high-end conventional concrete construction. The documented drawbacks are financial and spatial rather than structural. Lenders prefer a single general contractor presenting one complete proposal, and dome construction adds a specialist builder to an owner-managed project. Appraisers lack comparable sales, and dome homes are recorded as sitting on the market longer than conventional houses. Curved walls complicate cabinetry, furniture placement, and acoustics, and the practical response, custom built-ins, adds cost beyond the base figures. Oregon precedent exists at institutional scale (the twin Monolithic Domes of Portland's City Bible Church, in use since 1991); current residential dome-contractor availability in Oregon is confirmed by direct inquiry at build time. A partial application, a single domed or barrel-vaulted safe room inside an otherwise rectilinear house, is structurally reasonable (a compression shell over a small span suits a hardened room) and avoids the whole-house financing and layout drawbacks. No built precedent for the hybrid is documented, and pricing requires a specialty-forming quote against the actual room size and the ICC 500 loads above.

## 6.20 Water-Retaining Structures

**Simple**

A concrete cistern (a buried or ground-level tank storing water) is designed to its own rules, separate from the rules for dry walls. Water presses on every face all the time. The wall must not leak. In an earthquake the stored water itself moves and adds force. Separate design standards apply to those conditions.

**Professional**

A water-retaining structure is designed to the environmental-structures standards, not the dry-wall assumptions of §6.5. ACI 350 governs the structure: sustained hydrostatic load on every face, liquid-tightness, and crack-width control tighter than a dry structural wall's serviceability limit. ACI 350.3 governs the seismic design of liquid-containing structures: impulsive and convective (sloshing) hydrodynamic forces, tank vibration periods, sloshing wave height, and soil-structure interaction. Its stated scope includes concrete structures storing water without a lower size bound, so no size exemption removes a residential cistern from it. Whether the engineer of record applies the full ACI 350.3 methodology or treats the stored water as added seismic mass in the main structural analysis is a scale-dependent engineering judgment for the specific cistern. AWWA D110 and D115 apply to prestressed wire-wrapped and tendon-stressed tanks, a municipal-scale construction method, and do not apply at residential scale.

One documented owner-built poured cistern (Dancing Rabbit Ecovillage) used #6 bars wired on a roughly 1-foot grid, doweled into the base slab. That is a real-world reference point for discussion with the engineer, not a design value; no published general-purpose reinforcement table exists for residential cisterns, and the schedule depends on the tank's height, wall thickness, and edge restraint. Any control or construction joint in a water-retaining wall takes a cast-in waterstop and a sealed exposed face (§6.5). The cistern's sizing, siting, and plumbing are part of the project's water-independence planning; this section contains only the structural design standards.

## 6.21 Two Design Tracks At A Glance

**Simple**

The table compares the two design paths element by element, from foundation to roof, with the engineering cost and the long-life alignment of each. It shows where the paths differ at a glance.

The structural choices on both paths:

| Element | Engineered path | Prescriptive (no-PE) path |
|---|---|---|
| Foundation | Geotechnical-informed engineered foundation; concrete or reinforced masonry stem walls | ORSC R403 footing per Table R403.1 with R403.1.3 SDC reinforcement |
| Above-grade walls | Engineered concrete (ACI 318 / 332) or reinforced masonry (TMS 402); double-wythe permitted | Single-wythe reinforced CMU per R606; or PCA 100 above-grade concrete; SDC C R608 if applicable |
| Wall ties | Stainless steel W2.8 minimum; thermally-broken if R-value driven | N/A for single-wythe |
| Floor system | Hollow-core precast or CIP one-way slab | Manufacturer-engineered wood I-joists or open-web wood trusses on bond beams |
| Roof system | Concrete deck + PMR (primary); concrete deck + standing seam (alternate) | Manufacturer-engineered wood truss with standing-seam metal roofing |
| Wall height | Per engineered design; commonly 9–10 ft for residential | 9 ft cap (10 ft hard limit) |
| Stories above grade plane | Engineered for the project | 3 maximum (R301.2.2.7); cap at 2 for safety margin |
| Roof eave-to-ridge | Per engineered design | ≤ 15 ft |
| Diaphragm openings | Engineered with chord and collector reinforcement | < 50% of diaphragm width |
| Fire performance | Concrete and masonry assemblies; fire ratings inherent | Concrete/masonry walls with wood-framed floor and roof; need fire-rated assemblies where required |
| Engineering cost (2026 Oregon dollars) | $4,000–$10,000 + $1,500–$3,500 geotech | $0 PE for the homeowner; manufacturer-stamped products carry their own engineering |
| Long-life alignment | 100%; full concrete shell | 70–80%; concrete walls and foundation; wood floors and roof on shorter cycles |

## 6.22 Structural Hold Points

Construction cannot proceed past these points without inspection sign-off and (where applicable) engineer-of-record approval.

| Hold point | What gets verified | Who signs off |
|---|---|---|
| Footing (pre-pour) | Bearing surface, footing geometry, reinforcement, anchor bolts, embeds, UFER ground | Local building inspector; engineer of record on engineered foundations |
| Foundation wall (pre-pour) | Reinforcement, vertical bar continuity from footing, anchor bolts, sleeves, dampproofing readiness | Building inspector |
| Foundation drainage and dampproofing/waterproofing (pre-backfill) | Drain rock, perimeter drain, membrane continuity, capillary break | Building inspector |
| Slab subgrade (pre-pour) | Subgrade compaction, capillary break, vapor retarder, soil-gas retarder where applicable, under-slab insulation, sleeves | Building inspector |
| CMU grouting (per lift) | Cleanouts (where required), reinforcement position, lift height | Building inspector; special inspector where required (grout-lift triggers in §6.9; the full program is in the Inspection And Approval Sequence chapter) |
| Concrete placement (at delivery) | Mix-design conformance, slump, air, temperature, batch ticket | Engineer of record on engineered work; special inspector where required |
| Reinforcement at floor and roof level | Bond beam continuity, tie-down anchors, embeds for floor/roof system | Building inspector |
| Floor diaphragm (pre-cover) | Reinforcement (CIP), shop drawings for precast, manufacturer-stamped product (engineered wood) | Building inspector; engineer for engineered diaphragms |
| Roof structure (pre-cover) | Truss installation per manufacturer drawings, anchorage, diaphragm continuity | Building inspector; manufacturer's installation requirements |
| Safe-room rated door and frame (where a safe room is built) | Installation and anchorage against the door manufacturer's tested installation documentation; installation outside those instructions voids the rating | Engineer of record, or special inspector where the safe-room design assigns it |

The embed verification method for every hold point that lists embeds (templates, wiring to reinforcement, the second-person checklist, photographs) is in §6.10.

**Resilience embeds on the pre-pour checklist.** Disaster-specific embeds are cast in during the scheduled pours or added after cure as post-installed retrofits (§6.9); casting in is the clean path. The owner selects which of these the design includes, and each selected item joins the pre-pour embed checklist at its matching hold point:

- safe-room anchorage and rated-door-frame embeds (§6.19)
- a sleeve or conduit for a future generator, propane, or fuel-oil supply line
- a cast-in embed plate or bolt pattern for a communications antenna mast, sized for the site wind load
- an access sleeve or interface for a manual backup well pump, where the water system includes a well

**Special inspection, scoped.** Special inspection is a structural specialty code (OSSC/IBC) program; the base residential code does not operate one. It applies to this project where the engineered design invokes it (grouted CMU per the TMS 602 inspection levels, structural concrete with f'c above 4,000 psi, post-tensioned elements) or where the building official requires it. The engineer of record defines the program in the construction documents.

The Inspection And Approval Sequence chapter contains the inspection-readiness criteria for each hold point. The Foundation, Basement, Slabs, And Concrete Placement chapter contains the construction sequence around the concrete-related holds.

## 6.23 The Structural Standard

The project's structural standard:

1. Every load has a defined path to the soil.
2. Every assembly is designed to a referenced standard (ACI 318/332/PCA 100 for concrete, TMS 402/602 for masonry, ASCE 7 for loads).
3. The design path (engineered or prescriptive) is chosen at design time and held throughout construction.
4. Reinforcement detailing matches the calculations: lap lengths, cover, hook lengths, bond beams, anchor bolts.
5. Concrete mix design matches the exposure class and the long-life target.
6. The structural shell is concrete and reinforced masonry. Wood appears only where the project deliberately accepts a manufacturer-engineered product (roof trusses, floor I-joists) for the prescriptive path.
7. Inspection and special-inspection records cover every hold point.
8. Field changes are treated as design changes when they affect approved work.
