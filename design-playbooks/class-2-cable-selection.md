---
title: "Class 2 Cable Selection"
description: "Vendor-neutral selection and evidence workflow for indoor commercial Class 2 power and controls."
published: true
page_type: playbook
page_status: draft
confidence_level: medium
domain_primary: electrical
ai_role: prescriptive_standard
invocation_triggers:
  systems_present: [class_2_power, low_voltage_lighting, building_automation, power_limited_controls]
decision_axes: [circuit_classification, cable_selection, conductor_allocation, installation_method]
related_pages:
  - "../ontology/reg-and-class/class-2-circuit-cabling.md"
  - "../hardware/cabling/class-2-cable-catalog.md"
tags: electrical, class-2, cabling, selection
editor: markdown
---

# Class 2 Cable Selection — Design Playbook

## 1. Purpose and Use

Use this shared playbook when choosing cable for indoor commercial Class 2
power/control circuits. Begin with [regulatory basis](../ontology/reg-and-class/class-2-circuit-cabling.md)
and use the [multi-vendor catalog](../hardware/cabling/class-2-cable-catalog.md)
for product evidence. Lighting, BAS and other extensions reference this guidance.

## 2. Design Intent

Select a documented product appropriate for the circuit, route and terminals.
Keep code requirements, manufacturer limits, KIS preferences and project decisions
separate. Belden seeds the catalog; it is not an exclusive manufacturer standard.

## 3. Space / System Definition

Capture source classification, output voltage/current, load behavior, destinations,
circuit count, route environment and installed length basis. Independently identify
power, control and communications circuits, including their isolation requirements.

## 4. Constraint Envelope

### 4.1 Hard Constraints

Verify source and equipment listing, applicable wiring permissions, cable certification,
route environment, conductor/terminal compatibility, current/temperature limits and
acceptable load voltage. Use exact manufacturer data and adopted code, not family
name extrapolation.

### 4.2 Soft Constraints

Cable standardization, shielding preference, spare conductors, stock, cost and
pulling labour are project/KIS choices. They cannot waive a hard constraint.

### 4.3 Hidden Constraints

Bundle heating, ambient temperature, simultaneous loaded circuits, connector range,
strand acceptance, pulling/bend limits and actual device voltage limits can govern.
A manufacturer's current figure at a stated temperature is not automatically the
allowable installed ampacity for a bundled multi-circuit installation.

## 5. Baseline / Default Design Pattern

1. Record adopted code/edition and qualifying Class 2 output evidence.
2. Classify each route segment: environmental air, riser, general interior and any special exposure.
3. Determine permitted cable type or documented substitution and the wiring method.
4. Count actual required independent circuits, conductors, physical pairs and separately chosen spares.
5. Choose candidates from any catalog manufacturer with matching construction and verified evidence.
6. Check current/temperature, circuit voltage drop, terminals, shield treatment and installation dimensions.
7. Record exact selected orderable SKU, data-sheet revision, project acceptance and remaining conditions.

A catalog entry is a selection candidate. “Manufacturer data checked” establishes
only the fields identified in that entry. “Project accepted” requires a project
record and does not promote the product to an unrestricted universal approval.

## 6. Typical Variants

- Two-conductor cable: one independent two-wire circuit if all selection gates pass.
- Three-conductor cable: one two-wire circuit plus one spare conductor; not a spare pair.
- Four-conductor cable: potentially two independent circuits; not necessarily two twisted pairs.
- Multi-pair cable: allocate each verified physical pair to its circuit and retain spare identities.
- Shielded cable: use where required by the interface/noise review. Termination follows equipment instructions; do not universally prescribe head-end-only grounding.

## 7. Decision Gates

| Gate | Proceed when | Otherwise |
|---|---|---|
| Source classification | Qualifying source/output and applicable requirements documented | Hold Class 2 selection conclusion |
| Route permission | Environment, cable listing/substitution and wiring method established | Resolve route or listing evidence |
| Product identity | Exact construction and current source sheet established | Retain as candidate; no inferred specifications |
| Electrical/mechanical fit | Loading, voltage, terminals and installation criteria supported | Revise selection or obtain evidence |
| Project acceptance | Reviewed selection and applicable conditions recorded | Keep provisional |

## 8. Design Zoning / Grouping Strategy

Count cables, circuits, conductors and pairs independently. Preserve each source
output and destination input. Sharing a jacket is not electrically combining
outputs. Electrical paralleling requires its own product/terminal and code review;
parallel *cable runs* must not be confused with parallel conductors or supplies.

The intake guide proposes four active plus two spare pairs in a six-pair trunk.
This remains an **application option**, not a general Class 2 or QDCD requirement.
Demand-based feed allocation remains in force in [EPS allocation](eps-pdu-allocation.md).
Two unused pairs are 50% of four active pairs, but one-third of total pair capacity.
Two six-pair cables or one nine-pair cable are alternatives only after actual
circuit demand and product availability are established. No universal nine-pair
market ceiling is adopted.

## 9. Common Failure Modes

Blindly copying code section numbers across editions; assuming CMP implies CL2P
dual marking; selecting an unverified SKU from a pattern; assuming every 16 AWG
product has 18 AWG stranding; using source-sheet nominal current as installed
ampacity; using a generic bend multiplier instead of the selected product limit.

## 10. Safe Assumptions (and Limits)

Unknown specifications stay unknown. A blank value is not zero and is not permission
to use the nearest product's value. Datasheet confirmation alone does not settle
wet/outdoor, industrial, hazardous-location or special-system suitability.

## 11. Documentation Expectations

For every candidate retain manufacturer, base part number, orderable suffix when
selected, construction, conductor/pair counts, AWG/stranding, actual markings,
shield/drain, OD, conductor DCR and its basis, voltage/temperature limits, minimum
bend radii, pulling tension, source URL/revision/review date and evidence status.
Record project-specific current, length, voltage-drop budget, load voltage,
bundle/ambient, terminal evidence, spare allocation and shield termination.

For routing, retain one physical cable ID with its circuit/conductor mappings.
The LV extension's bundle model consumes selected cable attributes; this catalog
does not implement its voltage-drop or conductor-selection engine.

## 12. When to Go Deeper / Exit This Playbook

Escalate unresolved source classification, output combination, terminal paralleling,
industrial/hazardous/wet routes, emergency/fire-alarm systems, power/data-specific
requirements or any installation beyond the product evidence.

## 13. Cross-Links to Supporting Knowledge

[Regulatory basis](../ontology/reg-and-class/class-2-circuit-cabling.md) ·
[Product catalog](../hardware/cabling/class-2-cable-catalog.md) ·
[Allocation index](smartdc-allocation-index.md) ·
[LV bundle contract](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/ontology/canonical-model/cable-route.md).

## 14. Status and Stewardship

Draft; reviewed 2026-10-15. KIS Solutions, electrical engineering.

## 15. Author Notes

Derived from the owner-supplied October 15 cable selection guide, reconciled with
manufacturer sources and existing demand-based allocation doctrine. Regulatory
claims remain subject to the edition-aware review stated in the linked basis.
