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

KIS owner directives from 2026-10-05 and hardware/architecture clarifications from 2026-10-26; manufacturer facts are separately attributed in the product pages. Supplied project-source sheets remain outside Git; public manufacturer links support reusable product facts. SW4/SW8 signal capacities are now corroborated by the manufacturer page/specification sheet. EPS data without dedicated evidence remains owner-provided. Draft guidance can support supervised review, not unqualified construction release.

| Hardware page | Device mini playbook |
|---|---|
| [QDCD](../hardware/lighting/qdcd.md) | [Assign existing channels](qdcd-channel-assignment.md) |
| [EPS PDU](../hardware/lighting/eps-pdu.md) | [Allocate supply outputs](eps-pdu-allocation.md) |
| [CIO](../hardware/lighting/smartdc-cio.md), [SW4/SW8](../hardware/lighting/smartdc-sw4-sw8.md) | [Allocate sensors, buses and CIOs](smartdc-sensor-cio-allocation.md) |

LV extension owns project records, sequence, markup and companion topology contract: [implementation workflow](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/controller-power-placement.md). Future controller families receive their own hardware pages/mini playbooks; do not universalize QDCD/EPS limits.

## Open Verification Items

| Item | Current evidence / action |
|---|---|
| `CIO-PORT-FANIN` | CIO has eight direct sensor ports with one aggregated isolated-room scene/group per port. Maximum sensors per port is unknown; possible four remains a question. Obtain supported models, combining/wiring and power limits. |
| `CIO-QDCD16-FW` | Owner reports 2026 firmware expansion from 8 to 16 QDCDs per CIO. Obtain updated datasheet/release evidence and record installed firmware/applicability; keep this distinct from the already documented 16 SDCnet peripherals. |
| SW4/SW8 | Input distinction confirmed: four 0–10 V inputs vs eight on/off dry-contact inputs; SW4 also permits dry-contact configuration. Selected sensor electrical compatibility, power, listings and exact installation/addressing rules still need applicable evidence. |
| QDCD control variants | Integral Casambi is variant-specific. All-Casambi small systems may omit CIO/SW signal hardware; wired sensor paths use their controlling CIO. Verify exact profiles, pairing, power, required features and mixed command precedence. No native QDCD wired input capacity is established. |

Other open items: dedicated EPS evidence; reduced-feed/internal aggregation; precise bus distance/branch/termination rules; PDU command/API vs SNMP notification behavior; controller-only Smart and mixed PDU policy; practical lamp/feed route and voltage-drop limits; expansion/spare policy. Unknowns affect only the dependent conclusion. For a CIO-based design, owner location is required before final routes; a supported all-Casambi option has no invented CIO requirement.

## Larger-Fixture EPS Power Aggregation

For single fixtures above 95 W, review the [EPS fixture power aggregation directive](eps-pdu-allocation.md#eps-fixture-power-aggregation--owner-directive-2026-10-06): 1–4 Class 2 feeds, one combined fixture output, inside the fixture housing, restricted to on/off nominal 48 VDC CV. Count every feed and keep all feeds in the same approved control group. Sensor aggregators are separate. Current model support is pending; retain design candidates with a feed ledger rather than forcing them into ordinary single-channel limits.

The allocation decision tree starts when a **single fixture exceeds 95 W**. Dimming is a hard incompatibility with the typical aggregator path. A compatible on/off 48 VDC CV fixture becomes one dedicated combined-power LV micro zone with one aggregator output and the necessary 1–4 upstream channels. See [decision tree](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/design-playbooks/eps-pdu-allocation.md#oversized-single-fixture-decision-tree-and-micro-zone).

## Open Framework Item: Exterior Lighting

**Status: unresolved. Owner flag: 2026-10-06.**

Exterior lighting needs dedicated framework guidance: scope and area/fixture classification, applicable lighting-control/code review and narrative, compatible power/driver selection, outdoor equipment/installation evidence and coordination with the LV implementation workflow. Do not infer an exterior control sequence or equipment suitability from existing interior guidance.

Low-opacity wine/burgundy exterior map fill is an accepted presentation directive, not a completed exterior-lighting design rule. Track implementation and review deliverables in the [LV workflow open item](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/lv-project-workflow-and-readiness.md#open-framework-item-exterior-lighting).

## Separate Upstream and Downstream Voltage-Drop Budgets

Record a separate budget and basis for each side of a converting/controller device. The upstream review checks actual input voltage under load, input demand including losses/auxiliaries, selected-device operating/conversion limits and required output capability. A wide input range alone does not prove the required output is available throughout that range. Within the verified operating envelope, evaluate efficiency, conductor heating and installation conditions when choosing a budget.

Downstream, check the selected fixture interface and wiring arrangement: CV input tolerance and CC driver compliance/headroom require their applicable evidence. Do not transfer a downstream percentage upstream and label it universally required. Preserve both budgets, source/output voltage, actual per-circuit current, route length, conductor resistance basis and unresolved evidence.

The proposed 6% upstream and 3% downstream figures remain unapproved options, not defaults. Paralleled conductors, cable construction, terminal acceptance, protection and bundle/ambient conditions require applicable manufacturer/installation verification before reliance. Do not treat resistance-equivalent gauge as physical conductor size or terminal/listing approval. This doctrine partially defines the review method; it does not close the practical route/drop verification item.


## Shared Class 2 Cable Selection

Use the general [Class 2 cable-selection playbook](class-2-cable-selection.md), [regulatory basis](../ontology/reg-and-class/class-2-circuit-cabling.md), and [multi-vendor catalog](../hardware/cabling/class-2-cable-catalog.md). These belong to the shared electrical knowledgebase. Actual feed demand governs; the catalog's six-pair/four-active example does not reinstate a fixed four-feed requirement. Product evidence does not resolve pending voltage-drop budgets, terminal paralleling or installed routing calculations.
