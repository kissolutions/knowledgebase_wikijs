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

The variants have different input capabilities; they are not interchangeable four/eight-port versions of the same analog interface.

| Device | Maximum device/input connections | Signal capability | Network |
|---|---:|---|---|
| SW8 | 8 | On/off devices: programmable momentary or maintained dry-contact inputs | One networkable SDCnet interface device |
| SW4 | 4 | Analog 0–10 V inputs; manufacturer also permits momentary/maintained dry-contact configuration | One networkable SDCnet interface device |

Owner clarification, 2026-10-26, is corroborated by the manufacturer [SDCnet Interfaces page](https://smartdclighting.com/product/sdcnet-interfaces/) and [SW4/SW8 specification sheet](https://smartdclighting.com/wp-content/uploads/2026/10/SMARTDC-SW4SW8-Specsheet.pdf), catalog descriptions on PDF p. 2 (retrieved 2026-10-26). Both variants provide input LED-status outputs; two RJ45 connections support SDCnet daisy-chaining. Do not treat SW8 as an eight-input 0–10 V interface.

Exact selected-sensor electrical compatibility, interface/sensor power demand, mounting/plenum ratings and wiring rules still require the applicable installation evidence. Input capacity does not prove that a multi-function sensor consumes only one connection; account for each required signal.

## 3. Interfaces and Integration

SDCnet RJ45 connection back toward CIO. Prefer local ceiling/wall-panel locations near related QDCDs, subject to selected-device installation ratings. Wired physical sensors/controls connect through a compatible signal input: dry-contact on/off to SW8, analog 0–10 V to SW4. SW4 dry-contact use is supported where deliberately configured. Count one physical SW module as a network device, separately from its attached inputs; retain the verified addressing/bus-unit basis. Casambi devices are counted separately and do not consume these wired inputs.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Do not borrow QDCD/CIO mounting ratings or sensor specifications for SW devices. Do not count eight inputs as eight bus devices. Do not pack 0–10 V signals into spare SW8 ports, infer 0–10 V sink/source compatibility from the label alone, or assume a powered sensor's on/off output is a compatible dry contact. Verify actual terminals, power budget and signal mapping.

## 9. Ecosystem and Related Devices

[Sensor/CIO allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [CIO](smartdc-cio.md)

## 10. Cost and Commercial Reality (Order-of-Magnitude)

Pricing not established; do not invent prices.

## 11. Procurement and Availability

Confirm exact variant, firmware, lead time and accessories with vendor.

## 12. Selection and Sizing Considerations (Rules of Thumb)

Size on/off and analog signal pools separately. Eight compatible on/off connections can fill one SW8; four compatible 0–10 V connections can fill one SW4. A mixed eight-device list is not automatically one SW8. Geographic and independent-control requirements can increase installed counts above signal-capacity lower bounds. See the linked mini playbook.

## 13. Commissioning and Validation Considerations

Reconcile equipment/port IDs with drawings; test every approved control association, configuration and applicable fail/emergency behavior.

## 14. Lifecycle, Maintenance, and Longevity

Record as-built location, port map and configuration; maintenance requirements beyond supplied sheets remain unconfirmed.

## 15. Operational Mechanics

Do not infer signal precedence, reduced-input routing, failure state or emergency operation. Obtain applicable wiring/configuration evidence.

## 16. Cross-links and Navigation

[Sensor/CIO allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [CIO](smartdc-cio.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-26; steward KIS Solutions. Signal-capability clarification is now manufacturer-corroborated by the linked product page and specification sheet. Owner placement/design directives remain separate from product evidence; no complete installation or compatibility certification is implied.
