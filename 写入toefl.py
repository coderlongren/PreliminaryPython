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
        try:
            # cursor.execute(sqllevel6)
            # result = cursor.fetchall()
            # i = 1
            # list = []
            for line in f:
                line = line[:-1]
                data = line.split(" ")
                english = data[0]
                chinese = ""
                count = 0
                len = 0
                for c in data[1]:
                    if c == ",":
                        count = count + 1
                        if len > 8 or count > 2:
                            c = ";"

                    chinese = chinese + c
                    len = len + 1
                flag = True
                sql =  "INSERT INTO toefl(english,chinese) VALUES ('%s', '%s')" % (english,chinese)
                print(sql)
                cursor.execute(sql)
        except IOError as e:
                print(e)
        db.commit()
        # 关闭数据库
        db.close()
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