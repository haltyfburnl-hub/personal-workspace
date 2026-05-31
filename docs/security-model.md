# Privacy and Security Model

Personal Workspace is designed for AI-assisted research workflows that may touch sensitive personal, career, company, and interview material. The project keeps the public repository focused on reusable templates and synthetic examples while private work stays in ignored local folders.

## Data that may appear in real use

A real local workspace may contain:

- Company research notes and market observations.
- Job opportunity assessments and interview preparation notes.
- Personal career context, resumes, compensation expectations, and family constraints.
- Contracts, financial records, source screenshots, and private references.
- AI-generated drafts that may mix public facts with private interpretation.

These materials should not be committed to the public repository.

## Security boundaries

The repository uses these boundaries by default:

- `workspaces/` is ignored by Git, so generated local workspaces are private by default.
- `exports/`, `.env`, virtual environments, and Python caches are ignored.
- Public examples use synthetic companies and synthetic decisions.
- Templates separate `sources/`, `analysis/`, `drafts/`, and `final/` so users can review what is safe to share.
- The workspace creation script writes only local Markdown files and does not call external APIs.

## Main risks

The highest-risk failure modes are:

- A user accidentally commits private workspace files.
- A generated example includes real names, family details, financial data, API keys, or confidential company information.
- A path-handling bug writes files outside the intended workspace folder.
- AI-assisted drafts are shared before a human checks sources, assumptions, and privacy-sensitive details.

## Mitigations

The project mitigates these risks through:

- Privacy-first `.gitignore` defaults.
- Synthetic examples rather than real personal data.
- A `--dry-run` preview command to show planned folders and templates before writing files.
- A clear contribution guide and security policy.
- Tests for workspace type discovery and preview behavior.

## How Codex Security would help

Codex Security would be useful for this project because the repository sits at the boundary between AI-assisted work and private personal research. Useful checks include:

- Reviewing scripts for unsafe path handling before adding new file-generation features.
- Detecting accidental secrets or sensitive examples before publication.
- Checking pull requests that change template or export behavior.
- Reviewing future helpers that summarize, export, or transform workspace content.

## Maintainer review checklist

Before merging a change, maintainers should check:

- Does it create files only under the expected workspace or export path?
- Does it avoid committing private local workspaces?
- Are examples synthetic or anonymized?
- Are README, demo, and tests updated when user-facing behavior changes?
- Does the change keep source notes, analysis, drafts, and final outputs clearly separated?
