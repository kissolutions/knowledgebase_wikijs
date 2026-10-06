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

## Larger-Fixture EPS Power Aggregation

For single fixtures above 95 W, review the [EPS fixture power aggregation directive](eps-pdu-allocation.md#eps-fixture-power-aggregation--owner-directive-2026-10-06): 1–4 Class 2 feeds, one combined fixture output, inside the fixture housing, restricted to on/off nominal 48 VDC CV. Count every feed and keep all feeds in the same approved control group. Sensor aggregators are separate. Current model support is pending; retain design candidates with a feed ledger rather than forcing them into ordinary single-channel limits.

The allocation decision tree starts when a **single fixture exceeds 95 W**. Dimming is a hard incompatibility with the typical aggregator path. A compatible on/off 48 VDC CV fixture becomes one dedicated combined-power LV micro zone with one aggregator output and the necessary 1–4 upstream channels. See [decision tree](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/design-playbooks/eps-pdu-allocation.md#oversized-single-fixture-decision-tree-and-micro-zone).

## Open Framework Item: Exterior Lighting

**Status: unresolved. Owner flag: 2026-10-06.**

Exterior lighting needs dedicated framework guidance: scope and area/fixture classification, applicable lighting-control/code review and narrative, compatible power/driver selection, outdoor equipment/installation evidence and coordination with the LV implementation workflow. Do not infer an exterior control sequence or equipment suitability from existing interior guidance.

Low-opacity wine/burgundy exterior map fill is an accepted presentation directive, not a completed exterior-lighting design rule. Track implementation and review deliverables in the [LV workflow open item](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/lv-project-workflow-and-readiness.md#open-framework-item-exterior-lighting).
