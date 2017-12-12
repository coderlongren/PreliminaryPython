#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request as ur
# import html2text

domain = 'http://www.liaoxuefeng.com'   #廖雪峰网站的域名
path = 'D:/pythonWorkingspace/Spider_liaoxuefeng' #保存路径


# 在主页上获取所有链接
f = ur.urlopen("https://www.liaoxuefeng.com/wiki//001431927781401bb47ccf187b24c3b955157bb12c5882d000")
print(f.read())

f.close()
