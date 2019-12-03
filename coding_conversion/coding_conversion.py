"""
批量文件处理：将GBK编码的文件转化为UTF-8编码
代码来自于：https://www.jianshu.com/p/164f91f51dbc
"""

import os
path = './'      #文件夹目录
files= os.listdir(path)             #得到文件夹下的所有文件名称
for file in files:                  #遍历文件夹
     if not os.path.isdir(file):    #判断是否是文件夹，不是文件夹才打开
         try:
             fGBK = open(path+'\\'+file,'r',encoding='gbk')  #尝试打开文件,打不开说明不是gbk编码,进入异常处理
             content = fGBK.read()  # 无异常则继续转换
             fGBK.close()
             fUTF = open(path + '\\' + file, 'w', encoding='utf-8')
             fUTF.write(content)
             fUTF.close()
             print(file + '已经转换为UTF-8')
         except:
             print(file + '不是GBK编码')