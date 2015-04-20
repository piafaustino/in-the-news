import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from pprint import pprint
from abs_articles.items import ABSArticlesItem

#number of pages to be scraped. URL does not specify date.
#325 pages approximately covers 6 to 7 months of news for Metro Manila, 825 for around 15 months.
PAGE_COUNT_METRO = 825

#for Regional news, 6 to 7 months are equivalent to approximately 450 pages.
PAGE_COUNT_REGION = 900

def ascii_or_remove(s):
	return s.encode('ascii',errors='ignore')

class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()

class GmaSpider(scrapy.Spider):
	name = 'abs_list_spider'
	allowed_domains = ['abs-cbnnews.com']

#	url_list = ['http://www.abs-cbnnews.com/list/Metro-Manila?page=' + str(x) for x in xrange(0,PAGE_COUNT_METRO+1)]
	url_list2 = ['http://www.abs-cbnnews.com/list/Region?page=' + str(x) for x in xrange(450,PAGE_COUNT_REGION+1)]

#	start_urls = url_list + url_list2
	start_urls = url_list2

	articles_list_xpath = '//div[@class="view-content"]/div/div[@class="node-list"]'

	def parse(self, response):
		"""
		Default callback Scrapy uses to process download response.
		"""
		sel = Selector(response)
		for article in sel.xpath(self.articles_list_xpath):
			loader = ArticleLoader(item=ABSArticlesItem(), selector=article)

			loader.add_xpath('title', './h3/a/text()')
			loader.add_xpath('link','./h3/a/@href')
			loader.add_xpath('description','./div[@class="short_description"]/text()')
			loader.add_xpath('description','./div[@class="short_description"]/p/text()')
			loader.add_xpath('byline','./div[@class="byline"]/text()')

			yield loader.load_item()
