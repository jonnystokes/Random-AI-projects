File: `I_designing_for_centuries_durability.md`

# Wave 3 Pre-Research: Designing For Centuries, Durability Engineering

Agent I. Area: the mechanisms behind the thousand-year structural-shell goal, currently implicit in the manuscript. This file is pre-research only: gathered understanding plus a candidate question bank. It does not answer the questions and does not draft manuscript text.

Manuscript chapters read first: Structural System And Concrete Design (existing section 6.13, Concrete Durability And Mix Discipline, already covers ACI 318 exposure classes F/S/W/C, a mix-design parameter table, and sourced Code citations to ACI 318 Chapter 19, ACI 305R/306R/308R, and the ASTM material and test standards; section 6.7, Wall Ties, already specifies stainless tie material and flags galvanic corrosion between mixed metals; section 6.8 states cover values), Foundation, Basement, Slabs, And Concrete Placement (section 7.11 covers dampproofing versus waterproofing and a recommended long-life waterproofing assembly; section 7.17 covers consolidation, finishing, and curing durations), Envelope, Waterproofing, Thermal Performance, And Radon (section 8.6 covers slab-edge and below-grade wall assemblies; section 8.7 covers the protected-membrane roof, parapets, and penetrations), Materials, Suppliers, Procurement, And Substitution (section 16.3-16.4), and Documentation, Maintenance, And Future Upgrades (section 20.6 states concrete footings and foundations have no replacement horizon "if properly built" but does not define what condition monitoring watches for over a multi-century span).

This pre-research goes past what those sections already state: the deterioration mechanisms themselves, the wider menu of corrosion-resistant reinforcement, cathodic protection and inhibitors, self-healing and crystalline chemistry, ancient and vernacular durability precedent, detailing failure modes, service-life modeling, and a century-scale inspection regime, none of which the existing chapters currently cover. Sibling draft D asks one broad question (its Q18) naming the deterioration mechanisms; this file treats each mechanism, and each mitigation category, as its own researched subtopic.

---

## PART 1: GATHERED UNDERSTANDING

### 1. The Durability Framework

ACI 201.2R ("Guide to Durable Concrete," current edition ACI PRC-201.2-23) is the main US reference guide organizing concrete durability around mass transport (how water, ions, and gas move through concrete) and then treats each deterioration mode in its own chapter: freezing and thawing, alkali-aggregate reaction, sulfate attack, other chemical attack, physical salt attack, corrosion of embedded metals, and abrasion. ACI 318 Chapter 19 sets the exposure-class system (categories F, S, W, C) the existing manuscript section already uses, with minimum w/cm, minimum f'c, air content, and cementitious-material limits tied to each class.

ACI 318's exposure classes do not include an explicit multi-century "design working life" dial. By contrast, the UK/European system (BS EN 1992 "Eurocode 2" paired with BS 8500) names design working life categories directly (commonly cited as 10, 25, 50, and 100 years) and ties the required "structural class," which sets nominal cover, to whichever category is chosen: moving from a 50-year to a 100-year design life is a defined adjustment (more cover, higher concrete strength class, or both), not an open engineering judgment call. Even this system's longest named category, 100 years, is two orders of magnitude short of this project's stated thousand-year goal. No mainstream code, US or international, defines a thousand-year design-life category or a deemed-to-satisfy table for one.

The international fib Model Code 2010 (the CEB-FIP successor body) offers a full or semi-probabilistic durability design methodology as an alternative to fixed tables: a designer models the actual deterioration mechanism (chloride diffusion, carbonation depth) with its statistical uncertainty and solves for the cover, mix, or protection needed to hit an arbitrary target service life and reliability level, rather than reading a value off a table calibrated to 50 or 100 years. Whether this methodology has ever been applied to a residential-scale project, or only to major infrastructure, is an open question below.

Given this gap, a genuine thousand-year target is necessarily an assembly of: the most conservative end of standard code provisions applied by default rather than only where triggered; the corrosion-resistant-reinforcement and self-healing technologies below; the detailing practices below; a planned, century-scale inspection and maintenance regime; and the empirical evidence from historic concrete and masonry that specific material and geometric choices measurably survive many centuries. No single code citation certifies the thousand-year goal; the chapter has to state that plainly rather than imply otherwise.

### 2. Deterioration Mechanisms

**Carbonation.** Atmospheric CO2 diffuses into the pore structure and reacts with calcium hydroxide and calcium-silicate-hydrate, forming calcium carbonate and dropping pore-fluid pH from roughly 12.5-13 to below roughly 9. Once the carbonation front reaches the reinforcement, the steel's protective oxide film breaks down (carbonation-induced corrosion, distinct from chloride-induced). Depth generally follows a square-root-of-time relationship; the rate constant depends on w/c, cement content, curing duration, cover, ambient CO2 concentration, and relative humidity. Carbonation proceeds fastest at intermediate relative humidity (roughly 50-70%): pores need some moisture for the CO2 to become carbonic acid, but fully saturated pores block CO2 diffusion. Field prevention: lower w/c, adequate curing (longer moist curing densifies the surface layer CO2 must cross first), adequate cover, low-permeability mix. Open question: some SCM-heavy mixes reportedly carbonate faster per unit depth than plain portland mixes if curing is cut short, since the SCM reaction that would otherwise density the pore structure needs time; this needs direct verification, not assumption.

