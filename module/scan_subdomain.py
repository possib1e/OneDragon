import os,csv
def get_ip_url_from_oneforall(filename):
    os.system("cat OneForAll/results/*.txt | massdns/bin/massdns --output S -q -r massdns/lists/resolvers.txt > output/"+ filename +"/final-domains-ips.txt")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | cut -d ' ' -f1 |rev |cut -c 2- |rev |sort -u > output/"+ filename +"/urls_sub.txt")
    os.system("sed -i 's/^/http:\/\/&/g' output/" + filename + "/urls_sub.txt")
    os.system("cat output/"+ filename + "/final-domains-ips.txt | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' |sort -u > output/"+filename+"/ips_all.txt")
    pass

def start_oneforall(filename):
    os.chdir('./OneForAll')
    os.system("rm -rf results/")
    cmd ="python3 oneforall.py  --targets "+filename + " run"
    print(cmd)
    os.system(cmd)
    os.chdir('../')
    #将最终结果使用massdns进行再次验证，并且拆分成ip和子域名单独文件拷贝到output目录
    get_ip_url_from_oneforall(filename)

if __name__ == '__main__':
    pass