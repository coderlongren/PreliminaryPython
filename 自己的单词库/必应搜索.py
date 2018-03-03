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

# 获得单词的音标，
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
            # ddd=reobj1.findall(it[1].xpath('a')[0].get('onmouseover',None))
            yingbiao.append("%s"%(it[0].text))
            # print("it[0]text",it[0].text)
            # ddd=reobj1.findall(it[3].xpath('a')[0].get('onmouseover',None))
            yingbiao.append("%s"%(it[2].text))
     if len(yingbiao)>0: #数据整形成一个字符串，用死个 || 分割
        return reduce(lambda x, y:"%s||||%s"%(x,y),yingbiao)
     else:
        return ""

# 获得单词的意思 有 BUG
def get_shiyi(htmlselector):
    Chitiao = []
    hanyi_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/ul//li'
    get_shiyi = htmlselector.xpath(hanyi_xpath)
    # print("y有几个意思",len(get_shiyi))
    # print("shiyi 长度",len(get_shiyi))
    for item in get_shiyi:
        it = item.xpath('span')
        if it[0].text == "网络":
            continue
        Chitiao.append('%s%s'%(it[0].text,it[1].xpath('span')[0].text))
    if len(Chitiao) > 0:
        return reduce(lambda x,y:"%s||%s"%(x,y),Chitiao)
    else:
        return ""

# 获得单词的例句
def get_liju(selector):
    liju = []

# 主方法
def get_word(word):
    # 获得页面
    pagehtml =get_page(word)
    selector = etree.HTML(pagehtml.decode('utf-8'))
    # 单词释义
    chitiao = get_shiyi(selector)
    # 生成音标和读音
    yinbiao = get_yingbiao(selector)
    # print(yinbiao)
    shiyi = get_shiyi(selector)
    # print(shiyi)
    # 获得例句
    # liju = get_liju(selector)
    # return "%s\t%s"
    return "%s:%s;%s"%(word,yinbiao,shiyi)
def isWord(word):
    flag = True
    for c in word:
        if (c <= 'Z' and c >= 'A') or (c <='z' and c >= 'a'):
            flag = True
        else:
            return False

    return flag

# 获得单词读音
def getMP3(html_selector):
     yingbiao=[]
     yingbiao_xpath='/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div'
     #xpath#
     bbb="(https\:.*?mp3)" ##这个是为了获得对应的读音MP3文件，使用正则表达式
     reobj1=re.compile(bbb,re.I|re.M|re.S)
     get_yingbiao=html_selector.xpath(yingbiao_xpath)
     item  = get_yingbiao[0]
     it=item.xpath('div')
     # 获得 读音MP3URL
     MP3url=reobj1.findall(it[1].xpath('a')[0].get('onmouseover',None))
     print(MP3url)
if __name__ == "__main__":
    fr = open(r'E:\单词大作战后台单词库\NEWtoeflr.json' , 'r',encoding='UTF-8')
    fw = open(r'E:\单词大作战后台单词库\必应爬取的数据\junior.json' , 'w',encoding='UTF-8')

    i = 1
    list = []
    for line in fr:
        print(i)
        if i > 0:
            word = line[:-1].strip()
            if isWord(word):
                line = get_word(word)
                print(line)
                list.append(line)
            # time.sleep(1)
        i = i + 1

    for line in list:
        fw.write(line + "\n")





