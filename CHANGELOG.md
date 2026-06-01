# Changelog

All notable project maintenance changes are tracked here.

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
