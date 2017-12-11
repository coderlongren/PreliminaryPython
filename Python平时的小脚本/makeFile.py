#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import io
filename = input("please input a filename of unexited:")
f = open(filename,'w',encoding='UTF-8')
f.write('写入了一行')
print("你好")

