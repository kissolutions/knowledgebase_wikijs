---
title: Enclosed Office Lighting Controls Playbook
description: 
published: true
date: 2026-03-02T00:01:05.558Z
tags: lighting controls, playbook, enclosed office, office
editor: markdown
dateCreated: 2026-01-11T21:24:05.224Z
---

# Enclosed Office Lighting Controls — Design Playbook

<!--
DESIGN PLAYBOOK
Domain: Lighting Controls
Space Type: Enclosed Office (Private Office)
Primary code baseline: IECC 2015+ occupant sensor control required for private/enclosed offices (verify local adoption & amendments).
-->

## 1. Purpose and Use

<!-- ANCHOR: PURPOSE -->

This Design Playbook defines **how KIS Solutions designs lighting controls for enclosed offices** (private offices) under common commercial project constraints and energy-code requirements.

This playbook is used to:
- Provide a clear, defensible **starting point** for enclosed office lighting controls so designers are not starting from a blank page
- Help designers make early decisions that account for **energy code triggers**, daylight zones, and realistic coordination constraints
- Reduce redesign caused by late discovery of **controls requirements**, sensor coverage issues, or receptacle-control scope
- Produce consistent, reviewable outcomes across projects and engineers

This playbook is prescriptive. It documents **organizational defaults and judgment**, not an exhaustive catalog of options.

This playbook intentionally does **not** explain hardware fundamentals (sensor technologies, power packs, etc.). Those live in linked reference pages.

---

## 2. Design Intent

<!-- ANCHOR: DESIGN INTENT -->

The design intent for enclosed office lighting controls prioritizes:
- **Code compliance that remains valid even when the project changes**, such as during value engineering, contractor substitutions, or minor layout revisions
- Predictable occupant experience (avoid nuisance shutoff and confusing behavior)
- Commissioning success with minimal tuning burden
- Documentation clarity that survives bid delivery and limited CA

This playbook deliberately does *not* optimize for:
- Advanced “scene” programming for a single user
- Highly customized or project-specific control sequences that require detailed programming, tuning, or ongoing oversight to function correctly

<!-- ANCHOR: ESCALATION NOTE
Higher performance requirements = exit playbook and write a project-specific controls narrative.
-->

---

## 3. Space Type Definition (Decision-Oriented)

<!-- ANCHOR: SYSTEM DEFINITION -->

An **enclosed office** is a fully enclosed, room-based office space intended for one (or a few) occupants, typically with a door and full-height walls.

