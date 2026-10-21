---
title: Working-State Versioning
description: Two-state rolling recovery for unaccepted milestones
published: false
date: 2026-10-15T00:00:00.000Z
tags: governance, milestones, versioning
editor: markdown
dateCreated: 2026-10-15T00:00:00.000Z
---

# Working-State Versioning (draft v0.1)

**Keep only `current/` and `previous/` as editable milestone states.** An immutable `accepted/` baseline is created at milestone acceptance. This is deliberately not a full history or a Git-style chain of engineering iterations.

```text
Milestone_M4/
  current/        # active engineering records
  previous/       # one recoverable copy; replaced by next checkpoint
  accepted/       # absent until milestone acceptance; never overwritten
  state.json      # schema/commit references and concise last-change note
```

## Trigger and retention

Before a **substantial** recalculation, bulk extraction correction, routing optimization, controller relocation, channel reassignment, or other operation that could overwrite useful derived work:

1. Validate that `current/` is a complete, readable state.
2. Atomically replace `previous/` with a consistent copy of `current/`, including data model and metadata needed to reconstruct it. Do this **before** any mutation.
3. Apply the modification to `current/`, ideally through a staging location and atomic replacement.
4. Validate references and record a brief what-changed summary in `state.json`.

Routine prose edits do not require checkpoints. Repeated transformations **will overwrite** the single previous copy; if the owner identifies an especially valuable proposal, accept it or explicitly export it as a named package artifact before the next substantial revision.

The working directory need not duplicate unchanged source drawings or data sheets. Retain stable source references and source-file hashes; store evidence once at the project package level.

## Undo and redo semantics

`Undo last revision` should **swap** the current and previous working states after verifying both are valid, preserving the displaced current state as the new previous. A second undo toggles back (redo), unless intervening work takes another checkpoint. Never destructively replace the only recovery copy during an undo.

`Restore previous controller locations only` creates a new `current/` combining the selected prior attributes and still-valid present attributes. Save the complete pre-restore current state in `previous/` first, and report dependencies and conflicts. Accepted fields cannot be overwritten by either restore operation.

## Acceptance and reopening

On `Accept M4`, take a stable accepted baseline containing only approved values and their provenance, along with an acceptance receipt and exception list. This baseline must be immutable, versioned and included in the release package; it is **not** a third rotating work copy.

On `Reopen M4`, initialize a working revision from the accepted baseline while leaving that baseline intact. Never delete an earlier issued accepted baseline; any later accepted revision gets a new baseline ID (e.g. M4-A002) in release records, even though only the latest working/previous pair is kept.

Do not assume an accepted baseline exists for every active milestone. The `accepted/` directory may be absent before initial acceptance.

## Minimal state.json

```json
{
  "working_state_schema_version": "0.1.0",
  "milestone_id": "M4",
  "state_status": "provisional",
  "current_revision": 2,
  "previous_revision": 1,
  "last_change_summary": "Revised controller locations and associated routes",
  "project_schema_version": null,
  "framework_commit": null,
  "updated_at": null
}
```

The JSON is an example; populate timestamps, commit hashes, and schema versions when known. No agent should claim a snapshot has been made unless a real storage write succeeds.

## Minimum operational tests

- Failed recalculation leaves a usable `previous/`.
- Undo swaps states without losing either result.
- Targeted restore changes specified attributes only and reports affected dependencies.
- Accepted fields remain unchanged through optimization, undo, and restore.
- A cold-start agent reconstructs `current/`, `previous/`, and accepted exceptions without the original chat.
