#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql


class ReadFile:
    def readLines(self):
        f = open(r'E:\newGRE.txt', 'r')
        # print(f.read())
        i=0
        list=[]
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
         # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        for line in f:
            try:
                # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
                strs = line.split(" ")
                if len(strs) != 2:
                    continue
                data=(strs[0] ,strs[1])
                list.append(data)
                sql =  "INSERT INTO GRE(english,chinese) VALUES ('%s', '%s')" % (list[0][0],list[0][1])
                print(sql)
                i=i+1
                print("第%d行"%(i))
                cursor.execute(sql)

            except IOError as e:
                # Rollback in case there is any error
                 print("异常 回滚", e)
                 db.rollback()
            db.commit()
            list.clear()
            print("ok")
        # if i>0:
        #     cursor.executemany(sql,list)
        #     cnx.commit()
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