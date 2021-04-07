# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/6/30 1:31 上午
#@Author : Yihang He 
#@File : demo12.py
#@Software: PyCharm

products= [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

# question1
print("------  商品列表 ------")
num=0
for i in products:
    print("%d\t%s\t%s"%(num,i[0],i[1]))
    num += 1
    print("\n")

# question2 根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，
# 最终用户输入q退出是，打印购买的商品列表
shopping_cart=[]
while True:
    command1 = input("输入商品编号加入购物车或输入q退出：")
    if command1 == "q":
        break

    try:
       command2 = int (command1)
    except ValueError:
        print("输入错误")
    else:

        if command2 not in range(0,6):
            print ("输入错误")
        else:
            products[command2].insert(0,command2)
            shopping_cart.append(products[command2])
print("------  商品列表 ------")
for i in shopping_cart:
    print("%d\t%s\t%s"%(i[0],i[1],i[2]))
    print("\n")








