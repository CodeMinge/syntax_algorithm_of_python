#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from mongo_cache import MongoCache

class AlexaCallback:
    def __init__(self, max_urls=1000):
        self.max_urls = max_urls
        self.seed_url = 'web.csv'

    def __call__(self, url, html):
        urls = []
        cache = MongoCache()
        for _, website in csv.reader(open(self.seed_url)):
            if website not in cache:
                urls.append(website)
                if len(urls) == self.max_urls:
                    break
        return urls