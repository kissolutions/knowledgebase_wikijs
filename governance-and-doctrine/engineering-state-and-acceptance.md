---
title: Engineering State and Milestone Acceptance
description: Framework-wide governance of provisional, accepted, and reopened project engineering data
published: false
date: 2026-10-15T00:00:00.000Z
tags: governance, engineering-state, milestones
editor: markdown
dateCreated: 2026-10-15T00:00:00.000Z
---

# Engineering State and Milestone Acceptance (draft v0.1)

Applies to all KIS design domains, including BAS and LV lighting. A design agent must preserve engineering decisions across independent runs and framework upgrades. Project-specific records belong in a project package, not in this reusable knowledge repository.

## Core principle

**Derived -> accepted -> canonical.** A computed, inferred, optimized, or agent-generated result is a *candidate*, not a durable authority. Explicit acceptance promotes its approved attributes and relationships into canonical project engineering state. Once accepted, that state becomes a constraint on downstream work, not an invitation to independently solve the same question again.

"Canonical" denotes *project approval status*, not source provenance. A source-extracted fact can be provisional if ambiguous; a derived cable route can be canonical when accepted. Keep provenance and approval status as separate fields.

## States

- **Provisional:** Working fact, assumption, or derived candidate. May be revised, subject to working snapshot rules.
- **Accepted:** Approved attributes and relationships pinned to a milestone baseline.
- **Revalidation required:** Accepted data whose supporting assumption, source, or dependency has changed. Maintain the existing accepted value pending review; do not auto-replace.
- **Superseded:** Former accepted value replaced by a later accepted revision; preserve the decision trail.
- **Rejected:** Candidate expressly excluded, with reason.

An open RFI, contradiction, unsupported inference, or explicit hold is not promoted by default bulk acceptance.

## Standard commands

- `Accept M1 canonical. Flag derived information and present the exceptions list.` — accept eligible, verified source-based candidates and previously approved decisions only.
- `Accept M1 including derived, excluding unresolved/conflicting items.` — accept eligible derived design results as part of the specified milestone, with exceptions.
- `Accept M1 except [IDs].` — accept the eligible milestone content but withhold named attributes/objects.
- `Reopen [object.attribute or milestone] — reason: ...` — create a controlled working revision while keeping the accepted baseline intact.
- `Show changes since last snapshot.` and `Undo last revision.` — working-state maintenance (see working-state policy).

No silence-as-consent: only an explicit approval instruction promotes data.

## Milestone closeout procedure

1. Identify in-scope object IDs and attributes; classify each by provenance, evidence, approval and unresolved dependencies.
2. Present a **short receipt**: included count, excluded count, exception IDs with reasons, and high-consequence derived decisions. Avoid item-by-item confirmation of uncontroversial records.
3. Apply the owner's bulk acceptance directive atomically to eligible attributes and relationships; never expand the approved scope beyond the directive.
4. Create the immutable accepted milestone baseline and machine-readable acceptance receipt. Include source references, authority, timestamps, schema version, and framework commit if known.
5. Carry exceptions forward as provisional records with stable IDs; a milestone may be **accepted with exceptions**. Downstream tasks must respect unresolved dependencies.

Acceptance granularity is the smallest meaningful attribute or object group needed to avoid reopening an entire milestone. E.g. accept controller location without implicitly accepting its cable route, or accept valve Cv without approving actuator fail position.

## Reopening and impact analysis

A reopened accepted attribute creates a new provisional working value. Retain the original accepted value, the reason, and a link to affected dependencies. Proposed replacements do not become canonical until separately accepted. Changes in source drawings, calculation method, or framework version may flag **revalidation required** but shall not silently trigger regeneration or substitution of accepted outputs.

Example: an accepted LV lighting controller room/location constrains future cable routing. A later optimizer must route from that location, not relocate it. If the room boundary changes, flag the location for review. Example: a selected valve Cv may be accepted while actuator fail position remains open.

## Minimum acceptance receipt

```json
{
  "receipt_schema_version": "0.1.0",
  "milestone_id": "M4",
  "baseline_id": "M4-A001",
  "directive": "Accept M4 except CIO-03.route",
  "authority": "owner",
  "accepted_record_refs": ["CIO-03.location"],
  "excluded": [{"ref": "CIO-03.route", "reason": "unresolved routing"}],
  "source_snapshot_id": "M4-current",
  "accepted_at": null,
  "framework_commit": null
}
```

The example is illustrative. Real acceptance receipts require an actual timestamp and stable references.

## Related rules

- [Working-State Versioning](/governance-and-doctrine/working-state-versioning)
- [Project Engineering Package Standard](/governance-and-doctrine/project-engineering-package-standard)
- [AI Agent Framework Guide](/AI/AGENT-FRAMEWORK-GUIDE)
