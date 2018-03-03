#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def readLines(self):
        f = codecs .open(r'E:\middle.txt' , 'w' , 'utf-8' )
        # print(f.read())
        i=0
        list=[]
        dict = {}
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # Sql 查询
        sqlLevel6 = "select * from level6"
        sqlLevel4 = "select * from level4"
        try:
            # 执行
            cursor.execute(sqlLevel6)
            # 获取所有记录
            results = cursor.fetchall()
            list = []
            for row in results:
                list.append(row)
            cursor.execute(sqlLevel4)
            # 获取所有记录
            results = cursor.fetchall()
            for row in results:
                list.append(row)
            shuffle(list)
            for row in list:
                english = row[1]
                chinese = row[2][:-2]
                dict[english] = chinese

            js  = json.dumps(dict,ensure_ascii=False,sort_keys=False, indent=4, separators=(',', ': '))
            # shuffle(js)
            f.write(js)
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