#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import string
from downloader import Downloader

D = Downloader()
template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'
countries = set()
ch =[]
for i in range(97,123):  # 所有小写
	ch.append(chr(i))
# print(ch)

for letter in ch:
	page = 0
	while True:
		html = D(template_url.format(letter, page))
		try:
			ajax = json.loads(html)
		except ValueError as e:
			print(e)
			ajax = None
		else:
			for record in ajax['records']:
				countries.add(record['country'])
		page += 1
		if ajax is None or page >= ajax['num_pages']:
			break

open('countries.txt', 'w').write('\n'.join(sorted(countries)))