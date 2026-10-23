---
title: RS-485 Electrical Loading Calculator
page_type: engineering-calculator
page_status: draft
published: true
tags: rs485, calculator, bacnet, modbus
---

# RS-485 Electrical Loading Calculator

## Purpose
Screen the aggregate receiver loading of an RS-485 segment. Applicable to Modbus RTU, BACnet MS/TP and other RS-485 protocols. **Not** a universal device-count calculator.

## Inputs
- Number of each transceiver model on the electrical segment.
- Manufacturer's RS-485 receiver unit-load (UL) rating for each interface.
- Driver/transceiver support and manufacturer-specific limits.

## Equation
```text
total_UL = Σ(device_quantity × device_UL)
```

For a conventional 32-unit-load driver, compare the total to the driver's supported load. Confirm the actual hardware; modern interfaces may use fractional unit loads and different driver capabilities.

## Example (hypothetical ratings)
```text
30 sensors × 1/8 UL = 3.75 UL
1 gateway × 1 UL     = 1.00 UL
total               = 4.75 UL
```

## Interpretation and limitations
- Passing the unit-load screen does **not** prove that the gateway supports the number of nodes, that cable length and topology are acceptable, or that the network will meet polling requirements.
- Termination, biasing, cable impedance/capacitance, stubs, common-mode voltage, isolation, shielding, grounding and noise must be evaluated separately.
- The often-quoted '31 devices' arises in some traditional 32-UL implementations, but is not a universal Modbus or RS-485 protocol maximum.
- Obtain actual unit-load ratings from each manufacturer's datasheet; do not assume fractional loads.
- Verify the most restrictive gateway, transceiver, cable and manufacturer-supported topology limits.

## Used by
Modbus RTU reference; BACnet MS/TP reference; Modbus RTU Network Design; Modbus Communications Troubleshooting; gateway and sensor hardware pages.
