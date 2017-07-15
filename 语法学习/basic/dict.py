#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
	'M': 95,
	'B': 75,
	'T': 85
}

print('d[\'M\'] =', d['M'])
print('d[\'B\'] =', d['B'])
print('d[\'T\'] =', d['T'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))