#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在windows平台下不能用fork
# multiprocessing模块是跨平台版本的多进程模块

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 创建子进程传入执行函数和函数参数
    print('Child process will start.')
    p.start()
    p.join()  # 当前进程等待p执行完毕后再执行
    print('Child process end.')