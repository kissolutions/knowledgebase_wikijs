---
title: KMC Controllers Overview
description: Index and orientation for KMC BAS controller hardware pages
published: true
date: 2026-09-27T00:00:00.000Z
tags: hardware, controller, kmc, overview
editor: markdown
dateCreated: 2026-09-27T00:00:00.000Z
---

# KMC Controllers — Overview

This section documents **KMC controller hardware as physical devices**: what I/O capacity each model has, how it expands, and what constraints it imposes. It does not cover how KIS selects or configures controllers for a project — that is a bas-logic-gen concern (see below).

## How These Pages Are Used

The bas-logic-gen Controls Engineering Playbook assigns points to controller/panel hardware at Stage 8. That stage, and the spare-capacity policy it applies, both depend on the real I/O capacity and module chunk sizes recorded here. Right now those numbers are marked PENDING on each page — filling them in from the actual KMC datasheets is the next step before Stage 8 can be run with confidence on a real project.

## Controllers

| Model | Page | Status |
|---|---|---|
| BAC-5901 | [BAC-5901](BAC-5901.md) | Draft — specs pending |
| BAC-5902 | [BAC-5902](BAC-5902.md) | Draft — specs pending |
| BAC-9300 | [BAC-9300](BAC-9300.md) | Draft — specs pending |

## Related (bas-logic-gen)

- Controller/Panel I/O Assignment: `design-playbooks/controls-engineering-playbook.md`, Stage 8
- KIS usage conventions per model: `platforms/kmc/controller-mappings/`
- Spare capacity policy and module chunk sizes: `platforms/kmc/architecture-constraints.md`

## Scaling Beyond KMC

This folder currently holds only the KMC family. A project on a different controller platform (a PLC-based system, or another BAS controller line) would get its own sibling folder here, following the same hardware-template structure — not built yet, since no such project has required it.
