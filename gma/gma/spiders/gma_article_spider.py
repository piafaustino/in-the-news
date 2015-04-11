import scrapy
from scrapy import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import re

from gma.items import GmaItem

#filename for url list text file
URL_LIST = 'traffic_urls'

#filename for location keywords text file
LOCATION_KEYWORDS = 'location_keywords'

def location_from_article(s):
    with open(LOCATION_KEYWORDS, 'r') as file:
        location_keywords = file.read().splitlines()

    location_keywords = [x.strip().lower() for x in location_keywords]
    location_keywords = set(location_keywords)
    location_keywords.remove('')
    location_keywords = [x + ' ' for x in location_keywords]

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

    return urls_list[:10]

class ArticleLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip, ascii_or_remove)
    default_output_processor = Join()

    location_in = MapCompose(unicode.strip, ascii_or_remove, location_from_article)
    location_out = Join(', ')

class GmaSpider(scrapy.Spider):
    name = 'gma_article_spider'
    allowed_domains = ['gmanetwork.com']
    start_urls = open_url_file()

    item_fields = {
                   'title':'//title/text()',
                   'link':'//link[@rel="canonical"]/@href',
                   'author':'//strong/a/text()',
                   'date':'//span[@class="timestamp"]/text()',      
                   'article':'//div[@class="text_body"]/div/text()',
    }

    backup_item_fields = {
                            'article':'//div[@class="text_body"]/text()',
                            'title':'//title/text()',
                            'link':'//link[@rel="canonical"]/@href',
                            'author':'//span[@class="byline"]/a[@rel="author"]/text()',
                            'date':'//span[@class="timestamp"]/text()',      
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

        article_data = loader.get_output_value('article')
        loader.add_value('location', article_data)

        yield loader.load_item()
