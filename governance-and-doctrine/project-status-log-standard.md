---
title: Project Status Log Standard
description: Required project document for current state and continuous project history
published: true
date: 2026-11-22T00:00:00.000Z
tags: governance, project-documents, status, archiving
editor: markdown
dateCreated: 2026-11-22T00:00:00.000Z
---

# Project Status Log Standard

**Framework requirement P17:** Every project using the KIS Knowledge Model must maintain one **Project Status Log**. This is a shared project document, independent of the project's engineering domain, plugins, registers and deliverable formats. Record it in the project's file inventory alongside the other files in use. No dedicated link field in a PER or another domain document is required.

Use the [blank log](../templates/project-status-log/PROJECT_STATUS_LOG_TEMPLATE.md) and its [instructions](../templates/project-status-log/README.md). Store the project copy as `project-status-log.md` in approved project storage. Keep the same file throughout the project; do not replace it with successive dated status documents. File version history and immutable archive copies preserve earlier states without becoming parallel working logs.

## 1. Current state

Maintain a concise **Current state** block at the top and overwrite it as the project evolves. Include:

- The as-of date, project phase/milestone and responsible maintainer.
- Every current deliverable's filename, revision/version and project-relative location. Distinguish the latest working revision from the latest issued or accepted revision when they differ. Mark unknown or not-yet-created items explicitly.
- A short architecture or approach summary appropriate to the project.
- Standing project rules, owner directives and protected decisions, with their source references.
- Open items, next actions and responsible parties, citing existing register IDs when available.

Deliverables may include an equipment/device/points workbook, engineering register, BOM, basis of design, drawings, calculations or other domain outputs. No particular domain deliverable or register is a prerequisite for maintaining the log. Use `not applicable` where a section does not apply; do not invent architecture or records to fill the template.

## 2. Continuous history

Below Current state, maintain an **append-only dated log**, oldest entry first and newest last. During active work, add an entry for each working day or material decision. Every session that changes a deliverable must update Current state and append an entry before handoff; multiple sessions on one day may have separate entries. Every deliverable revision must be accounted for.

Each entry identifies its recording date (and timezone if a time is used), the event date if different, what changed and why, affected filenames and versions, related record IDs or source locators, and who made any decision. Distinguish the author recording an event from the person authorized to decide; agent-generated work is not human approval. State unknown attribution explicitly. Record material decisions and open-item dispositions even when no file is uprevved.

Preserve earlier entries. Correct mistakes through a new dated correction referring to the earlier entry. On resuming a project, read Current state and relevant history, then confirm the listed source files and revisions before relying on the summary. A discrepancy must be reconciled and recorded rather than silently resolved in favor of the log.

## 3. Authority and adoption during a project

The log is authoritative for the maintained project progression narrative. It summarizes and cites engineering records; it does not replace their authority. Where a project uses a PER, cite its RFI-, ISS-, REC- or CHG- IDs as applicable. The PER CHANGE LOG remains authoritative for PER edits. Other domains retain their own register and revision rules. The log neither grants acceptance nor reopens protected decisions.

When adopting the log mid-project, reconstruct available earlier history from register change logs, deliverable change notes and dated handoff/status documents. Place reconstructed events in chronological order before starting the continuing append-only record. Identify them as back-filled, retain the original event dates separately from the reconstruction date, and cite the source files and versions. Mark gaps, uncertainty and conflicting evidence; do not invent a complete history. After adoption, order new entries by recording date. History discovered later is appended as a newly recorded back-fill entry with the earlier event date identified; do not insert it into or rewrite the established history.

Existing handoff and as-built status snapshots are source inputs. Future handoffs use the maintained log; any separately required snapshot is a dated view or extract of it, with its source as-of date, rather than a parallel maintained status record. Retain previously issued documents as evidence.

## 4. Project files and archive packages

The log must be present in the project's working file set and file inventory from initialization, or from adoption on an existing project. This requirement applies to all framework projects, including those with no PER or domain plugin. Do not require a special link from another document.

Every project archive package, including interim archives and closeout, must contain the complete `project-status-log.md` as of the package cutoff, with both Current state and the full history. A summary-only export or an external link is insufficient. Include it in the package inventory and record its revision or SHA-256 hash using the package's existing inventory convention. Preserve issued archive copies immutably; later updates belong in the working log and a new archive revision.

Before archiving, verify that the log's listed deliverable versions agree with the packaged files and that open items remain explicit. Identify externally retained or excluded items and their disposition; do not imply they are included. Retain the source evidence needed to interpret decisions. A missing log, missing history or unexplained version mismatch fails the package completeness check. These are requirements for preparation and review; they do not imply an archive builder already exists.

## 5. Repository boundary

Only blank templates, generic conventions and sanitized examples belong in the public framework repository. Keep populated logs and their project files in approved project storage. Do not copy client-identifying pilot content into the reusable template or proposal record.
