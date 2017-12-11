#!/usr/bin/python3
# -*- coding: UTF-8 -*-
fo = open("test1.txt", "r+",encoding="UTF-8")
print ("文件名: ", fo.name)

line = fo.readline()
print ("读取行: %s" % (line))
print("当前指针%d"%(fo.tell()))

# fo.seek(0,0)
# print("当前指针%d"%(fo.tell()))

fo.truncate(10)
line = fo.readlines()
print ("读取行: %s" % (line))

# 关闭文件
fo.close()