> For deeper classification context and edge cases, see:
> **[Interior Space Types → Enclosed Office](../interior-space-types#enclosed-office)**

---

## 4. Constraint Envelope

<!-- ANCHOR: CONSTRAINT MODEL -->

The enclosed office lighting control design must respond to the requirements of the **adopted energy code family**. These code families are largely independent; where a jurisdiction has adopted multiple, the *most stringent* applicable requirements govern.

This section branches into:

- **4.A IECC — International Energy Conservation Code**
- **4.B ASHRAE 90.1 — ANSI/ASHRAE/IES Energy Standard**
- **4.C Title 24 — California Energy Code**
- **4.D Automatic Receptacle Control Considerations**
---

### 4.A IECC — International Energy Conservation Code

#### Hard Constraints (Occupancy Sensor Controls)
Energy codes based on IECC (2015, 2018, 2021, 2024) require **occupancy sensor control** in enclosed office spaces. Specific requirements vary slightly by edition:

- **Auto-OFF timeout**
  - **IECC 2015:** sensors must shut lighting OFF within **30 minutes** of vacancy.
  - **IECC 2018 and later:** sensor must shut lighting OFF within **20 minutes** of vacancy.
- **Manual-ON vs Auto-ON**
  - Where auto-ON is used, the lights may come ON to no more than **50%** of full lighting power unless occupant-initiated (manual ON). Manual-OFF is required.
- **Daylight-responsive control**
  - When lighting in a daylight zone exceeds code thresholds (IECC-defined), daylight-responsive dimming or switching is required.

#### Automatic Receptacle Control (Where Applicable)

- *IECC 2021, 2024* explicitly include **Automatic Receptacle Control (ARC)** requirements for enclosed offices
> IECC language varies by edition and adopted amendments. Always verify the specific adopted version and local amendments.
---

### 4.B ASHRAE 90.1 — ANSI/ASHRAE/IES Standard

#### Hard Constraints (Occupancy Sensor Controls)
ASHRAE 90.1 clauses (varies by edition starting around 2010/2013/2016/2019/2022) require lighting controls in enclosed offices:

- **Occupancy sensor control** is required for enclosed offices larger than a code-defined threshold (often ≥ 100 ft²).
- **Occupancy sensor controls must:**
  - Provide **manual ON** (vacancy) control
  - Provide **auto-OFF** to turn lights OFF when the space is unoccupied
  - Have an **auto-OFF timeout** (commonly 20 minutes; confirm adopted edition)
- **Daylight-responsive controls**
  - Required in spaces with ample daylight access (usually within a defined perimeter zone)


#### Automatic Receptacle Control

- In more recent ASHRAE 90.1 editions (2019/2022), **ARC-equivalent requirements** may exist. Confirm against the *specific adopted edition and any referenced addenda*.
> The specific sections are typically found in ASHRAE 90.1 Section C (Lighting) or corresponding chapters, and the precise numeric thresholds and exceptions should be verified based on the adopted edition.

---

### 4.C Title 24 — California Energy Code (CEC)
California’s Title 24 (Part 6) has its own structure and terminology, but similar control intent.

#### Lighting Control Requirements

- **Occupancy/vacancy sensors** are required in enclosed private offices.
- Title 24 typically requires:
  - **Manual ON** with optional auto-ON
  - **Auto-OFF** timeouts (often 15–20 minutes depending on Title 24 cycle)
  - **Daylight dimming** on perimeter offices where daylight zones apply

#### Receptacle and Plug Load Controls

- Title 24 may have separate provisions for **receptacle/plug load controls** in office spaces.
- These requirements are not always parallel to IECC ARC and should be checked against the current Title 24 iteration.
> Title 24 is unique in structure and enforcement; it has its own compliance software (CEC-approved methods) and verification paths.


---
### 4.D Automatic Receptacle Control considerations

Under IECC editions that include Automatic Receptacle Control (notably IECC 2021 and later), **enclosed offices are required to automatically control a portion of receptacle outlets**.
> For background and detailed requirements, see:
> **[Controls Fundamentals → Automatic Receptacle Control](../controls-fundamentals/automatic-receptacle-control)**

Although Automatic Receptacle Control is **not a lighting control requirement**, it is **functionally coupled to lighting controls** once it becomes applicable. At KIS, ARC is typically implemented using the time switches and occupancy sensors that are part of the same manufacturer family as the lighting controls, to ensure consistent behavior and reliable commissioning.”

In practice, this means:
- The **same occupancy detection** used for lighting is typically used to control receptacles (shared sensors)
- Receptacle control is most reliably achieved using the **same control ecosystem** as the lighting system (signal polarities, programming methods, voltages)
- The choice of lighting control approach directly affects how receptacle control can be implemented within certain areas.

When ARC is required, lighting controls should **not** be designed in isolation.

Design implications:
- Line-voltage wall sensors may no longer be sufficient on their own
- A low-voltage sensor driving **multiple relays or power packs** (lighting + receptacle) may be required
- Mixing unrelated lighting and receptacle control systems increases coordination and commissioning risk

For this reason, once ARC is triggered by code, **lighting control strategy selection becomes a system-level decision**, not a device-level decision.

---

### 4.E Soft Constraints

- Project budgets often restrict device count
- Limited CA increases the need for unambiguous controls intent
- Coordination risk (sensors, furniture, ceiling, HVAC, etc.)

---

### 4.F Hidden Constraints

- Office layout unknown at early design
- Contractors substituting devices
- Late furniture or partition changes
- Sensor performance assumptions not verified

---

## 5. Baseline / Default Control Pattern

<!-- ANCHOR: BASELINE PATTERN -->

### Baseline (KIS default)

Unless a decision gate is triggered, use:

- **Wall-mounted combination occupancy sensor / manual control** (line-voltage) controlling the enclosed office lighting circuit
- Configure to satisfy code:
  - Auto-OFF timeout per adopted IECC (10 min) :contentReference[oaicite:14]{index=14}
  - Manual-ON (vacancy) is preferred; or
  	- if auto-ON is preferred by owner, limit initial ON to ≤50% where required :contentReference[oaicite:15]{index=15}

**KIS default hardware approach**
- Default to **line-voltage** wall sensor where it can reliably detect occupancy and where only lighting is being controlled.

The baseline intentionally avoids:
- Separate ceiling sensor + separate wall switch unless coverage requires it
- Multi-device complexity that increases commissioning and substitution risk

---

## 6. Typical Variants

<!-- ANCHOR: VARIANTS -->

### 6.1 Offices with windows (daylight zone likely)

Applied when:
- The office is within a **primary sidelit daylight zone** and daylight-responsive control thresholds apply (commonly triggered based on daylight zone rules and connected lighting in zone). :contentReference[oaicite:16]{index=16}

Changes from baseline:
- Provide **daylight-responsive control** for the office lighting serving the daylight zone (typically dimming/stepping per code-compliant system capability). :contentReference[oaicite:17]{index=17}

Invariant elements:
- Occupant sensor control remains required
- Auto-OFF timeout remains code-driven

<!-- ANCHOR: CODE EXCERPTS (WINDOW OFFICES)
Insert jurisdiction-specific daylight zone and control function excerpts here.
-->

---

### 6.2 Offices without windows (no meaningful daylight)

Applied when:
- No daylight zone applicability (interior office or no meaningful sidelight)

Changes from baseline:
- Daylight-responsive controls omitted

Invariant elements:
- Occupant sensor control required
- Manual-ON / partial Auto-ON and timeout requirements still apply :contentReference[oaicite:18]{index=18}

---

### 6.3 Atypical office layouts (coverage or geometry breaks wall sensor)

Applied when:
- Wall sensor cannot reliably detect occupancy due to geometry (e.g., deep room, L-shape, shelving/door location, obstructed line-of-sight)

Changes from baseline:
- Use a **ceiling-mounted occupancy sensor** for detection
- Provide a **separate manual wall switch/dimmer** (as required by design intent and device ecosystem)
- Keep the control intent simple and room-based

Invariant elements:
- Occupant sensor drives Auto-OFF and (if used) Auto-ON limits per adopted code :contentReference[oaicite:19]{index=19}

---

## 7. Decision Gates

<!-- ANCHOR: DECISION GATES -->

### Code edition gates (core)

- Is the adopted energy code **IECC 2015**?
  - **Yes** → Auto-OFF timeout can be **≤30 minutes** (configure accordingly) :contentReference[oaicite:20]{index=20}
  - **No (IECC 2018+)** → Auto-OFF timeout must be **≤20 minutes** :contentReference[oaicite:21]{index=21}

- Does the adopted energy code include **automatic receptacle control** (IECC 2021+ / 2024 or local equivalent)?
  - **Yes** → Apply Section 9 (Receptacle Control) and select a controls ecosystem that can drive both lighting + receptacles :contentReference[oaicite:22]{index=22}
  - **No** → Lighting controls only

### Window / daylight gates

- Is the office within a daylight zone where daylight-responsive controls apply?
  - **Yes** → Use “Offices with windows” variant (daylight-responsive control)
  - **No** → Use “Offices without windows” variant :contentReference[oaicite:23]{index=23}

### Layout gate

- Will a wall sensor reliably detect occupancy for the full office area and typical behavior?
  - **Yes** → Use baseline wall-mounted combo sensor
  - **No** → Use “Atypical layout” variant (ceiling sensor + separate manual control)

---

## 8. Control Zoning Strategy

<!-- ANCHOR: ZONING -->

Enclosed offices are **room-based zones**:
- One office = one lighting control zone (default)
- Avoid sharing zones between offices unless there is a compelling architectural constraint (rare)

---

## 9. Automatic Receptacle Control (When Required)

<!-- ANCHOR: RECEPTACLE CONTROL -->

### 9.1 Requirement (when applicable)

Where automatic receptacle control is required, enclosed offices must control **≥50%** of 125V, 15/20A receptacles. :contentReference[oaicite:24]{index=24}

Common implementation methods allowed include:
- Time schedule controls (with override limits)
- Occupancy sensor control
- Automated signal that turns receptacles off within ~20 minutes after vacancy (per code language and summaries) :contentReference[oaicite:25]{index=25}

Also expect requirements for:
- Distribution (controlled receptacles located near uncontrolled ones) :contentReference[oaicite:26]{index=26}
- Permanent marking per NFPA 70 / NEC controlled receptacle marking practices :contentReference[oaicite:27]{index=27}
- Exceptions (continuous operation loads, safety/security needs, etc.) :contentReference[oaicite:28]{index=28}

<!-- ANCHOR: CODE EXCERPTS (RECEPTACLE CONTROL)
Insert jurisdiction-specific excerpt here.
-->

### 9.2 KIS go-forward implementation (current default)

**Current KIS approach (when receptacle control is required):**
- Use a **single low-voltage occupancy sensor** to provide occupancy state
- Drive:
  1) a lighting control power pack, and  
  2) a **separate relay-based power pack** rated **15–20A** for controlled receptacles  
