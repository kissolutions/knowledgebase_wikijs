---
title: Eaton / Tripp Lite UPS network management cards
page_type: hardware
page_status: draft
published: true
tags: hardware, ups, networking
---

# UPS network-management cards — compatibility investigation

## 0. Scope

Reference stub for network supervision of UPS systems. This is a **manufacturer-verification placeholder**, not an approved card selection.

## 1–3. Relevant interfaces

- **Tripp Lite TLNETCARD** is an older UPS management-card designation referenced by field inventory. Do not assume compatibility with Eaton-branded replacement UPS models because of brand acquisition or physical connector resemblance.
- Obtain exact UPS catalog/version, existing card and slot details, firmware, serial port/network interface and current vendor compatibility chart.
- Confirm communication method (SNMP traps/polling, dry contacts, Modbus/BACnet gateway or proprietary protocol), security policy, IP address allocation, alarm semantics and client network approval.
- An observed displayed MAC of all zeroes despite a different label MAC is **a specific as-found discrepancy** to investigate in private project records, not a normal product characteristic.

## 17. Status

**Draft / no compatibility determination.** Proposed Eaton SU1000RTXLCD2U substitute management card is explicitly UNVERIFIED; do not publish a replacement part number without manufacturer confirmation.
