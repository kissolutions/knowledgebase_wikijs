---
title: Lighting Controls Guidance Index
description: Entry point linking room vocabulary, review inputs, existing lighting playbooks and unresolved guidance
published: true
date: 2026-10-05T12:40:08.000Z
tags: lighting, controls, space types, review
editor: markdown
dateCreated: 2026-10-04T03:18:00.000Z
page_type: reference
page_status: draft
confidence_level: medium
domain_primary: electrical-lighting
reference_kind: edge-case-catalog
ai_role: supporting_detail
ai_priority: medium
invocation_triggers:
  uncertainty_flags: [lighting_guidance_selection, room_classification_unknown, code_basis_unknown]
decision_axes: [space_function, selected_code_basis, source_intent, guidance_readiness]
parent_pages:
  - ../ontology/reg-and-class/interior-space-types.md
related_pages:
  - enclosed-office-lighting-controls-playbook.md
  - open-office-lighting-controls-playbook.md
  - ../ontology/signal-and-control-dev/occupancy-sensors.md
---

# Lighting Controls Guidance Index

## 0. Parent Page and Purpose

**Deepens:** [Interior Space Types](../ontology/reg-and-class/interior-space-types.md).

Find the relevant vocabulary/playbook and identify the inputs and verification still needed for a room's lighting-control review. This index is navigation and review support, not an automated compliance engine or a new control prescription.

## 1. Summary

