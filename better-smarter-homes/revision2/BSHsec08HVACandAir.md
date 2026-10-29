# Section 8 — HVAC and Air

*Heating, cooling, and breathing — the house as a living system*

This section covers how the house is heated, cooled, and ventilated. The design uses radiant floor heating driven by a ground-loop heat exchanger, per-room hydronic control so every room is its own micro-climate, balanced mechanical ventilation with heat recovery, and an airtight envelope that makes all of the above efficient.

The guiding philosophy: **heat the masses, not the air**; **every room tuned independently**; **the envelope is so tight that ventilation must be deliberate**; **treat the ground-loop heat exchanger as a black box** for now and let the specifics evolve with technology.

---

## 8.1 HVAC Philosophy

**Plain language:** Most houses heat and cool the air and hope the people in the room feel comfortable. This house heats and cools the concrete floors and walls — the thermal mass — so the building itself stays at the right temperature and the air along with it. Heat comes from the ground beneath the house through a heat exchanger. Every room has its own valve to set its own temperature. Fresh air comes through a balanced ventilation system that recovers heat from the air leaving the house.

**Technical detail:** Core HVAC design principles:

- **Radiant floor heating** on every habitable floor — hydronic (water-based) loops embedded in a thin concrete topping slab over the structural slab
- **Ground-source heat exchanger** as the primary heat and cool source — a black-box system that extracts heat from the earth in winter and deposits heat into the earth in summer
- **Per-room hydronic zoning** — each room has its own thermostat and its own manifold valve, so every room is an independent thermal zone
- **Balanced mechanical ventilation** with heat recovery (HRV or ERV) — brings fresh air in and exhausts stale air out, with heat exchanged between the two streams
- **Airtight envelope** (see Section 5) means ventilation must be mechanical — you can't rely on leaks to bring in fresh air
- **Minimal ductwork** — because heating and cooling happen through the floors, only ventilation air needs ducting, which is a fraction of the duct volume a conventional forced-air house needs
- **Integrated with the domestic hot water system** (see Section 6) — the heat exchanger can preheat domestic water, and the water heater can serve as backup space heat

**Why this differs from standard residential:**
- Standard houses use forced-air furnaces and central air conditioners pushing heated or cooled air through ducts to every room
- Standard houses often have a single thermostat controlling the entire house — "hot upstairs, cold downstairs" is a universal complaint
- Standard houses rely on natural envelope leakage for ventilation, which is uncontrolled, wasteful, and sometimes inadequate
- Standard houses have massive supply-and-return duct systems consuming 5–10% of the floor area and adding major air-sealing challenges

**The thermal mass advantage:**
- **Thousands of pounds of concrete** in the floors, walls, and foundation act as a thermal flywheel
- **Slow to heat up, slow to cool down** — the system can run at low intensity continuously rather than cycling hard
- **Grid-flexibility ready** — can pre-heat during cheap-electricity hours and coast through expensive hours
- **Comfortable by physics** — radiant surfaces at 70–72°F feel as comfortable as forced air at 74–76°F because a warm floor radiates heat directly to the body

---

## 8.2 The Ground-Loop Heat Exchanger — Black Box Treatment

**Plain language:** The heating and cooling plant is a ground-source heat pump — a machine that moves heat between the house and the ground using buried pipes. It provides heat in winter (pulling warmth from the earth) and cooling in summer (dumping heat into the earth). The exact type and configuration of this system will be chosen closer to build time because the technology is evolving fast and site conditions matter a lot. For now, the design treats it as a "black box" with defined inputs and outputs, and the rest of the HVAC system connects to it through standard hydronic interfaces.

**Technical detail:** Black box specification for the ground-source heat exchanger:

**What the system must do:**
- **Deliver hot water** (heated fluid) to the radiant floor manifolds at the design flow rate and temperature (110–120°F typical for radiant floors)
- **Deliver chilled water** (cooled fluid) to the radiant cooling and/or ventilation cooling coils during summer (55–60°F typical)
- **Optionally preheat domestic hot water** through a heat exchanger in the loop
- **Operate efficiently year-round** — COP (coefficient of performance) of 3.5 or better for heating, EER (energy efficiency ratio) of 15 or better for cooling
- **Interface with standard hydronic components** — manifolds, pumps, zone valves, expansion tanks

**What the system can be (options evaluated at build time):**

**Option A — Closed-loop vertical ground-source heat pump (geothermal):**
- **Deep boreholes** (200–400 ft deep, one per ton of capacity, typically 3–6 boreholes for a 3,000 sqft home)
- **Closed loop of HDPE pipe** filled with a water/glycol mixture circulates through the boreholes
- **Heat pump unit inside the basement** extracts or dumps heat via a refrigerant cycle
- **High capital cost** ($25k–$45k installed)
- **Very long life** — the ground loop lasts 50+ years, the heat pump itself 20–25 years
- **Best fit for: sites with limited horizontal space, clay or rocky soil where trenching is hard**

**Option B — Closed-loop horizontal ground-source heat pump:**
- **Shallow trenches** (4–8 ft deep, hundreds of feet of trench)
- **Closed loop of HDPE pipe** in the trenches
- **Same heat pump unit in the basement** as Option A
- **Lower capital cost** ($15k–$30k installed)
- **Requires substantial yard area** — roughly the size of the house footprint in trenches
- **Best fit for: rural sites with plenty of open land (typical for this design)**

**Option C — Open-loop (pump-and-dump) ground-source heat pump:**
- **Well water as the heat source/sink** — pumped through the heat exchanger and discharged to a second well, pond, or stream
- **Lowest capital cost** ($10k–$20k) if a well and discharge point already exist
- **Requires ample, reliable groundwater**
- **Regulatory complexity** — water rights, discharge permits
- **Not evaluated as primary** — too site-dependent, too regulated for default design

**Option D — Air-source heat pump (not ground-source):**
- **Refrigerant exchange with outside air** via an outdoor unit (looks like a traditional AC condenser)
- **Modern cold-climate models** (Mitsubishi Hyper Heat, Daikin Altherma, Chiltrix) maintain COP > 2.5 down to 0°F
- **Much lower capital cost** ($8k–$18k)
- **Much lower efficiency at temperature extremes** than ground-source
- **Best fit as: a starter system or a backup** for the ground-source system
- **Western Oregon climate:** air-source is entirely viable here; eastern Oregon (colder winters) benefits more from ground-source

