---
title: Definitions
description: definitions of words that pertain to this knowledge model
published: true
date: 2026-03-02T00:54:21.953Z
tags: definitions
editor: markdown
dateCreated: 2026-03-01T16:25:25.552Z
---

# KIS Knowledge System — Systems Engineering & Knowledge Model Glossary

This glossary defines the academic and systems-engineering terms used in the development of KIS Design Playbooks and supporting knowledge layers.

This vocabulary supports:

- Hardware Fundamentals  
- Interior Space Type Definitions  
- Design Playbooks  
- Control Ecosystem Decisions  
- Code Interpretation  
- Knowledge Governance  

---

# I. Knowledge Structure Terms

## Declarative Knowledge
**“What is.”**  
Factual, descriptive, classification-based knowledge.

Examples:
- Interior Space Types page  
- Hardware Fundamentals pages  
- Code classification explanations  

---

## Procedural Knowledge
**“How to.”**  
Stepwise or decision-based guidance.

Examples:
- Design Playbooks  
- Decision Gates  
- Baseline design patterns  

---

## Contextual Knowledge
Knowledge that depends on environment, constraints, or delivery model.

Examples:
- Value engineering pressure  
- Limited construction administration  
- Contractor substitution behavior  

---

## Prescriptive
Directs action. Tells the reader what to do.

Design Playbooks are prescriptive.

---

## Descriptive
Explains without directing action.

Space Type pages are descriptive.

---

## Normative
Defines required behavior, usually driven by code.

Energy code requirements are normative.

---

# II. Systems Engineering Terms

## System
A set of interacting components forming a coherent whole.

Example:
Lighting + sensors + controls + receptacles = a room-level system.

---

## Subsystem
A functional unit within a larger system.

Examples:
- Occupancy sensing subsystem  
- Daylight control subsystem  
- Receptacle control subsystem  

---

## Interface
The point of interaction between systems.

Examples:
- Lighting controls ↔ receptacle controls  
- Lighting controls ↔ HVAC occupancy input  

---

## Integration
Ensuring multiple subsystems operate coherently.

Example:
One occupancy sensor driving lighting and receptacles.

---

## Architecture
The structural arrangement of system components.

Examples:
- Line-voltage sensor architecture  
- Low-voltage sensor + power pack architecture  
- Room-based control ecosystem  

---

## Ecosystem
A coordinated family of components designed to work together reliably.

Examples:
- Lutron room-based systems  
- Wattstopper DLM  
- Unified lighting + receptacle control platforms  

---

## Robustness
Ability of a design to survive change without failure.

Examples:
- Survives value engineering  
- Remains code-compliant after layout changes  

---

## Fragility
A design that technically complies but fails under normal project pressures.

---

# III. Knowledge Modeling Terms

## Ontology
A structured definition of categories and relationships.

Example:
Interior Space Types defining Open Office vs Enclosed Office.

Ontology defines meaning and relationships.

---

## Taxonomy
A classification hierarchy.

Example:

Interior Spaces  
├── Office  
│   ├── Enclosed Office  
│   └── Open Office  
├── Assembly  
└── Circulation  

Taxonomy organizes categories.

---

## Abstraction
Describing something at a higher level while hiding detail.

Example:
“Open Office” instead of describing furniture layout and window spacing.

---

## Granularity
Level of detail.

Too granular:
- Explaining PIR sensor physics in a playbook.

Too coarse:
- “Provide lighting controls per code.”

---

## Layered Knowledge Architecture
A structured separation of knowledge types.

KIS Model Layers:

1. Hardware Fundamentals — components  
2. Space Type Definitions — classification  
3. Design Playbooks — procedural decisions  
4. Project Documents — implementation artifacts  

---

## Separation of Concerns
Keeping different types of logic in separate layers.

Example:
Do not define space classification inside a lighting playbook.

---

## Encapsulation
Hiding complexity behind a simplified interface.

Example:
Playbook references a baseline without repeating hardware theory.

---

# IV. Decision System Terms

## Baseline
Default design pattern used unless a decision gate triggers deviation.

---

## Variant
A named, repeatable deviation from the baseline.

---

## Decision Gate
A binary condition that forces branching.

Example:
Is Automatic Receptacle Control required?  
Yes → Change control architecture  
No → Remain baseline  

Decision gates are the core intelligence of playbooks.

---

## Constraint Envelope
The full set of constraints governing a design.

Includes:
- Hard constraints  
- Soft constraints  
- Hidden constraints  

---

## Hard Constraints
Non-negotiable requirements (typically code-driven).

---

## Soft Constraints
Budget, owner preferences, schedule.

---

## Hidden Constraints
Unwritten but real forces affecting outcomes.

Examples:
- Value engineering pressure  
- Contractor substitutions  
- No construction administration  

---

## Escalation Trigger
A condition that invalidates the baseline and requires a project-specific design approach.

---

## Failure Mode
A predictable way a system fails.

Categories:
- Design-time failures  
- Documentation failures  
- Operational failures  

---

# V. Engineering Reasoning Terms

## Institutional Knowledge
Experience-based patterns encoded into standards or playbooks.

Example:
Lighting and receptacle controls should share a common ecosystem.

---

## Heuristic
A rule of thumb.

Example:
Default to line-voltage sensors unless ARC requires ecosystem-level control.

---

## Defensive Design
Designing for real-world project conditions, not ideal ones.

---

## First-Order Effect
Direct requirement.

Example:
Occupancy sensor required by code.

---

## Second-Order Effect
Indirect consequence of a requirement.

Example:
ARC requirement forces change in control architecture.

---

# VI. Code Interpretation Terms

## Explicit Requirement
Directly stated in code.

---

## Implicit Condition
Emerges from thresholds and classifications but not explicitly named.

Example:
“Open Office” is an implicit classification.

---

## Jurisdictional Adoption
The specific code edition legally in force.

---

## Most Stringent Governs
When multiple codes apply, the strictest requirement controls design.

---

# VII. Governance and Scaling Terms

## Decision System
A structured, constraint-driven framework for making repeatable design decisions.

---

## Governance
Rules that keep playbooks consistent and disciplined.

Examples:
- One primary decision per playbook  
- Baseline must be defensible  
- Variants must be limited and named  

---

## Scalability
Ability to apply the same framework across domains:
- Lighting  
- HVAC  
- Power  
- Industrial controls  

---

## Cognitive Load Reduction
Primary purpose of playbooks:
- Eliminate blank-page design paralysis  
- Reduce unnecessary option evaluation  

---

# Summary

The KIS Knowledge System consists of:

- An ontology (space definitions)  
- A taxonomy (organized structure)  
- A layered knowledge architecture  
- A decision-gate-driven procedural system  
- Governance rules that preserve consistency  

This framework transforms documentation into a structured engineering decision system.