# urllib.request库高级应用之ProxyHandler处理器_代理设置
import os
import ssl

# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context

# 单个代理IP
import urllib.request

# 获取路由url
url = 'https://www.baidu.com'

# 构造请求头信息
headers = {
}

proxies = {'http':'118.190.95.26:9001'}
# 构造两个代理Handler，一个代理IP，一个没有代理IP
httpproxy_handler = urllib.request.ProxyHandler(proxies=proxies)
nullproxy_handler = urllib.request.ProxyHandler({})

# 定义一个代理开关
proxySwitch = True

# 通过urllib.request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

 # 构造请求
request = urllib.request.Request(url=url, headers=headers)
# 发出请求，获取响应页面
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

'''
# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。

response = opener.open(request)


# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。

# urllib2.install_opener(opener)

# response = urlopen(request)

print(response.read().decode('utf-8'))
'''


