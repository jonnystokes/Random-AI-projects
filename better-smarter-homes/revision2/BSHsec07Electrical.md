# Section 7 — Electrical

*Power in, power everywhere, and never drill through concrete to get it*

This section covers every wire in the building: where power enters, how it gets distributed, how every room gets its own breaker, how future solar and EV charging bolt on without rework, and the specific design choices that support the 1000-year envelope goal.

The guiding philosophy: **one exterior interconnect point**, generous panel capacity, per-room circuit granularity, wiring routed through the service layer for life-of-building accessibility, and every conduit sleeve and breaker slot needed for future expansion built in from day one.

---

## 7.1 Electrical Philosophy

**Plain language:** The electrical system is designed the same way as the plumbing: come in at one spot on the outside of the house, distribute everything through the walkable space between floors, give every room its own breaker so anything can be shut off without affecting the rest of the house, and leave room for future upgrades like solar panels and electric vehicle charging without having to rip anything out.

**Technical detail:** Core electrical design principles:

- **Single exterior service entry** via the interconnect box (see Section 3 and 7.2) — no service conductor penetrations through the concrete envelope
- **Main panel located in the basement** directly inside the wall from the interconnect box — shortest possible run of service-entrance conductors through the envelope
- **Subpanels on each floor** fed from the main panel through the service layer — minimizes home-run distances and voltage drop
- **One dedicated circuit per room minimum**, with rooms that have significant loads (kitchen, laundry, primary bathroom) getting multiple
- **All branch-circuit wiring runs in the service layer** (the 4–5 ft walkable space between floors) where possible — never buried in poured concrete, rarely inside finished walls
- **Oversized conduit sleeves** at every floor-to-floor penetration for future re-wires and additions
- **Future-proofed capacity**: service size and panel space sized for the home plus realistic additions (solar, EV, shop, hot tub, heat pump) without a service upgrade
- **Grounding integrated with the structural rebar cage** — the foundation rebar doubles as the primary grounding electrode (see 7.5)

**Why this differs from standard residential:**
- Standard houses bury Romex in stud bays; this design puts most wiring in the service layer, behind grating, accessible for life
- Standard houses have one panel; this design has a main panel plus one subpanel per floor for shorter, simpler circuits
- Standard houses size the service for current loads; this design sizes for lifetime loads including solar, EV, and shop
- Standard houses treat the grounding electrode as an afterthought; this design uses the structural rebar cage (a Concrete-Encased Electrode, often called a "Ufer ground") as the primary electrode — and it was going to be there anyway

---

## 7.2 Service Entry and the Interconnect Box

**Plain language:** The electric company's wires don't come into the house through the concrete. They stop at a weatherproof box mounted on the outside of the house on the utility side, along with the water line, the gas line if any, and the communication lines. From that box, everything goes underground into a single sleeve that passes through the basement wall, and from the inside of the wall fans out to the appropriate equipment.

**Technical detail:** Electrical service entry sequence:

1. **Utility drop or lateral** from the power company (overhead service drop or underground service lateral) terminates at the meter base on the exterior wall of the exterior interconnect box housing
2. **Meter base** (utility-owned meter, structure-owned socket) is mounted on the exterior wall of the interconnect box, readable and sealable by the utility without entering the house
3. **Service-entrance conductors** run from the meter base through a short sleeve into the interconnect box
4. **Main service disconnect** (outdoor-rated, required by 2020 NEC onward within sight of the meter or immediately inside) sits inside the interconnect box or on its exterior — this lets first responders and the utility kill all power at the exterior without entering the house
5. **From the disconnect, service conductors run underground** in a conduit sleeve through the basement wall into the basement interior
6. **Inside the basement**, conductors terminate at the main distribution panel (MDP) mounted on the interior face of the same wall the sleeve passed through

**Interconnect box specifications:**
- **NEMA 3R or 4 rated enclosure** (outdoor, weatherproof, sized for meter base, disconnect, and space for future solar disconnect and EV load center)
- **Mounted on a concrete pad or integral extension of the foundation** — not attached directly to the block veneer, which is decorative, not structural for hanging heavy gear
- **Lockable** with utility access for the meter compartment
- **Heated interior** (small low-wattage heater on a thermostat) for the pressure reducing valve and water meter — the electrical side doesn't need heat
- **Sized with at least 30% empty DIN rail and knockout space** for future additions

**Why the exterior disconnect matters (2020+ NEC):**
- NEC 230.85 requires an emergency disconnect in a readily accessible outdoor location for one- and two-family dwellings (new rule as of 2020 NEC, adopted by Oregon)
- First responders can cut power without entering a burning or flooded house
- Utility can disconnect for non-payment, maintenance, or emergency without entering the house
- This rule aligns perfectly with the interconnect box concept — it would be required anyway

**Sleeve specifications through the basement wall:**
- **Conduit sleeve** (PVC Schedule 80 or rigid metal) cast into the concrete wall during the pour
- **Oversized** compared to the actual service conductor diameter — a 4 inch sleeve for a 2-2-2-4 aluminum service-entrance cable, for example, with the extra space used for low-voltage, communication, or future additions
- **Waterproofed** with a link-seal or equivalent mechanical seal after pulling the conductors — not caulk, not spray foam
- **Sloped slightly downward toward the exterior** so any water that gets in drains out, not in

**Key code references:**
- NEC 230 (services)
- NEC 230.85 (emergency disconnect, dwelling units)
- NEC 312.2 (damp and wet locations, enclosures)
- OESC (Oregon Electrical Specialty Code, currently based on 2023 NEC)

---

## 7.3 Service Size and Capacity Planning

**Plain language:** The electrical service — meaning the capacity of the main wires coming into the house from the utility — is sized bigger than a normal house. A standard new home in Oregon gets 200 amps. This design calls for 320 or 400 amps, because the house will eventually have solar panels feeding back, an electric vehicle charger or two, possibly a shop, a hot tub, and electric heating equipment all running at once.

**Technical detail:** Service size decision:

**Standard residential service sizes:**
- 100 amp — older homes, small homes, minimum for a modern house
- 200 amp — standard for new construction, typical 2,500–4,000 sqft home
- 320 amp — high-end residential, "meter-main" style with two 200 amp sections
- 400 amp — luxury homes, multiple outbuildings, heavy loads, commercial-residential

**For this design: 320 to 400 amp service recommended**

**Load inventory that drives the sizing decision:**

| Load Category | Typical Continuous Draw | Peak |
|---|---|---|
| General lighting and outlets | 10–30 A | 50 A |
| Kitchen (two SA circuits + appliances) | 15 A | 60 A |
| Laundry (washer + dryer, electric) | 5 A | 30 A |
| HVAC (air handler, heat pump) | 10–25 A | 60 A |
| Electric water heater (if installed) | 15 A | 25 A |
| Radiant floor heating circulators | 2–5 A | 10 A |
| Ground-loop heat exchanger pumps | 3–8 A | 15 A |
| Hot tub (for future) | 20–50 A | 50 A |
| EV charger Level 2 (each) | 32–48 A | 48 A |
| Shop circuits (future) | 10–30 A | 50 A |
| Solar backfeed (future, reverse) | — | 40–80 A |

**Using the optional NEC method (NEC 220.83) for a modern all-electric home with all the above, the computed load lands around 240–320 amps, which is why 400 amp service is the right call for this philosophy.**

**Service equipment options:**

**Option A — Single 400A main panel:**
- One panel with a 400A main breaker and 40–60 breaker spaces
- Simple, single point of disconnect
- Large panel physical footprint
- One single point of failure

