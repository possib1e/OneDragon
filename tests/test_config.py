# -*- coding: utf-8 -*-
import os
import unittest

from module.config import (
    get_config_value,
    list_supported_config,
    load_config,
    require_config_value,
    summarize_config,
)


class ConfigLoaderTest(unittest.TestCase):
    def tearDown(self):
        for filename in (
            "tmp-invalid-config.yaml",
            "tmp-unsupported-key.yaml",
            "tmp-unsupported-section.yaml",
        ):
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

    def test_example_config_loads_nested_values(self):
        result = load_config("config.example.yaml")

        self.assertEqual(result["values"]["paths"]["output_root"], "output")
        self.assertEqual(result["values"]["scope"]["authorized_only"], True)
        self.assertEqual(result["values"]["scan"]["ffuf_timeout_seconds"], 60)
        self.assertEqual(result["values"]["reports"]["generate_summary"], False)

    def test_get_config_value_returns_existing_value(self):
        result = load_config("config.example.yaml")

        self.assertEqual(get_config_value(result, "paths", "output_root"), "output")

    def test_get_config_value_returns_default_for_missing_value(self):
        result = load_config("config.example.yaml")

        self.assertEqual(
            get_config_value(result, "paths", "missing_key", default="fallback"),
            "fallback",
        )

    def test_get_config_value_returns_default_for_empty_config(self):
        self.assertEqual(
            get_config_value(None, "paths", "output_root", default="output"),
            "output",
        )

    def test_require_config_value_raises_for_missing_value(self):
        result = load_config("config.example.yaml")

        with self.assertRaises(ValueError) as error:
            require_config_value(result, "paths", "missing_key")

        self.assertIn("paths.missing_key", str(error.exception))

    def test_summarize_config_returns_stable_key_lines(self):
        result = load_config("config.example.yaml")

        summary = summarize_config(result)

        self.assertIn("scope.targets_file=targets.txt", summary)
        self.assertIn("paths.output_root=output", summary)
        self.assertIn("scan.ffuf_timeout_seconds=60", summary)
        self.assertIn("reports.generate_summary=False", summary)

    def test_list_supported_config_returns_sections_and_keys(self):
        supported = list_supported_config()

        self.assertIn("scope: targets_file, authorized_only", supported)
        self.assertIn("paths: output_root, oneforall_root, ffuf_wordlist, massdns_resolvers", supported)
        self.assertIn("reports: keep_raw_outputs, generate_summary", supported)

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

    def test_unsupported_section_raises_error(self):
        self.write_config(
            "tmp-unsupported-section.yaml",
            "scope:\npaths:\nscan:\nreports:\nunknown:\n",
        )

        with self.assertRaises(ValueError) as error:
            load_config("tmp-unsupported-section.yaml")

        self.assertIn("unsupported config section", str(error.exception))
        self.assertIn("unknown", str(error.exception))

    def test_unsupported_key_raises_error(self):
        self.write_config(
            "tmp-unsupported-key.yaml",
            "scope:\n"
            "  targets_file: targets.txt\n"
            "paths:\n"
            "  output_root: output\n"
            "scan:\n"
            "  unknown_timeout: 30\n"
            "reports:\n"
            "  generate_summary: false\n",
        )

        with self.assertRaises(ValueError) as error:
            load_config("tmp-unsupported-key.yaml")

        self.assertIn("unsupported config value", str(error.exception))
        self.assertIn("scan.unknown_timeout", str(error.exception))


if __name__ == "__main__":
    unittest.main()