**Chloride ingress.** Chloride ions penetrate by diffusion (approximated by Fick's second law), capillary absorption during wetting-drying cycles, and permeation under hydrostatic pressure below grade. Once concentration at the rebar reaches a chloride threshold (commonly cited in the 0.15-0.20% by mass of cement range, or roughly 0.03-0.05% by mass of concrete; figures vary by source and are unverified pending direct citation), the passive film breaks down locally, causing pitting corrosion, more localized and often faster than the general corrosion from carbonation. Oregon sources are not primarily marine spray away from the coast; more likely sources are calcium chloride accelerator use in cold-weather concreting, deicing salt on exterior slabs and driveways in the Cascades/high-desert freeze zones, and site-specific groundwater chloride (requires testing, not assumption). Prevention: low w/c, adequate cover, SCMs (all three common ones measurably reduce the chloride diffusion coefficient), corrosion-resistant reinforcement at the highest-risk locations, avoiding calcium chloride accelerator near reinforcement, penetrating sealers. Testing: RCPT (ASTM C1202, coulombs passed, a lab test); surface resistivity (AASHTO T358, a Wenner four-probe field/lab method, correlated to chloride diffusion resistance, with portable meters reported at roughly $330-395, 2025); sorptivity (ASTM C1585, capillary absorption).

**Alkali-silica reaction (ASR).** Reactive amorphous or microcrystalline silica in aggregate reacts with alkali hydroxides in the pore solution (from cement and, cumulatively, from other sources) to form an expansive gel that swells on absorbing water, generating internal pressure and a network of interconnected surface cracks. Three ingredients are necessary: reactive silica, sufficient alkali, sufficient moisture (roughly above 80% internal relative humidity); removing any one interrupts the reaction. Testing: ASTM C1260 (accelerated mortar bar, 16 days, aggressive), ASTM C1293 (concrete prism, 1-2 years, considered more field-representative), ASTM C1567 (accelerated mortar bar evaluating a specific aggregate/cement/SCM combination together, 16 days). Mitigation once reactive aggregate is confirmed or suspected: SCM replacement (fly ash and slag at adequate replacement rates measurably suppress expansion by lowering pore-solution alkalinity), lithium admixtures (lithium nitrate most commonly cited, interferes with gel-formation chemistry directly, used both preventively and therapeutically on existing ASR-affected concrete). Low-alkali cement ALONE is explicitly not sufficient per FHWA guidance found in this research, because total alkali loading from all mix constituents matters, not cement type alone; a real, commonly-missed misconception. Oregon relevance: Oregon appears on a 1956-era (Mielenz) list of US states with documented historical ASR occurrences. Aggregate reactivity is a deposit-specific property, not a statewide constant; whatever aggregate this project sources (including any owner-crushed or locally pit-sourced material) needs its own ASTM C1260/C1293/C1567 testing rather than an assumption based on regional geology.

**Sulfate attack, external and internal (DEF).** External: sulfate ions from soil, groundwater, or (rarely) adjacent sulfate-bearing material penetrate concrete and react with calcium aluminate hydrates and unhydrated C3A, forming expansive ettringite and gypsum, causing expansion, cracking, and eventual loss of cohesion. ACI 318-19 Table 19.3.2.1 sets four sulfate exposure classes (S0-S3) from water-soluble sulfate in soil and dissolved sulfate in water, each with a maximum w/cm and required cement type or SCM combination; reported figures (needing direct-table verification): severe exposure (roughly 0.2-2% sulfate in soil, or 1,500-10,000 mg/L in water) calls for Type V cement (C3A under 5%) and w/cm below roughly 0.45; moderate exposure allows Type II (C3A under 8%) below roughly 0.50 w/cm. Internal (delayed ettringite formation, DEF): a distinct mechanism from external attack, triggered when concrete's internal temperature during curing or heat treatment exceeds roughly 150-160°F (65-70°C), which decomposes the ettringite that would normally form early and defers its formation until after the concrete has hardened; the later growth happens inside an already-rigid matrix and cracks it from within, with no external sulfate source required. Directly relevant to mass concrete pours and to any accelerated curing (steam, hot mix water, high cement content) the project might use to speed owner-made block production, a real collision between the fast-demold ambition flagged elsewhere in the project's research and the century-durability goal this file covers.

**Freeze-thaw.** Water in saturated concrete pores expands roughly 9% by volume on freezing; above a critical saturation threshold, with no nearby escape path, hydraulic pressure microcracks the paste, and repeated cycles accumulate as scaling, spalling, and popouts. Entrained air (millions of microscopic, closely spaced, disconnected bubbles) gives freezing water room to expand into without stressing the paste. Governing parameters: total air content (roughly 5-8% by volume, sized by aggregate size and exposure) and void spacing factor (average distance between bubbles; a commonly cited target is roughly 0.20 mm or less measured per ASTM C457, though some early research cites a looser 0.25 mm threshold; treat both as reported figures needing verification), tested via ASTM C231 (pressure) or C173 (volumetric) at the truck. A correctly dosed air-entraining admixture can still fail in the field: over-working or over-finishing a slab collapses entrained air near the surface, exactly the zone needing it most, a commonly cited real field problem. Aggregate freeze-thaw soundness is a separate property from paste air-entrainment: porous, high-absorption aggregate causes D-cracking (freeze-thaw distress originating inside the aggregate itself, showing as cracks parallel to joints or edges) regardless of the paste's air-void system; low-absorption, dense aggregate resists it. ASTM C666 tests concrete specimens for freeze-thaw durability factor.

**Leaching and efflorescence.** Calcium hydroxide (portlandite, a free byproduct of cement hydration) dissolves into water moving through or across concrete. Migrating out and recrystallizing as calcium carbonate on an exposed surface produces visible white efflorescence, mostly cosmetic and diagnostic (a sign of an active moisture path) rather than structural in the short term. Sustained water movement THROUGH concrete (soft water, low-mineral rainwater or snowmelt, the most effective solvent because it is furthest from calcium saturation) progressively dissolves calcium out of the paste itself, increasing porosity and permeability and accelerating every other mechanism in this section; this is normally discussed for dams and other mass water-retaining structures but is a real, if slow, contributor over a genuinely multi-century horizon, relevant anywhere the design channels water through or along concrete for decades (foundation drains, a concrete water cistern under the project's water-independence goal, roof drainage over concrete parapets).

**Physical salt attack.** Distinct from sulfate ATTACK (a chemical reaction): a purely physical process where dissolved salts are drawn to an evaporating surface by capillary action and crystallize as the water evaporates, generating pore pressure from the growing crystal volume, producing surface scaling that can resemble freeze-thaw scaling. One reported example: the crystal-form transformation of sodium sulfate (thenardite to mirabilite) involves roughly a 314% volume increase (unverified, needs direct source check). Most associated internationally with arid and semi-arid climates (US Southwest, southern Europe, the Middle East, coastal Australia cited in the research); less an Oregon-wide risk given the wetter climate generally, but the same wick-and-evaporate geometry occurs anywhere a concrete element draws water up by capillary action to an exposed face that repeatedly dries: an exposed slab edge above a chronically damp base, a planter built against a foundation wall, a sun-facing retaining-wall face above wet backfill. A site-condition and detailing question, not a general climate concern.

### 3. Reinforcement Corrosion Mechanics, Cover, And Crack Control

Fresh concrete's high pore-solution pH (roughly 12.5-13.5) forms a thin, stable, protective oxide layer on embedded steel; this passive layer is what keeps ordinary black steel from rusting inside sound concrete for decades. Corrosion starts once the layer breaks down, either by carbonation dropping local pH below roughly 9-10, or by chloride reaching a threshold concentration at the steel surface regardless of pH. Corrosion is an electrochemical process: anodic sites (iron dissolving) and cathodic sites (oxygen reduction) connected by the steel itself (electron path) and the pore solution (ion path); a small anodic pit paired with a large cathodic area concentrates the attack, which is part of why chloride-driven pitting can be more aggressive than uniform carbonation-driven corrosion.

Rust (iron oxide/hydroxide corrosion products) occupies roughly 2 to 6 times the volume of the steel consumed (a range reported across multiple sources, worth precise verification before citation). The accumulating corrosion product generates expansive pressure against the surrounding concrete, cracking and eventually spalling the cover. Once cover cracks, water, oxygen, and any chloride present reach the steel faster, accelerating further corrosion: a self-reinforcing failure sequence, which is the mechanism behind the Champlain Towers South collapse (see section 9/case studies below) and behind the century-scale reasoning for why cover and crack control matter as much as raw compressive strength.

Cover is both the physical distance a carbonation or chloride front must cross and the confinement that resists early cover-cracking. Cracks that intersect reinforcement create fast paths straight to the steel, short-circuiting cover's diffusion protection. ACI 224/ACI 318 tie allowable crack width to exposure severity; reported figures needing direct-citation verification: roughly 0.016 in./0.4 mm for interior/dry exposure, roughly 0.013 in./0.33 mm for exterior exposure, with stricter limits (roughly 0.007 in./0.18 mm) proposed in some deicing-salt bridge-deck literature. ACI 350 (environmental and watertight structures) imposes materially tighter crack-width and minimum-shrinkage-reinforcement rules than ordinary ACI 318 buildings, because a crack that leaks water is also a corrosion-initiation path; directly relevant to any concrete water cistern or tank under this project's water-independence goal, and a genuine cross-reference point rather than a duplicate topic.

### 4. Low-Permeability Mix Design And Verification Testing

The existing manuscript section already sets w/c targets (0.45 general long-life, 0.40 severe exposure). The gap this chapter fills: HOW an owner-builder or small ready-mix supplier verifies that delivered or placed concrete achieved low permeability, since a passed 28-day cylinder break measures strength, not permeability, and the two do not automatically track together, especially for SCM mixes that keep gaining both strength and reduced permeability well past 28 days.

RCPT (ASTM C1202): measures total electrical charge (coulombs) through a saturated concrete disc over 6 hours; a widely cited rough scale (unverified pending direct standard citation): under 1,000 coulombs "very low," 1,000-2,000 "low," 2,000-4,000 "moderate," over 4,000 "high" chloride-ion penetrability. A lab test, not owner-performable. Surface resistivity (AASHTO T358, Wenner four-probe): a nondestructive alternative correlated to RCPT and to the chloride diffusion coefficient; portable meters reported at roughly $330-395 (2025), lab-grade units at roughly $6,000-11,000; the inexpensive tier is plausibly within reach for an owner doing QC on owner-mixed concrete, unlike RCPT. Sorptivity (ASTM C1585): capillary water absorption rate on a dried, then partially submerged specimen; ties directly to freeze-thaw and to chloride/sulfate ingress by capillary suction between wetting cycles.

Extended curing is a durability lever, not only a strength lever: continuing moist curing well past the manuscript's existing 7/14-day minimums measurably continues reducing permeability for SCM mixes in particular, because fly ash and slag reactions keep consuming calcium hydroxide and refining pore structure for months. How many extra curing days buys how much extra service life is a real, currently unanswered, owner-actionable question.

### 5. Supplementary Cementitious Materials (SCM) For Durability

**Fly ash** (Class F typical for durability, ASTM C618): slow-reacting pozzolan, reduces permeability and heat of hydration, historically economical. Oregon-specific supply note already documented in this project's research: the PGE Boardman coal plant closure (2020) removed Oregon's own fly ash source; current Oregon supply is trucked from out-of-state plants through regional distributors, with a Lehigh Hanson Portland terminal cited as the common Oregon source.

**Slag cement / GGBS** (ASTM C989): reacts faster than fly ash, slower than portland alone; notably effective against sulfate attack and chloride ingress at higher replacement rates (30-50% cited in the existing manuscript table); available in the Pacific Northwest through the same regional terminals as fly ash.

**Silica fume** (ASTM C1240): extremely fine grained, highly reactive, produces the densest, lowest-permeability paste fastest among common SCMs, but sharply increases water demand (needs a high-range water reducer in practice) and raises plastic-shrinkage cracking risk if not cured immediately and continuously. Priced by the pound (roughly $1-3/lb, per existing project research) rather than the ton, typically used at 5-10% dosage for a targeted durability boost, not as the primary SCM.

**Metakaolin**: a calcined kaolin clay pozzolan, broadly similar performance to silica fume in several studies (dense paste, strong early pozzolanic activity) without silica fume's extreme water demand and handling difficulty; less commonly stocked by mainstream US ready-mix suppliers than fly ash, slag, or silica fume; likely a specialty order, an open sourcing question rather than an assumption of unavailability.

**Natural pozzolans** (volcanic ash, calcined shale, some zeolites; also covered under ASTM C618): the original pozzolan material (the term comes from Pozzuoli, Italy, the volcanic-ash source the Romans mined), and the material behind the ancient-concrete durability case studies below. Oregon and the Pacific Northwest sit on substantial volcanic geology; whether a usable natural pozzolan deposit (volcanic ash, pumice, scoria) exists within practical hauling distance of the actual build site is a genuinely open, regionally specific, low-cost, low-carbon research question fully in keeping with the project's make-your-own materials ethos, not a researched fact here.

Cross-cutting trade-offs: early strength gain is fastest with plain portland, fast with silica fume/metakaolin, moderate with slag, slowest with fly ash; all SCMs slow early strength somewhat in cold weather, which is a real scheduling interaction with the project's winter-pour realities; water demand rises with silica fume and metakaolin, falls slightly with fly ash, stays roughly neutral with slag; long-term permeability reduction is fastest and strongest per unit replacement with silica fume and metakaolin, strong at high replacement with slag, slower but ultimately comparable with fly ash given adequate curing time; ASR suppression varies by source chemistry (SCMs are generally net-suppressive at adequate replacement, but this is source-specific, which is why ASTM C1567 testing of the actual aggregate/cement/SCM combination is the only real verification, not a category-wide rule of thumb).

### 6. Corrosion-Resistant Reinforcement: The Full Menu

**Black (ordinary) steel**: relies entirely on the concrete's alkalinity and low permeability; fine at normal cover and normal exposure per the existing manuscript durability section. The question this chapter adds: where across the house is black steel NOT enough, and where does an upgrade earn its cost.

**Epoxy-coated rebar** (ASTM A775/A934): a fusion-bonded epoxy coating electrostatically applied to the bar; widely used from the 1970s onward, especially for bridge decks and marine substructures. A well-documented, multi-decade failure history exists: Florida Keys bridges first showed failing coating as early as 6-12 years into service, starting in the mid-1980s, with the coating disbonding from the steel even where visibly uncorroded, and once chloride or moisture reaches under a disbonded or damaged patch, corrosion proceeds UNDERNEATH the coating, hidden from inspection, sometimes concentrated faster than on bare steel. Handling damage (bending, tying, dropping, UV exposure before placement) is the most commonly cited root cause of coating breaches. Net assessment: a real corrosion-life extension over bare steel in mild-to-moderate exposure, no longer considered top-tier for genuinely severe, chloride-rich, multi-century exposure given the documented failure mode; still the cheapest upgrade from black steel.

**Hot-dip galvanized rebar** (ASTM A767): a zinc coating metallurgically bonded to the steel, not a surface film; the zinc corrodes preferentially (sacrificially), and its own corrosion products accumulate gradually rather than suddenly, delaying the onset of damaging expansive pressure at the base steel. The zinc layer is reported harder than the underlying steel and more resistant to handling damage than an epoxy film. Cost reportedly competitive with epoxy on an initial basis (roughly $1.20-1.60 per linear foot for common sizes reported) and roughly a quarter of stainless steel's initial cost; longevity is reported comparable to stainless in some galvanizing-industry sources, a claim needing independent (non-industry) verification.

**Stainless steel reinforcement, solid** (ASTM A955, typically Type 316 or 2205 duplex for best chloride resistance): the highest-performing corrosion-resistant option in the gathered literature, effectively removing chloride-threshold and carbonation-depassivation as failure triggers for the bar itself over a multi-century horizon. Also the most expensive by a wide margin (reported up to roughly $9 per linear foot for common sizes, several times galvanized or epoxy). A realistic strategy given cost is targeted use at the highest-risk locations (at-grade splash zones, reduced-cover locations, anywhere future repair access is destructive or unlikely) rather than a whole-house default. Stainless-clad or duplex-clad bar (a carbon-steel core with a metallurgically bonded stainless outer layer, marketed in the US under names like MMFX2/ChrōmX) is a lower-cost middle option; this research did not find hard pricing for it, an open sourcing question.

**GFRP rebar** (glass-fiber-reinforced polymer; ASTM D7957 material spec; ACI 440.11-22 design code; ICC-ES AC454 acceptance criteria): does not corrode electrochemically (it is not a metal), removing the corrosion-driven cracking/spalling failure mode for the bar itself entirely. Current reported US pricing places it near, or in some reported cases below, epoxy-coated steel on an installed-cost basis once its much lighter weight (easier handling, lower freight, faster tying, no corrosion-related future labor) is counted, though raw material cost per linear foot is reported somewhat above plain black steel (roughly $0.55-2.50/ft depending on size and source, versus roughly $0.40-1.25/ft for basic black steel, both 2025-2026-reported). ACI 440.11 explicitly covers footings, slabs, and walls, matching much of this project's structural scope, but the existing structural chapter already flags a real limit worth carrying forward, not contradicting: current AC454 acceptance criteria for FRP bar in general concrete construction is limited to Seismic Design Category A or B. Whether the project's actual build site falls in that SDC range, given Oregon's Cascadia seismic exposure, needs checking against the manuscript's own site-to-SDC matrix; if not, GFRP could still suit non-primary elements (slab-on-grade temperature-and-shrinkage steel, a detached lower-risk structure) even where it cannot serve as primary structural reinforcement. GFRP is also a brittle-failure material (no yielding before rupture, unlike steel), a structural-design consideration independent of its corrosion performance, and its bond behavior with concrete differs from deformed steel (different development-length and lap rules under ACI 440.11), a real detailing difference, not a simple substitution.

**Basalt FRP (BFRP) rebar**: a less standardized US market than GFRP; multiple sources describe US approval as project-specific or ESR-based rather than under one universal consensus standard, unlike GFRP's ACI 440.11. Reported in several studies to have somewhat better bond strength and better resistance to concrete's high-pH pore solution than plain E-glass GFRP, but glass-fiber chemistry itself varies (ECR-glass and AR-glass GFRP formulations are engineered to close this alkalinity gap), so "GFRP" is not one uniform product and the specific glass chemistry matters. BFRP still showed measurable bond-strength loss (double-digit percentages reported) after months of alkaline, elevated-temperature aging in lab studies: FRP bars have their own long-term aging behavior in concrete's alkaline environment, distinct from, but not absent the way steel corrosion is.

Practical framing: a mixed-reinforcement strategy, corrosion-resistant material only where it earns its cost (below-grade, at-grade splash zones, destructive-to-repair locations, anywhere the exposure class already reads "severe" under the manuscript's own table), is more defensible on cost than an all-stainless or all-GFRP house, and is the kind of side-by-side option layout this chapter should give the owner.

### 7. Cathodic Protection, Sacrificial Anodes, And Corrosion Inhibitors

**Galvanic (sacrificial) embedded anodes**: small zinc or zinc-alloy units tied directly to the reinforcement at placement, needing no external power or control panel, a real practical advantage for a standalone rural house with no ongoing professional monitoring contract. Reported anode service life is roughly 10-20 years, meaning a genuine century-scale galvanic-anode strategy is a repeated, planned replacement program, not an install-once fix; this belongs in the maintenance-chapter replacement-horizon table, cross-referenced from this chapter.

**Impressed current cathodic protection (ICCP)**: an externally powered system (a rectifier driving current through installed anodes to the rebar network), used far more often to REPAIR and preserve already-corroding structures than for new construction. Oregon's own Highway 101 coastal bridges are a real, documented in-state case: ODOT installed both ICCP and sacrificial thermal-sprayed-zinc systems starting in the late 1980s on the historic 1930s Conde McCullough spans (Cape Creek, Yaquina Bay, Depoe Bay) specifically to arrest existing chloride-driven corrosion rather than replace the bridges, at a reported cost far below full replacement: roughly $2.4 million (Cape Creek), roughly $4 million (Depoe Bay), roughly $12.7 million (the larger Yaquina Bay bridge), against an estimated $70 million-plus to replace all three. A strong, citable, Oregon-specific precedent for the maintenance section of this chapter, though bridge-scale, not residential-scale; whether a rural concrete house would ever need cathodic protection, or whether this is purely a large-marine-structure tool, is an open question.

**Corrosion inhibitors, admixed**: calcium nitrite, the longest-established chemical corrosion inhibitor, reacts with iron at the steel surface to help maintain or re-form the passive oxide layer even with some chloride present, effective up to a chloride threshold beyond which it is overwhelmed; reported to accelerate set time, a real scheduling interaction with the project's cold- and hot-weather concreting practices already in the manuscript.

**Migrating corrosion inhibitors (MCI)**: applied to the hardened concrete surface (not admixed at batching), diffusing inward to reach the reinforcement; reported not to affect set time, since it is a post-placement treatment. Positioned in the gathered material both as a new-construction supplemental option and as a REPAIR/retrofit option applicable decades into a structure's life, directly relevant to the century-scale maintenance regime this chapter should define (a preventive maintenance step, not only a one-time construction choice).

### 8. Self-Healing, Autogenous Healing, Bacterial Concrete, Crystalline And Hydrophobic Admixtures

**Autogenous healing** (no additive): ordinary portland concrete has some natural self-healing capacity because unhydrated cement grains remain in the paste indefinitely and continue reacting when water reaches them through a crack, and dissolved calcium hydroxide can recrystallize as calcium carbonate inside the crack. Generally effective only for fine cracks (a commonly cited threshold around 0.1-0.2 mm, unverified), working better in continuously or intermittently damp conditions than dry-sheltered ones.

**Crystalline admixtures** (Xypex, Kryton, Penetron, and similar): a Portland-cement-and-reactive-chemical blend, added at batching or applied as a surface slurry to hardened concrete, reacting with residual moisture and unhydrated cement to grow needle-like crystals through the pore network and any subsequent fine cracks, blocking the water path. Described in the gathered research as currently the most commercially mature, most widely specified self-healing-adjacent technology, because it needs no special curing regime and no living organism to survive batching, mixing, and placement; it integrates into an otherwise ordinary concrete process. A hydrophilic mechanism (draws water in to react), distinct from the hydrophobic category below.

**Hydrophobic pore-blocking admixtures** (a distinct category; example found: Hycrete): form a water-repelling layer through the pore network rather than growing water-attracting crystals; marketed against the crystalline category on the claim that a hydrophilic product still allows some capillary water uptake because the concrete stays water-attracting even after crystal growth, while a true hydrophobic pore-blocker reduces capillary uptake more completely. Treat the comparative-superiority claim as vendor-sourced and unverified pending independent test data.

**Bacterial (biogenic) self-healing concrete**: alkaliphilic, spore-forming bacteria (Bacillus species most researched) embedded in the mix, typically protected inside a carrier (zeolite or other porous aggregate cited in recent research) to survive the concrete's high pH and mechanical mixing while dormant, until a crack admits water and oxygen. Germinating spores metabolize a calcium-based nutrient (commonly calcium lactate) also embedded in the mix, precipitating calcium carbonate that fills the crack (microbially induced calcite precipitation). The Dutch company Basilisk (a TU Delft spin-off from Henk Jonkers' research) is the most commercially established product found, reported effective for cracks up to roughly 1 mm (0.04 in.) wide, with a demonstrated repair-market application (a river lock project in the UK). Bacterial self-healing is newer to market and less broadly proven at ordinary contractor or ready-mix scale than crystalline admixtures, a real maturity gap.

Practical framing: for a mostly-solo owner-builder using ordinary ready-mix or owner-batched concrete, crystalline admixtures are the more readily available, lower-friction option to specify today; bacterial concrete is a genuine but harder-to-source, harder-to-verify emerging option worth a dedicated availability question, not a default recommendation.

### 9. Lessons From Ancient And Vernacular Durable Concrete And Mortar

**Roman hot-mixed lime concrete** (MIT/Harvard research, Masic et al., published in Science Advances, 2023): the historically overlooked white "lime clasts" in Roman concrete, long assumed to signal sloppy mixing, are now understood as a deliberate byproduct of "hot mixing": using reactive quicklime (calcium oxide) directly rather than pre-slaked lime, driving the mix to temperatures reported near 400°C locally around the reacting lime, which also accelerates curing and shortens construction schedules. When a later crack reaches a lime clast, water dissolves calcium out of the clast and it recrystallizes as calcium carbonate inside the crack, sealing it. The research team's lab replication reported cracked hot-mixed samples fully healing (water flow through the crack stopped) within two weeks of exposure to running water, while control samples with no quicklime clasts showed no healing. This is functionally a historical precedent for the crystalline-admixture mechanism above, achieved with an ordinary, period-appropriate, still-commercially-available material (quicklime) rather than a proprietary modern chemical: a real, low-tech, potentially replicable method worth a direct research question about owner-scale testing for this project's own concrete or owner-made-block mixes.

**Roman seawater concrete** (Marie Jackson and collaborators, ongoing research since the 2010s, harbor and breakwater structures around the Bay of Naples): a separate mechanism specific to marine structures. Volcanic ash (pozzolana, the material's namesake source at Pozzuoli) reacted with lime and, critically, with ongoing seawater percolation through the structure over centuries, continuing to grow new interlocking mineral crystals (notably aluminous tobermorite and phillipsite) inside the pore structure long after initial construction: the internal structure was still actively strengthening on a 2,000-year timescale rather than only degrading, the opposite long-term trajectory from ordinary portland concrete in the same chloride-rich, wave-action exposure. The platy crystal shape is reported to add resistance to brittle fracture, not just fill pores. A genuinely different chemical system from modern portland cement (much lower calcium content, much higher reliance on the volcanic ash's own aluminosilicate chemistry), not a simple swap-in for residential construction, but the strongest available real-world evidence that a cementitious material can survive millennia in a genuinely aggressive, chloride-rich exposure.

**The Pantheon's unreinforced dome**: standing roughly 1,900 years, the largest unreinforced concrete dome in the world. The gathered research repeats the general Roman hot-mixing/pozzolan narrative for it without a mechanism specific to the dome beyond that. Worth stating plainly: the Pantheon has no embedded reinforcement at all, so it structurally sidesteps the entire reinforcement-corrosion failure mode driving most modern reinforced-concrete deterioration. Not directly transferable to a code-built modern structural shell needing reinforcement for tension and seismic performance, but a real illustration that plain, well-proportioned, unreinforced concrete or masonry mass has its own separate, long, corrosion-free durability path, worth a design question about where (if anywhere) deliberately unreinforced mass elements make sense in this specific house (a garden wall, a root cellar, a non-structural mass element) as a corrosion-proof-by-design choice.

**Chinese sticky-rice lime mortar**: a composite organic-inorganic mortar developed roughly 1,500 years ago (reported Northern Wei Dynasty origin, 4th-6th century CE), made by mixing a sticky-rice starch solution into slaked lime mortar. Amylopectin, identified in modern research as the active component, interferes with and controls calcium carbonate crystal growth as the lime mortar carbonates and hardens, producing a denser, more compact, lower-permeability, better-adhering mortar than plain lime mortar. Used historically for high-value structures (tombs, pagodas, city walls, parts of the Great Wall), some reported to have survived earthquakes and resisted modern demolition equipment (anecdotal at the specific-incident level, unverified). Modern conservation researchers have used the same recipe to repair genuinely old masonry (an 800-year-old bridge in China cited). A real, cheap, worldwide, non-Western vernacular durability technology, and a strong candidate for owner-scale testing specifically for this project's mortar and jointing work; the sibling mortar/grout/jointing draft already asks about hydrated lime's role, but not about sticky-rice addition specifically.

**American tabby concrete** (coastal South Carolina, Georgia, Florida, 1700s-1800s): a lime-sand-oyster-shell concrete (burned oyster shells calcined into quicklime, slaked, then mixed with sand, water, and more whole or crushed shell, sometimes ash), used by colonial-era coastal builders. Original structures reported still standing after 200-plus years in a humid, salt-air, coastal climate. The source-level explanation (shell content resists humidity and salt air) is a general claim rather than a mechanistically explained one in the gathered research, worth treating as a real historical data point (a long-lived, low-tech, regionally sourced lime-shell concrete in a wet, salty climate not unlike parts of the Oregon coast) rather than a proven mechanism. A legitimate research question, and a creative, real, low-embodied-energy option if the site or a nearby source has usable shell material, and separately relevant as another worldwide precedent for lime-pozzolan-shell systems alongside the owner's already-flagged interest in lime-pozzolan block options.

Cross-cutting point to state plainly: none of these historical systems is a drop-in replacement for code-engineered modern reinforced concrete, and none was designed under a structural code or tested to a modern strength/durability standard. Their value to this project is as sourced, testable ingredients or techniques (hot-mixed quicklime, natural volcanic pozzolan, sticky-rice admixture, shell-lime aggregate) that could be evaluated experimentally under the project's own existing lab-cylinder alternative-materials path, not assumed to work by historical reputation alone.

### 10. Detailing For Durability: Drip Edges, Overhangs, Drainage, Salt Traps

**Drip edges**: industry sources converge on a minimum roughly 2-inch projection past the wall face with a formed drip groove on the underside, so water running along the underside of a horizontal projection (sill, coping, band, overhang) is forced to detach and fall clear rather than following the underside back to the wall face by surface tension. Without the groove, water can travel backward under a projecting element even when the top surface and visible joints look intact, wetting a wall for years from a "protected" detail before any surface sign appears.

**Parapet coping**: one of the more failure-prone details because it combines several risk factors: the highest, most sun- and freeze-cycled element on the building; a horizontal or near-horizontal top that can pond water if it does not slope; and joints between coping sections that are a direct path into the wall below if not properly lapped and sealed. The existing manuscript PMR roof section already specifies parapet membrane continuity (up, over, and down under a metal coping or counter-flashing) and already names the failure modes (condensation inside the parapet cavity, freeze-thaw at the coping joints, UV at exposed membrane terminations). This chapter's addition: the coping CAP material choice itself. Rigid concrete or masonry coping caps are reported prone to their own cracking over time from thermal movement and freeze-thaw, which is why coastal or aggressive-exposure practice increasingly favors metal (aluminum, stainless steel) or GRP coping systems over a solid concrete cap on the most exposed elements, a real material-substitution option worth laying out even though the structural wall beneath stays concrete or masonry either way.

**Salt traps and standing water generally, beyond parapets**: any horizontal or near-horizontal ledge, reveal, sill, or setback on an exterior wall face collects water and, if any chloride source exists (even a small one, like wind-blown road spray reaching a driveway-adjacent wall, or deicing-salt splash), concentrates dissolved salts as water evaporates between rain events, triggering the physical-salt-attack and freeze-thaw-scaling mechanisms locally at that ledge regardless of the building's overall climate zone. The repeated design response across the gathered sources: slope every horizontal or near-horizontal surface (not only roofs) to positive drainage, avoid flat ledges on an exterior wall face wherever the architecture allows, and where a ledge is unavoidable (a window sill, a belt course), give it its own drip edge and slope rather than relying on the main wall's drainage plane to handle redirected water.

**Foundation-level standing water, century-scale framing**: the manuscript's existing foundation-drainage sections already cover the perimeter drain, the waterproofing-versus-dampproofing trigger list, and downspout discharge distance. This chapter's addition is the century-scale consequence: a drain or downspout discharge adequate on day one but silted up, crushed by later landscaping, or buried under an added patio or planter decades later re-creates the exact standing-water or chloride/sulfate-concentration condition the whole rest of this chapter tries to prevent. "Maintain the original drainage design intent" belongs as an explicit item in the century-scale maintenance regime (section 12 below), not only as a one-time construction-phase checklist item.

**Planters and landscaping against structural walls**: a repeatedly cited real-world problem pattern in home-inspection and forensic literature (found in general research, not yet directly source-verified for this compiled note, flagged for verification) is a built-in planter or dense landscaping bed placed directly against a foundation or structural wall, keeping the adjacent soil chronically damp, sometimes irrigated on its own timer independent of the building's drainage design, functionally defeating the waterproofing and drainage design from outside. A real, entirely avoidable problem worth an explicit prevention rule in this chapter.

### 11. Service-Life Modeling And The Honest Limits Of Code

**Life-365**: a Fickian-diffusion-based chloride service-life prediction tool, originated through an ACI Strategic Development Council effort and moving toward ACI Committee 365 ownership. Models time to corrosion initiation (time for chloride concentration at rebar depth to reach a critical threshold) as a function of cover depth, w/cm (through an assumed or measured diffusion coefficient), SCM use, surface chloride exposure severity, and, in later versions, surface treatments and reinforcement type. Free or low-cost, used industry-wide as a comparative design tool (mix A against mix B for the same exposure), not typically treated as a precise absolute-year prediction. Whether it is usable, and how, for a residential-scale, mostly non-marine, mostly non-deicing Oregon exposure is an open question, since most published case studies and default exposure data are bridge- or marine-oriented.

**Eurocode 2 / BS 8500 design working life system** and **fib Model Code 2010**: covered in section 1 above. Repeated here as the two international reference points most directly useful for framing a design life beyond what ACI 318 addresses by table alone.

**The extreme end of the literature**: two data points, both far outside ordinary structural practice, both worth carrying as clearly labeled unverified leads rather than design guidance. First, low-level radioactive waste containment regulatory guidance reported requiring engineered barrier integrity for up to 500 years, reasoned explicitly from conventional reinforced and mass concrete durability principles pushed to their limit (extra cover, extra density, monitoring, planned maintenance for the first 100 years, then a passive-performance requirement). Second, specialty geopolymer (alkali-activated, non-portland) concrete research literature reporting formulations projected, via accelerated and modeled weathering rather than actual multi-millennial observation, to endure on the order of 2,500 to 5,000 years for waste-containment use. Neither is a buildable residential specification, but both show the durability-engineering literature does seriously engage multi-century-to-multi-millennial targets outside ordinary structural codes, directly relevant framing for why this project's thousand-year goal needs its own chapter, and a legitimate place to look for transferable principles (extreme cover, extreme density, redundant protection, planned inspection) even though the containment industry's exact specifications do not apply to a house.

**Honest gap to state plainly**: no mainstream US or international structural code defines a thousand-year design-life category, deemed-to-satisfy table, or verification test. The chapter has to say this directly rather than imply a code citation validates the goal, then build the case from the assembled pieces in sections 2 through 10 plus the maintenance regime in section 12.

### 12. Century-Scale Inspection And Maintenance Regime

The existing maintenance chapter states the concrete footing and foundation have "no replacement date, if properly built," but, unlike its treatment of shorter-lived components (a water heater, gutters), it does not define what condition monitoring watches for over a multi-century span. This is the clearest gap this new chapter fills for the existing documentation and maintenance chapter, not a duplicate of it.

**Visual survey** (zero cost, owner-performable): the existing maintenance calendar already has the owner surveying concrete and masonry cracks annually with logged widths. This chapter's addition: what to look for beyond crack width. Rust staining on a surface (a visible sign of corrosion starting well before cracking or spalling is visible, since corrosion products can wick through the pore structure and stain the surface ahead of mechanical damage); efflorescence patterns and whether they recur after cleaning (recurring efflorescence at the same spot flags an ongoing water path worth tracing to its source, not just a cosmetic bleach-and-forget item); hollow-sounding areas found by tapping or chain-dragging a suspect surface (a delamination indicator, standard bridge-deck inspection practice, directly performable by an owner with a hammer or a length of chain, no special equipment).

**Instrumented owner-level monitoring**: tell-tale or crack-monitor gauges (two overlapping marked plates spanning a crack, reusable, no power needed, reported at roughly $15-50 retail per unit) let an owner objectively track whether a specific crack is stable or actively growing over months or years, a cheap, zero-training tool suited to a solo owner-builder's own long-term monitoring, rather than requiring a professional visit to answer "is this getting worse."

**Professional-tier tools**, for periodic (not necessarily annual) deeper checks or before a major renovation, addition, or repair decision: a cover meter or GPR scan to confirm as-built rebar position and cover against the design drawings (useful once, as-built, and again before ever coring or anchoring into an old wall decades later); a surface-resistivity or half-cell potential survey (ASTM C876, the standardized corrosion-probability mapping method using a reference electrode, interpreting readings more negative than roughly -350 mV as high corrosion probability and more positive than roughly -200 mV as low probability) as a targeted diagnostic once visual signs suggest active corrosion somewhere and its extent needs mapping before a repair decision.

**A planned interval, not only a reactive one**: this research did not find a ready-made "century home" inspection calendar. ICRI's published guidance is aimed at professionals evaluating existing distress, not at owners on a preventive schedule, and no homeowner-specific periodic schedule surfaced. This is itself a finding: this chapter likely has to adapt the bridge and infrastructure inspection-interval concept (periodic professional condition surveys, ODOT's own bridge inspection cycles among them, a real, findable precedent) down to residential scale, rather than quoting an existing residential standard, since none was found. Flag this explicitly as an open design question rather than implying a source exists.

**Repair readiness**: the finished construction documentation, already required by the existing documentation and maintenance chapter, needs to stay specifically usable for a future repair decision: as-built cover and reinforcement type by location (so a future owner or repair contractor knows whether a given wall has black, epoxy, galvanized, stainless, or GFRP bar before selecting a repair method, since some repair techniques, like impressed current cathodic protection, interact with reinforcement type); the original mix design and admixtures used (relevant if a future patch material needs to be chemically and electrochemically compatible with the original; an incompatible patch is a well-documented repair-industry problem, since it can create a new corrosion cell AT THE PATCH BOUNDARY, a reported cause of repeated or spreading repairs rather than a single fix, worth its own citation-verification question); and the original waterproofing and drainage design intent, so future landscaping, additions, or renovations do not accidentally defeat it.

### 13. Oregon-Specific Notes

Freeze-thaw exposure varies sharply by region: the Cascades and Central/Eastern Oregon (the "high desert") see materially more hard-freeze cycling than the Willamette Valley or the immediate coast. Exact cycle-count or weathering-index data by specific build-site location is unverified here, pending a direct climate-data lookup (NOAA normals, or an ASTM C216-style weathering-index calculation, the same index method used for brick grade selection, defined as freezing-cycle days multiplied by average annual winter rainfall).

ASR history: Oregon appears on a historical (1956-era, Mielenz) list of states with documented ASR occurrences. Aggregate reactivity is deposit-specific, not a statewide constant; the actionable takeaway is source-specific testing of whatever aggregate the project uses, especially given the project's own make-your-own-block and possible own-aggregate ambitions, rather than a general regional reactivity rating.

Coastal salt exposure and its documented precedent: Oregon's own Highway 101 coastal bridges are a real, heavily documented case of chloride-driven reinforced-concrete corrosion in a marine environment, addressed at the state level with both sacrificial and impressed-current cathodic protection. Directly useful as an in-state precedent even though bridge-scale, and a strong pointer to how seriously to weigh chloride exposure for any part of this project sited near the coast or exposed to wind-driven salt spray, a siting-dependent variable, not a statewide constant.

Aggressive soil and groundwater: the project's existing site-evaluation and geotechnical work (septic siting, foundation geotech) is a natural point to ADD sulfate and pH testing of on-site soil and groundwater, since the same test pits or borings already planned for septic and foundation purposes could, at little added mobilization cost, also be sampled for water-soluble sulfate and pH.

### 14. Cost Summary (All Figures As Reported In Sources Above, Unverified Across Multiple Sources, Years Noted Where Found)

| Item | Reported range | Year |
|---|---|---|
| Fly ash, bulk (existing project research) | $80-150/ton bulk; $15-25/50 lb bag retail | 2026 |
| Slag cement (GGBS), bulk (existing project research) | $100-180/ton bulk | 2026 |
| Silica fume (existing project research) | $1-3/lb, 50 lb bags | 2026 |
| Surface resistivity meter, portable (Resipod-class) | roughly $330-395 | 2025 |
| Surface resistivity meter, lab-grade | roughly $6,000-11,000 | not stated |
| Tell-tale crack monitor gauge, retail | roughly $15-50 per unit | 2025-2026 |
| GFRP rebar | roughly $0.55-2.50/linear ft; roughly $3-6/kg | 2025-2026 |
| Black steel rebar, basic | roughly $0.40-1.25/linear ft | 2025-2026 |
| Galvanized rebar | roughly $1.20-1.60/linear ft | not stated |
| Stainless steel rebar, common sizes | up to roughly $9/linear ft | not stated |
| UHPC (proprietary/specialty mixes) | roughly $360-3,000/cubic yard | not stated |
| Ordinary ready-mix, comparison baseline | roughly $167/cubic yard | not stated |
| Long-life foundation waterproofing upgrade over code-minimum dampproofing (existing manuscript) | $5,000-15,000 | 2026 |
| ODOT coastal bridge cathodic-protection rehab (infrastructure scale, precedent only) | $2.4M (Cape Creek), $4M (Depoe Bay), $12.7M (Yaquina Bay), versus est. $70M+ to replace all three | not stated |

None of these figures are independently cross-verified across multiple sources; all require direct verification before any manuscript `Code` or cost entry is written.

### 15. Proposed Chapter Outline: Designing For Centuries, Durability Engineering

1. The Durability Framework: Exposure, Design Life, And The Century-Scale Design Problem
2. How Concrete Fails: The Deterioration Mechanisms (carbonation, chloride, ASR, sulfate/DEF, freeze-thaw, leaching, physical salt attack)
3. Reinforcement Corrosion: Passivation, Cover, And Crack Control
4. Low-Permeability Mix Design And Verifying It
5. Supplementary Cementitious Materials For Durability
6. Corrosion-Resistant Reinforcement: The Full Menu
7. Cathodic Protection, Sacrificial Anodes, And Corrosion Inhibitors
8. Self-Healing Concrete: Crystalline, Bacterial, And Autogenous
9. What Ancient And Vernacular Concrete Teaches
10. Detailing For Durability: Water Off, Salt Out
11. Service-Life Modeling And The Honest Limits Of Code
12. The Century-Scale Inspection And Maintenance Regime

---

## PART 2: CANDIDATE RESEARCH QUESTIONS

### A. Framework, Exposure Classes, Design Life

**Q1.** What does ACI PRC-201.2-23 (Guide to Durable Concrete) state, chapter by chapter, and does its guidance conflict anywhere with ACI 318 Chapter 19's exposure-class minimums for a project deliberately targeting beyond-code service life?
Lands in: Designing for Centuries (proposed chapter). [CODE]
Leads: ACI 201.2R-23 organizes by mass transport then per-mechanism chapters; verify against ACI 318-19/22 directly.

**Q2.** How does the Eurocode 2 / BS 8500 "design working life" and "structural class" system translate cover and mix requirements as design life increases from 50 to 100 years, and can that adjustment logic be extrapolated (with engineering judgment, not code authority) toward a longer target?
Lands in: Designing for Centuries. [CODE]
Leads: BS 8500 Table A.4 (50-year) vs Table A.5 (100-year); structural class tied to concrete strength class and cover.

**Q3.** Has fib Model Code 2010's full-probabilistic durability design methodology ever been applied to a residential-scale structure, and is the underlying calculation (e.g., a chloride-diffusion service-life spreadsheet) something a structural engineer of record could run for this specific house?
Lands in: Designing for Centuries. [CODE][METHOD]

**Q4.** What does ACI 318's own commentary say about the assumed service life behind its exposure-class minimums (commonly understood as roughly 50-75 years), and how much conservative margin is available by applying the "severe" exposure class by default across the whole structural shell rather than only where triggered?
Lands in: Designing for Centuries. [CODE]

**Q5.** Do any published case studies exist of a single-family residence (anywhere in the world) explicitly engineered to a stated multi-century design life, and what design choices did that project make?
Lands in: Designing for Centuries. [REAL-WORLD-EXPERIENCE]

**Q6.** What is the actual engineering and regulatory reasoning behind the 500-year barrier-integrity requirement for low-level radioactive waste containment, and which of its conservative-design principles (cover, density, redundancy, monitoring) transfer to a residential structural shell versus which are containment-specific and irrelevant here?
Lands in: Designing for Centuries. [CODE][METHOD]
Leads: unverified; low-level waste facility guidance reportedly requires 500-year intruder-barrier integrity with passive performance after year 100.

**Q7.** What do the geopolymer-concrete waste-containment projections of multi-millennial service life rest on (accelerated testing, modeling, or real long-term data), and is any of that testing methodology adaptable to verify a durability claim for this project's own alternative-materials test-to-prove path?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [TEST-TO-PROVE][MATERIALS/INGREDIENTS]
Leads: unverified 2,500-5,000-year geopolymer projection figure, modeled/accelerated, not observed.

### B. Carbonation

**Q8.** What carbonation depth, after how many years, is plausible for this project's specified long-life mix (0.45 or 0.40 w/c, with SCM) under Oregon's wet marine and inland climate conditions, using a recognized prediction model?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][TEST-TO-PROVE]

