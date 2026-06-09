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

1. Introduce a config loader with validation. Done: `--config` now validates that the file exists in the project root and contains the expected top-level sections.
2. Move hard-coded scanner paths into `config.example.yaml`.
3. Keep legacy defaults for backward compatibility.
4. Wire validated config values into scanner wrappers after the legacy defaults are covered by tests.
5. Document each option in this file as it becomes active.

## Current CLI Support

`--config` is available as a validation hook:

```bash
python3 start.py --config config.example.yaml targets.txt
```

At this stage the option validates the file shape but does not change scanner behavior. This keeps the legacy workflow stable while configuration support is introduced incrementally.

To validate configuration without launching scanners, use:

```bash
python3 start.py --config config.example.yaml --check-config
```

## Test Coverage

Config validation is covered by `tests/test_config.py` and CLI behavior is covered by `tests/test_start_cli.py`. The tests check the example config, missing files, path restrictions, missing required sections, and the scanner-safe `--check-config` mode.
