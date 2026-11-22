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
  project-status-log.md     # complete Current state and continuous dated history
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

## Required Project Status Log (P17)

Every framework project maintains one `project-status-log.md`, independent of any PER, engineering domain or plugin. Record it alongside the other project files in use. Every archive package, including interim packages and closeout, MUST include the complete log as of its cutoff, with both the editable Current state block and the full append-only dated history. An external link, a summary-only export or a new standalone handoff snapshot does not satisfy this requirement. No dedicated link field in another project document is required.

Before packaging, update Current state and append the latest changes/decisions, then reconcile the listed deliverable filenames and versions with the packaged files. Keep open items and externally retained or excluded deliverables explicit. Include the log in `manifest.json`'s `files` inventory at path `project-status-log.md`, role `documentation`, with its SHA-256 hash. The manifest schema checks this inventory entry; file presence, history and consistency still require package review. A missing log or unexplained version mismatch fails the archive completeness gate.

The package contains an immutable copy; the single working log continues in project storage. Retain the issued package unchanged and create a new package revision for later updates. The parent [Project Status Log Standard](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/governance-and-doctrine/project-status-log-standard.md) and [template](https://github.com/kissolutions/knowledgebase_wikijs/tree/main/templates/project-status-log) govern maintenance, mid-project back-fill and source authority.

## First-class data

Each meaningful engineering record needs stable identity, type, source provenance, approval status, evidence refs, and dependencies. Values accepted as project authority remain pinned independent of whether they were sourced or calculated.

Accepted derived results MUST retain their sizing/routing inputs and methodology reference; retaining a spreadsheet alone is insufficient. A future framework may run a comparison as a **proposed reassessment**, never overwrite accepted values during resume. Domain-specific objects (valves, controllers, cable routes, sequences, devices) belong in domain schemas, not in this universal package specification.

## Manifest minimum

See [package-manifest.schema.json](/governance-and-doctrine/package-manifest.schema.json) for a machine-readable draft. At minimum include:
- package ID, package revision, release status, creation date;
- schema ID/version and framework repository + immutable commit SHA;
- domain schema and spreadsheet template versions/hashes where applicable;
- milestone accepted baseline IDs and their pending exceptions;
- file inventory with paths and SHA-256 hashes, including the required complete `project-status-log.md`;
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

Export should be a short milestone/release procedure: update and reconcile the Project Status Log; freeze current data; validate references; collect current canonical records, the complete log and necessary evidence; write receipts and manifest; verify inventory hashes; build ZIP; cold-start test. Working snapshots use the two-state policy and do not need full ZIP exports after every change. A cold-start review must recover current file versions, project progression and open items from the package without the original conversation.

**Deferred for implementation:** archive-builder scripts, schema migrations, SharePoint/Drive synchronization, and GitHub release automation. This draft defines the contract only; it does not claim those capabilities already exist.

## Related governance

- [Engineering State and Milestone Acceptance](/governance-and-doctrine/engineering-state-and-acceptance)
- [Working-State Versioning](/governance-and-doctrine/working-state-versioning)
