#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 启动大量子进程

import os, time, random
from multiprocessing import Pool

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocess done...')
	p.close()
	p.join()
	print('All subprocess done...')
	
# Pool(4)表示可以同时跑4个进程
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行（很明显的停顿）