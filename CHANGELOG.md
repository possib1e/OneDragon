# Changelog

All notable project maintenance changes are tracked here.

## 2026-06-01

- Reworked README structure for clearer setup, scope, outputs, and roadmap.
- Added `.gitignore` entries for runtime scan outputs and local Python/editor files.
- Added `SECURITY.md` with responsible-use and vulnerability-reporting guidance.
- Added `CONTRIBUTING.md` with lightweight contribution and testing expectations.
- Hardened output directory recreation by using `pathlib` and `shutil` instead of shelling out to `rm -rf`.
- Added basic CLI argument and target-file validation to `start.py`.
