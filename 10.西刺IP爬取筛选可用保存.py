# 提取可用ip并存入文件
# 爬取的 ip 有大量都是不可用的，我们需要将可用的 ip 提取出来，这里我们使用站长之家的 ip 查询 http://ip.chinaz.com/

import urllib
import socket
socket.setdefaulttimeout(3)

inf = open("ip.txt")    # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://ip.chinaz.com/getip.aspx"
# 将可用ip写入valid_ip.txt
ouf = open("valid_ip.txt", "a+")

for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        valid_ip = proxy['http'][7:]
        print('valid_ip: ' + valid_ip)
        ouf.write(valid_ip)
    except Exception as e:
        print(proxy)
        print(e) 
        continue