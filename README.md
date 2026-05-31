# Personal Workspace

Personal Workspace is a lightweight open-source template for organizing AI-assisted research, career planning, company analysis, and reusable work documents.

The project is designed for people who need a clear, repeatable workspace instead of scattered notes, screenshots, and one-off prompts. It provides a practical folder structure, reusable Markdown templates, and a small Python script that can create a clean workspace for a new company, role, project, or personal research topic.

## Current status

This is an early open-source project. The repository is public, licensed, documented, and includes a working script, templates, examples, contribution guidance, issue templates, and tests.

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
|   |-- project-statement.md
|   `-- workflows/
|-- examples/
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

Clone the repository and create a new workspace:

```bash
git clone https://github.com/haltyfburnl-hub/personal-workspace.git
cd personal-workspace
python3 scripts/create_workspace.py "Example Company" --type company
```

The script creates a local workspace folder under `workspaces/` and copies the relevant templates into it.

## Workspace types

```bash
python3 scripts/create_workspace.py "Example Company" --type company
python3 scripts/create_workspace.py "Example Role" --type job
python3 scripts/create_workspace.py "Example Interview" --type interview
```

## Included templates

- `templates/company-profile.md`: capture company facts, products, market position, risks, and open questions.
- `templates/company-comparison.md`: compare two or more companies or roles using explicit decision criteria.
- `templates/job-opportunity-review.md`: evaluate whether a role is worth pursuing.
- `templates/interview-prep.md`: prepare positioning, examples, likely questions, and closing notes.

## Examples

- `examples/example-company-workspace.md`: synthetic company workspace structure.
- `examples/company-comparison-example.md`: synthetic comparison between two opportunities.

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
- A public roadmap for planned improvements.
- A changelog for visible project history.
- A contribution guide for outside changes.
- A security policy focused on privacy-safe examples.

## Privacy note

This repository is a public template. Do not commit private resumes, family information, contracts, identity documents, financial files, API keys, or confidential company material.

Use `workspaces/` locally for private work. The folder is ignored by Git by default.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).