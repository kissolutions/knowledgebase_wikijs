---
title: "SmartDC SDCS CIO"
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

# SmartDC SDCS CIO

## 0. Purpose and Scope

Lighting system controller and sensor/data hub; PDnet to QDCDs, SDCnet to sensor peripherals.

## 1. Core Function

Lighting system controller and sensor/data hub; PDnet to QDCDs, SDCnet to sensor peripherals.

## 2. Capabilities and Variants (What Is Possible)

Retain three distinct capacities rather than a single generic device count:

| Interface / function | Capacity and behavior | Evidence / status |
|---|---|---|
| Direct CIO sensor ports | **8 ports**; each port operates its attached sensors as one aggregated control group / one scene | Eight inputs in supplied sheet; grouped behavior and isolated-room design use clarified by owner, 2026-10-26 |
| QDCD driver connections, shown as **PDnet** in manufacturer topology | Legacy documented maximum **8 QDCDs**; owner reports a **2026 firmware update expands this to 16 QDCDs** | Adopt 16 only as an explicitly recorded firmware-dependent owner design basis pending updated manufacturer confirmation; see `CIO-QDCD16-FW` below |
| SDCnet peripherals, such as SW4/SW8 | Legacy documented maximum **16 SDCnet devices** | Separate from the QDCD count; do not combine the two into one sixteen-device allowance |

Supplied SMARTDC-SDCS-CIO Specification Sheet pp. 1–3: topology shows 250 ft maximum distance from CIO on each network. Input via PDnet RJ45 at nominal 48 VDC. SDCnet output 24 VDC, 250 mA maximum combined across both ports; standby <1 W. Not plenum rated; 0–45°C, noncondensing 0–95% RH. Ethernet 10/100 and REST API listed. Retain supported dry-contact, 0–10 V dimming and 0/24 V sensor interfaces subject to exact wiring instructions.

### Direct sensor ports: grouped room controls

**Owner hardware clarification / KIS application rule, 2026-10-26:** A direct CIO sensor port may accept multiple compatible sensors, but their signals are aggregated and operate as a group. **One scene/control group maps to one sensor port. Use each port for an isolated room/control group only.** This does not restrict the whole CIO to one room: other ports may serve other independent room groups. Additional sensors on one port extend that group's sensing, not the number of independently controllable rooms or scenes. Do not combine independent occupancy areas or an occupancy-only area and a separately controlled daylight area on one port merely because connectors are available.

**Open item `CIO-PORT-FANIN`:** Maximum physical sensors per direct port is **unknown**; the owner's possible value of **4** is a question, not an established rating. Obtain the supported sensor models, input types, wiring/combining method, per-port/total sensor-power limits and exact aggregation behavior. Do not multiply 8 ports by 4 to claim 32-sensor capacity or infer how analog signals may be combined.

### Firmware-dependent QDCD expansion

**Open item `CIO-QDCD16-FW`:** Owner reports that a firmware release in 2026 increased the CIO's supported QDCD count from the documented 8 to **16**. Obtain an updated datasheet or manufacturer firmware/release confirmation identifying the applicable CIO hardware/firmware, QDCD compatibility and any topology/power/distance conditions. Record the actual installed firmware and the explicit basis when using 16 in project sizing; do not silently apply it to unverified legacy CIOs.

**Network terminology:** Manufacturer wiring diagrams label the QDCD connection **PDnet** and peripheral connection **SDCnet**; preserve those interface labels in wiring/port ledgers. The reported expansion concerns the QDCD count, not a new combined QDCD/peripheral allowance. The [public 2025 CIO sheet](https://smartdclighting.com/wp-content/uploads/2025/07/SMARTDC-SDCS-CIO-Specification-Sheet.pdf), topology p. 3, still shows 8 QDCDs and 16 SDCnet peripherals (reviewed 2026-10-26); it does not confirm the new firmware limit. Updated manufacturer evidence remains pending.

## 3. Interfaces and Integration

Receives power from a nearby QDCD via PDnet and distributes power/data to daisy-chained SDCnet devices (sheet p. 1). Trace CIO/control and peripheral demand into the power budget; do not hide it inside lamp watts. RJ45 appearance does not establish Ethernet interchangeability. Distinguish PDnet, SDCnet and Ethernet.

## 4. Regulatory Requirements and Certifications (Constraints)

Use the exact selected model listing and installation instructions. This page is a draft product knowledge record, not a compliance finding.

## 5. Accessories and Supporting Components

See linked devices and allocation mini playbook.

## 6. Typical Application Contexts

Multi-area LV lighting with remote drivers and local sensor aggregation. Application context does not assign project control intent.

## 7. Historical Context and Evolution

The reviewed 2025 topology documents eight QDCDs per CIO. Owner reports a 2026 firmware expansion to sixteen, with updated manufacturer/firmware evidence still pending under `CIO-QDCD16-FW`; do not erase the legacy basis or apply the reported expansion indiscriminately.

## 8. Pitfalls, Assumptions, and Failure Modes

Sixteen bus devices are not sixteen sensors or sixteen direct sensor ports. Multiple sensors on one direct port are not independently addressable scenes. Keep legacy 8-QDCD, reported firmware-expanded 16-QDCD and documented 16-SDCnet-peripheral counts distinct. Do not assume sixteen peripherals fit the 250 mA budget. Exact branching/termination, combined route interpretation and mixed CIO/Casambi command precedence remain verification items.

## 9. Ecosystem and Related Devices

[CIO/sensor allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [QDCD](qdcd.md) · [SW4/SW8](smartdc-sw4-sw8.md)

## 10. Cost and Commercial Reality (Order-of-Magnitude)

Pricing not established; do not invent prices.

## 11. Procurement and Availability

Confirm exact variant, firmware, lead time and accessories with vendor.

## 12. Selection and Sizing Considerations (Rules of Thumb)

Direct-input demand is sized by independent isolated-room scene/control groups, not just physical sensor count: up to eight occupied ports before electrical/power/wiring constraints. Unknown fan-in cannot be used to increase verified capacity. QDCD allocation uses the applicable documented/explicit firmware-dependent project capacity rather than an unconditional eight- or sixteen-driver rule. Geographic, peripheral-power and control requirements can increase installed counts above lower bounds; see the linked mini playbook.

## 13. Commissioning and Validation Considerations

Record CIO model/firmware, QDCD count, SDCnet peripheral count and direct-port-to-room/scene map separately. For every shared sensor port, test the actual group response and isolation from other ports. Verify expanded-driver operation when relying on the 2026 update, and test all approved control associations and applicable fail/emergency behavior.

## 14. Lifecycle, Maintenance, and Longevity

Record as-built location, port map and configuration; maintenance requirements beyond supplied sheets remain unconfirmed.

## 15. Operational Mechanics

Do not infer signal precedence, reduced-input routing, failure state or emergency operation. Obtain applicable wiring/configuration evidence.

## 16. Cross-links and Navigation

[CIO/sensor allocation mini playbook](../../design-playbooks/smartdc-sensor-cio-allocation.md) · [QDCD](qdcd.md) · [SW4/SW8](smartdc-sw4-sw8.md)

## 17. Status and Stewardship

Draft; last reviewed 2026-10-26; steward KIS Solutions. The 2026 capacity expansion and direct-port grouping behavior are dated owner-provided clarifications, not independently verified updated manufacturer ratings. `CIO-PORT-FANIN` and `CIO-QDCD16-FW` remain open. Project applicability/firmware evidence is retained outside this public knowledgebase.
