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

### Step 1A — First-Pass Routing for Other Spaces

Do not stop the classification attempt because the architectural label has no explicit IECC match. Before narrative selection:

1. Propose a Building Code Space Type and, where supported, Building Code Occupancy Group from source plans/code summaries, actual activities and the selected building-code definitions. Preserve source citations, whether the classification is documented or inferred, confidence, alternatives and missing facts. Do not assign every room the building's overall occupancy group or invent an official space type.
2. Independently test the actual use against the selected energy-code edition's named spaces. A synonym needs supporting use evidence. Then evaluate any applicable area/enclosure catch-all. For IECC 2021, other spaces of 300 square feet or less enclosed by floor-to-ceiling partitions remain occupant-sensor candidates. Check-only markup area is not verified threshold evidence.
3. For spaces still unmatched, propose **occupancy** or **time switch** as the initial automatic-control path, with the applicable section, inputs and rationale. Under 2021 C405.2.2, areas without occupant-sensor controls complying with C405.2.1.1 generally require time-switch controls complying with C405.2.2.1, subject to the applicable exceptions. Use the [edition-specific directives](iecc-occupant-sensor-directives.md) and adopted source text. Building-code classification is a useful retrieval clue; it is not a direct lookup assigning an IECC control requirement.
4. Distinguish a code-required path from a KIS design preference or permitted alternative. Actual occupancy pattern, source control intent and feasible sensing coverage may inform a proposal. A named mandatory-sensor use cannot be changed to time-switch-only merely because scheduled operation seems convenient.
5. Record functions separately when both control methods apply. For example, warehouse storage requires occupant sensors; the KIS partial-off solution also requires time-switch shutoff because the sensors leave those lights on at reduced power. Open-office whole-area shutoff and individual-zone vacancy response are distinct obligations. Do not force these into a single mutually exclusive label.
6. Present the proposed classifications and control path for the existing review gates. Keep unresolved facts as `needs_review`, with a specific question; no match is not an exemption. Preserve documented source controls and existing scoped authority.

The review output includes Space ID, exact source room label/use, proposed building-code space type and occupancy group, proposed energy-code type (or unresolved), verified area/enclosure where needed, occupancy/time-switch candidate and any combined functions, rule/source locator, documented-versus-inferred basis, and review status. This is a documentation/review directive; it does not claim new schema fields or an implemented automatic matcher.

### Area Precision for Threshold Decisions

Use first-pass room/zone area estimates to screen the thresholds explicitly present in the applicable code provision. Detailed area takeoff is not required for every room. If the estimate is near a threshold such that plausible uncertainty could change the result, perform a second, more accurate measurement before finalizing the affected control decision. If uncertainty cannot be bounded, obtain better measurement evidence rather than assuming the room falls on the convenient side.

Record the applicable section, actual area definition and exact comparison operator; examples such as 250, 300 or 600 square feet apply only where the selected code provision establishes them. Check the area of the object regulated by the rule (room, open-office area or individual control zone). Use calibrated/dimensioned source geometry for the second pass and retain its basis, refined result and any resulting narrative/zone change. Use unrounded values. A check-only display polygon is useful for screening but is not automatically accurate threshold evidence. Far from a threshold, a supported above/below conclusion with recorded basis is sufficient for screening; important quantity takeoffs remain the owner's separate work.

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

## M3 Scope Boundaries

**Sequence parameter specificity.** Owner-level specificity is sufficient at M3. A sequence may establish its trigger, resulting state and control method without fixing clock times, manual-override durations, override area limits or commissioning setpoints. Record those parameters as **deferred to M4/M5**, when zones, channels and loads make them answerable, rather than as M3 deficiencies. “Business Hours” is a sufficient schedule description; an M3 gate does not fail because it is not yet “5:00–22:00.” Preserve any already established values and applicable code constraints separately from the project settings still to be selected.

**Photometric scope.** Wattage is the quantitative lighting-performance check at M3; photometric calculations are outside this gate. Record any illuminance-dependent requirement and its basis, including a reduced-level footcandle floor, a corridor darkest-floor-point exception or a daylight setpoint's delivered level, and defer its verification. Do not hold M3 open for calculations requiring photometry. Do not convert percentage of input power into an illuminance claim: flag the unit mismatch and carry it forward. A deferred exception remains unverified, not proven by M3 acceptance.

