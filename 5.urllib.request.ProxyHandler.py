# 使用代理
'''
urllib.request.ProxyHandler(proxies=None)

当需要抓取的网站设置了访问限制，这时就需要用到代理来抓取数据。
'''
# 导入urllib.request,parse方法
import urllib.request,urllib.parse
import os
import ssl
# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com'

data = {
     'first': 'true',
     'pn': 1,
     'kd': 'Python'
 }
proxy = urllib.request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy

opener = urllib.request.build_opener(proxy)  # 挂载opener

urllib.request.install_opener(opener)  # 安装opener

data = urllib.parse.urlencode(data).encode('utf-8')

page = opener.open(url, data).read()

page = page.decode('utf-8')

print(page)