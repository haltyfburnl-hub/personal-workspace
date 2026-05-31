# Personal Workspace

Personal Workspace is a lightweight open-source template for organizing AI-assisted research, career planning, company analysis, and reusable work documents.

The project is designed for people who need a clear, repeatable workspace instead of scattered notes, screenshots, and one-off prompts. It provides a practical folder structure, reusable Markdown templates, and a small setup script that can create a clean workspace for a new company, role, project, or personal research topic.

## What this project helps with

- Build a repeatable workspace for company and role research.
- Keep source notes, analysis, drafts, and final deliverables separated.
- Use AI tools such as Codex, ChatGPT, Gemini, NotebookLM, and other assistants with clearer context.
- Avoid mixing private personal data into public examples.
- Turn informal research into structured documents that can be reviewed and improved.

## Repository structure

```text
personal-workspace/
├── docs/
│   ├── project-statement.md
│   └── workflows/
│       ├── company-research.md
│       └── job-opportunity-review.md
├── scripts/
│   └── create_workspace.py
├── templates/
│   ├── company-profile.md
│   ├── interview-prep.md
│   └── job-opportunity-review.md
├── .gitignore
├── LICENSE
└── README.md
```

## Quick start

Clone the repository and create a new workspace:

```bash
git clone https://github.com/haltyfburnl-hub/personal-workspace.git
cd personal-workspace
python3 scripts/create_workspace.py "Example Company" --type company
```

The script creates a workspace folder under `workspaces/` and copies the relevant templates into it.

## Example use cases

- Research a company before an interview.
- Compare whether a role is worth pursuing.
- Prepare a structured interview note from multiple source documents.
- Build a repeatable personal knowledge base for work decisions.
- Keep AI-generated drafts auditable by separating sources, analysis, and final outputs.

## Privacy note

This repository is a public template. Do not commit private resumes, family information, contracts, identity documents, financial files, or confidential company material.

Use `workspaces/` locally for private work. The folder is ignored by Git by default.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).