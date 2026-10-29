# Chapter 11 — Smart Home and Network Systems

*A local brain, not a rented one — the house works even when the internet doesn't*

This chapter covers the digital nervous system of the house: home automation, security, cameras, access control, audio/video distribution, energy monitoring, and the philosophy that binds them all together.

The guiding philosophy: **local-first, cloud-optional**; **every automation has a manual fallback**; **the house doesn't depend on any company staying in business**; **privacy is default, data stays at home**; **the smart layer enhances the house but never becomes the house**.

---

## 11.1 The Local-First Principle

**Plain language:** Most "smart homes" today are rented services — the lights work because a company's servers are running somewhere, the thermostat talks to the cloud before it talks to the furnace, the doorbell sends video to a stranger's data center. This design rejects that model. Every smart feature runs on a computer inside this house. If the internet dies, if a company goes bankrupt, if someone in Silicon Valley decides to sunset a product, the house keeps working. The owner owns the brain.

**Technical detail:** Core principles:

- **Every core automation runs on a local server** inside the house — no dependency on any cloud service for the house to function
- **Every smart device works when the internet is out** — light switches still turn on lights, thermostats still heat rooms, locks still lock
- **Every smart device has a physical fallback** — a wall switch, a mechanical override, a key — smart features are additive, not replacements
- **Data stays at home** — camera footage, energy usage, presence data, all stored locally; cloud backup is optional and encrypted
- **No manufacturer can brick the system** — if one vendor disappears, their devices can be replaced, the automation logic stays
- **Open protocols preferred** over proprietary — Matter, Z-Wave, Zigbee, MQTT, HTTPS APIs are the preferred bindings, not manufacturer-specific cloud APIs
- **The house should still function at a basic level with the smart layer completely removed** — every room has manual controls, every system has manual overrides, every door has a key

**Why this matters:**
- **Cloud services get sunset regularly** — Nest Revolv, Iris by Lowes, Insteon, Wink, Staples Connect, Google Works-with-Nest, Amazon Halo, many more — each left paying customers with dead hardware
- **Internet outages are real** — rural Oregon sees weather-driven internet outages multiple times per year; in urban areas, ISP failures happen monthly
- **Data privacy matters** — cloud cameras mean the home's video feeds live on someone else's servers, subject to breach, subpoena, or policy change
- **Monthly fees compound** — subscription services for smart home features add up to hundreds of dollars per year indefinitely
- **A 1000-year house shouldn't depend on a 10-year service** — the philosophy alignment forces a local-first architecture

---

## 11.2 Hub Architecture

**Plain language:** The house has a small, dedicated server — a computer about the size of a book — that runs the automation software. This server is the "brain" that connects all the smart devices together and decides when the lights turn on, when the heat goes up, when the security camera records. The server lives in the basement network closet, sips a trickle of electricity, and runs open-source software the owner can inspect and modify.

**Technical detail:** Smart home hub design:

**Hardware:**
- **Dedicated small-form-factor server** — Intel NUC, Minisforum, Beelink, or purpose-built (Home Assistant Yellow, Home Assistant Green)
- **Specifications:** 8+ GB RAM, 250+ GB SSD, quad-core processor, low power (15–35W idle)
- **Mounted in the network rack** with the switching and patch panel (see the low-voltage and networking discussion in the Electrical Power and Lighting chapter)
- **UPS backup** for graceful handling of power outages (see the backup power discussion)
- **Ethernet-connected** (not WiFi) to the core switch for maximum reliability
- **Redundant backup** — nightly image backup to a NAS (Network-Attached Storage) also in the rack

**Software — primary recommendation: Home Assistant:**
- **Open-source, locally-installable, no cloud dependency** for core functionality
- **Massive integration library** — 2,500+ integrations for virtually every smart device brand
- **Active community** — both user community for help and developer community for ongoing improvement
- **Backed by a foundation** (Open Home Foundation) rather than a single company — less vendor risk
- **Runs on dedicated hardware or as a virtual machine** on a general-purpose server
- **Updated approximately monthly** — user-controlled update pacing

**Software — alternatives:**
- **Hubitat Elevation** — local-first, commercial hardware, simpler than Home Assistant but less flexible
- **openHAB** — open-source, more technical, less user-friendly
- **Home Assistant is the strong default** for this design due to ecosystem breadth and community size

**Why NOT the common alternatives:**
- **Amazon Alexa hub / Echo** — cloud-dependent, Amazon-locked, limited local control
- **Google Home / Nest Hub** — cloud-dependent, Google-locked
- **Apple HomeKit** — Apple-locked (no Android access), limited integrations, some local control but weaker than Home Assistant
- **SmartThings** — Samsung-locked, cloud-dependent for major features, historically unstable through acquisitions

**Secondary hubs (bridge devices to specific protocols):**
- **Z-Wave stick / USB controller** (Zooz ZST10 700, Aeotec Z-Stick 7) — connects Home Assistant to Z-Wave devices
- **Zigbee coordinator** (SkyConnect, ConBee II, Sonoff Zigbee 3.0) — connects Home Assistant to Zigbee devices
- **Matter controller** — Home Assistant has native Matter support as of 2023; this is the future-facing protocol
- **Thread border router** — increasingly built into smart home hubs and devices; bridges Thread to other networks
- **Proprietary bridges as needed** — Lutron Caseta Smart Bridge Pro for Lutron switches, Philips Hue Bridge for Hue lights, etc. — each bridge lives in the rack

**Multiple hubs coexist:**
- **One server running Home Assistant** as the primary brain
- **Multiple radio sticks** plugged into the server for different protocols
- **Proprietary bridges** on the network where a specific ecosystem is chosen (Lutron for scene lighting, for example)
- **All reporting to and controllable from Home Assistant** as the unified interface

---

## 11.3 Communication Protocols

