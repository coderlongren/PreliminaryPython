#!/usr/bin/python3
# -*- coding: UTF-8 -*-
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
    def readLines(self):
        f = open(r'E:\middle.txt', 'r')
        # print(f.read())
        i=0
        list=[]
        # dict = {"abc":"abc"}
        for line in f:
            strs = line.split('\u3000')
            if len(strs) > 3 or len(strs) <= 1:
                continue

            data=(strs[0], strs[1][:])
            str1 = strs[0]
            str2 = strs[1][:-2]
            try:
                sql =  "INSERT INTO level6(english,chinese) VALUES ('%s', '%s')" % (str1, str2)
                print(sql)
                i=i+1
                print("第%d行"%(i))
                cursor.execute(sql)
                db.commit()
            except:
                # Rollback in case there is any error
                 db.rollback()
            # db.commit()
            list.clear()
        # if i>0:
        #     cursor.executemany(sql,list)
        #     cnx.commit()
        f.close()
        db.close()
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