**Option B — 320A meter-main with two 200A distribution panels:**
- Utility meter feeds a main disconnect box with two 200A breakers
- Each 200A breaker feeds a separate panel (for example: one panel for the house, one panel for the shop/garage/future additions, or one panel per floor)
- More flexibility for future expansion and solar integration
- Slightly higher cost but simpler re-wiring later

**Recommended: Option B — 320A service with meter-main and two 200A subpanels**, one labeled "House" and one labeled "Expansion" (solar, EV, shop, future additions).

**Why oversize now rather than upgrade later:**
- A service upgrade after the house is built requires: utility coordination, possible new service lateral from the transformer, permit, inspection, new meter base, and possibly trenching through finished landscaping
- The cost delta between a 200A and 400A service at build time is a few thousand dollars (bigger wire, bigger panel, bigger main breaker)
- The cost of upgrading from 200A to 400A after the fact is often $10,000 to $20,000+
- For a 1000-year home, the original service might see multiple utility-side upgrades (higher-voltage neighborhood feeds, for example) but the house-side capacity should be set-and-forget

**Key code references:**
- NEC 220 (branch-circuit, feeder, and service load calculations)
- NEC 220.83 (optional method for existing dwellings — useful for computed load projections)
- NEC 230.42 (service-entrance conductor ratings)
- NEC 310.15 (conductor ampacity tables)

---

## 7.4 Main Panel, Subpanels, and Distribution

**Plain language:** Instead of one giant breaker box with every circuit in it, the design uses a main panel in the basement that feeds smaller panels on each floor. Every room's breaker lives in the panel closest to that room. This keeps wires shorter, makes troubleshooting easier, and lets any floor be worked on without killing power to the rest of the house.

**Technical detail:** Panel hierarchy:

**Main distribution panel (MDP):**
- **Location:** Basement, mounted on the interior face of the exterior wall, directly inside from the interconnect box
- **Rating:** 320–400A main breaker (matched to service size)
- **Contents:** Main breaker, feeder breakers to each subpanel, solar backfeed breaker space, basement branch circuits
- **Empty space:** At least 30% of breaker slots unused at commissioning for future circuits
- **Accessibility:** 36 inch working clearance in front (NEC 110.26), not behind a door, not in a closet, not over a washer or sink

**Floor 1 subpanel:**
- **Location:** Interior wall, ideally near the wet zone (reduces conduit runs to kitchen and bathroom) or near a mechanical closet accessing the service layer
- **Rating:** 100–200A feeder breaker, 30–40 breaker slots
- **Contents:** All Floor 1 branch circuits (rooms, kitchen, bathroom, lighting, outlets)
- **Empty space:** At least 20% of breaker slots unused at commissioning

**Floor 2 subpanel:**
- **Location:** Interior wall on Floor 2, accessible from a hallway or mechanical closet
- **Rating:** 100–200A feeder breaker, 30–40 breaker slots
- **Contents:** All Floor 2 branch circuits
- **Empty space:** At least 20% of breaker slots unused at commissioning

**Optional: outdoor / expansion subpanel:**
- **Location:** Inside the interconnect box or adjacent weatherproof enclosure
- **Rating:** 100–200A feeder breaker
- **Contents:** Outdoor utility service bay circuits, future EV charger, future hot tub, future shop, solar disconnect
- **Empty space:** Substantial — this panel is where the "what I don't know I'll add" budget lives

**Feeder sizing between main and subpanels:**

| Feeder Amp Rating | Copper Conductor | Aluminum Conductor | Conduit |
|---|---|---|---|
| 100A | 3 AWG THHN | 1 AWG THHN | 1 inch |
| 125A | 2 AWG THHN | 1/0 AWG THHN | 1-1/4 inch |
| 150A | 1 AWG THHN | 2/0 AWG THHN | 1-1/4 inch |
| 200A | 2/0 AWG THHN | 4/0 AWG THHN | 1-1/2 inch |

**Feeder routing:** Conduit from the main panel up through the service layer to each floor's subpanel location. Conduit sizes the full run — no transitions, no pull boxes in inaccessible places.

**Why subpanels instead of one giant main:**
- **Shorter home-runs** — every branch circuit is shorter from its subpanel than it would be from a basement-only main
- **Lower voltage drop** on long runs to the far side of a large home
- **Floor-level isolation** — shut off one floor's subpanel to work on that floor
- **Simpler troubleshooting** — the breaker for a given room is in the panel on that floor, not in a different part of the house
- **Physically smaller main panel** (fewer branch breakers) leaves room for feeder breakers plus solar backfeed plus expansion capacity

**Panel brand and quality:**
- **Square D QO, Eaton BR/CH, Siemens, or Leviton smart panels** — all good, all widely available, all with wide breaker and accessory support
- **Avoid:** off-brand panels, panels with discontinued breakers, aluminum-bussed panels older than 20 years in renovation contexts (not applicable here — new panels only)
- **Smart panel consideration:** Panels like Span Home or Leviton Smart Load Center add per-breaker monitoring and remote control. Useful for energy management and solar integration, but add cost and a cloud dependency concern. **Decision deferred to build time** — traditional panels are fully adequate, smart panels are a "nice to have" if the cost and cloud-independence concerns line up

**Key code references:**
- NEC 408 (switchboards, switchgear, and panelboards)
- NEC 110.26 (working space around electrical equipment)
- NEC 215 (feeders)
- NEC 240 (overcurrent protection)

---

## 7.5 Grounding and Bonding

**Plain language:** Every electrical system needs a connection to the earth so that if lightning strikes or a wire shorts to something metal, the electricity has a safe path to ground instead of going through a person. Normally this is a couple of 8-foot copper rods driven into the dirt outside. In this design, the massive rebar cage inside the concrete foundation is used instead — it's a much better ground, it was going to be there anyway, and it's protected inside the concrete forever.

**Technical detail:** Grounding electrode system:

**Primary grounding electrode — Concrete-Encased Electrode (CEE), commonly called a "Ufer ground":**
- **What it is:** At least 20 feet of bare #4 or larger rebar (or 20 feet of #2 AWG bare copper conductor) embedded in at least 2 inches of concrete that is in direct contact with earth — NEC 250.52(A)(3)
- **In this design:** The mat foundation rebar mat IS this electrode — there's tens of thousands of feet of rebar down there, continuous and in contact with the subgrade
- **Connection:** At least one #4 rebar in the foundation is bent up and terminated above the basement slab before the pour, with a stub accessible from inside the basement. A grounding electrode conductor (GEC) clamps to this stub and runs to the main panel's ground bus
- **Redundancy:** A second #4 rebar stub is cast in at the opposite corner of the building, with the option of bonding it to the panel as well, or leaving it as a future-use stub

**Supplemental grounding electrodes (if desired, not required with a CEE):**
- **Ground rods:** Two 8 ft copper-clad steel rods driven at least 6 feet apart, connected to the main panel ground bus. Optional with a CEE but cheap insurance for lightning performance
- **Metal underground water pipe:** If the service water line is metallic for at least 10 feet underground, it's bonded to the ground system per NEC 250.52(A)(1). If it's plastic (HDPE or PEX), not applicable — this design uses plastic, so it's not.

**Grounding electrode conductor (GEC) sizing:**

| Service Size | GEC to CEE (copper) |
|---|---|
| 200A | #4 AWG |
| 320A | #2 AWG |
| 400A | #1/0 AWG |