- Typical wiring: one sensor daisy-chained to both power packs (manufacturer-approved wiring and ratings must be followed)

**Verification note (code intent):**
- Using occupancy state to control receptacles is consistent with IECC-recognized methods (occupancy sensor / automated signal) in published summaries. :contentReference[oaicite:29]{index=29}

**Important design note:**
- The most robust approach is to keep **lighting controls and receptacle controls in the same control ecosystem** (same manufacturer family / platform) to reduce integration failures and substitution risk.

Examples of “same ecosystem” intent:
- Lutron room-based system end-to-end
- Wattstopper DLM end-to-end
- Equivalent single-platform solution where lighting + receptacle modules are designed to work together

---

## 10. Power Pack vs Line-Voltage Occupancy Sensor (Tradeoffs)

<!-- ANCHOR: POWERPACK VS LINE VOLTAGE -->

### Default (KIS): Line-voltage wall sensor (lighting only)

Use line-voltage wall sensors when:
- The office is typical geometry
- Only lighting is being controlled
- You want lowest device count and simplest documentation

### When a power pack approach becomes compelling

Power packs and low-voltage sensors become compelling when:
- You must control **both lighting and receptacles** from the same occupancy state (automatic receptacle control scenario)
- You need multiple relays from one occupancy input (lighting relay + receptacle relay)
- You are integrating with a room/area controls platform where the occupancy sensor is a shared input to multiple devices

