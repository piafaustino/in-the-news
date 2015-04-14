# -*- coding: utf-8 -*-

# Scrapy settings for inquirer_articles project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'inquirer_articles'

SPIDER_MODULES = ['inquirer_articles.spiders']
NEWSPIDER_MODULE = 'inquirer_articles.spiders'

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 524, 522]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'inquirer_articles (+http://www.yourdomain.com)'