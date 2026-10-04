---
title: Interior Space Types
description: This page describes the concept of Occupancy within regulatory documents like Building Code, ASHRAE, IECC.
published: true
date: 2026-03-02T06:09:37.712Z
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

This page describes **what spaces are**, not **how to design them**. Preserve source room names, Building Code Space Type, Building Code Occupancy Group and Energy Code Space Type separately; none automatically supplies the others. New circulation/room/daylight vocabulary below is draft KIS framework terminology informed by owner workflow decisions, with regulatory applicability still requiring a selected edition and source verification.

---

For proposed synonym mappings and owner confirmation, follow the [room classification and controls review playbook](../../design-playbooks/room-classification-and-controls-review-playbook.md). This catalog supplies definitions and retrieval candidates; the playbook owns the review process and keeps building and energy classifications separate.

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

Keep the office definition separate from edition-specific control thresholds. Room area, enclosure, actual use, glazing and connected lighting are inputs to the selected code review; a vocabulary label alone does not establish an exemption or required control sequence.

This catalog does not use a universal 250 SF cutoff to define an enclosed office. Determine applicable triggers, exceptions and required behavior from the project's selected standard, edition, jurisdiction and amendments with exact source references. An enclosed office can be larger than a particular control threshold while remaining architecturally enclosed.

Use the [lighting guidance index](../../design-playbooks/lighting-controls-guidance-index.md) to locate the relevant playbook and its review limitations.

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

For KIS shared vocabulary, an **open office** is an office work area with shared workstations or desks that are not individually enclosed as separate rooms. Shared circulation between workstations is ordinarily part of that work area unless architectural designation or a reviewed distinct corridor establishes a separate tracking Space.

Area is an observed input, not the definition. Do not classify an office as open solely because it exceeds a numerical threshold, or as enclosed solely because it is small. Record actual enclosure and use separately.

#### Relationship to Energy Codes (Lighting Controls)

Select applicable office control requirements from the adopted edition and amendments. Independent control-area limits, sensor coverage, shutoff behavior and daylight requirements belong to the referenced code interpretation/playbook, not a timeless size-based vocabulary rule.

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

## Multi-Function / Assembly Spaces

*(To be developed)*

---

## Corridors and Circulation Spaces

These are KIS working descriptions, not quoted regulatory definitions or automatic occupancy classifications.

- **Corridor:** a distinct traffic passage connecting rooms or larger areas, commonly bounded by opposing walls. It remains a circulation Space even when no luminaire is depicted. A short cased opening is not automatically a corridor; unclear extent needs architectural/owner review.
- **Door alcove:** a recess serving door access and opening directly onto a larger Space. An untagged three-sided alcove can remain part of the surrounding Space, with its location/doors described there.
- **Vestibule:** a source-designated entry or transition space. Preserve an architect's actual designation; do not merge every named vestibule merely because the informal phrase "door vestibule" was used for an alcove.
- **Secondary circulation:** movement paths within another use, such as aisles between open-office workstations. They ordinarily remain part of that use unless architectural evidence supports separate tracking.

A finish/material or ceiling transition can support a reviewed tracking boundary. It does not establish independent occupancy sensing or other control requirements by itself. Architectural naming, actual use and project evidence govern classification; fixture arrangement does not establish a Space boundary.

For LV project tracing and owner review, follow the [extension's boundary workflow](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/architectural-space-intake.md#when-an-untagged-area-is-its-own-space).

Corridor control guidance is pending edition-specific review. Do not prescribe sensor counts, timeout, dimming behavior or a daylight exemption from this vocabulary entry. Record missing lighting/control documentation as a review question, not proof of an unlit or exempt corridor.

---

## Other Room Functions

These working definitions preserve intended use without automatically assigning Building Code Space Type, Building Code Occupancy Group, Energy Code Space Type or controls. Unknown use stays unknown until source-supported or owner-confirmed. Dedicated control playbooks for these functions remain to develop.

| Function | Working description and classification question |
|---|---|
| Conference / meeting room | Space used for group meetings; record capacity, enclosure and actual meeting use separately from office use |
| Huddle room | Small meeting/collaboration room; the label alone does not establish the applicable meeting-room code category |
| Break room | Staff rest/refreshment space; distinguish seating, food preparation and equipment functions where relevant |
| Copy / print room or area | Space serving document production/equipment; record whether enclosed or part of another occupied work area |
| Storage | Space used to store materials/items; document known purpose and use without inferring contents or classification from shape |
| IDF / communications room | Source-designated communications/equipment space; the acronym does not establish a lighting-control exception |
| Wellness room | Source-designated wellness/support space; its specific activity and occupancy need confirmation before code classification |
| Reception | Space for receiving visitors, desk service and/or waiting; record its actual components and architectural extents |
| Lobby | Arrival, waiting and circulation space; distinct named uses within it may warrant reviewed tracking subdivisions |
| Hospitality | Broad source label for amenity/service use; document actual activity rather than automatically treating it as break room, lobby or food service |
| Classroom | Space used for organized instruction; record the actual instructional use, capacity and enclosure for later classification |

## Daylight Vocabulary

**Primary daylight zone** and **secondary daylight zone** identify geometric areas associated with daylight entering a space under the selected code/edition. They are not room types, power channels or automatic statements that daylight controls are required. Exact extents, naming, thresholds, exceptions and required control separation must be established from that selected reference.

Record window/skylight presence, calculated daylight-zone geometry and control applicability as separate observations/conclusions. Do not use "has windows" as a substitute for a daylight calculation, or use a supply channel's wattage as the whole daylight-zone load. Edition-specific daylight guidance remains to develop through the [lighting guidance index](../../design-playbooks/lighting-controls-guidance-index.md).

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
