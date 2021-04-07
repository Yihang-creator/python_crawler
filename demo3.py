# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/6/30 12:04 上午
#@Author : Yihang He 
#@File : demo3.py
#@Software: PyCharm

# for i in range(5):
#     print(i)
#
# for i in range(-10,-100,-30):
#     print(i)
#
# name = "chengdu"
#
# for x in name :
#     print(x,end="\t")
"""
a = ["aa","bb","cc","dd"]

for i in range(len(a)):
    print(i,a[i])
"""
"""
i = 0
while i < 5:
    print("当前事第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i+=1
"""
"""
i=1
sum=0
while i <=100:
    sum += i
    i += 1
print(sum)
"""
"""
i=0

while i < 10:
    i = i+1
    print ("-"*30)
    if  i==5:
        break
    print (i)
"""

for i in range(1,10):
    for j in range(1,i+1):
        print ("%d*%d=%d"%(i,j,i*j),end="\t")
    print("\n")