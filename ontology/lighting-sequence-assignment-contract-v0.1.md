---
title: "Lighting Sequence Assignment Contract v0.1"
page_type: canonical_model
page_status: draft
domain_primary: electrical-lighting
published: true
tags: [lighting, sequence, assignment, M3]
editor: markdown
---

# Lighting Sequence Assignment Contract v0.1

**Scope:** Cross-domain, project-independent semantic contract for matching and assigning standard or custom lighting-control sequences at M3. Project instances and executable validators belong in domain/project repositories. See [M3 Lifecycle](../design-playbooks/m3-lighting-sequence-lifecycle-v0.1.md) and [Standard SEQ Registry](../design-playbooks/lighting-control-standard-sequences.md).

## Identity and scope

- **Standard** `SEQ-###`: globally unique in the framework, versioned definition in WikiJS. Only `approved` revisions are standard selectable candidates.
- **Custom** `PSEQ-###`: project-scoped identity for owner-directed behavior, not automatically reusable in other projects. May be promoted later through a separately assigned standard ID and review.
- **Sequence definition** and **sequence assignment** are separate records; editing one must not silently edit the other.
- **Endpoint zone**: zone with no child zones in the project hierarchy. Only endpoint zones have one active sequence assignment. Parents have no assignments and derive aggregate relationships; one endpoint can serve several Spaces when source control intent and constraints allow.
- **Revision:** retain explicit definition revision and project/model revision on assignments; never resolve an existing assignment to an unpinned latest revision.

## Sequence definition minimum

`id` (SEQ or project-scoped PSEQ); `revision`; `origin` (standard/project); `status` (draft/reviewed/approved/superseded); `title`; full `narrative`; by-function required behavior and known unknowns; applicability/requirements/exception evidence; supported parameter contract; owner/review decision and provenance. Hardware examples are non-normative unless part of explicitly verified functional requirements.

## Assignment record minimum

| Field | Type / meaning |
|---|---|
| `endpoint_zone_id` | Persistent leaf zone ID; stable across display name edits |
| `sequence_id` | Full `SEQ-###` or `PSEQ-###`; never attach to parent |
| `sequence_revision` | Exact verified/accepted revision |
| `assignment_status` | `proposed`, `verified`, or `accepted`, independent of sequence definition status |
| `decision_id` | Owner acceptance/override decision ID when accepted; nullable while proposed |
| `parameters` | Project-specific values validated against sequence envelope/code; no unreviewed behavioral change hidden as parameter |
| `origin_basis` | `matched_standard` or `owner_custom`; other provenance/override source captured in evidence |
| `source_intent_refs` | Relevant existing MEP control sources and comparison result |
| `requirement_refs` | Verified applicable criteria/assumptions/unknowns for that endpoint |
| `override_note` | Explicit scoped owner-authorized deviation/selection rationale where needed |

**Cardinality:** one current assignment per active leaf, zero assignments for every parent. Before M3 can lock, **every in-scope endpoint with lighting/control direction needs an accepted assignment** (or an explicitly documented blocked exception; blocked exceptions cannot masquerade as locked compliant scope). A leaf may exist provisionally without a sequence during M1/M2; M3 leaves it flagged if required direction is unknown. Additional overlay requirements (e.g. intersecting daylight area) are modeled as associations/constraints and do **not** imply a second active SEQ on the same endpoint by default. If an overlay materially changes the endpoint's required functional behavior, re-evaluate the selected sequence and zone split rather than attaching conflicting executable sequences.

## Applicability and review

Agent matching first separates source requirements from adopted code edition/path/jurisdiction and independently reviewed building/energy classifications. Match **approved standard revisions only**, then prove coverage of occupancy, manual switching, light reduction, scheduling, daylight, emergency and independent control requirements. Conflicts or missing criteria create findings rather than an automatically approved assignment. An owner's custom sequence can be proposed and explicitly adopted without promotion to the standard registry, but remains subject to requirements verification.

**Owner authority:** selection/adoption (assignment), custom authoring (definition) and departure from existing MEP intent are different decisions. An approved definition does not approve a project assignment. Changes preserve the prior revision and assignment record; accepted items do not silently change on library refresh.

## Parent/child coordination

A parent may define `occupancy_aggregation` and shared manual-control links, but is not an independently driven endpoint. Parent conditions consumed by a leaf sequence must be identified by referenced signal/relationship and implemented/verified downstream. Leaf zone sequence can depend on an aggregate condition; this does not create a parent's own SEQ. Daylight zone areas can cross parent/child geometry; preserve their distinct extent and luminaire/control associations.

## Project review output

One narrative per unique `sequence_id + sequence_revision`, followed by assignment rows (Room ID(s), endpoint ID, applied parameters, local devices/function observations, status, exceptions, decision and source references). Separate a **required function** from an actual documented/selected device quantity. Render Light Reduction explicitly. Provide an all-Space daylight determination, lit/unlit/served relationships, source-intent comparison and M4/M5 deferred-item ledger.

## Versioning and implementation boundary

The shared contract is v0.1; it does not alter LV schema versions v0.7–v0.9 or claim generated PDF support. An LV companion register may implement this contract with explicit references to existing stable zone IDs and versioned project schema. Validation should reject missing/wrong/duplicate/parent assignments, unknown or unapproved standard revisions, and accepted assignments without owner evidence.

Owner: KIS Solutions; 2026-10-17.
