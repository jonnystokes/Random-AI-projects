# Section 4 — Structural Design

*How the building holds itself up*

This section covers the bones of the home: the foundation, the walls, the floors between levels, the service layer that hides utilities, the roof, and the testing program that validates every design choice. This is where the 1000-year goal is either won or lost. Everything else in the house — the plumbing, the electrical, the paint, the appliances — can be replaced. The structure is what lasts.

---

## 4.1 Overall Building Shape and Size

**Plain language:** The home is a square, stacked three levels high. Each level is about the same size as the ones above and below. The square shape is simpler to build, stronger against wind and earthquakes, and easier to design than an irregular shape.

**Technical detail:** Design parameters:

- **Footprint shape:** Square
- **Footprint width:** 50-100 ft per side, depending on desired floor area
- **Per-floor area:** 2,500 sq ft (50x50 ft) to 10,000 sq ft (100x100 ft)
- **Total conditioned area (3 levels):** 7,500 to 30,000 sq ft
- **Level count:** 3 (basement + 2 above-grade floors)
- **Internal layout:** 3x3 room grid (9 rooms per level, flexible use)
- **Wall alignment:** All walls on all levels align vertically, so walls on upper floors sit directly above walls on lower floors
- **Door placement:** Door locations can vary between floors; the structure depends on the walls, not the doors

**Why a square:**
- Simplest shape to build, least waste in materials
- Equal strength in all directions for wind and seismic loads
- Minimum exterior wall area per square foot of floor space (energy efficient)
- Symmetrical load distribution to the foundation
- Easier to lay out a regular 3x3 grid of rooms

**Why walls align vertically:**
- Each wall carries the load of every wall directly above it straight down to the foundation
- No need for beams, transfer structures, or special engineering at the floor transitions
- Matches the code-friendly prescriptive path (no engineered structural design required if prescriptive limits are met)

**Key code references:**
- ORSC R301 (design criteria — general structural requirements)
- ORSC R606 (general masonry construction — prescriptive requirements)

---

## 4.2 Foundation — Mat Slab with Extended Edge

**Plain language:** The foundation is a single thick concrete slab that covers the entire footprint of the building, plus a margin that sticks out past the walls. All the walls sit directly on top of this slab. It spreads the weight of the building evenly across the ground.

**Technical detail:** Mat foundation (also called raft foundation) design:

- **Shape:** Single continuous concrete slab under the entire building
- **Extension beyond walls:** 6-12 inches past the exterior walls for edge load distribution
- **Thickness in field (under floor area only):** 6-8 inches
- **Thickness under walls (thickened edge / integral grade beam):** 12-16 inches
- **Rebar:** #5 bar (5/8-inch diameter) in a grid pattern, typically 12 inches on center both ways, with additional bars in the thickened wall zones
- **Concrete strength:** 4,000-5,000 psi (pounds per square inch — concrete compressive strength at 28 days after pouring)
- **Extends below frost depth:** The foundation edge extends down below the frost depth for the climate zone (12-36 inches)

**Why a mat foundation instead of conventional footings plus a slab:**
- Matches the "overbuild and simplify" philosophy — one pour instead of two separate structural systems
- Distributes concentrated wall loads over a wide area
- Provides a built-in waterproofing surface at the lowest point of the building
- Handles seismic loads by acting as a single rigid plate instead of discrete footings
- Eliminates the possibility of differential settlement between footings and slab

**Stack-up from bottom to top under the slab:**
1. Native soil or compacted fill (see 4.3 for under-slab insulation layers)
2. Compacted gravel base (6-12 inches of 3/4-inch crushed rock)
3. Capillary break layer (4 inches of clean 1-inch+ crushed rock with no fines)
4. Vapor barrier (6-mil polyethylene minimum, 10-15 mil recommended)
5. Under-slab insulation (Type XIV EPS, 40 psi, 4 inches — see 4.3)
6. Second vapor barrier (optional, recommended)
7. Radiant floor tubing (attached to the rebar grid below)
8. Rebar grid on chairs
9. Concrete slab

**Key code references:**
- ORSC R403 (footings — footing size and reinforcement)
- ORSC R506 (concrete floors on ground — slab-on-grade)
- ACI 332 (Residential Code Requirements for Structural Concrete — reference standard)

---

## 4.3 Under-Slab Insulation

