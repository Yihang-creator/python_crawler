# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/1 1:06 上午
#@Author : Yihang He 
#@File : demo21.py
#@Software: PyCharm

def printinfo():
    print("---------------------")
    print("   人生苦短 我用python")
    print("---------------------")

printinfo()

def add2Num(a,b):
    return a+b

print(print(add2Num(11,22)))

def divide(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu

sh,yu = divide(5,2) #需要使用多个值老保存返回内容
print(sh)
print(yu)

def test1():
