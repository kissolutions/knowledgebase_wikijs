---
title: Product Type / Class Page TEMPLATE
description: Template for pages describing what a product family or platform implies and constrains
published: true
date: 2026-09-26T00:00:00.000Z
tags: template, product-class
editor: markdown
dateCreated: 2026-09-26T00:00:00.000Z
---

---
# ==============================
# KIS KNOWLEDGE MODEL METADATA
# ==============================

page_type: product-class
page_status: draft | validated | deprecated
confidence_level: low | medium | high

domain_primary: <lighting_controls | bas_controllers | vfds | ...>
manufacturer: <optional — omit for vendor-neutral classes>
product_family: <family or platform name>

discipline_scope:
  - <controls | electrical | mechanical | ...>

# ------------------------------
# AI INVOCATION & REASONING
# ------------------------------

ai_role: constraint_source
ai_priority: high | medium | low

invocation_triggers:
  systems:
    - condition: <example: product_family_specified == true>
  programmatic_signals:
    - <example: owner_standard_names_this_platform>

decision_axes:
  - <ecosystem_selection>
  - <capability_fit>
  - <implementation_limits>

related_pages:
  upstream:
    - <physical_entity_pages for member devices>
  lateral:
    - <competing product_class pages>
  downstream:
    - <playbooks that assume this platform>

---

# <Product Type / Class Name>

<!--
PRODUCT TYPE / CLASS TEMPLATE
Purpose: Describe what choosing this product family or platform IMPLIES and CONSTRAINS.
This sits between Physical Entity pages (one device) and Playbooks (what we do).
Do NOT include:
- Individual device datasheet detail (→ Physical Entity page; link it)
- Firm standards for using the product (→ Playbook)
-->

## 0. Purpose and Scope

**What this class is:**  
**Member products / devices:** (link each Physical Entity page)  
**What this page does NOT do:** recommend the product or define our standards for it.

---

## 1. Ecosystem Overview

<!-- ANCHOR: ECOSYSTEM — how the family fits together; required companion products; tools. -->

---

## 2. Capabilities

### 2.1 What the class can do
### 2.2 Capability differences between members

| Member | Distinguishing capability | Limit |
|---|---|---|
| {{Product}} | {{Capability}} | {{Limit}} |

---

## 3. Imposed Constraints

<!--
ANCHOR: CONSTRAINTS
Hard limits the class imposes on anything built with it.
Classify as the framework does: hard / soft / hidden.
-->

### 3.1 Hard constraints
### 3.2 Soft constraints
### 3.3 Hidden constraints

---

## 4. Configuration and Programming Model

<!-- ANCHOR: CONFIGURATION — how the class is set up or programmed, at the level needed to reason about it. -->

---

## 5. Integration and Interoperability

### 5.1 Supported protocols and interfaces
### 5.2 Known integration friction

---

## 6. Lock-in, Procurement and Lifecycle

### 6.1 Procurement paths and substitution risk
### 6.2 Tooling and licensing dependencies
### 6.3 Product lifecycle / obsolescence

---

## 7. Pitfalls, Assumptions and Failure Modes

---

## 8. Cross-links and Navigation

- Member devices: {{Physical Entity pages}}
- Playbooks that assume this class: {{page}}
- Competing classes: {{page}}

---

## 9. Status and Stewardship

- **Status:** Draft / Validated / Deprecated  
- **Last Review:** YYYY-MM  
- **Owner:** {{Role or Name}}
