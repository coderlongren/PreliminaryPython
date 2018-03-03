#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql
import json
import codecs

f = codecs .open(r'E:\testJson1.json' , 'r' , 'utf-8' )
i=0
list=[]
dict = {}
#
dict = {}
# db = pymysql.connect(host ='localhost',port =3306, user= 'root',passwd='rensailong', db='wordwar',charset="utf8")
 # host='XX.XX.XX.XX', port=3306, user='root', passwd='root123', db='数据库名称', charset="utf8"
# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# Sql 查询
# sql = "select * from level4"


js = json.dumps(dict,ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))
f.write(js)

# 关闭数据库
db.close()
f.close()
print("ok")