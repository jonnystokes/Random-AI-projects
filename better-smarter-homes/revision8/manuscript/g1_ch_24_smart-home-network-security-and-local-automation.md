# Chapter 24: Smart Home, Network, Security, and Local Automation

Every function that keeps the house safe and usable works with the internet down. Lights run from wall switches, water shuts off at a valve with a handle, and heat comes from the equipment's own controls. Smoke alarms sound each other over their own wiring. Inside the house, a controller runs the automation over a wired network, and the internet adds remote access, updates and notifications. Cable, conduit and the rack go in before concrete and finishes close the walls, and they outlast every device on them by decades. Low-voltage wiring here follows the 2026 Oregon Electrical Specialty Code, in force since October 1, 2026, and Oregon's recording law sets what the cameras may hear.

> **Jon's note.** [JON: drafted from the record, confirm or rewrite] I want the house to keep working when the internet is down, when a company switches off its servers, or when a subscription lapses. On a rural site the connection drops more often than in town, and a concrete house will outlive every gadget I put in it. So the money goes first into what I cannot add later: the cables, the conduit, the rack and the battery behind it. Devices are replaceable, and I want to be able to repair or swap any one of them myself without the company that sold it. Nothing that keeps people safe or the house dry waits on an automation. [JON: Home Assistant as the controller, or another platform?] [JON: do you want voice control in the house at all?]

## 24.1 What keeps working when the network is down

**Simple**

Smart devices stop working for reasons that have nothing to do with the device. In a storm the internet line goes down. Or the company that made a lamp or a lock shuts off its servers, and the device stops answering. In this house the logic runs on a controller in a cabinet indoors, and every device it touches also has a plain manual control. When the controller itself fails, the switches, valves, thermostats and door hardware still work by hand.

**Applied**

| Function | Keeps working without the controller through | The controller adds |
|---|---|---|
| Lighting | Hardwired wall switches | Scenes, schedules, occupancy control |
| Water shutoff | A motorized valve with a manual handle | Automatic closing when a leak sensor trips |
| Heating and ventilation | The equipment's own controls and wired thermostats | Scheduling, coordination, alerts |
| Locks | An interior thumbturn and a metal key | Guest codes, status, auto-lock |
| Smoke and carbon monoxide alarms | Their own interconnect wiring and backup batteries | A phone notification |
| Cameras | Recording to the recorder in the rack | Motion alerts and remote viewing |
| Garage door | The wall button and the opener's own safety system | Left-open alerts and scheduled closing |

1. Fill in the manual column for every automated device before buying it. Leave off the list any device without a manual control.
2. Choose devices that keep working over a local radio or a documented local connection when the internet is cut.
3. Put the controller, the network equipment and the camera recorder on the rack's battery unit, fed from the battery-backed panel.
4. Record where each manual override is, in the house binder and on a card in the mechanical room.

**Professional**

Local-first means the automation logic and the device control both run on an owner-controlled controller inside the house. Cloud services are opt-in and limited to remote access, software updates and notifications. Cloud-dependent devices, whose logic lives on a manufacturer's server, are kept out of the design. Such a device stops working when the maker shuts the backend, sells the product line, or moves a free interface behind a subscription. Its hardware is intact and becomes electronic waste, because the intelligence it ran on was never in the house.

Two measures keep a dead controller from becoming a dead house. Through an outage, the controller, the switches, the router and any well-pump control electronics stay on the battery-backed circuit. Between the grid dropping and the backup source picking up the load, a small uninterruptible power supply covers the gap. Every safety- or function-critical device also has an override that needs no controller, network or app, so a dead controller, switch or software release leaves an ordinary house run by hand.

Code-required functions keep their required behavior with the controller off. ORSC R314 and R315 require the smoke and carbon monoxide alarms to be hardwired, battery-backed and interconnected. Those rules and their Code entries are in the branch-circuit chapter. ORSC R311.2 governs the egress door, stated with the locks below. The equipment's own safety limits, the panel's overcurrent and ground-fault protection and the required disconnects stay outside the automation. Reading and logging their state is all the controller does with them.

## 24.2 Who may do the work, and which permits apply

**Simple**

Oregon lets you install the network, security and control wiring in your own house without an electrician's license. That exemption covers electrical work on a house your family owns and does not plan to sell or rent. Your work still has to meet the electrical code. It goes on a permit with inspections unless a specific rule exempts it. State law takes telephone and data systems inside a one- or two-family house out of the licensing and permit law. Paid installers hold a state limited-energy license, and alarm work takes the higher of its two classes.

**Applied**

1. Before design, ask the site's electrical inspector in writing whether the data cabling goes on the low-voltage permit, and which inspections apply.
2. Apply for the owner's electrical permit before the first low-voltage cable goes in, unless the inspector's written answer exempts the work.
3. Install the Class 2 and communications wiring yourself, to the electrical code, on the house the family owns.
4. For paid data, control or intercom wiring, hire a Class B limited energy technician or a contractor who employs one.
5. For paid fire alarm, burglar alarm or security wiring, hire a Class A limited energy technician.
6. Use a CCB-licensed residential contractor with the board's endorsement for paid telephone, cable TV, audio or doorbell prewiring.
7. File the permit, each inspection result and the inspector's written answers in the house binder.

**Professional**

Under ORS 479.540(1) the owner's license exemption turns on ownership and on the property not being held for sale or rent. Its text stands beside the building and plumbing exemptions in the legal chapter. Under ORS 479.560(1)(a) the state or its agent issues the owner's electrical permit, so the owner applies and calls for inspections in the owner's own name. Limited-energy wiring is electrical installation under the same law. ORS 479.905(4) defines limited-energy electrical activity as wiring and products of not more than 100 volt-amperes in Class 2 and Class 3 installations. That definition takes in the network, sensor, camera and control wiring of this house.

ORS 479.540(9)(f) leaves two questions for the local electrical official. One is whether Ethernet structured cabling counts as a telecommunications system under that paragraph. Its closing clause, installation by a telecommunications service provider, may limit the dwelling item as well as the multifamily item, and that is the second question. ORS 479.530(6) places the demarcation point where the provider's cabling or protector meets the customer's premises. Power over Ethernet cabling also carries Class 2 power to cameras and access points, and the same answer has to address that power.

Two rules in the entries below narrow the paperwork at the margins. Because a Class 2 product fed from a listed transformer needs no certification mark, an unlisted sensor on a 24-volt supply is lawful where a line-voltage one would not be. The garage-door permit relief covers only wiring added after a house is wired, so a new house's original garage-door wiring goes on the permit with the rest, and the small-systems license waiver leaves the permit rules untouched.

Anyone paid to do this wiring needs a license or a statutory exemption. Under ORS 479.840(1)(b) a limited energy contractor license costs $125 a year, and the people doing the work hold the Class A or Class B technician license. Costs are 2026 figures unless a different year is given. ORS 479.940 lets a CCB-licensed residential contractor with the board's endorsement prewire telephone, cable television, audio and doorbells in houses of one or two families without an electrical license. ORS 479.940(5) keeps the permit and code requirements for that work.

**Code**

```
License-exempt electrical work still meets the code and takes a permit.
  Exempt work complies with ORS chapters 455 and 479 and their rules, and no one works on a new electrical installation without a permit except as ORS 479.540 provides.
  Source: ORS 479.540(1)(a); ORS 479.550(1).

Telephone and data systems inside a one- or two-family dwelling are outside the Electrical Safety Law.
  ORS 479.510 to 479.945 do not apply to installing telecommunications systems on the customer side of the demarcation point in one- and two-family dwellings.
  Source: ORS 479.540(9)(f).

Class 2 products behind a listed Class 2 transformer need no product certification.
  Products other than wiring are exempt, except in damp or wet locations, air-handling spaces, OESC Chapter 5 areas and protective signaling systems.
  Source: OAR 918-261-0039(1).

Garage-door control wiring added later needs no permit.
  Class 2 wiring on the load side of a listed garage-door controller in a one- or two-family dwelling, when it is not part of the original wiring.
  Source: OAR 918-261-0039(2).

A few small limited-energy systems need no installer's license.
  Class 2 and 3 systems of 100 VA or less: single-station smoke detectors, closed-circuit TV and master-antenna TV in buildings of three stories or less, and intercom and audio in one- and two-family dwellings.
  Source: OAR 918-282-0110(4).

Paid limited-energy work takes a technician license of the right class.
  Class A covers all limited-energy systems, and Class B covers all except protective signaling: fire alarm, burglar alarm, security, nurse call and voice evacuation.
  Source: ORS 479.905(1), (2), (5); ORS 479.910(1).
```

## 24.3 Radio through concrete

**Simple**

Why does a concrete house need more cable than a wood one? Concrete and the steel bars inside it absorb and reflect the 2.4-gigahertz radio band that Wi-Fi, Zigbee and Thread devices use. One concrete-block wall cuts such a signal to between one-sixteenth and one-thirtieth of its strength. Four inches of reinforced concrete cut it to between one-fortieth and one-two-hundredth. Z-Wave radios work near 908 megahertz, a lower frequency that passes through masonry better. Between rooms in this house the dependable link is a cable, with a wireless access point or a radio repeater at its end.

