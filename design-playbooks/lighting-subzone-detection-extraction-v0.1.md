---
title: Lighting Subzone Detection and Extraction Process v0.1
page_type: playbook
page_status: draft
domain_primary: electrical-lighting
ai_role: prescriptive_standard
published: true
tags: [lighting, M3, subzones, daylight, owner-review]
editor: markdown
---

# Lighting Subzone Detection and Extraction Process v0.1

**Invocation:** M3, after reviewed Space classification and electrical-lighting-plan readiness, before endpoint SEQ/PSEQ selection. **Repeatable on demand:** a late daylight-zone determination, corrected source switch/circuit evidence, modified Light Points or owner instruction reopens **affected Spaces only**, independent of calendar/milestone timing. Preserve previously accepted revision as a baseline and show the delta. This process has two communicating discovery paths: **geometry/requirements-first** and **fixture/symbol-first**. Neither must finish before the other starts.

## Process B1 — Detect subzone candidates

Run a **fast, per-Space screen** using accepted room/Light Point geometry, source electrical lighting plan, original switch/circuit notation and independently reviewed code/daylight requirements.

| Flag | Observation | Evidence treatment |
|---|---|---|
| `SZ-01` | Multiple switch symbols near separate doorways | Typically potential 3-way/multiway controls; do **not** infer multiple zones solely from count. If adjacent door locations and labels corroborate one group, dismiss with evidence. |
| `SZ-02` | Two or more adjacent switch/dimmer symbols | Strong subzone cue; inspect legend, control letters and connected luminaires. |
| `SZ-03` | Multiple branch circuits/home runs entering the Space | Investigate; separate circuits do **not** prove separate control groups. |
| `SZ-04` | Matching lowercase/small letters on switch/dimmer and fixture labels (`a`, `x`) | Strongest usual source cue; correlate all matching luminaires and retain original source labels (which are **not** automatically the final alphabetical internal labels). |
| `SZ-05` | Keyed notes, legend, or detail expressly defines control groups | Source evidence of distinct behavior when applicable. |
| `SZ-06` | Applicable code, verified edition/exception, requires independent occupancy/control areas | **Derived**, not MEP-observed, subzone; record calculation, threshold/geometry/source. |
| `SZ-07` | Daylight boundary and affected luminaires require separately responding groups | **Derived**, not source-asserted; record independent daylight extent and affected Light Point IDs. |

Each detection finding has `confidence`: `LOW`, `MEDIUM`, `HIGH`, `VERIFIED`; `VERIFIED` is higher than `HIGH` and requires explicit corroborating evidence/owner confirmation. Store observed source or code evidence, rationale and `finding_status`: `confirmed`, `probable`, `ambiguous`, `dismissed`. Expose a focused owner/Teams meeting discussion report for **all unresolved findings below HIGH**; also show unresolved contradictions **even if HIGH**. Confidence is about strength of the *finding*, not automatic approval of a control sequence.

**Fast path:** If source detection flags are absent/dismissed **and** code and daylight screening establish no independent control requirement, classify the Space `single_zone_candidate`, and stop detailed subzone processing. A missing source control legend, unresolved code applicability or incomplete daylight screen is **not** a negative finding; use `source_review_required`. Subsequent daylight information can reopen fast-path Spaces.

## Process B2 — Extract and reconcile functional zones

1. Queue only flagged or reopened Spaces, with provenance `mep`, `code`, `daylight`, `owner` (multiple bases allowed). Discover by **either** boundary/requirement-first (e.g. daylight polygon or independently required control area) **or** luminaire/symbol-first (e.g. dual dimmers or switched letters). Reconcile both paths iteratively rather than imposing an ordering.
2. Build provisional endpoint groups; correlate every accepted M2 Light Point to one group where supported. Put unresolved Light Point assignments in a **scratch-only** `Unzoned` bucket. It is not a canonical `light_zone`, is never given a SEQ/PSEQ, and must be empty to accept the review.
3. Generate **one flat editable CSV** for all flagged Spaces, sorted by full Space name/room ID, lower-case sequential subzone labels `a`, `b`, `c` ... and stable Light Point ID. Include Space ID/full name, stable Light ID/display label, fixture type, internal zone ID, editable subzone label, observed source group, basis/evidence, confidence, proposed status, owner comment. Rows match by immutable IDs; CSV order is never authoritative.
4. Render a **separate additive subzone-label layer** over the existing accepted Light Point drawing: short lowercase letter adjacent to each existing Light Point, distinct editable markup object with stable ID, and append/update one structured subzone field in each Light Point annotation's comments; retain other comments and source drawings. Re-render from CSV after every reviewed edit. Do **not** use PDF graphical editing as a parallel source of zone ownership.
5. Owner reviews **CSV only** as the edit surface; the PDF is a derived verification/presentation product. Process CSV changes, check membership/no duplicates/valid labels and stable IDs, rebuild affected parent/leaf groupings, re-render the annotations, and present the complete revised package. Iterate as many times as needed. Preserve previous accepted IDs and geometry where possible; don't silently rewrite unrelated Spaces.
6. Accept the subzone register only after **every in-scope Light Point is assigned exactly once to a valid endpoint, Unzoned is empty, and any required code/daylight separation is resolved or expressly blocked**. Owner acceptance of memberships is **separate** from later sequence acceptance. Unknown fixture/interface facts remain honest gaps for M4 when unrelated to membership.

### Naming and identity

Lowercase `a` onward **per Space** is a display convention, not a globally unique ID or source-label claim. No lowercase label is needed for a genuinely single-zone Space. Stable zone IDs remain immutable; where owner changes only a display letter, preserve zone ID and update derived output. A cross-Space shared zone or multi-level control scheme is a separately reviewed exception; do not duplicate Light Objects.

### Daylight changes at any time

Daylight areas are **independent requirement/extent objects**, not ordinary parent/child lighting-zone nodes. A later `DL-` boundary discovery can affect lights in one or multiple Spaces. Record affected Space IDs, Light Point IDs, extent/basis (measured/asserted/unresolved), and applicable source/code constraints. Mark those Spaces `reprocess_required`; rerun B1/B2 only for impacted membership and sequence dependencies. On membership/subdivision changes invalidate **affected** accepted endpoint sequence assignments and request re-verification; do not silently relock M3. Existing independent controls can remain unchanged when new daylight evidence doesn't alter required response.

### Owner review and repeatability

Prepare two reports: (a) **candidate detection** with all flag evidence, sources and confidence, and (b) **editable per-light subzone CSV**. A subset report for below-HIGH or contradictory observations is suitable for owner walk-through over Teams. Owner can resolve flagged concerns without guessing full geometry or rewriting Light Point identifiers. Accepted register and additive label manifest are repeatable derived artifacts; neither changes original M1/M2 Light Point source identities.

**Implementation ownership:** Generic detection heuristics, code/daylight applicability and approval gates live in WikiJS. LV implementation owns per-project register/CSV import, stable ID reconciliation, PDF annotation schema/overlay and acceptance tests. Refer to [M3 lifecycle](m3-lighting-sequence-lifecycle-v0.1.md) and [sequence assignment contract](../ontology/lighting-sequence-assignment-contract-v0.1.md). An SVG example is a reusable graphic asset, not a substitute for a source plan or verified code-derived geometry.
