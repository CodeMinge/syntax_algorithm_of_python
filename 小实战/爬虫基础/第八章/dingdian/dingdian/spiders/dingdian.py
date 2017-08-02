import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request

from dingdian.items import DingdianItem

'''
	yield Request请求新的URL，后面跟的是回调函数，你需要一个函数来处理这个返回值，
	就调用这个函数返回值会以参数的形式传递给你所调用的函数
'''

class DingdianSpider(scrapy.Spider):
	name = 'dingdian'
	allowed_domains = ['23us.so']
	bash_url = 'http://www.23us.so/list/'
	bashurl = '.html'
	
	def start_requests(self):
		for i in range(1, 10):
			url = self.bash_url + str(i) + '_1' + self.bashurl
			yield Request(url, self.parse)
			break
		
	def parse(self, response):
		max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
		# print(max_num)
		# print(str(response.url)[:-7])
		bashurl = str(response.url)[:-7]
		for num in range(1): # 试验的时候选取一页就行 for num in range(1, int(max_num) + 1)
			url = bashurl + '_' + str(num) + self.bashurl
			print(url)
			yield Request(url, callback=self.get_name)
			# break
			
	def get_name(self, response):
		tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
		for td in tds:
			print(td)
			novelname = td.find('a').get_text()
			novelurl = td.find('a')['href']
			yield Request(novelurl, callback=self.get_chapterurl, meta={'name': novelname, 'url': novelurl})
			break
			
	def get_chapterurl(self, response):
		item = DingdianItem()
		item['name'] = str(response.meta['name']).replace('\xa0', '')
		item['novelurl'] = response.meta['url']
		category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
		author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
		bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
		name_id = str(bash_url)[-6:-1].replace('/', '') # 小说编号的截取是有误的
		item['category'] = str(category).replace('/', '')
		item['author'] = str(author).replace('/', '')
		item['name_id'] = name_id
		print(item)
		yield item