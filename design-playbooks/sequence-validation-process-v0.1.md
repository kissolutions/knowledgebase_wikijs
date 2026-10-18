---
title: IECC Lighting Sequence Validation Microprocess v0.1
page_type: playbook
page_status: draft
domain_primary: electrical-lighting
ai_role: prescriptive_standard
published: true
---

# PROC-SEQ-VALIDATE v0.1: 2021 and 2024 IECC

**Independent process.** Following selection of an endpoint SEQ/PSEQ, evaluate the project-specific code and functional requirements against the effective sequence assignment. Neither the reusable SEQ definition nor the canonical project schema contains these edition-specific validation rules. The external [rule catalog](rules/iecc-lighting-sequence-validation-v0.1.json) is separately versioned. The engine is [sequence_code_validate.py](https://github.com/kissolutions/lv-lighting-design/blob/main/generators/sequence_code_validate.py), invoked on each sequence build through [sequence_validation_build.py](https://github.com/kissolutions/lv-lighting-design/blob/main/generators/sequence_validation_build.py).

## Triggers

Run after every sequence selection or build; when any sequence parameter, room classification, daylight association, jurisdiction, permit-date basis, code edition, applicable amendment, exception or source intent changes; before accepting M3; and on independent request at any later date. Reruns preserve historical acceptance and emit a new result plus changes from a prior result. Revalidate **affected endpoint zones**; do not indiscriminately rebuild the project.

## Inputs and operations

Input is a separately documented **Regulatory Basis** (IECC edition 2021 or 2024; jurisdiction, amendments, compliance path, adoption evidence, confirmed/provisional status) plus immutable endpoint/Space classification, area, source controls, applicable daylight, documented exceptions, pinned SEQ revision, and effective assignment parameters.

Apply rules using tri-state applicability: **applicable**, **not applicable**, **unresolved**. Missing adoption dates, room classifications, special-application status or exception evidence are not treated as false. An applicable rule may propose a previously missing deterministic value but **must not overwrite** an accepted value. Numeric constraints produce a check and, if missing, a finding, not a fabricated engineering setpoint. An incompatible sequence/parameter yields a conflict. A guessed code year yields a provisional review finding, never compliance certification.

Each run produces an independent JSON work product: process version, rule catalog revision, input fingerprint, code-basis evidence, applicable/unresolved rules, required values, proposed missing values, conflicts, source references and optional revision delta. Outcomes: `rule_checks_passed`, `needs_review`, `conflict`. No outcome is a blanket assertion of project compliance.

## Starter rule scope

| Edition | First-pass rule family | Section |
|---|---|---|
| 2021 | General occupant sensor controls and <=20 min shutoff | C405.2.1/.1.1 |
| 2021 | Open office >=300 SF, independent zones <=600 SF, vacancy response <=20% | C405.2.1.3 |
| 2021 | Corridor and warehouse occupancy reduction | C405.2.1.4/.1.2 |
| 2021 | Conditional light-reduction methods; daylight response continuous to <=15% and OFF | C405.2.3/.3.1, C405.2.4/.4.1 |
| 2024 | General occupant sensing; source verification pending | C405.2.1/.1.1 |
| 2024 | Continuous dimming to <=10% power and OFF in listed spaces | C405.2.3/.3.1 |
| 2024 | Daylight-response continuous dimming and OFF; numeric low-end not yet established | C405.2.4 |

**Evidence distinction:** The 2021 rule entries have been reviewed against accessible [ICC model-code Chapter 4](https://codes.iccsafe.org/content/IECC2021V3.0/chapter-4-ce-commercial-energy-efficiency), corroborated by [DOE/PNNL analysis](https://www.energycodes.gov/sites/default/files/2022-09/2021_IECC_Commercial_Analysis_Final_2022_09_02.pdf). The unamended 2024 final ICC section could not be directly retrieved in this research pass. Draft 2024 rules are based on secondary corroboration from [Lutron](https://assets.lutron.com/a/documents/3672755_iecc_2024_application_summary.pdf), [Current/Cooper](https://cdn.currentlighting.com/image/upload/v1750699370/Site/applicationguide/NX_IECC_ApplicationGuide.pdf), and [Legrand/Wattstopper](https://mzltg.com/wp-content/uploads/2025/05/quick_guide-2024_IECC_v04.10.2025-FINAL.pdf). They remain *unqualified* until primary-text verification. A manufacturer example is not an adopted code rule.

**Known coverage gaps:** All editions require project-specific exceptions, local amendments, special-application, selected optional efficiency/LLLC alternatives, detailed daylight geometry/wattage applicability, emergency controls and commissioning checks. Some alternate 2021 light-reduction paths, 2024 high-end-trim manual-dimmer exceptions, and the full 2024 listed-space and occupancy rules require additional rule records. A matching subset of rules does not establish comprehensive code compliance. Reconcile with the existing [IECC Occupant Sensor Directives](iecc-occupant-sensor-directives.md).

The sequence catalog remains unchanged. A future revision of this process or its rule data does not mandate a canonical model schema change. It merely produces a new validation work product.
