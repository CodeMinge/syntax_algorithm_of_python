#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
import urllib
from urllib import request
from urllib import parse
import lxml.html
import http.cookiejar

LOGIN_EMAIL = '825479572@qq.com'
LOGIN_PASSWORD = 'zxc1234'
LOGIN_URL = 'http://example.webscraping.com/places/default/user/login'

def login_basic():
    data = {'email':LOGIN_EMAIL, 'password':LOGIN_PASSWORD}
    encoded_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    request = urllib.request.Request(LOGIN_URL, encoded_data)
    response = urllib.request.urlopen(request)
    print(response.geturl())           # 输出还是登陆页的url，说明登陆失败
	
def login_formkey():
    html = urllib.request.urlopen(LOGIN_URL).read()
    data = parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    request = urllib.request.Request(LOGIN_URL, encoded_data)
    response = urllib.request.urlopen(request)
    print(response.geturl())

def login_cookies():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    html = opener.open(LOGIN_URL).read()
    data = parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    request = urllib.request.Request(LOGIN_URL, encoded_data)
    response = opener.open(request)
    print(response.geturl())
    return opener	
	
def parse_form(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data	

def main():
    login_cookies()

if __name__ == '__main__':
    main()