**Q9.** Does extending SCM-mix curing beyond the manuscript's existing 14-day minimum measurably reduce long-term carbonation rate, and what is the practical extra curing duration that earns a meaningful reduction for an owner willing to invest the extra field time?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][METHOD]

**Q10.** Is there a real risk that a high-fly-ash-replacement mix carbonates faster per unit depth than a plain portland mix if curing is cut short, and if so what replacement rate and curing duration combination avoids it?
Lands in: Designing for Centuries. [MATERIALS/INGREDIENTS][PROBLEM-SOLUTION]

**Q11.** What field test methods (phenolphthalein spray on a core or drilled sample, at minimum) let an owner-builder directly verify actual carbonation depth on this project's own concrete at 10, 25, and 50 years, without hiring a full engineering firm each time?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [TOOLS][METHOD]

### C. Chloride Ingress

**Q12. **Which specific locations on this house (garage slab, driveway-adjacent wall, any below-grade wall near a road, any surface exposed to wind-driven salt if coastal) carry meaningful chloride exposure risk in an inland or Cascades-foothill Oregon site, versus a genuinely coastal site, and how does the exposure-class assignment change between the two?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][CODE]

**Q13.** What is the actual chloride threshold concentration at the rebar (by mass of cement or of concrete) accepted by current ACI/RILEM literature, given the range of figures found in this pre-research, and which value should the manuscript cite?
Lands in: Designing for Centuries. [CODE]
Leads: reported range 0.15-0.20% by mass of cement; verify against a single authoritative source before citing.