This scope limit does not cancel the targeted area-threshold screening/second pass above: that is classification evidence rather than a photometric performance check. Record counts and known values normally without manufacturing detailed design inputs.

**Deferred-item handoff.** List the affected sequence/Space/zone, parameter or requirement, basis, missing evidence, responsible follow-up and receiving milestone (M4/M5). M3 acceptance covers the owner-level control direction; it does not close these later checks or certify final compliance. Distinguish an explicitly deferred implementation detail from a missing control direction or contradictory sequence.

## Daylight Zones — Directive, Flagged for Expansion

Every Space receives an explicit daylight-zone determination: **zone**, **not a zone**, or **unresolved**. State absence explicitly; never interpret a blank or null as “no.” Record the project code edition and determination basis for each Space, including negative determinations.

**Owner assertion versus measured geometry.** An owner-asserted zone extent is sufficient to carry an M3 control decision. Record it as an owner assertion, with the owner decision reference; keep missing sidelit/toplit geometric evidence as a separate open question. An asserted zone is not a measured zone. Without source evidence or an owner assertion, retain unresolved rather than inventing either geometry or an assertion.

**Extent is an independent fact.** A daylight zone can span several Spaces or only part of one. Give it a stable review identity and record all covered Space IDs, described/asserted/measured extent and basis, responding luminaire IDs, and setpoint with units when established. Unknown setpoints/units remain explicit and deferred under the M3 scope rule. Do not derive zone extent from room boundaries or treat every luminaire in a covered room as responding automatically. Record daylight-control applicability separately from zone presence.

**Edition sensitivity.** Daylight provisions are edition-dependent: thresholds, zone definitions, lighting-power trade-offs and exceptions must be reviewed for the selected edition. Never carry a daylight conclusion across editions. When the project edition changes, reopen and re-run all daylight determinations and dependent control conclusions, preserving prior decisions as history.

**Geometry evidence.** Geometric establishment requires glazing evidence sufficient to determine the relevant extents and heights: elevations, window/storefront schedules or a calibrated plan with glazing extent and head-height information, as applicable. Where the source set lacks this evidence, state the gap; retain an existing owner assertion as asserted and do not invent geometry. This section is flagged for expansion into edition-specific geometry and verification guidance, not an automatic geometric evaluator.

## Narrative-versus-Fixture Cross-Reference — Standing M3 Check

After control direction is recorded and before the M3 gates, review **every Space in both directions**:

- **Direction with no luminaires:** determine whether it is served by another Space's fixtures (for example, an open vertical volume or adjacent open area), has fixtures missing from the source, or is genuinely unlit and correctly out of lighting scope. Name the disposition and evidence. Record the serving Space and fixture references where applicable; unresolved service is an explicit finding. Do not mark it out of scope merely because its own fixture list is empty.
- **Luminaires with no direction:** record an omission and resolve it. No Space with luminaires leaves M3 without a control direction. A shared sequence/control association may provide that direction when explicitly traced.

Publish a **separate cross-reference review record**, not only room notes. Include model/source revision, all reviewed Space IDs, sequence/direction reference, luminaire references, serving-Space relationship where relevant, disposition, finding/resolution and decision evidence. Summarize Spaces checked and findings open/resolved, including a zero-findings result. Preserve physical fixture identity and primary ownership; record shared service without duplicating fixtures or loads.

An anonymized owner-reported first application found one issue among 47 Spaces: a stair with time-switch direction appeared to lack fixtures, but was served by pendants at the level above. Retain this as workflow precedent, not evidence that every empty fixture list has the same explanation.

These are required project review records and manual/agent checks. They do not claim new schema fields, automatic daylight geometry or an implemented cross-reference validator.

## 7. Decision Gates

| Gate | Pass evidence | Pending result |
|---|---|---|
| Classifications confirmed? | Owner-reviewed independent classifications and necessary inputs | Candidate classification; no final dependent conclusions |
| Source scheme complete? | Function-by-function source observations or supported not-applicable basis | Explicit source gap/ambiguity |
| Missing-function narrative authorized? | Existing or new scoped authorization, or supplied owner narrative | No assigned replacement controls |
| Guidance supports the proposed function? | Applicable verified guidance, or a reviewed primary-source derivation | Guidance gap; no automatic compliance result |
| Narrative/fixture cross-reference complete? | Separate all-Space review record; each lit Space has direction; empty fixture lists have an explicit disposition/service relationship or finding | Missing direction or unresolved service contradiction |
| M3 deferrals recorded? | Parameter/photometric follow-ups assigned to M4/M5 with basis; every Space has an explicit daylight determination | Missing determination or untracked follow-up; an identified deferred parameter alone is not an M3 deficiency |
| Interpretation/options/narrative approved? | Identified approval and adopted revision within authority | Proposal remains provisional |

