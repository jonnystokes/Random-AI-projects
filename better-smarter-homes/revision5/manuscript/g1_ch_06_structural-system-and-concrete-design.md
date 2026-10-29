# Chapter 6: Structural System And Concrete Design

This chapter covers the structural system that turns site preparation and foundation work into a building. It establishes the load path, names the design path the project takes (engineered or prescriptive), specifies the concrete and reinforced-masonry assemblies, addresses wall ties and reinforcement detailing, lays out the floor and roof options, and identifies the structural hold points where work cannot proceed without sign-off.

This is a concrete-and-reinforced-masonry house. The structural shell uses concrete, masonry, and steel reinforcement. There is no wood framing in the structural shell, with two practical exceptions: manufacturer-engineered wood-truss roofs and manufacturer-engineered wood-I-joist floors are options where the project chooses the prescriptive design path to avoid a structural-engineering line item. The make-versus-buy and the trade-offs are covered in §6.4.

The Soil, Ground Prep, Drainage, And Foundation Risk chapter delivers the soil class and the bearing assumption that the foundation design starts from. The Foundation, Basement, Slabs, And Concrete Placement chapter takes the foundation construction detail (excavation, forming, embeds, slab stack, concrete ordering and placement, curing). This chapter is the structural-design layer between them.

## 6.1 The Structural Goal

The building has to carry every imposed load down to the soil and back up through the bracing system, with margins that make sense for a multi-century design horizon.

**Simple**

A house has weight pulling down (gravity, snow, furniture, occupants), forces pushing sideways (wind, earthquakes, soil pressure on basement walls), and uplift trying to lift parts off (high wind on roof). Every one of those forces has to find a path to the ground without breaking anything along the way. The structural design is the map of those paths.

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

For each load, ask the hard question: where does it go next? If the answer is not obvious from the drawings, the design is not ready.

**Professional**

The structural system requires a complete gravity and lateral load path. Dead load, live load, roof live load, snow load, wind load, seismic load, soil pressure, hydrostatic pressure, and construction loads are collected, transferred through floors and walls as primary elements, resisted by the lateral system, and anchored at the foundation.

For this project, the structural language is regularity:

- aligned bearing walls stacked floor over floor
- continuous reinforced wall lines without offsets
- floor diaphragms tied to wall elements through chord and collector reinforcement
- bond beams or ring beams at key levels
- controlled openings sized within prescriptive or engineered limits
- foundation elements designed from site-specific ground information

The building should be traceable in section. Roof to wall. Floor to wall. Wall to foundation. Foundation to soil. Lateral force to diaphragm. Diaphragm to shear wall. Shear wall to foundation.

A heavy assembly is not automatically a strong assembly. Adding mass without a defined load path adds cost without adding capacity.

**Code**

```
ORSC R301: design criteria for residential structural loading.
  - Establishes baseline gravity, snow, wind, seismic, and flood loads.
  - References the climatic and geographic table at R301.2(1) for site-specific values.

ORSC R301.1.3: engineered design (nonprescriptive design) path.
  - Where structural elements exceed ORSC prescriptive limits or do not conform to this code, those elements shall be designed in accordance with accepted engineering practice.
  - The engineer of record stamps the structural drawings and supporting calculations.

ORSC R301.2: location-specific climatic and geographic design criteria.
  - Adopted by the local jurisdiction.

ORSC R301.2.2: seismic provisions.
  - Adoption of seismic design category and the reinforcing requirements that follow.
  - SDC D0/D1/D2 trigger expanded reinforcement for foundations, walls, and floor diaphragms.

ORSC R301.2.2.5: concrete construction provisions.
  - Above-grade concrete walls in SDC D0/D1/D2 must comply with PCA 100 or be designed in accordance with ACI 318.
  - ACI 332-20 covers the same residential scope as a residential-specific code.

ORSC R301.2.2.6: irregular building conditions.
  - Lists irregularity conditions that trigger engineered analysis for the entire story.
  - Includes offsets in vertical lateral elements, large diaphragm openings, mass irregularities, and mixing wood framing above masonry/concrete in stories above grade plane.

ORSC R301.5: minimum uniformly distributed live loads.
  - 40 psf for habitable rooms (except sleeping rooms at 30 psf).
  - 30 psf for sleeping rooms.
  - 50 psf for stairs.
  - Higher values for decks, garages, and storage areas.

ASCE 7: Minimum Design Loads and Associated Criteria for Buildings and Other Structures.
  - Provides the load combinations, snow shape coefficients, wind pressure calculation, and seismic spectral values that engineered designs use.

Oregon Design Criteria Hub (oregon.gov/bcd): Oregon site-specific design criteria source.
  - Confirms ground snow load, basic wind speed, exposure category, seismic design category for participating jurisdictions.
```

