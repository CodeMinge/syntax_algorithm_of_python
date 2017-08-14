#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from link_crawler import link_crawler
from mongo_cache import MongoCache
from alexa_cb import AlexaCallback


def main():
    starttime = datetime.datetime.now()
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    link_crawler('http://example.webscraping.com', scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)

if __name__ == '__main__':
    main()