**Applied**

1. Mark on the floor plan every concrete or grouted-block wall between the rack and each room.
2. Plan one ceiling access point for each zone those walls enclose, and run a cable to each location.
3. Before the pour or the grout lift, set a sleeve or conduit through each wall the cable has to cross.
4. Place a mains-powered repeater, a hardwired smart switch or a plug-in module, on each side of any concrete wall the mesh must cross.
5. Put each battery sensor in a room that has a mains-powered repeater or an access point.
6. After fit-out, walk each room with a phone signal meter and read the controller's mesh map.
7. Add a repeater wherever a device shows a weak link or a single route.
8. Save the mesh map and the signal readings with the as-built drawings.

**Professional**

Loss through a wall depends on its thickness, its moisture and its steel. As planning figures, a single concrete-block wall takes 12 to 15 dB from a 2.4 GHz signal and a 4-inch reinforced concrete wall 16 to 23 dB. Rebar reflects part of the signal on top of the concrete's own absorption, so grouted, reinforced cells lose more than hollow block. Each 10 dB of loss divides received power by ten, and a 20 dB wall leaves one percent of the signal.

Higher frequencies lose more in the same wall, so Wi-Fi's 5 and 6 GHz bands reach fewer rooms through masonry than its 2.4 GHz band. Z-Wave's North American channels near 908 MHz penetrate concrete and masonry better than the 2.4 GHz band that Zigbee, Thread, Bluetooth and Wi-Fi share. They also sit outside that band's traffic. That sub-gigahertz channel is a physical reason to put security devices on Z-Wave in this house, apart from the local-first argument.

Battery-powered end devices do not relay mesh traffic. Mains-powered routers placed at planned points relay it, and a single hop across a 15 to 20 dB wall is not dependable. So a router on one side of such a wall needs a router or the wired backbone on the other side. Cable to each zone's access point takes the wall out of the radio path. Sleeves for that cable are set before the concrete is placed, because a core drilled through cured concrete later can cut reinforcement.

## 24.4 Structured cabling, conduit and the service entrance

**Simple**

Cables in the walls will outlast every device plugged into them, so the house gets one high-grade data cable everywhere. Every data line runs home to the rack, and any wall jack can take a new job by moving one patch cord there. Data cables keep a fixed distance from power wiring. Power wires induce electrical noise, and a fault could put house voltage on a data line. Empty conduit, plastic pipe with a pull string inside, runs to the roof and the outbuildings. Through it a future cable goes in without cutting concrete.

**Applied**

1. Use Category 6A solid 23 AWG cable with a riser (CMR) jacket for every data run.
2. Home-run every data, camera and access-point cable from its outlet to the patch panel in the rack.
3. Mark every drop on the floor plan before rough-in, with the count set by the final plan.
4. Run fiber, or empty 2-inch conduit for it, to any outbuilding more than 100 meters (328 feet) of cable from the rack.
5. Lay a spare 2-inch conduit with a pull string from the rack area to the roof plane, for solar monitoring cable and an antenna feed.
6. Stub empty conduit to each exterior wall elevation, for cameras and lighting added later.
7. Run a communications conduit with a pull string from the demarcation to the road, even where service starts by fixed wireless or satellite.
8. Cap and mark every buried conduit with a tracer wire and a staked or GPS-recorded end.
9. Keep communications and Class 2 cables 2 inches from power conductors.
10. Waive the 2 inches only where the power wiring is in raceway or metal-sheathed cable, or a continuous nonconductor separates them.
11. Never pull data cable through a drilled hole that carries a power cable.
12. Firestop every cable penetration of the garage separation and any other fire-rated assembly with a listed firestop system.
13. Seal each conduit where it passes from conditioned space to the outside.
14. Place the demarcation and the structured-media enclosure beside the electrical service, so the protector's bonding conductor runs less than 20 feet.
15. Bond the protector with 14 AWG copper or larger.
16. Pull cable listed for wet locations through underground conduit.
17. Label both ends of every cable and conduit, and photograph each wall before it closes.

**Professional**

CMR cable is permitted wherever CM is and in risers too, so one cable type serves every run without a location-by-location check. Category 6A at 23 AWG supports 10GBASE-T over the full 100-meter channel that TIA-568 defines, which leaves headroom for multi-gigabit access points and cameras through several equipment generations. Under the 2023 OESC this wiring falls under NEC Article 722 for cables, Article 725 for Class 2 and Class 3 circuits and Article 800 for communications.

Power over Ethernet carries power and data on one cable. It removes a separate circuit and outlet at each camera and access point, and one PoE switch on the UPS then backs up every powered device at once. Bundled PoE cables heat, and NEC 725.144 limits conductor current by gauge and bundle size. By the Ethernet Alliance's analysis of that table, 75°C Category 6A 23 AWG cable carries IEEE 802.3bt Class 8 power in bundles of up to 192 cables, against 91 for Category 5e 24 AWG. No residential bundle approaches either number. Code entries for the Class 2 separation and PoE rules are in the branch-circuit and low-voltage chapter.

Firestopping matters here chiefly at the garage-to-dwelling separation, the one rated assembly in a house whose other walls carry no rating. In poured concrete or grouted masonry the sleeve is the firestop's substrate, so its size and position are fixed before the pour.

At the demarcation, the primary protector drains surges on the incoming line into the same grounding electrode system as the power service. Kept short and straight, the bonding conductor holds the voltage difference between the two systems small during a strike, which is why the demarcation sits beside the service. Where that run cannot stay short, a separate rod for the communications protector is driven and bonded to the power electrodes.

Under the 2026 OESC the base code is the 2026 NEC. By EC&M's summary of the changes, that edition moved the interior communications and Class 2 rules into new Articles 720 to 723 and deleted Article 805. NEC Chapter 8 now covers only communications outside and entering buildings. The entries below give the 2023 section numbers. Oregon's 2026 amendments relax three general rules for limited-energy wiring. Conduit leaving the conditioned house is still sealed against warm-air circulation, but the sealant no longer has to be identified for the cable insulation (720.8(A)(1)). Cable ties need no securement listing (720.30(A)(3)). Outdoor raceways above grade get the wet-location relief in the last entry below.

**Code**

```
Communications cable carries the listing for its location.
  CM cable is permitted throughout a one- or two-family dwelling, risers included, and CMP is required in a plenum.
  Source: OESC/NEC 800.179 (2023 edition).

Communications and Class 2 cables stay separated from power conductors.
  At least 2 inches from light and power conductors, unless the power wiring is in raceway or metal-sheathed cable or a continuous nonconductor separates them.
  Source: OESC/NEC 800.133 and 725.136 (2023 edition).

Cable penetrations of fire-rated assemblies are firestopped.
  Openings through fire-resistance-rated walls, floors and ceilings are sealed by a method that keeps the assembly's rating.
  Source: OESC/NEC 800.26 and 300.21 (2023 edition).

The incoming communications protector is bonded to the power grounding system.
  Bonding conductor 14 AWG or larger and no longer than 20 feet in a one- or two-family dwelling, or a separate rod bonded to the power electrodes with 6 AWG copper.
  Source: OESC/NEC 800.100 (2023 edition).

Communications cable in an outdoor raceway above grade needs no wet-location listing.
  The raceway interior is a wet location, but communications, optical fiber and CATV coaxial cable are exempt, and a protective raceway of 8 feet or less is not wet.
  Source: OESC/NEC 720.11 as amended by Table 1-E (2026 edition).
```

[FIGURE: structured-cabling-riser, the rack, patch panel and demarcation beside the electrical service, home runs to rooms, spare conduits to the roof, the road and an outbuilding]

## 24.5 Audio and video runs

**Simple**

Speakers and screens change every few years, and the wires to them stay in the walls for decades. Speaker wire inside a wall carries a fire listing printed on its jacket. Far from its video source, a television gets its picture over one data-grade cable with a small extender box at each end. That link is direct and does not depend on the house network. Each wall-mounted screen location gets its own conduit, so the next kind of cable can be pulled to it.

**Applied**

1. Use speaker cable listed CL2 or CL3 inside walls, and CL2P or CL3P in a plenum.
2. Size 8-ohm speaker runs by length: 16 AWG up to 80 feet, 14 AWG from 80 to 200 feet, 12 AWG beyond.
3. Use 18 AWG on a 70-volt distributed-audio system.
4. Feed any display more than 25 feet from its source through a point-to-point HDBaseT extender over Category 6A, up to 100 meters (328 feet).
5. Run a conduit with a pull string from each wall-mounted display to the equipment location.
6. Pull buried outdoor speaker cable through conduit, and mount each outdoor speaker at its maker's setback from sprinklers and direct sun.

**Professional**

