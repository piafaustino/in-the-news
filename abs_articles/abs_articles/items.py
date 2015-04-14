# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ABSArticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    byline = scrapy.Field()
    description = scrapy.Field()

class ABSArticleItem(scrapy.Item):
	title = scrapy.Field()
	byline = scrapy.Field()
	date = scrapy.Field()
	article = scrapy.Field()
	author = scrapy.Field()
	link = scrapy.Field()
	location = scrapy.Field()
