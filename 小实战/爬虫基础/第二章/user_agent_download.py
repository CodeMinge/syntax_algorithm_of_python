#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import urllib
from urllib import request

def download(url, user_agent='wswp', num_retries=2):
	print('Downloading', url)
	headers = {'User-agent': user_agent}
	req = urllib.request.Request(url, headers=headers) # 使用Request来包装请求
	try:
		html = urllib.request.urlopen(req).read()      # 使用urlopen来获取页面
	except urllib.request.URLError as e:
		print('Download error:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# recursively retry 5xx HTTP errors
				return download(url , num_retries - 1)
	return html
	
#print(download('http://www.baidu.com'))