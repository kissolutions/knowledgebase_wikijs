---
title: ASCO ATS controller auxiliary status interfaces
page_type: hardware
page_status: draft
published: true
tags: hardware, ats, generator, monitoring
---

# ASCO automatic transfer switch — auxiliary contact evidence

## 0. Scope

Manufacturer-interface stub; not a declaration that any particular ATS has source-position contacts accessible to BAS.

## 1–3. Verification requirements

Before allocating digital inputs, identify exact ASCO switch series, controller family/catalog, option codes, approved as-built terminal diagram and contact ratings. Verify whether **Normal/Utility position**, **Emergency/Generator position**, **transfer in progress**, **source available** and **alarm** are exposed as distinct outputs (and if dry contacts are isolated). Controller screens and front-panel LEDs do not establish available output terminals.

Record contact form, normal energized state, voltage class and failure state. If no accessory contact is installed, treat availability as **unresolved**, not as an inferred design feature. Keep owner-approval for new accessory installation distinct from monitor-only scope.

## 16–17. Related and status

- [Generator/ATS status monitoring playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/ats-generator-status-monitoring.md)
- **Draft stub:** specific models and manufacturer terminal/rating documents are not yet supplied.
