# -*- coding: utf-8 -*-
import json
import sys
import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from start import main


class StartCliTest(unittest.TestCase):
    def run_main(self, args):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            code = main(args)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = original_stdout
        return code, output

    def test_check_config_success_does_not_require_targets_file(self):
        code, output = self.run_main(["--config", "config.example.yaml", "--check-config"])

        self.assertEqual(code, 0)
        self.assertIn("Config OK", output)
        self.assertIn("config.example.yaml", output)
        self.assertIn("paths.output_root=output", output)
        self.assertIn("Supported config keys:", output)
        self.assertIn("scope: targets_file, authorized_only", output)

    def test_check_config_requires_config_argument(self):
        code, output = self.run_main(["--check-config"])

        self.assertEqual(code, 1)
        self.assertIn("--config", output)

    def test_targets_file_is_required_for_scan_mode(self):
        code, output = self.run_main([])

        self.assertEqual(code, 1)
        self.assertIn("targets file is required", output)

    def test_summarize_output_reports_missing_output_without_scanning(self):
        code, output = self.run_main(["--summarize-output", "missing-output.txt"])

        self.assertEqual(code, 0)
        self.assertIn("OneDragon output summary", output)
        self.assertIn("output_exists=False", output)

    def test_summarize_output_can_emit_json(self):
        code, output = self.run_main(
            ["--summarize-output", "missing-output.txt", "--summary-format", "json"]
        )

        self.assertEqual(code, 0)
        parsed = json.loads(output)
        self.assertEqual(parsed["project"], "missing-output.txt")
        self.assertEqual(parsed["output_exists"], False)


if __name__ == "__main__":
    unittest.main()
