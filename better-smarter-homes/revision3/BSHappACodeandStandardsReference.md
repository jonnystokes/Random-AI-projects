# Appendix A — Code and Standards Reference

*Every code section cited in this document, explained in plain language with context*

This appendix is the navigational map to every code and standard referenced throughout the BSH Design and Engineering Documentation. For each entry, you will find:

- **The official citation** (how it appears in the code)
- **The plain-language summary** of what the code section says
- **The full scope** of what the section covers
- **Where it is referenced** elsewhere in this document
- **Why it matters** for this design

The codes are organized hierarchically:

1. **The Oregon Code Structure** — an overview of how Oregon building codes fit together
2. **Oregon Revised Statutes (ORS)** — the legislative foundation
3. **Oregon Administrative Rules (OAR)** — how the statutes are implemented
4. **Oregon Residential Specialty Code (ORSC)** — the main building code
5. **Oregon Electrical Specialty Code (OESC)** and the **National Electrical Code (NEC)** — electrical
6. **Oregon Plumbing Specialty Code (OPSC)** — plumbing
7. **Oregon Mechanical Specialty Code (OMSC)** — HVAC and mechanical
8. **Oregon Energy Efficiency Specialty Code (OEESC)** — energy performance
9. **Industry Consensus Standards** — ACI, ASHRAE, ASTM, ANSI, UL, AHRI, etc.
10. **Federal Regulations** — EPA, FEMA, OSHA

Every section cited in this document is included. Every section has a plain-language summary so the reader doesn't need to pull the code book to understand what's required. When multiple sections combine to create a requirement, that relationship is explained.

---

## 1 — The Oregon Code Structure

**Plain language:** Oregon has its own set of building codes, which are customized versions of national model codes. The state code is based on the International Code Council's (ICC) model codes, but with Oregon-specific amendments. The electrical code is based on the NFPA's National Electrical Code. The plumbing code is based on the Uniform Plumbing Code (UPC), which is less common than the International Plumbing Code (IPC) used in most other states.

**Technical detail:** The Oregon code family:

| Code | Base Document | Publisher | Scope | How often updated |
|---|---|---|---|---|
| ORSC | 2021 IRC + Oregon amendments | Oregon BCD | One- and two-family dwellings, townhouses | Every 3 years typical |
| OESC | 2023 NEC + Oregon amendments | Oregon BCD | Electrical, all occupancies | Every 3 years |
| OPSC | 2021 UPC + Oregon amendments | Oregon BCD | Plumbing, all occupancies | Every 3 years |
| OMSC | 2021 IMC + Oregon amendments | Oregon BCD | Mechanical/HVAC, all occupancies | Every 3 years |
| OEESC | ASHRAE 90.1 + IECC + amendments | Oregon BCD | Energy efficiency, commercial | Every 3 years |
| OSSC | 2021 IBC + Oregon amendments | Oregon BCD | Commercial, non-residential | Every 3 years |

**Oregon BCD** = Oregon Building Codes Division, a division of the Department of Consumer and Business Services.

**How to access the codes:**

- **Free online access:** The Oregon Building Codes Division provides free online access to all specialty codes at **oregon.gov/bcd** under "Codes and Rules." The codes can be viewed online but not downloaded in full.
- **Paid hardcopies and PDF downloads:** The International Code Council (iccsafe.org) sells the base codes. Oregon amendments are overlaid on top.
- **Local library:** Many county libraries have copies of the current ORSC for reference.
- **Building department:** The county building department will have a current copy for reference; they are generally helpful to owner-builders who come in prepared.

**Jurisdictional note:** Counties and cities in Oregon administer the codes but cannot adopt less restrictive requirements. They can adopt additional requirements (more restrictive local amendments) in limited cases — check with the specific jurisdiction for any local modifications.

---

## 2 — Oregon Revised Statutes (ORS)

Oregon Revised Statutes are the enabling laws passed by the Oregon Legislature. They authorize the Building Codes Division to adopt and enforce the specialty codes. A few ORS sections are directly relevant to this design.

### ORS 701.010 — Owner-Builder Exemption from Contractor Licensing

**Plain language:** A homeowner can build their own home on their own land without being a licensed general contractor. They can also do their own plumbing, electrical, and HVAC work on that home. The exemption is limited to a home the owner will occupy as their residence.

**Full text (summary):** The statute exempts individuals performing construction work on a structure they own and will occupy from the requirement to be licensed by the Construction Contractors Board (CCB). The exemption includes the ability to act as the general contractor, coordinate subcontractors, and perform trade work.

**Restrictions:**
- The property must be owned by the individual (not an LLC or other entity — see Tandem Properties LLC v. CCB, 2002)
- The individual must intend to reside in the property as their primary residence
- The property cannot be constructed for the primary purpose of sale
- See ORS 455.320 for the residency requirement that prevents abuse of this exemption

**Where referenced in this document:** Legal, Permits, and Inspections; Build Sequence; Business and Brand Framework. The owner-builder exemption is the legal foundation for this entire design — without it, the owner would need a CCB license or would need to hire a licensed contractor.

**Why it matters:** This statute defines what is legally permitted for this project. Misunderstanding or violating it would expose the owner to CCB action, permit revocation, and potential legal issues at resale.

### ORS 455.320 — Residency Requirement

**Plain language:** A home built under the owner-builder exemption must be occupied by the owner-builder for at least three years before it can be sold. This prevents people from using the exemption to build and flip houses for profit while avoiding contractor licensing.

**Full text (summary):** The statute requires that a person who builds or does construction work on a structure under the owner-builder exemption must occupy that structure as their primary residence for a minimum of three years before selling.

**Documentation of residency** (per Oregon BCD guidance):
- Driver's license address
- Voter registration
- Utility bills in the owner's name
- Oregon income tax returns showing residency
- Homestead property tax exemption

**Where referenced in this document:** Legal, Permits, and Inspections; the portfolio vision discussion in Business and Brand Framework. This requirement fundamentally shapes the portfolio pacing — every home requires 3+ years of residency, so a 5–10 home lifetime portfolio spans 30–50+ years.

**Why it matters:** Selling before the 3-year period would violate the exemption, potentially requiring reclassification of the work as contractor-built (which would trigger licensing, permit, and inspection requirements retroactively). Also creates tax implications (short-term capital gains vs. primary-residence exclusion).

### ORS Chapter 455 — State Building Code (general)

**Plain language:** This entire chapter of Oregon law governs how the state adopts and enforces building codes. It authorizes the Building Codes Division, defines the types of specialty codes, sets enforcement procedures, and provides the legal basis for permits and inspections.

**Key sub-sections:**
- **ORS 455.020** — creates the Building Codes Division
- **ORS 455.100** — authorizes the state building code
- **ORS 455.110** — requires adoption of nationally-recognized codes
- **ORS 455.150** — local government administration
- **ORS 455.320** — owner-builder residency (see above)

**Where referenced in this document:** Legal, Permits, and Inspections; Build Sequence.

### ORS Chapter 701 — Construction Contractors and Building Code

**Plain language:** This chapter of Oregon law regulates contractors — who needs a license, what licenses cost, what requirements apply, and the exemption for owner-builders (ORS 701.010).

**Key sub-sections:**
- **ORS 701.005** — definitions
- **ORS 701.010** — owner-builder exemption (see above)
- **ORS 701.021** — when licensing is required
- **ORS 701.081** — bond and insurance requirements for licensed contractors
- **ORS 701.505** — Construction Contractors Board

**Where referenced:** Legal, Permits, and Inspections; Build Sequence; Business and Brand Framework.

---

## 3 — Oregon Administrative Rules (OAR)

OARs are the detailed implementation rules adopted by state agencies under the authority of the ORS. The building codes themselves (ORSC, OESC, etc.) are adopted as OARs.

**OAR Chapter 918** — Building Codes Division rules. Includes:
- **OAR 918-480** — owner-builder registration and requirements
- **OAR 918-020** — permit fees and procedures
- **OAR 918-460** — inspections

**OAR Chapter 340** — DEQ (Department of Environmental Quality) rules, including septic system requirements (OAR 340-071).

**OAR Chapter 690** — Water Resources Department rules, including well construction standards (OAR 690-200 through 690-230).

**Where referenced in this document:** Land, Site, and Feasibility; Legal, Permits, and Inspections; Build Sequence.

---

## 4 — Oregon Residential Specialty Code (ORSC)

The ORSC is the primary building code for one- and two-family dwellings in Oregon. The 2023 ORSC is based on the 2021 International Residential Code (IRC) with Oregon amendments. Every ORSC section referenced in this document is below, organized by chapter.

### ORSC Chapter 1 — Administration

#### ORSC R105 — Permits

**Plain language:** A building permit is required before any construction begins. The permit application must include plans, specifications, and the site location. Permits expire if work doesn't start within a set time or is abandoned during construction.

**Scope:** Defines when a permit is required, what must be submitted, how long permits remain valid, and the rights of inspectors.

**Key requirements:**
- Application must be made before work begins
- Plans must be submitted for structures over a threshold size
- Permits expire after 180 days of no activity
- Fees must be paid at application
- Owner-builder status must be declared at application

**Where referenced:** Legal, Permits, and Inspections; Build Sequence.

#### ORSC R106 — Construction Documents

**Plain language:** Permit applications must include drawings and specifications showing the design in enough detail for inspectors to verify code compliance.

**Scope:** Defines what drawings must show — site plan, floor plans, elevations, structural details, MEP schematics as applicable.

**Where referenced:** Legal, Permits, and Inspections; Build Sequence.

#### ORSC R109 — Inspections

**Plain language:** The building inspector has the right to enter and inspect the work at every critical stage. Work cannot be covered up until it passes inspection. Required inspections include foundation, framing, rough plumbing, rough electrical, rough mechanical, insulation, and final.

**Scope:** Defines the sequence of inspections, what is inspected at each, and the inspector's authority to stop work for violations.

**Where referenced:** Legal, Permits, and Inspections, extensively. This is the backbone of the inspection sequence.

#### ORSC R110 — Certificate of Occupancy

**Plain language:** Before the building can be legally occupied, a final inspection must verify that all work passes code. A Certificate of Occupancy (CO) is then issued. A Temporary Certificate of Occupancy (TCO) may be issued when the home is habitable but not fully complete.

**Scope:** Defines when a CO can be issued, when a TCO is allowed, and what minimum conditions must be met for a TCO.

**Key requirements for TCO (typical, though jurisdiction-specific):**
- All required inspections for the occupied portion must pass
- At least one complete bathroom
- Working kitchen (at minimum a sink)
- Heating source functional
- Water heater installed
- Smoke and CO detectors installed
- Egress compliant
- No hazardous conditions

**Where referenced:** Legal, Permits, and Inspections; the TCO and move-in discussion in Build Sequence.

### ORSC Chapter 3 — Building Planning

#### ORSC R301 — Design Criteria

**Plain language:** This section sets the overall structural design requirements — what loads the building must withstand (snow, wind, earthquake, dead load, live load) based on the building's location.

**Scope:** The master structural requirements chapter. Sub-sections cover specific loads.

**Where referenced:** Structural Design.

#### ORSC R301.2.1 — Wind Design Criteria

**Plain language:** Walls, roofs, and anchors must resist wind loads based on the local basic wind speed. Oregon basic wind speeds vary from 90 to 115 mph.

**Scope:** Wind speed requirements, pressure zones, fastening requirements.

**Where referenced:** Structural Design.

#### ORSC R301.2.2 — Seismic Provisions

**Plain language:** Buildings must be designed to resist earthquake loads based on local seismic design category. Most of Oregon is in SDC D, the highest residential seismic category.

**Scope:** Seismic design categories, detailing requirements, shear wall and anchor requirements.

**Where referenced:** Structural Design, particularly for the masonry wall design.

