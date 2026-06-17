# -*- coding: utf-8 -*-
import os


OUTPUT_ARTIFACTS = (
    ("final-domains-ips.txt", "Resolved subdomain records"),
    ("urls_sub.txt", "Subdomain URLs"),
    ("ips_all.txt", "Resolved IP addresses"),
    ("urls_ip.txt", "Web services discovered from IP scans"),
    ("ip_port_scan_results.txt", "Port scan results"),
    ("urls_all.txt", "Combined URL list"),
    ("ffuf_all.csv", "Raw ffuf CSV output"),
    ("ffuf_redup.txt", "Deduplicated ffuf findings"),
)


def _validate_project_name(project):
    if not project or not project.strip():
        raise ValueError("targets file is required for output summary")
    if os.path.basename(project) != project:
        raise ValueError("targets file must be in the project root directory")


def _count_lines(filepath):
    with open(filepath, "r") as input_file:
        return sum(1 for _line in input_file)


def collect_output_summary(project, output_root="output"):
    _validate_project_name(project)
    output_dir = os.path.join(output_root, project)
    artifacts = []

    for filename, description in OUTPUT_ARTIFACTS:
        filepath = os.path.join(output_dir, filename)
        exists = os.path.isfile(filepath)
        artifacts.append(
            {
                "name": filename,
                "description": description,
                "exists": exists,
                "lines": _count_lines(filepath) if exists else 0,
            }
        )

    return {
        "project": project,
        "output_root": output_root,
        "output_dir": output_dir,
        "output_exists": os.path.isdir(output_dir),
        "artifacts": artifacts,
    }


def format_output_summary(summary):
    lines = [
        "OneDragon output summary",
        "project={}".format(summary["project"]),
        "output_dir={}".format(summary["output_dir"]),
        "output_exists={}".format(summary["output_exists"]),
        "artifacts:",
    ]
    for artifact in summary["artifacts"]:
        state = "present" if artifact["exists"] else "missing"
        lines.append(
            "- {name}: {state}, lines={lines}, description={description}".format(
                name=artifact["name"],
                state=state,
                lines=artifact["lines"],
                description=artifact["description"],
            )
        )
    return lines


def write_output_summary(summary, filename="summary.txt"):
    if not summary["output_exists"]:
        raise ValueError(
            "output directory does not exist: {}".format(summary["output_dir"])
        )
    summary_path = os.path.join(summary["output_dir"], filename)
    with open(summary_path, "w") as output_file:
        output_file.write("\n".join(format_output_summary(summary)))
        output_file.write("\n")
    return summary_path
