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
        f = open(r'E:\单词大作战后台单词库\gre.json' , 'w',encoding='UTF-8')
        try:
            cursor.execute(sqlgre)
            result = cursor.fetchall()
            for line in result:
                f.write(line[1] + "\n")
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
            f.write(line + "\n")


if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()