WikiJS owns general electrical room/code analysis, control selection/configuration and decision trees. The [LV extension](https://github.com/kissolutions/lv-lighting-design) owns its project intake/model, boundary tracing, implementation/grouping and output routines. Keep project facts outside both framework repositories.

For an existing MEP design, extract its documented scheme before using these pages to check it. Missing source information or incomplete guidance creates a review finding. A KIS preferred design pattern is not automatically an approved replacement.

Use the [room classification and controls review playbook](room-classification-and-controls-review-playbook.md) for proposed synonym mappings, owner confirmation, source-function completeness, scoped permission to fill gaps and primary-source fallback when guidance is unfinished. The [application-guide draft](lighting-control-application-guide.md) and [IECC draft profiles](iecc-occupant-sensor-directives.md) are now owned here; their verification gaps remain open.

## 2. Detail

### Required Review Inputs

Record the source room name and supported actual use; independently selected Building Code Space Type, Building Code Occupancy Group and Energy Code Space Type; area and basis; enclosure/partition evidence; windows/skylights and daylight assessment; source fixture/control groups; lighting loads where a rule needs them; manual/occupancy/daylight/scheduling and emergency observations; source documents and revisions.

Establish the selected energy standard/compliance path, edition, jurisdiction, amendments, exact applicable sections and verification evidence. A room reference does not establish local adoption. Do not combine unrelated standards or treat a remembered threshold as a project requirement.

### Room-to-Guidance Map

The tokens below are retrieval aliases, not automatic classifications from source labels.

| Reviewed function / alias | Definition | Control guidance | Readiness |
|---|---|---|---|
| `enclosed_office` | [Enclosed office](../ontology/reg-and-class/interior-space-types.md#enclosed-office) | [Existing playbook](enclosed-office-lighting-controls-playbook.md) | Draft content exists; verify code statements and distinguish KIS defaults |
| `open_office` | [Open office](../ontology/reg-and-class/interior-space-types.md#open-office) | [Existing playbook](open-office-lighting-controls-playbook.md) | Draft content exists; verify edition-specific control-area and behavior rules |
| `corridor`, secondary circulation, door alcove, vestibule | [Circulation vocabulary](../ontology/reg-and-class/interior-space-types.md#corridors-and-circulation-spaces) | Dedicated control playbook pending | Guidance incomplete; manual review |
| Conference, meeting, huddle | [Room functions](../ontology/reg-and-class/interior-space-types.md#other-room-functions) | Dedicated control playbook pending | Guidance incomplete; confirm use/classification |
| Break room, copy/print, storage | [Room functions](../ontology/reg-and-class/interior-space-types.md#other-room-functions) | Dedicated control playbooks pending | Guidance incomplete; manual review |
| IDF / communications, wellness | [Room functions](../ontology/reg-and-class/interior-space-types.md#other-room-functions) | Dedicated control playbooks pending | Guidance incomplete; do not invent an exception |
| Reception, lobby, hospitality | [Room functions](../ontology/reg-and-class/interior-space-types.md#other-room-functions) | Dedicated control playbooks pending | Guidance incomplete; actual use/boundaries require review |
| Classroom | [Room functions](../ontology/reg-and-class/interior-space-types.md#other-room-functions) | Dedicated control playbook pending | Guidance incomplete; manual review |
| Primary/secondary daylight zones | [Daylight vocabulary](../ontology/reg-and-class/interior-space-types.md#daylight-vocabulary) | Edition-specific geometry/control guide pending | Record geometry and applicability separately; manual review |

Supporting hardware/function pages: [occupancy sensors](../ontology/signal-and-control-dev/occupancy-sensors.md), [lighting powerpack](../ontology/signal-and-control-dev/lighting-powerpack.md), [automatic receptacle control](../ontology/functional-constructs/automatic-receptacle-control.md). Hardware fundamentals do not prescribe the room's sequence or establish code applicability.

### Separate Four Sources of Meaning

| Information | Record and apply as |
|---|---|
| Source drawing/schedule/sequence | Observed project intent, with document/revision/locator |
| Code requirement | Selected standard/edition/section, applicable condition, exceptions and verified source |
| KIS default/preference | Organizational design choice with its decision gates; distinct from a code mandate |
| Project-specific departure | Proposal, authority, approval and adopted change, while preserving the original intent |

### Review Result

Record assessed functions, source/code/guide references and revisions, facts relied on, reasoning, reviewer/date and unresolved questions. Use `not_reviewed`, `compliant`, `deficient`, `ambiguous_source`, or `no_information` for the reviewed scope. A deficient finding requires identified conflicting behavior and a verified applicable criterion. Missing documents or guidance do not by themselves prove deficiency or compliance. Separately flag typical implementation versus manual review and preserve proposals/approvals.

## 3. Edge Cases

| Case | Treatment | Consequence |
|---|---|---|
| Area has no tag | Document actual architectural association or an owner-reviewed proposal | Do not create a room/control classification from fixture placement |
| Finish change splits corridor tracking | Retain architectural evidence and reviewed Space extents | Does not automatically require two independent control zones |
| Source controls absent | Record no information after reviewing available sources | Physical room/fixture intake can continue; affected design remains pending |
| Playbook missing or draft rule unverified | Follow the selected-code primary-source fallback and flag the derivation for owner approval | Keep unresolved options/conditions visible; no automatic recipe or compliance finding |
| Office area near a numerical trigger | Resolve area/convention and the selected rule | Vocabulary alone never supplies a universal cutoff |

## 4. Applicability Limits

Existing office playbooks include legacy broad edition statements and citation placeholders that need primary-source review before their numbers become reusable verified rules. This index does not validate those statements. No new sensor counts, timeouts, dimming percentages, daylight dimensions or exemption thresholds are adopted here.

A future verified rule profile should state standard/edition, exact section/source, conditions, exceptions, required behavior, amendment scope, reviewer/date and status. Develop those profiles before exposing numeric rules to an automated checker. Do not infer physical sensor quantity from control-area quantity alone.

### Future Feature: 2018 IECC Daylight-Control Exception Calculations

**Status: Flagged for later development; not implemented or adopted as a verified rule.** Build a WikiJS calculation guide and reusable calculator/review worksheet for numerical daylight-responsive-control exceptions. The initial target is the owner's supplied excerpt showing the adjusted interior lighting power allowance in Equation 4-9, provisionally indexed to 2018 IECC C405.2.3 Exception 4. Verify the full selected code text, printing/errata, jurisdiction/amendments and applicability before using the calculation to support a project decision. Keep other exceptions and later editions separate until individually verified.

The supplied excerpt gives this candidate calculation:

`LPA_adj = LPA_norm × (1.0 − 0.4 × UDZFA / TBFA)`

Planned inputs and checks:

- Establish whether the exception's new-building condition and the project's compliance path apply; retain evidence for other provisions that may independently require daylight controls.
- Determine connected lighting power using the applicable C405.3.1 accounting, rather than assuming a fixture-takeoff sum or LV output load is the code quantity.
- Determine normal interior lighting power allowance using C405.3.2 and any applicable C406 adjustment identified by the excerpt. Record the allowance method, area categories and verified inputs.
- Derive uncontrolled sidelit/toplit floor area (`UDZFA`) from verified edition-specific daylight-zone geometry and actual/proposed daylight-control coverage. Resolve overlapping areas and partial coverage under the verified rule; do not blindly sum room or zone areas.
- Determine total floor area (`TBFA`) using the same building-area scope included in the allowance calculation. A room-only or partial-project takeoff must not silently substitute for the required building-wide inputs.
- Use consistent units, retain input evidence and calculation precision, and flag missing inputs or impossible area relationships. A zero/unknown denominator cannot produce an exception finding.

The planned report should show inputs, area/allowance basis, equation substitution, adjusted allowance, comparison with connected lighting power, numerical margin and unresolved applicability questions. Distinguish a calculated comparison from an approved exception determination. Include reviewed worked examples and meaningful boundary/missing-input tests when the calculator is implemented. General calculations belong here; an LV project may supply evidence and consume a reviewed result without maintaining a duplicate code rule.

Development evidence: owner-supplied cropped excerpt, October 2026. The full adopted text and surrounding conditions have not yet been validated for this feature. The [ICC 2018 IECC Chapter 4 entry](https://codes.iccsafe.org/content/iecc2018/chapter-4-ce-commercial-energy-efficiency) is a retrieval starting point, not evidence that the full text was reviewed. No project calculation, exception approval or software implementation is created by this backlog entry.

### Pending M3 Guidance Backlog

**Status: All items flagged for later work; none is completed or promoted to a verified rule by this list.** Preserve the first M3 testing agent's F-1 through F-18 identifiers and suggested priorities below. High means the agent reported needing direct owner input to complete its framework-driven review; priority is not a determination of engineering consequence or an instruction to defer unresolved project obligations. Requirements, proposed KIS defaults, beta-project owner decisions and system-specific constraints need separate treatment when developed.

| ID | Reported priority | WikiJS home / work to address |
|---|---|---|
| F-1 | High | New conference/huddle playbook: sensing function, manual-on versus proposed 50% automatic-on, independent fixture-type controls, dimming and optional daylight-capable design. Distinguish required daylight operation from a capability/preference. |
| F-2 | High | New lobby/reception/hospitality playbook: time-switch operation/override, fixture-type dimmers, staff-controlled counter open/closed modes, shelf and under-counter task/background lighting. |
| F-3 | High | New corridor playbook: edition-specific scheduling/occupancy requirements and proposed KIS partial-off sequence of 20% after 20 minutes. Verify which functions apply before adopting a sequence. |
| F-4 | Medium | New break-room playbook: proposed 50% automatic-on, mixed fixture-type dimmer choices, and under-cabinet lighting with scheduling and a local counter switch. |
| F-5 | Medium | Small enclosed-room guidance for storage/coat/IDF/copy-print: proposed vacancy on/off and five-minute delay, equipment-room sensor placement, and classification choice between a named room category and an area-based enclosed-space provision. Do not assume these room uses share every requirement. |
| F-6 | High | Expand open-office playbook: verified edition-specific zone-area limits, reduction and whole-space shutoff; fixture-group/area reconciliation. Review the beta sequence: occupancy brings all zones to 20% and the occupied zone to full; a vacant zone returns to 20% after 20 minutes; all off when all zones are empty. Resolve timing/transition ambiguities before reuse. |
| F-7 | High | Enclosed-office selection gate: where the selected system lacks a compatible combination sensor/switch, evaluate a ceiling sensor plus separate wall switch. General selection logic belongs here; actual system capability evidence belongs in its extension. |
| F-8 | Low | Verify and correct the reported 10-versus-20-minute inconsistency in the enclosed-office text; resolve/remove leftover citation markers using reviewed primary-source evidence. |
| F-9 | Medium | Verify and edition-tag the reported 250 SF, daylight-exemption and office continuous-dimming statements in the office playbook and Interior Space Types. The owner's 2024 attribution is a review lead, not validated code text. |
| F-10 | High | Complete the selected 2018 profile from primary text: scheduling and reported two-hour/5,000 SF override conditions; manual reduction; under-cabinet specific-application controls; full automatic-on permissions; daylight triggers/sidelit geometry; Exception 4 calculation; and allowance values/methods. Explicitly assess tenant-remodel applicability rather than applying a new-building exception automatically. Coordinate with the existing daylight-calculation feature above. |
| F-11 | Medium | Review candidate KIS defaults from beta: five-minute small-room and 20-minute office/common-space delays; corridor 20% partial-off after 20 minutes; reception master time-switch button; under-cabinet background/task operation; daylight-capable design while considering the power exception; and an unsplit cove ring for aesthetics. Separate code constraints, compatibility and independent-control needs from preferences before promotion. |
| F-12 | Medium | Expand classification decision examples: a wellness room used as an enclosed office, hospitality functioning as lobby, and an alcove light intentionally scheduled as a night light. Preserve actual use and owner basis; names alone do not establish classification, and night-light operation is a separate decision. |
| F-13 | Medium | Develop reviewed room/application examples supporting sensor quantity, placement and coverage proposals. Examples supplement verified equipment/coverage evidence; absence of an example is not automatically a prohibition on an evidence-based proposal. |
| F-18 | Low | Develop emergency/exit lighting guidance and source-review routing. Preserve missing-source observations separately from unfinished knowledge guidance; a backlog priority does not resolve a project's emergency-lighting obligations. |

The remaining four items belong to the LV extension and are linked here so none is lost:

| ID | Reported priority | LV work to address |
|---|---|---|
| F-14 | High | Step 1/code-basis establishment: identify the actual authority having jurisdiction, rather than using mailing-city text as proof; record selected code basis before dependent M3 conclusions. |
| F-15 | Medium | M3 review evidence/output home for gate scope/status, owner directions/interpretations, adopted narrative and per-room checks; develop agreed model status fields without making a generated owner-decision report a new primary record. |
| F-16 | Medium | Explicit design-build/minimal-source-controls branch: record source gaps, then use existing applicable owner authority/narrative and the WikiJS review gates. Do not interpret missing source controls as automatic permission to design. |
| F-17 | Low | Document verified selected-system constraints/capabilities that shape narratives: combination-device availability, software sequence reconfiguration and daylight-capable hardware. Do not generalize beta-system properties to all LV systems. |

Track LV work in the [extension roadmap](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/governance-and-doctrine/roadmap.md#pending-m3-lv-workflow-gaps). Development evidence: owner-supplied *LV_Framework_Guidance_Gaps_M3.md*, October 2026. This is a backlog transcription and ownership review, not verification of the agent's numerical/code claims. Keep the original testing report and project decisions in approved project storage. General guidance promotion requires its own review; project acceptance does not establish a reusable standard.

## 5. Sources and Validation

Owner-confirmed Beta 1 workflow and vocabulary decisions, October 2026; existing WikiJS office playbooks and the Interior Space Types catalog. This is a draft navigation/terminology update, not regulatory verification. Repository paths are supplied for agent retrieval; WikiJS page routes omit the `.md` suffix.

## 6. Status and Stewardship

- **Status:** Draft; room control profiles and code verification remain incomplete.
- **Last Review:** 2026-10.
- **Owner:** KIS Solutions.


## SmartDC/EPS device-specific allocation

[Device allocation index](smartdc-allocation-index.md): QDCD, CIO, SW4/SW8 and EPS PDU hardware constraints and mini playbooks. Apply after designated micro channels; distinguish manufacturer facts from owner preferences and open verification.
