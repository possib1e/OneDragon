import os,csv
def start_oneforall(filename):
    os.chdir('./OneForAll')
    os.system("rm -rf results/")
    cmd ="python3 oneforall.py  --targets "+filename + " run"
    print(cmd)
    os.system(cmd)
    os.chdir('../')
    get_ip_url_from_oneforall(filename)


def get_ip_url_from_oneforall(filename):
    os.system("cat OneForAll/results/*.txt | massdns/bin/massdns --output S -q -r massdns/lists/resolvers.txt > output/"+ filename +"/final-domains-ips.txt")
    os.system("sleep 1")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | cut -d " " -f1 |rev |cut -c 2- |rev |sort -u > output/"+ filename +"/sub_urls.txt")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' |sort -u > output/"+filename+"/final-ips.txt")
    pass

def get_ips_urls_from_oneforall(target):
    ips_all = []
    urls_all = []
    csv_name = "/root/tools/OneDragon/OneForAll/results/" + target + ".csv"
    with open(csv_name, 'r', encoding='utf-8') as f:
        rows = csv.reader(f)  # 去掉首行
        next(rows)
        for row in rows:
            ips = row[8].split(',')
            for ip in ips:
                ips_all.append(ip)
            urls_all.append(row[4])

        ips_all = set(ips_all)
        urls_all = set(urls_all)

        os.system("mkdir ../output/" + target)

        with open('../output/'+ target +'/ips.txt', 'a', encoding='utf-8') as f_ip:
            for ip in ips_all:
                f_ip.write(ip + '\n')
        with open('../output/'+ target +'/sub_urls.txt', 'a', encoding='utf-8') as f_url:
            for url in urls_all:
                f_url.write(url + '\n')

if __name__ == '__main__':
    pass