import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

from gma.items import GmaItem

URL_LIST = 'traffic_urls'
LOCATION_KEYWORDS = 'location_keywords'

def location_from_article(s):
    with open(LOCATION_LIST, 'r') as f:
        location_keywords = f.read()

    location_keyword_list = location_keywords.split('\n')
    location_keyword_list = [x.strip().lower() for x in location_keyword_list]

    loc_tag = []

    for location in location_keyword_list:
        if location in s:
            loc_tag.append(location)

    return loc_tag

def ascii_or_remove(s):
    return s.encode('ascii',errors='ignore')

def open_url_file():
    with open(URL_LIST, 'r') as file:
        urls = file.read()

    urls_list = urls.split('\n')

    return urls_list

class ArticleLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
    default_output_processor = Join()

    location_in = MapCompose(location_from_article)

class GmaSpider(scrapy.Spider):
    name = 'gma_article_spider'
    allowed_domains = ['gmanetwork.com']
    start_urls = open_url_file()

    item_fields = {
                   'title':     '//title/text()',
                   'link':      '//link[@rel="canonical"]/@href',
                   'author':    '//strong/a/text()',
                   'date':      '//span[@class="timestamp"]/text()',      
                   'article':   '//div[@class="text_body"]/div/text()',
                   'location':  '//div[@class="text_body"]/div/text()'
    }

    backup_item_fields = {
                            'article':   '//div[@class="text_body"]/text()',
                            'title':     '//title/text()',
                            'link':      '//link[@rel="canonical"]/@href',
                            'author':    '//span[@class="byline"]/a[@rel="author"]/text()',
                            'date':      '//span[@class="timestamp"]/text()',
                            'location':  '//div[@class="text_body"]/text()',      
    }

    def parse(self, response):
        """
        Default callback Scrapy uses to process downloaded response.
        """
        sel = Selector(response)
        loader = ArticleLoader(item=GmaItem(), selector=sel)

        for field, xpath in self.item_fields.iteritems():
            if not loader.get_xpath(xpath):
                xpath = self.backup_item_fields[field]
                if field == 'link':
                    loader.add_value(field, response.url)

            loader.add_xpath(field, xpath)

        yield loader.load_item()
