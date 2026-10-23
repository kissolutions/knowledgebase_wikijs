---
title: ABB ACH580 VFD — embedded fieldbus and BAS/PLC interface
page_type: hardware
page_status: draft
published: true
tags: hardware, vfd, abb, bacnet, modbus
---

# ABB ACH580 — fieldbus integration constraints

## 0–3. Primary vendor facts

The ACH580 HVAC control program's **embedded fieldbus (EFB)** on RS-485 supports **Modbus RTU**, **BACnet MS/TP** and **N2**, selected by configuration, rather than running several protocols on the same EFB port simultaneously. The protocol and related addressing/baud/points are configured in **parameter group 58**. Manufacturer source: ABB *ACH580 HVAC control program firmware manual*, **3AXD50000027537**, especially EFB interface/parameter group 58. [ABB ACH580 document index](https://library.e.abb.com/public/02fa7e659ce54142a533ee7e0c5846cf/LinkList_ACH580-01.html).

Separate optional Ethernet fieldbus adapters can provide other protocols, subject to installed hardware, firmware and correct port/configuration:

- **FMBT-21:** Modbus/TCP adapter.
- **FBIP-21:** BACnet/IP adapter.
- **FEIP-21:** EtherNet/IP adapter (do not mistake FEIP-21 for FBIP-21).

**Design impact:** switching embedded RS-485 EFB from BACnet MS/TP to Modbus RTU for a PLC removes the direct BACnet MS/TP path on that EFB. If the BAS head-end needs the same values, provide an independently validated path via PLC gateway/integration or a supported separate adapter; don't silently assume dual-protocol EFB operation.

## 15. Operational verification

Confirm actual model, firmware, installed adapter modules, drive control location/priority, source of run-enable, fault reset, STO/hand/bypass interfaces, parameters and register/object support. Decide which device owns start commands and how loss of the selected network is handled. No safety interlock should depend solely on supervisory network communication unless approved design and code permit.

## 17. Status

**Draft / EFB fact verified from ABB manual reference.** Physical port count, drive model option, communication maps and actual project ownership remain model-/installation-specific.
