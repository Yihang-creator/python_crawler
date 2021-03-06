# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/5 9:30 下午
#@Author : Yihang He 
#@File : testBS4.py
#@Software: PyCharm

"""
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以规划为4种

- Tag
— NavigableString
- BeautifulSoup
- Comment

"""

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")
#
# print(bs.title)
# print(bs.a)
# print(bs.head)


#1. Tag 标签及其内容：拿到他所找到的第一个内容


# print(bs.title.string)

#2.Navaigable string 标签里的内容

# print(bs.a.attrs)
# print(type(bs))

#3.BeautifulSoup 表示整个文档


#print(bs.name)
# print(bs.attrs)

#print(type(bs.a.string))     #是一个特殊的Navigable String comment


#------------------------------















#文档的遍历
#
# print(bs.head.contents)
# print(bs.head.contents[1])







#文档的搜索

#(1) find_all()
#字符串过滤：会查找与字符串完全匹配的内容
# t_list= bs.find_all("a")


#正则表达式搜索：使用search 方法来匹配内容
import re
t_list = bs.find_all(re.compile("a"))


# #方法 ： 传入一个函数（方法），根据函数的要求来搜索 (了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)

# for item in t_list:
#     print(item)

#2.kwargs 参数

# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_= True)
# t_list = bs.find_all(href="http://news.baidu.com")
#
# for item in t_list:
#     print(item)

#3. text 参数
#
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text= re.compile("\d")) #应用正则表达式来查找包含特定文本的内容
# for item in t_list:
#     print(item)

#4.limit 参数
# t_list = bs.find_all("a",limit=3)
#
# for item in t_list:
#     print(item)
#
#

#css 选择器
#t_list = bs.select("title")  #通过标签来查找

# t_list = bs.select(".mnav")   #通过类名来查找


# t_list = bs.select("#u1")  #通过id来查找

# t_list = bs.select("a[class='bri']")  #通过属性来查找

# t_list = bs.select("head > title")  #通过子标签来查找

t_list =bs.select(".mnav ~.bri")

print(t_list[0].get_text())

for item in t_list:
    print(item)


