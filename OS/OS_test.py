#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
print(os.name)
# print(os.uname()) windows 上不存在次函数

print(os.environ)
print(os.environ.get("PATH"))
print(os.environ.get("JAVA_HOME"))