**Q14.** Is a portable surface-resistivity meter (AASHTO T358, roughly $330-395 reported) a realistic owner-builder purchase for QC on owner-mixed concrete, and how does an owner interpret the readings without a lab's calibration data?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [TOOLS][TEST-TO-PROVE][COST]

**Q15.** What deicing practice (rock salt versus calcium magnesium acetate versus sand-only) should this project specify for its own driveway and walks to avoid self-inflicted chloride exposure at the exact structure the whole chapter protects?
Lands in: Designing for Centuries; cross-reference Site Development. [PROBLEM-SOLUTION][MATERIALS/INGREDIENTS]

**Q16.** Where a below-grade wall sits near a septic drain field or greywater dispersal area, does effluent chemistry (not chloride specifically, but dissolved salts and nutrients generally) pose any measurable concrete-durability risk requiring its own testing, separate from the standard sulfate/chloride soil test?
Lands in: Designing for Centuries; cross-reference Water, Well, And Septic. [PROBLEM-SOLUTION][TEST-TO-PROVE]

### D. Alkali-Silica Reaction

**Q17.** What ASR testing (ASTM C1260, C1293, or C1567) should this project require before committing to any specific aggregate source, including any owner-crushed or locally pit-sourced aggregate, and what does that testing cost and take in lead time?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [TEST-TO-PROVE][COST]

