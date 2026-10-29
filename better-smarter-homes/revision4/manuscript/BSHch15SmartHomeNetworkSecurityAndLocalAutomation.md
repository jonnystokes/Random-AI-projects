# Chapter 15: Smart Home, Network, Security, And Local Automation

This chapter covers the digital layer of the house: network rack, local automation, smart switches, sensors, security cameras, access control, audio, video, energy monitoring, voice control, smart appliances, privacy, cybersecurity, backup power, and long-term service.

The rule is simple: the house must still work when the internet is down, a vendor disappears, a subscription ends, or the automation server is turned off.

Exact cable categories, device models, camera resolutions, PoE levels, NVR sizing, storage duration, access-control rules, privacy laws, wireless protocols, security settings, alarm monitoring, UPS runtimes, and cybersecurity requirements must be verified during final design.

## Smart Home Scope

**Simple**

A smart home should make the house easier to live in. It should not make the house fragile.

Lights should still turn on from a wall switch. Doors should still open from the inside. Heat should still work. Cameras should still record locally. The internet should be useful, not required.

**Applied**

Separate the smart-home work into layers:

| Layer | Job |
|---|---|
| Network | Moves data through the house. |
| Power | Keeps racks, switches, hubs, cameras, and sensors running. |
| Automation | Connects devices and runs scenes. |
| Security | Handles cameras, locks, sensors, and alerts. |
| Monitoring | Tracks energy, water, comfort, and equipment status. |
| Manual fallback | Lets the house work without automation. |

Plan the network rack and low-voltage pathways before finishes close the walls.

**Professional**

Smart-home design should be infrastructure first and gadget second. The permanent value is the pathway, rack space, power, labels, documentation, network segmentation, and manual fallback. Devices can change. Protocols can change. The wiring and access plan should survive several generations of equipment.

The source direction is local-first, cloud-optional, privacy-aware, and serviceable. That should remain the backbone of this chapter.

**Code**

Low-voltage wiring, communications cabling, fire alarm circuits, power-limited circuits, optical fiber, coax, equipment grounding, penetrations, support, separation from power wiring, device listings, and electrical connections can be code-controlled.

Use the adopted electrical code, manufacturer instructions, product listings, approved plans, and local inspection requirements. Do not treat low voltage as no rules.

## Local-First Principle

**Simple**

Local-first means the house has its own brain inside the house.

If the internet goes out, the lights still work. The locks still work. The heat still works. The cameras still record. The owner is not renting the nervous system of the house from a company.

**Applied**

Use these rules:

- Core automations run locally.
- Cloud services are optional.
- Every important action has a physical fallback.
- Cameras record locally by default.
- Local controls keep working during an internet outage.
- Subscriptions are not required for basic function.
- A failed device can be replaced without rebuilding the house.

Before buying a device, ask what stops working when the cloud account is removed.

**Professional**

The local-first principle protects reliability, privacy, ownership, and long-term maintainability. A long-life concrete house should not depend on a short-life cloud product for ordinary use.

Local-first does not mean no internet. It means the internet adds remote access, software updates, weather data, notifications, and optional integrations. It does not hold the house hostage.

**Code**

Code-required functions and life-safety functions should not depend on optional consumer automation. Smoke alarms, CO alarms, egress doors, mechanical safety controls, electrical protection, and required disconnects must keep their required behavior independent of a smart-home platform.

Automation can add notification and logging, but it should not replace required safety systems.

## Network Rack, Hub, And Controller

**Simple**

The network rack is the utility room for data.

It holds the router, switches, patch panels, automation hub, camera recorder, storage, and backup power. If the rack is clean, labeled, and accessible, the smart home is much easier to fix.

**Applied**

Reserve rack space for:

- Internet modem or fiber terminal.
- Router or firewall.
- Network switch.
- Patch panels.
- PoE switch if cameras or access points need it.
- Automation controller.
- Camera recorder or local storage.
- Backup storage.
- UPS.
- Cable management.
- Ventilation and service clearance.

Label both ends of every cable before walls close.

**Professional**

The automation controller should be treated like a serviceable appliance. It needs stable power, wired network connection, backup, cooling, access, and a recovery plan. A local controller such as Home Assistant, with protocol bridges as needed, can support that direction. The final controller should be selected at build time based on support, device ecosystem, backup behavior, local control, and owner skill level.

Do not bury the brain of the house in a closet full of coats. Put it where it can be maintained.

**Code**

Electrical receptacles, equipment grounding, working space, low-voltage terminations, communications grounding, cable support, penetrations, firestopping, power-limited circuits, and equipment listings may apply to the rack area.

Network equipment should not block required electrical working space, plumbing shutoffs, mechanical access, or inspection access.

