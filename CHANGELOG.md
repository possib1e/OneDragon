# Changelog

All notable project maintenance changes are tracked here.

## 2026-07-27

- Added `docs/ci.md` to document scanner-safe maintenance CI checks.
- Documented the local equivalent command set for CI validation.
- Linked CI guidance from tooling and installation docs.
- Updated the roadmap for CI boundary documentation.

## 2026-07-10

- Extended maintenance CI to compile the test suite.
- Added scanner-safe CI smoke checks for JSON and Markdown output summaries.
- Kept CI checks limited to local validation and summary rendering, without running scanners.
- Updated the roadmap for summary-format CI coverage.

## 2026-07-09

- Added a shared `render_output_summary()` helper for text, JSON, and Markdown summaries.
- Reused the same summary format list for CLI choices and config validation.
- Routed CLI printing and written summary files through the shared renderer.
- Added tests for shared rendering and unsupported summary format rejection.
- Updated report schema notes and roadmap for centralized format handling.

## 2026-07-08

- Added validation for written output summary filenames.
- Restricted summary filenames to the inspected output directory.
- Added report and CLI tests for nested summary filename rejection.
- Updated configuration, reporting, and roadmap docs for the summary filename boundary.

## 2026-07-07

- Added `reports.summary_format` to the supported config surface.
- Allowed `--summarize-output` to use the configured summary format when the CLI format is omitted.
- Added validation for supported summary formats: `text`, `json`, and `markdown`.
- Added config and CLI tests for configured summary format defaults and command-line overrides.
- Updated configuration, reporting, and roadmap docs for the new report setting.

## 2026-07-06

- Added Markdown output support for scanner-safe output summaries.
- Added report and CLI tests for `--summary-format markdown`.
- Documented Markdown summary usage for issues, pull requests, and release notes.
- Updated the report schema notes to cover text, JSON, and Markdown payloads.

## 2026-07-04

- Added `schema_version` to scanner-safe output summaries.
- Documented the output summary schema for downstream JSON consumers.
- Added tests for schema version presence in collected, text, and JSON summaries.
- Updated reporting docs and roadmap for the versioned schema note.

## 2026-06-28

- Added output completeness status to scanner-safe summaries.
- Added missing artifact name lists to text and JSON summary output.
- Added tests for incomplete and complete output summary states.
- Updated reporting docs and roadmap for the completeness signal.

## 2026-06-19

- Added report totals for present artifacts, missing artifacts, and total lines.
- Included totals in text and JSON summary output.
- Added tests for collected, formatted, and JSON summary totals.
- Updated reporting docs and roadmap for the totals step.

## 2026-06-18

- Added JSON output support for scanner-safe output summaries.
- Added `--summary-format text|json` for `--summarize-output`.
- Added report and CLI tests for parseable JSON summary output.
- Updated reporting docs and roadmap for structured report support.

## 2026-06-17

- Added scanner-safe output summary reporting for existing result artifacts.
- Added `--summarize-output` and `--write-summary` CLI options.
- Added report module tests and CLI coverage for summary mode.
- Added reporting documentation and linked it from README.
- Added `reports.summary_filename` to `config.example.yaml`.

## 2026-06-16

- Added supported config surface output to `--check-config`.
- Added `list_supported_config()` and tests for supported section/key reporting.
- Updated configuration docs and roadmap to keep supported config keys visible.

## 2026-06-15

- Added explicit validation for supported config sections and keys.
- Added tests for unsupported config sections and unsupported key errors.
- Updated configuration docs and roadmap to describe the constrained config surface.

## 2026-06-14

- Added scanner-safe config summary output for `--check-config`.
- Added deterministic summary helper and tests for key parsed config values.
- Updated configuration docs and roadmap with the pre-flight config summary step.

## 2026-06-11

- Added safe config value access helpers for optional and required settings.
- Added tests for defaults, missing values, and required config value errors.
- Updated configuration docs and roadmap for the scanner wrapper migration path.

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
