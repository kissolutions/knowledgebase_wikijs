---
title: Open Office Lighting Controls Design Playbook
description: This Playbook will guide the energy-code dependent, constraint-aware 
published: true
date: 2026-01-11T19:10:24.878Z
tags: lighting controls, playbook, open office
editor: markdown
dateCreated: 2026-01-11T18:55:09.915Z
---

# Open Office Lighting Controls — Design Playbook

<!--
DESIGN PLAYBOOK
Domain: Lighting Controls
Scope: Open Office Environments
-->

## 1. Purpose and Use

<!--
ANCHOR: PURPOSE
-->

This Design Playbook defines **how KIS Solutions designs lighting control systems for open office environments** under typical commercial project constraints. It is the **primary starting point** for engineers responsible for laying out, documenting, and reviewing lighting controls in open office spaces.

This playbook is used to:
- Provide a clear, defensible **starting point** for open office lighting control design, so engineers are not designing from a blank page
- Make **early design decisions** that already account for code requirements, typical project constraints, and downstream coordination
- Reduce rework and redesign caused by **late discovery of code triggers, daylighting requirements, or control complexity**
- Ensure that different engineers, across different projects, arrive at **consistent and reviewable lighting control solutions**

This playbook is prescriptive. It documents **organizational defaults and judgment**, not an exhaustive set of options.

This playbook intentionally does **not**:
- Explain how lighting hardware works
- Teach energy code fundamentals
- Compare control technologies in the abstract

Those topics are covered in linked reference material.

---

## 2. Design Intent

<!--
ANCHOR: DESIGN INTENT
-->

The design intent for open office lighting controls prioritizes:
- **Code compliance that remains valid even when the project changes**, such as during value engineering, contractor substitutions, or minor layout revisions
- **Predictable behavior** in shared work spaces
- **Robustness against value engineering and contractor substitution**
- **Commissioning success** with reasonable effort

The primary failures this playbook seeks to avoid are:
- Nuisance shutoff or dimming that erodes occupant trust
- Over-zoning that increases cost and commissioning risk
- Control strategies that rely on idealized furniture layouts
- Designs that meet code on paper but fail operationally

This playbook deliberately does *not* optimize for:
- Individual occupant customization
- Maximum theoretical energy savings
- Highly customized or project-specific control sequences that require detailed programming, tuning, or ongoing oversight to function correctly


<!--
ANCHOR: ESCALATION NOTE
Higher performance or customization requires exiting this playbook.
-->

---

## 3. Space Type Definition (Decision-Oriented)