In-wall speaker cable carries a Class 2 or Class 3 cable listing. In 2023 the NEC moved those listings from Article 725 to Article 722, and the 2026 edition keeps them there under a title that covers all limited-energy cables. Conductor resistance grows with length, and against an 8-ohm load a long, thin run turns a measurable share of the amplifier's power into heat in the wire. Seventy-volt systems step the voltage up at the amplifier and down at each speaker, so the current stays small and lighter wire serves long runs.

HDBaseT sends uncompressed video, audio and control over one twisted-pair cable as a point-to-point link. Networked audio-video distribution depends on multicast handling (IGMP snooping) in the switches, which ties the picture to the network's configuration. With the network down, the point-to-point link keeps the house's audio and video working.

## 24.6 Switches, dimmers and lighting control wiring

**Simple**

Smart switches sit in the wall where an ordinary switch would, so a guest works the room the usual way. Inside, each needs a neutral wire and a deeper box. At rough-in the neutral costs cents of wire. Adding one after the finishes go on means opening the wall. Smart bulbs serve colored accent lights. Any room that may get color-tuning lights needs its control wiring chosen before the walls close. Color-tuning lights come with two control systems that use different numbers of wires.

**Applied**

1. Run a neutral conductor to every switch box, including boxes that get an ordinary switch on day one.
2. Use deep boxes for smart devices: 22 cubic inches or more for a single gang, or a 4-inch square box with a mud ring.
3. Wire three-way and four-way locations with hardwired companion switches, travelers home-run, as the default.
4. Use a smart switch with wireless secondary controls only where a traveler cannot be run.
5. Buy switches and dimmers with a UL or ETL listing mark.
6. Check each lamp against the dimmer maker's compatibility list at the dimmer's control type: forward phase, reverse phase, 0-10 V or DALI.
7. Choose 0-10 V or DALI-2 for each tunable-white zone before rough-in: 0-10 V needs up to five conductors, DALI-2 two.
8. Mount switches and thermostats 15 to 48 inches above the floor, and no higher than 44 inches over a counter 20 to 25 inches deep.
9. Where DC lighting is chosen, run each 12- or 24-volt circuit as Class 2 wiring sized for its voltage drop.
10. Label each DC circuit at its source and at every box.
11. Keep a wall switch as the primary control in every room.

**Professional**

NEC 404.2(C) requires a grounded conductor at switch locations controlling lighting in bathrooms, hallways, stairways and habitable rooms. Electronic switches draw standby current through the neutral while the load is off. Two of the rule's exceptions apply only where a raceway has room for a neutral or a box can take a new cable without removing finish. Neither condition holds in a poured wall or a grouted cell. Code entries for the neutral and for box fill are in the branch-circuit chapter.

Under NEC 314.16 a device counts as two conductors of the largest size connected to it and the equipment grounds count as one. Smart switches' bodies take up the box volume a plain switch leaves free. Snap switches are listed to UL 20, solid-state dimmers to UL 1472 and energy-management controls to UL 916. Imported smart switches with no U.S. listing mark fail the certification rule in the entry below, whatever their features. Oregon's 2023 Table 1-E struck the NEC 210.70 sentence that barred a wall control relying only on a battery. Battery-powered wireless secondaries could therefore serve required lighting outlets under the 2023 OESC. No 210.70 row appears in the 2026 table, so the 2026 NEC wording governs.

LED drivers paired with a forward-phase (TRIAC) dimmer built for incandescent loads flicker, buzz, drop out or stop short of a low level. Reverse-phase (ELV), 0-10 V and DALI controls avoid that mismatch, and the maker's compatibility list confirms each driver-and-dimmer pair. Tunable-white fixtures take two control values, brightness and color temperature. On 0-10 V each value needs its own analog pair beside the switched hot. Control-voltage drop on a long run then leaves fixtures on one circuit at different colors and levels. DALI-2 addresses both values digitally on one pair with no analog drop, and the evening color schedule runs on the local controller through either interface.

Fed from the battery bank or a DC-to-DC converter, a 12- or 24-volt DC lighting circuit skips two conversions, battery to AC in the inverter and AC back to DC in each fixture's driver. It also dims natively. It falls under the Class 2 rules and needs heavier conductors than a 120-volt circuit for the same power over the same distance. Fixture choice is narrower, and the house gains a second wiring system to document for a future electrician. Reach figures in the mounting step come from ANSI A117.1. That standard does not bind a private single-family house, and holding to it keeps every control usable from a wheelchair and readable on a thermostat display.

**Code**

```
A product the code requires to be listed is a certified electrical product.
  In the OESC, "listed" or "labeled" has the meaning of a certified electrical product, one certified under ORS 479.760 and not decertified.
  Source: OESC Table 1-E, 90.4(D) amendment (2023 and 2026 editions); ORS 479.530(3).
```

## 24.7 The equipment rack, its cooling and its battery

**Simple**

One cabinet, the rack, holds the internet equipment, the network switches, the controller and the camera recorder. Its electronics run day and night and turn all their power into heat, so the rack gets vents or a fan. At the bottom, a battery unit keeps everything running through a power blink. In a long outage it signals the equipment to shut down cleanly before its battery runs flat, and the controller's stored settings come through undamaged.

**Applied**

1. Reserve rack space in conditioned space near the demarcation and the panel, with working room in front, for:
   - the internet terminal and the router or firewall
   - the network switch, the PoE switch and the patch panels
   - the controller, the camera recorder and its storage
   - the UPS and the cable management
2. Vent the rack through top panels or a fan kit. Never close it in a sealed, unconditioned closet.
3. Add up the nameplate watts of everything on the rack, and multiply by 3.41 for its heat in BTU per hour.
4. Size the UPS at 1.6 times that watt total, in volt-amperes, for at least 30 minutes at full load. Sixty minutes is the better target.
5. Plug every device in the rack into the UPS outlets, the PoE switch included.
6. Connect the UPS to the controller or recorder by USB, and run Network UPS Tools so each dependent device shuts down before the battery empties.
7. Feed the rack from a circuit on the battery-backed panel.
8. Label the UPS with its install date. Replace a sealed lead-acid battery every 3 years and a lithium iron phosphate unit every 7.
9. Leave open air space above and below the UPS.
10. Install a Type 2 surge protective device at the main panel as the first stage, with the UPS as the second.
11. Add the rack's standby watts, times 24 hours, to the daily energy list for the battery bank.

**Professional**

Every watt the rack draws ends as heat, at 3.41 BTU per hour per watt. Recorders run near 75 W, a switch near 40 W, a router near 15 W and the UPS itself near 10 W. That rack draws 140 W and gives off 480 BTU per hour. As planning figures, top venting holds a residential rack near 20°F above the room, and a fan kit cuts the rise to 5°F. Heat is the main long-term cause of failure in network equipment, which is the reason the rack sits in conditioned space.

Line-interactive UPS units are rated in volt-amperes on an assumed power factor of 0.6, which is why the volt-ampere rating is set at 1.6 times the load in watts. Network UPS Tools broadcasts the power state over the network, so storage, controller and recorder shut down in order and restart automatically when power returns.

Sealed lead-acid batteries vent hydrogen under deep discharge and charge, the reason for the open air space. Lithium iron phosphate units cost more, last 8 to 10 years against 3 to 5 for lead-acid, and tolerate heat better. Their extra cost returns within the first lead-acid replacement. Residential UPS units are listed to UL 1778, and APC, CyberPower, Eaton and Tripp Lite list their consumer and small-business lines to it.

The rack UPS is sized on its own, apart from any whole-house generator or battery. It bridges the handoff interval of every transfer to backup power, whatever the whole-house design becomes. On the critical-loads plan the network and the controller sit on the backed-up panel. Their draw runs around the clock, so their standby watts set part of the battery bank's daily floor: a 140 W rack uses 3.4 kWh a day.

Oregon did not adopt the NEC 230.67 surge-protection requirement in the 2023 OESC. Under the 2026 OESC, Table 1-E makes 230.67(A) to (C) and (E) effective October 1, 2027. That rule belongs to the electrical service chapter. Either way, a Type 2 device at the main panel protects the well pump and the electronics from rural lightning and utility surges. The UPS clamps whatever passes it.

## 24.8 The local controller, its radios and voice

**Simple**

Every scene, schedule and alert runs on the controller, a small computer in the rack. It talks to the devices over three radio systems and the wired network, and none of that traffic leaves the house. Locks, leak sensors and door sensors go on Z-Wave, the radio that reaches through concrete and has the steadiest record. Lights and ordinary sensors go on Zigbee or Matter. Voice control, if the house gets it, runs on a speaker that understands speech on its own hardware, so no recording leaves the house.

**Applied**

1. Run Home Assistant on dedicated hardware, Home Assistant Green or a small x86 computer, on a wired network port.
2. Add a Z-Wave 800-series USB radio for locks, leak sensors, door and window sensors and smoke-alarm bridges.
3. Add a Zigbee 3.0 USB radio, run through Zigbee2MQTT or ZHA, for lighting and general sensors.
4. Add a Thread border router for Matter-over-Thread devices once the border-router mesh proves stable in the house.
5. Connect appliances and other Wi-Fi devices only where the device offers Matter over Wi-Fi or a documented local interface.
6. Automate the leak shutoff and the freeze alerts first, then a goodnight scene and the away and home modes.
7. Add left-open alerts for doors and the garage, then occupancy lighting and seasonal schedules.
8. Leave cooking appliances, interior doors and window operation manual.
9. Back up the controller configuration every night to local storage and every week off-site.
10. Where voice is wanted, use a satellite that processes speech on the controller: Home Assistant Voice Preview Edition or a Willow unit.
11. Keep microphones out of bedrooms and bathrooms.
12. Tell overnight guests which rooms have a microphone.

