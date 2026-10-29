# Chapter 15: Smart Home, Network, Security, And Local Automation

This chapter covers the digital layer: the structured cabling and network, the local automation controller, smart switches, security cameras, access control and locks, alarm systems, energy and water monitoring, audio and video, network security, backup power for the rack, and commissioning. It is built on a local-first rule: the house keeps working when the internet is down, a subscription ends, or a vendor disappears.

The wiring methods, device listings, separations, and recording-law constraints that govern this work in Oregon are independent of whether a device connects to the internet. The electrical code of record is the 2023 Oregon Electrical Specialty Code (OESC), the 2023 NEC with Oregon amendments in Table 1-E; the 2023 NEC reorganized low-voltage cabling into Article 722 (cable requirements), Article 725 (Class 2 and Class 3 circuits), and Article 800 (communications). Product models and protocols change every cycle, so this chapter fixes the infrastructure, the code, and the architecture, and treats specific devices as replaceable examples.

## 15.1 Scope And The Local-First Principle

The permanent value of the smart home is the cabling, rack space, power, labels, and network architecture, not the devices. Core functions run locally so ordinary use never depends on a cloud service, and life-safety systems keep their required behavior independent of the automation platform.

**Simple**

A smart home should make the house easier to live in without making it fragile. Lights still turn on from the wall switch, doors still open from the inside, heat still works, and cameras still record, whether or not the internet is up. The internet adds remote access, updates, and notifications; it does not hold the house hostage.

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
2023 OESC (NEC 2023 + Table 1-E): governs low-voltage, communications, and control wiring; Articles 722 (cabling), 725 (Class 2/3 circuits), 800 (communications).
Life-safety independence: smoke/CO alarms (ORSC R314/R315), egress operation (R311.2), and required electrical protection operate independently of the automation platform.
```

## 15.2 The Legal And Permit Layer

An owner-builder may install low-voltage and communications wiring on their own primary residence under the same intent-based exemption that covers line-voltage work, but the work still complies with the electrical code and is permitted except where a specific exemption applies. Paid low-voltage work for others requires a limited-energy license.

**Applied**

- Perform the owner's own low-voltage work under the homeowner exemption on the primary residence, to code.
- Pull a low-voltage permit for new installations except where a specific exemption applies (such as Class 2 wiring on the load side of a listed Class 2 transformer, or listed intercom and CCTV work in a one- or two-family dwelling under the stated conditions).
- Confirm the local jurisdiction's low-voltage permit posture before final design; enforcement varies by county and city.
- Use a licensed Limited Energy contractor for any paid low-voltage work on a third party's home.

**Professional**

ORS 479.540(1) exempts an owner from electrical licensing for work on a residence the owner occupies and does not intend to sell or lease, and it applies to Class 2, Class 3, and communications work as it does to line-voltage. The exemption is from licensing, not from the code: ORS 479.540(1)(a) requires the work to comply with ORS Chapter 455 and the OESC, and a permit is required for new low-voltage installations except where specifically exempted (OAR 918-261-0039 for load-side Class 2 wiring, OAR 918-271-0030 for certain listed CCTV, intercom, and single-station work). Paid low-voltage work for others runs through the Limited Energy Technician Class A (protective signaling, fire alarm, security, data, control) or Class B (everything except protective signaling) framework under OAR Chapter 918, Division 271, with a Limited Energy Contractor license and a signing supervisor.

**Code**

```
ORS 479.540(1): owner exemption from electrical licensing for the owner-occupied, not-for-sale residence; applies to low-voltage.
ORS 479.540(1)(a): the work still complies with ORS Chapter 455 and the OESC; permits required except where exempted.
OAR 918-261-0039 and 918-271-0030: specific Class 2 load-side and listed-system permit exemptions.
OAR Chapter 918, Division 271: Limited Energy Technician Class A/B and contractor licensing for paid work.
```

## 15.3 Structured Cabling And Wiring Methods

The structured cabling is the durable spine that outlives several generations of devices. It uses the correct cable listing for its location, keeps its required separation from power wiring, is firestopped at rated penetrations, and is bonded at the demarcation.

**Applied**

- Standardize on Category 6A solid 23 AWG cable with a riser (CMR) jacket as the structured-cabling default; CMR is permitted anywhere a general-purpose (CM) cable is, including riser runs.
- Home-run every data, camera, and access-point cable to the rack, and pull a spare pathway where future replacement would be destructive.
- Keep communications and Class 2/3 cabling at least 2 inches from power conductors, or separate them by a raceway or a continuous nonconductor; do not share a drilled stud hole with power cable.
- Firestop every penetration of a rated wall, floor, or ceiling with a listed through-penetration system.
- Locate the demarcation and structured-media enclosure near the electrical service so the communications bonding conductor stays short.

**Professional**

NEC 800.179 permits general-purpose CM cable throughout a one- and two-family dwelling; CMR is required for vertical runs through more than one floor, and CMP only in a true plenum. Standardizing on Category 6A 23 AWG gives bandwidth headroom for multi-gigabit Ethernet and satisfies the Power-over-Ethernet bundle-heating rules (NEC 725.144 and Table 725.144) for any residential bundle, including cameras and access points that draw IEEE 802.3bt Type 3 or Type 4 power for heaters, illuminators, and pan-tilt motors. Separation from power follows NEC 800.133 and 725.136 (at least 2 inches unless one circuit is in a raceway or metal-sheathed cable). NEC 800.26 requires firestopping at rated penetrations per 300.21, which applies even where the dwelling is otherwise unrated (the garage-dwelling separation and floor-ceiling barriers must keep their rating). NEC 800.100 bonds the incoming communications protector with a conductor no smaller than 14 AWG and not longer than 20 feet for a one- and two-family dwelling, or a separate bonded ground rod where 20 feet is not practicable.

**Code**

```
NEC 800.179: CM (general-purpose) cable permitted throughout a one- and two-family dwelling; CMR for multi-floor risers, CMP for plenums.
NEC 800.133 and 725.136: at least 2-inch separation of communications/Class 2/3 from power conductors unless separated by raceway or continuous nonconductor.
NEC 725.144 and Table 725.144: Power-over-Ethernet conductor bundling limits; Category 6A 23 AWG supports Type 4 bundles.
NEC 800.26 and 300.21: firestopping at penetrations of rated assemblies with a listed system.
NEC 800.100: communications bonding conductor at least 14 AWG, not longer than 20 feet, or a bonded ground rod.
```

## 15.4 Smart Switches And Lighting Control

Smart switches preserve the wall-control habit and keep basic lighting local, and every switch box gets a neutral and enough volume for a deeper device. The switches are listed for the load.

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
NEC 404.2(C): grounded (neutral) conductor required at switch boxes controlling lighting in bathrooms, hallways, stairways, and habitable rooms.
NEC 314.16: box fill (device counts as two conductors of the largest size; grounds count as one); use deep boxes for smart devices.
UL 20, UL 1472, UL 916: listings for snap switches, solid-state dimmers, and energy-management devices.
Lighting outlets and closet luminaires: see the branch-circuit chapter (NEC 210.70, 410.16).
```

