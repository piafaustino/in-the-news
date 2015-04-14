import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from pprint import pprint
from inquirer_articles import InquirerArticlesItem
import datetime

#start date of article list, exclusive for the site
START = 2014-01-01

#end date of article list, exclusive for the site
END = 2014-12-31

def ascii_or_remove(s):
	return s.encode('ascii', errors='ignore')

def isoformat_start_end(start,end):
	start = datetime.datetime.strptime(start, "%d-%m-%Y")
	end = datetime.datetime.strptime(end, "%d-%m-%Y")
	date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

	return date_generated = [date.strftime("%d-%m-%Y") for date in in date_generated]


class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()


class InquirerSpider(scrapy.Spider):
	name = 'inquirer_list_spider'
	allowed_domains = ['http://www.inquirer.net']

	start_urls = []

	dates = isoformate_start_end(START,END)
	for date in dates:
		url = 'http://www.inquirer.net/article-index?d=' + date
		start_urls.append(url)

	articles_list_xpath = '//li/a[@rel="bookmark"]'

	def parse(self, response):
		"""
		Default callback Scrapy uses to process download response.
		"""
		sel = Selector(response)
		for article in sel.xpath(self.articles_list_xpath):
			loader = ArticleLoader(item=InquirerArticlesItem, selector=article)

			loader.add_xpath('title','./text()')
			loader.add_xpath('link','./@href')

			yield loader.load_item()