**Professional**

Home Assistant runs Zigbee, Z-Wave and Matter natively on local hardware with no cloud dependency. Its remote access and cloud voice are opt-in, through a self-hosted VPN or the Nabu Casa subscription at $6.50 a month. Hubitat's Elevation C-8 Pro is a closed hub with built-in Z-Wave 800 and Zigbee 3.0 radios and Matter support. It states full local processing as a design goal and needs no subscription. Aqara's M3 bridges Zigbee, Thread and Matter devices as a local hub. Lutron RadioRA 3 is a closed, fully local lighting system that integrates with Home Assistant over the Lutron Integration Protocol. Where the budget allows, it serves as a lighting layer under the whole-house controller.

Matter 1.3 supports local control across Apple Home, Google Home, Amazon Alexa and Home Assistant at once. Matter 1.5 added camera, soil-sensor and energy-management device types, whose certified products are arriving slowly. Matter over Wi-Fi is reliable. Matter over Thread depends on several border routers and on a router that forwards IPv6 multicast correctly. When a border router reboots or multicast breaks, a Thread device drops out of the mesh.

Z-Wave 800-series devices with S2 security, Long Range and SmartStart are mature, and Z-Wave remains the most reliable residential mesh for locks, sensors and switches. Zigbee 3.0 devices are cheaper and serve lighting and sensors well, with a history of interoperability problems that keeps them off security roles. Cloud-dependent Wi-Fi devices crowd the access point and have the worst firmware-support record of the lot.

Damage prevention and freeze alerts come first, daily-repetition scenes second, occupancy lighting and seasonal schedules third, and novelty integrations last. Every automation's failure default leaves the house operable by hand, as the opening section states.

Cloud voice assistants send every command to a vendor's servers, which conflicts with the local-first rule and adds a standing microphone with an always-on connection. Home Assistant Voice Preview Edition runs wake-word detection, speech recognition (Whisper) and speech output (Piper) on the controller, and Willow satellites use the same on-device approach. ORS 165.540(1)(c) applies to any device that obtains a conversation. Under that statute a satellite that processes audio locally and retains no recording stands better than one that uploads audio. Its terms are stated in the camera section.

## 24.9 Network security

**Simple**

Some smart devices are badly made and never updated, and each one is a small computer on your network. Walls inside the network are the defense. Cameras sit on one segment, gadgets on another, the family's computers on a third, and a firewall decides which segment may talk to which. On its own segment, a weak camera cannot reach a laptop. Nothing inside the house is opened directly to the internet. Remote access runs through an encrypted tunnel to your phone.

**Applied**

1. Put the internet provider's gateway in bridge mode, with an owner-controlled router and firewall behind it.
2. Build at least four VLANs, named management, trusted, IoT and cameras, plus a guest network for visitors.
3. Set the firewall to default-deny between VLANs. Allow trusted to reach IoT, and block IoT from starting a connection to trusted.
4. Give the camera VLAN no internet access except time service and firmware downloads, and let only the recorder talk to the cameras.
5. Enable multicast DNS reflection across the VLANs so phones discover devices without an open firewall.
6. Forward no port from the internet to any device. Use a VPN (Tailscale or WireGuard) for remote access.
7. Run a filtering DNS resolver (AdGuard Home or Pi-hole) for the house.
8. Give every device its own password from a password manager, and change the factory passwords on the day of installation.
9. Turn on automatic security updates for the router, the switches and the access points.
10. Update cameras, the recorder and the controller by hand, after reading each release note.
11. Choose devices whose maker states the support period and signs its updates.
12. Record every device's address, firmware version and install date in the inventory.

**Professional**

Segmentation limits what a compromised device can reach. Taken over on an isolated VLAN, a smart bulb or camera affects its own segment and cannot pivot to a laptop or a phone. Prosumer routers and managed switches support VLAN tagging, and the segmentation is a one-time design made at setup rather than retrofitted. Firewall rules run one way: trusted initiates to IoT, and IoT never initiates to trusted. Phones and the controller view camera streams through the recorder's RTSP output, never by a direct connection to a camera.

For the mid-range spine, UniFi's UDM SE or UDR7 gateway with USW-Pro switches and U7 access points puts VLANs, firewall and PoE in one management console. pfSense or OPNsense on a Protectli appliance gives the most control at the firewall. The provider's router is never the house firewall.

CISA's Cross-Sector Cybersecurity Performance Goals 2.0 (December 11, 2025), NIST SP 800-213 on IoT device cybersecurity, NIST SP 800-41 Rev. 1 on firewalls and CISA's July 2025 microsegmentation guidance converge on segmentation, default-deny and microsegmentation for IoT-heavy networks.

Device selection screens against the NIST consumer-IoT baseline. NIST IR 8425, published in 2022, profiles the core baseline for consumer products. NIST IR 8425A, from September 2024, states the requirements for consumer-grade routers, and NIST IR 8259 Rev. 1 of April 2026, with the 8259A and 8259B core baselines, states the manufacturer's side. Unique credentials, signed and supported updates and a published support period are what the baseline asks for. No statute or code requires any of this for a single-family house, which is why no Code entry follows. As a project rule, no dashboard, camera or lock is reachable from the public internet, and remote access runs only through the VPN.

## 24.10 Leak, freeze, tank and equipment alarms

**Simple**

Wired to an automatic shutoff valve, a leak sensor turns a burst supply line into a mop-up instead of a gutted floor. One that only sends a message protects nothing while you are asleep or away, so the valve closes on its own. Slow failures get watched too: a cold pump house, a cistern running low in August, a failing battery bank, a stopped septic pump. Each shows up on your phone hours or days before it becomes damage.

**Applied**

1. Put a leak sensor at the water heater, under each sink, behind the washer and dishwasher, at the pressure tank and on the mechanical-room floor.
2. Install a motorized ball valve with a manual handle on the main supply, downstream of the pressure tank.
3. Program the controller to close the valve when any leak sensor trips, and to send an immediate alert.
4. Choose a valve with battery backup that holds its position on power loss.
5. Do the valve plumbing on the owner's plumbing permit, or hire a plumber, and call the inspection before covering the joint.
6. Clamp a flow sensor on the main for a running-water alert. It needs no plumbing permit.
7. Fit the cistern with a sight gauge or a float-and-cable dial as the always-working reading.
8. Add an ultrasonic or pressure sensor in the tank reporting to the controller, with a low-level alert.
9. Mount a temperature sensor at pipe level in the pump house. Alert and switch on the heat tape before the air reaches 32°F.
10. Read state of charge, fault codes and charging status from the battery inverter into the controller, and alert on any fault code.
11. Wire a dry contact from the septic high-water alarm panel into the controller as a second notification. Leave the alarm on its own circuit.
12. Place a PM2.5 monitor and a CO2 monitor in the main living zone.
13. During a smoke event, hold indoor PM2.5 at or under 10 micrograms per cubic meter, and admit outdoor air briefly when the CO2 reading climbs.
14. Send a leak, a freeze or a fault code as an immediate alert.
15. Send tank level and filter status in a daily summary, and trends in a monthly report.

**Professional**

Notification-only leak detectors protect nothing while the house is empty or asleep, so the sensor-and-valve pair is the design. Products split by where they act. Flume clamps a sensor on the meter or the pipe and reads flow without opening the plumbing. Moen Flo, Phyn Plus and Flologic put a powered valve in the main line, and a powered valve is plumbing work under permit and inspection.

ORS 693.020(1)(a) takes the owner's work on the owner's own building outside the plumbing licensing law, and ORS 447.060(1)(a) exempts work not done for hire. ORS 693.020(4) keeps the inspection requirement in force. What the valve does when power fails matters more than its app. One that closes when power fails leaves the household without water in every outage, so the specified valve holds position and carries a battery.

Tank reading comes in three tiers, and the house gets two of them. Sight gauges need no power and no electronics, and they give a reading to whoever walks to the tank. Floats on a cable, turning a dial at a convenient spot, are mechanical as well. Ultrasonic or pressure-transducer sensors reporting to the controller add a reading from indoors and an automatic low-level alert, at the cost of depending on power and the controller. Turning the reading into a budget decision takes two more numbers: a days-remaining figure, tank volume divided by daily draw, and a conservation trigger decided beforehand. Both come from the water-independence chapter.

Freeze protection in the pump house guards the one point of failure for the whole water supply. Its sensor sits at pipe level, not in the room air, and triggers the heat tape or a circulator as well as the alert. Battery telemetry exposes a failing battery, a charge-controller fault or a fast state-of-charge decline before a no-power event.

