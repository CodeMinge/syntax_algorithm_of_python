#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
#GET
import sys
from urllib import request
import json
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)
page = response.read()
page = page.decode('utf-8')

print(page)
'''

#'''
#POST
import sys
from urllib import request,parse
import json
from bs4 import BeautifulSoup

url = 'http://shuju.wdzj.com/plat-info-initialize.html'

data = {
	'wdzjPlatId':59
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

#print(page)
for key in json.loads(page).keys():
	print(key)
#'''