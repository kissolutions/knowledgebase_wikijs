---
title: Allen-Bradley Logix controller families for building plant systems
page_type: hardware
page_status: draft
published: true
tags: hardware, controllers, rockwell, plc
---

# Allen-Bradley Logix controllers — plant architecture reference

## 0. Purpose

Manufacturer-anchored family guide for early plant controls selection. **Not a selected bill of material or approved failover design.** Keep physical I/O module capacity, compatible communication firmware and CPU memory/connection limits model-specific.

## 1–3. Candidate family / I/O concepts

- **CompactLogix 5380 / 5069-L3x** uses Rockwell Logix architecture with EtherNet/IP communication. Check full catalog number, onboard ports, motion/safety/process variants and limits against the [5380 product page and manual 5069-UM001](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/programmable-controllers/small-controllers/compactlogix-family/compactlogix-5380-controllers.html).
- **ControlLogix 5580 / 1756** is an alternative family with catalog-specific redundant controller options; do not equate 1756 redundancy with application-managed CompactLogix Hot Backup. [Rockwell HIGHAV-RM002G-EN-P](https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/highav-rm002_-en-p.pdf).
- **Distributed I/O** can use compatible 5069 Compact 5000/5094 FLEX 5000 adapters with EtherNet/IP, subject to architecture, connection, update and environmental constraints. The physical I/O card location, controller owning the channel, and producing field device are separate relationships.
- **DLR ring** is a network topology; it does not make a single CPU redundant. Confirm exact DLR-capable adapters, switches/supervisor and network failover assumptions before committing the topology.

## 4–15. Cross-domain design constraints

- BACnet MS/TP/IP chillers and VFDs are **not automatically native EtherNet/IP devices**. Choose verified protocol gateways or hardware interfaces with a defined point/register map and polling/update/failure behavior. The [Moxa MGate 5105-MB-EIP](../../../hardware/gateways/moxa-mgate-5105-mb-eip.md) is a **Modbus-to-EtherNet/IP bridge, not a BACnet gateway**.
- Determine controller loss tolerance, warm/cold spare, retained state consistency and effect on drives/chillers before controller selection.
- CPU choice does not eliminate requirement for independently functioning hardwired life-safety and equipment protective interlocks.
- Tag counts and network points are not physical I/O channel counts; size modules only from verified hardwired channel requirements and reservations.

## 16–17. Related / status

- [HVAC PLC staged availability playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/hvac-plc-staged-availability.md)
- [Proposed point counting contract](https://github.com/kissolutions/controls-engineering/blob/main/docs/engineering-data/point-allocation-and-counting-proposal.md)
- **Draft.** Controller memory, input limits, redundant 5069 I/O compatibility, Hot Backup code-tool access and exact switchover timings are intentionally **not asserted** until catalog/firmware review.
