---
title:  DCV Constraint and Assumption Synthesis Page
description: Constraints Synthesis page for building reasoning models
published: true
date: 2026-03-02T07:10:18.477Z
tags: 
editor: markdown
dateCreated: 2026-01-18T15:00:01.061Z
---

---
page_type: constraint-synthesis
page_status: draft
confidence_level: climate-and-occupancy-dependent

domain_primary: ventilation
domain_secondary:
  - demand_controlled_ventilation
  - retail_warehouse
  - oa_heavy_systems

discipline_scope:
  - mechanical
  - controls
  - architectural
  - operations
  - energy_modeling

applicability_scope:
  building_types:
    - retail_warehouse
    - big_box
    - supermarket
    - hybrid_mercantile
  climates:
    - humid
    - mixed_humid
  project_phases:
    - schematic
    - design_development
    - construction_documents

ai_role: reasoning_scaffold
ai_priority: high

invocation_triggers:
  ventilation_metrics:
    - condition: oa_fraction >= 0.30
    - condition: oa_load_fraction >= 0.35
    - condition: oa_latent_fraction >= 0.50
  load_characteristics:
    - condition: shr <= 0.70
  system_type:
    - packaged_rtu
    - constant_volume_or_vav

decision_axes:
  - dcv_eligibility
  - ventilation_dominance
  - latent_control_feasibility
  - rtu_selectability
  - coil_selection_constraints

related_pages:
  upstream:
    - Ventilation Fundamentals
    - Psychrometrics Fundamentals
    - Load Calculation Fundamentals
  downstream:
    - Warehouse Ventilation Playbook
    - RTU Selection Guidelines
    - Controls Sequences for DCV
---

# Demand-Controlled Ventilation — Constraint Synthesis

## 1. Why This Page Exists (Context and Risk)

Demand-Controlled Ventilation (DCV) is often discussed as an **energy-saving feature**, but in many buildings it is actually a **core performance constraint** driven by physics, humidity control, and equipment limitations.

This page exists to:
- Distinguish **DCV as a control strategy** from DCV as a **system-level necessity**
- Prevent DCV decisions from being made solely on code minimums or rules of thumb
- Explicitly connect **load metrics, airflow realism, and equipment selectability**
- Capture when a building is fundamentally **ventilation-driven rather than envelope-driven**

---

## 2. Physical Reality vs Modeling Reality

### Key Principle
> Ventilation metrics reveal whether a system is governed by people, weather, or equipment — not by square footage alone.

DCV becomes a constraint when:
- Outdoor air dominates total load
- Latent performance is driven primarily by ventilation
- Equipment must operate far from catalog “nominal” conditions

---

## 3. Governing Metrics and Classification Thresholds

The following metrics collectively determine whether DCV is:
- Optional
- Beneficial
- Operationally critical

### 3.1 Sensible Heat Ratio (SHR)

**Observed:** SHR ≈ 0.65  
**Interpretation:**  
- Latent-heavy space
- Typical of humid climates, OA-heavy systems, retail occupancy, and frequent door operation

**Constraint Implication:**
- Coil latent capacity is a first-order constraint
- Equipment selection must be validated at **mixed-air conditions**
- Nominal tonnage alone is insufficient

---

### 3.2 Supply Airflow Realism

**Estimated Supply Airflow:** ~7,400 CFM  
(Assuming ~55°F supply air, ΔT ≈ 20°F)

**Interpretation:**
- Airflow is consistent with typical packaged RTU ranges (350–425 CFM per ton)
- Does not rely on extreme ΔT assumptions

**Constraint Implication:**
- System is physically buildable with real fans, ducts, and diffusers
- DCV modulation will occur within realistic airflow bounds

---

### 3.3 Outdoor Air Fraction (OA / SA)

**Observed:** ~35%

**Interpretation:**
- Extremely high for packaged RTUs
- Mixed-air conditions dominate coil entering air state

