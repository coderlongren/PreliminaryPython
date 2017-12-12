#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import  requests
url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding= r.apparent_encoding
    print(r.text[:])
except:
    print('失败')