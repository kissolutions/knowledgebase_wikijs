---
title: Physical Boundary Register v0.1
description: Shared cross-domain canonical structure for physical construction boundaries and barrier evidence
published: true
tags: ontology, physical-boundary, register, fire-life-safety
editor: markdown
---

# Physical Boundary Register v0.1

**Status:** Initial schema contract, 2026-10-17; implementation candidate for project spreadsheets. **Owner:** Parent KIS knowledgebase. **Process:** [Physical Boundary Intake v0.1](../design-playbooks/physical-boundary-intake-v0.1.md). **Machine-readable companion:** [JSON Schema v0.1](physical-boundary-register-v0.1.schema.json), for optional structural checking and derived interchange; the editable project register is authoritative.

## Scope and identity

A **Physical Boundary** is an identified wall, floor, horizontal assembly, shaft enclosure or other physical construction element/segment affecting engineering layout, compartmentation or crossings. It is **not** a logical room/lighting-zone edge and not automatically an approved opening or penetration.

- One stable `Boundary ID` per distinct modeled segment; IDs survive label/geometry edits and are never silently reused.
- `Boundary Type` describes physical form. `Code Classification(s)` describe code-defined function under the project governing code basis and may have more than one applicable designation. A two-hour rating does **not** automatically establish a Fire Barrier.
- `Adjacent Space A` and `Adjacent Space B` reference Space IDs; one side may be exterior, unmodeled, or unknown. A boundary can join multiple modeled spaces only by segmentation or an explicit relationship convention.
- Segmentation follows materially different physical construction, rating, classification or crossing constraints; do not create a wall segment for every superficial drawing line.
- The project **Code Basis** owns jurisdiction, adopted code editions and amendments. Each boundary retains its specific classification evidence and source revision. A source-described designation is distinct from an independently verified code applicability determination.
- A physical boundary can be modeled as `adjacent_context` without bringing it into installation scope.

## Core register columns

| Field | Type | Required | Guidance |
|---|---|---|---|
| Boundary ID | Stable string | Yes | e.g., B-014; never repurpose |
| Description | Text | Yes | Neutral physical/location description |
| Boundary Type | Enum | Yes | wall, floor, ceiling, roof, shaft_enclosure, other, unknown |
| Code Classification(s) | Multi-value | Yes (may be empty) | fire_wall, fire_barrier, fire_partition, smoke_barrier, smoke_partition, horizontal_assembly, exterior_wall, other; **no inferred default** |
| Classification State | Enum | Yes | unreviewed, source_observed, verified, unresolved, not_applicable |
| Fire-Resistance Rating (minutes) | Nonnegative integer / unknown | No | Preserve evidence and distinguish unknown from nonrated; a known nonrated finding uses explicit rating status |
| Rating State | Enum | Yes | unknown, stated, verified, not_rated, conflict |
| Smoke Barrier Status | Enum | Yes | yes, no, unknown; separate from smoke_partition designation |
| Smoke Partition Status | Enum | Yes | yes, no, unknown |
| Adjacent Space A ID | Space ID / null | No | The first adjacent space, when confirmed |
| Adjacent Space B ID | Space ID / null | No | The second adjacent space, when confirmed |
| Side A / Side B Context | Text | No | Exterior, unmodeled, adjacent area, or uncertainty notes |
| Level / Location | Text | No | Human-readable |
| Geometry Reference | Text | No | Persistent PDF annotation/CAD object identifier and drawing coordinates where supported |
| Source Reference | Text | No | Document, sheet/detail, revision, explicit locator |
| Code Basis Reference | Text | No | Link to project-level adopted codes; do not repeat editions on every row |
| Scope Disposition | Enum | Yes | in_scope, interface_only, adjacent_context, excluded, unresolved |
| Review State | Enum | Yes | provisional, reviewed, accepted, superseded; **reviewed is not Engineering Acceptance** |
| Notes / Open Item IDs | Text or linked IDs | No | Distinguish unknown, evidence gaps and conflicts |
| Parent / Related Boundary IDs | IDs | No | e.g., common wall assembly segments, optional |

The schema companion uses a JSON property contract with `snake_case` names; spreadsheet display column names above remain human-readable. The baseline project export must not infer null values from blank cells.

## Classification safeguards

- IFC/IBC classifications, local amendments, and special facility provisions are selected under the applicable **project code basis**, not by a hardcoded assumption that one edition always applies.
- `fire_wall`, `fire_barrier`, `fire_partition`, `smoke_barrier`, `smoke_partition`, `horizontal_assembly`, and `exterior_wall` are candidate code vocabulary values only where the adopted standard defines/applicably uses them. Record the exact source terminology and clause when it differs.
- A source explicitly saying “2 HR” supports a **stated rating** but not independently the classification of Fire Barrier; an unknown class remains unknown.
- A Smoke Barrier Yes/No assertion needs its own supporting evidence; absence of a symbol does not imply No.
- `not_rated` is an affirmative finding and requires evidence. Blank/null means unknown, not zero hours.
- Code classifications can overlap. Review contradictions rather than silently clearing conflicting values.

## Downstream interactions

Route-crossing detection may produce a **candidate crossing** referencing `Boundary ID`, route/segment ID, drawing intersection, and review status. It is not automatically a physical penetration or an approved firestop. The later Boundary Crossing Review evaluates construction, applicable protection requirements, responsibility and whether a penetration already exists.

Accepted boundary geometry/classification decisions must be preserved against later derived reconfiguration within their accepted scope, per [KIS Framework v1.0](../governance-and-doctrine/systems-engineering-framework-v1.md). A project-wide snapshot/baseline does not mark all boundaries accepted.

## Scope of v0.1

This contract is ready for a **manual spreadsheet/markup pilot**. It does not create a mandatory wall survey, infer fire ratings by geometry, automate CAD/PDF extraction, certify building-code classifications, determine firestop systems, or implement route intersection software. Domain processes decide when to invoke targeted or full intake.
