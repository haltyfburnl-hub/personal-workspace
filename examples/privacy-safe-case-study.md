# Privacy-Safe Case Study

This case study is synthetic, but it reflects recurring personal research workflows that motivated the project: collecting scattered notes, using AI to organize them, and producing a reviewed decision document without exposing private material.

## Situation

A user is comparing two career opportunities while preparing for interviews. The raw inputs include public company pages, job descriptions, interview notes, compensation assumptions, commute constraints, and private family or financial context.

Instead of saving everything in one document, the user creates a workspace:

```bash
python3 scripts/create_workspace.py "Example Opportunity Review" --type company
```

## Workspace layout

```text
workspaces/example-opportunity-review/
|-- sources/
|-- analysis/
|-- drafts/
|-- final/
|-- company-profile.md
|-- job-opportunity-review.md
`-- interview-prep.md
```

## How the workflow is used

1. Public source links and raw notes go into `sources/`.
2. Personal constraints and private judgments stay in local-only notes under `analysis/`.
3. AI-assisted drafts go into `drafts/` and are treated as unreviewed.
4. A short, human-reviewed decision summary goes into `final/`.
5. If an example is shared publicly, all private details are replaced with synthetic names, rounded numbers, and generalized constraints.

## Example reviewed outcome

```text
Decision: Continue the interview process, but do not over-invest until the reporting line and success metrics are confirmed.

Reasons:
- The role matches the user's experience in commercial execution and cross-functional coordination.
- The company has a plausible growth path, but public information is not enough to assess internal decision quality.
- Compensation, location, and family timing need confirmation before serious preparation work.

Open questions:
- Who owns final commercial decisions?
- What are the first 90-day goals?
- How much autonomy does the role actually have?
```

## Why this matters

AI tools are useful for organizing this kind of research, but they can also blur the line between public facts, private context, assumptions, and final answers. This project makes that boundary visible and repeatable.
