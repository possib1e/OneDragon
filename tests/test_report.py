# -*- coding: utf-8 -*-
import json
import os
import shutil
import unittest

from module.report import (
    collect_output_summary,
    format_output_summary,
    format_output_summary_json,
    format_output_summary_markdown,
    write_output_summary,
)


class OutputReportTest(unittest.TestCase):
    output_root = "tmp-report-output"
    project = "targets.txt"

    def setUp(self):
        self.output_dir = os.path.join(self.output_root, self.project)
        os.makedirs(self.output_dir)
        self.write_output("urls_sub.txt", "http://a.example\nhttp://b.example\n")
        self.write_output("ips_all.txt", "127.0.0.1\n")

    def tearDown(self):
        if os.path.exists(self.output_root):
            shutil.rmtree(self.output_root)

    def write_output(self, filename, content):
        with open(os.path.join(self.output_dir, filename), "w") as output_file:
            output_file.write(content)

    def test_collect_output_summary_counts_present_artifacts(self):
        summary = collect_output_summary(self.project, self.output_root)

        artifacts = dict((item["name"], item) for item in summary["artifacts"])
        self.assertEqual(summary["schema_version"], 1)
        self.assertEqual(summary["output_dir"], self.output_dir)
        self.assertEqual(summary["totals"]["present_artifacts"], 2)
        self.assertEqual(summary["totals"]["missing_artifacts"], 6)
        self.assertEqual(summary["totals"]["total_lines"], 3)
        self.assertEqual(summary["complete"], False)
        self.assertIn("final-domains-ips.txt", summary["missing_artifact_names"])
        self.assertIn("ffuf_redup.txt", summary["missing_artifact_names"])
        self.assertEqual(artifacts["urls_sub.txt"]["lines"], 2)
        self.assertEqual(artifacts["ips_all.txt"]["lines"], 1)
        self.assertEqual(artifacts["ffuf_all.csv"]["exists"], False)

    def test_collect_output_summary_marks_complete_output(self):
        for filename in (
            "final-domains-ips.txt",
            "urls_ip.txt",
            "ip_port_scan_results.txt",
            "urls_all.txt",
            "ffuf_all.csv",
            "ffuf_redup.txt",
        ):
            self.write_output(filename, "placeholder\n")

        summary = collect_output_summary(self.project, self.output_root)

        self.assertEqual(summary["complete"], True)
        self.assertEqual(summary["missing_artifact_names"], [])
        self.assertEqual(summary["totals"]["present_artifacts"], 8)

    def test_format_output_summary_includes_artifact_state(self):
        summary = collect_output_summary(self.project, self.output_root)

        lines = format_output_summary(summary)

        self.assertIn("OneDragon output summary", lines)
        self.assertIn("schema_version=1", lines)
        self.assertIn("project=targets.txt", lines)
        self.assertIn("complete=False", lines)
        self.assertIn("present_artifacts=2", lines)
        self.assertIn("total_lines=3", lines)
        self.assertTrue(
            any("missing_artifact_names=final-domains-ips.txt" in line for line in lines)
        )
        self.assertTrue(any("urls_sub.txt: present" in line for line in lines))
        self.assertTrue(any("ffuf_all.csv: missing" in line for line in lines))

    def test_write_output_summary_writes_summary_file(self):
        summary = collect_output_summary(self.project, self.output_root)

        summary_path = write_output_summary(summary, "summary.txt")

        self.assertTrue(os.path.isfile(summary_path))
        with open(summary_path, "r") as summary_file:
            content = summary_file.read()
        self.assertIn("OneDragon output summary", content)

    def test_format_output_summary_json_returns_parseable_json(self):
        summary = collect_output_summary(self.project, self.output_root)

        parsed = json.loads(format_output_summary_json(summary))

        self.assertEqual(parsed["project"], "targets.txt")
        self.assertEqual(parsed["schema_version"], 1)
        self.assertEqual(parsed["output_root"], self.output_root)
        self.assertEqual(parsed["complete"], False)
        self.assertIn("ffuf_all.csv", parsed["missing_artifact_names"])
        self.assertEqual(parsed["totals"]["total_lines"], 3)
        self.assertEqual(len(parsed["artifacts"]), 8)

    def test_format_output_summary_markdown_returns_review_table(self):
        summary = collect_output_summary(self.project, self.output_root)

        lines = format_output_summary_markdown(summary)

        self.assertIn("# OneDragon Output Summary", lines)
        self.assertIn("- Schema version: 1", lines)
        self.assertIn("| Artifact | State | Lines | Description |", lines)
        self.assertTrue(any("| urls_sub.txt | present | 2 |" in line for line in lines))
        self.assertTrue(any("| ffuf_all.csv | missing | 0 |" in line for line in lines))

    def test_write_output_summary_writes_json_summary_file(self):
        summary = collect_output_summary(self.project, self.output_root)

        summary_path = write_output_summary(summary, "summary.json", "json")

        with open(summary_path, "r") as summary_file:
            parsed = json.loads(summary_file.read())
        self.assertEqual(parsed["project"], "targets.txt")

    def test_write_output_summary_writes_markdown_summary_file(self):
        summary = collect_output_summary(self.project, self.output_root)

        summary_path = write_output_summary(summary, "summary.md", "markdown")

        with open(summary_path, "r") as summary_file:
            content = summary_file.read()
        self.assertIn("# OneDragon Output Summary", content)
        self.assertIn("| urls_sub.txt | present | 2 |", content)

    def test_write_output_summary_rejects_nested_summary_filename(self):
        summary = collect_output_summary(self.project, self.output_root)

        with self.assertRaises(ValueError) as error:
            write_output_summary(summary, os.path.join("nested", "summary.txt"))

        self.assertIn("output directory", str(error.exception))

    def test_write_output_summary_rejects_empty_summary_filename(self):
        summary = collect_output_summary(self.project, self.output_root)

        with self.assertRaises(ValueError) as error:
            write_output_summary(summary, " ")

        self.assertIn("summary filename", str(error.exception))

    def test_collect_output_summary_rejects_nested_project_path(self):
        with self.assertRaises(ValueError) as error:
            collect_output_summary(
                os.path.join("nested", "targets.txt"), self.output_root
            )

        self.assertIn("project root", str(error.exception))


if __name__ == "__main__":
    unittest.main()
