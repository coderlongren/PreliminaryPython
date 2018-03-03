#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import pymysql
import importlib
from random import  shuffle

importlib.reload(sys)
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "rensailong", "wordwar")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
class ReadFile:
    def readLines(self):
        list=[]
        dict = {"abc":"abc"}
        i = 0
        f = open(r'E:\newlevel6.txt', 'r')
        for line in f:
            strs = line.split(" ")
            line.rstrip()
            dict[strs[0]] = strs[1]
        f.close()
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