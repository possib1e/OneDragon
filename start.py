import sys
from module.scan_subdomain import start_oneforall
from module.scan_port import start_masscan_to_nmap
from module.scan_file import start_ffuf
from module.scan_vuln import start_xray_scan
from module.common import rm_output_file
#python3 start.py targets.txt

if __name__ == '__main__':
    filename = sys.argv[1]
    rm_output_file(filename)

    #输入target.txt
    #输出output/target.txt/下的 final-domains-ips.txt urls_sub.txt ips_all.txt
    start_oneforall(filename)

    #输入output/target.txt下的 ips_all.txt urls_sub.txt
    #输出output/target.txt下的 ip_port_scan_results.txt urls_ip.txt urls_all.txt
    start_masscan_to_nmap(filename)

    #输入output/target.txt下的 urls_all.txt
    #输入output/target.txt下的 ffuf_all.csv ffuf_redup.txt
    start_ffuf(filename)

    # 输入output/target.txt下的 urls_all.txt
    # 输出xary下的扫描报告
    start_xray_scan(filename)
