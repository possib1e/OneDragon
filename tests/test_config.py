# -*- coding: utf-8 -*-
import os
import unittest

from module.config import load_config


class ConfigLoaderTest(unittest.TestCase):
    def tearDown(self):
        for filename in ("tmp-valid-config.yaml", "tmp-invalid-config.yaml"):
            if os.path.exists(filename):
                os.remove(filename)

    def write_config(self, filename, content):
        with open(filename, "w") as config_file:
            config_file.write(content)

    def test_empty_config_path_returns_none(self):
        self.assertIsNone(load_config(None))

    def test_example_config_loads_required_sections(self):
        result = load_config("config.example.yaml")

        self.assertEqual(result["path"], "config.example.yaml")
        self.assertEqual(result["sections"], ["paths", "reports", "scan", "scope"])

    def test_missing_config_file_raises_error(self):
        with self.assertRaises(ValueError) as error:
            load_config("missing-config.yaml")

        self.assertIn("config file not found", str(error.exception))

    def test_config_path_must_stay_in_project_root(self):
        with self.assertRaises(ValueError) as error:
            load_config(os.path.join("docs", "configuration.md"))

        self.assertIn("project root", str(error.exception))

    def test_missing_required_section_raises_error(self):
        self.write_config(
            "tmp-invalid-config.yaml",
            "scope:\npaths:\nscan:\n",
        )

        with self.assertRaises(ValueError) as error:
            load_config("tmp-invalid-config.yaml")

        self.assertIn("reports", str(error.exception))


if __name__ == "__main__":
    unittest.main()
