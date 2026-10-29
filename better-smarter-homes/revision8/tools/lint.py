"""Revision 8 chapter lint: the measured targets of STYLE_GUIDE.md section 12 plus the
pattern-shaped bans of section 10. The floor, not the standard; the reading is the standard.

Usage:  python tools/lint.py manuscript/g1_ch_11_the-wall-system-foundation-to-roofline.md [--all]
Exit code 1 when any gate FAILs. --all lists every offending line instead of the first ten.
Reads only; never writes to the manuscript.
"""
import bisect
import re
import sys
import statistics
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
try:
    from chapters import ORDER, R7  # the final chapter order, for the Revision 7 word-count baseline
except Exception:  # noqa: BLE001
    ORDER, R7 = [], None

LAYER_RE = re.compile(r"^\*\*(Simple|Applied|Professional|Code)\*\*\s*$")
SECTION_RE = re.compile(r"^## (\d+)\.(\d+)\s+(.*)$")
UNNUMBERED_RE = re.compile(r"^## (?!\d)(.*)$")
SUBHEAD_RE = re.compile(r"^### (.*)$")
CHAPTER_RE = re.compile(r"^# Chapter (\d+):\s*(.*)$")
LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")
BOLD_RUNIN_RE = re.compile(r"^\*\*[^*]{2,70}[.:]\*\*\s")
# a sentence may also start with $, bold, italics, a section sign or a curly quote (bug 14, 2026-10-27)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[$*_" + chr(0xA7) + chr(0x201C) + chr(0x2018) + r"])")
PLACEHOLDER = chr(0x2024)  # stands in for an abbreviation's period while sentences are split
CLOSING_SECTIONS = ("who decides what", "open items", "decisions this chapter records", "records to keep")

RESEARCH_NARRATION = re.compile(
    r"\bno published\b|\bwas located\b|\bwere located\b|\bwas found\b|\bwere found\b|\bwas identified\b|"
    r"\bwere identified\b|\bthe project research\b|\bthis project's research\b|\bthe research behind\b|"
    r"\bno independently monitored\b|\bnot documented\b|\bundocumented\b|\bno documented\b|\bno source[s]? (documents?|found|ranks?|exists?)\b|"
    r"\bas of (january|february|march|april|may|june|july|august|september|october|november|december) 20\d\d\b|"
    r"\bno built oregon precedent\b|\bthe research (located|confirmed|found)\b|\bno comparative .{0,40} (were|was) located\b|"
    # brief v3: source-class attributions and anonymized specifics (fault 37)
    r"\bsecondary[- ]sources?\b|\bsecondary summaries\b|\bindustry sources?\b|\bgeneral (septic |homesteading |land[- ]investing |contractor )?guidance\b|"
    r"\bdocumented (examples|today)\b|\bindependent-agent reporting\b|\bin the published cases\b|\bsources? (report|reports|reported|describe|describes)\b|"
    r"\bper general\b|\bnational contractor guides?\b|\bcirculating in\b|\bat least one (county|counties|utility|investor-owned|jurisdiction|lender|insurer|district|carrier)\b|"
    # brief v4: anonymous reporters ("Rural users report", "They are reported to cut theft")
    r"\b(users|owners|homeowners|builders|people|installers) report(s|ed)?\b|\b(is|are) reported to\b",
    re.I)
# "this chapter" and its paraphrases (faults 27 and 44); "the table below" is allowed
SELF_DESCRIPTION = re.compile(
    r"\b[Tt]his (chapter|section|book)\b|\b[Tt]he book\b(?! name)|\b[Ww]hat follows\b|\b[Nn]othing here is new\b|\b[Bb]elow is the\b|"
    r"\b[Tt]he (order|list|steps|sequence|items?) above\b|\b[Aa]s (stated|described|noted|explained) (above|earlier|below)\b|"
    r"\b[Aa]n earlier section\b|\b[Ss]tated in full\b|\b[Ss]tep \d+ (catches|covers|handles|does|is where)\b")
PROTECTED = ("I have wanted to build a long-life concrete home in Oregon for about ten years. This book is the plan.",)
HEDGES = re.compile(r"\b(informally|literally|essentially|in a sense|arguably|in some sense|typically|generally)\b", re.I)
STOCK = re.compile(r"\b(delve|tapestry|realm|landscape|crucial|pivotal|robust|seamless|leverage|foster|elevate|transformative|journey|unlock|empower|embrace|ecosystem)\b", re.I)
INTENSIFIERS = re.compile(r"\b(truly|deeply|profoundly|remarkably|beautifully|simply|really|actually|very|quite)\b", re.I)
ANTITHESIS = re.compile(r"\bis not [^.]*\. (It is|They are)\b|\bnot (just|only|merely) [^.]{0,60}\bbut\b", re.I)
SELF_NARRATION = re.compile(r"\b([Tt]he point is|[Ww]hat this means is|[Ii]n short|[Ii]n other words)\b")
FOSSILS = re.compile(r"\b(book|chapter|section|block|layer|table|entry)s? (carr|answer|say|tell|give|touch|travel|hold|want|need|cover|has a job|have .*job|runs on)", re.I)
ANALOGY = re.compile(r"\b(like a|like an|the way you|the way a|as if|imagine|think of|picture a)\b", re.I)
SELF_CHECK = re.compile(r"\bask(s)? (yourself|:)|, ask:", re.I)
CHAPTER_NUMBER_REF = re.compile(r"(?<!ORS )(?<!OAR )(?<!ORSC )(?<!OPSC )(?<!OESC )(?<!OMSC )(?<!OSSC )(?<!IRC )(?<!IBC )(?<!IMC )(?<!UPC )(?<!NEC )\b[Cc]hapter \d+\b")
# codes, standards and session laws have chapters of their own ("ACI 318 Chapter 19", "Oregon Laws 2025, chapter 78")
CODE_CONTEXT = re.compile(r"\b(ACI|ASTM|ORSC|OSSC|OPSC|OMSC|OESC|OEESC|IRC|IBC|IECC|IFC|OFC|IPC|IMC|UPC|NEC|NFPA|ASHRAE|"
                          r"ASCE|TMS|UL|OAR|ORS|CFR|U\.S\.C|Laws|Handbook|[Cc]ode|[Ss]tandard)\b")