## Wired Network And Protocol Strategy

**Simple**

Wires are boring in the best way.

A wired camera does not worry about weak Wi-Fi. A wired access point gives better wireless. A wired computer is easier to trust. Wireless is still useful, but the important things should get wire when practical.

**Applied**

Use the right path for each device:

| Device Type | Preferred Direction |
|---|---|
| Cameras | Wired network where practical. |
| Access points | Wired backhaul to the rack. |
| TVs and media devices | Wired network plus spare pathway where practical. |
| Desktops and office gear | Wired network. |
| Sensors | Wired where easy, low-power wireless where wiring is not worth it. |
| Smart switches | Line-voltage switch wiring plus local automation support. |
| HVAC controls | Dedicated control wiring and manufacturer-approved interfaces. |

Pull spare pathways where future replacement would be painful.

**Professional**

The permanent design issue is not whether one protocol is fashionable. It is whether the house has enough pathway, power, separation, labels, and access for future systems.

Ethernet, Wi-Fi, Z-Wave, Zigbee, Thread, Matter, Bluetooth, proprietary lighting systems, and wired control systems each have a place. Use wired infrastructure for fixed, high-bandwidth, high-reliability devices. Use wireless for sensors, retrofit devices, and locations where wiring is not worth the damage.

**Code**

Communications circuits, power-limited circuits, remote-control circuits, coax, optical fiber, fire alarm wiring, thermostat wiring, and cable routing have code rules. Separation from power wiring matters.

Do not run low-voltage cable casually beside line-voltage conductors or through unprotected penetrations. Verify cable ratings, raceway use, firestopping, grounding, support, and outdoor transitions.

## Automation Boundaries And Manual Fallback

**Simple**

Automate chores, not survival.

It is fine for a goodnight button to turn off lights, lock doors, lower heat, and arm sensors. It is not fine if that button is the only way to lock a door or turn on a light.

**Applied**

Good automation targets:

- Goodnight scene.
- Away mode.
- Home arrival lighting.
- Leak alerts and water shutoff coordination.
- Door left open alerts.
- Exterior lighting after dark.
- Bathroom fan or ventilation boost where approved.
- Equipment runtime alerts.
- Energy dashboards.
- Filter reminders.

Avoid automation where a failure creates danger, lockout, fire risk, flooding, or blocked egress.

**Professional**

Automation should be graded by consequence. A failed accent-light scene is annoying. A failed water shutoff, lock, heat control, security state, or exhaust control can matter. The more serious the consequence, the more the system needs local operation, manual override, clear state feedback, and documented recovery.

The fail-safe principle is simple: the default state should keep people safe and able to use the house.

**Code**

Automation cannot override required safety behavior. Doors must meet egress requirements. Equipment must meet listing and manufacturer control requirements. Electrical loads must be switched by devices rated for the load. Required alarms must still function as required.

Smart controls are not a shortcut around code, listing, or inspection.

## Lighting Automation And Scene Control

**Simple**

Smart lighting is useful because it gets used every day.

The best version still feels normal. A guest should be able to walk into a room and use the wall switch without instructions.

**Applied**

Plan lighting automation around normal behavior:

- Wall switches remain primary controls.
- Dimmers are selected to match the load.
- Neutral conductors and box depth are planned before rough-in.
- Motion control is used in closets, pantry, utility areas, halls, and selected bathrooms where it makes sense.
- Night lighting stays low and simple.
- Scenes are optional, not required for basic use.
- Every switch and scene is labeled in the documentation.

Do not make ordinary lighting depend on a phone app.

**Professional**

Smart switches are often better infrastructure than smart bulbs because they preserve the wall-control habit and keep basic operation local. Smart bulbs have a place for color, lamps, specialty rooms, and accents, but they can create confusion if people cut power at the wall.

Scene design should be practical: morning, evening, movie, cooking, cleaning, goodnight, away, and path lighting. Fewer good scenes beat a giant list nobody uses.

**Code**

Switches, dimmers, neutral conductors, box fill, load ratings, luminaire compatibility, closet lighting, wet-location fixtures, energy requirements, and required lighting outlets must follow the adopted electrical code and product listings.

Use smart devices only where they are listed for the load and installation method.

## Security, Cameras, And Privacy

**Simple**

Cameras should protect the house without turning the house into a spying machine.

The best default is local recording, clear camera locations, no cameras in private rooms, and audio off unless the legal and privacy questions are answered.

**Applied**

Plan cameras by purpose:

| Area | Purpose |
|---|---|
| Front entry | See visitors, deliveries, and entry activity. |
| Back and side entries | See door activity and approach paths. |
| Driveway | See vehicles and arrival patterns. |
| Perimeter | See movement around the building. |
| Utility areas | See equipment or service areas if useful. |
| Interior | Avoid unless there is a clear reason. |

