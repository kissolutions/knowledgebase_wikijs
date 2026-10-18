---
title: "Standard Lighting Control Sequences — SEQ Registry"
description: "Canonical KIS standard SEQ namespace, candidate index, and assignment contract"
published: true
tags: [lighting, controls, sequence, standards, M3]
editor: markdown
page_type: reference
page_status: draft
confidence_level: medium
domain_primary: electrical-lighting
ai_role: prescriptive_standard
related_pages:
  - lighting-control-application-guide.md
  - lighting-controls-guidance-index.md
  - room-classification-and-controls-review-playbook.md
  - iecc-occupant-sensor-directives.md
---

# Standard Lighting Control Sequences — SEQ Registry

## Contract and authority

**`SEQ-###` is reserved exclusively for a KIS framework *standard lighting control sequence*.** A `SEQ-` identity means the definition is managed and versioned in this shared knowledgebase; it does **not** assert that its draft contents are approved for application or automatically code-compliant. **Only `status: approved` definitions are selectable as standard designs without first authoring/approving the definition.** Every application still requires project code and source-intent checks.

A custom sequence created for a single project stays in that project's sequence register and **must not take a `SEQ-###` number**. Suggested project-specific namespace is `PSEQ-###` scoped by project identity; these IDs are distinct from the global KIS sequence registry. A project sequence may later be proposed for standardization; promoting it requires review and allocation of a new `SEQ-` ID, not a silent reinterpretation of the project identity.

`SEQ-` identifies a **behavioral control sequence**, not a room type, lighting device, controller type, zone, or energy-code edition. Reuse one sequence across qualifying spaces and code profiles where its explicit parameters, exceptions and verified functions match. Fix the sequence revision for each adopted assignment.

## Initial standard sequence index — reserved drafts

These numbers are **reserved KIS standard library slots** informed by the current [Application Guide](lighting-control-application-guide.md), [Enclosed Office Playbook](enclosed-office-lighting-controls-playbook.md), [Open Office Playbook](open-office-lighting-controls-playbook.md) and [IECC draft directives](iecc-occupant-sensor-directives.md). **None of the entries below is yet an approved, complete standard sequence or verified code recipe.** Titles are intended behavior families for initial development, not unconditional prescribed operation.

| Standard ID | Candidate functional sequence | Possible uses / matching cues | Status |
|---|---|---|---|
| `SEQ-001` | Manual ON, occupancy-based automatic OFF | Enclosed office and other supported sensor-controlled spaces | **Reserved — draft** |
| `SEQ-002` | Limited automatic ON, occupancy-based automatic OFF | Permitted partial-ON applications | **Reserved — draft** |
| `SEQ-003` | Full automatic ON, occupancy-based automatic OFF | Only where full-ON behavior is expressly permitted | **Reserved — draft** |
| `SEQ-004` | Time-switch scheduled shutoff with manual override | Appropriate time-switch-controlled areas | **Reserved — draft** |
| `SEQ-005` | Occupancy-based reduction on vacancy | Corridor or other verified reduction applications | **Reserved — draft** |
| `SEQ-006` | Independent occupancy-zone response with shared aggregate conditions | Open offices requiring independently controlled areas | **Reserved — draft** |
| `SEQ-007` | Occupancy reduction plus scheduled complete shutoff | Warehouse applications where both functions apply | **Reserved — draft** |

**Do not auto-assign the draft slots.** The descriptions above are placeholders for authored, verified narrative/function contracts. Numeric requirements, permitted full-ON behaviors, group sizes, timings, exceptions, daylight and emergency interactions depend on the selected and verified code basis. The same ID must not be repurposed for fundamentally different behavior once approved.

## Required content for each approved SEQ definition

