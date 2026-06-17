# -*- coding: utf-8 -*-
import os
import shutil
import unittest

from module.report import (
    collect_output_summary,
    format_output_summary,
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
        self.assertEqual(summary["output_dir"], self.output_dir)
        self.assertEqual(artifacts["urls_sub.txt"]["lines"], 2)
        self.assertEqual(artifacts["ips_all.txt"]["lines"], 1)
        self.assertEqual(artifacts["ffuf_all.csv"]["exists"], False)

    def test_format_output_summary_includes_artifact_state(self):
        summary = collect_output_summary(self.project, self.output_root)

        lines = format_output_summary(summary)

        self.assertIn("OneDragon output summary", lines)
        self.assertIn("project=targets.txt", lines)
        self.assertTrue(any("urls_sub.txt: present" in line for line in lines))
        self.assertTrue(any("ffuf_all.csv: missing" in line for line in lines))

    def test_write_output_summary_writes_summary_file(self):
        summary = collect_output_summary(self.project, self.output_root)

        summary_path = write_output_summary(summary, "summary.txt")

        self.assertTrue(os.path.isfile(summary_path))
        with open(summary_path, "r") as summary_file:
            content = summary_file.read()
        self.assertIn("OneDragon output summary", content)

    def test_collect_output_summary_rejects_nested_project_path(self):
        with self.assertRaises(ValueError) as error:
            collect_output_summary(
                os.path.join("nested", "targets.txt"), self.output_root
            )

        self.assertIn("project root", str(error.exception))


if __name__ == "__main__":
    unittest.main()
