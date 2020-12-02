import os,sys
from OneDragon.module.scan_subdomain import start_oneforall
from OneDragon.module.scan_port import start_masscan_to_nmap
from OneDragon.module.scan_file import start_ffuf
from OneDragon.module.scan_vuln import start_xray_scan
from OneDragon.module.common import read_file
#python3 start.py targets.txt

if __name__ == '__main__':
    targets = read_file(sys.argv[1])
    for target in targets:
        os.system("rm -rf output/" + target)
        start_oneforall(target)
        start_masscan_to_nmap(target)
        start_ffuf(target)
        start_xray_scan(target)
