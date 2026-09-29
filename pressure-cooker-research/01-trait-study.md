# 01. Pressure Cooker Trait Study

This document describes each trait a pressure cooker can have, what the trait does to
food, what values exist on the market, and which values matter for tenderizing old,
tough meat. Model names are used only as examples of a trait. Source links are in
[sources.md](sources.md).

Contents

1. How a pressure cooker works (why pressure and temperature are one dial)
2. Trait: working pressure (PSI)
3. Trait: minimum pressure and number of pressure levels
4. Trait: temperature in non-pressure modes (slow cook, sous vide, keep warm)
5. Trait: ramp rate (time to reach pressure)
6. Trait: pressure release method
7. Trait: altitude behavior
8. Trait: capacity and fill limits
9. Trait: inner pot material
10. Trait: lid design
11. Trait: control and programmability
12. Trait: safety systems, certification, and recall history (electric vs stovetop)
13. Trait: maintenance and consumables
14. Trait: canning claims
15. Trait scorecard for the old-hen use case

---

## 1. How a pressure cooker works

A pressure cooker is a sealed pot. Water inside boils, the steam cannot escape, and
the pressure rises above atmospheric. At higher pressure water boils at a higher
temperature, so the food cooks in liquid and steam hotter than 212°F.

The key physical fact for this study: **the temperature inside a pressure cooker is
set by the pressure, and nothing else.** Saturated steam at a given gauge pressure has
one temperature. The heating element does not choose a temperature; it adds heat
until the pressure sensor says "enough," and the temperature follows.

Gauge pressure to steam temperature at sea level (computed from the Antoine equation
for water; full table in `data/pressure-temperature-table.csv`):

| Gauge psi | °C | °F | Where you see it |
|---:|---:|---:|---|
| 0 | 100 | 212 | Open pot, simmer |
| 1.5 | 102.6 | 217 | Lowest setting on Breville Fast Slow Pro |
| 3.0 | 105.2 | 221 | Breville "Dessert" preset |
| 5.8 | 109.6 | 229 | Bottom of Instant Pot "Low" band |
| 7.2 | 111.6 | 233 | Top of Instant Pot "Low" band; Ninja Foodi "Low" |
| 9.0 | 114.0 | 237 | Breville "Poultry" and "Soup" presets |
| 10.2 | 115.5 | 240 | Bottom of Instant Pot "High" band |
| 11.6 | 117.2 | 243 | Top of Instant Pot "High" band; Ninja Foodi "High" |
| 12.0 | 117.7 | 244 | Breville max; typical "electric high" |
| 12.3 | 118.0 | 245 | Instant Pot Max "High" |
| 15.0 | 121.1 | 250 | Stovetop standard; Instant Pot Max "Max" |

Rule of thumb: about 2.5°F per psi in this range.

Consequences:

- There is no such thing as pressure cooking below 212°F. "Low pressure" means 217 to
  233°F, not 180°F.
- If the goal is a slow, low-temperature cook (say 160 to 200°F), that is a
  **non-pressure mode** (slow cook, sous vide, keep warm, or custom temperature). The
  pressure lid may still be on, but the valve is venting and there is no pressure.
- The owner's three variables collapse to two under pressure: pressure (which sets
  temperature) and ramp rate. Temperature becomes an independent variable only in
  non-pressure modes.

## 2. Trait: working pressure (PSI)

**What it does.** Higher pressure means higher temperature, which speeds every heat
driven reaction: collagen conversion, starch gelatinization, flavor extraction, and
also the squeezing of water out of muscle fibers. A 15 psi cooker at 250°F cooks
noticeably faster than a 12 psi cooker at 244°F. Common guidance is to add about 10%
time at 12 to 13 psi, 20% at 8 to 9 psi, and up to 25% when converting a 15 psi
recipe to an 11 to 12 psi electric.

**Ranges found on the market.**

