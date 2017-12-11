#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import io
from io import StringIO

f = StringIO()
f.write("hello")
f.write("long")
print(f.getvalue())

f_bit = io.BytesIO()
f_bit.write('中文'.encode('utf-8'))
print(f_bit.getvalue())