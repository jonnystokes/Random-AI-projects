# Chapter 15: Smart Home, Network, Security, And Local Automation

This chapter specifies the digital layer: the structured cabling and network, the local automation controller, smart switches, security cameras, access control and locks, alarm systems, energy and water monitoring, audio and video, network security, backup power for the rack, and commissioning. It is built on a local-first rule: the house keeps working when the internet is down, a subscription ends, or a vendor disappears.

The wiring methods, device listings, separations, and recording-law constraints that govern this work in Oregon are independent of whether a device connects to the internet. The electrical code of record is the 2023 Oregon Electrical Specialty Code (OESC), the 2023 NEC with Oregon amendments in Table 1-E; the 2023 NEC reorganized low-voltage cabling into Article 722 (cable requirements), Article 725 (Class 2 and Class 3 circuits), and Article 800 (communications). Product models and protocols change every cycle, so this chapter fixes the infrastructure, the code, and the architecture, and treats specific devices as replaceable examples.

## 15.1 Scope And The Local-First Principle

The permanent value of the smart home is the cabling, rack space, power, labels, and network architecture, not the devices. Core functions run locally so ordinary use never depends on a cloud service, and life-safety systems keep their required behavior independent of the automation platform.

**Simple**

A smart home should make the house easier to live in without making it fragile. Lights still turn on from the wall switch, and doors still open from the inside. Heat still works and cameras still record, whether or not the internet is up. The internet adds remote access, updates, and notifications. Basic functions never depend on it.

**Applied**

Separate the work into layers and plan the durable parts first:

- Network: structured cabling and switching that moves data through the house.
- Power: backup power for the rack, switches, controller, and cameras.
- Automation: a local controller that runs scenes and connects devices.
- Security: cameras, locks, sensors, and alerts.
- Monitoring: energy, water, comfort, and equipment status.
- Manual fallback: a physical control for every important function.

Plan the rack and low-voltage pathways before finishes close the walls, and label both ends of every cable.

**Professional**

Local-first design protects reliability, privacy, ownership, and maintainability. Core automations run on a local controller, cloud features are opt-in, cameras record to local storage, and every critical action has a physical fallback. A long-service concrete house does not depend on a short-life cloud product for ordinary use. Code-required and life-safety functions (smoke and carbon monoxide alarms, egress doors, mechanical safety controls, electrical protection, and required disconnects) keep their required behavior independent of the smart-home platform; automation may add notification and logging but does not replace a required safety system.

**Code**

```
Low-voltage, communications, and control wiring follow the electrical code.
  2023 OESC (2023 NEC with Oregon Table 1-E): Article 722 (cable requirements), Article 725 (Class 2 and Class 3 circuits), Article 800 (communications).
  Source: OESC/NEC Articles 722, 725, 800 (2023 edition).

Life-safety functions operate independently of the automation platform.
  Smoke and CO alarms per R314/R315; egress operation per R311.2; required electrical protection per the OESC; automation adds notification only.
  Source: ORSC R314, R315, R311.2 (2023 edition).
```

## 15.2 The Legal And Permit Layer

An owner-builder may install low-voltage and communications wiring on their own primary residence under the same intent-based exemption that covers line-voltage work, but the work still complies with the electrical code and is permitted except where a specific exemption applies. Paid low-voltage work for others requires a limited-energy license.

**Simple**

You may wire your own home's network and security cables under the same owner exemption that covers the rest of your electrical work. The exemption skips the license, not the code or the permit. Doing the same work for pay on someone else's house requires a state limited-energy license.

**Applied**

- Perform the owner's own low-voltage work under the homeowner exemption on the primary residence, to code.
- Pull a low-voltage permit for new installations except where a specific exemption applies (such as Class 2 wiring on the load side of a listed Class 2 transformer, or listed intercom and CCTV work in a one- or two-family dwelling under the stated conditions).
- Confirm the local jurisdiction's low-voltage permit posture before final design; enforcement varies by county and city.
- Use a licensed Limited Energy contractor for any paid low-voltage work on a third party's home.

**Professional**

