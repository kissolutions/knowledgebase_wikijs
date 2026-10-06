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

## EPS Fixture Power Aggregation — Owner Directive, 2026-10-06

Fixtures with rated input above 100 W are permitted design candidates through an EPS fixture power aggregator. This is a **power aggregator**, distinct from SW4/SW8 sensor aggregators. Reserve this path for **on/off-only, nominal 48 VDC constant-voltage fixtures** controlled directly through the EPS supply outputs. It is not a dimming or constant-current path. Do not use it to bypass a narrative that requires dimming; retain that incompatibility for review.

The owner describes a small box installed **inside the fixture housing**, accepting **1–4 separate Class 2 inputs** and providing **one combined output** to one larger fixture. Owner-stated maximum is up to **400 W with four inputs**. Scale input count to the selected fixture's actual LV nameplate demand; do not automatically allocate four inputs as with the preferred QDCD supply convention. A one-input configuration is permitted where sufficient. The analogy to QDCD concerns multiple supply inputs, not output count: the fixture aggregator has only one output and provides no independent downstream control zones.

### Allocation and Control

- Preserve one physical Light Object and its complete nameplate/input load. Do not split it into fictitious fixtures or copy its full wattage onto every input.
- Assign each populated aggregator input to a distinct identified EPS/PDU output and feed. Each input consumes one supply output; count these in addition to direct-light and QDCD feed allocations. A given PDU output cannot also supply another allocated load.
- Use the smallest supported input count from 1 through 4 that covers the complete fixture demand within verified per-feed limits, available combined output and any established project design margin. Nominal arithmetic starts with ceiling(fixture input watts / 100 W), but 100 W per feed and 400 W combined are owner-stated upper bounds, not a substitute for equipment evidence. Do not silently discard the current 95 W project feed target. Check each feed's actual demand, aggregate losses/auxiliaries and selected PDU total budget; do not assume an equal load split without device evidence. An exact 400 W fixture needs explicit resolution of these constraints, not an automatic four-feed approval.
- Keep all feeds serving the one fixture in the same approved functional on/off group. No independently commanded occupancy/daylight/manual zones may be assigned to different inputs of that aggregator. Document coordinated switching through the EPS units, including behavior if a feed is unavailable; do not invent a switching API or assume feed-loss behavior.
- Confirm selected fixture operation at nominal 48 VDC CV and record its rated voltage range separately from source AC/other fixture information. Confirm the selected PDU output's actual voltage and aggregator compatibility rather than transferring a nominal voltage from another EPS variant.
- One aggregator output serves the one fixture. Do not generalize this exception into a 400 W ordinary Class 2 lighting channel or assume that the combined output retains Class 2 classification. Preserve the upstream Class 2 feed identities and obtain the selected device's installation/listing basis for the short internal fixture connection.
- Record a stable power-aggregator ID (simple display tag **FA-01**, fixture aggregator), served Light Object/Room/zone IDs, input count, every supply output-to-input pair, one output-to-fixture link, nameplate load, demand/rating basis and open items. Locate it at the served fixture with an **inside fixture housing** note; equipment/connection review should identify the internal unit, while device-free micro-channel maps remain device-free.

### Evidence and Current Model Limit

This directive records owner-provided EPS capability and KIS permitted application, not a verified specification for an exact product. Exact part number, supported reduced-input configurations, input loading/sharing, voltage compatibility, switching behavior, losses, thermal/mechanical fit and installation/listing details remain to be confirmed from the selected EPS device. The gym/high-bay application is a candidate, not an established project requirement or selected fixture.

Current canonical light ownership allows one supply channel per light, and topology v1/v1.1 supports PDU-to-QDCD feeds only. Those validators/exporters **do not implement or prove** this fixture-aggregator path. Until a versioned contract and meaningful checks support it, retain the candidate and its full feed/output ledger in the project review record; flag model-support readiness rather than rejecting the physical fixture solely for exceeding 100 W. Do not force-fit it by raising an ordinary channel limit, inventing a QDCD, using sensor-aggregator fields, duplicating Light Objects or claiming the legacy checks passed this topology. Final channel/PDU counts and coordinated routing must include the documented aggregator feeds when support is implemented.