**Bonding:**
- **Main panel:** Grounded (neutral) and ground busses **bonded together at the main panel only**, via the main bonding jumper (NEC 250.28). In all subpanels, neutral and ground are **separate** — this is the most commonly-violated rule in DIY installations
- **Metallic water piping:** Bonded to the panel ground bus at the first accessible point inside the structure (NEC 250.104). In this design, the copper Type L main trunk serves as this bond — one #4 copper bonding jumper from the ground bus to a bonding clamp on the copper trunk
- **Gas piping (if any):** Bonded per NEC 250.104(B) — one #6 copper minimum to the point where the gas line enters the house
- **HVAC equipment:** Bonded through the equipment grounding conductor in the circuit feeding it — no separate bond needed
- **Structural steel:** If any steel joists or lintels are used, bonded to the ground system per NEC 250.104(C)

**Why the CEE is better than ground rods:**
- **Dramatically lower resistance to earth** — a typical CEE measures 2–10 ohms, a ground rod measures 25–100 ohms
- **Continuous contact with moist subgrade soil** — doesn't dry out in summer like rods in dry dirt can
- **Protected inside concrete** — doesn't corrode, doesn't get damaged by digging, doesn't get stolen
- **Free** — the rebar is already there for structural reasons

**Key code references:**
- NEC 250 (grounding and bonding — entire article)
- NEC 250.50 (grounding electrode system)
- NEC 250.52 (grounding electrodes)
- NEC 250.53 (grounding electrode installation)
- NEC 250.66 (size of grounding electrode conductor)
- NEC 250.104 (bonding of piping systems and exposed structural metal)

---

## 7.6 Circuit Design Philosophy

**Plain language:** Every room gets its own breaker. If something goes wrong in the living room, only the living room loses power, not the bedrooms or the kitchen. Kitchens get several breakers because they have so many appliances. This costs a little more in wire and breakers up front but makes the house dramatically more livable — no flipping a breaker and losing half the house.

**Technical detail:** Circuit granularity:

**One dedicated 20A general-purpose branch circuit per room, minimum**, for rooms under about 200 square feet with typical residential load.

**Larger rooms (living room, great room, primary bedroom) get two circuits** — one for outlets on two walls, one for outlets on the other two walls — so that one tripped breaker doesn't kill the whole room.

**Lighting circuits are separate from outlet circuits in every habitable room**, so that a tripped outlet breaker doesn't leave you in the dark. This is above code minimum (code allows lighting and outlets on the same circuit in most rooms) but it's a livability choice that matters.

**Circuit count per typical room:**

| Room Type | Outlet Circuits | Lighting Circuits | Total |
|---|---|---|---|
| Small bedroom (under 150 sqft) | 1 | 1 (shared with adjacent room OK) | 1–2 |
| Primary bedroom | 2 | 1 | 3 |
| Living room / great room | 2 | 1 | 3 |
| Dining room | 1 | 1 | 2 |
| Hallway | 0 | 1 | 1 |
| Office / study | 1 | 1 | 2 |

**Breaker sizing:**
- **20A breakers for general-purpose outlet circuits** — using 12 AWG copper wire
- **15A breakers for lighting-only circuits** — using 14 AWG copper wire (optional; many builders use 20A everywhere for simplicity)
- **Standard: use 20A / 12 AWG everywhere for habitable rooms** — slightly higher wire cost, zero ambiguity, more capacity per circuit

**Wire type:**
- **THHN/THWN-2 individual conductors in EMT or PVC conduit** for runs in the service layer and exposed in the basement — durable, replaceable in the future by pulling new wire through existing conduit
- **NM-B (Romex) for runs inside finished walls where conduit isn't practical** — only used where the run is short and the wall is unlikely to be opened again
- **MC cable (metal-clad) as an alternative in the service layer** — self-protecting, doesn't require conduit, slightly more expensive

**Design preference: conduit everywhere possible**, so that any circuit can be re-pulled, upgraded, or repurposed over the life of the building. This is the electrical equivalent of the accessible service layer philosophy.

**Smoke and CO detection:**
- **Hardwired, interconnected smoke alarms** in every bedroom, outside each sleeping area, and on every floor per NEC 760 / ORSC R314
- **Combination smoke/CO detectors** in hallways outside bedrooms and within 10 feet of any fuel-burning appliance per ORSC R315
- **Battery backup** in every unit (10-year sealed batteries recommended)
- **Powered from a dedicated circuit** that is not AFCI or GFCI protected (nuisance tripping would defeat the purpose)

**Key code references:**
- NEC 210 (branch circuits)
- NEC 210.11 (branch circuits required)
- NEC 210.52 (receptacle outlets in dwelling units)
- NEC 310.15 (conductor ampacity)
- ORSC R314 (smoke alarms)
- ORSC R315 (carbon monoxide alarms)

---

## 7.7 Kitchen Circuits

**Plain language:** Kitchens eat electricity. Between the fridge, oven, cooktop, dishwasher, microwave, disposal, toaster, coffee maker, and whatever someone is blending at any given moment, one circuit can't handle it. Code requires at least two 20-amp circuits for the countertop outlets alone, plus dedicated circuits for most big appliances. This design uses more than the minimum, so no kitchen activity trips a breaker.

**Technical detail:** Kitchen circuit plan:

**Required circuits (NEC 210.11(C)):**
- **Minimum two 20A small-appliance (SA) branch circuits** serving the countertop receptacles, refrigerator, and nothing else — NEC 210.11(C)(1)
- **Dedicated 20A circuit for the dishwasher** — NEC 210.11(C)(2) (when installed, can share with disposal in some jurisdictions but better to separate)
- **Dedicated 20A circuit for the garbage disposal** (if installed)
- **Dedicated 20A circuit for the microwave** (if built-in or over-range)

**Recommended circuits for this design (above code minimum):**
- **Three 20A countertop SA circuits** instead of two — split by countertop zone (north counter, south counter, island)
- **Dedicated 20A circuit for the refrigerator** — isolated from the SA circuits so a countertop short doesn't kill the fridge and spoil food
- **Dedicated 20A circuit for the dishwasher**
- **Dedicated 20A circuit for the disposal** (if installed)
- **Dedicated 20A circuit for the microwave**
- **Dedicated 40–50A 240V circuit for the electric range or cooktop** (if electric)
- **Dedicated 30A 240V circuit for the wall oven** (if separate from cooktop)
- **Dedicated 20A circuit for the kitchen lighting**
- **Dedicated 20A circuit for under-cabinet lighting** (optional, often combined with kitchen lighting)
- **Dedicated 20A circuit for a coffee bar / beverage center** (optional, nice-to-have)

**Total kitchen circuit count: 9 to 12 circuits** depending on appliance choices and optional features. This is dramatically more than a typical kitchen (which has 4–6 circuits) and reflects the "nothing trips" design goal.

**Countertop receptacle spacing (NEC 210.52(C)):**
- **Receptacles required along every countertop 12 inches or wider**
- **Maximum 24 inch horizontal distance** between any point along the counter and the nearest receptacle
- **Maximum 48 inch distance between receptacles**
- **Island counters:** at least one receptacle per island per the 2020+ NEC
- **Peninsula counters:** same treatment as islands

**GFCI protection:** All countertop receptacles in the kitchen must be GFCI-protected per NEC 210.8(A)(6). All dishwasher circuits must be GFCI-protected per NEC 210.8(D) (added in 2020 NEC). See 7.9 for GFCI strategy.

**AFCI protection:** All kitchen branch circuits serving outlets in the kitchen must be AFCI-protected per NEC 210.12(A) (kitchen added to AFCI list in the 2014 NEC). See 7.9 for AFCI strategy.