ORS 479.540(1) exempts an owner from electrical licensing for work on a residence the owner occupies and does not intend to sell or lease, and it applies to Class 2, Class 3, and communications work as it does to line-voltage. The exemption is from licensing, not from the code: ORS 479.540(1)(a) requires the work to comply with ORS Chapter 455 and the OESC. A permit is required for new low-voltage installations except where specifically exempted (OAR 918-261-0039 for load-side Class 2 wiring, OAR 918-271-0030 for certain listed CCTV, intercom, and single-station work). Paid low-voltage work for others runs through the Limited Energy Technician Class A (protective signaling, fire alarm, security, data, control) or Class B (everything except protective signaling) framework under OAR Chapter 918, Division 271, with a Limited Energy Contractor license and a signing supervisor.

**Code**

```
The owner exemption reaches low-voltage work on the owner's residence.
  License exemption for residential or farm property owned by the person or immediate family and not intended for sale, exchange, lease, or rent; applies to Class 2, Class 3, and communications wiring.
  Source: ORS 479.540(1).

The exemption does not waive the code or the permit.
  Work complies with ORS Chapter 455 and the OESC; permits required for new installations except where specifically exempted.
  Source: ORS 479.540(1)(a); OAR 918-261-0039; OAR 918-271-0030.

Paid low-voltage work is licensed work.
  Limited Energy Technician Class A (protective signaling, fire alarm, security, data, control) or Class B; Limited Energy Contractor license with a signing supervisor.
  Source: OAR chapter 918, division 271.
```

## 15.3 Structured Cabling And Wiring Methods

The structured cabling is the durable spine that outlives several generations of devices. It uses the correct cable listing for its location, keeps its required separation from power wiring, is firestopped at rated penetrations, and is bonded at the demarcation.

**Simple**

The cables in the walls will outlive every gadget plugged into them, so one good cable goes everywhere. Every data line runs home to one rack, so any cable can be repurposed by moving one plug. Data cables also keep their distance from power wires. Power induces noise, and a fault could put line voltage on a data line.

**Applied**

- Standardize on Category 6A solid 23 AWG cable with a riser (CMR) jacket as the structured-cabling default; CMR is permitted anywhere a general-purpose (CM) cable is, including riser runs.
- Home-run every data, camera, and access-point cable to the rack, and pull a spare pathway where future replacement would be destructive.
- Keep communications and Class 2/3 cabling at least 2 inches from power conductors, or separate them by a raceway or a continuous nonconductor; do not share a drilled stud hole with power cable.
- Firestop every penetration of a rated wall, floor, or ceiling with a listed through-penetration system.
- Locate the demarcation and structured-media enclosure near the electrical service so the communications bonding conductor stays short.

**Professional**

NEC 800.179 permits general-purpose CM cable throughout a one- and two-family dwelling; CMR is required for vertical runs through more than one floor, and CMP only in a true plenum. Standardizing on Category 6A 23 AWG gives bandwidth headroom for multi-gigabit Ethernet and satisfies the Power-over-Ethernet bundle-heating rules (NEC 725.144 and Table 725.144) for any residential bundle. Cameras and access points drawing IEEE 802.3bt Type 3 or Type 4 power for heaters, illuminators, and pan-tilt motors stay inside those limits. Separation from power follows NEC 800.133 and 725.136 (at least 2 inches unless one circuit is in a raceway or metal-sheathed cable). NEC 800.26 requires firestopping at rated penetrations per 300.21, which applies even where the dwelling is otherwise unrated (the garage-dwelling separation and floor-ceiling barriers must keep their rating). NEC 800.100 bonds the incoming communications protector with a conductor no smaller than 14 AWG and not longer than 20 feet for a one- and two-family dwelling, or a separate bonded ground rod where 20 feet is not practicable.

**Code**

