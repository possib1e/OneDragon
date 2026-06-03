# Tooling and Artifact Layout

OneDragon keeps a legacy integrated scanner workflow in one repository. This page separates bundled tools, configuration examples, and generated runtime artifacts so contributors can review changes more safely.

## Bundled or Integrated Tool Directories

- `OneForAll/`: vendored OneForAll workflow used for subdomain collection.
- `massdns`: massdns entrypoint expected by the legacy subdomain verification flow.
- `masscan_to_nmap/`: wrapper directory for masscan and nmap based port discovery.
- `ffuf/`: ffuf binary and bundled wordlists for directory discovery.
- `xray/`: xray scanner files and AWVS crawler integration.
- `module/`: OneDragon wrapper modules that orchestrate each scanner stage.

## Configuration and Documentation

- `config.example.yaml`: planned configuration surface for paths, timeouts, output directories, and report settings.
- `docs/installation.md`: runtime and external tool setup notes.
- `docs/configuration.md`: configuration migration plan.
- `docs/roadmap.md`: maintenance roadmap.
- `SECURITY.md`: responsible-use and vulnerability reporting guidance.
- `CONTRIBUTING.md`: contribution expectations and lightweight verification steps.

## Runtime Inputs

- `target.txt`: legacy single-target example.
- `targets.txt`: multi-target example file used by the current command examples.

Keep target files scoped to assets with explicit authorization. Avoid committing real client or third-party target data.

## Generated Runtime Artifacts

Generated files should stay out of git unless they are tiny examples used for documentation:

- `output/<targets-file>/`
- `ffuf/output/`
- `OneForAll/results/`
- `xray/output/`
- `xray/log.xray.log`
- `masscan_to_nmap/ip.txt`
- `masscan_to_nmap/masscan.json`
- `masscan_to_nmap/results.txt`
- `masscan_to_nmap/web.txt`

## Review Guidance

- Treat changes under `module/`, `start.py`, and documentation as OneDragon-maintained code.
- Treat changes under vendored scanner directories as higher-risk because they may affect upstream tool behavior.
- Prefer documenting assumptions before changing scanner command strings.
- Keep CI checks scanner-safe: syntax, help output, docs, and config validation are safe; live scans belong in isolated authorized environments.
