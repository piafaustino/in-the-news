# -*- coding: utf-8 -*-

# Scrapy settings for abs_articles project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'abs_articles'

SPIDER_MODULES = ['abs_articles.spiders']
NEWSPIDER_MODULE = 'abs_articles.spiders'

RETRY_TIMES = 10
HTTP_RETRY_CODES = [500, 502, 503, 504, 400, 408, 524]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'abs_articles (+http://www.yourdomain.com)'
