---
title: "EPS Class 2 PDU"
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

# EPS Class 2 PDU

## 0. Purpose and Scope

Power distribution unit supplying direct lighting or QDCD power inputs.

## 1. Core Function

Power distribution unit supplying direct lighting or QDCD power inputs.

## 2. Capabilities and Variants (What Is Possible)

Owner-provided family information: 8, 16 or 32 Class 2 outputs. Eight-output version cannot be Smart; 16/32 versions can be purchased Smart. Smart provides network management/programming/monitoring. EPS manufacturer specification sheets have not been supplied; output voltage, per-output watts, input/aggregate power, monitoring/control commands, listing and placement ratings require evidence. Nominal 100 W Class 2 project channel profile does not prove a PDU rating.

## 3. Interfaces and Integration

Direct lighting under PDU network on/off control requires Smart under owner policy; typically CV on/off applications. Owner describes external Ethernet software/sensors and SNMP traps; traps are notifications, and the actual switching command path/API is unconfirmed. QDCD dimming/complex controls use separate supply-output-to-input mappings.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Do not count four QDCD output channels as four PDU allocations automatically. Do not assume 8/16/32 times 100 W is supported aggregate power. Smart preference for controller-only loads and permission for mixed direct/QDCD use remain owner decisions.

## 9. Ecosystem and Related Devices

[EPS PDU allocation mini playbook](../../design-playbooks/eps-pdu-allocation.md) · [QDCD](qdcd.md)

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

[EPS PDU allocation mini playbook](../../design-playbooks/eps-pdu-allocation.md) · [QDCD](qdcd.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-06; steward KIS Solutions. Owner directives are design policy, separately identified from manufacturer evidence.

## Fixture Power Aggregator Accessory

Owner directive dated 2026-10-06: an EPS fixture power aggregator combines 1–4 separate Class 2 supply inputs into one output, up to an owner-stated 400 W, inside a fixture housing. This supports larger nameplate fixtures, particularly high bays. KIS reserves it for on/off-only nominal 48 VDC constant-voltage operation through EPS outputs; no dimming or constant-current use. Input count follows fixture demand and verified feed/aggregate constraints, not an automatic four-feed allocation. It is distinct from sensor aggregators and from QDCD's four lighting outputs. The exact product specification is not yet verified. See [allocation directive](../../design-playbooks/eps-pdu-allocation.md#eps-fixture-power-aggregation--owner-directive-2026-10-06) for feed counting, coordinated on/off control, evidence and current model-support limits.

The allocation decision tree starts when a **single fixture exceeds 95 W**. Dimming is a hard incompatibility with the typical aggregator path. A compatible on/off 48 VDC CV fixture becomes one dedicated combined-power LV micro zone with one aggregator output and the necessary 1–4 upstream channels. See [decision tree](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/design-playbooks/eps-pdu-allocation.md#oversized-single-fixture-decision-tree-and-micro-zone).
