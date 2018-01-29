#!/usr/bin/python3
# -*- coding: UTF-8 -*-
def calc(*numbers) :
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

calc(1,2,3)
# print(calc([1,2,3]))