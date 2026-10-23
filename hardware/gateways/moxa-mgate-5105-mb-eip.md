---
title: Moxa MGate 5105-MB-EIP gateway
page_type: hardware
page_status: draft
published: true
tags: hardware, gateway, modbus, ethernet-ip, moxa
---

# Moxa MGate 5105-MB-EIP — Modbus/EtherNet-IP gateway

## 0. What it is / is not

Manufacturer-documented **Modbus RTU/ASCII/TCP to EtherNet/IP** gateway. **This device does NOT provide native BACnet MS/TP or BACnet/IP conversion**. It cannot bridge a BACnet chiller to an Allen-Bradley PLC unless another supported protocol and map are provided.

## 1–3. Manufacturer capabilities

Per [Moxa official product page](https://moxa.com/en/products/industrial-edge-connectivity/protocol-gateways/ethernet-ip-gateways/mgate-5105-mb-eip-series):

| Property | Vendor-published specification |
|---|---|
| Serial | One RS-232/422/485 port, Modbus RTU/ASCII master or slave |
| Ethernet | Two 10/100 RJ45 ports; Modbus TCP client/server; EtherNet/IP Scanner / Adapter |
| Modbus command limit | 100 commands for serial Modbus; 100 for Modbus TCP |
| EtherNet/IP I/O data | Max 496 bytes input and 496 bytes output (configuration dependent) |
| Power | 12–48 VDC |
| Temperature | Standard 0–60°C; -T model -40 to +75°C |

## 4–15. Integration limits / design checks

Check exact registers or coils needed from each drive, serial bus addresses, gateway Modbus timing, scan/command capacity, data types/endianness, EtherNet/IP assembly sizes, cyclic update/RPI, fault status, write authority and security. Two Ethernet jacks do not prove the specific managed ring topology or redundancy role without manufacturer support. Source drives on their EFB typically cannot simultaneously speak BACnet MS/TP and Modbus RTU on the same EFB channel.

## 17. Status

Draft, vendor hardware envelope documented. **No project-specific point map, BACnet gateway role or production connectivity validated.**
