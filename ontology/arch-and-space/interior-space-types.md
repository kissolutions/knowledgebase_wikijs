---
title: Interior Space Types
description: This page describes the concept of Occupancy within regulatory documents like Building Code, ASHRAE, IECC.
published: true
date: 2026-03-02T05:49:09.475Z
tags: occupancies, building code
editor: markdown
dateCreated: 2026-01-11T19:02:58.312Z
---

# Interior Space Types — Definitions and Code Context

## Purpose

This page defines common **interior space types** used in commercial and industrial projects and explains how those spaces are typically understood from a **use, occupancy, and code perspective**.

The intent of this page is to:
- Establish a shared language for space types across disciplines
- Clarify how codes implicitly and explicitly differentiate spaces
- Provide context *before* design decisions are made
- Support downstream Design Playbooks without duplicating prescriptive guidance

This page describes **what spaces are**, not **how to design them**.

---

## 1. How Space Types Are Defined

Interior space types are not defined by a single factor.

In practice, a space type emerges from the interaction of:
- Architectural intent
- Occupancy characteristics
- Typical use patterns
- Code classification and thresholds
- Behavioral assumptions embedded in codes

A single architectural room name may map to different space types depending on how the space is used, occupied, and controlled.

---

## 2. Why Space Type Definitions Matter

Correctly understanding space type affects:
- Which energy code requirements apply
- Whether automatic controls are mandatory
- How daylighting provisions are triggered
- How egress and life safety requirements are interpreted
- How predictable occupant behavior is assumed to be

Misclassifying a space often leads to:
- Incorrect control strategies
- Missed or misapplied code requirements
- Poor occupant experience
- Redesign late in the project lifecycle

Space type definition is therefore a **foundational design decision**, even though it is often implicit.

---

## 3. Common Axes of Differentiation

Codes and standards distinguish space types along several recurring axes. These axes explain *why* different spaces are treated differently, even when they appear similar.

Common differentiators include:

### 3.1 Occupancy Density
- Number of occupants per unit area
- Whether occupancy is sparse, moderate, or dense

### 3.2 Duration of Occupancy
- Continuous vs intermittent use
- Short-term vs long-term presence

### 3.3 Predictability of Movement
- Static occupants vs frequent movement
- Episodic vs continuous circulation

### 3.4 Individual vs Shared Use
- Single-user control vs shared control
- Whether individual preferences can be reasonably accommodated

### 3.5 Task Variability
- Consistent tasks vs highly variable activities
- Uniform vs specialized lighting and environmental needs

### 3.6 Visibility and Supervision
- Whether occupants are visually apparent
- Whether presence can be easily inferred without sensors

These axes are rarely stated explicitly in code language, but they strongly influence how requirements are written and enforced.

---

## 4. Interior Space Type Catalog

The sections below describe common interior space types at a **conceptual and code-aware level**. Each section focuses on definition, use, and implications — not design solutions.

---

## Enclosed Office

### Definition (Implicit and Code-Derived)

An **enclosed office** is not defined as a unique named space type in most building or energy codes.

Instead, it is an **implicitly recognized condition** based on enclosure, size, and use patterns that allow codes to make assumptions about individual occupancy and control.

For practical design purposes, an enclosed office is understood as:

- An **office-use space** intended for one or a small number of occupants  
- A space that is **fully enclosed by full-height walls and a door**  
- A room whose size and function support **individual or room-level control assumptions**

This implicit definition is derived from how codes treat small office spaces differently from larger shared areas.

---

### Relationship to Energy Codes (Lighting Controls)

Energy codes such as the IECC do not explicitly define an “enclosed office.”

However, they commonly establish **size-based thresholds** that distinguish between:
- Small, enclosed office rooms, and
- Larger office areas requiring shared control strategies

In practice, an enclosed office is typically:
- **Less than 250 square feet**, and
- **Fully enclosed**, and
- Served by lighting intended for a specific room

When these conditions are met, energy codes often allow:
- Room-based occupancy sensing
- Simpler control zoning
- Exemption from some daylight-responsive control requirements

These allowances are based on the assumption that:
- Occupancy is limited
- Use is predictable
- Control behavior can be localized to a single room

---

### Relationship to Building Code Occupancy Classification

Under the International Building Code (IBC), enclosed offices are typically classified as:

- **Group B — Business Occupancy**

This classification is consistent with:
- Administrative or professional use
- Moderate occupant loads
- Continuous but predictable occupancy

Enclosed offices do **not** constitute a separate occupancy group; they are a **sub-condition** within Business occupancy that affects how systems are designed and controlled.

---

### Distinction from Open Offices

Although both enclosed and open offices fall under Business occupancy, they differ in ways that are critical for design:

Enclosed offices are characterized by:
- Individual or very small group use
- Dedicated lighting systems serving a single room
- Predictable occupancy patterns
- Clear physical boundaries

Open offices, by contrast, involve:
- Shared use by many occupants
- Shared lighting systems
- Greater behavioral variability
- Less precise alignment between presence and lighting demand

These differences explain why enclosed offices are often treated more simply by energy codes.

---

### Distinction from Conference and Multi-Function Rooms

Enclosed offices are sometimes confused with:
- Small conference rooms
- Huddle rooms
- Multi-function spaces

However, enclosed offices differ because:
- They are intended for **ongoing individual work**, not meetings
- Occupancy density is low and stable
- Use is continuous rather than episodic

Conference and multi-function rooms often:
- Trigger assembly-related assumptions
- Involve higher peak occupant loads
- Require different life-safety and control considerations

---

### Why This Implicit Definition Exists

