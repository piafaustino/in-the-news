import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

from gma.items import GmaItem

#3463 count for all the pages for the year 2014
PAGE_COUNT = 3463

def ascii_or_remove(s):
    return s.encode('ascii',errors='ignore')

class ArticleLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
    default_output_processor = Join()

class GmaSpider(scrapy.Spider):
    name = 'gma_spider'
    allowed_domains = ['gmanetwork.com']

    gma_page_url = ['http://www.gmanetwork.com/news/archives?'+'p='+ str(i) +'&'+'from=01012014&to=12312014' for i in range(1,PAGE_COUNT+1)]

    start_urls = gma_page_url

    article_list_xpath = '//div[@class="items"]/li'

    #always put a . at the xpath
    item_fields = {
                   'title':     './h3/a/text()',
                   'link':      './h3/a/@href',
                   'author':    './div/span/text()',
                   'time':      './div/div/text()',
    }

    def parse(self, response):
        """
        Default callback Scrapy uses to process downloaded response.
        """

        #Selectors are like the BeautifulSoup and lxml of Scrapy. With the similar
        #function, selectors 'select' certain parts of the HTML document specified
        #by either XPATH or CSS expressions.
        sel = Selector(response)

        for article in sel.xpath(self.article_list_xpath):

            #Items provide the container of scraped data,
            #while Item Loaders provide the mechanism for populating that container.

            #Item Loaders are designed to provide a flexible, efficient and easy
            #mechanism for extending and overriding different field parsing rules,
            #either by spider, or by source format (HTML, XML, etc)
            #without becoming a nightmare to maintain.
            loader = ArticleLoader(item=GmaItem(), selector=article)

            #iterate over fields and add xpaths to the loader.
            #input processors always receive iterables. If the value is not an iterable,
            #then it will be converted before being passed to an input processor
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)

                collected_value = loader.get_collected_values(field)
            loader.add_xpath('date', '//div[@class="items"]/h2/text()')

            #data collected from 'add_xpath' is passed through the output processor
            #of the name field and is then assigned to the name field of the item.
            yield loader.load_item()

