# -*- coding: utf-8 -*-
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

    def test_check_config_requires_config_argument(self):
        code, output = self.run_main(["--check-config"])

        self.assertEqual(code, 1)
        self.assertIn("--config", output)

    def test_targets_file_is_required_for_scan_mode(self):
        code, output = self.run_main([])

        self.assertEqual(code, 1)
        self.assertIn("targets file is required", output)


if __name__ == "__main__":
    unittest.main()
