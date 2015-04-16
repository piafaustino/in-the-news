import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import re

from abs_articles.items import ABSArticleItem

#filename for url list text file
URL_LIST = './keywords_and_urls/traffic_urls'

#filename for location keywords text file
LOCATION_KEYWORDS = './keywords_and_urls/location_keywords'

def location_from_article(s):
	with open(LOCATION_KEYWORDS, 'r') as file:
		location_keywords = file.read().splitlines()

	if '' in location_keywords:
		location_keywords.remove('')

	location_keywords = set([x.strip().lower() for x in location_keywords])
	location_keywords = [' ' + x + punct for x in location_keywords for punct in ('',' ',',','.',':',';')]

	loc_tag = []

	for location in location_keywords:
		if location in s.lower():
			location = location.strip()
			loc_tag.append(location)

	# to remove false matches of the Quezon Province in the article
	if 'quezon' in loc_tag:
		quezon_count = len(re.findall(r'quezon', s.lower()))
		quezon_city_count = len(re.findall(r'quezon city', s.lower()))

		if quezon_city_count == quezon_count:
			loc_tag.remove('quezon')

	return loc_tag

def ascii_or_remove(s):
	return s.encode('ascii',errors='ignore')

def open_url_file():
	with open(URL_LIST, 'r') as file:
		urls_list = file.read().splitlines()

	return urls_list

class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()

	location_in = MapCompose(unicode.strip, ascii_or_remove, location_from_article)
	location_out = Join(', ')

class ABSArticleSpider(scrapy.Spider):
	name = 'abs_article_spider'
	allowed_domains = ['abs-cbnnews.com']
	start_urls = open_url_file()

	item_fields = {
					'title':'//div[@class="text-article"]/h1/span/text()',
					'byline':'//div[@class="byline"]/text()',
					'date':'//div[@class="posted"]/text()',
					'article':'//div[@class="body"]/p/text()',
					'author':'//div[@class="body"]/p[last()]/strong/text()',
	}

	backup_item_fields = {
					'title':'//h3/a/text()',
					'article':'//p/text()',
	}

	def parse(self, response):
		"""
		Default callback Scrapy uses to process downloaded response.
		"""
		sel = Selector(response)
		loader = ArticleLoader(item=ABSArticleItem(),selector=sel)

		for field, xpath in self.item_fields.iteritems():
			if not loader.get_xpath(xpath):
				xpath = self.backup_item_fields.get(field)
			loader.add_xpath(field, xpath)

		loader.add_value('link', unicode(response.url))
		article_data = loader.get_output_value('article')
		loader.add_value('location', article_data)

		yield loader.load_item()
