import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

from abs_articles.items import ABSArticlesItem

def ascii_or_remove(s):
	return s.encode('ascii',errors='ignore')

class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()

class GmaSpider(scrapy.Spider):
	name = 'abs_list_spider'
	allowed_domains = ['abs-cbnnews.com']

	url_list = ['http://www.abs-cbnnews.com/list/Metro-Manila?page=' + str(x) for x in xrange(0,50)]
	url_list2 = ['http://www.abs-cbnnews.com/list/Region?page=' + str(x) for x in xrange(0,50)]

	start_urls = urls_list + urls_list2

	articles_list_xpath = '//div[@class="view-content"]/div/div[@class="node-list"]'
	item_fields = {
					'title':'./h3/a/text()',
					'link':'./h3/a/@href',
					'description':'./div[@class="short_description"]/text()',
					'byline':'./div[@class="byline"]/text()',
	}

	def parse(self, response):
		"""
		Default callback Scrapy uses to process download response.
		"""
		sel = Selector(response)
		for article in sel.xpath(self.articles_list_xpath):
			loader = ArticleLoader(item=ABSArticlesItem(), selector=article)
			for field, xpath in self.item_fields.iteritems():
				loader.add_xpath(field, xpath)

				collected_value = loader.get_collected_values(field)

			yield loader.load_item()
