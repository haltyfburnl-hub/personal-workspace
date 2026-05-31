import importlib.util
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_workspace.py"

spec = importlib.util.spec_from_file_location("create_workspace", SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CreateWorkspaceTests(unittest.TestCase):
    def test_slugify_latin_name(self):
        self.assertEqual(module.slugify("Example Company"), "example-company")

    def test_slugify_non_latin_name_is_stable(self):
        first = module.slugify("示例公司")
        second = module.slugify("示例公司")
        self.assertEqual(first, second)
        self.assertTrue(first.startswith("workspace-"))
        self.assertEqual(len(first), len("workspace-12345678"))

    def test_template_map_contains_company_workflow(self):
        self.assertIn("company", module.TEMPLATE_MAP)
        self.assertIn("company-profile.md", module.TEMPLATE_MAP["company"])

    def test_list_workspace_types_includes_templates(self):
        output = module.list_workspace_types()
        self.assertIn("company:", output)
        self.assertIn("job:", output)
        self.assertIn("interview:", output)
        self.assertIn("company-profile.md", output)
        self.assertIn("interview-prep.md", output)


if __name__ == "__main__":
    unittest.main()
