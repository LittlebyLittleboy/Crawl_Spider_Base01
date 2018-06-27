# urllib.parse.urlencode()方法的使用
'''
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
'''

'''urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None)

urlencode（）主要作用就是将url附上要提交的数据。
'''

'''
经过urlencode（）转换后的data数据为?first=true?pn=1?kd=Python，最后提交的url为

http://www.lagou.com/jobs/positionAjax.json?first=true?pn=1?kd=Python

Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
'''

# 导入urllib.request,parse方法
import urllib.request,urllib.parse
import os
import ssl
# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context

# 获取路由地址，安全版协议
url = r'http://www.lagou.com/jobs/positionAjax.json?'

# 构造请求头，进行第一层伪装
headers = {
      'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
      'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
      'Connection': 'keep-alive'
  }

# post表单提交数据构造
form = {
 'first': 'true',
 'pn': 1,
 'kd': 'Python'
}

# 将表单要提交的数据附在路由url上
data = urllib.parse.urlencode(form).encode('utf-8')

# 构造请求
request = urllib.request.Request(url=url,data=data)

# urllib模拟浏览器发出请求，response接收响应的页面
response = urllib.request.urlopen(request)

# 对HTTPResponse类型数据进行操作，得到二进制类型数据
bytes = response.read()

# 二进制类型数据解码得到字符串类型
str = bytes.decode('utf-8')

# 打印输出html页面内容
print(str)

# 存放文件的路径
path = os.path.join(os.path.abspath('.'),'lagou.html')

# 获取的页面内容写入文件
with open(path,mode='w') as fw:
	fw.write(str)