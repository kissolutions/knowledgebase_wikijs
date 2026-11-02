---
title: "IECC 2021 Daylight Zone Qualification and M3 Review v0.1"
description: "Window and roof-opening qualification, daylight-control applicability and fixture-selection handoff"
published: true
page_type: playbook
page_status: draft
confidence_level: medium
domain_primary: electrical-lighting
ai_role: prescriptive_standard
invocation_triggers:
  systems_present: [lighting]
  uncertainty_flags: [daylight_geometry_unknown, daylight_control_applicability_unknown]
decision_axes: [daylight_qualification, shading, control_applicability, dimming_requirements]
related_pages:
  - room-classification-and-controls-review-playbook.md
  - m3-lighting-sequence-lifecycle-v0.1.md
  - sequence-validation-process-v0.1.md
---

# IECC 2021 Daylight Zone Qualification — Design Playbook

Revision: 2026-11-01, v0.1. This completes the edition-specific review guidance prompted by the owner's shading review. Scope is the IECC 2021 commercial prescriptive path; other editions and amendments require their own source comparison.

## 1. Purpose and Use

Run during the first M3 requirements review, before sequence matching and the external fixture-distributor schedule. Establish three separate results: opening/zone qualification, required daylight controls, and the resulting fixture/driver performance requirement. Re-run affected results when glazing, shading, geometry, lighting power, source intent or code basis changes.

## 2. Design Intent

Evaluate the actual daylight opportunity and preserve source/approved controls. A window does not automatically require a daylight sensor. Absence of a daylight-control requirement does not establish that the lighting can be non-dimming.

## 3. Space / System Definition (Decision-Oriented)

Identify each relevant wall opening, rooftop monitor and roof opening; give each candidate zone a stable review reference. Link served Spaces and responding Light Points without changing their physical ownership. A room can contain several daylight contributions with different outcomes.

## 4. Constraint Envelope

### 4.1 Hard Constraints

Select jurisdiction, compliance path, edition, printing and amendments first. Use C405.2.4 through C405.2.4.3 and C402.4.3 Equation 4-5 for this profile. Check C405.2 scope and specific-application provisions independently.

### 4.2 Soft Constraints

Owner preferences or supported source design may retain daylight response/dimming beyond the code minimum. Record those decisions separately from code requirements.

### 4.3 Hidden Constraints

Plan views alone may omit overhang depth, sill/head elevations, glazing transmittance or external obstructions. Request only the missing evidence consequential to the decision. Refine estimates near a boundary instead of comparing rounded labels.

## 5. Baseline / Default Design Pattern

### 5.1 Collect evidence and qualify each opening

Record source sheet/revision and the opening's location, orientation to true north, dimensions/elevations, shading, obstruction evidence and applicable VT. Distinguish measured/source-supported facts, owner assertions and unknowns.

For C405.2.4.2, all applicable conditions must hold. Evaluate these numeric screens before drawing a final sidelit zone:

| Item | Qualifying condition | Equality |
|---|---|---|
| 4 — Fenestration area | Area >=24 ft² | Qualifies on this condition |
| 5 — Blocking building/geological formation | Separation D > H/2; H is from glazing bottom to obstruction top | D = H/2 fails |
| 6 — Visible transmittance | VT >=0.20 | Qualifies on this condition |
| 7 — Shading overhang | PF <=1.0 for orientation within 45° of true north; PF <=1.5 otherwise | At the applicable limit qualifies |

**Overhang calculation:** `PF = A / B` using consistent units. A is the horizontal distance from the glazing plane to the farthest continuous overhang/eave/permanent shading-device edge. B is the vertical distance from the **bottom of glazing to the shading underside**, not the gap above the window head. For a simple horizontal awning, B equals glazing height plus head-to-underside gap. Check each differing opening separately. B must be positive and supported; unknown orientation or geometry remains unresolved when it could change the result.

Item 5 addresses a blocking building/geological formation; item 7 directly addresses an overhanging projection. Do not stretch one into the other to obtain a desired result. A supported failure of either applicable condition is sufficient to reject that opening's sidelit contribution; an overhang's mere presence is not a failure. If no relevant overhang or obstruction exists, record that confirmed absence/basis and the condition's nonapplicability rather than inventing dimensions.

