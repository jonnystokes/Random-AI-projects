# Revision 6 Code Library

Created: 2026-07-09; expanded the same day with full OAR rule text, three more ORS chapters, and the BCD energy documents.

Purpose: give a writing session offline copies of the free official Oregon documents, plus the tested online routes for reading the copyrighted model-code text. Use this when verifying or expanding a `Code` entry.

## How To Verify A Citation While Writing

1. Check the matching `revision5/research_questions_*.md` file first. The appended research already extracts most needed values with sources.
2. For ORSC, OESC, OPSC, OMSC, or OSSC section text, fetch the UpCodes page for the section (routes below). UpCodes serves the full Oregon-adopted text and is machine-readable. Verified example: ORSC R401.3 and R403.1.6 text fetched successfully on 2026-07-09.
3. UpCodes integrates Oregon amendments without marking them. For any amendment-sensitive section, cross-check against the official Oregon amendment PDFs in this folder.
4. For statutes (ORS) and administrative rules (OAR), use the downloaded files in `ors/` and `oar/`, or fetch the public sources listed below.
5. If a value cannot be verified by these routes, mark it for research. Never guess.

## Online Routes (tested 2026-07-09)

| Code | Edition | Official viewer | Machine-readable route |
|---|---|---|---|
| ORSC (residential) | 2023, based on 2021 IRC | codes.iccsafe.org/content/ORRC2023P1 (browser only; returns 403 to tools) | up.codes/viewer/oregon/irc-2021/chapter/N/... (full text, fetchable, no paywall observed) |
| OESC (electrical) | 2023, based on 2023 NEC | nfpa.org free access (requires account, browser only) | up.codes/viewer/oregon/nfpa-70-2023 plus the amendments table PDF in this folder |
| OPSC (plumbing) | 2023, based on 2021 UPC | epubs.iapmo.org/2023/OPC/ (JavaScript viewer, not fetchable) | up.codes/codes/oregon lists the OPSC viewer; research files hold the extracted OPSC values |
| OMSC (mechanical) | 2025 | codes.iccsafe.org/content/ORMSC2025P1 (browser only) | up.codes/codes/oregon |
| OSSC (commercial structural) | 2025 | codes.iccsafe.org/content/ORSSC2025P1 (browser only) | up.codes/codes/oregon |
| OEESC (commercial energy) | 2025 | Full PDF from BCD (downloaded here) | `25oeesc.pdf` |
| ORS (statutes) | current | oregonlegislature.gov/bills_laws/ors/orsNNN.html | downloaded in `ors/`, plain HTML |
| OAR (admin rules) | current | secure.sos.state.or.us/oard/ | oregon.public.law/rules/oar_chapter_NNN_division_NN (fetchable; division indexes downloaded in `oar/`, individual rules fetched per page) |
| BCD adopted-codes hub | - | oregon.gov/bcd/codes-stand/Pages/adopted-codes.aspx | fetchable; source of the PDFs below |

## Downloaded Files

Oregon-published PDFs (root of this folder):

- `23orsc-ch1.pdf` - full text of ORSC Chapter 1 (administration, permits, inspections, certificate of occupancy). The only ORSC chapter BCD publishes as a PDF.
- `23orsc-errata.pdf`, `23orsc-R310-amend.pdf`, `23orsc-stacked-amend.pdf`, `23orsc-r327-amend.pdf` - ORSC 2023 errata and amendments (R310 emergency escape, stacked amendments, R327 wildfire hardening).
- `sam-26-01-23orscref22ossc.pdf` - statewide alternate method 26-01.
- `23oesc-table1-E.pdf` - the OESC Table 1-E Oregon electrical amendments. Combined with NEC 2023, this defines the OESC.
- `25omsc-errata.pdf`, `25ossc-errata.pdf`, `25ossc-ch34-amendments.pdf` - 2025 mechanical and structural errata/amendments.
- `25oeesc.pdf` - the complete 2025 Oregon Energy Efficiency Specialty Code (commercial; residential energy lives in ORSC Chapter 11).
- `orsc-blower-door-form.pdf` - the BCD blower-door results reporting checklist (April 2024); the source for the 3.25/2.75 ACH50 thresholds.
- `res-techb-slabedge-insulation.pdf` - BCD technical bulletin with the verbatim Table N1101.1(1) envelope values.
- `os-Table1MinSepDistances.pdf` - DEQ onsite-wastewater minimum separation distances (OAR 340-071-0220 Table 1).
- `25omsc-matrix.pdf` - the 2025 OMSC code review committee matrix (September 2024): the de facto amendment summary BCD has not yet published formally; shows the dwelling-ventilation amendments item by item.
- `calculator-orsc-tradeoff.xlsx` - BCD's envelope trade-off calculator for ORSC Chapter 11 (Table N1104.1(1) UA demonstration); the compliance path for a concrete roof that cannot meet the prescriptive R-value.

`ors/` - full HTML of ORS chapters 012 (limitations and statute of repose), 105 (property records), 165 (recording law), 215 (county land use), 227 (city planning), 447 (plumbing law), 455 (building code), 476 (fire, CO alarms), 479 (electrical), 480 (LP gas), 537 (water and wells), 671 (architects and landscape), 672 (engineering, surveying), 693 (plumbers), 701 (CCB and owner-builder).

`oar/` - full rule text for OAR 340-071 (`oar-340-071-full.html`, the current onsite wastewater rules including the 2026 changes), OAR 340-073 (`oar-340-073-full.html`, construction standards), and OAR 918-305 (`oar-918-305-full.html`, electrical program) from the SOS database, plus division index pages for 340-071, 918-8, 918-305, 918-440, 918-480, and 918-750. For any other division's full text, use the SOS route `secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=NNNN` (division IDs are on the index pages) or fetch individual rules from oregon.public.law.

## What Cannot Be Obtained Without Purchase

These stay behind paywalls. The research files already extract the values the manuscript needs from them; buying is a last resort only if a future chapter needs sustained new material from one of them.

- ACI 318, ACI 332, ACI 301 (concrete design and residential concrete): purchase from ACI or read excerpts as adopted through OSSC references.
- ASTM standards (C90, C94, C1077, E1745, and others): purchase per standard from ASTM.
- ASHRAE 62.2 and handbook chapters: ASHRAE sells; read-only versions of some standards at ashrae.org.
- TMS 402/602 (masonry): purchase from TMS.
- TCNA Handbook (tile): purchase.
- NEC 2023 full text: free read-only at nfpa.org after creating a free account (browser only); the owner can do this in a browser if a session ever needs NEC text beyond the amendments table and the research extracts.

Nothing on this list blocks Revision 6. The manuscript cites these standards by number and describes what they control, which is lawful and does not require reproducing their text.
