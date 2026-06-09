# -*- coding: utf-8 -*-
import argparse
import os
import sys
from module.config import load_config
from module.common import rm_output_file
#python3 start.py targets.txt


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Run the OneDragon authorized security testing workflow."
    )
    parser.add_argument(
        "targets_file",
        nargs="?",
        help="Project-root file containing one authorized root domain per line.",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Optional project-root config file to validate before running.",
    )
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Validate the config file and exit without running scanners.",
    )
    return parser.parse_args(argv)


def validate_target_file(filename):
    if os.path.basename(filename) != filename:
        raise ValueError("targets file must be in the project root directory")
    if not os.path.isfile(filename):
        raise ValueError("targets file not found: {}".format(filename))


def main(argv=None):
    args = parse_args(argv)
    try:
        config = load_config(args.config)
    except ValueError as error:
        print("Error: {}".format(error))
        return 1

    if args.check_config:
        if not args.config:
            print("Error: --check-config requires --config.")
            return 1
        print(
            "Config OK: {} ({})".format(
                config["path"], ", ".join(config["sections"])
            )
        )
        return 0

    filename = args.targets_file
    if not filename or not filename.strip():
        print("Error: targets file is required.")
        return 1

    try:
        validate_target_file(filename)
    except ValueError as error:
        print("Error: {}".format(error))
        return 1

    rm_output_file(filename)

    from module.scan_file import start_ffuf
    from module.scan_port import start_masscan_to_nmap
    from module.scan_subdomain import start_massdns, start_oneforall
    from module.scan_vuln import start_xray_scan

    #输入target.txt
    #输出output/target.txt/下的 final-domains-ips.txt urls_sub.txt ips_all.txt
    start_oneforall(filename)
    start_massdns(filename)

    #输入output/target.txt下的 ips_all.txt urls_sub.txt
    #输出output/target.txt下的 ip_port_scan_results.txt urls_ip.txt urls_all.txt
    start_masscan_to_nmap(filename)

    #输入output/target.txt下的 urls_all.txt
    #输入output/target.txt下的 ffuf_all.csv ffuf_redup.txt
    start_ffuf(filename)

    # 输入output/target.txt下的 urls_all.txt
    # 输出xary下的扫描报告
    start_xray_scan(filename)

    return 0


if __name__ == '__main__':
    sys.exit(main())
