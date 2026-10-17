---
title: Equipment and Device Register Model
description: Physical equipment accountability, device identity, membership and BOM boundaries
published: false
date: 2026-10-15T00:00:00.000Z
tags: governance, equipment, devices, bom
editor: markdown
dateCreated: 2026-10-15T00:00:00.000Z
---

# Equipment and Device Register Model (draft v0.1)

## Purpose and boundary

One **DEVICE LIST** worksheet/register tracks physical **Equipment** and **Devices** that are materially relevant to a project. This is an engineering accountability register, **not** a procurement-only BOM, a complete plant inventory, an I/O point list, or a software/scope activity list.

Include an existing, new, furnished-by-others, or proposed physical record when:
- The source documents explicitly tag it and assign an actual, possible, disputed, or unresolved project scope (e.g., TAB, rebalancing, relocation).
- KIS/contractors purchase, install, modify, wire, configure, program, commission, monitor, control, or integrate it.
- The physical item has a scope dependency requiring its own identity or technical/contractual accountability.

Do not insert unrelated owner infrastructure, pre-existing remote SCADA servers, a purely virtual network interface, software objects, design tasks, RFIs, speculative components, or implied controllers for equipment whose internals are outside scope. An existing networked device can be included **when it itself is the physical item being integrated**, even if supplied by others.

## Record Type (required for populated records)

**Equipment:** An identifiable physical functional assembly/package, often with a source drawing equipment tag. Examples: DD1.24 VAV box, existing DD1.23 VAV box with TAB-only scope, complete pump package, fabricated DDC panel. Equipment may have no child device records, because only the relevant internals are tracked. Equipment may itself be a procured item.

**Device:** A separately identifiable physical component whose procurement, installation, connection, wiring, commissioning, configuration, programming, monitoring, integration or scoped work warrants a distinct record. Examples: KMC BAC-9001A, KMC TSP-8003, VFD, DP transmitter, UPS with I/O. Existing controllers count when directly subject to work. Devices need not be network-addressable or standalone and do not require a parent.

Do not equate Equipment with a procurement grouping or Device with a network endpoint. One equipment package may contain one DDC controller plus non-network-addressed remote I/O.

## Identity and relationships

- **Internal ID:** stable project-local identity; preserve accepted IDs during reclassification. Never conflate this with drawing tag, SCADA name or owner's asset tag.
- **Source Document Tag**, **Operational / SCADA Name**, and **Owner Asset Tag:** separate optional peer attributes.
- **Record Type:** Equipment | Device.
- **Parent Internal ID:** optional relationship for *actual physical membership* of a Device within an Equipment. Referenced parent must exist uniquely and have Record Type=Equipment. Cannot point to itself. Do not create parents solely to group procurement or communication connections.
- Do not use Parent ID for *serves*, *communicates with*, *wired to*, or project-wide subsystem membership. Those are relationships in controls/I/O documentation, not assembly containment.
- **Scope and confidence:** concise field values. Do not duplicate decision history, BOM items, assumptions and RFIs in every cell. Keep detailed discussions in Scope Review, RFIs and evidence.

## Worked examples

| Internal ID | Record Type | Source tag / description | Parent ID | Tracking reason |
| --- | --- | --- | --- | --- |
| D-11 | Equipment | DD1.24 dual-duct VAV box | — | Tagged functional equipment with controls scope |
| D-12-A | Device | BAC-9001A | D-11 | Physical DDC controller supplied and programmed |
| D-12-B | Device | TSP-8003 | D-11 | Physical hardwired actuator/airflow I/O supplied and connected |
| D-15-A | Equipment | DD1.69 dual-duct VAV box | — | Existing tagged equipment with TAB / scope question |
| D-15-B | Equipment | DD1.23 dual-duct VAV box | — | Existing tagged equipment with TAB / scope question |
| D-20 | Device | UPS | — | Physical UPS furnished, with an I/O monitoring interface |

These are examples from a *working* project model and do not override project-specific owner acceptance. Do not invent internal DD1.23/DD1.69 controllers where internal device work is not established.

A DDC panel can be Equipment containing BAC controller, I/O module, UPS, etc., when their membership is physical and the panel itself is a genuine assembly. A UPS positioned next to, rather than within, the panel does not automatically have that panel as parent.

## BOM and I/O separation

- Equipment may be purchased complete, or fabricated using component purchases. **BOM is a separate, orderable line-item dataset**, related to Device List records when applicable.
- The mere presence of parent and child records does not authorize purchasing both a complete assembly and all its included components. Use procurement responsibility, BOM scope/quantity and package composition to prevent double-counting.
- Components such as DIN rail and terminal blocks need not have Device records unless separately tracked because of engineering scope; they may appear only on an assembly BOM.
- I/O point records link to the appropriate real physical Device/controller/endpoint and retain their own Internal Point IDs. An equipment source tag can exist without a point list.

## Extraction, validation and acceptance

Capture what drawings and scope establish. Do not fabricate technical characteristics merely to fill empty fields. Preserve provenance and selection confidence separately from acceptance. A classification or parent relationship produced by an agent remains provisional until approved under Engineering State and Milestone Acceptance.

Validations: populated Record Type is Equipment or Device; populated Parent Internal ID references one unique Equipment record other than self; duplicate populated Internal IDs are invalid. Blank Parent ID is normal.

## Domain extension boundary

This is a cross-domain register ontology and inclusion rule. Domain-specific takeoff steps, installation requirements, engineering sequences, and BOM pricing logic belong in domain playbooks/repositories.
