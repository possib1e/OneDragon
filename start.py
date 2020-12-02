import os,sys
from module.scan_subdomain import start_oneforall
from module.scan_port import start_masscan_to_nmap
from module.scan_file import start_ffuf
from module.scan_vuln import start_xray_scan
from module.common import read_file
#python3 start.py targets.txt

if __name__ == '__main__':
    targets = read_file(sys.argv[1])
    for target in targets:
        os.system("rm -rf output/" + target)
        start_oneforall(target)
        start_masscan_to_nmap(target)
        start_ffuf(target)
        start_xray_scan(target)
