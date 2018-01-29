#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time

start = time.clock()
# fib方法一
# fib = lambda n, x = 0, y = 1:x if not n else fib(n - 1, y, x + y)
# 方法二
# fib = lambda n:1 if n <= 2 else fib(n - 1) + fib(n - 2)
# 方法三  列出所有的fib数列
def fib(n):
    result = [0,1]
    for i in range(n - 2):
        result.append(result[-1] + result[-2])
    return result
print(fib(1))
#
# for i in range(2):
#     print(i)