"""Two-page fridge sheet: old laying hen, freezer to plate. Built with reportlab."""
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT

OUT = "/home/user/Random-AI-projects/pressure-cooker-research/fridge-sheet/old-hen-fridge-sheet.pdf"
INK, INK2, MUTED, RULE, HEAD_BG, ZEBRA = "#0b0b0b", "#3a3936", "#6f6d67", "#c3c2b7", "#e8eef7", "#f5f5f2"

base = ParagraphStyle("b", fontName="Helvetica", fontSize=7.0, leading=8.2, textColor=INK)
bold = ParagraphStyle("bd", parent=base, fontName="Helvetica-Bold")
small = ParagraphStyle("s", parent=base, fontSize=6.3, leading=7.4, textColor=INK2)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=17, textColor=INK)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=8.8, leading=10, textColor=INK, spaceBefore=3.5, spaceAfter=1.5)
sub = ParagraphStyle("sub", parent=base, textColor=INK2, fontSize=7.2)

def P(t, st=base): return Paragraph(t, st)
def tbl(rows, widths, head=True, zebra=True, fs=None):
    data = [[P(c, bold if (head and i == 0) else base) if isinstance(c, str) else c for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    st = [("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 3), ("RIGHTPADDING", (0,0), (-1,-1), 3),
          ("TOPPADDING", (0,0), (-1,-1), 1.1), ("BOTTOMPADDING", (0,0), (-1,-1), 1.1),
          ("LINEBELOW", (0,0), (-1,-1), 0.25, colors.HexColor(RULE)), ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor(RULE))]
    if head: st.append(("BACKGROUND", (0,0), (-1,0), colors.HexColor(HEAD_BG)))
    if zebra:
        for r in range(1 if head else 0, len(rows)):
            if (r % 2) == 0: st.append(("BACKGROUND", (0,r), (-1,r), colors.HexColor(ZEBRA)))
    t.setStyle(TableStyle(st)); return t

W = letter[0] - 0.7*inch  # usable width with 0.4in margins
story = []

# ---------------- PAGE 1 ----------------
story.append(P("OLD LAYING HEN: FREEZER TO PLATE", h1))
story.append(P("4 to 6 lb bird, 6 qt electric pressure cooker (Instant Pot Pro Plus settings shown). Roseburg OR, ~500 ft: no altitude adjustment. Full research: github.com/jonnystokes/Random-AI-projects", sub))
story.append(Spacer(1, 3))

story.append(P("1. TIMELINE (about 4 days, ~30 min hands-on)", h2))
story.append(tbl([
 ["When", "Do", "Why (short)", "Skip it and..."],
 ["Days 0 to 2", "Freezer to fridge, wrapped, on a tray. ~1 day per 4 to 5 lb", "Slow thaw prevents thaw rigor (violent contraction of pre-rigor frozen meat); surface stays under 40°F", "Counter/warm-water thaw = toughest result. From-frozen cooking fast-thaws inside the pot"],
 ["Day 2 to 3", "Rest thawed bird 24 h more in fridge", "Post-thaw rigor resolves; enzymes age the meat", "Stiffer, chewier"],
 ["Day 3", "Cut into 8 pieces; back + neck to broth pile", "2x surface for brine/acid; breast handled separately; fits under fill line", "Brine reaches center slower; breast overcooks"],
 ["Day 3, 12 to 24 h", "Brine + acid marinade (box 2), fridge", "Seasons to center, holds juice, softens surface collagen", "Bland inside, ~2x juice loss, ~3x shear force (spent-hen study)"],
 ["Day 3 alt (whole bird)", "Inject (box 3), rest 2 to 24 h", "Only fast way to season a whole bird's core", "Outside-only brine needs 48 h"],
 ["Day 4, last 1 to 2 h, optional", "Breast only: ginger or pineapple 1 to 2 h, OR baking soda 15 to 20 min + rinse", "Breast has no collagen to soften; enzymes cut fibers, soda holds water", "Dry breast (fine if shredding into sauce)"],
 ["Day 4", "Drain, pat dry, optional 3 to 4 min skin-side sear", "Roasted flavor in meat surface and broth", "No tenderness loss"],
 ["Day 4", "COOK (box 4)", "Collagen to gelatin. Irreversible step", "Too short = rubbery; quick release = stringy"],
 ["Day 4", "Rest 20 to 30 min IN the liquid", "Meat reabsorbs liquid and seasoning while cooling", "Less seasoned, bleeds on the board"],
 ["Day 4", "Broth stage (box 5)", "Recovers gelatin/flavor from the 60% of the bird that is not meat", "Most of the hen's value in the trash"],
], [0.95*inch, 2.05*inch, 2.45*inch, 1.75*inch]))

story.append(P("2. BRINE + ACID MARINADE (per lb of meat; pieces; fridge; 12 to 24 h)", h2))
story.append(tbl([
 ["Ingredient", "Amount", "What it brings", "Limit"],
 ["Salt (table)", "1 tsp per lb (2% by weight)", "Reaches the core (1 to 2 cm in 12 h, full in 24 to 48 h); fibers hold water (loss 12% -> 4 to 7%); carries dissolved flavors in; mild tenderizing", "Over ~3% by weight = firm, cured"],
 ["Vinegar 5%", "1 part vinegar : 3 parts water, to cover (~1.2% acid). Lemon: 1 : 5", "pH ~4.5: proteins swell and take up liquid; collagen solubility 9% -> 29%; spent hens: shear cut 2/3, cooking loss 50% -> 39%", "Over ~1.5% acid or over 24 h = chalky outer mm"],
 ["Sugar", "1/2 tsp per lb", "Balances; rides in with salt; helps a sear brown", "More tastes like ham brine"],
 ["Aromatics", "Onion, garlic, bay, peppercorn, herbs", "Surface + liquid flavor only (1 to 3 mm deep max)", "None"],
 ["Optional, breast only, last 1 to 2 h", "1 tbsp grated ginger OR 1/4 cup pineapple juice per lb", "Enzymes cut fibers; keep working up to ~150°F during ramp", "Overnight or overdose = paste"],
 ["Optional, breast only", "1/2 tsp baking soda per lb, 15 to 20 min, rinse", "Raises pH; breast holds water", "No collagen effect; soapy if unrinsed. Never soda ash"],
], [1.25*inch, 1.75*inch, 3.0*inch, 1.2*inch]))

story.append(P("3. INJECTION (whole bird or big pieces)", h2))
story.append(tbl([
 ["Solution", "Amount", "Where", "When"],
 ["3% salt in stock or water (1 tbsp + 1 tsp salt per 2 cups); dissolved flavors only: soy, Worcestershire, garlic powder; 1 to 2 tbsp melted butter per cup. Strain.", "1 oz per lb", "Grid every 1 to 1.5 in: thighs, legs, breast. Massage after", "2 to 24 h before cooking. Overnight is best"],
], [3.3*inch, 0.85*inch, 1.9*inch, 1.15*inch]))

story.append(P("4. THE COOK", h2))
story.append(tbl([
 ["", "FAST: high pressure (~2 h total)", "BEST: low-temp hold (overnight, hands-off)", "EASY: slow cooker / slow-cook mode"],
 ["Mode", "Pressure Cook, HIGH (12 psi) or MAX (15 psi)", "Sous Vide 165 to 175°F (or Keep Warm Custom). No pressure. Lid closed, valve VENTING", "Slow Cook LOW/HIGH (185 to 209°F); glass lid or valve venting"],
 ["Setup", "Pieces + 1.5 to 2 cups liquid (wine, aromatics), halfway up the pieces. Min liquid 1.5 cups", "Legs/thighs/wings in a bag with 1 to 2 tbsp wine + aromatics; OR fully submerged in 1% salted stock. Breast in its own bag", "0 to 1/2 cup liquid for meat; cover the bird if you want broth"],
 ["Time", "HIGH: 40 to 45 min intact pieces; 75 to 90 min falls apart. MAX: subtract ~20%", "Legs/thighs 12 to 24 h at 165 to 175°F (older bird = longer). Breast 2 to 4 h at 150 to 155°F", "Pieces 4 to 6 h LOW; whole 10 to 12 h LOW"],
 ["Release", "NATURAL, 20 to 25 min. Never Quick", "n/a", "n/a"],
 ["Breast", "Pull at 25 to 30 min for sliceable; else shred into sauce", "Separate bag, separate temperature", "Pull early or shred"],
 ["Rest", "20 to 30 min in the liquid", "Chill in bag, or shred into bag juices", "In the juices; reduce juices for sauce"],
 ["Result", "Tender braise, driest of the three, excellent broth", "Juiciest and most tender an old hen gets", "Tender, moderate juiciness"],
 ["Done test", "Leg meat pulls from bone with light pressure. Resists: +15 min. Strings: went too long", "Same; hours of overshoot do little harm", "Same"],
 ["Water loss", "Zero (sealed)", "Lid closed + venting: small; check every 12 to 24 h. OPEN POT LOSES ~1 CUP/HOUR", "Negligible with lid on"],
], [0.7*inch, 2.4*inch, 2.55*inch, 1.55*inch]))

story.append(P("5. BROTH STAGE (after pulling meat)", h2))
story.append(tbl([
 ["In the pot", "Liquid", "Setting", "Time", "Notes"],
 ["Bones, skin, cartilage, back, neck, feet if any; 1 onion, 1 carrot, 2 celery, 2 garlic; 1 tbsp vinegar", "Cover, stay under 2/3 line", "Pressure Cook HIGH or MAX", "90 to 180 min, natural release (two 90 min runs = richest)", "Pressure broth is darker and meatier than simmered. Feet make it gel. Vinegar is for flavor; mineral gain is negligible"],
], [2.4*inch, 1.0*inch, 1.0*inch, 1.3*inch, 1.5*inch]))
story.append(PageBreak())

# ---------------- PAGE 2 ----------------
story.append(P("REFERENCE TABLES", h1))
story.append(P("6. PRESSURE = TEMPERATURE = TIME (sea level; old-hen legs to fork-tender; time roughly doubles every 15°F cooler)", h2))
story.append(tbl([
 ["Setting", "psi", "°F", "Time to tender", "Juiciness", "Note"],
 ["Sous vide / hold", "0", "143", "~3 days", "Best", "Pink-juicy style; old bird stays slightly chewy"],
 ["Sous vide / hold", "0", "165 to 175", "12 to 24 h", "Best", "The recommended 'best track'"],
 ["Slow cooker LOW/HIGH", "0", "185 to 209", "4 to 6 h pieces; 10 to 12 h whole", "Moderate", "Both settings end near a simmer; LOW just takes longer to get there"],
 ["Simmer / boil", "0", "212", "3 to 4 h", "Moderate", "45 min boiled = rubbery. 4 h boiled = stewing hen"],
 ["Instant Pot LOW", "5.8 to 7.2", "229 to 233", "75 to 90 min (est.)", "Lower", "Rarely useful for meat"],
 ["Instant Pot HIGH", "10.2 to 11.6", "240 to 243", "45 min intact / 90 min shred", "Lowest", "Default choice"],
 ["Instant Pot MAX / stovetop", "15", "250", "35 min intact / 70 min shred", "Lowest", "Saves ~20% time vs HIGH, nothing else"],
], [1.35*inch, 0.75*inch, 0.75*inch, 1.55*inch, 0.7*inch, 2.1*inch]))

story.append(P("7. LIQUID LEVEL BY GOAL (6 qt pot, one bird)", h2))
story.append(tbl([
 ["Method / goal", "Liquid", "Height on bird", "Why"],
 ["Pressure, whole bird, meat is the goal", "1 cup (6 qt) / 1.5 cups (8 qt) + trivet", "Bird above water", "Steam cooks it; firmer, sliceable; flavor stays in meat"],
 ["Pressure, pieces, shreddable", "1.5 to 2 cups", "Halfway up", "Braise; gentler on natural release"],
 ["Pressure, broth stage", "Cover bones", "Submerged", "Extraction needs contact. Never above 2/3 line, never below 1.5 cups"],
 ["Slow cooker, meat is the goal", "0 to 1/2 cup", "Bottom 1/2 in or none", "Sealed lid: no evaporation; bird gives ~1 cup of its own juice"],
 ["Slow cooker, soup or broth", "Cover", "Submerged", "You want the flavor in the liquid"],
 ["Low-temp hold, bag", "1 to 2 tbsp in bag; bath full", "Bag submerged", "Bath is only a heater"],
 ["Low-temp hold, no bag", "Cover completely, 1% salt (2 tsp per qt)", "Fully submerged, required", "165°F air is a poor heater; exposed meat dries"],
 ["Stovetop simmer", "Cover, lid partly on", "Submerged", "Loses 20 to 35% in a few hours: top up"],
], [1.9*inch, 1.7*inch, 1.2*inch, 2.4*inch]))
story.append(P("Submerging never toughens meat; it moves flavor into the liquid and makes skin soggy. Salt any liquid the meat sits in to ~1%.", small))

story.append(P("8. WHAT MOVES INTO MEAT", h2))
story.append(tbl([
 ["Ingredient", "Depth", "Practical use"],
 ["Salt (+ sugar, garlic/onion powder, soy, MSG dissolved in it)", "To the center in 24 to 48 h, or during any long hold", "Equilibrium or dry brine 1.5 to 2%; injection"],
 ["Acid", "A few mm", "Surface tenderizing on pieces; mild in the pot (wine, tomato)"],
 ["Herbs, spices, oil-soluble aromatics", "1 to 3 mm even after 24 h (wine: under 1 mm in 18 h)", "Put them in the sauce and broth, not the marinade"],
 ["Cooking liquid, on cooling", "Reabsorbed as meat cools", "Always rest and shred in the liquid"],
], [2.3*inch, 2.2*inch, 2.7*inch]))

story.append(P("9. INSTANT POT PRO PLUS QUICK SETTINGS", h2))
story.append(tbl([
 ["Item", "Value"],
 ["Pressure levels", "LOW 5.8 to 7.2 psi (229 to 233°F) | HIGH 10.2 to 11.6 psi (240 to 243°F) | MAX 15 psi / 95 to 115 kPa (250°F). MAX only in Pressure Cook and Canning"],
 ["Manual pressure cook", "Pressure Cook > Pressure field (Low/High/Max) > hours/minutes > venting field (NATURAL / Pulse / Quick). Ignore presets"],
 ["Sous vide", "77 to 194°F, 30 min to 99 h 30 min. Lid fully closed, valve VENTING, or lid off. Not a loose lid"],
 ["Keep Warm custom", "77 to 203°F, up to 10 h (a second hold mode for shorter jobs)"],
 ["Minimum liquid / max fill", "1.5 cups / 2/3 line (1/2 for beans or foaming)"],
 ["Max pressure run", "4 h per run; back-to-back runs allowed for broth"],
 ["Slow Cook", "Runs cooler than a Crock-Pot; use HIGH, cut liquid 15 to 20%, at least 3 h"],
 ["Sealing ring", "Replace every 12 to 18 months; keep a spare; one for savory, one for sweet"],
 ["Time to pressure", "8 to 15 min with 2 cups liquid; a full cold pot 20 to 40 min. Ramp and natural release are cooking time too"],
], [1.5*inch, 5.7*inch]))

story.append(P("10. RULES", h2))
rules = [
 ["ALWAYS", "Fridge thaw. Salt 12 h minimum. Natural release on meat. Rest in the liquid. Leg-pull test before serving. Water-level check every 12 to 24 h on multi-day holds."],
 ["NEVER", "Counter or warm-water thaw. Quick release on meat. Pull a pressure cook at 30 min because it 'looks done'. Enzyme marinade overnight. Soda ash. Open pot for a long hold. Fill above 2/3."],
 ["IF RUBBERY", "It needs MORE time, not less heat. Boiling is not the problem; stopping early is."],
 ["IF STRINGY", "Went too long under pressure or quick-released. Next time: 10 min less, natural release, or use the low-temp hold."],
 ["BREAST", "Never juicy on an old hen. Brine or inject; pull early; or plan to shred into sauce. Soda or ginger helps."],
 ["SAFETY", "Poultry safe at 165°F instantly, or 150°F held 3+ min. Above 140°F is out of the danger zone, so a 165°F hold for 24 h is safe. Delay-start is not for raw poultry."],
 ["PRIORITY IF RUSHED", "Fridge thaw > 12 h salt > natural release > rest in liquid > acid marinade > cut into pieces > sear > breast treatment."],
]
story.append(tbl(rules, [1.1*inch, 6.1*inch], head=False))
story.append(P("Sources and full explanations: pressure-cooker-research documents 02, 04, 05, 06 in the repo. Spent-hen vinegar data: Erdem 2025 (PMC12214402). Older-animal collagen: Naqvi et al. 2021, Meat Science.", small))

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.35*inch, rightMargin=0.35*inch, topMargin=0.3*inch, bottomMargin=0.3*inch,
                        title="Old Laying Hen: Freezer to Plate", author="Random-AI-projects research")
doc.build(story)
print("wrote", OUT)
