#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re # 正则表达式模块
from bs4 import BeautifulSoup
from user_agent_download import download

def crawl_sitemap(url):
	# download the sitemap file
	sitemap = download(url)
	# 将bytes转为string，使得findall能接收
	sitemap = sitemap.decode('utf-8')
	soup = BeautifulSoup(sitemap, "html.parser")

	i = 0
	res = soup.find_all('a')
	for r in res:
		print(url + r['href'])
		html = download(url + r['href'])
		if i == 3:   # 跑五个试试就行
			break
		i += 1
		
if __name__ == '__main__':
	crawl_sitemap('http://example.webscraping.com')