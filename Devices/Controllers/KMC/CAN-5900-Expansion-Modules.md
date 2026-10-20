---
title: CAN-5900 Expansion Modules
description: Manufacturer-verified CAN-5901 and CAN-5902 EIO addressing and engineering constraints
published: true
date: 2026-10-20T00:00:00.000Z
tags: hardware, controller, kmc, expansion, eio
editor: markdown
dateCreated: 2026-10-20T00:00:00.000Z
---

# CAN-5900 Series — EIO Expansion Modules

**Models:** CAN-5901 (8 inputs + 8 outputs); CAN-5902 (16 inputs, no outputs). Connect to a supported BAC-5900 series controller or KMD-5290 LAN controller; maximum **four expansion modules** per controller, on an EIO daisy-chain up to **200 ft (61 m)** from the controller.

**Authoritative source:** KMC Controls, *CAN-5900 Series Expansion Module Installation Guide*, document **925-019-03M** (© 2026). Address tables and switch diagrams: **page 3**. The source covers the **CAN-590x expansion family**; do not confuse CAN-5901/CAN-5902 expansion modules with BAC-5901/BAC-5902 parent controllers.

## EIO input / output object address map — page 3

The EIO address determines the controller-side input/output object numbers. These are **object-number ranges**, not module-terminal labels or BACnet device IDs. Mixed CAN-5901 and CAN-5902 configurations retain the same fixed ranges for each type and address.

| Physical EIO module address | CAN-5901 input objects | CAN-5901 output objects | CAN-5902 input objects | CAN-5902 outputs |
|---|---|---|---|---|
| 1 (factory default) | 11–18 | 9–16 | 43–58 | None |
| 2 | 19–26 | 17–24 | 59–74 | None |
| 3 | 27–34 | 25–32 | 75–90 | None |
| 4 | 35–42 | 33–40 | 91–106 | None |

The example **BAC-5900 parent controller** is shown with input objects **3–10** and output objects **1–8** (address 0). Verify model-specific parent I/O against the parent controller's own documentation; these tables are the installation guide's reference configuration.

**Critical:** A CAN-5902 at EIO address 1 uses **inputs 43–58**, **not** 11–26. A CAN-5901 at address 2 uses **inputs 19–26** and **outputs 17–24**, regardless of whether address 1 is a CAN-5902. Address modules consecutively (1, 2, …) to avoid gaps. CAN-5901 and CAN-5902 types may be mixed or replaced without renumbering remaining CAN-5901 objects.

## Module address DIP switches — page 3

**UP = OFF; DOWN = ON. Switch 4 must always remain UP/OFF.**

| Address | Switch 1 | Switch 2 | Switch 3 | Switch 4 |
|---|---|---|---|---|
| 1 (default) | DOWN / ON | UP / OFF | UP / OFF | UP / OFF |
| 2 | UP / OFF | DOWN / ON | UP / OFF | UP / OFF |
| 3 | DOWN / ON | DOWN / ON | UP / OFF | UP / OFF |
| 4 | UP / OFF | UP / OFF | DOWN / ON | UP / OFF |

Set the physical address switches to match the intended object block; the input/output numbers follow the address, not installation order.

## Installation and software constraints (pages 1–9)

- **Firmware compatibility (page 1):** CAN-5902 requires BAC-5900 parent firmware **R1.2.0.9 or later**. The KMD-5290 minimum appears as “RXXX or later” in this edition of the guide; **do not treat that placeholder as a verified KMD-5290 version**.
- **EIO network (pages 2–3, 9):** Maximum four modules. Use **18 AWG shielded twisted-pair** with maximum capacitance **51 pF/ft** (Belden 82760 or equivalent). Continue + to + and – to –; bond shield through devices and ground it at **one end only**. Set the EOL switch **ON at both physical ends only**; the module ships with EOL OFF.
- **Configuration (page 7):** Expansion input/output objects **are not automatically created** on the controller. Explicitly create/configure the required input objects (11 and higher) and output objects (9 and higher) using KMC Connect, KMC Converge or TotalControl. The modules typically do not appear as standalone nodes in Network Manager; supported firmware/software may show them via proprietary objects.
- **Module diagnostics (pages 6–8):** READY flashes about once per second when operating normally. EIO COMM **rapid flashing** indicates communication; **slow flashing** can indicate the module has been silenced through its proprietary object; **solid on** may indicate open network or blown isolation bulbs. The HPO-0055 network isolation bulbs can be damaged by ground-potential/phase discrepancies; lit bulbs indicate improper phasing. Module firmware **1.0.0.1 or later** exposes the relevant **[PRP140-x] EIO_0x** proprietary object for status, firmware, reset and silence.
- **Output safety (pages 4–5, 9):** **Never connect 24 VAC directly to a CAN-5901 output without a compatible HPO-6701, HPO-6703 or HPO-6705 output override board.** For HPO-6701/6703/6705 switched outputs, use **SC (Switched Common)**, not GND. Leave factory output-slot jumpers unless installing an override board.
- **Loss-of-communications behavior (page 5):** CAN-5901 generally **holds last output values** when EIO communication is lost until communications return or power is lost. Exception documented for CAN-5901 module firmware **0.0.0.1**: outputs turn off approximately 30 s after loss. Evaluate the process hazard of this behavior; do not assume outputs fail-safe on communications loss.
- **Power coordination (page 5):** One CAN-590x module per **24 VAC Class 2 transformer**, per the manufacturer. Recommend supplying controller and module transformers from the same electrical circuit so their power failure/restart behavior is coordinated.
- **Physical features (pages 1, 9):** Install in a metal enclosure for RF shielding and protection. CAN modules have **no room sensor port**. The CAN-5902 does not provide outputs or output override slots.

## Model and terminology boundaries

- **BAC-5901 / BAC-5902** = parent controller model pages. **CAN-5901 / CAN-5902** = EIO expansion modules.
- Object-number ranges above are manufacturer-defined; controller programming tags, terminal labeling, channel direction, and hardware suitability require separate project verification.
- Source-specific confirmed facts here do **not** validate all previously marked-PENDING quantitative specifications on parent controller pages.

## Related pages

- [BAC-5901 parent controller](BAC-5901.md)
- [BAC-5902 parent controller](BAC-5902.md)
- [KMC controllers overview](KMC-Controllers-Overview.md)

**Source status:** Page 3 address map, switch positions and listed installation constraints transcribed from manufacturer Installation Guide **925-019-03M**.