---
title: "Class 2 Circuit Cabling — Regulatory Basis"
description: "Edition-aware cable classification, permitted-use and installation review for general Class 2 systems."
published: true
page_type: ontology
page_status: draft
confidence_level: medium
domain_primary: electrical
ai_role: regulatory_reference
invocation_triggers:
  systems_present: [class_2_power, low_voltage_lighting, building_automation, power_limited_controls]
decision_axes: [circuit_classification, cable_listing, environmental_air, installation_method]
related_pages:
  - "../../design-playbooks/class-2-cable-selection.md"
  - "../../hardware/cabling/class-2-cable-catalog.md"
tags: electrical, class-2, cabling, regulatory
editor: markdown
---

# Class 2 Circuit Cabling

## 0. Purpose and Scope

Shared regulatory review for indoor commercial Class 2 power/control circuits,
including lighting and BAS. Product facts belong in the linked catalog; project
allocations and route geometry remain in their domain extensions.

**Evidence status:** this is a draft code-review map, not a complete adopted-code
specification. The supplied October 15, 2026 cable guide is intake evidence.
Manufacturer data was checked separately. Exact enforceable language, exceptions
and local amendments must be recorded from the project's adopted NEC before a
project compliance determination. Development reports are not adopted code.

## 1. Regulatory Definition

Establish Class 2 from the permitted power source/output and its applicable
listing and circuit limitations. Do not establish it merely from nominal voltage,
a load below 100 W, a cable marked CL2, or a software output limit. Keep circuit
classification, cable listing, insulation voltage and equipment rating separate.

The supplied shorthand of 60 VDC / 30 VAC / 100 VA is **not adopted as a universal
classification test**. Review the applicable source category, AC/DC limits,
current/power limits and conditions in the selected edition and source listing.
The LV lighting equipment's nominal operating range and 95 W grouping preference
are application constraints, not a general definition of Class 2.

## 2. Governing Codes and Standards

| Subject | Review locator / edition boundary |
|---|---|
| Source and circuit requirements | NEC Article 725; source review locator 725.121 and applicable Chapter 9 source-limit tables; verify adopted edition |
| Cable installation/listing | 2020-era locators: 725.135, 725.154 and 725.179. The 2023 reorganization introduces Article 722; use its installation/listing provisions rather than blindly carrying old section numbers forward |
| Communications cable markings | CMP/CMR/CM identify communications cable types; review applicable Articles 800/805 and permitted substitution provisions in the adopted edition |
| Environmental air | NEC 300.22 and applicable power-limited cable provisions; distinguish fabricated ducts from other environmental-air spaces |
| Separation | NEC 725.136, selected subsection and exception, adopted edition |
| Cable tray/raceways | Applicable Article 392 and raceway/Chapter 9 requirements, together with circuit-specific rules |
| Source/product certification | Applicable listed source/end-product standard and instructions; UL 1310 is a relevant source standard, not a substitute for identifying the actual equipment listing |
| Cable certification | Applicable cable listing standard, such as UL 13 or UL 444; certification and manufacturer evidence for the exact product |

Leviton's publisher-authored 2023 change guide identifies 722.135 for cable
installation and 722.179 for listing/marking. This confirms the relocation map,
not every installation permission or exception. An edition change requires a
new review of the affected requirements.

## 3. Requirements

### 3.1 Classification and application review

Record the route's actual conditions before selecting cable:

| Route condition | Cable classification to evaluate | Limit of this classification |
|---|---|---|
| Other space used for environmental air | CL2P or a permitted substitute, including CMP where allowed | Not blanket permission to route through fabricated supply/return ducts |
| Riser/floor penetration | CL2R or permitted higher/substitute classification | A vertical route can also be an environmental-air space; evaluate both |
| General indoor, non-plenum/non-riser route | CL2 or permitted substitute | A wall cavity, raceway or suspended ceiling does not automatically establish this condition |
| Wet/outdoor/UV, burial, industrial or hazardous location | Separate applicable product ratings and wiring method | Plenum marking alone does not establish any of these capabilities |

