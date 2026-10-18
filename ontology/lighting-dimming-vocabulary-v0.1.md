---
title: "Lighting Dimming Scheme and Control Interface Vocabulary v0.1"
page_type: reference
page_status: draft
domain_primary: electrical-lighting
published: true
tags: [lighting, controls, dimming, fixture]
editor: markdown
---

# Lighting Dimming Scheme and Interface Vocabulary v0.1

**Two independent concepts must never share a column or enum.**

## Dimming scheme — required lighting behavior

Defined on the lighting control **sequence** (the `SEQ-` or `PSEQ-` behavioral definition), for each endpoint zone:
- `continuous`: user/control command can vary output over the supported dimming range (subject to resolution, driver curve, minimum output). Does **not** prove dim-to-off.
- `stepped`: only discrete commanded light levels are required; include required step count and levels/behavior when specified. A continuous-capable system may sometimes implement discrete scenes, subject to verified controller behavior.
- `none`: sequence only requires on/off behavior, even if its installed fixtures happen to be capable of dimming.
- `unknown`: source or design intent unresolved, valid during intake but **not** for an approved standard or locked M3 sequence.

Use a separate `dimming_steps` integer (minimum 2) only for a `stepped` scheme. A stepped control requirement does not establish electrical waveform or a fixture interface.

## Fixture dimming interface — accepted physical control signal

These are canonical lower-case machine values. Present human-readable descriptions in forms and schedules. Multiple *documented alternative* interfaces may be listed; do not claim simultaneous support unless manufacturer evidence establishes it.

| Value | Engineer-facing label | Technical interpretation |
|---|---|---|
| `triac_forward_phase` | TRIAC / forward-phase | Forward/leading-edge line-voltage phase-cut input |
| `elv_reverse_phase` | ELV / reverse-phase | Reverse/trailing-edge phase-cut input |
| `phase_cut_universal` | Phase-cut universal | Manufacturer explicitly supports both leading and trailing edge |
| `zero_to_ten_v` | 0–10 V | Analog low-voltage dimming control |
| `one_to_ten_v` | 1–10 V | Distinct analog control characteristic; not automatically interchangeable with 0–10 V |
| `dali` | DALI / DALI-2 | Digital addressable lighting interface; note compatible version/profile separately |
| `dmx512` | DMX512 | Digital data interface; specify profile/capabilities separately |
| `pwm` | PWM control input | Pulse-width modulated dimming signal; verify voltage/frequency/polarity |
| `ccr` | Constant-current reduction | Reducing regulated drive current as manufacturer's dimming method; not itself a universal controller command interface |
| `proprietary_digital` | Other digital interface | Specify protocol and manufacturer |
| `integrated_wireless` | Integrated wireless control | Only if fixture/driver **itself** accepts wireless commands; specify protocol (e.g. Casambi/Bluetooth) in notes |
| `none` | No dimming input | Interface confirmed absent |
| `other` | Other documented method | Explain in notes and seek vocabulary extension if recurring |
| `unknown` | Not established | Missing or conflicting data; **not** synonymous with no dimming |

TRIAC is not a synonym for all phase-cut dimming. A wireless lighting system or LV controller network may drive a separate driver using 0–10 V, PWM or another physical fixture input; record the *fixture-side interface*, not merely the upstream network name. CV/CC power regulation, driver/driverless architecture and AC/DC source voltage remain separate attributes.

## Recommended first-class fixture-schedule fields

- `fixture_type_id`, exact `source_mark` and `interface_basis` (`source` or `selected`).
- `dimming_interfaces[]` using the enumerated vocabulary; source alternatives are evidence, not a selection.
- `supported_dimming_schemes[]` — continuous, stepped, none or unknown as manufacturer-supported capability.
- `minimum_dim_percent` (minimum stable commanded level); `dim_to_off` (`true`/`false`/`null`). A fixture dimming to 1% does not necessarily turn completely off.
- `signal_mode` for analog 0–10/1–10 V (`sink`, `source`, `sink_or_source`, `not_applicable`, `unknown`).
- `driver_location` (`integral`, `remote`, `driverless`, `unknown`).
- `source_ref_ids[]` and `notes` preserving source schedule, datasheet, drivers, and variants.

**Additional useful properties for future device-level compatibility checks:** minimum/maximum electrical input and signal voltage; 0–10 V sink/source current capacity and control-channel fanout; phase-cut load type, minimum/maximum load and neutral requirement; PWM input voltage/frequency; DALI version/addressing and bus/power requirements; 0–100% command versus measured light-level curve, low-end stability, fade behavior, stepped level values; fixture/driver substitution, control-wire/power topology and emergency compatibility. Preserve these as manufacturer's stated numeric facts, not unsupported defaults. Do not add them as mandatory fields before actual device families require them.

## Design verification handoff

At M3 compare `dimming_scheme` to reviewed functional requirements. At M2 retain the **source fixture** interface; at M4 independently validate the **selected** fixture/driver interface, selected output controller/dimmer capability and signal/power constraints. A dimmable fixture in a `none` scheme is fine. A required continuous scheme cannot be implemented with a confirmed on/off-only interface; a stepped requirement may be implemented by a configurable continuous controller **only if tested/verified**, not inferred from the enum alone. A valid choice in an enum does not establish device-to-controller compatibility.

**Implementation:** [LV fixture interface companion](https://github.com/kissolutions/lv-lighting-design/blob/main/schemas/fixture-dimming-interface-v0.1.schema.json) and [M3 sequence schema v0.2](https://github.com/kissolutions/lv-lighting-design/blob/main/schemas/m3-sequence-assignments-v0.2.schema.json). The machine schemas validate data shapes and known choices; the engineering selection still needs evidence and functional verification.

Owner: KIS Solutions; October 2026.