<!--
ANCHOR: SYSTEM DEFINITION
-->
> For a detailed discussion of office space classifications, uses, and code context, see:
> **[Interior Space Types → Open Office](../interior-space-types#open-office)**

For lighting control purposes, an **open office** is understood as a space that:
- Serves multiple workstations within a shared, contiguous area
- Uses shared lighting systems across multiple occupants
- Lacks full-height partitions between users
- Exhibits non-uniform daylight conditions across the space

This definition is intentionally brief.

If the space:
- Feels like a shared work area rather than a room
- Serves many occupants with the same lighting system
- Cannot reasonably satisfy individual lighting preferences

Then it should be treated as an **open office** for lighting control design, and this playbook applies.


---

## 4. Constraint Envelope

<!--
ANCHOR: CONSTRAINT MODEL
-->

### 4.1 Hard Constraints

- Applicable energy codes (IECC, ASHRAE 90.1, adopted local amendments)
- Mandatory occupancy sensing
- Mandatory daylight-responsive control in defined daylight zones
- Life-safety and emergency lighting separation

<!--
ANCHOR: CODE EXCERPTS
Insert relevant IECC / ASHRAE excerpts here with year and jurisdiction.
-->

Hard constraints define **what functions must exist**, not how they are implemented.

---

### 4.2 Soft Constraints

- Owner or tenant standards
- Typical tenant improvement budgets
- Project schedules
- Architectural ceiling and lighting concepts

Soft constraints influence how conservative or flexible the design should be.

---

### 4.3 Hidden Constraints

<!--
ANCHOR: INSTITUTIONAL JUDGMENT
-->

- Limited or no construction administration
- Contractor-driven control substitutions
- Aggressive value engineering of lighting controls
- Future furniture reconfiguration outside engineer control

Hidden constraints strongly influence baseline choices and documentation clarity.

---

## 5. Baseline / Default Control Pattern

<!--
ANCHOR: BASELINE PATTERN
If nothing else is known, this is what we do.
-->

Unless a decision gate is triggered, open office lighting controls shall follow this baseline pattern:

- **Automatic ON/OFF control via occupancy sensing** serving defined control zones
- **Manual ON capability** via local control devices
- **Automatic OFF** to satisfy energy code requirements
- **Daylight-responsive control applied only where daylight contribution is meaningful**

Baseline assumptions:
- Control zones balance predictability and coverage
- Sensors are selected and placed for reliable presence detection, not edge-case sensitivity
- Manual controls provide limited, intuitive adjustment rather than full customization

The baseline intentionally avoids:
- Excessively granular zoning
- Complex time-based or behavioral sequences
- Reliance on furniture layouts likely to change

This baseline represents a solution that can be sketched quickly, defended easily, and documented clearly.

---

## 6. Typical Variants

<!--
ANCHOR: VARIANTS
-->

Variants are applied only when a specific constraint forces deviation from the baseline.

### Daylight-Driven Perimeter Open Office

Applied when:
- A significant portion of the space falls within a defined daylight zone

Changes from baseline:
- Separate daylight-responsive control zones at the perimeter
- Interior zones remain non-daylight-responsive

Invariant elements:
- Occupancy control philosophy
- Manual control expectations

---

### Deep-Plan or Low-Daylight Open Office

Applied when:
- Daylight penetration is minimal or inconsistent

Changes from baseline:
- Daylight-responsive controls omitted entirely

Invariant elements:
- Occupancy-based control
- Zoning approach

---

### Extended-Hours or High-Density Office

Applied when:
- Occupancy patterns are irregular or extended

Changes from baseline:
- Sensor placement and timeout settings biased toward reliability

---

## 7. Decision Gates

<!--
ANCHOR: DECISION GATES
-->

- Is the space subject to mandatory daylight-responsive control by code?
  - **Yes** → Apply Daylight-Driven Perimeter variant
  - **No** → Remain on baseline

- Is daylight contribution inconsistent or negligible?
  - **Yes** → Remove daylight-responsive controls
  - **No** → Remain on baseline

- Are there owner-mandated control behaviors beyond the baseline?
  - **Yes** → Exit playbook and develop a project-specific control narrative
  - **No** → Remain within playbook

- Is the project delivery model likely to undermine complex controls?
  - **Yes** → Bias toward simplified baseline implementation

<!--
ANCHOR: EXIT CONDITIONS
-->

Decision gates exist to force early clarity and prevent late redesign.

---

## 8. Control Zoning Strategy

<!--
ANCHOR: ZONING
-->

A control zone is a **deliberate design grouping** of luminaires that respond together.

Baseline zoning principles:
- Zones serve multiple workstations predictably
- Daylight zones align with façade geometry, not furniture
- Interior zones are kept larger to reduce complexity

Common zoning failures include:
- Oversized zones causing nuisance shutoff
- Applying daylight control where daylight is ineffective
- Overly granular zones that increase commissioning risk

---

## 9. Common Failure Modes

<!--
ANCHOR: FAILURE MODES
-->

### Design-Time Failures
- Over-customizing early without constraints
- Assuming static furniture layouts

### Documentation Failures
- Unclear control intent on drawings
- Mismatch between plans and narratives

### Construction / Operational Failures
- Contractor simplification during value engineering
- Poor sensor placement due to ceiling coordination

---

## 10. Safe Assumptions (and Limits)

<!--
ANCHOR: SAFE ASSUMPTIONS
-->

Safe assumptions include:
- Typical office occupancy patterns
- Furniture changes within general planning modules

Assumptions break down in:
- Agile workplaces
- Mixed-use floor plates
- Highly irregular daylight conditions

When assumptions break, escalation is required.

---

## 11. Documentation Expectations

<!--
ANCHOR: DOCUMENTATION
-->

Construction documents shall clearly convey:
- Control zone boundaries
- Sensor locations and coverage intent
- Manual control locations
- Daylight control applicability

<!--
ANCHOR: CAD EXAMPLES
Insert plan views, boxed notes, elevations, and redlines here.
-->

Documents must allow a contractor to implement intended behavior without interpretation.

---

## 12. When to Go Deeper / Exit This Playbook

<!--
ANCHOR: ESCALATION
-->

Exit this playbook when:
- Control behavior exceeds standard code compliance
- Spaces require individualized lighting behavior
- Risk or liability exceeds baseline assumptions

At that point, develop a project-specific lighting control narrative.

---

## 13. Cross-Links to Supporting Knowledge

<!--
ANCHOR: CROSS LINKS
-->

- Occupancy Sensor Fundamentals
- Lighting Control Power Pack Fundamentals
- Daylight Zoning Principles
- Commissioning Practices

These references provide detail but are not required to use this playbook.

---

## 14. Status and Stewardship

- **Status:** Draft  
- **Last Judgment Review:** YYYY-MM  
- **Playbook Owner:** TBD  

---

## 15. Author Notes (Institutional Context)

<!--
ANCHOR: INSTITUTIONAL CONTEXT
-->

Open office lighting controls are frequently subject to value engineering and minimal stakeholder input. This playbook reflects a bias toward designs that survive those conditions while remaining compliant, predictable, and defensible.
