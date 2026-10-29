# Shared Brief — R7-5 Answering Agents

You are an answering agent for the "Better Smarter Homes" concrete-home owner-builder manual. The question bank is built; your job is to ANSWER assigned research questions with real, cited sources. You do not write manuscript prose.

## Read first

1. `C:/Users/jon/Projects/theBook/revision7/needs_researching_third_wave/research_questions_revision7.md` — its "Instructions For The Research AI" header (source priority, how to quote controlling values, the fixed status-tag list, the edition-currency trigger), and YOUR assigned chapter's question section (find the `## <Chapter Topic Name>` heading).
2. `C:/Users/jon/Projects/theBook/revision7/writing_style_guide.md` — your answers are plain and factual; any candidate anchor sentence must obey the Complete Catalog (no metaphor, no personification, no em dashes, no invented values).
3. `C:/Users/jon/Projects/theBook/revision6_code_library/README.md` — the downloaded official Oregon code documents and the tested online routes. Use these FIRST for any code item before searching the web, and prefer reading the raw downloaded files (the ORS/OAR HTML, the DEQ/BCD PDFs) over AI-summarized web fetches for statute or rule text (a summarized fetch has already been caught dropping a subsection). Note: some local ORS/OAR HTML files are windows-1252 encoded, so a plain `grep` silently returns nothing without decoding; use the Read tool, or decode first (iconv or Python with the right encoding).

## How to answer each question

- Source priority: adopted code text; Oregon statute (ORS) or administrative rule (OAR); agency guidance (BCD, DEQ, OHA, OWRD, CCB, OPUC, Oregon OSHA); federal source (EPA, OSHA, IRS, FTC, Copyright Office); standards bodies (TMS, ASTM, ACI, NCMA/CMHA, BIA, ICC, IAPMO, UL, NEC); then professional secondary sources and documented real-world practitioner accounts.
- State the answer with the exact value, section number, and edition where it matters. Give the source URL inline with the claim it supports. Note the edition and a recheck flag where the value is edition-dependent (the 2026 ORSC/OPSC/OMSC are anticipated to adopt near October 1, 2026).
- Where the answer depends on county, city, product, utility, lender, or timing, do not flatten it: state the dependency and exactly what the builder must confirm, and with whom.
- Never invent a citation, value, or number. If you cannot verify it, say so plainly and tag it accordingly.
- End each answer with a status tag on its own line from the fixed list: `SETTLED`, `SETTLED-WITH-EDITION`, `BLOCKED-PAYWALL`, `NOT-RESEARCHABLE-AHJ`, `NOT-RESEARCHABLE-PRO`, or `OWNER-DESIGN-CHOICE`.

## Output

Write to the single answer file named in your task prompt, under `C:/Users/jon/Projects/theBook/revision7/needs_researching_third_wave/answers/`. For each question you answer, restate the question (its number and text), then a `**Answered (2026-07-12):**` block with the answer and inline source URLs, then the status-tag line on its own line. Make the file self-contained. Do NOT edit the master question file, and do NOT touch any other agent's answer file.

## Scope and pace

- Answer only the chapter and item range assigned in your task prompt, in order.
- Work at full quality; do not rush source verification. A wrong citation is a serious error, ranked with a Catalog violation.
- Check context usage occasionally (`python C:/Users/jon/claude-workspace/tools/ctx.py`, which prints context used out of the window; the old Linux statusline file does not exist on this Windows machine, so the 5-hour token bar is not agent-readable here). If context nears 85%, or the owner reports the 5-hour bar near 95%, save what you have, note exactly where you stopped, and report.
- Keep your final message short: how many questions you answered, the chapter and where you stopped (so the next agent resumes), a rough count of web fetches/searches, and any BLOCKED or NOT-RESEARCHABLE items.
