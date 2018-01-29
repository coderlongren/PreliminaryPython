#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request as ur
import requests
# import html2text

domain = 'http://www.liaoxuefeng.com'   #廖雪峰网站的域名
path = 'D:/pythonWorkingspace/Spider_liaoxuefeng' #保存路径


# 在主页上获取所有链接
# f = ur.urlopen("https://www.liaoxuefeng.com/wiki//001431927781401bb47ccf187b24c3b955157bb12c5882d000")#
kv = {'user-agent':'Mozilla/5.0'}
url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000l"
f = requests.get(url,headers=kv)
# f = ur.urlopen("https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000l")

print(f.text[:])

f.close()
