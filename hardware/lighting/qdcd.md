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

### Casambi and non-Casambi variants

| Variant | Control architecture |
|---|---|
| QDCD 4CHDR1 BC / explicitly Casambi-enabled selection | Integral Casambi radio; compatible Casambi wireless controls and sensors can communicate with the selected QDCD profile |
| QDCD 4CHDR1 / non-Casambi selection | No integral Casambi capability is established; do not assign direct Casambi control merely because another QDCD in the project has it |

Manufacturer's [QDCD product page](https://smartdclighting.com/product/quaddcdrive/) identifies the optional integral Casambi radio and separate variant sheets (reviewed 2026-10-26). Record exact ordered model and enabled profile rather than treating every QDCD as wireless.

**Owner application clarification, 2026-10-26:** Casambi-enabled QDCDs support compatible kinetic/self-powered controls, including Casambi-compatible EnOcean devices. They may also participate in a CIO-based arrangement where hardwired sensor signals reach the QDCD through the controlling CIO and its supported inputs/SDCnet peripherals. This does **not** establish native hardwired sensor terminals on a QDCD. Obtain the selected-device/profile pairing and command-precedence configuration; do not assume arbitrary EnOcean radio protocols are Casambi-compatible.

**All-Casambi small-system option:** With Casambi-enabled QDCDs and compatible wireless wall controls plus occupancy/ambient-light sensors, the room control path can operate **without a CIO or SW interface modules** when the approved functions are all supported in that architecture. Externally powered Casambi OCC/ALS sensors are available; their control communication is wireless even though they require power wiring. For example, the [Casambi US ecosystem](https://us.casambi.com/ecosystem/) lists powered occupancy sensors and a 24 VDC external-power daylight sensor. Select/verify actual models, supply and demand; do not infer a common voltage or source of sensor power, or confuse these with kinetic wall controls.

Omitting the CIO does not eliminate QDCD/fixture supply feeds or sensor power. Preserve independent room/daylight functions, coverage, manual-off behavior and any required scheduling, integration or emergency functions; a CIO-free option is an architecture choice, not automatic proof that every required feature exists. A mixed CIO/Casambi system retains explicit associations and unresolved command precedence until configured/tested.

## 2A. Verified Parallel CC Luminaire Wiring — Manufacturer Drawing, 2025-06-30

**Authoritative equipment-specific evidence:** SmartDC drawing **"QDCD 4CHDR1 WITH STATIC COLOR TEMPERATURE CONSTANT CURRENT LUMINAIRES ON CHANNEL ONE WIRED IN PARALLEL,"** Rev **A2**, dated **06/30/25**, supplied by the owner as `QDCD-4CHDR1-WITH-3-STATIC-CCT-CC-LUMINAIRES-ON-CH-1-PARALLEL.pdf` (1 page). The diagram explicitly depicts three CC luminaires connected as parallel branches to the same QDCD output.

**Manufacturer's stated limits and condition (drawing callout):**
- **Each luminaire sharing one parallel CC channel must have the same *rated mA*.** It is not sufficient that fixtures share 36 V nominal, their wattages are compatible, or the owner placed them in one cohort.
- **Total channel current must not exceed 4 A** (sum of parallel branch ratings).
- **Total channel power must not exceed 100 W**; aggregate QDCD power must not exceed **400 W**.
- The KIS standard retains a stricter **95 W design maximum** on an ordinary 100 W Class 2 microchannel.

For an output containing multiple CC fixtures, the selected output-current setting is based on the **sum** of individual equally rated branch currents, subject to actual programmable step/range/tolerance. For example, two separately verified 1,139 mA branches require a nominal 2,278 mA total; **this is an arithmetic target, not proof that an exact 2,278 mA setting is available** on a QDCD with approximately 100 mA adjustment steps. The exact programming and allowable current tolerance remain a verification requirement.

**Qualification scope:** This manufacturer's document demonstrates permitted *parallel static-CCT CC topology* with the stated equal-rated-current and power/current constraints. It does not establish:
- that two *different luminaire types* with coincidentally equal current ratings have the necessary matching current-voltage characteristics or stable branch sharing;
- permissible rated-mA mismatch/tolerance (do not invent one);
- load behavior after one branch disconnects, current imbalance, or independently powered emergency/battery modules;
- whether the published example applies without further qualification to tunable-white or different LED-module technologies.

**Owner topology preference vs equipment permission:** KIS's design policy is parallel electrical connection for every multi-fixture Class 2 output. SmartDC separately publishes **series** examples; those are manufacturer-supported alternatives, not the KIS chosen method. Do not confuse physical daisy-chaining with electrically series-connected LED strings.

**Evidence rules:** For a multi-fixture CC channel, record the fixture's **actual verified rated mA at the remote-driver interface** (using `LightObject.design.input_current_ma` with a traceable actual fixture/LED-module source), do not manufacture that rating solely from `W / V_nominal`. Record the manufacturer parallel drawing's identifier and the fixture compatibility basis. Equal rated mA is a **mandatory gate**, not sufficient final engineering qualification. If rated mA is missing or differs across members, reject the group until a different supported configuration is designed. Emergency/base fixture pairings require additional approval of failover and control behavior, regardless of matching rated mA.

## 3. Interfaces and Integration

Supplied sheet pp. 3–6: PDnet RJ45 chain to CIO/QDCDs, CAT5e Class 2; topology labels power wiring 48–57 VDC, 18 AWG minimum power/ground pair. This diagram range is distinct from the catalog 24–57 VDC input range. The legacy topology shows eight QDCDs per CIO and 250 ft maximum distance from CIO; the [CIO firmware clarification](smartdc-cio.md#firmware-dependent-qdcd-expansion) records owner-reported 2026 expansion to sixteen QDCDs pending updated manufacturer/firmware confirmation. Keep QDCD/PDnet and SDCnet-peripheral counts separate. Luminaire wiring uses manufacturer Table A (1 V drop basis); validate actual current, gauge and route. No direct wired sensor-input capacity is confirmed. In a CIO-free Casambi architecture, retain actual power feeds and wireless associations rather than inventing a CIO/PDnet control string.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

Not established in the supplied sources.

## 8. Pitfalls, Assumptions, and Failure Modes

Four lighting outputs do not establish four sensor inputs. Four outputs do not merge four room control zones. Total watts alone do not prove voltage/current compatibility or reduced-feed routing. **A shared nominal LED voltage does not qualify two different rated-mA CC luminaires for one parallel output.** See the manufacturer's Rev A2 wiring restriction in section 2A. Casambi is variant-specific; powered wireless sensors still need a supply. Casambi profile/device limits and mixed CIO/Casambi command precedence remain open, without making a CIO mandatory for an otherwise supported all-Casambi system.

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

Draft; last reviewed 2026-10-26; steward KIS Solutions. Existing manufacturer electrical evidence remains distinct from the dated owner clarification on wireless/hybrid architectures and the pending CIO firmware expansion. The linked manufacturer/Casambi pages corroborate radio variants and powered wireless sensor availability; they do not constitute a tested project integration or command-precedence result.
