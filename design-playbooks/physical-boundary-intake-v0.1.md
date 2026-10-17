---
title: Physical Boundary & Barrier Intake Process v0.1
description: Reusable targeted or full intake procedure creating a verified-by-source physical boundary register
published: true
tags: playbook, process, boundary, MEP, fire-life-safety
editor: markdown
---

# PROC-PHYSICAL-BOUNDARY-INTAKE — v0.1

**Status:** Process skeleton; manual/agent-assisted pilot, not an automated extractor. **Parent contract:** [KIS Systems Engineering Framework v1.0](../governance-and-doctrine/systems-engineering-framework-v1.md). **Work product:** [Physical Boundary Register v0.1](../ontology/physical-boundary-register-v0.1.md).

## Purpose and invocation

Identify *physical construction boundaries* that matter to a system of interest, record drawing/field evidence and construction/classification uncertainty, and provide reliable inputs to later route and penetration reviews. May be invoked in **Phase 1 Intake** initially and revisited whenever a source revision, routing change or site finding exposes missing boundary data.

**Modes:**
1. **Targeted intake (default):** Register only boundaries crossed, approached, used as mounting constraints or necessary to understand in-scope interfaces.
2. **Full inventory (on instruction):** Survey physical boundaries over a defined project scope. Never infer that a project requires all building walls registered.

### Inputs

Defined SoI and physical area; applicable Space Register/room boundaries; architecture and life-safety plans, partition schedules, wall types, RCP, structural drawings, drawings' dates/revisions; source register; project code-basis candidates; existing markups and accepted geometry; field observation where supplied. Mark missing critical sources as open items.

### Method

1. **Establish boundary scope.** State full/targeted mode, source revisions and relevant systems/routes. Distinguish physical walls/barriers from logical room/zone boundaries.
2. **Find candidates.** Inspect relevant plans and schedules, following visible wall/assembly geometry and identifying shafts, slabs, enclosures and rated/smoke separations. Avoid cataloging irrelevant details.
3. **Assign identity and relationships.** Allocate stable Boundary IDs; reference adjacent Space IDs where supported. For exterior or unmodeled sides use context notes, not fabricated Room IDs. Segment where construction or protection requirements differ.
4. **Capture evidence.** Record physical type, source terminology, indicated rating, classified designation, smoke barrier/partition observations, location and persistent markup/CAD geometry ID. Preserve exact drawing sheet/detail and revision.
5. **Classify carefully.** Record *source_observed* when drawings supply a designation and *verified* only when supported by the applicable reviewed code-basis and competent review. Treat rating and classification independently. Never infer Fire Barrier from 2 HR alone, or infer nonrated/no smoke barrier from lack of indication.
6. **Reconcile.** Compare room adjacency, plan versus life-safety/partition schedules, and source revisions; record conflict/open items. Respect existing individually accepted geometry.
7. **Review package.** Produce/update editable Boundary Register, optionally unflattened color/label markup and discrepancy list; summarize limits of source coverage and unknowns. Ask human to confirm only consequential uncertain classifications, boundaries and exclusions.
8. **Persist.** Update the authoritative project register; record process version, scope, inputs/revisions, findings and owner decisions. Other derived views regenerate from this register.

### Invariants and validation

- Unique non-reused Boundary IDs and valid stable Space references when provided.
- Every asserted classification/rating/smoke designation retains suitable source evidence; absent evidence remains unknown.
- Logical Space boundary and physical construction boundary are distinct.
- No automatic approval of wall penetration, firestop design or engineering compliance from geometric intersection.
- Previously accepted segments are not silently redrawn or reclassified by derived processes.
- Scope disposition describes responsibility separately from modeled inclusion.
- No milestone is declared passed merely because structural checks pass.

### Completion / tailored effort

Complete for the **stated survey scope** when every identified consequential boundary has a record or explicit unresolved finding; source-revision references and human review questions are available. Unsurveyed portions remain unsurveyed (not confirmed nonrated). A small project may use a concise register and single review markup; a healthcare/multilevel scope may need cross-discipline reconciliation. Do not relax invariants.

### Later process handoff — Boundary Crossing Review (candidate)

**PROC-BOUNDARY-CROSSING-REVIEW**, version pending: input boundary register plus proposed routes; identify candidate intersections; verify crossing context, construction type, rating, penetration/existing opening evidence, code requirements and responsibilities; output crossing review items and constraints. No automatic firestop selection or acceptance of a penetration. This is a handoff specification, **not** a claim of implementation.

### Process validation / BETA test

Use a compact two-room wall/corridor drawing with one rated separation, one unclassified partition and one route crossing. Check adjacency, class/rating separation, unknown smoke status, persistent annotation ID, source locator and route handoff. Test preservation of an accepted segment across re-extraction. Capture process version and differences from earlier methods.