The absence of an explicit “enclosed office” definition reflects how codes operate:

- Codes define **thresholds and behaviors**, not room names
- Small, enclosed spaces allow simpler assumptions about control and occupancy

Design practice uses the term “enclosed office” to describe spaces where:
- Individual control assumptions are reasonable
- Shared-system complexity is unnecessary
- Code allowances can be safely applied

This implicit definition supports consistent interpretation across projects and informs downstream Design Playbooks.

---

## Open Office
### Definition 
(Implicit and Code-Derived)
An **open office** is not explicitly defined as a named space type in most building or energy codes.

Instead, it is an **implicitly defined condition** that emerges from how codes classify *office use*, *occupancy*, and *control thresholds*.

For practical design purposes, an open office is understood as:

- An **office-use space** that does **not** meet the criteria for a small, enclosed office  
- A space that exceeds size thresholds where individual, room-based control assumptions no longer apply  
- A shared-use work area that is treated collectively by energy and building codes

This implicit definition is derived from the following code behaviors.

---

#### Relationship to Energy Codes (Lighting Controls)

Energy codes such as the IECC do not define an “open office” directly.

Instead, they distinguish between:
- **Small, enclosed offices** (typically less than 250 SF), and
- **Larger office areas** that require different control treatment

When an office space:
- Is **greater than 250 SF**, and
- Is **not fully enclosed**, and
- Serves multiple occupants who cannot be guaranteed to be "satisfied" at the same time

It is implicitly treated as an **open office** for lighting control purposes.

This distinction drives requirements for:
- Automatic lighting shutoff
- Control zoning
- Daylight-responsive controls

---

#### Relationship to Building Code Occupancy Classification

Under the International Building Code (IBC), open offices are typically classified as:

- **Group B — Business Occupancy**

This classification reflects:
- Administrative and professional use
- Moderate occupant loads
- Predictable, non-assembly behavior

Open offices are **not** classified as Assembly spaces because:
- They are not intended for large, transient gatherings
- They do not support a single, defined assembly function
- Occupancy is distributed rather than concentrated

---

#### Distinction from Multi-Function or Assembly Spaces

Although open offices may host:
- Informal collaboration
- Small meetings
- Flexible work arrangements

They are **not** multi-function rooms in the building code sense.

Multi-function or assembly spaces are characterized by:
- Episodic use
- High occupant density during events
- Different life-safety and control assumptions

Open offices remain:
- Continuously occupied
- Business-use spaces
- Governed by office-specific control logic rather than assembly logic

---

#### Why This Implicit Definition Exists

The absence of an explicit “open office” definition reflects a broader pattern in codes:

- Codes define **use categories and thresholds**, not furniture layouts
- Design practice fills in the gaps between named classifications

The term “open office” exists to describe the **practical reality** of how shared office spaces behave under code, even when the code itself does not use the term.

This implicit definition provides the foundation for downstream design decisions addressed in related Design Playbooks.

---

### Typical Uses

Open offices are commonly used for:
- General administrative work
- Knowledge work with intermittent collaboration
- Call centers and support staff
- Flexible or reconfigurable tenant layouts

They are not optimized for privacy or individualized environmental control.

---

### Occupant Flow and Behavior

Occupancy in open offices is typically:
- Moderate to high density
- Predictable in schedule but variable at the individual level
- Continuous rather than episodic

Occupants may move frequently, and visual presence does not always correlate with active use.

---

### Code Classification Implications

From a code perspective, open offices are generally treated as:
- Business occupancy
- Shared-use, non-dwelling spaces

This classification often triggers:
- Mandatory automatic lighting shutoff
- Daylight-responsive control requirements
- Larger and more complex daylight zones

---

### Relationship to Other Office Space Types

Open offices sit between:
- Enclosed offices (single-user, predictable)
- Multi-function or assembly spaces (high variability)

They share traits with both but fully match neither.

---

### Why This Matters for Design

Because open offices are shared and behaviorally complex, they require **intentional design strategies**, which are addressed in downstream Design Playbooks.

---

## Enclosed Office

*(To be developed)*

---

## Multi-Function / Assembly Spaces

*(To be developed)*

---

## Corridors and Circulation Spaces

*(To be developed)*

---

## Warehouses and Industrial Spaces

*(To be developed)*

---

## Relationship to Design Playbooks

This page defines **space types and their implications**.

Design Playbooks reference these definitions and provide **prescriptive guidance** for:
- Lighting controls
- HVAC zoning
- Power distribution
- Controls and automation

The separation is intentional:
- This page answers **what is this space?**
- Playbooks answer **how do we design for it?**


## 5. THOUGHTS TO PUT ELSEWHERE
It is up to MEP Engineering to design what we believe to be industry-standard functions for these spaces. MEP engineers must make the decision where specific and complex lighting controls are mandatory for a particular space, whether through explict or implied code or other standard requirements, or via an explicit owner requirement
1. Determine any minimum requirements from the other stakeholders (requested by Project Engineer or Project Manager)
2. Design something with an open specification to bid out the hardware to any Electrical Contractor.
3. 


In most small Tenant Improvement work, or smaller ground-up buildings where MEP is hired by Architectural / Developer without any Planning or Construction Administration scope, the stakeholders do not have much functional requirements for their spaces, and general lighting is a budgeted option subject to Value Engineering. If a project is purely a "bid job" where the owner is insulated from the MEP engineer, we can expect Lighting Controls to be bid out at the cheapest fixed cost by the cheapest Contractors. This balance between competing directives drives how we design, draw and document our lighting solutions

Learn this inside and out.