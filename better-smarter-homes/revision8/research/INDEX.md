# Research Index (Revision 8)

Every piece of research the project has gathered, where it lives, and which chapter uses it.
Nothing is deleted from here; new findings are added under `new/`. The code library stays at
`../../revision6_code_library/` (12 MB of downloaded Oregon code text and the tested routes for
verifying citations; read its README before touching a Code entry).

## Folders

| Folder | What it holds | Numbering |
|---|---|---|
| `answers/` | Wave 3 (2026-07-12 to 07-15): every research question for chapters 2 to 36, answered with inline sources and a status tag (SETTLED, BLOCKED-PAYWALL, NOT-RESEARCHABLE-AHJ, OWNER-DESIGN-CHOICE). The authority for values and citations in Revision 8. | Final chapter numbers (the file prefix is the chapter) |
| `question-bank/` | The Wave 3 question bank (`research_questions_revision7.md`, about 2,000 questions with Lands-in tags), the per-area pre-research drafts that fed it (`drafts/`), the book map written while reading Revision 6, and the research playbook. | Final chapter numbers in the bank; topic names in the drafts |
| `wave2/` | The Revision 6 research wave: `research_questions_revision6.md` and its `answers/`. Older and shallower than Wave 3; still the source for some carried values. | Revision 6 numbering (21 chapters); find material by topic |
| `wave1/` | The Revision 5 research files (`research_questions_chNN_chNN.md`) and the owner-fabrication phase-2 file. Oldest; values here were carried into the manuscript long ago. | Revision 5 numbering; find material by topic |
| `OBLIGATIONS.md` | The Revision 7 final-pass ledger: cross-chapter obligations, question-bank corrections, owner flags, and the per-chapter list of known weak spots in the Revision 7 text. | Revision 7 chapter numbers equal the final numbers for 1 to 13; later numbers are the confirmed order, so they also match |
| `R7-CHAPTER-MAP.md` | The Revision 7 status board with per-chapter scope notes and boundary notes. Historical; BOOK_STRUCTURE.md supersedes its order. | Final numbers |
| `new/` | Findings made during Revision 8 writing, one file per chapter: `chNN.md`. Format below. | Final numbers |

## Answer files by chapter

| Chapter | Answer files in `answers/` |
|---|---|
| 1 | none (no research questions) |
| 2 | `ch02_oregon-code-and-compliance-map.md` |
| 3 | `ch03_land-site-and-feasibility.md`, `ch03_land_part2.md`, `ch03_land_part3.md`, `ch03_land_part4.md` |
| 4 | `ch04_legal_part1.md`, `ch04_legal_part2.md` |
| 5 | `ch05_soil.md` |
| 6 | `ch06_structural.md` |
| 7 | `ch07_what-concrete-enables.md` |
| 8 | `ch08_durability.md` |
| 9 | `ch09_passive.md` |
| 10 | `ch10_foundation.md` |
| 11 | `ch11_wall-system.md` |
| 12 | `ch12_blocks_part1.md`, `ch12_blocks_part2.md` |
| 13 | `ch13_masonry.md` |
| 14 | `ch14_envelope.md` |
| 15 | `ch15_roof.md` |
| 16 | `ch16_aesthetics.md` |
| 17 | `ch17_plumbing-supply.md` |
| 18 | `ch18_water-independence.md` |
| 19, 20 | `ch19-24_mep-energy.md` (the DWV and electrical-service items), plus `ch21-24_electrical-solar-hvac-smart.md` where it overlaps |
| 21, 22, 23, 24 | `ch21-24_electrical-solar-hvac-smart.md`, plus `ch19-24_mep-energy.md` where it overlaps |
| 25 | `ch25_interiors.md` |
| 26 | `ch26_developing-site.md` |
| 27 | `ch27_tools.md` |
| 28 | `ch28_materials.md` |
| 29 | `ch29_build-sequence.md` |
| 30 | `ch30_body-and-mind.md` |
| 31, 32, 33 | `ch31-33_inspection-testing-finance.md` |
| 34 | `ch34_resilience.md` |
| 35 | `ch35_documentation.md` |
| 36 | `ch36_business.md`, `ch36_business_part2.md`, `ch36_business_part3.md` |

`answers/_ANSWERING_BRIEF.md` is the brief the answering agents worked from; it explains the
status tags and the Lands-in lines.

## The `new/` format

One file per chapter, `new/chNN.md`, appended to, never rewritten. Each entry:

```
## 2026-10-27  <question in one line>
Finding: <what was found, with the number or statement exactly as the source gives it>
Source: <URL, or document title and section; the retrieval date>
Confidence: <high | medium | low> and why
Used in: <section N.k, or "open item">
```

A finding with no source is not filed and not used.

## Known corrections to the answer files

Listed in `OBLIGATIONS.md` under "Question-bank corrections". A writer who finds another error in
an answer file does not edit the answer file; the correction goes in `new/chNN.md` with the
evidence, and the orchestrator applies it to the answer file at closeout.
