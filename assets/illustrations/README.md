# KIS Engineering Illustrations (Informative)

Illustrations in this directory are **non-normative** engineering education and onboarding aids, similar in authority to explanatory illustrations in the NEC Handbook. They do not add requirements or override an approved process, data contract, source drawing, or engineering decision. The governing written process/specification controls if interpretation differs.

## Space Boundary Markup

![Interior wall / room polygon example](space-boundary-markup-example.svg)

**Purpose:** Illustrate a small inward visual buffer from the room-side finished wall face, editable polygon vertices, ordinary doorway bridging, and preliminary light point containment. A visual buffer is **not** a reduction in the engineering area of a space. It must not redefine the architectural room boundary or override accepted owner-returned geometry. The source geometry and code-relevant area convention remain distinct.

**Related guidance:** [LV Architectural Space Intake](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/architectural-space-intake.md) and KIS [Physical Boundary Intake](../../design-playbooks/physical-boundary-intake-v0.1.md). The illustrated Space polygon is not itself a Physical Boundary Register entry.

## Historical Clockwise Fixture ID Example — Superseded

> **NOT CURRENT PRACTICE.** The figure below records a prior proposed fixture-type/clockwise numbering method, now superseded for LV Lighting M1 and M2. **Do not use it for new takeoffs, human review labels or training as the active convention.**

![Superseded light numbering by type within Room 105](light-ids-clockwise-room-example.svg)

**Current practice:** M1 establishes owner-approved room-local Light Point labels **top-to-bottom by row, left-to-right within each row**, regardless of fixture type. M2 uses and preserves those labels while reconciling physical fixtures and source schedule types; it does not renumber by type or clockwise ring. Immutable Light Object IDs and source-observation IDs remain separate.

**Governing instructions:** [Phase 1 Intake Process Map](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/phase-1-intake-process-map-v0.1.md) and [M2 Approved Light Point Identity and Fixture Scheduling](https://github.com/kissolutions/lv-lighting-design/blob/main/docs/design-playbooks/m2-fixture-numbering.md). The historical illustration is retained to document the superseded proposal and must be replaced for active training use.

## Maintenance conventions

- Mark diagrams **INFORMATIVE**, **Training**, or **Conceptual Example**; never present as design approval or code source.
- Keep each diagram near the named process/schema it explains, with links in both directions when useful.
- Review diagrams when underlying process/schema conventions change.
- Drawn names, fixture counts, room geometry, scales and products are explanatory placeholders unless a real project source is cited explicitly.

**Format:** SVG is the repository-native image format here: scalable, diffable, and directly rendered by Markdown/GitHub. These are faithful conceptual vector renditions of the two figures developed during the M1 discussion, rather than binary copies of the originally generated PNGs.