**Option E — Hydronic air-to-water heat pump (Chiltrix, SpacePak, etc.):**
- **Air-source heat pump that outputs hot or chilled water** directly to hydronic loops
- **Combines the simplicity of air-source with the comfort of radiant**
- **Emerging technology** — fewer installers, shorter track record, rapidly improving
- **Best fit as: a modernized interpretation of the design** — possibly the right choice depending on build-time options

**Default design assumption for planning purposes:**
- **Closed-loop horizontal ground-source heat pump** (Option B), 3-ton nominal capacity for a 3,000 sqft home, with air-source backup
- **Interfaces to document at rough-in:** 2-inch hydronic supply and return lines, electrical feed (see Section 7), condensate drain, ventilation for the basement equipment location

**Black box interfaces defined in this document:**
- **Hot supply manifold connection** — 1-1/4 inch copper or PEX-A to radiant floor primary loop
- **Chilled supply manifold connection** — 1-1/4 inch copper or PEX-A to radiant cooling and fan coil loops
- **Domestic hot water preheat loop** — 1 inch copper to a heat exchanger feeding the water heater inlet
- **Electrical:** dedicated 40–60A 240V circuit (see Section 7)
- **Physical space reserved:** 8 ft x 10 ft of basement mechanical room floor area, 8 ft ceiling clearance

**Why black-box it:**
- **Technology is changing fast** — today's best choice may be obsolete in 3 years when construction begins
- **Site specifics matter** — borehole drilling cost, ground conditions, water availability all drive the final choice
- **Installer expertise matters** — whoever installs the system should have deep experience with the specific technology chosen
- **The rest of the house doesn't care** — as long as the black box delivers hot and cold fluid at the right temperatures, everything else works

**Key code references:**
- OMSC Chapter 13 (hydronic systems)
- OMSC Chapter 14 (solar systems) — by analogy, renewable thermal systems
- IGSHPA (International Ground Source Heat Pump Association) standards
- ANSI/AHRI 330 (ground-source heat pump equipment rating)

---

## 8.3 Radiant Floor Heating

**Plain language:** Hot water flows through PEX tubing embedded in a thin concrete slab on every floor. The slab becomes the radiator. The whole floor becomes a giant, gentle heating surface. You walk on warm concrete, feel comfortable at lower air temperatures, and never hear a furnace blow.

**Technical detail:** Radiant floor heating design:

**Construction sequence (per floor):**
1. Structural floor slab poured (thick, reinforced, see Section 4)
2. Layer of Type XIV EPS or XPS insulation on top (R-10 minimum, R-15 preferred) — prevents heat from going into the structural slab and being wasted downward
3. PEX-A tubing (1/2 inch typical) laid in a serpentine pattern across the insulation, stapled or clipped to the insulation with a spacing of 6–12 inches
4. Tubing connected to manifold headers at the edge of each room
5. Thin concrete topping slab (1.5–2 inches) poured over the tubing — fiber-reinforced, contains the tubing, becomes the thermal mass
6. Floor finish applied over the topping slab (tile, stained concrete, engineered wood over a thin underlayment)

**Radiant floor construction detail:**

```
Floor finish (tile, stained concrete, etc.)      <-- visible surface
───────────────────────────────────────────
Thin topping slab (1.5-2 in, fiber-reinforced)   <-- thermal mass + tubing encapsulation
   ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐      <-- PEX tubing in serpentine pattern
   │  │  │  │  │  │  │  │  │  │  │  │  │  │
───┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──    <-- insulation layer (XPS or EPS)
───────────────────────────────────────────
Structural slab (reinforced concrete)            <-- load-bearing floor
```

**Tubing specifications:**
- **1/2 inch PEX-A** with oxygen barrier (EVOH coating) — prevents oxygen diffusion into the water that would corrode ferrous components
- **Brands:** Uponor AquaPEX, Rehau RAUPEX, Viega FostaPEX — all established, all long-warrantied
- **Life expectancy:** 50+ years in a radiant floor application
- **Maximum loop length:** 300 feet per loop (typical), keep loops below this to maintain flow and even temperature distribution

**Spacing and flow:**
- **6-inch spacing** for high-output areas (bathrooms, entryways, tile floors, rooms above unheated basements)
- **9–12 inch spacing** for standard living areas
- **Closer to the exterior walls** (6-inch spacing at the perimeter even in standard rooms) to counter edge heat loss

**Water temperature:**
- **Supply temperature: 95–120°F** (lower is better for efficiency with a heat pump)
- **Return temperature: 85–105°F** (a 10°F delta across the loop is typical)
- **Floor surface temperature: 75–85°F** (never exceed 85°F per ASHRAE comfort guidelines — above this, feet feel uncomfortably warm)
- **Air temperature achieved: 65–72°F** with proper sizing

**Manifold design:**
- **One manifold per room** (or one manifold per cluster of rooms on the same thermostat zone)
- **Located in a dedicated mechanical niche** — typically inside a closet, under a stair, or in the service layer
- **Manifold includes:** supply and return headers, individual zone valves per loop, balancing valves, flow meters, air vents, drain ports
- **Each manifold fed from the primary loop** via a takeoff with isolation valves — allows any manifold to be serviced without draining the system

**Why radiant floors specifically:**
- **Massive heated surface** (the entire floor) means low operating temperatures are enough
- **Low operating temperatures pair perfectly with heat pumps** — heat pumps deliver the most heat efficiently at the lowest supply temperatures
- **Radiant heat feels more comfortable than convective heat** at the same air temperature, so you can set the thermostat 2–4°F lower and feel the same
- **No air movement, no dust circulation, no blower noise**
- **No visible equipment** — just floors

**Where radiant doesn't go:**
- **Under wall-to-wall carpet** — carpet insulates the floor from its own heat; works poorly
- **In a subfloor above insulated cavity with no topping slab** — possible with "staple-up" systems but far less effective than encapsulated-in-concrete
- **In the basement slab directly** — this design instead heats the first floor slab (above the basement); the basement stays naturally cool (an asset for food storage, wine, server rooms)

