---
title: Open Office Lighting controls (original)
description: IECC-compliant Open-plan office lighting controls, as required by Energy Codes
published: true
date: 2026-01-12T01:39:22.057Z
tags: iecc, open-office, lighting controls
editor: markdown
dateCreated: 2026-01-04T02:29:52.694Z
---

# Open Office Lighting Controls

## 1. Purpose and Scope

This page documents the **principles, constraints, and common control strategies** used for lighting control design in open office environments. It is intended to serve as **foundational knowledge** that explains *how and why* certain design approaches are used.

This page applies to:
- Open office spaces with multiple workstations
- Shared lighting systems serving multiple occupants
- Typical commercial ceiling heights and layouts

This page does **not** prescribe a single solution. Instead, it describes the **design space and tradeoffs** that inform later decisions.

---

## 2. Definition: What Is an “Open Office” (for Controls Purposes)

For lighting control design, an **open office** is characterized by:
- A large contiguous floor area
- Multiple workstations without full-height partitions
- Shared lighting systems serving multiple occupants
- Non-uniform daylight availability across the space

Key implications for controls:
- Individual occupant preferences cannot be perfectly satisfied
- Zoning decisions strongly influence comfort and energy performance
- Control strategies must balance predictability, compliance, and complexity

---

## 3. Design Drivers and Constraints

Energy code  establishes **minimum requirements**, not optimal design solutions. How we achieve the required functions is based on a combination of available technology, owner requirements and an analysis of the particular space (workflow of the users within the space)

### 3.1 Code and Regulatory Drivers

Lighting controls in open offices are driven by:
- Energy codes (e.g., IECC, ASHRAE 90.1)
- Mandatory occupancy sensing requirements
- Mandatory daylight-responsive controls in daylight zones

The most common Code driver we come across is IECC (2015 and more recent). 


### 3.2 Human Factors

Human considerations include:
- Visual comfort
- Predictability of lighting behavior
- Sensitivity to nuisance shutoff or dimming
- Perceived loss of control in shared spaces
- Construction Cost and Value Engineering



### 3.3 Physical Constraints

Physical constraints often include:
- Ceiling height and plenum conditions
- Luminaire layout and spacing
- Daylight penetration geometry
- Furniture layout and partition heights, which may change over time
- Detection radius of Occupancy Sensors
- Available mounting locations for sensors

---

## 4. Core Control Functions (Conceptual)

Open office lighting controls typically combine several core functions.

### 4.1 Occupancy Detection

Occupancy detection enables or disables lighting based on presence.

Common technologies include:
- Passive infrared (PIR)
- Ultrasonic
- Dual-technology sensors

Each technology differs in coverage, sensitivity, and false-off risk.

### 4.2 Daylight Responsive Dimming

Daylight-responsive controls reduce electric lighting output in response to available daylight.

Key considerations include:
- Sensor placement
- Calibration and commissioning
- Alignment between daylight zones and control zones
- Full On-Off, Partial On-Off or Dimming
- Open-loop or Closed-loop dimming control

### 4.3 Manual Override and Local Control

Manual controls allow occupants to:
- Turn lights on
- Adjust light levels
- Temporarily override automatic behavior

The degree of manual control affects user satisfaction and system complexity.

---

## 5. Control Zoning Concepts

### 5.1 What Is a Control Zone?

A control zone is a group of luminaires that respond together to control inputs.

Control zones are a **design choice**, not a fixed rule.

### 5.2 Common Zoning Approaches

Typical zoning geometries include:
- Row-based zoning (often parallel to building façades)
- Column-based zoning
- Grid-based zoning
- Hybrid zoning (e.g., perimeter vs interior)

Each approach involves tradeoffs related to:
- Daylight effectiveness
- Occupant predictability
- Wiring, programming, and commissioning complexity

---

## 6. Typical Failure Modes and Pitfalls

Common issues in open office lighting controls include:
- Oversized zones causing unnecessary shutoff
- Daylight dimming applied to zones without meaningful daylight
- Sensor coverage misaligned with furniture layouts
- Excessive zoning granularity increasing commissioning risk

These issues often arise when control intent is not clearly documented or when future space changes are not considered.

---

## 7. Assumptions Commonly Made (and When They Break)

Common assumptions include:
- Furniture layouts remain relatively stable
- Daylight penetration aligns with façade geometry
- Occupancy patterns are broadly uniform

These assumptions may break down in:
- Agile or frequently reconfigured offices
- Deep floor plates
- Spaces with mixed or irregular daylight exposure

---

## 8. Relationship to Other Concepts

This topic is closely related to:
- Daylight Zoning Principles
- Occupancy Sensor Technologies
- Lighting Control System Architectures
- Commissioning and Calibration Practices
- Human Factors in Shared Spaces

Each of these topics should be documented on its own canonical page.

---

## 9. External References (Non-Canonical)

External references may include:
- Energy codes (IECC, ASHRAE 90.1)
- Manufacturer application guides
- Industry recommended practices

These references support, but do not replace, the explanations in this page.

---

## 10. Status and Stewardship

- **Status:** Draft  
- **Last substantial review:** YYYY-MM  
- **Knowledge steward:** Role or name

## 11. Unstructued and Uncategorized thoughts
It is up to MEP Engineering to design what we believe to be industry-standard functions for these spaces. MEP engineers must make the decision where specific and complex lighting controls are mandatory for a particular space, whether through explict or implied code or other standard requirements, or via an explicit owner requirement
1. Determine any minimum requirements from the other stakeholders (requested by Project Engineer or Project Manager)
2. Design something with an open specification to bid out the hardware to any Electrical Contractor.
3. 


In most small Tenant Improvement work, or smaller ground-up buildings where MEP is hired by Architectural / Developer without any Planning or Construction Administration scope, the stakeholders do not have much functional requirements for their spaces, and general lighting is a budgeted option subject to Value Engineering. If a project is purely a "bid job" where the owner is insulated from the MEP engineer, we can expect Lighting Controls to be bid out at the cheapest fixed cost by the cheapest Contractors. This balance between competing directives drives how we design, draw and document our lighting solutions

Learn this inside and out.
