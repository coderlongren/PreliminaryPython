#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pymysql
import importlib

importlib.reload(sys)
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
class ReadFile:
    # 处理 middle的 文本
    def readLines(self):
        f = open(r'E:\middle.txt' , 'r')
        f2 =open(r'E:\newmiddle.txt' , 'w')
        list="["
        for line in f:
            str1 = ""
            str2 = ""
            flag = False
            next = False
            if len(line) == 1 or (line[0] >= 'A' and line[0] <= 'Z'):
                continue
            for c in line:
                if c != ' ' and flag == False:
                    str1 = str1 + c
                elif c == ' ' and flag == False:
                    flag = True
                else:
                    str2 = str2 + c
            sql =  "INSERT INTO middle(english,chinese) VALUES ('%s', '%s')" % (str1, str2)
            print(sql)
            # 执行
            cursor.execute(sql)
            db.commit()
            list = list + "[" + '"' + str1 + "," + '"' + "]" +  ","
            # f.wirite()
        f2.write(list)
        f.close()
        # print("ok")
        # f = open(r'E:\newMiddle.txt', 'w')
        with open(r'E:\newMiddle.txt','w') as f:
            # 乱序
            shuffle(list)
            for line in list:
                f.write(line)
        # f.close()
    # 重写
    def reWrite(self,list):
        f = open(r'E:\newMiddle.txt', 'w')
        # 乱序
        shuffle(list)
        for line in f:
            f.write(line)
        f.close()


if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()