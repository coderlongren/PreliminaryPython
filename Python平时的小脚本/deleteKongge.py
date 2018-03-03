#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

importlib.reload(sys)
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
class ReadFile:
    def readLines(self):
        list=[]
        i = 0
        f = open(r'E:\level6.txt', 'r')
        for line in f:
            # print(line)
            # data1 = ""
            # data2 = ""
            # flag = False
            # for c in line:
            #     if c != ' ' and flag != True:
            #         data1 = data1+c
            #     elif c != ' ' and flag == True:
            #         data2 = data2 + c
            #     else:
            #         flag = True
            # str = data1 +" "+data2
            # 删除每一行 后面的空格
            print("原来的长度",len(line))
            line.rstrip()
            print("现在的长度,",(len(line)))
            list.append(line)
        f.close()
        shuffle(list)
        # 重新写入文件
        f = open(r'E:\newlevel6.txt', 'w')
        for line in list:
            f.write(line)
        # print(len(list))
        f.close()

if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()