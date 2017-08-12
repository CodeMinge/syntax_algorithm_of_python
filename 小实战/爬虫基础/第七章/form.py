#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import sys

import base64
import pytesseract
import pprint
import http.cookiejar
import urllib
import lxml.html
from urllib import request
from urllib import parse
from io import BytesIO
from PIL import Image

REGISTER_URL = 'http://example.webscraping.com/places/default/user/register'

def extract_image(html):
    tree = lxml.html.fromstring(html)
    #print(tree)
    img_data = tree.cssselect('div#recaptcha img')[0].get('src')
    #print(img_data)
    # remove data:image/png;base64, header
    img_data = img_data.partition(',')[2]
    #print(img_data)
    # open('test_.png', 'wb').write(data.decode('base64'))
    # binary_img_data = img_data.decode('base64')
    binary_img_data = base64.b64decode(img_data)	
    file_like = BytesIO(binary_img_data)
    img = Image.open(file_like)
    img.save('test.png')
    return img

def register(first_name, last_name, email, password, captcha_fn):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    html = opener.open(REGISTER_URL).read()
    form = parse_form(html)
	#pprint.pprint(form)
    form['first_name'] = first_name
    form['last_name'] = last_name
    form['email'] = email
    form['password'] = form['password_two'] = password
    img = extract_image(html)
    captcha = captcha_fn(img)
    print(captcha)
    img.save('simples/' + captcha + '.png')
    ofile = open('C:/Users\door\Pictures\python\小实战\爬虫基础\第七章\simples\simples.csv','w')
    writer = csv.writer(ofile)
    writer.writerow([captcha + '.png,' + captcha])
    form['recaptcha_response_field'] = captcha
    encoded_data = urllib.parse.urlencode(form).encode(encoding='utf-8')
    request = urllib.request.Request(REGISTER_URL, encoded_data)
    response = opener.open(request)
    success = '/places/default/user/register' not in response.geturl()
    return success

def parse_form(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data	
	
if __name__ == '__main__':
    register()