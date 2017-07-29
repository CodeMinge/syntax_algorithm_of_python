#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from user_agent_download import download

def soupTest1():
	broken_html = '<ul class=country><li>Area<li>Population</ul>'
	soup = BeautifulSoup(broken_html, 'html.parser')
	fixed_html = soup.prettify()
	print(fixed_html)
	print('==soupTest Over==')
	
	ul = soup.find('ul', attrs={'class':'country'})
	print(ul.find('li'))
	print(ul.find_all('li'))

def soupTest2():
	html = download('http://example.webscraping.com/places/default/view/United-Kingdom-239')
	soup = BeautifulSoup(html, 'html.parser')
	tr = soup.find(attrs={'id':'places_area__row'})
	td = tr.find(attrs={'class':'w2p_fw'})
	print(td)
	area = td.text
	print(area)

if __name__ == '__main__':
	soupTest1()
	soupTest2()