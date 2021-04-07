# -*- coding = utf-8 -*-
#Author: Yihang He
#@Time : 2021/1/4 7:00 上午
#@Author : Yihang He 
#@File : testXwlt.py
#@Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding= "utf-8")      #创建workbook对象
worksheet = workbook.add_sheet("sheet_1")        #创建工作表
worksheet.write(0,0,"hello")   #写入数据 第一个参数为行 第二个参数为列 第三个为参数内容
workbook.save("student.xls")       #保存数据表