### 5.2 Establish the qualifying extent

For ordinary wall glazing, use window-head height above the floor, Hw: primary depth up to Hw; secondary reaches up to 2Hw from the glazing. Both have side extensions up to 0.5Hw from the fenestration edges, bounded by the applicable full-height walls. Follow the corrected Figure C405.2.4.2(1) and item 3. **Do not reuse the superseded two-foot secondary side extension.** The secondary area excludes the primary strip.

Rooftop monitors use the separate item 2 geometry and its figures, including obstruction-height limits; do not apply the ordinary wall-window sketch indiscriminately.

Toplit qualification is separate under C405.2.4.3: extent up to 0.7 times ceiling height subject to the stated obstructions; summer-solstice solar access; and VT times roof rough-opening area divided by toplit-zone area >=0.008. Record the needed roof/solar evidence rather than declaring no daylight because wall glazing failed.

### 5.3 Determine whether controls are required

After qualification, reconcile general-lighting power inside the qualifying zones **per Space**:

| C405.2.4 test | Trigger |
|---|---|
| Primary sidelit | More than 150 W |
| All sidelit, primary plus secondary | More than 300 W |
| Toplit | More than 150 W |

Equality alone does not trigger these tests. Preserve the power basis and revision; recheck substitutions, linear allowances and changed zone membership. Count each physical light once within a given sum; overlapping window contributions do not multiply its watts.

Review the section's patient-care, first-floor-above-grade Group A-2/Group M sidelit, and new-building adjusted-LPA exceptions only with their actual applicability evidence. The adjusted-LPA option requires the complete Equation 4-9 building calculation; a low-wattage room is insufficient. Preserve a qualifying zone even when its controls are not required by threshold/exception.

### 5.4 Carry the resulting control behavior

Where required, carry continuous daylight dimming to 15% light output or lower plus full shutoff into M3 and fixture selection. Preserve primary/secondary and sidelit/toplit independence, orientation grouping and the section's limited grouping permissions. Daylight response must respect the applicable unoccupied-power ceiling. Do not infer a sensor count or hardware interface from these functions.

Review all other dimming requirements and adopted source/owner intent before assigning continuous, stepped or none to a fixture group. A daylight-only exclusion does not clear occupancy, light-reduction, manual or other requirements.

## 6. Typical Variants

**Known failure:** Record the failed condition and reject only that contribution. Check the other openings and roof daylight before concluding that a Space has no qualifying zone.

**Missing or uncertain evidence:** Keep qualification/control applicability unresolved if the uncertainty can change the result. A supported failure may settle a contribution despite unrelated unknowns; record untested conditions honestly. Use conservative bounds only with a documented derivation.

**Space-level summary:** One qualifying contribution establishes zone presence, even if other contributions remain unresolved; extent or control applicability may still be incomplete. Report not a zone only after all relevant wall/roof contributions are ruled out on a supported basis. Otherwise retain unresolved. Keep asserted versus verified status explicit.

**Owner-asserted extent:** Retain the existing M3 permission to carry an owner-asserted zone/control direction, clearly labelled asserted. It does not become measured geometry or verified exception evidence. A proposed omission of required controls still needs a supported basis.

## 7. Decision Gates

| Review question | Required disposition |
|---|---|
| Every relevant opening/zone accounted for? | Qualified, rejected with reason, or unresolved; no blank-as-no |
| All relevant contributions resolved for the Space? | Report zone / not a zone / unresolved, with linked contribution results |
| Power and applicable exceptions resolved? | Report controls required / not required / unresolved separately |
| Dimming requirements resolved? | Carry reviewed behavior to SEQ/PSEQ and distributor request; hold affected unresolved selection scope |
| Evidence or geometry changed? | New determination/report revision, affected sequence review and schedule impact check |

### Synthetic boundary review cases

These are arithmetic/review examples, not project geometry or an automated test suite.