```
Cable listings match the location.
  CM (general-purpose) permitted throughout a one- and two-family dwelling; CMR for multi-floor risers; CMP only in plenums.
  Source: OESC/NEC 800.179 (2023 edition).

Communications and Class 2/3 cabling keep their separation from power.
  At least 2 inches from power conductors unless separated by a raceway, metal-sheathed cable, or continuous nonconductor.
  Source: OESC/NEC 800.133 and 725.136 (2023 edition).

Power-over-Ethernet bundles stay inside the heating limits.
  Bundling limits per the table; Category 6A 23 AWG supports Type 3 and Type 4 bundles at residential scale.
  Source: OESC/NEC 725.144 and Table 725.144 (2023 edition).

Penetrations of rated assemblies are firestopped.
  Listed through-penetration firestop systems at the garage separation and other rated barriers.
  Source: OESC/NEC 800.26 and 300.21 (2023 edition).

The incoming communications protector is bonded to the electrical grounding system.
  Bonding conductor at least 14 AWG and not longer than 20 feet in a one- and two-family dwelling, or a separate bonded ground rod.
  Source: OESC/NEC 800.100 (2023 edition).
```

## 15.4 Smart Switches And Lighting Control

Smart switches preserve the wall-control habit and keep basic lighting local, and every switch box gets a neutral and enough volume for a deeper device. The switches are listed for the load.

**Simple**

A smart switch lives in the wall where the old switch was, so the room still works the way every guest expects. The switch itself needs a neutral wire and a deeper box, both cheap at rough-in and disruptive later. Smart bulbs are for color effects; smart switches are the infrastructure.

**Applied**

- Run a neutral conductor to every switch box, and use deep boxes (about 22 cubic inches or a 4-inch square box with a mud ring) for the deeper smart devices.
- For multi-way control, use either a dedicated smart-switch system with wireless secondaries or hardwired companion switches with travelers home-run to the rack; the hardwired approach is more reliable.
- Specify only UL- or ETL-listed switches and dimmers.
- Confirm each specified lamp appears on the chosen dimmer's compatibility list at the correct control type to prevent flicker, drop-out, and hum.
- Keep the wall switch as the primary control so a guest can operate a room without an app.

**Professional**

NEC 404.2(C) requires a grounded (neutral) conductor at switch boxes controlling lighting in bathrooms, hallways, stairways, and habitable rooms, so a new build installs a neutral at every switch and gains the freedom to swap any device. Box fill follows NEC 314.16, with the device counting as two conductors of the largest size and the grounds counting as one; the deeper smart devices make box downsizing a mistake. Switches and dimmers carry the appropriate listing (snap switches to UL 20, solid-state dimmers to UL 1472, energy-management devices to UL 916). Smart switches are generally better infrastructure than smart bulbs because they keep basic operation at the wall and local; smart bulbs suit color and accent roles where cutting power at the wall is not a concern.

**Code**

```
Switch boxes controlling lighting get a grounded (neutral) conductor.
  Required at switch locations in bathrooms, hallways, stairways, and habitable rooms.
  Source: OESC/NEC 404.2(C) (2023 edition).

Box fill accommodates the deeper device.
  The device counts as two conductors of the largest size connected to it; equipment grounds count as one.
  Source: OESC/NEC 314.16 (2023 edition).

Switches and dimmers carry the matching listing.
  Snap switches UL 20; solid-state dimmers UL 1472; energy-management devices UL 916.
  Source: UL 20; UL 1472; UL 916.
```

## 15.5 Cameras And Oregon Recording Law

Video around the home is largely unregulated, but audio recording of conversations requires all-party notice under Oregon law, which is the constraint that shapes camera configuration. Cameras are kept out of bathrooms and bedrooms, and detection and privacy zones keep them off neighboring property.

**Simple**

Video is mostly legal; audio is the legal constraint. Oregon law bans recording a conversation unless every participant is specifically told it is being recorded. A porch camera with its microphone on can break that law. So the cameras here run with audio off, record locally, and stay pointed at the owner's own property.

**Applied**

- Disable audio by default on all exterior and shared-space cameras.
- Where audio serves an intercom function, use a device that announces it is recording and post a visible sign before the camera's field of view.
- Place no cameras in bathrooms or bedrooms.
- Configure motion-detection zones and privacy masks so alerts fire only on the owner's property and no neighbor's window or fenced yard is recorded, and document the masking.
- Record to local storage (a network video recorder), retain footage for a sensible window (a 14-to-30-day default), and strip audio before sharing any clip publicly.

**Professional**

