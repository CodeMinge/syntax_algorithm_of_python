#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def alexa():
    csv_filename = 'web.csv'
    urls = []
    for _, website in csv.reader(open(csv_filename)):
        urls.append(website)
    return urls
	
if __name__ == '__main__':
    print(alexa())
    print(len(alexa()))