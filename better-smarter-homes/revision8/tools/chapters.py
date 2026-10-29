"""The 36 chapters in final order, with the Revision 7 file each one was built from.

lint.py reads this for its word-count baseline (a Revision 8 chapter should not come out shorter
than its Revision 7 source unless its Open items say what went). A future build can read it for
the order of the book. Read-only data: nothing here writes a file.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
R7 = HERE.parent.parent / "revision7" / "manuscript"

# final number, Revision 7 source file, final slug (the Revision 8 file is g1_ch_NN_<slug>.md)
ORDER = [
    (1, "g1_ch_01_purpose-principles-and-how-to-use-this-book.md", "purpose-principles-and-how-to-use-this-book"),
    (2, "g1_ch_02_oregon-code-and-compliance-map.md", "oregon-code-and-compliance-map"),
    (3, "g1_ch_03_land-site-and-feasibility.md", "land-site-and-feasibility"),
    (4, "g1_ch_04_legal-permits-and-owner-builder-rules.md", "legal-permits-and-owner-builder-rules"),
    (5, "g1_ch_05_soil-ground-prep-drainage-and-foundation-risk.md", "soil-ground-prep-drainage-and-foundation-risk"),
    (6, "g1_ch_06_structural-system-and-concrete-design.md", "structural-system-and-concrete-design"),
    (7, "g1_chNEW_what-concrete-uniquely-enables.md", "what-concrete-uniquely-enables"),
    (8, "g1_chNEW_designing-for-centuries-durability.md", "designing-for-centuries-durability-engineering"),
    (9, "g1_chNEW_passive-and-bioclimatic-design.md", "passive-and-bioclimatic-design"),
    (10, "g1_ch_07_foundation-basement-slabs-and-concrete-placement.md", "foundation-basement-slabs-and-concrete-placement"),
    (11, "g1_ch_08_the-wall-system-foundation-to-roofline.md", "the-wall-system-foundation-to-roofline"),
    (12, "g1_ch_09_owner-made-blocks-and-alternative-concretes.md", "owner-made-blocks-and-alternative-concretes"),
    (13, "g1_ch_10_masonry-craft-laying-and-stacking-block-and-brick.md", "masonry-craft-laying-and-stacking-block-and-brick"),
    (14, "g1_ch_11_envelope-waterproofing-thermal-performance-and-radon.md", "envelope-waterproofing-thermal-performance-and-radon"),
    (15, "g1_chNEW_roof-system-and-roof-wall-junctions.md", "roof-system-and-roof-wall-junctions"),
    (16, "g1_chNEW_aesthetics-and-architectural-expression.md", "aesthetics-and-architectural-expression"),
    (17, "g1_ch_12_plumbing-water-supply-pressure-treatment-and-hot-water.md", "plumbing-water-supply-pressure-treatment-and-hot-water"),
    (18, "g1_chNEW_water-independence.md", "water-independence"),
    (19, "g1_ch_13_plumbing-dwv-sewage-venting-slope-distance-and-fixtures.md", "plumbing-dwv-sewage-venting-slope-distance-and-fixtures"),
    (20, "g1_ch_14_electrical-service-panels-grounding-and-load-planning.md", "electrical-service-panels-grounding-and-load-planning"),
    (21, "g1_ch_15_electrical-branch-circuits-wire-size-voltage-drop-lighting-low-voltage-and-future-power.md", "electrical-branch-circuits-wire-size-voltage-drop-lighting-low-voltage-and-future-power"),
    (22, "g1_ch_16_solar-battery-and-energy-independence.md", "solar-battery-and-energy-independence"),
    (23, "g1_ch_17_hvac-ventilation-humidity-and-air-quality.md", "hvac-ventilation-humidity-and-air-quality"),
    (24, "g1_ch_18_smart-home-network-security-and-local-automation.md", "smart-home-network-security-and-local-automation"),
    (25, "g1_ch_19_interiors-finishes-accessibility-and-livability.md", "interiors-finishes-accessibility-and-livability"),
    (26, "g1_chNEW_developing-the-site.md", "developing-the-site-shop-block-yard-and-outbuildings"),
    (27, "g1_chNEW_tools-equipment-and-owner-builder-shop.md", "tools-equipment-and-the-owner-builder-shop"),
    (28, "g1_ch_20_materials-suppliers-procurement-and-substitution.md", "materials-suppliers-procurement-and-substitution"),
    (29, "g1_ch_21_build-sequence-and-site-coordination.md", "build-sequence-and-site-coordination"),
    (30, "g1_chNEW_owner-builder-body-and-mind.md", "the-owner-builders-body-and-mind"),
    (31, "g1_ch_22_inspection-and-approval-sequence.md", "inspection-and-approval-sequence"),
    (32, "g1_ch_23_testing-commissioning-and-quality-control.md", "testing-commissioning-and-quality-control"),
    (33, "g1_ch_24_personal-project-finance-budget-financing-and-cash-flow.md", "personal-project-finance-budget-financing-and-cash-flow"),
    (34, "g1_chNEW_resilience-and-disaster-independence.md", "resilience-and-disaster-independence"),
    (35, "g1_ch_25_documentation-maintenance-and-future-upgrades.md", "documentation-maintenance-and-future-upgrades"),
    (36, "g1_ch_26_business-and-brand-framework.md", "business-and-brand-framework"),
]
