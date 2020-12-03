import os
def get_ip_url_from_oneforall(filename):
    os.system("cat OneForAll/results/*.txt | massdns/bin/massdns --output S -q -r massdns/lists/resolvers.txt > output/"+ filename +"/final-domains-ips.txt")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | cut -d ' ' -f1 |rev |cut -c 2- |rev |sort -u > output/"+ filename +"/sub_urls.txt")
    os.system("sed -i 's/^/http:\/\/&/g' output/" + filename + "/sub_urls.txt")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' |sort -u > output/"+filename+"/final-ips.txt")
    pass

def start_masscan_to_nmap(filename):
    get_ip_url_from_oneforall(filename)

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
