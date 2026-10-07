---
title: "SmartDC Sensor and CIO Allocation Mini Playbook"
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

# SmartDC Sensor and CIO Allocation Mini Playbook

## 1. Purpose and Use

Apply after accepted narrative and upstream micro-channel design.

## 2. Design Intent

Preserve independent operation and understandable spatial grouping.

## 3. Space / System Definition (Decision-Oriented)

Use exact selected family/model and served areas; this mini playbook specializes the LV implementation workflow.

## 4. Constraint Envelope

Use the linked hardware evidence and early AHJ/code/plenum facts. Unknown ratings remain open.

## 5. Baseline / Default Design Pattern

Input: physical sensor/device inventory, control associations, geographic channel/QDCD clusters and early plenum/code/AHJ facts.

1. Count unique physical sensors, separately wired and Casambi; also count wall controls separately so they are not mislabeled sensors. A sensor serving several channels/zones is counted once. Do not infer coverage or omit a required sensor from a capacity calculation.
2. Default wired sensor aggregation to SDCnet SW8/SW4. For S compatible wired sensor ports, ceiling(S/8) is a global device-count lower bound when SW8 is suitable; choose the smallest suitable SW4/SW8 mix geographically. Device count alone can have multiple mixes (e.g. nine sensors: two SW8 or SW8+SW4). Do not invent a cost/spare objective. Report global and local feasible counts separately; direct CIO inputs are an explicit design alternative, not the default.
3. Count SW devices and all other SDCnet peripherals using verified bus-counting rules. Casambi counts stay separate. For a CIO-based arrangement, ceiling(QDCD count/8) and ceiling(SDCnet device count/16) are lower bounds; feasible CIO count must also satisfy location, 250 ft routing and combined 250 mA bus power.
4. Critical owner question: where should CIOs be located? Prefer owner-designated IDF, Electrical or Storage rooms. Record proposed rooms until owner answers; dependent routes remain provisional.
5. From the furthest field devices work back toward the CIO to propose reasonable sensor strings. Place aggregators near associated QDCDs, favoring the QDCD closest to CIO within the associated group. Locate SW4/SW8 in nearby ceiling/wall panels only after ratings are confirmed.
6. After devices are placed, route SDCnet/SDCBus to SW4/SW8/peripherals and PDnet from CIO to/between QDCDs under their respective manufacturer specifications. Keep buses distinct. Follow documented daisy-chain connections, CAT5e Class 2 conventions, gauge/power rules, lengths, connectors, termination and permitted branches; do not invent unsupported star topology. Confirm the precise 250 ft distance interpretation before finalizing cumulative strings.
7. Show strings, numbered devices, route IDs and CIO association on the plan; check every physical connection and functional sensor/zone relationship. Owner reviews location and route markups.

Output: sensor totals and port ledger, aggregator and bus-device counts, CIO allocation, bus power/distance budget, minimum-vs-installed explanation and owner questions.

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

## Input from Earlier Room-Device Review

Room sensors/manual controls are identified, scheduled and provisionally located immediately after narrative lock. Use owner-returned device positions as inputs to aggregator clustering, CIO coordination and bus routing. Preserve Device IDs and parent/child zone associations; physical devices are counted once. Initial positions follow the LV milestone playbook: wall switches/scene controllers/dimmers at source electrical lighting-plan positions first (accepted owner locations prevail), with door/entry/glazing rules used only without a usable source location, ceiling occupancy sensors near served room/child-zone centers (tile-centered when a grid is visible), wall occupancy sensors at plan top-left corner placeholders, and corridor sensors near served-zone midpoints. Preserve source sheet/revision/symbol references, register positions to the accepted working frame, and flag conflicting/uncertain source locations instead of silently replacing them with a fallback. Provisional positions do not establish sensor coverage or final cable lengths. [Placement rules](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md#provisional-room-device-placement).
