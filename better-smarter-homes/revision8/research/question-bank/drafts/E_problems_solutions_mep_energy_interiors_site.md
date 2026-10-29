# Draft E — Research Questions: Real-World Problems, Solutions, and Creative Options for MEP, Energy, Interiors, and Site (Wave 3)

**Merge note.** This is one draft in the Wave-3 question drive. It covers the systems-and-living half of the build — plumbing (supply/pressure/treatment/hot water, DWV/well/septic), electrical (service/grounding/branch circuits/load), HVAC (heat pumps, radiant, ventilation, humidity, air quality), solar/battery/backup/off-grid, smart-home/network, interiors/finishes, and site/logistics/owner-builder health and safety. It follows the house format of `../research_questions_revision7.md` (numbered item, bold lead-in, `Lands in:` target). On merge into `../research_questions_revision7.md`: (1) items are numbered **E1–E68** so they will not collide with the main file's 1–22 and can be renumbered in place; (2) **dedupe against the main file's Section B (items 13–17, solar/ch15)** — the solar/battery block here (E40–E47) is deliberately problem-solution/creative-option focused and complements, rather than repeats, those code/permit items; also dedupe against the two answered waves before researching; (3) per the owner's mandate this draft is heavy on **[PROBLEM-SOLUTION]** and **[CREATIVE-IDEA]**, grounded in worldwide owner-builder / off-grid / professional experience, not just code. **`Leads:` lines are directional veins found in light forum/source scanning — starting points to verify, NOT verified facts or book claims.** No manuscript prose here.

Project frame assumed throughout: long-life all-electric concrete home, rural Oregon, radiant heat + heat pump, solar + battery, local-first smart home, well + septic, water-independence goal, mostly-solo owner-builder.

---

## E-1. Plumbing — Water Supply, Pressure, and Treatment

**E1. Pressure-tank short-cycling and waterlogging — the bladder-failure story.** What actually causes a well pressure tank to short-cycle (waterlogged/ruptured bladder, wrong air precharge, oversized pump), how to size drawdown and set precharge for a chosen cut-in/cut-out (e.g. 30/50 vs 40/60), and why iron/manganese sediment and chlorine shorten bladder life. Include the field diagnosis and the owner-replaceable fix.
Lands in: Plumbing Water Supply — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS] [COST]
Leads: midatlanticwater / freshwatersystems — Schrader-valve spray test confirms ruptured bladder; drain-and-recharge only buys 3–12 months; iron/Cl embrittles the bladder; precharge should sit ~2 psi below cut-in.

**E2. Constant-pressure / variable-speed (VFD) pumping as the creative alternative.** For steady whole-house pressure and far fewer cycles, when does a soft-start VFD constant-pressure submersible beat a conventional tank? Weigh pump-life/comfort gains against the off-grid downsides (continuous electronics draw, surge/lightning vulnerability, higher cost, harder rural repair).
Lands in: Plumbing Water Supply — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [COST]

**E3. Well-water treatment train — getting the ORDER right.** For the common rural-Oregon cocktail (iron, manganese, iron bacteria, hardness, low pH, tannins, occasional coliform), what is the correct sequence of stages and why does order control success (sediment → oxidation/iron filter → softener → carbon → UV; UV always last; softener before any RO)? What does a water test have to measure before you can design it?
Lands in: Plumbing Water Supply — [METHOD] [MATERIALS/INGREDIENTS] [PROBLEM-SOLUTION]
Leads: SpringWell / worldwaterreserve — UV must see already-clear water to work; iron/hardness must come out upstream or they foul the softener and shadow the UV lamp.

**E4. Iron/sulfur bacteria and biofilm — the recurring slime-and-smell problem.** Why shock chlorination keeps failing to hold, and what a durable solution looks like: continuous chlorine or hydrogen-peroxide injection with a contact/retention tank ahead of the pressure tank, plus filtration. Are there off-grid-friendlier (low-power, non-chemical) routes?
Lands in: Plumbing Water Supply — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]
Leads: worldwaterreserve / SpringWell — shock kills but bacteria recolonize; H2O2 or Cl injection + retention tank + iron filter + UV is the "solved" pattern people land on.

