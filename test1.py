#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def readLines(self):
        # print(f.read())
        i=0
        list=[]
        dict = {}
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        list = "[["
        # Sql 查询
        sqlLevel6 = "select * from level6"
        sqlLevel4 = "select * from level4"
        sqlmiddle = "select * from middle"
        sqlgre = "select * from gre"
        sqltoefl = "select * from toefl"
        sqlJunior = "select * from junior"
        f = open(r'E:\toefl\all1.json' , 'w',encoding='UTF-8')
        try:
            cursor.execute(sqltoefl)
            result = cursor.fetchall()
            i = 0
            j = 1
            for row in result:
                if i % 40 == 0 and i != 0:
                    j = j+1
                    list = list[:-1]
                    list = list + "]" + "," + "["
                    if j >= 70:
                        break
                    # f.close()
                    # list = "["
                i = i + 1
                print(i)
                temp = row[2]

                youfenhao = True
                for c in temp:
                    if c == ';':
                        youfenhao = False
                        break
                if youfenhao == True:
                    temp = temp + ";"

                list = list + "[" + '"' + row[1]  + '"'+ "," + '"' + temp + '"' + "]" + ","




            # cursor.execute(sqlLevel6)
            # result = cursor.fetchall()
            # for row in result:
            #     list = list + "[" + '"' + row[1]  + '"'+ "," + '"' + row[2] + '"' + "]" + ","
            #
            # cursor.execute(sqlmiddle)
            # result = cursor.fetchall()
            # for row in result:
            #     list = list + "[" + '"' + row[1]  + '"'+ "," + '"' + row[2] + '"' + "]" + ","
            #
            # cursor.execute(sqlgre)
            # result = cursor.fetchall()
            # for row in result:
            #     list = list + "[" + '"' + row[1]  + '"'+ "," + '"' + row[2] + '"' + "]" + ","
            #
            # cursor.execute(sqltoefl)
            # result = cursor.fetchall()
            # for row in result:
            #     list = list + "[" + '"' + row[1]  + '"'+ "," + '"' + row[2] + '"' + "]" + ","

            f.write(list)
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