# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/6/28 8:48 下午
#@Author : Yihang He 
#@File : demo2.py
#@Software: PyCharm


"""
age=18

print("my age is %d sui"%age)
print('my name is %s, my nationality is %s'%("yihang","China"))
"""
# password = input("请输入密码")
# print("the password you just entered")
#
# a=10
# print(type(password))
# if False:
#     print("True")
# else:
#     print("False")


import random

x=random.randint(0,2)

y=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
if y==0:
    if x==1:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("剪刀（0)",x,"you lose"))
    elif x==0:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("剪刀（0)",x,"it's a tie"))
    elif x==2:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("剪刀（0)",x,"you win"))
elif y==1:
    if x==2:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"you lose"))
    elif x==1:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"it's a tie"))
    elif x==0:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"you win"))
elif y==2:
    if x==0:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"you lose"))
    elif x==2:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"it's a tie"))
    elif x==1:
        print("你的输入为：%s \n 随机生成数字为：%s \n 哈哈，%s ：）"%("石头（1)",x,"you win"))
else:
    print("输入错误")