**Q18.** Which Oregon aggregate sources or regions (quarries, pits, river-gravel sources) have documented ASR reactivity findings on record with ODOT or a university lab, and is that data publicly available to a residential owner-builder?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [CODE][REAL-WORLD-EXPERIENCE]
Leads: Oregon listed among 17 states with historical (1956, Mielenz) ASR occurrences; source-specific, not regional.

**Q19.** If the project's own aggregate source tests as ASR-reactive, what SCM type and replacement rate (verified via ASTM C1567 with that specific aggregate and cement) suppresses expansion to an acceptable level, and does that requirement change the cement-type or SCM-sourcing decision made for other durability reasons?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][MATERIALS/INGREDIENTS]

**Q20.** Is lithium nitrate admixture available in Oregon at residential-project quantities, at what cost, and is it a realistic mitigation path if a preferred aggregate source tests borderline-reactive?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [MATERIALS/INGREDIENTS][COST]

**Q21.** What does an actual ASR-damaged concrete element look like in the field (crack pattern, gel exudation, timeline of onset), and how does an owner distinguish it from ordinary shrinkage cracking or freeze-thaw scaling during a routine inspection?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][REAL-WORLD-EXPERIENCE]

**Q22.** Does using recycled concrete aggregate (crushed demolition concrete) in any part of this project introduce its own ASR risk profile (old, already-reacted gel present, or aggregate reactivity inherited from an unknown source), separate from virgin-aggregate testing?
Lands in: Materials, Suppliers, Procurement, And Substitution. [MATERIALS/INGREDIENTS][PROBLEM-SOLUTION]

