#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import  os
print('Process (%s) start...'%(os.getpid()))
# only work on Unix/Linux
pid = os.fork()
if pid == 0:
    print('l am child process (%s) and my parent is %s' %(os.getpid(),os.getppid()))
else:
    print('l %s just create a chile process %s'%(os.getpid(),pid))


