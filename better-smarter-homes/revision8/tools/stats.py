"""Prose-shape statistics for the Better Smarter Homes manuscript (read-only).
Usage: python -I tools/stats.py <manuscript folder or one chapter file>
Reports per-file and whole-book: sentence length distribution by layer, choppiness,
sentence-opener repetition, layer label counts, Simple block lengths, 'you' density,
parenthetical-definition density, colon-fragment density, table and code-block share.
Skeleton chapters are left out of every table and total.
"""
import re, sys, collections, statistics
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # never crash on a character the console code page lacks
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
if len(sys.argv) < 2:
    sys.exit(__doc__)
target = Path(sys.argv[1])
files = sorted(target.glob("g1_ch*.md")) if target.is_dir() else [target]

LAYER_RE = re.compile(r"^\*\*(Simple|Applied|Professional|Code)\*\*\s*$")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])")

def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [s for s in SENT_SPLIT.split(text) if len(s.split()) >= 1]

book = collections.defaultdict(list)
book_openers = collections.Counter()
book_first_words = collections.Counter()
totals = collections.Counter()
per_file = []

for p in files:
    lines = p.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    layer = "freeform"
    in_code = False
    in_table = 0
    n_lines = len(lines)
    layer_counts = collections.Counter()
    simple_blocks = []
    cur_simple = []
    prose_sents = []
    layer_sents = collections.defaultdict(list)
    code_lines = 0
    table_lines = 0
    list_lines = 0
    paragraphs = 0
    para_words = []
    skeleton = any("_To research and write._" in l for l in lines)
    for l in lines:
        s = l.strip()
        if s.startswith("```"):
            in_code = not in_code
            code_lines += 1
            continue
        if in_code:
            code_lines += 1
            continue
        m = LAYER_RE.match(s)
        if m:
            if cur_simple:
                simple_blocks.append(" ".join(cur_simple)); cur_simple = []
            layer = m.group(1)
            layer_counts[layer] += 1
            continue
        if s.startswith("#"):
            if cur_simple:
                simple_blocks.append(" ".join(cur_simple)); cur_simple = []
            if re.match(r"^#{1,2} ", s):  # a ### subheading keeps its section's layer, as lint.py does
                layer = "freeform"
            continue
        if s.startswith("|"):
            table_lines += 1
            continue
        if not s:
            continue
        if re.match(r"^([-*]|\d+\.)\s", s):
            list_lines += 1
            body = re.sub(r"^([-*]|\d+\.)\s+", "", s)
            for sent in sentences(body):
                layer_sents[layer].append(sent)
            continue
        paragraphs += 1
        para_words.append(len(s.split()))
        ss = sentences(s)
        prose_sents.extend(ss)
        layer_sents[layer].extend(ss)
        if layer == "Simple":
            cur_simple.append(s)
    if cur_simple:
        simple_blocks.append(" ".join(cur_simple))

    all_sents = [x for v in layer_sents.values() for x in v]
    if not all_sents or skeleton:
        continue
    lens = [len(x.split()) for x in all_sents]
    short = sum(1 for n in lens if n <= 8) / len(lens)
    long_ = sum(1 for n in lens if n >= 30) / len(lens)
    openers = collections.Counter(" ".join(x.split()[:2]).lower() for x in all_sents)
    first = collections.Counter(x.split()[0].strip('"(').lower() for x in all_sents)
    words = sum(lens)
    you = sum(len(re.findall(r"\byou\b|\byour\b", x, re.I)) for x in all_sents)
    paren_defs = sum(len(re.findall(r"\([a-z][^)]{15,90}\)", x)) for x in all_sents)
    colon_frag = sum(1 for x in all_sents if re.search(r":\s", x))
    copula_start = sum(1 for x in all_sents if re.match(r"^(The|A|An|Each|Every|This|These|That|Those)\b", x))
    rec = dict(file=p.name[:52], skeleton=skeleton, words=words, sents=len(lens),
               avg=statistics.mean(lens), med=statistics.median(lens),
               short=short, long=long_,
               you_per_k=1000 * you / words, paren_per_k=1000 * paren_defs / words,
               colon_pct=colon_frag / len(lens), det_start=copula_start / len(lens),
               simple=layer_counts["Simple"], applied=layer_counts["Applied"],
               prof=layer_counts["Professional"], code=layer_counts["Code"],
               simple_avg_words=statistics.mean([len(b.split()) for b in simple_blocks]) if simple_blocks else 0,
               table_share=table_lines / n_lines, code_share=code_lines / n_lines,
               list_share=list_lines / n_lines, para_avg=statistics.mean(para_words) if para_words else 0,
               top_openers=openers.most_common(4))
    per_file.append(rec)
    for k, v in layer_sents.items():
        book[k].extend(len(x.split()) for x in v)
    book_openers.update(openers)
    book_first_words.update(first)
    totals["words"] += words

print("PER FILE (written chapters only)")
print(f"{'file':52} {'words':>6} {'avg':>5} {'<=8':>5} {'>=30':>5} {'you/k':>5} {'par/k':>5} {'col%':>5} {'det%':>5} {'S':>3} {'A':>3} {'P':>3} {'C':>3} {'Savg':>5} {'tbl%':>5} {'code%':>5} {'list%':>5}")
for r in per_file:
    if r["skeleton"]:
        continue
    print(f"{r['file']:52} {r['words']:6d} {r['avg']:5.1f} {r['short']*100:5.0f} {r['long']*100:5.0f} {r['you_per_k']:5.1f} {r['paren_per_k']:5.1f} {r['colon_pct']*100:5.0f} {r['det_start']*100:5.0f} {r['simple']:3d} {r['applied']:3d} {r['prof']:3d} {r['code']:3d} {r['simple_avg_words']:5.0f} {r['table_share']*100:5.0f} {r['code_share']*100:5.0f} {r['list_share']*100:5.0f}")

print()
print("SENTENCE LENGTH BY LAYER (whole book, written chapters)")
for k in ["Simple", "Applied", "Professional", "freeform"]:
    v = book.get(k, [])
    if not v:
        continue
    v_sorted = sorted(v)
    p90 = v_sorted[int(0.9 * len(v_sorted)) - 1]
    print(f"  {k:12} n={len(v):6d} avg={statistics.mean(v):5.1f} median={statistics.median(v):4.0f} p90={p90:3d} <=8w={100*sum(1 for n in v if n<=8)/len(v):4.0f}% 9-15w={100*sum(1 for n in v if 9<=n<=15)/len(v):4.0f}% 16-25w={100*sum(1 for n in v if 16<=n<=25)/len(v):4.0f}% >25w={100*sum(1 for n in v if n>25)/len(v):4.0f}%")

print()
print("MOST COMMON SENTENCE OPENERS (first two words, whole book)")
for o, n in book_openers.most_common(25):
    print(f"  {n:5d}  {o}")
print()
print("FIRST-WORD SHARE")
tot = sum(book_first_words.values())
for w, n in book_first_words.most_common(12):
    print(f"  {100*n/tot:5.1f}%  {w}")
print()
print(f"TOTAL WORDS (prose sentences, written chapters): {totals['words']}")
