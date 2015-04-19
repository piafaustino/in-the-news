# -*- coding: utf-8 -*-

# Scrapy settings for gma_videos project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gma_videos'

SPIDER_MODULES = ['gma_videos.spiders']
NEWSPIDER_MODULE = 'gma_videos.spiders'

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 524, 522]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gma_videos (+http://www.yourdomain.com)'
