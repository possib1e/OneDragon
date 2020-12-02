import os

def start_xray_scan(target):
    os.chdir('./xray')
    os.system("rm log.xray.log")
    os.system("ps aux|grep [.]/xray|awk '{print $2}'|xargs kill -9")
    os.system("mkdir output")
    print("nohup ./xray_linux_amd64 webscan --listen 172.17.0.1:7777 --html-output ../output/" + target + "/__datetime__.html > log.xray.log 2>&1 &")
    os.system("nohup ./xray_linux_amd64 webscan --listen 172.17.0.1:7777 --html-output ../output/" + target + "/__datetime__.html > log.xray.log 2>&1 &")

    start_awvs_crawl(target)
    os.chdir('../')

def start_awvs_crawl(target):
    os.chdir('./awvs')
    print("python3 start.py")
    os.system("cp ../../output/" + target + "/all_urls.txt -f url.txt")
    os.system("python3 start.py")


if __name__ == '__main__':
    pass
