---
title: Occupancy Sensors
description: Commercial occupancy sensors as typically used for lighting and HVAC control
published: true
date: 2026-03-02T05:46:16.656Z
tags: lighting control, occupancy
editor: markdown
dateCreated: 2026-01-11T15:17:35.879Z
---

# Occupancy Sensor — Hardware Fundamentals

---

## 0. Purpose and Scope

**What this device is:**  
An occupancy sensor is a hardware device that detects the presence or absence of people within a defined area and converts that detection into an electrical or logical signal usable by lighting, controls, or building automation systems.

Occupancy sensors sit at the boundary between **physical human behavior** and **electrical control logic**. Unlike switches, they do not rely on explicit user intent; instead, they infer occupancy based on sensed physical phenomena such as motion, heat, sound, or reflected energy.

**Why this device exists:**  
Occupancy sensors exist to automate lighting and system behavior in response to space usage, enabling energy savings, code compliance, and operational convenience without requiring continuous occupant interaction.

They range from simple, self-contained line-voltage devices that directly switch loads, to low-voltage and networked sensors that act as distributed inputs to more sophisticated control systems.

**What this page covers:**  
- Detection technologies and sensing physics  
- Hardware capabilities and limitations  
- Voltage class and integration behavior  
- Typical application contexts and failure modes  

**What this page does NOT do:**  
- Recommend specific zoning strategies  
- Select control architectures or platforms  
- Define project-specific design intent  

**Related abstraction levels:**  
- [[Lighting Controls – Fundamentals]]  
- [[Powerpacks]]  
- [[Room Controllers]]  
- [[Open Office Lighting Controls]]

---

## 1. Core Function

### 1.1 Primary function
- Detect occupancy or vacancy within a defined sensing area
- Convert physical detection into a control signal
- Provide a reliable indication of space usage state

### 1.2 What occupancy sensors fundamentally do *not* do
- They do not decide lighting zones
- They do not enforce schedules
- They do not inherently control dimming or load switching

Those behaviors are implemented elsewhere in the system.

---

## 2. Detection Technologies (Sensing Physics)

This section describes the **physical mechanisms** by which occupancy sensors detect people. These mechanisms fundamentally constrain coverage, reliability, and appropriate application.

### 2.1 Passive Infrared (PIR)

PIR sensors detect changes in infrared radiation caused by warm bodies moving across a segmented field of view.

**Characteristics:**
- Requires motion across detection zones
- Sensitive to line-of-sight movement
- Low susceptibility to false positives

**Limitations:**
- Poor detection of small or stationary movements
- Reduced effectiveness in obstructed spaces

---

### 2.2 Ultrasonic

Ultrasonic sensors emit high-frequency sound waves and detect changes in the reflected pattern caused by movement.

**Characteristics:**
- Detects minor motion
- Can sense around partial obstructions

**Limitations:**
- Susceptible to false positives from air movement
- Can detect motion outside intended spaces

---

### 2.3 Dual-Technology (PIR + Ultrasonic)

Dual-tech sensors combine PIR and ultrasonic sensing to improve reliability.

**Design intent:**
- Reduce false-offs from PIR limitations
- Reduce false-ons from ultrasonic limitations

Dual-tech sensors often require both technologies to agree before asserting occupancy.

---

### 2.4 Emerging and Specialized Technologies

- Microwave / radar-based sensing
- Thermal imaging
- Vision-based or AI-assisted detection

These technologies introduce higher complexity, cost, and data considerations, and are typically used in specialized applications.

---

## 3. Form Factors and Mounting

### 3.1 Common form factors
- Ceiling-mounted
	- radial pattern for whole area coverage
  - hallway pattern for tight focused strips
- Wall-mounted
- Corner-mounted
- Fixture-integrated

### 3.2 Mounting sensitivity
- Mounting height
- Orientation
- Obstructions
- Relationship to expected occupant movement

Improper mounting can negate otherwise appropriate sensor selection.

---

## 4. Power and Voltage Class (Major Branch Point)

### 4.1 Line-Voltage Occupancy Sensors

Line-voltage sensors are powered directly from the branch circuit and typically switch the lighting load directly.

**Characteristics:**
- Self-contained operation
- Limited configurability
- Direct load control

**Typical use cases:**
- Restrooms
- Storage rooms
- Utility spaces
- Simple enclosed rooms

---

### 4.2 Low-Voltage Occupancy Sensors

Low-voltage sensors are powered via Class 2 control circuits and provide signals to external controllers such as powerpacks or room controllers.

**Characteristics:**
- Logic separated from load switching
- Higher configurability
- Easier aggregation and coordination

Low-voltage sensors are increasingly common in modern lighting control systems and often participate in wired or wireless ecosystems.

---

## 5. Capabilities and Variants (What Is Possible)

### 5.1 Common capability dimensions
- Detection technology (PIR, ultrasonic, dual-tech)
- Field of view / coverage patterns
- Sensitivity adjustment
- Time delay adjustment
- Vacancy vs occupancy mode support
- Manual override input support
- Daylight sensing integration

---

### 5.2 Field of View and Coverage Patterns

Field of view is a manufactured characteristic defined by lens design, sensor placement, and internal signal processing. It is often the primary differentiator between occupancy sensors that otherwise appear functionally similar.

