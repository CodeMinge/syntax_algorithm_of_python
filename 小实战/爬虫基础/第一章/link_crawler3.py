#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib
import urllib.robotparser
import time
from datetime import datetime
import queue

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1):
	crawl_queue = queue.deque([seed_url])
	seen = {seed_url:0}
	num_urls = 0
	rp = get_robots(seed_url)
	print('get_robots:', rp)
	throttle = Throttle(delay)
	headers = headers or {}
	if user_agent:
		headers['User-agent'] = user_agent

	while crawl_queue:
		url = crawl_queue.pop()
		print(url)
		if rp.can_fetch(user_agent, url):
			throttle.wait(url)
			html = download(url, headers, proxy=proxy, num_retries=num_retries)
			html = html.decode('utf-8')
			links = []
			
			depth = seen[url]
			if depth != max_depth:
				if link_regex:
					links.extend(link for link in get_links(html) if re.match(link_regex, link))
				for link in links:
					link = normalize(seed_url, link)
					if link not in seen:
						seen[link] = depth + 1
						if same_domain(seed_url, link):
							crawl_queue.append(link)
			num_urls += 1
			if num_urls == max_urls:
				break
		else:
			print('Blocked by robots.txt:', url)
	print(seen)

class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}
        
    def wait(self, url):
        domain = urllib.parse.urlparse(url).netloc
        print(domain)
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()

def download(url, headers, proxy, num_retries, data=None):
	print('Downloading', url)
	req = urllib.request.Request(url, data, headers)
	opener = urllib.request.build_opener()
	if proxy:
		proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib.request.ProxyHandler(proxy_params))
	try:
		resp = opener.open(req)
		html = resp.read()
		code = resp.code
	except urllib.request.URLError as e:
		print('Download error:', e.reason)
		html = ''
		if hasattr(e, 'code'):
			code = e.code
			if num_retries > 0 and 500 <= code < 600:
				# retry 5XX HTTP errors
				return download(url, headers, proxy, num_retries-1, data)
		else:
			code = None
	return html

def normalize(seed_url, link):
    link, _ = urllib.parse.urldefrag(link) # remove hash to avoid duplicates
    return urllib.parse.urljoin(seed_url, link)


def same_domain(url1, url2):
    return urllib.parse.urlparse(url1).netloc == urllib.parse.urlparse(url2).netloc
			
def get_robots(url):
	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(urllib.parse.urljoin(url, '/robots.txt'))
	rp.read()
	return rp

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

if __name__ == '__main__':
	#link_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
	link_crawler('http://example.webscraping.com', '/places/default/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')