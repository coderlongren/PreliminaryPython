#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib.request
import re
import time
import pymysql
import json
import codecs
from random import shuffle
from lxml import etree
import urllib.request
from functools import reduce

def readLines():
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
    sqljunior = "select * from junior"

    f = open(r'E:\junior\all.json' , 'w',encoding='UTF-8')
    try:
        cursor.execute(sqljunior)
        result = cursor.fetchall()
        i = 0
        j = 1
        for row in result:
            if i % 40 == 0 and i != 0:
                j = j+1
                list = list[:-1]
                list = list + "]" + "," + "["
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
def get_page(myword):
    baseurl = 'http://cn.bing.com/dict/search?q='
    searchurl = baseurl + myword
    response = urllib.request.urlopen(searchurl)
    html = response.read()
    return html

def get_yingbiao(html_selector):
     yingbiao=[]
     yingbiao_xpath='/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div'
     #xpath#
     bbb="(https\:.*?mp3)" ##这个是为了获得对应的读音MP3文件，使用正则表达式
     reobj1=re.compile(bbb,re.I|re.M|re.S)
     get_yingbiao=html_selector.xpath(yingbiao_xpath)
     for item in get_yingbiao:
         it=item.xpath('div')
         if len(it)>0: #处理没有读音或者音标的部分
            ddd=reobj1.findall(it[1].xpath('a')[0].get('onmouseover',None))
            yingbiao.append("%s||%s"%(it[0].text,ddd[0]))
            ddd=reobj1.findall(it[3].xpath('a')[0].get('onmouseover',None))
            yingbiao.append("%s||%s"%(it[2].text,ddd[0]))
     if len(yingbiao)>0: #数据整形成一个字符串，用死个 || 分割
        return reduce(lambda x, y:"%s||||%s"%(x,y),yingbiao)
     else:
        return ""

def get_shiyi(htmlselector):
    Chitiao = []
    hanyi_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/ul/li'
    get_shiyi = htmlselector.xpath(hanyi_xpath)
    for item in get_shiyi:
        it = item.xpath('span')
        Chitiao.append('%s;%s'%(it[0].text,it[1].xpath('span')[0].text))
        if len(Chitiao) > 0:
            return reduce(lambda x,y:"%s||%s"%(x,y),Chitiao)
        else:
            return ""
def get_liju(selector):
    liju = []

def get_word(word):
    # 获得页面
    pagehtml =get_page(word)
    selector = etree.HTML(pagehtml.decode('utf-8'))
    getMP3(selector,word)

def getMP3(html_selector,word):
     yingbiao=[]
     yingbiao_xpath='/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div'
     #xpath#
     bbb="(https\:.*?mp3)" ##这个是为了获得对应的读音MP3文件，使用正则表达式
     reobj1=re.compile(bbb,re.I|re.M|re.S)
     get_yingbiao=html_selector.xpath(yingbiao_xpath)
     if len(get_yingbiao) > 0:
         item  = get_yingbiao[0]
         it=item.xpath('div')
         if len(it) > 0:
             # 获得 读音MP3URL
             MP3url=reobj1.findall(it[1].xpath('a')[0].get('onmouseover',None))
             print(word +":" + MP3url[0])
             path = "E:\单词大作战后台单词库\必应爬取的数据\\toefl单词读音\%s.mp3"%(word[:-1])
             urllib.request.urlretrieve(MP3url[0],path)

def isWord(word):
    flag = True
    for c in word:
        if c <= 'Z' and c >= 'A' or c <='z' and c >= 'a':
            flag = True
        else:
            return False

    return flag

if __name__ == "__main__":
    fr = open(r'E:\单词大作战后台单词库\NEWtoefl.json' , 'r',encoding='UTF-8')
    fw = open(r'E:\单词大作战后台单词库\必应爬取的数据\junior.json' , 'w',encoding='UTF-8')
    love = 'love'
    # print(test)
    i = 1
    for line in fr:
        print(i)
        i = i + 1
        if i > 2664:
            time.sleep(0.2) # 爬慢一点
            get_word(line)






