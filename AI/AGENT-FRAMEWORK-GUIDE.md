---
title: AI Agent Framework Guide
description: Vendor- and domain-neutral instructions for how an AI agent should use this knowledge framework
published: true
date: 2026-09-26T00:00:00.000Z
tags: ai, governance, framework
editor: markdown
dateCreated: 2026-09-26T00:00:00.000Z
---

# AI Agent Framework Guide

Instructions for any AI agent working with this knowledgebase or with a domain extension built on it. Domain-specific instructions belong in the extension's own repository, not here.

## 1. Know What Kind of Page You Are Reading

Read `page_type` before using a page. Each type answers a different question and carries different authority:

| Type | Tells you | Use it as |
|---|---|---|
| Ontology (physical entity, functional construct, regulatory/classification) | What exists and how it is defined | Fact |
| Concept | How systems behave, what trades off | Explanation — never a standard |
| Constraint synthesis | The envelope of reality before deciding | Decision inputs, assumptions, RFIs |
| Playbook | What we do by default, when we branch | Prescriptive standard |
| Product type / class | What a product family implies and limits | Constraint source |
| Reference / deep-dive | Detail, edge cases, worked references | Supporting detail, subordinate to a parent page |
| Design | What happened on one project | Precedent — never a rule |
| Governance / template | How the knowledge system works | Rules for authoring and reasoning |

Extension page types declare a parent type from this table; treat them with the parent's authority unless the extension's registry says otherwise.

## 2. Retrieval

- Match `invocation_triggers` against the signals in the task (systems present, program signals, uncertainty flags).
- Follow `related_pages` upstream to confirm facts and downstream to find the applicable playbook.
- Prefer the most specific validated page; note when only draft pages exist.

## 3. Reasoning

- Use `decision_axes` to frame what must be decided.
- Treat every assumption as an object that can be invalidated. Check `invalidated_if` conditions against the source material.
- Apply consequence logic (if → then) rather than pattern-matching on similar-looking examples.

## 4. When Information Is Missing or Conflicting

- Do not silently invent requirements.
- State the gap or conflict, what it affects, and whether it is an engineering decision or an implementation decision.
- Express it as an RFI when a person outside the team must answer it.

## 5. Epistemic Hygiene

- Keep facts, assumptions, decisions and precedent separate in every output.
- Preserve traceability: say which page or source document each conclusion came from.
- Never treat a design page or worked example as a universal standard.

For drawing-derived spatial work, follow [Drawing-Based Spatial Extraction and Verification](../design-playbooks/drawing-spatial-extraction-v0.1.md): AI performs the initial extraction and rendered visual verification before human review. Combine visual meaning/completeness with PDF/coordinate precision; verify both geometric and object correspondence for cross-drawing transfers. On a spatial discrepancy, inspect the rendered area before another corrective data pass. Preserve accepted owner geometry and keep unresolved scope explicit. Domain playbooks own object/counting definitions, markup styles and milestone acceptance.

## 6. Writing Pages

- Start from the matching template; keep its section order and metadata.
- Put content on the page type whose question it answers. If it fits none, it probably belongs on a constraint-synthesis page until proven otherwise.
- Do not modify framework pages to make a domain task easier; propose a framework change instead (see [Framework Extension Doctrine](/governance-and-doctrine/framework-extension-doctrine)).

## 7. Public-repository data boundary

**This WikiJS source repository and publicly accessible domain extension repositories are reusable engineering knowledge, not project archives.** Never commit client names or client-identifying facilities, IP/MAC addresses, serial numbers, network diagrams, project drawings, contracts, pricing, credentials, private Drive/SharePoint links, photographs or verbatim client communications. Store real project records in its approved private project location. Publish only independently verified generic manufacturer facts, sanitized/anonymized examples and broadly applicable processes. Before committing a workbook or code-generated attachment, run the domain's blank-template or sensitive-data check; examine hidden sheets, cell notes, document metadata, comments and formulas as well as visible cells. If exposure is discovered, stop reuse and remediate both current files and historical public reachability; removing data only from the latest file does not erase repository history.