CROSS_REF = re.compile(r"\b[Cc]hapter\b(?!\s*\d)")
CODE_BOOK_PREFIX = re.compile(r"\b(ORS|OAR|ORSC|OPSC|OESC|OMSC|OSSC|IRC|IBC|IMC|UPC|NEC|ASCE|ASTM|ACI|TMS|NFPA|CFR) [Cc]hapter\b")
CITATION = re.compile(r"\b(ORS|OAR|ORSC|OPSC|OESC|OMSC|OSSC|ASTM|ACI|ASCE|ASHRAE|NFPA|TMS|NEC|CFR|IRC|IBC)\b|\bR\d{3}\b|\bTable [A-Z]?\d")
DELEGATION_END = re.compile(r"(engineer of record|building department|geotechnical engineer|before the permit|at permit|permit application|pre-application meeting)[^.]*\.\s*$", re.I)
YEAR_TAG = re.compile(r"\((19|20)\d\d\)")
SIZE_WORDS = re.compile(r"\b(cheap|expensive|costly|a lot|a little)\b", re.I)
YOU = re.compile(r"\b[Yy]ou\b|\b[Yy]our\b(?! DEQ Online)")
HEDGED_RANGE = re.compile(r"\b(about|roughly|approximately|around)\s+\$?\d[\d,.]*\s*(?:percent|%|[a-zA-Z°]+)?\s*(?:to|and|through)\s+\$?\d", re.I)
# a Source line names something an inspector can open: a section, a rule number, a table, or a whole
# standard by designation ("ASTM D2487", "UL 858"); "Section" either case (bug 16 and Unsure 1, 2026-10-27)
SECTION_LEVEL = re.compile(r"\d+[A-Z]?\.\d+|\d{3}-\d{3}-\d{4}|\bR\d{3}\b|\bTable [A-Z]?\d|U\.S\.C\. \d+|CFR part \d+|\bSchedule \d+|\b[Ss]ection \d+|\bD\d{3}\b|§"
                           r"|\b(?:ASTM|ACI|TMS|ASCE|ANSI|UL|NFPA|CSA|ISO|AWS|ASHRAE|NSF|IAPMO|AASHTO|NCMA|ICC-ES|ESR)[\s-]?[A-Z]{0,2}[\s-]?\d|\bNo\. ?\d")
CHAPTER_HEADING_LINE = re.compile(r"^# Chapter \d+:")
ABBR = re.compile(r"\b(U\.S\.C|U\.S|v|No|St|Dr|Mr|Ms|etc|e\.g|i\.e|Or App|Or)\.")
STOP = {"the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "with", "at", "by", "from", "as", "that", "it", "its", "is", "are", "be",
        "this", "these", "those", "each", "every", "any", "all", "than", "not", "no", "which", "who", "what", "where", "when"}
PREP = {"in", "on", "by", "at", "with", "from", "before", "after", "without", "under", "over", "into", "per", "through"}
SMALL_WORDS = {"to", "and", "of", "the", "in", "for", "on", "with", "at", "by", "from", "a", "an", "or", "as", "vs", "into", "over", "under", "per"}
# number plus unit, also hyphenated ("12-inch") and with "%" or "in." (bug 9, 2026-10-27)
UNIT_NUMBER = re.compile(r"\$?\b(\d+(?:[.,]\d+)?)(?:\s*|-)(percent|%|inches|inch|in\.|feet|foot|ft|psf|psi|mph|gallons|gallon|gpm|amps|amp|volts|volt|degrees|°F|°C|lb|pounds|pound|mm|cm|kg|years|year|days|day|hours|hour|minutes|minute|square feet|sq ft|cfm|kW|kWh)(?![A-Za-z])", re.I)
UNIT_CANON = {"percent": "%", "inches": "in", "inch": "in", "in.": "in", "feet": "ft", "foot": "ft", "gallons": "gal",
              "gallon": "gal", "pounds": "lb", "pound": "lb", "years": "yr", "year": "yr", "days": "d", "day": "d",
              "hours": "h", "hour": "h", "minutes": "min", "minute": "min", "amps": "amp", "volts": "volt",
              "square feet": "sqft", "sq ft": "sqft"}


def unit_key(m):
    """'12 inches', '12-inch' and '12 in.' compare equal."""
    unit = m.group(2).lower()
    return m.group(1).replace(",", "") + UNIT_CANON.get(unit, unit)