Use local storage where practical. Mask neighbor areas. Document camera fields of view.

**Professional**

Security design should separate detection, recording, alerting, response, and privacy. Cameras are not a complete security system. Door sensors, window sensors, motion sensors, sirens, lighting, access control, good doors, good locks, and good habits all matter.

Local NVR or local recording software fits the book's philosophy. Cloud recording may be convenient, but it adds subscription risk, privacy exposure, outage dependency, and vendor lock-in.

**Code**

Camera installation touches electrical supply, low-voltage wiring, exterior penetrations, weather ratings, mounting, ladder safety during installation, and possibly privacy or recording laws.

Do not make legal claims about audio recording, neighbor views, monitoring, signs, or police response until the applicable laws and local rules are checked.

## Access Control And Locks

**Simple**

A smart lock is convenience. A real lock is security.

The door should always have a safe way out from the inside and a reliable way in for the owner.

**Applied**

Use layered access:

- Mechanical key backup.
- Durable exterior lock hardware.
- Smart access only where useful.
- Temporary codes for guests or service people.
- Clear code deletion process.
- Battery replacement schedule.
- Off-site emergency key plan.
- Manual unlock from inside.

Never let an app become the only way to enter or exit.

**Professional**

Smart locks should be evaluated by mechanical quality, local integration, battery behavior, weather exposure, code-safe egress, logging, update history, and fallback path. A retrofit smart motor over a quality deadbolt can preserve the mechanical key system while adding automation.

Access control also includes garage doors, gates, home office locks, equipment rooms, safes, and network-room access. Each one needs a different risk level.

**Code**

Egress doors and interior door operation are code-sensitive. Required exits must be openable from the inside as required. Electronic locks, access-control devices, delayed egress, keypads, and smart deadbolts need careful review if they affect required exit behavior.

Use listed hardware and verify the adopted code before adding locks that change egress.

## Audio, Video, Intercom, And Dashboards

**Simple**

Audio and video are comfort systems.

They should be easy to use, easy to mute, and easy to replace when technology changes.

**Applied**

Plan media locations before rough-in:

- TV walls.
- Speaker zones.
- Desk and office locations.
- Outdoor listening areas.
- Doorbell chime or intercom locations.
- Wall dashboard locations if used.
- Conduit or pathway from display to cabinet.
- Network drops.
- Power outlets.
- Local storage or media server if used.

Do not trap a display cable inside a finished concrete wall with no replacement path.

**Professional**

Whole-house audio, home theater, intercom, dashboards, and media servers should stay modular. The speakers, cables, boxes, conduits, rack space, and network are the durable part. Receivers, streaming boxes, displays, voice devices, and software will change faster.

Centralized AV distribution can be powerful but can also become expensive and underused. Many households are better served by good network drops, local media storage, and simple room-level equipment.

**Code**

Speaker wire, communications cable, coax, fiber, HDMI extenders, in-wall rated cables, equipment power, wall-mounted displays, outdoor speakers, penetrations, and low-voltage separation must follow code and product listings.

Use in-wall rated cable where cable is inside walls. Do not run ordinary patch cords inside building cavities.

## Energy, Water, And Equipment Monitoring

**Simple**

Monitoring helps the house tell you when something is wrong.

If power use jumps, water flows when nobody is using water, or the heat pump runs too long, the house should make that visible.

**Applied**

Useful monitoring targets:

- Whole-house electricity.
- Major electrical loads.
- Solar production if installed.
- Battery or backup-power status if installed.
- Water flow.
- Leak sensors.
- Well, pump, or pressure equipment if used.
- HVAC runtime.
- Indoor temperature and humidity.
- Outdoor conditions.
- Filter and maintenance reminders.

Monitoring should lead to action, not just graphs.

**Professional**

Energy and water monitoring are diagnostic tools. They can catch leaks, failing equipment, stuck pumps, abnormal HVAC runtime, unexpected standby loads, freezer problems, and user behavior issues.

The permanent design concern is safe installation, service access, sensor accuracy, local data retention, useful dashboards, alert thresholds, and long-term trend storage. Do not overload the owner with alarms that do not require action.

**Code**

Energy monitors, current transformers, panel-installed devices, water shutoff valves, flow meters, leak sensors, pump controls, and equipment integrations must follow electrical, plumbing, mechanical, listing, and manufacturer requirements.

Panel work belongs on the approved electrical path. Do not add current sensors or monitor wiring inside a panel casually.

## Voice Control And Smart Appliances

**Simple**

Voice control can be convenient. It can also be creepy.

Use it where it helps. Do not put microphones where privacy matters more than convenience.

