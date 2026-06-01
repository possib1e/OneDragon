# Configuration Notes

The current workflow still contains legacy hard-coded command paths. `config.example.yaml` documents the intended configuration shape for the next maintenance phase.

## Planned Configuration Areas

- Scan scope and target file location
- Output root directory
- OneForAll, massdns, ffuf, xray, and AWVS paths
- Wordlist and resolver list paths
- Timeout and wildcard-detection thresholds
- Report generation switches

## Current Safe Defaults

- Keep targets files in the project root.
- Keep generated outputs under `output/`.
- Keep runtime scanner artifacts out of git.
- Validate every scanner command in an isolated authorized environment before widening scope.

## Migration Plan

1. Introduce a config loader with validation.
2. Move hard-coded scanner paths into `config.example.yaml`.
3. Keep legacy defaults for backward compatibility.
4. Add a `--config` CLI option after the defaults are covered by tests.
5. Document each option in this file as it becomes active.
