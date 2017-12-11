#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "r+",encoding='UTF-8')
print ("文件名为: ", fo.name)

for line in fo.readlines():
    line.strip()
    print(line)
fo.close()