| Class | Typical working pressure | Steam temperature | Notes |
|---|---|---|---|
| Stovetop, modern (Fissler, Kuhn Rikon, Presto, etc.) | 15 psi high; many have a 8 to 10 psi low | 250°F high | The user regulates heat; the cooker regulates pressure by weight or spring |
| Electric multi-cooker, mainstream | 10.2 to 12 psi "High"; 5.5 to 7.2 psi "Low" | 240 to 244°F high; 229 to 233°F low | Instant Pot Duo, Duo Plus, Pro; Ninja Foodi; Zavor; Crock-Pot Express; most others |
| Electric, budget single-level | About 10 to 12 psi, one level | About 240°F | Instant Pot Rio (high only); many store brands |
| Electric, adjustable | 1.5 to 12 psi in 0.5 or 1.5 psi steps | 217 to 244°F | Breville Fast Slow Pro (8 levels) |
| Electric, high pressure | 15 psi "Max", 12.3 psi "High", 6.5 psi "Low" | 250 / 245 / 230°F | Instant Pot Max (discontinued); Instant Pot Pro Max (Wi-Fi, 15 psi) |
| Electric pressure canner | 15 psi sustained | 250°F | Presto Precise Digital Canner (a canner first, a cooker second) |

Instant Pot's manual states the bands: Low 5.8 to 7.2 psi (30 to 50 kPa), High 10.2
to 11.6 psi (70 to 90 kPa), and notes a maximum safety pressure of about 15.2 psi
that the unit will vent at. The working pressure cycles inside the band, so the
temperature also cycles by a few degrees.

**Does the 15 vs 12 psi gap matter for tough meat?** Only for speed. Both are far
above the temperature at which collagen converts. The difference is roughly a 20 to
25% time change. For tenderness quality, the release method and total time matter
more than the last 3 psi.

**Marketing caution.** "Reaches 15 psi" on an electric often means the safety limit,
not the working pressure. The Instant Pot Max was the only mainstream electric that
sustained 15 psi as a working pressure, and it was discontinued; its Wi-Fi successor
(Pro Max) advertises 15 psi again. Treat any 15 psi claim on an electric as "verify
in the manual's specification table."

## 3. Trait: minimum pressure and number of pressure levels

**What it does.** A lower pressure level is a lower temperature (see table). Lower
pressure is used for delicate foods (eggs, fish, soft vegetables) and for canning
high-acid foods. For tough meat, a lower pressure just means a longer cook at a
slightly lower temperature; it does not produce a fundamentally different result
because 229°F and 244°F are both far above the collagen threshold.

**Minimums found.**

| Cooker | Lowest pressure setting | Steam temp | Number of levels |
|---|---:|---:|---:|
| Breville Fast Slow Pro | 1.5 psi | ~217°F | 8 (1.5 to 12 psi) |
| Instant Pot Max | 6.5 psi | ~231°F | 3 (6.5 / 12.3 / 15) |
| Instant Pot Duo, Duo Plus, Pro | 5.8 to 7.2 psi band | ~229 to 233°F | 2 |
| Ninja Foodi (OP/FD/OL series) | 7.2 psi | ~233°F | 2 |
| Zavor LUX LCD | "Low" (psi not published) | not published | 2 |
| Instant Pot Rio, most budget units | none below High | ~240°F | 1 |

**The "slow cook under pressure" idea.** The lowest pressure cooking temperature
available on any electric found is about 217°F (1.5 psi). That is only 5°F above an
open simmer. If the owner wants "still under pressure but gentler," the useful range
is 1.5 to 7 psi (217 to 233°F), and the only electric that goes below about 5.8 psi
is the Breville. Whether that band is worth anything for old hens is discussed in
[02-tough-meat-science.md](02-tough-meat-science.md); short answer: a small benefit
in moisture retention at a large cost in time, and a true low-temperature hold in a
non-pressure mode does the job better.

**Reviewer consensus on low pressure.** Wirecutter staff who use Instant Pots weekly
could not recall using the low setting. It is rarely used in published recipes. That
is not a reason to skip it, only a note that recipes will assume High.

## 4. Trait: temperature in non-pressure modes

This is where the owner's "lower temperature" wish actually lives. Each multi-cooker
carries several non-pressure heating modes with fixed or adjustable temperatures.

