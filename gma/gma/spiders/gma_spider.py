import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

from gma.items import GmaItem

def ascii_or_remove(s):
    return s.encode('ascii',errors='ignore')

class ArticleLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
    default_output_processor = Join()

class GmaSpider(scrapy.Spider):
    name = 'gma_spider'
    allowed_domains = ['gmanetwork.com']
    start_urls = [
        'http://www.gmanetwork.com/news/archives?from=10012014&to=03312015'
    ]

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
        
        
        #to get the last page of the archive.
        for i in response.xpath('//ul[@class="pagination"]/li/a/text()'):
            x = i.extract()
        x = int(x)

        for i in xrange(x):
            i = str(i)
            gma_page_url = 'http://www.gmanetwork.com/news/archives?'+'p='+ i +'&'+'from=10012014&to=03312015'
            
            yield  scrapy.Request(gma_page_url, callback=self.parse)
        
