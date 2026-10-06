---
title: "SmartDC / EPS Device Allocation Index"
page_type: playbook
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

# SmartDC / EPS Device Allocation Index

## Purpose and Authority

KIS owner directives approved in the 2026-10-05 discussion; manufacturer facts are separately attributed in the product pages. The three supplied SmartDC sheets are project-source evidence, not added to Git. SW and EPS data without dedicated sheets remains owner-provided. Draft guidance can support supervised review, not unqualified construction release.

| Hardware page | Device mini playbook |
|---|---|
| [QDCD](../hardware/lighting/qdcd.md) | [Assign existing channels](qdcd-channel-assignment.md) |
| [EPS PDU](../hardware/lighting/eps-pdu.md) | [Allocate supply outputs](eps-pdu-allocation.md) |
| [CIO](../hardware/lighting/smartdc-cio.md), [SW4/SW8](../hardware/lighting/smartdc-sw4-sw8.md) | [Allocate sensors, buses and CIOs](smartdc-sensor-cio-allocation.md) |

LV extension owns project records, sequence, markup and companion topology contract: [implementation workflow](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/controller-power-placement.md). Future controller families receive their own hardware pages/mini playbooks; do not universalize QDCD/EPS limits.

## Open Verification Items

Dedicated SW4/SW8 and EPS sheets; SW power/input compatibility/listings/device-count rules; QDCD direct sensor capacity and wired/wireless limits; reduced-feed/internal aggregation; CIO/Casambi precedence; precise bus distance/branch/termination rules; PDU command/API vs SNMP notification behavior; controller-only Smart and mixed PDU policy; practical lamp/feed route and voltage-drop limits; expansion/spare policy. Unknowns block only the dependent conclusion. CIO owner location is required before final routes.