**Plain language:** Between the ground and the concrete slab is a layer of rigid foam insulation. This keeps the heat in the slab (important for radiant floor heating) and prevents the cold ground from sucking warmth out of the building.

**Technical detail:** Insulation specification:

- **Material:** Type XIV EPS (Expanded Polystyrene, 3 lb density nominal)
- **Compressive strength:** 40 psi (handles all residential structural loads with substantial safety factor)
- **R-value:** R-4 per inch
- **Thickness:** 4 inches (R-16 continuous)
- **Installation:** Two staggered 2-inch layers to eliminate thermal bridges at seams
- **Coverage:** Under the entire slab footprint, extending to the slab edge

**Why Type XIV EPS instead of XPS or standard EPS:**
- Compressive strength (40 psi) comfortably exceeds the worst-case load under the walls (calculated at approximately 21 psi for this design)
- Long-term moisture performance: EPS retains 94% of original R-value after 15 years (versus 52% for XPS in side-by-side studies)
- Lower water absorption: EPS absorbs about 5% water by volume versus 18% for XPS over time
- Cost-effective compared to XPS
- Available in standard 4x8 sheets, 2-inch thickness

**Why 4 inches is the right thickness:**
- Oregon code minimum for heated slabs is R-10 (roughly 2-2.5 inches)
- This design uses R-16 (4 inches) to exceed code by 60%
- With radiant floor heating and a ground-source heat exchanger, the insulation R-value has a direct effect on heating efficiency
- Additional inches beyond 4 provide diminishing returns per dollar

**Bedding and preparation:**
- Compacted 95% Proctor density native soil or imported fill
- 2-inch sand blinding layer (fine sand screeded flat) creates a smooth, uniform surface
- The sand layer acts like a "thermal pad" between the rough ground and the foam, eliminating air gaps

**Key code references:**
- ORSC N1101 (energy efficiency — thermal envelope requirements)
- ORSC N1102 (thermal envelope — slab insulation R-values)
- ASTM C578 (standard specification for rigid cellular polystyrene thermal insulation)

---

## 4.4 Walls — Double-Wythe Cavity Construction

**Plain language:** The walls are made of two separate walls with insulation sandwiched between them. The inner wall is structural and holds up the building. The outer wall is decorative — it protects the insulation and gives the building a clean block-and-stone appearance. In between is 4 inches of rigid foam insulation.

**Technical detail:** Double-wythe cavity wall assembly:

**Inner wythe (structural):**
- 8x8x16 CMU (Concrete Masonry Unit — standard concrete block, nominal 8-inch wide, 8-inch tall, 16-inch long)
- Laid in running bond pattern (each course offset from the one below by half a block)
- Rebar in designated cells, grouted solid with concrete
- Ungrouted cells available for utility chases or insulation fill
- Load-bearing — carries the full weight of the building above

**Cavity (insulation layer):**
- 4 inches wide nominal
- Filled with 4 inches of rigid polyiso foam board insulation, installed as two staggered 2-inch layers
- Small air gap (0.25 inch) allowed for drainage and installation tolerance
- Continuous from below grade to the top of the wall

**Outer wythe (decorative, non-load-bearing):**
- 4x8x16 partition block (4-inch wide partition-grade concrete block)
- Laid in running bond
- Not structural — carries only its own weight
- Protects the insulation from weather, UV, and impact
- Provides the finished exterior appearance (can be painted, stained, or left as bare concrete)
- Weep holes at the base every 24-32 inches for drainage of any incidental moisture that gets past the outer wythe

**Connection between wythes:** See 4.5.

**Insulation performance:**
- Polyiso R-value: R-6 to R-6.5 per inch
- 4 inches = R-24 to R-26 continuous (the "continuous" means no thermal bridges through studs or framing)
- Oregon code minimum for above-grade walls: R-15 continuous (this design exceeds code by roughly 60%)

**Why this assembly:**
- Inner wythe carries loads; outer wythe provides weather protection
- Thermal mass (the heavy concrete blocks) is inside the insulation layer, which keeps indoor temperatures stable
- Outer wythe is sacrificial — if damaged, can be repaired without affecting the structure
- Exterior aesthetic is solid stone appearance without needing expensive full-depth stone
- Insulation is protected from weather, fire, UV, and pest damage

**Key code references:**
- ORSC R606 (general masonry construction — prescriptive wall design)
- ORSC R608 (reinforced masonry construction — rebar and grout requirements)
- ORSC N1102 (thermal envelope — above-grade wall insulation)

