---
title: KIS Systems Engineering Framework v1.0 - Architecture Contract
description: Shared lifecycle, process, registry, configuration and presentation conventions for engineering domain extensions
published: true
tags: governance, systems-engineering, process, requirements, configuration
editor: markdown
---

# KIS Systems Engineering Framework v1.0 - Architecture Contract

**Status:** Architecture baseline v1.0 (2026-10-17). Establishes common vocabulary and behavior; **not** a claim that all domain schemas, processes or tools are production-ready.

**Reference basis:** Informed by the Systems Engineering Body of Knowledge (SEBoK) and its treatment of lifecycle processes, stakeholder needs, requirements, architecture, verification, validation, decision management and tailoring. These are KIS conventions, not an assertion that the five KIS phases are SEBoK's official stages.

**Authority:** This parent knowledgebase owns cross-domain conventions. Domain extensions define domain processes, schemas, acceptance criteria and generators. Project workspaces hold source evidence, authoritative working registers, review evidence and snapshots. Do not create independent sources of truth through derived reports, JSON or visualizations.

## 1. Lifecycle, process, milestone and work product

- **Engineering Lifecycle:** Organization of project work over time. KIS standard phase labels: **Phase 1 Intake** (source evidence and inventory); **Phase 2 Design Basis & Requirements** (applicability, stakeholder needs, requirements, constraints, approved functional direction); **Phase 3 Design Development** (selected solutions and physical/logical implementation); **Phase 4 Coordination & Delivery** (coordination, release and implementation documentation); **Phase 5 Verification & Closeout** (completed test evidence, installed configuration and closeout). Domain projects may omit or tailor phases based on contracted scope.
- **Phase:** High-level lifecycle grouping, not an exclusive owner of processes.
- **Process:** Named, reusable engineering operation that can be invoked in any appropriate phase or milestone. Process definitions are independent of any single workflow.
- **Milestone / Review Gate:** Domain-defined checkpoint with scope, required review evidence, responsible reviewers and completion criteria. Retain M1, M2, etc. designations. A passed software check does not itself establish milestone acceptance.
- **Work Product:** Named output or maintained engineering artifact (register, annotated drawing, narrative, calculation, schedule, report). Work product names and packages continue to follow their domain milestone conventions. One work product may be updated and reviewed at successive milestones.
- **Work Package:** Project-defined unit for organizing, assigning, progressing and closing out execution work. A Work Package is not inherently a System, Equipment item, contractual Scope of Work or single test; mappings among them may be one-to-many or many-to-many. A project may group or subdivide work packages to suit construction, commissioning and management needs.
- **Schedule of Values (SOV) / Commercial Valuation Reference (optional):** Contract-defined allocation of value for payment or commercial progress tracking, used only when the project requires it. Work Packages may optionally reference one or more SOV line items, without assuming a one-to-one mapping. No default SOV register, SOV ID, pricing columns or payment workflow is required in project trackers or domain lifecycles. Commercial valuation is not engineering acceptance or verification.
- **Process execution:** Particular invocation of a named process against identified input versions. May generate one or more work products and findings.

### Process contract (required for newly formalized shared processes)

Each reusable process defines: stable **Process ID**, **Version**, purpose, invocation conditions and suitable phases, required inputs, source/revision prerequisites, method, work products and their authoritative/derived roles, deterministic checks and human review, uncertainty/error handling, authority and scope of permitted change, treatment of accepted configurations, completion criteria and permissible tailoring. Execution evidence should retain the exact process version or immutable repository revision, inputs and outputs, run scope, findings and disposition; lightweight project logs are sufficient.

**Versioning and tests:** A changed process rule produces a new identifiable revision. Run the same reference input against old and new versions when evaluating changes; document differences and regressions. Do not mislabel an execution as using a version not actually followed.

**Tailoring:** Processes identify invariants that cannot be bypassed (e.g. source provenance, acceptance preservation, explicit unresolved status). A project may scale evidence depth, presentation, reviewer effort and optional steps to complexity and risk. Tailoring is recorded briefly when it changes a required default; do not require a separate approval form for routine small-project adaptation.

Initial reusable process candidates: Source Registration and Reconciliation; System Boundary and Scope Review; Requirements Derivation and Applicability Review; Requirements Traceability Review; Work Product Verification; Stakeholder Validation; Registry Query and Reporting; Configuration Snapshot/Comparison; Change Impact Review. Candidate names do not imply completed implementations.

## 2. System definition, context and scope

