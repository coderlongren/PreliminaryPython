#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import pymysql
from random import  shuffle
import importlib

importlib.reload(sys)
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "rensailong", "wordwar")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
class ReadFile:
    def readLines(self):
        list=[]
        i = 0
        f = open(r'E:\GRE.txt', 'r',encoding='UTF-8')
        for line in f:
            print(line)
            data1 = ""
            data2 = ""
            flag = False
            for c in line:
                if c != ' ' and flag != True:
                    data1 = data1+c
                elif c != ' ' and flag == True:
                    data2 = data2 + c
                else:
                    flag = True
            str = data1 +" "+data2
            list.append(str)
        f.close()
        shuffle(list)
        # 重新写入文件
        f = open(r'E:\newGRE.txt', 'w',encoding='UTF-8')
        for line in list:
            f.write(line)
        # print(len(list))
        f.close()

if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()