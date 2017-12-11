#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import  os
import os.path
"""
获取指定目录及其子目录下的 py 文件路径说明：
l 用于存储找到的 py 文件路径 get_py 函数，递归查找并存储 py 文件路径于 l
"""
l = []
def get_py(path,l):
    fileList = os.listdir(path) # 获取path目录下的所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename) # 获取path 和 filename组合之后的路径
        if os.path.isdir(pathTmp): # 如果是路径
            get_py(pathTmp,l) # 递归查找
        elif filename[-3:].upper()=='.PY': # 不是目录就判断
            l.append(pathTmp)

path = input("请输入要查找的路径")
get_py(path,l)
print('在%s路径下找到了%d个py文件'%(path,len(l)))
for filename in l:
    print(filename + '\n')