#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_max_area(L=[]):
	max_area = 0
	i = 0
	j = len(L) - 1
	while i < j:
		if L[i] > L[j]:
			max_area = max(max_area, (L[j] * (j - i - 1)))
			j -= 1
		else:
			max_area = max(max_area, (L[i] * (j - i - 1)))
			i += 1
	return max_area
print(get_max_area([3, 4, 2, 5]))
print(get_max_area([10, 6, 7, 2, 3, 12, 8, 6]))