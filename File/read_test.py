#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "r+",encoding='UTF-8')
print ("文件名为: ", fo.name)

line = fo.read(10)
print ("读取的字符串: %s" % (line))

# 关闭文件
fo.close()