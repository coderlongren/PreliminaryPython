#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)'%(name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s is running,,,,,'%os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Chile process will start ')
    p.start()
    p.join() # 等待子进程结束后在执行
    print('Chile process end')

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')