- **System of Interest (SoI):** System or defined portion being engineered/evaluated.
- **Context:** Relevant surrounding systems, environments, stakeholders and dependencies.
- **Boundary:** Explicit separation of the SoI from surrounding context.
- **Interface:** Defined interaction crossing a system or responsibility boundary.
- **Modeled relationship** and **scope of work responsibility** are separate dimensions. Recording an existing adjacent device does not make it part of the contractor's modification scope.
- Recommended scope dispositions: `in_scope`, `interface_only`, `adjacent_context`, `excluded`, `unresolved`. These are conceptual values, not a mandate to add columns to existing registers. Domain schemas may translate/display them.

A boundary review identifies exclusions, externally provided components, owner/contractor responsibilities, consequential interfaces and unresolved cases. Absence of a source fact does not establish exclusion.

## 3. Engineering Evidence and Requirements Registry

**Logical project-level registry,** implementable through one workbook or coordinated domain tables; no mandatory new global database or immediate domain schema migration. All domain registries follow the same logical record contract. Canonical editable project records remain authoritative; reports and views are derived.

### Record types

- **Need:** Stakeholder outcome or capability sought, prior to translation into engineering requirements.
- **Fact:** Supported observation or assertion about a source, asset, condition or product.
- **Requirement:** Applicable obligation the design must satisfy.
- **Constraint:** Restriction on feasible solutions from code, physical conditions, interfaces, product limits or binding directives.
- **Criterion:** Adopted design target/selection or evaluation rule; distinguish project standard from mandatory regulation.
- **Assumption:** Provisional input requiring confirmation, validity conditions or risk review.
- **Decision:** Selected interpretation or solution, with rationale and responsible authority.
- **Finding:** Verified inconsistency, deficiency, conflict or observation requiring disposition.

Keep **Source Evidence** as a separately addressable reference, not a synonym for Requirement. Facts, source quotations and unreviewed code text do not automatically establish applicability.

### Minimum logical fields

Stable `Record ID`; `Record Type`; atomic, unambiguous `Statement`; `Origin` and `Authority/Binding Basis`; `Source Locator + Revision`; `Applies To` (SoI, subsystem, scope, space, equipment, device or other stable IDs); `Applicability State`; `Evidence/Confidence`; `Review/Decision State`; `Derived From / Related IDs`; `Rationale or Notes`; and `Verification Method / Evidence` when relevant. Null/unresolved is not zero, absence, nonapplicability or accepted truth.

Keep statement validity, applicability, approval, and configuration acceptance logically distinct even if an initial project uses fewer visible columns. Retain superseded records or snapshots to explain provenance. Applicable codes, editions, amendments, occupancy/use conditions and specialty provisions are identified during Intake; binding applicability and derived requirements are evaluated in Design Basis. Evaluate interactions and conflicts explicitly; **'most stringent governs' is not a universal automatic precedence rule**.

A query/report process must support requests such as: all **currently applicable constraints** for a selected scope, all **current assumptions**, unresolved requirements by system, requirements from a code edition, or requirements changed since a baseline. Clearly separate current/applicable from observed-only, candidate, superseded and unresolved; use stable IDs and source locators.

### Traceability

Support lightweight links: evidence -> fact/need/requirement/constraint -> engineering decision -> work product -> verification/validation evidence. The links may be references in spreadsheets rather than a heavyweight model. Consequential decisions retain rationale and related applicable constraints; no formal trade study is mandated for ordinary choices.

## 4. Verification, validation and review

- **Verification:** Does the work product, system or process result meet specified requirements/criteria? Methods may include inspection, analysis, demonstration and test.
- **Validation:** Does the solution satisfy intended stakeholder needs in its intended context?
- Both are reusable processes invoked throughout the lifecycle; they are not postponed exclusively to Phase 5.
- **Milestone acceptance** indicates a defined review gate was met; it is not synonymous with engineering configuration acceptance or construction acceptance.
- Reports distinguish checks executed, checks unavailable/not reviewed, unresolved findings, responsible reviewer, evidence, and review scope.

## 5. Acceptance, snapshot, configuration baseline and change control

These are deliberately lightweight, distinct operations:

