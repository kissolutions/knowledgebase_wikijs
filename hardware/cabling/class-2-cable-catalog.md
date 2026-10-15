---
title: "Class 2 Cable Product Catalog — Multiple Manufacturers"
description: "Expandable source-backed cable candidates for indoor commercial Class 2 power/control applications."
published: true
page_type: reference
page_status: draft
confidence_level: medium
domain_primary: electrical
reference_kind: edge-case-catalog
ai_role: supporting_detail
ai_priority: medium
invocation_triggers:
  systems_present: [class_2_power, low_voltage_lighting, building_automation, power_limited_controls]
  uncertainty_flags: [cable_selection, product_substitution]
parent_pages:
  - "../../design-playbooks/class-2-cable-selection.md"
related_pages:
  - "../../ontology/reg-and-class/class-2-circuit-cabling.md"
tags: electrical, cable, catalog, class-2, multi-vendor
editor: markdown
---

# Class 2 Cable Product Catalog

## 0. Parent Page and Purpose

Supports [Class 2 cable selection](../../design-playbooks/class-2-cable-selection.md).
This is the shared, **vendor-neutral** catalog for candidate cables. Belden is the
first manufacturer; add others to this same catalog using the same evidence and
selection fields. No exclusive vendor standard or automatic cross-brand equivalence
is established. Product knowledge belongs here; project route assignments remain
in the relevant design extension.

## 1. Summary

The initial intake contains 20 Belden base part numbers. Eleven have manufacturer
construction data checked below; nine are retained separately pending confirmation.
An unavailable page does not prove a product does not exist. A base number is not
a complete purchase SKU: retain color, packaging, length and other ordering suffixes
when selected.

Evidence status is separate from application acceptance:

- **Manufacturer data checked:** the cited source supports the displayed fields.
- **Candidate — confirmation pending:** supplied part/configuration retained, but not confirmed for selection.
- **Project accepted:** an external project review record identifies the exact product, application and conditions. This catalog does not grant that approval.

## 2. Detail

### Manufacturer: Belden — checked construction data

Reviewed 2026-10-15. Each part link is its manufacturer evidence. Checked products
below are described by Belden as CMP with bare-copper conductors and PVC/Flamarrest
construction. Do **not** infer CL2P dual marking. Their use in Class 2 circuits
requires the [permitted-use/substitution review](../../ontology/reg-and-class/class-2-circuit-cabling.md).
A conductor count is not a claim of twisted-pair construction.

DCR values below are manufacturer **nominal conductor** resistance in ohms/1,000 ft,
not loop resistance or maximum design values. Retain temperature/basis before use
in calculations. OD is nominal inches. Product-specific values supersede the
supplied guide's generalized family values.

