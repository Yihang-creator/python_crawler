# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/1 8:26 下午
#@Author : Yihang He 
#@File : python爬虫.py
#@Software: PyCharm


from bs4 import BeautifulSoup          #网页解析，获取数据
import re           #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = "douban movie TOP250.xls"
    #3.保存数据
    saveData(datalist,savepath)

    #askURL("https://movie.douban.com/top250?start=0")

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
#影片图片规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S 让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*)</p>',re.S)


#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)         #保存获取到的网页源码



        # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div", class_="item") : #查找符合要求的字符串，形成列表
            #print(item)  #测试：查看电影item全部信息
            data = []  #保存一部电影的所有信息
            item = str(item)
            print(item)
            #影片详情的链接
            link = re.findall(findLink,item)[0]  #re库用来通过正则表达式查找指定的字符串
            data.append(link)


            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            #添加图片
            titles = re.findall(findTitle,item)   #片名可能只有中文名，没有外国名
            if len(titles) ==2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","") #去掉无关的符号
                data.append(otitle)    #添加外国名
            else:
                data.append(titles[0])
                data.append(" ")  #外国名留空


            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")  #去掉句号
                data.append(inq)         #添加概述
            else:
                data.append(" ")        #留空


            bd = re.findall(findBd,item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?"," ",bd)   #去掉<br/>
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())   #去掉前后的空格

            datalist.append(data)   #把处理好的一部电影信息放进datalist里面

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
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression= 0)
    sheet = book.add_sheet('douban movie top 250',cell_overwrite_ok=True)
    col = ("电影详情链接","photo link","movie chinese name","movie foreign name","rating","times rated","intro","related stuff")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)




if __name__ == "__main__":    #当程序执行时
    #调用函数
    main()
