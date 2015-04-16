import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from gma_videos.items import GmaVideosItem

#no. of pages for all the videos under 2014.
PAGE_COUNT = 4047

def ascii_or_remove(s):
	return s.encode('ascii', errors='ignore')

class ArticleLoader(ItemLoader):
	default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
	default_output_processor = Join()

class GmaVideoListSpider(scrapy.Spider):
	name = 'gma_videolist_spider'
	allowed_domains = ['gmanetwork.com']

	gma_page_url = ['http://www.gmanetwork.com/news/video?p=' + str(i) + '&to=12312014&from=01012014' for i in xrange(1,PAGE_COUNT+1)]

	start_urls = gma_page_url

	video_list_xpath = '//li[@class=""]'

	item_fields = {
					'title':'./a/div/h3/text()',
					'link':'./a[1]/@href',
					'show':'./a/div/div[2]/div/a/text()',
					'reporter':'./a/div/div[3]/div/a/text()',
					'date':'./a/div/div[@class="metadata"][last()]/div/text()'
	}

	def parse(self, response):
		"""
		Default callback Scrapy uses to process downloaded response.
		"""
		sel = Selector(response)
		for video in sel.xpath(self.video_list_xpath):
			loader = ArticleLoader(item=GmaVideosItem(), selector=video)

			for field, xpath in self.item_fields.iteritems():
				loader.add_xpath(field, xpath)

			yield loader.load_item()