ORS 165.540 regulates obtaining oral communications, not silent video, so exterior, driveway, and approach cameras and the owner's own interior living-area cameras are permitted where no reasonable expectation of privacy exists. Audio is the constraint: ORS 165.540(1)(c) prohibits obtaining any part of an in-person conversation unless all participants are specifically informed, and the statutory definition of conversation (ORS 165.535(1)) includes communications through video-conferencing programs. Two carve-outs matter here: ORS 165.540(3) lifts the subsection (1) prohibitions for subscribers and their family members acting in their homes, and ORS 165.540(6)(a)(C) permits an unconcealed recording device at private gatherings where the participants knew or reasonably should have known recording was occurring. Announced recording remains the clean practice, and a violation is a Class A misdemeanor (ORS 165.540(9)). ORS 163.700 and 163.701 make recording a person's intimate areas without consent a felony where they have a reasonable expectation of privacy, which is why bathrooms and bedrooms are excluded by default. No Oregon statute prescribes a residential retention period, and sharing footage with police is voluntary. Camera resolution, encoding, and Power-over-Ethernet class follow current product capability; the durable defaults are local recording, object filtering to cut false alerts, and Category 6A cabling to every camera for bandwidth and power headroom.

**Code**

```
In-person audio recording requires that all participants be specifically informed.
  ORS 165.540(1)(c); "conversation" includes video-conference communications (ORS 165.535(1)); violation is a Class A misdemeanor (ORS 165.540(9)).
  Source: ORS 165.540; ORS 165.535 (2025 edition).

Two exceptions cover the home and open recording.
  Subscribers and family members acting in their homes (ORS 165.540(3)); an unconcealed device where participants knew or reasonably should have known (ORS 165.540(6)(a)(C)).
  Source: ORS 165.540(3), (6)(a) (2025 edition).

Recording intimate areas without consent is a felony.
  Applies where the person has a reasonable expectation of privacy; no cameras in bathrooms or bedrooms.
  Source: ORS 163.700; ORS 163.701.

Deliberately targeting a neighbor's private space is chargeable harassment.
  Detection zones and privacy masks keep recording on the owner's property.
  Source: ORS 166.065.
```

## 15.6 Access Control And Locks

A smart lock adds convenience over a quality mechanical lock, and it never removes the safe interior egress that the code requires. Automated garage doors and gates comply with the entrapment-protection standard.

**Simple**

No lock in this house ever needs a phone, code, or battery to get out. The inside of every exit door has a plain thumbturn that opens with one motion. Smart features ride on top: remote checks, guest codes, and alerts. If the electronics die, the door still opens from inside and a metal key still works outside.

**Applied**

- Use a smart deadbolt with an interior thumbturn that opens with a single mechanical motion; do not use a lock that requires a phone or code to exit from inside.
- Specify locks with a mechanical key override and external power contacts as backups, and track battery state in the controller.
- Use a listed, entrapment-protection-compliant garage-door operator; do not bridge a non-compliant opener to the automation system for remote closing.
- Make any electronically controlled door on an egress path fail-safe (unlocks on power loss); reserve fail-secure for non-life-safety doors such as a server closet.

**Professional**

ORSC R311.2 requires the main egress door to open from inside without a key, tool, or special knowledge, which an interior thumbturn satisfies and a code-or-phone-only exit violates. UL 325 (federal law at 16 CFR Part 1211) governs residential garage-door operators: unattended operation (closing without a person in line of sight) requires a pre-motion audible and visual alarm and automatic suspension after repeated obstruction, and it is permitted only on sectional and horizontally sliding doors. A compliant smart opener or a compliant base opener with a listed controller is used rather than relay-bridging a non-compliant unit. UL 325 also covers vehicular gate operators (with monitored entrapment sensors), and ASTM F2200 governs the gate construction.

**Code**

```
The egress door opens from inside without a key, tool, or special knowledge.
  An interior thumbturn with a single mechanical motion satisfies the rule; a phone- or code-only exit violates it.
  Source: ORSC R311.2 (2023 edition).

Garage-door operators carry entrapment protection, including for remote closing.
  Unattended operation requires a pre-motion audible and visual alarm and automatic suspension after repeated obstruction; sectional and horizontally sliding doors only.
  Source: UL 325; 16 CFR Part 1211.

Automated gates use monitored entrapment protection and compliant construction.
  Gate operators per UL 325 with monitored sensors; gate construction per ASTM F2200.
  Source: UL 325; ASTM F2200.

Electronic locks on egress paths fail safe.
  Unlock on power loss for life-safety doors; fail-secure reserved for non-life-safety spaces.
  Source: ORSC R311.2 (2023 edition); lock listing and installation instructions.
```

