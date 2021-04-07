# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/1 1:48 上午
#@Author : Yihang He 
#@File : demo22.py
#@Software: PyCharm

# f = open("test.txt","w")  #open files
#
# f.write("hello")  #将字符串写入文件中
#
#
# f.close()  #close files

#read方法，读取指定的字符，开始时定位在文件头部，没执行一次向后移动指定字符数

f=open("test.txt","r")

content=f.read(5)
print(content)
content=f.read(5)
print(content)

f.close()

"""f=open("test.txt","r")

content=f.readline()
print("1: %s"%content)

content=f.readline()
print("2: %s"%content)
content=f.readline()
print("3: %s"%content)
content=f.readline()
print("4: %s"%content)


f.close()
"""
# f=open("test.txt","r")
#
# content=f.readlines()
#
# print(content)
#
# i=1
# for temp in content:
#     print("%d:%s"%(i,temp))
#     i += 1
#
# f.close()

import os

os.rename("test.txt","tests.txt")