**Q23.** For owner-made CMU or dry-cast block using locally sourced aggregate, does the smaller unit size and different compaction method change ASR risk or testing protocol compared to standard cast-in-place structural concrete?
Lands in: Owner-Made Blocks and Alternative Concretes (candidate chapter). [TEST-TO-PROVE][MATERIALS/INGREDIENTS]

### E. Sulfate Attack And Delayed Ettringite Formation

**Q24.** What water-soluble sulfate and dissolved-sulfate-in-water thresholds does ACI 318-19 Table 19.3.2.1 set for each exposure class, and what cement type or SCM combination does each class require, verified against the current adopted edition?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [CODE]

**Q25.** Should the project's already-planned septic and foundation geotechnical borings be expanded, at what marginal cost, to include water-soluble sulfate and pH testing of on-site soil and groundwater, and who performs that specific test locally in Oregon?
Lands in: Foundation and Concrete Placement; cross-reference Land, Site, And Feasibility. [TEST-TO-PROVE][COST][METHOD]

**Q26.** If the project uses any accelerated curing (steam, hot mix water, high early-strength cement) to speed owner-made block demolding, at what measured internal concrete temperature does delayed ettringite formation risk begin, and how does an owner monitor and cap internal temperature in a mass or accelerated pour without lab equipment?
Lands in: Owner-Made Blocks and Alternative Concretes; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][TOOLS][TEST-TO-PROVE]
Leads: reported 65-70°C (150-160°F) threshold, unverified pending direct ACI/RILEM citation.

**Q27.** Does the manuscript's own fast-demold, high-throughput block production ambition (the owner's flagged research vein) create a genuine DEF risk in practice at achievable field temperatures, or is that risk confined to true mass concrete and industrial precast with much larger thermal mass than a single block?
Lands in: Owner-Made Blocks and Alternative Concretes. [PROBLEM-SOLUTION][TEST-TO-PROVE]

**Q28.** What does external sulfate attack look like in progression (map cracking, expansion, softening, eventual disintegration), and over what realistic timeline does each stage occur in a moderate versus severe exposure class, so an owner doing an annual visual survey knows what stage they are looking at?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][REAL-WORLD-EXPERIENCE]

**Q29.** For any concrete water cistern or tank under the project's water-independence goal, does ACI 350's stricter crack-control and shrinkage-reinforcement requirement change the mix design, reinforcement spacing, or joint/waterstop detailing compared to an ordinary ACI 318 foundation wall, and by how much does that raise cost?
Lands in: Water Independence (candidate chapter); cross-reference Designing for Centuries. [CODE][COST][METHOD]

### F. Freeze-Thaw And Related Distress

**Q30.** What is the actual, defensible freeze-thaw exposure zone (weathering index or equivalent) for the specific build site, using NOAA climate normals or an ASTM C216-style calculation, and how does that change the air-content and durability-class specification versus a Willamette Valley baseline?
Lands in: Designing for Centuries; cross-reference Land, Site, And Feasibility. [CODE][METHOD][TEST-TO-PROVE]

**Q31.** What void spacing factor and total air content should this project specify (resolving the discrepancy between a roughly 0.20 mm and a roughly 0.25 mm target found in different sources), and how is that value verified at the truck versus verified in the hardened concrete months later?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [CODE][TEST-TO-PROVE]

**Q32.** How does over-finishing or over-troweling a slab in the field collapse the entrained air-void system near the surface, and what specific finishing-crew practice (timing, tool pressure, pass count) avoids it on an owner-built or small-crew pour?
Lands in: Foundation and Concrete Placement. [PROBLEM-SOLUTION][METHOD]

**Q33.** Which aggregate sources available to this project have documented freeze-thaw soundness data (low absorption, resistance to D-cracking) versus which are unknown or marginal, and what test (ASTM C666 on trial concrete, or a raw-aggregate soundness test) resolves an unknown source before committing to it at volume?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [TEST-TO-PROVE][MATERIALS/INGREDIENTS]

**Q34.** What does D-cracking look like in the field, how is it distinguished from ordinary surface scaling or ASR cracking during a routine owner inspection, and is it repairable or only preventable at the mix-design stage?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [PROBLEM-SOLUTION]

**Q35.** For any exposed concrete surface in the Cascades-foothill or high-desert portion of the site (a detached structure, a driveway, an exterior stair), does the freeze-thaw exposure alone justify a different (higher air content, lower w/c) mix specification than the main house's above-grade walls, and is running two mix designs on one project practical for a small pour schedule?
Lands in: Designing for Centuries; cross-reference Foundation and Concrete Placement. [METHOD][COST]

**Q36.** What is the realistic freeze-thaw durability factor (ASTM C666) achievable by an owner-mixed, hand- or small-mixer-batched concrete without a certified ready-mix plant's quality-control system, and does that gap argue for ready-mix delivery specifically for any freeze-thaw-exposed elements even if owner-mixing is used elsewhere?
Lands in: Foundation and Concrete Placement. [TEST-TO-PROVE][PROBLEM-SOLUTION]

### G. Leaching, Efflorescence, Physical Salt Attack

**Q37.** Over a genuinely multi-century horizon, does calcium leaching from continuous roof or foundation-drain water flow represent a real design concern for this specific house, or is it, as the dam-durability literature suggests, only relevant at a scale and duration this project will not reach?
Lands in: Designing for Centuries. [METHOD]

**Q38.** What does recurring efflorescence at the same location on a wall indicate about the underlying moisture path, and what is the correct owner response (trace and fix the water source, or only clean the surface)?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][METHOD]

**Q39.** Are there any locations on this specific design (a slab edge above a chronically damp base, a retaining wall face, a planter-adjacent wall) where the wick-and-evaporate geometry behind physical salt attack could occur despite Oregon's generally wet climate, and how is each identified during design review rather than discovered as a later failure?
Lands in: Designing for Centuries; cross-reference Envelope, Waterproofing, Thermal Performance, And Radon. [PROBLEM-SOLUTION][METHOD]

**Q40.** Does a penetrating silane/siloxane sealer measurably reduce leaching and efflorescence risk on exposed exterior concrete without materially affecting the wall assembly's vapor permeability, and at what reapplication interval does that protection need renewal over a multi-decade span?
Lands in: Designing for Centuries; cross-reference Envelope, Waterproofing, Thermal Performance, And Radon. [MATERIALS/INGREDIENTS][METHOD][COST]

### H. Reinforcement Corrosion Mechanics, Cover, Crack Control

**Q41.** What is the precise, citable rust-to-steel volume expansion ratio (the research found a reported 2-6x range) and which figure should the manuscript's Code entry use, sourced to a specific paper or standard rather than a range of secondary sources?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [CODE][TEST-TO-PROVE]

**Q42.** What are the precise, citable ACI 224/ACI 318 crack-width limits by exposure condition (interior, exterior, deicing-salt-exposed), and does the manuscript's existing structural chapter need a crack-width Code entry it currently lacks?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [CODE]

**Q43.** For this project's specified cover values (already in the structural chapter), what additional cover, if any, is defensible as a multi-century margin above code minimum, and at what practical cost in formwork, bar-chair spacing, and dead load?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][COST]

**Q44.** How does the Champlain Towers South forensic investigation's specific finding (measured steel-section loss from corrosion, compared against pristine bar samples) translate into a concrete, checkable lesson for this project's own below-grade and at-grade waterproofing and inspection practice?
Lands in: Designing for Centuries. [REAL-WORLD-EXPERIENCE][PROBLEM-SOLUTION]

**Q45.** What crack-control detailing (bar spacing, control-joint layout, shrinkage-and-temperature steel ratio) does this project's long concrete walls need beyond the structural-adequacy minimum, specifically to keep crack width below the exposure-appropriate durability limit rather than only below the structural-serviceability limit?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [METHOD][CODE]

**Q46.** Does an owner-buildable, low-cost half-cell potential survey (a copper/copper-sulfate reference electrode and a voltmeter) exist at a price and skill level a solo owner-builder could use for a baseline as-built corrosion-probability map, or does ASTM C876 realistically require a hired specialist every time?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [TOOLS][TEST-TO-PROVE][COST]

### I. Low-Permeability Mix Design And Verification Testing

**Q47.** Which permeability/durability verification test (RCPT, surface resistivity, or sorptivity) is the most cost-effective and practical for this project to specify on delivered ready-mix or on owner-mixed trial batches, given that a 28-day strength cylinder alone does not verify permeability?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [TEST-TO-PROVE][METHOD]

**Q48.** What RCPT or surface-resistivity target (in coulombs or in kilo-ohm-cm) should the manuscript specify as the actual durability acceptance criterion for the "long-life" mix, sourced to a specific standard's classification table rather than a general range?
Lands in: Designing for Centuries. [CODE][TEST-TO-PROVE]

**Q49.** How many additional days of moist curing, beyond the manuscript's existing 14-day SCM-mix minimum, produce a measurable additional permeability reduction, and is there a point of diminishing return where the extra owner labor is no longer worth the marginal gain?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [METHOD][PROBLEM-SOLUTION]

**Q50.** Can a small, portable surface-resistivity meter realistically be used by a single owner-builder as an in-process QC tool on their own pours (walls, slabs, owner-made block), or does electrode contact, moisture-conditioning, and calibration make it effectively a lab-only method despite the affordable hardware cost?
Lands in: Foundation and Concrete Placement. [TOOLS][TEST-TO-PROVE]

**Q51.** Does CO2 mineralization curing technology (the CarbonCure category) offer any measurable durability benefit (reduced permeability, reduced cement content at equal strength) relevant to this project, and is it available through any Oregon ready-mix supplier?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [MATERIALS/INGREDIENTS][METHOD]

### J. Supplementary Cementitious Materials

**Q52.** Given the Boardman plant closure, what is the current (2026) actual delivered cost and lead time for Class F fly ash to this project's specific build site, from the nearest regional terminal, at residential-project quantities rather than bulk-industrial quantities?
Lands in: Materials, Suppliers, Procurement, And Substitution. [COST][MATERIALS/INGREDIENTS]