---

## 4.5 Wall Ties Between the Two Wythes

**Plain language:** Something has to hold the outer wall to the inner wall so wind doesn't blow it over. Standard metal ties would work but they'd conduct cold through the insulation. Better option: fiberglass-reinforced polymer (FRP) ties. Strong, commercial-grade, and they don't conduct heat.

**Technical detail:** Wall tie specification:

- **Material:** Fiberglass-Reinforced Polymer (FRP) composite
- **Thermal conductivity:** Approximately 200x lower than steel
- **Embedment:** Both ends embedded in mortar joints of their respective wythes during construction
- **Spacing:** 16 inches vertical, 32 inches horizontal (matches code minimum for masonry cavity walls); closer spacing at corners and around openings
- **Load rating:** 1,000+ lbs per tie (for commercial-grade FRP ties)
- **Installation:** Placed during wall construction, not retrofit

**Why not steel ties:**
- Steel thermal conductivity (~50 W/mK) is 2,000x higher than foam insulation (~0.025 W/mK)
- Steel ties at typical spacing can reduce the effective R-value of a foam cavity wall from R-24 down to R-9-12
- Eliminates the value of expensive insulation

**Why not cheap plastic ties:**
- Standard plastic wall ties are not rated for structural loads
- FRP ties are engineered, tested, and have published load ratings

**Additional ties at high-stress areas:**
- Corners: every course
- Openings (doors, windows): around the perimeter
- Top of walls: at the bond beam level

**Bed joint reinforcement (optional addition):**
- Horizontal FRP or stainless steel ladder reinforcement laid into the mortar every 2-3 courses (16-24 inches vertical)
- Adds horizontal tensile strength to masonry walls
- Reduces cracking from thermal movement and minor settlement
- Installed during construction as part of the mortar work

**Key code references:**
- ORSC R606.10 (anchorage — lateral support and wall ties)
- TMS 602 (specification for masonry structures — tie requirements)

---

## 4.6 Rebar and Grouting Strategy

**Plain language:** Inside the hollow cells of the concrete blocks, vertical rebar runs from the foundation all the way up. Those cells get filled with concrete, creating columns of steel-reinforced concrete inside the block walls. Horizontal rebar runs at floor levels to tie the whole building together.

**Technical detail:** Reinforcement layout:

**Vertical reinforcement (in block cells):**
- #5 rebar (5/8-inch diameter) minimum for 8-inch block
- Spacing: every cell, or every other cell, or every 4 feet depending on seismic zone and design
- Anchored into the foundation slab (dowels placed in the foundation pour extending up at least 40 bar diameters)
- Continuous from foundation to top bond beam
- Overlaps (lap splices) minimum 40 bar diameters where rebar pieces join
- Cells containing rebar are fully grouted with concrete

**Horizontal reinforcement:**
- Bond beam at the top of each wall and at each floor level
- Bond beam is a course of special bond beam blocks (u-shaped or knockout blocks) with horizontal rebar laid in and grouted solid
- Rebar size: typically two #5 bars in each bond beam
- Runs continuously around the entire perimeter of each floor level

**Grouted vs. ungrouted cells:**
- **Grouted cells:** Contain rebar, filled with concrete grout. Load-bearing and structural.
- **Ungrouted cells:** Hollow, used for utility chases (electrical conduit, plumbing risers, low-voltage wiring)
- The pattern of grouted vs. ungrouted cells is part of the wall design