**Plain language:** Smart devices talk to the hub using different "languages" (protocols). Some are wired (most reliable), some are wireless. Each protocol has strengths — Z-Wave is great for battery-powered sensors, Zigbee for light bulbs, WiFi for cameras, ethernet for anything that doesn't move. This design uses whichever protocol is right for each job, and the hub translates between them.

**Technical detail:** Protocol selection by device type:

**Ethernet (wired) — highest reliability, preferred wherever possible:**
- **Used for:** security cameras (PoE), network equipment, wireless access points, TVs, computers, home audio equipment, smart home hub itself
- **Pros:** no interference, no battery, no range issues, encrypted, high bandwidth
- **Cons:** requires cable pulls (mitigated by the Electrical Power and Lighting chapter's comprehensive Cat6A infrastructure)
- **Preference:** use ethernet whenever a device is stationary and hardwiring is feasible

**WiFi — convenience, common for most "consumer" smart devices:**
- **Used for:** phones, tablets, streaming devices, some smart plugs, some smart appliances
- **Pros:** ubiquitous, no separate hub for many devices, easy setup
- **Cons:** consumes WiFi bandwidth, security concerns (devices on WiFi get internet access by default), battery devices drain quickly on WiFi
- **Best practice:** isolated "IoT VLAN" (virtual LAN) that segregates smart devices from the main network — they can talk to the hub but not to each other or to the internet without permission
- **Preference:** use for devices that need internet access or high bandwidth (streaming, cameras if not wired), avoid for simple on/off devices

**Z-Wave — low-power wireless mesh, preferred for switches, sensors, locks:**
- **Used for:** wall switches, motion sensors, door/window sensors, leak sensors, door locks, some thermostats
- **Pros:** low power (sensors run years on a battery), mesh network (each mains-powered device extends range), no WiFi interference, strong encryption, interoperable across brands
- **Cons:** slower than WiFi for data-heavy tasks, requires Z-Wave controller, limited bandwidth
- **Ideal for:** the "invisible infrastructure" — sensors and switches that never need to stream video or transfer files
- **Preference:** use for battery-powered sensors and wall-mounted switches

**Zigbee — similar to Z-Wave, popular for bulbs:**
- **Used for:** smart bulbs (Philips Hue, IKEA Tradfri), some motion sensors, some plugs
- **Pros:** low power, mesh, inexpensive, similar ecosystem to Z-Wave
- **Cons:** operates in 2.4 GHz, potential interference with WiFi; less encryption standardization than Z-Wave
- **Preference:** use for smart bulbs where dimmable smart switches aren't practical; lower priority than Z-Wave overall for this design

**Thread — emerging mesh protocol, basis of Matter:**
- **Used for:** increasingly all categories of smart home device as Matter adoption grows
- **Pros:** IP-based (compatible with general networking), low-power, mesh, multi-vendor
- **Cons:** newer ecosystem (2023+), smaller device catalog than Z-Wave/Zigbee in 2026
- **Preference:** watch this space — by the time this house is built, Thread/Matter may be the dominant smart home protocol

**Matter — application-layer standard on top of Thread and WiFi:**
- **Not a radio protocol but a "language" that devices from different brands speak**
- **Backed by:** Apple, Google, Amazon, Samsung, hundreds of device manufacturers
- **Pros:** true vendor-independence, local control by design, forward-looking
- **Cons:** new, still maturing, not every existing device supports it
- **Preference:** strongly prefer Matter-compatible devices for new purchases

**Bluetooth / Bluetooth LE — short range, device-specific:**
- **Used for:** phone-based proximity (smart locks, speakers), some sensors, some thermostats
- **Pros:** very low power, widely supported in phones
- **Cons:** short range (~30 ft), one-at-a-time pairing, limited automation use
- **Preference:** avoid as the primary protocol for anything; OK as a secondary channel

**Proprietary radio (Lutron ClearConnect, Insteon, etc.):**
- **Used for:** specific premium ecosystems (Lutron Caseta, Lutron RadioRA)
- **Pros:** rock-solid reliability, excellent response time, purpose-built
- **Cons:** vendor-locked, premium cost, requires a proprietary bridge
- **Preference:** acceptable for a key system (Lutron is widely used for professional lighting control) — understand the vendor lock before committing

**Protocol stack summary for this design:**

| Category | Primary Protocol | Secondary |
|---|---|---|
| Wall switches and dimmers | Z-Wave or Lutron Caseta | — |
| Smart bulbs | Zigbee (Hue) | Matter as available |
| Motion and occupancy sensors | Z-Wave | Zigbee |
| Door / window sensors | Z-Wave | Zigbee |
| Door locks | Z-Wave | Matter |
| Security cameras | Ethernet (PoE) | — |
| Thermostats / HVAC controls | Wired (see the HVAC, Ventilation, and Air Quality chapter) | Z-Wave fallback |
| Smart plugs | Z-Wave | Matter |
| Water leak sensors | Z-Wave | — |
| Smoke / CO | Hardwired (see the Electrical Power and Lighting chapter) | Z-Wave for app notifications |
| Voice control | Local (see the voice-control discussion) | — |
| Energy monitoring | Wired or WiFi | — |
| Home audio | Ethernet | — |

---

## 11.4 What to Automate — and What NOT to Automate

**Plain language:** Automation is a tool, not a goal. Some tasks are dramatically improved by automation — like turning off all the lights at bedtime, or notifying you when a door is left open, or adjusting the thermostat based on occupancy. Other tasks are fine manual — like operating the blinds, turning on the stove, or playing music. The design automates what genuinely benefits from it and leaves the rest alone.

**Technical detail:** Automation priority tiers:

**Tier 1 — High-value automations (do these first):**

- **"Goodnight" scene** — one button or voice command turns off all lights, locks doors, arms security, sets thermostats to night mode, turns off TVs
- **"Away" mode** — triggered by the last phone leaving the geofence or manual activation — arms security, sets HVAC to away setpoints, turns off non-essential equipment, locks doors
- **"Home" mode** — triggered by first phone entering the geofence — pre-cools or pre-heats to comfort setpoint, unlocks entry lock on arrival (optional), turns on entry lights after dark
- **Leak detection and auto-shutoff** — water leak sensors in kitchen, bathrooms, laundry, mechanical room; if any sensor triggers, a motorized valve on the main water line closes (catastrophic leak prevention)
- **Smoke / CO alarm smart notifications** — if a detector triggers, push notification to all residents' phones, text to designated emergency contact, optional audio announcement on smart speakers
- **Doorbell and intercom integration** — video doorbell streams to any indoor display or phone when pressed
- **Low-stakes security alerts** — door left open > 10 minutes, garage door still open at bedtime, window left open in rain
- **Monitoring-only automations** — energy usage dashboard, HVAC performance, water usage trends, battery levels on sensors, filter replacement reminders

**Tier 2 — Convenient automations (do after Tier 1):**

- **Automatic interior lighting** based on motion + time of day (brighter in daytime, dimmer at night, off in empty rooms after a delay)
- **Automatic exterior lighting** — on at dusk, off at dawn (photocell) or on motion after dark
- **Morning routine** — at 6 AM: slowly brighten bedroom to sunrise-matched color, unmute speakers for morning announcement, start coffee (if the coffee maker is smart), raise bedroom blinds
- **Seasonal HVAC adjustments** — summer/winter modes with different setpoints, pre-cool before the hottest part of the afternoon
- **Vacation mode** — randomizes lighting to simulate occupancy, sets HVAC to vacation setpoints, pauses mail delivery (via service integration)
- **Music scenes** — "dinner," "entertaining," "focus work" playlists and speaker groupings

**Tier 3 — Nice-to-have automations (optional):**

- **Room scene control** — multi-button keypads for "reading," "movie," "party" scenes in the living room
- **Voice-controlled task automation** — "start the dishwasher," "close the blinds" (requires specific hardware support)
- **Appliance-specific integration** — refrigerator inventory tracking, oven preheat-on-arrival, laundry-done notifications
- **Garden/irrigation automation** — (if irrigation system is installed) soil-moisture-based watering

**What NOT to automate:**

- **Cooking appliances** — ranges, ovens, cooktops stay manual; automation is a fire hazard here
- **Windows for ventilation** — manual control; automated windows are a luxury not aligned with the cost/benefit
- **Interior doors** — manual; automated doors don't solve a real problem
- **Baseline lighting** — every room still has physical switches that work without automation (see the lighting automation and access-control discussions)
- **Anything safety-critical with no manual override** — the house shouldn't DEPEND on an automation working; automation assists, doesn't replace

**The "fail-safe default" rule:**
- **If the automation fails, the default state is:** lights on (visible), doors unlocked from inside (egress), HVAC running (comfort), security unarmed at home (no lockout), cameras recording locally (no data loss)
- **Never automate into a "stuck locked out" state** — automation should never be the only way to accomplish a critical action

---

## 11.5 Lighting Automation (Integrated with Electrical Power and Lighting)

**Plain language:** Lighting automation is the most commonly used smart home feature because it's directly visible and immediately useful. The design uses smart switches (not smart bulbs) as the primary approach — each wall switch is "smart" and connects to the hub, so the same light works whether the hub is up or not. Smart bulbs are used in specific places where color changing or fine control matters.

**Technical detail:** Lighting automation architecture:

**Primary approach: smart switches (not smart bulbs):**
- **Every primary room has a smart dimmer switch** replacing the standard wall switch
- **Brands:** Lutron Caseta Diva, Zooz ZEN7x series, Inovelli Blue, Shelly 1L — all Z-Wave or proprietary-local
- **Require neutral wire** (see the smart-switch wiring discussion in the Electrical Power and Lighting chapter — already planned for)
- **Deep switch boxes** (see the smart-switch wiring discussion in the Electrical Power and Lighting chapter) — accommodate the larger smart switch bodies
- **Dumb bulbs in the fixtures** — LED bulbs operate on/off and dim through the switch, no independent intelligence

**Why switches, not bulbs:**
- **The switch always works** — even if the hub is dead, the wall switch still turns on the light
- **Standard bulbs are cheaper and longer-lived** than smart bulbs
- **One switch controls multiple bulbs in a fixture** — smart bulbs require per-bulb setup
- **Guests and children intuitively use wall switches** — no retraining required

**Smart bulbs (selective use):**
- **Color-changing bulbs** (Philips Hue, LIFX) in specific rooms where color adjustment is valuable — primary bedroom for sunset matching, entertainment areas for mood lighting, children's rooms for nightlight transitions
- **On a standard wall switch that remains in the "on" position** — the wall switch is a backup only
- **Or on a smart wall remote** (Lutron Pico, Aqara switch) that sends Zigbee commands to the bulbs rather than cutting power

**Lighting scenes (programmed sets of light states):**
- **"Wake up"** — slowly brighten bedroom over 20 minutes, off elsewhere
- **"Morning"** — kitchen 80%, dining 60%, hall 40%
- **"Evening"** — living room 50% warm, kitchen 40%, accent lights on
- **"Movie"** — main lights off, accent lights 20% warm, hall sconces on low
- **"Goodnight"** — all interior off, hall nightlights on, exterior path on
- **"Party"** — everything up bright, music zones coordinated
- **"Vacation"** — randomized activity patterns matching typical occupancy

**Motion-based automation:**
- **Closets, pantry, utility rooms** — on when entered, off 3 minutes after last motion
- **Bathrooms** — on when entered (dimmer at night based on time), off 10 minutes after last motion
- **Hallways** — on to 20% when motion at night, full when motion in daytime, off after 5 min
- **Basement stairs and mechanical areas** — on with motion, off after 10 min

**Presence-based automation:**
- **House occupied** (any phone in geofence or any motion sensor active in last 30 min) → normal lighting behavior
- **House empty** (all phones out of geofence AND no motion for 30 min) → all lights off, exterior on dusk-to-dawn
- **Sleeping** (after "goodnight" scene OR between 11 PM and 5 AM with no recent motion) → interior nightlights only, exterior security lighting on motion

**Dimmer recall:**
- **Each switch remembers its last dim level** when turned on via the wall paddle
- **Automation overrides** can set the level explicitly (e.g., "Movie" scene sets living room to 20%)

**Local-first fallback:**
- **If the hub is offline, all smart switches operate as normal wall dimmers** — tap to toggle, press and hold to dim
- **Automations pause but the lights still work**

**Coordination with the Electrical Power and Lighting chapter:** every lighting circuit is dimmable (see the lighting design discussion in the Electrical Power and Lighting chapter), every switch has a neutral (see the smart-switch wiring discussion in the Electrical Power and Lighting chapter), deep boxes accommodate smart switches (see the smart-switch wiring discussion in the Electrical Power and Lighting chapter).

---

## 11.6 Security and Cameras

**Plain language:** The house has cameras at the entry points, motion sensors at doors and windows, and a security system that can be armed when away. All camera footage is stored locally on a computer in the basement — no cloud subscription, no video going to a third party. The system can send alerts to phones when needed, but the footage itself stays home.

**Technical detail:** Security system design:

**Camera hardware:**
- **Power-over-Ethernet (PoE) IP cameras** — single cable for power and data, no WiFi dependency
- **Resolution:** 4K (8 megapixel) primary cameras; 1080p minimum for secondary
- **Night vision:** IR illumination (standard on most) or true low-light color (Reolink, Hikvision ColorVu — better detail in low light)
- **Lens:** fixed 2.8 mm wide for entry coverage; 4 mm for perimeter; 6 mm for narrow fields (driveway to road, path)
- **Weatherproofing:** IP67 minimum (dust-tight, waterproof)
- **Brands:** Reolink, Amcrest, Hikvision (value), Axis, Bosch (premium) — all work with local NVR without cloud subscription

**Camera locations:**
- **Every exterior door:** one camera with view of the door and approaching path
- **Driveway entrance:** one camera with view of incoming vehicles and pedestrians
- **Each corner of the house:** coverage of the perimeter
- **Back yard primary area:** coverage of recreation/garden spaces
- **Garage or carport (if present):** interior coverage
- **Interior (optional):** front entry interior, basement storage area — entirely optional, depends on owner preference

**Total camera count for a typical install:** 6–12 exterior, 0–3 interior

**Network Video Recorder (NVR) — local recording:**
- **Dedicated NVR or software-based** — Frigate (open-source, Home Assistant integration), Blue Iris (Windows), UniFi Protect (Ubiquiti, premium), Synology Surveillance Station (NAS-based)
- **Storage:** 4–16 TB of hard drive space — stores 30–90 days of continuous footage depending on camera count and settings
- **RAID redundancy** optional — 2-drive mirror prevents single-drive failure from losing footage
- **Frigate is the strong recommendation for this design:** open-source, integrates with Home Assistant, supports object detection (person, vehicle, animal) on local hardware, no cloud dependency

**Object detection (AI):**
- **Local-only object detection** — a small accelerator (Coral TPU, NVIDIA Jetson, or the NVR's own CPU/GPU) identifies people, vehicles, animals, packages
- **Filters false alerts** — motion from trees, shadows, lighting changes don't trigger notifications
- **Frigate and similar software handle this entirely locally** — no cloud AI service

**Motion / intrusion sensors:**
- **Door/window sensors** on every exterior door and every ground-floor window
- **Motion sensors** in hallways and main rooms
- **Glass break sensors** in specific rooms with large windows
- **All on Z-Wave or wired to a central security panel**
- **Battery-powered or hardwired** depending on location

**Security panel / alarm system:**
- **Options:**
  - **DIY local:** Home Assistant with an alarm dashboard and integration with sirens and sensors — no monitoring fee
  - **Commercial local:** Konnected, DSC, Ademco panels — hardwired to sensors, can integrate with Home Assistant
  - **Commercial monitored:** traditional security companies (ADT, Vivint, local alarm companies) — monthly fee for 24/7 monitoring, cloud-dependent
- **Recommendation:** DIY local with Home Assistant for the base, professional monitoring only if desired for insurance discounts or personal reassurance

**Siren and notification:**
- **Interior siren** — 100+ dB, wired to the security system, sounds when alarm triggered
- **Exterior strobe light (optional)** — visual alert at the house exterior
- **Phone notifications** — immediate push to all residents' phones with camera snapshot
- **Text / email** — optional to designated emergency contact
- **Smart speaker audio** — "Alarm triggered on front door" announced through house audio system

**Arm modes:**
- **Disarmed** — all sensors active for monitoring, no alarm
- **Armed Stay** — perimeter sensors active (doors and windows), interior motion disabled — used when home, especially at night
- **Armed Away** — all sensors active — used when leaving the house
- **Auto-arm** — based on geofence (last phone leaves = arm away); manual arm is always available

**Remote access:**
- **Via VPN** to the home network, not cloud services
- **WireGuard VPN on the router or dedicated device** — provides secure remote access to the cameras and security system
- **Phone apps:** Home Assistant Companion app (for alerts and control), Frigate app (for camera review)

**Privacy features:**
- **Privacy masks** in camera software for specific areas (e.g., neighbor's yard should be masked out)
- **Scheduled recording pauses** — disable interior cameras when home, enable when away
- **No cloud dependency** — footage stays on the local NVR

**Key code references:**
- No specific building code for security cameras (privacy laws apply — varies by jurisdiction)
- Oregon is a "one-party consent" state for audio recording — recording audio on cameras requires one person in the conversation to consent; outdoor cameras where conversations could be captured should have audio disabled by default

---

## 11.7 Access Control

**Plain language:** Door locks are a mix of traditional keys (always work, never depend on batteries or technology) and smart locks (convenience and logging). Every exterior door has both. Interior spaces can use keypad locks for home office or gun safe access without needing a physical key for each one.

**Technical detail:** Access control design:

**Exterior doors — dual approach:**

**Primary lock — traditional deadbolt:**
- **High-quality single-cylinder deadbolt** — Medeco, Mul-T-Lock, or Schlage Primus with high-security keys
- **Bump-proof, pick-resistant, drill-resistant** cylinder
- **1-inch throw bolt into reinforced strike plate**
- **Key override** — the house always has a mechanical key backup
- **Key system:** restricted keyway (key blanks not available to the general public) so keys can't be duplicated without authorization

**Secondary lock — smart deadbolt or smart retrofit:**
- **Smart lock options:**
  - **Smart deadbolt that replaces traditional deadbolt** — Yale Assure, Schlage Encode, Kwikset Halo (WiFi) — lose key-system integration
  - **Smart retrofit (motor attached to interior thumb-turn)** — August, Level Bolt — traditional deadbolt stays, key still works, smart adds convenience
- **Recommendation for this design: Level Bolt or August retrofit** — keeps the high-security mechanical lock working with the original restricted key system, adds smart access on top
- **Z-Wave preferred** over WiFi for lock communication — lower power, local-first protocol

**Smart features used:**
- **Auto-unlock on approach** (phone geofence + proximity)
- **Auto-lock after closing** (door closes and stays closed for 1 minute → locks automatically)
- **Scheduled codes** (guest codes, service codes that expire)
- **Notification on entry** — "front door unlocked by [name]" in the home log
- **Integration with "away" and "goodnight" modes**

**Fallbacks when smart fails:**
- **Physical key always works** — kept with residents, one in a key-holder inside the house, one off-site with a trusted person
- **Keypad** (on smart locks with keypads) works with stored codes even if network is down
- **Battery replacement** every 6–12 months; low-battery notifications on app

**Interior access control:**

**Home office with sensitive equipment (optional):**
- **Keypad deadbolt** (no key required, PIN only) — Schlage BE365 or similar — dumb keypad, no smart needed
- **Or smart keypad** for logging and scheduled codes

**Safe or secure storage:**
- **Biometric + key safe** — high-security storage with fingerprint or PIN + mechanical key override
- **Wall-mounted or floor-mounted** — bolted to structure

**Garage door (if garage added later):**
- **Smart garage door opener** — MyQ, Ratgdo (open-source alternative), Shelly — WiFi or Z-Wave
- **Auto-close after X minutes if left open** (automation)
- **Status reported to home dashboard**
- **Traditional remote also works** — smart is additive

**Key management philosophy:**

**Three levels of access:**
- **Primary residents** — physical keys and full smart access, can create and delete codes
- **Family / long-term guests** — smart codes or guest phone app access, logged separately
- **Short-term guests / service** — temporary codes that expire automatically

**Key storage:**
- **Three mechanical keys to every lock**:
  - One in daily use (kept with the resident)
  - One hidden on-site (secure spot, not an obvious "hide-a-key" location)
  - One off-site (with a trusted friend or family member, or in a bank safe deposit box)
- **Code inventory kept in the home's project binder** — not written on paper near the lock, but recorded securely
- **Annual key and code audit** — review who has access, remove expired codes, replace batteries

**Key code references:**
- No specific code — locks are not regulated for residential
- ORSC R311.2 (egress — interior doors must open without a key from the inside at all times — applies to any keyed interior lock)

---

## 11.8 Audio and Video Distribution

**Plain language:** Music plays in every room, the home theater in the great room has theater-quality sound, and TVs can share content between rooms. All of this runs on the local network — no dependency on any specific streaming service, and the music doesn't stop when the internet does (because the library is stored locally).

**Technical detail:** AV system design:

**Whole-house audio:**
- **Ceiling speakers in primary living spaces** — great room, kitchen, primary bedroom, primary bathroom, home office, outdoor patio
- **Brands:** Polk, Klipsch, Sonance, JBL, Bose (for built-in) — all make quality in-ceiling speakers
- **Wiring:** 16/4 or 14/4 speaker wire from central AV rack to each speaker location, pulled during rough-in
- **Amplification:** multi-zone amplifier in the AV rack (Sonos Amp, Russound, Denon Heos Amp) — 6–12 zones typical
- **Sources:**
  - **Local music server** — Plex, Jellyfin, Roon, or custom Home Assistant media player — music library stored on the NAS
  - **Streaming services** — Spotify, Apple Music, Tidal — for current music (requires internet)
  - **AirPlay / Chromecast / DLNA** — for casting from phones
- **Control:** Home Assistant dashboard, voice (see the voice-control discussion), wall keypads (optional), phone apps

**Home theater (great room or dedicated theater room):**
- **Main display:** 85–98 inch OLED or QLED TV, wall-mounted; OR motorized projector screen with 4K projector (if dedicated theater room)
- **Surround sound:** 5.1.2 or 7.1.4 configuration (Dolby Atmos) with ceiling speakers for height channels
- **Receiver:** Denon, Marantz, Yamaha, or dedicated cinema processor
- **Sources:**
  - **4K Blu-ray player** — for physical media, best-possible quality
  - **Streaming devices** — Apple TV 4K, Nvidia Shield, Roku Ultra — wired ethernet
  - **Local media server** — Plex/Jellyfin on the NAS, for personal movie collection
  - **Game consoles** — PlayStation, Xbox, Nintendo Switch
- **HDMI routing:** HDMI cables from each source through conduit to the receiver; receiver outputs to display

**Multi-room video:**
- **If desired:** HDMI matrix switch in the AV rack distributes any source to any TV in the house
- **Wiring:** HDMI-over-Cat6 extenders at each TV location, runs back to the matrix
- **Typically overkill:** most households don't actually share sources between TVs much; streaming apps per TV is simpler

**TV locations:**
- **Great room** — primary viewing
- **Primary bedroom** — evening viewing (optional)
- **Kitchen / breakfast area** — casual viewing (optional, small TV)
- **Basement rec room** — secondary or theater

**TV wiring at every location:**
- **Dual Cat6A** (streaming + spare)
- **Coax** (cable/antenna, even if initially unused)
- **Power outlets** behind the TV mount
- **In-wall conduit from TV location to cabinet location** for future HDMI runs

**Outdoor audio:**
- **Weather-resistant speakers** in the patio / outdoor living area
- **Rock speakers (optional)** — hidden in landscaping
- **Fed from the main multi-zone amp** with dedicated outdoor zone

**Volume management and limiting:**
- **Per-zone volume limits** — kids' room maxes out at 70%, outdoor speakers cap at 85% to avoid neighbor complaints
- **Schedule-based muting** — outdoor speakers auto-mute after 9 PM
- **Integration with "goodnight" scene** — all audio ramps down and stops

**Intercom:**
- **Voice announcements through whole-house audio** — "Dinner is ready" / "Car in the driveway" / "Package delivered"
- **Video doorbell feeds into the main room displays** when the doorbell is pressed
- **Room-to-room voice intercom** via smart speakers (see the voice-control discussion)

**Key code references:**
- NEC 725 (low-voltage wiring — see the service-layer conduit discussion in the Electrical Power and Lighting chapter)
- NEC 820 (coax, if used)

---

## 11.9 Energy Monitoring

**Plain language:** The house tracks its own energy use — total electricity consumed, production from solar (when added), use by major appliances, gas usage (if any), water usage. This data shows up on a home dashboard so the owner can spot problems (a circuit using more than it should), make decisions (which appliance to replace next), and optimize (pre-cool during cheap-electricity hours).

**Technical detail:** Energy monitoring design:

**Whole-house electricity monitoring:**
- **Current transformer (CT) clamps on the main service conductors** — reads total power draw non-invasively
- **Brands:** Emporia Vue Gen 2/3, Sense, IotaWatt, Shelly EM — all reasonably priced
- **Emporia Vue** is the strong recommendation — local API, 16 circuit-level CTs, WiFi or wired, Home Assistant integration
- **Installation:** inside the main panel, CT clamps around each main feeder and around selected branch circuits

**Per-circuit monitoring (granular):**
- **Major circuits monitored individually:** heat pump, water heater, EV charger(s), range, dryer, HVAC, kitchen SA circuits, solar backfeed (when installed)
- **General circuits monitored in aggregate** — total lighting, total general-purpose outlets
- **Budget ~15–20 CT clamps** for thorough monitoring

**Solar monitoring (when installed):**
- **Inverter data** (Enphase, SolarEdge, or string inverter) provides production data directly
- **Integration with Home Assistant** for dashboard visibility
- **Net usage calculation** — production minus consumption, per hour, per day

**Water monitoring:**
- **Smart water meter** or flow sensor on the main water line
- **Brands:** Flume (cellular, cloud-dependent — not preferred), Flo by Moen (WiFi, cloud), or a dumb pulse meter integrated with Home Assistant (preferred local option)
- **Detects leaks** (continuous flow > 30 min indicates leak)
- **Tracks total usage** by day/month
- **Integrates with leak shutoff valve** (see the Plumbing Systems chapter) for auto-shutoff on detected leak

**Gas monitoring (if any gas appliance):**
- **Utility smart meter** typically provides daily/hourly readings (varies by utility)
- **Pulse output meter** can feed directly to Home Assistant

**HVAC performance monitoring (see the HVAC controls and monitoring discussion):**
- **Equipment runtime, efficiency, zone temperatures** logged continuously
- **Compared to expected performance** based on outdoor conditions
- **Alerts on anomalies** (runtime > 125% of expected for several hours = suspected issue)

**Display and dashboards:**
- **Home Assistant energy dashboard** shows:
  - Real-time power draw (kW)
  - Daily / weekly / monthly usage (kWh)
  - Cost (based on utility rate schedule)
  - Solar production (when installed)
  - Grid import / export
  - Per-appliance breakdown
  - Carbon footprint (if desired)
- **Mobile access** via Home Assistant app
- **Wall-mounted dashboard tablet** (optional) in a central location

**Rate-optimized automations (future, with time-of-use rates or solar):**
- **Pre-cool / pre-heat** during low-rate or high-solar windows
- **EV charger scheduling** to charge during off-peak hours
- **Heat pump water heater scheduling** — heat water when cheap, coast during peak
- **Appliance delay** — dishwasher, dryer can start during off-peak windows

**Historical data:**
- **5+ years of hourly data stored locally** — useful for trend analysis, troubleshooting, tuning
- **Long-term storage in InfluxDB or similar** — efficient time-series database, optimized for this use

**Privacy:**
- **All energy data stays local** by default
- **Optional: upload anonymized data to the utility** for bill analysis and demand-response programs if the homeowner opts in
- **No cloud energy service required**

---

## 11.10 Voice Control — Local Options

**Plain language:** Voice control is convenient ("turn off the kitchen lights") but most voice assistants send everything you say to a cloud server owned by a big tech company. This design uses local voice recognition — the microphone picks up a wake word, processes what you said on a computer in the basement, and executes the command without any data leaving the house.

**Technical detail:** Voice control strategy:

**Local voice assistants (preferred):**

**Home Assistant Voice:**
- **Wake word: "Hey Jarvis" or custom** — runs on the smart home hub
- **Satellite devices** (small speakers with microphone) in each room — Home Assistant Voice Preview Edition, or DIY with a Raspberry Pi + microphone
- **Wake word detection on the satellite** — local, no audio transmitted until wake word
- **Speech-to-text on the central hub** — Whisper (OpenAI's open model, running locally) or faster local alternatives
- **Intent recognition and execution on the hub** — fully local
- **Text-to-speech on the hub** — Piper (local), or pre-recorded responses
- **No data leaves the house**

**Rhasspy:**
- **Open-source local voice assistant** — fully offline
- **More technical to set up** but very customizable
- **Good alternative for Home Assistant power users**

**Willow:**
- **Purpose-built local voice assistant hardware** — ESP32-based, local processing, open-source
- **Strong fit for this design's philosophy**

**Commercial (not preferred, but evaluated):**

**Amazon Alexa:**
- **Pros:** mature, many "skills" available, familiar to many
- **Cons:** all voice data to Amazon, cloud-dependent, privacy concerns, limited local control
- **Only recommended if:** Alexa is already in use and the owner values convenience over privacy

**Google Assistant:**
- **Similar trade-offs to Alexa** — cloud-dependent, Google-controlled

**Apple HomePod / Siri:**
- **More local processing than Alexa/Google** — Apple has shifted toward on-device
- **Cons:** Apple-locked, smaller smart home ecosystem, cloud for complex queries

**Recommendation for this design:**
- **Primary: Home Assistant Voice** with satellites in kitchen, living room, primary bedroom — all local
- **Optional overlay:** Apple HomePod in a living room for Apple-ecosystem features (if the household uses Apple devices heavily) — acknowledged privacy trade-off for convenience
- **Avoid:** always-listening cloud devices in private spaces (bedroom, bathroom)

**Wake word considerations:**
- **"Hey Jarvis"** — common in Home Assistant Voice
- **Custom wake words** — can be trained
- **No wake word (push-to-talk)** — maximum privacy, less convenient

**Commands supported (examples):**
- "Turn off all lights"
- "Set the bedroom to 70 degrees"
- "Goodnight" (triggers the scene)
- "What's the temperature outside?"
- "Lock the front door"
- "Play jazz in the kitchen"
- "Start the dishwasher" (if integrated smart dishwasher)

**Microphone placement:**
- **One satellite per major room** — kitchen counter, living room side table, primary bedroom nightstand, home office
- **Not in bathrooms** (privacy, humidity)
- **Not in basement** (rarely needed, reduces false wakes)

**Mute / privacy:**
- **Physical microphone mute switch** on every satellite — disables the microphone completely when desired
- **Schedule-based muting** — microphones off during private hours (e.g., 10 PM – 7 AM) unless manually activated
- **Wake-word-only activation** — no recording until wake word is detected

---

## 11.11 Smart Appliances — Evaluation Framework

**Plain language:** Refrigerators, washers, dryers, dishwashers, and other major appliances increasingly come with "smart" features. Some of these are actually useful. Many are just marketing. The design uses smart features when they genuinely help and ignores them when they don't.

**Technical detail:** Smart appliance decision framework:

**Worth-it smart features:**

- **Remote start / delay start** (dishwasher, washer, dryer, oven) — useful for time-of-use rate optimization or starting a load while away
- **Completion notifications** (laundry, dishwasher, oven) — phone alert when cycle is done, avoids forgetting a load or overcooking
- **Status checking** (refrigerator temp, oven preheat status, laundry cycle time remaining) — legitimate convenience
- **Energy use reporting** — per-appliance energy data
- **Preheating from away** (oven, sous vide equipment) — genuine time-saver

**Marginal smart features:**

- **Refrigerator inventory tracking** — usually requires manual entry or cameras; rarely worth the complexity
- **Grocery reordering from the refrigerator** — vendor lock-in, subscription dependencies
- **Recipe suggestions on a screen in the fridge** — a phone does this better
- **Cooking assistance ("use 3 cups flour, now add eggs")** — phone/tablet does this better

**Not-worth-it smart features:**

- **Voice control of the appliance via its own assistant** — redundant if a whole-house voice system exists
- **Social sharing of cooking or laundry** — irrelevant
- **Cloud-dependent features that stop working when the appliance's support ends** — major risk

**Evaluation framework (apply to any smart appliance purchase):**
1. **What does the smart feature DO that's valuable?** — if the answer is vague, skip
2. **Does it require cloud connection?** — if yes, does the appliance still work fully without the cloud?
3. **What's the support timeline?** — how long will the manufacturer maintain the smart features?
4. **Can it integrate with Home Assistant / local automation?** — if yes, it fits the design; if no, it's a silo
5. **Does it add cost vs. the non-smart equivalent?** — is the added cost justified by the added value?

**Recommended smart appliances (2026 assessment):**

- **Heat pump water heater with WiFi** — for monitoring, scheduling, and energy optimization (Rheem, AO Smith, Stiebel Eltron all have good options)
- **Induction cooktop (any brand)** — smart features usually marginal; reliability and responsiveness matter more
- **Dishwasher with delay start and notifications** — Bosch 800 series, Miele have good implementations
- **Washer and dryer with monitoring** — LG, GE, Samsung all offer; cloud dependencies vary
- **Refrigerator with basic monitoring** — temperature alerts are useful; screen-in-door features usually not
- **Smart smoke/CO detectors** — First Alert Onelink, Nest Protect; works with Home Assistant via integrations

**Key principle:** the appliance does its primary job well first; smart features are secondary.

---

## 11.12 Network and System Security

**Plain language:** A smart home is only as secure as its weakest device. Cheap smart plugs from unknown manufacturers have been found to expose the entire home network. The design segregates smart devices onto their own network so that even if one is compromised, the important data (computers, phones, cameras) stays separate.

**Technical detail:** Network security design:

**VLAN segmentation (Virtual LANs):**
- **Main network (VLAN 10)** — computers, phones, tablets, primary devices — full internet access
- **IoT network (VLAN 20)** — smart home devices, appliances, lights, plugs — internet access blocked by default, only specific allowed services
- **Camera network (VLAN 30)** — security cameras only — no internet access, only talks to the local NVR
- **Guest network (VLAN 40)** — for visitors — internet only, no access to local devices
- **Management network (VLAN 99)** — network equipment management — isolated, admin-only

**Firewall rules:**
- **Default deny** between VLANs — devices can't cross networks without explicit rules
- **IoT VLAN can talk to Home Assistant hub** (specific port, specific IP) — needed for control
- **IoT VLAN cannot talk to main VLAN devices** — a compromised smart plug can't attack computers
- **Cameras cannot talk to the internet** — prevents exfiltration even if a camera is compromised
- **Outbound filtering on IoT devices** — only specific manufacturer update servers allowed, nothing else

**Password and credential management:**
- **Unique strong password for every device** — no reused passwords
- **Password manager** (Bitwarden self-hosted, 1Password, KeePass) — stores all device credentials
- **Default admin passwords changed** on every device — this is the #1 security failure in smart homes
- **Two-factor authentication** enabled on every account that supports it
- **Local-only accounts** where cloud accounts aren't required

**Device firmware:**
- **Automatic firmware updates** on security-critical devices (router, firewall, network switch, NAS)
- **Manual firmware updates** on smart devices (read release notes first — sometimes updates break functionality)
- **Quarterly firmware review** — check all devices for outdated firmware as part of maintenance

**Physical security:**
- **Network rack secured** in the basement, inside a room that can be locked
- **Hub and NAS not exposed to public areas** of the house
- **Ethernet ports in public areas** (guest rooms, outdoor) on guest VLAN by default

**Incident response:**
- **Detection:** network monitoring software (PiHole for DNS monitoring, Firewalla for traffic, Security Onion for advanced detection) — alerts on unusual activity
- **Isolation:** suspected compromised device can be quickly moved to a quarantine VLAN or powered off
- **Remediation:** factory reset the device, change all credentials, review firewall logs

**Key code references:**
- No specific building code — this is digital hygiene
- GDPR, CCPA (privacy laws) — apply to data handling; a local-first approach minimizes exposure

---

## 11.13 UPS, Backup Power, and Resilience

**Plain language:** When the power goes out — common in rural Oregon during storms — the core systems should keep running for at least a few hours. The network, the hub, the security system, and enough lights to navigate should all stay up on battery backup. This isn't the same as whole-house backup (that's for solar/battery in a later phase) — this is just making sure the smart brain doesn't fall asleep when the lights flicker.

**Technical detail:** UPS and resilience design:

**Critical systems UPS (Uninterruptible Power Supply):**
- **Rack-mount UPS** in the network closet — 1500VA or 2200VA
- **Protects:** network switch, internet modem/router, Home Assistant hub, NVR, NAS, main access point
- **Runtime target:** 2–4 hours at full load (or 8+ hours at reduced load with unneeded devices spun down)
- **Brands:** APC Smart-UPS, CyberPower, Eaton — network-managed UPS with USB or SNMP reporting
- **Home Assistant integration** — UPS status visible in dashboard, automations can trigger based on grid-loss state

**Security system UPS:**
- **Security panel has integrated battery backup** (standard) — 24+ hour runtime
- **Cameras:** PoE switch on UPS — cameras stay up as long as the switch does
- **Door locks:** smart locks have their own batteries — months of standalone runtime

**Smart hub UPS:**
- **Hub on primary rack UPS** — stays up with network
- **Graceful shutdown** at low battery — hub saves state before powering off
- **Automatic restart** when power returns

**Backup power beyond UPS (deferred to future phase):**

- **Solar + battery system** (see the solar provisions discussion in the Electrical Power and Lighting chapter) — when installed, provides hours-to-days of grid-independent operation
- **Standby generator** (natural gas or propane) — provides indefinite operation but requires fuel service; not preferred for this design's all-electric philosophy
- **Portable battery / power station** (EcoFlow, Bluetti, Goal Zero) — flexibility, can be moved between house and vehicle

**Internet outage resilience:**
- **Cellular backup for internet** (optional) — 4G/5G router on standby, automatically takes over if primary internet fails
- **Core smart home functions work without internet** — see the local-first principle
- **Remote access via VPN fails** during internet outage — local access via wall switches, local dashboards still work

**Water outage resilience (coordinate with the Plumbing Systems chapter):**
- **Cistern storage** provides days of water independent of well pump or municipal supply
- **Smart features of water system** (leak detection, shutoff) don't require internet

**Heating outage resilience:**
- **Wood stove (optional, see the combustion-appliance discussion)** — heats in power outage
- **Passive solar gain** — the envelope is thermally massive; a cold snap + power outage doesn't immediately freeze pipes
- **Backup heat** — small resistance heater if the heat pump fails, manual control

**Resilience tiers:**

| Outage Duration | System Status |
|---|---|
| < 5 minutes | UPS covers — no impact |
| 5 min – 4 hours | Rack UPS covers; main power systems down but smart layer functional |
| 4 – 24 hours | Rack UPS depleted; smart hub down; manual systems functional |
| 1 – 3 days | House habitable (thermal mass), water available (cistern), limited lighting (battery lanterns) |
| 3+ days | Consider generator, solar battery, or evacuation |

**Testing:**
- **Quarterly UPS test** — disconnect utility, verify runtime
- **Annual full resilience test** — power off main breaker for an afternoon, verify every expected system stays up
- **Documentation** of runtime, issues, and improvements

---