**Slow cook mode.**

| Cooker | Settings and stated temperature |
|---|---|
| Instant Pot (Duo family, Pro) | Less 180 to 190°F, Normal 190 to 200°F, More 200 to 210°F (labelled Low/High on newer units) |
| Breville Fast Slow Pro | LO 194°F (90°C), HI 203°F (95°C), 2 to 12 hours |
| Zavor LUX LCD | LOW 190°F, HIGH 212°F |
| Ninja Foodi | LO and HI, temperatures not published |
| Traditional slow cookers (measured, three models) | Low settled at 165 to 187°F; High at 196 to 208°F; Warm at 160 to 202°F depending on brand |

Notes:

- Traditional slow cookers do not hold a fixed temperature. Both Low and High
  climb toward a simmer (about 209°F); Low just takes longer to get there (7 to 8
  hours vs 3 to 4). Measured units vary widely by brand.
- Instant Pot's slow cook mode is widely reported to run cooler and slower than a
  Crock-Pot on the same label, and its sealed lid prevents the evaporation a slow
  cooker recipe expects. Fixes people use: run "More"/High, reduce liquid 15 to 20%,
  or use a vented glass lid. Instant Pot's own manual warns that slow cook runs under
  3 hours "will result in uncooked food."
- Breville's slow cook holds at two fixed temperatures with dual sensors, which is
  closer to a true thermostat than the "heat until simmer" behavior of a Crock-Pot.

**Sous vide mode.** Some multi-cookers hold the water bath at a set temperature.
The food goes in a sealed bag, or, for a stewing hen, can simply sit submerged in
the liquid (that is a "low-temperature poach," which works the same way for
collagen).

| Cooker | Sous vide range | Precision |
|---|---|---|
| Instant Pot Pro, Pro Plus, Duo Plus (SV models) | 104 to 194°F (40 to 90°C); presets Chicken 140°F, Beef 130°F, Egg 145°F; up to 99.5 hours | manual states ±1°C on Max |
| Instant Pot Max | from 120°F, up to 99.5 hours | ±1.8°F stated |
| Zavor LUX LCD "Flex" | 102 to 356°F | not stated |
| Breville Fast Slow Pro | no sous vide mode | n/a |
| Ninja Foodi (select models) | sous vide mode on newer OL/FD units | not stated |

**Keep warm mode.** Instant Pot Pro lets you set Keep Warm to a custom 144 to 194°F
for up to 10 hours. That is, in effect, a second sous vide mode. Most other cookers
fix Keep Warm at about 145 to 172°F.

**Why this matters for the owner.** A multi-cooker with an adjustable sous vide or
custom keep-warm mode can hold a whole old hen in broth at 165 to 175°F for 12 to 24
hours. That is the low-temperature slow cook the owner described, and it is the
method the meat science favors for maximum juiciness (see document 02). It is not
"under pressure," but the meat does not know the difference: only temperature and
time act on collagen.

## 5. Trait: ramp rate (time to reach pressure)

**What sets it.** Heating element wattage, the mass of food and liquid, the pot's
starting temperature, and the pot's diameter (a wider base heats faster on the same
element). Stovetops are faster because a burner delivers more power than a 1000 to
1460 W element.

**Wattage examples (6 quart unless noted).**

| Cooker | Watts |
|---|---:|
| Instant Pot Duo, Duo Plus, Rio (6 qt) | 1000 |
| Instant Pot 3 qt models | 700 |
| Breville Fast Slow Pro | 1100 |
| Instant Pot Pro, Pro Max, 8 qt Duo/Duo Plus, Rio Wide 7.5 qt | 1200 |
| Zavor LUX LCD 8 qt | 1300 |
| Ninja Foodi Pro 6.5 qt | 1460 |
| Ninja Foodi 8 qt SMART XL | 1760 |

**Measured time to pressure.**

- 6 quart electric with 1 to 2 cups of liquid: 8 to 15 minutes. 3 quart: 5 to 10.
  8 quart: 15 to 20.
