# -*- coding: utf-8 -*-
import json
import os
import sys
import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from start import main


class StartCliTest(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("tmp-summary-format-config.yaml"):
            os.remove("tmp-summary-format-config.yaml")

    def write_config(self, summary_format, summary_filename=None):
        lines = [
            "scope:",
            "  targets_file: targets.txt",
            "paths:",
            "  output_root: output",
            "scan:",
            "  ffuf_timeout_seconds: 60",
            "reports:",
        ]
        if summary_filename is not None:
            lines.append("  summary_filename: {}".format(summary_filename))
        lines.append("  summary_format: {}".format(summary_format))
        with open("tmp-summary-format-config.yaml", "w") as config_file:
            config_file.write("\n".join(lines))
            config_file.write("\n")

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

    def test_summarize_output_can_emit_markdown(self):
        code, output = self.run_main(
            [
                "--summarize-output",
                "missing-output.txt",
                "--summary-format",
                "markdown",
            ]
        )

        self.assertEqual(code, 0)
        self.assertIn("# OneDragon Output Summary", output)
        self.assertIn("| Artifact | State | Lines | Description |", output)
        self.assertIn("| final-domains-ips.txt | missing | 0 |", output)

    def test_summarize_output_uses_configured_summary_format(self):
        self.write_config("markdown")

        code, output = self.run_main(
            [
                "--config",
                "tmp-summary-format-config.yaml",
                "--summarize-output",
                "missing-output.txt",
            ]
        )

        self.assertEqual(code, 0)
        self.assertIn("# OneDragon Output Summary", output)
        self.assertIn("| Artifact | State | Lines | Description |", output)

    def test_summarize_output_cli_format_overrides_configured_format(self):
        self.write_config("markdown")

        code, output = self.run_main(
            [
                "--config",
                "tmp-summary-format-config.yaml",
                "--summarize-output",
                "missing-output.txt",
                "--summary-format",
                "json",
            ]
        )

        self.assertEqual(code, 0)
        parsed = json.loads(output)
        self.assertEqual(parsed["project"], "missing-output.txt")

    def test_write_summary_rejects_configured_nested_summary_filename(self):
        self.write_config("text", os.path.join("nested", "summary.txt"))

        code, output = self.run_main(
            [
                "--config",
                "tmp-summary-format-config.yaml",
                "--summarize-output",
                "missing-output.txt",
                "--write-summary",
            ]
        )

        self.assertEqual(code, 1)
        self.assertIn("summary filename", output)


if __name__ == "__main__":
    unittest.main()