## 15.7 Alarm Systems And Monitoring

An alarm system can be self-monitored or professionally monitored, and only the professional monitoring is state-regulated. Local jurisdictions require alarm permits and penalize false alarms, so the system is designed to avoid a first-alarm police dispatch.

**Simple**

Watching your own cameras and calling the police yourself is unregulated. Paying a company to watch and call is a licensed service. Cities also fine repeat false alarms, and most require registering the system. The design goal is an alarm that verifies before anyone calls for a dispatch.

**Applied**

- Register the alarm system with the local jurisdiction (a permit is commonly required within 30 days of installation, sometimes even for an unmonitored siren).
- Design the system to avoid police dispatch on a first alarm: use video verification, require multiple contact attempts (enhanced call verification), and program a siren-only interval before manual escalation.
- Use a professional monitoring company that holds the required state license and follows enhanced call verification if monitoring is used.
- Route any fire-alarm protective-signaling work to a licensed Limited Energy Class A technician and an NFPA 72 design.

**Professional**

Alarm-monitoring services and security professionals are regulated by DPSST under ORS 181A.840 to 181A.995 and OAR Chapter 259; a professional monitoring company needs a private security entity license, but a self-monitored system (the owner watches cameras and decides whether to call police) has no DPSST involvement. False-alarm ordinances and alarm-permit registration are entirely local and vary by city and county, so the specific jurisdiction's rules and fees are confirmed at design. Most ordinances require enhanced call verification before dispatch. Fire-alarm protective signaling requires the Class A limited-energy scope and NFPA 72 compliance, which is separate from the general security and automation work.

**Code**

```
Professional alarm monitoring is a licensed private-security service.
  DPSST regulation of alarm-monitoring entities and security professionals; self-monitored systems are outside the regime.
  Source: ORS 181A.840-181A.995; OAR chapter 259.

Alarm registration and false-alarm penalties are local rules.
  Permit registration commonly required within 30 days of installation; fee and penalty schedules vary; verified for the site jurisdiction.
  Source: local alarm ordinance of the site jurisdiction.

Fire-alarm signaling is Class A licensed work to the alarm standard.
  Limited Energy Class A technician; system design and installation per NFPA 72.
  Source: OAR chapter 918, division 271; NFPA 72.
```

## 15.8 Local-First Controllers, Protocols, And Voice

The automation controller is the central architectural choice for a house that must work without the internet, so it runs locally with the device radios chosen for reliability. Voice control, where used, is processed locally.

**Simple**

The controller is the house's automation brain, and it lives in the rack, not in a company's cloud. Scenes, schedules, and alerts all run on it directly. Automation is also rationed: it earns its place where it prevents damage or saves a repeated chore. Cooking stays manual, and nothing safety-critical depends on an automation working.

**Applied**

- Run a local-first controller (Home Assistant is the reference open-source option) on dedicated hardware with a wired network connection and a nightly configuration backup.
- Automate the high-value items first: a goodnight scene (lights, locks, thermostats), an away and home mode, leak detection with automatic shutoff, alarm notifications, and left-open alerts for doors and the garage.
- Leave manual what automation does not improve: cooking appliances, interior doors, and window operation; keep a working physical control for every automated function.
- Set fail-safe defaults: on automation failure, lights operable at the wall, doors openable from inside, heating and ventilation running, and cameras still recording locally.
- Use a reliable mesh radio for security-critical devices: Z-Wave (800 series) for locks, leak sensors, and door and window sensors, where reliability matters most.
- Use Zigbee or Matter over Wi-Fi for sensors and lighting, and treat Matter over Thread as maturing rather than mission-critical until the border-router mesh is proven.
- Prefer wired or reliable-mesh devices over cloud-dependent Wi-Fi devices, which congest the access point and depend on a vendor's servers.
- Use a local voice assistant (on-device speech processing) where voice is wanted, and keep microphones out of bedrooms and bathrooms.

**Professional**

