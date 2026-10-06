---
title: "EPS PDU Allocation Mini Playbook"
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

# EPS PDU Allocation Mini Playbook

## 1. Purpose and Use

Apply after accepted narrative and upstream micro-channel design.

## 2. Design Intent

Preserve independent operation and understandable spatial grouping.

## 3. Space / System Definition (Decision-Oriented)

Use exact selected family/model and served areas; this mini playbook specializes the LV implementation workflow.

## 4. Constraint Envelope

Use the linked hardware evidence and early AHJ/code/plenum facts. Unknown ratings remain open.

## 5. Baseline / Default Design Pattern

Input: established micro channels, assigned QDCDs and direct-lighting control requirements.

1. Keep direct-lighting PDU outputs and QDCD supply feeds explicit and separate. Direct-connected lighting under PDU network on/off control requires a purchased Smart 16/32-output version; 8-output Smart is unavailable.
2. Prefer four PDU outputs feeding four QDCD inputs for configurability. Up to four are allocated to a QDCD. Using one to three is an exception justified by load/future expectations and conserved PDU outputs. Record every output/input pair, rationale, verified available wattage, constraints, and owner decision. Manufacturer reduced-feed/internal-routing evidence is needed before acceptance; do not substitute summed lamp watts for input demand/losses/auxiliary power.
3. Check supply voltage, per-output demand/rating, PDU total demand/rating, QDCD input capacity and selected wiring. Unconfirmed values stay unknown.
4. Count required outputs from direct assignments plus feed pairs; select feasible 8/16/32 devices. Record output-count lower bounds separately from feasible selections and installed quantities. No invented spare allowance.
5. Resolve Smart preference for controller-only service and mixed direct/QDCD use before final procurement. Any approved PDU with direct network-controlled lighting must be Smart.

Output: PDU schedule, direct-lighting outputs, QDCD input-feed map, demand/capacity ledger, exact Smart selection, exceptions and open items.

## 6. Typical Variants

Record explicit alternatives and supported exceptions; no silent regrouping or invented spare policy.

## 7. Decision Gates

Resolve hardware evidence and owner locations before finalizing dependent allocations/routes.

## 8. Design Zoning / Grouping Strategy

Preserve designated channels and functional zones; count geographic increases separately from lower bounds.

## 9. Common Failure Modes

Do not confuse power feeds, driver outputs, sensors and bus devices. Unconfirmed wiring cannot establish capacity.

## 10. Safe Assumptions (and Limits)

Owner defaults are preferences, not manufacturer ratings. Unknowns stay unknown.

## 11. Documentation Expectations

Stable IDs, evidence, port/feed maps, count rationale, owner decisions and editable markups.

## 12. When to Go Deeper / Exit This Playbook

Return device conflicts upstream or obtain manufacturer clarification; retain supported scope.

## 13. Cross-Links to Supporting Knowledge

[Device and playbook index](smartdc-allocation-index.md).

## 14. Status and Stewardship

Draft; KIS Solutions; October 2026.

## 15. Author Notes (Institutional Context)

Records owner directives from 2026-10-05; no claim of manufacturer verification beyond cited supplied sheets.