## 15.5 Cameras And Oregon Recording Law

Video around the home is largely unregulated, but audio recording of conversations requires all-party notice under Oregon law, which is the constraint that shapes camera configuration. Cameras are kept out of bathrooms and bedrooms, and detection and privacy zones keep them off neighboring property.

**Applied**

- Disable audio by default on all exterior and shared-space cameras.
- Where audio serves an intercom function, use a device that announces it is recording and post a visible sign before the camera's field of view.
- Place no cameras in bathrooms or bedrooms.
- Configure motion-detection zones and privacy masks so alerts fire only on the owner's property and no neighbor's window or fenced yard is recorded, and document the masking.
- Record to local storage (a network video recorder), retain footage for a sensible window (a 14-to-30-day default), and strip audio before sharing any clip publicly.

**Professional**

ORS 165.540 does not regulate video-only recording in places without a reasonable expectation of privacy, so exterior, driveway, and approach cameras and the owner's own interior living-area cameras are permitted. Audio is the trap: ORS 165.540(1)(c) prohibits obtaining any part of a conversation without informing all participants, which a doorbell or porch camera capturing visitors' speech can violate; the all-party-notice rule for audio is settled Oregon law. ORS 163.700 and 163.701 make recording a person's intimate areas without consent a felony where they have a reasonable expectation of privacy, which is why bathrooms and bedrooms are excluded by default. No Oregon statute prescribes a residential retention period, and sharing footage with police is voluntary. Camera resolution, encoding, and Power-over-Ethernet class follow current product capability; the durable defaults are local recording, object filtering to cut false alerts, and Category 6A cabling to every camera for bandwidth and power headroom.

