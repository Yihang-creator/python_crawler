# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2020/7/1 8:01 上午
#@Author : Yihang He 
#@File : demo31.py
#@Software: PyCharm



"""
try:
    print("------test----1-------")
    f = open("123.txt","r")
    print("------test-------2---")

except IOError:        #文件没找到，等于IO异常 （输入输出异常）
    pass
"""


# try:
#     print("------test----1-------")
#     f = open("123.txt", "r")
#     print("------test-------2---")
#
#     print(num)
# except Exception as result:     #put all the possible types of error in the little parenthesis
#     print("report errors")
#     print(result)
#
# import time
# try:
#     f = open("tests.txt","r")
#
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
#         print("close the txt")
#
# except Exception as result:
#
#
#
#     print("发生异常。。。")
#
# try:
#     fh = open("testfile1.txt","r")
#     try:
#         fh.write("this is a test file,used to test error")
#     finally:
#         print("close the file")
#         fh.close()
# except IOError:
#     print("Error: file not found or fail to read the file")
# finally 写在里面可以避免fh产生错误未定义，而导致再次出错

fh = open("gushi.txt","w")

fh.write("寒蝉凄切，对长亭晚，骤雨初歇。\n都门帐饮无绪，留恋处，兰舟催发\n"
         "执手相看泪眼，竟无语凝噎。\n念去去，千里烟波。暮霭沉沉楚天阔。\n多情自古伤离别，"
         "更那堪，冷落清秋节！\n"
         "今宵酒醒何处？杨柳岸，晓风残月。\n"
         "此去经年。应是良辰好景虚设。\n"
         "便纵有千种风情，更与何人说？")

fh.close()

def readfile(a):
    file = open(a,"r")
    whole_text = ""
    for line in file.readlines():
        whole_text = whole_text + line
    file.close()
    return whole_text
print(readfile("gushi.txt"))

def copyfile(txt):
    fh = open("copy.txt","w")
    fh.write(txt)
    fh.close()
    print("copy complete")

copyfile(readfile("gushi.txt"))