A code-permitted substitute and a dual-listed cable are different facts. If the
product sheet establishes only CMP, record CMP; do not relabel it CL2P/CMP.
Evaluate substitution using the adopted edition's actual table and conditions.
The source guide's CMP→CL2P, CMR→CL2R and CM→CL2 pairings are review candidates;
do not treat the abbreviated hierarchy as the complete substitution table.

### 3.2 Installation checks and exceptions

Select the applicable separation rule for the installation: open routing,
shared raceway/cable/tray, enclosure and associated equipment are not identical
cases. The supplied two-inch rule is not a universal permission to mix systems.
Record the applicable subsection, barrier/raceway construction and exception
before accepting an arrangement.

Similarly, do not carry forward the supplied blanket 40% tray fill, 4–5 ft
support spacing, 12 in sag or 8×OD bend-radius values as NEC mandates. Determine
support, fill, mechanical protection, bends and pulling limits from the actual
wiring method, cable/support manufacturer instructions and adopted provisions.
Calculate raceway fill using cable dimensions and the applicable rule, not an
unqualified conductor-count shortcut. Protect cables at penetrations and retain
required firestopping and support details.

Tray eligibility, environmental rating and mechanical suitability are separate
checks. CMP alone does not settle every tray application. Conversely, do not
require a TC marking for every power-limited cable installation without checking
the circuit-specific permissions. Industrial PLTC, ITC, TC and TC-ER products
must retain their own listing and permitted-use review; they are not generic
plenum alternatives.

### 3.3 Fire/smoke claims

NFPA 262 addresses flame travel and smoke in air-handling-space cable testing.
Do not translate a plenum rating into “non-toxic,” halogen-free, zero smoke,
wet-location suitability or circuit integrity. General-purpose cable compliance
also cannot be reduced to a standalone VW-1 claim.

## 4. Interactions with Other Codes

Check applicable building/mechanical environmental-air conditions and penetrations,
firestopping, emergency/life-safety system rules and the end-product instructions.
A power-limited lighting source does not, by itself, resolve the full lighting
system's applicable NEC article or listing. Fire alarm, emergency, hazardous
locations and power/data combinations require their specific review.

## 5. Common Interpretation Issues

- Nominal low voltage is not proof of Class 2 source classification.
- A 300 V cable insulation rating does not authorize a 300 V Class 2 circuit.
- A communication-type listing is not a statement that a cable can carry only data.
- Cable substitution does not establish a second marking on the product.
- Spare conductors and common jackets do not authorize tying independent outputs together.
- A low-smoke test is not a toxicity certification.

## 6. Related Concepts and Sources

- [Class 2 cable selection](../../design-playbooks/class-2-cable-selection.md).
- [Multi-vendor cable catalog](../../hardware/cabling/class-2-cable-catalog.md).
- [NFPA publication access](https://link.nfpa.org/) — obtain the adopted edition and amendments for project decisions.
- [Leviton 2023 Article 722/724/726 change guide](https://captaincode2023.leviton.com/node/369) — edition-navigation evidence, not a complete code extract.
- [UL Wire and Cable Marking and Application Guide, 2019](https://code-authorities.ul.com/wp-content/uploads/sites/46/2019/10/Wire-and-Cable10-3-2019-final.pdf) — certification/marking evidence; verify the applicable current category record.
- [NFPA codes and standards index](https://www.nfpa.org/for-professionals/codes-and-standards/list-of-codes-and-standards) — NFPA 262 scope.
- Owner-supplied *Low-Voltage Class 2 Commercial Lighting Cable Specification & Selection Guide*, received 2026-10-15. Its unsupported universal claims are reconciled above rather than promoted to code requirements.

## 7. Status and Stewardship

Draft; reviewed 2026-10-15. Steward: KIS Solutions, electrical engineering.
Open: adopted-edition clause/exception verification, installation-specific support
and tray criteria, and project approval. This page is reusable across vendors
and Class 2 applications; it is not confined to LV lighting.
