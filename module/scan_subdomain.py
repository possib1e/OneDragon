import os,csv
from .common import read_file
def get_ip_url_from_oneforall(filename):
    #将oneforall的结果复制到外部的output目录final-domains-ips.txt
    os.system("cat OneForAll/results/*.txt | massdns/bin/massdns --output S -q -r massdns/lists/resolvers.txt > output/"+ filename +"/final-domains-ips.txt")
    #筛选出扫描到的子域名urls_sub.txt
    os.system("cat output/"+ filename + "/final-domains-ips.txt | cut -d ' ' -f1 |rev |cut -c 2- |rev |sort -u > output/"+ filename +"/urls_sub.txt")
    os.system("sed -i 's/^/http:\/\/&/g' output/" + filename + "/urls_sub.txt")
    #筛选出子域名的IP,ips_all.txt
    os.system("cat output/"+ filename + "/final-domains-ips.txt | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' |sort -u > output/"+filename+"/ips_all.txt")
    pass

def start_oneforall(filename):
    os.system('cp targets.txt OneForAll/targets.txt')
    os.chdir('./OneForAll')
    os.system("rm -rf results/")
    cmd ="python3 oneforall.py  --targets "+filename + " run"
    print(cmd)
    os.system(cmd)
    os.chdir('../')
    #将最终结果使用massdns进行再次验证，并且拆分成ip和子域名单独文件拷贝到output目录
    get_ip_url_from_oneforall(filename)

def start_massdns(filename):
    #python3 massdns/scripts/subbrute.py massdns/lists/sub_16w.txt 832cp.cn | massdns -r massdns/lists/resolvers.txt -q -t A -o S -w 832cp.cn.txt
    for target in read_file(filename):
        os.system("python3 massdns/scripts/subbrute.py massdns/lists/sub_16w.txt "+target+" | massdns -r massdns/lists/resolvers.txt -q -t A -o S -w output/"+filename+"/"+target+".txt")
        a = os.popen("wc output/"+filename+"/"+target+".txt -l | cut -d ' ' -f1")
        length = int(a.read().strip())
        #解决泛解析问题，当子域名数量超过1000就认为泛解析了
        if(length>1000):
            os.system("rm -rf output/"+filename+"/"+target+".txt")
        else:
            # 筛选出扫描到的子域名urls_sub.txt
            os.system(
                "cat output/" + filename + "/"+target+".txt | cut -d ' ' -f1 |rev |cut -c 2- |rev |sort -u >> output/" + filename + "/urls_sub.txt")
            os.system("sed -i 's/^/http:\/\/&/g' output/" + filename + "/urls_sub.txt")
            # 筛选出子域名的IP,ips_all.txt
            os.system(
                "cat output/" + filename + "/"+target+".txt | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' |sort -u >> output/" + filename + "/ips_all.txt")

            pass

if __name__ == '__main__':
    pass
