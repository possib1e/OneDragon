# -*- coding: utf-8 -*-
import os


REQUIRED_SECTIONS = ("scope", "paths", "scan", "reports")


def load_config(config_path):
    if not config_path:
        return None
    if os.path.basename(config_path) != config_path:
        raise ValueError("config file must be in the project root directory")
    if not os.path.isfile(config_path):
        raise ValueError("config file not found: {}".format(config_path))

    sections = set()
    with open(config_path, "r") as config_file:
        for line in config_file:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if not line.startswith(" ") and stripped.endswith(":"):
                sections.add(stripped[:-1])

    missing = [section for section in REQUIRED_SECTIONS if section not in sections]
    if missing:
        raise ValueError(
            "config file is missing required section(s): {}".format(
                ", ".join(missing)
            )
        )

    return {"path": config_path, "sections": sorted(sections)}