**Real-world example (integration-driven):**
- An enclosed office is part of a tenant controls package where occupancy state must drive:
  - Lighting relay/dimming, **and**
  - Controlled receptacles, **and**
  - Potentially a local HVAC input (or future expansion)
In this case, a low-voltage sensor feeding modular relays within the same controls platform is often more reliable than mixing unrelated devices.

---

## 11. Documentation Expectations

<!-- ANCHOR: DOCUMENTATION -->

Documents must clearly show:
- Control type and intent (occupancy sensor required; timeout; manual-ON vs partial auto-ON intent)
- Daylight-responsive control applicability (if windows/daylight zone applies)
- Receptacle control scope (if applicable): % controlled, marking, and exceptions
- Required “ecosystem” intent when lighting + receptacles are linked

<!-- ANCHOR: CAD EXAMPLES
Insert plan notes, typical device schedule snippets, and detail callouts here.
-->

---

## 12. When to Go Deeper / Exit This Playbook

<!-- ANCHOR: ESCALATION -->

Exit this playbook when:
- Owner requires advanced personal control, scenes, or integration beyond room-based defaults
- The office is part of a larger connected lighting system with non-standard sequences
- Risk/liability demands a project-specific controls narrative (e.g., special security operations)

---

## 13. Cross-Links to Supporting Knowledge

<!-- ANCHOR: CROSS LINKS -->

- Occupancy Sensor Fundamentals
- Lighting Control Power Pack Fundamentals
- Daylight Zoning Principles
- Automatic Receptacle Control (ARC) overview / policy notes

---

## 14. Status and Stewardship

- **Status:** Draft  
- **Last Judgment Review:** YYYY-MM  
- **Playbook Owner:** TBD  

---

## 15. Author Notes (Institutional Context)

<!-- ANCHOR: INSTITUTIONAL CONTEXT -->

Enclosed offices are a high-volume space type where controls are often value engineered. The playbook defaults bias toward compliance and predictable occupant behavior with minimal devices, while providing a clear path to power packs and unified ecosystems when receptacle control or integration scope forces it.
