import sys
from pathlib import Path
from module.scan_subdomain import start_oneforall,start_massdns
from module.scan_port import start_masscan_to_nmap
from module.scan_file import start_ffuf
from module.scan_vuln import start_xray_scan
from module.common import rm_output_file
#python3 start.py targets.txt

def usage():
    print("Usage: python3 start.py <targets-file>")
    print("Example: python3 start.py targets.txt")


def validate_target_file(filename):
    target_file = Path(filename)
    if target_file.name != filename:
        print("Error: targets file must be in the project root directory.")
        sys.exit(1)
    if not target_file.is_file():
        print("Error: targets file not found: {}".format(filename))
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.strip():
        usage()
        sys.exit(1)

    validate_target_file(filename)
    rm_output_file(filename)

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