**Code**

```
ORS 165.540(1)(c): audio recording of a conversation requires all-party notice; disable audio or post notice.
ORS 165.540(3): homeowner exception for video in the owner's own home; no video-only regulation in non-private places.
ORS 163.700 / 163.701: recording intimate areas without consent is a felony; no cameras in bathrooms or bedrooms.
ORS 166.065 (harassment): applies where a camera is deliberately targeted at a neighbor's private space; use detection zones and privacy masks.
```

## 15.6 Access Control And Locks

A smart lock adds convenience over a quality mechanical lock, and it never removes the safe interior egress that the code requires. Automated garage doors and gates comply with the entrapment-protection standard.

**Applied**

- Use a smart deadbolt with an interior thumbturn that opens with a single mechanical motion; do not use a lock that requires a phone or code to exit from inside.
- Specify locks with a mechanical key override and external power contacts as backups, and track battery state in the controller.
- Use a listed, entrapment-protection-compliant garage-door operator; do not bridge a non-compliant opener to the automation system for remote closing.
- Make any electronically controlled door on an egress path fail-safe (unlocks on power loss); reserve fail-secure for non-life-safety doors such as a server closet.

**Professional**

ORSC R311.2 requires the main egress door to open from inside without a key, tool, or special knowledge, which an interior thumbturn satisfies and a code-or-phone-only exit violates. UL 325 (federal law at 16 CFR Part 1211) governs residential garage-door operators: unattended operation (closing without a person in line of sight) requires a pre-motion audible and visual alarm and automatic suspension after repeated obstruction, and it is permitted only on sectional and horizontally sliding doors. A compliant smart opener or a compliant base opener with a listed controller is used rather than relay-bridging a non-compliant unit. UL 325 also covers vehicular gate operators (with monitored entrapment sensors), and ASTM F2200 governs the gate construction.

**Code**

```
ORSC R311.2: egress door operable from inside without a key, tool, or special knowledge; interior thumbturn satisfies it.
UL 325 / 16 CFR Part 1211: residential garage-door operator entrapment protection; unattended operation requires pre-motion audible/visual alarm and obstruction suspension, sectional/sliding doors only.
UL 325 (gate operators) and ASTM F2200: vehicular gate operator entrapment protection and gate construction.
Electronic egress-path locks: fail-safe (unlock on power loss) for life-safety doors.
```

## 15.7 Alarm Systems And Monitoring

An alarm system can be self-monitored or professionally monitored, and only the professional monitoring is state-regulated. Local jurisdictions require alarm permits and penalize false alarms, so the system is designed to avoid a first-alarm police dispatch.

**Applied**

- Register the alarm system with the local jurisdiction (a permit is commonly required within 30 days of installation, sometimes even for an unmonitored siren).
- Design the system to avoid police dispatch on a first alarm: use video verification, require multiple contact attempts (enhanced call verification), and program a siren-only interval before manual escalation.
- Use a professional monitoring company that holds the required state license and follows enhanced call verification if monitoring is used.
- Route any fire-alarm protective-signaling work to a licensed Limited Energy Class A technician and an NFPA 72 design.

**Professional**

Alarm-monitoring services and security professionals are regulated by DPSST under ORS 181A.840 to 181A.995 and OAR Chapter 259; a professional monitoring company needs a private security entity license, but a self-monitored system (the owner watches cameras and decides whether to call police) has no DPSST involvement. False-alarm ordinances and alarm-permit registration are entirely local and vary by city and county, so the specific jurisdiction's rules and fees are confirmed at design. Most ordinances require enhanced call verification before dispatch. Fire-alarm protective signaling requires the Class A limited-energy scope and NFPA 72 compliance, which is separate from the general security and automation work.

