# Scanner-Safe CI

OneDragon's maintenance workflow is designed to validate repository health without running external scanners or contacting targets.

## Workflow

The GitHub Actions workflow lives at `.github/workflows/maintenance-checks.yml` and runs on pushes and pull requests to `master`.

It currently checks:

- Python compilation for `start.py`, `module/`, and `tests/`.
- CLI help output through `python start.py --help`.
- Config parsing through `python start.py --config config.example.yaml --check-config`.
- JSON output summary rendering through `python start.py --summarize-output targets.txt --summary-format json`.
- Markdown output summary rendering through `python start.py --summarize-output targets.txt --summary-format markdown`.
- Unit tests through `python -m unittest discover -s tests`.

## Safety Boundary

These checks are scanner-safe because they only parse local files, render local summaries, or execute unit tests. They do not launch OneForAll, massdns, masscan, nmap, ffuf, xray, AWVS, or any target-touching workflow.

Scanner behavior changes should be validated separately in an isolated environment with explicit authorization.

## Local Equivalent

Before pushing maintenance changes, run the same local checks with the Python launcher available on your machine. On Windows this may be `py -3`; on Linux CI it is `python`.

```bash
python -m compileall start.py module tests
python start.py --help
python start.py --config config.example.yaml --check-config
python start.py --summarize-output targets.txt --summary-format json
python start.py --summarize-output targets.txt --summary-format markdown
python -m unittest discover -s tests
```
