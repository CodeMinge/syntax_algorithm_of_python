#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 俄国沙皇问题

from lis2 import lis2

def my_sort(items=[]): # 排序策略：一升一降
	items.sort(key=lambda x:int(x[1]),reverse=True)
	items.sort(key=lambda x:int(x[0]))
	return items

def czar(items=[]):
	items = my_sort(items);
	
	L = []
	for item in items:
		L.append(item[1])
	print(L)
	
	lis2(L)
	
czar([[1,2],[1,3],[2,3],[2,4],[3,2],[4,5],[4,9],[5,3]]) #测试程序
czar([[3,2380],[1,11900],[4,3250],[1,100],[4,599],[2,872],[3,5560],[1,2500]]) #测试程序