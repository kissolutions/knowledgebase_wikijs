---
title: Room Classification and Lighting Controls Review Playbook
description: Owner-reviewed space classifications, source-controls intake and controls narrative development when guidance is incomplete
published: true
date: 2026-10-04T23:24:22.000Z
dateCreated: 2026-10-04T23:24:22.000Z
tags: lighting, controls, classification, narrative, review
editor: markdown
page_type: playbook
page_status: draft
confidence_level: medium
domain_primary: electrical-lighting
ai_role: prescriptive_standard
invocation_triggers:
  systems_present: [lighting]
  uncertainty_flags: [room_classification_unknown, source_controls_missing, lighting_guidance_incomplete]
decision_axes: [space_classification, source_intent, authorization, guidance_readiness, code_interpretation]
related_pages:
  - ../ontology/reg-and-class/interior-space-types.md
  - lighting-controls-guidance-index.md
  - lighting-control-application-guide.md
  - iecc-occupant-sensor-directives.md
---

# Room Classification and Lighting Controls Review — Design Playbook

## 1. Purpose and Use

Use this workflow to classify rooms, review an existing lighting-control scheme and develop a proposed narrative when the source scheme is missing or incomplete. WikiJS owns the general electrical classification, code analysis and controls guidance. Project extensions own source intake, project records and system-specific implementation. Keep real project facts and approvals outside the knowledge repositories.

## 2. Design Intent

Preserve architectural labels and documented MEP intent. Treat room classifications as reviewed decisions, missing controls as source gaps, and source-text interpretations as proposals until approved. An unfinished room guide must not silently supply a complete narrative or a compliance finding.

## 3. Space / System Definition (Decision-Oriented)

Keep the source room name/use, Building Code Space Type, Building Code Occupancy Group and Energy Code Space Type independent. An architectural synonym is a retrieval clue, not an automatic classification. A building occupancy group does not by itself establish a room's energy-code type. Relevant evidence may include actual activities, area/basis, enclosure, daylight conditions and source descriptions.

## 4. Constraint Envelope

### 4.1 Hard Constraints

Select the project's governing standard/path, edition, jurisdiction and amendments before applying requirements. IECC 2024 is used only where it is the selected project basis; it is not the default for all projects. Verify applicable final text, section/printing, errata, conditions and exceptions. Project approval does not waive code requirements or substitute for a responsible reviewer where needed.

### 4.2 Soft Constraints

Owner preferences and applicable KIS defaults can select among permitted options. Record those choices separately from mandatory requirements. Extensions may narrow selections to compatible systems without weakening required behavior.

### 4.3 Hidden Constraints

WikiJS pages may be missing, unfinished, ambiguous, unverified or inconsistent with the selected edition. Drawing symbols may identify hardware without specifying its complete operating sequence. These are explicit gaps, not permission to infer absent facts.

## 5. Baseline / Default Design Pattern

### Step 1 — Propose Room Classifications

Search [Interior Space Types](../ontology/reg-and-class/interior-space-types.md), related definitions and the [guidance index](lighting-controls-guidance-index.md) for matching uses and synonyms. Preserve the exact architectural label. Present candidate Building Code Space Types and Energy Code Space Types separately, with supporting pages/sections, source-use evidence, competing matches and missing inputs. Where the catalog has no supported match, record that gap and seek owner clarification or a separately reviewed code-based candidate; do not invent an official category. Unsupported classifications remain unknown in the applied project record.

### Step 2 — Confirm Classifications

The owner reviews candidates, confirms or revises the supported use and classification for each room, or leaves the issue unresolved. Record confirmed values, owner/date, basis and affected Space IDs. Confirm the applicable code basis and inputs needed for later analysis. Confirmation of a room type authorizes progression of that analysis; it does not authorize replacement or completion of source controls. Source extraction may proceed in parallel, but classification-dependent conclusions remain provisional until confirmation.

### Step 3 — Extract Source Controls and Authorize Gap Filling

Review available plans, symbols, legends, schedules, keyed/general notes, details, sequences and specifications. Check completeness by function: dimming/level control, manual controls, on/off and return-to-occupancy behavior, occupancy/vacancy sensing, and time-switch scheduling. Also check daylight and normal/emergency interactions where relevant. Record each function as documented, ambiguous, missing or supported not applicable; do not assume every function is required in every room. Retain source locators and missing referenced documents. Absence of a symbol is not proof that a function is unnecessary.

For affected rooms, present the gaps and ask the owner either to authorize a controls narrative proposal using WikiJS guidance, supply a specific narrative/clarification, or defer that scope. Record the affected rooms/functions and any limits on redesign. Reuse an existing authorization when it clearly covers the scope; do not ask repeatedly. Until authorization exists, controls remain unresolved while unrelated intake and source/code checking continue. A general instruction to test the framework or a confirmed room type is not blanket permission to invent controls. Preserve complete source functions when filling only partial gaps.

