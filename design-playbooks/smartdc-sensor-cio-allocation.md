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

Input: physical sensor/device inventory, required signal types, approved scene/control-group associations, selected Casambi/non-Casambi QDCD variants, geographic channel/QDCD clusters and early plenum/code/AHJ facts. Choose CIO-based, mixed wired/Casambi or all-Casambi control architecture explicitly; a CIO is not mandatory solely because QDCDs are present.

1. Count unique physical sensors, separately wired and Casambi; also count wall controls separately so they are not mislabeled sensors. A sensor serving several channels/zones is counted once. Do not infer coverage or omit a required sensor from a capacity calculation.
2. For wired SDCnet aggregation, use **SW8 for up to eight compatible on/off dry-contact inputs** and **SW4 for up to four 0–10 V inputs**; SW4 may also be deliberately configured for dry contacts. Size the signal pools separately, not every sensor as interchangeable: for A analog inputs, ceiling(A/4) is an SW4 lower bound. Allocate compatible remaining on/off inputs to suitable spare SW4 inputs or SW8s (eight per SW8), preserving function/geography. Count every required input of a multi-signal sensor. Do not invent a cost/spare objective. Direct CIO inputs are a distinct alternate path: **eight ports, one isolated-room scene/control group per port**, with compatible attached sensors acting as one group. Maximum sensors per port is unknown; possible four is an open question, not sizing capacity. Keep independent rooms/daylight groups on independent inputs.
3. Count CIO-connected QDCDs separately from all-Casambi QDCDs that do not use a CIO. Count each SW module and other SDCnet peripheral separately from attached sensors, retaining the verified bus-unit/addressing basis. For a CIO-based arrangement with uniform applicable QDCD capacity C, ceiling(CIO-connected QDCD count/C), ceiling(SDCnet peripheral count/16) and, when direct CIO inputs are used, ceiling(independent direct-port group count/8) are count lower bounds. **C=8** is the legacy documented QDCD basis; **C=16** is the owner-reported 2026 firmware-dependent basis, requiring explicit project applicability/firmware evidence and pending updated manufacturer confirmation. Mixed firmware needs CIO-by-CIO allocation, not a blanket global divisor. Do not silently split a supported owner-directed 16-QDCD candidate merely because an older sheet/checker says eight, or certify unverified legacy equipment for sixteen. Location, 250 ft routing and combined 250 mA SDCnet power remain separate constraints.
4. For each required CIO, establish its location with the owner. Prefer owner-designated IDF, Electrical or Storage rooms. Record proposed rooms until owner answers; dependent routes remain provisional. For an approved all-Casambi control path, record no CIO requirement rather than inventing a location or wired bus.
5. From the furthest field devices work back toward the CIO to propose reasonable sensor strings. Place aggregators near associated QDCDs, favoring the QDCD closest to CIO within the associated group. Locate SW4/SW8 in nearby ceiling/wall panels only after ratings are confirmed.
6. After devices are placed, route actual SDCnet/SDCBus peripherals and CIO/QDCD PDnet connections under their respective manufacturer specifications. Keep buses distinct. An all-Casambi option still needs verified QDCD and sensor power but not invented CIO/SW signal wiring. Follow documented daisy-chain connections, CAT5e Class 2 conventions, gauge/power rules, lengths, connectors, termination and permitted branches; do not invent unsupported star topology. Confirm the precise 250 ft distance interpretation before finalizing cumulative strings.
7. Show strings, numbered devices, route IDs and CIO association on the plan; check every physical connection and functional sensor/zone relationship. Owner reviews location and route markups.

Output: sensor totals and port ledger, aggregator and bus-device counts, CIO allocation, bus power/distance budget, minimum-vs-installed explanation and owner questions.

## 6. Typical Variants

| Architecture | Allocation consequence |
|---|---|
| CIO plus SW interfaces | Match SW8 on/off and SW4 analog inputs; retain separate PDnet/QDCD and SDCnet peripheral ledgers |
| CIO direct room ports | Up to eight independent port groups; each shared port serves one isolated room/scene, not independently addressable attached sensors; fan-in remains unknown |
| CIO plus Casambi-enabled QDCDs | Compatible wireless controls and CIO-mediated hardwired inputs may coexist; record associations and verify command precedence |
| All-Casambi small application | Use Casambi-enabled QDCDs with compatible wireless wall/OCC/ALS devices; omit CIO/SW modules only when all approved functions are supported; separately supply powered sensors |

Record explicit alternatives and supported exceptions; no silent regrouping or invented spare policy. Non-Casambi QDCDs do not acquire wireless capability from other devices' radios.

## 7. Decision Gates

Resolve hardware evidence and owner locations before finalizing dependent allocations/routes.

## 8. Design Zoning / Grouping Strategy

Preserve designated channels and functional zones; count geographic increases separately from lower bounds.

## 9. Common Failure Modes

Do not confuse power feeds, driver outputs, sensors, aggregated port groups and bus devices. Spare SW8 inputs cannot receive unsupported 0–10 V signals. More sensors on one CIO port do not create more independent scenes. Unconfirmed wiring or a guessed four-sensor fan-in cannot establish capacity. Do not apply a CIO requirement to a supported all-Casambi option.

## 10. Safe Assumptions (and Limits)

Owner defaults are preferences, not manufacturer ratings. Unknowns stay unknown.

## 11. Documentation Expectations

Stable IDs, exact device variants, firmware/basis, source evidence, scene-to-port and physical sensor-to-input maps, separate analog/on-off demand, separate QDCD/SDCnet counts, wireless associations, power budgets, count rationale, owner decisions and editable markups. Retain open items `CIO-PORT-FANIN` and `CIO-QDCD16-FW` from the CIO hardware page until their evidence is resolved. A software failure tied to an older contract is reported as such, not hidden or used to silently reverse an owner-reviewed candidate.

## 12. When to Go Deeper / Exit This Playbook

Return device conflicts upstream or obtain manufacturer clarification; retain supported scope.

## 13. Cross-Links to Supporting Knowledge

[Device and playbook index](smartdc-allocation-index.md).

## 14. Status and Stewardship

Draft; KIS Solutions; October 2026.

## 15. Author Notes (Institutional Context)

Records owner directives from 2026-10-05 and hardware/architecture clarifications from 2026-10-26. SW input capabilities are corroborated by the linked manufacturer page/sheet. Grouped direct CIO port use, possible fan-in and firmware-expanded driver capacity retain their separately stated owner basis/open items. This documentation does not upgrade the LV topology schema/checker; see its [implementation boundary](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/ontology/canonical-model/controller-power-topology-v1.md#hardware-clarifications-and-current-checker-boundary).

## Input from Earlier Room-Device Review

Room sensors/manual controls are identified, scheduled and provisionally located immediately after narrative lock. Use owner-returned device positions as inputs to aggregator clustering, CIO coordination and bus routing. Preserve Device IDs and parent/child zone associations; physical devices are counted once. Initial positions follow the LV milestone playbook: wall switches/scene controllers/dimmers at source electrical lighting-plan positions first (accepted owner locations prevail), with door/entry/glazing rules used only without a usable source location, occupancy and daylight sensors also at source design locations first, preserving accepted owner changes. Only without usable source positions apply ceiling occupancy room/child-zone centers (tile-centered when a grid is visible), wall occupancy top-left placeholders, corridor midpoints or flagged daylight placeholders. Preserve source sheet/revision/symbol references, register positions to the accepted working frame, and flag conflicting/uncertain source locations instead of silently replacing them with a fallback. Provisional positions do not establish sensor coverage or final cable lengths. [Placement rules](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md#provisional-room-device-placement).