High-water alarms on a septic tank catch a failed pump, a clogged effluent filter or an overdue pump-out before effluent surfaces or backs up. OAR 340-073-0055(4)(f) requires an audible and visual high-water alarm with a manual silence switch, in or near the building the pump serves and on a circuit separate from the pump. Its switch is set so the tank still holds one-third of a day's design flow when the alarm sounds. Beside that alarm the controller's notification is a second channel, never a replacement.

Consumer PM2.5 monitors show whether the ventilation system's recirculation mode is holding smoke out, instead of assuming it. CO2 climbs over hours of occupancy with the outdoor air shut off. Its reading marks the point at which a short outdoor-air exchange is worth the smoke it admits.

## 24.11 Energy monitoring, load shifting and smart appliances

**Simple**

In the panel, an energy monitor shows what each large load draws and when it runs. Timing is where the reading matters most. Water heater, car charger, well pump and laundry can all run at midday, fed directly by the solar array. Every kilowatt-hour used in daylight is one the battery never has to store, so the battery bank can be smaller. Smart appliances in this house watch and notify. Each machine reports that a cycle is done, and a person starts the next one. No phone ever starts the oven.

**Applied**

1. Install a whole-panel energy monitor with current transformers on the main feed.
2. Add a transformer on each large circuit:
   - heat pump and air handler
   - water heater and well pump
   - range and dryer
   - EV charger and shop feeder
3. Install the monitor under the owner's electrical permit, or hire a Class B technician and a journeyman electrician for the voltage tap.
4. Or specify a smart panel with per-circuit monitoring and control as the main panel.
5. Schedule the heat-pump water heater, EV charging, the well-pump fill and the laundry into the solar window, mid-morning to mid-afternoon.
6. Use each device's own scheduler or solar mode where it has one, and the controller where it does not.
7. Alert when a circuit draws power while its load should be off, and when a cycle runs past its usual length.
8. Add a third alert for a day's total over the budget.
9. Allow remote start only where the appliance's listing covers it and a person has loaded and armed the machine.
10. Keep the oven monitor-only.
11. Automate pool, well and irrigation controllers through their Class 2 control inputs, and layer any smart water-heater control on the heater's own thermostat.
12. Write each monitor channel against its circuit in the panel schedule.

**Professional**

Current transformers clamp around one conductor each and read its current by induction, and the head unit takes its voltage reference from a two-pole breaker. Emporia Vue 3 and Sense mount the head unit inside the panel, which the maker's listing has to cover. Transformers and head unit are listed together to UL 2808, the energy-monitoring equipment standard. IotaWatt keeps the head unit in a separate enclosure with the transformer leads run through conduit, which keeps third-party equipment out of the panel.

Span and Curb are smart panels and panel-mounted controllers that monitor and switch each circuit. In the electrical service chapter the smart panel is weighed as the energy-management system that lets a 200-ampere service carry two car chargers. Under the owner exemption the owner installs the transformers. Paid installers need the Class B limited-energy scope for the transformer and data side and a general journeyman electrician for the line-voltage tap.

Load shifting is the cheapest capacity on the system. Every kilowatt-hour shifted into the array's producing hours, mid-morning to mid-afternoon on a clear day, skips the battery. Otherwise the house buys storage to hold that kilowatt-hour until night, at a hardware cost for every kilowatt-hour of capacity. Heat-pump water heaters, EV chargers and well-pump controllers commonly include a schedule or a solar-following mode, so the shift costs a setting. How much battery and array the shift avoids depends on the load list and the array size. Battery sizing then takes the shifted loads out of the overnight total.

UL 858 governs household electric ranges, and its Section 47A, added in the 2015 edition, covers smart-enabled appliances. Remote start is permitted only in a mode the listing covers, which calls for a local enable at the appliance before a remote command is accepted. So a cold oven does not start from a phone. UL 749 for dishwashers, UL 2157 for washers and dryers and UL 1083 for countertop cooking carry the same family of limits. These are product standards, not building code.

Building code reaches them through the installation rule in the entry below, so a feature the listing excludes is a listing violation rather than a permit item. Pool, well and irrigation controllers are Class 2 control circuits with no such limits, and the actuated pump or valve carries its own listing. Smart water-heater controls (Aquanta, Rheem EcoNet) layer on a heater whose own listing holds its thermal protection.

**Code**

```
Power monitoring equipment may occupy a panelboard's wiring space when its listing allows it.
  The equipment is identified as a field-installable accessory of the listed enclosure or is a listed kit evaluated for field installation, and the wiring-space fill limit holds.
  Source: OESC/NEC 312.8(B) (2023 edition).

Listed equipment follows its listing and instructions.
  Listed or labeled equipment is installed and used in accordance with the instructions included in the listing or labeling.
  Source: OESC/NEC 110.3(B) (2023 edition).
```

## 24.12 Monitoring for aging in place

**Simple**

Fall detection, a morning check-in and voice-called help are decisions about how you want to live in the house. Those decisions belong to the interiors plan. Hardware for any of them passes three tests. It must work with the internet down and through a power outage, and it must keep cameras out of rooms where people undress. Wearable fall sensors record a jolt and nothing else. Cameras record the room.

**Applied**

1. Start from the livability plan's feature list, whether it names fall detection, a daily check-in, emergency calling, or none of them.
2. Reject any product whose detection logic runs only on the maker's servers.
3. Choose a wearable accelerometer, a pendant or a wristband, over a camera for fall detection in bedrooms and bathrooms.
4. Route an emergency call over a path that survives an internet outage, such as a cellular gateway on the rack battery.
5. Put the sensor hub and the calling path on the rack battery unit.
6. Write down who is called first, who second, and what happens when no one answers.
7. Test the whole chain with the occupant once a month, and log the test.
8. Tell the occupant and every visitor where each sensor is.

**Professional**

Deciding which features the house gets belongs with the reach ranges, the bathroom layout and the other aging-in-place choices in the interiors chapter. Implementing them belongs here, because a product's privacy posture, its outage behavior and its fit in the local-first architecture are network and hardware questions.

Camera-based fall detection analyzes video continuously in the rooms where falls happen. Those are the rooms the camera section keeps cameras out of, and the rooms ORS 163.700 names as private. Wearable accelerometers report acceleration and nothing about the room, so their privacy cost is the device on the wrist. Any system that depends on the internet or the grid fails in the storm that raises the fall risk. For a frail or medically vulnerable occupant, that failure is the most consequential one in the house. Local processing, a battery-backed hub and an outage-proof calling path are therefore conditions of purchase.

## 24.13 Cameras and Oregon's recording law

**Simple**

Video is mostly legal, and audio is the constraint. Oregon law bans recording an in-person conversation unless every participant is specifically told it is being recorded. Porch cameras with the microphone on record visitors talking to each other, which can break that law. So the cameras here run with audio off, record to the recorder in the rack, and stay pointed at your own property. At the driveway gate, a camera sends its pictures over the cellular network and stores them on its own card.

**Applied**

1. Disable audio on every exterior and shared-space camera.
2. Where the doorbell needs two-way talk, use a unit that announces it is recording, and post a sign readable before the camera's view.
3. Place no camera in a bathroom or a bedroom.
4. Set detection zones and privacy masks so alerts fire only on your property and no neighbor's window or fenced yard is recorded.
5. Photograph the mask settings for the binder.
6. Record to the recorder in the rack. Keep 14 to 30 days of full recording and 90 days of motion events.
7. Size the recorder at 65 to 85 GB per camera per day plus 50 percent, on mirrored drives, with RAID 6 above six cameras.
8. Specify 4K cameras with a 1080p sub-stream, 15 to 20 frames per second, H.265 encoding and IP66 or IP67 housings outdoors.
9. Turn on person, vehicle and package detection and leave plain motion alerts off.
10. Budget PoE at 802.3at for a fixed camera and 802.3bt Type 3 for a pan-tilt camera with a heater or continuous infrared.
11. Run Category 6A to every camera.
12. For the driveway entrance beyond cable reach, choose a solar cellular camera that records to its own card or to the recorder.
13. Treat cloud storage on it as optional, and budget $10 to $25 a month for its data plan.
14. Before buying it, check the cellular signal at the gate with a phone and the winter sun on the panel location.
15. Strip the audio from any clip before sharing it publicly.

**Professional**

ORS 165.540 regulates obtaining oral communications, not silent video. Exterior, driveway and approach cameras, and the owner's own interior living-area cameras, are lawful where no one has a reasonable expectation of privacy. Audio is the constraint. On January 7, 2025, the en banc Ninth Circuit upheld the all-party-notice rule against a First Amendment challenge in Project Veritas v. Schmidt (125 F.4th 929). The subscriber-in-home exception is why interior living-area cameras may carry audio among the family, and announced recording stays the practice wherever visitors are the other participants.

Sharing a clip whose audio carries a third party's conversation is a use-or-divulge exposure under ORS 165.540(1)(e). That is why the audio comes off before a clip leaves the house. No Oregon statute sets a retention period for residential footage, and handing footage to police is voluntary.