#### ORSC R301.2.3 — Snow Load

**Plain language:** Roofs must support the design snow load for the site. Snow loads vary from 20 psf in the Willamette Valley to 100+ psf in the Cascade mountains.

**Scope:** Ground snow load maps, conversion factors to roof snow load, slope factor adjustments.

**Where referenced:** Structural Design, particularly for the roof design in each option.

#### ORSC R301.3 — Story Height

**Plain language:** Each story of the house has a maximum height. For masonry construction, the maximum is 13 feet 7 inches from floor to the top of the next floor.

**Scope:** Establishes the maximum story height based on construction type.

**Critical detail for this design:**
- Maximum masonry story height: **13 feet 7 inches** floor to floor
- This design's story height: 9 ft ceiling + 4 ft service layer + 8 in slab = 12 ft 8 in
- Margin: 11 inches below maximum

**Where referenced:** Structural Design, specifically the story-height calculation proving the design is code-compliant.

#### ORSC R301.5 — Floor Live Load

**Plain language:** Residential floors must support 40 pounds per square foot of live load (people, furniture). Sleeping rooms must support 30 psf. Balconies, attics, and other specific uses have different requirements.

**Scope:** Live load tables for various occupancies and areas.

**Where referenced:** Structural Design, especially floor slab design.

#### ORSC R302 — Fire-Resistant Construction

**Plain language:** Walls and ceilings separating certain spaces must have specified fire-resistance ratings. The most common residential requirement is the wall between a garage and the house.

**Scope:** Fire-resistant assemblies, rated walls, firestop requirements.

**Where referenced:** Wall and ceiling finishes in Interiors, Finishes, and Livability.

#### ORSC R302.5 — Dwelling/Garage Separation

**Plain language:** The wall between an attached garage and the house must be fire-resistant (1/2-inch gypsum board minimum). The door between must be fire-rated (20-minute) and self-closing.

**Scope:** Separation between attached garage and dwelling, door requirements, duct penetration restrictions.

#### ORSC R302.5.1 — Garage/Dwelling Door

**Plain language:** The door between an attached garage and the house must be a 20-minute fire-rated door, solid-core, with self-closing hardware. It cannot be a hollow-core door.

**Where referenced:** Interior and exterior door discussions in Interiors, Finishes, and Livability. Note: this design does not include an attached garage in the initial build, but the code applies if a garage is added later.

#### ORSC R303 — Light, Ventilation, Heating

**Plain language:** Habitable rooms require natural light (typically a window with glass area equal to 8% of the floor area) and ventilation (openable window with 4% of floor area, or mechanical ventilation per ASHRAE 62.2). Rooms must be heatable to 68°F at 3 feet above the floor.

**Scope:** Minimum window sizes, ventilation rates, minimum heated temperature.

**Where referenced:** HVAC, Ventilation, and Air Quality; wall finishes and bathrooms in Interiors, Finishes, and Livability.

#### ORSC R303.4 — Closet Lighting

**Plain language:** Lights in closets must have clearance from stored materials to prevent fire from hot bulbs. Specific dimensions depend on the fixture type — incandescent, fluorescent, LED.

**Scope:** Minimum clearances around closet light fixtures.

**Where referenced:** Storage in Interiors, Finishes, and Livability.

#### ORSC R304 — Minimum Room Areas

**Plain language:** Habitable rooms must meet minimum size requirements. At least one habitable room must be 120 square feet. Other habitable rooms must be 70 square feet minimum with a minimum horizontal dimension of 7 feet. Kitchens must be 50 square feet minimum.

**Scope:** Minimum room sizes and dimensions.

**Where referenced:** Interior layouts in Interiors, Finishes, and Livability.

#### ORSC R310 — Emergency Escape and Rescue Openings

**Plain language:** Every sleeping room and every basement with habitable space must have a window that can serve as an emergency exit. The window must meet specific minimum size requirements — 5.7 square feet openable area, 20 inches minimum width, 24 inches minimum height, sill no more than 44 inches above the floor.

**Scope:** Egress window dimensions, sill height, operability, well requirements for below-grade egress.

**Where referenced:** Bedroom design in Interiors, Finishes, and Livability; the windows phase in Build Sequence.

#### ORSC R311 — Means of Egress

**Plain language:** Every dwelling must have at least one exit door that leads to the outside without requiring passage through any other dwelling unit. The door must be at least 32 inches wide (36 inches preferred) and openable from inside without keys, tools, or special knowledge.

**Scope:** Exit door requirements, hallway widths, stair requirements.

**Where referenced:** Exterior doors in Interiors, Finishes, and Livability; the windows and exterior doors phase in Build Sequence.

#### ORSC R311.2 — Interior Doors (egress)

**Plain language:** Interior doors must open without a key from inside at all times. No interior door can have a lock that requires a key or tool to open from inside. This applies even to bathroom and bedroom doors — thumb-turn locks are OK, keyed deadbolts are not.

**Where referenced:** Access control in Smart Home and Network Systems.

#### ORSC R311.7 — Stairways

**Plain language:** Stairs must meet minimum dimensional requirements — 10-inch minimum tread depth, 7.75-inch maximum riser height, 36-inch minimum width. Stairs must be uniform (no variation in riser height or tread depth beyond 3/8 inch within a stair run).

