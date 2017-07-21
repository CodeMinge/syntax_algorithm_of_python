#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个爬虫的流程其实是简单的，需要记住的是一些参数是怎么得来的

import sys
import urllib.request
import json
from bs4 import BeautifulSoup

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie&source=index'

response = urllib.request.urlopen(url)
result = response.read()
result = result.decode('utf-8')              # 返回的result并不是字典
# print(type(result) == type({}))

page = json.loads(result)                    # 转成字典
# print(type(page) == type({}))

tags = page['tags']
for item in tags:
	print(item)
	
# 根据标签，获取标签下的电影
movies = []
for tag in tags:
	
	limit = 0
	while 1:
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + urllib.parse.quote(tag) + '&page_limit=40&page_start=' + str(limit) # url中有中文，需要利用函数处理一下
		# print(url)
		response = urllib.request.urlopen(url)
		result = response.read()
		result = result.decode('utf-8')
		result = json.loads(result)
		result = result['subjects']
		if len(result) == 0:
			break
			
		for item in result:
			movies.append(item)
		limit += 40
		
		break
		### 上下两个break应该是不存在的，但是只是为了试验目的，节省时间
	break

# print(len(movies))
for x in range(0, len(movies)):
	item = movies[x]
	print(item)
	response = urllib.request.urlopen(url=item['url'])
	result = response.read()
	result = result.decode('utf-8')
	html = BeautifulSoup(result)
	title = html.select('h1')[0]    # 这个h1就是网页中h1标签，得到的也是它的内容
	title = title.select('span')[0]
	title = title.get_text()
	# print(title)
	# movies[x]['title'] = title
	
fw = open('movies.txt', 'w')

for item in movies:
	tmp = ''
	for key, value in item.items():
		tmp += str(value) + ','
	fw.write(tmp + '\n')
	
fw.close()