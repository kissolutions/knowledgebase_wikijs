---
title: "M3 Lighting Controls Sequence Lifecycle v0.1"
page_type: playbook
page_status: draft
domain_primary: electrical-lighting
ai_role: prescriptive_standard
published: true
tags: [lighting, M3, process, sequences]
editor: markdown
---

# M3 Lighting Controls Sequence Lifecycle v0.1

**Phase 2 — Design Basis & Requirements; Milestone M3 — Controls Narrative and Sequence Assignment.**
This lifecycle instantiates the shared KIS phase/process/milestone distinctions. It is a design-basis review cycle, not automatic approval of new control design or a requirement to implement physical sensor placements at M3.

## Flow

```mermaid
flowchart TD
 A["M1/M2 verified Spaces, Light Points, MEP evidence"] --> B["PROC-M3-CLASSIFY: candidate room/building/energy classifications"]
 B --> C{"Owner confirms applicable classifications?"}
 C -- No --> B
 C -- Yes --> D["PROC-M3-REQUIREMENTS: adopted code, exact requirements, exceptions"]
 D --> E["PROC-M3-SOURCE-CONTROLS: extract & compare MEP controls by function"]
 E --> F{"Complete supported source intent? / Changes authorized?"}
 F -- Unknown or gap --> G["Record findings; obtain scoped authorization or owner direction"]
 G --> H["PROC-M3-SEQ-MATCH: approved standard library"]
 F -- Source scheme acceptable --> H
 H --> I{"Approved SEQ matches and respects source intent?"}
 I -- Yes --> J["Propose SEQ-### revision"]
 I -- No --> K["PROC-M3-SEQ-AUTHOR: propose PSEQ-### with owner direction"]
 J --> L["PROC-M3-SEQ-VERIFY: required functions, options, source consistency"]
 K --> L
 L --> M{"Verifiable and approved interpretation?"}
 M -- No --> H
 M -- Yes --> N["PROC-M3-ZONE-ASSIGN: parent/leaf structure; SEQ on leaves only"]
 N --> O["PROC-M3-CROSS-REFERENCE: every Space, daylight determination, Light Points"]
 O --> P["One sequence narrative per ID/revision + associated rooms/leaves"]
 P --> Q{"M3 owner review and acceptance gate"}
 Q -- Rework --> B
 Q -- Accepted scoped direction --> R["M3 locked review; deferred details to M4/M5"]
```

## Stable M3 processes and work products

| Process ID | Primary input | Work product and invariant |
|---|---|---|
| `PROC-M3-CLASSIFY v0.1` | Architectural facts, actual use, occupied level, M1 Space register | Candidate **independent** Building Code Space Type, Building Code Occupancy Group, and Energy Code Space Type; owner confirmation or unknown |
| `PROC-M3-REQUIREMENTS v0.1` | Reviewed classifications, selected code edition/path/jurisdiction, amendments, area/enclosure, daylight evidence | Applicable requirements and exceptions matrix with exact source locators; unknown applicability remains open |
| `PROC-M3-SOURCE-CONTROLS v0.1` | M2 drawings, notes, symbols, schedules, existing sequences | By-function source observations and compliant/deficient/ambiguous/no-information/not-reviewed findings; never overwrite source intent |
| `PROC-M3-SEQ-MATCH v0.1` | Requirements, documented source functions, code profile, approved [SEQ Registry](lighting-control-standard-sequences.md) | Ranked candidates with applicability, revision, verified coverage and conflicts; never auto-select reserved draft entries |
| `PROC-M3-SEQ-AUTHOR v0.1` | Missing fit and explicit owner scope/authorization | Project-owned `PSEQ-###` narrative draft, parameters, evidence and unresolved issues; no silent promotion to standard |
| `PROC-M3-SEQ-VERIFY v0.1` | Proposed SEQ/PSEQ, adopted source, requirements | Per-function behavioral and code-applicability comparison, source-intent conflict finding, documented limitations |
| `PROC-M3-ZONE-ASSIGN v0.1` | Reviewed sequence and necessary functional subdivisions | Proposed endpoint/leaf zone assignments with exact sequence ID + revision and any parameter/owner overrides. **Parents have no assigned SEQ.** |
| `PROC-M3-CROSS-REFERENCE v0.1` | Spaces, Light Points, proposed zones/sequences, daylight determinations | All-Space narrative/fixture coverage review, lightless/service exceptions, missing-direction findings, M4/M5 deferrals |

A process may repeat for a subset of the project; do not multiply owner approval requests for each internal iteration. Confirming classification, authorizing gap filling, accepting an interpretation, and adopting a sequence are **distinct** owner decisions. Use one consolidated M3 review package after incremental issue resolution.

## Governing constraints

1. **Source vs requirement vs design proposal:** Preserve MEP source intent even when it differs from KIS preference. An existing design cannot be replaced merely because a library sequence looks attractive. Require scoped redesign authority and a separately approved result.
2. **Standard eligibility:** `SEQ-###` denotes KIS framework-managed standard identity; only approved revisions are valid standard selections. `PSEQ-###` is project-scoped and must be reviewed before adoption.
3. **Zone hierarchy:** A parent is only a container/coordination/aggregation node; it owns no direct luminaire assignments or physical outputs and receives **no `sequence_id`**. Every endpoint/leaf zone with accepted M3 direction references exactly one sequence identity/revision. A whole-room zone without children is a leaf. Daylight conditions can overlap occupancy leaves and remain independently traceable rather than being forced into one nesting hierarchy.
4. **Geometry vs requirements:** At M3 establish only functionally necessary zone splits and their rationale, such as an applicable open-office independent-control-area upper bound, shared aggregate conditions or daylight partitions. M4 establishes practical boundaries/device positions and verifies coverage. Do not infer physical sensor counts from zone counts.
5. **Narrative sufficiency:** Distinguish manual on/off, automatic activation, vacancy timeout/reduction, daylight, scheduling, light reduction, emergency/normal interaction, functional grouping and parameter uncertainty. Owner-level trigger, resulting state and control method are enough where later setpoints/timing detail is expressly deferred.
6. **Review coverage:** Every Space has explicit daylight determination (`yes/no/unresolved` with evidence), and every lit Space has a traced control direction. Any unlit Space is explicitly reconciled as intentionally unlit, served by another Space, missing source light data, or unresolved.
7. **Acceptance:** Issue one complete narrative per sequence ID and revision, followed by every assigned room/leaf and per-assignment variation/exception. Owner-approved lock applies only to the identified scope/revision and does not certify deferred field details or compliance beyond verified provisions.

## M3 acceptance gate

Release when: classification and code applicability are sufficiently supported; every applicable source-control function is recorded and compared; authorized sequence decisions are accepted; all leaf assignments and aggregate interfaces are traceable; daylight and all-Space fixture cross-reference is complete; consequential source/service conflicts are resolved; and acceptable M4/M5 deferrals have specific owners/scope. Otherwise retain an identified provisional M3 package, and continue unaffected work.

**Implementation note:** This describes the required process. The existing LV v0.7 model does not implement endpoint sequence references or a full code matcher; the LV extension will adopt a separately versioned companion contract and test it without falsely altering older project models.

**Owner:** KIS Solutions; 2026-10-17; v0.1.
