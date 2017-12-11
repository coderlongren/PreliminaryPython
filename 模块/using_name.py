#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def fac(n):
    if n == 1:
        return n
    return n*fac(n - 1)
if __name__ == '__main__':
    print("程序自身在运行")
    n = int(input("please input n"))
    print(fac(n))
else:
    print("来自另一个模块")