**E5. Aggressive (low-pH, soft) water eating copper — pinhole leaks and blue-green stains.** Diagnose acidic well or rainwater, compare the calcite/acid-neutralizer tank vs soda-ash injection, and confirm this is the argument for running the whole house in PEX rather than copper.
Lands in: Plumbing Water Supply — [PROBLEM-SOLUTION] [MATERIALS/INGREDIENTS] [METHOD]
Leads: rainwater sources (WRAP / NTO) flag low-pH rain corroding thin copper — same neutralizer fix applies to soft well water; PEX sidesteps it entirely.

**E6. Whole-house pressure design: PRV, thermal expansion, and water hammer.** Setting incoming pressure, when a closed system (check valve / PRV / backflow) forces a thermal-expansion tank on the water heater, and where water-hammer arrestors belong (washer, dishwasher, fast-closing solenoid valves).
Lands in: Plumbing Water Supply — [CODE] [METHOD] [PROBLEM-SOLUTION]

**E7. Freeze protection for the well head, pressure tank, and exposed lines.** Pitless-adapter/burial depth below frost, insulated pump house vs heat-tape vs self-draining layout, and how off-grid changes the math (heat tape is a nasty winter phantom load on the battery).
Lands in: Plumbing Water Supply — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]

**E8. Home-run (manifold) PEX vs trunk-and-branch.** A solo builder's case for a central labeled manifold: individual shutoffs, no buried in-wall fittings, easy troubleshooting — versus more pipe volume, longer wait-for-hot on long runs, and cost. When is each right?
Lands in: Plumbing Water Supply — [CREATIVE-IDEA] [METHOD] [COST]

## E-2. Plumbing — Hot Water

**E9. Heat-pump water heater placement — it cools and dries the room it stands in.** Where does an HPWH go in an all-electric concrete house so it isn't strangled by a cold winter garage? Cover ducting options, condensate routing, noise, minimum room volume, the split (compressor-outside) variant, and turning its cool dry exhaust into summer dehumidification.
Lands in: Plumbing Hot Water — [PROBLEM-SOLUTION] [CREATIVE-IDEA] [METHOD]
Leads: ENERGY STAR / attainablehome — drops to resistance below ~37–40°F; wants ~700–1000 ft³ or ducting; split HPWH puts the noisy/cooling compressor outdoors, the cold-climate creative fix.

**E10. Sizing an HPWH and soaking midday solar — the "hot-water battery."** First-hour rating vs recovery for the household, and running the tank on a timer/relay to consume midday PV so hot water becomes cheap stored energy.
Lands in: Plumbing Hot Water — [CREATIVE-IDEA] [METHOD] [COST]

**E11. Long hot-water waits and wasted water in a spread-out house.** Demand-controlled recirculation (button/motion-triggered, not a continuous loop that bleeds standby heat), structured-plumbing pipe sizing, and point-of-use boosters for far fixtures.
Lands in: Plumbing Hot Water — [PROBLEM-SOLUTION] [CREATIVE-IDEA] [METHOD]

**E12. One heat source for both domestic hot water and radiant floors — combi vs separate.** Legionella and scald/mixing-valve issues when storage runs low for radiant, buffer-tank strategy, and the open-loop (potable water through the floor) vs closed-loop code limits.
Lands in: Plumbing Hot Water / HVAC — [PROBLEM-SOLUTION] [CODE] [METHOD]

## E-3. Plumbing — DWV, Well, and Septic

**E13. Septic drainfield premature failure — the biomat / solids-carryover problem.** The dominant real-world failure chain (skipped pumping → solids/grease reach the field → biomat clogs the soil) and the prevention stack: effluent filter and its cleaning, pump interval, keeping vehicles/roots/compaction off the field, and what never goes down the drain.
Lands in: Plumbing Well and Septic — [PROBLEM-SOLUTION] [METHOD] [CODE]
Leads: NCSU Extension / WA-DOH / inspectapedia — #1 cause is not pumping on schedule; effluent filter (required on post-1999 permits) must be cleaned at pump-out or it chokes flow.