Deliberate surveillance of a neighbor falls under a different statute. Under the stalking law, monitoring another person's activities by electronic means without consent counts as contact. Two or more unwanted contacts that would alarm a reasonable person make the crime. Detection zones and privacy masks keep both the alerts and the recording on the owner's parcel. Photographed mask settings are the record that the camera was configured that way.

Camera resolution, encoding and PoE class change with each product cycle, and the values in the steps are 2026 planning figures. In H.265 at 15 frames per second, a 4K main stream runs 6 to 8 Mbps, which fills 65 to 85 GB per camera per day. Object detection for people, vehicles and packages is standard on Reolink, Ubiquiti, Hikvision and Axis cameras, and it removes most false alerts from wind, rain and animals. Local recording, object filtering and Category 6A to every camera for bandwidth and power headroom are the durable defaults.

Solar-powered cellular cameras are a mature category built for a gate too far from the house for cable or Wi-Fi. Reolink sells units that record to a microSD card, a Reolink Home Hub or an NVR, with cloud storage as an option. On those units the cellular link carries alerts and remote viewing, and the footage lives in the house. That gate camera is the one deliberate exception to the all-local network. Driveway length, terrain and tree cover set the cellular signal at the gate and the panel's winter charge, and neither is known until measured on the site.

**Code**

```
Recording an in-person conversation requires that every participant be specifically informed.
  Obtaining any part of a conversation by any device without that notice is a Class A misdemeanor, and a conversation includes a video-conference communication.
  Source: ORS 165.540(1)(c), (9); ORS 165.535(1) (2025 edition).

Two exceptions reach the household and open recording.
  Subscribers and members of their family acting in their homes, and an unconcealed device at a private meeting where the others knew or reasonably should have known.
  Source: ORS 165.540(3), (6)(a)(C) (2025 edition).

Recording a person's intimate area or nudity without consent is a crime where privacy is expected.
  An intimate area is a Class A misdemeanor and a state of nudity a Class C felony; bathrooms, dressing rooms and any enclosed space where a person undresses count.
  Source: ORS 163.700(1)(b), (2)(d), (3); ORS 163.701(1)(a), (2)(a) (2025 edition).

Electronic monitoring of another person without consent is stalking contact.
  Using an electronic device to obtain or monitor another person's activities without consent is contact, and repeated unwanted contact that reasonably alarms is a Class A misdemeanor.
  Source: ORS 163.730(3)(o), (9); ORS 163.732(1), (2)(a) (2025 edition).
```

## 24.14 Locks, garage doors and gates

**Simple**

No lock in this house needs a phone, a code or a battery to get out. Inside every exit door is a plain thumbturn that opens with one motion, and the code requires it. Smart features ride on top: guest codes, a lock-status light on the dashboard, an alert when a door stays open. When the electronics fail, the door still opens from inside, and a metal key still works outside. From a phone, the garage door closes only through an opener that beeps and flashes first.

**Applied**

1. Use a smart deadbolt with an interior thumbturn that opens in one mechanical motion.
2. Reject any lock that needs a phone or a code to exit.
3. Specify a mechanical key override and external power contacts, so a 9-volt battery held to the contacts wakes a dead lock.
4. Choose a Grade 1 rating under the BHMA hardware grades where the product line offers it.
5. Track battery state in the controller. Expect 6 to 12 months on alkaline AA cells in a mid-range deadbolt.
6. Buy a garage-door opener listed to UL 325.
7. Close it remotely only through the maker's own interface or a controller input the maker lists for it.
8. Never relay-bridge a non-compliant opener to the controller for remote closing.
9. Make any electronic lock on an egress door release when its power fails.
10. Reserve fail-secure hardware for a server closet or a storeroom.
11. On a vehicle gate, use an operator listed to UL 325 with monitored photo eyes or edge sensors.
12. Build the gate itself to ASTM F2200.
13. Log every code issued and revoked.

**Professional**

Egress rules exist for the person leaving in smoke or in the dark, and an interior thumbturn satisfies the rule while a code-only or phone-only exit violates it. That rule also decides the power-loss behavior of any electronic lock on an egress path. If a door stays locked from inside when the batteries die, it cannot be opened without special knowledge, so the hardware fails safe. Fail-secure hardware, which stays locked on power loss, belongs only where no one needs to get out. Smart deadbolts from Yale, Schlage, Kwikset and Level carry the key override and the external contacts, and the controller's battery warning arrives weeks before a lock goes dark.

UL 325 is the safety standard for garage-door, gate and window operators, and 16 CFR part 1211 makes its residential garage-door provisions federal law. Unattended operation means closing the door with no one in line of sight, which is what every remote-close automation does. Which doors may close unattended, and the warning and suspension sequence they need, are in the entry below. Relaying the controller across a plain opener's wall-button terminals bypasses that sequence. Remote closing therefore goes through a compliant smart opener, which Chamberlain, LiftMaster and Genie sell. Or it goes through a controller input the opener's maker lists for third-party use, such as a Konnected garage module.

For vehicle gates, UL 325 requires monitored entrapment-protection sensors on a residential Class I operator, and ASTM F2200 governs the gate itself: its gaps, rollers and guards. Both standards are read from the manufacturer's listing documents rather than from the code.

**Code**

```
The required egress door opens from inside without a key or special knowledge.
  The egress door is readily openable from inside the dwelling without the use of a key or special knowledge or effort.
  Source: ORSC R311.2 (2023 edition).

A garage door may close unattended only with the federal warning sequence.
  Unattended closing is barred on one-piece and swinging doors and otherwise requires a 5-second audible and flashing visual alarm before motion and suspension after two obstructed attempts.
  Source: 16 CFR 1211.14; UL 325.
```

## 24.15 Alarm systems and monitoring services

**Simple**

Watching your own cameras and deciding whether to call the police is unregulated. Paying a company to watch and call is a licensed service. Cities and counties fine repeat false alarms, and most require the system to be registered. Here the alarm verifies before anyone asks for a patrol car. First a camera shows a person, then the siren runs for a minute, and then a person decides whether to call.

**Applied**

1. Decide between self-monitoring and a monitoring company before buying the panel.
2. Register the alarm with the site's city or county when it is installed. Portland's deadline is 30 days, and Washington County registers unmonitored sirens too.
3. Program a siren-only interval of 60 seconds, with a person's decision before any dispatch request.
4. Escalate an alert only after a camera shows a person in the zone.
5. With a monitoring company, write its DPSST entity license and enhanced call verification into the contract: two listed contacts called before any dispatch request.
6. Put the alarm panel and its communicator on the rack battery, with a cellular path for the signal.
7. For a fire alarm control unit, hire a Class A technician and design the system to NFPA 72.
8. Feed that unit from a dedicated red-marked circuit with no GFCI or AFCI.
9. Test the alarm at an off-peak hour each quarter, covering the siren interval, the notifications and, with a company, its call sequence.

**Professional**

Watching a house for pay and reporting unlawful activity is a private security service under ORS 181A.840(9). Under ORS 181A.840(6) the company doing it is a private security entity, licensed by the Department of Public Safety Standards and Training under ORS 181A.870 with liability insurance and a licensed executive manager. Entities that only monitor alarms are excused from the use-of-force and citizen-arrest policies other entities file, which shows the license was written with monitoring companies in mind. Under the entry below a homeowner watching the household's own cameras needs no license, and neither does the installer wiring an intrusion alarm while doing that work.

Each city or county writes its own alarm registration and false-alarm rules. Under Portland City Code 14B.10, Portland requires a permit within 30 days of installation, at $25 for a residence and $125 for a business. Failing to register costs $100. Beaverton charges $30, forgives the first false alarm each year and fines the second through the twelfth $50 to $300. Washington County charges $20 the first year, requires registration even for an unmonitored siren and revokes the permit after excessive false alarms. Most ordinances also require enhanced call verification before dispatch. Once the parcel is known, its own ordinance replaces these examples.

Fire alarm systems with a control unit are protective signaling under ORS 479.905(5), Class A work designed to NFPA 72. Oregon's Table 1-E adds the dedicated, red-identified branch circuit in the entry below, with no ground-fault or arc-fault device in its supply. Interconnected smoke alarms under the residential code are not a fire alarm system, and their wiring and AFCI treatment are in the branch-circuit chapter.

**Code**

```
Protecting your own property is outside the private security law.
  The private security licensing law does not apply to a person while protecting the person's property, or to a person monitoring alarm systems not designed to detect threats to public safety or personal well-being.
  Source: ORS 181A.845(1)(g), (h) (2025 edition).

A paid monitoring company is a private security entity.
  A person who for pay supplies or employs providers to observe and report unlawful activity or to protect property for another is a private security entity.
  Source: ORS 181A.840(6)(a), (9)(a), (9)(c) (2025 edition).

A fire alarm control unit takes a dedicated, marked circuit without GFCI or AFCI.
  The branch circuit supplies no other load, its disconnect is red and marked "FIRE ALARM CIRCUIT" and accessible only to qualified personnel, and it is not supplied through a GFCI or an AFCI.
  Source: OESC Table 1-E, 760.41(B) (2023 and 2026 editions).
```

