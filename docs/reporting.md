# Reporting Notes

OneDragon includes a scanner-safe output summary command. It reads existing files under `output/<targets-file>/` and prints a compact artifact report without launching any scanners.

## Print a Summary

```bash
python3 start.py --summarize-output targets.txt
```

The command reports whether each expected artifact exists, how many lines it
contains, whether the output set is complete, which artifact names are still
missing, and totals for present artifacts, missing artifacts, and output lines.

## JSON Output

```bash
python3 start.py --summarize-output targets.txt --summary-format json
```

Use JSON when another tool needs to consume the report. The JSON payload includes
the same artifact entries, completeness status, missing artifact names, and
totals as the text output. See [Output Summary Schema](report-schema.md) for the
stable field contract.

## Markdown Output

```bash
python3 start.py --summarize-output targets.txt --summary-format markdown
```

Use Markdown when the summary needs to be pasted into an issue, pull request, or
release note. The Markdown output includes the same totals and artifact states
as the text output, plus a table for review.

## Write a Summary File

```bash
python3 start.py --summarize-output targets.txt --write-summary
```

By default this writes `summary.txt` under the matching output directory. The filename is controlled by `reports.summary_filename` in `config.example.yaml`. The file content follows `--summary-format`.

## Expected Artifacts

- `final-domains-ips.txt`
- `urls_sub.txt`
- `ips_all.txt`
- `urls_ip.txt`
- `ip_port_scan_results.txt`
- `urls_all.txt`
- `ffuf_all.csv`
- `ffuf_redup.txt`

This feature is intended for review and maintenance. It does not replace scanner-specific reports and does not execute live target activity.
