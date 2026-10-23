---
title: Modbus RTU Network Performance Calculator
page_type: engineering-calculator
page_status: draft
published: true
tags: modbus, rtu, calculator, communications
---

# Modbus RTU Network Performance Calculator

## Purpose
Estimate normal RTU polling time, utilization and required baud rate **per serial port**. This is a design screening method, not a substitute for measured performance.

## Inputs
- N: number of devices in a group.
- Q: transactions per device per scan.
- R: registers per FC03/FC04 read (1–125).
- B: serial baud (bit/s).
- C: bits per character (8N1 = 10; 8E1/8O1/8N2 = 11).
- S: desired group scan interval (s).
- t_dev: measured/estimated device turnaround (s).
- t_extra: additional inter-frame/driver/gateway time per transaction not already included in t_dev (s).

## Equations
For a normal FC03/FC04 register read, request = 8 bytes; response = 5 + 2R bytes.

```text
wire_bytes = 13 + 2R
wire_time = wire_bytes × C / B
transaction_time ≈ wire_time + t_dev + t_extra
group_time ≈ N × Q × transaction_time
utilization_fraction ≈ Σ(group_time / S) across all groups on one serial port
utilization_percent = 100 × utilization_fraction
```

The inverse for one uniform group, with a positive denominator:

```text
B_min = N × Q × (13 + 2R) × C / (S - N × Q × (t_dev + t_extra))
```

**Important:** `B_min` only represents a 100%-loaded theoretical boundary. To target a utilization fraction `u_target` (<1), replace `S` in the denominator with `u_target × S`. Select an actually supported baud rate and recalculate.

## Example
30 sensors; one FC03 read of 10 registers each; 19,200 baud; 8E1; 20 ms device turnaround; 5 ms additional overhead; 5 s target scan.

```text
wire_bytes = 33
wire_time = 33 × 11 / 19200 = 0.01891 s
transaction_time = 0.01891 + 0.020 + 0.005 = 0.04391 s
group_time = 30 × 0.04391 = 1.317 s
utilization = 1.317 / 5 × 100 = 26.3%
```

## Interpretation and limitations
- Treat utilization bands as internal engineering guidance, **not Modbus limits**. As an initial target, consider ≤50–60% nominal loading and validate under failure conditions.
- Different request groups may have different intervals; sum their fractional loads per port.
- Include every upstream TCP client's requests if the gateway forwards them onto the same RTU port.
- RTU requires inter-frame silence (at least 3.5 character times); ensure it is represented without double counting.
- This simplified formula is for successful FC03/FC04 reads; other functions, errors, retries, multi-register writes and gateway mapping require their actual frame lengths and timing.
- If the inverse denominator is zero/negative, no finite baud rate can meet the assumed timing budget; reduce requests or turnaround/overhead, increase interval or segment the network.
- Validate with observed full-cycle times and queueing behavior at commissioning.

## Used by
Modbus RTU Network Design; Modbus Communications Troubleshooting; Modbus RTU and TCP reference pages; applicable gateway and sensor hardware pages.
