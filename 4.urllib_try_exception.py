# 获取网站内容或访问网站失败后，得到报错信息


# 导入urllib.request,parse方法
import urllib.request,urllib.parse
import os
import ssl
# 屏蔽HTTPS协议SSL的ca认证
ssl._create_default_https_context = ssl._create_unverified_context


def get_page(url):
	headers = {
	      'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
	                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
	      'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
	      'Connection': 'keep-alive'
	}
	data = {
	    'first': 'true',
	    'pn': 1,
	    'kd': 'Python'
	}
	data = urllib.parse.urlencode(data).encode('utf-8')
	req = urllib.request.Request(url, headers=headers)
 
	try:
	    page = urllib.request.urlopen(req, data=data).read()
	    page = page.decode('utf-8')
	except error.HTTPError as e:
	    print(e.code())
	    print(e.read().decode('utf-8'))
	return page

if __name__ == '__main__':
	html = get_page('https://baidu.com')