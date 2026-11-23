# P17. Project status log as a named framework document

- **Type:** Shared project-document requirement, template and convention.
- **Disposition:** Owner approved adoption as a shared framework requirement on 2026-11-22.
- **Observation:** A plant-controls pilot used successive dated status and handoff snapshots. No single record showed project progression from beginning to end; each snapshot restated standing rules and open items.
- **Requirement:** Every project using the framework maintains one stable `project-status-log.md`, records it alongside the other files in use, and includes the complete log in every project archive package.
- **Structure:** An editable Current state block lists applicable deliverable filenames/versions, architecture or approach, standing rules and open items. An append-only dated history below it runs oldest first to newest last, identifies changed files/versions and related IDs, and attributes decisions.
- **Update rule:** Save Current state and a dated entry after changing a deliverable or making a material decision. Capture the next action so another session can resume work from the project files.
- **Adoption:** Back-fill available earlier history from register change logs, deliverable change notes and handoff/status documents, retaining event dates, source references, reconstruction date and explicit gaps.
- **Authority:** Cite existing records rather than duplicating their contents. Register change logs remain authoritative for register edits; this document records project progression. Snapshot documents are inputs or dated extracts, not parallel maintained logs.
- **Storage:** Blank generic templates belong in the framework; populated project logs belong in approved project storage. Client-identifying pilot details are omitted here.
- **Owner clarification (2026-11-22):** The log is independent of PER and other domain/plugin documents. No dedicated link or link field is required. It is recorded with the project's files and travels with the archive package.
- **Format decision:** Standalone Markdown, with one stable filename and immutable copies in issued archives. No PER tab, template migration or domain plugin dependency.
- **Evidence / confidence:** Medium; initially supported by one pilot. The universal requirement follows the owner's direction; this does not claim validation across every domain.
- **Implementation:** [Standard](../project-status-log-standard.md), [template and instructions](../../templates/project-status-log/README.md), and the shared AI guide and architecture contract. Archive-package draft integration is maintained with the existing archive proposal.
