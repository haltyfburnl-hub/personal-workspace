# Personal Workspace

Personal Workspace is a lightweight open-source template for organizing AI-assisted research, career planning, company analysis, interview preparation, and reusable work documents.

The project solves a practical problem: AI-assisted personal research often becomes a mix of scattered notes, prompts, screenshots, private context, and final drafts. That makes the work hard to audit, hard to reuse, and risky to publish. Personal Workspace provides a repeatable folder structure, Markdown templates, and a small Python script so users can keep sources, analysis, drafts, and reviewed outputs separate.

## Why this project matters

AI tools can help people turn messy research into useful decisions, but the workflow needs clear boundaries. A good personal research workspace should make it obvious:

- which notes are raw sources;
- which judgments are still working analysis;
- which drafts were AI-assisted and need review;
- which final materials are safe to share;
- which folders must stay private and out of Git history.

This repository makes that workflow public, reusable, and reviewable. It is intentionally small, but it addresses a real recurring need: company research, role evaluation, interview preparation, and personal knowledge work where privacy and auditability matter.

## Current status

This is an early open-source project. The repository is public, licensed, documented, and includes a working script, templates, examples, contribution guidance, issue templates, tests, GitHub Actions, and a first release.

The project does not claim broad adoption yet. Its current value is that it turns a recurring AI-assisted research workflow into a public, inspectable, privacy-aware template that can be improved through issues and pull requests.

## What this project helps with

- Build a repeatable workspace for company and role research.
- Keep source notes, analysis, drafts, and final deliverables separated.
- Use AI tools such as Codex, ChatGPT, Gemini, NotebookLM, and other assistants with clearer context.
- Avoid mixing private personal data into public examples.
- Turn informal research into structured documents that can be reviewed and improved.
- Make AI-assisted output easier to audit before it is shared.
- Compare multiple companies or roles with explicit criteria and source-backed judgment.

## Repository structure

```text
personal-workspace/
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- workflows/
|-- docs/
|   |-- api-credit-use-plan.md
|   |-- demo.md
|   |-- project-statement.md
|   |-- security-model.md
|   `-- workflows/
|-- examples/
|   |-- company-comparison-example.md
|   |-- example-company-workspace.md
|   `-- privacy-safe-case-study.md
|-- scripts/
|   `-- create_workspace.py
|-- templates/
|-- tests/
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
|-- ROADMAP.md
`-- SECURITY.md
```

## Quick start

Clone the repository and inspect available workspace types:

```bash
git clone https://github.com/haltyfburnl-hub/personal-workspace.git
cd personal-workspace
python3 scripts/create_workspace.py --list-types
```

Preview a workspace without creating files:

```bash
python3 scripts/create_workspace.py "Example Company" --type company --dry-run
```

Create the workspace:

```bash
python3 scripts/create_workspace.py "Example Company" --type company
```

The script creates a local workspace folder under `workspaces/` and copies the relevant templates into it. The `workspaces/` folder is ignored by Git by default.

## Workspace types

List supported workspace types:

```bash
python3 scripts/create_workspace.py --list-types
```

Create a workspace:

```bash
python3 scripts/create_workspace.py "Example Company" --type company
python3 scripts/create_workspace.py "Example Role" --type job
python3 scripts/create_workspace.py "Example Interview" --type interview
```

Preview a workspace without writing files:

```bash
python3 scripts/create_workspace.py "Example Company" --type company --dry-run
```

## Included templates

- `templates/company-profile.md`: capture company facts, products, market position, risks, and open questions.
- `templates/company-comparison.md`: compare two or more companies or roles using explicit decision criteria.
- `templates/job-opportunity-review.md`: evaluate whether a role is worth pursuing.
- `templates/interview-prep.md`: prepare positioning, examples, likely questions, and closing notes.

## Examples and docs

- `docs/demo.md`: end-to-end walkthrough from command usage to generated workspace structure.
- `docs/security-model.md`: privacy and security boundaries for local AI-assisted research.
- `examples/example-company-workspace.md`: synthetic company workspace structure.
- `examples/company-comparison-example.md`: synthetic comparison between two opportunities.
- `examples/privacy-safe-case-study.md`: privacy-safe case study based on recurring research workflows.

## Example use cases

- Research a company before an interview.
- Compare whether a role is worth pursuing.
- Compare multiple companies before deciding where to spend preparation time.
- Prepare a structured interview note from multiple source documents.
- Build a repeatable personal knowledge base for work decisions.
- Keep AI-generated drafts auditable by separating sources, analysis, and final outputs.

## Testing

Run the standard-library test suite:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Maintenance

The project is maintained through:

- GitHub issues for bugs and template requests.
- Pull requests for visible review and change history.
- A public roadmap for planned improvements.
- A changelog for visible project history.
- A contribution guide for outside changes.
- A security policy focused on privacy-safe examples.

## Privacy note

This repository is a public template. Do not commit private resumes, family information, contracts, identity documents, financial files, API keys, or confidential company material.

Use `workspaces/` locally for private work. The folder is ignored by Git by default.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
