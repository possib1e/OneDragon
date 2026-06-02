# Maintenance Roadmap

This roadmap tracks maintenance work that makes OneDragon easier to review, run, and improve.

## Near Term

- Document installation requirements and scanner assumptions.
- Add configuration examples for paths, timeouts, and output directories.
- Keep generated scan outputs out of version control.
- Improve CLI help and target-file validation.
- Create focused issues for Docker support, config loading, CI, and report generation.
- Add a lightweight CI workflow that checks syntax and CLI help without running scanners.

## Medium Term

- Add a config loader and a `--config` CLI option.
- Split scanner wrappers into smaller modules with testable boundaries.
- Replace shell string concatenation with safer subprocess calls.
- Extend CI from syntax checks to basic linting.
- Create a minimal summary report from existing output files.

## Release Goals

- `v0.1.1`: maintenance documentation, issue triage, and CLI help.
- `v0.2.0`: configuration file support and Docker-based runtime.
- `v0.3.0`: structured report generation and modular scanner execution.
