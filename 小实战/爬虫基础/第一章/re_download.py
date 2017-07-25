#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import urllib
from urllib import request

def download(url, num_retries= 2): # num_retries是重新下载次数
	print('Downloading', url)
	try:
		html = urllib.request.urlopen(url).read()
	except urllib.request.URLError as e:
		print('Download error:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# recursively retry 5xx HTTP errors
				return download(url , num_retries - 1)
	return html
	
print(download('http://httpstat.us/500'))