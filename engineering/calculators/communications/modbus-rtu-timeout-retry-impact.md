---
title: Modbus RTU Timeout and Retry Impact Calculator
page_type: engineering-calculator
page_status: draft
published: true
tags: modbus, rtu, calculator, troubleshooting
---

# Modbus RTU Timeout and Retry Impact Calculator

## Purpose
Estimate how nonresponding devices affect polling-cycle time and other devices sharing a serial port.

## Inputs
- T: effective timeout per attempt (seconds).
- K: additional retry attempts after the first attempt.
- F: number of failed requests in the scan.
- t_good: estimated healthy transaction time for each failed request.
- t_retry: additional retry/backoff overhead per failed request (seconds).
- t_scan: healthy total scan time (seconds).
- S: desired scan interval (seconds).

## Equations
```text
failed_request_time ≈ (K + 1) × T + t_retry
degraded_scan_time ≈ t_scan - Σ(t_good for failed requests)
                              + F × failed_request_time
degraded_utilization ≈ degraded_scan_time / S × 100%
```

This is a conservative planning model assuming each attempt reaches the full configured timeout. Check whether the client or gateway owns retries and whether the timeout starts before or after serial transmission/queueing.

## Example
30 sensors; normal scan 1.317 s; each healthy request 0.04391 s; 500 ms timeout; 2 additional retries; no extra retry delay; 5 s target scan.

```text
failed_request_time = 3 × 0.5 = 1.5 s
one failed sensor: 1.317 - 0.04391 + 1.5 = 2.773 s
three failed sensors: 1.317 - 3 × 0.04391 + 3 × 1.5 = 5.685 s
```

**Result:** three failures push the estimated cycle beyond the five-second target despite low nominal utilization.

## Interpretation and limitations
- Timeouts may include gateway queueing, RTU response waiting or TCP transport time; the actual semantics are implementation-specific.
- Retries may be implemented in more than one layer. Do not count the same retry twice.
- Some clients skip offline devices, back off, pipeline TCP requests or impose queue caps; measure actual degraded behavior.
- A timeout alone does not identify a failed cable or slave.
- Evaluate alarm/update requirements and test a controlled offline-device scenario during commissioning if safe.

## Used by
Modbus RTU Network Design; Modbus Communications Troubleshooting; Modbus TCP gateway hardware pages.
