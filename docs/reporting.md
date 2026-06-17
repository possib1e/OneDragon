# Reporting Notes

OneDragon includes a scanner-safe output summary command. It reads existing files under `output/<targets-file>/` and prints a compact artifact report without launching any scanners.

## Print a Summary

```bash
python3 start.py --summarize-output targets.txt
```

The command reports whether each expected artifact exists and how many lines it contains.

## Write a Summary File

```bash
python3 start.py --summarize-output targets.txt --write-summary
```

By default this writes `summary.txt` under the matching output directory. The filename is controlled by `reports.summary_filename` in `config.example.yaml`.

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
