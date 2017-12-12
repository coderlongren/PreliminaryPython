#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from multiprocessing import Process,Queue
import  os,time,random

# 写数据进程执行的代码
def write(q):
    print('process to write %s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue....'%value)
# 读进程执行的代码
def read():
    print('')
if __name__ == '__main__':
    # 父进程创建Queue 并且传递给子进程
    q = Queue()
    pw = Process(target=write(q),args=(q,))
    pr = Process(target=read(q),args=(q,))

    # 启动子进程pw 写入
    pw.start()
    # 启动子进程pr 读取
    pr.start()

