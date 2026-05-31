import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_workspace.py"

spec = importlib.util.spec_from_file_location("create_workspace", SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_slugify_latin_name():
    assert module.slugify("Example Company") == "example-company"


def test_slugify_non_latin_name_is_stable():
    first = module.slugify("示例公司")
    second = module.slugify("示例公司")
    assert first == second
    assert first.startswith("workspace-")
    assert len(first) == len("workspace-12345678")


def test_template_map_contains_company_workflow():
    assert "company" in module.TEMPLATE_MAP
    assert "company-profile.md" in module.TEMPLATE_MAP["company"]