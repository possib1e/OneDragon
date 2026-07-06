# Maintenance Roadmap

This roadmap tracks maintenance work that makes OneDragon easier to review, run, and improve.

## Near Term

- Document installation requirements and scanner assumptions.
- Add configuration examples for paths, timeouts, and output directories.
- Add a config validation hook before wiring config values into scanner wrappers.
- Add scanner-safe config checking through `--check-config`.
- Add unit tests for config validation and keep them in CI.
- Parse simple config values before wiring them into scanner wrappers.
- Add safe config value access helpers for scanner wrapper migration.
- Print a scanner-safe config summary for maintainers.
- Reject unsupported config sections and keys during validation.
- Expose supported config sections and keys through the config check output.
- Add scanner-safe output summary reporting for existing artifacts.
- Add JSON output for scanner-safe summaries.
- Add report totals for present artifacts, missing artifacts, and total lines.
- Add output completeness status and missing artifact names to summaries.
- Add a versioned schema note for scanner-safe output summaries.
- Add Markdown output for review-friendly summaries.
- Keep generated scan outputs out of version control.
- Document bundled tool directories and generated runtime artifacts.
- Improve CLI help and target-file validation.
- Create focused issues for Docker support, config loading, CI, and report generation.
- Add a lightweight CI workflow that checks syntax and CLI help without running scanners.

## Medium Term

- Wire validated config values into scanner wrappers.
- Expand the config parser only as new supported settings need it.
- Add more CLI tests before changing scanner execution flow.
- Expand tests around scanner wrapper boundaries before changing command execution.
- Split scanner wrappers into smaller modules with testable boundaries.
- Replace shell string concatenation with safer subprocess calls.
- Extend CI from syntax checks to basic linting.
- Expand summary reporting into structured report generation.
- Add report schema notes for downstream tooling integrations.
- Add compatibility examples for tools that consume JSON summaries.

## Release Goals

- `v0.1.1`: maintenance documentation, issue triage, and CLI help.
- `v0.2.0`: configuration file support and Docker-based runtime.
- `v0.3.0`: structured report generation and modular scanner execution.
