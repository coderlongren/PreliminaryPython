#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def readLines(self):
        f = codecs .open(r'E:\替换英文的level6.txt' , 'w' , 'utf-8' )
        # print(f.read())
        i=0
        list=[]
        dict = {}
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # Sql 查询
        sqltoefl = "select * from toefl"
        sqlLevel4 = "select * from level4"
        sqllevel6 = "select * from level6"
        try:
            cursor.execute(sqllevel6)
            result = cursor.fetchall()
            for line in result:
                str = line[1] + " " + line[2] + "\n"
            # for line in list:
                # sql =  "INSERT INTO level4(english,chinese) VALUES ('%s', '%s')" % (list[0][0], list[0][1])
                f.write(str)
                # print(sql)
                # 执行
                # cursor.execute(sql)
                # db.commit()
                # list = list + "[" + '"' + str1 + "," + '"' + "]" +  ","
                # f.wirite()

        except IOError as e:
            print(e)


        # 关闭数据库
        db.close()
        f.close()
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