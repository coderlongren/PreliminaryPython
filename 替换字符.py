#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def readLines(self):
        # f = codecs .open(r'E:\toeflTest.txt' , 'r' , 'utf-8' )
        f = codecs .open(r'E:\newtoeflTest.txt' , 'r' , 'utf-8' )
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # Sql 查询
        sqltoefl = "select * from toefl"
        sqlLevel4 = "select * from level4"
        sqllevel6 = "select * from level6"
        try:
            # cursor.execute(sqllevel6)
            # result = cursor.fetchall()
            i = 1
            list = []
            for line in f:
                line = line[:-2]
                if i == 1:
                    english = ""
                    for c in line:
                        if c == '+':
                            continue
                        english = english + c
                    print(english)
                if i == 2:
                    # 中文有几个意义
                    yiyi = line.split("#")
                    chinese = ""
                    for one in yiyi:
                        if one != "":
                            res = ""
                            flag = True
                            for c in one:
                                if c == "(":
                                    flag = False

                                if c == ")":
                                    flag = True

                                if flag == True:
                                    res = res + c

                            chinese = chinese + res + ";"



                if i == 4:
                    list.append(english + " " + chinese)
                    # print(list)
                    i = 0

                i = i + 1
                print(i)
            # 重新写入
            for line in list:
                f1.write(line + "\n")


        except IOError as e:
                print(e)


            # db.commit()
            # # 关闭数据库
            # db.close()
            # f.close()
        print("ok")
    def listFiles(self):
        d = os.listdir(r'E:\words.txt', 'r')
        return d

    def test(self):
        list1 = []
        f = open(r'E:\words.txt', 'r')
        for line in f:
            print(line)


if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()