**Q53.** Does a usable natural pozzolan deposit (volcanic ash, pumice, scoria) exist within practical hauling distance of the actual build site, and if so, has it ever been tested or used as a cement replacement locally?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [CREATIVE-IDEA][MATERIALS/INGREDIENTS][TEST-TO-PROVE]

**Q54.** Is metakaolin available from any Pacific Northwest supplier at residential quantities, at what cost per pound compared to silica fume, and does its lower water-demand profile make it a better fit than silica fume for owner-mixed (versus plant-mixed) concrete?
Lands in: Materials, Suppliers, Procurement, And Substitution. [MATERIALS/INGREDIENTS][COST]

**Q55.** What is the actual cold-weather early-strength penalty (in days to reach form-stripping or backfill strength) for a 25% fly ash mix versus a straight portland mix at Oregon's typical winter pour temperatures, and how does that change the project's pour scheduling?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][METHOD]

**Q56.** For owner-made block or dry-cast units specifically, which SCM (if any) is practical to add without disrupting the zero-slump, fast-demold production process, given that silica fume's high water demand and metakaolin's fineness could behave differently in a dry-cast press mix than in a wet-cast wall pour?
Lands in: Owner-Made Blocks and Alternative Concretes. [MATERIALS/INGREDIENTS][METHOD][PROBLEM-SOLUTION]

**Q57.** What ternary SCM blends (fly ash plus silica fume, or slag plus silica fume) are documented to outperform any single SCM for this project's combined durability threats (freeze-thaw, potential ASR, sulfate exposure), and is a ternary blend practical to batch consistently by hand or small mixer versus only at a ready-mix plant?
Lands in: Designing for Centuries; cross-reference Foundation and Concrete Placement. [MATERIALS/INGREDIENTS][METHOD]

**Q58.** Does using a high SCM replacement rate (30%+ fly ash or slag) measurably change the concrete's color, workability, or finishing behavior in ways an owner-builder crew needs to plan for before the first structural pour?
Lands in: Foundation and Concrete Placement. [PROBLEM-SOLUTION][REAL-WORLD-EXPERIENCE]

### K. Corrosion-Resistant Reinforcement

**Q59.** Where specifically on this house's structural drawings (by element: footing, stem wall, above-grade wall, slab edge, any water-retaining structure) does the exposure class already read "severe" under the existing manuscript table, and does that automatically justify a reinforcement upgrade at exactly those locations under a targeted (not whole-house) corrosion-resistant-rebar strategy?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [METHOD][COST]

**Q60.** Is stainless-clad or duplex-clad rebar (MMFX2/ChrōmX or equivalent) available to an Oregon residential project at what cost per linear foot, and how does its performance and price compare directly against solid Type 316 stainless for the same application?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [MATERIALS/INGREDIENTS][COST]

**Q61.** Given the documented Florida Keys epoxy-coated-rebar failure history (coating disbondment, underfilm corrosion), should this project avoid epoxy-coated rebar entirely for any severe-exposure element, or is the failure mode specific to marine splash-zone exposure and irrelevant to Oregon's mostly non-marine conditions?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [PROBLEM-SOLUTION][REAL-WORLD-EXPERIENCE]

**Q62.** What actual Seismic Design Category applies to the project's specific build site under the manuscript's existing site-to-SDC matrix, and does that rule out GFRP as primary reinforcement anywhere in the structural shell under current AC454/ACI 440.11 acceptance criteria?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [CODE]

**Q63.** Where GFRP cannot serve as primary reinforcement due to seismic category, does it remain viable for secondary elements (slab-on-grade temperature-and-shrinkage steel, a detached low-risk structure, a garden wall) elsewhere on the property, and what does that partial use save in long-term corrosion risk versus its added material cost?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][COST]

**Q64.** How does GFRP's different bond and development-length behavior (per ACI 440.11) change lap-splice lengths, hook details, and rebar spacing compared to the existing manuscript's steel-rebar lap tables, in enough detail for an engineer of record to detail a GFRP-reinforced element?
Lands in: Structural System and Concrete Design. [CODE][METHOD]

**Q65.** What is the actual bond-strength and long-term-alkaline-aging performance difference between basalt FRP and an alkali-resistant (AR-glass or ECR-glass) GFRP product, both sourced at real US suppliers, rather than the generic "E-glass GFRP" comparison found in most published research?
Lands in: Designing for Centuries. [MATERIALS/INGREDIENTS][TEST-TO-PROVE]

**Q66.** Does hot-dip galvanized rebar's reported handling-damage resistance (harder zinc coating than epoxy film) make it the more practical choice specifically for owner-builder self-placement (bending, tying, walking on top of mats) compared with epoxy-coated bar, independent of its corrosion performance?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [REAL-WORLD-EXPERIENCE][PROBLEM-SOLUTION]

**Q67.** Does mixing galvanized rebar with ordinary black steel or with stainless ties anywhere in the same structural element create a galvanic corrosion risk (the existing manuscript already flags this for mixed stainless/carbon tie wire), and what isolation practice avoids it at the design and field-tying stage?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][CODE]

**Q68.** What does a realistic mixed-reinforcement bill of materials look like for this specific house (which elements get black steel, which get galvanized, which get stainless, which if any get GFRP), and what is the total cost delta against an all-black-steel baseline?
Lands in: Designing for Centuries; cross-reference Materials, Suppliers, Procurement, And Substitution. [COST][METHOD]

### L. Cathodic Protection, Sacrificial Anodes, Corrosion Inhibitors

**Q69.** Is embedded galvanic anode protection ever specified proactively in NEW residential construction (rather than only as a later repair for already-corroding structures), and does it make sense to install anodes at this project's highest-risk locations (below-grade walls, any at-grade splash zone) at initial construction as cheap insurance?
Lands in: Designing for Centuries; cross-reference Foundation and Concrete Placement. [CREATIVE-IDEA][METHOD][COST]

**Q70.** What does a 10-20-year anode replacement program require in practice (access, disconnection, disposal of spent anodes, reconnection), and how is that documented so a future owner two or three anode-cycles from now knows the system exists and needs servicing?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [METHOD][PROBLEM-SOLUTION]

**Q71.** Does ODOT's coastal-bridge cathodic-protection program (Cape Creek, Yaquina Bay, Depoe Bay) offer any directly transferable design or installation detail for a much smaller residential-scale application, or is impressed-current cathodic protection purely an infrastructure-scale tool with no practical residential analog?
Lands in: Designing for Centuries. [REAL-WORLD-EXPERIENCE][METHOD]

**Q72.** What is the actual cost and set-time impact of calcium nitrite corrosion-inhibitor admixture at typical dosage, and does that set-time acceleration conflict with the project's existing hot-weather or cold-weather concreting practices in the foundation chapter?
Lands in: Foundation and Concrete Placement; cross-reference Designing for Centuries. [COST][PROBLEM-SOLUTION]

**Q73.** Is a migrating corrosion inhibitor a realistic, owner-applicable maintenance-phase treatment (surface-applied, no special equipment) for this project's own concrete at, say, the 25- or 50-year mark, and what does that product cost and require in surface preparation?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [METHOD][COST][MATERIALS/INGREDIENTS]

**Q74.** For a below-grade wall in contact with aggressive (sulfate- or chloride-bearing) soil confirmed by site testing, is the more cost-effective long-term strategy an upgraded reinforcement type, a corrosion inhibitor admixture, a proactive sacrificial anode, or some combination, worked out as an actual cost-per-added-service-year comparison?
Lands in: Designing for Centuries. [METHOD][COST]

### M. Self-Healing, Crystalline, Bacterial, Hydrophobic Admixtures

**Q75.** What does a crystalline admixture (Xypex, Kryton, Penetron, or equivalent) cost per cubic yard at residential quantities, and is it available through the same Oregon suppliers already sourcing this project's other admixtures?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [COST][MATERIALS/INGREDIENTS]

**Q76.** Is bacterial (Basilisk-type) self-healing concrete available for purchase or licensing by a US residential project at all, or is it currently limited to specific European demonstration projects and commercial-scale supply, making it a "watch, don't specify yet" technology for this build's actual timeline?
Lands in: Designing for Centuries. [MATERIALS/INGREDIENTS][TEST-TO-PROVE]

**Q77.** Independent of vendor marketing claims, does third-party (university or standards-body) test data show a measurable difference between a hydrophobic pore-blocking admixture and a crystalline admixture on the same concrete mix, or is the industry rivalry between the two categories overstated relative to real performance?
Lands in: Designing for Centuries. [TEST-TO-PROVE][MATERIALS/INGREDIENTS]

**Q78.** Can hot-mixed (quicklime-clast) Roman-style concrete be replicated at owner-builder scale using ordinary commercial quicklime, and does it pass this project's own alternative-materials lab-cylinder test-to-prove path for a real structural or block application, not only as a curiosity?
Lands in: Owner-Made Blocks and Alternative Concretes; cross-reference Designing for Centuries. [CREATIVE-IDEA][TEST-TO-PROVE][METHOD]
Leads: MIT/Harvard hot-mixing replication reportedly healed cracks within two weeks in lab conditions; unverified at owner-scale, and quicklime handling has its own safety requirements (exothermic reaction, causticity) needing separate research.

**Q79.** What safety precautions does quicklime (calcium oxide) handling require for an owner-builder attempting hot-mixed lime concrete or lime mortar at home scale, given its strongly exothermic and caustic reaction with water?
Lands in: Owner-Made Blocks and Alternative Concretes; cross-reference Designing for Centuries. [PROBLEM-SOLUTION][TOOLS]

**Q80.** Does adding a sticky-rice (or other amylopectin-rich starch) solution to this project's own mortar mix measurably improve density, permeability, or bond in a testable, owner-scale trial batch, and where would that trial land relative to the project's existing mortar/grout/jointing research?
Lands in: Masonry Craft; cross-reference Designing for Centuries. [CREATIVE-IDEA][TEST-TO-PROVE][MATERIALS/INGREDIENTS]

**Q81.** Is there any usable oyster-shell or other regional shell source (Oregon coast, or a seafood-processing byproduct stream) within practical reach of the build site, at what cost and in what quantity, if the project wanted to test a tabby-concrete-style lime-shell material for a non-structural or garden application?
Lands in: Designing for Centuries; cross-reference Materials, Suppliers, Procurement, And Substitution. [CREATIVE-IDEA][MATERIALS/INGREDIENTS][COST]

**Q82.** Where (if anywhere) does a deliberately unreinforced, mass, corrosion-proof-by-design concrete or masonry element make sense on this specific property (a garden wall, a root cellar, a well house, a retaining wall below a certain height), sized so it never needs steel at all and so the entire reinforcement-corrosion failure mode never applies to it?
Lands in: Designing for Centuries; cross-reference Site Development. [CREATIVE-IDEA][METHOD]

### N. Detailing For Durability

