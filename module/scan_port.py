import os
def start_masscan_to_nmap(target):
    os.chdir('./masscan_to_nmap')
    os.system("/bin/cp -rf ../output/" + target + "/ips.txt ip.txt")
    os.system("rm web.txt")
    os.system("rm results.txt")

    os.system("python start.py")

    os.system("/bin/cp -rf web.txt ../output/" + target + "/ip_urls.txt")
    os.system("/bin/cp -rf results.txt ../output/" + target + "/ip_port_scan_results.txt")
    os.system("cat ../output/" + target + "/ip_urls.txt ../output/" + target + "/sub_urls.txt >> ../output/" + target + "/all_urls.txt")
    os.chdir('../')
if __name__ == '__main__':
    pass
