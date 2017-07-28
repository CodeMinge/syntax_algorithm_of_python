#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
from user_agent_download import download

def iteration():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass

if __name__ == '__main__':
    iteration()