**Constraint Implication:**
- Coil performance must be checked at mixed air
- Economizer and relief sizing become non-trivial
- DCV is no longer an “efficiency add-on” — it becomes a **load-shaping mechanism**

---

### 3.4 Total Btuh per CFM

**Observed:** ~33 Btuh/CFM

**Interpretation:**
- Typical for OA-heavy retail and warehouse spaces
- Indicates balanced airflow and load

**Constraint Implication:**
- Fan energy is reasonable
- Coil performance is achievable without extreme measures
- System is not over-airing or under-airing the space

---

### 3.5 Outdoor Air Load as Percentage of Total Load

**Observed:** ~41%

**Interpretation:**
- Ventilation dominates cooling load
- Envelope improvements have diminishing returns

**Constraint Implication:**
- This is a **ventilation-driven building**
- DCV meaningfully impacts both energy and equipment performance
- Equipment selection and control strategy outweigh envelope tuning

---

### 3.6 Outdoor Air Latent as Percentage of Total Latent Load

**Observed:** ~63%

**Interpretation:**
- Majority of humidity load is driven by ventilation
- Not by people or internal processes

**Constraint Implication:**
- Humidity control lives or dies with OA control
- DCV directly improves latent performance
- This metric alone justifies DCV as a governing strategy

---

## 4. System-Level Design Implications

Taken together, these metrics impose the following constraints:

| Observation | Governing Constraint |
|------------|----------------------|
| OA fraction > 30% | Mixed-air coil validation required |
| OA latent > 60% | DCV critical for humidity control |
| SHR ~0.65 | Latent capacity dominates selection |
| OA load ~40% | Building is ventilation-driven |
| Btuh/CFM ~33 | Airflow assumptions are realistic |

---

## 5. DCV Eligibility and Role

DCV is appropriate and defensible when:
- IAQ demand is people-driven
- Outdoor air dominates latent load
- Equipment is packaged or semi-packaged
- Occupancy varies significantly over time

In this context, DCV is:
- A **load-shaping control**
- A **latent management tool**
- A **risk-reduction strategy** for equipment selection

DCV is **not**:
- A substitute for minimum ventilation
- An aggressive reduction mechanism below code-required OA floors

---

## 6. Failure Modes and Late-Phase Risks

If DCV is omitted or misapplied:
- Coil latent capacity may be insufficient
- Packaged RTUs may fail to control humidity
- Equipment selections may rely on unrealistic catalog assumptions
- Energy modeling and real operation will diverge

If DCV assumptions change:
- Occupancy profiles must be revalidated
- OA fractions must be rechecked
- Coil and RTU selections may become invalid

---

## 7. Where This Fits in the Design Process

These constraints sit between:
- Load calculation (Btuh)
- Equipment selection (RTUs, coils, fans)
- Controls strategy definition

They represent the **final reality check** before:
- Selecting actual catalog equipment
- Locking control sequences
- Freezing ventilation strategy

---

## 8. Explicit Assumptions (Basis of Design Ready)

- Outdoor air fraction is significant and variable
- IAQ demand is primarily occupancy-driven
- Humid climate conditions govern latent performance
- DCV modulates outdoor air above a fixed minimum
- Equipment selection is validated at mixed-air conditions

---

## 9. AI-Agent Triggers and Inputs

### Trigger Conditions
- OA fraction ≥ 30%
- OA latent fraction ≥ 50%
- SHR ≤ 0.70
- Packaged RTU system detected

### Reasoning Actions
- Elevate DCV from optional to critical
- Flag mixed-air coil validation requirement
- Deprioritize envelope optimization
- Emphasize control strategy robustness

---

## 10. Summary

This is not a fragile or marginal DCV case.

The metrics demonstrate a system that is:
- Physically realistic
- Ventilation-dominated
- Latent-sensitive
- Compatible with packaged equipment
- Strongly aligned with DCV as a governing constraint

DCV here is not an efficiency feature — it is an enabling strategy.
