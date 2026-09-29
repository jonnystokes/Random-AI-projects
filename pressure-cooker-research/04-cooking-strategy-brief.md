# 04. Cooking Strategy Brief: How the Methods Fit Together

Short answers to the owner's questions after reading the Stage 1 research.
Graph: [figures/tenderness-map.png](figures/tenderness-map.png)
(script: `figures/make_tenderness_map.py`).

## The one idea that explains everything

Two things happen to meat in hot liquid, on two very different clocks.

1. **Muscle fibers contract and squeeze out juice.** This is fast. Once the meat is
   above about 150°F it has already happened, within minutes. Every method in this
   study (boil, slow cook, pressure, and even a 165°F hold) does this. It is what
   makes meat firm.
2. **Collagen (the connective tissue) melts into gelatin.** This is slow, and the
   speed depends on temperature. Until it finishes, the meat is rubbery. When it
   finishes, the meat is tender and falls apart.

"Rubbery" is the state in between: fibers already tight, collagen not yet melted.
It is not caused by boiling. It is caused by **stopping before the collagen is
done**. A hen boiled for 45 minutes is rubbery. The same hen boiled for 4 hours is
a stewing hen, and falls off the bone. The all-day slow cook works for exactly one
reason: it runs long enough.

## So how does a pressure cooker help?

It runs the same collagen reaction at 240 to 250°F instead of 200 to 212°F, and the
reaction speed roughly doubles for every 15°F. That turns 4 hours into 45 to 90
minutes. That is the whole benefit: **time**. It does not make the meat more tender
than a long simmer; it gets to the same tender endpoint much sooner.

## Does higher pressure make it tougher?

No. Higher pressure makes it tender **faster**, with two side effects:

- **Drier.** Hotter fibers squeeze out a little more juice. Pressure-cooked meat is
  the driest of the liquid methods, and if you run it well past tender the dry
  fibers separate into strings. That is the "stringy" complaint, and it is an
  overshoot problem, not a pressure problem.
- **Less forgiving.** At 244°F the window between "still rubbery" (30 minutes) and
  "tender and intact" (45 minutes) and "falls apart" (90 minutes) is narrow. At
  200°F the same window is spread across hours, so it is hard to miss.

## Where does 1.5 psi fit? Isn't that just boiling?

Nearly. 1.5 psi is 217°F, only 5°F above a boil. It behaves like a slightly faster
simmer: tender in roughly 2.5 hours instead of 3 to 4, with about the same juiciness
as a simmer. It is not rubbery in the long run for the same reason boiling is not
rubbery in the long run. It sits on the graph right next to the boil point, a
little lower. Nothing magic happens there. The gentle end of pressure cooking (1.5
to 7 psi, 217 to 233°F) buys a small juiciness gain at the cost of roughly doubling
the time versus high pressure.

## Where does slow cooking fit?

A slow cooker on Low or High ends up at 185 to 209°F, a bare simmer. It is a boil
that takes longer to get there. All-day slow cooking works because it is 8 to 12
hours in the tender zone, not because the temperature is special. Its advantages:
forgiving, hands-off, moderate juiciness. Its cost: the day.

## The real gradient (all liquid methods, cooler to hotter)

| Method | Temperature | Time to tender (old hen) | Juiciness |
|---|---:|---:|---|
| Sous vide or low hold | 143°F | ~3 days | Best |
| Low hold | 165 to 175°F | 12 to 24 h | Best |
| Slow cooker, simmer | 185 to 212°F | 4 to 12 h | Moderate |
| Very low pressure | 217°F (1.5 psi) | ~2.5 h (estimated) | Moderate |
| Low pressure | 230°F (~6 psi) | 75 to 90 min (estimated) | Lower |
| Electric high pressure | 244°F (~12 psi) | 45 min intact, 90 min falls apart | Lowest |
| Stovetop pressure | 250°F (15 psi) | ~35 min | Lowest |

The only place on the gradient where juiciness changes a lot is **below about 175°F**.
Between 185 and 250°F the fibers are all fully contracted, so the juiciness
difference across that whole range (slow cooker to stovetop pressure) is small.
The big juiciness prize is a 165 to 175°F hold for 12 to 24 hours, which no pressure
setting can reach and which needs a sous vide or custom-temperature mode.

## What this means in practice

- **Hurry:** high pressure, 45 minutes for pieces, 90 for shredding, natural release.
- **Weekday, hands-off:** slow cooker or the cooker's slow mode, 8 to 12 hours.
- **Best possible:** 165 to 175°F hold for 12 to 24 hours (sous vide or custom
  keep-warm mode), then a short pressure run for the broth if wanted.
- **Never:** quick release on meat, or pulling a pressure cook at 30 minutes because
  it looks done. If it is rubbery, it needs more time, not less heat.
