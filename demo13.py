# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/6/30 11:44 下午
#@Author : Yihang He 
#@File : demo13.py
#@Software: PyCharm
#
# tup1 = ("abc","def",2000,2020)
#
# print(tup1[0])
# print(tup1[1:5]) #左闭右开

#add
# tup1= (12,34,56)
# #tup1[0] = 100  #report error, does not support item assignment
# tup2 = ("abc","xyz")
#
# tup = tup1 + tup2
# print (tup)


#
#
#
# #delete
# tup1= (12,34,56)
# print (tup1)
# #tup1[0] = 100  #report error, does not support item assignment
#
#
# del tup1        #delete the whole variable in the memory
# print(tup1)
#
#
#
# #change

#dict（字典）字典是
#无序的对象集合，使用键-值（key-value）存储，具有极快的查找速度。
#键（key）必须使用不可变类型
#同一个字典中，键必须是唯一的

# info = {"name": "吴彦祖","age":18}
# print(info["name"])
# print(info["age"])
#
# #访问不存在的键
# print(info["gender"]) # 直接访问会报错
#
# print(info.get("gender","m")) # using get method,return NOne if nothing is found

#增
# info = {"name": "吴彦祖","age":18}
# newID = input("please enter new ID:")
# info["id"] = newID
#
# print(info["id"])

#删
info = {"name": "吴彦祖","age":18}
print("删除前：%s"%info["name"])

#del delete the whol variable


#clear 清空但不删除





#改



#查
# print(info.keys())
#
# print(info.values())
#
# print(info.items())
#
# for key in info.keys():
#     print(key)
#
# for value in info.values():
#     print(value)
for key,value in info.items():
    print("key=%s, value=%s"%(key,value))

mylist = ["a", "b", "c","d"]



#use enumerate function
for i,x in enumerate(mylist):
    print(i,x)