**Applied**

For voice control, decide:

- Local or cloud voice processing.
- Which rooms get microphones.
- Which rooms never get microphones.
- Physical mute switch.
- Wake word behavior.
- Guest behavior.
- What commands are allowed.
- What commands are blocked for safety.
- What still works without voice.

For appliances, buy the appliance first. Treat the smart feature as extra.

**Professional**

Local voice control fits the project philosophy better than cloud-first assistants, but it needs more setup and maintenance. Cloud assistants are easier but create privacy, outage, and vendor-risk concerns. A hybrid approach can work if the private spaces and critical functions stay protected.

Smart appliances should be judged by primary function, serviceability, repair parts, local operation, cloud dependency, support life, and actual use. A dishwasher notification may be useful. A refrigerator that needs a cloud account to do basic tricks is not infrastructure.

**Code**

Voice control and appliance integrations must not create unsafe remote operation. Cooking appliances, heating equipment, locks, alarms, garage doors, gates, pumps, and motorized devices need manufacturer-approved control methods and safe default behavior.

Remote start, delayed start, and unattended operation should be verified against product instructions and applicable safety rules.

## Network Security And Data Boundaries

**Simple**

Every smart device is a little computer. Some little computers are badly built.

Do not let a cheap plug, camera, or appliance sit on the same open network as banking, work files, family photos, and private data.

**Applied**

Use security basics:

- Change default passwords.
- Use a password manager.
- Keep network gear updated.
- Separate guest devices.
- Separate cameras where practical.
- Separate unknown smart devices where practical.
- Disable cloud access when not needed.
- Use VPN for remote access where appropriate.
- Back up the automation controller.
- Document admin accounts.

Make the secure path the normal path.

**Professional**

Network segmentation is a core design feature, not a hobby detail. A main network, guest network, camera network, IoT network, and management network can reduce blast radius if a device is compromised. The exact VLAN and firewall design should match the router, owner skill level, support plan, and device requirements.

Security also includes update policy, credential rotation, local backups, incident response, physical rack security, DNS filtering, log review, and a way to quarantine a device quickly.

**Code**

Most network-security work is not building code. It can still affect safety and privacy when cameras, locks, alarms, gates, pumps, heating controls, and monitoring systems are connected.

Do not expose local dashboards, cameras, locks, or controls directly to the public internet. Use a verified remote-access method and document it.

## Backup Power, UPS, And Resilience

**Simple**

The smart home needs a small battery backup.

When the power flickers, the network should not crash, the hub should not corrupt its storage, and the cameras should not go blind immediately.

**Applied**

Put backup power on:

- Router or firewall.
- Network switch.
- PoE switch for cameras and access points if used.
- Automation controller.
- Camera recorder.
- Local storage.
- Internet equipment.
- Security panel if separate.

Record what stays on, how long it should last, and what shuts down first.

**Professional**

UPS design should match load, runtime target, graceful shutdown, surge protection, ventilation, battery replacement, monitoring, and replacement access. It is separate from whole-house backup, but it should coordinate with solar, battery, generator, transfer equipment, and critical circuits if those are used.

The system should survive brief outages cleanly and fail gracefully during long outages. Manual systems must still work after the rack shuts down.

**Code**

UPS units, batteries, rack power, surge protection, branch circuits, equipment listings, ventilation, working space, and backup-power interfaces must follow the adopted code and manufacturer instructions.

Do not build homemade battery or UPS systems into the house wiring unless they are designed, listed, permitted, and inspected correctly.

## Commissioning, Documentation, And Maintenance

**Simple**

A smart home that is not documented becomes a puzzle.

Label the wires. Name the devices clearly. Write down how to restart the system. Keep a backup.

**Applied**

Document:

- Rack layout.
- Cable labels.
- Patch panel map.
- Wi-Fi names and purpose.
- Device list.
- Automation list.
- Alarm zones.
- Camera fields of view.
- Access codes and who owns them.
- Backup method.
- UPS battery date.
- Update schedule.
- Recovery steps.

Test the system before move-in and after major updates.

**Professional**

Commissioning should verify manual fallback, local operation, internet-out behavior, power-failure behavior, camera recording, sensor response, alarm states, lock behavior, HVAC integration, lighting scenes, energy monitoring, backups, remote access, and dashboard accuracy.

Maintenance should be boring: update, back up, test, replace batteries, review accounts, check logs, test UPS, clean cameras, verify sensors, and retire old devices.

**Code**

Final approval may involve electrical, low-voltage, alarm, mechanical, plumbing, energy, exterior penetrations, and equipment-listing issues depending on what is installed.

Automation is not finished when the dashboard looks nice. It is finished when the house works locally, safely, privately, and predictably.