**E14. Septic type selection on a hard site (Oregon DEQ terms).** For high water table / shallow or slow-perc soil, walk the ladder: conventional gravity vs pressure-distribution vs sand filter vs ATU vs mound/capping fill — with siting, required reserve/replacement area, and the cost climb. What does the site/perc evaluation decide?
Lands in: Plumbing Well and Septic / Land Site and Feasibility — [PROBLEM-SOLUTION] [COST] [CODE]
Leads: Oregon DEQ onsite/subsurface wastewater program — soil and perc evaluation gates the whole feasibility question; reserve area is mandatory.

**E15. Creative wastewater load-cutters — graywater reuse and composting toilets, what Oregon allows.** Oregon's graywater reuse permit tiers, whether an indoor composting toilet is accepted, and how each reduces septic load and extends field life on a marginal site.
Lands in: Plumbing Well and Septic — [CREATIVE-IDEA] [CODE] [PROBLEM-SOLUTION]
Leads: Oregon DEQ graywater reuse permit program exists (roof/interior sources by tier) — verify current rules and whether composting toilets change the required septic sizing.

**E16. DWV venting you can't redo later in a masonry/concrete house.** Wet venting, island/loop vents for a kitchen island, air-admittance valves where OPSC permits them, and a slab-embedded drain layout that has to be right the first time.
Lands in: Plumbing DWV — [PROBLEM-SOLUTION] [METHOD] [CODE]

**E17. Under-slab DWV — get it perfect before the pour.** Trench and slope layout, sleeving through the slab, pressure/test-ball testing the buried system before concrete, protecting stub-ups, and sealing every slab penetration for both radon and water.
Lands in: Plumbing DWV / Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [METHOD] [TOOLS]

**E18. Well siting and yield — the independence question at the source.** Interpreting a drawdown/yield test, OWRD exempt-groundwater limits, required separations from septic/property lines/contamination sources, and the low-yield-well fix (large storage cistern + booster pump buffering a trickle well).
Lands in: Land Site and Feasibility / Plumbing Water Supply — [PROBLEM-SOLUTION] [CODE] [CREATIVE-IDEA]
Leads: OWRD exempt-use groundwater framework; low-yield homesteads commonly solve gpm shortfalls with a cistern buffer feeding a pressure pump.

## E-4. Electrical — Service, Panels, and Grounding

**E19. Concrete-encased electrode (Ufer) — the vapor-barrier trap.** Why rebar in a slab poured over poly cannot count as the CEE (broken earth contact), how to use the footing instead, the exact stub-up/connection detail cast before the pour, and the fallback when the whole foundation sits on foam/vapor barrier.
Lands in: Electrical Grounding — [PROBLEM-SOLUTION] [CODE] [METHOD]
Leads: ExpertCE / Texas-inspector — needs ≥20 ft of ½" rebar or bare #4 Cu, ≥2" cover, in direct earth contact; slab-on-poly disqualifies the slab, so the CEE goes in the footing and must be planned pre-pour.

**E20. Grounding, bonding, and surge protection for a steel-and-electronics house.** Foundation electrode + supplemental electrodes, bonding of any gas/CSST and metallic water, DC grounding for the solar/battery, and whole-house SPD at the panel to protect the well pump and electronics from rural lightning and utility surges.
Lands in: Electrical Grounding — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]

**E21. Service and panel sizing for an all-electric load.** Running an NEC-220 load calc for heat pump + HPWH + induction range + EV + well pump, why 200 A often ends up tight, and the fixes: load-management/EVEMS to dodge a service upgrade, or a 320 A meter-main. What margin should a long-life house design in?
Lands in: Electrical Service — [PROBLEM-SOLUTION] [METHOD] [CODE] [COST]

