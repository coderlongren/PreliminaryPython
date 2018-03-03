#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle
class ReadFile:
    def readLines(self):
        f = open(r'E:\newjunior.txt' , 'r',encoding='UTF-8')
        # print(f.read())
        # f1 = open(r'E:\newjunior.txt' , 'w',encoding='UTF-8')
        # i=0
        # list=[]
        # dict = {}
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        list = []
        # Sql 查询
        sqlLevel6 = "select * from level6"
        sqlLevel4 = "select * from level4"
        try:
            i = 1
            for line in f:
                data = line.split(" ")
                if len(data) != 2:
                    continue;
                str1 = data[0]
                str2 = data[1][:-1]
                print(str1 + " " + str2)
                list.append(str1 + " " + str2)
                # print(len(data))
                # list.append(data)
            shuffle(list)
            for line in list:
                data = line.split(" ")
                sql =  "INSERT INTO junior(english,chinese) VALUES ('%s', '%s')" % (data[0],data[1])
                print(sql)
                # 执行
                cursor.execute(sql)
                flag = True
                # for c in line:uyjuuu
                #     if c==' ':
                #         flag = False
                #         i = i + 1
                #         break

            db.commit()
            f.close()
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