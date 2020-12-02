import os,csv

def start_oneforall(target):
    os.chdir('./OneForAll')
    os.system("rm results/" + target + ".csv")
    cmd ="python3 oneforall.py  --target "+target + " run"
    print(cmd)
    os.system(cmd)
    get_ips_urls_from_oneforall(target)
    os.chdir('../')

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