## 24.16 Earthquake warning and emergency radio

**Simple**

Seconds of warning before an earthquake let a machine close a gas valve and release the door locks. That warning system already covers Oregon. Phones get the warning today. Connections into a home controller are sold to businesses, so the house keeps the wiring ready for one. When the cell towers and the internet are both down, an amateur radio reaches the county's emergency repeater. With a second license it reaches family across the country. Each license is a written test, and the range depends on the hills between the antenna and the repeater.

**Applied**

1. Where the house has LP gas, keep the mechanical seismic shutoff valve as the primary protection, whatever electronic warning arrives later.
2. Before buying the automation hardware, read the ShakeAlert licensed-operator list for a product that delivers alerts to a local controller.
3. If one exists, wire its contact or local message to close the gas valve and release the exterior locks.
4. Have the same signal turn on the lights and sound an announcement.
5. Until then, treat the phone's wireless emergency alert as the warning.
6. Pass the Technician class examination for the VHF and UHF repeater bands. Add the General class for long-distance HF.
7. Buy a VHF and UHF base transceiver and a handheld. Add an HF transceiver with the General license.
8. Ask the county emergency management office or the local radio club for the nearest ARES-affiliated repeater.
9. Check the line of sight to it from the antenna location.
10. Run the antenna feed through the roof conduit. Ground the mast and fit a lead-in discharge unit bonded to the house grounding electrode system.
11. Power the base radio from the rack battery or its own battery.

**Professional**

ShakeAlert is the USGS earthquake early warning system for California, Oregon and Washington, serving over 50 million residents. It delivers alerts to people and to automated systems seconds before strong shaking reaches a location. Automated action on its messages runs through a Technical Partner or Pilot Partner agreement with the USGS, an organizational relationship, or through a product from a USGS Licensed Operator. On the University of Oregon's operator list are a business-to-business on-site device (Early Warning Labs' Cloud Quake) and operating-system phone alerts. Latency and false-alarm rate belong to the delivery product, not to the underlying system, and both are evaluated against whichever product is considered at purchase.

Transit systems already slow trains on the warning, and elevators return to the nearest floor. In a house the equivalents are the gas valve, the exterior locks and the lights. A mechanical ball-and-pedestal gas valve, specified in the HVAC chapter, needs no warning and keeps working when every electronic path fails.

Technician class, where most operators start, grants full privileges on the 2-meter band (144 to 148 MHz) and the 70-centimeter band (420 to 450 MHz). Local emergency-services and community repeaters use those bands. General class adds the HF bands at up to 1,500 watts PEP, against a Technician's 200-watt HF limit. HF is what reaches across a region or a country with no repeater in between. Licensing comes from the FCC under 47 CFR part 97.

VHF and UHF range depends on line of sight. Repeaters on a hill or a tower extend coverage by seeing more receivers, and linked repeater networks reach hundreds of miles. In a valley, with terrain between the house and the repeater, the same equipment gets a shorter range than on an elevated site. A base station's receive log is lawful to keep, under the entry below. NEC Article 810 governs the antenna mast's grounding and the lead-in's discharge unit, bonded to the one grounding electrode system the whole house shares.

**Code**

```
Amateur and citizens band transmissions are outside the recording law.
  The prohibitions on obtaining, divulging or using a communication do not apply to a radio communication transmitted by a station operating on an authorized amateur or citizens band frequency.
  Source: ORS 165.540(7)(a) (2025 edition).
```

## 24.17 Commissioning, records and upkeep

**Simple**

Unplugging things is the test. With the internet line pulled, the lights, locks, heat and cameras keep working. With the main breaker open, the rack runs on its battery, shuts itself down cleanly and comes back on its own. Whatever fails either test gets fixed or gets written down as a convenience feature. Devices get replaced every five to ten years, and the cables and the rack stay for the life of the house.

**Applied**

1. With the internet up, run every scene from the dashboard, from a wall switch and, where fitted, by voice.
2. Confirm each camera records a motion event and each lock answers, then take a backup.
3. Pull the wide-area cable for four hours. Confirm scenes, sensors, locks, camera recording, motion alerts, the local dashboard and local voice all work.
4. Log any feature that fails the four-hour test as cloud-dependent in the as-built record.
5. Open the main breaker for 30 minutes. Confirm the rack stays up and the PoE cameras keep recording.
6. Confirm the controller and recorder shut down on the battery signal, then restore power and confirm everything returns with no manual step.
7. Disable the controller's cloud add-ons and confirm every automation still runs.
8. Disable Wi-Fi and confirm the wired devices still work.
9. Disable the Z-Wave radio and confirm each critical automation has a wired or Zigbee fallback, or record it as Z-Wave-dependent.
10. Review every camera at night for zones and masks on the property, audio off or announced, and infrared or floodlights triggering.
11. Review every lock for a working key, external contacts and thumbturn, the auto-lock timeout set, and the code log current.
12. Wet a leak sensor and watch the valve close.
13. Run the alarm test from the alarm section.
14. Restore the controller backup onto a spare or test instance and confirm it comes up.
15. Request the low-voltage final inspection in writing. Correct any defect and request reinspection within 20 days.
16. File the network diagram, the wiring diagram, the controller configuration, the device inventory, the maintenance schedule and the inspection record.
17. Reserve $500 to $2,000 a year for device replacement and updates, with the cabling and the rack outside the reserve.
18. Each year, repeat the internet-out and power-out tests, replace batteries on schedule, test the restore, and retire any device whose maker has ended support.
19. Each quarter, apply pending updates, review the accounts and read the logs.

**Professional**

Commissioning proves that the manual fallbacks work and that the house runs with the internet and the grid cut. It also proves that cameras, sensors, alarms and locks behave and that a backup restores to a working instance. Four hours without the internet is long enough for cloud-dependent features to time out and show themselves.

In the testing-and-commissioning chapter these tests are one track of the whole-house program, and the documentation chapter sets the backup rule and the replacement planning bands. Devices are consumables on a 5-to-10-year cycle against a cabling layer of 20 years or more, so the reserve funds devices and never rewiring. The inspector's response times and the owner's correction window are set by rule, in the entries below. The recurring items in the last two steps make up the maintenance calendar, and the schedule in the binder states each one's interval and the date it was last done.

**Code**

```
An electrical inspection follows a written request within fixed times.
  Within 48 hours excluding weekends and holidays, or within 7 calendar days at a remote location more than 60 miles or one hour's drive from the inspector's office.
  Source: OAR 918-271-0020(1), (2).

Defects are corrected and reinspection requested within 20 days.
  Defects the electrical inspector notes are corrected and an inspection request made within 20 calendar days of actual notice, with an extension on request.
  Source: OAR 918-271-0030(1), (2).

An owner's installation gets its results by posting at the site, and covered work waits.
  Posting at the job site is the notice of results for an owner installation, and covered work waits for clearance or the lapse of the inspection time after a written request.
  Source: OAR 918-271-0020(3)(a), (4).
```

## Who decides what

| Decision | Who decides | When, or what triggers it |
|---|---|---|
| Whether the data cabling goes on the low-voltage permit, and which inspections apply | The site's electrical inspector, in writing | After the parcel is chosen, before design |
| The OESC edition the permit is filed under | Jon, at the building department | At permit application, under OAR 918-305-0020 |
| The controller platform | Jon | Before device purchases |
| Voice control, and the rooms that get a microphone | Jon | Before device purchases |
| Drop count, camera and access-point locations | Jon, from the final floor plan | Before rough-in |
| The control system for each tunable-white zone (0-10 V or DALI-2) | Jon, with the lighting plan | Before electrical rough-in |
| DC lighting circuits | Jon, with the solar design | Before electrical rough-in |
| Multi-way switching method per location | Jon | At the electrical plan |
| Leak-valve plumbing by owner or plumber | Jon | At the plumbing permit |
| The cistern's days-remaining figure and conservation trigger | The water-independence plan | Before the first dry season |
| Self-monitoring or a monitoring company | Jon | Before the alarm panel is bought |
| Alarm registration, fee and false-alarm rules | The site's city or county ordinance | On installation |
| Which aging-in-place features the house gets | The interiors plan | At the interiors design |
| Fall-detection hardware for any feature chosen | Jon, by the three tests in the aging-in-place section | When the feature is chosen |
| ShakeAlert integration | Jon, from the licensed-operator list | When the automation hardware is bought |
| Nearest repeater, line of sight and antenna height | County emergency management or the local radio club, then Jon | Before the antenna is set |
| Driveway camera carrier and panel location | Jon, from a signal and sun check at the gate | Before purchase, on the site |
| A fire alarm control unit (none by default) | Jon, with a Class A technician | If a monitored fire system is chosen |
| Fail-secure hardware locations and lock grade | Jon | At the door hardware schedule |
| UPS chemistry and runtime | Jon, from the rack's measured wattage | At equipment selection |

## Open items