| Manufacturer | Base part / source | Construction | AWG / stranding | Shield | OD, in | Nominal conductor DCR, Ω/1,000 ft | Evidence status |
|---|---|---|---|---|---:|---:|---|
| Belden | [6300UE](https://catalog.belden.com/techdata/EN/6300UE_techdata.pdf) | 2 conductors | 18 / 7×26 | None | 0.154 | 6.5 | Manufacturer data checked |
| Belden | [6300FE](https://catalog.belden.com/techdata/EN/6300FE_techdata.pdf) | 2 conductors | 18 / 7×26 | Overall foil | 0.162 | 6.4 | Manufacturer data checked |
| Belden | [6301UE](https://catalog.belden.com/techdata/EN/6301UE_techdata.pdf) | 3 conductors | 18 / 7×26 | None | 0.163 | 6.5 | Manufacturer data checked |
| Belden | [6301FE](https://catalog.belden.com/techdata/EN/6301FE_techdata.pdf) | 3 conductors | 18 / 7×26 | Overall foil | 0.172 | 6.4 | Manufacturer data checked |
| Belden | [6302UE](https://catalog.belden.com/techdata/EN/6302UE_techdata.pdf) | 4 conductors | 18 / 7×26 | None | 0.180 | 6.79 | Manufacturer data checked |
| Belden | [6200UE](https://catalog.belden.com/techdata/EN/6200UE_techdata.pdf) | 2 conductors | 16 / 19×29 | None | 0.176 | 3.8 | Manufacturer data checked |
| Belden | [6200FE](https://catalog.belden.com/techdata/EN/6200FE_techdata.pdf) | 2 conductors | 16 / 19×29 | Overall foil | 0.184 | 4.0 | Manufacturer data checked |
| Belden | [6202UE](https://catalog.belden.com/techdata/EN/6202UE_techdata.pdf) | 4 conductors | 16 / 19×29 | None | 0.206 | 3.8 | Manufacturer data checked |
| Belden | [6202FE](https://catalog.belden.com/techdata/EN/6202FE_techdata.pdf) | 4 conductors | 16 / 19×29 | Overall foil | 0.215 | 4.0 | Manufacturer data checked |
| Belden | [6345FE](https://www.belden.com/products/specials/6345fe) | 6 pairs / 12 conductors | 18 / 7×26 | Overall foil | 0.357 | 6.93 | Manufacturer data checked |
| Belden | [6347FE](https://catalog.belden.com/techdata/EN/6347FE_techdata.pdf) | 9 pairs / 18 conductors | 18 / 7×26 | Overall foil | 0.423 | 6.94 | Manufacturer data checked |

### Selected mechanical and temperature evidence

These values are per product, **not family defaults**. Use the linked source sheet
for the other entries and populate their installation values before selection.
UL temperature and allowed installation/operating temperature are distinct fields.

| Base part | Source revision as printed | UL voltage / temperature | Operating range, °C | Minimum bend radius: stationary / installation | Maximum pull | Drain |
|---|---|---|---|---|---|---|
| 6300UE | 0.512; 09-07-2025 | 300 V / 75°C | 0 to +75 | 1.5 / 1.5 in | 45 lb | None |
| 6200UE | 0.501; 09-07-2025 | 300 V / 75°C | 0 to +75 | 1.8 / 1.8 in | 80 lb | None |
| 6345FE | 0.318; 09-07-2025 | 300 V / 75°C | 0 to +75 | 3.57 / 3.57 in | 274.3 lb | 24 AWG, 7×32 tinned copper |
| 6347FE | 0.294; 09-07-2025 | 300 V / 75°C | −20 to +75 | 4.23 / 4.23 in | 415.8 lb | 20 AWG, 7×28 tinned copper |

The multipair sheets state 3.5 A/conductor at 25°C for 6345FE and 2.5 A/conductor
at 25°C for 6347FE. These are source-stated conditions, **not project allowable
ampacity**. Evaluate simultaneous loading, installation/bundle conditions and all
other governing limits. This catalog does not establish voltage-drop reach.

### Belden intake entries — manufacturer confirmation pending

These are **claims from the supplied guide**, not verified product specifications.
Do not infer availability, construction, OD, ratings or substitutions from similar
part numbers. Preserve them as research leads until exact manufacturer evidence
is obtained. Source-page retrieval failed or no matching manufacturer result was
established during this review; neither outcome establishes nonexistence.

| Manufacturer | Supplied base part | Supplied configuration to verify | Supplied OD claim, in — unverified | Status |
|---|---|---|---:|---|
| Belden | 6302FE | 18 AWG, 4 conductors, overall shield | 0.180 | Candidate — confirmation pending |
| Belden | 6201UE | 16 AWG, 3 conductors, unshielded | 0.189 | Candidate — confirmation pending |
| Belden | 6201FE | 16 AWG, 3 conductors, overall shield | 0.191 | Candidate — confirmation pending |
| Belden | 6345UE | 18 AWG, 6 pairs, unshielded | 0.330 | Candidate — confirmation pending |
| Belden | 6245UE | 16 AWG, 6 pairs, unshielded | 0.405 | Candidate — confirmation pending |
| Belden | 6245FE | 16 AWG, 6 pairs, overall shield | 0.435 | Candidate — confirmation pending |
| Belden | 6347UE | 18 AWG, 9 pairs, unshielded | 0.410 | Candidate — confirmation pending |
| Belden | 6247UE | 16 AWG, 9 pairs, unshielded | 0.510 | Candidate — confirmation pending |
| Belden | 6247FE | 16 AWG, 9 pairs, overall shield | 0.545 | Candidate — confirmation pending |

### Adding another manufacturer

Add a manufacturer subsection and rows with manufacturer plus exact base part as
the product key. Maintain the following record for each product, expanding tables
or adding a linked product detail page when needed:

| Field group | Required captured information |
|---|---|
| Identity | Manufacturer, base part, selected orderable suffix, product description |
| Evidence | Manufacturer URL/document, revision/date, review date, fields checked, unresolved differences |
| Construction | Conductor and physical pair counts separately; AWG, material, stranding; insulation/jacket; shield/drain |
| Ratings | Actual listed markings; certification evidence; voltage; temperature; indoor/plenum/riser and special environmental ratings |
| Electrical | Conductor DCR with units, nominal/maximum status and temperature basis; stated current with all conditions |
| Mechanical | OD, minimum stationary/installation bend radii, pulling tension and stated conditions |
| Application | Candidate uses; exclusions; terminal compatibility; project-specific acceptance reference |
| Status | Checked data versus pending evidence; product availability if separately confirmed |

Use “unknown/not yet checked” rather than assuming defaults. Do not mark a new
vendor's product equivalent merely because gauge, count and plenum classification
match; compare electrical, mechanical, environmental and terminal requirements.
Future scale may justify separate manufacturer detail pages, with this page
remaining the common catalog entry point.

## 3. Edge Cases and Intake Reconciliation

| Supplied statement | Framework disposition |
|---|---|
| All listed products CL2P/CMP | Checked sheets establish CMP. Separate marking evidence from code substitution |
| All products 7×26 | Checked 16 AWG products use 19×29 |
| All products operate −20 to +75°C | Not universal; selected product rows above differ |
| All FE drains 24 AWG | 6347FE sheet specifies a 20 AWG drain |
| 6300FE OD 0.156; 6200UE 0.178; 6200FE 0.180; 6301FE 0.165 | Use checked values 0.162, 0.176, 0.184 and 0.172 in respectively |
| 6302UE OD 0.178; 6202UE 0.208; 6202FE 0.210; 6347FE 0.440 | Use checked values 0.180, 0.206, 0.215 and 0.423 in respectively |
| Universal 8×OD bend rule; 6345FE pull 156 lb | Use product limits; 6345FE gives 3.57 in radius and 274.3 lb |
| 6245FE pull 250 lb | Unverified; retain as intake claim only, not an installation limit |
| Nine pairs is the market maximum | Not established; do not constrain future manufacturer searches |
| Four feeds/controller; six-pair standard | Application proposal; actual demand and reviewed spare policy govern |
| Head-end-only shield grounding | Interface-specific; obtain equipment instructions |

## 4. Applicability Limits

The catalog establishes sourced product attributes, not a universal list of
approved installations. Do not infer installed ampacity, code compliance,
voltage-drop performance, wet/outdoor/hazardous suitability or equipment acceptance.
Source-sheet current figures and cable voltage ratings are not circuit power limits.
No exact UL certification database record or project installation has been
independently approved through this catalog review.

## 5. Sources and Validation

Initial source: owner-supplied *Low-Voltage Class 2 Commercial Lighting Cable
Specification & Selection Guide*, received 2026-10-15. Every supplied base number
is retained in one of the two tables above. Manufacturer sources linked per row
were accessed 2026-10-15; only displayed checked fields are asserted. Full copyrighted
manufacturer sheets are linked rather than copied into the repository.

Regulatory application and unresolved source assertions are tracked in
[Class 2 regulatory basis](../../ontology/reg-and-class/class-2-circuit-cabling.md).
No live project validation is claimed. Changes in product data, listings or adopted
code invalidate dependent selections and require review.

## 6. Status and Stewardship

Draft; last review 2026-10-15. Owner: KIS Solutions, electrical engineering.
Expand across manufacturers as new source-backed candidates are encountered.
