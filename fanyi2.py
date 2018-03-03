#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http
import hashlib
import urllib.request
import random
import json

while True:
    fin = open(r'E:\1.txt', 'r',encoding='UTF-8')               #以读的方式打开输入文件
    fout = open(r'D:\2.txt', 'w',encoding='UTF-8')             #以写的方式打开输出文件
    for eachLine in fin:
        appid = '20180227000128617'    #参考百度翻译后台，申请appid和secretKey
        secretKey = 'YUe_r7sK766rUpXcNPXU'
        httpClient = None
        myurl = '/api/trans/vip/translate'
        q = eachLine.strip()                   #文本文件中每一行作为一个翻译源
        fromLang = 'zh'                         #中文
        toLang = 'en'                             #英文
        salt = random.randint(32768, 65536)
        sign = appid+q+str(salt)+secretKey
        sign = sign.encode('UTF-8')
        m1 = hashlib.md5()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        html= response.read().decode('UTF-8')
        target2 = json.loads(html)
        src = target2["trans_result"][0]["dst"]
        #print(src)#取得翻译后的文本结果,测试可删除注释
        outStr = src
        fout.write(outStr.strip() + '\n')
    fin.close()
    fout.close()
    print('翻译成功，请查看文件')
    break