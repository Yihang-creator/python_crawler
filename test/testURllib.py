# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/4 2:41 上午
#@Author : Yihang He 
#@File : testURllib.py
#@Software: PyCharm

import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
#
# print(response.read().decode("utf-8")) #对获取到的网页源码进行utf-8解码

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode())

#超时处理
# try:
#
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout = 1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print ("time out!")

# reponse = urllib.request.urlopen("http://www.baidu.com",timeout = 1)
# print(reponse.getheader("server"))


# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# headers= {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"Eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers= {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))