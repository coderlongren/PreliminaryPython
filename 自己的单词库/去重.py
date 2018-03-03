#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def readLines(self):
        db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
        cursor = db.cursor()
        f = open(r'E:\单词大作战后台单词库\toefl.json' , 'r',encoding='UTF-8')
        f1 =  open(r'E:\单词大作战后台单词库\NEWtoefl.json' , 'w',encoding='UTF-8')
        l = []
        count = 1
        for line in f:
            l.append(line[:-1])
            # print(line)
            count = count + 1
        print(count)
        l = list(set(l))

        count = 1
        for line in l:
            # print(count)
            f1.write(line + "\n")
            count = count + 1
        print(count)
        f.close()
        f1.close()
        print("ok")

if __name__ == "__main__":
    readFile = ReadFile()
    # readFile.readLines()
    # readFile.test();
    readFile.readLines()