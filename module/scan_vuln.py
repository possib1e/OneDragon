import os
from .common import read_file

def start_xray_scan(filename):
    os.chdir('./xray')
    os.system("rm log.xray.log")
    os.system("ps aux|grep [.]/xray|awk '{print $2}'|xargs kill -9")
    os.system("mkdir output")
    urls = read_file('../output/' + filename + '/all_urls.txt')
    print("nohup ./xray_linux_amd64 webscan --listen 172.17.0.1:7777 --html-output ../output/" + filename + "/__datetime__.html > log.xray.log 2>&1 &")
    os.system("nohup ./xray_linux_amd64 webscan --listen 172.17.0.1:7777 --html-output ../output/" + filename + "/__datetime__.html > log.xray.log 2>&1 &")

    start_awvs_crawl(filename)
    os.chdir('../')

def start_awvs_crawl(filename):
    os.chdir('./awvs')
    os.system("/bin/cp -rf  ../../output/" + filename + "/all_urls.txt url.txt")
    print("python3 start.py")
    os.system("python3 start.py")


if __name__ == '__main__':
    pass
