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
        f = codecs .open(r'E:\besttoefl2.txt' , 'r' , 'utf-8' )
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # Sql 查询
        sqltoefl = "select * from toefl"
        sqlLevel4 = "select * from level4"
        sqllevel6 = "select * from level6"
        # sql = "select * from toefl"
        try:
            cursor.execute(sqltoefl)
            result = cursor.fetchall()
            i = 1
            list = []
            for line in result:
                f.write(line[1] + " " + line[2] + "\n")

                # data = line.split(" ")
                # if len(data) != 2:
                #     continue
                # english = data[0]
                # chinese = ""
                # flag = True
                # for c in data[1]:
                #     if c == "(":
                #         flag = False
                #     if c == ")":
                #         flag = True
                #     if flag == True:
                #         chinese = chinese + c
                #
                # sql =  "INSERT INTO toefl(english,chinese) VALUES ('%s', '%s')" % (english,chinese)
                # print(sql)
                # cursor.execute(sql)
        except IOError as e:
                print(e)
        # db.commit()
        # 关闭数据库
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