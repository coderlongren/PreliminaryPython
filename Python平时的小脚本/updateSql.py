#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
import sys
from random import shuffle
import importlib

importlib.reload(sys)  #此种方式行不通，可将编码方式设为sys.setdefaultencoding("utf-8")
class ReadFile:
    def readLines(self):
        f = codecs .open(r'E:\toefl.txt' , 'r+' , 'utf-8' )
        # print(f.read())
        i=0
        res=[]
        dict = {}
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # Sql update
        sql = "select * from level6"
        for line in f:
            str1 = ""
            str2 = ""
            flag = False
            for c in line:
                if c != ' ' and flag == False:
                    str1 = str1 + c
                elif c == ' ' and flag == False:
                    flag = True
                else:
                    str2 = str2 + c
            data= str1  + " " + str2
            list.append(data)

        # try:
        #     # 执行
        #     cursor.execute(sql)
        #     # 获取所有记录
        #     results = cursor.fetchall()
        #     for row in results:
        #         list ="[" + '"' +  row[1] + '"' + "," + '"' + row[2][:-2] +'"'+ "]"
        #         res = res + list + ","
        #
        #     res = res + "]"
        #     f.write(res)
        #     # js  = json.dumps(dict,ensure_ascii=False,sort_keys=False, indent=4, separators=(',', ': '))
        #     # # shuffle(js)
        #     # f.write(js)
        # except IOError as e:
        #     print(e)


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