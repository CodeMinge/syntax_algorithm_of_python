#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
from downloader import Downloader

FIELDS = ('country', 'id', 'pretty_link')
D = Downloader()
writer = csv.writer(open('countries.csv', 'w'))
writer.writerow(FIELDS)
html = D('http://example.webscraping.com/places/ajax/search.json?page_size=1000&page=0&search_term=.')
ajax = json.loads(html)
for record in ajax['records']:
	row = [record[field] for field in FIELDS]
	writer.writerow(row)