**Key code references:**
- OMSC 1301 (hydronic piping)
- ASHRAE 55 (thermal environmental conditions for human occupancy)
- ASHRAE Handbook — HVAC Applications, Chapter 6 (radiant heating and cooling)

---

## 8.4 Per-Room Hydronic Zoning

**Plain language:** Every room has its own thermostat and its own valve. If the primary bedroom wants 68°F and the office wants 72°F, they both get exactly what they want, at the same time, without a fight. This is the defining luxury feature of the whole HVAC system.

**Technical detail:** Zoning implementation:

**One zone per room — hardware:**
- **Thermostat in each room** (wall-mounted, battery or low-voltage wired, communicates with the manifold controller)
- **Motorized zone valve at the manifold** for that room's loop(s) — opens when the thermostat calls for heat, closes when satisfied
- **Manifold controller** (brand-specific: Uponor I-LON, Rehau Pro-Balance, Viega Multimatic) coordinates all the zone valves on a manifold
- **Primary loop pump** runs when any zone is calling; stops when all are satisfied

**Zone count for a typical 3,000 sqft home:**
- **Floor 1:** 5–7 zones (great room, kitchen, dining, powder room, office, entry)
- **Floor 2:** 4–6 zones (primary bedroom, primary bath, two or three secondary bedrooms, shared bath, hallway)
- **Basement:** 2–4 zones if heated (shop, mechanical, storage, rec room) — often the basement is minimally conditioned
- **Total:** 11–17 zones typical

**Thermostat options:**

**Option A — Traditional wired thermostats:**
- **24V control wiring from each thermostat to the manifold controller** — pulled during rough-in through the service layer
- **Simple, reliable, long-lived** — basic wired thermostats last 20+ years
- **No dependency on WiFi, cloud, or batteries**
- **Preferred for 1000-year-house philosophy**

**Option B — Smart thermostats:**
- **Wireless (Z-Wave, Zigbee, WiFi)** communication to a home automation hub
- **Programmable schedules, remote control, learning algorithms**
- **Shorter life (5–10 years typical), depends on network infrastructure, often cloud-dependent**
- **Used selectively** — main living areas yes, minor rooms maybe not

**Option C — Hybrid:**
- **Wired 24V backbone** to the manifold controller (always-works foundation)
- **Smart thermostat faceplates on top** of the wired backbone where desired
- **Best of both worlds:** system works even if the smart layer fails

**Recommended: Option C** — wired communication is the foundation, smart overlay adds features without creating single points of failure.

**Manifold control panel:**
- **One central controller per manifold** receives the signals from all the room thermostats and opens/closes zone valves accordingly
- **Networked controllers** from the manifolds report back to a master HVAC controller (often part of the home automation system)
- **Local display at each manifold** shows zone status, temperatures, flow rates, and any faults
- **Accessible through the service layer** for inspection and troubleshooting

**Zone balancing:**
- **Flow meters at each loop on the manifold** allow balancing — making sure each loop gets the right amount of water for its heated area
- **Commissioned during initial startup** by setting each loop's flow rate based on design calculations
- **Re-balanced if anything changes** (furniture, room function, additions)

**Zone reconfiguration:**
- **Merging zones:** possible in software — two thermostats can control one set of loops by configuration
- **Splitting zones:** harder (requires adding a loop and manifold port) — so loops are laid out with future flexibility in mind
- **Thermostat migration:** trivial — unplug one thermostat, plug in another — useful when a room's function changes

**Key code references:**
- OMSC 1301 (hydronic piping — applies to zoning components)
- ASHRAE 55 (thermal comfort — different rooms can legitimately have different setpoints)

---

## 8.5 Radiant Cooling

**Plain language:** Running cold water through the same floor loops that heat the house in winter can also cool it in summer — but only partially, because if the floor gets too cold, it drips condensation and becomes a slip hazard. So the design uses radiant cooling for a portion of the summer cooling load, combined with a dehumidified fresh-air supply and targeted fan coils for the hottest days.

**Technical detail:** Radiant cooling design:

**How radiant cooling works:**
- **Chilled water (55–60°F) circulates through the same PEX loops used for heating**
- **Floor surface cools to 65–70°F** — just cool enough to absorb heat from the room
- **Walls and ceiling radiate to the cool floor**, lowering the radiant mean temperature in the room
- **People feel cooler at higher air temperatures** — you can set the air to 78°F and feel like 74°F if the radiant mean is cool

**The condensation challenge:**
- **If the floor surface drops below the room's dew point, water condenses on the floor** — slip hazard, moisture damage, mold risk
- **In Oregon's climate:** summer dew point is typically 50–60°F; floor kept at 65°F has a comfortable 5–15°F margin
- **Mitigation:** dew point sensors in each room; automatic supply-temperature adjustment; dehumidification of ventilation air (ERV vs. HRV choice matters — see 8.7)

**Capacity of radiant cooling:**
- **Sensible cooling capacity: 10–15 BTU/hr per square foot of floor** — meaningful but not maximum
- **A 2,000 sqft floor provides 20,000–30,000 BTU/hr** (about 2 tons) of radiant cooling capacity
- **For comparison:** a 3,000 sqft home in Oregon needs about 24,000–36,000 BTU/hr peak sensible cooling — radiant can cover 60–90% of this
- **The rest comes from:** dehumidified ventilation air, optional fan coils in the most heat-gain-prone rooms, and the thermal mass absorbing and delaying peak loads

**Combined system — radiant + fan coils:**
- **Primary cooling: radiant floor** at 55–60°F supply water, modulated to stay above dew point
- **Latent cooling (humidity removal): ventilation ERV with dehumidification** (see 8.7)
- **Peak sensible cooling: small fan coils** in the kitchen (major heat source from cooking), the primary bedroom (comfort priority during sleep), and any south-facing room with large windows
- **Fan coils use the same chilled water** from the ground-source heat exchanger — tied into the hydronic primary loop

**Cooling zone control:**
- **Same per-room thermostats as heating** — each room calls for cooling in summer just as it calls for heating in winter
- **Heating/cooling mode is system-level** (changeover in spring and fall) rather than per-room, because the same pipes carry hot or cold water but not both simultaneously
- **Shoulder seasons:** some rooms may want heating while others want cooling — handled by ventilation temperature adjustment rather than flipping the radiant system

