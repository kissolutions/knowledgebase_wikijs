---
title: Drawing-Based Spatial Extraction and Verification v0.1
description: AI-led extraction, visual and geometric registration, and traceable human review of drawing-derived objects
published: true
page_type: playbook
page_status: draft
confidence_level: medium
domain_primary: systems-engineering
ai_role: prescriptive_standard
invocation_triggers:
  uncertainty_flags: [drawing_extraction, cross_drawing_transfer, spatial_discrepancy, owner_markup_return]
decision_axes: [visual_completeness, coordinate_registration, object_correspondence, acceptance_preservation]
related_pages:
  - ../AI/AGENT-FRAMEWORK-GUIDE.md
  - ../governance-and-doctrine/systems-engineering-framework-v1.md
editor: markdown
---

# Drawing-Based Spatial Extraction and Verification — v0.1

## 1. Purpose and Use

**Process ID:** `PROC-DRAWING-SPATIAL-EXTRACT`; **Version:** `0.1`.
Invoke for drawing-derived inventories, boundaries, symbols, devices, equipment, routes or endpoints, initially during Intake and again when drawings, working frames or owner geometry change. This shared method governs evidence and review; domain playbooks retain object definitions, source precedence, counting rules, markup styles and milestone criteria.

## 2. Design Intent

**AI performs the heavy extraction work. Human review makes it authoritative within the stated review scope.**

The normal workflow is **AI interpret → AI extract → AI visually verify → owner review/correction → AI reconcile → owner acceptance**. The owner primarily reviews, corrects, clarifies and approves. Owner-first digitizing is a valid chosen alternate path, not the default response to inconvenient PDF structure. Attempt every reasonably discernible in-scope object before presenting the first package; owner corrections should be exceptions rather than the main extraction mechanism. This is a performance objective, not a measured accuracy or time-saving claim.

## 3. Space / System Definition (Decision-Oriented)

| Evidence channel | Governs or establishes |
|---|---|
| Rendered source drawing | Depicted presence, apparent count, arrangement, approximate location and spatial meaning |
| PDF text, vectors, objects and coordinate geometry | Candidate discovery, transcription, measurement and reproducible precision |
| Legends, schedules, notes and related source views | Symbol meaning, physical occurrence/assembly interpretation and source intent |
| Project registers, model and annotation IDs | Persistent identity, relationships, review history and current reconciled configuration |
| Owner corrections and acceptance | Reviewed geometry or intent within the explicitly stated scope; preserve source observations separately |

No channel alone establishes completeness. A visible symbol is not automatically one physical device or fixture; apply domain counting and interpretation rules. A drawing depicts design information, not proof of installed field conditions.

## 4. Constraint Envelope

### 4.1 Hard Constraints

Retain source/revision provenance, stable identities, explicit unresolved findings and accepted configurations. Visual interpretation does not override source precedence, engineering constraints or approved counting rules. Conflicting evidence requires reconciliation.

### 4.2 Soft Constraints

Use a useful whole-sheet view and focused crops at sufficient resolution to distinguish relevant symbols. Scale review detail to the drawing and project; no universal pixel resolution or registration tolerance is imposed here.

### 4.3 Hidden Constraints

Crop boxes, rotation, resizing, differing revisions, repeated details, multiple levels, overlays and scans can make apparently valid coordinates misleading. Do not omit visible objects because their PDF representation is inconvenient or the existing register lacks them.

## 5. Baseline / Default Design Pattern

**Inputs:** Stated scope; registered source sheets/views/revisions; relevant legends, schedules and notes; existing authoritative registers; accepted geometry and owner returns; source and target coordinate frames when transferring objects. Missing evidence stays identified.

1. **Render and interpret.** Render every applicable source plan/view. Inspect the entire in-scope area and detailed regions, including untagged areas, repeated patterns and small or partially obscured symbols. The agent creates its own renders/crops; request an owner image only to resolve a specific ambiguity or unavailable view, not as a routine prerequisite.
2. **Extract.** Combine rendered interpretation with available text/vector/object/geometry data and related sources. Preserve source observations and uncertainty independently of proposed canonical object interpretations.
3. **Reconcile visually.** Compare the inventory and rendered generated markup with the source, area by area. Check count, arrangement, individual correspondence, location and relationships. Matching totals alone can conceal an omission paired with a duplicate.
4. **Review.** Present a substantially completed editable extraction package and focused questions. Keep uncertain objects visible and identified instead of silently omitting them or guessing.
5. **Ingest corrections.** Match returned annotations by persistent identity, retain the returned geometry/frame and review provenance, then reconcile the authoritative records and regenerate derived views. Do not optimize an accepted correction back toward a rejected machine interpretation.
6. **Record completion.** State the reviewed scope, evidence, corrections and remaining exceptions. Human acceptance remains distinct from automated consistency checks.

## 6. Typical Variants

**Owner-first markup:** Ingest supplied geometry and observations, preserving their identities or explicitly reconciling new annotations. Perform the same source/completeness checks for the agreed scope.

**Cross-drawing transfer:** Before bulk transfer:

1. Render source and target views and confirm compatible revision, scope and served level.
2. Establish the coordinate transform from common architectural/fixed features distributed across the mapped area: walls, corners, columns, doors or grids. Reconcile scale, rotation, crop and page/view frame. Choose enough nondegenerate controls for the transform used.
3. Record source/target frames, original source coordinates, transform basis and transformed target coordinates separately. Never repeatedly transform already transformed coordinates as if they were source data.
4. Produce an overlay or equivalent visual registration check. Inspect multiple distributed locations, including opposite/extreme sides, preferably with check features not used to fit the transform. Record residual/misalignment evidence and the task-specific adequacy judgment; do not assert precision beyond the source.
5. Bulk-transfer only within the verified extent. Establish and verify registration independently of the objects being transferred; those objects must not be the sole fit-and-check basis.
6. After transfer, separately verify **geometric correspondence** (positions align) and **object/semantic correspondence** (the correct object lands in the intended room, door, wall or other feature). The transferred objects are required evidence in this second check. A correct transform does not prove correct object selection or association.

If a single transform cannot align the relevant region, investigate revision differences, scan distortion or separate view frames; use documented local registrations where justified or leave the affected region unresolved.

## 7. Decision Gates

- **Discrepancy reported or detected?** Inspect a focused rendered source/markup crop before another corrective register/coordinate pass. Resolve depicted meaning first; if it remains ambiguous, retain the finding and seek focused clarification. Never cycle through repeated data-only corrections.
- **No usable visual source?** Continue supported nonspatial work, identify the affected extraction as not visually verified and obtain the missing view. Do not claim visual review from object extraction.
- **Transfer not registered?** Keep bulk transfer of the affected region pending; other verified regions can proceed.
- **Accepted geometry conflicts with new evidence?** Retain both and report the conflict. Reopening is scoped; acceptance does not authorize silent source-fact replacement or unrelated changes.

## 8. Design Zoning / Grouping Strategy

Review by meaningful areas/Spaces and served levels, checking sheet edges and transitions between areas as well as repeated groups. Grouping a review does not create functional zones, change scope or establish room classifications.

## 9. Common Failure Modes

- Treating all processed PDF objects as a complete inventory.
- Matching counts without checking individual locations and duplicates.
- Using transferred objects as the only registration controls and the only verification evidence.
- Moving model objects to fit label positions or silently reversing accepted owner edits.
- Reporting a software pass as visual verification or milestone acceptance.

## 10. Safe Assumptions (and Limits)

Approximate geometry may be an explicitly provisional review proposal where the domain permits it. It never establishes unsupported source names, classifications, physical assembly counts or design behavior. Unknowns remain unknown.

## 11. Documentation Expectations

Keep lightweight project evidence: process version or immutable repository revision, scope and inputs/revisions, source/target frames and registration basis where applicable, visual comparison/crop references, affected stable object IDs, findings/dispositions, reviewer and acceptance scope. A per-area count comparison can remain a verification artifact; it need not become a canonical model field.

Work products are the reconciled authoritative inventory/geometry records, editable derived markup, registration evidence where needed and review/findings record. Owner-returned annotations remain source evidence for reconciliation. Preserve superseded mappings/history; reports and overlays must not become competing registers.

## 12. When to Go Deeper / Exit This Playbook

Escalate unresolved symbols, conflicting revisions, unreadable views, nonrigid distortion, ambiguous associations or consequential owner/source conflicts for targeted review. Carry exceptions by affected object/area and downstream consequence. Logging an exception does not make the affected inventory complete or accepted; unaffected work can proceed. No approval form per object or mandatory global stop is introduced.

## 13. Cross-Links to Supporting Knowledge

- [AI Agent Framework Guide](../AI/AGENT-FRAMEWORK-GUIDE.md)
- [Shared lifecycle, process, review and acceptance contract](../governance-and-doctrine/systems-engineering-framework-v1.md)
- [Framework Extension Doctrine](../governance-and-doctrine/framework-extension-doctrine.md)

## 14. Status and Stewardship

- **Status:** Draft shared method adopted for supervised execution; automated completeness and registration verification are not supplied by this page.
- **Last Judgment Review:** 2026-10-25.
- **Playbook Owner:** KIS Solutions.
- **Completion:** The stated scope has a visual inventory/markup comparison, applicable registration and object-level checks, reconciled corrections and explicit remaining exceptions; domain human acceptance criteria still apply.
- **Tailoring:** Review artifacts and detail may be scaled to complexity. Preserve visual inspection, provenance, stable identities, explicit unknowns and accepted geometry.
- **BETA evaluation:** On a small synthetic drawing pair with several rooms, a rotated/cropped frame and a known omission/duplicate pair, compare prior and revised procedures. Check completeness beyond matching totals, distributed registration, wrong-room detection, label-only movement and preservation of an owner-moved anchor. Record observed results and limitations; this page does not claim that evaluation has run.

## 15. Author Notes (Institutional Context)

Generalizes owner-reviewed LV extraction proposals 004–010. Annotation font/marker settings and LV-specific inventory/milestone rules stay in the domain extension. This is an organizational execution method, not a code requirement or claim of automated drawing understanding.
