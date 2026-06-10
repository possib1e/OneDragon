# Changelog

All notable project maintenance changes are tracked here.

## 2026-06-10

- Extended config loading to parse one level of key/value settings from `config.example.yaml`.
- Added tests for parsed path, boolean, and integer config values.
- Updated configuration docs and roadmap for the staged parser support.

## 2026-06-09

- Added scanner-safe `--check-config` mode for validating config files without launching scanners.
- Refactored `start.py` into a testable `main(argv=None)` entrypoint.
- Added CLI tests for config checking and missing target-file handling.
- Updated CI and configuration docs to use `--check-config`.

## 2026-06-08

- Added unit tests for config validation behavior.
- Extended GitHub Actions to run `python -m unittest discover -s tests`.
- Documented config validation test coverage and updated the maintenance roadmap.

## 2026-06-04

- Added a lightweight config validation module for the planned `--config` workflow.
- Added `--config` CLI parsing while keeping legacy scanner defaults unchanged.
- Extended CI to check config option parsing with `config.example.yaml`.
- Updated configuration docs and roadmap with the staged config migration status.

## 2026-06-03

- Added `docs/tooling.md` to separate bundled tools, configuration examples, runtime inputs, and generated artifacts.
- Linked the tooling layout from README, installation notes, and the roadmap.
- Added a lightweight GitHub Actions workflow for Python syntax checks and CLI help output.
- Updated the maintenance roadmap to mark CI syntax checks as a near-term maintenance track.
- Kept the CI workflow scanner-safe by avoiding any target execution.

## 2026-06-02

- Added installation, configuration, and roadmap documentation.
- Added release notes for `v0.1.1`.
- Added `config.example.yaml` to document the planned configuration surface.
- Switched the main entrypoint to `argparse` for standard `--help` output.
- Deferred scanner module imports until after argument parsing so help output works before optional scanner dependencies are installed.
- Replaced `pathlib` usage in the entrypoint path checks with `os.path` for wider Python runtime compatibility.
- Added a project status section to clarify the current maintenance focus.
- Expanded the roadmap with third-party tool directory cleanup.
- Documented the recommendation to validate external scanner settings in an isolated authorized test environment.

## 2026-06-01

- Reworked README structure for clearer setup, scope, outputs, and roadmap.
- Added `.gitignore` entries for runtime scan outputs and local Python/editor files.
- Added `SECURITY.md` with responsible-use and vulnerability-reporting guidance.
- Added `CONTRIBUTING.md` with lightweight contribution and testing expectations.
- Hardened output directory recreation by using `pathlib` and `shutil` instead of shelling out to `rm -rf`.
- Added basic CLI argument and target-file validation to `start.py`.
