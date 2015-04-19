# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GmaVideosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    show = scrapy.Field()
    reporter = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    teaser = scrapy.Field()