**Code**

```
ORS 181A.840–181A.995 and OAR Chapter 259: DPSST regulation of alarm monitoring and security professionals; entity license for professional monitoring; self-monitored systems unregulated.
Local alarm ordinances: registration/permit and false-alarm penalties vary by jurisdiction; verify at the site.
Fire alarm (protective signaling): Limited Energy Class A technician and NFPA 72 compliance.
```

## 15.8 Local-First Controllers, Protocols, And Voice

The automation controller is the central architectural choice for a house that must work without the internet, so it runs locally with the device radios chosen for reliability. Voice control, where used, is processed locally.

**Applied**

- Run a local-first controller (Home Assistant is the reference open-source option) on dedicated hardware with a wired network connection and a nightly configuration backup.
- Use a reliable mesh radio for security-critical devices: Z-Wave (800 series) for locks, leak sensors, and door and window sensors, where reliability matters most.
- Use Zigbee or Matter over Wi-Fi for sensors and lighting, and treat Matter over Thread as maturing rather than mission-critical until the border-router mesh is proven.
- Prefer wired or reliable-mesh devices over cloud-dependent Wi-Fi devices, which congest the access point and depend on a vendor's servers.
- Use a local voice assistant (on-device speech processing) where voice is wanted, and keep microphones out of bedrooms and bathrooms.

**Professional**

A local controller keeps every automation running without the internet by default, with cloud features (remote access, voice) as opt-in through a self-hosted VPN or a subscription. Z-Wave remains the most reliable residential mesh for security-critical devices; Matter over Thread can drop out of the mesh if a border router reboots or Wi-Fi multicast breaks, so locks, alarms, and smoke-detector bridges use Z-Wave or a hardwired connection until Thread proves out on the site. A cloud voice assistant is incompatible with the local-first rule; a local assistant that processes audio on-device and retains no recording is both more private and, under ORS 165.540, a safer posture than one that uploads audio.

**Code**

```
Life-safety and code-required functions independent of the controller (see the scope section).
ORS 165.540: local, on-device voice processing that retains no recording is the safer posture for always-listening microphones.
Device listings: controllers, hubs, and radios are listed equipment installed per instructions.
```

## 15.9 Energy, Water, And Appliance Monitoring

Monitoring makes a problem visible: a jump in power, water flowing when no one is using it, or a heat pump running too long. The sensors are installed on the correct trade path, and automated shutoffs and appliances keep safe default behavior.

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
NEC 312.8(B): power-monitoring equipment permitted in a panelboard; current transformers system-listed (UL 2808).
ORS 479.540(1): owner may install monitoring on the owner-occupied residence; paid installer needs limited-energy scope plus a general electrician for line-voltage taps.
Powered in-line water shutoff valve: new plumbing requiring a licensed plumber (no homeowner exemption for new plumbing).
UL 858 Section 47A: remote start of a listed cooking appliance requires a local enable; oven remains monitor-only.
```

## 15.10 Audio, Video, And The Equipment Rack

Whole-house audio and video stay modular so the durable cabling and rack outlive the receivers and displays. The rack is ventilated, because heat is the main long-term failure cause for network gear.

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
NEC Article 725: in-wall speaker cable listed CL2 or CL3 (CL2P/CL3P for plenums).
NEC Article 800 / 722: cabling for audio-video distribution over Category 6A; in-wall rated cable only.
Rack: ventilation and electrical working space maintained; do not block required clearances.
```

## 15.11 Network Security Architecture

Every smart device is a small computer, and some are poorly built, so the network is segmented and defaults to deny. Cameras and untrusted devices are isolated from the trusted network, and remote access never exposes a service directly to the internet.

**Applied**

- Segment the network into at least four VLANs: management, trusted (computers and phones), IoT (smart devices, outbound internet only), and cameras (isolated, no camera internet access except firmware and time), plus an optional guest network.
- Run a default-deny firewall between VLANs: trusted can reach IoT, IoT cannot initiate back to trusted.
- Do not port-forward internal services to the internet; use a VPN (such as Tailscale or WireGuard) for remote access.
- Run a filtering DNS resolver on the LAN, give every device a unique password from a password manager, and rotate manufacturer defaults at install.
- Back up the controller configuration nightly to local storage and weekly off-site.