- **Identity:** `sequence_id`, stable revision, title, owner, status and adoption history.
- **Behavior:** operating narrative and explicit manual activation/deactivation, occupancy/vacancy, Light Reduction, time-switch, daylight and emergency/interface functions; distinguish `none`, `not_applicable` and `unknown`.
- **Parameters:** defaults and permissible ranges/conditions (e.g., timeout), with units and governing code constraints. A parameter value does not create a new SEQ unless the behavioral contract materially differs.
- **Required inputs/outputs:** occupancy presence, manual inputs, schedule/override signals, daylight measurements or parent aggregation signals as needed; commanded luminaire groups and independently controlled outputs.
- **Applicability:** appropriate energy-code space use, independently reviewed building/energy classification inputs, enclosure/area/geometry triggers, edition/standard profiles, amendments, prohibitions and exceptions. These are *matching* filters, not an assertion of jurisdiction-wide adoption.
- **Code evidence:** verified primary provisions or reviewed code profile, source version, applicability conditions and open verification exceptions. Approval as a KIS standard never waives local code review.
- **Zone interface:** required endpoint (leaf) zone behavior and any dependencies on shared/parent conditions. A SEQ **attaches to endpoint zones only**. Parent nodes have no SEQ and own neither direct Light Objects nor controller/power outputs. Parent occupancy aggregation remains a distinct hierarchy/coordination contract.
- **Physical implementation limits:** sensing coverage, physical output independence, possible overlapping daylight control relationships, interactions and verified product dependencies. A zone-count rule does not directly assign a sensor count.
- **Verification:** expected state transitions, checkable acceptance tests, conflict/exclusion rules, author/reviewer/date and approval decision.

## M3 sequence matching and authoring

1. Obtain reviewed room name/use, Building Code Space Type and Occupancy Group, **separately** reviewed Energy Code Space Type, geometry/area/daylight conditions, source MEP control functions and selected jurisdiction/code edition/amendments.
2. Determine required control behavior by function from verified applicable code provisions and documented source intent; preserve uncertainties rather than filling them from a candidate library entry.
3. Search **approved** `SEQ-` revisions and rank candidates by applicability and satisfaction of all required functions, including independent subzone behavior, daylight and emergency interaction. Report why candidates match and where they do not.
4. Present proposed endpoint-zone `SEQ-` assignments for owner selection/adoption; preserve the original source MEP scheme and obtain appropriate authority for departures. **Do not assign a SEQ to a parent zone.**
5. The owner may author or direct a new **project sequence** with a project-scoped `PSEQ-` identity, verify its behavior against selected code requirements, and assign it to one or more endpoint zones. Project custom sequences are not presumed KIS standards. A custom sequence may be promoted to a `SEQ-` only through separately recorded framework standard review.
6. M3 narrative review groups by sequence identity and revision: render **one complete narrative section per sequence**, then the room/endpoint-zone assignment table. Reuse text by reference; project parameters and approved owner overrides remain visible per endpoint assignment.
7. M4 instantiates zone geometries, Light Point memberships, compatible controller outputs and devices from accepted endpoint sequences and explicit hierarchical/overlay relationships. Do not create mandatory zones during M1 room extraction.

**Hierarchy invariant:** parent zones coordinate or aggregate children; **only leaves execute a SEQ**. The current [LV zone hierarchy v0.7](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/ontology/canonical-model/zone-hierarchy-v0.7.md) supports parent/child representation but does **not yet** enforce leaf `sequence_id` references. Daylight overlays can intersect occupancy subzones; do not force intersecting control areas into a single exclusive tree or duplicate fixtures.

## Readiness and next work

This file creates a **central index and authority rule**, not seven ready-to-run designs, a code compliance engine or a new canonical schema. Next: develop and source-verify individual `SEQ-` records, owner-review/approve them, then add a versioned endpoint `sequence_id`/revision association and validation in the LV domain. For now, record references in M3 review evidence without inserting unsupported schema keys.

**Owner:** KIS Solutions. **Status:** Draft standard registry, 2026-10-17.
