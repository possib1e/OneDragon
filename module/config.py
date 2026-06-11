# -*- coding: utf-8 -*-
import os


REQUIRED_SECTIONS = ("scope", "paths", "scan", "reports")
MISSING = object()


def _coerce_value(value):
    if value in ("true", "True"):
        return True
    if value in ("false", "False"):
        return False
    if value.isdigit():
        return int(value)
    return value.strip("\"'")


def load_config(config_path):
    if not config_path:
        return None
    if os.path.basename(config_path) != config_path:
        raise ValueError("config file must be in the project root directory")
    if not os.path.isfile(config_path):
        raise ValueError("config file not found: {}".format(config_path))

    current_section = None
    sections = set()
    values = {}
    with open(config_path, "r") as config_file:
        for line in config_file:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if not line.startswith(" ") and stripped.endswith(":"):
                current_section = stripped[:-1]
                sections.add(current_section)
                values.setdefault(current_section, {})
                continue
            if current_section and line.startswith(" ") and ":" in stripped:
                key, raw_value = stripped.split(":", 1)
                values[current_section][key.strip()] = _coerce_value(
                    raw_value.strip()
                )

    missing = [section for section in REQUIRED_SECTIONS if section not in sections]
    if missing:
        raise ValueError(
            "config file is missing required section(s): {}".format(
                ", ".join(missing)
            )
        )

    return {"path": config_path, "sections": sorted(sections), "values": values}


def get_config_value(config, section, key, default=None):
    if not config:
        return default
    return config.get("values", {}).get(section, {}).get(key, default)


def require_config_value(config, section, key):
    value = get_config_value(config, section, key, MISSING)
    if value is MISSING:
        raise ValueError("missing config value: {}.{}".format(section, key))
    return value