**E22. Where solar/battery ties in — main vs sub-panel and the busbar rule.** Line-side (supply-side) tap vs load-side breaker, the 120% busbar interconnection limit, whole-home backup vs a protected/critical-loads sub-panel, and provisioning spare panel space now.
Lands in: Electrical Service / Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [CODE] [CREATIVE-IDEA]

**E23. Conduit and box provisioning in poured/masonry walls — the "add a circuit later" is brutal here.** Chases and embedded conduit runs, extra home runs, empty spare conduits to key locations, and the veteran concrete-home "wish I'd run one more" list captured before concrete goes up.
Lands in: Electrical Branch Circuits / Build Sequence and Site Coordination — [CREATIVE-IDEA] [METHOD] [PROBLEM-SOLUTION]

**E24. Backup interconnection safety — transfer switch, interlock, and the backfeed hazard.** Manual transfer switch vs listed interlock kit vs whole-home ATS, why a "suicide cord" kills, and how a battery-inverter with a microgrid interconnect device changes the whole wiring picture.
Lands in: Electrical Service / Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [CODE] [METHOD]

## E-5. Electrical — Branch Circuits and Load

**E25. AFCI/GFCI nuisance tripping — the modern all-electric-house headache.** The shared-neutral (multiwire branch circuit) trap on single-pole AFCIs, dual-function-breaker interactions with LED drivers/motors/electronics, and design moves that prevent it (avoid shared neutrals, home-run circuits, verify breaker-brand compatibility).
Lands in: Electrical Branch Circuits — [PROBLEM-SOLUTION] [METHOD] [CODE]
Leads: viox / Leviton / StructureTech — MWBC sharing a neutral trips single-pole AFCIs; fix is a 2-pole AFCI or dedicated neutrals; isolate offending electronic loads to diagnose.

**E26. Circuit planning for a battery/off-grid house — critical vs non-critical loads.** Which circuits ride the backed-up sub-panel, dedicated dedicated circuits for well pump / HPWH / heat pump, and a phantom-load audit (heat tape, well controls, HRV, hub) so the battery isn't drained by trivia.
Lands in: Electrical Branch Circuits / Solar Battery and Energy Independence — [CREATIVE-IDEA] [METHOD] [PROBLEM-SOLUTION]

**E27. EV charging — rough it in cheap now or pay dearly later.** A stubbed 240 V run vs full circuit, load-managed charging that fits the existing service, and whether to size for two vehicles and future vehicle-to-home (V2H) using the car as a backup battery.
Lands in: Electrical Branch Circuits — [CREATIVE-IDEA] [COST] [METHOD]

**E28. Lighting without an electrician-later regret — neutrals, dimming, and DC.** Why smart switches need a neutral at every box, dimmer/LED compatibility, and the synergy of low-voltage/DC lighting in a battery house (no inverter losses, native dimming).
Lands in: Electrical Branch Circuits / Smart Home — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [METHOD]

## E-6. HVAC — Heat Pumps and Radiant Floors

**E29. Radiant-slab thermal lag and overheating in a superinsulated concrete house.** Why a high-mass slab overshoots on a sunny afternoon (slow response + passive-solar gain), and the control answer: outdoor-reset, slab sensors, anticipatory/weather-compensated logic — plus the low-mass (thin-slab / staple-up) alternative for responsiveness.
Lands in: HVAC — [PROBLEM-SOLUTION] [METHOD] [CREATIVE-IDEA]
Leads: Concrete Network / GBA / Barron Heating — high-mass slabs overheat with any extra gain unless outdoor-reset + anticipatory control; a very well-insulated house may over-deliver from the slab lag alone.

**E30. Air-to-water heat pump driving the radiant floor — cold-climate reality.** Buffer-tank sizing to stop short-cycling, glycol vs water and freeze protection, defrost behavior on a hydronic system, and which cold-climate ATW units actually exist for this house.
Lands in: HVAC — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]