**Q83.** What exact drip-edge and coping profile (projection distance, drip-groove dimension, slope) should this project specify at every horizontal projection on the house (window sills, belt courses, the parapet coping, any roof overhang trim), consistent across the whole exterior rather than decided piecemeal per detail?
Lands in: Envelope, Waterproofing, Thermal Performance, And Radon; cross-reference Designing for Centuries. [METHOD][CODE]

**Q84.** Should this project specify a metal (aluminum or stainless) or GRP coping cap over the parapet instead of a cast concrete coping cap, given the reported cracking tendency of rigid concrete copings under thermal and freeze-thaw cycling, and what does that substitution cost against a concrete cap?
Lands in: Envelope, Waterproofing, Thermal Performance, And Radon; cross-reference Designing for Centuries. [MATERIALS/INGREDIENTS][COST][PROBLEM-SOLUTION]

**Q85.** What is the complete list of every horizontal or near-horizontal exterior ledge, sill, or setback in this project's actual architectural design, and has each one individually been checked for positive slope and its own drip edge, rather than assumed to be covered by the general wall drainage plane?
Lands in: Envelope, Waterproofing, Thermal Performance, And Radon. [METHOD][PROBLEM-SOLUTION]

**Q86.** What explicit landscaping and irrigation rule (minimum planter distance from any foundation or structural wall, no irrigation zone directly against a wall) should this project adopt at the design stage to prevent the well-documented planter-against-foundation moisture problem, and how is that rule recorded so a future owner or landscaper does not violate it decades later?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Site Development. [PROBLEM-SOLUTION][METHOD]

**Q87.** How does this project verify, at final grading and landscaping sign-off and again periodically afterward, that the as-built drainage (grade slope, downspout discharge points, perimeter drain outlets) still matches the original design intent and has not been silted, buried, or regraded out of compliance?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Foundation and Concrete Placement. [METHOD][PROBLEM-SOLUTION]

**Q88.** For any below-grade or at-grade concrete surface near the septic drain field, does the project's own effluent-dispersal design create any standing-water or capillary-wetting condition against a structural wall that the durability chapter's "avoid standing water" principle would flag as a self-inflicted risk?
Lands in: Designing for Centuries; cross-reference Water, Well, And Septic. [PROBLEM-SOLUTION][METHOD]

**Q89.** What penetrating sealer product and reapplication schedule (silane/siloxane, breathable, non-film-forming) should this project specify for exposed exterior concrete and masonry surfaces, and how is that reapplication built into the maintenance calendar already in the documentation chapter rather than left as a one-time construction step?
Lands in: Envelope, Waterproofing, Thermal Performance, And Radon; cross-reference Documentation, Maintenance, And Future Upgrades. [MATERIALS/INGREDIENTS][METHOD][COST]

### O. Service-Life Modeling

**Q90.** Can Life-365 (or an equivalent chloride service-life tool) be run, with real inputs, for this project's specific mix design and exposure conditions, and does its output (a predicted time to corrosion initiation) produce a usable, citable number for the manuscript, or only a comparative ranking between mix options?
Lands in: Designing for Centuries. [METHOD][TEST-TO-PROVE]

**Q91.** What does applying the Eurocode "100-year design working life" structural-class cover adjustment change, in inches of cover or in concrete strength class, if worked through against this project's own wall and foundation sections, even though the project's target exceeds what that system names?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][CODE]

**Q92.** Is there a way to state the project's thousand-year goal as an honest, checkable engineering position (for example: "the structural shell is designed to the most conservative severe-exposure provisions available in current code, with the added protections in this chapter, understanding that no code table or model directly verifies a thousand-year outcome") without either overclaiming code support or abandoning the goal as unstatable?
Lands in: Designing for Centuries. [METHOD]

**Q93.** What real, physical evidence (not modeled projection) exists anywhere in the world for a REINFORCED (not plain mass) concrete structure surviving multiple centuries, given that the oldest reinforced concrete structures anywhere are barely over a century old (reinforced concrete itself dates to the mid-1800s), and how does the manuscript honestly frame the fact that the specific technology (steel-reinforced concrete) has no multi-century track record yet, only engineering models and ancient UNREINFORCED precedent?
Lands in: Designing for Centuries. [METHOD]

### P. Century-Scale Inspection And Maintenance Regime

**Q94.** What would an adapted, residential-scale version of a bridge-inspection interval schedule (drawing on ODOT's own bridge inspection cycle as a starting precedent) look like for this house: what gets checked, by whom (owner versus hired professional), and how often, from year 1 through year 100 and beyond?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [METHOD][REAL-WORLD-EXPERIENCE]

**Q95.** What is the real, all-in cost and lead time for hiring a half-cell potential survey or a cover-meter/GPR scan from an Oregon materials-testing firm, for an owner who wants a professional-tier baseline reading at, say, year 10 or year 25, separate from the owner's own annual visual survey?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [COST][TOOLS]

**Q96.** What tell-tale crack-gauge product, installation method, and reading-log format should the manuscript recommend, specific enough that an owner-builder could order the exact product and start using it the week a crack is first noticed?
Lands in: Documentation, Maintenance, And Future Upgrades. [TOOLS][METHOD]

**Q97.** Is an embedded corrosion-monitoring sensor (a wireless resistivity or half-cell sensor cast into the concrete at construction time) a realistic, affordable addition for THIS project at the time of the original pour, and if so, at which specific locations (the highest-risk elements identified in section K above) does it earn its cost against periodic external testing alone, done later?
Lands in: Designing for Centuries; cross-reference Foundation and Concrete Placement. [CREATIVE-IDEA][TOOLS][COST]

**Q98.** What does the incompatible-patch-repair corrosion-cell problem require the project's documentation to record (mix design, admixtures, reinforcement type and location, by element) so that a repair performed decades from now, by someone who never met the original builder, does not accidentally create a new corrosion cell at the patch boundary?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [METHOD][PROBLEM-SOLUTION]

**Q99.** Should the manuscript's existing maintenance-reserve sinking fund (already defined in the documentation chapter for components with known replacement horizons) include a line item for the structural shell's own periodic professional inspection and any eventual repair, given that the chapter currently treats the foundation and structure as having no replacement horizon at all rather than a periodic-inspection-and-maintenance cost?
Lands in: Documentation, Maintenance, And Future Upgrades. [COST][METHOD]

**Q100.** What repair method (patch repair, electrochemical chloride extraction, re-alkalization, cathodic protection retrofit) is appropriate at each stage of corrosion damage (pre-cracking, cracked, spalled), and does the manuscript need a decision table so a future owner facing visible damage knows which repair category to even start researching?
Lands in: Documentation, Maintenance, And Future Upgrades; cross-reference Designing for Centuries. [METHOD][PROBLEM-SOLUTION]

### Q. Oregon-Specific And Site-Dependent

**Q101.** What is the actual ASTM C216-style weathering index (freezing-cycle days multiplied by average annual winter rainfall) for the specific build site's location, calculated from NOAA or Oregon State University Extension climate data, rather than a general Willamette-Valley-versus-Cascades assumption?
Lands in: Land, Site, And Feasibility; cross-reference Designing for Centuries. [METHOD][TEST-TO-PROVE]

**Q102.** Does the specific build site's distance from the coast put it in any measurable wind-driven salt-spray exposure zone, and if the answer is no (an inland site), does that fully rule out chloride exposure as a design driver, or do the self-inflicted sources (deicing salt, any calcium chloride accelerator use) still matter regardless of distance from the ocean?
Lands in: Designing for Centuries; cross-reference Land, Site, And Feasibility. [METHOD]

**Q103.** What Oregon-licensed materials-testing labs perform ASTM C1260/C1293/C1567 ASR testing, soil/groundwater sulfate testing, and surface-resistivity or half-cell surveys, at what cost and turnaround, so the manuscript can name real, callable resources rather than only the test standards?
Lands in: Materials, Suppliers, Procurement, And Substitution; cross-reference Designing for Centuries. [COST][TOOLS]

**Q104.** Does Oregon's building department review process (per the manuscript's existing permitting chapters) treat a durability-driven design choice (upgraded cover, corrosion-resistant rebar, a crystalline admixture) as a substitution requiring extra documentation, or as a straightforward exceeds-minimum design choice needing no special approval?
Lands in: Designing for Centuries; cross-reference Inspection And Approval Sequence. [CODE][METHOD]

### R. Cross-Cutting Creative And Comparative Options

**Q105.** Laid out side by side with cost, service life, and where-it-earns-its-cost for each: black steel, epoxy-coated, hot-dip galvanized, solid stainless, stainless-clad, GFRP, and basalt FRP, what single comparison table would let the owner choose per-element rather than researching each material separately?
Lands in: Designing for Centuries. [COST][METHOD]

**Q106.** What would a genuinely belt-and-suspenders "maximum durability" specification look like for this project's single highest-consequence, hardest-to-repair element (likely the footing and foundation stem wall), combining the best affordable option from mix design, SCM, cover, reinforcement type, and detailing all at once, and what would that cost against the baseline long-life spec already in the structural chapter?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [METHOD][COST]

**Q107.** Does UHPC (ultra-high-performance concrete) make sense for any single, small, high-consequence element on this project (a critical footing, a water cistern, a bond beam at a stress concentration) even if it is not practical for the whole structural shell, given its reported sub-100-year-plus service life and low permeability, and is it available in a small-batch or precast form an owner-builder could obtain?
Lands in: Designing for Centuries; cross-reference Structural System and Concrete Design. [CREATIVE-IDEA][MATERIALS/INGREDIENTS][COST]

**Q108.** Is there a real, testable, creative option for a homemade or small-batch crystalline-admixture equivalent (using the same general chemistry principles found in commercial products) that an owner-chemist-minded builder could formulate and test under the alternative-materials path, or is the proprietary chemistry genuinely not replicable outside a manufacturer's lab?
Lands in: Owner-Made Blocks and Alternative Concretes; cross-reference Designing for Centuries. [CREATIVE-IDEA][TEST-TO-PROVE]

**Q109.** Across every durability technology gathered in this research (SCMs, corrosion-resistant rebar, crystalline admixtures, cathodic protection, sealers, detailing), which ones are genuinely additive (worth stacking together) and which are redundant (two ways of solving the same specific threat, where specifying both wastes money without adding protection)?
Lands in: Designing for Centuries. [METHOD][COST]

**Q110.** Does the manuscript's existing prescriptive-versus-engineered structural path decision (already in the structural chapter) change at all if durability is weighted as heavily as the seismic and gravity load path, given that several of the strongest durability options (GFRP, targeted stainless, an ACI 350-grade water structure) assume or require an engineer of record regardless of which structural path is otherwise chosen?
Lands in: Structural System and Concrete Design; cross-reference Designing for Centuries. [METHOD]

---

File path: `C:/Users/jon/Projects/theBook/revision7/needs_researching_third_wave/drafts/I_designing_for_centuries_durability.md`
