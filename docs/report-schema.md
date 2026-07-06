# Output Summary Schema

The output summary command is a scanner-safe reporting path. It reads local
files under `output/<targets-file>/` and does not execute scanners or contact
targets.

## Version

`schema_version` identifies the shape of the text, JSON, and Markdown summary
payloads. Version `1` includes the fields documented below.

Schema changes should be additive where possible. Increment `schema_version`
when a future change removes or renames a field, changes a field type, or
changes the meaning of an existing value.

## Top-Level Fields

- `schema_version`: integer report schema version.
- `project`: targets file name passed to the summary command.
- `output_root`: configured output root directory.
- `output_dir`: directory inspected for generated artifacts.
- `output_exists`: whether `output_dir` exists.
- `complete`: whether every expected artifact is present.
- `missing_artifact_names`: expected artifact names that are not present.
- `totals`: aggregate counts for present artifacts, missing artifacts, and
  total output lines.
- `artifacts`: per-artifact status entries.

## Artifact Fields

Each artifact entry contains:

- `name`: expected artifact filename.
- `description`: human-readable artifact purpose.
- `exists`: whether the artifact file is present.
- `lines`: line count when the artifact exists, otherwise `0`.

## Compatibility Notes

Consumers should prefer JSON output for automation:

```bash
python3 start.py --summarize-output targets.txt --summary-format json
```

Consumers should tolerate additional fields in future schema versions.
Markdown output is intended for human review in issues, pull requests, and
release notes rather than machine parsing.