**Scope:** Tread and riser dimensions, width, uniformity, headroom (6'8" minimum), handrail requirements.

#### ORSC R311.7.8 — Handrails

**Plain language:** Stairs with four or more risers must have at least one handrail. Handrails must be between 34 and 38 inches above the tread nosing, graspable (1.25–2 inch diameter), and continuous along the stair run.

**Where referenced:** Stairs in Structural Design and move-in/TCO requirements in Build Sequence.

#### ORSC R312 — Guards

**Plain language:** Any walking surface more than 30 inches above the ground must have a guard (railing) at least 36 inches tall. Spacing between rail members must be less than 4 inches (preventing a 4-inch sphere from passing through).

**Scope:** Guard location, height, intermediate rail spacing, child safety.

**Where referenced:** Exterior living features in Interiors, Finishes, and Livability; move-in/TCO requirements in Build Sequence.

#### ORSC R314 — Smoke Alarms

**Plain language:** Hardwired, interconnected smoke alarms are required in every bedroom, outside each sleeping area, and on every floor. Battery backup is required. Interconnection means when one alarm senses smoke, all alarms sound.

**Scope:** Smoke alarm locations, power source, interconnection, battery backup.

**Where referenced:** Electrical circuit design and move-in/TCO requirements in Build Sequence.

#### ORSC R315 — Carbon Monoxide Alarms

**Plain language:** CO alarms are required in every bedroom area (within 10 feet of any sleeping room) and within 10 feet of any fuel-burning appliance. Hardwired with battery backup.

**Scope:** CO alarm locations, power source, interconnection with smoke alarms.

**Where referenced:** Electrical circuit design and the combustion-appliance discussion in HVAC, Ventilation, and Air Quality.

#### ORSC R316 — Foam Plastic

**Plain language:** Foam plastic insulation (EPS, XPS, polyiso, spray foam) must be separated from interior living space by a thermal barrier (typically 1/2-inch drywall) to prevent rapid fire spread if a fire reaches the foam.

**Scope:** Thermal barrier requirements, ignition barriers, specific exceptions.

**Where referenced:** Envelope, Water, and Thermal Performance; trim and millwork in Interiors, Finishes, and Livability.

### ORSC Chapter 4 — Foundations

#### ORSC R401.3 — Drainage

**Plain language:** The ground surface around the foundation must slope away from the building at least 6 inches in the first 10 feet, directing water away from the foundation.

**Scope:** Surface drainage, runoff management, protection of the foundation from water accumulation.

**Where referenced:** Structural Design; envelope moisture management; Build Sequence.

#### ORSC R401.4 — Soil Tests and Soil Bearing Capacity

**Plain language:** This is the section of the Oregon Residential Specialty Code that addresses how to determine whether the soil at a building site can support the building. It provides prescriptive bearing capacity values for common soil types — values you can use without engineering analysis if your site clearly fits one of the categories.

**Full citation:** ORSC R401.4 (2023 edition) — Soil Tests and Soil Bearing Capacity

**Scope:**

R401.4 covers:
- When soil tests are required (and when prescriptive values are acceptable)
- Prescriptive allowable bearing pressures for common soil types
- Authority of the building official to require additional testing on questionable sites
- Documentation requirements

**The prescriptive bearing capacity table (R401.4.1):**

| Soil Type | Allowable Foundation Pressure (psf) |
|---|---|
| Crystalline bedrock | 12,000 |
| Sedimentary or foliated rock | 4,000 |
| Sandy gravel and gravel (GW, GP) | 3,000 |
| Sand, silty sand, clayey sand, silty gravel, clayey gravel (SW, SP, SM, SC, GM, GC) | 2,000 |
| Clay, sandy clay, silty clay, clayey silt, silt and sandy silt (CL, ML, MH, CH) | 1,500 |

These are conservative — actual bearing capacity is often higher with engineering analysis. The prescriptive values are sized so that soils visually identified in the field can be relied on without test results.

**Building official authority:**

Under R401.4.2, the building official may require:
- Soil tests when site conditions are questionable
- Engineering analysis when prescriptive values appear inadequate
- Geotechnical report on sites with known difficult conditions

In practice, most rural Oregon owner-builders proceed on prescriptive values, with the inspector verifying soil character at the pre-pour inspection. Tests are required when sites have visible problems or are in areas with documented soil issues.

**Where referenced in this document:** Bearing capacity reference tables and the site decision framework in Ground Prep and Foundation Risk; Structural Design.

**Why it matters:** R401.4 is the regulatory framework for "is this soil good enough." If the soil at the site is clearly one of the listed types (Sandy gravel and gravel, or Sand, etc.), and there are no contrary indications, the owner-builder can rely on the prescriptive value. If conditions are ambiguous or worse than the prescriptive categories, additional testing or engineering is required.

For this design with its heavier-than-typical concrete construction, foundation pressures of 2,500–4,000 psf are common. The prescriptive table shows that:
- Bedrock or sandy gravel/gravel: easy
- Sand or similar: marginal — needs spread footing geometry to distribute load
- Clay: inadequate without engineering — wider footing, soil improvement, or design changes needed

---

#### ORSC R403 — Footings

**Plain language:** Foundation footings must be sized based on soil conditions, building loads, and frost depth. Minimum footing size depends on wall height, building width, and soil bearing capacity.

**Scope:** Footing dimensions, reinforcement, placement below frost depth, mat slab design.

**Where referenced:** Foundation design in Structural Design. For Oregon, frost depth is 12–24 inches in most of the state, deeper in the mountains.

#### ORSC R403.1 — General (footings)

**Plain language:** Footings must extend below the frost line and bear on undisturbed soil (or properly-compacted fill). Footings for masonry walls have specific requirements.

**Scope:** General footing construction requirements.

**Where referenced:** Structural Design.

#### ORSC R404 — Foundation Walls

**Plain language:** Foundation walls retaining soil (like basement walls) must be designed to resist lateral soil pressure. Thickness, reinforcement, and anchorage requirements depend on wall height and backfill height.

**Scope:** Basement wall and crawl space wall requirements — thickness, reinforcement, height limitations.

**Where referenced:** Structural Design.

#### ORSC R405 — Foundation Drainage

**Plain language:** A foundation drain (perimeter drain / drain tile) is required around the base of basement walls, connected to a drainage point that removes water from below the basement floor level.

**Scope:** Drain tile specifications, gravel envelope, filter fabric, discharge.

**Where referenced:** Structural Design; envelope and waterproofing.

#### ORSC R406 — Foundation Waterproofing and Damp-Proofing

**Plain language:** Foundation walls retaining earth must have a damp-proofing coating on the exterior face. If hydrostatic water pressure is expected (high water table), full waterproofing is required instead of just damp-proofing.

**Scope:** Distinction between damp-proofing and waterproofing, specific materials and application methods.

**Key requirement for this design:**
- Damp-proofing is code minimum
- This design specifies full waterproofing (membrane-based) for the 1000-year durability goal — above code
- Fluid-applied elastomeric or sheet membranes; protection board; drainage mat

**Where referenced:** Structural Design and Envelope, Water, and Thermal Performance, extensively.

### ORSC Chapter 5 — Floors

#### ORSC R502 — Wood Floor Framing

**Plain language:** Wood floor framing requirements — joist size, spacing, spans, bridging. Not directly applicable to this design's concrete floor construction, but referenced for context on code floor design principles.

**Scope:** Wood floor framing, joists, girders, headers, bridging.

**Where referenced:** Structural Design, as a comparison to this design's concrete approach.

#### ORSC R506 — Concrete Floors on Ground

**Plain language:** Slab-on-grade floors must meet specified preparation requirements: base course, vapor barrier, reinforcement. Minimum slab thickness is 3.5 inches for most residential floors.

**Scope:** Base course depth, vapor barrier (minimum 6-mil polyethylene), reinforcement, thickness.

**Where referenced:** Foundation design and slab specifications in Structural Design.

### ORSC Chapter 6 — Wall Construction

#### ORSC R606 — General Masonry Construction

**Plain language:** Requirements for masonry walls — allowable heights, thickness, reinforcement, mortar types, workmanship, anchorage. The prescriptive path covers most residential masonry; engineered design (R608) is required for more demanding conditions.

**Scope:** The primary code chapter for prescriptive masonry design. Covers CMU, brick, and stone walls.

**Key requirements:**
- Maximum unsupported wall height limitations
- Minimum wall thickness based on height and construction type
- Mortar specifications (Type M, S, N, O)
- Reinforcement requirements
- Anchorage to floor and roof diaphragms
- Wall ties in cavity wall construction

**Where referenced:** Structural Design, extensively, for structural masonry design.

#### ORSC R606.9 — Lateral Support

**Plain language:** Masonry walls must be laterally supported at the top and bottom (by floor or roof diaphragms) and sometimes at intermediate points. Unsupported wall lengths are limited.

**Scope:** Lateral support spacing, intermediate support, diaphragm connections.

**Where referenced:** Structural Design.

#### ORSC R606.10 — Anchorage

**Plain language:** Masonry walls must be anchored to the floors above and the roof. Typical anchors: metal straps, anchor bolts, or embedded connectors. Spacing and size depend on wall height and loads.

**Scope:** Anchor types, spacing, embedment depth.

**Where referenced:** Structural Design.

#### ORSC R608 — Concrete Construction

**Plain language:** Requirements for structural concrete walls — cast-in-place concrete walls (as opposed to CMU masonry). Includes wall thickness, reinforcement, forming, and pour sequences.

**Scope:** Covers reinforced concrete walls beyond what is covered by R606 for CMU.

**Where referenced:** Structural Design, as a reference for engineered masonry alternatives.

### ORSC Chapter 7 — Wall Covering

#### ORSC R702 — Interior Covering

**Plain language:** Interior wall and ceiling covering requirements — typical drywall installation, plaster application, wood paneling, etc.

**Scope:** Drywall specifications, installation, fasteners, joints.

**Where referenced:** Wall finishes in Interiors, Finishes, and Livability.

### ORSC Chapter 10 — Chimneys and Fireplaces

#### ORSC R1001 — Masonry Fireplaces and Chimneys

**Plain language:** Requirements for traditional site-built masonry fireplaces — firebox dimensions, hearth requirements, chimney construction, clearances to combustibles.

**Scope:** Dimensional requirements, hearth, throat, smoke chamber, flue sizing, spark arrestor.

**Where referenced:** Combustion appliances in HVAC, Ventilation, and Air Quality, if a masonry fireplace is installed.

#### ORSC R1005 — Factory-Built Chimneys

**Plain language:** Factory-built (metal) chimneys used for wood stoves, pellet stoves, and gas appliances must be UL-listed and installed per the manufacturer's instructions. Specific clearances to combustibles must be maintained.

**Scope:** UL 103 listing, clearances, termination, support.

**Where referenced:** Combustion appliances in HVAC, Ventilation, and Air Quality, if a wood stove is installed.

### ORSC Chapter 11 — Energy Efficiency

The N1100 series of the ORSC covers energy efficiency requirements. Most come from the Oregon Energy Efficiency Specialty Code (OEESC) but are integrated here.

#### ORSC N1101 — General Energy Efficiency

**Plain language:** Sets overall energy efficiency requirements, climate zones (Oregon has zones 4C, 4B, 5B), and the prescriptive and performance compliance paths.

**Scope:** Climate zones, compliance methods.

#### ORSC N1102 — Building Thermal Envelope

**Plain language:** Establishes minimum R-values and U-factors for walls, ceilings, floors, and windows. Maximum air leakage rates. Currently requires ≤ 3.0 ACH50 for new residential construction in Oregon.

**Scope:** Insulation R-value tables, window U-factor tables, air leakage requirements, vapor barrier requirements.

**Key requirements:**
- Ceiling insulation: R-49 minimum (climate zone 4C)
- Wall insulation: R-20 cavity + R-5 continuous, or R-13 cavity + R-10 continuous
- Floor (over unconditioned space): R-30
- Basement wall: R-15 continuous or R-19 cavity
- Slab edge: R-10, 24 inches deep
- Window U-factor: 0.30 maximum
- Air leakage: ≤ 3.0 ACH50

**This design's performance:** Exceeds all these requirements. Wall assembly R-25 to R-40+, windows triple-pane U < 0.20, target ACH50 ≤ 1.0.

**Where referenced:** Envelope, Water, and Thermal Performance, extensively.

#### ORSC N1103 — Systems

**Plain language:** Energy efficiency requirements for HVAC, water heating, and lighting — minimum equipment efficiencies, duct sealing, insulation of hot water pipes, lighting efficacy.

**Scope:** Equipment efficiency tables, duct requirements, pipe insulation.

**Where referenced:** HVAC, Ventilation, and Air Quality.

#### ORSC N1103.6 — Mechanical Ventilation

**Plain language:** Whole-house ventilation is required in homes meeting the airtightness threshold. Ventilation rates follow ASHRAE 62.2.

**Scope:** When mechanical ventilation is required, minimum rates, commissioning.

**Where referenced:** Ventilation strategy in HVAC, Ventilation, and Air Quality.

#### ORSC N1104 — Lighting

**Plain language:** At least 90% of permanent lighting fixtures must use high-efficacy lamps (LED standard in 2026).

**Scope:** Percentage of high-efficacy lighting, exemptions.

**Where referenced:** Lighting design in Electrical Power and Lighting; interior lighting in Interiors, Finishes, and Livability.

---

## 5 — Oregon Electrical Specialty Code (OESC) and National Electrical Code (NEC)

The **OESC** is Oregon's adopted electrical code, based on the **NEC** (NFPA 70) with Oregon amendments. The OESC typically follows the most recent NEC adoption. As of 2026, Oregon uses the 2023 NEC with amendments. Most NEC references in this document apply directly to the OESC.

**Important note:** Where the OESC differs from the NEC, the OESC prevails in Oregon. Oregon amendments are listed in the front of the OESC.

### NEC Chapter 1 — General

#### NEC 110.26 — Working Space About Electrical Equipment

**Plain language:** Electrical panels and other equipment require clear working space in front — typically 36 inches wide and deep, 78 inches tall, with illumination. The space cannot be used for storage.

**Scope:** Required clearances based on equipment voltage and size.

**Key requirements:**
- 36 inches minimum depth in front of panels
- 30 inches minimum width
- Unobstructed access

**Where referenced:** Panel/distribution and grounding/bonding discussions in Electrical Power and Lighting.

### NEC Chapter 2 — Wiring and Protection

#### NEC Article 210 — Branch Circuits

**Plain language:** Requirements for branch circuits (the circuits from the panel to outlets and fixtures) — minimum ampacities, loads, required circuits for specific rooms, protection (GFCI, AFCI).

**Scope:** The master article for residential branch-circuit design.

**Where referenced:** Electrical Power and Lighting, extensively.

#### NEC 210.8 — GFCI Protection for Personnel

**Plain language:** Ground Fault Circuit Interrupters (GFCIs) are required in all locations where water and electricity could meet — bathrooms, kitchens, laundry, outdoors, garages, basements, near sinks.

**Scope:** Defines the locations requiring GFCI protection.

**Key GFCI locations (NEC 210.8(A) — dwellings):**
- (1) Bathrooms
- (2) Garages
- (3) Outdoors
- (4) Crawl spaces (if accessible)
- (5) Unfinished basements
- (6) Kitchens (all countertop receptacles)
- (7) Sinks (within 6 feet)
- (8) Boathouses, bathtubs, shower stalls
- (9) Laundry areas
- (10) Indoor damp/wet locations
- (11) Within 6 feet of outside edges of tubs and showers

**NEC 210.8(D)** adds dishwasher branch circuits.

**Where referenced:** GFCI and AFCI protection in Electrical Power and Lighting.

#### NEC 210.11 — Branch Circuits Required

**Plain language:** Specific minimum branch circuits are required: small appliance circuits in the kitchen (at least two 20A), laundry circuit (20A), bathroom circuit (20A), and general-purpose circuits for the rest of the house.

**Scope:** Required dedicated circuits in dwellings.

**Key subsections:**
- **(C)(1):** Two 20A small-appliance circuits minimum for kitchen/dining/pantry countertop outlets
- **(C)(2):** One 20A laundry branch circuit
- **(C)(3):** One 20A bathroom branch circuit (or one per bathroom)

**Where referenced:** Kitchen, bathroom, laundry, and wet-area circuit discussions in Electrical Power and Lighting.

#### NEC 210.12 — Arc-Fault Circuit Interrupter (AFCI) Protection

**Plain language:** AFCI protection is required on nearly all branch circuits supplying outlets in habitable spaces — bedrooms, living rooms, dining rooms, kitchens, hallways, closets, laundry areas.

**Scope:** Locations requiring AFCI protection.

**NEC 210.12(A) — Dwelling Units:**
- All 120V 15A and 20A branch circuits supplying outlets and devices in:
  - Kitchens
  - Family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, or similar areas

**Where referenced:** GFCI and AFCI protection in Electrical Power and Lighting.

#### NEC 210.19 — Branch Circuit Conductor Sizing

**Plain language:** Branch circuit conductors must be sized for the load, with consideration for voltage drop. Voltage drop over the full circuit should be ≤ 3%.

**Scope:** Minimum conductor size, continuous load calculations, voltage drop (informational note, not a hard requirement but recommended).

**NEC 210.19(A) — Informational Note:** 3% voltage drop target.

**Where referenced:** The wire schedule in Electrical Power and Lighting.

#### NEC 210.52 — Receptacle Outlets (dwelling units)

**Plain language:** Establishes minimum receptacle spacing in dwelling units. Receptacles must be placed so that no point along a wall is more than 6 feet from a receptacle (equivalent to 12 feet maximum between receptacles).

**Scope:** Receptacle placement and spacing rules.

**Subsections:**
- **(A):** General provisions — 6-foot rule, every wall 2 feet or longer
- **(C):** Kitchen countertops — 24 inch maximum from any point, 48 inch maximum between receptacles, GFCI required
- **(D):** Bathrooms — at least one receptacle within 3 feet of outside edge of each lavatory basin
- **(F):** Laundry — at least one receptacle for laundry equipment
- **(G):** Basements and garages — at least one receptacle
- **(H):** Hallways — hallways 10 feet or longer need at least one receptacle

**Where referenced:** Receptacle placement in Electrical Power and Lighting.

#### NEC 210.70 — Lighting Outlets Required

**Plain language:** Every habitable room must have at least one wall-switched lighting outlet. In bedrooms, a switched receptacle (not a permanent light) is acceptable. Bathrooms, hallways, stairways, and exteriors require their own switched lighting.

**Scope:** Required lighting outlet locations.

**Where referenced:** Lighting design in Electrical Power and Lighting and interior lighting in Interiors, Finishes, and Livability.

#### NEC Article 215 — Feeders

**Plain language:** Requirements for feeders (the conductors from the main panel to subpanels). Minimum size, overcurrent protection, and voltage drop limits.

**Scope:** Feeder conductor sizing, protection, routing.

**NEC 215.2:** Feeders must be sized for the continuous and non-continuous loads at 125% of continuous load.

**Where referenced:** Panel/distribution and the wire schedule in Electrical Power and Lighting.

#### NEC Article 220 — Branch Circuit, Feeder, Service Load Calculations

**Plain language:** How to calculate the total electrical load of a dwelling. Determines service size. Standard method and optional methods are provided.

**Scope:** Load calculation methods — general lighting, kitchen loads, appliances, heating/cooling.

**NEC 220.83 — Optional Method (existing dwelling):** Provides simplified load calculation that often yields lower (more realistic) total load for existing homes.

**Where referenced:** Service size and capacity planning in Electrical Power and Lighting.

#### NEC Article 230 — Services

**Plain language:** Requirements for the electric service — utility connection point, service entrance conductors, main disconnect, metering.

**Scope:** Service conductor sizing, routing, disconnect requirements.

**Key subsections:**
- **NEC 230.42:** Service entrance conductor ratings
- **NEC 230.67:** Surge protective device requirement at the service (2020+ NEC) — at least a Type 1 or Type 2 SPD must be installed at the service entrance
- **NEC 230.85:** Emergency disconnect required for one- and two-family dwellings (2020+ NEC) — an outdoor disconnect within sight of the meter

**Where referenced:** Service entry and surge protection in Electrical Power and Lighting.

#### NEC Article 240 — Overcurrent Protection

**Plain language:** Circuit breakers and fuses — ratings, placement, selective coordination.

**Scope:** All aspects of overcurrent protection.

**Where referenced:** Panel/distribution in Electrical Power and Lighting.

#### NEC Article 250 — Grounding and Bonding

**Plain language:** The master article for grounding and bonding — how the electrical system is connected to earth and how metallic systems (water pipes, structural steel) are bonded to the electrical ground.

**Scope:** Grounding electrode system, grounding electrode conductor, bonding of piping systems, separately derived systems.

**Key subsections:**
- **NEC 250.28:** Main bonding jumper (the connection between neutral and ground at the main panel, not at subpanels)
- **NEC 250.50:** Grounding electrode system
- **NEC 250.52:** Grounding electrodes (types)
- **NEC 250.52(A)(3):** Concrete-Encased Electrode (CEE) requirements
- **NEC 250.53:** Installation of grounding electrodes
- **NEC 250.66:** Grounding electrode conductor sizing
- **NEC 250.104:** Bonding of piping and structural metal

**Where referenced:** Grounding and bonding in Electrical Power and Lighting, extensively.

#### NEC Article 285 — Surge-Protective Devices (SPDs)

**Plain language:** Requirements for surge protectors at the service and throughout the premises.

**Scope:** SPD types, ratings, locations, UL 1449 listing.

**Where referenced:** Surge protection in Electrical Power and Lighting.

### NEC Chapter 3 — Wiring Methods

#### NEC 310.15 — Conductor Ampacity

**Plain language:** How much current a given wire can safely carry, based on size, insulation type, and installation conditions. This is the master ampacity table.

**Scope:** Ampacity under various conditions.

**Where referenced:** Service size and the wire schedule in Electrical Power and Lighting.

#### NEC 312.2 — Enclosures in Damp and Wet Locations

**Plain language:** Electrical enclosures exposed to moisture must be rated for the conditions. Wet locations require NEMA 4 or NEMA 4X enclosures; damp locations can use NEMA 3R.

**Where referenced:** Service entry in Electrical Power and Lighting.

#### NEC 314 — Boxes and Enclosures

**Plain language:** Requirements for outlet boxes, switch boxes, junction boxes — sizing based on the number of conductors, mounting, accessibility.

**Scope:** Box sizing, box fill calculations, accessibility.

**NEC 314.16:** Box fill calculations — counts conductors, devices, clamps to determine minimum box volume.

**Where referenced:** Smart-home electrical considerations in Electrical Power and Lighting.

#### NEC 340 — Underground Feeder and Branch Circuit Cable (Type UF)

**Plain language:** Requirements for UF cable used for direct burial. Not extensively used in this design (conduit preferred).

**Where referenced:** Wiring routes in Electrical Power and Lighting, by contrast.

#### NEC 342 — Intermediate Metal Conduit (IMC)

**Plain language:** A type of rigid metal conduit, between EMT and RMC in wall thickness. Specs and installation requirements.

**Where referenced:** Wiring routes in Electrical Power and Lighting.

#### NEC 344 — Rigid Metal Conduit (RMC)

**Plain language:** Heavy-wall metal conduit, for demanding applications. Specs and installation requirements.

**NEC 344.26:** Bends limit — 360 degrees of cumulative bends between pull points.

**Where referenced:** Wiring routes in Electrical Power and Lighting.

#### NEC 352 — Rigid PVC Conduit

**Plain language:** Specs for PVC conduit. Schedule 40 and 80 both covered.

**Where referenced:** Service entry and wiring routes in Electrical Power and Lighting.

#### NEC 358 — Electrical Metallic Tubing (EMT)

**Plain language:** Thin-wall steel conduit — the most common commercial conduit type and used extensively in this design's service layer. Specs and installation requirements.

**NEC 358.26:** Same 360-degree bend limit as RMC.

**Where referenced:** Wiring routes in Electrical Power and Lighting.

### NEC Chapter 4 — Equipment for General Use

#### NEC 404 — Switches

**Plain language:** Requirements for switches — ratings, grounding, locations.

**NEC 404.2(C):** Requires a neutral at every switch location in dwelling units (2011+ NEC) — enables smart switches without tripping.

**Where referenced:** Lighting design and smart-home electrical considerations in Electrical Power and Lighting.

#### NEC 406 — Receptacles, Cord Connectors, and Attachment Plugs

**Plain language:** Receptacle standards — ratings, types, special-purpose receptacles.

**Key subsections:**
- **NEC 406.4:** Ratings and types
- **NEC 406.9:** Weather-resistant receptacles (outdoor and wet locations)
- **NEC 406.9(B):** Weatherproof covers (in-use covers for outdoor)
- **NEC 406.12:** Tamper-resistant receptacles (required in dwellings)

**Where referenced:** Receptacle placement and the outdoor utility service bay in Electrical Power and Lighting.

#### NEC 408 — Switchboards, Switchgear, and Panelboards

**Plain language:** Requirements for panels — ratings, working spaces, labeling.

**Where referenced:** Panel/distribution in Electrical Power and Lighting.

#### NEC 410 — Luminaires, Lampholders, and Lamps

**Plain language:** Requirements for lights — fixture ratings, installation methods, IC ratings for recessed lights.

**Where referenced:** Lighting design in Electrical Power and Lighting.

#### NEC 422 — Appliances

**Plain language:** Requirements for appliances — dedicated circuits, ampacity, disconnects.

**Where referenced:** Kitchen circuits in Electrical Power and Lighting.

### NEC Chapter 6 — Special Equipment

#### NEC 625 — Electric Vehicle Charging Systems

**Plain language:** Requirements for EV chargers — dedicated circuits, overcurrent protection, connector types, GFCI equivalence via CCID.

**Key subsections:**
- **NEC 625.41:** Overcurrent protection
- **NEC 625.42:** Rating (125% continuous load)
- **NEC 625.54:** GFCI requirement (CCID built into EVSE provides equivalent protection, so separate GFCI not required for hardwired installs)

**Where referenced:** EV charging provisions in Electrical Power and Lighting.

#### NEC 690 — Solar Photovoltaic (PV) Systems

**Plain language:** Requirements for solar PV — conductor sizing, disconnects, grounding, backfeed into the electrical system.

**Key subsections:**
- **NEC 690.13:** Disconnect requirements (required outdoor disconnect for PV systems)

**Where referenced:** Future solar provisions in Electrical Power and Lighting.

### NEC Chapter 7 — Special Conditions

#### NEC 705 — Interconnected Electric Power Production Sources

**Plain language:** How solar, batteries, and other power sources connect to the utility grid. Includes the "120% rule" for backfeeding into a panel.

**Key subsections:**
- **NEC 705.12:** Load-side source connections
- **NEC 705.12(B):** The 120% rule — panel busbar rating × 120% must be at least (main breaker + solar breaker). Example: 200A panel × 120% = 240A; minus 200A main = 40A max solar backfeed

**Where referenced:** Future solar provisions in Electrical Power and Lighting.

### NEC Chapter 8 — Communications Systems

#### NEC 725 — Class 1, 2, 3 Remote-Control, Signaling, and Power-Limited Circuits

**Plain language:** Rules for low-voltage wiring — thermostats, doorbells, Ethernet, audio, security. Separation from power conductors.

**NEC 725.136:** Separation of Class 2 circuits from power conductors — minimum 2 inches unless in separate raceways.

**Where referenced:** Wiring routes and low-voltage/networking provisions in Electrical Power and Lighting.

#### NEC 760 — Fire Alarm Systems

**Plain language:** Requirements for fire alarm systems (for homes, typically the smoke/CO alarm interconnection). Larger systems in commercial buildings.

**Where referenced:** Circuit design philosophy in Electrical Power and Lighting.

#### NEC 770 — Optical Fiber Cables and Raceways

**Plain language:** Requirements for fiber-optic cables — routing, separations.

**Where referenced:** Low-voltage and networking provisions in Electrical Power and Lighting, if fiber is used.

#### NEC 800 — Communications Circuits

**Plain language:** Requirements for phone and other wired communication systems — spacing, grounding.

**Where referenced:** Low-voltage and networking provisions in Electrical Power and Lighting.

#### NEC 820 — Community Antenna Television and Radio Distribution Systems

**Plain language:** Requirements for coaxial cable television — grounding, routing.

**Where referenced:** Low-voltage and networking provisions in Electrical Power and Lighting.

---

## 6 — Oregon Plumbing Specialty Code (OPSC)

The **OPSC** is Oregon's adopted plumbing code, based on the **Uniform Plumbing Code (UPC)** published by the International Association of Plumbing and Mechanical Officials (IAPMO). Oregon is one of the "Western states" that uses the UPC as its base; most other US states use the **International Plumbing Code (IPC)** published by the International Code Council. This distinction matters because some details differ between the two codes (particularly for DWV and venting).

The current Oregon version is based on the 2021 UPC with Oregon-specific amendments.

### OPSC Chapter 3 — General Regulations

#### OPSC 312 — Protection of Piping

**Plain language:** Pipes passing through walls, floors, or foundations must be sleeved or protected to prevent damage. Pipes in contact with concrete must be protected from electrolytic corrosion where dissimilar metals are involved.

**Scope:** Sleeving, protection from corrosion, mechanical protection.

**Where referenced:** Plumbing layout and penetration details in Plumbing Systems.

### OPSC Chapter 4 — Plumbing Fixtures and Fixture Fittings

#### OPSC 407 — Water-Conserving Fixtures

**Plain language:** Plumbing fixtures must meet maximum flow and flush rate requirements: showerheads ≤ 2.5 GPM, lavatory faucets ≤ 1.5 GPM, kitchen faucets ≤ 2.2 GPM, toilets ≤ 1.6 GPF.

**Scope:** Maximum flow rates for residential fixtures.

**Key requirements:**
- Water closets (toilets): 1.6 GPF max (dual-flush options: 0.8/1.6 or 1.1/1.6)
- Showerheads: 2.5 GPM max (1.8–2.0 GPM commonly achieved in efficient fixtures)
- Lavatory faucets: 1.5 GPM max for residential (0.5 GPM for public)
- Kitchen faucets: 2.2 GPM max
- Urinals: 0.5 GPF max

**Where referenced:** Plumbing Systems and bathrooms in Interiors, Finishes, and Livability.

#### OPSC 411 — Plumbing Fixture Clearances

**Plain language:** Minimum clearances around plumbing fixtures — 15 inches from toilet centerline to nearest wall, 21 inches clear in front of toilet, 24 inches clear in front of shower/tub.

**Scope:** Required clearances around each fixture type.

**Key clearances:**
- Toilet: 15 inches minimum centerline-to-wall on each side; 21 inches clear in front
- Lavatory: 4 inches minimum from lavatory edge to wall; 21 inches clear in front
- Shower: minimum compartment size 1,024 square inches (typically 32x32 inch); 24 inches clear in front

**Where referenced:** Bathrooms in Interiors, Finishes, and Livability.

#### OPSC 412 — Wall-Hung and Counter-Mounted Lavatories

**Plain language:** Requirements for specific lavatory (bathroom sink) mounting types.

**Where referenced:** Bathrooms in Interiors, Finishes, and Livability.

#### OPSC 413 — Water Closets (Toilets)

**Plain language:** Specific requirements for toilets — flush rate, connection type, gaskets, wax rings.

**Scope:** Installation requirements for water closets.

**Where referenced:** Plumbing Systems and bathrooms in Interiors, Finishes, and Livability.

### OPSC Chapter 5 — Water Heaters

#### OPSC 501 — General Water Heater Requirements

**Plain language:** Water heaters must be listed (UL or equivalent), installed per the manufacturer's instructions, and include a temperature-pressure relief (T&P) valve piped to a safe discharge location.

**Scope:** Water heater listing, clearances, T&P valve, discharge pipe, expansion tank requirements, drain pan.

**Key requirements:**
- T&P valve required on every water heater
- T&P discharge pipe to indirect waste receptor or to outside
- Drain pan required when heater is located where leakage could damage the structure
- Expansion tank required in closed systems (where a PRV or backflow preventer prevents thermal expansion back into the supply)
- Seismic strapping required in Oregon (SDC D)

**Where referenced:** Water heating in Plumbing Systems.

### OPSC Chapter 6 — Water Supply and Distribution

#### OPSC 603 — Water Supply Protection

**Plain language:** The potable water supply must be protected from contamination by backflow. Backflow preventers are required at cross-connections.

**Scope:** Backflow prevention methods, device types, testing requirements.

**Key backflow protection devices (by severity):**
- Air gap (highest protection — physical gap between outlet and receptor)
- Reduced-pressure zone (RPZ) backflow preventer — for high-hazard connections
- Double check valve (DCV) — for moderate hazard
- Pressure vacuum breaker (PVB) — for low-pressure connections
- Atmospheric vacuum breaker (AVB) — for hose connections

**Where referenced:** Plumbing Systems.

#### OPSC 604 — Materials and Fittings for Water Supply

**Plain language:** What pipe materials are allowed for water supply. Copper Type L, PEX, CPVC are all acceptable. Each has its own installation requirements.

**Scope:** Approved materials, fittings, joints, installation.

**This design's choices:**
- Copper Type L for main trunk and supply mains
- PEX-A (Uponor, Rehau) for fixture branches
- No CPVC (less durable than copper or PEX)
- No galvanized (scale accumulation, reduced life)
- No lead pipe or lead-containing solder (illegal under federal law)

**Where referenced:** Water supply in Plumbing Systems.

#### OPSC 608 — Protection of Potable Water Supply

**Plain language:** Protection from freezing, from chemical contamination, from physical damage.

**Scope:** Freeze protection depth, wall protection, chemical separation.

**OPSC 608.2 — Freeze Protection:** Water supply pipes must be installed below the frost line or protected by insulation, heat tape, or both.

**Where referenced:** Pipe routing in Plumbing Systems.

#### OPSC 609 — Water Distribution Pipe Sizing

**Plain language:** Water supply pipes must be sized to deliver minimum fixture flow rates at minimum required pressures. Sizing is based on fixture unit counts and available pressure.

**Scope:** Fixture unit calculations, pipe sizing tables, pressure loss calculations.

**Key requirements:**
- 3/4 inch minimum supply pipe to the structure
- 1/2 inch minimum supply pipe to individual fixtures
- Maximum pressure: 80 psi static; PRV required if incoming is higher
- Minimum pressure: 15 psi at the fixture for most residential; some fixtures higher

**Where referenced:** Plumbing Systems.

#### OPSC 612 — Pressure Regulators

**Plain language:** A pressure reducing valve (PRV) is required where incoming water pressure exceeds 80 psi. The PRV reduces static pressure to 80 psi or less.

**Scope:** When PRVs are required, installation, adjustment.

**Where referenced:** Plumbing Systems.

### OPSC Chapter 7 — Drainage Systems

#### OPSC 701 — General Drainage

**Plain language:** Drain systems must be sized to carry the maximum expected flow, with adequate slope and proper venting. Drains must use fittings designed for drainage (not pressure fittings).

**Scope:** Drain slope (typically 1/4 inch per foot for smaller pipes, 1/8 inch per foot for larger), pipe sizing, fixture unit calculations.

**Key requirements:**
- 1/4 inch per foot minimum slope for 2.5" and smaller drains
- 1/8 inch per foot minimum for 3" and larger
- Fixture units per OPSC Table 702.1

**Where referenced:** Plumbing Systems.

#### OPSC 717 — Sewage Backup Protection

**Plain language:** Fixtures below the elevation of the next upstream manhole (basement fixtures in many cases) must have backwater valves to prevent sewer backup. Alternatively, the drain from the fixture must be pumped up.

**Scope:** Backwater valve requirements, sewage ejector pumps.

**Where referenced:** Basement plumbing in Plumbing Systems.

### OPSC Chapter 9 — Vents

#### OPSC 901 — Venting Requirements

**Plain language:** Every drain must be vented to allow air into the drain as water flows. Venting prevents siphonage of traps and allows sewer gas to escape outside. Vent arrangements: continuous vent, wet vent, circuit vent, or individual vent per fixture.

**Scope:** The master venting chapter.

**Key venting approaches:**
- **Individual vent** — every fixture has its own vent up to a stack or roof penetration. Most robust; used in this design.
- **Common vent** — two fixtures share one vent (wyes into the drain at the same level)
- **Wet vent** — a drain pipe also functions as the vent for upstream fixtures
- **Circuit vent** — a horizontal vent serving multiple fixtures
- **Air Admittance Valve (AAV)** — mechanical valve alternative; limited by code to 3 per house in Oregon, and at least one true through-roof vent must remain

**Where referenced:** Venting strategy in Plumbing Systems.

#### OPSC 906 — Vent Pipe Sizing

**Plain language:** Vents must be large enough to admit air and discharge gases without restriction. Sizing is based on the drains served.

**Where referenced:** Plumbing Systems.

#### OPSC 908 — Vent Termination

**Plain language:** Vents terminating through the roof must extend 6 inches above the roof deck. Vents terminating through a wall must be 10 feet from openings (windows, doors, air intakes) or 3 feet above them.

**Scope:** Vent termination heights, clearances from openings.

**Where referenced:** Venting strategy in Plumbing Systems, especially the sidewall venting option.

### OPSC Appendices

#### OPSC Appendix A — Recommended Rules for Sizing

Supplemental sizing guidance.

#### OPSC Appendix C — Alternate Water Sources

Requirements for graywater reuse and rainwater harvesting systems.

**Where referenced:** Cistern and non-potable systems in Plumbing Systems.

#### OPSC Appendix T — Tables

Sizing tables for various systems.

---

## 7 — Oregon Mechanical Specialty Code (OMSC)

The **OMSC** is Oregon's adopted mechanical code, based on the **International Mechanical Code (IMC)** with Oregon amendments. Covers HVAC equipment, ductwork, ventilation, combustion appliances, and some refrigeration applications.

Current version based on the 2021 IMC.

### OMSC Chapter 3 — General Regulations

#### OMSC 304 — Installation

**Plain language:** Equipment must be installed in accordance with the manufacturer's instructions and listed conditions. Installations must comply with all applicable codes.

**Scope:** General installation requirements applicable to all equipment.

**Where referenced:** HVAC, Ventilation, and Air Quality.

#### OMSC 306 — Access and Service Space

**Plain language:** Mechanical equipment must have adequate space for installation, operation, and service. Typical requirements: 30 inches clear in front of equipment, access opening at least 22 inches wide.

**Scope:** Access and working clearances for equipment.

**Where referenced:** Mechanical room design in HVAC, Ventilation, and Air Quality.

### OMSC Chapter 4 — Ventilation

**Plain language:** Establishes minimum ventilation requirements — outdoor air, exhaust, and makeup air. References ASHRAE 62.2 for dwelling ventilation.

**Scope:** Mechanical ventilation requirements, natural ventilation alternatives, contaminant control.

**Where referenced:** Ventilation strategy in HVAC, Ventilation, and Air Quality.

### OMSC Chapter 5 — Exhaust Systems

#### OMSC 504 — Clothes Dryer Exhaust

**Plain language:** Clothes dryers must be exhausted directly outside through a dedicated duct. No screens at the termination. Maximum length per manufacturer, typically 35 feet minus 5 feet per elbow.

**Scope:** Duct material, length limits, termination, lint management.

**Key requirements:**
- Rigid smooth-walled metal duct (no flex, no screens)
- 4-inch diameter typical
- Termination with damper, no screen
- Maximum length per manufacturer

#### OMSC 504.6 — Length Limitation (dryer)

**Plain language:** Maximum dryer duct length is typically 35 feet minus 5 feet for each 90° elbow. Longer runs may require booster fans or specialty equipment.

**Where referenced:** Dryer ventilation in HVAC, Ventilation, and Air Quality.

#### OMSC 505 — Domestic Cooking Exhaust Equipment

**Plain language:** Range hoods must be vented outdoors (not recirculating). Filter requirements (grease baffles). Limits on exhaust rate before makeup air is required.

**Scope:** Range hood ratings, duct sizing, termination, makeup air.

#### OMSC 505.2 — Makeup Air

**Plain language:** Range hoods exhausting more than 400 CFM require dedicated makeup air — an intake duct with damper, electrically interlocked with the hood. In a tight house, this requirement prevents negative pressure from the hood.

**Scope:** Makeup air sizing, damper, interlock.

**Where referenced:** Kitchen ventilation in HVAC, Ventilation, and Air Quality.

### OMSC Chapter 6 — Duct Systems

#### OMSC 603 — Duct Construction

**Plain language:** Duct systems must be constructed of approved materials — galvanized steel, aluminum, certain plastics for specific applications. Joints sealed with mastic; flex duct limited to short runs at register boots.

**Scope:** Duct materials, joint sealing, support, installation.

**Where referenced:** Ductwork in HVAC, Ventilation, and Air Quality.

#### OMSC 604 — Insulation

**Plain language:** Ducts passing through unconditioned space must be insulated to code minimums. Ducts inside the conditioned envelope don't require insulation.

**Scope:** R-values required for ducts in different locations.

**Where referenced:** Ductwork in HVAC, Ventilation, and Air Quality. Not applicable in this design because all ducts are inside the envelope.

### OMSC Chapter 9 — Installation of Specific Appliances

#### OMSC 915.3.1 — Carbon Monoxide Detection

**Plain language:** CO detectors required where fuel-burning appliances are installed — within 10 feet of the appliance room.

**Where referenced:** Combustion appliances in HVAC, Ventilation, and Air Quality.

### OMSC Chapter 13 — Hydronic Piping

#### OMSC 1301 — General

**Plain language:** Requirements for hot water heating and cooling piping — materials, pressure testing, installation.

**Scope:** Hydronic piping materials (PEX, copper, steel, CPVC), pressure/temperature limits, testing.

**Where referenced:** Radiant heating and cooling in HVAC, Ventilation, and Air Quality.

### OMSC Appendix C — Commissioning

Supplemental guidance for commissioning of HVAC systems.

**Where referenced:** HVAC commissioning in HVAC, Ventilation, and Air Quality.

---

## 8 — Oregon Energy Efficiency Specialty Code (OEESC)

The **OEESC** is Oregon's adopted energy code for commercial buildings. For residential, energy efficiency is covered in the ORSC Chapter 11 / N1100 series (see above). The OEESC references ASHRAE 90.1 and the IECC.

For this design's residential scope, the primary energy code is embedded in ORSC Chapter 11. See the Oregon Residential Specialty Code section of this appendix for those references.

---

## 9 — Industry Consensus Standards

### American Concrete Institute (ACI)

The ACI is the authoritative body for concrete practice in North America. Publishes "Building Code Requirements for Structural Concrete" and many specialized standards.

#### ACI 318 — Building Code Requirements for Structural Concrete

**Plain language:** The master standard for structural concrete design. Referenced by building codes for commercial construction; provides technical basis for many ORSC concrete requirements.

**Scope:** Design procedures, material requirements, construction requirements, quality control, durability provisions.

**Key sections referenced:**
- Chapter 19: Concrete (materials, mix design, testing)
- Chapter 20: Steel reinforcement
- Chapter 25: Reinforcement details
- Chapter 26: Construction

**Where referenced:** Structural concrete in Structural Design.

#### ACI 332 — Residential Code Requirements for Structural Concrete

**Plain language:** A simplified version of ACI 318 specifically for residential construction. Provides prescriptive solutions for common residential concrete work.

**Scope:** Foundations, walls, slabs in residential construction.

**Where referenced:** Structural Design, as a reference for residential-scale concrete design.

#### ACI 544 — Fiber-Reinforced Concrete

**Plain language:** Comprehensive technical guide for fiber-reinforced concrete — fiber types, mix design, testing, applications.

**Scope:** All aspects of fiber-reinforced concrete.

**Where referenced:** Fiber reinforcement in Structural Design and fiber testing in Testing, Commissioning, and Quality Control.

### American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE)

ASHRAE is the primary professional body for HVAC engineering in North America.

#### ASHRAE 55 — Thermal Environmental Conditions for Human Occupancy

**Plain language:** Defines the comfortable indoor environment for the majority of occupants. Specifies temperature, humidity, air speed, and radiant asymmetry ranges.

**Scope:** Thermal comfort, acceptable conditions, measurement and documentation.

**Key comfort ranges:**
- Winter: operative temperature 68–75°F, RH 30–60%
- Summer: operative temperature 75–80°F, RH 30–60%
- Floor surface temperature: 65–85°F

**Where referenced:** Radiant heating, zoning, and radiant cooling in HVAC, Ventilation, and Air Quality.

#### ASHRAE 62.2 — Ventilation and Acceptable Indoor Air Quality in Residential Buildings

**Plain language:** Sets minimum ventilation rates for dwellings. Balanced ventilation, exhaust-only, and supply-only all acceptable if they meet the rate.

**Scope:** Whole-house ventilation rates, local exhaust (bath, kitchen), source control.

**Key requirements:**
- Whole-house rate: 7.5 cfm per occupant + 0.03 cfm per sqft of conditioned floor area
- Bathroom exhaust: 50 CFM demand or 20 CFM continuous
- Kitchen exhaust: 100 CFM demand or 5 ACH continuous

**Where referenced:** Ventilation strategy in HVAC, Ventilation, and Air Quality.

#### ASHRAE 90.1 — Energy Standard for Buildings Except Low-Rise Residential

**Plain language:** The commercial energy standard. Defines minimum energy performance for commercial buildings. Not directly applicable to this residential design but informs the OEESC and provides reference values.

**Where referenced:** Envelope, Water, and Thermal Performance by context.

#### ASHRAE Handbook

**Plain language:** A four-volume reference updated on a rotating schedule — Fundamentals, HVAC Applications, HVAC Systems and Equipment, Refrigeration. The professional engineer's primary HVAC reference.

**Key chapters:**
- Fundamentals: heat transfer, psychrometrics, thermal comfort
- HVAC Applications Chapter 6: Radiant Heating and Cooling
- HVAC Applications Chapter 23: Building Envelopes
- HVAC Systems and Equipment: specific equipment types

**Where referenced:** HVAC, Ventilation, and Air Quality throughout.

#### ASHRAE Guideline 0 — The Commissioning Process

**Plain language:** Defines the commissioning process for building systems — ensuring systems are designed, installed, and operated to meet the owner's requirements.

**Where referenced:** HVAC commissioning in HVAC, Ventilation, and Air Quality.

### American Society for Testing and Materials (ASTM)

ASTM publishes thousands of materials and testing standards. Only those directly referenced in this document are listed here.

#### ASTM C31 / C31M — Standard Practice for Making and Curing Concrete Test Specimens in the Field

**Plain language:** How to cast concrete cylinders on a construction site for later strength testing. Specifies mold type, filling procedure, consolidation, initial curing.

**Scope:** Field procedure for cylinder casting.

**Where referenced:** Concrete mix testing in Testing, Commissioning, and Quality Control.

#### ASTM C39 / C39M — Standard Test Method for Compressive Strength of Cylindrical Concrete Specimens

**Plain language:** How to crush concrete cylinders to determine compressive strength. Specifies machine calibration, loading rate, result reporting.

**Scope:** Laboratory procedure for compressive strength testing.

**Where referenced:** Concrete mix testing in Testing, Commissioning, and Quality Control.

#### ASTM C78 — Standard Test Method for Flexural Strength of Concrete (Using Simple Beam with Third-Point Loading)

**Plain language:** How to test concrete in bending (flexure) rather than compression. The beam is supported at two points and loaded at two points equidistant from the supports, causing pure bending between the load points. Result: modulus of rupture (flexural strength) in psi.

**Scope:** Laboratory procedure for flexural strength.

**Where referenced:** Concrete mix testing in Testing, Commissioning, and Quality Control.

#### ASTM C143 / C143M — Standard Test Method for Slump of Hydraulic-Cement Concrete

**Plain language:** How to do the slump test — the standard workability measurement for concrete. Fill a cone, invert it, measure how far the concrete "slumps."

**Scope:** Field slump test procedure.

**Where referenced:** Concrete mix testing in Testing, Commissioning, and Quality Control.

#### ASTM C177 — Standard Test Method for Steady-State Heat Flux Measurements and Thermal Transmission Properties by Means of the Guarded-Hot-Plate Apparatus

**Plain language:** The gold standard for measuring insulation R-value. A sample is placed between heated and cooled plates in a laboratory setup; heat flow is measured precisely. All insulation product R-values come from this test.

**Scope:** Laboratory R-value testing.

**Where referenced:** Envelope, Water, and Thermal Performance; hot-box testing in Testing, Commissioning, and Quality Control, as the professional version of the DIY hot box.

#### ASTM C231 / C231M — Standard Test Method for Air Content of Freshly Mixed Concrete by the Pressure Method

**Plain language:** How to measure the amount of entrained air in fresh concrete (important for freeze-thaw resistance). Uses a pressure-based air meter.

**Where referenced:** Concrete mix testing in Testing, Commissioning, and Quality Control.

#### ASTM C518 — Standard Test Method for Steady-State Thermal Transmission Properties by Means of the Heat Flow Meter Apparatus

**Plain language:** A faster alternative to ASTM C177 for insulation R-value, using a heat flow sensor.

**Where referenced:** Hot-box testing in Testing, Commissioning, and Quality Control.

#### ASTM C578 — Standard Specification for Rigid, Cellular Polystyrene Thermal Insulation

**Plain language:** Defines the types and grades of polystyrene insulation (EPS and XPS). Specifies density, compressive strength, R-value, water absorption.

**Key types from C578:**
- Type I EPS: 0.9 pcf density, 10 psi compressive, R-3.6/inch
- Type II EPS: 1.35 pcf, 15 psi, R-4.0/inch
- **Type IX EPS:** 1.8 pcf, 25 psi, R-4.2/inch
- **Type XIV EPS:** 2.85 pcf, 40 psi, R-4.3/inch (used under slab in this design)
- Type IV XPS: 1.6 pcf, 25 psi, R-5.0/inch
- Type VI XPS: 1.8 pcf, 40 psi, R-5.0/inch

**Where referenced:** Envelope, Water, and Thermal Performance; Structural Design.

#### ASTM C1178 / C1178M — Standard Specification for Coated Glass Mat Water-Resistant Gypsum Backing Panel

**Plain language:** The standard for cement board products used behind tile in wet areas. Trade names: Durock, HardieBacker.

**Where referenced:** Wall finishes and bathrooms in Interiors, Finishes, and Livability.

#### ASTM C1289 — Standard Specification for Faced Rigid Cellular Polyisocyanurate Thermal Insulation Board

**Plain language:** Defines grades of polyiso insulation. Used for wall cavity insulation in this design.

**Where referenced:** Envelope, Water, and Thermal Performance.

#### ASTM C1325 — Standard Specification for Non-Asbestos Fiber-Mat Reinforced Cementitious Backer Units

**Plain language:** Another cement board standard (similar to C1178 but for fiber-mat-reinforced variants).

**Where referenced:** Wall finishes in Interiors, Finishes, and Livability.

#### ASTM C1363 — Standard Test Method for Thermal Performance of Building Materials and Envelope Assemblies by Means of a Hot Box Apparatus

**Plain language:** The "big brother" to ASTM C177 — tests full wall assemblies in a large hot box rather than just insulation materials. Captures thermal bridging effects.

**Where referenced:** Hot-box testing in Testing, Commissioning, and Quality Control.

#### ASTM C1396 / C1396M — Standard Specification for Gypsum Board

**Plain language:** The standard for all gypsum board (drywall) products — thickness, strength, fire ratings, water resistance.

**Where referenced:** Wall finishes in Interiors, Finishes, and Livability.

#### ASTM C1609 — Standard Test Method for Flexural Performance of Fiber-Reinforced Concrete (Using Beam With Third-Point Loading)

**Plain language:** The specialized flexural test for fiber-reinforced concrete. Measures not just the peak strength but also the post-crack behavior — how much load the fibers carry after the concrete cracks.

**Scope:** Beam geometry, loading rate, measurement of residual strength at specified deflections.

**Key output:**
- First-crack strength (similar to C78 for unreinforced)
- Peak strength
- Residual strength at L/600 deflection
- Residual strength at L/150 deflection
- Toughness index (area under the load-deflection curve)

**Where referenced:** Fiber reinforcement testing in Testing, Commissioning, and Quality Control.

#### ASTM D6951 — Standard Test Method for Use of the Dynamic Cone Penetrometer in Shallow Pavement Applications

**Plain language:** This is the standard that defines how a Dynamic Cone Penetrometer is built and how the test is performed. The standard specifies the cone shape, hammer weight, drop height, rod dimensions, and the procedure for running the test. Following this standard means your DCP results are comparable to professional DCP results worldwide.

**Full citation:** ASTM D6951 / D6951M — Standard Test Method for Use of the Dynamic Cone Penetrometer in Shallow Pavement Applications

**Scope:**

The standard specifies:
- Cone tip geometry: 60° apex angle, 20 mm base diameter
- Drive rod diameter: 16 mm
- Hammer mass: 8 kg (17.6 lb)
- Drop height: 575 mm (22.6 inches)
- Procedure for seating, driving, and recording
- Data presentation requirements
- Calculation methods for converting blow counts to soil parameters

**The standard provides the empirical correlation:**

```
log10(CBR) = 2.465 - 1.12 × log10(PI)
```

where PI is the penetration index in mm/blow and CBR is the California Bearing Ratio.

**Where referenced in this document:** DCP guidance in Ground Prep and Foundation Risk; the testing program; DCP equipment notes in the materials reference.

**Why it matters:** When buying a DCP, verify that it complies with ASTM D6951 — specifications matter. An off-spec DCP gives readings that don't match the published correlations. The standard also defines the procedure, so an owner-builder running the test per the standard gets data that's interpretable by a geotechnical engineer if needed later.

**Note on the "M" suffix:** D6951 is the inch-pound version; D6951M is the SI (metric) version. The two are equivalent; just ensure your equipment matches your data units.

**Related standards:**
- **ASTM D4318** — Atterberg limits (Liquid Limit, Plastic Limit, Plasticity Index)
- **ASTM D698** — Standard Proctor compaction test
- **ASTM D1557** — Modified Proctor compaction test
- **ASTM D1586** — Standard Penetration Test (SPT)
- **ASTM D5778** — Cone Penetrometer Test (CPT)
- **ASTM D2487** — Unified Soil Classification System (USCS)
- **ASTM D2488** — Visual-manual identification of soils

These are the family of geotechnical standards. Owner-builders working at the DCP level mostly need just D6951; the others are for laboratory or professional work.

---

#### ASTM E119 — Standard Test Methods for Fire Tests of Building Construction and Materials

**Plain language:** The standard fire test for rated wall, floor, and ceiling assemblies. An assembly is exposed to a standard fire curve, and the time until failure is recorded — providing "1-hour rated," "2-hour rated," etc.

**Where referenced:** Wall finishes in Interiors, Finishes, and Livability, especially fire rating context.

### American Society of Civil Engineers (ASCE)

ASCE publishes structural and civil engineering standards. The two most relevant to this design are ASCE 7 (loads) and ASCE 32 (frost-protected shallow foundations). The full ASCE catalog covers many more topics including seismic design, wind load methodology, and building rehabilitation.

#### ASCE 7 — Minimum Design Loads and Associated Criteria for Buildings and Other Structures

**Plain language:** ASCE 7 is the master standard for structural design loads in the United States — wind, snow, earthquake, dead load, live load. It defines the design parameters that buildings must resist. Every building code (including the IRC and ORSC) ultimately references ASCE 7 for the underlying load values.

**Full citation:** ASCE/SEI 7-22 (current as of 2026) — Minimum Design Loads and Associated Criteria for Buildings and Other Structures

The version updates every few years; ORSC 2023 references ASCE 7-16; future ORSC editions will catch up.

**Scope (ground-prep relevance):**

ASCE 7 Chapter 11–22 covers seismic design. Of particular relevance to Ground Prep and Foundation Risk is the **Site Classification system**:

| Site Class | Description | Typical Soils | Seismic Behavior |
|---|---|---|---|
| A | Hard rock | Crystalline bedrock | Best |
| B | Rock | Sedimentary or foliated rock | Very good |
| C | Very dense soil and soft rock | Dense gravel, dense sand, weathered rock | Good |
| D | Stiff soil | Most Oregon residential sites | Average — design baseline |
| E | Soft clay soil | Soft clay layers, plastic clays | Worse — amplifies shaking |
| F | Soils requiring site response analysis | Liquefiable, very organic, etc. | Worst — special design |

**Site Class is determined by the upper 100 feet of soil profile** — average shear wave velocity (Vs30), SPT N-value, or undrained shear strength.

For typical Oregon residential sites:
- Western Oregon, dense soils: Site Class D
- Coastal areas with soft soils: Site Class D or E
- Sites with deep soft clay or liquefiable sand: Site Class E or F
- Bedrock at surface: Site Class C or B

**Where referenced in this document:** Seismic behavior and Oregon soil conditions in Ground Prep and Foundation Risk; seismic loads in Structural Design.

**Why it matters:** Site classification directly affects the seismic design forces the foundation and structure must resist. Site Class E doubles or more the seismic design force compared to Site Class D. A site with poor seismic soil performance can require substantially heavier construction — or be unbuildable for residential use.

For owner-builders, Site Class is determined as part of the foundation design process by the structural engineer. The ground investigation provides the soil profile information that supports the classification.

**Cascadia subduction zone context:** Oregon has very high seismic risk from the Cascadia subduction zone. ASCE 7's seismic provisions are critical for any Oregon residential design. The 2023 ORSC has specific Cascadia-related amendments.

---

#### ASCE 32 — Design and Construction of Frost-Protected Shallow Foundations

**Plain language:** This is the standard for designing foundations that don't need to extend below the frost line, instead using horizontal insulation to prevent the soil under the foundation from freezing. ASCE 32 covers heated buildings, unheated buildings, and provides the design tables for insulation thickness based on local climate.

**Full citation:** ASCE/SEI 32-01 — Design and Construction of Frost-Protected Shallow Foundations

Published by the American Society of Civil Engineers (ASCE) and Structural Engineering Institute (SEI).

**Scope:**

The standard provides:
- Design parameters for FPSF based on **Air-Freezing Index (AFI)** for the location
- Insulation R-value and width requirements at the foundation perimeter
- Distinction between heated and unheated structures
- Worked examples for various climate zones
- Construction details

**Air-Freezing Index for Oregon locations:**

| Location | Air-Freezing Index (°F-days) | Climate Severity |
|---|---|---|
| Astoria, Coast | 0–250 | Mild |
| Portland | 250–500 | Moderate |
| Salem, Eugene | 250–500 | Moderate |
| Bend | 500–1,500 | Cold |
| Klamath Falls | 1,500–2,500 | Severe |
| La Grande, Baker City | 1,500–2,500 | Severe |
| Cascade summit areas | 2,500+ | Very severe |

**Insulation requirements** (general guidance — see ASCE 32 for specific values):

- **AFI < 1,500:** Vertical wall insulation only, no horizontal extension required
- **AFI 1,500–2,500:** Vertical wall insulation + 12–24 inch horizontal extension
- **AFI > 2,500:** Vertical wall insulation + 36–48 inch horizontal extension, possibly more

**Where referenced in this document:** Frost protection in Ground Prep and Foundation Risk; foundation design in Structural Design; envelope and thermal design.

**Why it matters:** ASCE 32 is the technical basis for the FPSF approach used in this design. Where the standard residential code requires footings below frost depth (12–48 inches in Oregon), FPSF allows shallower foundations with proper insulation — a substantial cost savings on excavation and concrete. The standard provides the engineering analysis and design tables that make FPSF code-compliant.

**Companion publication:** **NAHB Frost Protected Shallow Foundations Guide** — a builder-friendly explanation of ASCE 32 with practical detail. Free PDF available from the National Association of Home Builders.

---

### American National Standards Institute (ANSI)

ANSI coordinates and approves US voluntary consensus standards but does not typically write them itself.

#### ANSI A117.1 — Accessible and Usable Buildings and Facilities

**Plain language:** The technical standard for accessibility design. Adopted by the IBC and ADA by reference. Not required for single-family residences but provides the best guidance for accessible features.

**Where referenced:** Door widths, hardware, and aging-in-place in Interiors, Finishes, and Livability.

#### ANSI A137.1 — American National Standard Specifications for Ceramic Tile

**Plain language:** The standard for tile manufacturing and testing — dimensions, strength, water absorption, and critically, slip resistance (DCOF — Dynamic Coefficient of Friction).

**Key slip resistance requirement:** Wet areas and slip-hazard zones require DCOF ≥ 0.42.

**Where referenced:** Floor finishes and bathrooms in Interiors, Finishes, and Livability.

### Underwriters Laboratories (UL)

UL tests products for safety and issues "UL listings" for products that meet the applicable standards. Thousands of UL standards exist.

#### UL 96A — Standard for Installation Requirements for Lightning Protection Systems

**Plain language:** The installation standard for lightning protection systems — air terminals (rods), down-conductors, grounding, bonding.

**Scope:** Complete lightning protection system installation.

**Where referenced:** Surge protection in Electrical Power and Lighting.

#### UL 1449 — Standard for Surge Protective Devices

**Plain language:** The standard for SPDs. SPDs sold in the US are UL 1449 listed, with specific performance ratings (surge current capacity, voltage protection rating).

**Where referenced:** Surge protection in Electrical Power and Lighting.

#### UL 103 — Standard for Chimneys, Factory-Built, Residential Type and Building Heating Appliance

**Plain language:** The standard for factory-built metal chimneys (Class A) used with wood stoves, pellet stoves, and similar appliances.

**Where referenced:** ORSC R1005 and the combustion-appliance discussion in HVAC, Ventilation, and Air Quality.

### Air-Conditioning, Heating, and Refrigeration Institute (AHRI)

AHRI certifies HVAC equipment performance — the ratings printed on equipment labels.

#### AHRI 330 — Sound Rating of Outdoor Unitary Equipment

**Plain language:** How outdoor HVAC units (heat pumps, condensers) are rated for sound level.

**Where referenced:** Mechanical room design in HVAC, Ventilation, and Air Quality.

#### AHRI 340/360 — Performance Rating of Commercial and Industrial Unitary Air-Conditioning and Heat Pump Equipment

**Plain language:** How unitary HVAC equipment is rated for cooling and heating capacity and efficiency.

**Where referenced:** HVAC, Ventilation, and Air Quality.

### International Ground Source Heat Pump Association (IGSHPA)

IGSHPA develops standards and certification programs specifically for ground-source heat pump (geothermal) systems.

**Key IGSHPA standards:**
- IGSHPA Certified Installer program
- Design and installation guidelines
- Loop field sizing methodologies

**Where referenced:** Ground-source heat pump design in HVAC, Ventilation, and Air Quality.

---

## 10 — Federal Regulations

### Environmental Protection Agency (EPA)

#### EPA Section 608 (Clean Air Act) — Refrigerant Handling

**Plain language:** Anyone who handles refrigerants (refilling, repairing, disposing of AC/heat pump equipment) must be EPA 608 certified. The certification is required for legal refrigerant work.

**Scope:** Refrigerant recovery, recycling, reclaiming, certification.

**Where referenced:** Build Sequence — listed as a task that must be hired out because it involves refrigerant work.

#### EPA WaterSense

**Plain language:** A voluntary certification program for water-efficient fixtures. WaterSense-certified toilets, faucets, and showerheads exceed federal efficiency requirements by 20%+.

**Where referenced:** Plumbing Systems and bathrooms in Interiors, Finishes, and Livability.

#### EPA ENERGY STAR

**Plain language:** A voluntary certification program for energy-efficient appliances, windows, HVAC equipment, and whole homes. ENERGY STAR-certified products meet EPA's efficiency thresholds.

**Where referenced:** EV charger selection in Electrical Power and Lighting; appliances in Interiors, Finishes, and Livability.

#### EPA Lead Renovation, Repair and Painting Rule (RRP)

**Plain language:** Contractors working on pre-1978 homes must be lead-certified because of lead paint risk. Not applicable to new construction.

### Federal Emergency Management Agency (FEMA)

#### FEMA Flood Maps (FIRMs — Flood Insurance Rate Maps)

**Plain language:** FEMA maps showing areas at risk of flooding. Properties in Special Flood Hazard Areas (SFHA) require flood insurance for federally-backed mortgages and may have specific construction requirements (raised foundations, flood-resistant materials below the base flood elevation).

**Where referenced:** Site selection and due diligence in Land, Site, and Feasibility and Build Sequence.

### Occupational Safety and Health Administration (OSHA)

#### OSHA 29 CFR 1926 Subpart P — Excavation Safety

**Plain language:** Federal workplace safety regulation governing excavation work. Most relevant for owner-builders when digging foundation excavations or test pits. The regulation is enforced when there are workers (paid or unpaid) on site, and the safety principles apply universally even where enforcement doesn't.

**Full citation:** 29 CFR 1926 Subpart P — Excavations (Sections 1926.650 through 1926.652)

**Scope (ground-prep relevance):**

Subpart P covers:
- **§1926.650:** Definitions and scope
- **§1926.651:** Specific excavation requirements (access/egress, hazardous atmospheres, water accumulation, stability of adjacent structures, protection of employees)
- **§1926.652:** Requirements for protective systems (sloping, shoring, shielding)

**Key requirements relevant to ground prep and test pits:**

**Cave-in protection:** Excavations 5 feet deep or deeper require protective systems unless the excavation is in stable rock. Protection options:
- **Sloping:** Sloping the excavation walls back at an angle determined by soil type
- **Shoring:** Installing temporary supports (sheet piles, hydraulic shoring, etc.)
- **Shielding:** Using a trench box

**Soil classification (Subpart P Appendix A):**

| Type | Description | Maximum Allowable Slope |
|---|---|---|
| Type A | Cohesive, no fissures, no water, etc. | 3/4 H : 1 V (53° from horizontal) |
| Type B | Cohesive but with some adverse conditions | 1 H : 1 V (45°) |
| Type C | Granular, soft cohesive, fissured, water-saturated | 1.5 H : 1 V (34°) |

For owner-builder use, **assume Type C soil unless you have a geotechnical engineer's classification.** This means slope walls at 1.5 H : 1 V or use proper shoring.

**Access and egress:** Excavations 4 feet deep or deeper require ladders, ramps, or stairs within 25 feet of any worker.

**Water accumulation:** Workers shall not work in excavations with accumulated water unless adequate precautions (continuous pumping, special support systems) are in place.

**Adjacent structures:** Excavations cannot undermine sidewalks, foundations, or roadways without engineering analysis.

**Inspection requirements:** A "competent person" (someone trained to recognize hazards and authorized to take corrective action) must inspect excavations daily before work begins, and after any event that could affect stability (rain, earthquake, etc.).

**Where referenced in this document:** Test pit safety and excavation work in Ground Prep and Foundation Risk; Build Sequence.

**Why it matters:** Cave-ins kill multiple workers every year in the U.S. Most fatalities are in trenches or test pits where workers thought "it'll be fine, it's just a few minutes." A cubic yard of soil weighs about 3,000 pounds; a partial collapse can suffocate someone in seconds.

For owner-builders specifically:
- The regulation strictly applies if there are paid workers
- It applies to volunteer workers too in many interpretations
- Even working alone, the safety principles apply — survival is what matters
- **Never enter an unprotected vertical excavation more than 4 feet deep**
- **Sloped excavations are usually easier and safer than shored ones for owner-builder work**
- **A test pit is no exception — it's still an excavation**

For this design's basement excavation (8–10 feet deep), professional sloping (1.5:1) means the top of the excavation is 12–15 feet wider than the bottom. Plan your site layout accordingly. Or hire a contractor with shoring equipment for vertical-walled excavations.

---

#### FTC 16 CFR 460 — Labeling and Advertising of Home Insulation

**Plain language:** Requires truthful labeling of insulation products (R-value, savings claims). Referenced in the Envelope, Water, and Thermal Performance context.

---

### Federal and State Geotechnical Resources

In addition to formal codes and standards, several government databases provide essential information for site evaluation and design:

### NRCS Web Soil Survey

**Plain language:** Not a code or standard per se, but a critical reference resource. The Natural Resources Conservation Service (a USDA agency) maintains a free online tool that provides soil mapping, classification, and engineering interpretation for any address in the United States. For Oregon site evaluation, this is the single best starting resource.

**Access:** websoilsurvey.nrcs.usda.gov

**What it provides:**

For any selected location in the U.S., the Web Soil Survey returns:
- **Soil series** at that location (identified by name)
- **Soil texture** at various depths
- **Hydrologic group** (drainage class)
- **Slope class**
- **Drainage class**
- **Shrink-swell potential** — critical for expansive clay identification
- **Erosion characteristics**
- **Limitations for "Dwellings without basements"**
- **Limitations for "Dwellings with basements"**
- **Limitations for "Local roads and streets"**
- Several hundred other interpretations

**Limitation ratings** are stated as:
- **Not Limited** — soil supports the use without significant problems
- **Somewhat Limited** — soil has features that affect the use; mitigation recommended
- **Very Limited** — soil has features that severely affect the use; major mitigation required

**Example** — looking up a typical Willamette Valley site might return:

```
Soil: Woodburn silt loam, 0 to 3 percent slopes
Slope: 0-3%
Drainage class: Moderately well drained
Shrink-swell: Moderate
Hydrologic group: C
Limitations for Dwellings without basements: Moderate (shrink-swell)
Limitations for Dwellings with basements: Severe (wetness, shrink-swell)
```

That's actionable information BEFORE you ever drive to the site or run a DCP test. It tells you to expect moderate expansive clay, basement is risky due to wetness, and slab-on-grade should work with attention to shrink-swell mitigation.

**Where referenced in this document:** Site evaluation and Oregon soil conditions in Ground Prep and Foundation Risk; site evaluation and due diligence in Land, Site, and Feasibility and Build Sequence.

**Why it matters:** Web Soil Survey is free, comprehensive, and authoritative. It's the FIRST resource to consult when evaluating any U.S. site. For Oregon, the soil series database is well-developed; for most of the populated portions of the state, you can get useful soil information instantly.

**How to use:**

1. Go to websoilsurvey.nrcs.usda.gov
2. Search by address, coordinates, or interactive map
3. Define your "Area of Interest" (AOI) — the property boundary
4. View the Soil Map showing soil series at that location
5. Click "Soil Data Explorer" tab to access interpretations
6. Print the "Custom Soil Report" for the project file

The Custom Soil Report is a multi-page PDF with all the relevant information, suitable for the project binder and inspector reference.

---

### Oregon DOGAMI Maps and Databases

**Plain language:** The Oregon Department of Geology and Mineral Industries maintains free online maps of geological hazards relevant to building. For site evaluation, the most important are SLIDO (landslides), liquefaction susceptibility, and tsunami zones (coastal sites only).

**Access:** oregongeology.org

**Key DOGAMI products for site evaluation:**

**SLIDO — Statewide Landslide Information Database for Oregon:**
- Maps of historical landslides
- Maps of landslide-prone areas (geologic susceptibility)
- Recent landslide events
- Search by address or coordinates

**Liquefaction Susceptibility Maps:**
- Areas where saturated loose soils could liquefy in an earthquake
- Coverage focused on populated areas and infrastructure corridors
- Greatest concern: coast, lower river valleys, fill areas

**Earthquake Hazard Maps:**
- Shaking intensity expected from Cascadia subduction zone events
- Coverage statewide

**Tsunami Inundation Maps (coastal only):**
- Areas at risk of tsunami inundation
- Critical for coastal sites

**Geologic Maps:**
- Bedrock and surficial geology
- Fault locations
- Various scales available

**Where referenced in this document:** Site evaluation and Oregon soil conditions in Ground Prep and Foundation Risk; site selection in Land, Site, and Feasibility.

**Why it matters:** DOGAMI's products identify hazards at a regional scale that may not be obvious from on-site investigation. A site might look fine from a DCP test but be in an active landslide area; the SLIDO database catches that. A coastal site might pass all soil tests but be in a tsunami zone; the inundation maps catch that.

**Workflow for any Oregon site:**

1. Get the parcel coordinates from county records or GPS
2. Search NRCS Web Soil Survey for soil series and limitations
3. Search DOGAMI SLIDO for landslide history and susceptibility
4. Search DOGAMI for liquefaction susceptibility
5. Search FEMA flood maps for flood hazard
6. Search Oregon Water Resources for nearby well logs (water table info)
7. Compile findings into the site investigation file
8. THEN go to the site for DCP and visual investigation

This desktop workflow takes a few hours and costs nothing. It can identify showstoppers before you spend time and money on field investigation.

---

## 11 — Code Compliance Strategy

**Plain language:** This design goes beyond code minimum in nearly every area. Understanding code requirements is important to ensure the design meets them — not to do only the minimum, but to be sure nothing is missed. Code compliance is the floor; the design performance is the ceiling.

**Compliance strategy:**

1. **Every design decision is checked against applicable code sections.** Where the design exceeds code, the margin is documented (e.g., R-40 walls vs. R-20 minimum; ACH50 ≤ 1.0 vs. ≤ 3.0 minimum).

2. **Where design decisions are unusual** (service layer, interconnect box, individual vents instead of stacks), the design is documented with the specific code sections that permit or support the approach.

3. **Prescriptive vs. engineered path.** Some code sections provide prescriptive requirements (meeting specific numerical thresholds means compliance). Others require engineered design (stamped by a licensed professional). This design uses the prescriptive path where possible, engineered design where required (structural, particularly).

4. **Documentation for inspections.** The project binder includes the relevant code sections for each inspection, ready for the inspector's review.

5. **Changes during construction.** Any change from the permitted plans requires coordination with the building department — typically a revision review. All changes must continue to meet applicable codes.

6. **Post-construction changes.** Oregon law requires permits for substantial alterations. The homeowner continues to be subject to code requirements for any future modifications.

---

## 12 — How to Stay Current

Building codes update on a 3-year cycle. By the time this home is built, some code sections may have changed. Strategies to stay current:

**Subscribe to code changes:**
- Oregon Building Codes Division maintains a subscription list for code updates
- Industry newsletters (ICC, NFPA, AHRI) cover changes at the national level

**Review at each milestone:**
- Before permit application: verify current adopted codes
- Before each inspection: check if anything has changed since the plan was submitted (inspector will use the code in effect at permit, but for long builds, changes matter)
- Before future renovations: review current codes for applicability

**Build relationships with inspectors:**
- Local inspectors are the authoritative source on how codes are enforced in their jurisdiction
- A good relationship enables quick answers on ambiguous points
- Build respect through preparation and professionalism at every inspection

**Join owner-builder and professional communities:**
- Oregon-specific owner-builder groups share recent experiences
- Local home builders' associations often offer code seminars


---

## 13 — How These Standards Interact in This Design

For a typical ground-prep site investigation, the standards work together:

1. **NRCS Web Soil Survey** identifies the soil series and tells you what to expect (free desktop research)

2. **DOGAMI maps** identify hazards that might not be obvious on site (free desktop research)

3. **ORSC R401.4** tells you the prescriptive bearing capacity for the identified soil type

4. **ASTM D6951** provides the procedure for DCP testing to verify that the actual site soil performs as expected

5. **OSHA 29 CFR 1926 Subpart P** governs the safety of any test pits or excavations

6. **ASCE 7** classifies the site for seismic design (used by the structural engineer, informed by ground investigation findings)

7. **ASCE 32** governs FPSF design if a frost-protected shallow foundation approach is used

8. **The owner-builder consults all of these together** as part of the site evaluation and design process

If site conditions exceed the prescriptive code envelope (R401.4) or hazards are identified, a **geotechnical engineer** is engaged to provide site-specific analysis, which itself references all the same standards but with site-specific data.

---


*Every code section referenced in the BSH Design and Engineering Documentation is included above. When specific sections of the code matter to the work at hand, refer to this appendix for the plain-language summary. For the full legal text, consult the current Oregon specialty code as published by the Oregon Building Codes Division.*
