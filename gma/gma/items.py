# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

class GmaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    Container (dictionary-like object) for scraped data.
    """
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    article = scrapy.Field()