**Key code references:**
- NEC 210.11(C) (small-appliance branch circuits)
- NEC 210.52(C) (kitchen countertop receptacles)
- NEC 210.8(A) (GFCI protection — dwelling units)
- NEC 210.12 (AFCI protection)
- NEC 422 (appliances — dedicated circuits and ampacity)

---

## 7.8 Bathroom, Laundry, and Wet-Area Circuits

**Plain language:** Bathrooms and laundry rooms also get their own dedicated circuits. Every bathroom has at least one circuit for outlets that doesn't serve anything else. The laundry room has circuits for the washer, the dryer, and any outlets, all separate.

**Technical detail:** Wet-area circuit plan:

**Bathrooms:**
- **Minimum one dedicated 20A circuit per bathroom serving the receptacles** — NEC 210.11(C)(3)
- **Alternative allowed by code:** one 20A circuit serving multiple bathrooms' receptacles and nothing else — this design chooses one circuit per bathroom for isolation
- **All bathroom receptacles GFCI-protected** — NEC 210.8(A)(1)
- **All bathroom receptacles AFCI-protected** as of 2014 NEC — combined AFCI+GFCI breakers are widely available
- **Lighting on a separate circuit from receptacles** (livability choice, above code)
- **Dedicated circuit for the bathroom exhaust fan** if it draws over a few amps or is integral to an HRV — usually shares the lighting circuit but can be separate
- **Dedicated 20A circuit for a steam shower or jetted tub if installed** (often 240V for steam generators, check equipment specs)

**Laundry room:**
- **Minimum one dedicated 20A laundry branch circuit** serving the washer and nothing else — NEC 210.11(C)(2)
- **Dedicated 30A 240V circuit for an electric dryer** (if electric) — 10-3 wire with ground, 14-30R receptacle for new installations (4-wire grounded)
- **Dedicated 20A circuit for a gas dryer** — shared with the washer is allowed but this design separates them
- **Dedicated 20A circuit for the laundry-area lighting** (often shared with adjacent hallway)
- **All laundry-area receptacles GFCI-protected** — NEC 210.8(A)(10), added in 2017 NEC
- **GFCI protection for the washer receptacle** — yes, this applies even to the washing machine itself in 2020+ NEC

**Outdoor and garage circuits (see 7.14 for the outdoor utility service bay):**
- **All outdoor receptacles GFCI-protected** — NEC 210.8(A)(3)
- **Dedicated circuit(s) for the outdoor utility service bay** — see 7.14
- **Dedicated circuit(s) for any future detached structures** — conduit sleeved in from the main panel during original build

**Key code references:**
- NEC 210.11(C)(2) (laundry branch circuit)
- NEC 210.11(C)(3) (bathroom branch circuit)
- NEC 210.8(A) (GFCI protection in dwelling units)
- NEC 210.52(D) (bathroom receptacle requirements)
- NEC 210.52(F) (laundry receptacle requirements)

---

## 7.9 GFCI and AFCI Protection Strategy

**Plain language:** Two kinds of smart breakers protect the house from two different hazards. GFCIs (ground fault circuit interrupters) protect people from being shocked when water is involved — kitchens, bathrooms, outdoors, basements. AFCIs (arc fault circuit interrupters) protect from fires caused by damaged wiring. Modern code requires both in most of the house. This design uses combination breakers that do both jobs at once.

**Technical detail:** Protection strategy:

**GFCI protection (required by NEC 210.8):**
- **All 125V–250V receptacles in the following locations:**
  - Bathrooms (all receptacles)
  - Garages and detached accessory buildings
  - Outdoors (including decks and porches)
  - Crawlspaces (if accessible)
  - Unfinished basements
  - Kitchens (all countertop receptacles, plus dishwasher as of 2020 NEC)
  - Sinks — within 6 feet of the sink edge, any room
  - Laundry areas (all receptacles as of 2017 NEC)
  - Boathouses, bathtubs, shower stalls

**AFCI protection (required by NEC 210.12):**
- **All 120V 15A and 20A branch circuits supplying outlets in the following locations:**
  - Kitchens
  - Family rooms
  - Dining rooms
  - Living rooms
  - Parlors / dens / libraries
  - Bedrooms
  - Sunrooms
  - Recreation rooms
  - Closets
  - Hallways
  - Laundry areas
- **Effectively: everywhere except bathrooms, garages, outdoors, and unfinished spaces** — though many jurisdictions are moving toward AFCI everywhere

**Implementation method: combination AFCI/GFCI breakers in every habitable-room circuit**
- **Benefits:** both protections, both at the panel, no need for GFCI receptacles downstream in the room (though they can be added for convenience)
- **Downsides:** higher cost per breaker ($40–60 vs $10 for a standard breaker), occasional nuisance trips on older appliances with noisy motors or switching power supplies
- **Recommended brand approach:** match the panel manufacturer — Square D CAFCI/CGFCI if using a Square D QO panel, Eaton BR-CAF/GF for Eaton BR panels, etc.

**Non-AFCI, non-GFCI circuits (intentionally):**
- **Smoke and CO detector circuit** — never AFCI or GFCI (nuisance trips defeat the purpose)
- **Refrigerator circuit** — GFCI required in 2020 NEC but nuisance trip concerns exist; use a dedicated AFCI circuit and rely on the combination if jurisdiction requires, or use a GFCI receptacle at the fridge location
- **Critical medical equipment** (if applicable) — follow manufacturer and medical guidance

