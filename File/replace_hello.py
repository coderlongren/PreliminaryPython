#!/usr/bin/python3
# -*- coding: UTF-8 -*-
str = ['hello\n'*10]
with open('123.txt','a') as f:
    for line in str:
        f.write(line)

print(str)
with open('123.txt','r') as f:
    with open('123-1.txt','w+') as s:
        for i in f.readlines():
            s.write(i.replace('hello','hi'))