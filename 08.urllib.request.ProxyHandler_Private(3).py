# 备注：正常情况下，为了不暴露自己的代理账户和密码，代理的账户和密码，一般会提取出来，封装到其他模块，需要的时候再调用，
# 或者使用os.environ.get()来读取和修改环境变量。

import urllib.request

url ="http://www.baidu.com/"

header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

}

# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码

authproxy_handler=urllib.request.ProxyHandler({"http" :"username:password@61.135.217.7:80"})

opener = urllib.request.build_opener(authproxy_handler)

request = urllib.request.Request(url,headers=header)

response = opener.open(request)

print(response.read().decode('utf-8'))

 
# 使用os.environ来读取和修改环境变量：

import urllib.request

import os

username=os.environ.get("username")

password =os.environ.get("password")

print(username)

print(password)

url ="http://www.baidu.com/"

header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

}

# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码

authproxy_handler=urllib.request.ProxyHandler({"http" :username+':'+"password@61.135.217.7:80"})

opener = urllib.request.build_opener(authproxy_handler)

request = urllib.request.Request(url,headers=header)

response = opener.open(request)

print(response.read().decode('utf-8'))
