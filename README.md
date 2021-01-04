## 2020.12.02 项目介绍

### OneDragon 安全圈一条龙服务

全自动化挖洞，助力挖SRC的赏金猎人白帽子，一键实现子域名扫描，全端口扫描，目录扫描，漏洞扫描。

## 2021.1.4 更新使用说明

### 使用说明

将目标主域名填入target.txt中即可，例如baidu.com

`python3 start.py target.txt`
### 会自动进行如下的操作

1.使用oneforall进行子域名的扫描

https://github.com/shmilylty/OneForAll

2.使用masscan+nmap进行全端口的扫描

https://github.com/robertdavidgraham/masscan

https://github.com/nmap/nmap

3.使用ffuf进行常规目录扫描

https://github.com/ffuf/ffuf

4.使用awvs爬虫和xray进行漏洞的扫描

https://github.com/chaitin/xray