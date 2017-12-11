#!/usr/bin/python3
# -*- coding: UTF-8 -*-
def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass
try:
    print("try.....")
    r = 10/1
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
finally:
    print("finally")

print("end")
