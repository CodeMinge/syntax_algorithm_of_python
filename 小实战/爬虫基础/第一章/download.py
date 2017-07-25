#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import urllib
from urllib import request

def download(url):
	print('Downloading', url)
	try:
		html = urllib.request.urlopen(url).read()
	except urllib.request.URLError as e:
		print('Download error:', e.reason)
		html = None
	return html
	
print(download('http://www.meetup.com/'))