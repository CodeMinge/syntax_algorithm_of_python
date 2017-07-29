#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from user_agent_download import download

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url)
html = html.decode('utf-8')

print(re.findall('<td class="w2p_fw">(.*?)</td>',html))

print(re.findall('<tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>',html))