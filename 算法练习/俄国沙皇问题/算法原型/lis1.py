#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一般解：寻找最长子序列长度（扩展：同时找到最长子序列）

def getdp1(L=[]):
	dp = []
	max_len = 1
	
	for i in range(len(L)):
		if i == 0:
			dp.append(max_len)
		else:
			j = i -1
			while j >= 0:
				if((L[i] > L[j]) and (max_len < (dp[j] + 1))):
					max_len = dp[j] + 1
				j = j - 1
			dp.append(max_len)	
		max_len = 1
	return dp
	

def lis1(L=[]):
	dp = getdp1(L)
	print(dp)
	
	max_len = 1
	for i in range(len(dp)):
		if dp[i] > max_len:
			max_len = dp[i]
	print(max_len)
	
lis1([2,1,6,4,5,2,7,4]) # 测试程序
lis1([1,2,6,3,5,4,10,7,9]) # 测试程序