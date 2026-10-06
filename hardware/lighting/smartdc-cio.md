---
title: "SmartDC SDCS CIO"
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

# SmartDC SDCS CIO

## 0. Purpose and Scope

Lighting system controller and sensor/data hub; PDnet to QDCDs, SDCnet to sensor peripherals.

## 1. Core Function

Lighting system controller and sensor/data hub; PDnet to QDCDs, SDCnet to sensor peripherals.

## 2. Capabilities and Variants (What Is Possible)

Supplied SMARTDC-SDCS-CIO Specification Sheet pp. 1–3: up to eight QDCDs and sixteen SDCnet devices per CIO; topology shows 250 ft maximum distance from CIO on each network. Input via PDnet RJ45 at nominal 48 VDC. SDCnet output 24 VDC, 250 mA maximum combined across both ports; standby <1 W. Not plenum rated; 0–45°C, noncondensing 0–95% RH. Ethernet 10/100 and REST API listed. Page 2 documents eight sensor inputs; retain supported dry-contact, 0–10 V dimming and 0/24 V sensor interfaces subject to exact wiring instructions.

## 3. Interfaces and Integration

Receives power from a nearby QDCD via PDnet and distributes power/data to daisy-chained SDCnet devices (sheet p. 1). Trace CIO/control and peripheral demand into the power budget; do not hide it inside lamp watts. RJ45 appearance does not establish Ethernet interchangeability. Distinguish PDnet, SDCnet and Ethernet.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Sixteen bus devices are not sixteen sensors. Do not assume sixteen peripherals fit the 250 mA budget. Exact branching/termination, combined route interpretation and Casambi interaction remain verification items.

## 9. Ecosystem and Related Devices

[CIO/sensor allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [QDCD](qdcd.md) · [SW4/SW8](smartdc-sw4-sw8.md)

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

[CIO/sensor allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [QDCD](qdcd.md) · [SW4/SW8](smartdc-sw4-sw8.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-06; steward KIS Solutions. Owner directives are design policy, separately identified from manufacturer evidence.
