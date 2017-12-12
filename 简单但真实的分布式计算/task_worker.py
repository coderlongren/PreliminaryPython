#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 非服务端
import random, time, queue
from multiprocessing import freeze_support  #server启动报错，提示需要引用此包
from multiprocessing.managers import BaseManager

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
# QueueManager 只从网络上获取Queue 所以注册时候提供名字即可
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器 也就是运行tesk_Queue.py的机器
server_addr = '127.0.0.1'
print('connect to server%s'%server_addr)
# 端口和验证码要保持一致
m = QueueManager(address=(server_addr,5000),authkey=b'abc')

# 从网络连接
m.connect()
# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列获取任务，并且把结果下乳result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d'%(n,n))
        r = '%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task Queue is empty')

# 处理结果
print('worker exit')
