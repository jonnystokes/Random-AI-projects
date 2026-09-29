"""Time-to-tender vs cooking temperature for an old laying hen, all liquid methods.

Curve: t(T) = 0.75 h * 2^((244 - T)/15), a doubling every 15 F, fitted through the
reported old-hen points (45 min at 244 F, ~5 h at 200 F, 18 h at 167 F, 72 h at 143 F).
Colors and marks follow the dataviz reference palette (ordinal blue ramp for juiciness).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter

SURF, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
J = {"juiciest": "#104281", "moderate": "#2a78d6", "driest": "#86b6ef"}   # ordinal blue ramp, validated
TENDER_FILL = "#eef4fc"

def t_tender(T):  # hours
    return 0.75 * 2 ** ((244 - T) / 15)

pts = [  # (temp F, hours, juiciness, label, dx, dy, ha)
    (143, 72,  "juiciest", "Sous vide 143°F, 3 days\n(stewing-hen legs)",          8, -2,  "left"),
    (167, 18,  "juiciest", "Low hold 167°F, 18 h\n(old-animal research)",          6,  0,  "left"),
    (176, 10,  "moderate", "Confit / hold 176°F,\n8–12 h",                        -6,  0,  "right"),
    (195, 11,  "moderate", "Slow cooker LOW,\nwhole hen 10–12 h",                  6,  0,  "left"),
    (200, 5,   "moderate", "Slow cooker / simmer,\npieces 4–6 h",                  6,  0,  "left"),
    (212, 3.5, "moderate", "Boil or simmer 212°F,\n3–4 h",                         6,  0,  "left"),
    (217, 2.6, "moderate", "1.5 psi (217°F),\n~2.5 h (estimated)",                -6, -6,  "right"),
    (230, 1.4, "driest",   "Low pressure 230°F,\n75–90 min (estimated)",           -6,  0,  "right"),
    (244, 1.5, "driest",   "Electric HIGH 244°F,\n90 min: falls apart",            6,  0,  "left"),
    (244, 0.75,"driest",   "Electric HIGH 244°F,\n45 min: tender, intact",         6,  0,  "left"),
    (250, 0.58,"driest",   "Stovetop 15 psi\n250°F, ~35 min",                      6, -16, "left"),
]
fails = [  # under-cooked examples (hollow)
    (212, 0.75, "Boiled 45 min:\nhard and rubbery", -6, 0, "right"),
    (244, 0.5,  "Pressure 30 min:\nslightly rubbery", -6, 0, "right"),
]

fig, ax = plt.subplots(figsize=(11, 7.2), dpi=150)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
T = np.linspace(130, 264, 400)
ax.fill_between(T, t_tender(T), 200, color=TENDER_FILL, lw=0, zorder=0)
ax.plot(T, t_tender(T), color=INK2, lw=2, zorder=2)

ax.set_yscale("log")
ax.set_xlim(130, 264); ax.set_ylim(0.2, 150)
yt = [0.25, 0.5, 1, 2, 4, 8, 12, 24, 48, 72, 120]
ax.yaxis.set_major_locator(FixedLocator(yt)); ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticklabels(["15 min", "30 min", "1 h", "2 h", "4 h", "8 h", "12 h", "1 day", "2 days", "3 days", "5 days"])
ax.set_xticks([140, 160, 180, 200, 212, 230, 250])
ax.set_xticklabels(["140", "160", "180", "200", "212\nboil", "230\n~6 psi", "250\n15 psi"])
ax.grid(True, which="major", color=GRID, lw=0.8, zorder=0)
for s in ["top", "right"]: ax.spines[s].set_visible(False)
for s in ["left", "bottom"]: ax.spines[s].set_color(AXIS)
ax.tick_params(colors=MUTED, labelsize=9)
ax.set_xlabel("Cooking temperature, °F  (above 212°F only a pressure cooker can get there)", color=INK2, fontsize=10)
ax.set_ylabel("Time in the liquid before the meat is tender", color=INK2, fontsize=10)

for T0, h, j, lab, dx, dy, ha in pts:
    ax.scatter(T0, h, s=90, color=J[j], edgecolor=SURF, lw=2, zorder=4)
    ax.annotate(lab, (T0, h), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center", fontsize=8.2, color=INK)
for T0, h, lab, dx, dy, ha in fails:
    ax.scatter(T0, h, s=90, facecolor=SURF, edgecolor=INK2, lw=1.8, zorder=4)
    ax.annotate(lab, (T0, h), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center", fontsize=8.2, color=INK2, style="italic")

ax.text(135, 0.36, "TOUGH / RUBBERY ZONE\nfibers have contracted, collagen not yet converted", fontsize=9.5, color=INK2, va="bottom", ha="left", weight="bold")
ax.text(196, 60, "TENDER ZONE\ncollagen has turned to gelatin", fontsize=9.5, color=INK2, va="center", ha="left", weight="bold")
ax.text(197, 0.245, "◄ cooler: slower but juicier          hotter: faster but drier ►", fontsize=8.5, color=MUTED, ha="center", va="bottom")

# legend for juiciness (ordinal ramp), plus hollow marker
from matplotlib.lines import Line2D
h = [Line2D([], [], marker="o", ls="", ms=9, color=J["juiciest"], label="juiciest (below ~170°F)"),
     Line2D([], [], marker="o", ls="", ms=9, color=J["moderate"], label="moderate (175–220°F)"),
     Line2D([], [], marker="o", ls="", ms=9, color=J["driest"], label="driest (pressure, 229°F+)"),
     Line2D([], [], marker="o", ls="", ms=9, mfc=SURF, mec=INK2, label="not long enough: still rubbery")]
leg = ax.legend(handles=h, title="Juiciness of the result", loc="upper right", frameon=False, fontsize=8.5, title_fontsize=9)
leg.get_title().set_color(INK2)
for t in leg.get_texts(): t.set_color(INK)

fig.suptitle("How long an old hen needs to go tender, by cooking temperature", x=0.01, ha="left", fontsize=14, color=INK, weight="bold")
ax.set_title("Every liquid method runs the same reaction at a different speed. Below the line the meat is rubbery; above it, tender.\n"
             "Boiling is not what makes meat rubbery; stopping too early does. Curve fitted to reported old-hen cook times (time doubles every ~15°F cooler).",
             loc="left", fontsize=9.5, color=INK2, pad=10)
fig.text(0.01, 0.01, "Sources: pressure-cooker-research/sources.md. Points marked 'estimated' are extrapolated from the curve; no source has tested them on a hen.", fontsize=7.5, color=MUTED)
fig.tight_layout(rect=(0, 0.02, 1, 0.97))
for ext in ("png", "svg"):
    fig.savefig(f"/home/user/Random-AI-projects/pressure-cooker-research/figures/tenderness-map.{ext}", facecolor=SURF)
print("ok")
