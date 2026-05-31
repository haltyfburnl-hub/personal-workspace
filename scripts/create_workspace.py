#!/usr/bin/env python3
"""Create a local research workspace from the repository templates."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates"
WORKSPACE_DIR = ROOT / "workspaces"

TEMPLATE_MAP = {
    "company": ["company-profile.md", "job-opportunity-review.md", "interview-prep.md"],
    "job": ["job-opportunity-review.md", "interview-prep.md"],
    "interview": ["interview-prep.md"],
}


def slugify(value: str) -> str:
    """Return a stable filesystem-friendly slug.

    Non-Latin names are common in company research. If a readable ASCII slug
    cannot be produced, keep a stable short hash instead of collapsing every
    name to the same `workspace` folder.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    if cleaned:
        return cleaned
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    return f"workspace-{digest}"


def list_workspace_types() -> str:
    """Return supported workspace types and their templates."""
    lines = []
    for workspace_type in sorted(TEMPLATE_MAP):
        templates = ", ".join(TEMPLATE_MAP[workspace_type])
        lines.append(f"{workspace_type}: {templates}")
    return "\n".join(lines)


def copy_template(template_name: str, target_dir: Path) -> None:
    source = TEMPLATE_DIR / template_name
    if not source.exists():
        raise FileNotFoundError(f"Missing template: {source}")
    shutil.copyfile(source, target_dir / template_name)


def create_workspace(name: str, workspace_type: str) -> Path:
    target_dir = WORKSPACE_DIR / slugify(name)
    target_dir.mkdir(parents=True, exist_ok=False)

    for folder in ["sources", "analysis", "drafts", "final"]:
        (target_dir / folder).mkdir()

    for template_name in TEMPLATE_MAP[workspace_type]:
        copy_template(template_name, target_dir)

    readme = target_dir / "README.md"
    readme.write_text(
        f"# {name}\n\n"
        f"Workspace type: {workspace_type}\n\n"
        "## Folders\n\n"
        "- `sources/`: raw source notes and references.\n"
        "- `analysis/`: working notes and judgments.\n"
        "- `drafts/`: draft outputs.\n"
        "- `final/`: reviewed deliverables.\n\n"
        "Keep private materials local. Do not commit this workspace unless you intentionally want to publish it.\n",
        encoding="utf-8",
    )

    return target_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a local personal workspace.")
    parser.add_argument("name", nargs="?", help="Workspace name, such as a company or role name.")
    parser.add_argument(
        "--type",
        choices=sorted(TEMPLATE_MAP),
        default="company",
        help="Workspace type to create.",
    )
    parser.add_argument(
        "--list-types",
        action="store_true",
        help="List supported workspace types and exit.",
    )
    args = parser.parse_args()
    if not args.list_types and not args.name:
        parser.error("the following arguments are required: name")
    return args


def main() -> None:
    args = parse_args()
    if args.list_types:
        print(list_workspace_types())
        return

    target_dir = create_workspace(args.name, args.type)
    print(f"Created workspace: {target_dir}")


if __name__ == "__main__":
    main()
