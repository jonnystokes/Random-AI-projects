
## Section 0 — Purpose and Philosophy

### 0.1 Why This Document Exists

This document is a personal guide. It captures every design decision, every tested idea, and every reason behind them, so the work doesn't live only in one person's head. It is meant to be read for reference and for enjoyment of the ideas themselves.

The document serves four purposes:
1. A reference manual for the build
2. A record of the design philosophy so future improvements stay consistent
3. A resource a family member can read to understand the plan
4. A starting point that a technical professional could use later to help refine the design

Technical framing: This is a living design specification (a spec document that grows and changes over time) maintained as the single source of truth for the Better Smarter Homes Model 1.

### 0.2 The 1000-Year Goal

The goal is a home that lasts many lifetimes. The **core structure** — the concrete walls, the floors, the foundation — is what we hope will last 1000 years. Everything else in a house wears out much faster: paint, carpet, windows, appliances, roofing material, insulation, wiring, plumbing fittings. Those will be replaced many times over the life of the building. But the bones of the building should outlast every owner who ever lives in it.

Future testing and design improvements will push every part of the home toward a longer useful life. The goal isn't to achieve 1000 years in the first build. It is to establish a foundation so strong that future generations only need to replace the easily-replaceable parts, not the building itself.

Technical framing: The structural envelope (the concrete masonry load-bearing elements, foundation mat, and floor slabs) targets a multi-century service life through low-permeability concrete (concrete that water and oxygen cannot easily penetrate), pozzolanic admixtures (additives like fly ash or silica fume that make concrete denser and stronger over time), corrosion-protected reinforcement, and generous rebar cover. Non-structural systems (MEP — mechanical, electrical, plumbing — finishes, roofing surface, insulation) are designed for accessibility and replacement rather than permanence, because those components inherently have shorter service lives.

### 0.3 Design Principles

Three words drive every decision:

**Reliability** — The building and its systems should work every time, without surprises. If something can fail, it should fail in a way that gives warning, not all at once.

**Durability** — Components should last as long as possible. Where a choice exists between a cheap option that lasts 20 years and a more expensive option that lasts 100 years, the longer-lasting option usually wins.

**Simplicity** — The simpler the system, the less can go wrong. Complicated solutions should only be used when they solve real problems that simpler ones can't.

Additional philosophies that shape the design:
- **Overbuild** the things that are hard to fix later. Bones, foundation, envelope.
- **Testing-driven** — decisions backed by actual experiments, not assumptions.
- **Repairable** — every system accessible, every component replaceable, nothing buried where it can't be reached.
- **Fireproof** — concrete and steel structure, no wood framing anywhere.
- **Smart** — technology integrated throughout, but locally hosted and independent.

### 0.4 The Smart Home Rule (Independence from Outside Networks)

Every smart technology in the home must work without an internet connection. Cloud services, third-party servers, and subscription-based features are allowed to add convenience, but the core function must survive if those services disappear or the internet goes down.

Plain language: If a company goes out of business or the internet stops working, the house should still function. Lights still turn on. Heat still works. Doors still lock. Presence detectors still detect presence. Security still secures.

Technical framing: All critical home automation runs on a local hub or edge controller. External API (application programming interface — how one piece of software talks to another) calls are optional enhancements, never dependencies. Network infrastructure is wired wherever possible (Ethernet to every room) for reliability, with wireless as a convenience layer on top.

### 0.5 How to Read This Document

Every section follows the same pattern.

**First:** Plain language. What this is about, in words anyone can follow.

**Then:** Technical detail. The same information with specific terminology, materials, assemblies, and method.

**Then, if applicable:** Numbers and code references. Measurements, load capacities, R-values (how well insulation blocks heat), and the building code sections that apply. Each code reference includes a keyword explaining what the code is about — for example, "ORSC R301.3 (story height — structural height limits)" — so the reader knows why the code matters without having to look it up.

Technical terms are defined in parentheses on first use. Readers who already know the term can skip the parenthetical; readers who don't get a quick definition without leaving the page.

Some sections may add a third layer — a deeper technical appendix note — when the topic is complex enough that two layers aren't enough. Most sections will only need two.

---

*End of Section 0 — Purpose and Philosophy*
