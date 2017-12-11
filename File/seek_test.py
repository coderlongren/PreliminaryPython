#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 打开文件
fo = open("test.txt", "r+",encoding='UTF-8')
print ("文件名为: ", fo.name)

for line in fo.readlines():
    print('当前指针在',fo.tell(),line)

fo.seek(0,0)
line = fo.readline()
print('当前指针在',fo.tell(),line)
line = fo.readline()
print('当前指针在',fo.tell(),line)
fo.seek(0,1)
line = fo.readline()
print('当前指针在',fo.tell(),line)
line = fo.readline()
print('当前指针在',fo.tell(),line)
line = fo.readline()
print('当前指针在',fo.tell(),line)