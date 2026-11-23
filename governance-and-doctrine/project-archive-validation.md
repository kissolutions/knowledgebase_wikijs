# Project archive validation

Use this file inventory check before issuing or reissuing a KIS project archive. It applies to project ZIPs for interim or closeout storage across all domains. Domain deliverables such as bid PDFs, milestone review sets and workbook templates can be inputs to an archive. Their own release and review procedures still apply.

## Manifest contract

Use the [version 1.0.0 manifest schema](project-archive-manifest.schema.json). Place `manifest.json` at the ZIP root, or put it and all archive contents under one common wrapper folder. Inventory paths start at the directory containing the manifest and use forward slashes. List every regular file once, except `manifest.json` itself. Directory entries are optional. Use the exact file path and case as saved in the ZIP.

Record the package ID, revision, status, creation time in UTC and file inventory. For each file, record its path, role and lowercase SHA-256 checksum of its saved bytes. The archive inventory requires one `project-status-log.md` at the manifest level with role `documentation`. Use the complete saved project log from the package cutoff. See the [Project Status Log Standard](project-status-log-standard.md).

Framework references, source baselines and domain information can accompany the inventory as metadata. This check verifies inventory and file integrity. Engineering acceptance and milestone recovery have their own rules.

## Run before release

1. Stage the files selected for the archive in approved project storage. Review that the status log captures the package cutoff, dated history, open items and revisions of the included deliverables.
2. Write the manifest from those staged files and set the status for the intended release. Generate the lowercase SHA-256 values from the actual files you will include. PowerShell users can use `(Get-FileHash -Algorithm SHA256 -LiteralPath 'path/to/file').Hash.ToLowerInvariant()`.
3. Create the ZIP. Run the validator against the final ZIP in the approved environment using Python 3.11 or newer. Run the install command once in your Python environment.

   ```sh
   python -m pip install -r scripts/requirements-project-archive.txt
   python scripts/validate_project_archive.py /path/to/PROJECT_R01.zip
   ```

4. Use a passing result as the inventory gate before releasing the ZIP. An automated packager should stop if the command exits nonzero. If you change a staged file or the manifest, rebuild and validate the final ZIP again. Preserve an issued ZIP and assign a new revision for corrections.

The command reads the ZIP without extracting it. It checks the manifest structure and exact inventory, rejects duplicate or ambiguous paths, and recomputes each listed checksum from the archived bytes. A successful check confirms the file set and hashes. Keep the content review in step 1 to verify the engineering context and completeness of the project history.

Keep project archives and project-specific output in approved project storage. For earlier issued archives, retain the original ZIP and its original inventory convention. Apply this check when issuing a new archive under this schema.
