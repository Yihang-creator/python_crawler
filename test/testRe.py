# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/6 12:30 上午
#@Author : Yihang He 
#@File : testRe.py
#@Software: PyCharm


#正则表达式：字符串模式 （判断字符串是否符合一定的标准）

import re

#创建模式对象

pat = re.compile("AA")   #此处的AA，
# m = pat.search("CBA")   #search字符串被校验
# m = pat.search("AACBAADDCCAAA")   #用search方法，进行比对查找


# m=re.search("asd","Aasd")   #前面的字符串是规则，后面的字符串是查找对象
#
#
# print(m)
#
# print(re.findall("[A-Z]+","ASDaDFGAa"))




#sub

print(re.sub("a","A","abcdcasd"))  #找到a用A替换，在第三个字符串查找"A"

#建议在正则表达式中，被比较的字符串面前加上r，不用担心转义字符的问题

a = r"\aabd-\'"
print(a)

