# urllib.urlopen()方法的使用
'''
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

-         url:  需要打开的网址

-         data：Post提交的数据

-         timeout：设置网站的访问超时时间

直接用urllib.request模块的urlopen（）获取页面，page的数据格式为bytes类型，需要decode（）解码，转换成str类型。
'''

'''
urlopen返回对象提供方法：

-         read() , readline() ,readlines() , fileno() , close() ：对HTTPResponse类型数据进行操作

-         info()：返回HTTPMessage对象，表示远程服务器返回的头信息

-         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到

-         geturl()：返回请求的url
'''

# 导入urllib.request方法
import urllib.request
import os
import ssl
# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context

# 获取路由地址，安全版协议
url = 'https://python.org'

# urllib模拟浏览器发出请求，response接收响应的页面
response = urllib.request.urlopen(url=url)

# 对HTTPResponse类型数据进行操作，得到二进制类型数据
bytes = response.read()

# 二进制类型数据解码得到字符串类型
str = bytes.decode('utf-8')

# 打印输出html页面内容
print(str)

# 存放文件的路径
path = os.path.join(os.path.abspath('.'),'python.html')

# 获取的页面内容写入文件
with open(path,mode='w') as fw:
	fw.write(str)
