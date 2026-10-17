---
title: Boundary Crossing Review Process v0.1 - Skeleton
description: Preliminary reusable review procedure for route crossings of physical construction boundaries
published: true
tags: process, boundary, routing, coordination
editor: markdown
---

# PROC-BOUNDARY-CROSSING-REVIEW — v0.1 skeleton

**Status:** Proposed/manual only; no algorithm, code checker, firestop product selection, or automatic crossing geometry implementation.

**Trigger:** A route or proposed installation crosses (or might cross) a registered physical boundary, or an unregistered boundary appears in construction/routing review.

**Inputs:** [Physical Boundary Register](../ontology/physical-boundary-register-v0.1.md), route segment identities/geometry and source versions, project code basis, applicable partition/life-safety plans, proposed installation details, approved/accepted route constraints.

**Proposed procedure:** (1) identify candidate crossing with stable route and Boundary IDs; (2) verify actual physical intersection and existing opening/penetration status; (3) determine applicable construction, fire/smoke, installation and responsibility constraints; (4) record requirement references, unknowns and coordination actions; (5) return findings to route design and MEP coordination without silently changing accepted routes.

**Minimum output:** Crossing ID, Boundary ID, Route/Segment ID, proposed location/geometry ref, crossing state (candidate/verified/not_a_crossing/unresolved), known construction classification/rating, needed clarification, required reviewer, source reference, action/status.

**Invariants:** A plan-line crossing is not proof of a new penetration. Classification and firestop details require authoritative source/code/assembly evidence. Protection of previously accepted route geometry is preserved; contradictions become findings/change proposals.

**Completion:** Scoped candidate intersections are accounted for and unresolved high-consequence construction/protection issues are explicitly flagged. Actual release requirements remain defined by the invoking domain/project.

**Tailoring:** Small projects may use a generated CSV plus markup; complex ones may need dedicated crossing/penetration coordination packages. Not a mandatory complete penetration register.