- Reviewer tests: Instant Pot Duo Plus and Pro under 8 minutes; Zavor LUX under 9;
  Ninja Foodi 9 or more; Breville roughly 20 minutes reported in one rice test.
- Consumer Reports: electrics sometimes take almost three times longer than stovetops
  to reach pressure.
- A full pot of cold stock or a frozen bird can push an electric to 25 to 40 minutes
  before the timer even starts.

**Does ramp rate matter for tenderness?** Not much, and where it does, the effect is
mild. During the ramp the food sits between 180 and 212°F, which is active cooking.
A slow ramp adds unlogged cook time; a fast ramp subtracts it. The natural release
adds another 10 to 25 minutes of cooking at falling temperature. So a recipe's "45
minutes at high pressure" is really 70 to 90 minutes of heat, and the exact split
depends on the cooker. What ramp rate affects:

- Repeatability: a cooker that ramps consistently gives consistent results.
- Convenience: total time to dinner.
- Scorching risk: high wattage with thick liquid can burn the bottom before pressure
  builds (Instant Pot's "Burn" warning, Breville's ceramic pot).

**Adjustability.** No consumer electric exposes ramp rate as a user setting. It is
fixed by design. The only levers are wattage (choose the model), starting with hot
liquid, and using less liquid.

## 6. Trait: pressure release method

**Options.**

- Natural release (NR): turn off heat, wait 10 to 30 minutes for pressure to fall
  on its own. Food keeps cooking at falling temperature.
- Quick release (QR): open the valve; pressure drops to zero in about a minute and
  the liquid temperature crashes from about 244°F to 212°F almost instantly.
- Pulse or intermittent release: short bursts, used to avoid foaming and sputtering.
- Timed hybrid: 10 to 15 minutes natural then quick.

**Effect on meat.** Quick release after a meat cook makes the moisture inside the
muscle flash to steam and tear outward; the result reads as grainy, dry, or stringy.
Natural release lets the juices cool and settle. Every meat-focused source agrees on
natural release for meat, with one softener: meat fully submerged in liquid is less
affected by a quick release than meat sitting above the liquid.

**Automation as a trait.** Breville's cooker executes the chosen release
automatically at the end of the cycle (Auto Quick, Auto Pulse, Natural) and its
presets carry a default release per food (Meat and Stock default to Natural, Poultry
to Auto Pulse). Instant Pot Max and Pro Plus also automate release. Instant Pot Pro
adds "QuickCool," an ice tray on the lid to speed a natural release without a quick
vent. Standard Duo-class units require a hand on the valve for quick release.

For old hens: natural release is mandatory. An automatic natural release is a
convenience, not a requirement, since natural release just means "do nothing."

## 7. Trait: altitude behavior

A pressure cooker adds its gauge pressure on top of the ambient air pressure. At
altitude the ambient is lower, so the absolute pressure and therefore the
temperature inside are lower for the same setting. Colorado State University
extension guidance for electrics: add 5% cook time per 1,000 ft above 2,000 ft;
consider 2 to 4 tablespoons more liquid per cup; allow 5 to 10 minutes of natural
release even when a recipe says quick. Their testers found the adjustment mostly
mattered for beans, rice, and yogurt, less for meat.

Breville is the only electric found with an explicit altitude setting (1,000 to
6,000 ft in 1,000 ft steps; not to be used above 6,500 ft). Others require the user
to add time.

## 8. Trait: capacity and fill limits

- 6 quart: fits one 5 to 6 lb bird; minimum liquid for pressure about 1.5 cups.
- 8 quart: fits two birds or one bird plus lots of broth; usable fill about 6 quarts
  of liquid; minimum liquid about 2 cups; slower to pressure; heavier.
- Never fill above the 2/3 line (1/2 for foamy foods like beans). A whole stewing hen
  plus enough water to cover it approaches the line in a 6 quart.
- Wide-format pots (Instant Pot Rio Wide 7.5 qt) trade height for a larger searing
  surface; a whole bird still fits.
- Two-stage cooking (meat first, then bones back for broth) fits easily in 6 quart.

