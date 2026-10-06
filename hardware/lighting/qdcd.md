---
title: "SmartDC QuadDCDrive (QDCD)"
page_type: product_class
page_status: draft
confidence_level: medium
domain_primary: low-voltage-lighting
ai_role: prescriptive_standard
invocation_triggers:
  systems_present: [low_voltage_lighting, smartdc]
decision_axes: [power_allocation, controls, equipment_placement, owner_review]
related_pages:
  - "https://github.com/kissolutions/knowledgebase_wikijs/blob/main/design-playbooks/smartdc-allocation-index.md"
---

# SmartDC QuadDCDrive (QDCD)

## 0. Purpose and Scope

Remote programmable CV/CC driver for driverless LV fixtures; four independent lighting outputs. QCDC and cutie CD are dictation aliases for QDCD.

## 1. Core Function

Remote programmable CV/CC driver for driverless LV fixtures; four independent lighting outputs. QCDC and cutie CD are dictation aliases for QDCD.

## 2. Capabilities and Variants (What Is Possible)

Manufacturer evidence: supplied SMARTDC-QuadDCDrive Specification Sheet, revised 2025-06-30, pp. 1–2: 400 W aggregate maximum; up to four 100 W outputs; 24–57 VDC input; 12–55 VDC programmable output; 1–4 A current range in approximately 100 mA increments; ±1% current tolerance; 1 W standby. Verify current setting for each already-designated channel. QDCD 4CHDR1 BC includes Casambi; base QDCD 4CHDR1 does not list Casambi. 16-bit dimming with SDCnet/DMX; Casambi 8-bit. Dry locations only, not plenum rated; 0–45°C, 0–95% noncondensing RH.

Owner describes four independent Class 2 input feeds electrically aggregated; default four PDU outputs to four QDCD inputs. Independent-input routing/reduced-feed support is not established by the supplied sheet. Do not treat owner description as wiring permission.

## 3. Interfaces and Integration

Supplied sheet pp. 3–6: PDnet RJ45 chain to CIO/QDCDs, CAT5e Class 2; topology labels power wiring 48–57 VDC, 18 AWG minimum power/ground pair. This diagram range is distinct from the catalog 24–57 VDC input range. Maximum eight QDCDs per CIO, 250 ft maximum distance from CIO. Luminaire wiring uses manufacturer Table A (1 V drop basis); validate actual current, gauge and route. No direct wired sensor-input capacity is confirmed.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Four lighting outputs do not establish four sensor inputs. Four outputs do not merge four room control zones. Total watts alone do not prove voltage/current compatibility or reduced-feed routing. Casambi limits and CIO/Casambi precedence remain open.

## 9. Ecosystem and Related Devices

[QDCD assignment mini playbook](../../design-playbooks/qdcd-channel-assignment.md) · [CIO](smartdc-cio.md) · [EPS PDU](eps-pdu.md)

## 10. Cost and Commercial Reality (Order-of-Magnitude)

Pricing not established; do not invent prices.

## 11. Procurement and Availability

Confirm exact variant, firmware, lead time and accessories with vendor.

## 12. Selection and Sizing Considerations (Rules of Thumb)

Device constraints feed the linked mini playbook. Geographic and control requirements can increase installed counts above lower bounds.

## 13. Commissioning and Validation Considerations

Reconcile equipment/port IDs with drawings; test every approved control association, configuration and applicable fail/emergency behavior.

## 14. Lifecycle, Maintenance, and Longevity

Record as-built location, port map and configuration; maintenance requirements beyond supplied sheets remain unconfirmed.

## 15. Operational Mechanics

Do not infer signal precedence, reduced-input routing, failure state or emergency operation. Obtain applicable wiring/configuration evidence.

## 16. Cross-links and Navigation

[QDCD assignment mini playbook](../../design-playbooks/qdcd-channel-assignment.md) · [CIO](smartdc-cio.md) · [EPS PDU](eps-pdu.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-06; steward KIS Solutions. Owner directives are design policy, separately identified from manufacturer evidence.
