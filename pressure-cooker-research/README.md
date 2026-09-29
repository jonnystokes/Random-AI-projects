# Pressure Cooker Research: Stage 1 (Trait Study)

Purpose of this stage: understand every trait a pressure cooker has, what each trait
does to food, and which traits matter for turning a freezer full of old laying hens
into tender meat. No cookers are recommended or ranked in this stage. Model names
appear only as examples of what a trait looks like in the real world.

Owner brief that drove this research:

- Three controllable variables: pressure, how fast pressure builds, and temperature.
- Wants the option of a lower temperature "slow cook under pressure" mode.
- Wants to know the PSI and temperature ranges cookers come in, and their minimums.
- Wants the optimal pressure and temperature for tenderizing old, tough meat.
- Wants the best fast strategy and the best patient strategy for the softest meat.
- Stock: a year's worth of retired laying hens, already frozen.
- Leaning toward a plug-in (electric) cooker for safety.
- Follow-up request: include information about Instant Pots.

## Files

| File | What it covers |
|---|---|
| [01-trait-study.md](01-trait-study.md) | Every trait: pressure, temperature, ramp rate, release modes, minimum ranges, altitude, capacity, pot material, lids, safety systems, certifications, recall record, maintenance |
| [02-tough-meat-science.md](02-tough-meat-science.md) | Collagen science, time and temperature trade-offs, fast vs slow vs pressure, old-hen specifics, thaw rigor and frozen birds, broth |
| [03-instant-pot-notes.md](03-instant-pot-notes.md) | Instant Pot company history, model line, measured specs, safety mechanisms, recall record, known weaknesses |
| [data/pressure-temperature-table.csv](data/pressure-temperature-table.csv) | Gauge pressure to steam temperature, computed from the Antoine equation for water |
| [data/cooker-traits.csv](data/cooker-traits.csv) | Spec sheet of representative electric and stovetop cookers used as trait examples |
| [data/collagen-time-temperature.csv](data/collagen-time-temperature.csv) | Time-to-tender at each cooking temperature, from the sources cited |
| [data/old-hen-cook-reports.csv](data/old-hen-cook-reports.csv) | Real-world reports of pressure cooking old hens: time, setting, result |
| [sources.md](sources.md) | Every source used, grouped by topic, with notes on reliability |

## Ten-line summary

1. Pressure and temperature are not independent in a pressure cooker. Steam pressure sets the temperature. 15 psi is 250°F, 12 psi is 244°F, 7 psi is 232°F, 1.5 psi is 217°F. Nothing under pressure cooks below 212°F.
2. Stovetop cookers run at 15 psi. Almost all electric cookers top out at 10 to 12 psi. One discontinued electric line reached 15 psi.
3. The lowest pressure setting on typical electrics is 5.5 to 7 psi (about 229 to 233°F). The lowest on any electric found is 1.5 psi (about 217°F, Breville Fast Slow Pro). Some budget electrics have only one pressure level.
4. A true "low temperature" cook (145 to 205°F) happens only in non-pressure modes: slow cook, sous vide, or a custom keep-warm hold. Multi-cookers with a sous vide or custom temperature mode give the widest range (roughly 104 to 194°F on Instant Pot Pro, 102 to 356°F on Zavor LUX LCD).
5. Ramp rate is set by wattage, liquid volume and pot size. A 6 quart electric takes 8 to 15 minutes to reach pressure, an 8 quart 15 to 20. Stovetops can be up to three times faster. Ramp time is also cooking time, so it matters for recipe consistency more than for tenderness.
6. Collagen becomes gelatin from about 160°F up. Rate roughly doubles every 10 to 15°F. Fork-tender takes about 25 hours at 160°F, 6 hours at 185°F, 2.6 hours at 205°F, and 30 to 90 minutes at 240 to 250°F.
7. Higher temperature squeezes more water out of muscle fibers. Pressure gives the fastest tenderness with the most moisture loss. Low-temperature holds give the juiciest tenderness but need 12 to 72 hours. Meat from older animals needs a higher temperature or longer time than young meat to reach the same tenderness.
8. For old hens in a hurry: high pressure, natural release, 30 to 45 minutes for meat that holds together, 60 to 100 minutes for fall-apart shredding meat and broth. Quick release makes meat stringy.
9. For old hens with patience: hold dark meat at 165 to 175°F for 12 to 24 hours (sous vide or a custom temperature mode), or simmer at 185 to 200°F for 4 to 6 hours. Breast meat on an old hen will never be juicy under any method; plan to shred or chop it.
10. Birds frozen right after slaughter without a 24 to 48 hour rest can suffer "thaw rigor" and cook up tougher. Thaw slowly in the fridge and rest the thawed bird a day or two before cooking.