**E31. Defrost cycles and backup-heat behavior on an air-source heat pump.** The 25–35°F frost "Goldilocks zone," how resistance strips fire during defrost (and can spike an off-grid load), and why radiant thermal mass rides through a defrost dip better than forced air.
Lands in: HVAC — [PROBLEM-SOLUTION] [METHOD]
Leads: Lennox / GBA — frost is worst 25–35°F, defrost checks every 30–90 min and lasts 5–15 min; strips energize during defrost; slab mass buffers the temporary loss.

**E32. Does a superinsulated concrete box even need radiant?** Steelman the "one or two minisplits heat the whole house" argument against radiant comfort, the hybrid middle path (small radiant zone + ductless), and an honest cost/complexity comparison for an owner-builder.
Lands in: HVAC — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [COST]

**E33. Cooling and dehumidification in a radiant-heated house — radiant can't cool safely.** Adding ductless/ducted heat-pump cooling, the condensation risk if you try to chill a slab below dew point, and whether a standalone whole-house dehumidifier is needed in humid PNW shoulder seasons.
Lands in: HVAC — [PROBLEM-SOLUTION] [METHOD]

**E34. Zoning a high-thermal-mass house — when zoning fights the mass.** Why aggressive multi-zone control struggles against a slab that changes slowly, a realistic zone count, actuator/manifold reliability, and near-single-setpoint steady-state operation as the low-tech creative answer.
Lands in: HVAC — [CREATIVE-IDEA] [METHOD] [PROBLEM-SOLUTION]

## E-7. HVAC — Ventilation, Humidity, and Air Quality

**E35. HRV vs ERV for a tight house in marine/mixed Oregon.** The moisture-balance argument (ERV smooths winter dryness and summer humidity), core-frost control in cold weather, and the condensate drain/trap requirement. Which is the defensible default here and why?
Lands in: HVAC Ventilation — [PROBLEM-SOLUTION] [METHOD] [CREATIVE-IDEA]
Leads: GBA / Energy Vanguard — "you probably want an ERV"; PNW air feels damp but is drier than indoor air in absolute terms; frost defrost on the ERV core is the counter-consideration.

**E36. Balanced-ventilation ducting and commissioning — the part people skip.** Dedicated HRV/ERV ducting vs sharing the heat-pump air handler, balancing supply and exhaust airflow, filter (MERV) pressure-drop penalty, and actually measuring delivered CFM vs nameplate.
Lands in: HVAC Ventilation — [PROBLEM-SOLUTION] [METHOD] [TOOLS]

**E37. Construction moisture and year-one humidity in a concrete house.** Curing concrete/masonry dumps a lot of water into the building; how to dehumidify during construction, protect finishes, and know when the slab is dry enough to install flooring.
Lands in: HVAC Ventilation / Interiors — [PROBLEM-SOLUTION] [METHOD]

**E38. Kitchen range ventilation in a tight all-electric house.** Make-up-air requirement thresholds for a powerful hood, how induction lowers the exhaust need, and the tight-house depressurization risk (helped by having zero combustion appliances).
Lands in: HVAC Ventilation — [PROBLEM-SOLUTION] [CODE] [METHOD]

**E39. Wildfire smoke and rural air quality — a "clean-room" strategy.** High-MERV/HEPA on the ventilation intake, a recirculation/smoke mode that seals the tight envelope, PM/CO2 monitoring, and how the tight concrete envelope becomes a refuge during smoke events.
Lands in: HVAC Ventilation / Smart Home — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [METHOD]

## E-8. Solar, Battery, Backup, and Off-grid

**E40. Off-grid vs grid-tied-with-battery vs hybrid — the honest independence/cost trade.** Sizing to Oregon's worst-month winter sun, autonomy-days vs generator reliance, and why "full off-grid" frequently pencils worse than a grid-tied hybrid. Collect real owner regret/success stories.
Lands in: Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [COST] [CREATIVE-IDEA]
(Complements main-file item 16; go deeper on lived failure/success cases, not just the code path.)

