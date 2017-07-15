#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move_msg(n, f, t):
	print(f, '--->', t)

def move(n, a, b, c):
	if n == 1:
		move_msg(n, a, c)
	else:
		move(n - 1, a, c, b)
		move_msg(n, a, c)
		move(n - 1, b, a, c)