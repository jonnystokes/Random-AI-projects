# Chapter 14 — Documentation, Maintenance, and Future Upgrades

*Records, maintenance, and future upgrades after the build is done*

A house designed for a very long service life needs more than strong materials. It needs records, maintenance habits, replacement paths, and a way for future owners to understand what was built. This chapter gathers the long-term ownership material in one place.

---

## 14.1 Documentation and the Project Binder

**Plain language:** Every decision, every inspection, every spec, every material choice is recorded in a project binder — a physical binder and a digital backup. Over 5 years of building, the owner will forget a lot. The binder is the memory. Future owners (or the owner's future self) will need it.

**Technical detail:** Project binder contents:

**Physical binder (3-inch three-ring) with tabbed sections:**
1. **Property and legal** — deed, survey, title, zoning, permits
2. **Design** — architectural plans, engineering calcs, mechanical drawings (paper copy)
3. **Permit and inspection records** — every permit, every inspection sign-off
4. **Materials and suppliers** — what was installed, who supplied it, warranty info
5. **Subcontractors and contractors** — who did what, contact info, work performed
6. **Systems documentation** — HVAC manuals, electrical panel schedules, plumbing isometrics
7. **Maintenance schedule** — what to do when
8. **As-built drawings** — updated from design drawings with actual routing and locations
9. **Test results** — blower door, water pressure, well yield, energy use, etc.
10. **Photos** — hard-copy printouts of key construction phases for reference

**Digital backup (external hard drive + cloud backup):**
- **Full photo archive** — thousands of construction photos, labeled and organized by phase
- **All documents scanned** — searchable PDF
- **Video documentation** of complex systems (walk-throughs of the service layer, each manifold, each panel)
- **CAD files** from the design phase
- **Software backups** — Home Assistant configuration, etc. (see the Smart Home and Network Systems chapter)

**Update cadence:**
- **Weekly during construction** — add photos, update phase status, file any new paperwork
- **At every inspection** — file the inspection record, note any conditions
- **Annually after completion** — add maintenance notes, photo current state, note any changes or repairs

**Handoff-readiness:**
- **The binder should stand alone** — if the owner disappears, the next owner can pick up the binder and understand everything
- **Future resale** benefits directly from thorough documentation
- **Future renovations** benefit from knowing where every pipe and wire runs

---

## 14.2 Contingency and Lessons-Learned Planning

**Plain language:** Something will go wrong. A weather event will delay a pour. A material will arrive damaged. An inspection will fail. A family emergency will pause work for months. The plan accommodates these — not by rigid scheduling but by building in flex, and by keeping a running list of lessons learned for the next build.

**Technical detail:** Contingency approach:

**Time contingency:**
- **25–50% buffer on every phase estimate** — no phase ever goes exactly as planned
- **Seasonal flexibility** — if a phase misses its weather window, shift to indoor work and resume next season
- **Life-event flexibility** — job changes, children, illness — build schedule bends without breaking

**Budget contingency:**
- **10–15% contingency line in the overall budget** — for cost overruns and surprises
- **Ongoing cost tracking** — monthly review of actuals vs. plan
- **Adjustment points** — quarterly review of remaining budget vs. remaining scope; adjust scope if needed (defer or simplify)

**Quality contingency:**
- **Hold points** — don't cover up anything until inspected and photographed
- **Rework budget** — assume 5–10% of work will need redoing at some point
- **External review** — occasionally have a knowledgeable friend or contractor walk the site for a fresh perspective

**Health and wellness contingency:**
- **Injury plan** — how does the build pause if the owner-builder gets hurt?
- **Burnout prevention** — see the pacing discussion on pacing
- **Partner support** — frequent check-ins on family impact

**Lessons-learned journal:**
- **Ongoing notes** during the build — what worked, what didn't, what I'd do differently
- **Referenced for subsequent builds** (if the owner builds another BSH home)
- **Shared with the BSH brand** for future owner-builders (see the Land, Site, and Feasibility chapter3)

**Stop-work conditions:**
- **Serious safety incident** — pause, investigate, fix before continuing
- **Inspection failure with major rework** — pause, understand root cause, replan
- **Life emergency** — pause, handle life, return when possible
- **Financial stop** — ran out of money; stop, regroup, either raise funds or scale back

**Every build is one-of-one** — this plan anticipates learning. Later BSH homes (if the owner builds more) will go faster, cleaner, and with fewer surprises.

---

## 14.3 Technology Upgrade Strategy

**Plain language:** Technology changes fast. A home built today will see several generations of smart devices come and go. The design anticipates this: the wiring and infrastructure last, the devices are expected to be replaced, and the automation logic is written in a way that new devices can slot in without rewriting everything.

**Technical detail:** Technology lifecycle management:

**What lasts:**
- **Ethernet wiring (Cat6A)** — 20+ years of usefulness
- **Conduit (in-wall or service layer)** — perpetual
- **Network rack and basic rack infrastructure** — 15–20 years
- **Structural AV wiring (speaker wire, coax)** — 20–40 years

**What gets replaced on a cycle:**
- **Network equipment** (switches, routers, access points) — 5–8 year cycle
- **Smart hub hardware** — 5–10 year cycle
- **Cameras** — 5–10 year cycle (replaced for better sensors, better night vision, new features)
- **Smart switches** — 10–15 year cycle (Z-Wave/Lutron have been stable — long life)
- **Sensors** (motion, door, leak) — 5–10 year cycle, or on battery depletion
- **Smart locks** — 5–10 year cycle (mechanical locks last 30+ years)
- **Displays and TVs** — 7–12 year cycle

**Migration strategy for smart hub changes:**
- **Home Assistant configuration in version control (Git)** — full history of changes, easy rollback
- **Backup and restore procedures** — new hub can be restored from backup in under an hour
- **YAML configuration files** — human-readable, editable, portable (mostly — Home Assistant is slowly moving to UI config)
- **Documentation of every automation and integration** — in the project binder

**Vendor independence:**
- **Avoid any single vendor owning more than one category** of the smart home — don't put lights + locks + cameras + thermostat all in one ecosystem
- **Matter-first purchasing policy** as Matter matures — ensures cross-vendor compatibility

**Sunset planning:**
- **Annual review** — check status of every service and device manufacturer — any at risk of discontinuation?
- **Graceful migration** — replace sunsetting devices before forced end-of-life
- **Replacement budget** — reserve ~$500–$2,000/year for smart home updates and replacements

**What to NOT upgrade:**
- **Working devices don't need replacement** — resist the urge to upgrade every year
- **Infrastructure doesn't need replacing until it fails** — network, wiring, speakers, conduit all last longer than technology trends suggest
- **The automation logic is stable** — the "goodnight" scene from 2026 still makes sense in 2046 even if every device it touches has been replaced twice

**Future-facing considerations:**
- **Matter and Thread maturation** — likely dominates 2026–2035 smart home
- **Local AI for natural language and anomaly detection** — small language models running on home servers, recognizing patterns in energy use, detecting intrusions, personalizing voice interaction
- **Ambient computing** — sensors and intelligence blended into the house, less dependence on screens and explicit commands
- **Energy grid interaction** — bi-directional EV charging (V2H, vehicle-to-home), dynamic demand response
- **Health and environmental monitoring** — air quality, water quality, even basic health metrics integrated into the home system

**Key principle:** the goal is a house that continues to feel modern and responsive 20 years from now — because the architecture is flexible, not because everything was cutting-edge on build day.

---

## 14.4 Maintenance and Replacement Philosophy

The structure is intended to last far longer than the systems attached to it. That only works if the replaceable parts stay visible, documented, and accessible.

- Keep as-built drawings current after every change.
- Label every circuit, valve, conduit, data run, and shutoff.
- Photograph work before it is covered.
- Keep product manuals, warranties, permits, inspections, and test results together.
- Treat plumbing, electrical, HVAC, finishes, roofing surfaces, sensors, and network hardware as service-life items, not permanent parts of the house.
- Review the house annually for water, air, electrical, controls, and documentation issues.