### Step 4 — Develop and Review the Narrative

For authorized functions, retrieve matching space-type controls guidance and assess its applicability, revision and verification status. Use supported guidance as a design basis; draft or incomplete content remains subject to review. Keep the original source observations, code-derived requirements, KIS choices and proposed operating sequence separate.

When guidance is ambiguous, absent, unfinished or insufficient, consult the selected code's primary source text to align the supported requirements. For a project using IECC 2024, retrieve its applicable final text and amendments rather than relying on a remembered rule, a different edition or the unfinished draft profile. Capture exact sections/locators, source version, inputs, applicability, mandatory behavior, permitted alternatives, exception evidence, conflicts with WikiJS and unresolved questions. If source text cannot be retrieved or applicability cannot be established, flag the missing evidence and leave affected conclusions unresolved.

Code text may permit several valid sequences or leave equipment placement, coverage, sensor quantities and owner operating choices undetermined. Present those options and decisions explicitly; do not describe a chosen option as the only code requirement. Do not derive physical sensor counts from control-area counts alone. Obtain other verified guidance or an owner narrative for decisions the code does not settle.

Flag every source-text derivation for owner review, including which functions depend on it and any proposed change to WikiJS interpretation. Permission to build a proposal is separate from approval of the resulting interpretation, selected options and finished narrative. Adopt only the approved scoped narrative under the project's established authority; preserve original intent and approval history. An owner-supplied narrative still receives the applicable code/compatibility check, with conflicts retained for resolution.

## 6. Typical Variants

| Situation | Route |
|---|---|
| Complete source scheme | Check against supported guidance; preserve intent; propose a departure only with authority |
| Partially documented scheme | Retain known functions; obtain scoped permission or owner narrative for missing functions |
| No applicable source scheme | Record no information; request narrative-development authorization or owner narrative |
| Unfinished/missing room guide | Use reviewed selected-source derivation; flag interpretation and remaining choices for approval |
| Owner provides a narrative | Record it as owner direction, check applicable requirements and resolve conflicts before adoption |

## 7. Decision Gates

| Gate | Pass evidence | Pending result |
|---|---|---|
| Classifications confirmed? | Owner-reviewed independent classifications and necessary inputs | Candidate classification; no final dependent conclusions |
| Source scheme complete? | Function-by-function source observations or supported not-applicable basis | Explicit source gap/ambiguity |
| Missing-function narrative authorized? | Existing or new scoped authorization, or supplied owner narrative | No assigned replacement controls |
| Guidance supports the proposed function? | Applicable verified guidance, or a reviewed primary-source derivation | Guidance gap; no automatic compliance result |
| Interpretation/options/narrative approved? | Identified approval and adopted revision within authority | Proposal remains provisional |

These are review gates, not implemented model fields or an automatic compliance engine. Approval of one gate does not approve the others. Missing source evidence and missing guidance are distinct issues: an unavailable criterion leaves the check not reviewed; it does not by itself prove that the source scheme is deficient.

## 8. Design Zoning / Grouping Strategy

Room boundaries, independent control areas, physical sensing devices and power channels are separate. Preserve required independent behavior in implementation. Classification alone creates no default lighting zone. System-specific extensions select compatible equipment and grouping only after source intent or an approved narrative supports the behavior; incompatibility is a review conflict.

## 9. Common Failure Modes

### Design-Time Failures

Automatic synonym mapping; mixing building and energy classifications; applying the latest edition without a project basis; treating a code option as a mandate; assuming an exception without evidence.

### Documentation Failures

Replacing source observations with proposals; losing known functions during gap filling; treating authorization to draft as approval to adopt; recording a missing guide as source no-information or deficiency.

### Construction / Operational Failures

Selecting hardware before verifying required behavior; unverified sensing coverage; unresolved manual/daylight/emergency interaction; implementing a narrative that remains provisional.

## 10. Safe Assumptions (and Limits)

Source labels and retrieval aliases may generate candidates only. Unknowns remain unknown. No default classification, control sequence, exception, delay or sensor quantity is established by this workflow. Identified owner confirmation can establish actual use but does not make an unsupported code interpretation a verified rule.

## 11. Documentation Expectations

The project review package records Space IDs; original names/use evidence; candidate and confirmed independent classifications; owner/date; selected code basis; function-by-function source controls and gaps; scoped narrative authorization or owner direction; guide/source revisions; derived requirements/options/exceptions and uncertainties; proposed narrative; approval/adopted revision; and unresolved discrepancies. Retain known source functions and distinguish source, applied and proposed behavior. Existing project narratives, references and review/open-item records suffice until a structured contract is implemented.