Common field-of-view patterns include:
- **Wide-area coverage**
- **Narrow or long-throw coverage**
- **Corridor or aisle-focused coverage** (“hallway” sensors)
- **Multi-lobe vs single-lobe detection patterns**

Coverage effectiveness depends on several interacting factors:

- **Mounting height**  
  Increasing mounting height generally widens the coverage footprint but reduces sensitivity to small or low-motion activity. This tradeoff mirrors similar considerations in lighting photometric studies and wireless network heatmapping, where broader coverage often comes at the cost of signal resolution.

- **Orientation**  
  Sensor orientation strongly influences nuisance detection. Poor alignment may waste much of the sensing pattern on walls, furniture, windows, or adjacent spaces, leading to false positives or missed detection in the intended area.

- **Expected occupant movement patterns**  
  Understanding how occupants actually move and dwell within a space is often critical. In environments such as open offices, bullpen areas, or shared workspaces—where many desks may be unoccupied for long periods but circulation paths remain active—sensors focused on entrances and primary activity zones may perform better than sensors attempting to monitor aisleways.

  In smaller open-plan study rooms or offices, coverage focused near entrances and primary seating areas can reliably detect room entry while reducing nuisance trips caused by occupants remaining relatively motionless for extended periods.

Field of view selection is therefore not merely a coverage exercise, but a behavioral one, linking sensor geometry to how spaces are actually used.


---

### 5.3 Capability differences by voltage class
- Line-voltage sensors prioritize simplicity and direct control
- Low-voltage sensors prioritize flexibility and system integration

---

## 6. Interfaces and Integration

### 6.1 Line-voltage interfaces
- Switched hot output
- Load ratings
- Neutral requirements

### 6.2 Low-voltage interfaces
- Dry contact outputs
- Logic-level outputs
- Digital or networked signaling

### 6.3 Platform integration
- Proprietary ecosystems
- Open protocols
- Gateway-dependent systems

---

## 7. Regulatory Requirements and Certifications

- UL / ETL listings
- Plenum ratings
- Environmental ratings
- Energy code touchpoints (IECC, ASHRAE)

---

## 8. Accessories and Supporting Components

- Lenses and masks
- Mounting adapters
- Remote sensor heads
- Low-voltage power sources
- Control modules

---

## 9. Typical Application Contexts

### 9.1 Typical line-voltage applications
- Restrooms
- Small offices
- Storage spaces

### 9.2 Typical low-voltage applications
- Open offices
- Classrooms
- Conference rooms
- Multi-zone spaces

### 9.3 Poor-fit scenarios
- Overly complex systems for simple spaces
- Insufficient coverage for irregular layouts

---

## 10. Historical Context and Evolution

- Manual switching
- Standalone occupancy sensing
- Distributed low-voltage sensing
- Networked and software-defined sensing

---

## 11. Pitfalls, Assumptions, and Failure Modes

- False positives
- False negatives
- Coverage gaps
- Misapplied sensing technology
- Incorrect assumptions about occupant behavior

---

## 12. Ecosystem and Related Devices

- Powerpacks
- Room controllers
- Lighting controllers
- BAS / PLC inputs

---

## 13. Cost and Commercial Reality

- Line-voltage sensors (low cost, low complexity)
- Low-voltage sensors (moderate cost, higher flexibility)
- Networked sensors (higher cost, higher integration effort)

---

## 14. Procurement and Availability

- Electrical distributors
- Controls vendors
- Contractor-only ecosystems
- Commodity vs platform-locked devices

---

## 15. Selection and Sizing Considerations

- Coverage vs mounting height
- Sensor quantity vs reliability
- Redundancy vs nuisance trips

---

## 16. Commissioning and Validation

- Walk testing
- Sensitivity tuning
- Time delay validation
- Occupant feedback

---

## 17. Lifecycle, Maintenance, and Longevity

- Sensor aging
- Drift and recalibration
- Replacement vs reprogramming

---

## 18. Operational Mechanics

This section describes how occupancy sensors participate in system behavior once installed.

Typical topics include:
- Occupied vs vacant state transitions
- Interaction with enable / inhibit logic
- Interaction with manual overrides
- Failure containment and default behavior

*(Detailed wiring narratives and timing diagrams belong here.)*

---

## 19. Cross-links and Navigation

- [[Powerpacks]]
- [[Lighting Controls – Fundamentals]]
- [[Open Office Lighting Controls]]
- Occupancy Sensor Coverage Geometry

*working concepts*
- Occupancy Sensor Coverage Geometry
- Occupancy Sensor Detection Physics
- Occupancy vs Vacancy Logic
- Voltage-Class & Ecosystem Branches
	- Line-Voltage Occupancy Sensors
  - Low-Voltage Occupancy Sensors
  - Networked Occupancy Sensors
- Common Occupancy Sensor Failure Modes
- Occupant Behavior vs Sensor Performance
- Occupancy Sensors and Powerpacks
- Occupancy Sensors in Open Office Lighting Controls
- Occupancy Sensor Commissioning Techniques
- Occupancy Sensors vs Alternative Presence Detection
---

## 20. Status and Stewardship

- **Status:** Draft  
- **Steward:** Lighting / Controls Discipline Lead
