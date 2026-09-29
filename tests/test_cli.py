"""Проверки запуска программы отдельным процессом."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def run_cli(self, *arguments, cwd=ROOT):
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env.pop("PYTHONPATH", None)
        return subprocess.run(
            [sys.executable, str(ROOT / "main.py"), *arguments],
            cwd=cwd, env=env, capture_output=True, text=True,
            encoding="utf-8", timeout=10,
        )

    def test_commands(self):
        cases = [("sum", "10", "25"), ("gcd", "48", "18", "6"),
                 ("euclid", "-48", "18", "6"),
                 ("vowels", "Привет, мир!", "3")]
        for *arguments, expected in cases:
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), expected)

    def test_invalid_input(self):
        for arguments in [("sum", "-1"), ("sum", "abc"), ("gcd", "3")]:
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertEqual(result.returncode, 2)
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_demo(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Sum of odd numbers through 10: 25", result.stdout)
        self.assertEqual(len(result.stdout.splitlines()), 5)

    def test_launch_from_another_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_cli("euclid", "48", "18", cwd=folder)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "6")


if __name__ == "__main__":
    unittest.main()
