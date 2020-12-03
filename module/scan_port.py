import os
def start_masscan_to_nmap(filename):
    os.chdir('./masscan_to_nmap')
    os.system("/bin/cp -rf ../output/" + filename + "/final-ips.txt ip.txt")
    os.system("rm web.txt")
    os.system("rm results.txt")

    os.system("python start.py")

    os.system("/bin/cp -rf web.txt ../output/" + filename + "/ip_urls.txt")
    os.system("/bin/cp -rf results.txt ../output/" + filename + "/ip_port_scan_results.txt")
    os.system("cat ../output/" + filename + "/ip_urls.txt ../output/" + filename + "/sub_urls.txt >> ../output/" + filename + "/all_urls.txt")
    os.chdir('../')

if __name__ == '__main__':
    pass