Apply the M3 scope boundaries above when evaluating these gates. Owner-level narrative approval does not require deferred clock settings, override details, geometric daylight confirmation of an owner assertion, or photometric proof.

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

### M3 Review Layout — One Section per Sequence

Organize the M3 controls narrative review by sequence, preserving **one narrative to many rooms/zones**. Each section contains, in order:

1. **Sequence number / stable ID, title and revision**, with proposal/adoption status.
2. **Complete narrative**, including activation, vacancy, delays, overrides and interactions that have been established.
3. **Required functions and components**, shown once for the sequence: manual/automatic operation, manual switching, occupancy/vacancy sensing, dimming, Light Reduction, daylight, time-switch and other applicable functions. State required behavior and component types; state fixed quantities only when the narrative actually requires them.
4. **Assigned-room implementation table**, immediately below: every assigned Room ID/name and applicable zone ID, showing the devices, quantities, capabilities and settings actually documented or proposed for that room. Do not repeat generic requirements or fill rows with “required”/“yes” when concrete implementation information exists.

Use consistent columns across sequence sections. Suggested headers: **Room ID / Name | Zone | Basis / Status | Manual Controls | Occupancy / Vacancy Sensors | Dimming | Light Reduction | Daylight | Time Switch | Differences / Open Items**. For example, show “2 wall switches,” “1 ceiling sensor — vacancy mode,” “1 wall dimmer serving general lights,” or “2 switched groups — 50% power remains after vacancy,” as supported. Light Reduction remains a dedicated column, describing that room's implementation of the sequence requirement.

At M3, “what we have” means the documented source arrangement or the current proposed/adopted design, not a claim of installed or field-verified equipment. Label the basis/status and retain source/decision references; separate source and proposed entries where they differ. Record known quantities without inventing devices to complete a table. If device selection/count is pending narrative lock or coverage review, show **TBD** and the outstanding question. Physical device scheduling and final placement still follow narrative lock.

Keep matching entries identically worded and quantity-first so the owner can scan down columns. Mark differing cells with a short text flag as well as optional shading; distinguish a legitimate quantity/layout variation from a functional mismatch. Use **None** only for a confirmed absence, and **Unknown / TBD** for unresolved data. A quantity difference does not automatically require a different sequence; a different operating behavior needs a reviewed sequence variant or reassignment. Shared devices retain one physical identity and show their shared service instead of inflating totals.

Repeat the sequence ID and table headers on continuation pages. Keep the narrative and requirement summary with the start of its room table. An optional overall assignment index may supplement these sections, but does not replace them. Review sequence approval separately from room-assignment/implementation approval; highlight changes since the prior review without obscuring unchanged entries.

### M3 Control Narrative Data — Light Reduction

Include a dedicated **Light Reduction** header/column in every room/zone control narrative data table, alongside manual switches, occupancy and the other control functions. Carry it into review prints and adopted narrative records; do not leave this behavior discoverable only inside prose or the occupancy column.

In the sequence requirement summary, use readable values such as **Partial on**, **Partial off**, **50% off**, **50% on**, and **None**. These are examples, not a closed list. A sequence may include both partial-on and partial-off behavior; record both in the same cell or as separate actions associated with the same room/zone.

- State the applicable trigger and resulting level in the cell or linked narrative, including delay and affected lighting where established.
- Qualify percentages: power remaining, power reduction, light output, or a switched lighting group. Preserve the source meaning; do not assume these bases are interchangeable. For example, “Partial off — reduce lighting power to 50% on vacancy” describes a resulting power level.
- **None** means an explicitly established absence of light-reduction behavior. Missing or unresolved information remains **Unknown / pending review**, never defaulted to None.
- Keep source, proposed and adopted values distinguishable and preserve their evidence/decision references. A shorthand value does not by itself establish a code requirement, dimming hardware capability or final shutoff method. Retain occupancy and time-switch functions separately.

