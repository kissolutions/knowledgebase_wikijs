---
title: "QDCD Channel Assignment Mini Playbook"
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

# QDCD Channel Assignment Mini Playbook

## 1. Purpose and Use

Apply after accepted narrative and upstream micro-channel design.

## 2. Design Intent

Preserve independent operation and understandable spatial grouping.

## 3. Space / System Definition (Decision-Oriented)

Use exact selected family/model and served areas; this mini playbook specializes the LV implementation workflow.

## 4. Constraint Envelope

Use the linked hardware evidence and early AHJ/code/plenum facts. Unknown ratings remain open.

## 5. Baseline / Default Design Pattern

Input: already-designated compatible micro LV channels and approved functional control zones. The upstream LV step establishes voltage/type, CV/CC, current/range, Class 2 limits and connected load. Never recreate or silently regroup channels here.

1. Count eligible channels requiring QDCD outputs, including every dimming micro channel under the current owner solution. Ceiling(count/4) is an output-count lower bound. Apply selected QDCD electrical, aggregate-power and control-capacity constraints before calling a count a feasible minimum. **For every multi-luminaire QDCD constant-current output, enforce the manufacturer's Rev A2 parallel-wiring condition: each LED luminaire must have the same VERIFIED rated mA**; do not accept matching nominal voltage alone, even if an owner cohort lists both fixtures. Sum these branch ratings for the output-current target, subject to the QDCD's actual programmable range/increment; enforce 4 A maximum, 100 W nameplate / 95 W KIS design maximum per output and 400 W aggregate per unit. The manufacturer's example proves equal-rated-current parallel CC wiring is supported within its stated scope, **not** arbitrary mixing of different LED modules, current tolerances, or emergency behavior. Return an incompatible current/voltage/output requirement upstream as a conflict.
2. Group by room family first, then geography: fill nearby similar offices' boxes before opening a mixed-family group. A QDCD may serve several rooms through independent outputs. Family is an equipment-service grouping, separate from building/energy-code classification; preserve the recorded family and basis. Flag dispersion/reach conflicts for review. Independent controls, electrical compatibility, wiring and capacity remain mandatory. Spare outputs are acceptable.
3. Assign exactly one existing micro channel to each used QDCD output; preserve separate room-zone control behavior. One room zone may span several micro channels and QDCDs.
4. Prefer Casambi wall controllers/dimmers to avoid wall wiring; prefer wired occupancy/daylight sensing via SW4/SW8. Count controls separately and preserve each served-zone association. Unconfirmed QDCD wired sensor connections cannot be used as confirmed capacity.
5. For confirmed non-return-plenum areas, locate above ceiling in a common space fairly central to served zones. Co-locate compatible QDCDs serving the same room family where routing and access support it. Dry-location/environment/access constraints still apply. Return-plenum or unknown status requires another supported placement or confirmation.
6. Submit locations to owner for markup changes. Explain material alternative groupings using named rooms/channel IDs and proposed outputs; request a specific decision or highlight the affected area on plan.

Output: controller/output/channel map, electrical configuration, control associations, assigned watts, theoretical lower bound, feasible minimum if proven, proposed installed count, grouping rationale and owner location-review status.

## 6. Typical Variants

Record explicit alternatives and supported exceptions; no silent regrouping or invented spare policy.

## 7. Decision Gates

Resolve hardware evidence and owner locations before finalizing dependent allocations/routes. **Record each fixture's rated CC mA from its real datasheet/LED module approval; never derive nameplate current only as W/nominal V.** A documented owner compatibility decision still must comply with the manufacturer's same-rated-mA condition for parallel QDCD loads. For example, two 36 V modules rated 1,000 and 1,139 mA cannot share a channel just because their combined watts and summed amps fit. A base and battery/emergency variant require the same mA qualification *plus* a separate emergency-operation compatibility review. Series diagrams also exist in SmartDC literature, but KIS's selected multi-fixture Class 2 design method remains parallel.

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
