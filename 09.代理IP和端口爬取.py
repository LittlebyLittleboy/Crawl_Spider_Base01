# Python爬取西刺国内高匿代理或者快代理hip并验证

# 1.抓取ip存入文件
# 首先，我们访问西刺首页 http://www.xicidaili.com/，并点击国内高匿代理

# 提取IP和端口号，正则提取
import urllib.request
import re
import time
# 构造请求头
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}

pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})"
# pattern = r"<td>[\d\.a-zA-Z\/]+</td>"
# 指定爬取范围
for i in range(1,800):

    url = 'http://www.xicidaili.com/nn/' + str(i)
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request).read().decode('utf-8')

    # 提取ip和端口
    p = re.compile(pattern,re.S)
    ip_list = re.findall(pattern=p, string=response)

    # 将提取的ip和端口写入文件
    with open('./ip.txt','a+') as fw:
        for li in ip_list:
            ip = li[0] + ':' + li[1] + '\n'
            print(ip)
            fw.write(ip)

    # f = open("ip.txt","a+")
    # for li in ip_list:
    #     ip = li[0] + ':' + li[1] + '\n'
    #     print(ip)
    #     f.write(ip)
    # 每爬取一页暂停两秒
    time.sleep(2)