**Professional**

The current guidance from CISA and NIST converges on VLAN segmentation, a default-deny firewall, and microsegmentation for IoT-heavy homes. Cameras live on an isolated VLAN with no internet egress except for time and firmware, and the recorder is the only device that talks to them; the controller and phones view streams through the recorder rather than by direct connection. The internet gateway runs in bridge mode behind an owner-controlled router and firewall rather than trusting the provider's router. Most of this is not building code, but it protects the cameras, locks, alarms, and controls that are connected, so no local dashboard, camera, or lock is exposed directly to the public internet.

**Code**

```
Not building code, but a design requirement: no direct public-internet exposure of cameras, locks, dashboards, or controls; remote access via VPN.
Segmentation and default-deny firewall per CISA and NIST residential IoT guidance.
```

## 15.12 Backup Power And Resilience

A small uninterruptible power supply keeps the rack alive through outages so the network does not crash, the controller does not corrupt its storage, and the cameras do not go blind. It rides through short outages and shuts down gracefully in long ones, independent of any whole-house backup.

**Applied**

- Put the internet terminal, router or firewall, network switch, Power-over-Ethernet switch, controller, and recorder on the uninterruptible power supply.
- Size the unit to at least 1.6 times the total rack wattage in volt-amperes, targeting at least 30 minutes of runtime (60 is more comfortable).
- Connect the unit to the controller or recorder over USB and run power-management software so dependent devices shut down cleanly before the battery dies.
- Ventilate the unit (batteries off-gas under deep discharge) and label its install date; replace on schedule.
- Pair the rack unit with a whole-house surge protective device at the main panel.

**Professional**

The rack uninterruptible power supply is listed to UL 1778; a lithium-iron-phosphate unit costs more than sealed lead-acid but lasts longer and tolerates heat better, which pays back over a long-service design. Network UPS Tools broadcasts the power state so the storage, controller, and recorder shut down cleanly before the battery is exhausted, and restore automatically when power returns. The rack backup is sized independently of any whole-house generator or battery decision, so the rack rides through grid blips even when the rest of the house has separate backup. The whole-house surge protective device at the panel is the upstream defense, with the rack unit as the second line.

**Code**

```
UL 1778: uninterruptible power supply listing.
Whole-house Type 1 or Type 2 surge protective device at the service (NEC 230.67; see the electrical service chapter).
Graceful shutdown via power-management software so dependent devices power down before the battery is exhausted.
```

## 15.13 Commissioning, Documentation, And Maintenance

The smart home is proven by running the house with the internet pulled and the power cut, not by a dashboard that looks finished. The records let a future owner or technician restart and maintain the system without reverse-engineering it.

**Applied**

Commission the system and document the result:

- Internet-out test: pull the wide-area connection and confirm scenes, sensors, locks, cameras, the local dashboard, and local voice still work; record any feature that fails as cloud-dependent.
- Power-out test: cut the main breaker and confirm the rack rides the backup for its rated runtime, then shuts down gracefully and restarts cleanly.
- Camera review: confirm detection zones and privacy masks stay on the owner's property and audio is disabled or noticed.
- Lock review: confirm the mechanical key, external power contacts, and interior thumbturn work on every lock.
- Records: a network diagram (VLANs, switches, access points), a wiring diagram with every cable labeled at both ends, the controller configuration in version control and backed up, a device inventory (model, address, firmware, install date, location), and a maintenance schedule (battery dates, firmware cadence, password rotation).

**Professional**

Commissioning verifies the manual fallback, local operation, internet-out behavior, power-failure behavior, camera recording, sensor response, alarm states, and lock behavior, and confirms backups restore to a known-good instance. Maintenance is deliberately routine: update, back up, test, replace batteries, review accounts, check logs, test the backup power, and retire old devices. The smart home is complete when the house works locally, safely, privately, and predictably, and the documentation is good enough that a future repair does not start from guesswork.

**Code**

```
Final low-voltage inspection where required by the jurisdiction; communications bonding and firestopping verified.
Records to retain: network and wiring diagrams, controller backup, device inventory, and the maintenance schedule.
```