**E41. Battery-sizing mistakes and the cold-charging trap.** Nameplate vs usable kWh and DoD derating, LiFePO4's low-temperature charge cutoff (lithium plating below freezing), and locating/insulating/self-heating the pack so winter doesn't cripple it.
Lands in: Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]
Leads: Victron community / Bioenno — no charging below 0°C without damage; heated cells or an insulated warmed enclosure, and an MPPT temperature-sensor cutoff, are the standard defenses.

**E42. Generator auto-start integration and fuel choice for rural resilience.** Two-wire AGS vs comms-based start, propane vs diesel vs gasoline for storage and cold-start, sizing (~2× inverter continuous so it can charge while carrying loads), and open- vs closed-transition switching.
Lands in: Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [METHOD] [COST]
Leads: DIY Solar Forum / Unbound Solar — inverter signals a 2-wire generator at low SoC; propane derates ~10–15%; size the generator ~2× inverter output.

**E43. Interconnection and Permission-to-Operate delays — the hidden schedule-killer.** How PTO can trail final inspection by weeks-to-months, how to legally run the house on solar+battery before PTO, and the commissioning-documentation pitfalls that specifically strand self-installed systems.
Lands in: Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [CODE] [COST]
Leads: GreenLancer / Energyscape — interconnection, not construction, is often the critical path; self-installs stall on missing commissioning/inspection docs.

**E44. Roof vs ground-mount vs pole/tracker on a rural concrete house.** Ground-mount wins for cleaning, snow shedding, wiring, and no roof penetrations; pole-mount friendliness for a solo builder; and whether to deliberately use the reinforced concrete roof deck.
Lands in: Solar Battery and Energy Independence — [CREATIVE-IDEA] [COST] [METHOD]

**E45. DC-coupled vs AC-coupled, and all-in-one vs component stack.** Architecture trade-offs, expandability, and single-point-of-failure vs redundancy for an owner who values independence and field-repairability over elegance.
Lands in: Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [CREATIVE-IDEA] [METHOD]

**E46. Load-shifting instead of oversizing — the cheapest lever.** Time-shifting HPWH, EV, well-pump, and laundry into the solar window with smart controllers, and quantifying how much battery/array that avoids buying.
Lands in: Solar Battery and Energy Independence / Smart Home — [CREATIVE-IDEA] [METHOD] [COST]

**E47. Rapid shutdown, PV arc-fault, and fire-service access.** What module-level rapid shutdown (NEC 690.12) and PV arc-fault detection require, how they interact with an off-grid battery system, and what the local AHJ and fire code expect for labeling/access.
Lands in: Solar Battery and Energy Independence — [CODE] [PROBLEM-SOLUTION]

## E-9. Smart Home and Network

**E48. Local-first vs cloud — surviving vendor sunset and internet outages.** Choosing Zigbee / Z-Wave / Matter-over-Thread on a local hub (e.g. Home Assistant) so devices keep working when a company bricks its cloud or paywalls its API; the "you leased it, you didn't own it" failure mode and how to avoid e-waste.
Lands in: Smart Home — [PROBLEM-SOLUTION] [CREATIVE-IDEA] [METHOD]
Leads: XDA / Vucense — cloud-dependent devices die on backend shutdown; a local hub keeps automation on-site with sub-10ms latency and full function during outages.

**E49. RF goes to die in rebar and masonry — mesh reliability in a concrete house.** How concrete/CMU/rebar attenuate 2.4 GHz Zigbee/Thread and Z-Wave, and the design answer: a wired backbone, repeaters/routers placed with intent, and conduit/access points planned during the pour.
Lands in: Smart Home — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]
Leads: reinforced concrete heavily attenuates 2.4 GHz mesh — practitioners lean on wired Ethernet backbones plus mains-powered repeaters and pre-planned in-wall conduit.

**E50. Structured cabling you cannot add later.** Cat6/fiber home runs, PoE for cameras/APs/sensors, a real network rack/closet, and empty conduit to key rooms, the attic, and the roof (solar, antenna) before walls close.
Lands in: Smart Home / Electrical Branch Circuits — [CREATIVE-IDEA] [METHOD] [TOOLS]

