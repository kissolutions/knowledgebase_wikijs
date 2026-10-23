---
title: EIG Shark 250 power meter
page_type: hardware
page_status: draft
published: true
tags: hardware, power-monitoring, eig, meter
---

# EIG Shark 250 — power / energy meter

## 0. Purpose and scope

Physical meter and modular I/O facts for early BAS/PLC monitoring feasibility. This page is **not** a wiring approval or a Modbus point register. Verify the exact meter ordering code and installed cards from labels and manufacturer documentation.

## 1. Core function / capabilities

Measures power/energy and electrical quantities using appropriate voltage wiring and CTs. **Two optional card slots**, shared between network interfaces and I/O. Manufacturer's [Shark 250 manual E169701](https://www.electroind.com/products/Shark_250/pdf/manuals/Shark-250-Cyber-Secure-Power-Energy-Meter-User-Manual_E169701.pdf) lists options including **PO1S** (4 pulse outputs / 4 digital status inputs), **RO1S** (2 relay outputs / 2 digital status inputs), **1mAOS**, **20mAOS**, **INP100S Ethernet**, **INP300S IEC 61850 Ethernet**, **FOSTS/FOVPS fiber** and **RS1S serial**. Options occupy physical slots and are not free additional channels.

## 2. Electrical interfaces / constraints

- **Measured voltage**: 20–576 VAC line-to-neutral range per [manufacturer brochure E169702](https://www.electroind.com/products/Shark_250/pdf/brochures/Shark-250-Cyber-Secure-Meter-Brochure_E169702.pdf), specification page 7. Verify wiring method and actual PT/CT configuration.
- **Meter control power is separate from measurement voltage.** **D2** supply: **90–265 VAC** (or 100–370 VDC); **D** supply: 18–60 VDC. **Do not feed 277 VAC line-neutral into a D2 supply** on a 480Y/277-V system; EIG advises 120-V or appropriate control transformer. [Manufacturer FAQ](https://www.electroind.com/technical-support/faq/).
- **Protection and CTs**: EIG installation manual requires appropriately protected voltage/control-power leads and CT shorting provisions; use approved/certified instrument transformers of the meter's class (nominal **1 A or 5 A secondary**). See manual E169701 §4.1. Do not open CT secondaries under load.
- **Status inputs** on PO1S/RO1S are model- and option-dependent. The proposal records DC-only status-input electrical ratings and internal wetting, but **verify the specific option-card data sheet and wiring polarity before selecting a wet/dry external signal**. In particular, do not presume AC wet contacts are compatible.

## 3. Communication and data integration

The meter's physical status-input terminals do not by themselves establish BACnet/Modbus object address mapping. The **status-input Modbus register map has not yet been verified** against the separate EIG communication guide. Do not fabricate Modbus register offsets, debounce/scan behavior, or claim that every Shark 250 supports Ethernet: identify installed option cards.

## 15. Operational / design mechanics

For monitoring generator/ATS indication through this meter, count required status inputs, installed/remaining expansion slots, measured voltage source and contact signal type. A voltage-present threshold can indicate **voltage availability at a measured bus**, but is not automatically proof of generator-engine running. Treat wiring and point allocation as a design decision. [Conditional monitoring playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/ats-generator-status-monitoring.md).

## 16–17. Source and status

- EIG User Manual v1.18, Doc E169701: source for product and option-card claims; exact configuration must be field-verified.
- EIG Brochure E169702: measured voltage range, fuse/CT wiring examples, supply options.
- **Status:** Draft, physical capabilities partially verified; option-card input ratings, status Modbus registers and any device-specific ordering code remain OPEN.