A local controller keeps every automation running without the internet by default, with cloud features (remote access, voice) as opt-in through a self-hosted VPN or a subscription. Z-Wave remains the most reliable residential mesh for security-critical devices; Matter over Thread can drop out of the mesh if a border router reboots or Wi-Fi multicast breaks, so locks, alarms, and smoke-detector bridges use Z-Wave or a hardwired connection until Thread proves out on the site. Automation priority follows value: damage prevention (leak shutoff, freeze alerts) and daily-repetition scenes come first, occupancy lighting and seasonal schedules second, novelty integrations last, and the failure default for every automation leaves the house operable by hand. A cloud voice assistant is incompatible with the local-first rule; a local assistant that processes audio on-device and retains no recording is both more private and, under ORS 165.540, a safer posture than one that uploads audio.

**Code**

```
Life-safety and code-required functions stay independent of the controller.
  Smoke and CO alarms, egress operation, and required electrical protection function with the controller offline.
  Source: ORSC R314, R315, R311.2 (2023 edition).

Always-listening microphones follow the recording statute.
  On-device processing that retains no recording; all-party notice where audio is captured.
  Source: ORS 165.540 (2025 edition).
```

## 15.9 Energy, Water, And Appliance Monitoring

Monitoring makes a problem visible: a jump in power, water flowing when no one is using it, or a heat pump running too long. The sensors are installed on the correct trade path, and automated shutoffs and appliances keep safe default behavior.

**Simple**

A leak sensor and an automatic shutoff valve can turn a burst hose into a mop-up instead of a gutted floor. An energy monitor shows what each big load costs to run. The rule for smart appliances is watch and notify: the machine reports, and a person starts it.

**Applied**

- Install a whole-panel energy monitor with current transformers to track total and major-load electricity, and locate it on the approved electrical path.
- Use non-invasive water-flow sensors (which clamp on and need no plumbing permit), and have a licensed plumber install any powered in-line shutoff valve.
- Give any automated water shutoff a battery backup and a fail-state that does not trap occupants without water.
- Treat smart appliances as monitor-and-notify: allow remote start only where the appliance is listed for it and the user has enabled it locally; keep the oven monitor-only.
- Turn monitoring into action with alert thresholds, not just dashboards.

**Professional**

An in-panel energy monitor is field-installable under NEC 312.8(B) with system-listed current transformers (UL 2808); the owner may install the transformers on their own residence under the homeowner exemption, while a paid installer needs the limited-energy scope and a general electrician for any line-voltage tap. Non-invasive flow sensors are not plumbing work, but a powered in-line shutoff valve is new plumbing that requires a licensed plumber (there is no homeowner exemption for new plumbing). UL 858 Section 47A restricts remote start of a cooking appliance to listed modes that require a local enable, so pure remote start of a cold oven is not allowed; the durable default is monitor-and-notify with local enable for the dishwasher, washer, and dryer. Pool, well, and irrigation controllers are typically Class 2 control circuits that automate freely, with the actuated equipment carrying its own listing.

**Code**

```
Panel-mounted power monitoring is permitted with listed components.
  Monitoring equipment in a panelboard per the code; current transformers system-listed to UL 2808.
  Source: OESC/NEC 312.8(B) (2023 edition); UL 2808.

The trades split the monitoring installation.
  Owner installation permitted on the owner-occupied residence; paid installers need the limited-energy scope plus a general electrician for line-voltage taps; a powered in-line water valve is licensed plumbing work.
  Source: ORS 479.540(1); ORS 693.020 and 447.060 (plumbing licensing; see the water-supply chapter).

Remote start of cooking appliances is limited by the appliance listing.
  Listed modes require a local enable; a cold oven cannot be started purely remotely.
  Source: UL 858, Section 47A.
```

## 15.10 Audio, Video, And The Equipment Rack

Whole-house audio and video stay modular so the durable cabling and rack outlive the receivers and displays. The rack is ventilated, because heat is the main long-term failure cause for network gear.

**Simple**

The rack is the utility closet for data. It holds the internet gear, switches, controller, recorder, and backup power in one serviceable place. Electronics in it run warm all day, and trapped heat shortens their lives. So the rack gets ventilation, labeled cables, and room to work, the same treatment the mechanical room gives its equipment.

