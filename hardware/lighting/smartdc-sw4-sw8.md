---
title: "SmartDC SW4 / SW8 sensor aggregators"
page_type: product_class
page_status: draft
confidence_level: medium
domain_primary: low-voltage-lighting
ai_role: prescriptive_standard
invocation_triggers:
  systems_present: [low_voltage_lighting, smartdc]
decision_axes: [power_allocation, controls, equipment_placement, owner_review]
related_pages:
  - "https://github.com/kissolutions/knowledgebase_wikijs/blob/main/design-playbooks/smartdc-allocation-index.md"
---

# SmartDC SW4 / SW8 sensor aggregators

## 0. Purpose and Scope

Local SDCnet / SDCBus sensor aggregators. Normalize owner SDbus/SDnet spelling to SDCnet/SDCBus while preserving source terminology.

## 1. Core Function

Local SDCnet / SDCBus sensor aggregators. Normalize owner SDbus/SDnet spelling to SDCnet/SDCBus while preserving source terminology.

## 2. Capabilities and Variants (What Is Possible)

Owner-provided capacities: SW4 four wired sensor inputs; SW8 eight. Supplied QDCD/CIO topology shows SW4/SW8 on SDCnet, but dedicated device sheets are not supplied. Port compatibility, current demand, bus-device counting, mounting/plenum ratings and wiring rules remain unconfirmed.

## 3. Interfaces and Integration

SDCnet RJ45 connection back toward CIO. Prefer local ceiling/wall-panel locations near related QDCDs, subject to selected-device installation ratings. Wired physical sensors connect to aggregator ports; Casambi devices are counted separately.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Do not borrow QDCD/CIO mounting ratings or sensor specifications for SW devices. Do not count eight ports as eight bus devices; verify actual counting with manufacturer.

## 9. Ecosystem and Related Devices

[Sensor/CIO allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [CIO](smartdc-cio.md)

## 10. Cost and Commercial Reality (Order-of-Magnitude)

Pricing not established; do not invent prices.

## 11. Procurement and Availability

Confirm exact variant, firmware, lead time and accessories with vendor.

## 12. Selection and Sizing Considerations (Rules of Thumb)

Device constraints feed the linked mini playbook. Geographic and control requirements can increase installed counts above lower bounds.

## 13. Commissioning and Validation Considerations

Reconcile equipment/port IDs with drawings; test every approved control association, configuration and applicable fail/emergency behavior.

## 14. Lifecycle, Maintenance, and Longevity

Record as-built location, port map and configuration; maintenance requirements beyond supplied sheets remain unconfirmed.

## 15. Operational Mechanics

Do not infer signal precedence, reduced-input routing, failure state or emergency operation. Obtain applicable wiring/configuration evidence.

## 16. Cross-links and Navigation

[Sensor/CIO allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [CIO](smartdc-cio.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-06; steward KIS Solutions. Owner directives are design policy, separately identified from manufacturer evidence.
