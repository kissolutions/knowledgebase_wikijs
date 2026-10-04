---
title: Lighting Controls Guidance Index
description: Entry point linking room vocabulary, review inputs, existing lighting playbooks and unresolved guidance
published: true
date: 2026-10-04T03:18:00.000Z
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
| Playbook missing or draft rule unverified | Record guidance incomplete and seek manual review | Do not substitute a similar room's recipe without a supported decision |
| Office area near a numerical trigger | Resolve area/convention and the selected rule | Vocabulary alone never supplies a universal cutoff |

## 4. Applicability Limits

Existing office playbooks include legacy broad edition statements and citation placeholders that need primary-source review before their numbers become reusable verified rules. This index does not validate those statements. No new sensor counts, timeouts, dimming percentages, daylight dimensions or exemption thresholds are adopted here.

A future verified rule profile should state standard/edition, exact section/source, conditions, exceptions, required behavior, amendment scope, reviewer/date and status. Develop those profiles before exposing numeric rules to an automated checker. Do not infer physical sensor quantity from control-area quantity alone.

## 5. Sources and Validation

Owner-confirmed Beta 1 workflow and vocabulary decisions, October 2026; existing WikiJS office playbooks and the Interior Space Types catalog. This is a draft navigation/terminology update, not regulatory verification. Repository paths are supplied for agent retrieval; WikiJS page routes omit the `.md` suffix.

## 6. Status and Stewardship

- **Status:** Draft; room control profiles and code verification remain incomplete.
- **Last Review:** 2026-10.
- **Owner:** KIS Solutions.