**Applied**

- Use listed in-wall speaker cable (CL2 or CL3, plenum-rated where required), with the conductor gauge matched to the run length.
- Distribute a display more than about 25 feet from its source over a point-to-point extender on Category 6A cabling rather than a network-dependent scheme, keeping the video path independent of the network.
- Reserve rack space for the internet terminal, router or firewall, switches, patch panels, the automation controller, the camera recorder, storage, and the backup power unit, with cable management and service clearance.
- Ventilate the rack (passive top vents or active fans); do not seal it in an unconditioned closet.
- Do not trap a display cable in a finished concrete wall without a replacement pathway.

**Professional**

In-wall speaker wire is listed CL2 or CL3 under Article 725; a point-to-point HDBaseT-class extender over Category 6A keeps the audio-video path off the network stack, which suits a house that must function without the internet. The rack's heat load is roughly 1 BTU per hour per watt of equipment dissipation, and passive top venting holds a typical residential rack to about 20 degrees above ambient while active fans cut that further. The automation controller and the recorder are treated as serviceable appliances with stable power, wired network, cooling, and a recovery plan, located where they can be maintained rather than buried in a closet.

**Code**

```
In-wall audio cable is listed for the location.
  CL2 or CL3 under Article 725; CL2P/CL3P in plenums.
  Source: OESC/NEC Article 725 (2023 edition).

Video distribution cabling uses in-wall-rated communications cable.
  Point-to-point extension over Category 6A; cable listings per Articles 722 and 800.
  Source: OESC/NEC Articles 722 and 800 (2023 edition).
```

## 15.11 Network Security Architecture

Every smart device is a small computer, and some are poorly built, so the network is segmented and defaults to deny. Cameras and untrusted devices are isolated from the trusted network, and remote access never exposes a service directly to the internet.

**Simple**

Every smart device is a small computer, and some are badly made. The defense is walls inside the network. Cameras go on one segment, gadgets on another, family computers on a third. Firewall rules control which segment can talk to which. Nothing inside is ever opened directly to the internet. Remote access goes through an encrypted tunnel instead.

**Applied**

- Segment the network into at least four VLANs: management, trusted (computers and phones), IoT (smart devices, outbound internet only), and cameras (isolated, no camera internet access except firmware and time), plus an optional guest network.
- Run a default-deny firewall between VLANs: trusted can reach IoT, IoT cannot initiate back to trusted.
- Do not port-forward internal services to the internet; use a VPN (such as Tailscale or WireGuard) for remote access.
- Run a filtering DNS resolver on the LAN, give every device a unique password from a password manager, and rotate manufacturer defaults at install.
- Prefer devices from manufacturers meeting the NIST consumer-IoT baseline: unique credentials, signed and supported software updates, and documented support periods.
- Back up the controller configuration nightly to local storage and weekly off-site.

**Professional**

The current guidance from CISA and NIST converges on VLAN segmentation, a default-deny firewall, and microsegmentation for IoT-heavy homes. Cameras live on an isolated VLAN with no internet egress except for time and firmware, and the recorder is the only device that talks to them; the controller and phones view streams through the recorder rather than by direct connection. The internet gateway runs in bridge mode behind an owner-controlled router and firewall rather than trusting the provider's router. Device selection uses the NIST consumer-IoT baseline family as the screen: NIST IR 8425 (2022) profiles the core cybersecurity baseline for consumer IoT products, NIST IR 8425A (2024) states the requirements for consumer-grade routers, and the manufacturer-side foundations are NIST IR 8259 Rev. 1 (2026) with the 8259A and 8259B core baselines. None of this is building code; it is a project design requirement, sourced to the NIST and CISA guidance, and this section has no Code block because there is no statute, rule, or consensus standard to cite. The requirement it enforces stands: no local dashboard, camera, or lock is exposed directly to the public internet, and remote access runs only through the VPN.

## 15.12 Backup Power And Resilience

A small uninterruptible power supply keeps the rack alive through outages so the network does not crash, the controller does not corrupt its storage, and the cameras do not go blind. It rides through short outages and shuts down gracefully in long ones, independent of any whole-house backup.

**Simple**