**E51. Smart-home security and network segmentation.** An isolated IoT VLAN, keeping cameras and logic local, firmware/update discipline, and why an independence-minded owner avoids always-listening cloud microphones.
Lands in: Smart Home — [PROBLEM-SOLUTION] [METHOD]

**E52. Graceful degradation — the house must still work when the "brains" are down.** Backing the hub/network/well controls on the battery/UPS, and designing physical manual overrides (real switches, manual valves) so a dead server never means a dead house.
Lands in: Smart Home / Solar Battery and Energy Independence — [PROBLEM-SOLUTION] [CREATIVE-IDEA] [METHOD]

**E53. Monitoring as preventive maintenance.** Leak sensors with an automatic whole-house shutoff valve, well/cistern level, freeze alarms in the pump house, battery/inverter telemetry, and a septic high-level alarm — the sensor set that turns disasters into notifications.
Lands in: Smart Home — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [METHOD]

## E-10. Interiors and Finishes

**E54. Flooring over a slab — moisture-vapor-emission failures.** Why glue-down and rubber-backed floors blister and delaminate over concrete, the RH-probe / MVER testing that must precede installation, the under-slab vapor retarder as the real prevention, and topical moisture-mitigation coatings as the retrofit.
Lands in: Interiors — [PROBLEM-SOLUTION] [MATERIALS/INGREDIENTS] [METHOD]
Leads: CTLGroup / Xtreme Polishing — slab RH above ~80% or MVER above ~3 lb/1000 ft²/24 h delaminates adhesives/coatings; rubber backing re-emulsifies the glue; test before you install.

**E55. Polished/stained concrete as the finished floor — the mass-friendly creative option.** Crack control (saw-cut joint timing/spacing), stain/dye and sealing/maintenance, comfort and hardness underfoot, and coordinating grind/polish depth with embedded radiant tubing.
Lands in: Interiors — [CREATIVE-IDEA] [MATERIALS/INGREDIENTS] [METHOD] [COST]

**E56. Curbless / wet-room showers with a slab — waterproofing failure points.** Why tile and grout are not the waterproofing, pre-slope plus bonded/sheet membrane vs surface tile, single-plane linear-drain slope, the bonding-flange drain connection, and recessing the slab for a flush entry — decided before the pour.
Lands in: Interiors / Plumbing DWV — [PROBLEM-SOLUTION] [METHOD] [MATERIALS/INGREDIENTS]
Leads: Austin Tile Pro / craftingwithconcrete — leaks come from un-detailed seams/corners/drain and missing pre-slope; ¼"/ft minimum slope, membrane with a bonding-flange drain, slab recessed pre-pour.

**E57. Radon-resistant new construction — build the passive stack now, add a fan only if a test says so.** Sub-slab clean aggregate + gas-tight membrane + a 3"+ vent riser cast into the slab, sealed penetrations, Oregon's high-radon-area guidance, and the "test after occupancy, then activate" logic.
Lands in: Interiors / Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [CODE] [METHOD] [MATERIALS/INGREDIENTS]
Leads: Oregon OHA Appendix F / W.R. Meadows — 4" clean aggregate, ≥3" ABS/PVC riser teed into the sub-slab, all penetrations sealed; passive first, wired/roughed so a fan can be added.

**E58. Low-VOC / healthy materials for a tight envelope.** Off-gassing risk in a low-air-change house, choosing paints/adhesives/sealants/cabinetry (formaldehyde) accordingly, flush-out/bake-out procedures, and materials that age gracefully over a long-life build.
Lands in: Interiors / HVAC Ventilation — [PROBLEM-SOLUTION] [MATERIALS/INGREDIENTS] [CREATIVE-IDEA]