**Testing and maintenance:**
- **Monthly test of every GFCI and AFCI** by pressing the test button (owner's responsibility)
- **Annual logging** of any tripped breakers with notes on the cause — builds a maintenance record for the home

**Key code references:**
- NEC 210.8 (GFCI protection for personnel)
- NEC 210.12 (AFCI protection)
- NEC 406.4 (receptacle ratings and types)
- OESC adoption of 2023 NEC

---

## 7.10 Receptacle Count and Placement

**Plain language:** There are a lot of outlets — more than code requires. Every wall in every habitable room gets outlets spaced so that a standard appliance cord reaches without an extension cord. Exterior walls, interior walls, and every room are all covered. Extra outlets cost pennies; missing outlets cost headaches forever.

**Technical detail:** Receptacle placement:

**Habitable rooms — NEC 210.52(A) — "general provisions":**
- **Receptacles required along every wall 2 feet or longer**
- **Maximum 12 feet between receptacles along a wall** (so a 6-foot extension cord reaches any point)
- **Maximum 6 feet from any doorway or wall end** to the nearest receptacle
- **Floor receptacles count only if within 18 inches of the wall**

**This design: slightly above code**
- **Maximum 10 feet between receptacles** instead of 12 feet — tighter spacing for modern electronic device density
- **One receptacle per wall minimum**, regardless of wall length (code allows skipping walls under 2 feet, this design includes them)
- **Dedicated receptacles at obvious desk and entertainment center locations** — predicts where furniture goes and puts outlets there

**Receptacle type: tamper-resistant, weather-resistant where applicable**
- **Tamper-resistant (TR) receptacles required in dwelling units** for all 125V 15A and 20A non-locking receptacles — NEC 406.12
- **Weather-resistant (WR) receptacles required outdoors and in damp locations** — NEC 406.9
- **Combination TR/WR receptacles** for any outdoor or exterior-wall locations

**Special receptacle types:**
- **USB combination receptacles** in bedrooms, kitchen counters, office — nice-to-have, plan for 2–4 per room
- **20A T-slot receptacles** where a 20A appliance is expected (kitchen, laundry, outdoor utility bay)
- **240V receptacles** for the electric range, dryer, EV charger, any future 240V appliances

**Receptacle heights:**
- **Standard wall outlets:** 12–16 inches above finished floor (AFF) — typical
- **Kitchen countertop outlets:** 4 inches above countertop, 42–46 inches AFF
- **Bathroom vanity outlets:** above vanity counter, 42–46 inches AFF, on GFCI
- **Garage workbench outlets:** 48 inches AFF
- **Outdoor utility bay outlets:** 24 inches above grade, in weatherproof covers

**Receptacle count summary (example 3,000 sqft home):**
- **Floor 1:** 40–60 receptacles (living area, kitchen, dining, office, bathroom, hallway, entry)
- **Floor 2:** 30–50 receptacles (bedrooms, bathrooms, hallway, laundry if on this floor)
- **Basement:** 20–40 receptacles (shop area, mechanical room, general use)
- **Outdoor utility bay:** 4–8 receptacles (see 7.14)
- **Outdoor perimeter:** 4–8 receptacles (one per side of the house at minimum)
- **Total:** 100–170 receptacles

**Key code references:**
- NEC 210.52 (dwelling unit receptacle outlets)
- NEC 406.9 (weather-resistant receptacles)
- NEC 406.12 (tamper-resistant receptacles)
- NEC 210.52(C) (kitchen countertop receptacles — detailed in 7.7)

---

## 7.11 Lighting Design

**Plain language:** Lighting is on dedicated circuits, separate from outlets. The house uses LED fixtures throughout — they last 15 to 25 years, use a tenth the energy of incandescents, and come in any color temperature. Dimmers go everywhere for atmosphere control, and switches are laid out so you never have to walk across a dark room to turn on a light.

**Technical detail:** Lighting design principles:

**Light source: LED throughout**
- **Integrated LED fixtures** in most locations — no bulb to change for 15–25 years, lower energy use, better light quality
- **Standard E26/E27 screw-base LED bulbs in a few fixtures** where custom bulbs add character (pendant lights, certain decorative fixtures)
- **Avoid:** fluorescent, halogen, incandescent (all legacy, all short-lived, all being phased out)

**Color temperature:**
- **2700K–3000K (warm white)** for living spaces, bedrooms, dining — warm, relaxing, flattering
- **3500K–4000K (neutral white)** for kitchen task areas, bathrooms, laundry — cleaner, better for detailed work
- **5000K (daylight)** for shop, garage, service layer, utility — maximum visibility
- **Tunable fixtures** (adjustable color temperature) in primary living spaces — a premium feature

**Control: dimmers and switches**
- **Dimmer switches on every primary lighting circuit** — livability and mood control
- **Three-way switches at both entrances to any room with two entry points** — never walk into a dark room
- **Four-way switches for rooms with three entries** (staircases, large great rooms)
- **Standard rocker-style switches** throughout for consistency
- **Occupancy sensors** in closets, pantries, and rarely-used spaces — auto-off prevents wasted energy
- **Timer switches** for bathroom exhaust fans

**Switch heights:**
- **48 inches AFF** to the center of the switch — standard
- **44 inches AFF** for accessibility (ADA-informed, even if not ADA-required in a private residence)
- **Near the door on the strike-hinge side** (the side opposite the hinges) so the switch is reachable without stepping behind the door

**Lighting fixture types by room:**

| Room | Primary | Task | Accent |
|---|---|---|---|
| Kitchen | Recessed LEDs + island pendants | Under-cabinet LED strips | Toekick LEDs |
| Living room | Recessed LEDs + ceiling fan/light | Reading lamps (plug-in) | Wall sconces optional |
| Bedrooms | Ceiling fan/light + recessed | Bedside lamps (plug-in) | Closet LED strips |
| Bathrooms | Vanity bar or recessed | Vanity-side sconces | Shower recessed |
| Hallways | Recessed LEDs | — | Art lighting optional |
| Basement | LED shop lights or recessed | Workbench-mounted LED | — |
| Outdoor | Wall-mounted downlights, GFCI | Motion-sensor floods | Landscape low-voltage |

**Dedicated circuit notes:**
- **Outdoor lighting on its own circuit**, often with a photocell or timer
- **Landscape low-voltage lighting** runs through a 12V transformer on its own circuit — separate from 120V outdoor lighting
- **Christmas / holiday outlet circuits** at the eaves or roofline, switched from inside — "forever holiday lights" feature, one circuit each corner of the house

**Smart lighting considerations:**
- **Local control first, smart control layered on top** — see Section 10 (Smart Home Philosophy) for detailed treatment
- **Smart switches (Lutron Caseta, Shelly, Zooz) installed where remote control adds value** — not everywhere
- **Dumb switches retained in places where remote control isn't needed** — simpler, cheaper, longer-lived

**Key code references:**
- NEC 410 (luminaires, lampholders, and lamps)
- NEC 210.70 (lighting outlets required — every habitable room, bathrooms, hallways, stairways)
- NEC 404 (switches)
- ORSC N1104 (lighting efficiency — ≥90% high-efficacy lamps)

---

## 7.12 Wiring Routes — The Service Layer Advantage

**Plain language:** Most houses have wires buried inside the walls. If you ever want to add a new outlet, move a light, or upgrade to thicker wire for a big appliance, you have to cut the drywall open. This house runs most of its wiring through the 4-to-5-foot walkable space between the floors, inside metal conduit. Any wire can be pulled out and replaced by pulling it through the conduit — no drywall damage, no surprise.

**Technical detail:** Wiring route hierarchy:

**Priority 1 — Service layer runs (preferred for almost everything):**
- **Horizontal trunk routes along the service layer ceiling** (underside of the floor above) in EMT or PVC conduit
- **Vertical drops** through the floor slab to Floor 1 outlets via sleeved penetrations or interior partition walls
- **Vertical rises** through the floor slab to Floor 2 outlets via sleeved penetrations or interior partition walls
- **All trunk conduit supported from the masonry walls or ceiling slab using approved straps and standoffs**

**Priority 2 — Interior partition wall runs:**
- **For outlets on interior partition walls** (which are not concrete in this design — they're stud framing or CMU partitions)
- **NM-B (Romex) or MC cable inside the stud cavities** from the service layer up/down to the receptacle
- **Short, straight runs only** — any run over 6 feet considered for conduit routing instead

**Priority 3 — Concrete wall runs:**
- **For outlets on the exterior masonry walls** (which are concrete block with insulated cavity)
- **Conduit cast into the CMU core during block-laying** for vertical runs
- **Surface-mounted conduit in the service layer** for horizontal trunk, dropping down through the CMU core to the receptacle
- **Interior finish (drywall or furring strips) covers the conduit where it exits the CMU at the receptacle location**

**Priority 4 — Concealed slab runs (avoided):**
- **Wiring cast into the floor slab** — permanent, non-replaceable, philosophically at odds with the 1000-year design
- **Used only for:** radiant floor heating loops (which are PEX, not electrical), lightning protection down-conductors (if installed), and truly unavoidable runs
- **Never used for:** branch circuits, outlet feeds, anything that might need replacement

**Conduit sizing:**

| Use | Conduit Size | Typical Contents |
|---|---|---|
| Individual branch circuit | 1/2 inch EMT | 2–3 conductors + ground |
| Multi-circuit trunk | 3/4 to 1 inch EMT | 6–9 conductors |
| Feeder to subpanel | 1-1/4 to 1-1/2 inch EMT | 3–4 large conductors |
| Service entrance | 2 to 3 inch PVC or RMC | Service-entrance cable |
| Low-voltage (Ethernet, coax, security) | 3/4 to 1 inch | 4–8 cables |

**Pull boxes and junction boxes:**
- **Every 360 degrees of cumulative bends**, a pull box is required (NEC 344.26 for rigid metal conduit, NEC 358.26 for EMT)
- **In practice:** every 30–40 feet of run, or at every change of direction beyond two 90° bends
- **Pull boxes located in the service layer at accessible points**

**Separation of systems:**
- **High-voltage (120/240V) and low-voltage (Ethernet, security, HVAC control) in separate conduits** — per NEC 725.136 (Class 2 circuits must be physically separated from power conductors, minimum 2 inches for parallel runs outside conduit)
- **In practice:** run parallel conduits 6+ inches apart, or inside separate raceways, throughout the service layer

**Labeling:**
- **Every conduit labeled at every pull box** with source panel, destination, and circuit numbers
- **Every cable labeled at every termination** with circuit number and function
- **Panel directory kept current and a laminated copy kept at each panel**
- **Master wiring schedule maintained as a living document** in the home's project binder — updated with every addition or change

**Why this matters:**
- **A wire in conduit can be pulled out and replaced in under an hour** with no destruction
- **A wire buried in drywall requires cutting, patching, painting, and hope**
- **Over a 1000-year life, every electrical component will be replaced many times** — the envelope outlasts them all
- **Conduit is the tendons; wire is the muscle** — tendons are structural, muscle is replaceable

**Key code references:**
- NEC 342 (intermediate metal conduit)
- NEC 344 (rigid metal conduit)
- NEC 352 (rigid PVC conduit)
- NEC 358 (electrical metallic tubing — EMT)
- NEC 314 (outlet, device, pull, and junction boxes)
- NEC 725 (Class 1, 2, 3 remote-control, signaling, and power-limited circuits)

---

## 7.13 Outdoor Utility Service Bay — Electrical

**Plain language:** The outdoor utility bay is a small covered area on the exterior of the house with water hookups, compressed air, and GFCI outlets for using pressure washers, yard tools, and anything else outside. The electrical part of the bay includes multiple weatherproof outlets, good lighting, and a dedicated subpanel section so the outlet circuits are isolated from the rest of the house.

**Technical detail:** Outdoor utility bay electrical:

**Outlets:**
- **Minimum 4 GFCI-protected weatherproof receptacles** in the bay
- **20A T-slot receptacles** sized for power tools and pressure washers
- **240V 30A receptacle** for future use (welder, air compressor, EV)
- **USB charging receptacles** for phones and cordless tool batteries (optional)
- **All in weatherproof-in-use covers** (the bubble-type covers that stay weatherproof with a cord plugged in) per NEC 406.9(B)

**Circuits:**
- **Dedicated 20A circuit per outlet pair** — no sharing with house interior circuits
- **Dedicated 20A circuit for bay lighting**
- **Dedicated 30A 240V circuit for the future equipment receptacle**
- **All fed from the outdoor/expansion subpanel in the interconnect box area**

**Lighting:**
- **LED downlights under the bay roof overhang** — 2–4 fixtures, motion-activated
- **Work light receptacle** above the workbench (if a bay workbench is installed) for a movable task light

**Compressed air and utility interface:**
- **Air compressor** located inside the basement or mechanical area (noise reasons)
- **Air line runs through the service layer to the bay** with a quick-disconnect at the bay
- **Compressor electrical** on a dedicated 20A or 30A circuit depending on size

**Pressure washer provisions:**
- **Non-potable water supply** from the rainwater cistern (see Section 6)
- **Dedicated 20A receptacle** for an electric pressure washer

**Key code references:**
- NEC 210.8(A)(3) (outdoor GFCI)
- NEC 406.9 (weather-resistant and weatherproof receptacles)
- NEC 406.9(B) (weatherproof-in-use covers)

---

## 7.14 Future Solar Provisions

**Plain language:** Solar panels will probably go on the roof or on a ground-mounted array eventually, and they need electrical work to connect to the house. That work is easier and cheaper if the house is prepared during the original build. This design includes a spare circuit breaker slot in the main panel, a conduit sleeve from the roof (or a convenient location) down to the panel, and a labeled spot outside for the solar disconnect and inverter.

**Technical detail:** Solar-ready provisions:

**What to install during original construction:**

**1. Conduit from the future solar array location to the panel:**
- **1-1/4 inch EMT conduit** from the roof (if rooftop panels planned) or from the expected ground-mount location, through the service layer, to the interconnect box or main panel area
- **Empty conduit with a pull string** — no wire pulled until the solar system is installed
- **Sized for 60A solar backfeed** (typical for a 7–10 kW residential system) — oversizing for larger systems is cheap

**2. Dedicated breaker slot in the main panel:**
- **One double-pole breaker slot reserved and labeled "SOLAR — DO NOT USE"** at the far end of the panel busbar, opposite the main breaker (NEC 705.12(B) "120% rule" — solar breakers must be located at the opposite end of the busbar from the main)
- **Panel sized to accept the expected solar backfeed** — a 200A panel can accept up to 40A solar backfeed under the 120% rule (200A × 120% = 240A, minus 200A main = 40A available); a 320A or 400A panel can accept proportionally more

**3. Solar disconnect location on the exterior:**
- **Space reserved inside the interconnect box or on an adjacent exterior wall** for a future AC disconnect, required by NEC 690.13 and most utilities
- **Marked on the as-built drawings** so the installer knows where to mount it

**4. Roof penetration provisions (if rooftop solar):**
- **For a concrete slab roof (Option A, see Section 4):** a cast-in conduit stub and weatherproof curb at an appropriate edge of the roof where panels will mount — standard parapet roofs with internal drains can accept rail-mounted solar racks bolted through the roof with flashed penetrations
- **For a metal deck roof (Option B, see Section 4):** standing-seam-compatible mounts are widely available and don't require roof penetrations at all — just clamp to the seams. This is the preferred approach for metal roofs

**5. Inverter location:**
- **Wall space reserved in the basement near the main panel** for a string inverter (if that technology is chosen)
- **OR — microinverter / optimizer systems** (Enphase, SolarEdge) mount on each panel and don't need a central inverter wall location — just an AC combiner and disconnect

**Battery storage provisions:**
- **Space reserved in the basement** (near the main panel, with appropriate ventilation per manufacturer) for a future battery bank (Tesla Powerwall, Enphase IQ Battery, FranklinWH, etc.)
- **Feeder provisioned** from the main panel to the battery location — 60–100A circuit with conduit in place, wire pulled when battery is installed
- **Backup / critical loads subpanel** can be added at that time to island the most important circuits during a grid outage

**Net metering and utility interconnection:**
- **Oregon has net metering** for solar systems up to 25 kW residential (check current rules with the utility — Pacific Power, PGE, or relevant REA)
- **Utility approval required** for interconnection — the utility will require their own disconnect, meter upgrade if needed, and an inspection
- **Permits required:** electrical permit for the solar system, structural permit if the array is large or mounted in an unusual way

**Oversized interconnect box makes all of this clean:** because the original interconnect box has empty DIN rail and knockout space, the solar AC disconnect and possibly a small solar combiner live inside it — no new exterior enclosures needed, no extra holes through the wall.

**Key code references:**
- NEC 690 (solar photovoltaic systems — entire article)
- NEC 705 (interconnected electric power production sources)
- NEC 705.12 (load-side source connections — the "120% rule")
- NEC 690.13 (disconnects)

---

## 7.15 EV Charging Provisions

**Plain language:** Every house built from now on should be ready for electric vehicles. The design includes a spare 50-amp breaker slot for each future EV charger, plus conduit already run to the outdoor charger location, so installing the charger later is a two-hour job instead of a two-day job.

**Technical detail:** EV charging provisions:

**Target capability: two Level 2 EV chargers (240V 48A each)**

**Conduit provisioned during construction:**
- **Two separate 1-inch EMT conduits** from the main panel (or expansion subpanel in the interconnect box) to the two charger locations
- **Charger locations:** under the carport / covered parking / future garage — wherever the cars park
- **Pull strings in each conduit** — wire pulled when charger is installed
- **Weatherproof junction box at each charger location** — labeled, capped, ready

**Circuit provisioned:**
- **Two 50A 240V double-pole breaker slots reserved and labeled** in the expansion subpanel ("EV CHARGER 1" and "EV CHARGER 2")
- **Each slot sized for a 50A breaker** (40A continuous capability, typical for 48A chargers using the 125% continuous-load rule)

**Load management consideration:**
- **Level 2 chargers at 48A each are substantial loads** — two simultaneously running is 96A continuous, which is a significant portion of a 200A subpanel
- **Smart load management** — some chargers (Wallbox, ChargePoint, Emporia) can coordinate to reduce their draw when the house load is high
- **Alternative:** size the service for two chargers running simultaneously at full rate, which is why this design calls for 320–400A service

**Charger specifications (when installed):**
- **Hardwired chargers** preferred over plug-in (more efficient, longer-lived, less nuisance)
- **NEMA 14-50 receptacles** as an alternative if a plug-in charger is chosen
- **Energy Star certified chargers** for efficiency
- **Wi-Fi or ethernet capability** for monitoring and load management

**GFCI protection:**
- **EV chargers have integrated ground-fault protection** (CCID — charging circuit interrupting device)
- **A separate GFCI breaker is NOT required in front of a hardwired EV charger** per NEC 625.54 as long as the charger has CCID (all modern chargers do)

**Future-proofing for higher power:**
- **If conduit is oversized to 1-1/4 inch**, it can accept the wire for a future 80A EV charger (for commercial-grade chargers or V2H / vehicle-to-home applications)
- **If the expansion subpanel breaker slots support 80A double-pole breakers**, same story
- **Cheap insurance at build time; expensive retrofit later**

**Key code references:**
- NEC 625 (electric vehicle charging systems — entire article)
- NEC 625.41 (overcurrent protection)
- NEC 625.42 (rating — continuous load)
- NEC 625.54 (GFCI requirements for personnel protection)

---

## 7.16 Low-Voltage and Networking

**Plain language:** Every room gets hardwired ethernet — a physical network cable — to at least one outlet. WiFi covers the rest, but the backbone is wired. The smart home controller, the security cameras, and the home's main computing all run on the local network without depending on the internet. This is the digital nervous system of the house.

**Technical detail:** Low-voltage systems:

**Ethernet wiring:**
- **Cat6A minimum** throughout (supports 10 Gbps to 100 meters, future-proof for 20+ years)
- **Cat7 or Cat8 in critical runs** (server closet to core switches, for example) — overkill for most but cheap insurance on short runs
- **Minimum two Cat6A drops per habitable room** — one for a desk or entertainment center, one as a spare
- **Four drops in the primary office** — desk PC, printer, NAS, spare
- **Two drops per ceiling location for wireless access points** — one per floor at minimum, more for large footprints
- **Home-run topology** — every cable runs individually from the outlet to the central patch panel, no daisy-chaining

**Central networking location:**
- **Network closet or rack in the basement** — near the main panel or in a dedicated wiring closet
- **48-port patch panel** (or two 24-port) mounted in a standard 19-inch rack
- **Core switch:** managed switch, 24 or 48 ports, 10 Gbps uplinks — Unifi, Aruba Instant On, MikroTik, or similar
- **Internet gateway:** router or firewall, connected to the WAN source (fiber, cable, cellular backup)
- **UPS backup** for the networking gear — 30 minutes runtime minimum for graceful shutdown during outages

**Wireless access points:**
- **Ceiling-mounted access points** — Unifi, Aruba, Ruckus, or similar
- **Minimum one AP per floor**, centrally located
- **Additional APs for large floors** — one per 1,500 sqft typical
- **Power over Ethernet (PoE) from the core switch** — no separate power wiring to the APs
- **Service layer mounting** — APs can mount on the underside of the floor above, above the grated service layer ceiling, for centralized coverage without wall-mounting

**Coax cable (TV, cable internet):**
- **RG6 quad-shield runs from each entertainment-center outlet to the network closet**
- **Even if streaming replaces cable TV, the wire is cheap to install during construction** — future resale appeal, and it supports MoCA (Ethernet over coax) as a backup to the Ethernet drops
- **One coax per entertainment-center location** (living room, family room, primary bedroom, office)

**Telephone / legacy:**
- **Cat6A covers this** — legacy phone wiring is not installed, but Cat6A at each outlet can carry analog phone over a pair if ever needed (unlikely, but costs nothing)

**Security and automation low-voltage:**
- **Separate Cat6A runs for camera locations** — PoE cameras at every exterior door, at each corner of the house, and at the driveway entrance
- **Door/window sensors** on a Z-Wave or Zigbee wireless mesh — wired sensors are an option but wireless mesh is more common in modern builds
- **Security panel** in the network closet or a dedicated cabinet
- **Separate Cat6A to the security panel** for cloud-optional integration

**Intercom / video doorbell:**
- **Cat6A + PoE at each exterior door** for a hardwired video intercom
- **This is above and beyond a ring-style wireless doorbell** — a wired intercom lasts longer and doesn't depend on cloud services
- **Integration with the smart home hub** — see Section 10

**Conduit and pathway:**
- **All low-voltage wiring in 3/4-inch minimum conduit** in the service layer — same philosophy as high-voltage: replaceable, upgradeable, serviceable
- **Separated from 120/240V conduit** — minimum 2 inches apart per NEC 725.136, or use of dividers within shared raceways
- **Pull strings in all conduit** — always ready for the next upgrade

**Labeling:**
- **Every cable labeled at both ends** with room, location within the room, and patch panel port
- **Patch panel labeled clearly** with a printed schedule
- **Documentation updated at every addition** (see project binder in Section 11)

**Key code references:**
- NEC 725 (Class 1, 2, 3 remote-control, signaling, and power-limited circuits)
- NEC 770 (optical fiber cables and raceways) — applies to any fiber runs
- NEC 800 (communications circuits — telephone)
- NEC 820 (community antenna television and radio distribution systems — coax)

---

## 7.17 Surge Protection

**Plain language:** Lightning strikes, utility problems, or nearby transformer failures can send a huge pulse of electricity into the house and destroy every electronic device at once. A whole-house surge protector at the main panel stops most of this. It's a $200 device that protects $50,000 worth of electronics. Every modern house should have one.

**Technical detail:** Surge protection layers:

**Layer 1 — Type 1 or Type 2 whole-house surge protector at the main panel:**
- **Location:** Main distribution panel, immediately after the main breaker
- **Rating:** Minimum 40 kA per phase surge current capacity (kA = kiloamps), ideally 80–100 kA for Oregon's lightning climate
- **Type 1 SPDs** (surge protective devices) are installed on the line side of the main breaker — require more formal installation and are preferred for higher-performance systems
- **Type 2 SPDs** are installed on the load side of the main breaker — easier, adequate for most residential installations
- **Recommended brands:** Eaton CHSPT2Ultra, Siemens FS140, Square D HEPD80, Intermatic SurgeStop — all Type 2, all tested, all $150–$400

**Layer 2 — Type 3 point-of-use surge protectors:**
- **Location:** At any sensitive electronics — home theater, computer workstations, networking gear, refrigerator with electronic controls
- **These are plug-in strips** or hardwired branch-circuit protectors
- **Work in combination with the whole-house SPD** — the whole-house catches the big pulse, the point-of-use catches residual and smaller pulses

**Layer 3 — Low-voltage surge protection:**
- **Coax surge arrestors** where the cable or antenna enters the network closet
- **Ethernet surge protection** at the main internet connection point and at any outdoor PoE runs (to exterior cameras, outdoor APs)
- **Grounded to the main grounding bus** at the network closet

**Installation considerations:**
- **SPDs have a finite service life** — they absorb surges and eventually wear out
- **Modern SPDs have indicator lights** showing their status — green = working, red or dark = replace
- **Plan to replace the whole-house SPD every 10–15 years or after any major surge event**
- **Include SPD replacement in the home's maintenance schedule**

**Lightning protection system (separate and optional):**
- **A full lightning protection system** (air terminals / "lightning rods" on the roof, down-conductors, ground rods) is a separate system from surge protection
- **Worth considering for rural sites** in Oregon's lightning belt (eastern and southern Oregon see more lightning than the Willamette Valley)
- **Installed per UL 96A standards** by a certified installer
- **Bonded to the same grounding system as the electrical service**
- **Decision:** deferred to site-specific evaluation. Rural hilltop = probably yes. Suburban valley = probably no.

**Key code references:**
- NEC 230.67 (surge protective device — dwelling units — required as of 2020 NEC)
- NEC 285 (surge-protective devices)
- UL 1449 (SPD standard)
- UL 96A (lightning protection systems)

---

## 7.18 Smart Home Electrical Considerations

**Plain language:** The electrical system is designed to support smart home features (smart switches, smart outlets, automation, monitoring) without being dependent on any particular brand or platform. Every circuit can be made smart later by swapping the switch or breaker. The Smart Home Philosophy is handled in full in Section 10 — this is just the electrical groundwork.

**Technical detail:** Electrical foundations for smart home compatibility:

**Neutral wires in every switch box:**
- **NEC 404.2(C) requires a neutral at every switch location** in dwelling units (2011 NEC and later) — this is a smart-switch enabler since most smart switches need a neutral to operate
- **This code requirement is already met by standard practice**, but worth verifying during rough-in
- **Exception:** switches in raceway where a neutral can be added later — rare

**Deep switch and outlet boxes:**
- **4 inch square deep boxes with mud rings** where smart switches or dimmers might be installed — smart devices are physically larger than standard switches and need more wire-bending room
- **Specifically:** any location that might get a Lutron Caseta Diva, Shelly module, Zooz Z-Wave switch, or similar

**Conduit to every switch and outlet:**
- **As discussed in 7.12** — wires in conduit can be replaced, smart devices can be added or removed, the system can evolve over 1000 years without drywall destruction

**Dedicated circuits for smart home infrastructure:**
- **Network closet has its own dedicated 20A circuit**, UPS-backed — losing this circuit knocks out the home network, so isolate it
- **Smart home hub / controller has its own dedicated circuit** if a separate device (Home Assistant server, for example) rather than embedded in another device
- **Surveillance system and NVR have their own dedicated circuit** if installed

**Low-voltage control wiring for scene-based systems:**
- **Lutron RadioRA or Vantage systems** use low-voltage control wire to dimmers throughout the house — if this is the chosen platform, Cat5e or proprietary control cable is pulled during rough-in to every controllable light
- **Cloud-independent systems** (Lutron is primarily local, Hubitat is local, Home Assistant is local) are the design preference — see Section 10

**Smart panel consideration (repeated from 7.4):**
- **Span Home, Leviton Smart Load Center, Schneider Square D Pulse, Eaton Energy Management** — per-breaker monitoring, remote control, sometimes app-based
- **Deferred decision** — depends on the state of the market at build time and cloud-independence options
- **Not required** for a capable smart home — individual smart switches and outlets provide most of the functionality

**Key code references:**
- NEC 404.2(C) (neutral required at switch locations)
- NEC 314.16 (box fill calculations — important when stuffing smart devices in)
- NEC 725 (low-voltage / Class 2 control wiring)

---

## 7.19 Wire Schedule Summary

**Plain language:** A summary table of the wire types and sizes used in this design, for quick reference during planning and construction.

**Technical detail:** Wire schedule:

| Use | Type | Size | Typical Breaker |
|---|---|---|---|
| Service entrance (320A) | AL SER or CU THHN | 2/0 CU / 4/0 AL | 320A main |
| Service entrance (400A) | AL SER or CU THHN | 3/0 CU / 250 kcmil AL | 400A main |
| Feeder to 200A subpanel | CU or AL THHN | 2/0 CU / 4/0 AL | 200A |
| Feeder to 100A subpanel | CU or AL THHN | 3 CU / 1 AL | 100A |
| General lighting / outlets | CU THHN or NM-B | 12 AWG | 20A |
| Lighting only (optional) | CU THHN or NM-B | 14 AWG | 15A |
| Kitchen SA circuits | CU THHN or NM-B | 12 AWG | 20A |
| Bathroom circuits | CU THHN or NM-B | 12 AWG | 20A |
| Laundry circuit (washer) | CU THHN or NM-B | 12 AWG | 20A |
| Electric dryer (240V) | CU THHN or NM-B | 10 AWG | 30A |
| Electric range (240V) | CU THHN or NM-B | 6 AWG | 50A |
| Wall oven (240V) | CU THHN or NM-B | 8–10 AWG | 30A |
| EV charger (240V, 48A) | CU THHN | 6 AWG | 50A |
| Heat pump (240V) | CU THHN | 8 AWG | 40A |
| Water heater (240V, electric) | CU THHN or NM-B | 10 AWG | 30A |
| Well pump (240V) | CU THHN | 10 AWG | 30A |
| Solar backfeed (7–10 kW) | CU THHN | 6–8 AWG | 40–60A |
| Grounding electrode conductor | CU (bare or green) | #4 to 1/0 | N/A |
| Ethernet | Cat6A UTP | 23 AWG 4-pair | N/A (PoE) |
| Coax | RG6 quad-shield | — | N/A |

**Code minimums:**
- Smallest branch circuit: 15A, 14 AWG copper
- Smallest general-purpose receptacle circuit: 15A, 14 AWG copper (20A/12 AWG recommended)
- Smallest kitchen / bathroom / laundry SA circuit: 20A, 12 AWG copper
- Grounding electrode conductor: based on service size per NEC 250.66

**Voltage drop targets:**
- **≤ 3% for branch circuits** (NEC 210.19(A) Informational Note — not required, recommended)
- **≤ 3% for feeders**
- **≤ 5% combined** (branch + feeder) from service to farthest outlet
- **In practice:** 12 AWG to 50 feet, 10 AWG to 75 feet, 8 AWG to 120 feet for 20A continuous loads — size up for longer runs

**Key code references:**
- NEC 310.15 (conductor ampacity tables — Table 310.16 is the one most used)
- NEC 210.19 (branch circuit conductor sizing — including voltage drop informational note)
- NEC 215.2 (feeder sizing)
- NEC 250.66 (grounding electrode conductor sizing)
- NEC Chapter 9 Table 8 (conductor properties)

---

*End of Section 7 — Electrical*
