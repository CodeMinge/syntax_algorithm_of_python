#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 优解：寻找最长子序列长度

def BinarySearch(array, key):  #二分查找
    length=len(array)  
    ans=-1  
    l=0  
    r=length-1  
    while(l<=r):  
        mid=(l+r)>>1  
        if(array[mid]<key):  
            ans=mid  
            l=mid+1  
        else: r=mid-1  
    return ans+1 

def getdp2(L=[]):
	dp = []
	
	for i in range(len(L)):
		if i == 0:
			dp.append(L[i])
		else:
			j = BinarySearch(dp, L[i])
			if j < len(dp):
				dp[j] = L[i]
			else:
				dp.append(L[i])
	
	print(dp)
	return len(dp)
	

def lis2(L=[]):
	max_len = getdp2(L)
	print(max_len)
	
lis2([2,1,6,4,5,2,7,4]) # 测试程序
lis2([1,2,6,3,5,4,10,7,9]) # 测试程序