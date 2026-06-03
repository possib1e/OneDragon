# Installation Notes

OneDragon is a legacy integrated workflow that calls several external security tools. Before running it, prepare an isolated and authorized test environment.

## Runtime

- Python 3
- Linux-compatible shell tools used by the legacy commands, such as `cat`, `cut`, `grep`, `sed`, `sort`, and `timeout`
- OneForAll dependencies from `OneForAll/requirements.txt`
- `pandas`, used by the ffuf result reducer

## External Tools

The workflow expects these tools or directories to be available:

- OneForAll under `OneForAll/`
- massdns under `massdns/`
- masscan and nmap through `masscan_to_nmap/`
- ffuf and wordlists under `ffuf/`
- xray under `xray/`
- AWVS crawler integration under `xray/awvs/`

See `docs/tooling.md` for the distinction between bundled tools, examples, and generated runtime artifacts.

## Recommended Setup Flow

1. Clone the repository in an isolated environment.
2. Install Python dependencies for both the root workflow and OneForAll.
3. Confirm every external scanner binary is executable.
4. Put authorized root domains in a project-root targets file.
5. Run `python3 start.py --help` before launching a scan.
6. Run the workflow only against explicitly authorized targets.

## Verification

Use a syntax check before changing the workflow:

```bash
python3 -m compileall start.py module
```

For scanner behavior changes, use a small internal test domain first and inspect files under `output/<targets-file>/`.
