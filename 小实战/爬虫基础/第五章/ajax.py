#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import lxml.html
from downloader import Downloader

D = Downloader()
html = D('http://example.webscraping.com/places/default/search')
tree = lxml.html.fromstring(html)
print(tree.cssselect('div#result a'))  # 结果为[]

# 下面的网址就是AJAX请求，在检查页面中是可以找到的
html = D('http://example.webscraping.com/places/ajax/search.json?&search_term=A&page_size=10&page=0')
print(json.loads(html))

url = 'http://example.webscraping.com/places/ajax/search.json?page_size=10&page=0&search_term='
print(json.loads(D(url))['num_pages'])
print(json.loads(D(url + '*'))['num_pages'])
print(json.loads(D(url + '.'))['num_pages'])

url = 'http://example.webscraping.com/places/ajax/search.json?page_size=20&page=0&search_term=.'
print(json.loads(D(url))['num_pages'])

url = 'http://example.webscraping.com/places/ajax/search.json?page_size=1000&page=0&search_term=.'
print(json.loads(D(url))['num_pages'])