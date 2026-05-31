# End-to-End Demo

This demo shows the complete privacy-safe workflow: inspect available workspace types, preview the generated structure, create a local workspace, fill templates, and keep private materials out of Git.

## 1. List available workspace types

```bash
python3 scripts/create_workspace.py --list-types
```

Expected output:

```text
company: company-profile.md, job-opportunity-review.md, interview-prep.md
interview: interview-prep.md
job: job-opportunity-review.md, interview-prep.md
```

## 2. Preview before creating files

Use `--dry-run` when you want to verify the generated structure before writing anything locally.

```bash
python3 scripts/create_workspace.py "Example Company" --type company --dry-run
```

Expected output:

```text
Workspace: workspaces/example-company
Type: company

Folders:
- sources/
- analysis/
- drafts/
- final/

Templates:
- company-profile.md
- job-opportunity-review.md
- interview-prep.md
```

## 3. Create the workspace

```bash
python3 scripts/create_workspace.py "Example Company" --type company
```

Expected output:

```text
Created workspace: workspaces/example-company
```

The generated workspace looks like this:

```text
workspaces/example-company/
|-- README.md
|-- analysis/
|-- drafts/
|-- final/
|-- sources/
|-- company-profile.md
|-- job-opportunity-review.md
`-- interview-prep.md
```

## 4. Fill the workspace

A typical workflow uses each folder for a different level of confidence:

- `sources/`: raw source notes, URLs, screenshots, and private references kept locally.
- `analysis/`: working judgments, comparison notes, risks, and open questions.
- `drafts/`: AI-assisted drafts that still need human review.
- `final/`: reviewed outputs that are ready to share.

The template files help separate facts from interpretation. For example:

- `company-profile.md` keeps company facts, products, risks, and open questions together.
- `job-opportunity-review.md` records why an opportunity is or is not worth more preparation time.
- `interview-prep.md` turns research into a concise preparation note.

## 5. Keep private work local

The repository intentionally ignores `workspaces/` by default. This keeps private research, resumes, contracts, financial details, API keys, and confidential company material out of public Git history.

Before publishing any example, convert it into a synthetic or anonymized case first. See `examples/privacy-safe-case-study.md` for a safe pattern.