## 12. When to Go Deeper / Exit This Playbook

Escalate unresolved actual use, governing code, source intent, inaccessible text, consequential exceptions, conflicting owner direction, system limitations or missing coverage evidence. Continue unrelated verified work; do not finalize affected controls. Project approval of an interpretation does not automatically promote it into reusable WikiJS guidance. A separate knowledge review establishes applicability, sources, options, exceptions and page/rule status before reuse as an approved default.

## 13. Cross-Links to Supporting Knowledge

- [Interior Space Types](../ontology/reg-and-class/interior-space-types.md)
- [Lighting Controls Guidance Index](lighting-controls-guidance-index.md)
- [Application-guide draft](lighting-control-application-guide.md)
- [IECC occupant-sensor draft and verification register](iecc-occupant-sensor-directives.md)
- [Occupancy sensor fundamentals](../ontology/signal-and-control-dev/occupancy-sensors.md)

## 14. Status and Stewardship

- **Status:** Draft workflow; owner-directed, pending project proof. Numerical room profiles remain separately unverified.
- **Last Judgment Review:** 2026-10.
- **Playbook Owner:** KIS Solutions.

## 15. Author Notes (Institutional Context)

Owner-directed workflow, October 2026, following testing that exposed unfinished space-type controls guides. This page adds review and fallback routing; it does not introduce or verify new numerical code rules, device prescriptions or automated approval logic.

## Narrative Lock and Physical Device Review Handoff

The LV first-milestone room map uses owner-directed presentation categories: ordinary enclosed rooms blue; corridors/halls/circulation tracking Spaces green; open activity/common areas (open offices, gyms, play, dining, assembly) ruddy orange; multi-level atriums/open-to-above areas violet; service voids and confirmed out-of-scope/no-lighting areas gray; exterior areas low-opacity wine/burgundy. These colors do not assign building/energy-code room types, occupancy groups or control requirements. Accepted footprints must be editable fillable closed shapes with a lighter low-opacity fill than the outline; redraw nonfillable footprints with identity reconciliation. Preserve multi-level served-Space ownership without duplicate floor areas/lights. Follow the [LV room-map directive](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md#finalized-room-map-for-the-first-package) for precedence, unresolved categories, scope exclusions and final PDF review.

After owner adoption locks the narrative, identify/count its physical sensors, manual switches/dimmers and other room devices with stable IDs and all served-zone associations. The LV extension produces a device schedule and device-specific provisional review locations: wall switches, scene controllers and dimmers at source electrical lighting-plan locations first, retaining accepted owner changes; only without usable source locations use latch-side door frames (adjacent solid wall when glazing intervenes) or common-area entry routes; ceiling occupancy sensors near room/child-zone centers and visible tile centers; wall occupancy sensors at displayed-plan top-left corner placeholders; corridor sensors near served-zone midpoints. Apply occupancy quantities to served child zones, without automatically adding parent sensors. Retain source sheet/revision/symbol evidence, register positions into the accepted working frame and flag source conflicts; do not silently relocate shown controls under a fallback rule. Use the linked milestone playbook for swing clearance, source uncertainty and fallback rules. Owner finalizes placement; these proposals do not establish sensor coverage or installation details. Owner-returned locations feed subsequent controller/aggregator routing. Retain parent/cluster behavior separately from micro electrical channels. [Milestone deliverables](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md).

## M2 Source Fixture-Schedule Evidence Handoff

The original MEP fixture schedule is source design information required during physical takeoff, before fixture count/type/continuity acceptance. Preserve exact marks and suffixes, descriptions, assembly/section/length clues, electrical facts and detail/note evidence separately from LV substitutions. Reconcile RCP geometry with schedule descriptions and electrical circuiting/daisy chaining; a circular L4/L4A path may be an assembly or separate typed pieces and must not be collapsed on appearance alone. Missing referenced schedules require retrieval; genuinely absent schedules are recorded and affected interpretations remain provisional. Complete physical identity reconciliation before downstream room controls/narrative review. See [LV M2 source schedule gate](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/m2-linear-fixture-extraction.md#m2-source-fixture-schedule-gate).

## Physical Intake Beta Handoff

Apply owner-directed physical-section counts within the documented decision scope, preserving assembly identity without double counts. Preserve exact plan tags independently of schedule marks; unresolved suffix meanings keep affected counts provisional. Keynote-only luminaires remain distinct source types with unknown electrical data until evidenced. Exterior fixtures without served Spaces remain explicit takeoff holdouts with reasons and quantities. Presentation geometry/color must not silently reassign lights or establish code area quantities. The owner uses CAD for actual area takeoffs; markup areas are checks. See the [LV M1/M2 beta playbook](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/m1-m2-beta-review.md) for room/annotation/frame implementation and scoped owner-reported Bluebeam validation.
