# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2021/1/9 12:09 上午
#@Author : Yihang He 
#@File : 爬取股票.py
#@Software: PyCharm



from bs4 import BeautifulSoup          #网页解析，获取数据
import re           #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import xlwt
import sqlite3
import time
import json

# 平时我们浏览网页，就是通过浏览器发出请求，服务器接受到请求之后，响应我们的请求。
# 爬虫就是通过模拟浏览器的行为发出请求，把获得的数据进行处理。爬虫的优势在于可以快速的，批量的获得信息，对信息进行处理和保存。
# 我们浏览的网页其实是由html这门语言翻译而成的。我们在网站每一个字符都在html都有对应的位置。我们可以通过找到我们需要的信息的位置，寻找这个位置的规律。
# 找到规律之后，就可以用特殊的工具去提炼出网页中满足这个规律的所有字符。



#http://data.eastmoney.com/zjlx/list.html
def main():
    baseurl_half1 = "http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery1123013290190941055435_1610176856103&fid=f184&po=1&pz=50&pn="

    baseurl_half2 = "&np=1&fltt=2&invt=2&fields=f2%2Cf3%2Cf12%2Cf13%2Cf14%2Cf62%2Cf184%2Cf225%2Cf165%2Cf263%2Cf109%2Cf175%2Cf264%2Cf160%2Cf100%2Cf124%2Cf265&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2"
    #1.爬取网页
    datalist = getData(baseurl_half1,baseurl_half2)
    savepath = "stocks.xls"
    #3.保存数据
    saveData(datalist,savepath)

    #askURL("https://movie.douban.com/top250?start=0")

#股票代码
findNo = re.compile(r'"f12":(.*),"f13"')
#股票名称
findName = re.compile(r'<img.*src="(.*?)"',re.S) #re.S 让换行符包含在字符中
#股票最新价

#今日排行榜股票主力净占比
#今日排行榜股票今日排名
#今日排行榜股票今日涨跌

#5日排行榜股票主力净占比
#5日排行榜股票今日排名
#5日排行榜股票今日涨跌

#10日排行榜股票主力净占比
#10日排行榜股票今日排名
#10日排行榜股票今日涨跌

#所属板块





#爬取网页
def getData(baseurl1,baseurl2):
    datalist = []

    for i in range(1,86): #调用获取页面信息的函数，86次
        time.sleep(0.1)
        url = baseurl1 + str(i) + baseurl2
        html = askURL(url)         #保存获取到的网页源码
        text = re.findall(r'\"diff\":(.+)}}',html)
        jsonObj = json.loads(text[0])
        for item in jsonObj:
            data = []
            data.append(item["f12"] )#股票代码
            data.append(item["f14"]) # 股票名称
            data.append(item["f2"]) # 股票最新价

            data.append(item["f184"]) # 今日排行榜股票主力净占比
            data.append(item["f225"]) # 今日排行榜股票今日排名
            data.append(item["f3"]) # 今日排行榜股票涨跌

            data.append(item["f165"]) # 5日排行榜股票主力净占比
            data.append(item["f263"]) # 5日排行榜股票今日排名
            data.append(item["f109"]) # 5日排行榜股票涨跌

            data.append(item["f175"]) # 10日排行榜股票主力净占比
            data.append(item["f264"]) # 10日排行榜股票今日排名
            data.append(item["f160"])# 10日排行榜股票涨跌

            data.append(item["f100"]) # 所属板块
            datalist.append(data)


    #print(datalist)
    return datalist




#得到指定一个URL的网页内容
def askURL(url):
    head = {        #模拟浏览器头部信息，向豆瓣服务器发送信息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                          "/83.0.4103.116 Safari/537.36"
            }
                     #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，
                     # 浏览器（本质上高速浏览器，我们可以接受什么水平的文件）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        reponse = urllib.request.urlopen(request)
        html = reponse.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

 #3.保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('stock market', cell_overwrite_ok=True)
    col = ("#股票代码", "股票名称", "股票最新价", "今日排行榜股票主力净占比", "今日排行榜股票排名", "今日排行榜股票涨跌", "5日排行榜股票主力净占比",
           "5日排行榜股票排名","5日排行榜股票涨跌","10日排行榜股票主力净占比",
           "10日排行榜股票排名","10日排行榜股票涨跌","所属板块")
    for i in range(0, 13):
        sheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, 13):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)




if __name__ == "__main__":    #当程序执行时
    #调用函数
    main()
