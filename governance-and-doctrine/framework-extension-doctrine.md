---
title: Framework Extension Doctrine
description: Rules for domain knowledgebases that adopt the KIS framework and extend it with their own page types
published: true
date: 2026-09-26T00:00:00.000Z
tags: governance, doctrine, framework
editor: markdown
dateCreated: 2026-09-26T00:00:00.000Z
---

# Framework Extension Doctrine

## 1. Purpose

This wiki is two things at once:

1. **A framework** — the page taxonomy, metadata layer, templates, reasoning scaffold and vocabulary described in [Knowledge Model Map](/governance-and-doctrine/map-knowledge-model-structure) and [Definitions](/governance-and-doctrine/definitions).
2. **A content base** — pages written with that framework.

Other repositories may adopt the framework to build a **domain extension**: a knowledge base for a narrower purpose (for example, one that produces a specific deliverable). This page defines how an extension relates to the parent framework.

---

## 2. Authority

| Concern | Authority |
|---|---|
| Page taxonomy, metadata conventions, templates, reasoning model, framework vocabulary | **This wiki** |
| Physical entity (device) pages | **This wiki** |
| Domain content, domain vocabulary, domain settings and conventions | **The extension** |
| Page types that exist only to serve the extension's deliverable | **The extension**, registered as below |

An extension never edits this wiki's content to suit its own implementation. If the framework is insufficient, the fix is a framework change here (a new generic template or doctrine rule), not a local workaround.

---

## 3. Structure Follows Knowledge, Not Workflow

Folder and page structure organizes **domains of knowledge and system data**, following the framework's layers (ontology → concepts → constraint synthesis → playbooks, with reference, design and governance pages alongside).

**Workflow is encoded in playbooks**, not in folder order. A document tree numbered by process step couples knowledge to one workflow and breaks when the workflow changes.

---

## 4. Rules for Extension Page Types

An extension may add page types that the parent framework does not have. Each one must:

1. **Declare a parent type.** Every extension type specializes one framework type (e.g., a copy-ready implementation module specializes *reference* or *playbook*). This keeps retrieval and reasoning behavior predictable.
2. **Be registered.** The extension keeps a page-type registry listing each type, its parent, its template, and its intended AI role.
3. **Carry the framework metadata.** `page_type`, `page_status`, `confidence_level`, `ai_role`, `invocation_triggers`, `decision_axes` and `related_pages` keep their framework meanings. Extensions may add fields; they may not redefine existing ones.
4. **Preserve the separation of knowledge roles.** An extension type must still make clear whether it states what is true, what is assumed, what must be decided, what can be reused, or what is project-specific.

A type that proves useful beyond one extension should be generalized and promoted into this wiki's templates.

---

## 5. Linking Across the Boundary

- Extensions link **to** this wiki for framework rules and device facts; they do not copy them.
- Device-level facts (I/O, ratings, physical limits) stay on the wiki's physical entity pages. An extension page that depends on them links to the device page and records only how the extension uses the device.

---

## 6. Status and Stewardship

- **Status:** Draft  
- **Last Review:** 2026-09  
- **Owner:** KIS Solutions