## 6.2 The Design-Path Decision

A concrete-and-masonry residence in Oregon takes one of three design paths. The path drives plan submittal, inspection regime, and whether a licensed structural engineer is required.

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
4. a special-inspection program where required (typically for grouted CMU, structural concrete with f'c > 4,000 psi, or post-tensioned elements)

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

**Code**

```
ACI 318: Building Code Requirements for Structural Concrete.
  - Primary engineered structural concrete design standard.
  - Covers cast-in-place walls, slabs, beams, columns, footings, retaining walls, foundation walls, anchorage, development length, lap splice, cover, and exposure classes.
  - Edition referenced by Oregon adoption: confirm at permit application; ACI 318-19 and 318-25 are in current circulation.

ACI 332-20: Code Requirements for Residential Concrete.
  - Residential-specific code with prescriptive tables.
  - Covers footings, foundation walls, slabs-on-ground, above-grade walls in scope, and Chapter 12 expansive-soil residential design.

PCA 100: Prescriptive Design of Exterior Concrete Walls for One- and Two-Family Dwellings.
  - Referenced by ORSC R301.2.2.5 for above-grade concrete walls in SDC D0/D1/D2.

ORSC R608: prescriptive exterior above-grade concrete walls.
  - Available only in SDC C with limits on wall height, opening size, and reinforcement.

ORSC R404: foundation walls.
  - Prescriptive tables for foundation walls in flat and braced configurations.
  - SDC D0/D1/D2 reinforcement at R404.1.4.

ASTM A615/A615M: deformed reinforcing bars (Grade 60 typical).

ASTM A706: low-alloy reinforcing bars (better weldability and ductility; preferred for seismic).

ASTM C150: Portland cement.

ASTM C94: ready-mixed concrete specification.

ASTM C260, C494: air-entraining and chemical admixtures.

ACI Exposure Class system (F0/F1/F2/F3 for freeze-thaw, S0/S1/S2/S3 for sulfate, W0/W1/W2 for water, C0/C1/C2 for corrosion).
  - Drives concrete mix design parameters: minimum f'c, maximum w/c, air content, cement type, supplementary cementitious materials.
```

## 6.6 Reinforced Masonry Walls

Reinforced concrete masonry units (CMU) form the primary above-grade wall option for this project on the prescriptive path, and a frequent choice on the engineered path. ORSC R606 governs prescriptive masonry; TMS 402-22 governs engineered masonry.

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

**Code**

```
TMS 402-22: Building Code Requirements for Masonry Structures.
  - Engineered masonry design standard.
  - Composite, noncomposite, and veneer wall classifications under §5.1.4.
  - Anchor and tie requirements under §5.1.6.

TMS 602-22: Specification for Masonry Structures.
  - Construction specifications including grout placement, mortar, cleaning, and inspection.

ORSC R606: General Masonry Construction.
  - Prescriptive masonry provisions.
  - Grout proportions at Table R606.2.12.
  - Grout placement at R606.3.5.1 with 8-foot lift maximum and cleanout requirement at 5 feet.

ORSC R606.2.8.3: mortar type for SDC D0/D1/D2.
  - Type M or S Portland cement-lime required for the lateral force-resisting system.
  - Type N is not permitted for the lateral system in SDC D0+.

ASTM C90: Loadbearing Concrete Masonry Units.
  - Minimum compressive strength 2,000 psi net area.
  - Dimensional tolerances and exposure classifications.

ASTM C476: Grout for Masonry.
  - Fine grout and coarse grout proportions.
  - Slump requirements for masonry grout (8 in. minimum, often 10–11 in. for self-consolidating fine grout).

ASTM C270: Mortar for Unit Masonry.
  - Type M, S, N, O mortar proportions and properties.

ASTM C140: Sampling and Testing Concrete Masonry Units.
  - Compressive strength, water absorption, dimensional verification.

ASTM A615/A615M: deformed reinforcing bars (Grade 60 typical).
ASTM A706: low-alloy reinforcing bars (preferred for seismic).
ASTM A951: joint reinforcement for masonry.

ORSC R301.2.2.7: maximum stories above grade plane (3 stories).
```

## 6.7 Wall Ties For Cavity Walls

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

**FRP ties** are not the prescriptive default. AC125 covers externally bonded FRP for strengthening (not new construction ties). AC454 covers FRP rebar in concrete (limited to SDC A or B). TMS 402-22 Appendix D introduces composite reinforcement for masonry partition walls (explicitly partition, not loadbearing exterior cavity walls). Commercial FRP ties exist but require ICC ESR submittal and per-project building-official approval. Treat FRP ties as an engineered alternative requiring documentation, not a prescriptive option.

**Code**

```
TMS 402-22 §5.1.6: anchor and tie requirements for masonry walls.
  - Spacing, size, and frequency requirements.
  - Composite, noncomposite, and veneer-wall provisions.

ASTM A580: Standard Specification for Stainless Steel Wire.
  - Type 304 and Type 316 stainless wire for masonry ties.

ASTM A82: Standard Specification for Steel Wire, Plain, for Concrete Reinforcement.
  - Cold-drawn carbon-steel wire.

ASTM A951: Joint Reinforcement for Masonry.

ICC AC125: Acceptance Criteria for Concrete and Reinforced and Unreinforced Masonry Strengthening Using Externally Bonded Fiber-Reinforced Polymer (FRP) Composite Systems.

ICC AC454: Acceptance Criteria for Fiber-Reinforced Polymer (FRP) Bars for Internal Reinforcement of Concrete Members.

ICC ESR (Evaluation Service Reports).
  - Required for FRP tie products to demonstrate code compliance.
  - Per-project building-official approval typically required.

CMHA TEK 12-01B: Anchors and Ties for Masonry.

CMHA TEK 16-04A: Design of Concrete Masonry Noncomposite (Cavity) Walls.

CMHA TEK 16-01A: Multi-Wythe Concrete Masonry Walls.

BIA Tech Note 28D: Brick Veneer/Concrete Masonry Walls.

BIA Tech Note 44B: Wall Ties for Brick Masonry.
```

## 6.8 Reinforcement, Grout, And Lap Lengths

Detailing controls how reinforcement actually develops the strength the design assumes. Sloppy detailing breaks calculations.

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

Reinforcement placement is verified at each footing inspection, foundation-wall inspection, and (for grouted CMU walls) at each grouting cycle. The Inspection And Approval Sequence chapter takes the inspection detail.

**Code**

```
ORSC R403.1.3: footing and foundation reinforcement in SDC D0/D1/D2.
  - Bottom horizontal #4 placed 3–4 in. from bottom of footing.
  - Top horizontal #4 within 12 in. of top of stem wall.
  - Vertical #4 at 4 ft maximum on center with standard hook to bottom of footing extending 14 in. into stem wall.

ORSC R403.1.8: UFER ground (concrete-encased electrode).
  - Uncoated #4 minimum, 20 ft long, encased in minimum 2 in. of concrete, near bottom of footing.

ORSC R602.11: anchor bolts for sill plates (transferring to upper wall systems).
  - 1/2 in. minimum diameter, 7 in. embedment, 6 ft maximum on center (4 ft for SDC D2 two-story), 12 in. maximum from plate ends.
  - 3 in. by 3 in. by 0.229 in. plate washers required.

ORSC R606.3.5.1: grout placement.
  - Maximum 8 ft lift; cleanouts required at base of walls when total grout pour exceeds 5 ft; special inspection during grouting required when total pour exceeds 8 ft.

TMS 602: masonry construction specifications.
  - Cleanout sizing, grout consolidation, inspection during placement.

ACI 318 §25.4: development and lap splice of deformed bars.
  - Provides the engineering basis for lap-length tables.
```

## 6.9 Floor Systems

Floor systems are the structural element with the broadest range of options for a concrete-and-masonry house. Five viable paths, ranked by alignment with the long-life concrete philosophy:

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

**Code**

```
ACI 318 Chapter 7 (one-way slabs) and Chapter 8 (two-way slabs).
  - Engineered concrete floor design.
  - Cover, reinforcement ratios, deflection limits.

ACI 318 §7.7 and §11.7: openings in slabs and slab diaphragms.
  - Trim reinforcement around openings.
  - Boundary reinforcement and diagonal bars.

PCI Manual for the Design of Hollow-Core Slabs and Walls.
  - Industry-standard reference for hollow-core precast.

ACI 332-20 covers slab-on-ground for residential construction.
  - Not applicable to elevated structural slabs (use ACI 318).

ASCE 7 live-load values referenced by ORSC.
  - Habitable rooms: 40 psf live load.
  - Sleeping rooms: 30 psf.
  - Stairs: 50 psf (concentrated 300 lb).
  - Decks: 40 psf (60 psf for some occupancies).

Manufacturer-engineered systems:
  - Wood I-joist product evaluation reports (PER) under ICC ESR.
  - Open-web wood truss design by manufacturer with stamped shop drawings.
  - Hollow-core precast with manufacturer-stamped shop drawings and erection sequence.
```

## 6.10 Roof Structure

Roof structure is the highest-risk durability item if specified wrong. The structural shell aims for multi-century life; the roofing surface aims for 30–80 years. The roof framing has to bridge those time horizons.

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
- minimum two roof drains per primary drainage area (per IPC 1106)
- overflow scupper or secondary drainage sized for 100-year storm + drain failure
- ASCE 7 ponding-instability check on concrete deck
- snow load per OSU/SEAO snow lookup tool with 25 psf minimum

**Solar integration:** concrete deck makes future PV addition trivial. Embed cast-in anchors or post-tensioned attachment plates at design time. Avoid through-roof penetrations if possible; ballasted PV racks on a PMR-protected concrete deck are the cleanest long-life-friendly approach.

**Code**

```
ORSC R802: wood roof framing.
  - Span tables for rafters and ceiling joists.
  - Used for the prescriptive wood-truss-roof path.

ORSC R803: roof sheathing.
  - Plywood and OSB requirements per Table R803.1.

ORSC R806: roof ventilation.
  - Vented and unvented (R806.5) roof assembly requirements.

ORSC R905: roof coverings.
  - R905.10 for metal panel roofing.
  - Material-specific installation requirements.

ACI 318 Chapters 7 and 8 for engineered concrete roofs.

ASCE 7: snow load shape coefficients, drift, partial loading.

OSU/SEAO snow load lookup (snowload.seao.org/lookup.html): site-specific ground snow load.

IPC 1106: roof-drain sizing.

IBC Chapter 15 (referenced for roofs not covered by ORSC R905) and SPRI/NRCA technical references for low-slope roof design.
```

## 6.11 Stair Openings And Diaphragm Continuity

An opening interrupts the in-plane diaphragm. Trim reinforcement around the opening restores the load path.

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
ACI 318 §7.7: openings in slabs.
  - Trim reinforcement around openings.

ACI 318 §11.7: shear at openings.
  - Special reinforcement requirements.

ACI 318 §11.6: minimum reinforcement for slabs.

ORSC R301.2.2.6: irregular building conditions.
  - Diaphragm openings exceeding stated thresholds trigger engineered design.

TMS 402-22 §5.1.1: bond beam continuity at openings.
```

## 6.12 Service Layer And Story-Height Classification

A service layer (a horizontal void between floors used for mechanical, electrical, and plumbing routing) interacts with the structural design and the code definition of "story." Mismanagement of service-layer height creates plan-review problems.

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
ORSC R202: definition of "story."

ORSC R302.11: fireblocking in concealed spaces.

ORSC R302.12: draftstopping in floor/ceiling assemblies.

ORSC R305: ceiling height (7 ft minimum in habitable rooms).

ORSC R303: light and ventilation.

ORSC R310: emergency escape and rescue openings.

ORSC R311: means of egress.

ORSC R325: mezzanines.

ORSC R408: crawl spaces.

OMSC restrictions on plenum spaces and combustibles.
```

## 6.13 Concrete Durability And Mix Discipline

Concrete designed to last centuries requires deliberate mix design and placement discipline. Standard residential concrete is designed for ~50-year service. Long-life concrete adds margins on permeability, reinforcement protection, and thermal stability.

**Professional: exposure-class targets**

ACI 318 organizes concrete durability by exposure class. Mix-design parameters scale to the highest applicable class.

| Exposure | Class | Concern |
|---|---|---|
| Freeze-thaw | F0 (none) / F1 (moderate) / F2 (severe, no salts) / F3 (severe, with salts) | Frost damage in saturated freeze-thaw cycling |
| Sulfate | S0 / S1 (moderate) / S2 (severe) / S3 (very severe) | Sulfate attack on cement paste |
| Water | W0 / W1 (in contact) / W2 (low-permeability required) | Permeability and water transmission |
| Corrosion | C0 / C1 / C2 (severe; with chlorides) | Reinforcement corrosion in chloride environments |

For an Oregon long-life house above grade in mild exposure: F1, S0, W0, C1. For below-grade walls in contact with soil with potentially aggressive soils: F1 or F2, S1, W1 or W2, C1 or C2 depending on chloride exposure.

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

**Code**

```
ACI 318 Chapter 19: concrete durability requirements.
  - Exposure-class system and mix-design limits.
  - Maximum w/c ratio, minimum f'c, air-entrainment requirements by exposure class.

ACI 332-20 Chapter 4: concrete materials and mix design for residential.

ACI 305R: Hot Weather Concreting.
  - Temperature, humidity, and curing controls in hot weather.

ACI 306R: Cold Weather Concreting.
  - Protection from freezing during placement and curing; minimum temperature requirements.

ACI 308R: Guide to Curing Concrete.
  - Curing methods and durations.

ASTM C150: Portland cement (Type I, II, III, IV, V).
ASTM C595: Blended hydraulic cements.
ASTM C33: Concrete aggregates.
ASTM C618: Coal fly ash and raw or calcined natural pozzolan.
ASTM C989: Slag cement (granulated blast-furnace slag).
ASTM C1240: Silica fume.
ASTM C260: Air-entraining admixtures.
ASTM C494: Chemical admixtures.
ASTM C94: Ready-mixed concrete (specification, batching, mixing, delivery).
ASTM C172: Sampling fresh concrete.
ASTM C143: Slump.
ASTM C231: Air content (pressure method).
ASTM C39: Compressive strength of cylindrical specimens.
```

## 6.14 Fiber Reinforcement: Boundaries

Fiber-reinforced concrete (FRC) has legitimate uses but is not a replacement for primary structural reinforcement.

**Professional**

ACI 544.4R-18 sets the boundary: fibers can supplement and reduce conventional reinforcement in applications where continuous reinforcement is not essential to safety and integrity (slabs-on-ground, pavements, overlays, shotcrete linings, slabs-on-piles, some precast units). Fibers do not replace primary flexural reinforcement in residential structural members under code.

ACI 318 admits steel fibers as shear reinforcement in specific contexts (§11.4.6.1), and industrial slab-on-ground design routinely uses FRC as primary reinforcement under TR 34 (UK) and ACI 360R. For the residential structural shell, FRC is supplementary, not primary.

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
ACI 544.4R-18: Guide to Design with Fiber-Reinforced Concrete.
  - Defines where fibers may serve as primary versus supplementary reinforcement.

ACI 318 §11.4.6.1: steel fibers as shear reinforcement.
  - Engineering-controlled use in defined contexts.

ACI 360R: Design of Slabs-on-Ground.

ASTM C1116: Fiber-Reinforced Concrete.
ASTM C1609: Flexural performance of fiber-reinforced concrete (third-point loading).
```

## 6.15 Two Design Tracks At A Glance

Summary table covering the structural choices on both paths:

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

## 6.16 Structural Hold Points

Construction cannot proceed past these points without inspection sign-off and (where applicable) engineer-of-record approval.

| Hold point | What gets verified | Who signs off |
|---|---|---|
| Footing (pre-pour) | Bearing surface, footing geometry, reinforcement, anchor bolts, embeds, UFER ground | Local building inspector; engineer of record on engineered foundations |
| Foundation wall (pre-pour) | Reinforcement, vertical bar continuity from footing, anchor bolts, sleeves, dampproofing readiness | Building inspector |
| Foundation drainage and dampproofing/waterproofing (pre-backfill) | Drain rock, perimeter drain, membrane continuity, capillary break | Building inspector |
| Slab subgrade (pre-pour) | Subgrade compaction, capillary break, vapor retarder, soil-gas retarder where applicable, under-slab insulation, sleeves | Building inspector |
| CMU grouting (per lift) | Cleanouts (where required), reinforcement position, lift height | Building inspector; special inspector where required |
| Concrete placement (at delivery) | Mix-design conformance, slump, air, temperature, batch ticket | Engineer of record on engineered work; special inspector where required |
| Reinforcement at floor and roof level | Bond beam continuity, tie-down anchors, embeds for floor/roof system | Building inspector |
| Floor diaphragm (pre-cover) | Reinforcement (CIP), shop drawings for precast, manufacturer-stamped product (engineered wood) | Building inspector; engineer for engineered diaphragms |
| Roof structure (pre-cover) | Truss installation per manufacturer drawings, anchorage, diaphragm continuity | Building inspector; manufacturer's installation requirements |

The Inspection And Approval Sequence chapter takes the inspection-readiness criteria for each hold point. The Foundation, Basement, Slabs, And Concrete Placement chapter takes the construction sequence around the concrete-related holds.

## 6.17 The Structural Standard

The structural design closes the gap between architecture and construction. For this project, the standard is:

1. Every load has a defined path to the soil.
2. Every assembly is designed to a referenced standard (ACI 318/332/PCA 100 for concrete, TMS 402/602 for masonry, ASCE 7 for loads).
3. The design path (engineered or prescriptive) is chosen at design time and held throughout construction.
4. Reinforcement detailing matches the calculations: lap lengths, cover, hook lengths, bond beams, anchor bolts.
5. Concrete mix design matches the exposure class and the long-life target.
6. The structural shell is concrete and reinforced masonry. Wood appears only where the project deliberately accepts a manufacturer-engineered product (roof trusses, floor I-joists) for the prescriptive path.
7. Inspection and special-inspection records cover every hold point.
8. Field changes are treated as design changes when they affect approved work.
