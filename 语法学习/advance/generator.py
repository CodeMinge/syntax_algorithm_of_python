#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
def my_factorial(a):
    s=1
    while a>0:
        s=s*a
        a=a-1
    return s

def my_C(n, k):
    if k>n:
        return 0
    else:
        return int(my_factorial(n)/(my_factorial(k)*my_factorial(n-k)))

def my_triangles():
    t=[]
    while True:
        n , k = len(t), 0
        t=[]
        while k <= n:
            t.append(my_C(n, k))
            k+=1
        yield(t)

n=0
for t in my_triangles():
    print(t)
    n = n+1
    if n==10:
        break;