## 9. Trait: inner pot material

- Stainless steel (most Instant Pot, Zavor): durable, non-reactive with wine and
  vinegar, dishwasher and scrub safe, sears well, food can stick when sautéing.
- Ceramic non-stick (Breville, Ninja, some Instant Pot): easy release, but coatings
  wear, cannot take metal utensils or steel wool, and sear poorly. Replacement pots
  cost money.
- Tri-ply stainless bases spread heat and reduce scorching during the ramp.

For a stewing hen the material is irrelevant to tenderness; it matters for durability
over a year of weekly use and for deglazing after browning.

## 10. Trait: lid design

- Removable drop-in lid (Instant Pot Duo/Pro/Rio, Zavor): easy to wash, easy to swap
  for a glass lid in slow cook mode, condensation drips when lifting.
- Hinged lid (Breville, some Ninja): stays attached, some users find it awkward for
  right-handed use, spills condensation when opened.
- Dual-lid air fryer combos (Instant Pot Duo Crisp, Ninja Foodi): a second lid or a
  hinged air fry lid; more parts, more to clean.
- Sealing ring: silicone, absorbs odors, stretches with use. Instant Pot recommends
  replacement every 12 to 18 months (6 to 12 if used daily). Keep a spare.
- Lid lock and pressure indicator: the float pin must drop before the lid opens. See
  section 12 for what goes wrong when it does not.

## 11. Trait: control and programmability

- Preset buttons vs manual: every electric has a manual pressure cook mode with time
  and pressure level. Presets are conveniences. Some cookers let you save favorites
  (Instant Pot Pro "Fav 5").
- Maximum pressure cook time: Instant Pot 4 hours per run; Breville 2 hours per run.
  A 90 minute stewing hen is inside both. Back-to-back runs work for long broth.
- Maximum slow cook or sous vide time: Instant Pot 99.5 hours.
- Delay start: on all major electrics. Do not use with raw poultry sitting at room
  temperature for hours.
- Display feedback: Breville shows pressure, temperature and status; Instant Pot Pro
  shows a progress bar; Duo shows only the countdown.
- Wi-Fi app control (Instant Pot Pro Plus, Pro Max) is a convenience trait, not a
  cooking trait.
- Sensors: Breville advertises dual sensors (top and bottom) for temperature and
  pressure. Instant Pot uses a pressure switch and a thermistor in the base.

## 12. Trait: safety systems, certification, and recall history

**Why electric is considered safer.** An electric cooker manages heat itself. It
will not keep adding energy after the target pressure is reached, it will not boil
dry unnoticed, and it cannot be walked away from on a live burner. A stovetop cooker
depends on the cook to modulate heat and to notice the regulator. UL's analysis of
injury reports found most stovetop injuries involved experienced users ignoring the
manual. Electric cookers also add sensors and interlocks a stovetop lacks.

**Typical electric safety stack (Instant Pot lists ten).** Lid lock under pressure;
lid position detection (will not start if the lid is misaligned); pressure switch
that cuts heat above the band; temperature control that cuts heat on over
temperature; primary steam release valve; anti-block shield over the vent;
leaky-lid detection (will not build pressure if the ring is missing or the valve is
open); a pressure-relief path that pushes the inner pot down and vents around the
rim if everything else fails; electrical fuse; thermal fuse.

**Certification.** Look for UL or ULC listed (North America), or ETL. Absence of a
listing on a cheap import is a reason to walk away.

**The failure mode that actually hurts people: lids that open under pressure.**
Every major electric recall since 2020 has been the same defect: the lid could be
unlocked or came off while the pot was still pressurized, ejecting hot food.

| Year | Brand and model | Units (US) | Reported injuries |
|---|---|---:|---|
| Nov 2020 | Sunbeam Crock-Pot Express Crock SCCPPC600-V1 | ~914,000 | 99 burn injuries, 119 lid detachments |
| Aug 2023 | Sensio (Bella, Cooks, Crux, etc.) | ~860,000 | lid unlocks during use |
| Oct 2023 | Best Buy Insignia | ~930,000 | 31 incidents, 17 burns |
| May 2025 | SharkNinja Ninja Foodi OP300 series | ~1.8 million | 106 burn reports, 50 second or third degree, 26 lawsuits |
| Oct 2025 | ALDI Ambiano | ~46,000 | 8 severe burns |

