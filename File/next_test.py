#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# open file
# 打开文件
fo = open("test.txt", "r",encoding='UTF-8')
print ("文件名为: ", fo.name)

for index in range(5):
    line = next(fo)
    print ("第 %d 行 - %s" % (index + 1, line))

# 关闭文件
fo.close()