| Synthetic inputs | Expected single-condition result |
|---|---|
| A=4 ft, B=4 ft, true north | PF=1.0: qualifies |
| A=6 ft, B=4 ft, east | PF=1.5: qualifies |
| A=6.04 ft, B=4 ft, east | PF=1.51: fails |
| A=4.04 ft, B=4 ft, true north | PF=1.01: fails |
| Orientation exactly 45° from north | Use the 1.0 limit |
| D=6 ft, H=12 ft | Obstruction condition fails |
| D=6.01 ft, H=12 ft | Obstruction condition qualifies |
| Area=24 ft²; VT=0.20 | Both equality conditions qualify |
| Primary power=150 W; combined sidelit=300 W; toplit=150 W | None of these equality values independently triggers controls |
| Unknown B, VT or relevant obstruction geometry | Affected condition unresolved; no assumed pass/fail |

## 8. Design Zoning / Grouping Strategy

Keep daylight extent, room boundary, occupancy leaf zone and physical output channel distinct. Track responding Light Points and control groups explicitly. Preserve independent operation when grouping LV outputs; do not force a daylight split into a new physical room or duplicate a luminaire.

## 9. Common Failure Modes

### Design-Time Failures

Using only window presence; measuring B from the window head; assuming every canopy disqualifies glazing; transferring 2021 conditions to another edition.

### Documentation Failures

Recording “no daylight” when only one opening failed; hiding a threshold exemption as absence of a zone; treating missing dimensions as zero; losing source/owner basis.

### Construction / Operational Failures

Substituting glazing, canopy geometry or fixture loads without impact review; selecting on/off-only fixtures before all dimming requirements are known.

## 10. Safe Assumptions (and Limits)

Unknown facts remain unknown. Approximate dimensions support screening, not a decisive near-boundary result. An asserted design decision remains labelled asserted. Do not claim a measured negative determination or final code compliance from this checklist.

## 11. Documentation Expectations

Use existing project review records, without a new mandatory database or duplicate register. Retain:

- Code basis/printing, source revisions and opening/zone references; served Spaces and Light Points.
- Input values, units, source/owner basis, A/B/PF and D/H where relevant; condition results and failed/unresolved reasons.
- Separate qualification, geometric-verification and controls-required results; power sums, exceptions and remaining dimming requirements.
- Adopted sequence/control group, reviewer/decision references, pending questions and affected distributor schedule revision.

These are review requirements, not new canonical JSON fields. Link detailed evidence from the existing daylight/direction reports.

## 12. When to Go Deeper / Exit This Playbook

Escalate unusual/multiple shading geometry, ambiguous fenestration aggregation, unsupported power allocation, solar-access uncertainty, conflicting approved intent or another code path/edition. Resolve only affected decisions. Physical sensing layout, commissioning setpoints and photometry retain their existing M4/M5 scope.

## 13. Cross-Links to Supporting Knowledge

- [ICC 2021 Chapter 4](https://codes.iccsafe.org/content/IECC2021V3.0/chapter-4-ce-commercial-energy-efficiency): C402.4.3 Equation 4-5; C405.2.4 through .4.3.
- [ICC 2021 errata](https://www.iccsafe.org/wp-content/uploads/errata_central/2021-International-Energy-Conservation-Code-Errata-Complete.pdf): PDF page 20, March 11, 2022 section correction; page 21, corrected figure updated April 7, 2023.
- [General M3 daylight directive](room-classification-and-controls-review-playbook.md#daylight-zones--directive-flagged-for-expansion)
- [M3 lifecycle](m3-lighting-sequence-lifecycle-v0.1.md)
- [Independent sequence validation](sequence-validation-process-v0.1.md)

## 14. Status and Stewardship

Draft source-grounded review procedure; owner-directed integration, 2026-11-01. Reviewed the ICC indexed section text, owner-supplied items 5–7 and the directly retrieved ICC errata, including its corrected figure. This does not assert a successful full-page ICC download or establish local adoption.

The current LV evaluator checks sequence settings after independently established `daylight_control_required`; it does not calculate these geometry, shading, power-allocation or exception results. No automated geometry qualifier, new schema, completed 2024 profile or private-project rerun is claimed. Owner: KIS Solutions.

## 15. Author Notes (Institutional Context)

The first M3 review must identify shading and other consequential missing evidence early enough to prevent an incorrect fixture selection. Preserve the distinction between an owner design choice, its verification status and a code-required function.
