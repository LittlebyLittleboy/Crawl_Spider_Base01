# urllib.request.Request()方法的使用
'''
urllib.request.Request(url, data=None, headers={}, method=None)

使用request（）来包装请求，再通过urlopen（）获取页面。
'''

'''
用来包装头部的数据：

-         User-Agent ：这个头部可以携带如下几条信息：浏览器名和版本号、操作系统名和版本号、默认语言

-         Referer：可以用来防止盗链，有一些网站图片显示来源http://***.com，就是检查Referer来鉴定的

-         Connection：表示连接状态，记录Session的状态。
'''

# 导入urllib.request方法
import urllib.request
import os
import ssl
# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context

# 获取路由地址，安全版协议
url = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='

# 构造请求头，进行第一层伪装
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
  'Referer': 'https://movie.douban.com/chart',
  'Connection': 'keep-alive'
  }

# 构造请求
request = urllib.request.Request(url,headers=headers)

# 增加请求头信息
request.add_header('Host','movie.douban.com')

# urllib模拟浏览器发出请求，response接收响应的页面
response = urllib.request.urlopen(request)

# 对HTTPResponse类型数据进行操作，得到二进制类型数据
bytes = response.read()

# 二进制类型数据解码得到字符串类型
str = bytes.decode('utf-8')

# 打印输出html页面内容
print(str)

# 存放文件的路径
path = os.path.join(os.path.abspath('.'),'douban.html')

# 获取的页面内容写入文件
with open(path,mode='w') as fw:
	fw.write(str)
