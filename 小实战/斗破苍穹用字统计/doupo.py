#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

fr = open('斗破苍穹.txt', 'r')    # 读文件

characters = []                   # 记录出现得汉字
stats = {}                        # （汉字，出现次数）

for line in fr:                   # 一行一行地读
	line = line.strip()
	
	if len(line) == 0:
		continue
		
	for x in range(0, len(line)):
		if not line[x] in characters:
			characters.append(line[x])
		
		if stats.get(line[x], -1) == -1:
			stats[line[x]] = 0
		
		stats[line[x]] += 1

i = 0
for d,x in stats.items():
	print('key:'+d+',value:'+str(x))
	if i==20:
		i = 0
		break
	else:
		i += 1

stat = sorted(stats.items(), key=lambda d:d[1], reverse = True)

print('*************')

for d,x in stat:
	print('key:'+d+',value:'+str(x))
	if i==20:
		i = 0
		break
	else:
		i += 1

fw = open('结果.txt', 'w')
for d,x in stat:
	fw.write('key:'+d+'         value:'+str(x)+'\n')
	
fw.close()
	
fr.close()