A Colorado jury awarded $55.5 million against Sunbeam in December 2024 (reduced to
$9.1 million in June 2025). Instant Pot has faced individual lawsuits on the same
theory but has had no recall of a pressure cooking lid; its two recalls were a 2015
Smart-60 electric shock issue (about 1,140 units) and a 2018 Gem 65 multicooker (not
a pressure cooker) that overheated (about 104,000 units). Details in document 03.

**What this means as a trait.** The safety trait to inspect is the lid interlock:
a mechanical float pin that physically blocks the lid from turning until pressure is
gone, plus a lid-position sensor that stops the heater if the lid is not fully
locked. Ask, for any candidate: has this exact lid design been recalled, and can the
lid be forced open against the float pin. The other nine mechanisms rarely matter;
this one is the whole game.

**Stovetop, for completeness.** Modern stovetops (spring valve, multiple relief
paths, lid interlock) are safe when used per the manual, and they run at 15 psi with
a faster ramp. The owner's preference for electric is well founded on the "walk away
from it" argument, not on any inherent explosive risk of a modern stovetop.

## 13. Trait: maintenance and consumables

- Sealing ring: replace every 12 to 18 months; sooner with daily use; keep one for
  savory and one for sweet.
- Steam release valve and anti-block shield: remove and wash after every meat cook;
  replace the valve every 12 to 18 months or if it cracks.
- Float valve gasket: small silicone part, easy to lose in the dishwasher.
- Inner pot: stainless lasts indefinitely; ceramic coatings wear in one to three
  years of heavy use.
- Parts availability: a brand with a large installed base has cheap third-party
  rings and pots. Brand ownership changes (Instant Brands went through Chapter 11 in
  2023 and re-emerged as Instant Pot Brands in 2024) have not so far affected parts
  supply, but it is worth noting for a purchase meant to last years.

## 14. Trait: canning claims

Not the owner's question, but it comes up on spec sheets because "canning" is often
listed as a feature. USDA, the National Center for Home Food Preservation, and
extension services do not recommend any electric pressure cooker or electric canner
for low-acid foods (meat, including chicken) because none has been independently
validated to reach the required temperature throughout the jars. Instant Pot's own
site now limits the Max to water-bath canning. Presto's electric canner claims to
meet USDA guidelines but has not been independently tested as of the latest
extension statements. A year of frozen hens is a freezer plan, not a canning plan,
so this trait can be ignored.

## 15. Trait scorecard for the old-hen use case

| Trait | Matters how much | What to look for |
|---|---|---|
| High pressure level | Medium | 10 to 12 psi is enough; 15 psi saves 20% time |
| Low pressure level | Low | Nice to have; rarely used |
| Very low pressure (1.5 to 5 psi) | Low | Only Breville; marginal benefit |
| Adjustable non-pressure temperature (sous vide / custom keep warm) | High | 160 to 195°F range, adjustable in 1°F steps, 24+ hour timer |
| Slow cook that actually holds 185 to 200°F | Medium | Breville and Zavor state fixed temps; Instant Pot runs cool |
| Ramp rate | Low for tenderness, Medium for convenience | 1000 W or more at 6 qt; 1200 W or more at 8 qt |
| Natural release (auto or manual) | High | Any cooker; automation is convenience |
| Capacity | Medium | 6 qt fits one hen; 8 qt for two or a hen plus a lot of broth |
| Lid interlock integrity and recall record | High | Float-pin interlock, UL/ULC listing, no lid-opening recall on the exact lid design |
| Stainless inner pot | Medium | Durability over a year of weekly use |
| Pressure cook max time per run | Low | 2 hours is enough; 4 hours convenient for broth |
| Altitude adjust | Depends on where the owner lives | Only Breville has it; others need manual time additions |
| Canning | None | Ignore |
