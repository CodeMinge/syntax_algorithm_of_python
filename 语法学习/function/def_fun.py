#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	print(x1, x2)
	return x1, x2