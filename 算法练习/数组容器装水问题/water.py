#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数组容器装水问题

# 时间：O(n^2)
def getWater1(arr=[]):
	water = 0
	
	for i in range(len(arr) - 2):
		if i == 0:
			continue
		else:
			lmax = 0
			rmax = 0
			j = i - 1
			while j >= 0:
				lmax = max(lmax, arr[j])
				j -= 1
			#print(lmax)
			
			k = i + 1
			while k < len(arr):
				rmax = max(rmax, arr[k])
				k += 1
			#print(rmax)
			
			if (min(lmax, rmax) - arr[i]) > 0:
				water += min(lmax, rmax) - arr[i]
				
	#print(water)
	return water

# 时间：O(n)  空间：O(n)
def getWater2(arr=[]):
	water = 0
	tmp = 0
	L = []
	R = []
	
	for i in arr:
		tmp = max(tmp, i)
		L.append(tmp)
	
	tmp = 0
	for i in arr[::-1]:
		tmp = max(tmp, i)
		R.append(tmp)
	R.reverse()
	
	# print(L)
	# print(R)
	
	for i in range(len(arr) - 1):
		water += min(L[i], R[i]) - arr[i]
		
	# print(water)
	
	return water
	
# 时间：O(n)  空间：O(1)
def getWater3(arr=[]):
	water = 0
	ldex = 1
	rdex = len(arr) - 2
	lmax = arr[0]
	rmax = arr[len(arr) - 1]
	
	while(ldex <= rdex):
		if lmax <= rmax:
			water += max(0, lmax - arr[ldex])
			lmax = max(lmax, arr[ldex])
			ldex += 1
		else:
			water += max(0, rmax - arr[rdex])
			rmax = max(rmax, arr[rdex])
			rdex -= 1
			
	# print(water)
	
	return water

L = [0,1,0,2,1,0,1,3,2,1,2,1]
getWater1(L)
getWater2(L)
getWater3(L)