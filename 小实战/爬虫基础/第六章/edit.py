#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mechanize
import pprint
import login
import urllib
from urllib import request
from urllib import parse

COUNTRY_URL = 'http://example.webscraping.com/places/default/edit/Afghanistan-1'

def edit_country():
    opener = login.login_cookies()
    country_html = opener.open(COUNTRY_URL).read()
    data = login.parse_form(country_html)
    pprint.pprint(data)
	
    data['population'] = int(data['population']) + 1
    encoded_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    request = urllib.request.Request(COUNTRY_URL, encoded_data)
    response = opener.open(request)

    country_html = opener.open(COUNTRY_URL).read()
    data = login.parse_form(country_html)
    print('Population after:', data['population'])
	
if __name__ == '__main__':
    edit_country()