PAREN_DEF = re.compile(r"\b([a-z][a-z-]*(?: [a-z-]+){0,2}) \(([a-z][^)]{15,90})\)")


def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    text = ABBR.sub(lambda m: m.group(1) + PLACEHOLDER, text)  # "No. 26-01", "v.", "U.S." do not end a sentence
    return [s.replace(PLACEHOLDER, ".") for s in SENT_SPLIT.split(text) if s]


def words(text):
    # "$4,000", "0.5", "R403.1.3.5" and "A/B/C" are one word each (bug 7, 2026-10-27)
    return len(re.findall(r"[\w'$%-]+(?:[.,/][\w'$%-]+)*", text))


class Chapter:
    def __init__(self, path):
        self.path = Path(path)
        self.lines = self.path.read_text(encoding="utf-8-sig").splitlines()  # a BOM is not text (bug 21)
        m = re.search(r"g1_ch_(\d+)_", self.path.name)
        self.file_number = int(m.group(1)) if m else None
        self.parse()

    def parse(self):
        self.chapter_number = None
        self.chapter_title = ""
        self.sections = []          # dicts: num, k, title, line, layers:set, body lines by layer
        self.closing = {}           # name -> line
        self.has_note = False
        self.code_entries = []      # (section, lines)
        self.fences = []            # (start, end, layer, section_idx)
        self.paragraphs = []        # (line_no, text, layer, section_idx, is_list, in_blockquote)
        self.headings = []          # (line_no, kind, text)
        in_code = False
        fence_start = None
        layer = "freeform"
        sec_idx = -1
        para = []
        para_start = None
        in_closing = None

        def flush():
            nonlocal para, para_start
            if para:
                text = " ".join(para)
                self.paragraphs.append((para_start, text, layer, sec_idx, False, text.startswith(">")))
            para, para_start = [], None

        for i, raw in enumerate(self.lines, 1):
            line = raw.rstrip()
            s = line.strip()
            if s.startswith("```"):
                flush()
                if not in_code:
                    in_code, fence_start = True, i
                    if layer == "unlabeled":  # a second fence straight after a Code block is still Code
                        layer = "Code"
                else:
                    in_code = False
                    self.fences.append((fence_start, i, layer, sec_idx))
                    if layer == "Code":
                        self._split_code_entries(fence_start, i, sec_idx)
                        layer = "unlabeled"  # prose after a Code block needs its own label (bug 12)
                continue
            if in_code:
                continue
            m = CHAPTER_RE.match(s)
            if m:
                flush()
                self.chapter_number = int(m.group(1))
                self.chapter_title = m.group(2)
                self.headings.append((i, "chapter", m.group(2)))
                continue
            m = SECTION_RE.match(s)
            if m:
                flush()
                sec_idx = len(self.sections)
                self.sections.append({"num": int(m.group(1)), "k": int(m.group(2)), "title": m.group(3), "line": i,
                                      "layers": set(), "delegations": 0, "crossrefs": 0, "simple_blocks": [],
                                      "layer_text": defaultdict(list)})
                self.headings.append((i, "section", m.group(3)))
                layer = "freeform"
                in_closing = None
                continue
            m = UNNUMBERED_RE.match(s)
            if m:
                flush()
                name = m.group(1).strip().lower()
                self.closing[name] = i
                in_closing = name
                sec_idx = -2  # closing sections are not body
                layer = "closing"
                continue
            m = SUBHEAD_RE.match(s)
            if m:
                flush()
                self.headings.append((i, "subhead", m.group(1)))
                continue
            m = LAYER_RE.match(s)
            if m:
                flush()
                layer = m.group(1)
                if sec_idx >= 0:
                    self.sections[sec_idx]["layers"].add(layer)
                    if layer == "Simple":
                        self.sections[sec_idx]["simple_blocks"].append([])
                continue
            if s.startswith("> **Jon's note.**") or s.startswith("> **Jon’s note.**"):
                self.has_note = True
            if s.startswith("|"):
                flush()
                continue
            if not s or s == ">":  # a bare ">" separates two paragraphs of a blockquote (bug 20)
                flush()
                continue
            lm = LIST_RE.match(line)
            if lm:
                flush()
                text = lm.group(3)
                self.paragraphs.append((i, text, layer, sec_idx, True, False))
                self._collect(text, layer, sec_idx)
                continue
            if para_start is None:
                para_start = i
            para.append(s)
            self._collect(s, layer, sec_idx)
        flush()

    def _collect(self, text, layer, sec_idx):
        if sec_idx >= 0:
            sec = self.sections[sec_idx]
            sec["layer_text"][layer].append(text)
            if layer == "Simple" and sec["simple_blocks"]:
                sec["simple_blocks"][-1].append(text)

    def _split_code_entries(self, start, end, sec_idx):
        body = self.lines[start:end - 1]
        entry = []
        for l in body + [""]:
            if l.strip():
                entry.append(l)
            elif entry:
                self.code_entries.append((sec_idx, entry))
                entry = []


