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

    #start_oneforall(filename)
    start_masscan_to_nmap(filename)
    start_ffuf(filename)
    start_xray_scan(filename)