**Ceiling radiant cooling (alternative consideration):**
- **Radiant cooling works better in ceilings than floors** (cold air naturally falls, so cool ceilings cool the room more efficiently)
- **This design doesn't use ceiling radiant** because the ceilings are structural concrete slabs with a finished surface (plaster, painted, etc.) and embedding tubing in the underside of the floor slab above is complex
- **Possible future upgrade:** panel-style radiant ceiling in specific rooms, fed from the same hydronic system

**Key code references:**
- OMSC 1301 (hydronic piping)
- ASHRAE 55 (thermal comfort)
- ASHRAE Handbook — HVAC Applications, Chapter 6 (radiant heating and cooling)

---

## 8.6 Ventilation Strategy

**Plain language:** Because the house is built so airtight, you can't count on random leaks to bring in fresh air the way older houses do. Fresh air has to come in on purpose, through a mechanical system. A balanced ventilation system pulls stale air out of kitchens and bathrooms, brings fresh air into bedrooms and living spaces, and runs the two air streams past each other in a heat exchanger so that the outgoing warm air pre-warms the incoming cold air (in winter) or the outgoing cool air pre-cools the incoming hot air (in summer).

**Technical detail:** Ventilation design:

**Ventilation concept: balanced mechanical ventilation with heat recovery**

**Two types of heat recovery ventilator:**

**Heat Recovery Ventilator (HRV):**
- **Transfers sensible heat only** (temperature) between the two air streams
- **Better for cold, dry climates** — preserves indoor humidity in winter
- **Simpler, lower cost, fewer moving parts**
- **Good fit for Oregon's cool, generally-humid climate** — HRV retains indoor humidity in winter and exhausts excess humidity in shoulder seasons

**Energy Recovery Ventilator (ERV):**
- **Transfers both sensible heat (temperature) and latent heat (moisture)** — keeps humidity balanced
- **Better for hot, humid climates** — exhausts outdoor humidity before it enters the house in summer
- **Slightly higher cost, more complex core**
- **Good fit for Oregon's summer** — rejects outdoor humidity, helps keep dew point low for radiant cooling

**Recommended for this design: ERV**
- **Reasoning:** Oregon summers can have muggy days that push indoor dew point up, which directly conflicts with radiant cooling operation. ERV exhausts that summer humidity load. In winter, ERV retains indoor humidity that would otherwise dry out from tight-envelope ventilation.
- **Brands:** Zehnder ComfoAir, Panasonic Intelli-Balance, RenewAire, Broan AI Series — all high-efficiency, all with good track records
- **Efficiency target:** ≥85% sensible recovery efficiency, ≥60% latent recovery efficiency

**Ventilation rates:**

**Per ASHRAE 62.2 (the standard adopted by Oregon code for dwelling unit ventilation):**
- **Whole-house ventilation rate:** 
  - 7.5 cfm per occupant + 0.03 cfm per square foot of conditioned space
  - Example 3,000 sqft, 4 occupants: (7.5 × 4) + (0.03 × 3000) = 30 + 90 = **120 cfm continuous**
- **Local exhaust requirements:**
  - Kitchen: 100 cfm demand-controlled OR 25 cfm continuous
  - Bathroom: 50 cfm demand-controlled OR 20 cfm continuous each
  - Laundry (if enclosed): 50 cfm demand-controlled OR 20 cfm continuous

**This design: continuous ventilation + boost mode**
- **Baseline continuous rate:** meets ASHRAE 62.2 whole-house requirement through the ERV, running 24/7 at low speed
- **Boost mode:** ERV ramps up when bathroom or kitchen exhaust is called for, pulling additional air from those rooms
- **Range hood:** separate from ERV system — see 8.8 for kitchen ventilation detail

**Airflow distribution:**

**Supply registers (fresh air in):**
- **Bedrooms** — every sleeping room gets a supply
- **Living room / great room** — one or more supplies
- **Office / study** — one supply
- **Hallways** — pass-through air, no direct supply needed

**Exhaust registers (stale air out):**
- **Bathrooms** — every bathroom gets an exhaust
- **Kitchen** — ventilation-grade exhaust (separate from range hood)
- **Laundry** — exhaust if enclosed
- **Mudroom** — exhaust if wet

**Ductwork:**
- **Rigid round metal duct** (galvanized steel) through the service layer — long-lived, cleanable, doesn't collapse
- **Smooth interior surfaces** — low friction, quiet airflow
- **Flex duct only at the final connection to the register boot** — 18 inches maximum — so the ducts meet registers without rigid fabrication
- **Insulated where duct passes through unconditioned space** (not applicable here — all ducts are inside the conditioned envelope)
- **Sealed with mastic at every joint** — no duct tape, ever

**Duct sizing:**
- **Main trunk: 10–12 inch round** — sized for total system airflow at low velocity (≤600 fpm for quiet operation)
- **Branch ducts: 4–6 inch round** — sized for register airflow (25–75 cfm typical)
- **Kitchen ventilation branch: 6–8 inch** — higher volume
- **Range hood duct: 10 inch** — separate from main ventilation, see 8.8

**Key code references:**
- OMSC Chapter 4 (ventilation)
- ASHRAE 62.2 (ventilation and acceptable indoor air quality in residential buildings)
- ORSC M1505 (mechanical ventilation)
- ORSC N1103.6 (mechanical ventilation, in the energy code)

---

## 8.7 Dehumidification and Humidity Control