def run(path, show_all=False):
    ch = Chapter(path)
    cap = None if show_all else 10
    results = []   # (gate, value, target, status, details)

    def gate(name, value, target, ok, details=None, warn=False):
        status = "PASS" if ok else ("WARN" if warn else "FAIL")
        results.append((name, value, target, status, (details or [])[:cap] if cap else (details or [])))

    body_paras = [p for p in ch.paragraphs if p[3] >= -1 and not p[5]]          # opening and numbered sections, not the note
    body_text_lines = [(p[0], p[1]) for p in body_paras]
    all_prose_sents = []
    for ln, text, layer, sec, is_list, bq in ch.paragraphs:
        if sec == -2:
            continue
        for snt in sentences(text):
            all_prose_sents.append((ln, snt, layer, sec, is_list))

    # 1 em dashes and semicolons (prose; Code value lines may use semicolons)
    em = [(i, l) for i, l in enumerate(ch.lines, 1) if "—" in l]
    gate("em dashes", len(em), 0, not em, [f"{i}: {l.strip()[:90]}" for i, l in em])
    in_code = False
    semis = []
    for i, l in enumerate(ch.lines, 1):
        if l.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and ";" in l and not l.strip().startswith("|"):
            semis.append((i, l))
    gate("semicolons in prose", len(semis), 0, not semis, [f"{i}: {l.strip()[:90]}" for i, l in semis])

    # 2 research narration (body only)
    hits = [(ln, m.group(0), t) for ln, t in body_text_lines for m in RESEARCH_NARRATION.finditer(t)]
    gate("research narration phrases", len(hits), 0, not hits, [f"{ln}: '{h}' in: {t[:80]}" for ln, h, t in hits])

    # 3 colon fragments: a short noun phrase, a colon, then prose (not a list introducer)
    frags = []
    for idx, (ln, text, layer, sec, is_list, bq) in enumerate(ch.paragraphs):
        if sec == -2 or bq:
            continue
        m = re.match(r"^(\*\*)?([A-Z][^.!?:]{2,45}?)(\*\*)?: (?=[a-z\"'(])", text)
        if m:
            frags.append((ln, text[:90]))
        for sm in re.finditer(r"(?<=[.!?] )([A-Z][a-z]+(?: [a-z]+){0,3}): (?=[a-z])", text):
            frags.append((ln, text[max(0, sm.start() - 10):sm.start() + 70]))
    gate("colon fragments", len(frags), 0, not frags, [f"{ln}: {t}" for ln, t in frags])

    # 4 self-description
    sd = []
    for ln, t in body_text_lines:
        if any(p in t for p in PROTECTED):
            continue
        for m in SELF_DESCRIPTION.finditer(t):
            sd.append((ln, t[max(0, m.start() - 30):m.start() + 50]))
    gate("'this chapter / this section / the book' in prose", len(sd), 0, not sd, [f"{ln}: {t}" for ln, t in sd])

    # 5 bold run-in runs
    # a heading, layer label, fence or table between two paragraphs breaks the run (bug 13)
    breaks = [i for i, l in enumerate(ch.lines, 1)
              if re.match(r"^\s*(#|```|\||\*\*(Simple|Applied|Professional|Code)\*\*\s*$)", l)]
    runs, run_len, run_start, prev_ln = [], 0, None, None
    for ln, text, layer, sec, is_list, bq in ch.paragraphs:
        if prev_ln is not None and bisect.bisect_left(breaks, ln) - bisect.bisect_right(breaks, prev_ln) > 0:
            run_len = 0
        prev_ln = ln
        if sec < 0:
            run_len = 0
            continue
        if BOLD_RUNIN_RE.match(text):
            run_len += 1
            if run_len == 1:
                run_start = ln
            if run_len == 3:
                runs.append(run_start)
        else:
            run_len = 0
    gate("runs of 3+ bold run-in paragraphs", len(runs), 0, not runs, [f"run starting at line {r}" for r in runs])

    # 6 determiner share, 7 long sentences
    n_s = len(all_prose_sents)
    det = [s for s in all_prose_sents if re.match(r"^(\*\*)?(The|A|An)\b", s[1])]
    share = 100 * len(det) / n_s if n_s else 0
    gate("'The/A/An' sentence openers (%)", round(share, 1), "<= 18", share <= 18)
    long_s = [s for s in all_prose_sents if words(s[1]) >= 30]
    lshare = 100 * len(long_s) / n_s if n_s else 0
    gate("sentences of 30+ words (%)", round(lshare, 1), "<= 8", lshare <= 8, [f"{ln}: {t[:90]}" for ln, t, *_ in long_s])

    # 8-10 bands per layer
    def band(layer, avg_t, max_t):
        ss = [(ln, t) for ln, t, lay, sec, il in all_prose_sents if lay == layer and sec >= 0]
        if not ss:
            gate(f"{layer} sentences (avg / max words)", "none", f"<= {avg_t} / <= {max_t}", True)
            return
        lens = [words(t) for _, t in ss]
        avg, mx = statistics.mean(lens), max(lens)
        over = [f"{ln}: ({words(t)}w) {t[:80]}" for ln, t in ss if words(t) > max_t]
        gate(f"{layer} sentences (avg / max words)", f"{avg:.1f} / {mx}", f"<= {avg_t} / <= {max_t}", avg <= avg_t and mx <= max_t, over)
    band("Simple", 16, 25)
    band("Applied", 15, 25)
    band("Professional", 22, 40)

    # an Applied step is measured whole, not sentence by sentence (bug 8): under 25 words each
    steps = [(ln, t) for ln, t, layer, sec, il, bq in ch.paragraphs if sec >= 0 and layer == "Applied" and il]
    long_steps = [f"{ln}: ({words(t)}w) {t[:70]}" for ln, t in steps if words(t) > 25]
    gate("Applied steps over 25 words", len(long_steps), 0, not long_steps, long_steps)
    gate("Applied step length, average (info; target <= 15)",
         round(statistics.mean([words(t) for _, t in steps]), 1) if steps else 0, "info", True)

    # Simple block length
    long_blocks, short_blocks = [], []
    for sec in ch.sections:
        for blk in sec["simple_blocks"]:
            w = words(" ".join(blk))
            if w > 120:
                long_blocks.append(f"section {sec['num']}.{sec['k']}: {w} words")
            elif w < 40:
                short_blocks.append(f"section {sec['num']}.{sec['k']}: {w} words")
    gate("Simple blocks over 120 words", len(long_blocks), 0, not long_blocks, long_blocks)
    gate("Simple blocks under 40 words (info)", len(short_blocks), "info", True, short_blocks)

    # 11 paragraphs over 120 words
    big = [(ln, words(t)) for ln, t, layer, sec, is_list, bq in ch.paragraphs if sec >= 0 and not is_list and words(t) > 120]
    gate("paragraphs over 120 words", len(big), 0, not big, [f"{ln}: {w} words" for ln, w in big])

    # 12 sections without Simple; labels overall
    no_simple = [f"{s['num']}.{s['k']} {s['title']}" for s in ch.sections if "Simple" not in s["layers"]]
    gate("sections without a Simple block", len(no_simple), 0, not no_simple, no_simple)
    unlabeled = [f"{ln}: {t[:70]}" for ln, t, layer, sec, il, bq in ch.paragraphs
                 if sec >= 0 and layer == "unlabeled" and not t.startswith("[FIGURE")]
    gate("prose after a Code block with no layer label", len(unlabeled), 0, not unlabeled, unlabeled, warn=True)
    label_counts = Counter()
    for s in ch.sections:
        for l in s["layers"]:
            label_counts[l] += 1
    gate("layer labels S/A/P/C (info)", f"{label_counts['Simple']}/{label_counts['Applied']}/{label_counts['Professional']}/{label_counts['Code']}", "info", True)

    # 13 Code entries without Source
    missing = [f"section index {sec}: {e[0].strip()[:70]}" for sec, e in ch.code_entries if not any(l.strip().lower().startswith("source:") for l in e)]
    gate("Code entries without a Source line", len(missing), 0, not missing, missing)
    code_outside = [f"line {a}" for a, b, layer, sec in ch.fences if layer != "Code" and sec >= 0]
    gate("fenced blocks outside a Code label", len(code_outside), 0, not code_outside, code_outside)

    # 14 echo: unit-numbers shared by Professional and Code in one section
    echoes = []
    code_text_by_sec = defaultdict(list)
    for sec, e in ch.code_entries:
        code_text_by_sec[sec].append(" ".join(e))
    for idx, s in enumerate(ch.sections):
        prof = " ".join(s["layer_text"].get("Professional", []))
        code = " ".join(code_text_by_sec.get(idx, []))
        if not prof or not code:
            continue
        pn = {unit_key(m) for m in UNIT_NUMBER.finditer(prof)}
        cn = {unit_key(m) for m in UNIT_NUMBER.finditer(code)}
        shared = sorted(pn & cn)
        if shared:
            echoes.append(f"{s['num']}.{s['k']}: {', '.join(shared[:8])}")
    gate("Professional restating Code unit-values (sections)", len(echoes), 0, not echoes, echoes)

    # 14b echo of statements: a run of 6 words shared by Professional and Code in one section
    def shingles(text, n=6):
        toks = re.findall(r"[a-z0-9]+", text.lower())
        return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}
    stmt_echo = []
    for idx, s in enumerate(ch.sections):
        prof = " ".join(s["layer_text"].get("Professional", []))
        code = " ".join(code_text_by_sec.get(idx, []))
        if not prof or not code:
            continue
        shared = shingles(prof) & shingles(code)
        if shared:
            stmt_echo.append(f"{s['num']}.{s['k']}: '{sorted(shared)[0]} ...' (+{len(shared) - 1} more)")
    gate("Professional and Code sharing a 6-word run (sections)", len(stmt_echo), 0, not stmt_echo, stmt_echo)

    # 14c Applied blocks that open with a one-line framing imperative before the steps
    framing = 0
    applied_blocks = 0
    for idx, s in enumerate(ch.sections):
        if "Applied" not in s["layers"]:
            continue
        applied_blocks += 1
        first = next(((t, il) for ln, t, layer, sec, il, bq in ch.paragraphs if sec == idx and layer == "Applied"), None)
        if first and not first[1] and len(sentences(first[0])) == 1 and first[0].rstrip().endswith((".", ":")):
            framing += 1
    fshare = 100 * framing / applied_blocks if applied_blocks else 0
    gate("Applied blocks opening with a one-line framing sentence (%)", round(fshare), "<= 50", fshare <= 50, warn=True)

    # 15 year tags (a case, bill or measure citation's year is not a cost stamp)
    yt = []
    for ln, t in body_text_lines:
        for m in YEAR_TAG.finditer(t):
            back = t[max(0, m.start() - 70):m.start()]
            if re.search(r"(LUBA|Or App|Or \d|P[23]d|\bv\.|Bill|\bSB\b|\bHB\b|Measure|Laws|Guidebook|FAQ)", back):
                continue
            yt.append((ln, t[:80]))
    gate("year tags like '(2026)' in prose", len(yt), "<= 3", len(yt) <= 3, [f"{ln}: {t}" for ln, t in yt])

    # 16 delegation endings per section
    deleg = defaultdict(list)
    for ln, text, layer, sec, is_list, bq in ch.paragraphs:
        if sec >= 0 and not bq and DELEGATION_END.search(text):
            deleg[sec].append(ln)
    over = [f"{ch.sections[s]['num']}.{ch.sections[s]['k']}: {len(v)} (lines {v})" for s, v in deleg.items() if len(v) > 1]
    gate("sections with 2+ delegation-ending paragraphs", len(over), 0, not over, over)

    # 17 cross-reference sentences per section
    xr = defaultdict(list)
    for ln, t, layer, sec, il in all_prose_sents:
        if sec >= 0 and CROSS_REF.search(t) and not CODE_BOOK_PREFIX.search(t):
            xr[sec].append(ln)
    over = [f"{ch.sections[s]['num']}.{ch.sections[s]['k']}: {len(v)}" for s, v in xr.items() if len(v) > 1]
    gate("sections with 2+ cross-reference sentences", len(over), 0, not over, over, warn=True)
    simple_xr = [f"{ln}: {t[:80]}" for ln, t, layer, sec, il in all_prose_sents if layer == "Simple" and sec >= 0 and CROSS_REF.search(t) and not CODE_BOOK_PREFIX.search(t)]
    gate("cross-references inside Simple blocks", len(simple_xr), 0, not simple_xr, simple_xr)
    simple_cite = [f"{ln}: {t[:80]}" for ln, t, layer, sec, il in all_prose_sents if layer == "Simple" and sec >= 0 and CITATION.search(t)]
    gate("code citations inside Simple blocks", len(simple_cite), 0, not simple_cite, simple_cite)

    # 18 headings case
    bad = []
    for ln, kind, text in ch.headings:
        ws = re.findall(r"[A-Za-z][\w'’-]*", text)
        if kind == "chapter":
            # the whole title; the first word of the title and of a subtitle may be capitalized (bug 4)
            for seg in text.split(":"):
                toks = re.findall(r"[A-Za-z][\w'’-]*", seg)
                hit = next((w for w in toks[1:] if w.lower() in SMALL_WORDS and w[0].isupper()), None)
                if hit:
                    bad.append(f"{ln}: chapter title capitalizes '{hit}'")
                    break
        else:
            caps_small = [w for w in ws[1:] if w.lower() in SMALL_WORDS and w[0].isupper()]
            if caps_small:
                bad.append(f"{ln}: '{text}' capitalizes {caps_small[0]}")
                continue
            capitalized = [w for w in ws[1:] if w[0].isupper() and not w.isupper()]
            if len(ws) >= 3 and len(capitalized) >= max(2, int(0.6 * (len(ws) - 1))):
                bad.append(f"{ln}: '{text}' looks title-cased")
    gate("headings in machine title case", len(bad), 0, not bad, bad)

    # 19 numbering
    num_problems = []
    if ch.chapter_number is None:
        num_problems.append("no '# Chapter N:' heading")
    if ch.file_number and ch.chapter_number and ch.file_number != ch.chapter_number:
        num_problems.append(f"file says {ch.file_number}, heading says {ch.chapter_number}")
    ks = [s["k"] for s in ch.sections]
    if ks != list(range(1, len(ks) + 1)):
        num_problems.append(f"section numbers not contiguous: {ks}")
    wrong = [f"{s['num']}.{s['k']}" for s in ch.sections if s["num"] != ch.chapter_number]
    if wrong:
        num_problems.append(f"sections with the wrong chapter number: {wrong[:6]}")
    gate("numbering (chapter heading, file, contiguous sections)", len(num_problems), 0, not num_problems, num_problems)

    # 20 anatomy
    missing_parts = [name for name in CLOSING_SECTIONS if name not in ch.closing]
    if not ch.has_note:
        missing_parts.append("Jon's note")
    gate("anatomy present (note, who decides, open items, decisions, records)", len(missing_parts), 0, not missing_parts, missing_parts)
    skel = [i for i, l in enumerate(ch.lines, 1) if "_To research and write._" in l or "SKELETON" in l]
    gate("skeleton markers left", len(skel), 0, not skel, [f"line {i}" for i in skel])

    # 21 banned vocabulary and devices
    def scan(name, rx, lines_src=body_text_lines, warn=False):
        hs = [(ln, m.group(0), t) for ln, t in lines_src for m in rx.finditer(t)]
        gate(name, len(hs), 0, not hs, [f"{ln}: '{h}' in: {t[:70]}" for ln, h, t in hs], warn=warn)
    scan("hedges", HEDGES)
    scan("stock AI vocabulary", STOCK)
    scan("decorative intensifiers (review)", INTENSIFIERS, warn=True)
    scan("antithesis / 'not just X but Y'", ANTITHESIS)
    scan("self-narration", SELF_NARRATION)
    scan("text-as-agent fossils (review)", FOSSILS, warn=True)  # "a block holds its shape" is physical (bug 15)
    scan("reader self-check", SELF_CHECK)
    scan("chapter-number references", CHAPTER_NUMBER_REF)
    # the rest of the file too: tables, Code, the closing parts, the note (bug 22). A review list, because
    # most hits there are chapters of codes and standards; those within 30 characters of one are skipped.
    outside = []
    for i, l in enumerate(ch.lines, 1):
        if CHAPTER_HEADING_LINE.match(l.strip()):
            continue
        for m in re.finditer(r"\b[Cc]hapter (\d+)\b", l):
            if int(m.group(1)) > 36 or CODE_CONTEXT.search(l[max(0, m.start() - 30):m.start()]):
                continue
            outside.append(f"{i}: '{m.group(0)}' in: {l.strip()[:70]}")
    gate("chapter numbers anywhere in the file (review)", len(outside), 0, not outside, outside, warn=True)
    scan("'BSH'", re.compile(r"\bBSH\b"))
    scan("unanchored size words (review)", SIZE_WORDS, warn=True)
    non_simple = [(ln, t) for ln, t, layer, sec, il in all_prose_sents if layer not in ("Simple",) and sec >= 0]
    scan("analogy markers outside Simple", ANALOGY, non_simple)
    over = []  # one comparison per Simple block, counted per block, not per section (bug 17)
    for s in ch.sections:
        for bi, blk in enumerate(s["simple_blocks"], 1):
            n = sum(1 for t in sentences(" ".join(blk)) if ANALOGY.search(t))
            if n > 1:
                over.append(f"{s['num']}.{s['k']}, Simple block {bi}: {n}")
    gate("Simple blocks with 2+ comparisons", len(over), 0, not over, over)
    prof_you = [f"{ln}: {t[:80]}" for ln, t, layer, sec, il in all_prose_sents if layer in ("Professional",) and sec >= 0 and YOU.search(t)]
    gate("'you' in Professional", len(prof_you), 0, not prof_you, prof_you)
    you_total = sum(1 for ln, t, layer, sec, il in all_prose_sents if layer in ("Simple", "Applied") and YOU.search(t))
    gate("sentences with 'you' in Simple/Applied (info)", you_total, "info", True)

    # 22 gloss cadence
    glossed = Counter()
    for ln, t in body_text_lines:
        for m in PAREN_DEF.finditer(t):
            glossed[m.group(1).lower()] += 1
    dup = [f"'{k}' glossed {v} times" for k, v in glossed.items() if v > 1]
    gate("terms glossed more than once", len(dup), 0, not dup, dup)
    total_words = sum(words(t) for _, t in body_text_lines)
    gate("parenthetical definitions per 1,000 words (info)", round(1000 * sum(glossed.values()) / total_words, 1) if total_words else 0, "info", True)

    # 23 markers and counts
    jon = sum(l.count("[JON") for l in ch.lines)
    fig = sum(l.count("[FIGURE") for l in ch.lines)
    gate("[JON] markers / [FIGURE] markers (info)", f"{jon} / {fig}", "info", True)

    # 24 words vs Revision 7 baseline
    baseline = None
    if R7 and ch.file_number:
        for n, src, slug in ORDER:
            if n == ch.file_number:
                p = R7 / src
                if p.exists():
                    baseline = words(p.read_text(encoding="utf-8"))
    now = words("\n".join(ch.lines))
    if baseline:
        gate("words now / Revision 7 baseline", f"{now} / {baseline}", "not lower unless Open items say why", now >= baseline, warn=True)
    else:
        gate("words (info)", now, "info", True)
    gate("sections / subheadings (info)", f"{len(ch.sections)} / {sum(1 for h in ch.headings if h[1] == 'subhead')}", "info", True)

    # 25 Code entry shape (brief v3): one-sentence value line under 35 words, a section-level source, three parts
    long_vals, pointer_src, malformed = [], [], []
    for sec, e in ch.code_entries:
        name = f"{ch.sections[sec]['num']}.{ch.sections[sec]['k']}" if sec >= 0 else "?"
        lines = [l.strip() for l in e if l.strip()]
        if len(lines) < 3 or not lines[-1].lower().startswith("source:"):
            malformed.append(f"{name}: {lines[0][:60] if lines else ''}")
            continue
        val = " ".join(lines[1:-1])
        wc = words(val)
        n_sent = len(re.findall(r"[.!?]\s+(?=[A-Z])", ABBR.sub("", val))) + 1
        if wc > 35 or n_sent > 1:
            long_vals.append(f"{name}: {wc} words, {n_sent} sentence(s): {lines[0][:50]}")
        if not SECTION_LEVEL.search(lines[-1]):
            pointer_src.append(f"{name}: {lines[0][:45]} | {lines[-1][:45]}")
    gate("Code value lines over 35 words or more than one sentence", len(long_vals), 0, not long_vals, long_vals)
    gate("Code Source lines citing only a chapter, division or ordinance", len(pointer_src), 0, not pointer_src, pointer_src)
    gate("Code entries not three-part (requirement, value, Source)", len(malformed), 0, not malformed, malformed)

    # 26 hedged ranges (fault 38)
    hr = [(ln, m.group(0)) for ln, t in body_text_lines for m in HEDGED_RANGE.finditer(t)]
    gate("'about/roughly' before a range", len(hr), "<= 5", len(hr) <= 5, [f"{ln}: {h}" for ln, h in hr], warn=len(hr) <= 10)

    # 27 Simple blocks closing on what the reader does (fault 39)
    inst = []
    for s in ch.sections:
        for blk in s["simple_blocks"]:
            ss = sentences(" ".join(blk))
            if ss and (re.match(r"^(You|Your)\b", ss[-1]) or re.search(r"\band you \w+\b", ss[-1])):
                inst.append(f"{s['num']}.{s['k']}: {ss[-1][:70]}")
    gate("Simple blocks closing on 'You do X'", len(inst), "<= 3", len(inst) <= 3, inst)

    # 28 refrains (fault 40): the most repeated two- and three-word phrases in the body
    toks = re.findall(r"[a-z']+", " ".join(t for _, t in body_text_lines).lower())
    phr = Counter()
    for i in range(len(toks) - 1):
        a, b = toks[i], toks[i + 1]
        if a in PREP and b not in STOP:
            phr[f"{a} {b}"] += 1
        if i < len(toks) - 2:
            c = toks[i + 2]
            if a not in STOP and c not in STOP and not b.isdigit():
                phr[f"{a} {b} {c}"] += 1
    top = [(p, n) for p, n in phr.most_common(40) if n >= 6][:8]
    worst = top[0][1] if top else 0
    gate("most repeated phrases (review)", f"{worst}x '{top[0][0]}'" if top else 0, "< 10 for any phrase", worst < 10, [f"{n}x {p}" for p, n in top], warn=True)

    # 29 inventory sentences (fault 41), 'So' openers, clefts, abstract openers, false precision, marker wall
    inv = [(ln, t) for ln, t, layer, sec, il in all_prose_sents if sec >= -1 and not il and t.count(",") >= 5 and words(t) < 60]
    gate("inventory sentences (5+ commas in prose)", len(inv), "<= 4", len(inv) <= 4, [f"{ln}: {t[:80]}" for ln, t in inv], warn=True)
    so_open = [(ln, t) for ln, t, layer, sec, il in all_prose_sents if sec >= -1 and re.match(r"^So\b", t)]
    gate("sentences opening with 'So'", len(so_open), "<= 6", len(so_open) <= 6, [f"{ln}: {t[:70]}" for ln, t in so_open], warn=True)
    cleft = [(ln, t) for ln, t, layer, sec, il in all_prose_sents if sec >= -1 and "?" not in t and re.match(r"^What\b[^.?!]{3,70}\bis\b", t)]
    gate("'What ... is' cleft sentences", len(cleft), "<= 2", len(cleft) <= 2, [f"{ln}: {t[:70]}" for ln, t in cleft], warn=True)
    po = []
    for ln, t, layer, sec, il, bq in ch.paragraphs:
        if sec >= 0 and layer == "Professional" and not il:
            ss = sentences(t)
            if ss and words(ss[0]) < 8:
                po.append(f"{ln}: {ss[0][:70]}")
    gate("Professional paragraphs opening on a sentence under 8 words (review)", len(po), "review", not po, po, warn=True)
    prec = []
    for ln, t in body_text_lines:
        for m in re.finditer(r"\$[\d,]+", t):
            if len(m.group(0)[1:].replace(",", "").rstrip("0")) >= 4:
                prec.append(f"{ln}: {m.group(0)}")
    gate("dollar figures with 4+ significant digits (review)", len(prec), "review", not prec, prec, warn=True)
    note_markers = sum(l.count("[JON") for l in ch.lines if l.strip().startswith(">"))
    gate("[JON] markers in Jon's note", note_markers, "<= 4", note_markers <= 4, warn=True)

    # 30 the same 7-word run in two parts of the chapter (opening, note, sections)
    groups = defaultdict(str)
    for ln, t, layer, sec, il, bq in ch.paragraphs:
        if sec == -2:
            continue
        groups["note" if bq else sec] += " " + t
    keys = list(groups)
    sh7 = {k: shingles(groups[k], 7) for k in keys}

    def part_name(k):
        return "opening" if k == -1 else ("note" if k == "note" else f"{ch.sections[k]['num']}.{ch.sections[k]['k']}")
    pairs = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            shared = sh7[keys[i]] & sh7[keys[j]]
            if shared:
                pairs.append(f"{part_name(keys[i])} and {part_name(keys[j])}: '{sorted(shared)[0]} ...'")
    gate("7-word runs repeated between two parts of the chapter", len(pairs), "<= 2", len(pairs) <= 2, pairs, warn=True)

    # print
    print(f"LINT  {ch.path.name}")
    print(f"{'gate':62} {'value':>14}  {'target':<34} status")
    fails = 0
    for name, value, target, status, details in results:
        if status == "FAIL":
            fails += 1
        print(f"{name[:62]:62} {str(value):>14}  {str(target)[:34]:<34} {status}")
    detail_lines = [(n, s, d) for n, v, t, s, d in results if d and s in ("FAIL", "WARN")]
    if detail_lines:
        print("\nDETAILS")
        for name, status, details in detail_lines:
            print(f"- {name} [{status}]")
            for d in details:
                print(f"    {d}")
    print(f"\n{'PASS' if fails == 0 else 'FAIL'}: {fails} failing gate(s)")
    return fails


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):  # never crash on a character the console code page lacks (bug 1)
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    total = 0
    for a in args:
        total += run(a, show_all="--all" in sys.argv)
        print()
    sys.exit(1 if total else 0)