**E59. Interior condensation and thermal-bridge mold on concrete/masonry.** Where the dew point lands in the wall assembly, the vapor profile the interior finish needs, and the cold spots (window reveals, slab edge, ties) that grow mold if the detail is wrong.
Lands in: Interiors — [PROBLEM-SOLUTION] [METHOD]
(Cross-ref the wall-system chapter for the assembly's vapor/thermal design.)

**E60. Hanging things and building in on concrete/CMU walls.** Fastening into concrete/masonry (mechanical/adhesive anchors, and embeds/blocking planned before the pour), plus designing cabinetry, TVs, and storage for walls you can't just drive a screw into.
Lands in: Interiors — [CREATIVE-IDEA] [TOOLS] [METHOD]

## E-11. Site, Logistics, and Owner-Builder Health/Safety

**E61. The driveway and site access that quietly break the budget.** Grade, culvert, and drainage; base-rock depth to carry concrete and pump trucks; fire-apparatus turnaround/access; and why the durable driveway usually gets built first.
Lands in: Land Site and Feasibility / Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [COST] [METHOD]

**E62. Utility trenching and coordination — one trench, many services.** Shared vs separate trenches for power/water/data/septic, required separations and burial depths, sleeving for future pulls, and locating everything precisely before the slab locks it in.
Lands in: Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [CODE] [METHOD]

**E63. Water independence as layered redundancy — well + rainwater + storage.** Legality of potable roof-rainwater in Oregon, cistern sizing for dry-season autonomy, the first-flush + multi-stage filtration + UV train, low-pH corrosion control, and cross-connection/backflow rules when mixing well and rain sources.
Lands in: Land Site and Feasibility / Plumbing Water Supply — [CREATIVE-IDEA] [PROBLEM-SOLUTION] [CODE]
Leads: permies / AZ1863 / NTO Tank — first-flush + cartridge stages + UV for potable; low-pH rain corrodes copper (neutralize); design sources so they can't cross-connect; Oregon permits roof-collected rainwater.

**E64. Solo-builder sequencing and the "which trades to hire out" decision.** Sequencing a one-person build around pours (all-hands, time-critical, weather-critical), inspection hold points, and where hiring out is non-negotiable (concrete pump crew, service tie-in, septic install, crane picks).
Lands in: Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [METHOD] [COST]

**E65. Solo lifting and material handling — protecting the body over a multi-year build.** The realistic solo-lift ceiling, mechanical aids (cart/dolly, engine hoist/gantry, panel/vacuum lifter, genie material lift), planning material drops to the point of use, and the truth that one injury stalls a solo project.
Lands in: Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [TOOLS] [METHOD]
Leads: NIOSH / Oregon OSHA — overexertion is ~30% of construction musculoskeletal injuries; guidance caps solo lifts around 35–50 lb; carts, hoists, and kneeling creepers are the standard aids.

**E66. Working alone on a rural site — the fall/entrapment/no-one-coming problem.** Check-in systems and lone-worker devices, tasks never to do solo (roof edges, unshored trenches, energized/live work), trench cave-in and ladder rules, and a first-aid/comms plan when help is far away.
Lands in: Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [METHOD] [TOOLS]

**E67. Tools worth owning vs renting for a concrete-heavy solo build.** The high-payback buy list (rotary hammer, laser level/transit, mixer, plate compactor, quality PPE) vs the rent-only list (concrete pump, excavator, boom/scissor lift), and a tool strategy that amortizes over a long build.
Lands in: Build Sequence and Site Coordination — [CREATIVE-IDEA] [TOOLS] [COST]

**E68. Temporary power, water, and shelter to build from.** Temporary utility service vs jobsite generator, jobsite water before the well is in, secure on-site material/tool storage, and a weather/staging plan for pours in Oregon's wet season.
Lands in: Build Sequence and Site Coordination — [PROBLEM-SOLUTION] [METHOD]

---

*End of Draft E. Item count: 68 (E1–E68). Predominant tags: [PROBLEM-SOLUTION] and [CREATIVE-IDEA], as mandated. `Leads:` lines are unverified veins to chase, not book claims.*