In each assigned-room row, show how the actual documented/proposed implementation achieves the stated light-reduction behavior, including known device/group quantities and settings; do not merely duplicate the sequence requirement.

This is a required project narrative-data header. Existing linked project review records carry it until a versioned structured narrative contract is implemented.

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

All markup work remains live, editable and unflattened at every stage, including accepted reviews, issued/final coordinated packages and closeout. Narrative lock approves control direction; it does not lock or flatten owner-editable markup annotations. Preserve labels, symbols, geometry and stable annotation/object identities through assembly and subsequent edits. Follow the [LV annotation delivery rule](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md#annotation-identity-and-owner-return); printed schedule front sheets do not authorize flattening plan markups.

The LV first-milestone room map uses owner-directed presentation categories: ordinary enclosed rooms blue; corridors/halls/circulation tracking Spaces green; open activity/common areas (open offices, gyms, play, dining, assembly) ruddy orange; multi-level atriums/open-to-above areas violet; service voids and confirmed out-of-scope/no-lighting areas gray; exterior areas low-opacity wine/burgundy. These colors do not assign building/energy-code room types, occupancy groups or control requirements. Accepted footprints must be editable fillable closed shapes with a lighter low-opacity fill than the outline; redraw nonfillable footprints with identity reconciliation. Preserve multi-level served-Space ownership without duplicate floor areas/lights. Follow the [LV room-map directive](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md#finalized-room-map-for-the-first-package) for precedence, unresolved categories, scope exclusions and final PDF review.

After owner adoption locks the narrative, identify/count its physical sensors, manual switches/dimmers and other room devices with stable IDs and all served-zone associations. The LV extension produces a device schedule and device-specific provisional review locations: wall switches, scene controllers and dimmers at source electrical lighting-plan locations first, retaining accepted owner changes; only without usable source locations use latch-side door frames (adjacent solid wall when glazing intervenes) or common-area entry routes; occupancy and daylight sensors likewise start at source design locations. Only where no usable source location is available, propose ceiling occupancy sensors near room/child-zone centers and visible tile centers, wall occupancy sensors at displayed-plan top-left placeholders, corridor sensors near served-zone midpoints, and flagged daylight placeholders. Apply occupancy quantities to served child zones, without automatically adding parent sensors. Retain source sheet/revision/symbol evidence, register positions into the accepted working frame and flag source conflicts; do not silently relocate shown controls under a fallback rule. Use the linked milestone playbook for swing clearance, source uncertainty and fallback rules. Owner finalizes placement; these proposals do not establish sensor coverage or installation details. Owner-returned locations feed subsequent controller/aggregator routing. Retain parent/cluster behavior separately from micro electrical channels. [Milestone deliverables](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/milestone-review-packages.md).

## M2 Source Fixture-Schedule Evidence Handoff

The original MEP fixture schedule is source design information required during physical takeoff, before fixture count/type/continuity acceptance. Preserve exact marks and suffixes, descriptions, assembly/section/length clues, electrical facts and detail/note evidence separately from LV substitutions. Reconcile RCP geometry with schedule descriptions and electrical circuiting/daisy chaining; a circular L4/L4A path may be an assembly or separate typed pieces and must not be collapsed on appearance alone. Missing referenced schedules require retrieval; genuinely absent schedules are recorded and affected interpretations remain provisional. Complete physical identity reconciliation before downstream room controls/narrative review. See [LV M2 source schedule gate](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/m2-linear-fixture-extraction.md#m2-source-fixture-schedule-gate).

## Physical Intake Beta Handoff

Apply owner-directed physical-section counts within the documented decision scope, preserving assembly identity without double counts. Preserve exact plan tags independently of schedule marks; unresolved suffix meanings keep affected counts provisional. Keynote-only luminaires remain distinct source types with unknown electrical data until evidenced. Exterior fixtures without served Spaces remain explicit takeoff holdouts with reasons and quantities. Presentation geometry/color must not silently reassign lights or establish code area quantities. The owner uses CAD for actual area takeoffs; markup areas are checks. See the [LV M1/M2 beta playbook](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/m1-m2-beta-review.md) for room/annotation/frame implementation and scoped owner-reported Bluebeam validation.
