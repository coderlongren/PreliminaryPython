#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 打开文件
fo = open("test.txt", "r+",encoding="UTF-8")
print ("文件名: ", fo.name)

str = "第六行 "
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write('\n%s'%(str))

# 读取文件所有内容
fo.seek(0,0)
for index in range(6):
    line = next(fo)
    print ("文件行号 %d - %s" % (index + 1, line))

# 关闭文件
fo.close()