A battery unit in the rack keeps the network, controller, and cameras running when the power blinks. In a longer outage it tells the equipment to shut down cleanly before the battery empties. Without it, every grid blink means crashed gear, corrupted recordings, and blind cameras.

**Applied**

- Put the internet terminal, router or firewall, network switch, Power-over-Ethernet switch, controller, and recorder on the uninterruptible power supply.
- Size the unit to at least 1.6 times the total rack wattage in volt-amperes, targeting at least 30 minutes of runtime (60 is more comfortable).
- Connect the unit to the controller or recorder over USB and run power-management software so dependent devices shut down cleanly before the battery dies.
- Ventilate the unit (batteries off-gas under deep discharge) and label its install date; replace on schedule.
- Pair the rack unit with a whole-house surge protective device at the main panel.

**Professional**

The rack uninterruptible power supply is listed to UL 1778; a lithium-iron-phosphate unit costs more than sealed lead-acid but lasts longer and tolerates heat better, which pays back over a long-service design. Network UPS Tools broadcasts the power state so the storage, controller, and recorder shut down cleanly before the battery is exhausted, and restore automatically when power returns. The rack backup is sized independently of any whole-house generator or battery decision, so the rack rides through grid blips even when the rest of the house has separate backup; the whole-house provisions are stated in the electrical service chapter and the HVAC chapter's outage section. The whole-house surge protective device at the panel is the upstream defense, with the rack unit as the second line.

**Code**

```
The uninterruptible power supply is listed equipment.
  UL 1778 listing; installed per instructions with ventilation and replacement schedule.
  Source: UL 1778.

The service carries a surge protective device.
  Type 1 or Type 2 SPD at the service; the rack unit is the second line of defense.
  Source: OESC/NEC 230.67 (2023 edition; see the electrical service chapter).
```

## 15.13 Commissioning, Documentation, And Maintenance

The smart home is proven by running the house with the internet pulled and the power cut. The records let a future owner or technician restart and maintain the system without reverse-engineering it.

**Simple**

The real test is unplugging things. Pull the internet: lights, locks, heat, and cameras should not care. Cut the power: the rack should ride its battery, shut down cleanly, and come back by itself. What fails either test gets fixed or gets documented as a convenience feature, not a core one.

**Applied**

Commission the system and document the result:

- Internet-out test: pull the wide-area connection and confirm scenes, sensors, locks, cameras, the local dashboard, and local voice still work; record any feature that fails as cloud-dependent.
- Power-out test: cut the main breaker and confirm the rack rides the backup for its rated runtime, then shuts down gracefully and restarts cleanly.
- Camera review: confirm detection zones and privacy masks stay on the owner's property and audio is disabled or noticed.
- Lock review: confirm the mechanical key, external power contacts, and interior thumbturn work on every lock.
- Records: a network diagram (VLANs, switches, access points), a wiring diagram with every cable labeled at both ends, the controller configuration in version control and backed up, a device inventory (model, address, firmware, install date, location), and a maintenance schedule (battery dates, firmware cadence, password rotation).
- Budget the refresh: a reserve of roughly $500-$2,000 per year (2026) covers device replacement and updates across the system's life; the cabling and rack are excluded because they are the durable layer.

**Professional**

Commissioning verifies the manual fallback, local operation, internet-out behavior, power-failure behavior, camera recording, sensor response, alarm states, and lock behavior, and confirms backups restore to a known-good instance. Maintenance is deliberately routine: update, back up, test, replace batteries, review accounts, check logs, test the backup power, and retire old devices. Devices are consumables on a 5-to-10-year cycle against a 20-plus-year cabling layer, which is why the replacement reserve funds devices and never needs to fund rewiring. The smart home is complete when the house works locally, safely, privately, and predictably, and the documentation is good enough that a future repair does not start from guesswork.

**Code**

```
Low-voltage work closes out through the jurisdiction's inspection where required.
  Final low-voltage inspection per the local program; communications bonding and firestopping verified.
  Source: OESC/NEC 800.100, 800.26 (2023 edition); local permit program.

The records are part of the house file.
  Network and wiring diagrams, controller backup, device inventory, and the maintenance schedule retained with the house documentation.
  Source: project documentation standard (see the documentation chapter).
```
