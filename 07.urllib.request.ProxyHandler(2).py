# 如果代理IP足够多，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。
# 另外还可以使用延时，减少被反爬虫


# 代理IP列表随机抽取
import urllib.request
import random
import os
import ssl

# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context
# 获取路由url
url = 'https://www.baidu.com'
# 构造请求头
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

}

# 定义代理列表
proxy_list = [

    {"http" : "61.135.217.7:80"},

    {"http" : "111.155.116.245:8123"},

    {"http" : "122.114.31.177:808"},

]

# 随机选择一个代理
proxies = random.choice(proxy_list)

# 构造代理
httpproxy_handler=urllib.request.HTTPHandler({'http':'118.190.95.26:9001'})
# 通过urllib.request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
opener = urllib.request.build_opener(httpproxy_handler)
# 构造请求
request = urllib.request.Request(url=url,headers=headers)
# 发出请求，获取响应
response = opener.open(request)
# 对HTTPResponse类型数据进行操作，得到二进制类型数据
bytes = response.read()

# 二进制类型数据解码得到字符串类型
str = bytes.decode('utf-8')

# 打印输出html页面内容
print(str)

# 存放文件的路径
path = os.path.join(os.path.abspath('.'), 'ProxyHandler.html')

# 获取的页面内容写入文件
with open(path, mode='w') as fw:
    fw.write(str)