**Plain language:** Oregon is humid much of the year. A tight house keeps indoor humidity high in winter (because moisture from breathing, cooking, and showering doesn't escape) and can feel muggy in summer. The ventilation system helps, but for full humidity control — especially to make radiant cooling work in summer — a dedicated dehumidifier is integrated into the system.

**Technical detail:** Humidity control strategy:

**Target indoor humidity range: 35–55% relative humidity year-round**

**Winter humidity management:**
- **Source of humidity:** cooking, showering, breathing, plants, drying laundry indoors
- **Without ventilation:** humidity rises to 60–80% in a tight house — condensation on windows, mold risk, discomfort
- **With ERV ventilation:** humidity stays in the 35–50% range naturally — ERV exhausts enough moisture to balance the sources
- **If winter humidity still runs high:** the ERV can be switched to winter "dry mode" (less latent recovery, more moisture exhaust) or a separate dehumidifier runs briefly

**Summer humidity management:**
- **Source of humidity:** outdoor air infiltration (minimal in this design), ventilation air brought in through the ERV, interior sources (cooking, bathing)
- **ERV reduces incoming outdoor humidity** by transferring it back to the exhaust stream — typical latent recovery 60–70%
- **Dedicated dehumidifier** (ducted, whole-house) targets the remaining summer humidity — runs during the humid weeks, quiet during dry weeks

**Whole-house dehumidifier specification:**
- **Type:** ducted, refrigerant-cycle dehumidifier, integrated into the ventilation system
- **Brands:** Ultra-Aire, Santa Fe, Honeywell True-DRY — all ducted, all with >40 pints/day capacity
- **Capacity:** 70–90 pints/day for a 3,000 sqft home in Oregon (sized for summer peak)
- **Location:** basement mechanical room, near the ERV and manifold controller
- **Control:** humidistat calling at setpoint (45–50% RH typical); integrated into the home automation system for visibility

**Integration with radiant cooling:**
- **Dew point sensing in every room** — multiple small sensors feed the manifold controller
- **If any room's dew point rises toward the floor temperature,** radiant cooling in that zone reduces (warmer supply water) and dehumidification increases
- **Worst-case day:** muggy afternoon — dehumidifier runs, radiant floor supply water is raised to 62°F instead of 58°F, fan coil in the kitchen picks up the remaining sensible load
- **Typical day:** radiant floor at 58°F supply, dehumidifier cycles briefly, fan coils idle

**Humidity control in specific rooms:**
- **Bathrooms:** exhaust at 50 cfm (boost to 80–100 cfm during/after showers) via a humidity-sensing ventilation fan or the ERV in boost mode
- **Kitchen:** range hood handles most cooking-generated humidity; ventilation exhaust handles steam from non-range cooking
- **Wine cellar / food storage (if in basement):** separate humidity setpoint (55–70% RH for wine), separate small dehumidifier or humidifier as needed

**Key code references:**
- OMSC 1301 (hydronic piping — relevant to dehumidifier condensate drainage)
- ASHRAE 62.2 (ventilation rates affect humidity)
- ASHRAE 55 (thermal comfort includes humidity range)

---

## 8.8 Kitchen Ventilation — The Range Hood

**Plain language:** Cooking makes smoke, grease, steam, and odors. A real range hood — not a recirculating fan, not a microwave that pretends to be a range hood — exhausts all of that directly outside. Because the house is airtight, the range hood needs a matching fresh air inlet (a make-up air system) so it doesn't create negative pressure and suck air backward through other vents.

**Technical detail:** Kitchen ventilation design:

**Range hood specifications:**
- **Ducted exhaust to the exterior** — mandatory (not recirculating)
- **Capture efficiency** designed for the cooktop (a professional-style 36 or 48 inch cooktop needs a 36 or 48 inch hood with 6-inch overhang on each side)
- **Airflow rating:** 300–600 CFM for residential; higher for professional-style ranges
- **Variable speed** with multiple settings — low, medium, high, boost
- **Baffle filters** (stainless steel) — grease catches in the baffles, filters remove for dishwasher cleaning
- **LED task lighting** integrated
- **Brands:** Broan, Vent-A-Hood, Zephyr, Best (by Broan), Faber — all good, all widely serviceable

**Exhaust duct:**
- **Rigid smooth-wall metal duct** (galvanized or stainless steel) — 6 to 10 inch round depending on hood CFM
- **Short, straight run to exterior** — every elbow reduces effective airflow
- **Termination:** exterior wall cap with damper (check valve prevents backdraft), bug screen, insulated around the penetration
- **Location of termination:** at least 3 feet from any operable window or air intake (per code)
- **Sloped slightly outward** so any condensation drains out, not back into the hood

**Make-up air:**
- **Required for any hood exhausting over 400 CFM** in a tightly-sealed home per OMSC 505.2
- **Even smaller hoods benefit from make-up air** in a tight envelope — without it, the hood creates negative pressure that pulls air back through dryer vents, bathroom fans, fireplace flues, and any leaks
- **Make-up air system:** dedicated intake duct with damper, electrically linked to the range hood so it opens when the hood runs
- **Intake location:** exterior wall near the kitchen, with insect screen and insulated damper
- **Air is not tempered** (not heated or cooled) on a typical system — acceptable for short cooking periods; can be tempered through an inline duct heater for cold climates if desired

**Make-up air sizing:**
- **Volume equal to or slightly less than the hood exhaust** — at 600 CFM hood, a 550 CFM make-up air opening keeps house pressure neutral or very slightly negative

**Alternative: interlocked kitchen ventilation through the ERV:**
- **Instead of a massive dedicated range hood with its own make-up air**, some designs use a smaller hood (200–300 CFM) exhausted through the main ERV system in boost mode
- **Simpler, no make-up air complexity, but less capture efficiency** for heavy cooking (stir-fry, searing, grilling indoors)
- **Not preferred for this design** — the house is for a household that cooks, so a real range hood is worth the complexity

**Key code references:**
- OMSC 505 (domestic cooking exhaust equipment)
- OMSC 505.2 (make-up air required for exhaust hoods exceeding 400 CFM)
- ORSC M1503 (range hoods)

---

## 8.9 Dryer Ventilation

**Plain language:** An electric or gas clothes dryer vents a lot of hot, moist, lint-laden air. That air must exit the house directly, through a short, straight, metal duct to the outside. Like the range hood, the dryer creates a pressure imbalance in a tight house, so some thought is needed — usually the volume is small enough that planned leaks or the ERV can balance it.

**Technical detail:** Dryer exhaust design:

**Duct requirements:**
- **Rigid smooth-wall metal duct** — 4 inch round standard (check dryer manufacturer specs)
- **Maximum length per code:** 35 feet total equivalent length, minus 5 feet per elbow (OMSC 504.6)
- **In this design:** laundry is in the wet zone, exterior wall nearby — short straight run possible
- **Termination:** exterior wall cap with damper, no screen (lint clogs screens quickly — use a pest-resistant termination with a flapper damper instead)
- **Slope:** slightly outward
- **Booster fan:** required if run exceeds the dryer manufacturer's maximum — avoid by keeping the run short

**Gas dryer additional considerations:**
- **Gas supply** to the dryer location — if gas is used for drying
- **Combustion air** — with a power-vented gas dryer or a gas dryer in a tight house, combustion air must be provided (but most residential dryers vent their combustion products through the main exhaust duct)
- **This design preference: electric dryer** — simpler, no gas line needed, integrates with the all-electric philosophy, slightly less efficient but difference is small

**Heat pump dryer (alternative):**
- **A heat pump dryer doesn't vent to the outside** — it condenses moisture internally and drains it like a dishwasher
- **No exhaust duct needed**, no hole through the wall
- **Longer dry cycles, gentler on clothes, much more energy-efficient**
- **Higher purchase cost**
- **Strong candidate for this design** — eliminates one exterior penetration, integrates better with the airtight envelope

**Dryer lint management:**
- **Lint screen inside the dryer** — user responsibility, cleaned every load
- **Duct cleaning: annual minimum** — lint builds up in the duct and is a fire hazard
- **Accessible duct routing** — via the service layer, no concealed elbows, straight to the exterior

**Pressure balance:**
- **Typical dryer exhausts 150–225 CFM** during operation — modest compared to a range hood
- **With a tight envelope and the ERV running**, the pressure imbalance from a dryer is small and self-corrects
- **No dedicated make-up air required** (unless multiple exhausts run simultaneously, in which case the ERV handles balance)

**Key code references:**
- OMSC 504 (clothes dryer exhaust)
- OMSC 504.6 (length limitation)
- ORSC M1502 (clothes dryer exhaust)

---

## 8.10 Combustion Appliances — and Their Avoidance

**Plain language:** Any appliance that burns fuel indoors (gas stove, gas water heater, gas fireplace, wood stove) needs combustion air, creates combustion products that must be vented, and can be dangerous in a tightly-sealed house if not designed carefully. The cleanest path is to eliminate indoor combustion altogether — all-electric. If some combustion is desired (a gas cooktop, a wood stove for ambiance and backup heat), each one needs its own dedicated combustion air supply.

**Technical detail:** Combustion appliance strategy:

**Default: all-electric home**
- **Cooking:** induction cooktop, electric oven
- **Water heating:** heat pump water heater (preferred) or electric resistance water heater
- **Space heating:** ground-source heat pump (primary), electric resistance baseboard or radiant (backup)
- **Dryer:** electric or heat pump
- **No combustion appliances, no natural gas or propane service to the house**

**Why all-electric is the default:**
- **No combustion air complexity** in a tight envelope
- **No flue penetration** through the roof or walls (which are structural in this design)
- **No carbon monoxide hazard**
- **No indoor air pollution from cooking combustion** (gas cooking emits NOx and other pollutants — linked to asthma and other health effects)
- **Future-compatible with solar and battery** — all energy can come from the roof
- **Eliminates one utility service** — no gas meter, no gas line trenching, no gas inspection chain

**If combustion is desired for specific reasons:**

**Option A — Gas cooktop (for cooking preference):**
- **Sealed combustion design is not possible** — a gas cooktop is open-flame
- **Requires range hood with high capture efficiency and make-up air** (see 8.8)
- **Gas service to the kitchen only** — short run, capped and provisioned even if deferred
- **Not the default** — induction cooking is faster, more responsive, more controllable, and safer
- **Decision:** deferred to owner preference at build time; provisioned either way

**Option B — Wood stove or pellet stove (for backup heat and ambiance):**
- **Sealed combustion unit** — direct-vent or "outside-air-kit" equipped so combustion air comes from outside, not from the room
- **Dedicated exterior combustion air duct** per manufacturer's instructions
- **Vent: Class A insulated stainless steel chimney** through the roof (Option A roof) or side wall (Option B roof) — penetration details per manufacturer
- **Distance from combustibles, hearth, clearance to walls** per ORSC R1001–R1002 and manufacturer
- **Useful for:** long power outages (a non-electric heat source is genuinely valuable in a rural area with storm-prone utilities)
- **Decision:** provisioned as an option with a cast-in chimney sleeve and hearth pad location; installed if and when desired

**Option C — Fireplace (for ambiance only):**
- **Electric fireplace:** realistic flame effect, no combustion, no venting — plug in and go. **Recommended if a "fireplace" is desired.**
- **Gas fireplace:** sealed direct-vent unit; same considerations as a wood stove minus the fuel storage
- **Masonry fireplace with flue:** traditional, substantial, exits through the roof — possible but adds a major penetration and combustion air complexity

**Carbon monoxide detection (required anywhere combustion exists):**
- **CO detector within 10 feet of any fuel-burning appliance** — OMSC 915.3.1
- **CO detectors in sleeping areas** — ORSC R315
- **Hardwired and interconnected** (see Section 7)

**Key code references:**
- OMSC Chapter 9 (installation of specific appliances — including combustion)
- ORSC R1001–R1004 (masonry fireplaces and chimneys)
- ORSC R1005 (factory-built chimneys)
- OMSC 505 (domestic cooking — gas)
- ORSC R315 (carbon monoxide alarms)

---

## 8.11 Ductwork Philosophy

**Plain language:** Because heating and cooling happen through the floor, not through blown air, the ducts in this house are small and few. The ventilation ducts are the only ducts. They are all inside the conditioned space (in the service layer), so leakage doesn't waste energy. They're metal, smooth, and accessible — not the flex tubing crammed into an attic that most houses have.

**Technical detail:** Ductwork design principles:

**Ducts are ventilation only** — no heating or cooling supply/return ducts (because heating and cooling are radiant). This is a dramatic simplification from a conventional forced-air system, which uses the house as a duct to connect every room to one central air handler.

**All ducts inside the thermal envelope:**
- **Ductwork routed through the service layer** between floors — fully inside the conditioned space
- **No attic ducts** (this design doesn't have a traditional attic — see Section 4)
- **No crawlspace ducts** (this design uses a conditioned basement or mat slab, not a crawlspace)
- **Zero duct leakage to the outside** — because every inch of duct is inside the envelope

**Duct material:**
- **Galvanized steel rigid round duct** — long-lived, smooth interior (low friction, quiet), cleanable, doesn't sag or compress
- **Sealed at every joint** with mastic and fiber mesh tape — not duct tape (which fails in 5–10 years)
- **Insulation:** unnecessary because ducts are inside the conditioned envelope (this alone saves money, space, and installation labor vs. a conventional system where every duct is insulated)

**Duct sizing:**
- **Ventilation trunk:** 10 inch round, sized for 120–150 CFM at ≤600 feet per minute velocity (quiet)
- **Branch ducts to registers:** 4 to 6 inch round, sized per register CFM
- **Exhaust trunk:** same sizing approach
- **Calculations follow ACCA Manual D** (duct design)

**Register and grille selection:**
- **Supply registers:** directional, adjustable, located to distribute fresh air across the room without blowing on occupants
- **Return/exhaust grilles:** fixed, with cleanable filters — located high on interior walls for heated-air removal (warm stale air rises)
- **Ceiling-mounted registers** where the service layer allows — cleanest aesthetic
- **Wall-mounted registers** where structural constraints prevent ceiling routing

**Transfer grilles:**
- **Between bedrooms and hallways**, so that air supplied to bedrooms can return to the ERV without requiring a return duct in every bedroom (and without losing privacy)
- **Low transfer grilles near the floor** or **over-door transfer openings** — both are acceptable
- **Sized per ACCA Manual T** guidance for transfer air

**Accessibility:**
- **Every duct reachable from the service layer** — pull a grating panel, inspect, clean, modify
- **Cleanout ports** at strategic locations for duct cleaning
- **Dampers at every branch** — balancing is done once, then dampers stay untouched

**Why this is dramatically simpler than conventional:**
- **Duct volume in a conventional forced-air house:** 1,500–3,000 cubic feet of ductwork
- **Duct volume in this design:** 200–400 cubic feet (ventilation only)
- **Energy wasted in duct leakage in a typical home:** 20–30% of heating/cooling output — eliminated here

**Key code references:**
- OMSC Chapter 6 (duct systems)
- OMSC 603 (duct construction)
- OMSC 604 (insulation — not applicable inside conditioned space)
- ACCA Manual D (duct design)
- ASHRAE 62.2 (ventilation rates)

---

## 8.12 Equipment Location — The Mechanical Room

**Plain language:** All the heating, cooling, and ventilation equipment lives in one room in the basement. This puts noise, complexity, and service access all in one place. If something needs fixing, it's there. If something needs replacing in 20 years, the equipment can be swapped out with no disruption to the rest of the house.

**Technical detail:** Mechanical room specification:

**Location:**
- **Basement level, near the interconnect box wall** — minimizes service runs
- **Dedicated room or partitioned corner** — 8 ft x 10 ft minimum, 10 ft x 14 ft for a well-equipped system
- **Door access** from the main basement area — 32 inch minimum door for equipment movement
- **Ceiling height:** full 9 ft to accommodate tall equipment and overhead piping

**Contents:**
- **Ground-source heat pump** (black box) — typically 2–3 ft x 3–4 ft x 4–5 ft tall, wall-mounted or floor-standing
- **Primary hydronic pump and expansion tank** — mounted on a wall with isolation valves
- **Primary manifold** (main distribution) with supply and return to each floor's manifolds
- **Heat pump water heater** (see Section 6) — 6–7 ft tall, needs 1,000+ CF of room air for heat extraction
- **ERV / HRV** — wall or ceiling mounted, 2 ft x 3 ft x 1 ft typical
- **Whole-house dehumidifier** — ducted, floor or wall mounted
- **Water softener / filter** (see Section 6) — 5–6 ft tall, needs floor space
- **Backwash drain** (see Section 6) — floor drain required
- **Main electrical panel** (see Section 7) — wall mounted, 36 in working clearance in front

**Room requirements:**
- **Floor drain** for any equipment condensate, pressure relief, or drainback
- **Epoxy-painted concrete floor** — easy cleanup, resistant to water
- **Dedicated lighting** (see Section 7) — bright, 5000K, every area well-lit
- **Dedicated outlets** for service tools and future equipment
- **Ventilation to the rest of the basement** via transfer grilles — doesn't need its own supply but benefits from air movement
- **Sound isolation:** insulated walls and door to reduce noise transfer to living spaces above
- **No return air from this room to the ERV** — any leaking refrigerant, chemical fumes, or combustion products (if applicable) shouldn't re-enter the house

**Service clearances:**
- **30 inches minimum in front of every piece of equipment** for access and service
- **Full front-removable access** to the heat pump, water heater, and ERV — don't bury them against a wall
- **Ceiling clearance** for vertical piping and duct runs

**Documentation:**
- **Wall-mounted schematic** showing the entire mechanical system — printed, laminated, updated with every change
- **Equipment tags** with model numbers, serial numbers, install dates, service history
- **Maintenance log** kept in a binder in the mechanical room

**Noise:**
- **Typical equipment noise:** heat pump compressor 50–55 dB, water heater compressor 45–50 dB, ERV fan 35–45 dB
- **With insulated mechanical room walls and a solid-core door**, living-space noise impact is negligible
- **Consider:** flexible (vibration-isolating) connections between equipment and building structure to prevent vibration transmission

**Key code references:**
- OMSC 304 (installation — general)
- OMSC 306 (access and service space)
- NEC 110.26 (working spaces around electrical equipment — applies to panels in the mechanical room)

---

## 8.13 Controls, Monitoring, and Home Automation Integration

**Plain language:** The HVAC system has a brain — or actually several brains that talk to each other. Each manifold has a controller, the ERV has a controller, the heat pump has a controller, and all of them report to a central home automation system. The owner sees everything on a phone or tablet, can adjust any room's temperature from anywhere, and can spot problems (like a zone that's not reaching setpoint) before they become breakdowns.

**Technical detail:** Controls and monitoring design:

**Control hierarchy:**

**Level 1 — Equipment-level controls:**
- **Heat pump:** manufacturer's control board (Modbus, BACnet, or proprietary)
- **ERV:** manufacturer's control board (similar protocols)
- **Water heater:** manufacturer's control (typically minimal, some with WiFi)
- **Manifold controllers:** brand-specific (Uponor, Rehau, Viega all have their own)
- **Dehumidifier:** humidistat input, simple on/off or variable capacity

**Level 2 — HVAC integration controller:**
- **A dedicated HVAC controller** (Tekmar, Honeywell, Siemens residential) or a home automation system (Home Assistant, Hubitat) sitting above the equipment controls
- **Reads the room thermostats**, calls for heat or cool from the heat pump, opens/closes zone valves at the manifolds, adjusts ERV speed, controls the dehumidifier
- **Provides a unified schedule, unified setpoints, unified alerts**
- **Communicates via:** Modbus (reliable, long-established), BACnet (commercial standard), or MQTT / API (home automation ecosystem)

**Level 3 — Home automation layer:**
- **Home Assistant server** (or equivalent) as the owner-facing interface
- **Shows:** room-by-room temperature, humidity, setpoint, current call status, historical trends
- **Allows:** remote adjustment of setpoints, schedule changes, scene-based control ("vacation mode," "night mode")
- **Alerts:** equipment faults, filter change reminders, anomalies (zone not reaching setpoint, unusual runtime, etc.)
- **Integration:** ties HVAC with lighting, security, audio, etc. — see Section 10

**Sensors:**
- **Every room:** temperature + humidity + optional occupancy
- **Every manifold:** supply temp, return temp, flow rate per zone
- **Heat pump:** entering water temp, leaving water temp, power consumption, runtime
- **ERV:** outdoor air temp, incoming air temp (post-recovery), exhaust temp, fan speed
- **Dehumidifier:** inlet RH, outlet RH, runtime
- **Domestic hot water:** tank temp, recirculation temp

**Data logging:**
- **All sensor data logged at 1–5 minute intervals** by the home automation system
- **Storage:** local NAS or dedicated logging server (see Section 10)
- **Retention:** 5+ years of data — useful for trend analysis, fault detection, and system tuning
- **Backup:** daily off-site backup of the database

**Alarming:**
- **Critical faults:** immediate notification (phone, email) — no heat in winter, no cool in summer, water leak, CO detected
- **Warning faults:** daily summary — filter due, zone not reaching setpoint, anomalous runtime
- **Informational:** monthly report of energy use, comfort stats, equipment runtime

**Local-first philosophy:**
- **All controls work without internet** — the home automation hub runs locally, the equipment controllers are local, the thermostats are wired
- **Remote access (phone app when away) goes through a VPN** to the local system, not through a manufacturer's cloud
- **No component is rendered useless by a manufacturer going out of business**
- See Section 10 for the full smart home philosophy

**Key code references:**
- OMSC Chapter 3 (general regulations — applies to controls)
- Not specifically regulated — controls are a design and quality choice

---

## 8.14 Commissioning and Performance Testing

**Plain language:** When the HVAC system is first turned on, it needs to be set up and tested room-by-room. Every zone gets balanced so it delivers the right amount of heat. The ERV's airflows get measured to make sure each room gets the right ventilation. The dehumidifier is calibrated. This is called commissioning, and it's the difference between "the system works" and "the system works well."

**Technical detail:** Commissioning procedure:

**Phase 1 — Pre-operation checks:**
- **Hydronic system filled and pressure-tested** — 100 psi for 24 hours, no pressure loss
- **Air purged from all loops** — bleed at each manifold, at the ERV heat exchanger, at the heat pump
- **All zone valves manually cycled** — verify operation and no sticking
- **All thermostats paired** with the manifold controller — verify signal reception
- **Ductwork verified** — visual inspection of every joint, seal check
- **Electrical verified** — every breaker labeled, continuity check on control wiring

**Phase 2 — Hydronic balancing:**
- **Primary pump commissioned** — flow rate measured, pressure differential across the heat pump verified
- **Each zone balanced** — flow meter on the manifold set to design CFM per loop (example: 0.6 gpm per 100 sqft of heated floor at design delta-T of 10°F)
- **System run in "balancing mode"** with all zones calling for heat — adjust balancing valves until all zones reach setpoint within 30 minutes of startup
- **Document flow rates** for each zone in the system manual

**Phase 3 — Ventilation balancing:**
- **Measure airflow at every supply and exhaust register** using an airflow hood (borrowed, rented, or contractor's)
- **Compare to design CFM** for each register
- **Adjust branch dampers** until every register is within ±10% of design
- **Verify whole-house rate:** total supply CFM = total exhaust CFM (balanced) ± 5%
- **Document airflows** in the system manual

**Phase 4 — Control verification:**
- **Simulate each zone thermostat calling** — verify the correct zone valve opens and the pump runs
- **Simulate each bathroom exhaust switch** — verify the ERV boosts
- **Simulate range hood operation** — verify make-up air damper opens
- **Simulate dehumidifier call** — verify correct operation
- **Verify automation integration** — room setpoints display correctly, remote adjustment works, alerts fire on simulated faults

**Phase 5 — Performance verification over seasons:**
- **First winter:** measure actual heating performance — energy consumed, room temperatures achieved, heat pump COP
- **First summer:** measure actual cooling performance — dew point stability, floor surface temps, dehumidifier runtime
- **First shoulder season:** verify changeover between heating and cooling, ventilation-only mode works, humidity control is smooth
- **Annual review:** re-balance if anything has drifted; check heat pump refrigerant charge; clean ERV core; inspect all manifold connections

**Commissioning documentation:**
- **"As-built" system schematic** — updated from design documents to reflect actual routing, component locations, and control wiring
- **Zone balance table** — design flow rate, as-built flow rate, difference, re-balanced date
- **Airflow balance table** — design CFM, as-built CFM, difference, re-balanced date
- **Sensor calibration records** — temperature, humidity, flow sensors, verified against reference instrument

**Performance targets (post-commissioning):**
- **Heating: ≤20 min from 5°F below setpoint to setpoint** in any zone at design outdoor conditions
- **Cooling: ≤30 min from 5°F above setpoint to setpoint** in any zone
- **Ventilation: continuous flow within ±10% of design CFM at every register**
- **Humidity: 35–55% RH year-round in all occupied rooms**
- **Heat pump COP: ≥3.5 in heating, ≥15 EER in cooling, annualized**
- **Ventilation heat recovery: ≥85% sensible, ≥60% latent**

**Key code references:**
- OMSC 304 (installation — general)
- ASHRAE Guideline 0 (the commissioning process)
- ACCA Quality Installation standards

---

*End of Section 8 — HVAC and Air*