**Grout specification:**
- 2,000-3,000 psi compressive strength (lower than concrete slab because it's in confined spaces)
- High slump (fluid consistency) to flow around rebar and fill voids
- Poured in lifts of 4-5 feet maximum to prevent hydraulic pressure from blowing out the wall

**Key code references:**
- ORSC R608 (reinforced masonry construction — rebar placement and sizing)
- TMS 402 (building code requirements for masonry structures)

---

## 4.7 Concrete Mix Design for 1000-Year Service

**Plain language:** Regular concrete lasts 50-100 years because water and oxygen eventually get to the rebar and make it rust. Rust expands, cracks the concrete, and the whole thing falls apart. This design uses a concrete recipe that water can barely penetrate, with additives that protect the rebar chemically, plus extra thickness of concrete covering every rebar — all together targeting a lifespan measured in centuries.

**Technical detail:** Mix design strategy:

**Water-to-cement ratio:**
- Target: 0.40 or lower
- Effect: Denser concrete, far less permeable to water, oxygen, and chlorides
- This single variable has more effect on longevity than any other choice

**Cement replacements (pozzolanic admixtures):**
- 20-30% of cement replaced with fly ash (a byproduct of coal combustion, used as a cement substitute)
- OR 20-30% replaced with ground granulated blast furnace slag
- PLUS 5-10% silica fume (fine silica particles that fill microscopic gaps in the concrete matrix)
- Effect: Orders-of-magnitude reduction in permeability, continued strength gain for decades, self-healing of microcracks through ongoing pozzolanic reaction

**Corrosion-inhibiting admixture:**
- Calcium nitrite or amine-based inhibitor mixed into the concrete
- Effect: Chemically binds to rebar surface and resists corrosion even if chlorides eventually reach the steel

**Rebar cover (concrete thickness over the rebar):**
- Code minimum: 1.5-2 inches
- This design: 3-4 inches
- Effect: Doubles or triples the time required for carbonation (the slow chemical process where CO2 from the air eventually reaches the rebar) or chlorides to reach the steel

**No chlorides in the mix:**
- No calcium chloride accelerators
- No seawater
- Clean sand, clean gravel, clean water
- Effect: Rebar environment starts chloride-free

**Air entrainment:**
- 4-7% air entrainment in concrete exposed to freeze-thaw (the foundation walls below grade, the slab edges, the outer wythe if exposed)
- Effect: Microscopic air bubbles in the concrete give water somewhere to expand as it freezes, preventing cracking over hundreds of freeze-thaw cycles

**Rebar material choice:**
- Plain black rebar is acceptable when all the above measures are in place (dense concrete + inhibitors + thick cover = rebar never sees corrosion conditions)
- Galvanized rebar (zinc-coated) is an upgrade for the most exposed areas (foundation edges, slab edges)
- Stainless steel rebar is the ultimate but cost-prohibitive for the whole structure
- Epoxy-coated is NOT recommended — handling damage creates pinhole corrosion cells

**Validation:** All concrete mix choices should be validated through the in-house testing program (see Section 4.15) before committing to the final mix design.

**Key code references:**
- ACI 318 (building code requirements for structural concrete — mix design and cover requirements)
- ACI 332 (residential code requirements for structural concrete)

---

## 4.8 Floors Between Levels — Block-on-Side Course with Rebar and Slab

**Plain language:** At each floor level, the top course of block is rotated onto its side so the holes face horizontally. Horizontal rebar passes through those holes, tying the walls together and providing support for the floor slab above. Then a concrete floor is poured on top.

**Technical detail:** Floor transition assembly:

**Sideways block course:**
- Top course of the wall at each floor level is oriented with cells horizontal
- Horizontal rebar passes through the cells
- Provides tensile reinforcement in the horizontal direction
- Provides a natural channel for horizontal electrical or low-voltage runs if needed
- Ties the walls on all sides of the building together at each floor level, creating a "ring" of rebar-reinforced concrete

**Grouting the sideways course:**
- Cells filled with grout after rebar placement
- Creates a continuous reinforced horizontal beam around the entire perimeter

**Floor slab above:**
- Concrete slab poured on top of the sideways block course
- Slab thickness: 6-12 inches depending on span and load
- Rebar: grid in the top and bottom of the slab
- Fiber reinforcement: steel fibers and/or polypropylene fibers mixed into the concrete
- Optional: concrete ribs (integral deeper beams poured with the slab, dividing the floor area into panels) for stiffness and load capacity

**Ribbing pattern:**
- Ribs spaced to divide each floor into smaller panels
- Panel size: 6 ft to 12 ft per side depending on testing and load requirements
- Rib depth: additional 6-12 inches below the slab bottom
- Rib width: 6-8 inches
- Rib reinforcement: heavy rebar in the bottom of each rib, tied to the slab rebar

**Optional steel joist reinforcement:**
- Open-web steel joists can be added horizontally under the slab for additional load capacity
- Joists pass through the horizontal cells of the sideways block course
- This is the "optional overkill" upgrade, not required if the slab and rib design is sized correctly

**Floor load design:**
- Residential live load: 40 psf (code minimum for living spaces)
- This design: target 200-400 psf capacity (5-10x safety factor)
- Accounts for potential future heavy loads (commercial kitchen equipment, safes, aquariums, etc.)

**Key code references:**
- ORSC R301.5 (live loads — residential)
- ORSC R502 (wood floor framing — used as reference for loads even though this is concrete)
- ACI 318 (concrete slab design)

---

## 4.9 Floor Slab Design — Fiber-Reinforced Concrete with Testing-Driven Thickness

**Plain language:** The concrete floors are made with fibers mixed in (steel fibers, plastic fibers, or both) to make the concrete tougher and more crack-resistant. The exact thickness, fiber type, and rebar size are determined by destructive testing of sample slabs before committing to the final design.

**Technical detail:** Fiber-reinforced concrete specification:

**Fiber types:**
- **Steel fibers** (SFRC — Steel Fiber Reinforced Concrete): add ductility and post-crack toughness. The concrete still holds load after cracking instead of shattering. Dosage: 30-90 lbs per cubic yard.
- **Polypropylene fibers** (synthetic macro-fibers): reduce plastic shrinkage cracking during cure. Dosage: 0.1-0.2% by volume.
- **Combined** (hybrid): both fibers together for maximum performance.

**Structural design:**
- Slab thickness validated through testing program (see 4.15)
- Rebar grid in top and bottom of slab
- Rebar size, spacing, and overlap determined through testing
- Rib spacing and depth determined through testing

**Testing-driven approach:**
- Build sample slabs at multiple thicknesses, fiber types, and fiber dosages
- Test each sample to failure under increasing load
- Plot the results (load at failure vs. thickness, fiber content, rebar size)
- Select a design point that provides 5-10x safety factor over the design load
- This approach produces a quantified, data-driven design rather than guessing

**Why over-design to 200-400 psf capacity:**
- Code minimum (40 psf) is a safety floor, not a design target
- Higher capacity enables future flexibility (commercial kitchen equipment, heavy storage, aquariums, etc.)
- Negligible cost increase once forms and rebar are already set up
- Peace of mind for a home designed to last centuries

**Key code references:**
- ACI 544 (fiber reinforced concrete — design and testing)
- ASTM C1609 (flexural performance of fiber-reinforced concrete)
- ASTM C39 (compressive strength of concrete cylinders)

---

## 4.10 Optional Steel Joist Reinforcement

**Plain language:** If the concrete floor design still isn't strong enough or if extra redundancy is wanted, steel joists can be added under the floor. These pass through the horizontal cells of the sideways block course at each floor level. This is optional and probably overkill, but it's an option on the table.

**Technical detail:** Steel joist option:

**Joist type:** Open-web steel joists (commercial grade, pre-fabricated to specification)
**Depth:** Sized to fit through the 8-inch horizontal block cells minus tolerance
**Spacing:** 4-8 feet on center under the slab
**Support:** Joists rest on the sideways block course and extend across the full span
**Connection:** Welded or bolted to embed plates at each wall

**When to use:**
- Very large spans (greater than 20 feet clear between bearing walls)
- Very high load requirements
- Extra redundancy for critical structural elements

**When to skip:**
- Normal residential spans (up to 20 feet)
- Properly designed fiber-reinforced slab with adequate thickness and ribs

**Honest assessment:** For this design's 3x3 room grid with wall spacing of 15-35 feet between load-bearing walls, the concrete slab with fiber reinforcement and rebar grid will carry the load without steel joists. This option exists mainly for very large footprints or peace-of-mind overbuild.

---

## 4.11 Service Layer Construction

**Plain language:** Between each floor is a 4-5 foot tall crawlable space where all the plumbing, electrical, and HVAC run. It's not another floor of the house — it's a maintenance space. The "floor" of this space is a perforated metal walkway bolted to the walls, strong enough for a person to walk on without flexing or creaking.

**Technical detail:** Service layer assembly:

**Height:** 4-5 feet (adjustable in final design based on duct sizes and wire routing needs)

**Structural note:** The service layer's metal walkway does NOT structurally support the floor above. The concrete floor slab above sits directly on the sideways block course and transfers load to the walls. The walkway only supports people and tools during maintenance.

**Walkway material:**
- Perforated steel grating (the kind used in factories and commercial catwalks)
- Non-flammable (meets the design philosophy of no wood anywhere)
- Self-draining if any water reaches it
- Bolted to the walls on all sides, spanning across the open space between walls

**Walkway support:**
- Steel angle brackets bolted to the inner wythe of the wall
- Grating rests on the angles and is bolted to them
- Rubber gaskets at every bolted connection prevent creaking and rattling from thermal expansion and contraction

**Ceiling below (the underside of the service layer visible from the living space below):**
- Non-flammable drywall (gypsum board) screwed to metal studs or furring
- Metal studs bolted to the underside of the concrete floor slab above
- Fire-rated construction
- Smooth finished surface for painting

**Access to the service layer:**
- Pull-down ladder or removable hatch in the ceiling at one or more locations per floor
- Clearly labeled as "utility / mechanical access"
- No permanent stairs (would classify the space as habitable and change code treatment)

**Zoning note:** The service layer is intentionally designed as non-habitable utility space. No permanent lighting for occupancy, no fixed stairs, labeled as mechanical space on the plans. This keeps the building legally classified as 2 stories + basement, not 4 stories.

**Key code references:**
- ORSC R302 (fire-resistant construction)
- ORSC R311 (means of egress — stairs required for habitable spaces; pull-down access acceptable for utility spaces)

---

## 4.12 Roof Options

**Plain language:** Two roof options are kept open, each with its own character. No default — the choice depends on the specific home being built and the preferences at that time.

### 4.12a Option A — Concrete Slab with Parapet and Internal Drains

**Plain language:** A flat concrete roof with a short wall (parapet) around the edge, like the top of an old-world castle or a modern commercial building. Water drains inward through drain ports in the slab and down through internal pipes. The roof surface can be used as a rooftop patio.

**Technical detail:**
- Structural concrete slab matches the design of the interior floor slabs
- Slight slope toward drain ports: 1/4 inch per foot (roughly 2%, visually imperceptible)
- Parapet wall: 36-42 inches tall around the entire perimeter, integral to the wall structure, doubles as a code-compliant guardrail for rooftop access
- Drain ports: minimum 2 primary drains plus 2 overflow drains, 4-inch pipe minimum
- Drain piping runs inside the building envelope (insulated, freeze-protected)
- Waterproofing: hot-applied rubberized asphalt membrane or liquid-applied silicone coating, protected by gravel ballast or paver deck
- Insulation: continuous rigid foam on top of the slab, under the waterproofing (warm roof construction) OR inside the service layer below (cold roof construction)

**Pros:**
- Matches the castle aesthetic mentioned in the design philosophy
- Provides rooftop deck / patio potential
- Zero wood anywhere
- Structurally consistent with the rest of the building
- Parapet hides rooftop HVAC equipment and solar arrays

**Cons:**
- Higher weight (concrete + ballast + drains can exceed 100 psf)
- Internal drains are the single biggest failure point — require diligent maintenance
- More expensive per square foot than option B
- Requires careful waterproofing detail work

### 4.12b Option B — Steel Deck on Open-Web Joists, 3:12 Shed Slope

**Plain language:** A single-slope shed roof — one side of the building is tall, the other side is short, one continuous sheet of metal roofing runs from one side to the other. Open-web steel joists (like factory-made trusses) span between the walls and support the metal deck.

**Technical detail:**
- Structural: open-web steel joists at 4-6 feet on center, spanning between the top bond beam on opposite walls
- Deck: corrugated steel deck welded or fastened to the joists
- Waterproofing: standing seam metal roofing panels OR single-ply membrane (TPO/EPDM) depending on preference
- Insulation: closed-cell spray polyurethane foam on the underside of the deck (4-6 inches, R-24 to R-36)
- Panel seams: butyl tape sealant between laps, mechanical fasteners clamping through
- Slope: 3:12 (3 inches of rise per 12 inches of run — 14 degrees)
- Length: one continuous sheet from high side to low side where possible, with overlapping sheets using butyl tape sealant where the building exceeds single-sheet length

**Pros:**
- Lighter than concrete slab (10-15 psf structure)
- Faster and cheaper to build
- No internal drains — water sheds to one side and off the building
- Metal roof + standing seam is ideal for solar mounting (clip-on mounts, no roof penetrations)
- Large south-facing slope is optimal for solar panels
- Cleaner modern aesthetic
- Closed-cell spray foam dramatically deadens rain impact noise

**Cons:**
- Gives up rooftop access as living space
- Less "castle" aesthetic — more modern/industrial
- Metal roofing has a 50-year life vs. concrete slab's centuries
- Requires careful detailing at the low eave for water management

**Decision:** Neither option is a default. The choice depends on the site, the preferences at the time of each build, and the aesthetic goals for that particular home.

---

## 4.13 Story Height Math and Code Compliance

**Plain language:** Oregon building code limits how tall each floor can be for masonry construction. This design uses 13 feet 7 inches per story, which is the maximum allowed without needing engineered structural design. The math works out with room to spare.

**Technical detail:** Vertical stack per story:

| Layer | Height |
|---|---|
| Floor 1 clear ceiling height | 8 ft 0 in (96 in) |
| Service layer above | 4 ft 0 in (48 in) |
| Floor slab above (structural concrete) | 8 in |
| **Subtotal (story height as built)** | **12 ft 8 in (152 in)** |
| Code maximum for masonry (ORSC R301.3 item 3) | 13 ft 7 in (163 in) |
| **Remaining margin** | **11 in** |

**What this means:**
- Design fits within code with 11 inches of slack
- The slack can be absorbed into the service layer (making it 4 ft 11 in instead of 4 ft) if more room is needed for ducts or wire chases
- Or the slack can be distributed between a slightly taller ceiling and a slightly taller service layer

**Occupied space classification:**
- For code purposes, "story height" is generally measured floor to floor
- The service layer is designed as non-habitable utility space (see 4.11) so it does not count as a separate story
- Building is classified as 2 stories + basement, not 4 stories

**Block coursing:**
- Standard CMU = 8 inches per course with mortar joint
- 8 ft wall = 12 courses (clean math, no partial blocks)
- Service layer 4 ft = 6 courses plus sideways course
- Structural consistency on every floor

**Key code references:**
- ORSC R301.3 (story height — wind and seismic provisions, masonry limit 13 ft 7 in)
- ORSC R301.3 item 3 (masonry walls — bearing wall clear height limit 12 ft)

---

## 4.14 Stairs

**Plain language:** Stairs connect the floors. Where the stair goes in the 3x3 grid and what kind of stair is used both have big effects on the usable space. This section describes the options without picking one, because the specific stair for each home depends on the internal layout that buyer wants.

**Technical detail:** The specific stair location and type is left as a design decision to be made in the floor plan phase, because it depends heavily on buyer preferences and room usage.

### 4.14a Stair Types

**Straight stair:**
- A single flight from one floor to the next, straight line
- **Space required per floor:** 3-4 ft wide × 12-15 ft long = 36-60 sq ft
- **Pros:** Simplest, cheapest, fastest to climb
- **Cons:** Uses a long run of space in one direction

**L-shaped stair:**
- Two flights with a 90-degree turn and landing in the middle
- **Space required per floor:** 4-5 ft × 8-10 ft = 32-50 sq ft
- **Pros:** Fits in a corner, takes less continuous space
- **Cons:** Slightly more complex construction

**U-shaped (switchback) stair:**
- Two flights with a 180-degree turn and landing
- **Space required per floor:** 6-8 ft × 8-10 ft = 48-80 sq ft
- **Pros:** Fits tight in a single area, top and bottom land close together
- **Cons:** Longer travel path

**Zigzag / scissor stair:**
- Multiple short flights with landings between, visible multi-direction path
- **Space required per floor:** varies widely, similar to U-shape
- **Pros:** Dramatic aesthetic, breaks up long climbs
- **Cons:** More complex, harder to furnish the surrounding space

**Spiral / circular stair:**
- Treads radiating from a central column
- **Space required per floor:** 5-6 ft diameter = 20-28 sq ft
- **Pros:** Smallest footprint of any stair type
- **Cons:** Difficult for furniture moves, may not meet code for primary means of egress in some jurisdictions

### 4.14b Stair Code Requirements

**Plain language:** Code dictates the minimum and maximum sizes for stair steps, how tall the guard rails must be, and how much headroom is required. These rules exist because stairs are one of the most common places people fall and get hurt.

**Technical detail:**

- **Maximum riser height:** 7¾ inches (19.7 cm) — the vertical distance from one step to the next
- **Minimum tread depth:** 10 inches (25.4 cm) — the horizontal distance from the front to back of each step
- **Uniformity:** The largest and smallest riser in any flight must not vary by more than 3/8 inch; same for treads
- **Minimum width:** 36 inches (91 cm) clear width for primary stairs
- **Minimum headroom:** 6 feet 8 inches (80 inches, 2032 mm) above any part of the stair
- **Maximum slope:** Approximately 42 degrees (the 7¾ / 10 ratio above produces about 37.8 degrees)
- **Handrails required:** On at least one side for flights of 4 or more risers; height 34-38 inches above tread nosings
- **Guardrails:** Required at open sides of landings and stair runs higher than 30 inches above the adjacent floor; minimum 36 inches tall at landings
- **Landing:** Required at top and bottom of every flight; minimum depth equal to the stair width

**Key code references:**
- ORSC R311.7 (stairways — dimensional requirements)
- ORSC R311.7.8 (handrails — height and continuity)
- ORSC R312 (guards — guardrail requirements at elevated floors)

### 4.14c Stair Placement in the 3x3 Grid

Stair placement affects every room's usability. Common placements:

- **Central cell:** Stairs in the middle cell of the grid. All 8 other rooms open off the central circulation. Wastes the most desirable central room but creates equal access.
- **Corner cell:** Stairs in one corner of the grid. Frees the center for a primary room. Creates a longer travel path for rooms on the opposite side.
- **Edge cell (non-corner):** Stairs in the middle of one side of the grid. Compromise between central and corner.

**Decision deferred:** Specific stair type and location is a per-home design decision, not committed in this spec.

---

## 4.15 In-House Testing Program

**Plain language:** Before committing to a concrete mix, slab thickness, fiber content, rebar size, or any other critical structural choice, build small test versions and break them. The test results inform the final design with real data instead of guesses. This is how professional concrete engineering labs work, scaled down for one person with a garage and determination.

**Technical detail:** Testing program components:

### 4.15a Testing Rig

**Concept:** A reaction frame that applies calibrated loads to a sample until failure.

**Components:**
- Heavy steel reaction frame (welded from structural angle or channel)
- 20-ton bottle jack or hydraulic cylinder
- Digital load cell reading to a laptop or microcontroller
- Dial gauges or linear displacement transducers measuring deflection
- Sample support structure (two supports for flexural tests, full surface for compression)

**Cost:** $500-$1,500 to build; useful for thousands of tests

**Standards to match:**
- ASTM C39 (compressive strength of cylinders — 6x12 inch cylinders)
- ASTM C78 (flexural strength of concrete beams — third-point loading)
- ASTM C1609 (flexural performance of fiber-reinforced concrete)

### 4.15b Test Variables

**Concrete mix variables to test:**
- Water/cement ratio (0.35, 0.40, 0.45, 0.50)
- Cement replacement percentage (0%, 15%, 25%, 35% fly ash or slag)
- Silica fume percentage (0%, 5%, 10%)
- Aggregate gradation (fine/coarse ratios)
- Admixtures (plasticizers, air entrainment, corrosion inhibitors)

**Reinforcement variables:**
- Rebar size (#3, #4, #5, #6)
- Rebar spacing (6, 8, 12, 16 inches on center)
- Fiber type (none, steel, polypropylene, hybrid)
- Fiber dosage (varying amounts)

**Structural element variables:**
- Slab thickness (2, 4, 6, 8, 10, 12 inches)
- Rib depth and spacing
- Support condition (simply supported, fixed edges)

### 4.15c Data Analysis

**Approach:**
- Document every test with sample dimensions, mix design, cure time, load at failure
- Plot load vs. variable for each test series
- Build regression curves (linear or logarithmic) to predict strength for untested combinations
- Select design values with 5-10x safety factor over predicted service loads

**Testing timeline:**
- Concrete requires 28 days to reach nominal design strength
- Testing series of 50-100 samples across all variables requires 4-6 months of overlapping batches
- This is a serious but manageable commitment, ideally done before land purchase or during the land-hunting period

**Output:**
- A data-driven design specification for concrete mix, slab thickness, rebar, and fiber content
- A defensible engineering basis for the final structural design
- Validation that the home's structure genuinely exceeds code by the intended safety factors

**Key references:**
- ASTM C39 (compressive strength testing)
- ASTM C78 (flexural strength testing)
- ASTM C1609 (fiber-reinforced concrete testing)
- ACI 318 (structural concrete design requirements)
- ACI 544 (fiber-reinforced concrete design)

---

*End of Section 4 — Structural Design*