- **Permit status of the structured cabling.** Unknown: whether Ethernet and PoE cabling is a telecommunications system under ORS 479.540(9)(f), and whether that paragraph's provider clause limits the one- and two-family item as well as the multifamily item. Answered by: the site's electrical inspector in writing, or a Building Codes Division interpretation. Assumed meanwhile: the owner's electrical permit covers the cabling.
- **2026 NEC section numbers for the cabling rules.** Unknown: which sections of Articles 720 to 723, 742 and 750 replaced 2023 NEC 800.179, 800.133, 800.26, 800.100, 725.136 and 725.144. Answered by: the 2026 NEC text through NFPA's free browser access or the 2026 OESC handbook. Assumed meanwhile: the 2023 numbers, with the 2026 Table 1-E amendments as read.
- **Battery-only wall controls under the 2026 NEC.** Unknown: whether the 2026 NEC 210.70 keeps the sentence Oregon struck from the 2023 edition, since the 2026 Table 1-E has no 210.70 row. Answered by: 2026 NEC 210.70. Assumed meanwhile: a wireless secondary control is used only beside a hardwired switch.
- **NEC 312.8(B) fill condition.** Unknown: the exact wording of the wiring-space fill limit for monitoring equipment in the 2023 and 2026 editions. Answered by: the NEC text. Assumed meanwhile: the monitor's listing covers field installation in the panel.
- **Appliance remote-start listings.** Unknown: the exact conditions in UL 858 Section 47A, UL 749, UL 2157 and UL 1083. Answered by: the standards, or each appliance's installation manual at purchase. Assumed meanwhile: monitor-and-notify, with a local enable before any remote start.
- **Gate operator and gate standards.** Unknown: the monitored entrapment-protection wording in UL 325 for a Class I residential gate operator and the ASTM F2200 construction rules. Answered by: the operator's listing documents and the standards. Assumed meanwhile: monitored photo eyes or edge sensors on an operator listed to UL 325.
- **The site's alarm ordinance.** Unknown: the registration deadline, fee and false-alarm schedule where the parcel is. Answered by: the city or county ordinance after the parcel is chosen. Assumed meanwhile: registration on installation and a design that avoids a first-alarm dispatch.
- **Limited energy contractor supervision.** Unknown: whether a limited energy contractor needs a signing supervisor, as the Revision 7 text stated. Answered by: the contractor license rules in OAR chapter 918, division 282. Assumed meanwhile: the technician classes as ORS 479.905 states them.
- **ShakeAlert delivery to a home controller.** Unknown: whether a licensed operator sells a product that delivers alerts to a local controller, and its latency and false-alarm rate. Answered by: the licensed-operator list when the automation hardware is bought. Assumed meanwhile: phone alerts and the mechanical gas valve.
- **Amateur radio range from the site.** Unknown: the line of sight to the nearest ARES-affiliated repeater. Answered by: the county emergency management office or a radio club member on the site. Assumed meanwhile: a Technician license with a VHF and UHF base station and a handheld.
- **Amateur licensing rule text.** Unknown: the current 47 CFR part 97 text for the class privileges. Answered by: the eCFR in a browser. Assumed meanwhile: the privileges as stated.
- **Driveway camera signal and winter charge.** Unknown: the cellular signal at the gate and the winter sun on the panel location. Answered by: a phone signal check and a sun check on the site. Assumed meanwhile: a local-storage solar cellular unit with a $10 to $25 monthly plan.
- **Reach-range check.** Unknown: whether the drawn switch, thermostat and outlet heights fall within 15 to 48 inches, and 44 inches over a 20-to-25-inch obstruction. Answered by: a room-by-room review of the electrical rough-in plan. Assumed meanwhile: mounting within those ranges.
- **Drop count and locations.** Unknown: the number and location of data drops, cameras and access points. Answered by: the final floor plan. Assumed meanwhile: Category 6A to every candidate location, with spare conduit.
- **Freeze-alert margin and CO2 threshold.** Unknown: how far above 32°F the pump-house alert fires, and the CO2 level that calls for an air exchange in smoke mode. Answered by: the water-supply design and the ventilation commissioning. Assumed meanwhile: an alert before 32°F, and an air exchange when CO2 climbs.
- **Rack wattage.** Unknown: the rack's actual draw. Answered by: the nameplate sum at equipment selection, then a clamp-meter reading. Assumed meanwhile: 140 W.
- **Refresh reserve.** Unknown: the source of the $500 to $2,000 yearly figure, carried from Revision 7. Answered by: the component sinking fund once the devices are chosen. Assumed meanwhile: the figure as a planning band.
- **Certiorari in Project Veritas v. Schmidt.** Unknown: confirmation of the reported October 6, 2025 denial in docket 24-1061. Answered by: the Supreme Court docket. Assumed meanwhile: the en banc ruling stands.
- **DPSST licensing detail.** Unknown: the current text of ORS 181A.870 and the OAR chapter 259 monitoring rules. Answered by: the Department of Public Safety Standards and Training. Assumed meanwhile: a monitoring company holds an entity license.
- **Dropped from Revision 7.** The six-item "separate the work into layers" list, replaced by the manual-fallback table. Code entries that pointed at bodies of law or at guidance: the Articles 722, 725 and 800 group entry, the life-safety independence entry (now a Professional sentence), the division 271 licensing entry (replaced by ORS 479.905), the Article 725 and Articles 722 and 800 audio-video entries, the UL 1778 entry, the UL 20, UL 1472 and UL 916 entry, the NEC 404.2(C) and 314.16 entries (owned by the branch-circuit chapter), the NEC 230.67 entry (not an Oregon requirement before October 1, 2027), the ORS 166.065 entry (the statute does not reach cameras, replaced by the stalking statute), the local-ordinance entry, the NFPA 72 entry, the UL 858 and UL 2808 entries, the trades-split entry, the records entry, and the controller and microphone entries that duplicated the opening section and the camera section. Four statements corrected from the statutes: the plumber-only shutoff valve, the one-BTU-per-watt rack heat, the felony grade of ORS 163.700, and OAR 918-271-0030 as a permit exemption.

## Decisions this chapter records

- (decided) Every automated function keeps a manual control that works with the controller off.
- (decided) Core automation runs on a local controller in the house, with cloud features opt-in.
- (decided) Category 6A CMR cable home-run to one rack, with spare conduit to the roof, the road and the outbuildings.
- (decided) A neutral conductor at every switch box.
- (decided) Cameras record locally with audio off, none in bathrooms or bedrooms, zones and masks on the owner's parcel.
- (decided) A leak sensor and automatic shutoff valve pair, the valve holding position on power loss.
- (decided) Smart appliances monitor and notify, with the oven monitor-only.
- (decided) The rack on a UPS sized apart from the whole-house backup.
- (decided) No service exposed to the internet, remote access by VPN, at least four VLANs with a default-deny firewall.
- (decided) Every exit door opens from inside by a single mechanical motion, and electronic locks on egress doors fail safe.
- (Jon to confirm) Home Assistant on dedicated hardware as the controller.
- (Jon to confirm) Z-Wave for locks and security sensors, Zigbee and Matter for lighting and general sensors, Thread after it proves out on the site.
- (Jon to confirm) Local voice satellites if voice at all, with no microphone in a bedroom or bathroom.
- (Jon to confirm) Hardwired companion switches for multi-way control.
- (Jon to confirm) A lithium iron phosphate UPS.
- (Jon to confirm) Self-monitoring with video verification and a 60-second siren interval, with no monitoring company.
- (Jon to confirm) The owner installs the leak valve under the plumbing permit.
- (Jon to confirm) A wearable sensor rather than a camera for any fall detection the interiors plan calls for.
- (Jon to confirm) A Technician class license, a VHF and UHF base station and a handheld.
- (Jon to confirm) A solar cellular camera at the driveway gate as the one cellular device.
- (pending parcel) The permit treatment of the data cabling, the alarm ordinance, the serving repeater and the gate camera's carrier.
- (pending parcel) The 0-10 V or DALI-2 choice per tunable-white zone, and any DC lighting circuits, with the lighting and solar designs.

## Records to keep

- The owner's electrical permit, the inspector's written answer on the data cabling, and each inspection result.
- The network diagram: VLANs, switches, access points, firewall rules.
- The wiring diagram with every cable labeled at both ends, and the photographs of each wall before it closed.
- The conduit map, with each capped end's stake or GPS point.
- The mesh map and the room-by-room signal readings after fit-out.
- The controller configuration in version control, the nightly and weekly backups, and the dated restore tests.
- The device inventory: model, MAC address, network address, firmware version, install date, location, support end date.
- Pairing codes and credentials in the password manager, with the account list.
- Camera zone and mask screenshots, and the retention setting.
- The lock code log, issued and revoked.
- The UPS install date, battery replacements and the measured rack wattage.
- The commissioning log: internet-out, power-out, local-control, leak-chain, alarm and restore tests, each dated.
- The alarm registration and any monitoring contract.
- The amateur license and the repeater list.
- The maintenance schedule with each item's interval and last date.
