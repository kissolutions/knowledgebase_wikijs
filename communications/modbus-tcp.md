---
title: Modbus TCP — field integration reference
page_type: technical-reference
page_status: draft
published: true
tags: communications, modbus, ethernet, gateway
---

# Modbus TCP — field integration reference

## Purpose
Practical reference for native Modbus TCP devices and TCP-to-RTU gateways. See [Modbus Organization](https://www.modbus.org/) and [Modbus (Wikipedia)](https://en.wikipedia.org/wiki/Modbus) for the full protocol.

## Endpoint versus downstream identity

A Modbus TCP request normally targets an **IP address** and **TCP port 502**. Its Modbus Application Protocol (MBAP) header also contains a **Unit Identifier**.

- A **native Modbus TCP device** is identified on Ethernet by IP; treatment of Unit ID is device-specific (often ignored or constrained).
- A **TCP-to-RTU gateway** commonly uses Unit ID to select a downstream RTU slave. On a multiport gateway, its routing configuration also determines the serial port.
- Multiple RTU slaves can therefore be accessed through the **same gateway IP** with different Unit IDs.

```text
BAS client -- TCP/IP --> gateway 192.168.1.50:502
                              |
          Unit ID 7 ----------+--> serial port 1 --> RTU slave 7
          Unit ID 8 ----------+--> serial port 1 --> RTU slave 8
```

Example reads: `192.168.1.50:502, Unit ID 7, FC03, offset 100, quantity 2` and the same request with Unit ID 8. These are independent devices and data maps.

**Framing precision:** Modbus TCP does not simply carry an unchanged RTU frame. The TCP application data unit uses an MBAP header and omits the RTU CRC; the gateway handles framing and serial timing.

## Practical gateway limitations to verify

| Check | Why it matters |
|---|---|
| Exact model, firmware and operating mode | Gateway behavior varies by product |
| TCP client/connection limit | Concurrent BAS/PLC clients may be rejected |
| Unit ID-to-port routing | Missing/ambiguous routes prevent target selection |
| Per-port electrical node loading | Serial transceiver/cable constraints |
| Supported slave or route count | Manufacturer-specific implementation limit |
| Queueing and concurrency | Shared RTU port can execute only one transaction at a time |
| Timeouts and retries | Queue delay and offline nodes affect all clients |
| Function support and mapping mode | Transparent forwarding and protocol conversion are not equivalent |
| Register data format | Function, zero/one-based address, quantity, scaling and word order |
| Security and segmentation | Classic Modbus TCP has no native authentication/encryption |

## Diagnostic interpretation

- **Ping succeeds:** IP reachability only; not proof of Modbus service or RTU response.
- **TCP connection to port 502 succeeds:** Modbus service reachable; not proof that a slave exists.
- **Valid Modbus response:** request was serviced.
- **Exception 01/02/03:** function, address/range or request-value rejection; identify whether response originated downstream or in gateway.
- **Gateway exceptions 0A/0B:** downstream path unavailable or target did not respond, as reported by gateway.
- **Timeout:** no valid response before the client's deadline; investigate TCP path, gateway, queueing and serial bus.

## Related
- Modbus RTU — field integration reference
- Modbus RTU Network Design — engineering playbook
- Modbus Communications Troubleshooting — field playbook

**Status:** Draft; never generalize one gateway model's limits to all models.
