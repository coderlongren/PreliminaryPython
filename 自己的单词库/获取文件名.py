#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs
from random import shuffle

class ReadFile:
    def writename(self):
        f = open(r'E:\单词大作战后台单词库\必应爬取的数据\托福单词.json' , 'w',encoding='UTF-8')
        for root, dirs, files in os.walk(r'E:\单词大作战后台单词库\必应爬取的数据\toefl单词读音'):
                # print(root) #当前目录路径
                # print(dirs) #当前路径下所有子目录
                # print(files) #当前路径下所有非目录子文件
                for file in files:
                    # print(file[:-4])
                    f.write(file[:-4] + "\n")
                print("ok")
if __name__ == "__main__":
    readFile = ReadFile()
    readFile.writename()