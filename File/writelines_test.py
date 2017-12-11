#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 打开文件
with open('test2.txt','a',encoding="UTF-8") as fo:
    print ("文件名为: ", fo.name)
    seq = ["1\n", "第一行"]
    fo.writelines( seq )