#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lxml.html
from user_agent_download import download

def lxmlTest():
	broken_html = '<ul class=country><li>Area<li>Population</ul>'
	tree = lxml.html.fromstring(broken_html)
	fixed_html = lxml.html.tostring(tree, pretty_print=True)
	print(fixed_html)
	print('==lxmlTest Over==')

def scrape(html):
	tree = lxml.html.fromstring(html)
	td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
	area = td.text_content()
	print(area)
	return area
	
if __name__ == '__main__':
	lxmlTest()
	html = download('http://example.webscraping.com/places/default/view/United-Kingdom-239')
	scrape(html)