- **Engineering Acceptance:** Human directive to preserve a selected **derived configuration or engineering decision** against future automatic, optimized or subjective reconfiguration. May target one attribute, geometry segment, whole object, named collection or work product. It is forward-looking protection, *not* a certification of code compliance. Source facts instead require provenance and verification; routine non-reconfigurable facts need not be accepted.
- **Snapshot:** Immutable captured state of the selected project registries and listed associated work products, with scope, timestamp, responsible human/request, source revisions and hashes/revision IDs as available. No approval implied.
- **Configuration Baseline:** A snapshot explicitly designated as a future comparison/recovery reference. A single human directive such as `Make this the M4 baseline` captures the complete currently authoritative state in the stated milestone scope, including provisional records and open issues, without marking all records Accepted.
- **Design Baseline:** Preferred/default design pattern in a playbook, distinct from Configuration Baseline.
- **Change control:** Current working records may evolve after a baseline; preserve previous baseline immutably. A subsequent process may revise provisional data but must not silently alter accepted decisions. Propose alternatives, identify impacted records/work products and ask for reopening authority when needed. Baseline diff reports should identify added/removed/modified records; restoration requires explicit reconciliation and must not silently discard newer work.

**Minimum viable operation set:** Snapshot; Establish Baseline; Compare Baseline; Restore/Reconcile. Snapshot literal canonical registry copies first, with a small manifest; semantic diff and restoration automation can mature later. Baseline creation must not require per-record approvals. Where acceptance covers just location or segment geometry, other aspects of the object remain editable.

**Future implementation candidate (not mandatory): Markup/CAD-based acceptance.** Investigate direct acceptance via editable drawing markups or CAD object metadata. LV Lighting cable-route segment/named-route acceptance is the reference case; Bluebeam-specific conventions, annotation IDs and optimizer enforcement belong to the LV routing process until generalized.

## 6. Data contracts and presentation contracts

- **Data Contract:** Meaning, type, valid values, null/unknown behavior, identity, reference constraints, validation and downstream use for a canonical field.
- **Canonical Register:** Authoritative project engineering record. Project-specific authoritative files and revision rules must be stated explicitly; derived JSON is not a parallel source of truth.
- **Derived View:** Rebuildable representation of canonical information. It may summarize, filter or reorganize, but must preserve provenance, uncertainties and protected decisions.
- **Presentation Contract:** Minimum content, version/source labelling, review state, scope and fidelity required of a work product's rendered view.
- **Controls Scope Navigator:** Interactive engineering exploration across equipment, devices, I/O and locations.
- **Controls Scope Infographic:** Bird's-eye, summarized presentation showing scope, systems/locations and key boundaries.
- **Schedule Views:** Domain-specific alternate presentations of a canonical schedule; no competing independent registers.

## 7. Deferrals and implementation boundary

Not universal v1.0 requirements: formal trade studies, quantitative risk management metrics, measures of effectiveness/performance, full requirements-allocation hierarchy, formal interface-control documents, SysML or full MBSE. Apply such methods only when a domain/project warrants them.

v1.0 freezes **common terminology and behavioral contracts**. It does not certify or automatically migrate LV Lighting/BAS schemas, create a functioning shared registry query engine, implement PDF round trips, or establish a universal optimization algorithm. Domain extension milestones and process definitions remain independently versioned and tested.

## 8. Initial domain mapping: LV Lighting

- **Phase 1 Intake:** M1 Room Inventory and M2 Source Lighting & Controls Extraction.
- **Phase 2 Design Basis & Requirements:** M3 Controls Narrative & Compliance Review.
- **Phase 3 Design Development:** M4 LV Implementation & Review Markups.
- **Phase 4 Coordination & Delivery:** M5 Coordinated Issue.
- **Phase 5 Verification & Closeout:** M6 Commissioning & Closeout.

Domain M1/M2/M3/M4/M5/M6 nomenclature and printable milestone packages do not change. Domain playbooks reference shared process definitions rather than cloning common standards. Process execution, human review, and project-specific approval remain necessary even when checkers pass.

## 9. Stewardship

Shared vocabulary and process contracts belong here; domain engineering details belong in domain extensions and device/application facts in their established knowledgebase sections. New generic concepts are proposed upstream, tested with real work and versioned. The architecture is an intentionally minimal starting point subject to evidence-driven refinement.


## Informative illustrations and training aids

Explanatory diagrams and worked examples are **informative, non-normative** aids, analogous to NEC Handbook explanatory illustrations. The normative process, schema, governing code and owner-approved engineering record control in case of inconsistency. Keep figures linked to their governing definitions and review figures when those definitions change.

The shared [Engineering Illustrations index](../assets/illustrations/README.md) currently includes [Space Boundary Markup](../assets/illustrations/space-boundary-markup-example.svg) and [Clockwise Light Identification](../assets/illustrations/light-ids-clockwise-room-example.svg). These may illustrate domain examples without transferring ownership of shared concepts into any one domain.
