# Contributing

Thank you for considering a contribution to Personal Workspace.

This project is intentionally small and practical. Contributions should improve the clarity, repeatability, or usefulness of the workspace structure.

## Good contribution areas

- New reusable templates.
- Better workflow documentation.
- Safer privacy defaults.
- Small automation scripts with no heavy dependencies.
- Examples that do not expose private or confidential information.

## Guidelines

1. Keep examples generic and privacy-safe.
2. Prefer plain Markdown and standard Python.
3. Do not commit personal resumes, contracts, identity documents, financial files, or confidential company material.
4. Explain the use case clearly in the pull request.
5. Keep changes focused.

## Local check

For script changes, run:

```bash
python3 scripts/create_workspace.py "Example Company" --type company
```

The command should create a local folder under `workspaces/`. That folder is ignored by Git.