---
title:  Constraint and Assumption Synthesis Page TEMPLATE
description: Constraints Synthesis page for building reasoning models
published: true
date: 2026-03-02T00:02:19.661Z
tags: 
editor: markdown
dateCreated: 2026-01-17T23:14:21.788Z
---

---
# ==============================
# KIS KNOWLEDGE MODEL METADATA
# ==============================

page_type: constraint-synthesis
page_status: draft | validated | deprecated
confidence_level: low | medium | high | operationally-dependent

domain_primary: <building_type_or_system>
domain_secondary:
  - <optional>
  - <optional>

discipline_scope:
  - mechanical
  - electrical
  - lighting
  - fire_protection
  - architectural
  - structural
  - controls
  - operations

applicability_scope:
  building_types:
    - <warehouse>
    - <retail>
    - <office>
  project_phases:
    - concept
    - schematic
    - design_development
    - construction_documents

# ------------------------------
# AI INVOCATION & REASONING
# ------------------------------

ai_role: reasoning_scaffold
ai_priority: high | medium | low

invocation_triggers:
  geometry:
    - condition: <example: rack_height_ft >= 10>
    - condition: <example: ceiling_height_ft >= 14>
  systems:
    - condition: <example: lighting_plane_below_rack_top>
    - condition: <example: combustion_equipment_present>
  programmatic_signals:
    - <warehouse>
    - <big_box>
    - <industrial>
  uncertainty_flags:
    - <missing_operational_data>
    - <conflicting_model_signals>

decision_axes:
  - <classification_decision>
  - <equipment_selection>
  - <ventilation_basis>
  - <controls_strategy>
  - <code_trigger>

# ------------------------------
# ASSUMPTION MANAGEMENT
# ------------------------------

assumption_objects_enabled: true
rfi_generation_enabled: true
model_validation_enabled: true

related_pages:
  upstream:
    - <fundamentals_page>
  lateral:
    - <peer_constraint_page>
  downstream:
    - <playbook_page>

---

# <*<PAGE TITLE*>

## 1. Why This Page Exists (Context + Risk)
Describe **why this scenario is commonly misunderstood** and what risks occur if assumptions are made implicitly.

- Typical misclassifications
- Systems affected downstream
- Why generic code references are insufficient

> **Design Intent:** This page exists to force conscious decisions.

---

## 2. Physical Geometry vs Operational Reality

Document the distinction between *what the building looks like* and *how it actually operates*.

### Physical Characteristics
- Ceiling height:
- Structural elements:
- Fixture planes (lighting, sprinklers):
- Aisle or circulation geometry:

### Operational Reality
- How spaces are actually used
- Physical constraints that limit operations

> **Key Principle:** Geometry does not equal operation.

---

## 3. Classification Thresholds & Definitions

Identify thresholds that trigger major design changes.

- Code definitions
- Industry norms
- Practical vs conservative interpretation

### Governing Interpretation
State explicitly which interpretation governs this design and why.

---

## 4. Equipment, Process, or Occupancy Assumptions

### Included
- Equipment types:
- Power sources:
- Occupancy patterns:

### Explicitly Excluded
- Equipment or processes assumed **not** present

---

## 5. System-Level Design Implications

Map assumptions directly to consequences.

| Assumption | System Impact | Affected Disciplines |
|----------|---------------|---------------------|
|          |               |                     |

This section must support traceability.

---

## 6. Controls & Automation Considerations

Describe how assumptions affect:

- Control strategies
- Sensor requirements
- Zoning logic
- Monitoring exclusions

---

## 7. Cross-Discipline Coordination Notes

Document dependencies that require alignment.

- Architectural:
- Lighting:
- Fire Protection:
- Structural:
- Operations:

No discipline may change assumptions independently.

---

## 8. Explicit Assumptions (Basis of Design Ready)

Write assumptions exactly as they should appear in a Basis of Design.

- Declarative
- Testable
- Defensible

---

## 9. Critical RFIs

Questions that **must** be answered or confirmed.

- Owner RFIs
- Architect RFIs
- Operations RFIs
- Authority Having Jurisdiction RFIs

---

## 10. Failure Modes & Late-Phase Risks

Describe how this design can fail.

- Scope creep triggers
- Operational changes
- Reclassification risks
- Permit-stage surprises

---

## 11. AI-Agent Triggers & Inputs

Describe what an AI agent should detect to use this page.

### Model Signals
- Geometry patterns
- Equipment families
- Missing data

### Conflict Detection
- Signals that contradict assumptions

---

## 12. Structured Assumptions (Machine-Readable)

> Optional but recommended

```yaml
assumptions:
  - id: <ID>
    statement: "<assumption>"
    derived_from:
      - <condition>
    invalidated_if:
      - <condition>
  
  
```yaml
assumptions:
  - id: WH-A-01
    statement: Commodities are not stacked above approximately 6 ft
    derived_from:
      - lighting_plane_ft: 12
    invalidated_if:
      - lighting_height_changed: true
      - storage_policy_changed: true
      

Consequence Logic structure:
  consequences:
  - if:
      - no_combustion_equipment: true
    then:
      - co_sensors_required: false
      - exhaust_for_forklifts: false
      
RFI Automation Logic structure:
  rfi_triggers:
  - missing:
      - operational_storage_height
    generate_rfi: Confirm maximum operational storage height

