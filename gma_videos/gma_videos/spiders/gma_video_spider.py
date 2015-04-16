import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import re

from gma_videos.items import GmaVideosItem

#filename for url list text file
URL_LIST = './keywords_and_urls/traffic_urls'

#filename for location keywords text file
LOCATION_KEYWORDS = './keywords_and_urls/location_keywords'

def location_from_articles(s):
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

	# to remove false matches of Quezon Province to the article
	if 'quezon' in loc_tag:
		quezon_count = len(re.findall(r'quezon', s.lower()))
		quezon_city_count = len(re.findall(r'quezon_city', s.lower()))

		if quezon_city_count == quezon_count:
			loc_tag.remove('quezon')

	return loc_tag

def ascii_or_remove(s):
	return s.encode('ascii', errors='ignore')

def open_url_file():
	with open(URL_LIST, 'r') as file:
		urls_list = file.read().splitlines

	return urls_list

class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()

	location_in = MapCompose(unicode.strip, ascii_or_remove, location_from_articles)
	location_out = Join(', ')

class GmaVideoSpider(scrapy.Spider):
	name = 'gma_video_spider'
	allowed_domains = ['gmanetwork.com']

	start_urls = open_url_file()

	def parse(self, response):
		"""
		Default callback Scrapy uses to process download
		"""
		sel = Selector(response)
		loader = ArticleLoader(item=GmaVideosItem(),selector=sel)

		yield loader.loader_item()
