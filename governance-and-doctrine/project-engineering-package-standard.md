---
title: Project Engineering Package Standard
description: Portable engineering-state archive contract for SharePoint and Drive
published: false
date: 2026-10-15T00:00:00.000Z
tags: governance, archiving, schema
editor: markdown
dateCreated: 2026-10-15T00:00:00.000Z
---

# Project Engineering Package Standard (PEPS) — draft v0.1

A **Project Engineering Package** is a self-contained cold-storage snapshot of project engineering state, intended to survive loss of the originating agent conversation and to be read by later versions of the KIS framework.

## Required package files

```text
PROJECT_ID_PACKAGE_REV/
  manifest.json
  README.md
  canonical/                # accepted and provisional engineering records, stable IDs
  milestones/
    M1/
      current/
      previous/             # optional until first checkpoint
      accepted/             # optional until first acceptance
      state.json
  evidence/                 # drawings, applicable specifications, selected vendor documents
  artifacts/                # accepted spreadsheets, PDFs, narratives, markups
  release_records/          # receipts, inventory, validation report
```

For cold storage, omit transient scratch artifacts and superseded *unissued* submittal drafts. Retain superseded decisions, released documents, and any evidence needed to understand an accepted engineering conclusion. A source document can be stored once and referenced from multiple milestones.

The archive MUST NOT rely solely on changing SharePoint/Drive links for critical evidence. The official ZIP must be immutable after issuance. Drive and SharePoint copies should have identical SHA-256 checksums; designate one authoritative location to avoid conflicting edits.

## First-class data

Each meaningful engineering record needs stable identity, type, source provenance, approval status, evidence refs, and dependencies. Values accepted as project authority remain pinned independent of whether they were sourced or calculated.

Accepted derived results MUST retain their sizing/routing inputs and methodology reference; retaining a spreadsheet alone is insufficient. A future framework may run a comparison as a **proposed reassessment**, never overwrite accepted values during resume. Domain-specific objects (valves, controllers, cable routes, sequences, devices) belong in domain schemas, not in this universal package specification.

## Manifest minimum

See [package-manifest.schema.json](/governance-and-doctrine/package-manifest.schema.json) for a machine-readable draft. At minimum include:
- package ID, package revision, release status, creation date;
- schema ID/version and framework repository + immutable commit SHA;
- domain schema and spreadsheet template versions/hashes where applicable;
- milestone accepted baseline IDs and their pending exceptions;
- file inventory with paths and SHA-256 hashes;
- release validation status.

A null or missing commit/template version means **unknown**, not approved compatibility. Record what can be verified; do not fabricate version identifiers.

## Status and integrity

Package statuses: `working`, `review`, `issued`, `superseded`. Milestone acceptance does not automatically make the whole project package `issued`. An issued package's original ZIP is never edited in place; a later release receives a new package revision.

When importing into a newer framework:
1. Validate archive paths, file hashes, schema IDs, and schema versions.
2. Load accepted values in **resume mode** without recalculation.
3. Display open RFIs, provisional records, and revalidation triggers.
4. If migration is necessary, generate a new working package; preserve the original.
5. Any recalculation is a comparison, not automatic promotion to canonical state.

## Export and quality gate

Export should be a short milestone/release procedure: freeze current data; validate references; collect current canonical records and necessary evidence; write receipts and manifest; verify inventory hashes; build ZIP; cold-start test. Working snapshots use the two-state policy and do not need full ZIP exports after every change.

**Deferred for implementation:** archive-builder scripts, schema migrations, SharePoint/Drive synchronization, and GitHub release automation. This draft defines the contract only; it does not claim those capabilities already exist.

## Related governance

- [Engineering State and Milestone Acceptance](/governance-and-doctrine/engineering-state-and-acceptance)
- [Working-State Versioning](/governance-and-doctrine/working-state-versioning)
