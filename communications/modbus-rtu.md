---
title: Modbus RTU — field integration reference
page_type: technical-reference
page_status: draft
published: true
tags: communications, modbus, rs485
---

# Modbus RTU — field integration reference

## Purpose
Practical constraints for designing, commissioning, and diagnosing Modbus RTU networks. This is not a replacement for the protocol specification or a manufacturer's device manual.

References: [Modbus Organization](https://www.modbus.org/) · [Modbus (Wikipedia)](https://en.wikipedia.org/wiki/Modbus) · [RS-485 (Wikipedia)](https://en.wikipedia.org/wiki/RS-485).

## Architecture and BACnet comparison

| Topic | BACnet MS/TP | Modbus RTU |
|---|---|---|
| Shared medium | Usually RS-485 | Usually RS-485 |
| Local address | MS/TP MAC | Slave/server address |
| System-wide identity | BACnet Device Instance | No equivalent |
| Discovery | Who-Is/I-Am | No standardized discovery |
| Bus access | Token passing among masters | Normally one client/master; no token passing |
| Routing | BACnet internetwork routing | No native equivalent |
| Data | Objects and properties | Coils and registers |

**Token passing matters:** BACnet MS/TP masters coordinate bus access by circulating a token. Modbus RTU has no corresponding arbitration mechanism; independently transmitting masters can collide. A suitable Modbus TCP-to-RTU gateway can accept multiple TCP clients and serialize requests onto a single RTU bus, subject to gateway limits. This does not turn RTU into a multi-master protocol.

A slave address identifies a device only within its RTU address domain. The usual individually addressed range is 1–247; address 0 is broadcast (no reply). Do not mistake the address range for a supported physical device count.

## Physical and configuration constraints

- **Serial format:** confirm baud rate, data bits, parity and stop bits on every device and gateway serial port; all must be compatible.
- **Topology:** use a supported linear bus; avoid uncontrolled stars and long stubs.
- **Termination:** terminate the two electrical ends of the bus, not every node.
- **Biasing:** verify a stable idle state and avoid inappropriate duplicate bias networks.
- **Conductors:** verify A/B polarity against actual vendor pinouts; A/B naming is not consistent across manufacturers.
- **Reference and protection:** follow vendor requirements for signal common, shield, grounding, isolation, surge protection and common-mode limits.
- **Electrical capacity:** count transceiver unit loads and cable effects. The traditional 32-unit-load figure is not a universal 31-slave limit; modern fractional-load devices may differ.
- **Gateway capacity:** verify serial-port count, supported nodes, routing-table limits, TCP client count, request queuing, and supported operating modes from the exact model/firmware.
- **Performance capacity:** evaluate aggregate polling time, baud rate, register grouping, timeouts, retries and offline-node effects independently of address and electrical capacity.

## Data and addressing

| Table | Conventional reference | Common function |
|---|---|---|
| Coils | 0xxxx | 01 / 05 / 15 |
| Discrete inputs | 1xxxx | 02 |
| Input registers | 3xxxx | 04 |
| Holding registers | 4xxxx | 03 / 06 / 16 |

Each register is 16 bits. Multi-register values require manufacturer-defined signedness, scaling and byte/word order. A traditional holding-register label `40001` corresponds to zero-based protocol address `0`; `40101` corresponds to `100`. Some manuals/software instead use one-based register numbers. Verify notation, function code, starting offset and quantity together. A table's theoretical write capability does not establish that a specific device permits writes.

## Practical limitations and field implications

- No standardized discovery, point names, units or universal register map: retain manufacturer model/revision and register documentation.
- No native Modbus RTU routing: multiport TCP gateways require verified Unit ID-to-port routing; overlapping slave IDs on different ports require a supported disambiguation mechanism.
- No RTU multi-master arbitration: never connect two independent serial masters without an explicitly supported coordination architecture.
- Multiple TCP clients can overload a shared RTU bus even when all connections are accepted.
- A timeout is not a Modbus exception. An exception establishes that a Modbus-speaking endpoint responded, but the gateway may generate it rather than the intended slave.
- RS-485 is an electrical interface, not a protocol; BACnet MS/TP wiring compatibility does not imply Modbus interoperability.
- Classic Modbus RTU provides no native authentication or encryption; isolate and protect network access appropriately.

## Related procedures
- Modbus TCP — field integration reference
- Modbus RTU Network Design — engineering playbook
- Modbus Communications Troubleshooting — field playbook

**Status:** Draft; model-specific capacities must be verified from installed equipment documentation.
